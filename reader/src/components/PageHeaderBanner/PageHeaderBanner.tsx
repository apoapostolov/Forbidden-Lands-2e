/**
 * PageHeaderBanner - Landscape illustration header on each page
 * Extracted from PDF as img_00074_p0006.png
 * Appears at top of content pages (6+)
 */

import styles from './PageHeaderBanner.module.css'

export default function PageHeaderBanner() {
  return (
    <div className={styles.banner}>
      <img
        src="/assets/decorations/header-banner.png"
        alt="Header banner - Forbidden Lands landscape"
        className={styles.bannerImage}
      />
    </div>
  )
}
