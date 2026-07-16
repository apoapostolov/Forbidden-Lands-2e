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
  bottomSpan: Segment[]
} {
  const spanAll: Segment[] = []
  const left: Segment[] = []
  const right: Segment[] = []
  const bottomSpan: Segment[] = []

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
      if (i < segments.length && segments[i].type === 'blockquote') {
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

    // A heading carried with a full-width table spans with that table.
    if (seg.type === 'heading' && (seg as HeadingSegment).spanAll) {
      spanAll.push(seg)
      i++
      continue
    }

    // Fiction paragraphs span
    if (seg.type === 'paragraph' && (seg as ParagraphSegment).isFiction) {
      spanAll.push(seg)
      i++
      continue
    }

    // Long chapter fiction may continue at full width on following pages.
    if (
      seg.type === 'blockquote' &&
      ((seg as BlockquoteSegment & { spanAll?: boolean }).spanAll ||
        (seg as BlockquoteSegment & { isFiction?: boolean }).isFiction)
    ) {
      spanAll.push(seg)
      i++
      continue
    }

    // Spanning tables (>3 columns, marked by flow engine)
    if (seg.type === 'table' && (seg as TableSegment).spanAll) {
      spanAll.push(seg)
      i++
      continue
    }

    break
  }

  // Now split remaining segments at the column break marker
  let inRightColumn = false
  let inBottomSpan = false
  for (; i < segments.length; i++) {
    const seg = segments[i]

    // Check for bottom span marker
    if (seg.type === 'hr' && seg.id === '__bottom_span__') {
      inBottomSpan = true
      continue
    }

    // Check for column break marker
    if (seg.type === 'hr' && seg.id === '__column_break__') {
      inRightColumn = true
      continue
    }

    if (inBottomSpan) {
      bottomSpan.push(seg)
    } else if (inRightColumn) {
      right.push(seg)
    } else {
      left.push(seg)
    }
  }

  return { spanAll, left, right, bottomSpan }
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
    ((previousSegment?.type === 'heading' &&
      (previousSegment as HeadingSegment).level === 2) ||
      !!(seg as BlockquoteSegment & { isFiction?: boolean }).isFiction)

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
          <Tag key={seg.uid} id={h.id} className={cls}>
            {h.text}
          </Tag>
        )
      }
      case 'paragraph': {
        const p = seg as ParagraphSegment
        return (
          <TextBlock
            key={seg.uid}
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
            key={seg.uid}
            html={bq.html}
            variant="blockquote"
            isFiction={isChapterFictionAfterH2}
          />
        )
      }
      case 'table': {
        const t = seg as TableSegment
        return (
          <TableBlock
            key={seg.uid}
            headers={t.headers}
            rows={t.rows}
            spanAll={t.spanAll}
            columnLineWidthsEm={t.columnLineWidthsEm}
            rowContinuesFromPrevious={t.rowContinuesFromPrevious}
            rowContinuesOnNext={t.rowContinuesOnNext}
          />
        )
      }
      case 'hr':
        // Skip column break markers
        if (seg.id === '__column_break__') return null
        return <hr key={seg.uid} className="gold-rule" />
      case 'image-ref': {
        const img = seg as ImageRefSegment
        return (
          <ImageBlock
            key={seg.uid}
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
      (seg.type === 'heading' && !!(seg as HeadingSegment).spanAll) ||
      isChapterFictionAfterH2 ||
      (seg.type === 'blockquote' &&
        !!(seg as BlockquoteSegment & { spanAll?: boolean }).spanAll) ||
      (seg.type === 'table' && !!(seg as TableSegment).spanAll)

    return (
      <div
        key={seg.uid}
        data-segment-id={seg.uid}
        data-segment-type={seg.type}
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

  // Split segments into span-all / left / right / bottomSpan sections
  const { spanAll, left, right, bottomSpan } = splitByColumnBreak(segments)

  // Render span-all elements (H2 banners, fiction)
  const spanAllRendered = spanAll.map((seg, idx) =>
    renderSegment(seg, idx, spanAll, pageNumber, chapterIndex),
  )

  // Detect H2 without fiction after it — needs a spacer for frame clearance
  const hasH2 = spanAll.some(
    (s) => s.type === 'heading' && (s as HeadingSegment).level === 2,
  )
  const hasFictionAfterH2 = spanAll.some((s) => s.type === 'blockquote')
  const needsH2Spacer = sectionHeadingPage && hasH2 && !hasFictionAfterH2

  // Render left column segments
  const leftRendered = left.map((seg, idx) =>
    renderSegment(seg, idx, left, pageNumber, chapterIndex),
  )

  // Render right column segments
  const rightRendered = right.map((seg, idx) =>
    renderSegment(seg, idx, right, pageNumber, chapterIndex),
  )

  // Render bottom-span segments (span-all tables placed below columns)
  const bottomSpanRendered = bottomSpan.map((seg, idx) =>
    renderSegment(seg, idx, bottomSpan, pageNumber, chapterIndex),
  )

  return (
    <div
      className={`${sectionHeadingPage ? styles.sectionHeadingPage : ''} ${isFrontMatterCreditsPage ? styles.frontMatterCreditsPage : ''}`}
      style={{ flex: 1, minHeight: 0, display: 'flex', flexDirection: 'column' }}
      data-flow-root
      // Stop pointer events from reaching the flip library
      onMouseDown={(e) => e.stopPropagation()}
      onClick={(e) => e.stopPropagation()}
    >
      {/* Span-all content: H2 banners, fiction, chapter titles */}
      {spanAllRendered.length > 0 && (
        <div className={styles.spanAllWrap} data-flow-region="top-span">
          {spanAllRendered}
        </div>
      )}

      {/* Spacer to push columns below H2 decorative frame overhang */}
      {needsH2Spacer && <div className={styles.h2NoFictionSpacer} />}

      {/* Two explicit columns */}
      <div className={styles.columns}>
        <div className={styles.column} data-flow-region="column-1">
          {leftRendered}
        </div>
        <div className={styles.column} data-flow-region="column-2">
          {rightRendered}
        </div>
      </div>

      {/* Bottom-span content: tables placed below columns at full width */}
      {bottomSpanRendered.length > 0 && (
        <div className={styles.spanAllWrap} data-flow-region="bottom-span">
          {bottomSpanRendered}
        </div>
      )}
    </div>
  )
}
