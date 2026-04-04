import type { BookData, BookPage, Segment } from '@app-types/book'
import BookReader, { BookReaderHandle } from '@components/BookReader/BookReader'
import NavBar from '@components/NavBar/NavBar'
import SearchPanel from '@components/SearchPanel/SearchPanel'
import TableOfContents from '@components/TableOfContents/TableOfContents'
import bookDataRaw from '@data/book-data.json'
import { searchBook } from '@utils/search'
import { useCallback, useEffect, useMemo, useRef, useState } from 'react'

const COLUMN_HEIGHT_PT = 528
const RENDER_SAFETY_PT = 36
const EFFECTIVE_COLUMN_HEIGHT_PT = COLUMN_HEIGHT_PT - RENDER_SAFETY_PT
const MIN_AFTER_HEADING_PT = 14.6
const MIN_H4_AFTER_HEADING_PT = 19.6
const MIN_SOFT_FLOW_LINES = 2

type SegmentMetrics = {
  heightPt: number
  lineCount: number
  lineHeightPt: number
  softFlowEligible: boolean
}

type FitResult = {
  fitCount: number
  overflowAvailablePt: number
}

function decodeHtmlEntities(input: string): string {
  return input
    .replaceAll('&nbsp;', ' ')
    .replaceAll('&amp;', '&')
    .replaceAll('&lt;', '<')
    .replaceAll('&gt;', '>')
    .replaceAll('&quot;', '"')
    .replaceAll('&#39;', "'")
}

function stripHtml(input: string): string {
  return decodeHtmlEntities(input)
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
}

function estimateWrappedLineCount(text: string, charsPerLine: number): number {
  if (!text.trim()) return 1
  return Math.max(1, Math.ceil(text.length / charsPerLine))
}

function extractListItems(html: string): string[] {
  const matches = html.match(/<li[\s\S]*?<\/li>/gi)
  if (!matches) return []
  return matches.map((item) => stripHtml(item)).filter((item) => item.length > 0)
}

function extractListItemHtml(html: string): string[] {
  return html.match(/<li[\s\S]*?<\/li>/gi) ?? []
}

function escapeHtmlText(text: string): string {
  return text
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;')
}

function splitPlainTextByLines(
  text: string,
  headLines: number,
  totalLines: number,
): { headText: string; tailText: string } | null {
  const words = text.split(/\s+/).filter(Boolean)
  if (words.length < 8) return null

  let splitAt = Math.floor(words.length * (headLines / Math.max(totalLines, 1)))
  splitAt = Math.max(4, Math.min(splitAt, words.length - 4))

  const headText = words.slice(0, splitAt).join(' ').trim()
  const tailText = words.slice(splitAt).join(' ').trim()
  if (!headText || !tailText) return null

  return { headText, tailText }
}

function splitParagraphSegmentForPageBoundary(
  seg: Extract<Segment, { type: 'paragraph' }>,
  availablePt: number,
): {
  head: Extract<Segment, { type: 'paragraph' }>
  tail: Extract<Segment, { type: 'paragraph' }>
} | null {
  const metrics = paragraphMetrics(seg)
  const linesThatFit = Math.floor(availablePt / metrics.lineHeightPt)
  const maxHeadLines = metrics.lineCount - MIN_SOFT_FLOW_LINES
  const headLines = Math.min(linesThatFit, maxHeadLines)
  if (headLines < MIN_SOFT_FLOW_LINES) return null

  const tailLines = metrics.lineCount - headLines
  if (tailLines < MIN_SOFT_FLOW_LINES) return null

  const listItemHtml = extractListItemHtml(seg.html)
  if (listItemHtml.length > 0) {
    const wrapperTag = /<ol[\s>]/i.test(seg.html) ? 'ol' : 'ul'
    const lineCounts = listItemHtml.map((li) =>
      Math.max(1, estimateWrappedLineCount(stripHtml(li), 44)),
    )

    let usedLines = 0
    let splitIndex = 0

    while (
      splitIndex < lineCounts.length &&
      usedLines + lineCounts[splitIndex] <= headLines
    ) {
      usedLines += lineCounts[splitIndex]
      splitIndex += 1
    }

    // If no whole list item fits, try splitting the first item text.
    if (splitIndex === 0 && listItemHtml.length > 0) {
      const firstText = stripHtml(listItemHtml[0])
      const split = splitPlainTextByLines(firstText, headLines, lineCounts[0])
      if (!split) return null

      const headLi = `<li>${escapeHtmlText(split.headText)}</li>`
      const tailLi = `<li>${escapeHtmlText(split.tailText)}</li>`
      const headHtml = `<${wrapperTag}>\n${headLi}\n</${wrapperTag}>`
      const tailHtml = `<${wrapperTag}>\n${tailLi}\n${listItemHtml.slice(1).join('\n')}\n</${wrapperTag}>`

      return {
        head: {
          ...seg,
          html: headHtml,
          heightPt: headLines * metrics.lineHeightPt,
        },
        tail: {
          ...seg,
          html: tailHtml,
          heightPt: Math.max(MIN_SOFT_FLOW_LINES, tailLines) * metrics.lineHeightPt,
          isChapterOpener: false,
        },
      }
    }

    if (splitIndex <= 0 || splitIndex >= listItemHtml.length) return null

    const headPart = listItemHtml.slice(0, splitIndex)
    const tailPart = listItemHtml.slice(splitIndex)
    const headLineCount = lineCounts.slice(0, splitIndex).reduce((s, c) => s + c, 0)
    const tailLineCount = lineCounts.slice(splitIndex).reduce((s, c) => s + c, 0)
    if (headLineCount < MIN_SOFT_FLOW_LINES || tailLineCount < MIN_SOFT_FLOW_LINES)
      return null

    return {
      head: {
        ...seg,
        html: `<${wrapperTag}>\n${headPart.join('\n')}\n</${wrapperTag}>`,
        heightPt: headLineCount * metrics.lineHeightPt,
      },
      tail: {
        ...seg,
        html: `<${wrapperTag}>\n${tailPart.join('\n')}\n</${wrapperTag}>`,
        heightPt: tailLineCount * metrics.lineHeightPt,
        isChapterOpener: false,
      },
    }
  }

  const text = stripHtml(seg.html)
  const split = splitPlainTextByLines(text, headLines, metrics.lineCount)
  if (!split) return null

  return {
    head: {
      ...seg,
      html: `<p>${escapeHtmlText(split.headText)}</p>`,
      heightPt: headLines * metrics.lineHeightPt,
    },
    tail: {
      ...seg,
      html: `<p>${escapeHtmlText(split.tailText)}</p>`,
      heightPt: tailLines * metrics.lineHeightPt,
      isChapterOpener: false,
    },
  }
}

function paragraphMetrics(seg: Extract<Segment, { type: 'paragraph' }>): SegmentMetrics {
  const lineHeightPt = 14.6
  const listItems = extractListItems(seg.html)

  const lineCountFromHeight = Math.max(1, Math.round(seg.heightPt / lineHeightPt))

  if (listItems.length > 0) {
    const lineCountFromText = Math.max(
      1,
      listItems.reduce(
        (sum, item) => sum + Math.max(1, estimateWrappedLineCount(item, 44)),
        0,
      ),
    )
    const lineCount = Math.max(lineCountFromHeight, lineCountFromText)
    return {
      heightPt: Math.max(seg.heightPt, lineCount * lineHeightPt),
      lineCount,
      lineHeightPt,
      softFlowEligible: true,
    }
  }

  const text = stripHtml(seg.html)
  const lineCountFromText = estimateWrappedLineCount(text, 58)
  const lineCount = Math.max(lineCountFromHeight, lineCountFromText)

  return {
    heightPt: Math.max(seg.heightPt, lineCount * lineHeightPt),
    lineCount,
    lineHeightPt,
    softFlowEligible: true,
  }
}

function headingMetrics(seg: Extract<Segment, { type: 'heading' }>): SegmentMetrics {
  const charsPerLine =
    seg.level === 2 ? 24 : seg.level === 3 ? 30 : seg.level === 4 ? 36 : 22
  const lineHeightPt =
    seg.level === 2 ? 30 : seg.level === 3 ? 17 : seg.level === 4 ? 14 : 22
  const lineCountFromText = estimateWrappedLineCount(seg.text, charsPerLine)
  const lineCountFromHeight = Math.max(1, Math.round(seg.heightPt / lineHeightPt))
  const lineCount = Math.max(lineCountFromText, lineCountFromHeight)

  return {
    heightPt: Math.max(seg.heightPt, lineCount * lineHeightPt),
    lineCount,
    lineHeightPt,
    softFlowEligible: false,
  }
}

function segmentMetrics(seg: Segment): SegmentMetrics {
  if (seg.type === 'heading') {
    return headingMetrics(seg)
  }
  if (seg.type === 'paragraph') {
    return paragraphMetrics(seg)
  }

  const fallbackLineHeight = 14.6
  const lineCount = Math.max(1, Math.round(seg.heightPt / fallbackLineHeight))
  return {
    heightPt: seg.heightPt,
    lineCount,
    lineHeightPt: fallbackLineHeight,
    softFlowEligible: false,
  }
}

function headingFollowOnReservePt(next: Segment | undefined): number {
  if (next?.type !== 'paragraph') {
    return MIN_AFTER_HEADING_PT
  }
  const nextMetrics = segmentMetrics(next)
  return Math.max(MIN_AFTER_HEADING_PT, MIN_SOFT_FLOW_LINES * nextMetrics.lineHeightPt)
}

function canSoftFlowToSecondColumn(
  metrics: SegmentMetrics,
  availablePt: number,
  columnCapacityPt: number,
): { allowed: boolean; remainingHeightPt: number } {
  if (!metrics.softFlowEligible || availablePt <= 0) {
    return { allowed: false, remainingHeightPt: metrics.heightPt }
  }

  const linesThatFit = Math.floor(availablePt / metrics.lineHeightPt)
  if (linesThatFit < MIN_SOFT_FLOW_LINES) {
    return { allowed: false, remainingHeightPt: metrics.heightPt }
  }

  const linesRemaining = metrics.lineCount - linesThatFit
  if (linesRemaining < MIN_SOFT_FLOW_LINES) {
    return { allowed: false, remainingHeightPt: metrics.heightPt }
  }

  const remainingHeightPt = linesRemaining * metrics.lineHeightPt
  if (remainingHeightPt > columnCapacityPt) {
    return { allowed: false, remainingHeightPt: metrics.heightPt }
  }

  return { allowed: true, remainingHeightPt }
}

function segmentGuardPt(seg: Segment): number {
  switch (seg.type) {
    case 'heading':
      return 4
    case 'blockquote':
      return 4
    case 'table':
      return 8
    case 'image-ref':
      return 6
    case 'paragraph':
      return 5
    default:
      return 4
  }
}

function fitCountForPage(segments: Segment[]): FitResult {
  const hasSectionBanner =
    segments.length > 0 && segments[0].type === 'heading' && segments[0].level === 2

  // Section-heading pages lose substantial vertical space to framed banner and
  // fiction treatment. Reserve extra capacity so content doesn't spill into a
  // hidden third CSS column at runtime.
  const pageCapacityPt = hasSectionBanner
    ? EFFECTIVE_COLUMN_HEIGHT_PT - 72
    : EFFECTIVE_COLUMN_HEIGHT_PT

  let col = 0
  let fill = 0

  for (let i = 0; i < segments.length; i++) {
    const seg = segments[i]
    const metrics = segmentMetrics(seg)
    const budget = metrics.heightPt + segmentGuardPt(seg)

    if (seg.type === 'heading') {
      const level = seg.level
      if (level === 2 && i > 0) {
        return { fitCount: i, overflowAvailablePt: 0 }
      }
      if (
        level === 4 &&
        segments[i + 1]?.type === 'paragraph' &&
        fill +
          budget +
          Math.max(MIN_H4_AFTER_HEADING_PT, headingFollowOnReservePt(segments[i + 1])) >
          pageCapacityPt
      ) {
        return { fitCount: i, overflowAvailablePt: 0 }
      }
      if (
        level === 3 &&
        col === 1 &&
        fill > 0 &&
        fill + budget + headingFollowOnReservePt(segments[i + 1]) > pageCapacityPt - 8
      ) {
        return { fitCount: i, overflowAvailablePt: 0 }
      }
    }

    if (fill + budget > pageCapacityPt) {
      if (col === 0) {
        const availablePt = pageCapacityPt - fill
        const softFlow = canSoftFlowToSecondColumn(metrics, availablePt, pageCapacityPt)
        if (softFlow.allowed) {
          col = 1
          fill = softFlow.remainingHeightPt
          continue
        }

        col = 1
        fill = 0

        if (budget > pageCapacityPt) {
          return { fitCount: i, overflowAvailablePt: 0 }
        }
      } else {
        return {
          fitCount: i,
          overflowAvailablePt: Math.max(0, pageCapacityPt - fill),
        }
      }
    }

    fill += metrics.heightPt
  }

  return { fitCount: segments.length, overflowAvailablePt: 0 }
}

function applyRuntimeLeakGuard(data: BookData): BookData {
  const pages: BookPage[] = JSON.parse(JSON.stringify(data.pages)) as BookPage[]

  for (let i = 0; i < pages.length; i++) {
    const page = pages[i]
    const fit = fitCountForPage(page.segments)
    const fitCount = fit.fitCount
    if (fitCount >= page.segments.length) continue

    const keepCount = Math.max(1, fitCount)
    let kept = page.segments.slice(0, keepCount)
    let overflow = page.segments.slice(keepCount)

    // Soft split first overflow paragraph/list at page boundary when possible,
    // so we keep usable content on the current page instead of hard-punting
    // the entire segment to the next page.
    if (fit.overflowAvailablePt > 0 && fitCount < page.segments.length) {
      const candidate = page.segments[fitCount]
      if (candidate?.type === 'paragraph') {
        const split = splitParagraphSegmentForPageBoundary(
          candidate,
          fit.overflowAvailablePt,
        )
        if (split) {
          kept = [...kept, split.head]
          overflow = [split.tail, ...page.segments.slice(fitCount + 1)]
        }
      }
    }

    page.segments = kept

    if (overflow.length === 0) continue

    if (!pages[i + 1]) {
      pages.push({
        pageNumber: pages.length + 1,
        chapterTitle: page.chapterTitle,
        chapterIndex: page.chapterIndex,
        layout: page.layout,
        segments: [],
      })
    }

    const next = pages[i + 1]
    next.segments = [...overflow, ...next.segments]
  }

  const normalizedPages = pages.map((p, idx) => ({
    ...p,
    pageNumber: idx + 1,
  }))

  return {
    ...data,
    totalPages: normalizedPages.length,
    pages: normalizedPages,
  }
}

const bookData = applyRuntimeLeakGuard(bookDataRaw as BookData)

/** Read initial page from URL hash synchronously before first render. */
function readHashPage(): number {
  const m = window.location.hash.match(/^#page\/(\d+)$/)
  if (!m) return -1
  const n = parseInt(m[1], 10)
  if (isNaN(n)) return -1

  // URL hash is human-facing (1-based): #page/1 is the first numbered page.
  // Convert to the reader's logical 0-based index.
  const logical = n - 1
  return Math.min(Math.max(0, logical), bookData.totalPages - 1)
}

const INITIAL_PAGE = readHashPage()

export default function App() {
  const readerRef = useRef<BookReaderHandle>(null)
  const [currentPage, setCurrentPage] = useState(INITIAL_PAGE)
  const [tocOpen, setTocOpen] = useState(false)
  const [searchValue, setSearchValue] = useState('')

  // Compute search results
  const searchResults = useMemo(() => {
    return searchBook(bookData, searchValue)
  }, [searchValue])

  /** Called by BookReader whenever a page flip completes. */
  const handlePageChange = useCallback((page: number) => {
    setCurrentPage(page)
    if (page < 0) {
      history.replaceState(null, '', '#')
      return
    }
    history.replaceState(null, '', `#page/${page + 1}`)
  }, [])

  /** 'T' key toggles the TOC panel (treated as a keyboard shortcut). */
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      const tag = (e.target as HTMLElement).tagName
      if ((e.key === 't' || e.key === 'T') && tag !== 'INPUT' && tag !== 'TEXTAREA') {
        setTocOpen((open) => !open)
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  return (
    <>
      <BookReader
        ref={readerRef}
        bookData={bookData}
        initialPage={INITIAL_PAGE}
        onPageChange={handlePageChange}
      />

      <NavBar
        currentPage={currentPage}
        totalPages={bookData.totalPages}
        onGoToInstant={(p) => readerRef.current?.goToPageInstant(p)}
        onPrev={() => readerRef.current?.prevPage()}
        onPrevInstant={() => readerRef.current?.prevPageInstant()}
        onNext={() => readerRef.current?.nextPage()}
        onNextInstant={() => readerRef.current?.nextPageInstant()}
        onTocOpen={() => setTocOpen(true)}
        searchValue={searchValue}
        onSearchChange={setSearchValue}
      />

      <SearchPanel
        matches={searchResults}
        isOpen={searchValue.length > 0}
        onNavigate={(p) => {
          readerRef.current?.goToPage(p)
          setCurrentPage(p)
          history.replaceState(null, '', `#page/${p + 1}`)
        }}
        currentPage={currentPage}
      />

      <TableOfContents
        entries={bookData.toc}
        currentPage={currentPage}
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        onNavigate={(p) => {
          readerRef.current?.goToPageInstant(p)
          setCurrentPage(p)
          history.replaceState(null, '', `#page/${p + 1}`)
        }}
      />
    </>
  )
}
