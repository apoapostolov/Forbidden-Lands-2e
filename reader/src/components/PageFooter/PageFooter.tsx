import styles from './PageFooter.module.css'

interface PageFooterProps {
  pageNumber: number
  side: 'left' | 'right'
  chapterTitle: string
}

export default function PageFooter({ pageNumber, side, chapterTitle }: PageFooterProps) {
  const chapterLabel = chapterTitle.toUpperCase()

  return (
    <footer
      className={`${styles.footer} ${side === 'left' ? styles.left : styles.right}`}
      data-page-footer
    >
      {/* Decorative skull separator with text overlaid in the image areas */}
      <div className={styles.ornamentWrap}>
        <img
          src="/assets/decorations/skull-separator.png"
          className={styles.decorImage}
          alt=""
          aria-hidden="true"
        />
        {/* Page number sits over the skull head center (~32% from top) */}
        <span className={`${styles.number} small-caps-deco`}>{pageNumber}</span>
        <span className={styles.chapterLabel}>{chapterLabel}</span>
      </div>
    </footer>
  )
}
