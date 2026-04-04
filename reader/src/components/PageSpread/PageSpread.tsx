import PageBackground from '@components/PageBackground/PageBackground'
import PageHeader from '@components/PageHeader/PageHeader'
import PageFooter from '@components/PageFooter/PageFooter'
import PageContent from '@components/PageContent/PageContent'
import type { BookPage } from '@types/book'

interface PageSpreadProps {
  page: BookPage
  side: 'left' | 'right'
}

/**
 * Renders a single page from book-data.json.
 * Used both in the static preview and as children of the FlipBook.
 */
export default function PageSpread({ page, side }: PageSpreadProps) {
  return (
    <PageBackground side={side}>
      <PageHeader chapterTitle={page.chapterTitle} side={side} />
      <PageContent segments={page.segments} />
      <PageFooter pageNumber={page.pageNumber} side={side} />
    </PageBackground>
  )
}
