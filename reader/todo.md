# Forbidden Lands Reader — TODO

Checklist organized by development phase. Check items off as they are completed.
Add notes with `→ note` on the same line for blockers or decisions.

---

## Phase 1 — Project Scaffold

- [ ] Initialize Vite 6 + React 19 + TypeScript project in `reader/`
- [ ] Configure ESLint (TypeScript + React rules)
- [ ] Configure Prettier
- [ ] Set up CSS Modules + PostCSS
- [ ] Configure Vite path aliases (`@corebook`, `@images`, `@data`, `@styles`)
- [ ] Add Google Fonts: IM Fell Great Primer, IM Fell Double Pica, Cinzel, Libre Franklin, Cormorant SC
- [ ] Create `styles/variables.css` with full color palette + font-size scale
- [ ] Create `styles/typography.css` (all 8 semantic text roles)
- [ ] Confirm dev server runs with `npm run dev`
- [ ] Symlink `public/images` → `../analysis/images/`
- [ ] Copy `../analysis/image_manifest.json` + `../analysis/toc.json` → `src/data/`

## Phase 2 — Content Pre-processor

- [ ] Create `scripts/preprocess.ts` (Node.js build-time script)
- [ ] Install `unified`, `remark-parse`, `remark-gfm`, `rehype-react` deps
- [ ] Parse all corebook `*.md` files in chapter order (00–11)
- [ ] Emit typed segment objects: HeadingSegment / ParagraphSegment / BlockquoteSegment / TableSegment / HorizontalRuleSegment / ImageRefSegment
- [ ] Estimate pixel height per segment (formula in development_plan.md Phase 2)
- [ ] Paginate: two-column model, 53 lines per column × 2 = 106 lines per page
- [ ] Inject images from manifest by chapter matching
- [ ] Write `src/data/book-data.json`
- [ ] Add `prebuild` npm script that runs `preprocess.ts` before Vite build
- [ ] Build chapter index: `{ chapterTitle, firstPage, lastPage }[]`
- [ ] Build lunr search index + write `src/data/search-index.json`
- [ ] Test: verify all 11 chapters parse without errors
- [ ] Test: verify page count is reasonable (expect 180–220 pages)

## Phase 3 — Typography and Theme

- [ ] Implement `<PageBackground>` component (SVG noise + sepia gradient)
- [ ] Parchment SVG noise texture in `public/textures/parchment-noise.svg`
- [ ] Verify IM Fell Great Primer renders correctly at 8pt / 10.67px body size
- [ ] Implement ornamental drop cap (`::first-letter` on chapter opening paragraphs)
- [ ] Implement all 8 text role CSS classes (`.chapter-title`, `.section-heading`,
  `.subsection`, `.bold-label`, `.flavour-text`, `.body-text`, `.small-caps-deco`,
  `.body-label`)
- [ ] Add gold separator rule (`<hr class="gold-rule">`) CSS
- [ ] Side-by-side pixel comparison: rendered page vs PDF screenshot for Chapter 2

## Phase 4 — Page Layout Engine

- [ ] Create `<PageContent>` two-column CSS grid component
- [ ] Create `<TextBlock>` — renders sanitized HTML paragraphs
- [ ] Create `<TableBlock>` — GFM table with ornamental border via CSS border-image
- [ ] Design ornamental border SVG in `public/textures/ornamental-border.svg`
- [ ] Create `<Sidebar>` callout box (darker parchment bg + frame)
- [ ] Create `<ImageBlock>` (image + optional caption, aspect-ratio preserved)
- [ ] Create `<PageHeader>` (top running head: chapter name + decorative rule)
- [ ] Create `<PageFooter>` (page number centered + chapter name)
- [ ] Test: render three sample pages statically (no flip) and compare to PDF

## Phase 5 — Book Renderer

- [ ] Install `react-pageflip`
- [ ] Create `<FlipBook>` wrapping `HTMLFlipBook`
- [ ] Pass all pages from `book-data.json` as `<PageSpread>` children
- [ ] Configure `width`, `height`, `flippingTime: 800`, spread mode
- [ ] Implement cover page (single-page full bleed, `00-cover.png`)
- [ ] Implement chapter opener pages (full-art, text-free)
- [ ] CSS `transform: scale()` viewport fitting (fill screen height)
- [ ] Ensure even pages are left, odd pages are right

## Phase 6 — Physics and Interaction

- [ ] Tune `maxShadowOpacity: 0.6`, `minShadowOpacity: 0.05`
- [ ] Add CSS `filter: drop-shadow` on active page layer (lifts with animation)
- [ ] Implement spine gradient (inner page edge darkens toward gutter)
- [ ] Keyboard: `←` / `→` turn page; `Home` = cover; `End` = last page
- [ ] Click on outer 40px edge zone = turn page
- [ ] Double-click chapter art = zoom modal (Framer Motion)
- [ ] Touch/swipe: test on tablet viewport (react-pageflip native)
- [ ] Tune physics until page turn "feels heavy" (parchment weight)

## Phase 7 — Navigation and UI Chrome

- [ ] Create `<TableOfContents>` slide-in panel (from `toc.json`)
  - [ ] Nested levels h1/h2/h3 with proper indentation
  - [ ] Click entry navigates to page via `flipBook.pageFlip().flip(n)`
  - [ ] Active chapter highlighted
- [ ] Bottom bar: page number display + input field (type to jump)
- [ ] Previous / Next chapter buttons in bottom bar
- [ ] Fullscreen toggle button (`requestFullscreen`)
- [ ] URL hash sync: `#page/42` updates on turn; handle on load
- [ ] Hamburger button to open TOC panel

## Phase 8 — Search

- [ ] Install `flexsearch` (lighter than lunr.js, faster)
- [ ] Build search index from pre-processor output
- [ ] Create `<SearchOverlay>` (keyboard shortcut: `Ctrl+F` / `Cmd+F`)
- [ ] Fuzzy match against all text segments
- [ ] Results: chapter name + page number + 120-char snippet
- [ ] Click result: navigate to page; close overlay
- [ ] Keyboard: `Escape` closes; `↑` / `↓` move through results

## Phase 9 — Icon Fonts

- [ ] Install `fonttools` Python package (`pip install fonttools`)
- [ ] Write `scripts/extract_fonts.py`: extract `Swordlings.ttf` from source PDF
- [ ] Convert to WOFF2 (`fonttools` + `brotli`)
- [ ] Map FL dice/sword/shield glyphs to Unicode PUA codepoints
- [ ] Add `@font-face` for `fl-icons` in `typography.css`
- [ ] Pre-processor: convert `⚔️` / `🛡️` → `<span class="fl-icon">X</span>`
- [ ] Test all icon characters render at body text size

## Phase 10 — Polish and Responsive

- [ ] Responsive breakpoints:
  - [ ] ≥ 1400px: full two-page spread
  - [ ] 768–1399px: single page, full height
  - [ ] < 768px: scroll mode (no flip, linear chapter scroll)
- [ ] "Dark room" mode toggle: `rgba(0,0,0,0.6)` overlay + vignette + book glows
- [ ] Optional page-turn sound (Web Audio API, toggle in menu, off by default)
- [ ] Print CSS: disable flip, paginated print layout
- [ ] All images: `alt` text from manifest `role_guess` + chapter name
- [ ] ARIA `role="document"` on FlipBook, `aria-label` on page turns
- [ ] Lazy-load images beyond current spread ±2 pages
- [ ] Run Lighthouse audit: target ≥ 80 performance, ≥ 95 accessibility
- [ ] Production build: `npm run build` exits clean, zero TS errors

## Phase 11 — QA and Definition of Done

- [ ] All 11 chapters render without content gaps
- [ ] Page turn physics acceptable on Chrome, Firefox, Safari
- [ ] Works on iPad-class device (1024px touch screen)
- [ ] Full-text search returns correct results for 10 test queries
- [ ] TOC navigates correctly to all chapter first-pages
- [ ] Zero console errors on production build
- [ ] Side-by-side comparison: 5 random pages vs PDF — ≥ 95% layout match
- [ ] `README.md` complete with local dev setup instructions
