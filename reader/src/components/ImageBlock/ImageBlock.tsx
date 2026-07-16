import styles from './ImageBlock.module.css'

interface ImageBlockProps {
  filename: string
  width: number
  height: number
  altText: string
  caption?: string
}

export default function ImageBlock({ filename, altText, caption }: ImageBlockProps) {
  return (
    <figure className={styles.figure}>
      <img
        src={`/images/${filename}`}
        alt={altText}
        loading="lazy"
        className={styles.image}
      />
      {caption && (
        <figcaption className={`${styles.caption} body-label`}>{caption}</figcaption>
      )}
    </figure>
  )
}
