# TODO - pdf-to-markdown

## Current Focus

- pdf-to-markdown mega cleanup bundle
- canonical owner: `skills/pdf-to-markdown/`

## Scope And Boundaries

- owns the reusable PDF/OCR cleanup scripts and skill guidance
- owns generic cleanup passes, table recovery, and prose reflow helpers
- does not own book-specific manuscript text or lore corrections unless they are generalized into a reusable rule

## Active Prompt Queue

### [x] Prompt 1 — Bundle the cleanup scripts

Copy the canonical cleanup scripts into `skills/pdf-to-markdown/scripts/` and keep the bundled versions in sync with the repo-local scripts.

Context:

- the skill should ship with runnable helpers, not just prose guidance

Inputs:

- `scripts/pdf_to_markdown.py`
- `scripts/ocr_markdown_audit.py`
- `scripts/repair_flattened_tables.py`
- `scripts/markdown_reflow.py`
- `scripts/pdf_debug_passes.py`

Outputs:

- a skill-local `scripts/` bundle that mirrors the canonical behavior

Validation:

- each bundled script runs with `--help`
- the bundled `pdf_to_markdown.py` reports version `1.0.0`

Delegation notes:

- keep the bundle generic
- do not introduce repo-specific defaults into the shared copy

Status:

- completed and synced with the canonical scripts

### [x] Prompt 2 — Sync installed skill copies

Propagate the updated skill bundle to the installed skill directories so the same behavior exists everywhere the skill is loaded.

Context:

- the skill copy should not drift between repos and global installations

Inputs:

- current repo skill bundle
- installed skill directories in the user profile

Outputs:

- synchronized `SKILL.md`, `scripts/`, `references/`, and plan files

Validation:

- compare the installed bundle against the canonical bundle
- confirm the skill description and bundled scripts match

Delegation notes:

- prefer overwrite-sync over partial copy
- keep the canonical bundle as the source of truth

Status:

- completed for the lifestyle mirror and installed skill directories

### [x] Prompt 3 — Expand generic cleanup coverage

Add only agnostic cleanup lessons from other repos into the shared references or passes when they apply to any complex PDF-to-Markdown workflow.

Context:

- Tales-of-the-Old-West cleanup code contains some useful generic failure classes
- generic lessons should be separated from world-specific corrections

Inputs:

- current references and cleanup passes
- cross-repo notes from other PDF cleanup work

Outputs:

- updated problem-class guidance
- any new reusable pass or script improvement

Validation:

- the new rule applies to at least two unrelated document types
- the new behavior does not require book-specific vocabulary

Delegation notes:

- keep system-specific lore fixes out of the shared bundle
- convert them into generic structural classes where possible

Status:

- completed for the reusable cleanup coverage already absorbed into the shared bundle

## Working Rules

- canonical source first
- derived copies must be regenerated, not hand-edited where possible
- keep the skill bundle and the repo-local scripts in sync
- update the plan when a recurring failure mode becomes reusable
- stop and triage only when a fix is unsafe or ambiguous

## Decision Log

- 2026-04-27: standardize on a generic mega cleanup bundle with `1.0.0` versioning
- 2026-04-27: add `markdown_reflow.py` for wrap/unwrap paragraph normalization

## Risks And Blockers

- Potential drift between repo copies if sync is not repeated after edits.
- Some complex multi-column tables still require manual repair.
- Repo-specific corrections must remain behind profiles or local overlays.

## Template

Use this structure when the queue changes materially:

```md
# TODO - <Project Name>

## Current Focus

- epic name and one-sentence mission
- explicit canonical file or system owner

## Scope And Boundaries

- what this pass owns
- what this pass explicitly does not own

## Active Prompt Queue

### [ ] Prompt 1 — <goal>

Short prompt description.

Context:

- canonical files, systems, and assumptions this prompt depends on

Inputs:

- exact files, commands, or upstream prompts to inspect before acting

Outputs:

- expected file or system result

Validation:

- tests, lint, preview commands, or manual checks

Delegation notes:

- constraints, non-goals, and implementation guidance needed for a cheaper executor to finish safely

## Working Rules

- canonical source
- derived outputs
- rollback or safety notes
- prompt completeness and delegation readiness
- constant pushing when context allows
- cleanup removes completed prompts from the active TODO first; optional archiving happens separately, after removal, in `TODO_ARCHIVE.md` or a project-specific archive
```
