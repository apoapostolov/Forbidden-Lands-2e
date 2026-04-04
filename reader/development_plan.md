# Forbidden Lands 2E — Web Book Reader: Development Plan

## Project Overview

A browser-based interactive book reader that renders the Forbidden Lands 2nd Edition
corebook with physics-based page turning, exact typographic fidelity to the print
edition, and a two-column spread layout. Content is sourced from the markdown corebook;
images from the PDF extraction pipeline.

**Target feel:** Opening a physical copy of the book. Parchment texture. Heavy fonts.
Weighted page physics. No "app" chrome — pure book.

---

## Source Materials

| Asset | Location |
|-------|----------|
| Corebook markdown | `../corebook/` (11 chapters, ~13 000 lines) |
| Extracted PDF images | `../analysis/images/` (339 PNGs, alpha retained) |
| Image manifest | `../analysis/image_manifest.json` |
| TOC structure | `../analysis/toc.json` |
| CSS approximation | `../analysis/extracted_styles.css` |

---

## Technical Architecture

### Tech Stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Build tool | Vite 6 + TypeScript | Fast HMR, native ESM, good TS support |
| UI framework | React 19 | Component model suits page/spread tree |
| Page physics | `react-pageflip` (StPageFlip) | Canvas-based, real curl physics, touch support |
| Markdown parser | `unified` + `remark-parse` + `rehype-react` | Extensible AST, custom element mapping |
| Animations | `framer-motion` | Entrance/exit animations for non-flip UI |
| CSS | CSS Modules + CSS custom properties | Scoped styles, book theme variables |
| Testing | Vitest + Testing Library | Unit + component tests |
| Dev server | Vite with `--host` | Local LAN accessible for tablet testing |

### Content Pipeline

```text
corebook/*.md
  └─ [preprocess.ts] ─→ AST segments (heading / para / table / blockquote / image-ref)
       └─ [paginate.ts] ─→ virtual pages (estimated line heights → page breaks)
            └─ [manifest-merge.ts] ─→ inject image nodes from image_manifest.json
                 └─ book-data.json  ─→  consumed by React renderer at runtime
```

The pre-processor runs at build time (`npm run prebuild`) and writes
`src/data/book-data.json`. The renderer is pure React — no runtime markdown parsing.

### Page Layout Model

Each "page" is a fixed-size React component matching the extracted book dimensions:

- **Page size**: 482 × 680 pt → scaled to viewport via CSS `transform: scale()`
- **Layout**: Two-column grid (column gap ~12pt) for body chapters
- **Single column**: Cover, chapter openers, full-page art spreads
- **Text flow**: CSS Multi-column with `column-fill: auto` inside fixed-height containers
- **Overflow detection**: Node.js pagination script measures estimated line heights and
  hard-splits content blocks across page boundaries

### Page Physics Implementation

Uses `react-pageflip`:

- Each `<Page>` component passed as a child
- `width` / `height` props match the rendered page dimensions
- `flippingTime` set to 800 ms (weighted feel)
- `useMouseEvents` + `useKeyboard` enabled
- `startPage` prop for TOC navigation
- Shadow intensity tuned for parchment (darker at spine, lighter at edge)

Custom CSS layered on top:

- Parchment texture overlay (SVG noise + sepia gradient)
- Drop shadow on active page (simulates page lifting off stack)
- Spine gradient on inner page edge
- Page curl CSS shadow during animation

### Typography System

All fonts loaded via `@font-face`. Priority mapping from PDF extraction:

| Role | PDF font | Web font | Fallback |
|------|----------|----------|---------|
| Body | `IM_FELL_Great_Primer_Rom` | IM Fell Great Primer (Google Fonts) | Georgia, serif |
| Body italic | `IM_FELL_Great_Primer_Ita` | IM Fell Great Primer Italic | Georgia, italic |
| Section heading | `IM_FELL_Double_Pica_Roma` | IM Fell Double Pica | IM Fell Great Primer |
| Chapter title | `IM_FELL_THREE_LINE_PICA` | IM Fell Great Primer SC | Cinzel Decorative |
| Subsection caps | `FFJustlefthandCapsMedium` | Cinzel (Google Fonts) | Trajan Pro |
| Bold label | `Branding-Bold` | Libre Franklin Bold | Franklin Gothic |
| Medium body label | `Branding-Medium` | Libre Franklin | Franklin Gothic |
| Small caps decorative | `NorthwoodHigh-SC700` | Cormorant SC (Google Fonts) | EB Garamond |
| Dice / icons | `Swordlings` / `ZapfDingbats` | Extracted FL icon font (WOFF2) | Unicode fallback |

### Book Color Palette

Extracted from PDF palette analysis (corrected for PyMuPDF encoding artifacts):

```css
:root {
  --page-bg:           #f5ede0;   /* aged parchment */
  --page-bg-dark:      #e8d9c4;   /* verso page, slightly darker */
  --text-primary:      #1a1208;   /* near-black ink */
  --text-heading:      #2c1a0e;   /* dark brown heading */
  --text-accent:       #8b1a1a;   /* blood-red accent (drop caps, rules) */
  --border-ornamental: #5c3d1e;   /* table borders and frame lines */
  --sidebar-bg:        #ede0cb;   /* inset sidebar / callout boxes */
  --spine-dark:        #1a0f06;   /* book spine deepest shadow */
  --gold-rule:         #b8960c;   /* thin gold separator rules */
}
```

### Component Tree

```text
<App>
 └─ <BookReader>
      ├─ <TableOfContents>       — slide-in TOC overlay
      ├─ <SearchOverlay>         — full-text search
      ├─ <BookmarkPanel>         — saved page positions
      └─ <FlipBook>              — react-pageflip root
           └─ <PageSpread>       — one page; rendered × N pages
                ├─ <PageBackground>   — parchment texture + shadow layer
                ├─ <PageHeader>       — chapter title + page number
                ├─ <PageContent>      — two-column content grid
                │    ├─ <TextBlock>
                │    ├─ <TableBlock>  — with ornamental borders
                │    ├─ <Sidebar>     — inset callout boxes
                │    └─ <ImageBlock>  — chapter art with caption
                └─ <PageFooter>       — page number + chapter name
```

---

## Development Phases

### Phase 1 — Project Scaffold

- Vite 6 + React 19 + TypeScript project init
- ESLint + Prettier config
- CSS Modules + PostCSS setup
- Google Fonts integration (IM Fell series, Cinzel, Libre Franklin, Cormorant SC)
- Base CSS variables (colors, fonts, spacing)
- Vite aliases: `@corebook`, `@images`, `@data`

### Phase 2 — Content Pre-processor (Node.js build script)

- Read all `../corebook/*.md` files in chapter order
- Parse with `unified` + `remark-parse` into MDAST
- Walk AST, emit typed segment objects:
  - `HeadingSegment` (level 1–4, text, id)
  - `ParagraphSegment` (html string, estimated height in pt)
  - `BlockquoteSegment` (flavour text)
  - `TableSegment` (header rows, data rows, column count)
  - `HorizontalRuleSegment`
  - `ImageRefSegment` (resolved from image manifest by chapter)
- Paginate: walk segments, pack into pages using estimated heights
  - Line height: 8pt text × 1.45 = 11.6pt per line; column height ~620pt ≈ 53 lines
  - Two columns × 53 lines = ~106 lines per page
- Write `src/data/book-data.json` with full page array + TOC index

### Phase 3 — Typography & Theme Layer

- Implement all CSS custom properties from palette
- `<PageBackground>` component: SVG noise texture + sepia gradient overlay
- Page shadow system (box-shadow layers on spread)
- Implement all 8 semantic text classes (`.chapter-title`, `.section-heading`, etc.)
- Verify font rendering matches PDF screenshots at 1:1 scale
- Ornamental drop cap (`::first-letter` styled with IM Fell)

### Phase 4 — Page Layout Engine

- `<PageContent>` two-column CSS grid layout
- `<TextBlock>` renders HTML from segment (dangerouslySetInnerHTML, sanitized at
  build time)
- `<TableBlock>` with CSS border-image using ornamental border PNGs extracted from
  analysis/images
- `<Sidebar>` inset callout with parchment-darker background + ornamental frame
- `<ImageBlock>` with `object-fit: contain`, max sizing, caption
- `<PageHeader>` and `<PageFooter>` with running heads (chapter name) + page number

### Phase 5 — Book Renderer (FlipBook assembly)

- `<FlipBook>` wraps `HTMLFlipBook` from `react-pageflip`
- Renders all pages from `book-data.json`
- Spread mode: two pages visible (even = left, odd = right)
- Cover: single-page full bleed (0-cover.png)
- Chapter openers: single-page no-text art spread, fade into first content page
- Scale to viewport: `transform: scale()` on wrapper so pages fill screen height

### Phase 6 — Physics Tuning + Interaction

- Tune `flippingTime`, `maxShadowOpacity`, `minShadowOpacity` in react-pageflip
- Add CSS transition on lifted-page drop-shadow (`filter: drop-shadow`)
- Keyboard: `←` / `→` turn page; `Home` = cover; `End` = last page
- Touch/swipe: native via react-pageflip; test on tablet viewport
- Click on page edge zone (outer 40px) to turn page
- Double-click chapter art: zoom modal (Framer Motion scale transition)

### Phase 7 — Navigation & UI Chrome

- `<TableOfContents>` slide-in panel (left edge): renders from `toc.json`
  - Nested levels (h1/h2/h3), click navigates to page
- Page number input field in bottom bar (type page number, jump)
- Previous/Next chapter buttons
- Fullscreen toggle (`document.documentElement.requestFullscreen()`)
- URL hash sync: `#page/42` updates as you turn pages; navigable

### Phase 8 — Search

- Full-text index built at pre-process time (lunr.js or flexsearch)
- Search overlay: fuzzy match against all text segments
- Results show chapter, page number, snippet
- Jump to page from result

### Phase 9 — Icon Fonts and Dice Symbols

- Extract `Swordlings.ttf` / `ZapfDingbats` WOFF2 from PDF using fonttools (`pip
  install fonttools`)
- Map FL-specific characters (⚔️ sword, shield, etc.) to Unicode private-use codepoints
- Load via `@font-face` in CSS
- Pre-processing converts Markdown emoji (`⚔️`) to `<span class="fl-icon">` elements

### Phase 10 — Polish and Responsive

- Responsive scaling: full spread (desktop ≥ 1400px), single page (tablet), scroll
  mode (mobile < 768px)
- Dark room mode: ambient overlay (`rgba(0,0,0,0.6)` + vignette), book glows like lit
  by candlelight
- Page sound: optional paper-rustle audio on page turn (Web Audio API, toggle)
- Print CSS: usable as PDF export source (no flip, paginated print media)
- Accessibility: ARIA `role="document"`, all images have alt text from manifest
- Performance: lazy-load images beyond current spread ±2 pages

---

## File Structure

```text
reader/
  development_plan.md          ← this file
  development_log.md
  changelog.md
  todo.md
  README.md                    ← created Phase 1
  src/
    main.tsx
    App.tsx
    components/
      BookReader/
      FlipBook/
      Page/
      PageContent/
      TextBlock/
      TableBlock/
      Sidebar/
      ImageBlock/
      TableOfContents/
      SearchOverlay/
    hooks/
      useBook.ts
      usePageFlip.ts
      useKeyboard.ts
      useFullscreen.ts
    data/
      book-data.json           ← generated by prebuild
      image-manifest.json      ← symlinked from ../analysis/
      toc.json                 ← symlinked from ../analysis/
    styles/
      variables.css
      typography.css
      page.css
      table.css
      sidebar.css
      flipbook.css
    utils/
      paginator.ts             ← height estimation + page break logic
      markdownParser.ts
      manifestMerger.ts
    scripts/
      preprocess.ts            ← build-time content pipeline
  public/
    fonts/                     ← self-hosted WOFF2 (IM Fell, Cinzel, etc.)
    images/                    ← symlinked from ../analysis/images/
    textures/
      parchment-noise.svg
      parchment-dark.svg
      ornamental-border.svg
    audio/
      page-turn.mp3
  index.html
  vite.config.ts
  tsconfig.json
  package.json
  .eslintrc.json
  .prettierrc
```

---

## Key Constraints and Risks

| Risk | Mitigation |
|------|-----------|
| Two-column text overflow across pages is hard to compute | Use estimated line heights in pre-processor; allow manual page-break markers `<!-- BREAK -->` in markdown |
| Proprietary fonts not extractable | Use closest Google Fonts substitutes; accept minor glyph differences |
| react-pageflip performance on low-end devices | Cap simultaneous canvas layers; single-page mobile fallback |
| Image transparency artifacts | All images already PNG from PyMuPDF; spot-check alpha layers on complex art |
| Long chapters (07-magic.md = 4895 lines) | Paginate at build time; never load more than 20 pages into DOM at once (virtualization) |
| Table ornament borders require art assets | Extract from PDF analysis images; or hand-draw as SVG |

---

## Definition of Done

A build is shippable when:

- All 11 chapters render without content gaps or overflows
- Page turn physics feel weighted and natural on desktop and tablet
- Typography matches the print book at 95%+ visual fidelity
- Full-text search returns results within 200 ms
- TOC navigation jumps to correct page number
- Lighthouse score ≥ 80 (performance), ≥ 95 (accessibility)
- Zero console errors in production build
