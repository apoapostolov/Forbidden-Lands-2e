import { smartFixContent } from '@utils/smartContentFix'
import DOMPurify from 'dompurify'
import styles from './TableBlock.module.css'

interface TableBlockProps {
  headers: string[]
  rows: string[][]
  /** Table spans both columns (set by flow engine for >3-column tables) */
  spanAll?: boolean
  columnLineWidthsEm?: number[]
  rowContinuesFromPrevious?: boolean[]
  rowContinuesOnNext?: boolean[]
}

export default function TableBlock({
  headers,
  rows,
  spanAll,
  columnLineWidthsEm,
  rowContinuesFromPrevious,
  rowContinuesOnNext,
}: TableBlockProps) {
  function renderFixedInline(text: string) {
    const fixed = smartFixContent(text)
    const clean =
      typeof window !== 'undefined'
        ? DOMPurify.sanitize(fixed, { USE_PROFILES: { html: true } })
        : fixed
    return <span dangerouslySetInnerHTML={{ __html: clean }} />
  }

  const measuredWidthTotal =
    columnLineWidthsEm?.reduce((sum, width) => sum + width, 0) ?? 0

  return (
    <div
      className={`${styles.wrapper} ${spanAll ? styles.wrapperSpan : styles.wrapperColumn}`}
    >
      <div className={styles.dressTop} />
      <table className={styles.table}>
        <caption className={styles.visuallyHidden}>Rules reference table</caption>
        {measuredWidthTotal > 0 && (
          <colgroup>
            {columnLineWidthsEm?.map((width, index) => (
              <col
                key={index}
                style={{ inlineSize: `${(width / measuredWidthTotal) * 100}%` }}
              />
            ))}
          </colgroup>
        )}
        {headers.length > 0 && (
          <thead>
            <tr>
              {headers.map((h, i) => (
                <th key={i} scope="col" className={`${styles.th} bold-label`}>
                  {renderFixedInline(h)}
                </th>
              ))}
            </tr>
          </thead>
        )}
        <tbody>
          {rows.map((row, ri) => (
            <tr
              key={ri}
              className={`${ri % 2 === 0 ? styles.rowEven : styles.rowOdd} ${rowContinuesFromPrevious?.[ri] ? styles.rowContinuesFromPrevious : ''} ${rowContinuesOnNext?.[ri] ? styles.rowContinuesOnNext : ''}`}
            >
              {row.map((cell, ci) => (
                <td key={ci} className={`${styles.td} body-text`}>
                  {renderFixedInline(cell)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <div className={styles.dressBottom} />
    </div>
  )
}
