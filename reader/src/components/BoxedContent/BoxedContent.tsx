/**
 * BoxedContent - Frame a section with decorative top/bottom
 * Used for special rule boxes, examples, etc.
 * Extracted from PDF: img_02085_p0025.png (top), img_02086_p0025.png (bottom)
 */

import styles from './BoxedContent.module.css'

interface BoxedContentProps {
  children: React.ReactNode
  title?: string
}

export default function BoxedContent({ children, title }: BoxedContentProps) {
  return (
    <div className={styles.boxedContent}>
      <div className={styles.boxTop}>
        <img
          src="/assets/decorations/box-top.png"
          alt="Box top decoration"
          className={styles.topImage}
        />
      </div>

      <div className={styles.boxBody}>
        {title && <h4 className={styles.boxTitle}>{title}</h4>}
        <div className={styles.content}>{children}</div>
      </div>

      <div className={styles.boxBottom}>
        <img
          src="/assets/decorations/box-bottom.png"
          alt="Box bottom decoration"
          className={styles.bottomImage}
        />
      </div>
    </div>
  )
}
