# Changelog

All notable changes to `pdf-to-markdown` are documented here.

The project follows semantic versioning:

- MAJOR: incompatible behavior changes
- MINOR: new backward-compatible capabilities
- PATCH: backward-compatible fixes and clarifications

## [1.0.0] - 2026-04-27

### Added

- modular PDF-to-Markdown cleanup pipeline
- shared flattened-table repair pass
- wrap/unwrap prose-width helper
- bundled skill scripts and reference docs
- generic problem-class and layout guidance

### Changed

- moved book-specific notes into `projects/`
- standardized the skill bundle on terse topic names
- made the shared cleanup layer system-agnostic

## [1.0.1] - 2026-04-27

### Added

- explicit guidance for switching from scripted repair to semantic reading
- module-overlay proposal for project-specific JSON or YAML fixes
- regression test suite under `scripts/tests/`

### Changed

- clarified when to keep fixes in modules instead of the shared pipeline
- documented the regression-command entrypoint for script changes
