import type {
    BlockquoteSegment,
    HeadingSegment,
    ImageRefSegment,
    ParagraphSegment,
    Segment,
    TableSegment,
} from '@app-types/book'
import ImageBlock from '@components/ImageBlock/ImageBlock'
import TableBlock from '@components/TableBlock/TableBlock'
import TextBlock from '@components/TextBlock/TextBlock'
import styles from './PageContent.module.css'

interface PageContentProps {
  segments: Segment[]
  sectionHeadingPage?: boolean
  pageNumber?: number
  chapterIndex?: number
}

function renderSegment(
  seg: Segment,
  idx: number,
  segments: Segment[],
  pageNumber?: number,
  chapterIndex?: number,
) {
  const previousSegment = idx > 0 ? segments[idx - 1] : null

  // Chapter fiction is ONLY the blockquote directly after an H2 section heading.
  const isChapterFictionAfterH2 =
    seg.type === 'blockquote' &&
    previousSegment?.type === 'heading' &&
    (previousSegment as HeadingSegment).level === 2

  // First prose paragraph after chapter fiction gets chapter-opener treatment.
  const isFirstParagraphAfterChapterFiction =
    seg.type === 'paragraph' &&
    previousSegment?.type === 'blockquote' &&
    idx >= 2 &&
    segments[idx - 2]?.type === 'heading' &&
    (segments[idx - 2] as HeadingSegment).level === 2

  const isMarkedFrontMatterFiction =
    seg.type === 'paragraph' &&
    !!(seg as ParagraphSegment).isFiction &&
    chapterIndex === 0

  const isFrontMatterCreditsSecondColumnStart =
    chapterIndex === 0 &&
    pageNumber === 1 &&
    seg.type === 'heading' &&
    (seg as HeadingSegment).level === 3 &&
    (seg as HeadingSegment).text === 'ILLUSTRATIONS & GRAPHICS'

  const shouldSpanAll =
    (seg.type === 'heading' && (seg as HeadingSegment).level === 2) ||
    isChapterFictionAfterH2

  const isHeading = seg.type === 'heading'

  const element = (() => {
    switch (seg.type) {
      case 'heading': {
        const h = seg as HeadingSegment
        if (h.level === 1 && pageNumber !== undefined && pageNumber <= 2) {
          return null
        }
        const Tag = `h${h.level}` as 'h1' | 'h2' | 'h3' | 'h4'
        const cls = ['chapter-title', 'section-heading', 'subsection', 'bold-label'][
          h.level - 1
        ]
        return (
          <Tag key={idx} id={h.id} className={cls}>
            {h.text}
          </Tag>
        )
      }
      case 'paragraph': {
        const p = seg as ParagraphSegment
        return (
          <TextBlock
            key={idx}
            html={p.html}
            isChapterOpener={!!p.isChapterOpener || isFirstParagraphAfterChapterFiction}
            isFiction={isMarkedFrontMatterFiction}
            variant="body"
          />
        )
      }
      case 'blockquote': {
        const bq = seg as BlockquoteSegment
        return (
          <TextBlock
            key={idx}
            html={bq.html}
            variant="blockquote"
            isFiction={isChapterFictionAfterH2}
          />
        )
      }
      case 'table': {
        const t = seg as TableSegment
        return <TableBlock key={idx} headers={t.headers} rows={t.rows} />
      }
      case 'hr':
        return <hr key={idx} className="gold-rule" />
      case 'image-ref': {
        const img = seg as ImageRefSegment
        return (
          <ImageBlock
            key={idx}
            filename={img.filename}
            width={img.width}
            height={img.height}
            altText={img.altText}
            caption={img.caption}
          />
        )
      }
      default:
        return null
    }
  })()

  // Wrap in a div to attach data attribute for search highlighting
  if (element && seg.type !== 'hr') {
    return (
      <div
        key={idx}
        data-segment-idx={idx}
        className={`${styles.segmentWrap} ${isHeading ? styles.headingWrap : ''} ${shouldSpanAll ? styles.spanAllWrap : ''} ${isChapterFictionAfterH2 ? styles.fictionAfterH2Wrap : ''} ${isMarkedFrontMatterFiction ? styles.frontMatterFictionWrap : ''} ${isFrontMatterCreditsSecondColumnStart ? styles.creditsSecondColumnStart : ''}`}
      >
        {element}
      </div>
    )
  }

  return element
}

export default function PageContent({
  segments,
  sectionHeadingPage = false,
  pageNumber,
  chapterIndex,
}: PageContentProps) {
  const isFrontMatterCreditsPage = chapterIndex === 0 && pageNumber === 1
  const firstCreditsH2Index = isFrontMatterCreditsPage
    ? segments.findIndex(
        (seg) => seg.type === 'heading' && (seg as HeadingSegment).level === 2,
      )
    : -1

  const renderedSegments = segments.map((seg, idx) =>
    renderSegment(seg, idx, segments, pageNumber, chapterIndex),
  )

  if (firstCreditsH2Index >= 0) {
    renderedSegments.splice(
      firstCreditsH2Index + 1,
      0,
      <div
        key="credits-columns-offset"
        className={`${styles.segmentWrap} ${styles.spanAllWrap} ${styles.creditsColumnsOffset}`}
        aria-hidden="true"
      />,
    )
  }

  return (
    <main
      className={`${styles.columns} ${sectionHeadingPage ? styles.sectionHeadingPage : ''} ${isFrontMatterCreditsPage ? styles.frontMatterCreditsPage : ''}`}
      role="region"
      aria-label="Page content"
      // Stop pointer events from reaching the flip library so that the text
      // area remains selectable/copyable. Clicks in the page margin padding
      // (outside this element) still propagate and trigger the page turn.
      onMouseDown={(e) => e.stopPropagation()}
      onClick={(e) => e.stopPropagation()}
    >
      {renderedSegments}
    </main>
  )
}
