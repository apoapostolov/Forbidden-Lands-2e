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
      const vh = window.innerHeight - 32 // 16px padding each side
      const scaleH = vh / BASE_PAGE_H
      const scaleW = vw / BASE_SPREAD_W
      setScale(Math.min(scaleH, scaleW, 1)) // never upscale beyond 100%
    }
    update()
    window.addEventListener('resize', update)
    return () => window.removeEventListener('resize', update)
  }, [])

  return { scale, pageWidth: BASE_PAGE_W, pageHeight: BASE_PAGE_H }
}
