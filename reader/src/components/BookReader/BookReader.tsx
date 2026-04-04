import type { BookData } from '@app-types/book'
import PageSpread from '@components/PageSpread/PageSpread'
import { useViewportScale } from '@hooks/useViewportScale'
import type { RefObject } from 'react'
import { forwardRef, useEffect, useImperativeHandle, useRef } from 'react'
import HTMLFlipBook from 'react-pageflip'
import styles from './BookReader.module.css'

interface BookReaderProps {
  bookData: BookData
  initialPage?: number
  onPageChange?: (page: number) => void
}

export interface BookReaderHandle {
  goToPage: (page: number) => void
  nextPage: () => void
  prevPage: () => void
}

/** Minimal interface for the methods we call on the pageFlip handle. */
interface PageFlipRef {
  pageFlip: () => {
    flip: (n: number) => void
    flipNext: () => void
    flipPrev: () => void
  }
}

const BookReader = forwardRef<BookReaderHandle, BookReaderProps>(
  ({ bookData, initialPage = 0, onPageChange }, ref) => {
    const flipRef = useRef<PageFlipRef | null>(null)
    const { scale, pageWidth, pageHeight } = useViewportScale()

    useImperativeHandle(ref, () => ({
      goToPage: (page: number) => flipRef.current?.pageFlip().flip(page),
      nextPage: () => flipRef.current?.pageFlip().flipNext(),
      prevPage: () => flipRef.current?.pageFlip().flipPrev(),
    }))

    // Keyboard navigation
    useEffect(() => {
      function onKey(e: KeyboardEvent) {
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          flipRef.current?.pageFlip().flipNext()
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          flipRef.current?.pageFlip().flipPrev()
        } else if (e.key === 'Home') {
          flipRef.current?.pageFlip().flip(0)
        } else if (e.key === 'End') {
          flipRef.current?.pageFlip().flip(bookData.totalPages - 1)
        }
      }
      window.addEventListener('keydown', onKey)
      return () => window.removeEventListener('keydown', onKey)
    }, [bookData.totalPages])

    return (
      <div className={styles.wrapper}>
        <div
          className={styles.scaler}
          style={{ transform: `scale(${scale})`, transformOrigin: 'center center' }}
        >
          <HTMLFlipBook
            ref={flipRef as RefObject<never>}
            width={pageWidth}
            height={pageHeight}
            minWidth={320}
            maxWidth={pageWidth}
            minHeight={400}
            maxHeight={pageHeight}
            flippingTime={800}
            showCover={false}
            maxShadowOpacity={0.6}
            drawShadow={true}
            useMouseEvents={true}
            usePortrait={false}
            startPage={initialPage}
            startZIndex={10}
            size="fixed"
            autoSize={false}
            mobileScrollSupport={false}
            clickEventForward={true}
            swipeDistance={50}
            showPageCorners={true}
            disableFlipByClick={false}
            className={styles.flipBook}
            style={{}}
            onFlip={(e: { data: number }) => onPageChange?.(e.data)}
          >
            {bookData.pages.map((page, idx) => (
              <div key={page.pageNumber}>
                <PageSpread page={page} side={idx % 2 === 0 ? 'right' : 'left'} />
              </div>
            ))}
          </HTMLFlipBook>
        </div>
      </div>
    )
  },
)
BookReader.displayName = 'BookReader'
export default BookReader
