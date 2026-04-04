import { smartFixContent } from '@utils/smartContentFix'
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
  // Apply smart content fixes (emoji greyscale, diamond bullets)
  const fixed = smartFixContent(html)

  // DOMPurify is available at runtime in the browser
  const clean =
    typeof window !== 'undefined'
      ? DOMPurify.sanitize(fixed, { USE_PROFILES: { html: true } })
      : fixed

  const isFictionIntro =
    variant === 'body' && /^<p>\s*<em>[\s\S]*<\/em>\s*<\/p>$/i.test(clean)

  const className = [
    styles.block,
    variant === 'blockquote' ? 'flavour-text' : 'body-text',
    isChapterOpener ? 'chapter-opener' : '',
    isFictionIntro ? 'fiction-intro' : '',
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
