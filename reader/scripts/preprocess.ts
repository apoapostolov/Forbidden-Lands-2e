#!/usr/bin/env tsx
/**
 * Forbidden Lands Reader — Content Pre-processor
 *
 * Reads all corebook/*.md files, parses them into segment objects,
 * paginates using estimated heights, and writes src/data/book-data.json.
 *
 * Usage:
 *   npx tsx scripts/preprocess.ts
 *   npm run preprocess
 */

import { existsSync, readFileSync, writeFileSync } from 'fs'
import type {
  Heading,
  Image,
  List,
  ListItem,
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
import { visit } from 'unist-util-visit'
import { fileURLToPath } from 'url'

// ── Paths ─────────────────────────────────────────────────────────────────────
const __dirname = dirname(fileURLToPath(import.meta.url))
const READER_DIR = resolve(__dirname, '..')
const COREBOOK_DIR = resolve(READER_DIR, '..', 'corebook')
const MANIFEST = resolve(READER_DIR, 'src', 'data', 'image_manifest.json')
const TOC_FILE = resolve(READER_DIR, 'src', 'data', 'toc.json')
const OUTPUT = resolve(READER_DIR, 'src', 'data', 'book-data.json')

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
]

// ── Layout constants (pt) ─────────────────────────────────────────────────────
// Matches dev plan: 482 × 680pt page, 50pt h-margins, 60pt v-margins
// IMPORTANT: this must track actual runtime CSS layout, including
// PageHeaderBanner + PageFooter occupancy inside the page content column.
// Previous value (560pt) overestimated available space and could pack trailing
// paragraphs into clipped/non-visible area at page boundaries.
const COLUMN_HEIGHT_PT = 528
// 2 columns per page — used implicitly by the paginator (2 × COLUMN_HEIGHT_PT)
const WORDS_PER_COL_LINE = 8 // balanced safety: allow normal left→right flow
const LINE_HEIGHT_PT = 11.6 // 8pt × 1.45
const PARA_MARGIN_PT = 3 // minimal — CSS segments have near-zero margin
const LIST_WORDS_PER_COL_LINE = 7 // balanced safety for indented bullet lists
const LIST_ITEM_EXTRA_PT = 2 // account for li spacing + marker rendering
const LIST_BLOCK_EXTRA_PT = 6 // account for ul/ol margins and wrap variance
const RENDER_SAFETY_PT = 36 // keep strict reserve without over-fragmenting pages
const MIN_SPLIT_LINES = 1
const MIN_SPLIT_TAIL_LINES_SAME_PAGE = 1
const MIN_SPLIT_TAIL_LINES_NEXT_PAGE = 1
const SPLIT_FIT_SAFETY_PT = 0
const MAX_SPLIT_HEAD_REMAINDER_PT = LINE_HEIGHT_PT * 0.35
const ENABLE_ROUTINE_PARAGRAPH_SPLIT = false
const MIN_SPLIT_HEIGHT_PT = LINE_HEIGHT_PT * MIN_SPLIT_LINES
const MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT = MIN_SPLIT_HEIGHT_PT + PARA_MARGIN_PT
const ENABLE_HEADING_FOLLOW_SPLIT = true
const MIN_H4_FOLLOW_PREVIEW_PT =
  MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT +
  segmentGuardPt({ type: 'paragraph', html: '', heightPt: 0 })

function estimateListBlockHeight(itemHeights: number[]): number {
  return itemHeights.reduce((s, h) => s + h, 0) + LIST_BLOCK_EXTRA_PT
}

// ── Types ─────────────────────────────────────────────────────────────────────
interface BaseSegment {
  type: string
  heightPt: number
  id?: string
}
interface HeadingSegment extends BaseSegment {
  type: 'heading'
  level: 1 | 2 | 3 | 4
  text: string
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
}
interface BlockquoteSegment extends BaseSegment {
  type: 'blockquote'
  html: string
}
interface TableSegment extends BaseSegment {
  type: 'table'
  headers: string[]
  rows: string[][]
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
      return (seg as ParagraphSegment).isListSegment ? 8 : 5
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

/** Convert MDAST node subtree to plain text */
function toText(node: Node): string {
  let text = ''
  if ('value' in node) text += (node as { value: string }).value
  if ('children' in node) {
    for (const child of (node as { children: Node[] }).children) {
      text += toText(child)
    }
  }
  return text.trim()
}

/** Estimate reading height of a text string in pt */
function textHeightPt(str: string, wordsPerLine = WORDS_PER_COL_LINE): number {
  const words = str.split(/\s+/).filter(Boolean).length
  const lines = Math.max(1, Math.ceil(words / wordsPerLine))
  return lines * LINE_HEIGHT_PT + PARA_MARGIN_PT
}

function escapeHtmlText(str: string): string {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

function isSentenceBoundaryWord(word: string): boolean {
  return /[.!?]["')\]]*$/.test(word)
}

function isAwkwardSplitEnding(word: string): boolean {
  const cleaned = word.toLowerCase().replace(/[^a-z]/g, '')
  return new Set([
    'and',
    'or',
    'but',
    'that',
    'which',
    'who',
    'whom',
    'whose',
    'to',
    'of',
    'in',
    'on',
    'at',
    'for',
    'from',
    'with',
    'by',
    'as',
    'if',
    'than',
    'then',
    'a',
    'an',
    'the',
  ]).has(cleaned)
}

/** Convert a single MDAST node to an HTML string via unified pipeline */
function nodeToHtml(node: Node): string {
  const root: MdastRoot = { type: 'root', children: [node as MdastRoot['children'][0]] }
  // We already have an MDAST tree — use runSync to transform to HAST, then stringify
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const processor = unified()
    .use(remarkRehype as any, { allowDangerousHtml: false })
    .use(rehypeSanitize)
    .use(rehypeStringify)
  const hast = processor.runSync(root as Parameters<typeof processor.runSync>[0])
  return String(
    processor.stringify(hast as Parameters<typeof processor.stringify>[0]),
  ).trim()
}

const headingHeights: Record<number, number> = { 1: 28, 2: 24, 3: 14, 4: 11 }

// ── Load manifest and index by "chapter" name ─────────────────────────────────
function loadManifest(): Map<string, ManifestEntry[]> {
  if (!existsSync(MANIFEST)) {
    console.warn('[!] image_manifest.json not found — images will be skipped')
    return new Map()
  }
  const raw: ManifestEntry[] = JSON.parse(readFileSync(MANIFEST, 'utf8'))
  const map = new Map<string, ManifestEntry[]>()
  for (const entry of raw) {
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

  // Inline markdown images are rare in this corpus; they're handled via the
  // manifest injection loop below. The visit call is kept for future use.
  visit(tree, 'image', (node: Image) => {
    void node
  })

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
      if (h.depth === 1 && segments.length === 0) title = text
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
        isChapterOpener,
        isFiction,
        heightPt: textHeightPt(text),
      })
    } else if (node.type === 'blockquote') {
      const html = nodeToHtml(node)
      const text = toText(node)
      segments.push({
        type: 'blockquote',
        html,
        heightPt: textHeightPt(text) + 12,
      })
    } else if (node.type === 'table') {
      const t = node as Table
      const rows: string[][] = []
      for (const row of t.children as TableRow[]) {
        rows.push(row.children.map((cell) => toText(cell)))
      }
      const headers = rows.shift() ?? []
      segments.push({
        type: 'table',
        headers,
        rows,
        heightPt: (rows.length + 1.5) * LINE_HEIGHT_PT + 8,
      })
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
        itemHeights.push(
          textHeightPt(toText(item), LIST_WORDS_PER_COL_LINE) + LIST_ITEM_EXTRA_PT,
        )
      }
      const totalHeight = estimateListBlockHeight(itemHeights)
      segments.push({
        type: 'paragraph',
        html,
        isListSegment: true,
        itemLiHtmls,
        itemHeights,
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
  let currentPage: BookPage = newPage(pageNumber, chapters[0].title, 0)

  function flush() {
    if (currentPage.segments.length > 0 || pageNumber === 1) {
      pages.push(currentPage)
    }
    pageNumber++
    colFill = 0
    colNum = 0
  }

  function nextColumn() {
    if (colNum === 0) {
      colNum = 1
      colFill = 0
    } else {
      flush()
    }
  }

  function stripHtmlText(html: string): string {
    return html
      .replace(/<[^>]+>/g, ' ')
      .replace(/\s+/g, ' ')
      .trim()
  }

  function splitParagraphByAvailableHeight(
    seg: ParagraphSegment,
    availablePt: number,
    minTailLines = MIN_SPLIT_TAIL_LINES_SAME_PAGE,
  ): [ParagraphSegment, ParagraphSegment] | null {
    const totalText = stripHtmlText(seg.html)
    if (!totalText) return null

    const words = totalText.split(/\s+/).filter(Boolean)
    if (words.length < 6) return null

    const totalLines = Math.max(
      1,
      Math.ceil((seg.heightPt - PARA_MARGIN_PT) / LINE_HEIGHT_PT),
    )
    // Do not split short paragraphs; one-line tails/heads look broken.
    if (totalLines <= 3) return null
    const adjustedAvailablePt = Math.max(0, availablePt - SPLIT_FIT_SAFETY_PT)
    const availableLines = Math.floor(
      Math.max(0, adjustedAvailablePt - PARA_MARGIN_PT) / LINE_HEIGHT_PT,
    )

    // Allow split if current column can show at least 2 lines and next
    // column/page can carry at least 1 line of continuation.
    if (availableLines < MIN_SPLIT_LINES) return null
    if (totalLines - availableLines < minTailLines) return null

    let splitIdx = Math.floor((words.length * availableLines) / totalLines)
    if (splitIdx < 3 || words.length - splitIdx < 3) return null

    // Prefer a nearby sentence boundary if it still leaves a meaningful tail.
    // This keeps breaks less jarring while preserving page flow.
    const boundaryLookBack = 14
    const boundaryLookAhead = 8
    let boundaryIdx = -1
    for (let i = splitIdx - 1; i >= Math.max(2, splitIdx - boundaryLookBack); i--) {
      if (isSentenceBoundaryWord(words[i])) {
        boundaryIdx = i + 1
        break
      }
    }
    if (boundaryIdx < 0) {
      for (
        let i = splitIdx;
        i < Math.min(words.length - 3, splitIdx + boundaryLookAhead);
        i++
      ) {
        if (isSentenceBoundaryWord(words[i])) {
          boundaryIdx = i + 1
          break
        }
      }
    }
    if (boundaryIdx >= 3 && words.length - boundaryIdx >= 8) {
      const tailWordCount = words.length - boundaryIdx
      if (tailWordCount <= 16) {
        splitIdx = boundaryIdx
      }
    }

    // Back off split point until the head truly fits the remaining space.
    // This avoids visual spill under footer/header caused by rough word/line
    // estimation when line lengths vary.
    let headText = words.slice(0, splitIdx).join(' ').trim()
    let tailText = words.slice(splitIdx).join(' ').trim()
    while (splitIdx >= 3) {
      const headHeight = textHeightPt(headText)
      const headRemainderPt = adjustedAvailablePt - headHeight
      const tailLines = Math.max(
        1,
        Math.ceil((textHeightPt(tailText) - PARA_MARGIN_PT) / LINE_HEIGHT_PT),
      )
      if (
        headHeight <= adjustedAvailablePt &&
        tailLines >= minTailLines &&
        headRemainderPt <= MAX_SPLIT_HEAD_REMAINDER_PT
      ) {
        const endingWord = words[splitIdx - 1] ?? ''
        if (isAwkwardSplitEnding(endingWord) && splitIdx - 1 >= 3) {
          splitIdx -= 1
          if (splitIdx < 3 || words.length - splitIdx < 3) return null
          headText = words.slice(0, splitIdx).join(' ').trim()
          tailText = words.slice(splitIdx).join(' ').trim()
          continue
        }
        break
      }
      splitIdx -= 1
      if (splitIdx < 3 || words.length - splitIdx < 3) return null
      headText = words.slice(0, splitIdx).join(' ').trim()
      tailText = words.slice(splitIdx).join(' ').trim()
    }
    if (!headText || !tailText) return null
    if (tailText.split(/\s+/).filter(Boolean).length < 6) return null

    const head: ParagraphSegment = {
      ...seg,
      html: `<p>${escapeHtmlText(headText)}</p>`,
      heightPt: textHeightPt(headText),
    }
    const tail: ParagraphSegment = {
      ...seg,
      html: `<p>${escapeHtmlText(tailText)}</p>`,
      heightPt: textHeightPt(tailText),
      isChapterOpener: false,
    }
    return [head, tail]
  }

  function addSegment(seg: Segment, chTitle: string, chIdx: number, nextSeg?: Segment) {
    const effectiveColumnHeight = Math.max(0, COLUMN_HEIGHT_PT - RENDER_SAFETY_PT)
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

    // Rule: every ## section heading starts on a new page.
    if (seg.type === 'heading' && (seg as HeadingSegment).level === 2) {
      if (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0) {
        flush()
        currentPage = newPage(pageNumber, chTitle, chIdx)
      }
      colFill = 0
      colNum = 0
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

    const headingFollowReservationPt =
      seg.type === 'heading'
        ? nextSeg?.type === 'paragraph'
          ? Math.max(
              MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT,
              Math.min((nextSeg as ParagraphSegment).heightPt * 0.4, 64),
            )
          : MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT
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

    // Headings: reserve just enough room for one line of body text below.
    // No aggressive reservation — fill space first, fix orphans later.
    const headingNextReservationPt =
      seg.type === 'heading'
        ? (seg as HeadingSegment).level === 4
          ? nextSeg?.type === 'paragraph'
            ? MIN_H4_FOLLOW_PREVIEW_PT
            : MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT
          : headingFollowReservationPt
        : 0

    const headingNeedsNextColumn =
      seg.type === 'heading' &&
      colFill + segBudgetPt + headingNextReservationPt > effectiveColumnHeight

    const willOverflow =
      colFill + segBudgetPt > effectiveColumnHeight || headingNeedsNextColumn

    if (willOverflow) {
      const availablePt = effectiveColumnHeight - colFill - segGuardPt

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
          if (splitAt >= 2 && remaining >= 1) {
            // Commit head to current column
            const headHtml = `<ul>\n${liHtmls.slice(0, splitAt).join('\n')}\n</ul>`
            const head: ParagraphSegment = {
              ...pSeg,
              html: headHtml,
              itemLiHtmls: liHtmls.slice(0, splitAt),
              itemHeights: heights.slice(0, splitAt),
              heightPt: estimateListBlockHeight(heights.slice(0, splitAt)),
            }
            currentPage.segments.push(head)
            colFill += head.heightPt
            // Push tail to next column/page
            const tailHtml = `<ul>\n${liHtmls.slice(splitAt).join('\n')}\n</ul>`
            const tailHeight = estimateListBlockHeight(heights.slice(splitAt))
            const tail: ParagraphSegment = {
              ...pSeg,
              html: tailHtml,
              itemLiHtmls: liHtmls.slice(splitAt),
              itemHeights: heights.slice(splitAt),
              heightPt: tailHeight,
              isChapterOpener: false,
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

        // ── Regular paragraph: text-level word split ──────────────────────────
        const prevSeg =
          currentPage.segments.length > 0
            ? currentPage.segments[currentPage.segments.length - 1]
            : null
        const followsHeading = prevSeg?.type === 'heading'
        const canSplitParagraph =
          !pSeg.isListSegment &&
          (ENABLE_ROUTINE_PARAGRAPH_SPLIT ||
            (ENABLE_HEADING_FOLLOW_SPLIT && followsHeading))

        if (canSplitParagraph) {
          if (colNum === 0) {
            const split = splitParagraphByAvailableHeight(
              pSeg,
              availablePt,
              MIN_SPLIT_TAIL_LINES_SAME_PAGE,
            )
            if (split) {
              const [head, tail] = split
              currentPage.segments.push(head)
              nextColumn()
              addSegment(tail, chTitle, chIdx)
              return
            }
          }

          if (colNum === 1) {
            const split = splitParagraphByAvailableHeight(
              pSeg,
              availablePt,
              MIN_SPLIT_TAIL_LINES_NEXT_PAGE,
            )
            if (split) {
              const [head, tail] = split
              currentPage.segments.push(head)
              flush()
              currentPage = newPage(pageNumber, chTitle, chIdx)
              colFill = 0
              colNum = 0
              addSegment(tail, chTitle, chIdx)
              return
            }
          }
        }
      }

      if (seg.type === 'heading') {
        // Move heading to next column/page so it stays with content.
        // IMPORTANT: never replace currentPage unless a new page was actually
        // started by nextColumn(); otherwise we'd drop already-added segments.
        nextColumn()
        if (colNum === 0 && colFill === 0) {
          // Started new page via flush
          currentPage = newPage(pageNumber, chTitle, chIdx)
        }
      } else {
        nextColumn()
        if (colNum === 0 && colFill === 0) {
          // Started new page
          currentPage = newPage(pageNumber, chTitle, chIdx)
        }
      }
      colFill = 0
    }

    currentPage.segments.push(seg)
    colFill += seg.heightPt
  }

  for (const ch of chapters) {
    // Record chapter start page
    const startPage =
      colFill === 0 && colNum === 0 ? pageNumber : pageNumber + (colNum === 1 ? 1 : 0)
    let chStart = startPage

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

  const imageMap = loadManifest()
  console.log(`[…] Image manifest: ${imageMap.size} chapters with images`)

  const chapters: { title: string; index: number; segments: Segment[] }[] = []

  for (let i = 0; i < CHAPTER_FILES.length; i++) {
    const file = join(COREBOOK_DIR, CHAPTER_FILES[i])
    if (!existsSync(file)) {
      console.warn(`[!] Missing: ${file} — skipping`)
      continue
    }
    process.stdout.write(`[…] Parsing ${CHAPTER_FILES[i]} …`)
    const { title, segments } = parseChapter(file, i, imageMap)
    chapters.push({ title, index: i, segments })
    console.log(` ${segments.length} segments`)
  }

  console.log('[…] Paginating …')
  const { pages, chapterIndex } = paginate(chapters)

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
  console.log(`[✓] Expected pages (plan): 180–220. Got: ${pages.length}`)
}

main()
