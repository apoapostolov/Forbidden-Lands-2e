#!/usr/bin/env tsx
/**
 * Forbidden Lands Reader — Content Pre-processor
 *
 * Reads all 01-corebook/*.md files, parses them into segment objects,
 * paginates using estimated heights, and writes src/data/book-data.json.
 *
 * Usage:
 *   npx tsx scripts/preprocess.ts
 *   npm run preprocess
 */

import { existsSync, readFileSync, writeFileSync } from 'fs'
import type {
  Blockquote as MdastBlockquote,
  Heading,
  List,
  ListItem,
  Paragraph as MdastParagraph,
  Root as MdastRoot,
  Node,
  Table,
  TableRow,
} from 'mdast'
import { dirname, join, resolve } from 'path'
import rehypeSanitize from 'rehype-sanitize'
import rehypeStringify from 'rehype-stringify'
import remarkGfm from 'remark-gfm'
import remarkParse from 'remark-parse'
import remarkRehype from 'remark-rehype'
import { unified } from 'unified'
import { fileURLToPath } from 'url'

// ── Paths ─────────────────────────────────────────────────────────────────────
const __dirname = dirname(fileURLToPath(import.meta.url))
const READER_DIR = resolve(__dirname, '..')
const COREBOOK_DIR = resolve(READER_DIR, '..', '01-corebook')
const IMAGES_DIR = resolve(READER_DIR, 'public', 'images')
const MANIFEST = resolve(READER_DIR, 'src', 'data', 'image_manifest.json')
const TOC_FILE = resolve(READER_DIR, 'src', 'data', 'toc.json')
const OUTPUT = resolve(READER_DIR, 'public', 'book-data.json')

// ── Chapter files in order ────────────────────────────────────────────────────
const CHAPTER_FILES = [
  '01-front-matter.md',
  '02-your-adventurer.md',
  '03-skills.md',
  '04-talents.md',
  '05-combat-and-damage.md',
  '06-critical-injuries.md',
  '07-magic.md',
  '08-journeys.md',
  '09-the-stronghold.md',
  '10-gear.md',
  '11-appendix.md',
  '12-mercenaries-of-forbidden-lands.md',
  '13-lifepaths-of-the-forbidden-lands.md',
  '14-traderoads-of-the-forbidden-lands.md',
]

// ── Layout constants (pt) ─────────────────────────────────────────────────────
// Matches dev plan: 482 × 680pt page, 50pt h-margins, 60pt v-margins
// IMPORTANT: this must track actual runtime CSS layout, including
// PageHeaderBanner + PageFooter occupancy inside the page content column.
// Previous value (560pt) overestimated available space and could pack trailing
// paragraphs into clipped/non-visible area at page boundaries.
const COLUMN_HEIGHT_PT = 528
// 2 columns per page — used implicitly by the paginator (2 × COLUMN_HEIGHT_PT)
const BODY_LINE_WIDTH_EM = 19.5 // accounts for real glyph widths and inline labels
const LIST_LINE_WIDTH_EM = 19.8 // marker and hanging-list indentation
const LINE_HEIGHT_PT = 11.95 // 11px × 1.45 converted to points
const PARA_MARGIN_PT = 4.1 // .body-text margin-bottom: 0.5em
const LIST_ITEM_EXTRA_PT = 2 // account for li spacing + marker rendering
const LIST_BLOCK_EXTRA_PT = 6 // account for ul/ol margins and wrap variance
const TABLE_LINE_HEIGHT_PT = 11.7
const TABLE_CELL_PADDING_PT = 4.5
const COLUMN_TABLE_DECOR_PT = 27
const SPAN_TABLE_DECOR_PT = 39
const COLUMN_TABLE_WIDTH_PT = 176
const SPAN_TABLE_WIDTH_PT = 346
const TABLE_FONT_SIZE_PT = 6
const BLOCKQUOTE_DECOR_PT = 38
const BLOCKQUOTE_LINE_WIDTH_EM = 13.5
const BLOCKQUOTE_LINE_HEIGHT_PT = 13.6
const FICTION_LINE_WIDTH_EM = 29
const FICTION_LINE_HEIGHT_PT = 20.7
const FICTION_MARGIN_PT = 10
const RENDER_SAFETY_PT = 30 // calibrated footer clearance after fixed page chrome
const TABLE_LAYOUT_POLICY = {
  maxColumnCount: 3,
  minColumnTrackEm: 4.5,
  maxColumnHeightRatioBeforePromotion: 1,
  maxColumnRowHeightRatioBeforePromotion: 0.52,
  minSpanHeightImprovement: 0.22,
  minRowsAfterHeading: 1,
  minCellLinesPerFragment: 1,
  minUsableColumnAfterSpanPt: 150,
} as const
// H2 artwork and optional chapter fiction span the full page width. Reserve
// their rendered height from both columns instead of charging only the left.
const SECTION_HEADING_RESERVE_PT = 145
const SECTION_FICTION_MIN_RESERVE_PT = 48
const MIN_SPLIT_LINES = 2
const MIN_SPLIT_HEIGHT_PT = LINE_HEIGHT_PT * MIN_SPLIT_LINES
const PARAGRAPH_GUARD_PT = 1.5
const LIST_GUARD_PT = 2
const MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT =
  MIN_SPLIT_HEIGHT_PT + PARA_MARGIN_PT + PARAGRAPH_GUARD_PT

function estimateListBlockHeight(itemHeights: number[]): number {
  return itemHeights.reduce((s, h) => s + h, 0) + LIST_BLOCK_EXTRA_PT
}

function tableColumnLineWidths(
  headers: string[],
  rows: string[][],
  columnCount: number,
  spanAll: boolean,
): number[] {
  const tableWidth = spanAll ? SPAN_TABLE_WIDTH_PT : COLUMN_TABLE_WIDTH_PT
  const horizontalPaddingEm = 2
  const contentWidthEm = Math.max(
    columnCount * TABLE_LAYOUT_POLICY.minColumnTrackEm,
    tableWidth / TABLE_FONT_SIZE_PT - horizontalPaddingEm * columnCount,
  )
  const weights = Array.from({ length: columnCount }, (_, columnIndex) => {
    const values = [headers[columnIndex] ?? '', ...rows.map((row) => row[columnIndex] ?? '')]
    const intrinsicWidth = Math.max(1, ...values.map(textWidthEm))
    return Math.sqrt(intrinsicWidth)
  })
  const weightTotal = weights.reduce((sum, weight) => sum + weight, 0)
  return weights.map((weight) =>
    Math.max(
      TABLE_LAYOUT_POLICY.minColumnTrackEm,
      (contentWidthEm * weight) / weightTotal,
    ),
  )
}

function tableIntrinsicMinWidthEm(headers: string[], rows: string[][]): number {
  const columnCount = Math.max(1, headers.length, ...rows.map((row) => row.length))
  const cellPaddingEm = 2
  return Array.from({ length: columnCount }, (_, columnIndex) => {
    const values = [headers[columnIndex] ?? '', ...rows.map((row) => row[columnIndex] ?? '')]
    const widestToken = Math.max(
      TABLE_LAYOUT_POLICY.minColumnTrackEm,
      ...values.flatMap((value) =>
        value.split(/\s+/u).filter(Boolean).map(textWidthEm),
      ),
    )
    return widestToken + cellPaddingEm
  }).reduce((sum, width) => sum + width, 0)
}

function estimateTableRowHeight(
  cells: string[],
  columnLineWidths: number[],
): number {
  const lines = Math.max(
    1,
    ...cells.map((cell, index) =>
      estimateWrappedLines(cell, columnLineWidths[index] ?? 3.5),
    ),
  )
  return lines * TABLE_LINE_HEIGHT_PT + TABLE_CELL_PADDING_PT
}

function estimateTableHeight(
  rowHeights: number[],
  headerHeightPt: number,
  spanAll: boolean,
): number {
  const decorHeightPt = spanAll ? SPAN_TABLE_DECOR_PT : COLUMN_TABLE_DECOR_PT
  return headerHeightPt + rowHeights.reduce((sum, height) => sum + height, 0) + decorHeightPt
}

// ── Types ─────────────────────────────────────────────────────────────────────
interface BaseSegment {
  type: string
  heightPt: number
  id?: string
  uid?: string
}
interface HeadingSegment extends BaseSegment {
  type: 'heading'
  level: 1 | 2 | 3 | 4
  text: string
  spanAll?: boolean
}
interface ParagraphSegment extends BaseSegment {
  type: 'paragraph'
  html: string
  isChapterOpener?: boolean
  isFiction?: boolean
  /** True when this segment was sourced from a markdown list node */
  isListSegment?: boolean
  /** Per-top-level-item <li>...</li> HTML for paginator splitting */
  itemLiHtmls?: string[]
  /** Height estimate per item (pt) */
  itemHeights?: number[]
  /** Preserve ordered versus unordered list semantics across fragments. */
  listTag?: 'ul' | 'ol'
  /** MDAST source retained only while preprocessing, never serialized. */
  sourceNode?: MdastParagraph
  /** Continuation metadata used by tests, search, and future rendering refinements. */
  continuesFromPrevious?: boolean
  continuesOnNext?: boolean
}
interface BlockquoteSegment extends BaseSegment {
  type: 'blockquote'
  html: string
  /** MDAST source retained only while preprocessing, never serialized. */
  sourceNode?: MdastBlockquote
  spanAll?: boolean
  isFiction?: boolean
  continuesFromPrevious?: boolean
  continuesOnNext?: boolean
}
interface TableSegment extends BaseSegment {
  type: 'table'
  headers: string[]
  rows: string[][]
  spanAll?: boolean
  layoutReason?:
    | 'column-count'
    | 'intrinsic-width'
    | 'row-height'
    | 'table-height'
    | 'column-fit'
    | 'runtime-overflow'
  columnLineWidthsEm?: number[]
  rowHeights?: number[]
  headerHeightPt?: number
  rowContinuesFromPrevious?: boolean[]
  rowContinuesOnNext?: boolean[]
  continuesFromPrevious?: boolean
  continuesOnNext?: boolean
}
interface HRSegment extends BaseSegment {
  type: 'hr'
}
interface ImageRefSegment extends BaseSegment {
  type: 'image-ref'
  filename: string
  width: number
  height: number
  altText: string
  caption?: string
}
type Segment =
  | HeadingSegment
  | ParagraphSegment
  | BlockquoteSegment
  | TableSegment
  | HRSegment
  | ImageRefSegment

function tableRowsThatFit(table: TableSegment, availableHeightPt: number): number {
  const rowHeights = table.rowHeights ?? []
  const fixedHeight =
    (table.headerHeightPt ?? 0) +
    (table.spanAll ? SPAN_TABLE_DECOR_PT : COLUMN_TABLE_DECOR_PT)
  let usedHeight = fixedHeight
  let count = 0
  for (const rowHeight of rowHeights) {
    if (usedHeight + rowHeight > availableHeightPt) break
    usedHeight += rowHeight
    count++
  }
  return count
}

function tableFragment(
  table: TableSegment,
  startRow: number,
  endRow: number,
): TableSegment {
  const rowHeights = (table.rowHeights ?? []).slice(startRow, endRow)
  const headerHeightPt = table.headerHeightPt ?? 0
  return {
    ...table,
    rows: table.rows.slice(startRow, endRow),
    rowHeights,
    rowContinuesFromPrevious: table.rowContinuesFromPrevious?.slice(
      startRow,
      endRow,
    ),
    rowContinuesOnNext: table.rowContinuesOnNext?.slice(startRow, endRow),
    heightPt: estimateTableHeight(rowHeights, headerHeightPt, !!table.spanAll),
  }
}

function layoutTable(
  table: Pick<
    TableSegment,
    | 'headers'
    | 'rows'
    | 'rowContinuesFromPrevious'
    | 'rowContinuesOnNext'
  > &
    Partial<TableSegment>,
  spanAll: boolean,
  layoutReason: TableSegment['layoutReason'],
): TableSegment {
  const columnCount = Math.max(
    1,
    table.headers.length,
    ...table.rows.map((row) => row.length),
  )
  const headers = Array.from(
    { length: columnCount },
    (_, index) => table.headers[index] ?? '',
  )
  const rows = table.rows.map((row) =>
    Array.from({ length: columnCount }, (_, index) => row[index] ?? ''),
  )
  const columnLineWidthsEm = tableColumnLineWidths(
    headers,
    rows,
    columnCount,
    spanAll,
  )
  const headerHeightPt = estimateTableRowHeight(headers, columnLineWidthsEm)
  const rowHeights = rows.map((row) =>
    estimateTableRowHeight(row, columnLineWidthsEm),
  )
  return {
    type: 'table',
    heightPt: estimateTableHeight(rowHeights, headerHeightPt, spanAll),
    ...table,
    headers,
    rows,
    spanAll,
    layoutReason,
    columnLineWidthsEm,
    headerHeightPt,
    rowHeights,
    rowContinuesFromPrevious:
      table.rowContinuesFromPrevious ?? rows.map(() => false),
    rowContinuesOnNext: table.rowContinuesOnNext ?? rows.map(() => false),
  }
}

function chooseTableLayout(headers: string[], rows: string[][]): TableSegment {
  const columnCount = Math.max(1, headers.length, ...rows.map((row) => row.length))
  if (columnCount > TABLE_LAYOUT_POLICY.maxColumnCount) {
    return layoutTable({ headers, rows }, true, 'column-count')
  }

  const columnLayout = layoutTable({ headers, rows }, false, 'column-fit')
  const spanLayout = layoutTable({ headers, rows }, true, 'column-fit')
  const legalHeight = COLUMN_HEIGHT_PT - RENDER_SAFETY_PT
  const intrinsicWidthPt = tableIntrinsicMinWidthEm(headers, rows) * TABLE_FONT_SIZE_PT
  if (intrinsicWidthPt > COLUMN_TABLE_WIDTH_PT) {
    return { ...spanLayout, layoutReason: 'intrinsic-width' }
  }

  const tallestColumnRow = Math.max(0, ...(columnLayout.rowHeights ?? []))
  const tallestSpanRow = Math.max(0, ...(spanLayout.rowHeights ?? []))
  const rowHeightImprovement =
    tallestColumnRow > 0
      ? 1 - tallestSpanRow / tallestColumnRow
      : 0
  if (
    tallestColumnRow >
      legalHeight * TABLE_LAYOUT_POLICY.maxColumnRowHeightRatioBeforePromotion &&
    rowHeightImprovement >= TABLE_LAYOUT_POLICY.minSpanHeightImprovement
  ) {
    return { ...spanLayout, layoutReason: 'row-height' }
  }

  const tableHeightImprovement =
    columnLayout.heightPt > 0
      ? 1 - spanLayout.heightPt / columnLayout.heightPt
      : 0
  if (
    columnLayout.heightPt >
      legalHeight * TABLE_LAYOUT_POLICY.maxColumnHeightRatioBeforePromotion &&
    spanLayout.heightPt <= legalHeight &&
    tableHeightImprovement >= TABLE_LAYOUT_POLICY.minSpanHeightImprovement
  ) {
    return { ...spanLayout, layoutReason: 'table-height' }
  }

  return columnLayout
}

function tableWithRows(
  table: TableSegment,
  rows: string[][],
  rowContinuesFromPrevious: boolean[],
  rowContinuesOnNext: boolean[],
): TableSegment {
  const columnLineWidthsEm =
    table.columnLineWidthsEm ??
    tableColumnLineWidths(
      table.headers,
      rows,
      Math.max(1, table.headers.length),
      !!table.spanAll,
    )
  const headerHeightPt =
    table.headerHeightPt ??
    estimateTableRowHeight(table.headers, columnLineWidthsEm)
  const rowHeights = rows.map((row) =>
    estimateTableRowHeight(row, columnLineWidthsEm),
  )
  return {
    ...table,
    rows,
    columnLineWidthsEm,
    headerHeightPt,
    rowHeights,
    rowContinuesFromPrevious,
    rowContinuesOnNext,
    heightPt: estimateTableHeight(rowHeights, headerHeightPt, !!table.spanAll),
  }
}

function splitTextForTableLines(
  value: string,
  lineWidthEm: number,
  maxLines: number,
): { head: string; tail: string } {
  const trimmed = value.trim()
  if (!trimmed || estimateWrappedLines(trimmed, lineWidthEm) <= maxLines) {
    return { head: trimmed, tail: '' }
  }

  const words = trimmed.split(/\s+/u)
  let low = 1
  let high = words.length - 1
  let splitAt = 0
  while (low <= high) {
    const candidate = Math.floor((low + high) / 2)
    if (estimateWrappedLines(words.slice(0, candidate).join(' '), lineWidthEm) <= maxLines) {
      splitAt = candidate
      low = candidate + 1
    } else {
      high = candidate - 1
    }
  }
  if (splitAt > 0) {
    return {
      head: words.slice(0, splitAt).join(' '),
      tail: words.slice(splitAt).join(' '),
    }
  }

  // A single unbroken token still needs a legal escape hatch. Split it at the
  // widest character boundary that fits the requested number of table lines.
  const characters = [...trimmed]
  const maxWidthEm = lineWidthEm * maxLines
  let usedWidthEm = 0
  let characterSplit = 0
  while (characterSplit < characters.length) {
    const nextWidth = textWidthEm(characters[characterSplit])
    if (usedWidthEm + nextWidth > maxWidthEm) break
    usedWidthEm += nextWidth
    characterSplit++
  }
  characterSplit = Math.max(1, Math.min(characterSplit, characters.length - 1))
  return {
    head: characters.slice(0, characterSplit).join(''),
    tail: characters.slice(characterSplit).join(''),
  }
}

function splitOversizedFirstTableRow(
  table: TableSegment,
  availableHeightPt: number,
): { head: TableSegment; tail: TableSegment } | null {
  const firstRow = table.rows[0]
  if (!firstRow) return null
  const fixedHeightPt =
    (table.headerHeightPt ?? 0) +
    (table.spanAll ? SPAN_TABLE_DECOR_PT : COLUMN_TABLE_DECOR_PT)
  const availableRowHeightPt = availableHeightPt - fixedHeightPt
  const maxLines = Math.floor(
    (availableRowHeightPt - TABLE_CELL_PADDING_PT) / TABLE_LINE_HEIGHT_PT,
  )
  if (maxLines < TABLE_LAYOUT_POLICY.minCellLinesPerFragment) return null

  const widths = table.columnLineWidthsEm ?? []
  const cellSplits = firstRow.map((cell, index) =>
    splitTextForTableLines(
      cell,
      widths[index] ?? TABLE_LAYOUT_POLICY.minColumnTrackEm,
      maxLines,
    ),
  )
  if (!cellSplits.some((cell) => cell.tail)) return null

  const existingFromPrevious = table.rowContinuesFromPrevious?.[0] ?? false
  const existingOnNext = table.rowContinuesOnNext?.[0] ?? false
  const head = tableWithRows(
    table,
    [cellSplits.map((cell) => cell.head)],
    [existingFromPrevious],
    [true],
  )
  const tail = tableWithRows(
    table,
    [cellSplits.map((cell) => cell.tail), ...table.rows.slice(1)],
    [
      true,
      ...(table.rowContinuesFromPrevious?.slice(1) ??
        table.rows.slice(1).map(() => false)),
    ],
    [
      existingOnNext,
      ...(table.rowContinuesOnNext?.slice(1) ??
        table.rows.slice(1).map(() => false)),
    ],
  )
  head.continuesOnNext = true
  tail.continuesFromPrevious = true
  return { head, tail }
}

function segmentGuardPt(seg: Segment): number {
  switch (seg.type) {
    case 'heading':
      return 1
    case 'blockquote':
      return 4
    case 'table':
      return 4
    case 'image-ref':
      return 6
    case 'paragraph':
      return (seg as ParagraphSegment).isListSegment
        ? LIST_GUARD_PT
        : PARAGRAPH_GUARD_PT
    default:
      return 4
  }
}

interface BookPage {
  pageNumber: number
  chapterTitle: string
  chapterIndex: number
  layout: 'two-column' | 'single-column' | 'full-art' | 'cover'
  segments: Segment[]
}
interface TocEntry {
  level: number
  title: string
  page: number
}
interface ChapterIndex {
  chapterTitle: string
  chapterIndex: number
  firstPage: number
  lastPage: number
}
interface ManifestEntry {
  xref: number
  filename: string
  width: number
  height: number
  colorspace: string
  has_alpha: boolean
  original_ext: string
  pages: number[]
  chapters: string[]
  role_guess: string
}
interface BookData {
  generatedAt: string
  totalPages: number
  chapters: ChapterIndex[]
  toc: TocEntry[]
  pages: BookPage[]
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

// ── Helpers ───────────────────────────────────────────────────────────────────

/** Convert an MDAST node subtree to plain text without losing word boundaries. */
function rawText(node: Node): string {
  let text = ''
  if ('value' in node && typeof (node as { value?: unknown }).value === 'string') {
    text += (node as { value: string }).value
  }
  if ('children' in node) {
    for (const child of (node as { children: Node[] }).children) {
      text += rawText(child)
    }
  }
  return text
}

function toText(node: Node): string {
  return rawText(node).trim()
}

function countWords(value: string): number {
  return value.match(/\S+/gu)?.length ?? 0
}

interface NodeSplit {
  head?: Node
  tail?: Node
}

/**
 * Split a phrasing-content subtree after a word limit while cloning its
 * ancestors on both sides. This preserves strong/emphasis/link markup in both
 * paragraph fragments instead of flattening continuation text to plain text.
 */
function splitNodeAtWordLimit(node: Node, wordLimit: number): NodeSplit {
  const nodeWords = countWords(rawText(node))
  if (nodeWords === 0) return { head: { ...node } }
  if (nodeWords <= wordLimit) return { head: { ...node } }
  if (wordLimit <= 0) return { tail: { ...node } }

  const structured = node as Node & { children?: Node[]; value?: unknown }
  if (Array.isArray(structured.children)) {
    const headChildren: Node[] = []
    const tailChildren: Node[] = []
    let remainingWords = wordLimit
    let tailStarted = false

    for (const child of structured.children) {
      const childWords = countWords(rawText(child))
      if (tailStarted) {
        tailChildren.push({ ...child })
        continue
      }
      if (childWords === 0) {
        headChildren.push({ ...child })
        continue
      }
      if (childWords <= remainingWords) {
        headChildren.push({ ...child })
        remainingWords -= childWords
        continue
      }

      const splitChild = splitNodeAtWordLimit(child, remainingWords)
      if (splitChild.head) headChildren.push(splitChild.head)
      if (splitChild.tail) tailChildren.push(splitChild.tail)
      tailStarted = true
    }

    const cloneWithChildren = (children: Node[]) =>
      ({ ...node, children } as unknown as Node)
    return {
      head: headChildren.length > 0 ? cloneWithChildren(headChildren) : undefined,
      tail: tailChildren.length > 0 ? cloneWithChildren(tailChildren) : undefined,
    }
  }

  if (typeof structured.value === 'string') {
    const matches = [...structured.value.matchAll(/\S+/gu)]
    const lastHeadWord = matches[wordLimit - 1]
    if (!lastHeadWord || lastHeadWord.index === undefined) {
      return { tail: { ...node } }
    }
    const boundary = lastHeadWord.index + lastHeadWord[0].length
    const headValue = structured.value.slice(0, boundary).trimEnd()
    const tailValue = structured.value.slice(boundary).trimStart()
    return {
      head: headValue ? ({ ...node, value: headValue } as Node) : undefined,
      tail: tailValue ? ({ ...node, value: tailValue } as Node) : undefined,
    }
  }

  // Atomic inline nodes (for example images) cannot be divided safely.
  return { tail: { ...node } }
}

function splitParagraphSegment(
  segment: ParagraphSegment,
  maxHeadLines: number,
): { head: ParagraphSegment; tail: ParagraphSegment } | null {
  if (!segment.sourceNode || segment.isListSegment || segment.isFiction) return null
  if (isDiamondMetadataText(toText(segment.sourceNode))) return null
  if (maxHeadLines < MIN_SPLIT_LINES) return null

  const totalWords = countWords(toText(segment.sourceNode))
  if (totalWords < 2) return null

  // Find the furthest word boundary that fits the legal line count. This
  // mirrors greedy browser wrapping and fills the last line instead of
  // assuming that every line contains a fixed number of words.
  let low = 1
  let high = totalWords - 1
  let targetHeadWords = 0
  while (low <= high) {
    const candidateWords = Math.floor((low + high) / 2)
    const candidate = splitNodeAtWordLimit(segment.sourceNode, candidateWords)
    if (!candidate.head || !candidate.tail) {
      high = candidateWords - 1
      continue
    }
    const candidateLines = estimateWrappedLines(toText(candidate.head))
    if (candidateLines <= maxHeadLines) {
      targetHeadWords = candidateWords
      low = candidateWords + 1
    } else {
      high = candidateWords - 1
    }
  }
  if (targetHeadWords === 0) return null

  const split = splitNodeAtWordLimit(segment.sourceNode, targetHeadWords)
  if (!split.head || !split.tail) return null

  const headNode = split.head as MdastParagraph
  const tailNode = split.tail as MdastParagraph
  const headText = toText(headNode)
  const tailText = toText(tailNode)
  if (
    estimateWrappedLines(headText) < MIN_SPLIT_LINES ||
    estimateWrappedLines(tailText) < MIN_SPLIT_LINES
  ) {
    return null
  }

  return {
    head: {
      ...segment,
      html: nodeToHtml(headNode),
      heightPt: paragraphHeightPt(headText),
      sourceNode: headNode,
      continuesOnNext: true,
    },
    tail: {
      ...segment,
      html: nodeToHtml(tailNode),
      heightPt: paragraphHeightPt(tailText),
      sourceNode: tailNode,
      isChapterOpener: false,
      continuesFromPrevious: true,
    },
  }
}

function splitBlockquoteSegment(
  segment: BlockquoteSegment,
  maxHeadLines: number,
): { head: BlockquoteSegment; tail: BlockquoteSegment } | null {
  if (!segment.sourceNode || maxHeadLines < MIN_SPLIT_LINES) return null

  const totalWords = countWords(toText(segment.sourceNode))
  if (totalWords < 2) return null

  let low = 1
  let high = totalWords - 1
  let targetHeadWords = 0
  while (low <= high) {
    const candidateWords = Math.floor((low + high) / 2)
    const candidate = splitNodeAtWordLimit(segment.sourceNode, candidateWords)
    if (!candidate.head || !candidate.tail) {
      high = candidateWords - 1
      continue
    }
    if (
      estimateWrappedLines(toText(candidate.head), BLOCKQUOTE_LINE_WIDTH_EM) <=
      maxHeadLines
    ) {
      targetHeadWords = candidateWords
      low = candidateWords + 1
    } else {
      high = candidateWords - 1
    }
  }
  if (targetHeadWords === 0) return null

  const split = splitNodeAtWordLimit(segment.sourceNode, targetHeadWords)
  if (!split.head || !split.tail) return null
  const headNode = split.head as MdastBlockquote
  const tailNode = split.tail as MdastBlockquote
  const headText = toText(headNode)
  const tailText = toText(tailNode)
  if (
    estimateWrappedLines(headText, BLOCKQUOTE_LINE_WIDTH_EM) < MIN_SPLIT_LINES ||
    countWords(tailText) < 1
  ) {
    return null
  }

  return {
    head: {
      ...segment,
      html: nodeToHtml(headNode),
      heightPt: blockquoteHeightPt(headText),
      sourceNode: headNode,
      continuesOnNext: true,
    },
    tail: {
      ...segment,
      html: nodeToHtml(tailNode),
      heightPt: blockquoteHeightPt(tailText),
      sourceNode: tailNode,
      continuesFromPrevious: true,
    },
  }
}

function splitFictionBlockquoteSegment(
  segment: BlockquoteSegment,
  maxHeadLines: number,
): { head: BlockquoteSegment; tail: BlockquoteSegment } | null {
  if (!segment.sourceNode || maxHeadLines < MIN_SPLIT_LINES) return null
  const totalWords = countWords(toText(segment.sourceNode))
  if (totalWords < 2) return null

  let low = 1
  let high = totalWords - 1
  let targetHeadWords = 0
  while (low <= high) {
    const candidateWords = Math.floor((low + high) / 2)
    const candidate = splitNodeAtWordLimit(segment.sourceNode, candidateWords)
    if (!candidate.head || !candidate.tail) {
      high = candidateWords - 1
      continue
    }
    if (
      estimateWrappedLines(toText(candidate.head), FICTION_LINE_WIDTH_EM) <=
      maxHeadLines
    ) {
      targetHeadWords = candidateWords
      low = candidateWords + 1
    } else {
      high = candidateWords - 1
    }
  }
  if (targetHeadWords === 0) return null

  const split = splitNodeAtWordLimit(segment.sourceNode, targetHeadWords)
  if (!split.head || !split.tail) return null
  const headNode = split.head as MdastBlockquote
  const tailNode = split.tail as MdastBlockquote
  return {
    head: {
      ...segment,
      html: nodeToHtml(headNode),
      heightPt: fictionHeightPt(toText(headNode)),
      sourceNode: headNode,
      spanAll: true,
      isFiction: true,
      continuesOnNext: true,
    },
    tail: {
      ...segment,
      html: nodeToHtml(tailNode),
      heightPt: fictionHeightPt(toText(tailNode)),
      sourceNode: tailNode,
      spanAll: true,
      isFiction: true,
      continuesFromPrevious: true,
    },
  }
}

function glyphWidthEm(character: string): number {
  if (/\s/u.test(character)) return 0.23
  if (/[ilI1|.,:;'`!]/u.test(character)) return 0.24
  if (/[mwMW@%&]/u.test(character)) return 0.71
  if (/[A-Z]/u.test(character)) return 0.54
  if (/[0-9]/u.test(character)) return 0.46
  if ('-–—()[]{}/\\'.includes(character)) return 0.31
  if (/[^\p{L}\p{N}\p{P}\p{Z}]/u.test(character)) return 0.78
  return 0.43
}

function textWidthEm(value: string): number {
  return [...value].reduce((width, character) => width + glyphWidthEm(character), 0)
}

/** Approximate the browser's greedy word wrapping at the rendered font width. */
function estimateWrappedLines(
  value: string,
  lineWidthEm = BODY_LINE_WIDTH_EM,
): number {
  const words = value.trim().split(/\s+/u).filter(Boolean)
  if (words.length === 0) return 1

  const spaceWidth = glyphWidthEm(' ')
  let lines = 1
  let usedWidth = 0
  for (const word of words) {
    let wordWidth = textWidthEm(word)
    const requiredWidth = (usedWidth > 0 ? spaceWidth : 0) + wordWidth
    if (usedWidth + requiredWidth <= lineWidthEm) {
      usedWidth += requiredWidth
      continue
    }
    if (usedWidth > 0) {
      lines++
      usedWidth = 0
    }
    while (wordWidth > lineWidthEm) {
      lines++
      wordWidth -= lineWidthEm
    }
    usedWidth = wordWidth
  }
  return lines
}

/** Estimate reading height of a text string in pt. */
function textHeightPt(str: string, lineWidthEm = BODY_LINE_WIDTH_EM): number {
  const lines = estimateWrappedLines(str, lineWidthEm)
  return lines * LINE_HEIGHT_PT + PARA_MARGIN_PT
}

/** Diamond-prefixed metadata is converted to a visual list at runtime. */
function paragraphHeightPt(str: string): number {
  const lines = str
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .filter(Boolean)
  const diamondLines = lines.filter((line) => /^[✦✧]/u.test(line))
  if (diamondLines.length < 2) return textHeightPt(str)

  const renderedLines = lines.reduce(
    (sum, line) => sum + estimateWrappedLines(line, LIST_LINE_WIDTH_EM),
    0,
  )
  return (
    renderedLines * LINE_HEIGHT_PT +
    diamondLines.length * LIST_ITEM_EXTRA_PT +
    LIST_BLOCK_EXTRA_PT
  )
}

function isDiamondMetadataText(str: string): boolean {
  return str
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .filter((line) => /^[✦✧]/u.test(line)).length >= 2
}

function blockquoteHeightPt(str: string): number {
  return (
    estimateWrappedLines(str, BLOCKQUOTE_LINE_WIDTH_EM) *
      BLOCKQUOTE_LINE_HEIGHT_PT +
    BLOCKQUOTE_DECOR_PT
  )
}

function fictionHeightPt(str: string): number {
  return (
    estimateWrappedLines(str, FICTION_LINE_WIDTH_EM) * FICTION_LINE_HEIGHT_PT +
    FICTION_MARGIN_PT
  )
}

/** Convert a single MDAST node to an HTML string via unified pipeline */
function nodeToHtml(node: Node): string {
  const root: MdastRoot = { type: 'root', children: [node as MdastRoot['children'][0]] }
  // We already have an MDAST tree — use runSync to transform to HAST, then stringify
  const processor = unified()
    .use(remarkRehype, { allowDangerousHtml: false })
    .use(rehypeSanitize)
    .use(rehypeStringify)
  const hast = processor.runSync(root as Parameters<typeof processor.runSync>[0])
  return String(
    processor.stringify(hast as Parameters<typeof processor.stringify>[0]),
  ).trim()
}

const headingHeights: Record<number, number> = { 1: 32, 2: 24, 3: 26, 4: 18 }

// ── Load manifest and index by "chapter" name ─────────────────────────────────
function loadManifest(): Map<string, ManifestEntry[]> {
  if (!existsSync(MANIFEST)) {
    console.warn('[!] image_manifest.json not found — images will be skipped')
    return new Map()
  }
  const raw: ManifestEntry[] = JSON.parse(readFileSync(MANIFEST, 'utf8'))
  const available = raw.filter((entry) => existsSync(join(IMAGES_DIR, entry.filename)))
  if (available.length !== raw.length) {
    console.warn(
      `[!] ${raw.length - available.length} manifest images are unavailable in ${IMAGES_DIR} — skipping them`,
    )
  }
  const map = new Map<string, ManifestEntry[]>()
  for (const entry of available) {
    for (const ch of entry.chapters) {
      if (!map.has(ch)) map.set(ch, [])
      map.get(ch)!.push(entry)
    }
  }
  return map
}

// ── Parse a single markdown file into segments ────────────────────────────────
function parseChapter(
  filePath: string,
  chapterIndex: number,
  imageMap: Map<string, ManifestEntry[]>,
): { title: string; segments: Segment[] } {
  const md = readFileSync(filePath, 'utf8')

  // Full parse
  const tree = unified().use(remarkParse).use(remarkGfm).parse(md)

  let title = CHAPTER_FILES[chapterIndex]
    .replace(/^\d+-/, '')
    .replace(/-/g, ' ')
    .replace('.md', '')
  let firstParagraph = true
  let pendingFiction = false
  let fictionBlock = false
  const segments: Segment[] = []

  // Walk top-level nodes
  for (const node of tree.children) {
    if (node.type === 'html') {
      const raw = (node as { value?: string }).value ?? ''
      if (/<!--\s*FICTION_START\s*-->/i.test(raw)) {
        fictionBlock = true
      }
      if (/<!--\s*FICTION_END\s*-->/i.test(raw)) {
        fictionBlock = false
      }
      if (/<!--\s*FICTION\s*-->/i.test(raw)) {
        pendingFiction = true
      }
      continue
    }

    if (node.type === 'heading') {
      const h = node as Heading
      const text = toText(h)
      if (segments.length === 0) title = text
      // Front-matter title is assumed/known in the reader UI and should not
      // consume layout space on pages 1-2.
      if (chapterIndex === 0 && h.depth === 1) {
        continue
      }
      segments.push({
        type: 'heading',
        level: Math.min(h.depth, 4) as 1 | 2 | 3 | 4,
        text,
        heightPt: headingHeights[Math.min(h.depth, 4)] ?? 16,
        id: text.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
      })
    } else if (node.type === 'paragraph') {
      const html = nodeToHtml(node)
      const text = toText(node)
      const isChapterOpener = firstParagraph && chapterIndex > 0
      const isFiction = fictionBlock || pendingFiction
      firstParagraph = false
      pendingFiction = false
      segments.push({
        type: 'paragraph',
        html,
        sourceNode: node as MdastParagraph,
        isChapterOpener,
        isFiction,
        heightPt: paragraphHeightPt(text),
      })
    } else if (node.type === 'blockquote') {
      const html = nodeToHtml(node)
      const text = toText(node)
      segments.push({
        type: 'blockquote',
        html,
        sourceNode: node as MdastBlockquote,
        heightPt: blockquoteHeightPt(text),
      })
    } else if (node.type === 'table') {
      const t = node as Table
      const rows: string[][] = []
      for (const row of t.children as TableRow[]) {
        rows.push(row.children.map((cell) => toText(cell)))
      }
      const headers = rows.shift() ?? []
      segments.push(chooseTableLayout(headers, rows))
    } else if (node.type === 'thematicBreak') {
      segments.push({ type: 'hr', heightPt: 8 })
    }
    // list nodes: convert to HTML paragraph (with per-item metadata for split logic)
    else if (node.type === 'list') {
      const listNode = node as List
      const html = nodeToHtml(node)
      const itemLiHtmls: string[] = []
      const itemHeights: number[] = []
      for (const item of listNode.children as ListItem[]) {
        // Wrap in single-item list to get valid HTML, then extract the <li> tag
        const wrapper: List = {
          type: 'list',
          ordered: listNode.ordered ?? false,
          spread: listNode.spread ?? false,
          children: [item],
        }
        const wrapHtml = nodeToHtml(wrapper)
        const liMatch = wrapHtml.match(/(<li[\s>][\s\S]*<\/li>)/i)
        itemLiHtmls.push(liMatch ? liMatch[1] : '')
        const itemHtml = itemLiHtmls.at(-1) ?? ''
        const hasNestedList = /<(?:ul|ol)[\s>]/iu.test(itemHtml)
        const itemLineWidth = hasNestedList
          ? LIST_LINE_WIDTH_EM - 1.5
          : LIST_LINE_WIDTH_EM
        const nestedListReservePt = hasNestedList ? 8 : 0
        itemHeights.push(
          textHeightPt(toText(item), itemLineWidth) +
            LIST_ITEM_EXTRA_PT +
            nestedListReservePt,
        )
      }
      const totalHeight = estimateListBlockHeight(itemHeights)
      segments.push({
        type: 'paragraph',
        html,
        isListSegment: true,
        itemLiHtmls,
        itemHeights,
        listTag: listNode.ordered ? 'ol' : 'ul',
        heightPt: totalHeight,
      })
    }
  }

  // Inject chapter art images after the chapter title (first h1)
  const chapterImages = imageMap.get(title) ?? []
  const artImages = chapterImages.filter(
    (e) =>
      e.role_guess === 'full-page-art' || e.role_guess === 'chapter-art/illustration',
  )
  if (artImages.length > 0) {
    // Insert after first heading
    const headingIdx = segments.findIndex(
      (s) => s.type === 'heading' && (s as HeadingSegment).level === 1,
    )
    const insertAt = headingIdx >= 0 ? headingIdx + 1 : 0
    const img = artImages[0]
    const maxWidthPt = 160 // fit in one column
    const ratio = img.height / Math.max(img.width, 1)
    const heightPt = Math.min(maxWidthPt * ratio, 200)
    segments.splice(insertAt, 0, {
      type: 'image-ref',
      filename: img.filename,
      width: img.width,
      height: img.height,
      altText: `${title} — chapter art`,
      heightPt,
    })
  }

  // Keep source paragraph boundaries exactly as-authored in corebook/*.md.
  return { title, segments }
}

// ── Paginator ─────────────────────────────────────────────────────────────────
function paginate(chapters: { title: string; index: number; segments: Segment[] }[]): {
  pages: BookPage[]
  chapterIndex: ChapterIndex[]
} {
  const pages: BookPage[] = []
  const chapterIndexOut: ChapterIndex[] = []

  let pageNumber = 1
  let colFill = 0 // pt filled in current column
  let colNum = 0 // 0 = left, 1 = right
  let pageSpanReservePt = 0
  let currentPage: BookPage = newPage(pageNumber, chapters[0].title, 0)

  function flush() {
    if (currentPage.segments.length > 0 || pageNumber === 1) {
      pages.push(currentPage)
    }
    pageNumber++
    colFill = 0
    colNum = 0
    pageSpanReservePt = 0
  }

  function nextColumn() {
    if (colNum === 0) {
      currentPage.segments.push({
        type: 'hr',
        heightPt: 0,
        id: '__column_break__',
      })
      colNum = 1
      colFill = 0
    } else {
      flush()
    }
  }

  function pageHasColumnContent(segments: Segment[]): boolean {
    let index = 0
    while (index < segments.length) {
      const segment = segments[index]
      if (segment.type === 'heading' && segment.level === 2) {
        index++
        if (segments[index]?.type === 'blockquote') index++
        continue
      }
      if (
        (segment.type === 'heading' &&
          (segment.level === 1 || !!segment.spanAll)) ||
        (segment.type === 'table' && !!segment.spanAll) ||
        (segment.type === 'paragraph' && !!segment.isFiction)
      ) {
        index++
        continue
      }
      break
    }
    return index < segments.length
  }

  function addSegment(seg: Segment, chTitle: string, chIdx: number, nextSeg?: Segment) {
    const segGuardPt = segmentGuardPt(seg)
    const segBudgetPt = seg.heightPt + segGuardPt

    // Ensure current page matches the chapter
    if (currentPage.chapterTitle !== chTitle && currentPage.segments.length > 0) {
      flush()
      currentPage = newPage(pageNumber, chTitle, chIdx)
    } else if (currentPage.chapterTitle !== chTitle) {
      currentPage.chapterTitle = chTitle
      currentPage.chapterIndex = chIdx
    }

    // Wide tables use the page-width span stack. Consecutive tables can share
    // a page when their measured fragments fit; otherwise rows continue on a
    // fresh page with their header repeated. An individually oversized row is
    // split by cell text so no table fragment can cross the legal footer line.
    if (seg.type === 'table' && (seg as TableSegment).spanAll) {
      const table = seg as TableSegment
      const carriedHeadings: HeadingSegment[] = []
      while (currentPage.segments.at(-1)?.type === 'heading') {
        const heading = currentPage.segments.pop() as HeadingSegment
        colFill = Math.max(0, colFill - heading.heightPt - segmentGuardPt(heading))
        carriedHeadings.unshift({
          ...heading,
          spanAll: heading.level > 2 ? true : heading.spanAll,
        })
      }
      if (currentPage.segments.at(-1)?.id === '__column_break__') {
        currentPage.segments.pop()
        colNum = 0
      }

      const hasColumnContent =
        colFill > 0 || pageHasColumnContent(currentPage.segments)
      if (hasColumnContent) {
        flush()
        currentPage = newPage(pageNumber, chTitle, chIdx)
      }
      colFill = 0
      colNum = 0

      const headingReserve = carriedHeadings.reduce(
        (sum, heading) => sum + heading.heightPt + segmentGuardPt(heading),
        0,
      )
      let availableTableHeight =
        COLUMN_HEIGHT_PT -
        RENDER_SAFETY_PT -
        pageSpanReservePt -
        headingReserve -
        segmentGuardPt(table)

      let fittingRows = tableRowsThatFit(table, availableTableHeight)
      if (
        fittingRows === 0 &&
        (pageSpanReservePt > 0 || currentPage.segments.length > 0)
      ) {
        flush()
        currentPage = newPage(pageNumber, chTitle, chIdx)
        availableTableHeight =
          COLUMN_HEIGHT_PT -
          RENDER_SAFETY_PT -
          headingReserve -
          segmentGuardPt(table)
        fittingRows = tableRowsThatFit(table, availableTableHeight)
      }

      let head: TableSegment
      let tail: TableSegment | null = null
      if (table.rows.length === 0 && table.heightPt <= availableTableHeight) {
        head = table
      } else if (fittingRows > 0) {
        const splitAt = Math.min(table.rows.length, fittingRows)
        head = tableFragment(table, 0, splitAt)
        if (splitAt < table.rows.length) {
          head.continuesOnNext = true
          tail = tableFragment(table, splitAt, table.rows.length)
          tail.continuesFromPrevious = true
        }
      } else {
        const oversizedSplit = splitOversizedFirstTableRow(
          table,
          availableTableHeight,
        )
        if (!oversizedSplit) {
          throw new Error(
            `Unable to fit table header and one content line on page ${pageNumber}`,
          )
        }
        head = oversizedSplit.head
        tail = oversizedSplit.tail
      }

      currentPage.segments.push(...carriedHeadings, head)
      pageSpanReservePt += headingReserve + head.heightPt + segmentGuardPt(head)
      colFill = 0
      colNum = 0

      if (tail) {
        flush()
        currentPage = newPage(pageNumber, chTitle, chIdx)
        addSegment(tail, chTitle, chIdx, nextSeg)
      }
      return
    }

    // Rule: every ## section heading starts on a new page.
    if (seg.type === 'heading' && (seg as HeadingSegment).level === 2) {
      if (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0) {
        flush()
        currentPage = newPage(pageNumber, chTitle, chIdx)
      }
      colFill = 0
      colNum = 0
      pageSpanReservePt = SECTION_HEADING_RESERVE_PT
      currentPage.segments.push(seg)
      return
    }

    // Fiction immediately following an H2 spans both columns. Long fiction is
    // split across pages at legal word boundaries using its larger rendered
    // font and full-width measure.
    const previousSegment = currentPage.segments.at(-1)
    if (
      seg.type === 'blockquote' &&
      ((previousSegment?.type === 'heading' &&
        (previousSegment as HeadingSegment).level === 2) ||
        (seg as BlockquoteSegment).isFiction)
    ) {
      const fiction = {
        ...(seg as BlockquoteSegment),
        spanAll: true,
        isFiction: true,
      }
      fiction.heightPt = Math.max(
        SECTION_FICTION_MIN_RESERVE_PT,
        fiction.sourceNode
          ? fictionHeightPt(toText(fiction.sourceNode))
          : fiction.heightPt,
      )
      const availableHeight =
        COLUMN_HEIGHT_PT - RENDER_SAFETY_PT - pageSpanReservePt
      if (fiction.heightPt > availableHeight) {
        const maxHeadLines = Math.floor(
          (availableHeight - FICTION_MARGIN_PT) / FICTION_LINE_HEIGHT_PT,
        )
        const split = splitFictionBlockquoteSegment(fiction, maxHeadLines)
        if (split) {
          currentPage.segments.push(split.head)
          pageSpanReservePt += split.head.heightPt
          flush()
          currentPage = newPage(pageNumber, chTitle, chIdx)
          addSegment(split.tail, chTitle, chIdx, nextSeg)
          return
        }
      }
      pageSpanReservePt += fiction.heightPt
      currentPage.segments.push(fiction)
      return
    }

    // Front-matter layout rule:
    // Keep CREDITS on page 1 and start the marked intro fiction on a new page.
    if (
      chIdx === 0 &&
      seg.type === 'paragraph' &&
      !!(seg as ParagraphSegment).isFiction
    ) {
      const pageAlreadyHasFiction = currentPage.segments.some(
        (s) => s.type === 'paragraph' && !!(s as ParagraphSegment).isFiction,
      )
      if (
        !pageAlreadyHasFiction &&
        (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0)
      ) {
        flush()
        currentPage = newPage(pageNumber, chTitle, chIdx)
        colFill = 0
        colNum = 0
      }
    }

    // Front-matter layout rule:
    // Keep all intro fiction on page 2 and start "FORBIDDEN LANDS" on page 3.
    if (
      chIdx === 0 &&
      seg.type === 'heading' &&
      (seg as HeadingSegment).level === 3 &&
      (seg as HeadingSegment).text === 'FORBIDDEN LANDS' &&
      (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0)
    ) {
      flush()
      currentPage = newPage(pageNumber, chTitle, chIdx)
      colFill = 0
      colNum = 0
    }

    // Page 1 has a curated credits spread rather than a height-driven split.
    // Keep the production credits in the left column and begin the artwork
    // credits in the right column, matching the intended two-column design.
    if (
      chIdx === 0 &&
      pageNumber === 1 &&
      colNum === 0 &&
      seg.type === 'heading' &&
      (seg as HeadingSegment).level === 3 &&
      (seg as HeadingSegment).text === 'ILLUSTRATIONS & GRAPHICS'
    ) {
      nextColumn()
    }

    // Calculate capacity only after any chapter/front-matter transition above,
    // since those transitions can reset the page-wide H2/fiction reserve.
    const isCuratedCreditsLeftColumn =
      chIdx === 0 && pageNumber === 1 && colNum === 0
    const measuredColumnHeight = Math.max(
      0,
      COLUMN_HEIGHT_PT -
        RENDER_SAFETY_PT -
        (isCuratedCreditsLeftColumn ? 0 : pageSpanReservePt),
    )
    const effectiveColumnHeight =
      pageSpanReservePt > 0 &&
      measuredColumnHeight < TABLE_LAYOUT_POLICY.minUsableColumnAfterSpanPt
        ? 0
        : measuredColumnHeight

    const headingFollowReservationPt =
      seg.type === 'heading'
        ? (() => {
            if (nextSeg?.type === 'paragraph') {
              const paragraph = nextSeg as ParagraphSegment
              if (
                paragraph.isListSegment &&
                paragraph.itemHeights &&
                paragraph.itemHeights.length > 0
              ) {
                return (
                  estimateListBlockHeight(paragraph.itemHeights.slice(0, 2)) +
                  segmentGuardPt(paragraph)
                )
              }
              return Math.min(
                paragraph.heightPt + segmentGuardPt(paragraph),
                MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT,
              )
            }
            if (nextSeg?.type === 'table') {
              const table = nextSeg as TableSegment
              const preview = tableFragment(table, 0, Math.min(2, table.rows.length))
              return preview.heightPt + segmentGuardPt(preview)
            }
            return MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT
          })()
        : 0

    // Heading + first-paragraph attempt: if near boundary, keep heading only
    // when we can also keep a meaningful portion of the following paragraph.
    if (
      seg.type === 'heading' &&
      (seg as HeadingSegment).level === 3 &&
      colNum === 1 &&
      colFill > 0 &&
      colFill + segBudgetPt + headingFollowReservationPt > effectiveColumnHeight - 8
    ) {
      flush()
      currentPage = newPage(pageNumber, chTitle, chIdx)
      colFill = 0
      colNum = 0
    }

    // Every heading must retain two lines of its first paragraph, or the first
    // two items when its first text block is a list.
    const headingNextReservationPt =
      seg.type === 'heading' ? headingFollowReservationPt : 0

    const headingNeedsNextColumn =
      seg.type === 'heading' &&
      colFill + segBudgetPt + headingNextReservationPt > effectiveColumnHeight

    const willOverflow =
      colFill + segBudgetPt > effectiveColumnHeight || headingNeedsNextColumn

    if (willOverflow) {
      if (seg.type === 'table') {
        const table = seg as TableSegment
        const availableTableHeight = effectiveColumnHeight - colFill - segGuardPt
        const fittingRows = tableRowsThatFit(table, availableTableHeight)
        const precedingSegment = currentPage.segments.at(-1)
        const requiredRows =
          precedingSegment?.type === 'heading'
            ? TABLE_LAYOUT_POLICY.minRowsAfterHeading
            : 1
        if (
          fittingRows >= Math.min(requiredRows, table.rows.length) &&
          fittingRows < table.rows.length
        ) {
          const head = tableFragment(table, 0, fittingRows)
          head.continuesOnNext = true
          currentPage.segments.push(head)
          colFill += head.heightPt + segmentGuardPt(head)

          const tail = tableFragment(table, fittingRows, table.rows.length)
          tail.continuesFromPrevious = true
          nextColumn()
          if (colNum === 0 && colFill === 0) {
            currentPage = newPage(pageNumber, chTitle, chIdx)
          }
          addSegment(tail, chTitle, chIdx, nextSeg)
          return
        }

        // If even the first measured row cannot fit in a completely fresh
        // column, the table is intrinsically a page-width object. Re-layout it
        // at the wider measure, then let the span paginator split rows/cells.
        if (
          fittingRows === 0 &&
          colFill === 0 &&
          pageSpanReservePt === 0 &&
          !table.spanAll
        ) {
          const promoted = layoutTable(table, true, 'runtime-overflow')
          addSegment(promoted, chTitle, chIdx, nextSeg)
          return
        }
      }

      // Paragraph continuation logic:
      // - left column: allow paragraph to continue into right column if both sides
      //   can hold at least 2 lines.
      // - right column: split paragraph so tail continues on next page, again with
      //   at least 2 lines on each side.
      if (seg.type === 'paragraph') {
        const pSeg = seg as ParagraphSegment

        // ── List segment: split by item count (≥2 items per column) ──────────
        if (pSeg.isListSegment && pSeg.itemLiHtmls && pSeg.itemHeights) {
          const liHtmls = pSeg.itemLiHtmls
          const heights = pSeg.itemHeights
          const listGuardPt = segmentGuardPt(pSeg)
          // Count how many top-level items fit in the remaining column space
          let cumHeight = 0
          let splitAt = 0
          for (let k = 0; k < heights.length; k++) {
            const headWithItemHeight = cumHeight + heights[k] + LIST_BLOCK_EXTRA_PT
            if (colFill + headWithItemHeight + listGuardPt > effectiveColumnHeight) break
            cumHeight += heights[k]
            splitAt = k + 1
          }
          const remaining = liHtmls.length - splitAt
          const previousFlowSegment = currentPage.segments.at(-1)
          const requiredHeadItems = previousFlowSegment?.type === 'heading' ? 2 : 1
          if (splitAt >= Math.min(requiredHeadItems, liHtmls.length) && remaining >= 1) {
            // Commit head to current column
            const listTag = pSeg.listTag ?? 'ul'
            const headHtml = `<${listTag}>\n${liHtmls.slice(0, splitAt).join('\n')}\n</${listTag}>`
            const head: ParagraphSegment = {
              ...pSeg,
              html: headHtml,
              itemLiHtmls: liHtmls.slice(0, splitAt),
              itemHeights: heights.slice(0, splitAt),
              heightPt: estimateListBlockHeight(heights.slice(0, splitAt)),
              continuesOnNext: true,
            }
            currentPage.segments.push(head)
            colFill += head.heightPt + segmentGuardPt(head)
            // Push tail to next column/page
            const tailHtml = `<${listTag}>\n${liHtmls.slice(splitAt).join('\n')}\n</${listTag}>`
            const tailHeight = estimateListBlockHeight(heights.slice(splitAt))
            const tail: ParagraphSegment = {
              ...pSeg,
              html: tailHtml,
              itemLiHtmls: liHtmls.slice(splitAt),
              itemHeights: heights.slice(splitAt),
              heightPt: tailHeight,
              isChapterOpener: false,
              continuesFromPrevious: true,
            }
            nextColumn()
            if (colNum === 0 && colFill === 0) {
              currentPage = newPage(pageNumber, chTitle, chIdx)
            }
            addSegment(tail, chTitle, chIdx)
            return
          }
          // Not enough items fit — fall through to normal overflow (move whole list)
        }

        const availableTextHeight =
          effectiveColumnHeight - colFill - segGuardPt - PARA_MARGIN_PT
        const maxHeadLines = Math.floor(
          availableTextHeight / BLOCKQUOTE_LINE_HEIGHT_PT,
        )
        const paragraphSplit = splitParagraphSegment(pSeg, maxHeadLines)
        if (paragraphSplit) {
          currentPage.segments.push(paragraphSplit.head)
          colFill +=
            paragraphSplit.head.heightPt + segmentGuardPt(paragraphSplit.head)
          nextColumn()
          if (colNum === 0 && colFill === 0) {
            currentPage = newPage(pageNumber, chTitle, chIdx)
          }
          addSegment(paragraphSplit.tail, chTitle, chIdx)
          return
        }

        // If conservative word/markup constraints make the required preview
        // unsplittable, carry the heading forward with the paragraph instead
        // of leaving the heading orphaned at the boundary.
        const precedingSegment = currentPage.segments.at(-1)
        if (precedingSegment?.type === 'heading') {
          currentPage.segments.pop()
          colFill -= precedingSegment.heightPt + segmentGuardPt(precedingSegment)
          nextColumn()
          if (colNum === 0 && colFill === 0) {
            currentPage = newPage(pageNumber, chTitle, chIdx)
          }
          currentPage.segments.push(precedingSegment)
          colFill = precedingSegment.heightPt + segmentGuardPt(precedingSegment)
          addSegment(seg, chTitle, chIdx, nextSeg)
          return
        }
      }

      // Framed examples and GM notes can be longer than a column. Split their
      // source tree at a word boundary while charging each fragment for its
      // repeated decorative frame.
      if (seg.type === 'blockquote') {
        const blockquote = seg as BlockquoteSegment
        const availableTextHeight =
          effectiveColumnHeight -
          colFill -
          segGuardPt -
          BLOCKQUOTE_DECOR_PT
        const maxHeadLines = Math.floor(availableTextHeight / LINE_HEIGHT_PT)
        const blockquoteSplit = splitBlockquoteSegment(blockquote, maxHeadLines)
        if (blockquoteSplit) {
          currentPage.segments.push(blockquoteSplit.head)
          colFill +=
            blockquoteSplit.head.heightPt + segmentGuardPt(blockquoteSplit.head)
          nextColumn()
          if (colNum === 0 && colFill === 0) {
            currentPage = newPage(pageNumber, chTitle, chIdx)
          }
          addSegment(blockquoteSplit.tail, chTitle, chIdx, nextSeg)
          return
        }
      }

      if (seg.type === 'heading') {
        // Move heading to next column/page so it stays with content.
        // IMPORTANT: never replace currentPage unless a new page was actually
        // started by nextColumn(); otherwise we'd drop already-added segments.
        if (colFill === 0 && pageSpanReservePt > 0) {
          flush()
        } else {
          nextColumn()
        }
        if (colNum === 0 && colFill === 0) {
          // Started new page via flush
          currentPage = newPage(pageNumber, chTitle, chIdx)
        }
      } else {
        const retryInFreshColumn = colFill > 0
        if (colFill === 0 && pageSpanReservePt > 0) {
          flush()
        } else {
          nextColumn()
        }
        if (colNum === 0 && colFill === 0) {
          // Started new page
          currentPage = newPage(pageNumber, chTitle, chIdx)
        }
        if (retryInFreshColumn) {
          addSegment(seg, chTitle, chIdx, nextSeg)
          return
        }
      }
      colFill = 0
    }

    currentPage.segments.push(seg)
    colFill += segBudgetPt
  }

  for (const ch of chapters) {
    // Record chapter start page
    const chStart = currentPage.segments.length > 0 ? pageNumber + 1 : pageNumber

    for (let i = 0; i < ch.segments.length; i++) {
      const seg = ch.segments[i]
      addSegment(seg, ch.title, ch.index, ch.segments[i + 1])
    }

    // Chapter just ended — where is current page?
    chapterIndexOut.push({
      chapterTitle: ch.title,
      chapterIndex: ch.index,
      firstPage: chStart,
      lastPage: pageNumber,
    })
  }

  // Flush final page
  if (currentPage.segments.length > 0) pages.push(currentPage)

  return { pages, chapterIndex: chapterIndexOut }
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

// ── Main ──────────────────────────────────────────────────────────────────────
function main() {
  console.log('[…] Forbidden Lands — content pre-processor')

  const missingChapters = CHAPTER_FILES.filter(
    (chapterFile) => !existsSync(join(COREBOOK_DIR, chapterFile)),
  )
  if (missingChapters.length > 0) {
    throw new Error(
      `Missing required corebook chapters in ${COREBOOK_DIR}: ${missingChapters.join(', ')}`,
    )
  }

  const imageMap = loadManifest()
  console.log(`[…] Image manifest: ${imageMap.size} chapters with images`)

  const chapters: { title: string; index: number; segments: Segment[] }[] = []

  for (let i = 0; i < CHAPTER_FILES.length; i++) {
    const file = join(COREBOOK_DIR, CHAPTER_FILES[i])
    process.stdout.write(`[…] Parsing ${CHAPTER_FILES[i]} …`)
    const { title, segments } = parseChapter(file, i, imageMap)
    chapters.push({ title, index: i, segments })
    console.log(` ${segments.length} segments`)
  }

  console.log('[…] Paginating …')
  const { pages, chapterIndex } = paginate(chapters)
  if (chapters.length !== CHAPTER_FILES.length || pages.length === 0) {
    throw new Error(
      `Preprocessing produced invalid output: ${chapters.length} chapters and ${pages.length} pages`,
    )
  }

  for (const page of pages) {
    page.segments.forEach((segment, segmentIndex) => {
      if (segment.type === 'paragraph' || segment.type === 'blockquote') {
        delete (segment as ParagraphSegment).sourceNode
      }
      segment.uid = `page-${page.pageNumber}-segment-${segmentIndex}`
    })
  }

  const headingPageMap = buildHeadingPageMap(pages)

  const tocSeed: TocEntry[] = existsSync(TOC_FILE)
    ? JSON.parse(readFileSync(TOC_FILE, 'utf8'))
    : []

  // Keep the curated TOC ordering/titles, but always align pages to where
  // headings actually land after pagination changes.
  const toc: TocEntry[] = tocSeed.map((entry) => {
    const key = normalizeTocKey(entry.title)
    const resolvedPage = headingPageMap.get(key)
    if (!resolvedPage) return entry
    return {
      ...entry,
      page: resolvedPage,
    }
  })

  // The legacy curated TOC predates supplemental corebook chapters. Append
  // any missing chapter-level entries so all required manuscripts are
  // reachable from reader navigation without disturbing curated ordering.
  const tocKeys = new Set(toc.map((entry) => normalizeTocKey(entry.title)))
  for (const chapter of chapterIndex) {
    const key = normalizeTocKey(chapter.chapterTitle)
    if (!key || tocKeys.has(key)) continue
    toc.push({
      level: 1,
      title: chapter.chapterTitle,
      page: chapter.firstPage,
    })
    tocKeys.add(key)
  }

  const bookData: BookData = {
    generatedAt: new Date().toISOString(),
    totalPages: pages.length,
    chapters: chapterIndex,
    toc,
    pages,
  }

  writeFileSync(OUTPUT, JSON.stringify(bookData, null, 2), 'utf8')
  console.log(
    `[✓] book-data.json written — ${pages.length} pages, ${chapters.length} chapters`,
  )
  console.log(`    → ${OUTPUT}`)

  // Summary
  const totalSegments = pages.reduce((n, p) => n + p.segments.length, 0)
  console.log(`[✓] Total segments across all pages: ${totalSegments}`)
  console.log(`[✓] Generated pages: ${pages.length}`)
}

const invokedScript = process.argv[1] ? resolve(process.argv[1]) : ''
if (invokedScript === fileURLToPath(import.meta.url)) {
  main()
}

export {
  COLUMN_HEIGHT_PT,
  RENDER_SAFETY_PT,
  TABLE_LAYOUT_POLICY,
  chooseTableLayout,
  layoutTable,
  splitOversizedFirstTableRow,
  tableRowsThatFit,
}
