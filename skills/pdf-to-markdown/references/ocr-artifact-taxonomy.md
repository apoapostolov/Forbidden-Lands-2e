# OCR Artifact Taxonomy for RPG PDFs

This reference teaches agents how to recognize the major classes of damage that
appear in tabletop RPG PDFs and OCR markdown.

## Why Taxonomy Matters

Weak agents often see "bad OCR" as one problem.

That is a mistake.

Each artifact class behaves differently:

- some can be removed mechanically
- some must be reconstructed structurally
- some must be preserved and escalated

You must classify before you clean.

## Tier 1: Page Furniture

These are not manuscript content.

Examples:

- page numbers
- running book titles
- repeated chapter labels in headers
- footer slogans
- decorative publisher lines

Signs:

- repeated on many pages
- short
- all-caps or small-caps
- disconnected from surrounding paragraph flow

Default action:

- remove from clean manuscript
- preserve in raw

## Tier 2: Heading Damage

These artifacts affect hierarchy and navigation.

Subtypes:

- spaced-letter headings
- partially merged headings
- headings split across pages
- heading-like lines that are actually quotes
- title fragments repeated as running headers

Typical examples:

- `C H A P T E R  I I`
- `## **TYPE OF GOVERNMENT**`
- `Army Lines` extracted before the paragraph that logically belongs under `Game Time`

Default action:

- reconstruct cautiously
- preserve intended hierarchy
- do not flatten everything to one heading level

## Tier 3: Paragraph Flow Damage

The words are mostly present, but the sentence flow is broken.

Subtypes:

- hard line wraps
- paragraph breaks mid-sentence
- dropped initial letters from decorative drop caps
- stray sentence fragments from adjacent columns

Typical examples:

- `elcome to...`
- `his chapter...`
- `magic will now...` after a separated fragment from the previous page

Default action:

- rejoin when confidence is high
- keep ambiguity visible when confidence is low

## Tier 4: Table Damage

This is the most dangerous class for rules text.

Subtypes:

- image-text tables extracted as plain lines
- merged headers
- D66 tables flattened into sentence streams
- matrix tables with collapsed columns
- embedded `<br>` line breaks inside cells

Typical examples:

- `D66 PROFESSION ATTRIBUTE 1ST SKILL...`
- `ADVANTAGE DICE Well-Trained Units +1 Orc or Dwarf Infantry +1`

Default action:

- reconstruct as tables whenever possible
- preserve row integrity above all
- do not paraphrase rules tables into prose

## Tier 5: Image and Sidebar Artifacts

These are extraction leftovers from non-body layout elements.

Subtypes:

- picture placeholders
- picture text markers
- sidebars detected as italic blocks
- captions extracted as standalone lines

Default action:

- remove placeholders
- convert usable picture text into tables or plain prose
- convert sidebar prose into blockquotes when appropriate

## Tier 6: Domain-Term Corruption

The OCR keeps structure but corrupts setting or rules terminology.

Typical examples:

- kin names
- discipline names
- talent paths
- place names
- monster names

This is the most tempting area for hallucination.

Default action:

- correct only when confidence is high or corroborated elsewhere in the same document
- otherwise preserve the damaged form and mark for later review

## Tier 7: Mixed Damage

Many lines belong to more than one class.

Example:

- a running header repeated in all caps inside a picture-text block
- a table row that is also a paragraph fragment
- a decorative chapter quote extracted as a heading

Default action:

- solve the structural question first
- only then solve wording

## Classification Questions

For any suspicious block, ask:

1. Is this manuscript content or page furniture?
2. Is this structure, prose, or data?
3. Is the source damage local or repeated?
4. Can I repair this mechanically with high confidence?
5. If I guess wrong, do I destroy playability or just polish?

If the answer to question 5 is "destroy playability," escalate.
