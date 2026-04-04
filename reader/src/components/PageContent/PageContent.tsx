import TextBlock from '@components/TextBlock/TextBlock'
import TableBlock from '@components/TableBlock/TableBlock'
import ImageBlock from '@components/ImageBlock/ImageBlock'
import type {
  Segment,
  HeadingSegment,
  ParagraphSegment,
  BlockquoteSegment,
  TableSegment,
  ImageRefSegment,
} from '@types/book'
import styles from './PageContent.module.css'

interface PageContentProps {
  segments: Segment[]
}

function renderSegment(seg: Segment, idx: number) {
  switch (seg.type) {
    case 'heading': {
      const h = seg as HeadingSegment
      const Tag = `h${h.level}` as 'h1' | 'h2' | 'h3' | 'h4'
      const cls = ['chapter-title', 'section-heading', 'subsection', 'bold-label'][h.level - 1]
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
}

export default function PageContent({ segments }: PageContentProps) {
  return (
    <main className={styles.columns} role="region" aria-label="Page content">
      {segments.map((seg, idx) => renderSegment(seg, idx))}
    </main>
  )
}
