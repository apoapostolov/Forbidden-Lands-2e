import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import TableBlock from './TableBlock'

describe('TableBlock', () => {
  it('exposes a caption and scoped column headers', () => {
    render(<TableBlock headers={['Talent', 'Rank']} rows={[['Chef', '1']]} />)

    expect(screen.getByRole('table', { name: 'Rules reference table' })).toBeVisible()
    expect(screen.getByRole('columnheader', { name: 'Talent' })).toHaveAttribute(
      'scope',
      'col',
    )
  })
})
