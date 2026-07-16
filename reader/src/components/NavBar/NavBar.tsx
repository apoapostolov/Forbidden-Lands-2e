import { type FormEvent, useEffect, useRef, useState } from 'react'
import styles from './NavBar.module.css'

interface NavBarProps {
  currentPage: number
  totalPages: number
  onGoToInstant: (page: number) => void
  onPrev: () => void
  onPrevInstant: () => void
  onNext: () => void
  onNextInstant: () => void
  onTocOpen: () => void
  searchValue: string
  onSearchChange: (value: string) => void
}

export default function NavBar({
  currentPage,
  totalPages,
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
  const [fullscreen, setFullscreen] = useState(() => Boolean(document.fullscreenElement))
  const inputRef = useRef<HTMLInputElement>(null)
  const holdTimerRef = useRef<number | null>(null)
  const holdIntervalRef = useRef<number | null>(null)
  const suppressClickRef = useRef(false)

  function clearHoldTimers() {
    if (holdTimerRef.current !== null) window.clearTimeout(holdTimerRef.current)
    if (holdIntervalRef.current !== null) window.clearInterval(holdIntervalRef.current)
    holdTimerRef.current = null
    holdIntervalRef.current = null
  }

  function startHold(direction: 'prev' | 'next') {
    clearHoldTimers()
    const step = direction === 'prev' ? onPrevInstant : onNextInstant
    holdTimerRef.current = window.setTimeout(() => {
      suppressClickRef.current = true
      step()
      holdIntervalRef.current = window.setInterval(step, 120)
    }, 350)
  }

  function stopHold() {
    clearHoldTimers()
  }

  function handleClick(action: () => void) {
    if (suppressClickRef.current) {
      suppressClickRef.current = false
      return
    }
    action()
  }

  function handleJump(event: FormEvent) {
    event.preventDefault()
    const pageNumber = Number.parseInt(jumpValue, 10)
    if (Number.isFinite(pageNumber) && pageNumber >= 1 && pageNumber <= totalPages) {
      onGoToInstant(pageNumber - 1)
      setJumpValue('')
      inputRef.current?.blur()
    }
  }

  async function toggleFullscreen() {
    try {
      if (document.fullscreenElement) await document.exitFullscreen()
      else await document.documentElement.requestFullscreen()
    } catch (error) {
      console.error('Fullscreen request failed:', error)
    }
  }

  useEffect(() => {
    const syncFullscreen = () => setFullscreen(Boolean(document.fullscreenElement))
    document.addEventListener('fullscreenchange', syncFullscreen)
    return () => {
      clearHoldTimers()
      document.removeEventListener('fullscreenchange', syncFullscreen)
    }
  }, [])

  return (
    <nav className={styles.bar} aria-label="Book navigation">
      <button
        type="button"
        className={styles.btn}
        onClick={onTocOpen}
        aria-label="Open table of contents"
        aria-haspopup="dialog"
        title="Table of contents (T)"
      >
        ☰
      </button>

      <button
        type="button"
        className={styles.btn}
        onPointerDown={() => startHold('prev')}
        onPointerUp={stopHold}
        onPointerCancel={stopHold}
        onPointerLeave={stopHold}
        onClick={() => handleClick(onPrev)}
        disabled={currentPage <= -1}
        aria-label="Previous page"
        title="Previous page"
      >
        ‹
      </button>

      <form className={styles.pageForm} onSubmit={handleJump}>
        <label className={styles.visuallyHidden} htmlFor="page-jump">
          Jump to page
        </label>
        <input
          id="page-jump"
          ref={inputRef}
          className={styles.pageInput}
          value={jumpValue}
          onChange={(event) => setJumpValue(event.target.value)}
          placeholder={currentPage < 0 ? 'Cover' : String(currentPage + 1)}
          inputMode="numeric"
          pattern="[0-9]*"
          autoComplete="off"
        />
        <span className={styles.pageTotal}> / {totalPages}</span>
      </form>

      <button
        type="button"
        className={styles.btn}
        onPointerDown={() => startHold('next')}
        onPointerUp={stopHold}
        onPointerCancel={stopHold}
        onPointerLeave={stopHold}
        onClick={() => handleClick(onNext)}
        disabled={currentPage >= totalPages - 1}
        aria-label="Next page"
        title="Next page"
      >
        ›
      </button>

      <div className={styles.spacer} />

      <form
        className={styles.searchForm}
        role="search"
        onSubmit={(event) => event.preventDefault()}
      >
        <label className={styles.visuallyHidden} htmlFor="book-search">
          Search book
        </label>
        <input
          id="book-search"
          className={styles.searchInput}
          type="search"
          value={searchValue}
          onChange={(event) => onSearchChange(event.target.value)}
          placeholder="Search…"
          autoComplete="off"
          spellCheck="false"
        />
        <span className={styles.searchIcon} aria-hidden="true">
          🔍
        </span>
      </form>

      <button
        type="button"
        className={`${styles.btn} ${styles.fsBtn}`}
        onClick={toggleFullscreen}
        aria-label={fullscreen ? 'Exit fullscreen' : 'Enter fullscreen'}
        aria-pressed={fullscreen}
        title={fullscreen ? 'Exit fullscreen' : 'Enter fullscreen'}
      >
        ⛶
      </button>
    </nav>
  )
}
