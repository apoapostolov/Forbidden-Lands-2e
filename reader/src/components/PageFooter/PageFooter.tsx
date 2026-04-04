import styles from './PageFooter.module.css'

interface PageFooterProps {
  pageNumber: number
  side: 'left' | 'right'
}

export default function PageFooter({ pageNumber, side }: PageFooterProps) {
  return (
    <footer
      className={`${styles.footer} ${side === 'left' ? styles.left : styles.right}`}
    >
      <img
        src="/assets/decorations/skull-separator.png"
        className={styles.decorImage}
        alt=""
        aria-hidden="true"
      />
      <span className={`${styles.number} small-caps-deco`}>{pageNumber}</span>
    </footer>
  )
}
