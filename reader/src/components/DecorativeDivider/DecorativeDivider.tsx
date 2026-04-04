/**
 * DecorativeDivider - Skull and line separator between sections
 * Extracted from PDF as img_00070_p0006.png
 */

import styles from './DecorativeDivider.module.css'

interface DecorativeDividerProps {
  variant?: 'skull' | 'line'
}

export default function DecorativeDivider({ variant = 'skull' }: DecorativeDividerProps) {
  return (
    <div className={styles.divider} data-variant={variant}>
      {variant === 'skull' && (
        <img
          src="/assets/decorations/skull-separator.png"
          alt="Decorative separator"
          className={styles.skullSeparator}
        />
      )}
      {variant === 'line' && <div className={styles.line} />}
    </div>
  )
}
