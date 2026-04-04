import styles from './TableBlock.module.css'

interface TableBlockProps {
  headers: string[]
  rows: string[][]
}

export default function TableBlock({ headers, rows }: TableBlockProps) {
  return (
    <div className={styles.wrapper}>
      <table className={styles.table}>
        {headers.length > 0 && (
          <thead>
            <tr>
              {headers.map((h, i) => (
                <th key={i} className={`${styles.th} bold-label`}>
                  {h}
                </th>
              ))}
            </tr>
          </thead>
        )}
        <tbody>
          {rows.map((row, ri) => (
            <tr key={ri} className={ri % 2 === 0 ? styles.rowEven : styles.rowOdd}>
              {row.map((cell, ci) => (
                <td key={ci} className={`${styles.td} body-text`}>
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
