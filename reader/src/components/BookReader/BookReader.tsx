import { useRef, useEffect, forwardRef, useImperativeHandle } from 'react'
import HTMLFlipBook from 'react-pageflip'
import PageSpread from '@components/PageSpread/PageSpread'
import type { BookData } from '@types/book'
import { useViewportScale } from '@hooks/useViewportScale'
import styles from './BookReader.module.css'

interface BookReaderProps {
  bookData: BookData
  initialPage?: number
}

export interface BookReaderHandle {
  goToPage: (page: number) => void
  nextPage: () => void
  prevPage: () => void
}

const BookReader = forwardRef<BookReaderHandle, BookReaderProps>(
  ({ bookData, initialPage = 0 }, ref) => {
    const flipRef = useRef<InstanceType<typeof HTMLFlipBook>>(null)
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
            ref={flipRef}
            width={pageWidth}
            height={pageHeight}
            flippingTime={800}
            showCover={false}
            maxShadowOpacity={0.6}
            minShadowOpacity={0.05}
            drawShadow={true}
            useMouseEvents={true}
            usePortrait={false}
            startPage={initialPage}
            size="fixed"
            autoSize={false}
            mobileScrollSupport={false}
            className={styles.flipBook}
            style={{}}
          >
            {bookData.pages.map((page, idx) => (
              <div key={page.pageNumber}>
                <PageSpread
                  page={page}
                  side={idx % 2 === 0 ? 'right' : 'left'}
                />
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
