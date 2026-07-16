import { MAX_SEARCH_RESULTS, type SearchMatch } from '@utils/search'
import { useEffect, useRef, useState } from 'react'
import styles from './SearchPanel.module.css'

interface SearchPanelProps {
  matches: SearchMatch[]
  query: string
  isOpen: boolean
  onNavigate: (match: SearchMatch) => void
  currentPage: number
}

export default function SearchPanel({
  matches,
  query,
  isOpen,
  onNavigate,
  currentPage,
}: SearchPanelProps) {
  const [activeSegmentUid, setActiveSegmentUid] = useState<string | null>(null)
  const highlightedElementRef = useRef<HTMLElement | null>(null)

  useEffect(() => {
    highlightedElementRef.current?.classList.remove(styles.highlightedParagraph)
    highlightedElementRef.current = null

    if (!activeSegmentUid) return
    const frame = requestAnimationFrame(() => {
      const element = document.querySelector<HTMLElement>(
        `[data-segment-id="${CSS.escape(activeSegmentUid)}"]`,
      )
      if (!element) return
      element.classList.add(styles.highlightedParagraph)
      highlightedElementRef.current = element
      element.scrollIntoView({ behavior: 'smooth', block: 'center' })
    })

    return () => cancelAnimationFrame(frame)
  }, [activeSegmentUid, currentPage])

  useEffect(() => {
    if (!isOpen) setActiveSegmentUid(null)
  }, [isOpen])

  useEffect(() => {
    setActiveSegmentUid(null)
  }, [query])

  if (!isOpen) return null

  const resultLabel =
    matches.length >= MAX_SEARCH_RESULTS
      ? `First ${MAX_SEARCH_RESULTS} results`
      : `${matches.length} result${matches.length === 1 ? '' : 's'}`

  return (
    <aside className={styles.panel} aria-labelledby="search-results-title">
      <div className={styles.header}>
        <h2 id="search-results-title" className={styles.title}>
          Search results
        </h2>
        <p className={styles.resultCount} role="status" aria-live="polite">
          {resultLabel} for “{query.trim()}”
        </p>
      </div>

      {matches.length === 0 ? (
        <p className={styles.empty}>No matching rules found.</p>
      ) : (
        <div className={styles.results}>
          {matches.map((match) => (
            <button
              type="button"
              key={`${match.segmentUid}-${match.matchStart}`}
              className={`${styles.result} ${
                match.pageIdx === currentPage ? styles.current : ''
              }`}
              onClick={() => {
                setActiveSegmentUid(match.segmentUid)
                onNavigate(match)
              }}
              aria-label={`Page ${match.pageNumber}: ${match.matchText}`}
            >
              <span className={styles.page}>Page {match.pageNumber}</span>
              <span className={styles.context}>
                <span className={styles.before}>{match.contextBefore}</span>
                <mark className={styles.match}>{match.matchText}</mark>
                <span className={styles.after}>{match.contextAfter}</span>
              </span>
            </button>
          ))}
        </div>
      )}
    </aside>
  )
}
