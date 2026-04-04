import type { BookData, Segment } from '@app-types/book'

export interface SearchMatch {
  pageNumber: number
  pageIdx: number
  segmentIdx: number
  segmentType: string
  matchStart: number
  matchEnd: number
  contextBefore: string
  matchText: string
  contextAfter: string
  fullText: string
}

/**
 * Extract plain text from HTML (simple approach - removes tags)
 */
function stripHtml(html: string): string {
  return html.replace(/<[^>]*>/g, '')
}

/**
 * Get plain text representation of a segment
 */
function getSegmentText(segment: Segment): string {
  switch (segment.type) {
    case 'paragraph':
      return stripHtml(segment.html)
    case 'heading':
      return segment.text
    case 'blockquote':
      return stripHtml(segment.html)
    case 'hr':
    case 'image-ref':
      return ''
    case 'table':
      // Simple table representation
      return segment.rows.map((row) => row.join(' | ')).join(' | ')
    default:
      return ''
  }
}

/**
 * Search through all pages and find matches
 */
export function searchBook(
  bookData: BookData,
  query: string,
  caseSensitive = false
): SearchMatch[] {
  if (!query.trim()) return []

  const results: SearchMatch[] = []
  const searchQuery = caseSensitive ? query : query.toLowerCase()
  const contextLength = 60 // characters before/after match

  for (let pageIdx = 0; pageIdx < bookData.pages.length; pageIdx++) {
    const page = bookData.pages[pageIdx]

    for (let segIdx = 0; segIdx < page.segments.length; segIdx++) {
      const segment = page.segments[segIdx]
      const fullText = getSegmentText(segment)

      if (!fullText) continue

      const searchText = caseSensitive ? fullText : fullText.toLowerCase()
      let matchIdx = 0

      while ((matchIdx = searchText.indexOf(searchQuery, matchIdx)) !== -1) {
        const matchStart = matchIdx
        const matchEnd = matchIdx + searchQuery.length

        // Get context
        const contextStart = Math.max(0, matchStart - contextLength)
        const contextEnd = Math.min(fullText.length, matchEnd + contextLength)

        const contextBefore = fullText.substring(contextStart, matchStart)
        const matchText = fullText.substring(matchStart, matchEnd)
        const contextAfter = fullText.substring(matchEnd, contextEnd)

        results.push({
          pageNumber: page.pageNumber,
          pageIdx,
          segmentIdx: segIdx,
          segmentType: segment.type,
          matchStart,
          matchEnd,
          contextBefore,
          matchText,
          contextAfter,
          fullText,
        })

        matchIdx = matchEnd
      }
    }
  }

  return results
}
