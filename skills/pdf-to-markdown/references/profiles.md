# Document Profiles

Profiles are starting points, not rules.

## `default`

Use when the document is generic or you are unsure which profile fits.

Bias:

- moderate structure damage
- no strong repeated footer phrase known in advance
- generic cleanup behavior only

## `corebook`

Use when the PDF has clear chapter structure and repeated running headers.

Bias:

- preserve chapter hierarchy aggressively
- expect repeated page furniture

## `supplement`

Use when the PDF is booklet-sized and chaptering is light.

Bias:

- fewer assumptions about chapter numbering
- stronger suspicion that all-caps booklet titles are running furniture

## `spell-compendium`

Use when the document is spell-heavy and repeated metadata blocks appear.

Bias:

- protect spell metadata
- expect many heading-level spell names

## `bestiary`

Use when creatures dominate the document.

Bias:

- preserve labeled stat lines over paragraph beauty
- avoid flattening attack tables into prose

## `lifepath-generator`

Use when the PDF is table-dense.

Bias:

- table integrity outranks paragraph elegance
- repeated dice ranges are likely row boundaries, not clutter

## Choosing quickly

Ask:

1. Which structure would be most damaging to lose?
2. What repeats most often in the page margin bands?
3. Is the document mainly prose, rules text, tables, or generated results?

Choose the profile that protects the highest-risk structure.
