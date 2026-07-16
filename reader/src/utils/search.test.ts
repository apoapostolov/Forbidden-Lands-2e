import type { BookData } from '@app-types/book'
import { buildSearchIndex, htmlToText, searchBook } from './search'
import { describe, expect, it } from 'vitest'

const book: BookData = {
  generatedAt: '2026-01-01T00:00:00.000Z',
  totalPages: 1,
  chapters: [],
  toc: [],
  pages: [
    {
      pageNumber: 1,
      chapterTitle: 'Test',
      chapterIndex: 0,
      layout: 'two-column',
      segments: [
        {
          type: 'paragraph',
          uid: 'page-1-segment-0',
          heightPt: 10,
          html: '<p>Mark &amp; Robin <em>survive</em>.</p>',
        },
        {
          type: 'table',
          uid: 'page-1-segment-1',
          heightPt: 10,
          headers: ['Talent'],
          rows: [['Chef']],
        },
      ],
    },
  ],
}

describe('searchBook', () => {
  it('normalizes HTML and trims the query', () => {
    const matches = searchBook(buildSearchIndex(book), '  robin  ')
    expect(matches).toHaveLength(1)
    expect(matches[0]).toMatchObject({
      pageIdx: 0,
      segmentUid: 'page-1-segment-0',
      matchText: 'Robin',
    })
  })

  it('indexes table headers and limits results', () => {
    expect(searchBook(buildSearchIndex(book), 'Talent')).toHaveLength(1)
    expect(searchBook(buildSearchIndex(book), 'i', 1)).toHaveLength(1)
  })
})

describe('htmlToText', () => {
  it('decodes entities without retaining tags', () => {
    expect(htmlToText('<p>A&nbsp;&amp;&nbsp;B</p>')).toBe('A & B')
  })
})
