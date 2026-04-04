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
  const hasChapterHeading = page.segments.some(
    (seg) => seg.type === 'heading' && 'level' in seg && seg.level === 1,
  )
  const hasSectionHeading = page.segments.some(
    (seg) => seg.type === 'heading' && 'level' in seg && seg.level === 2,
  )

  return (
    <PageBackground side={side}>
      {/* PageHeader removed — using PageHeaderBanner for book-accurate layout */}
      {!hasSectionHeading && <PageHeaderBanner showChapterOverlay={hasChapterHeading} />}
      <PageContent segments={page.segments} sectionHeadingPage={hasSectionHeading} />
      <PageFooter
        pageNumber={page.pageNumber}
        side={side}
        chapterIndex={page.chapterIndex}
        chapterTitle={page.chapterTitle}
      />
    </PageBackground>
  )
}
