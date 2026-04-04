import type { BookPage } from '@app-types/book'
import PageBackground from '@components/PageBackground/PageBackground'
import PageContent from '@components/PageContent/PageContent'
import PageFooter from '@components/PageFooter/PageFooter'
import PageHeaderBanner from '@components/PageHeaderBanner/PageHeaderBanner'

interface PageSpreadProps {
  page: BookPage
  side: 'left' | 'right'
}

/**
 * Renders a single page from book-data.json.
 * Used both in the static preview and as children of the FlipBook.
 *
 * NOTE: PageHeader (modern running head) removed in favor of PageHeaderBanner
 * (book-accurate decorative banner) for authentic FL book layout.
 */
export default function PageSpread({ page, side }: PageSpreadProps) {
  return (
    <PageBackground side={side}>
      {/* PageHeader removed — using PageHeaderBanner for book-accurate layout */}
      <PageHeaderBanner />
      <PageContent segments={page.segments} />
      <PageFooter
        pageNumber={page.pageNumber}
        side={side}
        chapterIndex={page.chapterIndex}
        chapterTitle={page.chapterTitle}
      />
    </PageBackground>
  )
}
