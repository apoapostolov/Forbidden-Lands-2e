# Document Profiles

Document profiles help weaker agents choose the least-wrong default behavior
before they start editing.

## Why Profiles Matter

Not all RPG books break in the same way.

A spell compendium and a lifepath generator may both come from PDFs, but they
stress different parts of the pipeline:

- spell books stress repeated metadata blocks
- lifepath books stress dice tables
- bestiaries stress statblocks
- warfare supplements stress matrix tables and nested lists

Profiles are not magic. They are just a disciplined starting point.

## Available Profiles

### `default`

Use when:

- the document is a generic supplement
- you are unsure which profile fits

Assumption:

- moderate structure damage
- no strong repeated footer phrase known in advance

### `corebook`

Use when:

- the book has clear chapter structure
- running chapter headers repeat often
- the manuscript is long and sectioned

Bias:

- preserve chapter hierarchy aggressively
- expect repeated page furniture

### `supplement`

Use when:

- the book is booklet-sized
- chaptering is light
- front matter is short

Bias:

- fewer assumptions about `Chapter N`
- stronger suspicion that all-caps booklet titles are running furniture

### `spell-compendium`

Use when:

- the book is mainly spells or magical disciplines
- spell blocks repeat with labels like rank, range, duration, ingredient

Bias:

- protect spell metadata
- expect many heading-level spell names
- expect repeated footer phrase like `spells & sorcerers`

### `bestiary`

Use when:

- creatures dominate the document
- statblocks and attacks matter more than prose flow

Bias:

- preserve labeled stat lines over paragraph beauty
- avoid flattening attack tables into prose

### `lifepath-generator`

Use when:

- the book is table-dense
- childhood, kin, profession, events, or origin tables dominate

Bias:

- table integrity outranks paragraph elegance
- repeated dice ranges are likely row boundaries, not clutter

## How To Choose Quickly

Ask:

1. Does the document mostly teach procedures, list spells, define creatures, or generate results?
2. Which structure would be most damaging to lose: headings, statblocks, or tables?
3. Is the repeated noise phrase obvious from the first three pages?

Choose the profile that protects the highest-risk structure.

## Important Limit

Profiles do not replace judgment.

If the profile behavior conflicts with the actual document, stop trusting the
profile and trust the evidence.
