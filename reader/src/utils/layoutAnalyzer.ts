/**
 * Page Layout Analyzer — metadata for smart content placement
 *
 * Analyzes segment composition to flag:
 * - Tables that should span both columns
 * - Images that need special text wrapping
 * - Lists that should stay together with preceding content
 * - Orphaned elements
 */

export interface LayoutMetadata {
  // If true, the table should be rendered as full-page width
  tableSpansTwoColumns?: boolean
  // If true, this segment should avoid column break before it
  avoidBreakBefore?: boolean
  // If true, keep with next segment (list + preceding text)
  keepWithNext?: boolean
  // Estimated ideal column count (1 or 2)
  preferredColumns?: 1 | 2
}

/**
 * Analyze a table and decide if it needs to span both columns
 */
export function analyzeTable(
  headers: string[],
  rows: string[][],
  context?: { precedingListItems?: number },
): LayoutMetadata {
  const metadata: LayoutMetadata = {}

  // Wide tables should span
  if (headers.length >= 5) {
    metadata.tableSpansTwoColumns = true
  }

  // Tall tables should span
  if (rows.length >= 15) {
    metadata.tableSpansTwoColumns = true
  }

  // Headers with very long text
  const maxHeaderLength = Math.max(...headers.map((h) => h.length))
  if (maxHeaderLength > 30) {
    metadata.tableSpansTwoColumns = true
  }

  // Prevent break before if preceded by short list
  if (context?.precedingListItems && context.precedingListItems <= 3) {
    metadata.avoidBreakBefore = true
  }

  return metadata
}

/**
 * Analyze a list segment to decide content flow
 */
export function analyzeList(itemCount: number): LayoutMetadata {
  const metadata: LayoutMetadata = {}

  // Very short lists stay with preceding text
  if (itemCount <= 3) {
    metadata.avoidBreakBefore = true
    metadata.keepWithNext = true
  }

  return metadata
}

/**
 * Analyze an image segment for text wrapping strategy
 */
export function analyzeImage(widthPt: number, heightPt: number): LayoutMetadata {
  const metadata: LayoutMetadata = {}
  const pageWidthPt = 482 // from PDF
  const columnWidthPt = (pageWidthPt - 50 * 2 - 14) / 2 // margins + gap

  // If image is wider than column, it needs special handling
  if (widthPt > columnWidthPt) {
    metadata.tableSpansTwoColumns = true // treat like a wide table
    metadata.avoidBreakBefore = true
  }

  // Tall images should avoid orphaning
  if (heightPt > 150) {
    metadata.avoidBreakBefore = true
  }

  return metadata
}

/**
 * Apply layout metadata to CSS classes on the rendered element
 */
export function layoutMetadataToClass(meta: LayoutMetadata): string {
  const classes: string[] = []
  if (meta.tableSpansTwoColumns) classes.push('layout-span-two-cols')
  if (meta.avoidBreakBefore) classes.push('layout-avoid-break-before')
  if (meta.keepWithNext) classes.push('layout-keep-with-next')
  return classes.join(' ')
}
