import { FormEvent, useEffect, useRef, useState } from 'react'
import styles from './NavBar.module.css'

interface NavBarProps {
  currentPage: number
  totalPages: number
  onGoTo: (page: number) => void
  onGoToInstant: (page: number) => void
  onPrev: () => void
  onPrevInstant: () => void
  onNext: () => void
  onNextInstant: () => void
  onTocOpen: () => void
  searchValue: string
  onSearchChange: (value: string) => void
}

function isFullscreen() {
  return !!document.fullscreenElement
}

export default function NavBar({
  currentPage,
  totalPages,
  onGoTo,
  onGoToInstant,
  onPrev,
  onPrevInstant,
  onNext,
  onNextInstant,
  onTocOpen,
  searchValue,
  onSearchChange,
}: NavBarProps) {
  const [jumpValue, setJumpValue] = useState('')
  const [fs, setFs] = useState(isFullscreen)
  const inputRef = useRef<HTMLInputElement>(null)
  const searchRef = useRef<HTMLInputElement>(null)
  const holdTimerRef = useRef<number | null>(null)
  const holdIntervalRef = useRef<number | null>(null)
  const isHoldingRef = useRef(false)
  const suppressClickRef = useRef(false)
  const lastPrevClickAtRef = useRef(0)
  const lastNextClickAtRef = useRef(0)

  const MULTI_CLICK_WINDOW_MS = 650

  function clearHoldTimers() {
    if (holdTimerRef.current) {
      window.clearTimeout(holdTimerRef.current)
      holdTimerRef.current = null
    }
    if (holdIntervalRef.current) {
      window.clearInterval(holdIntervalRef.current)
      holdIntervalRef.current = null
    }
  }

  function startHold(direction: 'prev' | 'next') {
    clearHoldTimers()
    isHoldingRef.current = false

    const step = () => {
      if (direction === 'prev') onPrevInstant()
      else onNextInstant()
    }

    holdTimerRef.current = window.setTimeout(() => {
      isHoldingRef.current = true
      suppressClickRef.current = true
      step()
      holdIntervalRef.current = window.setInterval(step, 85)
    }, 180)
  }

  function stopHold() {
    if (isHoldingRef.current) {
      suppressClickRef.current = true
    }
    isHoldingRef.current = false
    clearHoldTimers()
  }

  function onPrevClick() {
    if (suppressClickRef.current) {
      suppressClickRef.current = false
      return
    }

    const now = Date.now()
    const isMultiClick = now - lastPrevClickAtRef.current <= MULTI_CLICK_WINDOW_MS
    lastPrevClickAtRef.current = now

    if (isMultiClick) {
      onPrevInstant()
      return
    }

    onPrev()
  }

  function onNextClick() {
    if (suppressClickRef.current) {
      suppressClickRef.current = false
      return
    }

    const now = Date.now()
    const isMultiClick = now - lastNextClickAtRef.current <= MULTI_CLICK_WINDOW_MS
    lastNextClickAtRef.current = now

    if (isMultiClick) {
      onNextInstant()
      return
    }

    onNext()
  }

  function handleJump(e: FormEvent) {
    e.preventDefault()
    const n = parseInt(jumpValue, 10)
    if (!isNaN(n) && n >= 1 && n <= totalPages) {
      onGoToInstant(n - 1) // book-data pages are 0-indexed in react-pageflip
      setJumpValue('')
      inputRef.current?.blur()
    }
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().then(() => setFs(true))
    } else {
      document.exitFullscreen().then(() => setFs(false))
    }
  }

  useEffect(() => {
    return () => {
      clearHoldTimers()
    }
  }, [])

  return (
    <nav className={styles.bar} aria-label="Book navigation">
      <button
        className={styles.btn}
        onClick={onTocOpen}
        aria-label="Open table of contents"
        title="Table of contents (T)"
      >
        ☰
      </button>

      <button
        className={styles.btn}
        onMouseDown={() => startHold('prev')}
        onMouseUp={stopHold}
        onMouseLeave={stopHold}
        onTouchStart={() => startHold('prev')}
        onTouchEnd={stopHold}
        onTouchCancel={stopHold}
        onClick={onPrevClick}
        aria-label="Previous page (←)"
        title="Previous page"
      >
        ‹
      </button>

      <form className={styles.pageForm} onSubmit={handleJump}>
        <input
          ref={inputRef}
          className={styles.pageInput}
          value={jumpValue}
          onChange={(e) => setJumpValue(e.target.value)}
          placeholder={currentPage < 0 ? 'Cover' : String(currentPage + 1)}
          aria-label="Jump to page"
          inputMode="numeric"
          pattern="[0-9]*"
        />
        <span className={styles.pageTotal}> / {totalPages}</span>
      </form>

      <button
        className={styles.btn}
        onMouseDown={() => startHold('next')}
        onMouseUp={stopHold}
        onMouseLeave={stopHold}
        onTouchStart={() => startHold('next')}
        onTouchEnd={stopHold}
        onTouchCancel={stopHold}
        onClick={onNextClick}
        aria-label="Next page (→)"
        title="Next page"
      >
        ›
      </button>

      <div className={styles.spacer} />

      <form className={styles.searchForm}>
        <input
          ref={searchRef}
          className={styles.searchInput}
          type="text"
          value={searchValue}
          onChange={(e) => onSearchChange(e.target.value)}
          placeholder="Search..."
          aria-label="Search book"
        />
        <span className={styles.searchIcon}>🔍</span>
      </form>

      <button
        className={`${styles.btn} ${styles.fsBtn}`}
        onClick={toggleFullscreen}
        aria-label={fs ? 'Exit fullscreen' : 'Enter fullscreen'}
        title={fs ? 'Exit fullscreen (F11)' : 'Fullscreen'}
      >
        {fs ? '⛶' : '⛶'}
      </button>
    </nav>
  )
}
