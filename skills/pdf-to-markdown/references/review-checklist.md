# Review Checklist

Use this after a long OCR cleanup pass.

## Front Matter

- Is the title correct?
- Is the title page debris gone from the clean file?
- Is the contents page either reconstructed or intentionally omitted?

## Headings

- Does the heading hierarchy make sense at a glance?
- Did any quotes get mistaken for headings?
- Did any recurring headers survive as duplicate sections?
- [ ] No page number artifacts remain (`–7–`, `– 88 –`, `# – 14 –`)
- [ ] No running headers remain (each chapter header appears once)
- [ ] No spaced-character headings remain
- [ ] No missing possessives (`S` as standalone token in headings)
- [ ] No broken or truncated headings remain
- [ ] No orphaned text fragments between sections
- [ ] No running headers embedded in paragraph text

## Tables

- Are the most important rules tables still tables?
- Do dice ranges still align with outcomes?
- Did any matrix table collapse into a paragraph?
- [ ] Tables are proper pipe tables with header and alignment rows
- [ ] No description text in numeric columns, no numeric data in description columns

## Paragraphs

- Do opening paragraphs read naturally?
- Are obvious drop-cap losses repaired?
- Are unrelated column fragments accidentally merged?
- [ ] No mid-sentence paragraph breaks
- [ ] Bullet lists are compact (no blank lines between items)
- [ ] No `<br>` tags in body text

## Visual Conversions

- Are sidebars and epigraphs visually distinct?
- Are picture placeholders gone?
- Are picture-text blocks either converted or intentionally preserved?
- [ ] No `**==> picture` placeholders or picture text markers remain

## Encoding

- [ ] Smart quotes (U+2019, U+201C, U+201D) are consistent throughout

## Verification

- Did lint pass?
- If lint exceptions were added, are they local and justified?
- Did the final report name unresolved ambiguity?
- [ ] Spot-check 3–5 sections against the original PDF
