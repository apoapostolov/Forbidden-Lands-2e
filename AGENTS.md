# Repository agent guidance

## Scope and authority

- This file governs the entire repository. Work on `main`; releases, version
  commits, and tags MUST be made from `main`. Do not create agent branches.
- Preserve unrelated working-tree changes. Never replace substantive material
  with summaries, templates, cleanup prose, or reorganized approximations.
- Published book chapters are rules sources; `proposals/` and files named
  `*-proposal.md` are design records, not canonical rules until implemented.

## Skill routing

- Read every selected `SKILL.md` completely before acting; load only the
  references it routes to for the task.
- Rules, subsystems, professions, spells, talents, strongholds:
  `/forbidden-lands-design`; add `/forbidden-lands-synergy-analysis` when rules
  combine, stack, renew resources, alter authority, or affect campaign play.
- Monsters, human enemies, beasts, demons, encounters, Lore Rolls, salvage:
  `/forbidden-lands-bestiary`.
- Canon, chronology, places, kin, factions, religion, and regional continuity:
  `/forbidden-lands-lore`.
- Premodern survival, work, material culture, custom, faith, violence, care, or
  psychology: `/forbidden-lands-medieval-authenticity`.
- Final manuscript wording, rules voice, examples, and GM-facing situations:
  `/forbidden-lands-writing-voice`.
- Engine-independent YZE construction or comparison: `/yze-design`.
- Use `changelog-generator` for changelog work and `agents-md` for this file.
  For compound work, use the smallest stack that covers every material claim.

## Changelog policy

- `CHANGELOG.md` is for players and Game Masters. Record only material new
  content, changed rules, removed options, compatibility breaks, and substantial
  public skill capabilities.
- Never changelog audits, analysis passes, proposals, refactors, formatting,
  presentation, metadata, file organization, prompt wiring, validation, or
  minor wording cleanup unless it changes how the game is played or adjudicated.
- Under `[Unreleased]`, use `Added`, `Changed`, `Removed`, and `Fixed` only as
  needed. Write one concise entry per coherent player- or GM-visible feature
  type, not per file, table, spell, or implementation step.
- Book labels MUST follow **Book 01 — Corebook, casting modes.** Substitute
  **Book 02 — Gamemaster's Guide** or **Book 03 — Book of Beasts** as needed.
- Skill labels MUST follow **`/forbidden-lands-bestiary` — adversary
  construction.** Use the slash-command name, never an internal reference
  filename or a generic workstream label.
- Lead with what is now possible at the table. Include exact numbers only when
  they help readers judge scope, access, risk, or compatibility.

## README and release management

- `README.md` is a stable edition overview, not a second changelog. Update it
  only for a release/version change, a major book feature, a public skill being
  added/removed/renamed, or a changed installation or usage path.
- Keep `## What this edition brings` cumulative and capability-focused. Do not
  add audits, process history, minor revisions, or Unreleased implementation
  detail.
- When cutting a release, move applicable Unreleased entries under the dated
  version, restore a fresh `[Unreleased]` section, update README version claims,
  and tag the release only after the main-branch commit is verified.

## Validation and publication

- Run `git diff --check` and `markdownlint-cli2` on changed Markdown files.
  Check headings, tables, cross-references, and terminology in rendered context.
- Do not commit, tag, push, publish, or rewrite history unless the user asks.
