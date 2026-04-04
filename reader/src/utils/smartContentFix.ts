/**
 * Smart Content Fixer — Post-processing for markdown-to-HTML content
 *
 * Tasks:
 * 1. Replace skull emoji (☠️ 💀) with text-based symbol (⚰)
 * 2. Convert colored emoji (⚔️) to greyscale via CSS class
 * 3. Fix diamond bullets (✦) as proper list markers
 * 4. Improve text wrapping around images and tables
 * 5. Prevent list orphaning across columns
 */

/**
 * Apply smart fixes to HTML content. Currently handles:
 * - Replacing skull emoji (☠️, 💀) with text-based coffin symbol (⚰)
 * - Wrapping colored emoji (⚔️) in a span with greyscale filter class
 * - Ensuring diamond bullets display correctly
 */
export function smartFixContent(html: string): string {
  let fixed = html

  // Replace skull emoji (☠️, ☠, 💀) with text-based alternative (⚰ coffin)
  // Coffin symbol renders as text, not colored emoji, and fits the dark DM aesthetic
  const skullEmoji = ['☠️', '☠', '💀']
  for (const skull of skullEmoji) {
    fixed = fixed.replace(
      new RegExp(skull.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'),
      '⚰',
    )
  }

  // Wrap remaining colored emoji (⚔️) in a span with greyscale filter
  // This prevents them from standing out in a black-and-white book layout
  const coloredEmoji = ['⚔️', '⚔', '🩸']
  for (const emoji of coloredEmoji) {
    const regex = new RegExp(
      `(?!<[^>]*>${emoji})${emoji.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`,
      'g',
    )
    fixed = fixed.replace(regex, `<span class="emoji-grey">${emoji}</span>`)
  }

  // Ensure diamond bullets (✦) are rendered as proper list markers
  // If found in text (not XML), wrap in list structure
  if (fixed.includes('✦')) {
    // Match lines starting with ✦ (item definitions in spell blocks, etc.)
    // Convert to actual list items
    fixed = fixed.replace(
      /^✦\s*/gm,
      '<li class="diamond-bullet"><span class="diamond-marker">✦</span> ',
    )
    // Close any open lists
    if (fixed.includes('<li class="diamond-bullet">')) {
      fixed = fixed.replace(
        /<li class="diamond-bullet">/g,
        '<ul class="diamond-list"><li class="diamond-bullet">',
      )
      fixed = fixed.replace(/(<\/li>)(?!<li class="diamond-bullet">)/g, '$1</ul>')
    }
  }

  return fixed
}

/**
 * Estimate if a table is too large to fit in a single column.
 * Tables with many rows or wide headers should span both columns.
 */
export function shouldTableSpan(headers: string[], rows: string[][]): boolean {
  // If header count is high (5+ columns), this table needs width
  if (headers.length >= 5) return true

  // If total content is large (20+ rows), it will orphan
  if (rows.length >= 20) return true

  // Rough content width estimate: sum header text lengths
  const totalHeaderChars = headers.reduce((sum, h) => sum + h.length, 0)
  if (totalHeaderChars > 150) return true

  return false
}

/**
 * Check if a list should be kept with its preceding text (avoided orphaning).
 * Very short lists (1–3 items) should stay together.
 */
export function shouldListStayTogether(itemCount: number): boolean {
  return itemCount <= 3
}
