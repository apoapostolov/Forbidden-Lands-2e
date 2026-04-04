import styles from './PageBackground.module.css'

interface PageBackgroundProps {
  side: 'left' | 'right'
  children: React.ReactNode
}

/** White page shell — no texture, clean paper matching the FL01 print edition */
export default function PageBackground({ side, children }: PageBackgroundProps) {
  return (
    <div className={`${styles.page} ${side === 'left' ? styles.left : styles.right}`}>
      <div className={styles.content}>{children}</div>
    </div>
  )
}
