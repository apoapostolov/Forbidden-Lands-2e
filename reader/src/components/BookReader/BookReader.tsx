import type { BookData } from '@app-types/book'
import CoverPage from '@components/CoverPage/CoverPage'
import PageSpread from '@components/PageSpread/PageSpread'
import { useViewportScale } from '@hooks/useViewportScale'
import type { RefObject } from 'react'
import { forwardRef, useEffect, useImperativeHandle, useRef, useState } from 'react'
import HTMLFlipBook from 'react-pageflip'
import styles from './BookReader.module.css'

interface BookReaderProps {
  bookData: BookData
  initialPage?: number
  onPageChange?: (page: number) => void
}

export interface BookReaderHandle {
  goToPage: (page: number) => void
  goToPageInstant: (page: number) => void
  nextPage: () => void
  nextPageInstant: () => void
  prevPage: () => void
  prevPageInstant: () => void
}

/** Minimal interface for the methods we call on the pageFlip handle. */
interface PageFlipRef {
  pageFlip: () => {
    flip: (n: number) => void
    flipNext: () => void
    flipPrev: () => void
    turnToPage: (n: number) => void
    getCurrentPageIndex: () => number
  }
}

const DEFAULT_FLIP_MS = 800
const FAST_FLIP_MS = 140
const RAPID_NAV_THRESHOLD_MS = 220

interface NavOptions {
  forceInstant?: boolean
}

const BookReader = forwardRef<BookReaderHandle, BookReaderProps>(
  ({ bookData, initialPage = -1, onPageChange }, ref) => {
    const flipRef = useRef<PageFlipRef | null>(null)
    const currentPageRef = useRef(initialPage + 1)
    const isFlippingRef = useRef(false)
    const lastNavAtRef = useRef(0)
    const resetFlipSpeedTimerRef = useRef<number | null>(null)
    const { scale, pageWidth, pageHeight } = useViewportScale()
    const [flippingTime, setFlippingTime] = useState(DEFAULT_FLIP_MS)
    const [layoutStable, setLayoutStable] = useState(true)
    const [snapOffsetX, setSnapOffsetX] = useState(0)
    const [useZoomScale, setUseZoomScale] = useState(false)

    function clampLogicalPage(page: number) {
      return Math.max(-1, Math.min(page, bookData.totalPages - 1))
    }

    function toInternalPage(logicalPage: number) {
      return clampLogicalPage(logicalPage) + 1
    }

    function toLogicalPage(internalPage: number) {
      return internalPage - 1
    }

    function maxInternalPage() {
      return bookData.totalPages
    }

    function clampInternalPage(page: number) {
      return Math.max(0, Math.min(page, maxInternalPage()))
    }

    function scheduleDefaultFlipSpeed() {
      if (resetFlipSpeedTimerRef.current) {
        window.clearTimeout(resetFlipSpeedTimerRef.current)
      }
      resetFlipSpeedTimerRef.current = window.setTimeout(() => {
        setFlippingTime(DEFAULT_FLIP_MS)
      }, 450)
    }

    function maybeEnableFastFlip() {
      const now = Date.now()
      if (now - lastNavAtRef.current <= RAPID_NAV_THRESHOLD_MS) {
        setFlippingTime(FAST_FLIP_MS)
        scheduleDefaultFlipSpeed()
      }
      lastNavAtRef.current = now
    }

    function snapLeftPageToPixelGrid() {
      const flipBookEl = document.querySelector(`.${styles.flipBook}`)
      if (!(flipBookEl instanceof HTMLElement)) return

      const leftCandidates = Array.from(
        flipBookEl.querySelectorAll('.stf__item.--left.--simple'),
      ).filter((el): el is HTMLElement => el instanceof HTMLElement)

      if (leftCandidates.length === 0) return

      const leftPage = leftCandidates
        .map((el) => ({ el, rect: el.getBoundingClientRect() }))
        .filter(({ rect }) => rect.width > 20 && rect.height > 20)
        .sort((a, b) => b.rect.width * b.rect.height - a.rect.width * a.rect.height)[0]

      if (!leftPage) return

      const rect = leftPage.rect
      const delta = Math.round(rect.left) - rect.left
      setSnapOffsetX((prev) => (Math.abs(delta) > 0.01 ? prev + delta : prev))
    }

    function requestGoTo(logicalPage: number, options: NavOptions = {}) {
      if (!options.forceInstant) {
        maybeEnableFastFlip()
      }
      const api = flipRef.current?.pageFlip()
      if (!api) return
      const targetInternal = toInternalPage(clampLogicalPage(logicalPage))
      api.turnToPage(targetInternal)
      currentPageRef.current = targetInternal
      isFlippingRef.current = false
      onPageChange?.(toLogicalPage(targetInternal))
    }

    function requestDelta(delta: number, options: NavOptions = {}) {
      if (delta === 0) return
      if (!options.forceInstant) {
        maybeEnableFastFlip()
      }
      const api = flipRef.current?.pageFlip()
      if (!api) return

      if (options.forceInstant || isFlippingRef.current) {
        const targetInternal = clampInternalPage(currentPageRef.current + delta)
        api.turnToPage(targetInternal)
        currentPageRef.current = targetInternal
        isFlippingRef.current = false
        onPageChange?.(toLogicalPage(targetInternal))
        return
      }

      isFlippingRef.current = true
      if (delta > 0) {
        api.flipNext()
      } else {
        api.flipPrev()
      }
    }

    useImperativeHandle(ref, () => ({
      goToPage: (page: number) => requestGoTo(page),
      goToPageInstant: (page: number) => requestGoTo(page, { forceInstant: true }),
      nextPage: () => requestDelta(1),
      nextPageInstant: () => requestDelta(1, { forceInstant: true }),
      prevPage: () => requestDelta(-1),
      prevPageInstant: () => requestDelta(-1, { forceInstant: true }),
    }))

    useEffect(() => {
      currentPageRef.current = toInternalPage(initialPage)
      isFlippingRef.current = false
    }, [initialPage, bookData.totalPages])

    useEffect(() => {
      setUseZoomScale(CSS.supports('zoom', '1'))
    }, [])

    useEffect(() => {
      if (!layoutStable) return
      const raf = requestAnimationFrame(() => snapLeftPageToPixelGrid())
      return () => cancelAnimationFrame(raf)
    }, [layoutStable, scale])

    // Guard against transient react-pageflip initialization states that can
    // briefly place the spread far outside viewport bounds.
    //
    // Important UX rule: the reader must never stay hidden. We keep the book
    // visible by default and only use this effect to opportunistically confirm
    // stable bounds, not to gate rendering behind opacity: 0.
    useEffect(() => {
      let raf = 0
      let tries = 0
      const maxTries = 120

      const check = () => {
        const flipBookEl = document.querySelector(`.${styles.flipBook}`)
        if (flipBookEl instanceof HTMLElement) {
          const rect = flipBookEl.getBoundingClientRect()
          const isValid =
            rect.height > 0 &&
            rect.top >= 0 &&
            rect.bottom <= window.innerHeight &&
            Number.isFinite(rect.top) &&
            Number.isFinite(rect.bottom)

          if (isValid) {
            setLayoutStable(true)
            return
          }
        }

        tries += 1
        if (tries >= maxTries) {
          // Do not hide the reader if convergence never happens.
          return
        }

        raf = requestAnimationFrame(check)
      }

      raf = requestAnimationFrame(check)
      return () => cancelAnimationFrame(raf)
    }, [scale, initialPage])

    // Keyboard navigation
    useEffect(() => {
      function onKey(e: KeyboardEvent) {
        const instantForKeyboard = e.repeat || isFlippingRef.current

        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          requestDelta(1, { forceInstant: instantForKeyboard })
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          requestDelta(-1, { forceInstant: instantForKeyboard })
        } else if (e.key === 'Home') {
          requestGoTo(-1, { forceInstant: instantForKeyboard })
        } else if (e.key === 'End') {
          requestGoTo(bookData.totalPages - 1, { forceInstant: instantForKeyboard })
        }
      }
      window.addEventListener('keydown', onKey)
      return () => {
        window.removeEventListener('keydown', onKey)
        if (resetFlipSpeedTimerRef.current) {
          window.clearTimeout(resetFlipSpeedTimerRef.current)
        }
      }
    }, [bookData.totalPages])

    return (
      <div className={styles.wrapper}>
        <div
          className={`${styles.scaler} ${layoutStable ? styles.ready : styles.pending}`}
          style={{
            transform: useZoomScale ? undefined : `scale(${scale})`,
            transformOrigin: useZoomScale ? undefined : 'center center',
            zoom: useZoomScale ? scale : undefined,
            marginLeft: `${snapOffsetX}px`,
          }}
        >
          <button
            type="button"
            className={`${styles.marginNav} ${styles.marginLeft}`}
            aria-label="Previous page"
            onMouseDown={(e) => e.preventDefault()}
            onClick={() => requestDelta(-1)}
          />
          <HTMLFlipBook
            ref={flipRef as RefObject<never>}
            width={pageWidth}
            height={pageHeight}
            minWidth={320}
            maxWidth={pageWidth}
            minHeight={400}
            maxHeight={pageHeight}
            flippingTime={flippingTime}
            showCover={true}
            maxShadowOpacity={0.6}
            drawShadow={true}
            useMouseEvents={false}
            usePortrait={false}
            startPage={toInternalPage(initialPage)}
            startZIndex={10}
            size="fixed"
            autoSize={false}
            mobileScrollSupport={false}
            clickEventForward={false}
            swipeDistance={50}
            showPageCorners={false}
            disableFlipByClick={true}
            className={styles.flipBook}
            style={{}}
            onFlip={(e: { data: number }) => {
              const internalPage = e.data

              currentPageRef.current = internalPage
              onPageChange?.(toLogicalPage(internalPage))

              isFlippingRef.current = false
              requestAnimationFrame(() => {
                snapLeftPageToPixelGrid()
              })
            }}
          >
            <div key="cover" data-density="hard">
              <CoverPage />
            </div>
            {bookData.pages.map((page, idx) => (
              <div key={page.pageNumber}>
                <PageSpread page={page} side={(idx + 1) % 2 === 0 ? 'right' : 'left'} />
              </div>
            ))}
          </HTMLFlipBook>
          <button
            type="button"
            className={`${styles.marginNav} ${styles.marginRight}`}
            aria-label="Next page"
            onMouseDown={(e) => e.preventDefault()}
            onClick={() => requestDelta(1)}
          />
        </div>
      </div>
    )
  },
)
BookReader.displayName = 'BookReader'
export default BookReader
