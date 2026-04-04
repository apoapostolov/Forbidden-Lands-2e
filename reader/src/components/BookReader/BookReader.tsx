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
const BURST_STREAK_MIN = 2

interface NavOptions {
  forceInstant?: boolean
}

const BookReader = forwardRef<BookReaderHandle, BookReaderProps>(
  ({ bookData, initialPage = -1, onPageChange }, ref) => {
    const flipRef = useRef<PageFlipRef | null>(null)
    const currentPageRef = useRef(initialPage + 1)
    const desiredSpreadRef = useRef(0)
    const isFlippingRef = useRef(false)
    const lastNavAtRef = useRef(0)
    const resetFlipSpeedTimerRef = useRef<number | null>(null)
    const rapidPressStreakRef = useRef(0)
    const burstCommitRafRef = useRef<number | null>(null)
    const { scale, pageWidth, pageHeight } = useViewportScale()
    const [flippingTime, setFlippingTime] = useState(DEFAULT_FLIP_MS)
    const [layoutStable, setLayoutStable] = useState(false)
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

    function logicalToSpread(logicalPage: number) {
      if (logicalPage < 0) return -1
      return Math.floor(logicalPage / 2)
    }

    function internalToSpread(internalPage: number) {
      if (internalPage <= 0) return -1
      return Math.floor((internalPage - 1) / 2)
    }

    function maxSpread() {
      return logicalToSpread(bookData.totalPages - 1)
    }

    function spreadToInternalPage(spread: number) {
      if (spread < 0) return 0 // cover
      // First page of the spread in internal indexing.
      return Math.min(bookData.totalPages, spread * 2 + 1)
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
        rapidPressStreakRef.current += 1
        scheduleDefaultFlipSpeed()
      } else {
        rapidPressStreakRef.current = 1
      }
      lastNavAtRef.current = now
    }

    function driveTowardsDesired() {
      if (isFlippingRef.current) return
      const currentSpread = internalToSpread(currentPageRef.current)
      const desired = Math.max(-1, Math.min(desiredSpreadRef.current, maxSpread()))

      if (desired === currentSpread) return

      const api = flipRef.current?.pageFlip()
      if (!api) return

      const spreadDistance = Math.abs(desired - currentSpread)
      const shouldBurstSkip =
        rapidPressStreakRef.current >= BURST_STREAK_MIN && spreadDistance >= 1
      const targetInternal = spreadToInternalPage(desired)

      if (shouldBurstSkip) {
        // Burst mode is intentionally non-animated for speed.
        api.turnToPage(targetInternal)
        currentPageRef.current = targetInternal
        onPageChange?.(toLogicalPage(targetInternal))
        isFlippingRef.current = false
        rapidPressStreakRef.current = 0
      } else if (desired > currentSpread) {
        isFlippingRef.current = true
        api.flipNext()
      } else {
        isFlippingRef.current = true
        api.flipPrev()
      }
    }

    function commitDesiredInstantly() {
      const api = flipRef.current?.pageFlip()
      if (!api) return

      const desired = Math.max(-1, Math.min(desiredSpreadRef.current, maxSpread()))
      const targetInternal = spreadToInternalPage(desired)

      api.turnToPage(targetInternal)
      currentPageRef.current = targetInternal
      isFlippingRef.current = false
      onPageChange?.(toLogicalPage(targetInternal))
      rapidPressStreakRef.current = 0
    }

    function scheduleBurstCommit() {
      if (burstCommitRafRef.current) {
        cancelAnimationFrame(burstCommitRafRef.current)
      }

      burstCommitRafRef.current = requestAnimationFrame(() => {
        burstCommitRafRef.current = null
        commitDesiredInstantly()
      })
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
      desiredSpreadRef.current = logicalToSpread(clampLogicalPage(logicalPage))

      const shouldPreemptAnimation = options.forceInstant || isFlippingRef.current

      if (shouldPreemptAnimation) {
        if (burstCommitRafRef.current) {
          cancelAnimationFrame(burstCommitRafRef.current)
          burstCommitRafRef.current = null
        }
        commitDesiredInstantly()
        return
      }

      if (rapidPressStreakRef.current >= BURST_STREAK_MIN) {
        scheduleBurstCommit()
        return
      }

      driveTowardsDesired()
    }

    function requestDelta(delta: number, options: NavOptions = {}) {
      if (delta === 0) return
      if (!options.forceInstant) {
        maybeEnableFastFlip()
      }
      desiredSpreadRef.current = Math.max(
        -1,
        Math.min(desiredSpreadRef.current + delta, maxSpread()),
      )

      const shouldPreemptAnimation = options.forceInstant || isFlippingRef.current

      if (shouldPreemptAnimation) {
        if (burstCommitRafRef.current) {
          cancelAnimationFrame(burstCommitRafRef.current)
          burstCommitRafRef.current = null
        }
        commitDesiredInstantly()
        return
      }

      if (rapidPressStreakRef.current >= BURST_STREAK_MIN) {
        scheduleBurstCommit()
        return
      }

      driveTowardsDesired()
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
      desiredSpreadRef.current = logicalToSpread(clampLogicalPage(initialPage))
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
    useEffect(() => {
      let raf = 0
      let tries = 0
      const maxTries = 120
      setLayoutStable(false)

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
          // Fallback: show the reader even if bounds check never converges,
          // to avoid an indefinite hidden UI.
          setLayoutStable(true)
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
        if (burstCommitRafRef.current) {
          cancelAnimationFrame(burstCommitRafRef.current)
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
              const incomingSpread = internalToSpread(internalPage)

              // Ignore stale completion events from preempted animations.
              if (!isFlippingRef.current && incomingSpread !== desiredSpreadRef.current) {
                return
              }

              currentPageRef.current = internalPage
              onPageChange?.(toLogicalPage(internalPage))

              isFlippingRef.current = false
              requestAnimationFrame(() => {
                snapLeftPageToPixelGrid()
                const currentSpread = internalToSpread(currentPageRef.current)
                if (currentSpread === desiredSpreadRef.current) {
                  rapidPressStreakRef.current = 0
                }
                driveTowardsDesired()
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
