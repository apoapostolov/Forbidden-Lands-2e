# Visual PDF Comparison and Illustrations

This reference explains two related workflows:

- how to compare a damaged markdown block against the visual PDF layout
- how to preserve important book illustrations as shared markdown assets

## Why Visual Comparison Matters

Text extraction alone is not enough for many RPG books.

The PDF often uses:

- two-column layouts
- floating spell tables
- sidebars placed between spell entries
- statblocks that sit beside prose
- illustration callouts that interrupt reading order

When OCR is wrong, the fix often depends on seeing the page, not just reading
the raw text dump.

## When To Use Visual Comparison

Escalate from raw markdown to visual PDF comparison when any of these happen:

- a spell or rule block is mixed with another block
- a table appears in the middle of a paragraph
- a sidebar or callout has been merged into prose
- a heading is present but the following body clearly belongs elsewhere
- the same sentence seems to continue in two incompatible directions
- two page columns have been interleaved

If structure is ambiguous, compare against the PDF before rewriting.

## Practical Comparison Method

Use a repeatable sequence:

1. Find the damaged block in the clean markdown.
2. Pull the matching PDF pages with `pdftotext -layout`.
3. If that is still ambiguous, inspect the rendered page visually.
4. Identify which content belongs to:
   - main prose
   - sidebar
   - table
   - statblock
   - caption
5. Rebuild the markdown in reading order, not in OCR order.

## Strong Visual Clues

These patterns were confirmed by manual repair work in this repo:

- Spell list tables may float into later pages in the PDF, but in markdown they
  should usually be moved before the spell descriptions for that discipline.
- Sidebar callouts like `Iron in Objects` or `Teramalda` may be better rendered
  as bold subsection labels with short paragraphs, not promoted to peer chapter
  headings.
- A block that starts as one spell's prose and suddenly changes into another
  spell's metadata is almost always a column splice, not a legitimate inline
  continuation.
- If a spell header is followed by text that is obviously another spell's body,
  recover both blocks from the PDF as one replacement span rather than patching
  line by line.
- If a statblock sits visually under a spell header and before the next spell,
  keep it with that spell even if OCR placed it after the next heading.

## Safe Reconstruction Rule

When the PDF makes the intended reading order clear, it is safe to:

- move a floated spell list to the start of its section
- convert a boxed sidebar into a bold label plus paragraph block
- regroup a statblock under the spell that owns it
- replace a whole damaged span instead of preserving line-level OCR order

Do not preserve wrong OCR order when the PDF visibly disproves it.

## Visual Comparison Restraint

Do not use visual comparison as permission to rewrite prose freely.

Use it to recover:

- ownership of text blocks
- correct reading order
- table position
- sidebar boundaries
- illustration placement

Not to rewrite style, lore, or rules wording beyond what the page supports.

## Illustration Preservation Workflow

Some users want important illustrations kept in the markdown manuscript.

Default assumptions:

- save image files under `/illustrations`
- keep transparency when available: `yes`
- insert at original source position when possible: `yes`
- allow reuse across chapter files: `yes`

The `/illustrations` directory is shared across the manuscript and may be used
by multiple chapter files.

## How The User Should Specify Illustration Requests

Ask for one or more of the following:

- page number or page range
- nearby heading or caption
- short description of the image
- desired filename slug if they care
- whether transparency should be retained
- whether placement should stay at the original position or move elsewhere

Recommended request shape:

```text
Keep the illustration on page 149 near "Teramalda".
Save it as illustrations/teramalda.png.
Retain transparency: yes.
Insert position: original.
```

Or:

```text
Keep the dwarf fortress map from pages 34-35.
Save under /illustrations.
Retain transparency: no.
Insert it under the "The Stronghold" heading.
```

## Markdown Insertion Conventions

If the user wants the image inserted into the manuscript:

- place it near the original visual position by default
- if the original position is impossible to recover cleanly, place it directly
  after the nearest relevant heading
- use a normal markdown image link or an HTML image block only if markdown is
  insufficient for the desired presentation

Example:

```md
![Teramalda illustration](illustrations/teramalda.png)
```

If the image belongs to a sidebar or callout, place it before or after that
block rather than inside a table.

## Illustration Asset Rules

- Prefer stable lowercase filenames with hyphens.
- Do not create chapter-local duplicates if the same illustration can be shared
  from `/illustrations`.
- Preserve transparency unless the user explicitly says otherwise or the export
  format cannot support it.
- If transparency status is unclear, default to retaining it.
- If placement is unclear, default to original source position.

## If The User Does Not Want Images Inserted Yet

It is valid to:

- extract and save the image only
- note the intended insertion point
- leave the markdown unchanged until the user confirms placement

This is often safer for long OCR cleanup passes.
