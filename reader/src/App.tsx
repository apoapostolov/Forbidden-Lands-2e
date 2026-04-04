import type { BookData } from '@app-types/book'
import BookReader, { BookReaderHandle } from '@components/BookReader/BookReader'
import NavBar from '@components/NavBar/NavBar'
import SearchPanel from '@components/SearchPanel/SearchPanel'
import TableOfContents from '@components/TableOfContents/TableOfContents'
import bookDataRaw from '@data/book-data.json'
import { searchBook } from '@utils/search'
import { useCallback, useEffect, useMemo, useRef, useState } from 'react'

const bookData = bookDataRaw as BookData

/** Read initial page from URL hash synchronously before first render. */
function readHashPage(): number {
  const m = window.location.hash.match(/^#page\/(\d+)$/)
  if (!m) return -1
  const n = parseInt(m[1], 10)
  if (isNaN(n)) return -1

  // URL hash is human-facing (1-based): #page/1 is the first numbered page.
  // Convert to the reader's logical 0-based index.
  const logical = n - 1
  return Math.min(Math.max(0, logical), bookData.totalPages - 1)
}

const INITIAL_PAGE = readHashPage()

export default function App() {
  const readerRef = useRef<BookReaderHandle>(null)
  const [currentPage, setCurrentPage] = useState(INITIAL_PAGE)
  const [tocOpen, setTocOpen] = useState(false)
  const [searchValue, setSearchValue] = useState('')

  // Compute search results
  const searchResults = useMemo(() => {
    return searchBook(bookData, searchValue)
  }, [searchValue])

  /** Called by BookReader whenever a page flip completes. */
  const handlePageChange = useCallback((page: number) => {
    setCurrentPage(page)
    if (page < 0) {
      history.replaceState(null, '', '#')
      return
    }
    history.replaceState(null, '', `#page/${page + 1}`)
  }, [])

  /** 'T' key toggles the TOC panel (treated as a keyboard shortcut). */
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

  return (
    <>
      <BookReader
        ref={readerRef}
        bookData={bookData}
        initialPage={INITIAL_PAGE}
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
