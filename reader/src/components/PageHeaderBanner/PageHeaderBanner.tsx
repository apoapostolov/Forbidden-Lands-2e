/**
 * PageHeaderBanner - Landscape illustration header on each page
 * Extracted from PDF as img_00074_p0006.png
 * Appears at top of content pages (6+)
 */

import styles from './PageHeaderBanner.module.css'

interface PageHeaderBannerProps {
  showChapterOverlay?: boolean
}

export default function PageHeaderBanner({
  showChapterOverlay = false,
}: PageHeaderBannerProps) {
  return (
    <div className={styles.banner}>
      <img
        src="/assets/decorations/header-banner.png"
        alt="Header banner - Forbidden Lands landscape"
        className={styles.bannerImage}
      />
      {showChapterOverlay && (
        <img
          src="/assets/decorations/chapter-header-overlay.png"
          alt=""
          aria-hidden="true"
          className={styles.bannerOverlay}
        />
      )}
    </div>
  )
}
