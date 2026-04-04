# Changelog

All notable changes to the FL Reader project follow
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.

---

## [Unreleased]

### Planned

- Full content pipeline from corebook markdown
- Physics-based page turning (react-pageflip)
- Two-column typographic layout matching print edition
- Full-text search with flexsearch
- TOC navigation panel
- Icon font extraction from source PDF

---

## [0.0.0] — 2026-04-04

### Added

- Project planning documents: `development_plan.md`, `todo.md`,
  `development_log.md`, `changelog.md`
- PDF layout analysis complete: 339 images extracted, 401 tables detected,
  445 TOC bookmark entries, full font matrix produced
- `analyze_pdf.py` script for future re-analysis runs
- Extracted CSS approximation (`analysis/extracted_styles.css`)
- Image chapter manifest (`analysis/image_manifest.json`)
