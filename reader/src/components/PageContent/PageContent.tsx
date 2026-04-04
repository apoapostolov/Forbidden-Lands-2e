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
}

function renderSegment(seg: Segment, idx: number) {
  const element = (() => {
    switch (seg.type) {
      case 'heading': {
        const h = seg as HeadingSegment
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
            isChapterOpener={p.isChapterOpener}
            variant="body"
          />
        )
      }
      case 'blockquote': {
        const bq = seg as BlockquoteSegment
        return <TextBlock key={idx} html={bq.html} variant="blockquote" />
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
      <div key={idx} data-segment-idx={idx}>
        {element}
      </div>
    )
  }

  return element
}

export default function PageContent({ segments }: PageContentProps) {
  return (
    <main
      className={styles.columns}
      role="region"
      aria-label="Page content"
      // Stop pointer events from reaching the flip library so that the text
      // area remains selectable/copyable. Clicks in the page margin padding
      // (outside this element) still propagate and trigger the page turn.
      onMouseDown={(e) => e.stopPropagation()}
      onClick={(e) => e.stopPropagation()}
    >
      {segments.map((seg, idx) => renderSegment(seg, idx))}
    </main>
  )
}
