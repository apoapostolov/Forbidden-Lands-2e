# TODO: PDF to RPG Markdown Expansion Plan

## Phase 1: Extraction and Audit Foundations

- [x] Audit the existing `scripts/pdf_to_markdown.py` pipeline and identify its current passes, assumptions, and blind spots.
- [x] Define the core OCR artifact taxonomy for RPG books: page furniture, running headers, decorative headings, flattened tables, sidebars, epigraphs, and drop-cap damage.
- [x] Add a separate OCR audit script that weaker agents can run before editing to classify likely damage.
- [x] Document the minimum safe output set: raw extraction, clean manuscript, and optional audit report.

## Phase 2: Repair Heuristics and Training Material

- [x] Expand the `pdf-to-rpg-markdown` skill into a phased workflow written explicitly for weaker agents.
- [x] Add a repair playbook that explains what to fix first and what must never be guessed.
- [x] Add a table reconstruction manual for image-text tables, merged headers, dice tables, and flattened matrix tables.
- [x] Add quality gates and escalation rules so agents know when to stop automating and ask for review.

## Phase 3: Script Capability Upgrades

- [x] Extend the converter pipeline so it can emit a structured OCR artifact report alongside `.raw.md` and cleaned markdown.
- [x] Add optional document profiles tuned for common RPG layouts: corebook, supplement, spell compendium, bestiary, lifepath generator.
- [x] Add stronger paragraph-rejoin heuristics for dropped initial letters, split all-caps headings, and repeated footer bleed.
- [x] Strengthen page-furniture recognition so repeated short header and footer strings can be inferred from page-sized chunks, not just explicit page-number lines.
- [x] Add safer table conversion helpers for common single-line OCR matrix dumps.
- [x] Add chapter split helpers that work for non-`Chapter N` section books.

## Phase 4: Reference Corpus and Calibration

- [x] Build a reference set of before-and-after examples from repo documents: towns, spells, battles, legends.
- [x] Record common Forbidden Lands-specific OCR errors: kin names, talent paths, discipline names, and recurring layout phrases.
- [x] Add a "high-confidence correction list" separate from speculative lore repairs.
- [x] Add examples of when not to repair automatically.

## Phase 5: Operationalization for Other Agents

- [x] Add an `agents/openai.yaml` entrypoint for invoking the skill cleanly.
- [x] Add a standard turn template for agents: diagnose, plan, process, verify, report.
- [x] Add a review checklist for human spot-checking after a long OCR cleanup pass.
- [x] Add a triage worksheet for deciding whether a document needs automation only, automation plus manual repair, or full manual reconstruction.

## Phase 6: Regression and Advanced Automation

- [ ] Build regression fixtures from actual repo raw and clean pairs so script changes can be checked against known outputs.
- [ ] Add supplement-specific correction packs for recurring local OCR errors beyond the current high-confidence list.
- [ ] Add a matrix-table classifier that can route simple one-line tables to automation and complex layouts to manual review.
- [ ] Add section-splitting presets for common supplement structures such as `Introduction`, `New Rules`, and discipline or appendix headings.
- [ ] Add an end-to-end processing playbook for long books that combines audit, profile selection, helper scripts, lint, and chapter splitting in one documented loop.
