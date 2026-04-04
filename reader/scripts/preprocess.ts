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
import type { Heading, Image, Root as MdastRoot, Node, Table, TableRow } from 'mdast'
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
const COLUMN_HEIGHT_PT = 560 // usable column height (680 - 60×2 - 20 header/footer)
// 2 columns per page — used implicitly by the paginator (2 × COLUMN_HEIGHT_PT)
const WORDS_PER_COL_LINE = 8 // ~35 chars in narrow column
const LINE_HEIGHT_PT = 11.6 // 8pt × 1.45
const PARA_MARGIN_PT = 6 // bottom margin per paragraph

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

const headingHeights: Record<number, number> = { 1: 38, 2: 28, 3: 22, 4: 16 }

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
  const segments: Segment[] = []

  // Inline markdown images are rare in this corpus; they're handled via the
  // manifest injection loop below. The visit call is kept for future use.
  visit(tree, 'image', (node: Image) => {
    void node
  })

  // Walk top-level nodes
  for (const node of tree.children) {
    if (node.type === 'heading') {
      const h = node as Heading
      const text = toText(h)
      if (h.depth === 1 && segments.length === 0) title = text
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
      firstParagraph = false
      segments.push({
        type: 'paragraph',
        html,
        isChapterOpener,
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
    // list nodes: convert to HTML paragraph
    else if (node.type === 'list') {
      const html = nodeToHtml(node)
      const text = toText(node)
      segments.push({
        type: 'paragraph',
        html,
        heightPt: textHeightPt(text) + 4,
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

  function addSegment(seg: Segment, chTitle: string, chIdx: number) {
    // Ensure current page matches the chapter
    if (currentPage.chapterTitle !== chTitle && currentPage.segments.length > 0) {
      flush()
      currentPage = newPage(pageNumber, chTitle, chIdx)
    } else if (currentPage.chapterTitle !== chTitle) {
      currentPage.chapterTitle = chTitle
      currentPage.chapterIndex = chIdx
    }

    // Headings: keep with next content — simple approach: don't break heading at column bottom
    const willOverflow = colFill + seg.heightPt > COLUMN_HEIGHT_PT

    if (willOverflow) {
      if (seg.type === 'heading') {
        // Move heading to next column/page so it stays with content
        nextColumn()
        currentPage =
          currentPage.segments.length === 0
            ? currentPage
            : newPage(pageNumber, chTitle, chIdx)
        if (currentPage.segments.length === 0 && pages.length > 0) {
          // already on new page from flush, fix currentPage
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

    for (const seg of ch.segments) {
      addSegment(seg, ch.title, ch.index)
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

  const toc: TocEntry[] = existsSync(TOC_FILE)
    ? JSON.parse(readFileSync(TOC_FILE, 'utf8'))
    : []

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
