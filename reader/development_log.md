# Development Log

Chronological record of decisions, discoveries, and blockers.

---

## 2026-04-04 — Project kickoff

### Context

Initiated the FL Reader project. Source PDF fully analyzed.

### PDF Analysis Findings (key facts for renderer design)

- **Page dimensions**: 481.89 × 680.32 pt (≈ B5 format, slightly narrower)
- **Layout**: Predominantly two-column across all body chapters
- **Body font**: `IM_FELL_Great_Primer_Rom` at 8pt / 10.67px — available as
  "IM Fell Great Primer" on Google Fonts
- **Chapter titles**: `IM_FELL_THREE_LINE_PICA` at 23pt — closest match is
  IM Fell Great Primer SC or Cinzel Decorative
- **Section headings**: `IM_FELL_Double_Pica_Roma` at 14.7pt
- **Subsection**: `FFJustlefthandCapsMedium` — hand-lettered caps, substitute Cinzel
- **Labels / sidebars**: `Branding-Medium` / `Branding-Bold` — substitute Libre Franklin
- **Icon font**: `Swordlings` — FL custom dice/weapon glyphs; extractable from PDF
- **Decorative**: `SkullZ`, `ZapfDingbatsStd` — small ornaments
- **Total unique images**: 339 (PNG, alpha retained)
- **Tables detected**: 401 across 212 pages
- **TOC entries**: 445 (deeply nested chapter/section/subsection)
- **Corebook content**: 11 chapters, ~13 000 markdown lines, ~13 400 build-time lines
  in local corebook

### Architecture Decisions

- **Content pipeline runs at build time** (Node.js preprocess script → `book-data.json`).
  The browser never parses markdown at runtime. This keeps rendering fast and page
  breaks deterministic.

- **react-pageflip chosen for physics layer** over a custom Three.js approach.
  StPageFlip uses HTML5 Canvas with a well-tested Bezier curl simulation. Physics tuning
  via `flippingTime` and shadow opacity params is sufficient for the "heavy parchment"
  feel without custom shader work.

- **Pagination uses line-height estimation** (8pt × 1.45 ≈ 11.6pt line height;
  ~620pt usable column height ≈ 53 lines per column; 106 lines per two-column page).
  Tables and images use fixed height estimates from manifest metadata.
  Manual `<!-- BREAK -->` markers in markdown allow authors to force page breaks.

- **Image assignment**: The manifest's `chapters[]` field (set during PDF extraction)
  maps each image to its chapter. During pre-processing, images are injected at the
  first occurrence of their chapter heading. Oversized images become chapter art on
  their own page.

- **Font fallback strategy**: IM Fell series is the only irreplaceable visual element.
  It is self-hosted as WOFF2 (download from Google Fonts CDN at build time). Cinzel
  covers the chapter-title / subsection roles adequately. Libre Franklin is a
  reasonable Branding substitute. Swordlings must be extracted from the PDF with
  fonttools — this is a Phase 9 task and does not block earlier phases.

- **Color palette**: PyMuPDF returned garbled hex values for text colors (encoding
  artifact in multi-byte color space). Colors have been manually identified from
  visual inspection of the PDF. See `development_plan.md` for the corrected palette.

- **No SSR**: purely client-side SPA. Page data is static JSON loaded once.
  Virtualizing page DOM nodes (keep only current spread ±4 pages in the DOM) is
  planned for Phase 10 to handle the full 200+ page count without memory pressure.

### Open Questions

- Can `SkullZ` and `ZapfDingbats` glyphs be extracted and legally redistributed?
  → These are standard ornament fonts; check license. Fallback: use SVG sprites.

- The cover image `00-cover.png` in the local corebook is a clean version (no text
  overlay). Should the reader show the splash-art-only cover or a recreation of the
  full cover with stamped text? → Decision deferred to Phase 5.

- Should the pre-processor track proposal changes (the local corebook already has 2E
  houserule proposals applied)? → Yes. The reader renders the local `corebook/`
  canonical version, not the upstream public repo.

### Blockers

None currently.

### Next Step

Begin Phase 1: scaffold the Vite project.
