import type { BookData, Segment } from '@app-types/book'

export const MAX_SEARCH_RESULTS = 200

export interface SearchDocument {
  pageNumber: number
  pageIdx: number
  segmentUid: string
  segmentType: string
  fullText: string
}

export interface SearchMatch extends SearchDocument {
  matchStart: number
  matchEnd: number
  contextBefore: string
  matchText: string
  contextAfter: string
}

const NAMED_ENTITIES: Record<string, string> = {
  amp: '&',
  apos: "'",
  gt: '>',
  lt: '<',
  nbsp: ' ',
  quot: '"',
}

function decodeHtmlEntities(text: string): string {
  return text.replace(/&(#x?[0-9a-f]+|[a-z]+);/giu, (entity, code: string) => {
    if (code.startsWith('#x')) {
      return String.fromCodePoint(Number.parseInt(code.slice(2), 16))
    }
    if (code.startsWith('#')) {
      return String.fromCodePoint(Number.parseInt(code.slice(1), 10))
    }
    return NAMED_ENTITIES[code.toLowerCase()] ?? entity
  })
}

export function htmlToText(html: string): string {
  return decodeHtmlEntities(html.replace(/<[^>]*>/gu, ' '))
    .replace(/\s+/gu, ' ')
    .trim()
}

function getSegmentText(segment: Segment): string {
  switch (segment.type) {
    case 'paragraph':
    case 'blockquote':
      return htmlToText(segment.html)
    case 'heading':
      return segment.text
    case 'table':
      return [segment.headers, ...segment.rows]
        .map((row) => row.map(htmlToText).join(' | '))
        .join(' | ')
    case 'image-ref':
      return [segment.altText, segment.caption].filter(Boolean).join(' ')
    case 'hr':
      return ''
  }
}

export function buildSearchIndex(bookData: BookData): SearchDocument[] {
  return bookData.pages.flatMap((page, pageIdx) =>
    page.segments.flatMap((segment) => {
      const fullText = getSegmentText(segment)
      if (!fullText) return []
      return [
        {
          pageNumber: page.pageNumber,
          pageIdx,
          segmentUid: segment.uid,
          segmentType: segment.type,
          fullText,
        },
      ]
    }),
  )
}

export function searchBook(
  index: SearchDocument[],
  query: string,
  limit = MAX_SEARCH_RESULTS,
  caseSensitive = false,
): SearchMatch[] {
  const normalizedQuery = query.trim()
  if (!normalizedQuery || limit <= 0) return []

  const results: SearchMatch[] = []
  const searchQuery = caseSensitive
    ? normalizedQuery
    : normalizedQuery.toLocaleLowerCase()
  const contextLength = 60

  for (const document of index) {
    const searchText = caseSensitive
      ? document.fullText
      : document.fullText.toLocaleLowerCase()
    let matchIdx = 0

    while ((matchIdx = searchText.indexOf(searchQuery, matchIdx)) !== -1) {
      const matchStart = matchIdx
      const matchEnd = matchIdx + searchQuery.length
      const contextStart = Math.max(0, matchStart - contextLength)
      const contextEnd = Math.min(document.fullText.length, matchEnd + contextLength)

      results.push({
        ...document,
        matchStart,
        matchEnd,
        contextBefore: document.fullText.substring(contextStart, matchStart),
        matchText: document.fullText.substring(matchStart, matchEnd),
        contextAfter: document.fullText.substring(matchEnd, contextEnd),
      })

      if (results.length >= limit) return results
      matchIdx = matchEnd
    }
  }

  return results
}
