import type { BookData, Segment } from '@app-types/book'
import BookReader, { BookReaderHandle } from '@components/BookReader/BookReader'
import NavBar from '@components/NavBar/NavBar'
import SearchPanel from '@components/SearchPanel/SearchPanel'
import TableOfContents from '@components/TableOfContents/TableOfContents'
import bookDataRaw from '@data/book-data.json'
import { PAGE_METRICS, useFlowPagination } from '@hooks/useFlowPagination'
import { searchBook } from '@utils/search'
import { useCallback, useEffect, useMemo, useRef, useState } from 'react'

/**
 * Extract chapters from the preprocessor output for the flow engine.
 * The preprocessor now produces a flat segment list per chapter;
 * the flow engine handles all pagination at runtime.
 */
function extractChapters(data: BookData): Array<{
  title: string
  index: number
  segments: Segment[]
}> {
  // Group pages by chapter to extract segments
  const chapterMap = new Map<number, { title: string; segments: Segment[] }>()

  for (const page of data.pages) {
    const existing = chapterMap.get(page.chapterIndex)
    if (existing) {
      existing.segments.push(...page.segments)
    } else {
      chapterMap.set(page.chapterIndex, {
        title: page.chapterTitle,
        segments: [...page.segments],
      })
    }
  }

  return Array.from(chapterMap.entries())
    .sort(([a], [b]) => a - b)
    .map(([index, { title, segments }]) => ({ title, index, segments }))
}

const rawData = bookDataRaw as BookData
const chapters = extractChapters(rawData)

/** Read initial page from URL hash synchronously before first render. */
function readHashPage(totalPages: number): number {
  const m = window.location.hash.match(/^#page\/(\d+)$/)
  if (!m) return -1
  const n = parseInt(m[1], 10)
  if (isNaN(n)) return -1
  const logical = n - 1
  return Math.min(Math.max(0, logical), totalPages - 1)
}

export default function App() {
  const readerRef = useRef<BookReaderHandle>(null)
  const [tocOpen, setTocOpen] = useState(false)
  const [searchValue, setSearchValue] = useState('')

  // Run the flow engine to paginate content using real DOM measurements
  const { bookData, isReady, error } = useFlowPagination({
    chapters,
    tocEntries: rawData.toc,
    columnWidth: PAGE_METRICS.columnWidth,
    contentWidth: PAGE_METRICS.contentWidth,
    columnHeight: PAGE_METRICS.contentHeight,
    sectionHeadingColumnHeight: PAGE_METRICS.sectionHeadingContentHeight,
  })

  const [currentPage, setCurrentPage] = useState(-1)

  // Set initial page once flow engine completes
  useEffect(() => {
    if (isReady && bookData) {
      const initial = readHashPage(bookData.totalPages)
      setCurrentPage(initial)
    }
  }, [isReady, bookData])

  // Compute search results
  const searchResults = useMemo(() => {
    if (!bookData) return []
    return searchBook(bookData, searchValue)
  }, [bookData, searchValue])

  /** Called by BookReader whenever a page flip completes. */
  const handlePageChange = useCallback((page: number) => {
    setCurrentPage(page)
    if (page < 0) {
      history.replaceState(null, '', '#')
      return
    }
    history.replaceState(null, '', `#page/${page + 1}`)
  }, [])

  /** 'T' key toggles the TOC panel. */
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      const tag = (e.target as HTMLElement).tagName
      if ((e.key === 't' || e.key === 'T') && tag !== 'INPUT' && tag !== 'TEXTAREA') {
        setTocOpen((open) => !open)
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  // Show loading state while flow engine runs
  if (!isReady || !bookData) {
    return (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100vh',
          color: '#8b7355',
          fontFamily: 'var(--font-body)',
          fontSize: '18px',
          background: '#1c1c1c',
        }}
      >
        {error ? (
          <div style={{ color: '#cc4444', textAlign: 'center' }}>
            <p>Flow engine error:</p>
            <p style={{ fontSize: '14px', opacity: 0.7 }}>{error}</p>
          </div>
        ) : (
          <p>Paginating…</p>
        )}
      </div>
    )
  }

  return (
    <>
      <BookReader
        ref={readerRef}
        bookData={bookData}
        initialPage={currentPage}
        onPageChange={handlePageChange}
      />

      <NavBar
        currentPage={currentPage}
        totalPages={bookData.totalPages}
        onGoToInstant={(p) => readerRef.current?.goToPageInstant(p)}
        onPrev={() => readerRef.current?.prevPage()}
        onPrevInstant={() => readerRef.current?.prevPageInstant()}
        onNext={() => readerRef.current?.nextPage()}
        onNextInstant={() => readerRef.current?.nextPageInstant()}
        onTocOpen={() => setTocOpen(true)}
        searchValue={searchValue}
        onSearchChange={setSearchValue}
      />

      <SearchPanel
        matches={searchResults}
        isOpen={searchValue.length > 0}
        onNavigate={(p) => {
          readerRef.current?.goToPage(p)
          setCurrentPage(p)
          history.replaceState(null, '', `#page/${p + 1}`)
        }}
        currentPage={currentPage}
      />

      <TableOfContents
        entries={bookData.toc}
        currentPage={currentPage}
        isOpen={tocOpen}
        onClose={() => setTocOpen(false)}
        onNavigate={(p) => {
          readerRef.current?.goToPageInstant(p)
          setCurrentPage(p)
          history.replaceState(null, '', `#page/${p + 1}`)
        }}
      />
    </>
  )
}
