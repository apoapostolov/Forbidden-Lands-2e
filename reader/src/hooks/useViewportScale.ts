import { useEffect, useState } from 'react'

const BASE_PAGE_WIDTH = 642
const BASE_PAGE_HEIGHT = 907
const BASE_SPREAD_WIDTH = BASE_PAGE_WIDTH * 2 + 4
const SINGLE_PAGE_QUERY = '(max-width: 900px), (orientation: portrait)'

interface ViewportScale {
  scale: number
  singlePage: boolean
}

function getSinglePagePreference(): boolean {
  return window.matchMedia(SINGLE_PAGE_QUERY).matches
}

export function useViewportScale(): ViewportScale {
  const [viewport, setViewport] = useState<ViewportScale>(() => ({
    scale: 1,
    singlePage: getSinglePagePreference(),
  }))

  useEffect(() => {
    const media = window.matchMedia(SINGLE_PAGE_QUERY)
    const nav = document.querySelector<HTMLElement>('nav[aria-label="Book navigation"]')

    function update() {
      const singlePage = media.matches
      if (singlePage) {
        setViewport({ scale: 1, singlePage: true })
        return
      }

      const navRect = nav?.getBoundingClientRect()
      const availableWidth = window.innerWidth - 32
      const bottomReserve = navRect
        ? Math.max(24, window.innerHeight - navRect.top + 12)
        : 96
      const availableHeight = Math.max(240, window.innerHeight - 16 - bottomReserve)
      const scale = Math.min(
        availableHeight / BASE_PAGE_HEIGHT,
        availableWidth / BASE_SPREAD_WIDTH,
        1,
      )
      setViewport({ scale: scale * 0.98, singlePage: false })
    }

    update()
    const frame = requestAnimationFrame(update)
    const observer = nav ? new ResizeObserver(update) : null
    observer?.observe(nav as HTMLElement)
    media.addEventListener('change', update)
    window.addEventListener('resize', update)
    window.addEventListener('fullscreenchange', update)

    return () => {
      cancelAnimationFrame(frame)
      observer?.disconnect()
      media.removeEventListener('change', update)
      window.removeEventListener('resize', update)
      window.removeEventListener('fullscreenchange', update)
    }
  }, [])

  return viewport
}
