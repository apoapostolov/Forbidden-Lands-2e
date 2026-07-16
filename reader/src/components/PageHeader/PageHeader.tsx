import styles from './PageHeader.module.css'

interface PageHeaderProps {
  chapterTitle: string
  side: 'left' | 'right'
}

export default function PageHeader({ chapterTitle, side }: PageHeaderProps) {
  return (
    <header
      className={`${styles.header} ${side === 'left' ? styles.left : styles.right}`}
    >
      <span className={`${styles.title} small-caps-deco`}>{chapterTitle}</span>
      <div className={styles.rule} />
    </header>
  )
}
