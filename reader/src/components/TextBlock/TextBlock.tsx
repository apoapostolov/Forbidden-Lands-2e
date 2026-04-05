import { smartFixContent } from '@utils/smartContentFix'
import DOMPurify from 'dompurify'
import styles from './TextBlock.module.css'

interface TextBlockProps {
  html: string
  isChapterOpener?: boolean
  isFiction?: boolean
  variant?: 'body' | 'blockquote'
}

export default function TextBlock({
  html,
  isChapterOpener,
  isFiction = false,
  variant = 'body',
}: TextBlockProps) {
  // Apply smart content fixes (emoji greyscale, diamond bullets)
  const fixed = smartFixContent(html)

  // DOMPurify is available at runtime in the browser
  const clean =
    typeof window !== 'undefined'
      ? DOMPurify.sanitize(fixed, { USE_PROFILES: { html: true } })
      : fixed

  const className = [
    styles.block,
    variant === 'blockquote' ? 'flavour-text' : 'body-text',
    isChapterOpener ? 'chapter-opener' : '',
    isFiction ? 'fiction-intro' : '',
  ]
    .filter(Boolean)
    .join(' ')

  // Non-fiction blockquotes get decorative sidebar treatment
  if (variant === 'blockquote' && !isFiction) {
    return (
      <div className={styles.sidebar}>
        <div className={styles.sidebarTop} />
        <div className={className} dangerouslySetInnerHTML={{ __html: clean }} />
        <div className={styles.sidebarBottom} />
      </div>
    )
  }

  return (
    <div
      className={className}
      // Content is sanitized at runtime via DOMPurify
      dangerouslySetInnerHTML={{ __html: clean }}
    />
  )
}
