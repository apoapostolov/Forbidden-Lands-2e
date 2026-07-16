import type { BookData } from '@app-types/book'
import BookReader, { type BookReaderHandle } from '@components/BookReader/BookReader'
import NavBar from '@components/NavBar/NavBar'
import SearchPanel from '@components/SearchPanel/SearchPanel'
import TableOfContents from '@components/TableOfContents/TableOfContents'
import { isEditableTarget } from '@utils/keyboard'
import { buildSearchIndex, searchBook, type SearchMatch } from '@utils/search'
import {
  useCallback,
  useDeferredValue,
  useEffect,
  useMemo,
  useRef,
  useState,
} from 'react'
import styles from './App.module.css'

function readHashPage(totalPages: number): number {
  const match = window.location.hash.match(/^#page\/(\d+)$/u)
  if (!match) return -1
  const pageNumber = Number.parseInt(match[1], 10)
  if (!Number.isFinite(pageNumber)) return -1
  return Math.min(Math.max(0, pageNumber - 1), totalPages - 1)
}

export default function App() {
  const readerRef = useRef<BookReaderHandle>(null)
  const [bookData, setBookData] = useState<BookData | null>(null)
  const [loadError, setLoadError] = useState<string | null>(null)
  const [tocOpen, setTocOpen] = useState(false)
  const [searchValue, setSearchValue] = useState('')
  const [currentPage, setCurrentPage] = useState(-1)
  const deferredSearchValue = useDeferredValue(searchValue)
  const searchIndex = useMemo(
    () => (bookData ? buildSearchIndex(bookData) : []),
    [bookData],
  )
  const searchResults = useMemo(
    () => searchBook(searchIndex, deferredSearchValue),
    [deferredSearchValue, searchIndex],
  )

  const handlePageChange = useCallback((page: number) => {
    setCurrentPage(page)
    history.replaceState(null, '', page < 0 ? '#' : `#page/${page + 1}`)
  }, [])

  const navigateToSearchMatch = useCallback((match: SearchMatch) => {
    readerRef.current?.goToPage(match.pageIdx)
  }, [])

  const closeToc = useCallback(() => setTocOpen(false), [])
  const navigateFromToc = useCallback((page: number) => {
    readerRef.current?.goToPageInstant(page)
  }, [])

  useEffect(() => {
    const controller = new AbortController()
    fetch('/book-data.json', { signal: controller.signal })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Book data request failed (${response.status})`)
        }
        return response.json() as Promise<BookData>
      })
      .then((data) => {
        if (!Array.isArray(data.pages) || data.pages.length === 0) {
          throw new Error('Book data contains no pages')
        }
        setBookData(data)
        setCurrentPage(readHashPage(data.totalPages))
      })
      .catch((error: unknown) => {
        if (error instanceof DOMException && error.name === 'AbortError') return
        setLoadError(error instanceof Error ? error.message : String(error))
      })
    return () => controller.abort()
  }, [])

  useEffect(() => {
    function onKey(event: KeyboardEvent) {
      if (
        event.defaultPrevented ||
        event.ctrlKey ||
        event.metaKey ||
        event.altKey ||
        isEditableTarget(event.target)
      ) {
        return
      }
      if (event.key.toLocaleLowerCase() === 't') {
        event.preventDefault()
        setTocOpen((open) => !open)
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  if (!bookData) {
    return (
      <main className={styles.loadingState} aria-busy={!loadError}>
        {loadError ? (
          <div role="alert">
            <h1>Reader unavailable</h1>
            <p>{loadError}</p>
          </div>
        ) : (
          <p>Loading the Forbidden Lands…</p>
        )}
      </main>
    )
  }

  return (
    <div className={styles.appShell}>
      <a className={styles.skipLink} href="#reader-content">
        Skip to book content
      </a>

      <BookReader
        ref={readerRef}
        bookData={bookData}
        currentPage={currentPage}
        onPageChange={handlePageChange}
      />

      <NavBar
        currentPage={currentPage}
        totalPages={bookData.totalPages}
        onGoToInstant={(page) => readerRef.current?.goToPageInstant(page)}
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
        query={deferredSearchValue}
        isOpen={searchValue.trim().length > 0}
        onNavigate={navigateToSearchMatch}
        currentPage={currentPage}
      />

      <TableOfContents
        entries={bookData.toc}
        currentPage={currentPage}
        isOpen={tocOpen}
        onClose={closeToc}
        onNavigate={navigateFromToc}
      />
    </div>
  )
}
