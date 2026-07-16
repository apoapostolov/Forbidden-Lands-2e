import type { TocEntry } from '@app-types/book'
import { useEffect, useRef } from 'react'
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
  const dialogRef = useRef<HTMLDialogElement>(null)

  useEffect(() => {
    const dialog = dialogRef.current
    if (!dialog) return
    if (isOpen && !dialog.open) dialog.showModal()
    else if (!isOpen && dialog.open) dialog.close()
  }, [isOpen])

  function levelClass(level: number): string {
    if (level === 1) return styles.l1
    if (level === 2) return styles.l2
    return styles.l3
  }

  return (
    <dialog
      ref={dialogRef}
      className={styles.panel}
      aria-labelledby="toc-title"
      onCancel={(event) => {
        event.preventDefault()
        onClose()
      }}
      onClose={onClose}
      onClick={(event) => {
        if (event.target === event.currentTarget) onClose()
      }}
    >
      <div className={styles.dialogContent}>
        <div className={styles.header}>
          <h2 id="toc-title" className={`${styles.title} small-caps-deco`}>
            Contents
          </h2>
          <button
            type="button"
            className={styles.closeBtn}
            onClick={onClose}
            aria-label="Close table of contents"
          >
            ✕
          </button>
        </div>

        <hr className="gold-rule" />

        <nav aria-label="Table of contents">
          <ul className={styles.list} role="list">
            {entries.map((entry, entryIndex) => {
              const nextEntry = entries[entryIndex + 1]
              const isActive =
                entry.page <= currentPage + 1 &&
                (nextEntry ? nextEntry.page > currentPage + 1 : true)
              return (
                <li
                  key={`${entry.level}-${entry.title}-${entry.page}`}
                  className={`${styles.item} ${levelClass(entry.level)} ${
                    isActive ? styles.active : ''
                  }`}
                >
                  <button
                    type="button"
                    className={styles.entryBtn}
                    aria-current={isActive ? 'page' : undefined}
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
        </nav>
      </div>
    </dialog>
  )
}
