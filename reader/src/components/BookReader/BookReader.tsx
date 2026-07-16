import type { BookData } from '@app-types/book'
import CoverPage from '@components/CoverPage/CoverPage'
import PageSpread from '@components/PageSpread/PageSpread'
import { useViewportScale } from '@hooks/useViewportScale'
import { isEditableTarget } from '@utils/keyboard'
import { forwardRef, useCallback, useEffect, useImperativeHandle, useMemo } from 'react'
import styles from './BookReader.module.css'

interface BookReaderProps {
  bookData: BookData
  currentPage: number
  onPageChange: (page: number) => void
}

export interface BookReaderHandle {
  goToPage: (page: number) => void
  goToPageInstant: (page: number) => void
  nextPage: () => void
  nextPageInstant: () => void
  prevPage: () => void
  prevPageInstant: () => void
}

const BookReader = forwardRef<BookReaderHandle, BookReaderProps>(
  ({ bookData, currentPage, onPageChange }, ref) => {
    const { scale, singlePage } = useViewportScale()

    const goToPage = useCallback(
      (page: number) => {
        onPageChange(Math.max(-1, Math.min(page, bookData.totalPages - 1)))
      },
      [bookData.totalPages, onPageChange],
    )

    const changePage = useCallback(
      (delta: number) => goToPage(currentPage + delta),
      [currentPage, goToPage],
    )

    useImperativeHandle(
      ref,
      () => ({
        goToPage,
        goToPageInstant: goToPage,
        nextPage: () => changePage(1),
        nextPageInstant: () => changePage(1),
        prevPage: () => changePage(-1),
        prevPageInstant: () => changePage(-1),
      }),
      [changePage, goToPage],
    )

    useEffect(() => {
      function onKey(event: KeyboardEvent) {
        if (
          event.defaultPrevented ||
          event.ctrlKey ||
          event.metaKey ||
          event.altKey ||
          isEditableTarget(event.target) ||
          document.querySelector('dialog[open]')
        ) {
          return
        }

        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
          event.preventDefault()
          changePage(1)
        } else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
          event.preventDefault()
          changePage(-1)
        } else if (event.key === 'Home') {
          event.preventDefault()
          goToPage(-1)
        } else if (event.key === 'End') {
          event.preventDefault()
          goToPage(bookData.totalPages - 1)
        }
      }

      window.addEventListener('keydown', onKey)
      return () => window.removeEventListener('keydown', onKey)
    }, [bookData.totalPages, changePage, goToPage])

    const visiblePages = useMemo(() => {
      if (currentPage < 0) return []
      const first = bookData.pages[currentPage]
      if (!first) return []
      if (singlePage) return [first]
      const second = bookData.pages[currentPage + 1]
      return second ? [first, second] : [first]
    }, [bookData.pages, currentPage, singlePage])

    const pageAnnouncement =
      currentPage < 0
        ? 'Book cover'
        : singlePage || visiblePages.length === 1
          ? `Page ${currentPage + 1} of ${bookData.totalPages}`
          : `Pages ${currentPage + 1} and ${currentPage + 2} of ${bookData.totalPages}`

    return (
      <main
        id="reader-content"
        className={styles.wrapper}
        tabIndex={-1}
        aria-label="Forbidden Lands reader"
      >
        <div
          className={styles.scaler}
          style={{ transform: singlePage ? undefined : `scale(${scale})` }}
        >
          <button
            type="button"
            className={`${styles.marginNav} ${styles.marginLeft}`}
            aria-label="Previous page"
            disabled={currentPage <= -1}
            onClick={() => changePage(-1)}
          />

          <div className={styles.spread} key={`${currentPage}-${singlePage}`}>
            {currentPage < 0 ? (
              <div className={styles.pageSlot}>
                <CoverPage />
              </div>
            ) : (
              visiblePages.map((page, index) => (
                <div
                  key={page.pageNumber}
                  className={`${styles.pageSlot} ${index > 0 ? styles.secondaryPage : ''}`}
                >
                  <PageSpread page={page} side={index === 0 ? 'left' : 'right'} />
                </div>
              ))
            )}
          </div>

          <button
            type="button"
            className={`${styles.marginNav} ${styles.marginRight}`}
            aria-label="Next page"
            disabled={currentPage >= bookData.totalPages - 1}
            onClick={() => changePage(1)}
          />
        </div>

        <p
          className={styles.pageStatus}
          role="status"
          aria-live="polite"
          aria-atomic="true"
        >
          {pageAnnouncement}
        </p>
      </main>
    )
  },
)

BookReader.displayName = 'BookReader'
export default BookReader
