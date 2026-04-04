import styles from './PageBackground.module.css'

interface PageBackgroundProps {
  side: 'left' | 'right'
  children: React.ReactNode
}

/** Parchment page shell — renders the aged paper texture and shadow layers */
export default function PageBackground({ side, children }: PageBackgroundProps) {
  return (
    <div className={`${styles.page} ${side === 'left' ? styles.left : styles.right}`}>
      {/* SVG noise texture overlay */}
      <div className={styles.noiseOverlay} aria-hidden />
      {/* Warm sepia gradient — fades from warm centre toward cooler edges */}
      <div className={styles.gradientOverlay} aria-hidden />
      {/* Spine shadow on the inner edge */}
      <div className={styles.spineGradient} aria-hidden />
      {/* Page content sits on top of all texture layers */}
      <div className={styles.content}>{children}</div>
    </div>
  )
}
