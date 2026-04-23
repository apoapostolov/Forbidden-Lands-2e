---
name: pdf-to-markdown
description: Convert PDFs into clean Markdown for RPG books, rulebooks, and supplements. Use this whenever a PDF, OCR dump, or raw markdown extraction needs structural cleanup, table recovery, heading repair, and manuscript-safe formatting. In this repository, always use it for Forbidden Lands PDF-to-markdown work and consult the local cleanup module before finalizing output.
---

# PDF To Markdown

This skill was imported from the lifestyle repo and upgraded for this workspace.

It is for **conversion + cleanup discipline**, not just extraction.

## Workflow

1. Locate the source PDF and decide where the markdown should live.
2. Preserve the raw source and create a staged output (`.raw.md` then `.clean.md`).
3. Prefer layout-aware extraction when structure matters:
   - `pdftotext -layout` for text-heavy pages
   - PyMuPDF / `pymupdf4llm` for richer layout-aware extraction
4. Save a raw markdown draft first, then clean it into a readable final file.
5. Repair structure before prose:
   - remove page numbers and running headers
   - normalize headings and section hierarchy
   - reconstruct tables before line-level prose edits
6. Rejoin broken paragraphs and line wraps without inventing text.
7. Normalize lists, blockquotes, table captions, and table footnotes consistently.
8. Keep derived markdown beside the source PDF or in a clearly named sibling file.
9. Run lint for final markdown if the file remains in-repo.

## Module References (Read As Needed)

### Core module for this repo

If the document is a Forbidden Lands source (corebook/supplement/proposal source PDF), read:

- `references/forbidden-lands-2e-cleanup-rules.md`

This module contains repository-local cleanup rules and validation priorities.

### Legacy and cross-repo notes

Use these when project logging is needed:

- `references/projects.md` (append-only project notes)
- `references/toolchain.md` (install/toolchain notes)

## Forbidden Lands Rule

For Forbidden Lands conversions in this workspace, do not stop at generic cleanup.
Apply the local cleanup module, especially for:

- spaced-character headings
- possessive/apostrophe OCR damage
- running-header contamination (standalone and inline)
- multi-column table bleed and merged row corruption
- loose bullet lists introduced by extraction
- OCR glyph substitution in spell metadata blocks

## RPG Book Defaults

- Treat large rulebooks as source documents, not prose to rewrite.
- Preserve chapter structure and section order.
- Keep OCR or extraction artifacts in a `raw` or staged file if first pass is messy.
- Escalate to visual PDF comparison when reading order is ambiguous.
- Prefer deterministic, scriptable repairs for repeated artifact classes.

## Strong Default Operating Procedure

When asked to process a document:

1. Preserve raw artifact.
2. Extract or reuse raw markdown.
3. Apply structural cleanup first.
4. Apply prose cleanup second.
5. Apply repo-local module rules (for Forbidden Lands docs).
6. Validate with lint and targeted spot-checks against the PDF.
7. Report what was fixed automatically vs what needs manual review.

## Non-Negotiable Rules

- Never overwrite the raw OCR file with cleaned output.
- Never silently invent or lore-edit uncertain text.
- Never flatten tables into paragraphs for convenience.
- Never weaken repo-wide lint rules to hide cleanup defects.
- Never assume one successful cleanup pattern is globally safe.

## Validation

Before handing off:

- confirm heading hierarchy is intact
- confirm table blocks remain machine-readable markdown tables
- confirm repeated page furniture is removed
- confirm unresolved ambiguities are explicitly flagged
- run markdown lint on changed files when they remain in-repo
