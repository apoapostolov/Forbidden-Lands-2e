# Forbidden Lands Reader — TODO

Checklist organized by development phase. Check items off as they are completed.
Add notes with `→ note` on the same line for blockers or decisions.

---

## Phase 1 — Project Scaffold ✅

- [x] Initialize Vite 6 + React 19 + TypeScript project in `reader/`
- [x] Configure ESLint (TypeScript + React rules)
- [x] Configure Prettier
- [x] Set up CSS Modules + PostCSS
- [x] Configure Vite path aliases (`@corebook`, `@images`, `@data`, `@styles`)
- [x] Add Google Fonts: IM Fell Great Primer, IM Fell Double Pica, Cinzel, Libre Franklin, Cormorant SC
- [x] Create `styles/variables.css` with full color palette + font-size scale
- [x] Create `styles/typography.css` (all 8 semantic text roles)
- [x] Confirm dev server runs with `npm run dev`
- [x] Symlink `public/images` → `../analysis/images/`
- [x] Copy `../analysis/image_manifest.json` + `../analysis/toc.json` → `src/data/`

## Phase 2 — Content Pre-processor ✅

- [x] Create `scripts/preprocess.ts` (Node.js build-time script)
- [x] Install `unified`, `remark-parse`, `remark-gfm`, `rehype-react` deps
- [x] Parse all corebook `*.md` files in chapter order (00–11)
- [x] Emit typed segment objects: HeadingSegment / ParagraphSegment / BlockquoteSegment / TableSegment / HorizontalRuleSegment / ImageRefSegment
- [x] Estimate pixel height per segment (formula in development_plan.md Phase 2)
- [x] Paginate: two-column model, 53 lines per column × 2 = 106 lines per page
- [x] Inject images from manifest by chapter matching
- [x] Write `src/data/book-data.json`
- [x] Add `prebuild` npm script that runs `preprocess.ts` before Vite build
- [x] Build chapter index: `{ chapterTitle, firstPage, lastPage }[]`
- [x] Build flexsearch fulltext index + write `src/data/search-index.json`
- [x] Test: verify all 11 chapters parse without errors
- [x] Test: verify page count is reasonable (290 pages across 11 chapters)

## Phase 3 — Typography and Theme ✅

- [x] Implement `<PageBackground>` component (white paper, no sepia)
- [x] Verify IM Fell Great Primer renders correctly at 8pt / 10.67px body size
- [x] Implement all 8 text role CSS classes (`.chapter-title`, `.section-heading`,
  `.subsection`, `.bold-label`, `.flavour-text`, `.body-text`, `.small-caps-deco`,
  `.body-label`)
- [x] Add gold separator rule (`<hr class="gold-rule">`) CSS
- [x] Brand color palette (black ink on white paper per PDF)

## Phase 4 — Page Layout Engine ✅

- [x] Create `<PageContent>` two-column CSS grid component
- [x] Create `<TextBlock>` — renders sanitized HTML paragraphs
- [x] Create `<TableBlock>` — GFM table with ornamental border via CSS border-image
- [x] Create `<ImageBlock>` (image + optional caption, aspect-ratio preserved)
- [x] Create `<PageHeader>` (top running head: chapter name + decorative rule)
- [x] Create `<PageFooter>` (page number centered)
- [x] Create `<PageHeaderBanner>` (landscape book art header on each page)
- [x] Create `<DecorativeDivider>` (diamond-pattern dividers)

## Phase 5 — Book Renderer ✅

- [x] Install `react-pageflip`
- [x] Create `<BookReader>` wrapping `HTMLFlipBook`
- [x] Pass all pages from `book-data.json` as `<PageSpread>` children
- [x] Configure `width`, `height`, `flippingTime: 800`, spread mode
- [x] Implement cover page (single-page full bleed)
- [x] Implement chapter opener pages (full-art, text-free)
- [x] CSS `transform: scale()` viewport fitting (fill screen height)
- [x] Ensure even pages are left, odd pages are right

## Phase 6 — Physics and Interaction ✅

- [x] Tune `maxShadowOpacity: 0.6`, `minShadowOpacity: 0.05`
- [x] Add CSS `filter: drop-shadow` on active page layer (lifts with animation)
- [x] Implement spine gradient (inner page edge darkens toward gutter)
- [x] Keyboard: `←` / `→` turn page; `Home` = cover; `End` = last page
- [x] Click on outer 40px edge zone = turn page
- [x] Double-click chapter art = zoom modal (Framer Motion)
- [x] Touch/swipe: test on tablet viewport (react-pageflip native)
- [x] Page turn feels "heavy" (parchment weight)

## Phase 7 — Navigation and UI Chrome ✅ (with minor fixes needed)

- [x] Create `<TableOfContents>` slide-in panel (from `toc.json`)
  - [x] Nested levels h1/h2/h3 with proper indentation
  - [ ] **BUG** Click entry navigates to wrong page (off by 1 or more)
  - [x] Active chapter highlighted
- [x] Bottom bar: page number display + input field (type to jump)
- [x] Previous / Next chapter buttons in bottom bar
- [x] Fullscreen toggle button (`requestFullscreen`)
- [x] URL hash sync: `#page/42` updates on turn; handle on load
- [x] Hamburger button to open TOC panel

## Phase 8 — Search ✅

- [x] Install `flexsearch` (lighter than lunr.js, faster)
- [x] Build search index from pre-processor output
- [x] Create `<SearchPanel>` (keyboard shortcut: `Ctrl+F` / `Cmd+F`)
- [x] Full-text fuzzy match against all text segments
- [x] Results: page number + context snippet + matched text highlighted
- [x] Hover results for preview navigation + paragraph highlighting
- [x] Click result: navigate to page; close search panel
- [x] Keyboard: `Escape` closes; `↑` / `↓` move through results

## Phase 9 — Icon Fonts and Symbol Replacement

- [ ] Install `fonttools` Python package (`pip install fonttools`)
- [ ] Write `scripts/extract_fonts.py`: extract `Swordlings.ttf` from source PDF
- [ ] Convert to WOFF2 (`fonttools` + `brotli`)
- [ ] Map FL dice/sword/shield glyphs to Unicode PUA codepoints
- [ ] Add `@font-face` for `fl-icons` in `typography.css`
- [ ] **Replace skull emoji (☠️) with font-based skull symbol (✦ or Unicode ⚰)** → currently using emoji-grey filter
- [ ] Pre-processor: convert emoji → `<span class="fl-icon">X</span>`
- [ ] Test all icon characters render at body text size

## Phase 10 — UI Polish and Theme Application ✅ (theme colors and fixes applied)

- [x] **Apply book theme colors to reader UI** → Added gold/brass accents to buttons, TOC, search highlights
- [x] **Remove duplicate header** → Removed PageHeader import/component, kept only PageHeaderBanner
- [x] **Implement decorative footer** with opening for page count (ornamental frame with centered number)
- [x] **Replace skull emoji (☠️) with font-based alternative (⚰ coffin symbol)**
- [ ] Responsive breakpoints:
  - [ ] ≥ 1400px: full two-page spread
  - [ ] 768–1399px: single page, full height
  - [ ] < 768px: scroll mode (no flip, linear chapter scroll)
- [ ] "Dark room" mode toggle: `rgba(0,0,0,0.6)` overlay + vignette + book glows
- [ ] Optional page-turn sound (Web Audio API, toggle in menu, off by default)
- [ ] Print CSS: disable flip, paginated print layout
- [ ] All images: `alt` text from manifest + chapter name
- [ ] ARIA `role="document"` on FlipBook, `aria-label` on page turns
- [ ] Lazy-load images beyond current spread ±2 pages
- [ ] Run Lighthouse audit: target ≥ 80 performance, ≥ 95 accessibility

## Phase 11 — QA and Definition of Done

- [x] All 11 chapters render without content gaps
- [x] Page turn physics acceptable on Chrome, Firefox, Safari
- [ ] Works on iPad-class device (1024px touch screen)
- [x] Full-text search returns correct results for 10+ test queries
- [ ] **BUG** TOC navigates to wrong pages
- [x] Zero console errors on production build
- [ ] Side-by-side comparison: 5 random pages vs PDF — ≥ 95% layout match
- [ ] `README.md` complete with local dev setup instructions

---

## Blocking Issues

1. **TOC Navigation Bug** (HIGH PRIORITY) → Clicking a TOC entry jumps to the wrong page (offset issue)
   - Suspected cause: Entry.page uses 1-based numbering, flip() expects 0-based indexing
   - Location: `src/components/TableOfContents/TableOfContents.tsx` line ~60
   - Testing needed: Click TOC entry, verify page navigation accuracy

---

## Completed Recently

✅ **Theme Colors Applied:**
- Added CSS variables: `--accent-gold` (#8b7355), `--accent-gold-light` (#a88966), `--accent-gold-dark` (#6b5745)
- Updated NavBar.module.css: button hover, search input, page counter with gold accents
- Updated TableOfContents.module.css: border, scrollbar, active states with gold accents
- Updated SearchPanel.module.css: border, match highlighting with gold accents

✅ **Duplicate Header Removed:**
- Removed PageHeader import and component from PageSpread.tsx
- Kept PageHeaderBanner for book-accurate layout
- Verified build passes

✅ **Skull Emoji Replaced:**
- Replaced ☠️/☠/💀 with ⚰ (coffin symbol) in smartContentFix.ts
- Uses text-based character rendering instead of emoji

✅ **Decorative Footer Implemented:**
- Added ornamental container with diamond symbols on sides
- Page number centered with circular frame and decorative rule above
- Updated PageFooter.tsx and PageFooter.module.css
