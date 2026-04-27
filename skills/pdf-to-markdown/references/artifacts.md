# Artifact Classes

Use this file to classify OCR and layout damage before you repair anything.

## Common classes

- page furniture: page numbers, running titles, footer slogans, copyright lines
- heading damage: spaced headings, split headings, wrong heading levels
- picture damage: placeholders, picture-text blocks, captions that should be dropped
- prose damage: hard wraps, split paragraphs, broken hyphenation, dropped opening letters
- table damage: flattened tables, split tables, merged cells, broken headers
- list damage: loose bullets, merged bullets, list items separated by blank lines
- structure damage: wrong reading order, interleaved columns, wrong ownership of blocks

## Triage rule

Repair the class, not the line.

If a line is only suspicious because it looks ugly, leave it alone until the class is confirmed.
