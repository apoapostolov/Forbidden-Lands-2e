# Cleanup Issues

Recurring artifact classes found in complex RPG PDF extractions.

## 1. Spaced headings

Decorative headings often extract with spaces between every letter.

Fix:

- split on 2+ spaces to find word boundaries
- collapse letter-spaced groups
- apply word segmentation only to the collapsed text
- use a corrections map for edge cases

## 2. Missing possessives and apostrophes

Extraction may drop possessive apostrophes or separate the `s`.

Fix:

- repair only inside headings or other confirmed title text
- keep the apostrophe style consistent

## 3. Broken headings

Column breaks can split headings into fragments or orphaned stubs.

Fix:

- compare against the surrounding chapter structure
- delete orphan fragments
- rebuild obvious split headings

## 4. Sidebar and prose splits

Two-column layouts often split a sentence across a column break.

Fix:

- join the text only when the continuation is clearly the same sentence
- do not join across structural markers

## 5. Running headers embedded in text

Running headers can appear as standalone lines or stray substrings.

Fix:

- identify the repeated string once
- remove every later occurrence

## 6. Garbled multi-column tables

The hardest class.

Fix:

- read the page visually
- recover the row and column structure
- rebuild the table explicitly
- replace the damaged block in one operation

## 7. Broken pipe tables

Rows, headers, and cells can collapse into one line or one cell.

Fix:

- keep one logical entry per row
- preserve headers first
- do not paraphrase the data

## 8. Loose bullet lists

Blank lines between bullets produce loose lists.

Fix:

- remove blank lines between adjacent bullet items
- preserve spacing around the list boundaries
