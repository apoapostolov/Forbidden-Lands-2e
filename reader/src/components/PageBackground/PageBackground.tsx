import styles from './PageBackground.module.css'

interface PageBackgroundProps {
  side: 'left' | 'right'
  pageNumber?: number
  children: React.ReactNode
}

/** White page shell — no texture, clean paper matching the FL01 print edition */
export default function PageBackground({
  side,
  pageNumber,
  children,
}: PageBackgroundProps) {
  return (
    <article
      className={`${styles.page} ${side === 'left' ? styles.left : styles.right}`}
      aria-label={pageNumber ? `Book page ${pageNumber}` : 'Book cover'}
      data-book-page={pageNumber}
    >
      <div className={styles.content} data-page-content-shell>
        {children}
      </div>
    </article>
  )
}
