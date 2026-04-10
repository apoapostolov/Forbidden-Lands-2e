# OCR Repair Playbook

This is the operational repair manual for converting raw OCR markdown into a
working manuscript.

## Rule One

Repair **artifact classes**, not random lines.

If you drift line-by-line without a class-based plan, you will produce a file
that looks cleaner but is less trustworthy.

## Phase Order

### 1. Stabilize the Container

Fix:

- document title
- title page residue
- front matter
- repeated book-name headers

Do not start by fixing typos inside spell descriptions.

### 2. Rebuild Navigation

Fix:

- chapter headings
- section headings
- heading levels
- duplicated heading fragments

The file must become navigable before it becomes elegant.

### 3. Rebuild Data

Fix:

- tables
- statblocks
- roll tables
- matrix sections

In RPG documents, data structure is usually more important than prose polish.

### 4. Rebuild Prose

Fix:

- paragraph joins
- mid-sentence wraps
- obvious OCR word breaks
- drop-cap damage

### 5. Normalize and Verify

Fix:

- whitespace
- `<br>` leftovers
- list spacing
- blockquote consistency

Then lint and review.

## High-Confidence Repairs

These are usually safe:

- removing repeated page numbers
- removing repeated running headers
- converting obvious `## **HEADING**` to a section heading
- converting obvious picture placeholders to nothing
- replacing `<br>` in table cells with spaces
- joining a line that clearly continues the same sentence

## Medium-Confidence Repairs

These need comparison against nearby structure:

- reconstructing spaced headings
- rebuilding flattened tables
- moving a line under a different heading
- deciding whether a short italic block is a sidebar or flavor quote

## Low-Confidence Repairs

These should be escalated or preserved cautiously:

- restoring corrupted lore names from memory
- reconstructing missing table cells with no nearby support
- rewriting ambiguous rules language
- inventing headings that are not supported by repeated patterns

## Drop-Cap Repair Rules

When the first letter of a paragraph is missing:

- compare nearby pages for the same pattern
- check whether the paragraph begins with a common word missing one initial
- confirm that the missing letter does not create a different valid word

Safe examples:

- `elcome` → `Welcome`
- `his chapter` → `This chapter`

Unsafe example:

- `ore` could be `Lore`, `More`, `Core`, or `Ore`

## Repetition Rules

When a suspicious line repeats across pages, it is usually page furniture.

When a suspicious structure repeats in many sections, it is usually layout logic.

Use repetition as evidence.

## "Do Not Beautify" Rule

Your job is not to rewrite the supplement into better prose unless the user asks.

Your job is to recover:

- order
- hierarchy
- table structure
- legibility

Do not convert blunt RPG prose into literary prose during OCR cleanup.

## Safe Escalation Note

If you cannot repair a block without guessing, keep the best recovered version,
leave a note in your summary, and move on.
