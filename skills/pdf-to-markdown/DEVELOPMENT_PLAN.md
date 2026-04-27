# Development Plan — pdf-to-markdown

## Goal

Build a reusable, repo-agnostic PDF-to-Markdown cleanup bundle that can handle complex RPG layouts, restore table structure, and reflow hard-wrapped prose without forcing book-specific logic into the generic pipeline.

## Canonical sources

- `skills/pdf-to-markdown/SKILL.md`
- `skills/pdf-to-markdown/scripts/`
- `scripts/pdf_to_markdown.py`
- `scripts/markdown_reflow.py`
- `references/profiles.md`
- `references/tables.md`
- `projects/`
- `scripts/tests/`

## Decisions already made

- Keep the generic pipeline as the baseline.
- Keep book-specific corrections behind profiles, command-line overlays, or `projects/` notes.
- Keep a separate module-overlay format for project-specific fixes instead of hard-coding them into the shared scripts.
- Treat flattened-table repair as a shared utility, not a one-off fix.
- Keep wrap/unwrap paragraph handling in one script with mode flags.
- Version the cleanup bundle as `1.0.0`.

## Implementation order

1. Bundle the scripts inside `skills/pdf-to-markdown/scripts/`.
2. Sync the canonical skill bundle to the other installed skill locations.
3. Update the skill docs so they explain the problem classes and matching passes.
4. Keep the `markdown_reflow.py` wrapper as the canonical prose-width helper.
5. Add new recurring failures to the reference notes only when they are truly generic.
6. Add regression tests in `scripts/tests/` for every parser, pass, and CLI surface that changes.

## Validation

- `python scripts/pdf_to_markdown.py --list-passes`
- `python scripts/markdown_reflow.py --help`
- `python scripts/repair_flattened_tables.py --help`
- `python -m unittest discover -s scripts/tests`
- markdown lint on edited skill docs and plan files

## Risks

- Overfitting a generic pass to one layout style.
- Copy drift between repo-local and installed skill bundles.
- Adding too many book-specific corrections to the default profile.
