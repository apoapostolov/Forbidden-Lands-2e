import { useCallback, useEffect } from 'react'

/**
 * Reads initial page from URL hash `#page/42` and
 * updates the hash whenever the page changes.
 */
export function useHashPage(onNavigate: (page: number) => void) {
  // Parse hash on mount → navigate to that page
  useEffect(() => {
    const match = window.location.hash.match(/^#page\/(\d+)$/)
    if (match) {
      const p = parseInt(match[1], 10)
      if (!isNaN(p) && p >= 0) onNavigate(p)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const setHash = useCallback((page: number) => {
    history.replaceState(null, '', `#page/${page}`)
  }, [])

  return { setHash }
}
