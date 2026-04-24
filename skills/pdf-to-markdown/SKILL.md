---
name: pdf-to-markdown
description: Convert, extract, and clean RPG PDFs and OCR dumps into manuscript-grade markdown. Use for any Forbidden Lands PDF, rulebook, supplement, or raw markdown extraction that needs structural cleanup, table recovery, heading repair, and manuscript-safe output. In this repo, always use this skill for FL PDF work. Triggers on: PDF conversion, OCR cleanup, two-column extraction, table repair, raw markdown cleanup, supplement recovery.
---

# PDF to Markdown

This is the repo's authoritative skill for converting RPG PDFs and OCR dumps into usable markdown manuscripts.

It covers the full pipeline: tool selection, phased extraction, structural repair, prose cleanup, and quality validation.

## Toolchain

Prefer the tool best suited to the source:

| Tool                  | Best for                                                           |
| --------------------- | ------------------------------------------------------------------ |
| **markitdown**        | Two-column layouts, weapon/stat tables, mixed-format RPG corebooks |
| **pymupdf4llm**       | Column-aware extraction, custom pipelines, richer layout fidelity  |
| **pdftotext -layout** | Fast plain-text dump, text-heavy single-column pages               |
| **md-anything**       | Scanned PDFs needing OCR first, mixed media docs                   |

Markitdown wrapper: `/home/apoapostolov/.openclaw/workspace/scripts/markitdown`

Install if missing:

```bash
cd /home/apoapostolov/git-ext/markitdown
uv venv --python 3.12 .venv
uv pip install -e 'packages/markitdown[all]'
```

For column-aware pymupdf4llm extraction:

```bash
python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output-dir --profile supplement
```

Available profiles: `default`, `corebook`, `supplement`, `spell-compendium`, `bestiary`, `lifepath-generator`

See `references/document-profiles.md` for profile selection guidance.

## Required Mindset

Weaker agents fail OCR recovery in four ways:

1. over-trust the extractor and leave broken structure in place
2. over-edit and silently invent content
3. flatten everything into paragraphs and destroy hierarchy
4. try to "fix everything everywhere" without a triage order

Treat OCR repair as **forensic editorial work**.

## Triage Before Editing

Before any cleanup, run the audit script:

```bash
python scripts/ocr_markdown_audit.py path/to/file.raw.md
python scripts/ocr_markdown_audit.py path/to/file.raw.md path/to/file.clean.md
```

Then fill out `references/triage-worksheet.md` mentally before committing to a strategy.

## Layout Recon Before Extraction

For a new or badly damaged PDF, do a fast structural survey before choosing a profile or starting cleanup. The goal is to map the document's layout logic, not to repair prose.

Capture these facts first:

1. TOC/bookmarks and chapter breaks
2. page count and spread count
3. sample page geometry from the opening, middle, and late sections
4. repeated running headers, footers, page furniture, and title treatments
5. font families, sizes, and bold/italic patterns
6. image inventory, including repeated icons, banners, and full-page art
7. table inventory, especially matrix tables, statblocks, and roll tables

Use the survey to decide whether the document is primarily:

- single-column prose
- two-column rules text
- table-dense reference material
- statblock-heavy bestiary content
- image-heavy layout with captions and sidebars

If a layout report already exists, use it as the first-pass map, but still verify ambiguous spans visually before rewriting. Keep the survey separate from the raw extraction so the same layout evidence can support multiple cleanup passes.

## Workflow

### Phase 0: Preserve the Source

Never destroy the raw extraction.

Minimum output set:

- source PDF
- `.raw.md` extraction output
- `.clean.md` working manuscript

Optional: `.ocr-report.md` audit report, chapter splits, issue-specific repair notes.

### Phase 1: Diagnose Before Editing

Before rewriting anything, inspect the opening pages, a middle spread, and a late section.

- See `references/ocr-artifact-taxonomy.md` for the seven damage tiers.
- See `references/calibration-examples.md` for before/after output calibration.

### Phase 2: Structural Recovery

Fix these before any prose edits:

1. page furniture (page numbers, running titles, footer slogans)
2. heading hierarchy
3. picture-text blocks
4. table structure

Skipping this order lets paragraph cleanup blur content that should stay separated.

See `references/table-reconstruction-manual.md` for table-specific repair rules.
See `references/layout-analysis-workflow.md` for the generic survey and layout-summary workflow.

Flattened-table helper:

```bash
python3 scripts/repair_flattened_tables.py path/to/file.clean.md --write
```

### Phase 3: Prose Recovery

After structure is stable:

1. rejoin broken paragraphs
2. remove OCR line-wrap damage
3. fix drop-cap splits
4. normalize blockquotes, captions, and sidebar text
5. correct only high-confidence OCR errors

Do not silently lore-edit ambiguous words unless justified by local context.

### Phase 4: Supplement-Specific Repair

RPG books need domain-aware repair.

- See `references/repair-playbook.md` for FL-specific patterns by artifact class.
- See `references/cleanup-issue-catalog.md` for the eight common artifact categories with examples and grep detection commands.
- See `references/high-confidence-corrections.md` for safe FL-specific term repairs.

For layout ambiguity, compare visually:

```bash
pdftotext -layout -f START_PAGE -l END_PAGE path/to/book.pdf -
```

See `references/pdf-visual-comparison-and-illustrations.md` for column-splice recovery and illustration preservation.

### Phase 5: Quality Gates

Run lint:

```bash
./.tools/markdownlint/node_modules/.bin/markdownlint path/to/file.clean.md
```

Section split helper:

```bash
python3 scripts/split_markdown_sections.py path/to/file.clean.md output-dir --level 2
python3 scripts/split_markdown_sections.py path/to/file.clean.md output-dir --pattern '^## '
```

Then verify all gates with `references/review-checklist.md` and `references/quality-gates-and-escalation.md`.

## Strong Default Operating Procedure

1. Preserve raw artifact.
2. Run extraction or reuse raw markdown.
3. Run audit script and read the report.
4. Work through `references/triage-worksheet.md` to pick automation depth.
5. Produce a separate `.clean.md` working file.
6. Repair opening sections first so the user sees a real manuscript shape.
7. Continue through the file by artifact class, not by whim.
8. For table collapses, try the flattened-table helper before manual reconstruction.
9. For ambiguous column splices, use visual PDF comparison before rewriting.
10. When structure is clean enough to split, use the heading-based split helper.
11. Normalize FL spell metadata glyph surrogates (`E RANK 1` → `- Rank: 1`) only inside spell metadata blocks.
12. When layout corruption is ambiguous, replace the whole damaged span in recovered reading order rather than patching line-by-line.
13. When a floated spell list or summary table is found, move it before the spell descriptions.
14. When a boxed note is clearly a sidebar, use a bold label plus paragraph block instead of promoting it to a section heading.
15. If illustrations are requested, save in `/illustrations`, retain transparency by default, insert at original position by default.
16. At the end, report: files created, artifact classes fixed, what remains ambiguous, whether lint passed.

## Non-Negotiable Rules

- Never overwrite the raw OCR file with cleaned output.
- Never silently lore-edit ambiguous text.
- Never merge tables into plain paragraphs for convenience.
- Never collapse heading levels just because the extractor got them wrong.
- Never hide risky cleanup behind broad repo-wide lint disables.
- Never treat one successful repair as globally safe.

## Repair Priorities (When Time Is Limited)

1. title and chapter structure
2. running headers / footers / page numbers
3. table reconstruction in playable sections
4. paragraph continuity
5. repeated OCR garbage
6. cosmetic normalization

## Reference File Index

| File                                                    | When to read                                           |
| ------------------------------------------------------- | ------------------------------------------------------ |
| `references/ocr-artifact-taxonomy.md`                   | Classifying damage tiers                               |
| `references/triage-worksheet.md`                        | Before committing to a cleanup strategy                |
| `references/document-profiles.md`                       | Choosing extraction profile                            |
| `references/layout-analysis-workflow.md`               | Generic PDF survey, geometry, image, and table analysis |
| `references/cleanup-issue-catalog.md`                   | Specific artifact patterns with grep commands and code |
| `references/repair-playbook.md`                         | Concrete repairs by artifact class                     |
| `references/table-reconstruction-manual.md`             | Table-specific rules and archetypes                    |
| `references/high-confidence-corrections.md`             | Safe FL-specific term repairs                          |
| `references/quality-gates-and-escalation.md`            | When to stop automating                                |
| `references/review-checklist.md`                        | Post-cleanup spot-check                                |
| `references/calibration-examples.md`                    | Output quality calibration                             |
| `references/repo-calibration-corpus.md`                 | Real repo before/after examples                        |
| `references/when-not-to-repair-automatically.md`        | Escalation examples                                    |
| `references/pdf-visual-comparison-and-illustrations.md` | Column splices, illustrations                          |
| `references/agent-turn-template.md`                     | Standard agent turn structure                          |
| `references/projects.md`                                | Project log (append-only)                              |
| `references/toolchain.md`                               | Tool install and version notes                         |
