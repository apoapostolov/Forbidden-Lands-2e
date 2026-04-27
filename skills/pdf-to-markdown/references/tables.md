# Table Reconstruction

Tables are the highest-risk structures in OCR cleanup.

## Main principle

Prefer an imperfect but structured table over a smooth paragraph that loses row boundaries.

## Table types

### Dice tables

Examples:

- D6 result tables
- D66 event tables
- 3D6 consequence tables

Repair goal:

- every roll range stays attached to its row
- every row becomes one markdown table row or one bullet item if table recovery is unsafe

### Matrix tables

Examples:

- size by settlement type
- population by density
- profession choice grids

Repair goal:

- preserve headers first
- preserve row labels second
- preserve intersections third

### Statblocks

Examples:

- monsters
- NPCs
- units
- spell entities

Repair goal:

- keep labels and values adjacent
- do not let stat lines merge into prose paragraphs

## Repair strategy

### Already a pipe table but dirty

Fix:

- `<br>` inside cells
- extra blank lines
- uneven header spacing
- broken emphasis markers

### One-line flattened table

Repair method:

1. identify the header row
2. find the repeated roll pattern
3. split on each row token
4. rebuild row by row

### Complex matrix beyond safe automation

If the column structure is unclear:

- preserve linewise blocks
- label the block for review
- do not fabricate cells

## Shared helper

Use the shared flattened-table pass or the compatibility wrapper:

```bash
python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output-dir --pass flattened-tables
python scripts/repair_flattened_tables.py path/to/file.md --write
```

## Forbidden moves

- do not drop rows because they are hard
- do not merge multiple dice ranges into one row unless the source clearly does
- do not paraphrase mechanical effects
- do not reorder rows for aesthetics
