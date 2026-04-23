# Forbidden Lands 2E Cleanup Rules Module

Use this module when converting Forbidden Lands PDFs or raw OCR markdown in this repository.

This module converts local repository cleanup rules into a reusable reference for the `pdf-to-markdown` skill.

## 1) Processing Order

Always process in this order:

1. preserve raw source (`.pdf`, `.raw.md`)
2. remove page furniture (running headers/footers/page numbers)
3. restore heading hierarchy
4. reconstruct tables
5. repair prose continuity and OCR line-wrap artifacts
6. run quality checks and lint

Do not reverse this order. Paragraph-first cleanup tends to hide structural defects.

## 2) High-Frequency Artifact Classes

### A. Spaced-character headings

Examples:

- `C H A P T E R  I`
- `Fa st Ac t ion s`

Action:

- collapse intra-word spacing
- keep intended heading level
- use correction dictionary for edge cases

### B. Missing possessives/apostrophes

Examples:

- `Man S Best Friend` → `Man’s Best Friend`
- `Founder S Day` → `Founder’s Day`

Action:

- restore possessive punctuation where context is unambiguous
- prefer typographic apostrophe consistency across document

### C. Broken/orphaned headings from column breaks

Examples:

- truncated headings (`Erika Ga`)
- orphan continuation fragments posing as headings

Action:

- cross-check with table of contents or local section sequence
- delete non-heading fragments
- merge only when target heading is clear

### D. Running headers embedded in body text

Action:

- remove both standalone repeated headers and inline contaminations
- keep the first true chapter heading; remove repeats

### E. Multi-column table bleed / merged row corruption

Action:

- detect overlong lines and row-merging artifacts
- rebuild table structure before prose edits
- split merged entries into proper rows and columns
- verify against rendered PDF when uncertain

### F. Loose bullet lists

Action:

- remove blank lines between adjacent bullet items unless list intentionally contains multi-paragraph items

### G. Spell metadata OCR glyph substitution

In `Spells & Sorcerers`, a leading `E` in metadata lines is often a broken glyph bullet.

Safe in metadata blocks only:

- `E RANK 1` → `- Rank: 1`
- `E RANGE: Short` → `- Range: Short`
- `E DURATION: Immediate` → `- Duration: Immediate`
- `E INGREDIENT: Candle (1 roll)` → `- Ingredient: Candle (1 roll)`

Do not apply this substitution to normal prose.

## 3) Forbidden Lands High-Confidence Corrections

Common safe normalizations (context permitting):

- `forbidden lands` → `Forbidden Lands`
- `strongh old` → `Stronghold`
- `willpow er` → `Willpower`
- `agi lity` → `Agility`
- `str ength` → `Strength`
- `empat hy` → `Empathy`

Supplement phrase anchors seen in this repository:

- `Spells & Sorcerers`
- `Towns & Villagers`
- `Battles & Sieges`
- `Legends & Adventurers`

## 4) Quality Gates

Before finalizing `.clean.md`:

- no residual page-number artifacts
- no repeated running headers
- no spaced-character headings
- no orphan heading fragments
- no unresolved table row mergers in gameplay-critical sections
- no loose bullet spacing regressions
- no unresolved `picture` placeholders intended as temporary markers
- lint pass (or tightly scoped local lint exception with justification)

## 5) Escalation Rule

Stop automatic cleanup and flag for manual review when:

- heading intent is ambiguous
- table ownership across columns cannot be established confidently
- OCR corruption risks changing rule meaning
- visual order and extracted order conflict heavily

When escalated, use small page-window visual comparison and replace the damaged span in coherent reading order.

## 6) Pointers to Local Canonical Material

This module is a practical distillation. For deeper patterns and examples, consult:

- `skills/markitdown/SKILL.md` (Post-Extraction Cleanup catalog)
- `skills/pdf-to-rpg-markdown/references/high-confidence-corrections.md`
- `skills/pdf-to-rpg-markdown/references/repair-playbook.md`
- `skills/pdf-to-rpg-markdown/references/quality-gates-and-escalation.md`
