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
  // Use a single regex per emoji type to avoid double-wrapping when both the
  // full emoji (⚔️ = ⚔ + U+FE0F variation selector) and bare codepoint appear.
  fixed = fixed.replace(/⚔\uFE0F?/g, '<span class="emoji-grey">⚔</span>')
  fixed = fixed.replace(/🩸/g, '<span class="emoji-grey">🩸</span>')

  // Ensure diamond bullets (✦) are rendered as proper list markers
  // If found in text (not XML), wrap in list structure
  if (fixed.includes('✦')) {
    // Step 1: Normalize markdown-parser <ul><li>✦ ... patterns.
    // The markdown parser wraps ✦-prefixed items in plain <ul><li>, leaving
    // the ✦ as literal text INSIDE the <li>. We must convert these to
    // diamond-list items BEFORE the CSS ::before rule adds a second ✦.
    fixed = fixed.replace(/<ul>([\s\S]*?)<\/ul>/g, (_match: string, inner: string) => {
      if (!inner.includes('✦')) return _match
      if (!/<li>(?:\s*<[^>]+>\s*)*✦/.test(inner)) return _match
      // a) ✦ directly after <li>  (most common)
      let converted = inner.replace(
        /<li>✦\s*/g,
        '<li class="diamond-bullet"><span class="diamond-marker">✦</span> ',
      )
      // b) ✦ inside first inline wrap tag, e.g. <li><strong>✦ RANK 1:</strong>
      converted = converted.replace(
        /<li>(<[^>]+>)\s*✦\s*/g,
        '<li class="diamond-bullet"><span class="diamond-marker">✦</span> $1',
      )
      return `<ul class="diamond-list">${converted}</ul>`
    })

    // Step 2: Convert any remaining bare ✦-prefixed lines (e.g. lines that
    // were NOT inside a <ul><li> — they appear as plain text at line start).
    fixed = fixed.replace(
      /^✦\s*(.+)$/gm,
      '<li class="diamond-bullet"><span class="diamond-marker">✦</span> $1</li>',
    )
    // Step 3: Wrap consecutive diamond-bullet <li> runs in a single <ul>.
    fixed = fixed.replace(
      /((?:<li class="diamond-bullet">[^\n]*<\/li>\n*)+)/g,
      '<ul class="diamond-list">$1</ul>',
    )

    // Step 4: Flatten accidental nested diamond-list wrappers where the
    // first item is wrapped in an inner <ul>, causing deeper indentation.
    // Repeat until stable to handle multiple nesting levels.
    let prev = ''
    while (prev !== fixed) {
      prev = fixed
      fixed = fixed.replace(
        /<ul class="diamond-list">\s*<ul class="diamond-list">([\s\S]*?)<\/ul>\s*([\s\S]*?)<\/ul>/g,
        '<ul class="diamond-list">$1$2</ul>',
      )
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
