// @vitest-environment node

import type { BookData } from '@app-types/book'
import { readFileSync } from 'node:fs'
import { describe, expect, it } from 'vitest'

const bookData = JSON.parse(
  readFileSync(new URL('../public/book-data.json', import.meta.url), 'utf8'),
) as BookData

describe('generated book data', () => {
  it('contains every required chapter and at least one page', () => {
    expect(bookData.chapters).toHaveLength(11)
    expect(bookData.pages.length).toBeGreaterThan(0)
    expect(bookData.totalPages).toBe(bookData.pages.length)
  })

  it('assigns a unique stable identifier to every segment', () => {
    const uids = bookData.pages.flatMap((page) =>
      page.segments.map((segment) => segment.uid),
    )
    expect(uids.every(Boolean)).toBe(true)
    expect(new Set(uids).size).toBe(uids.length)
  })

  it('emits explicit right-column markers', () => {
    expect(
      bookData.pages.some((page) =>
        page.segments.some((segment) => segment.id === '__column_break__'),
      ),
    ).toBe(true)
  })

  it('starts the second credits column with the artwork credits', () => {
    const creditsPage = bookData.pages[0]
    const columnBreakIndex = creditsPage.segments.findIndex(
      (segment) => segment.id === '__column_break__',
    )
    const secondColumnStart = creditsPage.segments[columnBreakIndex + 1]

    expect(columnBreakIndex).toBeGreaterThan(0)
    expect(secondColumnStart).toMatchObject({
      type: 'heading',
      level: 3,
      text: 'ILLUSTRATIONS & GRAPHICS',
    })
  })
})
