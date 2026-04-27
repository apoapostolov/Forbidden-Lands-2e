# Module overlay proposal for `pdf-to-markdown`

## Purpose

Keep the shared `pdf-to-markdown` scripts generic while allowing one project, one manuscript, or one document family to carry its own correction data in external JSON or YAML overlays.

The core rule is simple:

- shared code owns shared structure
- module overlays own project-specific corrections
- retired project logic stays out of the script body

That keeps the pipeline flexible without turning `pdf_to_markdown.py` into a dump of dead special cases.

## Why modules exist

Some corrections are real, useful, and still not generic.

Examples:

- repeated title fragments tied to one book or one campaign line
- book-specific footer text that should never become a shared default
- metadata glyph repairs that only apply to one document family
- one-off heading fixes that are safe in a single project but wrong elsewhere

These belong in a module overlay, not in the shared Python script.

## Where modules live

Proposed layout:

- `skills/pdf-to-markdown/projects/modules/registry.yaml` — active module list
- `skills/pdf-to-markdown/projects/modules/<module-id>.yaml` — human-edited overlay
- `skills/pdf-to-markdown/projects/modules/<module-id>.json` — optional machine-exported form
- `skills/pdf-to-markdown/projects/modules/archive/` — retired modules kept for history

If JSON is easier for tooling, keep YAML as the authoring format and export JSON for validation. If the team prefers JSON first, the same field set applies.

## Proposed schema

A module should describe four things:

1. what it applies to
2. what it may change
3. what it must never touch
4. how it is validated

### Core fields

- `schema_version` — schema revision for the overlay format
- `module_id` — stable identifier, usually slug-style
- `title` — human-readable name
- `status` — `draft`, `active`, `archived`
- `scope` — `project`, `document-family`, or `document`
- `applies_to` — titles, profiles, signals, or content markers
- `overlays` — safe correction data
- `guards` — exclusions and safety rules
- `evidence` — examples and the reason each rule exists
- `tests` — fixtures or assertions that prove the overlay still works
- `provenance` — where the rule came from and when it was last reviewed
- `expires` — optional retirement or review date

### Overlay blocks

A module overlay may contain only data, not executable code.

Suggested blocks:

- `heading_corrections`
- `dropcap_replacements`
- `footer_phrases`
- `regex_replacements`
- `pass_overrides`
- `skip_passes`
- `layout_hints`
- `manual_review_triggers`
- `fixture_paths`

That keeps the core script simple: read the overlay, apply the safe fields, log what happened.

## Example YAML overlay

```yaml
schema_version: 1
module_id: forbidden-lands-corebook
status: active
scope: document-family
title: Forbidden Lands corebook overlay
applies_to:
  profiles:
    - corebook
  title_contains:
    - Forbidden Lands
  signals:
    - repeated chapter-name footer
    - spell metadata glyphs
    - known title-fragment repairs
overlays:
  heading_corrections:
    Or Bidden F Lands: Forbidden Lands
    Forbid Den Lands: Forbidden Lands
  dropcap_replacements:
    "elcome ": "Welcome "
    "his ": "This "
  footer_phrases:
    - forbidden lands
  regex_replacements:
    - pattern: '(?m)^E RANK (\d+)$'
      replacement: '- Rank: \1'
      scope: spell_metadata
      confidence: high
guards:
  never_touch:
    - prose paragraphs without a direct match in evidence
    - tables unless the rule explicitly targets table cells
  min_confidence: high
evidence:
  - file: projects/forbidden-lands.md
    note: project-specific corrections kept out of shared code
  - file: examples/corebook-spell-block.md
    note: sample metadata block that justifies the glyph repair
tests:
  fixtures:
    - input: fixtures/forbidden-lands/spell-block.raw.md
      expected: fixtures/forbidden-lands/spell-block.clean.md
provenance:
  source: manual review of recurring project-specific OCR damage
  last_reviewed: 2026-04-27
expires:
  review_after: 2026-10-01
```

## Example JSON shape

The JSON form should be the same information with the same field names.

```json
{
  "schema_version": 1,
  "module_id": "forbidden-lands-corebook",
  "status": "active",
  "scope": "document-family",
  "title": "Forbidden Lands corebook overlay",
  "applies_to": {
    "profiles": ["corebook"],
    "title_contains": ["Forbidden Lands"],
    "signals": ["repeated chapter-name footer", "spell metadata glyphs"]
  },
  "overlays": {
    "footer_phrases": ["forbidden lands"],
    "heading_corrections": {
      "Or Bidden F Lands": "Forbidden Lands"
    }
  },
  "guards": {
    "never_touch": ["prose paragraphs without a direct match in evidence"],
    "min_confidence": "high"
  }
}
```

## How the core skill should use modules

The core skill should treat overlays as data files, not as a place to hide new code.

Recommended loop:

1. extract or inspect the document
2. classify the damage as generic or project-specific
3. look for a matching active module
4. apply only the module fields that are safe and directly supported
5. write the correction back to the module file, not the script body
6. add or update a regression test when the rule is stable
7. move dead project logic into the archive instead of keeping it active

## When a module may be promoted

A module rule can move upward only when it proves itself at each stage.

- **Module only:** one project, one layout family, or one manuscript set
- **Shared reference:** applies to multiple unrelated books with the same structural damage
- **Core script:** generic transformation, reliable regression coverage, no setting vocabulary

If the rule still depends on a setting name, a chapter list, or a project-specific footer, keep it in the module.

## Retirement policy

Archive modules when:

- the project is complete and no longer active
- the module is superseded by a more generic rule
- the module was only needed for one historical import pass

Archived modules should stay readable for provenance, but they should not be part of the active default path.

## Open questions

- Should the authoring format be YAML first and JSON export only, or should both be first-class?
- Should the registry be explicit, or should the loader discover modules by folder name?
- Should the skill auto-write module changes immediately, or queue them for review when confidence is low?
- Which module fields are safe to auto-promote without human approval?

## Recommendation

Use YAML for authoring, JSON for machine validation, and keep the active module registry separate from the shared script.

That gives the skill a place to learn without stuffing the core pipeline full of dead special cases.
