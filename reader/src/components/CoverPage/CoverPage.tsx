import styles from './CoverPage.module.css'

export default function CoverPage() {
  return (
    <div className={styles.cover}>
      <img
        src="/assets/cover/book-cover.png"
        alt="Forbidden Lands — Player's Handbook cover"
        className={styles.coverImage}
      />
    </div>
  )
}
