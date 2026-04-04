import { useEffect, useRef } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import type { TocEntry } from '@types/book'
import styles from './TableOfContents.module.css'

interface TableOfContentsProps {
  entries: TocEntry[]
  currentPage: number
  isOpen: boolean
  onClose: () => void
  onNavigate: (page: number) => void
}

export default function TableOfContents({
  entries,
  currentPage,
  isOpen,
  onClose,
  onNavigate,
}: TableOfContentsProps) {
  const panelRef = useRef<HTMLDivElement>(null)

  // Close on Escape
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === 'Escape' && isOpen) onClose()
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [isOpen, onClose])

  // Close on outside click
  useEffect(() => {
    function onClick(e: MouseEvent) {
      if (panelRef.current && !panelRef.current.contains(e.target as Node)) {
        onClose()
      }
    }
    if (isOpen) document.addEventListener('mousedown', onClick)
    return () => document.removeEventListener('mousedown', onClick)
  }, [isOpen, onClose])

  function levelClass(level: number): string {
    if (level === 1) return styles.l1
    if (level === 2) return styles.l2
    return styles.l3
  }

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            className={styles.backdrop}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
          />

          {/* Panel */}
          <motion.div
            ref={panelRef}
            className={styles.panel}
            initial={{ x: '-100%' }}
            animate={{ x: 0 }}
            exit={{ x: '-100%' }}
            transition={{ type: 'spring', stiffness: 380, damping: 40 }}
            role="navigation"
            aria-label="Table of contents"
          >
            <div className={styles.header}>
              <span className={`${styles.title} small-caps-deco`}>
                Contents
              </span>
              <button
                className={styles.closeBtn}
                onClick={onClose}
                aria-label="Close table of contents"
              >
                ✕
              </button>
            </div>

            <hr className="gold-rule" />

            <ul className={styles.list}>
              {entries.map((entry, i) => {
                const isActive = entry.page <= currentPage + 1 &&
                  (entries[i + 1] ? entries[i + 1].page > currentPage + 1 : true)
                return (
                  <li
                    key={i}
                    className={`${styles.item} ${levelClass(entry.level)} ${isActive ? styles.active : ''}`}
                  >
                    <button
                      className={styles.entryBtn}
                      onClick={() => {
                        onNavigate(entry.page - 1)
                        onClose()
                      }}
                    >
                      <span className={styles.entryTitle}>{entry.title}</span>
                      <span className={styles.entryPage}>{entry.page}</span>
                    </button>
                  </li>
                )
              })}
            </ul>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  )
}
