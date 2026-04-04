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
      <div className={styles.container}>
        <div className={styles.ornament} />
        <span className={`${styles.number} small-caps-deco`}>{pageNumber}</span>
        <div className={styles.ornament} />
      </div>
    </footer>
  )
}
