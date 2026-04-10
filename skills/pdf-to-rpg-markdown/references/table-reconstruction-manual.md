# Table Reconstruction Manual

Tables are the highest-risk structures in RPG OCR recovery.

If you damage a table, you damage play.

## Main Principle

Prefer an imperfect but structured table over a smoother paragraph that loses
row boundaries.

## Table Archetypes in RPG Books

### Dice Tables

Examples:

- D6 result tables
- D66 event tables
- `3D6` consequence tables

Typical columns:

- roll
- title or result
- consequence
- notes

Repair goal:

- every roll range stays attached to its row
- every row becomes one markdown table row or one bullet item if true table
  recovery is impossible

### Matrix Tables

Examples:

- size by settlement type
- population by density and settlement size
- profession talent choice grids

Repair goal:

- preserve headers first
- preserve row labels second
- preserve intersections third

### Statblocks

Examples:

- monsters
- units
- spell entities

Repair goal:

- keep labels and values adjacent
- use bullets if the extractor completely destroyed table geometry
- do not let stat lines merge into prose paragraphs

## Recognition Heuristics

Likely table material often contains:

- many repeated dice notations
- repeated numeric ranges
- alternating label-value patterns
- sequences of capitalized terms without sentence punctuation
- keywords like `D6`, `D66`, `Rank`, `Range`, `Duration`, `Ingredient`, `Cost`

## Repair Strategy

### Case A: Already a Pipe Table but Dirty

Fix:

- `<br>` inside cells
- extra blank lines
- uneven header spacing
- broken emphasis markers

### Case B: One-Line Flattened Table

Example:

`D66 WEALTH GEAR 11-16 Too much debt. -2 21-26 In debt. -1`

Repair method:

1. identify the header row
2. find the repeated roll pattern
3. split on each roll token
4. rebuild row-by-row

### Case C: Image-Text Dump with `<br>`

Repair method:

1. split on `<br>`
2. identify whether the first meaningful line is a header
3. determine column count from the header
4. rebuild conservatively

### Case D: Complex Matrix Beyond Safe Automation

If you cannot confidently infer the column structure:

- preserve as linewise blocks
- label it for review
- do not fabricate cells

## Utility Script for Simple Flattened Tables

For a narrow class of single-line OCR table collapses, use:

```bash
python3 scripts/repair_flattened_tables.py path/to/file.md
python3 scripts/repair_flattened_tables.py path/to/file.md --write
```

This helper is intentionally conservative.

Good fit:

- one-line tables beginning with `D6`, `D66`, or `3D6`
- repeated roll ranges in the same line
- simple two-column output after recovery

Bad fit:

- real matrix tables
- tables with merged headers
- tables where row payloads contain many embedded numeric ranges

## When a Bullet List Is Better

Use bullets instead of a markdown table when:

- the original source is already closer to a stat list than a grid
- cells are too merged to reconstruct safely
- the same information can be preserved more faithfully as labeled items

## Forbidden Moves

- do not drop rows because they are hard
- do not merge multiple dice ranges into one row unless the source clearly does
- do not paraphrase mechanical effects
- do not reorder rows for aesthetics
