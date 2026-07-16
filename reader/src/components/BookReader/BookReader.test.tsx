import type { BookData, BookPage } from '@app-types/book'
import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import BookReader from './BookReader'

const viewport = vi.hoisted(() => ({ singlePage: false }))

vi.mock('@hooks/useViewportScale', () => ({
  useViewportScale: () => ({ scale: 1, singlePage: viewport.singlePage }),
}))

vi.mock('@components/CoverPage/CoverPage', () => ({
  default: () => <div>Cover</div>,
}))

vi.mock('@components/PageSpread/PageSpread', () => ({
  default: ({ page }: { page: BookPage }) => <div>Page {page.pageNumber}</div>,
}))

const pages: BookPage[] = Array.from({ length: 6 }, (_, index) => ({
  pageNumber: index + 1,
  chapterTitle: 'Test chapter',
  chapterIndex: 0,
  layout: 'two-column',
  segments: [],
}))

const bookData: BookData = {
  generatedAt: '2026-07-16T00:00:00.000Z',
  totalPages: pages.length,
  chapters: [],
  toc: [],
  pages,
}

describe('BookReader navigation', () => {
  beforeEach(() => {
    viewport.singlePage = false
  })

  afterEach(cleanup)

  it('advances and reverses by a full spread in two-page mode', () => {
    const onPageChange = vi.fn()
    const { rerender } = render(
      <BookReader bookData={bookData} currentPage={0} onPageChange={onPageChange} />,
    )

    fireEvent.click(screen.getByRole('button', { name: 'Next page' }))
    expect(onPageChange).toHaveBeenLastCalledWith(2)

    rerender(
      <BookReader bookData={bookData} currentPage={2} onPageChange={onPageChange} />,
    )
    fireEvent.click(screen.getByRole('button', { name: 'Previous page' }))
    expect(onPageChange).toHaveBeenLastCalledWith(0)
  })

  it('advances one page at a time in single-page mode', () => {
    viewport.singlePage = true
    const onPageChange = vi.fn()
    render(
      <BookReader bookData={bookData} currentPage={0} onPageChange={onPageChange} />,
    )

    fireEvent.click(screen.getByRole('button', { name: 'Next page' }))
    expect(onPageChange).toHaveBeenLastCalledWith(1)
  })

  it('opens page 1 when advancing from the cover in spread mode', () => {
    const onPageChange = vi.fn()
    render(
      <BookReader bookData={bookData} currentPage={-1} onPageChange={onPageChange} />,
    )

    fireEvent.click(screen.getByRole('button', { name: 'Next page' }))
    expect(onPageChange).toHaveBeenLastCalledWith(0)
  })

  it('uses the spread step for keyboard navigation', () => {
    const onPageChange = vi.fn()
    render(
      <BookReader bookData={bookData} currentPage={2} onPageChange={onPageChange} />,
    )

    fireEvent.keyDown(window, { key: 'ArrowRight' })
    expect(onPageChange).toHaveBeenLastCalledWith(4)

    fireEvent.keyDown(window, { key: 'ArrowLeft' })
    expect(onPageChange).toHaveBeenLastCalledWith(0)
  })
})
