/**
 * Smart Content Fixer — Post-processing for markdown-to-HTML content
 *
 * Tasks:
 * 1. Replace emoji-style dice symbols with text glyph symbols
 * 2. Bold swords, skulls, and blood drops consistently
 * 3. Fix diamond bullets (✦) as proper list markers
 * 4. Improve text wrapping around images and tables
 * 5. Prevent list orphaning across columns
 */

/**
 * Apply smart fixes to HTML content. Currently handles:
 * - Replacing swords/skulls/blood-drop emoji with text glyph symbols
 * - Wrapping those symbols in a bold symbol span for consistent rendering
 * - Ensuring diamond bullets display correctly
 */
export function smartFixContent(html: string): string {
  let fixed = html

  const swordHtml = '<span class="fl-symbol fl-symbol-sword">⚔&#xFE0E;</span>'

  // Table-cell/plain-cell legacy normalization when the entire fragment is
  // just x-markers (e.g. "x", "x x", "x x x") from corrupted dice symbols.
  fixed = fixed.replace(/^\s*[xX](?:\s+[xX]){0,5}\s*$/g, (m: string) =>
    m
      .trim()
      .split(/\s+/)
      .map(() => swordHtml)
      .join(' '),
  )

  // Legacy content normalization:
  // Earlier processing passes replaced dice sword symbols with plain x/X in
  // several passages and table cells. Convert those dice-context markers back.
  fixed = fixed.replace(
    /(<t[dh][^>]*>\s*)([xX](?:\s+[xX]){0,5})(\s*<\/t[dh]>)/g,
    (_m: string, open: string, marks: string, close: string) => {
      const swords = marks
        .trim()
        .split(/\s+/)
        .map(() => '<span class="fl-symbol fl-symbol-sword">⚔&#xFE0E;</span>')
        .join(' ')
      return `${open}${swords}${close}`
    },
  )
  fixed = fixed.replace(
    /\bcounts?\s+as\s+[xX]\b/g,
    (m: string) => `${m.slice(0, m.length - 1)}⚔`,
  )
  fixed = fixed.replace(/\bfor\s+every\s+[xX]\s+rolled\b/g, (m: string) =>
    m.replace(/[xX]/, '⚔'),
  )
  fixed = fixed.replace(/\bextra\s+[xX]\b/g, (m: string) => m.replace(/[xX]/, '⚔'))
  fixed = fixed.replace(/\bone\s+or\s+more\s+[xX]\b/g, (m: string) =>
    m.replace(/[xX]/, '⚔'),
  )
  fixed = fixed.replace(/\badditional\s+[xX]\b/g, (m: string) => m.replace(/[xX]/, '⚔'))

  // Broader dice-prose recovery for standalone x markers:
  // "rolls one x", "needs two x", "more x than", "x rolled", etc.
  fixed = fixed.replace(
    /\b(one|two|three|four|five|more|extra|additional|several|required|needs?|counts?|rolls?|rolled|per)\s+[xX]\b/gi,
    (_m: string, lead: string) => `${lead} ⚔`,
  )
  fixed = fixed.replace(/\b[xX]\s+rolled\b/gi, '⚔ rolled')
  fixed = fixed.replace(/\b[xX]\s+than\b/gi, '⚔ than')
  fixed = fixed.replace(
    /\bcounts?\s+as\s+[xX]\b/gi,
    (m: string) => `${m.slice(0, m.length - 1)}⚔`,
  )

  // Normalize all symbol variants to text-presentation glyphs and bold them.
  // Use FE0E (text presentation selector) to avoid color emoji rendering.
  // Also normalize any legacy coffin replacement back to skull.
  fixed = fixed.replace(
    /(?:☠\uFE0F?|💀|⚰\uFE0F?)/g,
    '<i class="fl-symbol fl-symbol-fa fl-symbol-skull fa-solid fa-skull" aria-hidden="true"></i>',
  )
  fixed = fixed.replace(
    /⚔\uFE0F?/g,
    '<span class="fl-symbol fl-symbol-sword">⚔&#xFE0E;</span>',
  )
  fixed = fixed.replace(
    /🩸\uFE0F?/g,
    '<i class="fl-symbol fl-symbol-fa fl-symbol-blood fa-solid fa-droplet" aria-hidden="true"></i>',
  )

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
