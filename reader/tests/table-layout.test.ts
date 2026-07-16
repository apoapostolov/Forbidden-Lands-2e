// @vitest-environment node

import {
  COLUMN_HEIGHT_PT,
  RENDER_SAFETY_PT,
  chooseTableLayout,
  layoutTable,
  splitOversizedFirstTableRow,
  tableRowsThatFit,
} from '../scripts/preprocess'
import { describe, expect, it } from 'vitest'

const LEGAL_TABLE_HEIGHT_PT = COLUMN_HEIGHT_PT - RENDER_SAFETY_PT - 4

describe('adaptive table layout', () => {
  it('keeps compact reference tables in one column', () => {
    const table = chooseTableLayout(
      ['Roll', 'Result'],
      [
        ['1', 'Clear'],
        ['2', 'Rain'],
      ],
    )

    expect(table.spanAll).toBe(false)
    expect(table.layoutReason).toBe('column-fit')
  })

  it('promotes structurally wide tables to the full page width', () => {
    const table = chooseTableLayout(
      ['D6', 'Name', 'Cost', 'Weight'],
      [['1', 'Long spear', '4 silver', 'Normal']],
    )

    expect(table.spanAll).toBe(true)
    expect(table.layoutReason).toBe('column-count')
  })

  it('can promote a narrow table when its column layout is excessively tall', () => {
    const rows = Array.from({ length: 24 }, (_, index) => [
      String(index + 1),
      'A detailed consequence with enough words to wrap repeatedly in the narrow measure.',
    ])
    const table = chooseTableLayout(['Roll', 'Consequence'], rows)

    expect(table.spanAll).toBe(true)
    expect(table.layoutReason).toBe('table-height')
  })

  it('splits a single page-tall row by cell text until every fragment is legal', () => {
    const oversizedText = Array.from(
      { length: 900 },
      (_, index) => `consequence-${index + 1}`,
    ).join(' ')
    let table = layoutTable(
      {
        headers: ['Roll', 'Exceptional consequence'],
        rows: [['66', oversizedText]],
      },
      true,
      'runtime-overflow',
    )
    let fragmentCount = 0

    while (tableRowsThatFit(table, LEGAL_TABLE_HEIGHT_PT) === 0) {
      const split = splitOversizedFirstTableRow(table, LEGAL_TABLE_HEIGHT_PT)
      expect(split).not.toBeNull()
      expect(split!.head.heightPt).toBeLessThanOrEqual(LEGAL_TABLE_HEIGHT_PT)
      expect(split!.head.rowContinuesOnNext).toEqual([true])
      expect(split!.tail.rowContinuesFromPrevious?.[0]).toBe(true)
      table = split!.tail
      fragmentCount++
      expect(fragmentCount).toBeLessThan(100)
    }

    expect(fragmentCount).toBeGreaterThan(1)
    expect(table.heightPt).toBeLessThanOrEqual(LEGAL_TABLE_HEIGHT_PT)
  })
})
