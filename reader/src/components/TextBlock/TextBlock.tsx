import DOMPurify from 'dompurify'
import styles from './TextBlock.module.css'

interface TextBlockProps {
  html: string
  isChapterOpener?: boolean
  variant?: 'body' | 'blockquote'
}

export default function TextBlock({
  html,
  isChapterOpener,
  variant = 'body',
}: TextBlockProps) {
  // DOMPurify is available at runtime in the browser
  const clean =
    typeof window !== 'undefined'
      ? DOMPurify.sanitize(html, { USE_PROFILES: { html: true } })
      : html

  const className = [
    styles.block,
    variant === 'blockquote' ? 'flavour-text' : 'body-text',
    isChapterOpener ? 'chapter-opener' : '',
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <div
      className={className}
      // Content is sanitized at runtime via DOMPurify
      dangerouslySetInnerHTML={{ __html: clean }}
    />
  )
}
