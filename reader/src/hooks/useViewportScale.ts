import { useEffect, useState } from 'react'

// Base page dimensions in px (482pt × 680pt, 1pt = 1.333px)
const BASE_PAGE_W = 642
const BASE_PAGE_H = 907
// Spread is two pages wide + small gap
const BASE_SPREAD_W = BASE_PAGE_W * 2 + 4

interface ViewportScale {
  scale: number
  pageWidth: number
  pageHeight: number
}

/**
 * Calculates the CSS scale factor so the two-page spread fills the viewport.
 * Respects both width and height constraints.
 */
export function useViewportScale(): ViewportScale {
  const [scale, setScale] = useState(1)

  useEffect(() => {
    function update() {
      const vw = window.innerWidth - 32 // 16px padding each side
      // Reserve vertical room using ACTUAL nav position/size so we avoid
      // first-render clipping when nav mounts a moment after the reader.
      const nav = document.querySelector(
        'nav[aria-label="Book navigation"]',
      ) as HTMLElement | null
      const navRect = nav?.getBoundingClientRect()

      const topReserve = 16
      const bottomReserve = navRect
        ? Math.max(24, window.innerHeight - navRect.top + 12)
        : 96

      const vh = Math.max(240, window.innerHeight - topReserve - bottomReserve)
      const scaleH = vh / BASE_PAGE_H
      const scaleW = vw / BASE_SPREAD_W
      const rawScale = Math.min(scaleH, scaleW, 1)
      const safeScale = rawScale * 0.98
      setScale(safeScale)
    }

    update()
    // Re-run after first paint + shortly after mount to capture late nav layout.
    const raf1 = requestAnimationFrame(update)
    const raf2 = requestAnimationFrame(update)
    const t1 = window.setTimeout(update, 120)
    const t2 = window.setTimeout(update, 420)

    window.addEventListener('resize', update)
    window.addEventListener('fullscreenchange', update)

    return () => {
      cancelAnimationFrame(raf1)
      cancelAnimationFrame(raf2)
      window.clearTimeout(t1)
      window.clearTimeout(t2)
      window.removeEventListener('resize', update)
      window.removeEventListener('fullscreenchange', update)
    }
  }, [])

  return { scale, pageWidth: BASE_PAGE_W, pageHeight: BASE_PAGE_H }
}
