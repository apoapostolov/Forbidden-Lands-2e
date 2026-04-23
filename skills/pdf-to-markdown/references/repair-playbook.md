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
- reassigning a block to a different spell or rules entry after a two-column
  splice
- deciding whether a floated table should be moved earlier in markdown reading
  order

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

## Visual Comparison Rules

If raw markdown and local OCR heuristics still disagree about structure, use
the visual PDF as the tie-breaker.

Use visual comparison especially when:

- two spell entries are interleaved
- a table is embedded in the middle of prose
- a sidebar has been mistaken for body text

## RPG Statblock Repair Rules

Forbidden Lands 2E uses a fixed NPC/monster statblock format. When repairing
statblocks, enforce this layout:

```md
#### NPC Name

Prose description of the NPC — personality, appearance, motivation.

**Strength N, Agility N, Wits N, Empathy N**

> **SKILLS:** Skill 3, Skill 2
> **TALENTS:** Talent Name N
> **GEAR:** Item (N), Item
```

Rules:

1. **Attribute line is never a heading.** `### Strength N...` must become
   `**Strength N...**`. This is the most common extractor error in this book.

2. **SKILLS and TALENTS are blockquoted.** `> **SKILLS:**` and `> **TALENTS:**`
   with no blank line between them. MD028 fires if there is a blank line between
   consecutive blockquote lines — collapse it.

3. **GEAR is bold inline, not blockquoted.** `**GEAR:** ...` without `>`.

4. **ARMOR follows GEAR when present.** `> **ARMOR:** N` goes in the blockquote
   after GEAR (or replaces it if there is no gear).

5. **Prose description comes before the statblock.** If an NPC entry has no
   description paragraph above the `**Strength` line, suspect a two-column
   splice. Check the PDF before inventing prose.

6. **Two-column splice detection:** Compare the NPC heading order in the markdown
   against the visual order in the PDF. If statblock lines appear under the wrong
   NPC heading, the block must be reconstructed from PDF, not patched line-by-line.

## Adventure Site Heading Hierarchy Rules

Adventure site chapters have a three-tier hierarchy. Apply this when repairing
a chapter where all headings are at `###`:

```
## Adventure Site Name          (H2 — the site itself)
  ### Named Section             (H3 — Background, Locations, Events, etc.)
    #### 1. Numbered Location   (H4 — every numbered or named sub-entry)
    #### Named NPC Entry        (H4 — every NPC in Monsters and NPCs)
    #### Named Event Entry      (H4 — every event in Events)
```

Rules:

1. The adventure site itself is H2 if it is a major chapter section.
2. Top-level named sections (Background, Recommended Reading, Getting Here,
   Legend, Locations, Monsters and NPCs, Events) are H3.
3. Everything below a named section is H4: numbered locations, named NPCs,
   named events, and named sub-tables (Strange Events, Who Does What?, etc.).
4. Do not promote H4 entries to H3. That flattens the visual hierarchy and
   breaks the reading structure.

- a statblock has been attached to the wrong spell

When the PDF makes ownership clear, it is safe to rebuild the whole span in
proper reading order.

## Manual Discoveries Confirmed In This Repo

These patterns were repeatedly confirmed during `Spells & Sorcerers` cleanup:

- floated spell-list tables often belong before the discipline's spell entries
  in markdown, even if the PDF placed them later for page layout reasons
- boxed sidebars like `Iron in Objects` or `Teramalda` are usually better kept
  as bold labels with paragraph text than as peer headings
- if one spell's metadata is immediately followed by another spell's body, that
  is usually a column splice and both spell blocks should be rebuilt together
- when a damaged run spans several related spells, replacing the whole run from
  the PDF is safer than performing isolated line edits

## Recent Issue Patterns: Adventure Site OCR Repair

The latest work on Weatherstone and Vale of the Dead exposed these recurring
issues in Forbidden Lands adventure-site extracts:

- H3 headings used for every location, NPC, and event entry. Adventure sites
  need H2 for the site, H3 for section headers, and H4 for all numbered or
  named subentries.
- Statblocks split across columns or attached to the wrong NPC. The attribute
  line must be a bold paragraph, not a heading, and the full block must be
  rebuilt in PDF reading order when it crosses columns.
- `TALENTS:` lines were merged into `GEAR:` lines. Fix by forcing `> **TALENTS:**`
  and `**GEAR:**` on separate lines with the correct blockquote semantics.
- Skeleton trait lines like `BONY:` were collapsed into the gear line. These
  require separate bullet or bold-prefix formatting.
- OCR list prefixes such as `CREATURES:` and `TREASURES:` should be bolded on
  bullet lines, not left as plain text.
- `D6 Monster Attacks` should often become a labeled roll-table, not a raw
  heading and paragraph dump.
- Broken content often appears as orphaned fragments after a column splice
  (`Morme` / `Captured!` / `The Flooding`). These need to be reassembled into
  coherent event entries, not simply patched line-by-line.
- Strange scanner residue can appear as stray alphanumeric junk lines. If a
  line clearly comes from a page artifact rather than the narrative, remove it.
- Loose list spacing between statblock bullets must be collapsed to keep the
  markdown list tight and prevent renderer `<p>` wrapping.

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
