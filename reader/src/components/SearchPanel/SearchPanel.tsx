import type { SearchMatch } from '@utils/search'
import { useCallback, useEffect, useRef, useState } from 'react'
import styles from './SearchPanel.module.css'

interface SearchPanelProps {
  matches: SearchMatch[]
  isOpen: boolean
  onNavigate: (pageIdx: number) => void
  currentPage: number
}

export default function SearchPanel({
  matches,
  isOpen,
  onNavigate,
  currentPage,
}: SearchPanelProps) {
  const [hoveredMatch, setHoveredMatch] = useState<number | null>(null)
  const [previousPage, setPreviousPage] = useState<number>(currentPage)
  const highlightedElementRef = useRef<HTMLElement | null>(null)

  // Track when we hover to enable preview navigation
  const handleMouseEnter = useCallback(
    (match: SearchMatch, idx: number) => {
      setPreviousPage(currentPage)
      setHoveredMatch(idx)
      onNavigate(match.pageIdx)

      // Apply pulse effect to the matching paragraph
      setTimeout(() => {
        applyHighlight(match)
      }, 300)
    },
    [currentPage, onNavigate],
  )

  // Return to previous page when hover ends
  const handleMouseLeave = useCallback(() => {
    setHoveredMatch(null)
    removeHighlight()
    if (previousPage !== currentPage) {
      onNavigate(previousPage)
    }
  }, [previousPage, currentPage, onNavigate])

  // Find and highlight the matching paragraph
  function applyHighlight(match: SearchMatch) {
    removeHighlight()

    // Find the segment elements on the current page
    const segments = document.querySelectorAll('[data-segment-idx]')
    for (const elem of segments) {
      const segmentIdx = parseInt(elem.getAttribute('data-segment-idx') || '-1', 10)
      if (segmentIdx === match.segmentIdx && elem instanceof HTMLElement) {
        elem.classList.add(styles.highlightedParagraph)
        highlightedElementRef.current = elem
        elem.scrollIntoView({ behavior: 'smooth', block: 'center' })
        break
      }
    }
  }

  function removeHighlight() {
    if (highlightedElementRef.current) {
      highlightedElementRef.current.classList.remove(styles.highlightedParagraph)
      highlightedElementRef.current = null
    }
  }

  useEffect(() => {
    if (!isOpen) {
      setHoveredMatch(null)
      removeHighlight()
    }
  }, [isOpen])

  if (!isOpen || matches.length === 0) {
    return null
  }

  return (
    <div className={styles.panel}>
      <div className={styles.header}>
        <h3 className={styles.title}>
          {matches.length} result{matches.length !== 1 ? 's' : ''}
        </h3>
      </div>

      <div className={styles.results}>
        {matches.map((match, idx) => (
          <button
            key={`${match.pageIdx}-${match.segmentIdx}-${match.matchStart}`}
            className={`${styles.result} ${
              match.pageIdx === currentPage ? styles.current : ''
            } ${hoveredMatch === idx ? styles.hovered : ''}`}
            onClick={() => {
              onNavigate(match.pageIdx)
              setHoveredMatch(null)
              removeHighlight()
            }}
            onMouseEnter={() => handleMouseEnter(match, idx)}
            onMouseLeave={handleMouseLeave}
            title={`Go to page ${match.pageNumber}`}
          >
            <div className={styles.page}>Page {match.pageNumber}</div>
            <div className={styles.context}>
              <span className={styles.before}>{match.contextBefore}</span>
              <span className={styles.match}>{match.matchText}</span>
              <span className={styles.after}>{match.contextAfter}</span>
            </div>
          </button>
        ))}
      </div>
    </div>
  )
}
