/**
 * Flow Engine V2 — DOM-measurement-based pagination
 *
 * Core principle: Never estimate heights. Render content into a real DOM
 * container, ask the browser how tall it is, and use that truth to decide
 * what fits on each page/column.
 *
 * This eliminates the dual-layer mismatch between the old preprocessor
 * (TypeScript height estimates) and CSS multi-column layout (browser reflow).
 */

import type {
  BookData,
  BookPage,
  ChapterIndex,
  HeadingSegment,
  ParagraphSegment,
  Segment,
  TocEntry,
} from '@app-types/book'

// ── Configuration ──────────────────────────────────────────────────────────

// MIN_SPLIT_LINES removed — MIN_SPLIT_WORDS is used instead

/** Minimum word count for a viable paragraph split half */
const MIN_SPLIT_WORDS = 4

/** Small gap (px) to reserve at bottom of column for safety */
const COLUMN_BOTTOM_RESERVE_PX = 2

// ── Types ──────────────────────────────────────────────────────────────────

export interface FlowPage {
  pageNumber: number
  chapterTitle: string
  chapterIndex: number
  leftColumn: Segment[]
  rightColumn: Segment[]
}

// MeasureContext removed — using inline params instead

// FlowState removed — state is managed via local variables in runFlowEngine

// ── Measurement helpers ────────────────────────────────────────────────────

/**
 * Create an off-screen measurement container that matches the exact
 * column width and CSS styling of the real page layout.
 */
export function createMeasureContainer(columnWidth: number): HTMLDivElement {
  const container = document.createElement('div')

  // Position off-screen but still rendered (not display:none, which gives 0 height)
  container.style.cssText = `
    position: absolute;
    left: -9999px;
    top: 0;
    width: ${columnWidth}px;
    visibility: hidden;
    pointer-events: none;
    z-index: -1;
  `

  // Apply the same typography classes as the real page content
  container.className = 'flow-measure-container'

  document.body.appendChild(container)
  return container
}

export function destroyMeasureContainer(container: HTMLDivElement): void {
  container.remove()
}

/**
 * Measure the rendered height of a segment by inserting it into a real DOM
 * container and reading the browser's computed dimensions.
 */
function measureElement(el: HTMLElement, container: HTMLDivElement): number {
  container.appendChild(el)
  // Force layout calculation
  const height = el.getBoundingClientRect().height
  container.removeChild(el)
  return height
}

// ── Segment rendering for measurement ──────────────────────────────────────

/**
 * Create a DOM element that renders a segment identically to how
 * PageContent.tsx renders it. We need this for accurate measurement.
 */
function renderSegmentForMeasure(seg: Segment): HTMLElement {
  const wrapper = document.createElement('div')
  wrapper.className = 'segment-measure-wrap'

  switch (seg.type) {
    case 'heading': {
      const h = seg as HeadingSegment
      const tag = `h${h.level}` as 'h1' | 'h2' | 'h3' | 'h4'
      const el = document.createElement(tag)
      const cls = ['chapter-title', 'section-heading', 'subsection', 'bold-label'][
        h.level - 1
      ]
      el.className = cls
      el.textContent = h.text
      el.id = h.id ?? ''
      wrapper.appendChild(el)
      break
    }
    case 'paragraph': {
      const p = seg as ParagraphSegment
      const div = document.createElement('div')
      div.className = `body-text ${p.isChapterOpener ? 'chapter-opener' : ''} ${p.isFiction ? 'fiction-intro' : ''}`
      div.innerHTML = p.html
      wrapper.appendChild(div)
      break
    }
    case 'blockquote': {
      const div = document.createElement('div')
      div.className = 'flavour-text'
      div.innerHTML = (seg as { html: string }).html
      wrapper.appendChild(div)
      break
    }
    case 'table': {
      const t = seg as { headers: string[]; rows: string[][] }
      const table = document.createElement('table')
      const thead = document.createElement('thead')
      const headerRow = document.createElement('tr')
      for (const h of t.headers) {
        const th = document.createElement('th')
        th.textContent = h
        headerRow.appendChild(th)
      }
      thead.appendChild(headerRow)
      table.appendChild(thead)
      const tbody = document.createElement('tbody')
      for (const row of t.rows) {
        const tr = document.createElement('tr')
        for (const cell of row) {
          const td = document.createElement('td')
          td.textContent = cell
          tr.appendChild(td)
        }
        tbody.appendChild(tr)
      }
      table.appendChild(tbody)
      wrapper.appendChild(table)
      break
    }
    case 'hr': {
      const hr = document.createElement('hr')
      hr.className = 'gold-rule'
      wrapper.appendChild(hr)
      break
    }
    case 'image-ref': {
      const img = seg as { filename: string; width: number; height: number; altText: string }
      const imgEl = document.createElement('img')
      imgEl.src = `/images/${img.filename}`
      imgEl.alt = img.altText
      imgEl.style.maxWidth = '100%'
      imgEl.style.height = 'auto'
      wrapper.appendChild(imgEl)
      break
    }
  }

  return wrapper
}

// ── Paragraph splitting with DOM measurement ───────────────────────────────

function stripHtml(html: string): string {
  const tmp = document.createElement('div')
  tmp.innerHTML = html
  return tmp.textContent ?? ''
}

function isSentenceBoundary(word: string): boolean {
  return /[.!?]["')\]]*$/.test(word)
}

/**
 * Split a paragraph so the head portion fits within availableHeight px.
 * Uses binary search on word count with real DOM measurement.
 */
function splitParagraphByMeasure(
  seg: ParagraphSegment,
  availableHeight: number,
  measureContainer: HTMLDivElement,
): { head: ParagraphSegment; tail: ParagraphSegment } | null {
  const text = stripHtml(seg.html)
  const words = text.split(/\s+/).filter(Boolean)

  if (words.length < MIN_SPLIT_WORDS * 2) return null

  // Binary search for the maximum number of words that fit
  let lo = MIN_SPLIT_WORDS
  let hi = words.length - MIN_SPLIT_WORDS
  let bestSplit = -1

  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2)
    const headText = words.slice(0, mid).join(' ')

    const testEl = document.createElement('div')
    testEl.className = 'body-text'
    testEl.innerHTML = `<p>${escapeHtml(headText)}</p>`

    const height = measureElement(testEl, measureContainer)

    if (height <= availableHeight) {
      bestSplit = mid
      lo = mid + 1
    } else {
      hi = mid - 1
    }
  }

  if (bestSplit < MIN_SPLIT_WORDS || words.length - bestSplit < MIN_SPLIT_WORDS) {
    return null
  }

  // Look for a nearby sentence boundary for a cleaner break
  const lookBack = Math.min(12, bestSplit - MIN_SPLIT_WORDS)
  for (let i = bestSplit - 1; i >= bestSplit - lookBack; i--) {
    if (isSentenceBoundary(words[i])) {
      // Verify this still fits
      const candidateText = words.slice(0, i + 1).join(' ')
      const testEl = document.createElement('div')
      testEl.className = 'body-text'
      testEl.innerHTML = `<p>${escapeHtml(candidateText)}</p>`
      const h = measureElement(testEl, measureContainer)
      if (h <= availableHeight && words.length - (i + 1) >= MIN_SPLIT_WORDS) {
        bestSplit = i + 1
        break
      }
    }
  }

  // Also look forward a few words for a sentence boundary
  if (!isSentenceBoundary(words[bestSplit - 1])) {
    const lookAhead = Math.min(8, words.length - MIN_SPLIT_WORDS - bestSplit)
    for (let i = bestSplit; i < bestSplit + lookAhead; i++) {
      if (isSentenceBoundary(words[i])) {
        const candidateText = words.slice(0, i + 1).join(' ')
        const testEl = document.createElement('div')
        testEl.className = 'body-text'
        testEl.innerHTML = `<p>${escapeHtml(candidateText)}</p>`
        const h = measureElement(testEl, measureContainer)
        if (h <= availableHeight && words.length - (i + 1) >= MIN_SPLIT_WORDS) {
          bestSplit = i + 1
          break
        }
      }
    }
  }

  const headText = words.slice(0, bestSplit).join(' ')
  const tailText = words.slice(bestSplit).join(' ')

  return {
    head: {
      ...seg,
      html: `<p>${escapeHtml(headText)}</p>`,
      heightPt: 0, // Not used in new engine
    },
    tail: {
      ...seg,
      html: `<p>${escapeHtml(tailText)}</p>`,
      heightPt: 0,
      isChapterOpener: false,
    },
  }
}

/**
 * Split a list segment by items that fit within availableHeight.
 */
function splitListByMeasure(
  seg: ParagraphSegment,
  availableHeight: number,
  measureContainer: HTMLDivElement,
): { head: ParagraphSegment; tail: ParagraphSegment } | null {
  const liMatches = seg.html.match(/<li[\s\S]*?<\/li>/gi)
  if (!liMatches || liMatches.length < 2) return null

  const isOrdered = /<ol[\s>]/i.test(seg.html)
  const wrapperTag = isOrdered ? 'ol' : 'ul'

  // Find how many items fit
  let splitAt = 0
  for (let i = 1; i <= liMatches.length; i++) {
    const headHtml = `<${wrapperTag}>\n${liMatches.slice(0, i).join('\n')}\n</${wrapperTag}>`
    const testEl = document.createElement('div')
    testEl.className = 'body-text'
    testEl.innerHTML = headHtml
    const height = measureElement(testEl, measureContainer)

    if (height <= availableHeight) {
      splitAt = i
    } else {
      break
    }
  }

  if (splitAt < 1 || liMatches.length - splitAt < 1) return null

  const headHtml = `<${wrapperTag}>\n${liMatches.slice(0, splitAt).join('\n')}\n</${wrapperTag}>`
  const tailHtml = `<${wrapperTag}>\n${liMatches.slice(splitAt).join('\n')}\n</${wrapperTag}>`

  return {
    head: {
      ...seg,
      html: headHtml,
      heightPt: 0,
    },
    tail: {
      ...seg,
      html: tailHtml,
      heightPt: 0,
      isChapterOpener: false,
    },
  }
}

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')
}

// ── Typography rules ───────────────────────────────────────────────────────

function isH2(seg: Segment): boolean {
  return seg.type === 'heading' && (seg as HeadingSegment).level === 2
}

function isHeading(seg: Segment): boolean {
  return seg.type === 'heading'
}

function isListSegment(seg: Segment): boolean {
  return seg.type === 'paragraph' && /<[uo]l[\s>]/i.test((seg as ParagraphSegment).html)
}

function isFiction(seg: Segment): boolean {
  return seg.type === 'paragraph' && !!(seg as ParagraphSegment).isFiction
}

// ── Main flow algorithm ────────────────────────────────────────────────────

export interface FlowEngineOptions {
  /** The available width for a single column, in px */
  columnWidth: number
  /** The available height for content in a column, in px */
  columnHeight: number
  /** All segments from all chapters, in order */
  chapters: Array<{
    title: string
    index: number
    segments: Segment[]
  }>
  /** TOC entries (for page resolution after flow) */
  tocEntries?: TocEntry[]
}

export interface FlowResult {
  bookData: BookData
  pageCount: number
}

/**
 * Run the flow engine: measure each segment in the DOM, assign to
 * pages and columns based on actual rendered heights.
 *
 * This must be called after fonts are loaded and the DOM is ready.
 */
export function runFlowEngine(options: FlowEngineOptions): FlowResult {
  const { columnWidth, columnHeight, chapters, tocEntries = [] } = options

  const measureContainer = createMeasureContainer(columnWidth)
  const effectiveHeight = columnHeight - COLUMN_BOTTOM_RESERVE_PX

  const pages: BookPage[] = []
  const chapterIndex: ChapterIndex[] = []

  let pageNumber = 1
  let currentPage = newPage(pageNumber, chapters[0]?.title ?? '', 0)
  let leftSegments: Segment[] = []
  let rightSegments: Segment[] = []
  let currentColumn: 'left' | 'right' = 'left'
  let columnFill = 0 // px used in current column

  function getCurrentSegments(): Segment[] {
    return currentColumn === 'left' ? leftSegments : rightSegments
  }

  // setCurrentSegments removed — not needed since we push to getCurrentSegments()

  function flushPage(): void {
    currentPage.segments = buildPageSegments(leftSegments, rightSegments)
    if (currentPage.segments.length > 0 || pageNumber === 1) {
      pages.push(currentPage)
    }
    pageNumber++
    leftSegments = []
    rightSegments = []
    currentColumn = 'left'
    columnFill = 0
  }

  function nextColumn(): void {
    if (currentColumn === 'left') {
      currentColumn = 'right'
      columnFill = 0
    } else {
      flushPage()
      currentPage = newPage(pageNumber, currentPage.chapterTitle, currentPage.chapterIndex)
    }
  }

  function measureSeg(seg: Segment): number {
    const el = renderSegmentForMeasure(seg)
    return measureElement(el, measureContainer)
  }

  // Process all chapters
  for (const chapter of chapters) {
    const chStartPage = pageNumber

    // Ensure new chapter context on current page
    if (currentPage.chapterTitle !== chapter.title) {
      if (leftSegments.length > 0 || rightSegments.length > 0) {
        flushPage()
        currentPage = newPage(pageNumber, chapter.title, chapter.index)
      } else {
        currentPage.chapterTitle = chapter.title
        currentPage.chapterIndex = chapter.index
      }
    }

    for (let i = 0; i < chapter.segments.length; i++) {
      const seg = chapter.segments[i]
      const nextSeg = chapter.segments[i + 1]

      // ── Rule: H2 headings always start on a new page ──
      if (isH2(seg)) {
        if (leftSegments.length > 0 || rightSegments.length > 0 || columnFill > 0) {
          flushPage()
          currentPage = newPage(pageNumber, chapter.title, chapter.index)
        }
        columnFill = 0
        currentColumn = 'left'
      }

      // ── Rule: Front-matter fiction starts on a new page ──
      if (
        chapter.index === 0 &&
        isFiction(seg) &&
        !getCurrentSegments().some((s) => isFiction(s))
      ) {
        if (leftSegments.length > 0 || rightSegments.length > 0) {
          flushPage()
          currentPage = newPage(pageNumber, chapter.title, chapter.index)
        }
      }

      // ── Rule: "FORBIDDEN LANDS" h3 in front-matter starts page 3 ──
      if (
        chapter.index === 0 &&
        seg.type === 'heading' &&
        (seg as HeadingSegment).level === 3 &&
        (seg as HeadingSegment).text === 'FORBIDDEN LANDS'
      ) {
        if (leftSegments.length > 0 || rightSegments.length > 0) {
          flushPage()
          currentPage = newPage(pageNumber, chapter.title, chapter.index)
        }
      }

      // Measure the segment
      const segHeight = measureSeg(seg)

      // ── Rule: Heading + follow-on content cohesion ──
      // If a heading barely fits but leaves no room for the next segment,
      // move it to the next column/page.
      if (isHeading(seg) && nextSeg) {
        const headingLevel = (seg as HeadingSegment).level
        // Measure a minimum follow-on (one line of body text ≈ 18px)
        const minFollowOn = headingLevel >= 3 ? 20 : 30
        if (columnFill + segHeight + minFollowOn > effectiveHeight) {
          nextColumn()
          if (currentColumn === 'left') {
            currentPage = newPage(pageNumber, chapter.title, chapter.index)
          }
          columnFill = 0
        }
      }

      // Does the segment fit in the current column?
      if (columnFill + segHeight <= effectiveHeight) {
        // It fits! Add it.
        getCurrentSegments().push(seg)
        columnFill += segHeight
        continue
      }

      // ── Overflow: segment does not fit ──
      const availableSpace = effectiveHeight - columnFill

      // Try paragraph splitting
      if (seg.type === 'paragraph' && availableSpace > 30) {
        const pSeg = seg as ParagraphSegment

        // Try list split first
        if (isListSegment(seg)) {
          const listSplit = splitListByMeasure(pSeg, availableSpace, measureContainer)
          if (listSplit) {
            getCurrentSegments().push(listSplit.head)
            nextColumn()
            if (currentColumn === 'left') {
              currentPage = newPage(pageNumber, chapter.title, chapter.index)
            }
            // Re-process the tail
            getCurrentSegments().push(listSplit.tail)
            columnFill = measureSeg(listSplit.tail)
            continue
          }
        }

        // Try text paragraph split
        const textSplit = splitParagraphByMeasure(pSeg, availableSpace, measureContainer)
        if (textSplit) {
          getCurrentSegments().push(textSplit.head)
          nextColumn()
          if (currentColumn === 'left') {
            currentPage = newPage(pageNumber, chapter.title, chapter.index)
          }
          getCurrentSegments().push(textSplit.tail)
          columnFill = measureSeg(textSplit.tail)
          continue
        }
      }

      // No split possible — move whole segment to next column/page
      nextColumn()
      if (currentColumn === 'left') {
        currentPage = newPage(pageNumber, chapter.title, chapter.index)
      }
      columnFill = 0

      // Check if the segment fits in a fresh column
      if (segHeight > effectiveHeight) {
        // Segment is taller than a full column — force it in and let it overflow
        // (this handles very large tables or images)
        getCurrentSegments().push(seg)
        columnFill = segHeight
      } else {
        getCurrentSegments().push(seg)
        columnFill = segHeight
      }
    }

    // Record chapter range
    chapterIndex.push({
      chapterTitle: chapter.title,
      chapterIndex: chapter.index,
      firstPage: chStartPage,
      lastPage: pageNumber,
    })
  }

  // Flush final page
  currentPage.segments = buildPageSegments(leftSegments, rightSegments)
  if (currentPage.segments.length > 0) {
    pages.push(currentPage)
  }

  // Clean up measurement container
  destroyMeasureContainer(measureContainer)

  // Normalize page numbers
  const normalizedPages = pages.map((p, idx) => ({
    ...p,
    pageNumber: idx + 1,
  }))

  // Resolve TOC page numbers
  const headingPageMap = buildHeadingPageMap(normalizedPages)
  const resolvedToc = tocEntries.map((entry) => {
    const key = normalizeTocKey(entry.title)
    const resolvedPage = headingPageMap.get(key)
    return resolvedPage ? { ...entry, page: resolvedPage } : entry
  })

  const bookData: BookData = {
    generatedAt: new Date().toISOString(),
    totalPages: normalizedPages.length,
    chapters: chapterIndex,
    toc: resolvedToc,
    pages: normalizedPages,
  }

  return { bookData, pageCount: normalizedPages.length }
}

// ── Helpers ────────────────────────────────────────────────────────────────

/**
 * Build the page segments array from left/right column segments.
 * We use a column-break marker segment to tell the renderer where
 * the left column ends and the right column begins.
 */
function buildPageSegments(left: Segment[], right: Segment[]): Segment[] {
  // We store left + right segments concatenated, with a special marker
  // that the renderer uses to split them into two columns.
  // The marker is a zero-height HR segment with a special id.
  if (left.length === 0 && right.length === 0) return []

  const result: Segment[] = [...left]

  if (right.length > 0) {
    // Add column break marker
    result.push({
      type: 'hr',
      heightPt: 0,
      id: '__column_break__',
    })
    result.push(...right)
  }

  return result
}

function newPage(num: number, chapterTitle: string, chapterIndex: number): BookPage {
  return {
    pageNumber: num,
    chapterTitle,
    chapterIndex,
    layout: 'two-column',
    segments: [],
  }
}

function normalizeTocKey(text: string): string {
  return text
    .toLowerCase()
    .replace(/^\s*\d+\s*[.:)]\s*/u, '')
    .replace(/^\s*text\s*box\s*:\s*/u, '')
    .replace(/[^a-z0-9\s]/gu, ' ')
    .replace(/\s+/gu, ' ')
    .trim()
}

function buildHeadingPageMap(pages: BookPage[]): Map<string, number> {
  const map = new Map<string, number>()
  for (const page of pages) {
    for (const seg of page.segments) {
      if (seg.type !== 'heading') continue
      const key = normalizeTocKey((seg as HeadingSegment).text)
      if (!key) continue
      if (!map.has(key)) map.set(key, page.pageNumber)
    }
  }
  return map
}
