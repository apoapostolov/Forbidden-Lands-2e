// @vitest-environment node

import type {
  BookData,
  BookPage,
  ParagraphSegment,
  Segment,
  TableSegment,
} from '@app-types/book'
import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'

const bookData = JSON.parse(
  readFileSync(new URL('../public/book-data.json', import.meta.url), 'utf8'),
) as BookData

const COLUMN_BUDGET_PT = 528 - 30
const SECTION_HEADING_RESERVE_PT = 145
const SECTION_FICTION_MIN_RESERVE_PT = 48
const LINE_HEIGHT_PT = 11.95
const PARA_MARGIN_PT = 4.1
const MIN_USABLE_COLUMN_AFTER_SPAN_PT = 150

function segmentGuardPt(segment: Segment): number {
  if (segment.type === 'paragraph') return segment.isListSegment ? 2 : 1.5
  if (segment.type === 'heading') return 1
  if (segment.type === 'table') return 4
  if (segment.type === 'image-ref') return 6
  return 4
}

function pageBodyLayout(page: BookPage): { bodyStart: number; columnBudgetPt: number } {
  let bodyStart = 0
  let spanReservePt = 0

  while (bodyStart < page.segments.length) {
    const segment = page.segments[bodyStart]

    if (segment.type === 'heading' && segment.level === 2) {
      spanReservePt += SECTION_HEADING_RESERVE_PT
      bodyStart++
      const fiction = page.segments[bodyStart]
      if (fiction?.type === 'blockquote') {
        spanReservePt += Math.max(SECTION_FICTION_MIN_RESERVE_PT, fiction.heightPt)
        bodyStart++
      }
      continue
    }

    // Chapter titles and marked fiction are rendered above the columns. Their
    // bespoke layouts predate the general flow model, so exclude them from the
    // ordinary column accounting without imposing a second synthetic reserve.
    if (
      (segment.type === 'heading' && segment.level === 1) ||
      (segment.type === 'paragraph' && segment.isFiction)
    ) {
      bodyStart++
      continue
    }

    if (
      (segment.type === 'heading' && segment.spanAll) ||
      (segment.type === 'table' && segment.spanAll) ||
      (segment.type === 'blockquote' && segment.spanAll)
    ) {
      spanReservePt +=
        segment.type === 'blockquote'
          ? segment.heightPt
          : segment.heightPt + segmentGuardPt(segment)
      bodyStart++
      continue
    }

    break
  }

  const measuredColumnBudgetPt = Math.max(
    0,
    COLUMN_BUDGET_PT -
      (page.chapterIndex === 0 && page.pageNumber === 1 ? 0 : spanReservePt),
  )
  return {
    bodyStart,
    columnBudgetPt:
      spanReservePt > 0 &&
      measuredColumnBudgetPt < MIN_USABLE_COLUMN_AFTER_SPAN_PT
        ? 0
        : measuredColumnBudgetPt,
  }
}

function isColumnBreak(segment: Segment | undefined): boolean {
  return segment?.type === 'hr' && segment.id === '__column_break__'
}

describe('generated book data', () => {
  it('contains every required chapter and at least one page', () => {
    expect(bookData.chapters).toHaveLength(14)
    expect(bookData.chapters.slice(-3).map((chapter) => chapter.chapterTitle)).toEqual([
      'Mercenaries of the Forbidden Lands',
      'Lifepaths of the Forbidden Lands',
      'Traderoads of the Forbidden Lands',
    ])
    expect(
      bookData.chapters.every(
        (chapter) => chapter.firstPage > 0 && chapter.lastPage >= chapter.firstPage,
      ),
    ).toBe(true)
    expect(bookData.toc.slice(-3).map((entry) => entry.title)).toEqual([
      'Mercenaries of the Forbidden Lands',
      'Lifepaths of the Forbidden Lands',
      'Traderoads of the Forbidden Lands',
    ])
    expect(bookData.pages.length).toBeGreaterThan(0)
    expect(bookData.totalPages).toBe(bookData.pages.length)
  })

  it('assigns a unique stable identifier to every segment', () => {
    const uids = bookData.pages.flatMap((page) =>
      page.segments.map((segment) => segment.uid),
    )
    expect(uids.every(Boolean)).toBe(true)
    expect(new Set(uids).size).toBe(uids.length)
  })

  it('emits explicit right-column markers', () => {
    expect(
      bookData.pages.some((page) =>
        page.segments.some((segment) => segment.id === '__column_break__'),
      ),
    ).toBe(true)
  })

  it('starts the second credits column with the artwork credits', () => {
    const creditsPage = bookData.pages[0]
    const columnBreakIndex = creditsPage.segments.findIndex(
      (segment) => segment.id === '__column_break__',
    )
    const secondColumnStart = creditsPage.segments[columnBreakIndex + 1]

    expect(columnBreakIndex).toBeGreaterThan(0)
    expect(secondColumnStart).toMatchObject({
      type: 'heading',
      level: 3,
      text: 'ILLUSTRATIONS & GRAPHICS',
    })
  })

  it('flows ordinary paragraphs across column and page boundaries', () => {
    const continuations = bookData.pages.flatMap((page) =>
      page.segments.filter(
        (segment): segment is ParagraphSegment =>
          segment.type === 'paragraph' && !!segment.continuesFromPrevious,
      ),
    )

    expect(continuations.length).toBeGreaterThan(0)
    expect(
      bookData.pages.some((page) =>
        page.segments.some(
          (segment) => segment.type === 'paragraph' && !!segment.continuesOnNext,
        ),
      ),
    ).toBe(true)
    expect(
      bookData.pages.some((page) =>
        page.segments.some((segment) => 'sourceNode' in segment),
      ),
    ).toBe(false)
  })

  it('keeps every paragraph endpoint inside the footer-safe column budget', () => {
    for (const page of bookData.pages) {
      const { bodyStart, columnBudgetPt: budget } = pageBodyLayout(page)
      let used = 0

      page.segments.forEach((segment, index) => {
        if (index < bodyStart) return
        if (isColumnBreak(segment)) {
          used = 0
          return
        }

        used += segment.heightPt + segmentGuardPt(segment)
        if (segment.type === 'paragraph') {
          expect(
            used,
            `page ${page.pageNumber} paragraph exceeded its column budget`,
          ).toBeLessThanOrEqual(budget + 0.01)
        }
      })
    }
  })

  it('keeps ordinary paragraph continuation fragments substantial', () => {
    const fragments = bookData.pages.flatMap((page) =>
      page.segments.filter(
        (segment): segment is ParagraphSegment =>
          segment.type === 'paragraph' &&
          !segment.isListSegment &&
          (!!segment.continuesFromPrevious || !!segment.continuesOnNext),
      ),
    )

    expect(fragments.length).toBeGreaterThan(0)
    expect(
      fragments.every(
        (fragment) =>
          fragment.html.replace(/<[^>]+>/gu, '').trim().length > 0 &&
          fragment.heightPt >= LINE_HEIGHT_PT * 2,
      ),
    ).toBe(true)
  })

  it('keeps every table fragment inside its remaining legal page area', () => {
    const violations: string[] = []

    for (const page of bookData.pages) {
      const { bodyStart, columnBudgetPt: budget } = pageBodyLayout(page)
      let used = 0

      page.segments.forEach((segment, index) => {
        if (index < bodyStart) return
        if (isColumnBreak(segment)) {
          used = 0
          return
        }

        used += segment.heightPt + segmentGuardPt(segment)
        if (segment.type === 'table' && used > budget + 0.01) {
          violations.push(
            `page ${page.pageNumber}: table ended at ${used.toFixed(1)}pt of ${budget.toFixed(1)}pt`,
          )
        }
      })

      const spanningTables = page.segments
        .slice(0, bodyStart)
        .filter(
          (segment): segment is TableSegment =>
            segment.type === 'table' && !!segment.spanAll,
        )
      for (const table of spanningTables) {
        expect(table.rows.length).toBeGreaterThan(0)
        expect(table.rowHeights).toHaveLength(table.rows.length)
      }
    }

    expect(violations).toEqual([])
  })

  it('emits complete adaptive table metadata and legal row continuations', () => {
    const tables = bookData.pages.flatMap((page) =>
      page.segments.filter(
        (segment): segment is TableSegment => segment.type === 'table',
      ),
    )
    const continuationRows = tables.flatMap((table) =>
      table.rows.map((row, index) => ({
        row,
        fromPrevious: table.rowContinuesFromPrevious?.[index] ?? false,
        onNext: table.rowContinuesOnNext?.[index] ?? false,
      })),
    )

    expect(tables.length).toBeGreaterThan(300)
    expect(tables.some((table) => table.spanAll)).toBe(true)
    expect(tables.some((table) => !table.spanAll)).toBe(true)
    expect(tables.some((table) => table.continuesOnNext)).toBe(true)

    for (const table of tables) {
      expect(table.layoutReason).toBeTruthy()
      expect(table.columnLineWidthsEm).toHaveLength(table.headers.length)
      expect(table.rowHeights).toHaveLength(table.rows.length)
      expect(table.rowContinuesFromPrevious).toHaveLength(table.rows.length)
      expect(table.rowContinuesOnNext).toHaveLength(table.rows.length)
      expect(table.rows.every((row) => row.length === table.headers.length)).toBe(
        true,
      )
    }

    expect(continuationRows.filter((row) => row.onNext).length).toBe(
      continuationRows.filter((row) => row.fromPrevious).length,
    )
  })

  it('never strands a heading before its paragraph or list continuation', () => {
    const violations: string[] = []

    bookData.pages.forEach((page, pageIndex) => {
      page.segments.forEach((segment, segmentIndex) => {
        if (segment.type !== 'heading' || segment.level === 2) return
        const next = page.segments[segmentIndex + 1]

        if (isColumnBreak(next)) {
          const nextColumnSegment = page.segments[segmentIndex + 2]
          if (nextColumnSegment?.type === 'paragraph') {
            violations.push(`page ${page.pageNumber}: ${segment.text}`)
          }
          return
        }

        if (!next) {
          const nextPageSegment = bookData.pages[pageIndex + 1]?.segments.find(
            (candidate) =>
              !isColumnBreak(candidate) &&
              !(candidate.type === 'heading' && candidate.level === 2),
          )
          if (nextPageSegment?.type === 'paragraph') {
            violations.push(`page ${page.pageNumber}: ${segment.text}`)
          }
          return
        }

        if (next.type !== 'paragraph' || !next.continuesOnNext) return
        if (next.isListSegment) {
          if ((next.itemLiHtmls?.length ?? 0) < 2) {
            violations.push(`page ${page.pageNumber}: ${segment.text}`)
          }
          return
        }

        const estimatedLines = Math.max(
          1,
          Math.ceil((next.heightPt - PARA_MARGIN_PT) / LINE_HEIGHT_PT),
        )
        if (estimatedLines < 2) {
          violations.push(`page ${page.pageNumber}: ${segment.text}`)
        }
      })
    })

    expect(violations).toEqual([])
  })
})
