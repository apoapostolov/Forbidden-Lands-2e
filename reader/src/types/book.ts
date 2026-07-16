// ── Segment types (Phase 2: pre-processor output) ──────────────────────────

export type SegmentType =
  | 'heading'
  | 'paragraph'
  | 'blockquote'
  | 'table'
  | 'hr'
  | 'image-ref'

export interface BaseSegment {
  type: SegmentType
  /** Estimated height in pt for pagination */
  heightPt: number
  id?: string
  /** Stable identifier assigned after pagination for search and focus targeting. */
  uid: string
}

export interface HeadingSegment extends BaseSegment {
  type: 'heading'
  level: 1 | 2 | 3 | 4
  text: string
  spanAll?: boolean
}

export interface ParagraphSegment extends BaseSegment {
  type: 'paragraph'
  html: string
  isChapterOpener?: boolean
  isFiction?: boolean
  isListSegment?: boolean
  itemLiHtmls?: string[]
  itemHeights?: number[]
  listTag?: 'ul' | 'ol'
  continuesFromPrevious?: boolean
  continuesOnNext?: boolean
}

export interface BlockquoteSegment extends BaseSegment {
  type: 'blockquote'
  html: string
  spanAll?: boolean
  isFiction?: boolean
  continuesFromPrevious?: boolean
  continuesOnNext?: boolean
}

export interface TableSegment extends BaseSegment {
  type: 'table'
  headers: string[]
  rows: string[][]
  /** Wide table should span both columns. */
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

export interface HRSegment extends BaseSegment {
  type: 'hr'
}

export interface ImageRefSegment extends BaseSegment {
  type: 'image-ref'
  filename: string
  width: number
  height: number
  altText: string
  caption?: string
}

export type Segment =
  | HeadingSegment
  | ParagraphSegment
  | BlockquoteSegment
  | TableSegment
  | HRSegment
  | ImageRefSegment

// ── Page types ──────────────────────────────────────────────────────────────

export type PageLayout = 'two-column' | 'single-column' | 'full-art' | 'cover'

export interface BookPage {
  pageNumber: number
  chapterTitle: string
  chapterIndex: number
  layout: PageLayout
  segments: Segment[]
}

// ── TOC types ────────────────────────────────────────────────────────────────

export interface TocEntry {
  level: number
  title: string
  page: number
}

export interface ChapterIndex {
  chapterTitle: string
  chapterIndex: number
  firstPage: number
  lastPage: number
}

// ── Root data shape ──────────────────────────────────────────────────────────

export interface BookData {
  generatedAt: string
  totalPages: number
  chapters: ChapterIndex[]
  toc: TocEntry[]
  pages: BookPage[]
}
