---
name: pdf-to-markdown
description: Convert, extract, and clean complex PDFs and OCR dumps into manuscript-grade markdown. Use for any roleplaying-game PDF, rulebook, supplement, or raw markdown extraction that needs structural cleanup, table recovery, heading repair, or manuscript-safe output. Triggers on: PDF conversion, OCR cleanup, two-column extraction, table repair, raw markdown cleanup, supplement recovery.
---

# PDF to Markdown

This is the repo's authoritative skill for converting RPG PDFs and OCR dumps into usable markdown manuscripts.

It covers the full pipeline: tool selection, phased extraction, structural repair, prose cleanup, and quality validation.

## Canonical bundle

The skill ships with a bundled `scripts/` directory. Use those scripts first, and keep them synced with the repo copies so the behavior stays identical everywhere.

Bundled scripts:

- `scripts/pdf_to_markdown.py` — modular extraction and cleanup pipeline
- `scripts/ocr_markdown_audit.py` — artifact audit before and after cleanup
- `scripts/repair_flattened_tables.py` — compatibility wrapper for flattened roll tables
- `scripts/markdown_reflow.py` — wrap or unwrap prose while preserving tables and lists
- `scripts/pdf_debug_passes.py` — pass-by-pass debugging helper

## Toolchain

Prefer the tool best suited to the source:

| Tool                  | Best for                                                           |
| --------------------- | ------------------------------------------------------------------ |
| **markitdown**        | Two-column layouts, weapon/stat tables, mixed-format RPG corebooks |
| **pymupdf4llm**       | Column-aware extraction, custom pipelines, richer layout fidelity  |
| **pdftotext -layout** | Fast plain-text dump, text-heavy single-column pages               |
| **md-anything**       | Scanned PDFs needing OCR first, mixed media docs                   |

If a tool is missing, install it like this:

- `markitdown`: `cd /home/apoapostolov/git-ext/markitdown && uv venv --python 3.12 .venv && uv pip install -e 'packages/markitdown[all]'`
- `pymupdf4llm`: `pip install pymupdf4llm`
- `wordninja`: `pip install wordninja`
- `pdftotext` / `pdfimages`: `sudo apt install poppler-utils`
- `md-anything`: install the repo or MCP package that provides the local command; if it is not available, fall back to `pymupdf4llm` or `pdftotext -layout`
- `markdownlint-cli2`: `npx -y markdownlint-cli2 --version`
- OCR helpers: `sudo apt install tesseract-ocr poppler-utils` and `pip install pytesseract pdf2image`

The bundled scripts only need Python 3.10+ and the extraction libraries above when you actually use the PDF pipeline.

Markitdown wrapper: `/home/apoapostolov/.openclaw/workspace/scripts/markitdown`

Install if missing:

```bash
cd /home/apoapostolov/git-ext/markitdown
uv venv --python 3.12 .venv
uv pip install -e 'packages/markitdown[all]'
```

For column-aware pymupdf4llm extraction:

```bash
python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output-dir --profile default
```

Useful CLI flags:

- `--pass NAME` — run only the named cleanup pass; repeat to run several
- `--skip-pass NAME` — skip a pass in the default pipeline; repeatable
- `--heading-correction OLD=NEW` — add a project-specific heading overlay
- `--dropcap-repair OLD=NEW` — add a project-specific drop-cap repair overlay
- `--footer-phrase TEXT` — suppress an additional repeated footer phrase
- `--list-passes` — print the available pass names and exit
- `--version` — print the mega cleanup script version (`1.0.0`) and exit

When the file is already structurally sound but the prose width needs to change, use the bundled reflow script:

```bash
python scripts/markdown_reflow.py path/to/file.md --mode unwrap --write
python scripts/markdown_reflow.py path/to/file.md --mode wrap --width 75 --write
```

Available profiles: `default`, `corebook`, `supplement`, `spell-compendium`, `bestiary`, `lifepath-generator`

See `references/profiles.md` for profile selection guidance.

## When to switch from scripts to reading

Prefer a scripted fix when the problem is repetitive, local, and can be described as a stable transformation rule.

Switch to direct reading when the fix depends on meaning instead of shape. That includes:

- content that may belong in more than one section
- paragraphs that bleed across a heading, table, sidebar, or illustration boundary
- repairs that would invent missing text, move text between sections, or guess at reading order
- cases where visual comparison is ambiguous and the surrounding prose is the only reliable clue

When you switch, read before and after the damaged span, compare the full section, and decide whether the content is truly misplaced or only badly wrapped. If confidence is still low after that pass, ask the user before making a semantic change.

Rule of thumb: if you can write the fix as a repeatable transformation and prove it with a regression test, script it. If you need to understand what the text means before you can fix it, read first.

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

If the document needs only one repair class, prefer the matching pass instead of running the full pipeline. The converter is now modular; use the pass flags to avoid over-cleaning a file that only needs a narrow fix.

## Problem classes and matching tools

Use the smallest tool that matches the damage.

| Problem class | Best first move | Notes |
| --- | --- | --- |
| Page furniture, page numbers, footer slogans | `scripts/ocr_markdown_audit.py` + `scripts/pdf_to_markdown.py --pass noise-removal` | Remove repeated noise before trying prose fixes. |
| Running headers | `--pass running-headers` | Keep the first occurrence and remove repeats. |
| Spaced or decorative headings | `--pass spaced-headings` | Good for split heading words and letter-spaced titles. |
| Picture placeholders or picture text | `--pass picture-blocks` | Convert table-like picture text, discard captions only when safe. |
| Heading hierarchy collapse | `--pass heading-hierarchy` | Demote or promote headings based on structure, not line shape. |
| Sidebar paragraphs | `--pass sidebars` | Convert long italic-only sidebar text into blockquotes. |
| Hard-wrapped prose or split paragraphs | `scripts/markdown_reflow.py --mode unwrap` | Rejoin paragraphs without touching tables or lists. |
| Prose width normalization | `scripts/markdown_reflow.py --mode wrap` | Reflow to a target width after structure is stable. |
| Inline `<br>` in tables | `--pass table-br-cleanup` | Keep the table; remove `<br>` inside cells. |
| Flattened roll tables | `--pass flattened-tables` or `scripts/repair_flattened_tables.py` | Canonical shared table repair. |
| Loose bullet lists | `--pass loose-lists` | Collapse blank lines between list items. |
| Drop-cap damage | `--pass dropcap-repair` | Apply only high-confidence opening-letter repairs. |
| Ambiguous multi-column splices or interleaved NPC blocks | manual repair after audit | Do not invent missing rows or reassign ownership blindly. |

If a cleanup request touches more than one class, run the structural passes first, then the prose-width tool, then audit again.

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

- source PDF
- `.raw.md` extraction output
- `.clean.md` working manuscript

Optional: `.ocr-report.md` audit report, chapter splits, issue-specific repair notes.

### Phase 1: Diagnose Before Editing

Before rewriting anything, inspect the opening pages, a middle spread, and a late section.

- See `references/artifacts.md` for the damage tiers.
- See `references/examples.md` for before/after output calibration.

### Phase 2: Structural Recovery

Fix these before any prose edits:

1. page furniture (page numbers, running titles, footer slogans)
2. heading hierarchy
3. picture-text blocks
4. table structure

Skipping this order lets paragraph cleanup blur content that should stay separated.

See `references/tables.md` for table-specific repair rules.
See `references/layout.md` for the generic survey and layout-summary workflow.

Flattened-table helpers:

```bash
python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output-dir --pass flattened-tables
python3 scripts/repair_flattened_tables.py path/to/file.clean.md --write
```

The standalone helper remains for compatibility, but the shared `flattened-tables` pass is the canonical implementation.

### Phase 3: Prose Recovery

After structure is stable:

1. rejoin broken paragraphs
2. remove OCR line-wrap damage
3. fix drop-cap splits
4. normalize blockquotes, captions, and sidebar text
5. correct only high-confidence OCR errors

Do not silently lore-edit ambiguous words unless justified by local context.

### Phase 4: Project-Specific Repair

RPG books need domain-aware repair, but keep it layered on top of the generic pipeline.

- See `references/repair.md` for the repair playbook.
- See `references/issues.md` for the common artifact categories with examples and detection commands.
- See `references/fixes.md` for safe high-confidence repairs.
- Keep system-specific notes in `projects/` and keep the shared references agnostic.

## Module overlays

Use external JSON or YAML modules for project-specific corrections instead of hard-coding them into the shared scripts.

Module overlays should carry the book-specific or campaign-specific fixes that are safe within one project but not general enough for the core bundle. Keep the core script generic and let it read overlay files from `projects/` or a sibling module directory.

See `projects/module-overlay-proposal.md` for the schema draft and promotion policy.

Promote a fix through this ladder:

1. local note in `projects/`
2. project module overlay
3. shared reference note only if the pattern is generic across unrelated documents
4. core script change only if the behavior is structural, well-tested, and not tied to any one setting

Retire old project modules by marking them archived instead of deleting the history. That keeps the bundle from accumulating dead system logic.

For layout ambiguity, compare visually:

```bash
pdftotext -layout -f START_PAGE -l END_PAGE path/to/book.pdf -
```

See `references/visual.md` for column-splice recovery and illustration preservation.

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

Then verify all gates with `references/review.md` and `references/quality.md`.

Run the regression suite after any parser, profile, or repair change:

```bash
python -m unittest discover -s scripts/tests
```

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
11. Normalize book-specific glyph surrogates only inside confirmed metadata blocks, and only when the document profile or local evidence supports it.
12. When layout corruption is ambiguous, replace the whole damaged span in recovered reading order rather than patching line-by-line.
13. When a floated spell list or summary table is found, move it before the spell descriptions.
14. When a boxed note is clearly a sidebar, use a bold label plus paragraph block instead of promoting it to a section heading.
15. If illustrations are requested, save in `/illustrations`, retain transparency by default, insert at original position by default.
16. At the end, report: files created, artifact classes fixed, what remains ambiguous, whether lint passed.

## Non-Negotiable Rules

- Never overwrite the raw OCR file with cleaned output.
- Never silently lore-edit ambiguous text.
- See `references/repair.md` for the repair playbook.
- See `references/issues.md` for the common artifact categories with examples and detection commands.
- See `references/fixes.md` for safe high-confidence repairs.
- Keep system-specific notes in `projects/` and keep the shared references agnostic.
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
| `references/artifacts.md`                               | Damage classes and what they mean                      |
| `references/triage.md`                                  | Before committing to a cleanup strategy                |
| `references/profiles.md`                                | Choosing extraction profile                            |
| `references/layout.md`                                  | Generic PDF survey, geometry, image, and table analysis |
| `references/issues.md`                                  | Specific artifact patterns with detection and repair   |
| `references/repair.md`                                  | Concrete repairs by artifact class                     |
| `references/tables.md`                                  | Table-specific rules and archetypes                    |
| `references/fixes.md`                                   | Safe high-confidence repairs                           |
| `references/quality.md`                                 | When to stop automating                                |
| `references/review.md`                                  | Post-cleanup spot-check                                |
| `references/examples.md`                                | Output quality calibration                             |
| `references/limits.md`                                  | Escalation examples                                    |
| `references/visual.md`                                  | Column splices and visual comparison                   |
| `references/turn.md`                                    | Standard agent turn structure                          |
| `references/projects.md`                                | Project log and project-note index                     |
| `references/toolchain.md`                               | Tool install and version notes                         |

## Maintenance loop

This skill is allowed to learn from each cleanup session.

When you see a new recurring OCR pattern, do three things before finishing:

1. classify the pattern in the problem-class table above
2. decide whether the fix belongs in a script, a reference note, or both
3. apply the reusable fix immediately if it is safe and mechanical

If the new pattern is only safe in one book, write it down as a local note instead of generalizing it into the skill.

If the pattern is general and repeatable, update the bundled scripts and references so the next run starts smarter.

If the pattern is only safe in one project, encode it in the relevant module overlay instead of adding it to the shared code.
