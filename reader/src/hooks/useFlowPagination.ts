/**
 * useFlowPagination — React hook that runs the DOM-measurement flow engine
 *
 * Runs once on mount after fonts are loaded, produces paginated BookData
 * that replaces the old static book-data.json page assignments.
 */

import type { BookData, TocEntry } from '@app-types/book'
import { runFlowEngine } from '@utils/flowEngine'
import { useEffect, useState } from 'react'

interface ChapterInput {
  title: string
  index: number
  segments: import('@app-types/book').Segment[]
}

interface UseFlowPaginationOptions {
  chapters: ChapterInput[]
  tocEntries: TocEntry[]
  /** Column width in px (from CSS variables, typically ~237px) */
  columnWidth: number
  /** Full content width (both columns + gap) in px */
  contentWidth: number
  /** Available content height in px (page height minus margins, header, footer) */
  columnHeight: number
  /** Content height on section heading pages (no header banner) */
  sectionHeadingColumnHeight: number
}

interface UseFlowPaginationResult {
  bookData: BookData | null
  isReady: boolean
  pageCount: number
  error: string | null
}

/**
 * Compute page dimensions from CSS variables.
 * These match the values in variables.css:
 *   --page-width: 642px
 *   --page-height: 907px
 *   --page-margin-h: 76px
 *   --page-margin-v: 35px
 *   --column-gap: 19px
 *
 * Content area = page-width - 2*margin-h = 642 - 152 = 490px
 * Column width = (490 - 19) / 2 = 235.5px ≈ 235px
 *
 * Vertical content area (normal page with header banner):
 *   page-height - 2*margin-v - header - footer
 *   = 907 - 70 - 80 - 66 = 691px available for columns
 *
 * Section heading pages hide the banner, gaining headerHeight:
 *   907 - 70 - 66 = 771px — but H2 frame + fiction consume part of this
 *   (handled dynamically by the flow engine)
 */
export const PAGE_METRICS = {
  pageWidth: 642,
  pageHeight: 907,
  marginH: 76,
  marginV: 35,
  columnGap: 19,
  /** Header banner (64px) + margin-bottom (16px) */
  headerHeight: 80,
  /** Footer (62px) + padding-top (4px) */
  footerHeight: 66,

  get contentWidth() {
    return this.pageWidth - 2 * this.marginH
  },
  get columnWidth() {
    return Math.floor((this.contentWidth - this.columnGap) / 2)
  },
  /** Available column height on a normal page (with header banner) */
  get contentHeight() {
    return this.pageHeight - 2 * this.marginV - this.headerHeight - this.footerHeight
  },
  /** Available column height on section heading pages (no header banner) */
  get sectionHeadingContentHeight() {
    return this.pageHeight - 2 * this.marginV - this.footerHeight
  },
}

export function useFlowPagination(
  options: UseFlowPaginationOptions,
): UseFlowPaginationResult {
  const [bookData, setBookData] = useState<BookData | null>(null)
  const [isReady, setIsReady] = useState(false)
  const [pageCount, setPageCount] = useState(0)
  const [error, setError] = useState<string | null>(null)

  const { chapters, tocEntries, columnWidth, contentWidth, columnHeight, sectionHeadingColumnHeight } =
    options

  useEffect(() => {
    let cancelled = false

    async function paginate() {
      try {
        // Wait for fonts to load — critical for accurate measurement
        await document.fonts.ready

        if (cancelled) return

        const result = runFlowEngine({
          columnWidth,
          contentWidth,
          columnHeight,
          sectionHeadingColumnHeight,
          chapters,
          tocEntries,
        })

        if (cancelled) return

        setBookData(result.bookData)
        setPageCount(result.pageCount)
        setIsReady(true)
      } catch (err) {
        if (!cancelled) {
          console.error('[FlowEngine] Pagination failed:', err)
          setError(err instanceof Error ? err.message : String(err))
        }
      }
    }

    paginate()

    return () => {
      cancelled = true
    }
  }, [chapters, tocEntries, columnWidth, contentWidth, columnHeight, sectionHeadingColumnHeight])

  return { bookData, isReady, pageCount, error }
}
