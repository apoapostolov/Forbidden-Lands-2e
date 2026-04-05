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
  /** Available content height in px (page height minus margins, header, footer) */
  columnHeight: number
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
 * Column width = (490 - 19) / 2 = 235.5px ≈ 236px
 *
 * Vertical content area:
 *   page-height - 2*margin-v = 907 - 70 = 837px
 *   minus header banner ≈ 64px
 *   minus footer ≈ 95px
 *   = 837 - 64 - 95 = 678px available for columns
 *
 * But the actual flex layout gives the .columns container the remaining
 * space after header+footer are positioned. We measure this dynamically.
 */
export const PAGE_METRICS = {
  pageWidth: 642,
  pageHeight: 907,
  marginH: 76,
  marginV: 35,
  columnGap: 19,
  headerHeight: 64,
  footerHeight: 95,

  get contentWidth() {
    return this.pageWidth - 2 * this.marginH
  },
  get columnWidth() {
    return Math.floor((this.contentWidth - this.columnGap) / 2)
  },
  get contentHeight() {
    return this.pageHeight - 2 * this.marginV - this.headerHeight - this.footerHeight
  },
}

export function useFlowPagination(
  options: UseFlowPaginationOptions,
): UseFlowPaginationResult {
  const [bookData, setBookData] = useState<BookData | null>(null)
  const [isReady, setIsReady] = useState(false)
  const [pageCount, setPageCount] = useState(0)
  const [error, setError] = useState<string | null>(null)

  const { chapters, tocEntries, columnWidth, columnHeight } = options

  useEffect(() => {
    let cancelled = false

    async function paginate() {
      try {
        // Wait for fonts to load — critical for accurate measurement
        await document.fonts.ready

        if (cancelled) return

        const result = runFlowEngine({
          columnWidth,
          columnHeight,
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
  }, [chapters, tocEntries, columnWidth, columnHeight])

  return { bookData, isReady, pageCount, error }
}
