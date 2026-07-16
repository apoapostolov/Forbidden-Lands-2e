import styles from './ImageBlock.module.css'

interface ImageBlockProps {
  filename: string
  width: number
  height: number
  altText: string
  caption?: string
}

export default function ImageBlock({
  filename,
  width,
  height,
  altText,
  caption,
}: ImageBlockProps) {
  return (
    <figure className={styles.figure}>
      <img
        src={`/images/${filename}`}
        alt={altText}
        width={width}
        height={height}
        loading="lazy"
        decoding="async"
        className={styles.image}
        onError={(event) =>
          event.currentTarget.closest('figure')?.setAttribute('hidden', '')
        }
      />
      {caption && (
        <figcaption className={`${styles.caption} body-label`}>{caption}</figcaption>
      )}
    </figure>
  )
}
