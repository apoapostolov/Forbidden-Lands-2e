---
name: pdf-to-rpg-markdown
description: |
  Use when converting tabletop RPG PDFs or raw OCR markdown into clean,
  structured manuscripts. This skill is designed for long, ugly, multi-pass
  recovery work: column-aware extraction, OCR artifact triage, heading and
  table reconstruction, paragraph repair, and quality-gated manuscript output.
  It is explicitly written so weaker agents can follow a disciplined workflow
  instead of improvising.
---

# PDF to RPG Markdown

This skill is the repo's full recovery workflow for turning RPG PDFs and OCR
scrapes into usable markdown manuscripts.

It is not just a converter recipe. It is a **processing discipline**:

- extract conservatively
- diagnose the artifact classes
- repair one class at a time
- verify after each major phase
- escalate when automation becomes riskier than the damage

Use this skill when the source is:

- a PDF that still has selectable text
- a scanned PDF that has already gone through OCR
- a `.raw.md` file produced from a PDF tool
- a half-cleaned markdown dump that still contains OCR structure damage

## Primary Goal

Produce markdown that is:

- readable by humans
- structurally useful to later AI passes
- faithful to the source's content and hierarchy
- clearly separated into raw, clean, and optionally reviewed outputs

The target is **working manuscript quality**, not false perfection.

## Required Mindset

Weaker agents usually fail OCR recovery in one of four ways:

1. they over-trust the extractor and leave broken structure in place
2. they over-edit and silently invent content
3. they flatten everything into paragraphs and destroy hierarchy
4. they try to "fix everything everywhere" without a triage order

Do not do that.

Treat OCR repair as **forensic editorial work**.

## Workflow Order

Always work in phases.

### Phase 0: Preserve the Source

Never destroy or overwrite the source PDF or raw OCR file.

Minimum output set:

- source PDF
- `.raw.md` extraction output
- `.clean.md` working manuscript

Optional:

- `.ocr-report.md` audit report
- chapter splits
- issue-specific repair notes

### Phase 1: Diagnose Before Editing

Before rewriting anything substantial:

1. inspect the opening pages
2. inspect a middle spread
3. inspect a late section
4. identify the dominant artifact classes

Use the audit script:

```bash
python scripts/ocr_markdown_audit.py path/to/file.raw.md
```

For PDF extraction:

```bash
python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output-dir
```

Read:

- `references/ocr-artifact-taxonomy.md`
- `references/quality-gates-and-escalation.md`
- `references/triage-worksheet.md`
- `references/document-profiles.md`

### Phase 2: Structural Recovery

Repair these before prose-level cleanup:

1. page furniture
2. running headers and footers
3. title block and front matter
4. heading hierarchy
5. picture-text blocks
6. table structure

If you skip this order, later paragraph cleanup will blur content that should
have stayed separated.

### Phase 3: Prose Recovery

Once structure is stable:

1. rejoin broken paragraphs
2. remove OCR line-wrap damage
3. fix obvious drop-cap splits
4. normalize blockquotes, captions, and sidebar text
5. correct only the *high-confidence* OCR errors

Do **not** silently lore-edit ambiguous words unless you can justify them.

### Phase 4: Supplement-Specific Repair

RPG books need domain-aware repair.

Examples:

- spell books need repeated spell blocks normalized
- bestiaries need statblock boundaries preserved
- lifepath generators need dice tables reconstructed exactly
- warfare books need matrix tables and list indentation preserved
- some spell books use custom glyph bullets that OCR misreads as `E`; in
  metadata lines like `E RANK 1` or `E RANGE: Short`, treat that leading `E`
  as a broken bullet marker, not as semantic text

Use:

- `references/table-reconstruction-manual.md`
- `references/repair-playbook.md`
- `references/high-confidence-corrections.md`
- `references/pdf-visual-comparison-and-illustrations.md`

### Phase 5: Quality Gates

Before you consider the pass done, verify:

- the file is still readable
- headings are not flattened
- tables remain tables
- quotes are not converted into prose
- obvious running headers are gone
- OCR placeholders are gone or intentionally preserved
- lint passes, or file-local lint exceptions are justified and documented

## Required Files in This Skill

Use these references in order:

1. `TODO.md`
   The phased project plan for building and improving this capability
2. `references/ocr-artifact-taxonomy.md`
   What kinds of OCR damage exist and how to recognize them
3. `references/repair-playbook.md`
   Concrete repair methods by artifact class
4. `references/table-reconstruction-manual.md`
   Table-specific heuristics and safe reconstruction rules
5. `references/quality-gates-and-escalation.md`
   When to trust automation, when to stop, and how to review results
6. `references/document-profiles.md`
   How to choose a cleanup profile before processing
7. `references/agent-turn-template.md`
   The standard turn shape weaker agents should follow
8. `references/review-checklist.md`
   How to spot-check a long cleanup pass
9. `references/triage-worksheet.md`
   How to decide automation depth
10. `references/high-confidence-corrections.md`
    Safe correction patterns and repo-specific OCR repairs
11. `references/calibration-examples.md`
    Before-and-after examples to calibrate output quality
12. `references/when-not-to-repair-automatically.md`
    Examples of where automation should stop
13. `references/repo-calibration-corpus.md`
    Real raw-to-clean examples from this repository
14. `references/pdf-visual-comparison-and-illustrations.md`
    How to compare visually against PDFs and preserve illustrations safely

## Strong Default Operating Procedure

When the user asks to process a document:

1. Preserve the raw artifact.
2. Run the extraction or reuse the raw markdown.
3. Generate an OCR audit report.
4. Produce a separate `.clean.md` working file.
5. Repair the opening sections first so the user sees a real manuscript shape.
6. Continue through the file by artifact class, not by whim.
7. Run `markdownlint` on the cleaned file.
8. If lint exceptions are needed because of preserved OCR complexity, use
   narrow file-local disables instead of weakening repo-wide rules.
9. When simple one-line table collapse survives the main pass, try the
   flattened-table helper before doing manual reconstruction.
10. When the manuscript is clean enough to split, use the heading-based split
    helper instead of relying only on `Chapter N` assumptions.
11. In `Spells & Sorcerers`, normalize OCR spell metadata that begins with a
    leading `E` into plain markdown bullets such as `- Rank:` and `- Range:`
    instead of preserving the broken glyph surrogate.
12. When layout corruption remains ambiguous, compare against the visual PDF and
    replace the whole damaged span in recovered reading order instead of
    preserving wrong OCR order line-by-line.
13. When the PDF clearly shows a floated spell list or summary table, move it
    before the spell descriptions in markdown so the manuscript stays
    navigable.
14. When a boxed note is clearly a sidebar rather than a peer section, prefer a
    bold label plus paragraph block instead of promoting it to a section
    heading.
15. If the user wants illustrations preserved, save them in `/illustrations` by
    default, preserve transparency by default, and insert at original source
    position by default unless the user specifies otherwise.

## Tooling

### Extraction

Preferred extractor:

- `pymupdf4llm`

Why:

- better reading order for columns
- preserves markdown-ish structure
- surfaces picture-text blocks instead of hiding them

### Cleanup

Primary script:

```bash
python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output-dir --profile supplement
```

Audit script:

```bash
python scripts/ocr_markdown_audit.py path/to/file.raw.md
python scripts/ocr_markdown_audit.py path/to/file.raw.md path/to/file.clean.md
```

Flattened table helper:

```bash
python3 scripts/repair_flattened_tables.py path/to/file.clean.md --write
```

Section split helper:

```bash
python3 scripts/split_markdown_sections.py path/to/file.clean.md output-dir --level 2
python3 scripts/split_markdown_sections.py path/to/file.clean.md output-dir --pattern '^## '
```

Rendered PDF comparison:

```bash
pdftotext -layout -f START_PAGE -l END_PAGE path/to/book.pdf -
```

Use smaller page windows when mixed columns or sidebars make a large extract
hard to interpret reliably.

Available profiles:

- `default`
- `corebook`
- `supplement`
- `spell-compendium`
- `bestiary`
- `lifepath-generator`

### Lint

Use:

```bash
./.tools/markdownlint/node_modules/.bin/markdownlint path/to/file.clean.md
```

## Non-Negotiable Rules

- Never overwrite the raw OCR file with cleaned output.
- Never "fix" lore terms by guessing when confidence is low.
- Never merge tables into plain paragraphs for convenience.
- Never collapse heading levels just because the extractor got them wrong.
- Never hide risky cleanup behind broad repo-wide lint disables.
- Never treat one successful document as proof that the same repair is safe for all documents.

## Repair Priorities

When time is limited, fix in this order:

1. title and chapter structure
2. running headers / footers / page numbers
3. table reconstruction in playable sections
4. paragraph continuity
5. repeated OCR garbage
6. cosmetic normalization

## What "Genius-Level" Means Here

It does **not** mean ornate prose or aggressive rewriting.

It means:

- seeing the difference between decoration and structure
- recognizing repeated extraction patterns across pages
- encoding those patterns so weaker agents can repeat the method
- knowing where certainty ends

If a weaker agent follows this skill correctly, it should be able to produce a
clean working manuscript that a stronger agent can refine instead of rebuild.
