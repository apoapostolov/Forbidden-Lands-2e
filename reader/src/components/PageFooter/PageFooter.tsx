import styles from './PageFooter.module.css'

interface PageFooterProps {
  pageNumber: number
  side: 'left' | 'right'
  chapterIndex: number
  chapterTitle: string
}

export default function PageFooter({
  pageNumber,
  side,
  chapterIndex,
  chapterTitle,
}: PageFooterProps) {
  return (
    <footer
      className={`${styles.footer} ${side === 'left' ? styles.left : styles.right}`}
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
        {/* Chapter label sits between the two horizontal decorative lines (~73% from top) */}
        <span className={styles.chapterLabel}>
          {chapterIndex}.&nbsp;{chapterTitle.toUpperCase()}
        </span>
      </div>
    </footer>
  )
}
