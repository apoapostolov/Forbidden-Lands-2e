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

/**
 * Split segments into left/right columns using the __column_break__ marker
 * inserted by the flow engine.
 */
function splitByColumnBreak(segments: Segment[]): {
  spanAll: Segment[]
  left: Segment[]
  right: Segment[]
} {
  const spanAll: Segment[] = []
  const left: Segment[] = []
  const right: Segment[] = []

  // First, extract span-all elements (H2 heading, fiction after H2, H1)
  // These go above the two-column layout
  let i = 0
  while (i < segments.length) {
    const seg = segments[i]

    // H2 section heading always spans
    if (seg.type === 'heading' && (seg as HeadingSegment).level === 2) {
      spanAll.push(seg)
      i++
      // Blockquote immediately after H2 is fiction — also spans
      if (
        i < segments.length &&
        segments[i].type === 'blockquote'
      ) {
        spanAll.push(segments[i])
        i++
      }
      continue
    }

    // H1 chapter title spans
    if (seg.type === 'heading' && (seg as HeadingSegment).level === 1) {
      spanAll.push(seg)
      i++
      continue
    }

    // Fiction paragraphs span
    if (
      seg.type === 'paragraph' &&
      (seg as ParagraphSegment).isFiction
    ) {
      spanAll.push(seg)
      i++
      continue
    }

    break
  }

  // Now split remaining segments at the column break marker
  let inRightColumn = false
  for (; i < segments.length; i++) {
    const seg = segments[i]

    // Check for column break marker
    if (seg.type === 'hr' && seg.id === '__column_break__') {
      inRightColumn = true
      continue
    }

    if (inRightColumn) {
      right.push(seg)
    } else {
      left.push(seg)
    }
  }

  return { spanAll, left, right }
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
        // Skip column break markers
        if (seg.id === '__column_break__') return null
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
    const isSpanAll =
      (seg.type === 'heading' && (seg as HeadingSegment).level === 2) ||
      isChapterFictionAfterH2

    return (
      <div
        key={idx}
        data-segment-idx={idx}
        className={`${styles.segmentWrap} ${isHeading ? styles.headingWrap : ''} ${isSpanAll ? styles.spanAllWrap : ''} ${isChapterFictionAfterH2 ? styles.fictionAfterH2Wrap : ''} ${isMarkedFrontMatterFiction ? styles.frontMatterFictionWrap : ''}`}
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

  // Split segments into span-all / left / right sections
  const { spanAll, left, right } = splitByColumnBreak(segments)

  // Render span-all elements (H2 banners, fiction)
  const spanAllRendered = spanAll.map((seg, idx) =>
    renderSegment(seg, idx, spanAll, pageNumber, chapterIndex),
  )

  // Render left column segments
  const leftRendered = left.map((seg, idx) =>
    renderSegment(seg, idx, left, pageNumber, chapterIndex),
  )

  // Render right column segments
  const rightRendered = right.map((seg, idx) =>
    renderSegment(seg, idx, right, pageNumber, chapterIndex),
  )

  return (
    <main
      className={`${sectionHeadingPage ? styles.sectionHeadingPage : ''} ${isFrontMatterCreditsPage ? styles.frontMatterCreditsPage : ''}`}
      role="region"
      aria-label="Page content"
      style={{ flex: 1, minHeight: 0, display: 'flex', flexDirection: 'column' }}
      // Stop pointer events from reaching the flip library
      onMouseDown={(e) => e.stopPropagation()}
      onClick={(e) => e.stopPropagation()}
    >
      {/* Span-all content: H2 banners, fiction, chapter titles */}
      {spanAllRendered.length > 0 && (
        <div className={styles.spanAllWrap}>
          {spanAllRendered}
        </div>
      )}

      {/* Two explicit columns */}
      <div className={styles.columns}>
        <div className={styles.column}>
          {leftRendered}
        </div>
        <div className={styles.column}>
          {rightRendered}
        </div>
      </div>
    </main>
  )
}
