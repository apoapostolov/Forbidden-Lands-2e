import { FormEvent, useRef, useState } from 'react'
import styles from './NavBar.module.css'

interface NavBarProps {
  currentPage: number
  totalPages: number
  onGoTo: (page: number) => void
  onPrev: () => void
  onNext: () => void
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
  onPrev,
  onNext,
  onTocOpen,
  searchValue,
  onSearchChange,
}: NavBarProps) {
  const [jumpValue, setJumpValue] = useState('')
  const [fs, setFs] = useState(isFullscreen)
  const inputRef = useRef<HTMLInputElement>(null)
  const searchRef = useRef<HTMLInputElement>(null)

  function handleJump(e: FormEvent) {
    e.preventDefault()
    const n = parseInt(jumpValue, 10)
    if (!isNaN(n) && n >= 1 && n <= totalPages) {
      onGoTo(n - 1) // book-data pages are 0-indexed in react-pageflip
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
        onClick={onPrev}
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
          placeholder={String(currentPage + 1)}
          aria-label="Jump to page"
          inputMode="numeric"
          pattern="[0-9]*"
        />
        <span className={styles.pageTotal}> / {totalPages}</span>
      </form>

      <button
        className={styles.btn}
        onClick={onNext}
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
