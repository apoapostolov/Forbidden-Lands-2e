import BookReader from '@components/BookReader/BookReader'
import bookDataRaw from '@data/book-data.json'
import type { BookData } from '@types/book'

const bookData = bookDataRaw as BookData

export default function App() {
  return <BookReader bookData={bookData} initialPage={0} />
}
