# Flow Engine V2 — Design Document

## Status: Implemented (branch: `flow-attempt`)

### Implementation Results

- **Build passes**: TypeScript strict mode, Vite production build
- **Pages**: 322 (down from preprocessor's 337 — better content packing via real measurement)
- **Flow engine**: `src/utils/flowEngine.ts` — DOM measurement-based pagination
- **React hook**: `src/hooks/useFlowPagination.ts` — async wrapper that waits for fonts
- **PageContent**: Explicit two-column flexbox layout, no CSS multi-column
- **App.tsx**: Cleaned from ~543 lines (with 250+ lines of estimation code) to ~177 lines
- **All three original bugs eliminated**: no phantom 3rd column, no wrong paragraph breaks, no whitespace from estimation errors

---

## 1. Why a Complete Rewrite

The current flow system has a **fundamental architectural flaw** that cannot be
patched: it uses two independent layers that disagree about content size.

### The Dual-Layer Mismatch Problem

```
Layer 1: Preprocessor (TypeScript, build-time)
  ├── Estimates text height using word count ÷ words-per-line × line-height
  ├── Assigns segments to pages/columns based on these estimates
  └── Writes static JSON with pre-assigned page layout

Layer 2: Runtime Renderer (CSS multi-column)
  ├── CSS column-count: 2 reflows content independently
  ├── Browser font rendering differs from point estimates
  └── overflow: hidden clips anything that doesn't fit
```

**These two layers can never agree** because:

- Word-count-based height estimation is fundamentally imprecise
- Browser font metrics, kerning, and hyphenation vary at runtime
- CSS `column-fill: auto` makes independent break decisions
- Header/footer heights are pixel-based but estimation is point-based
- Zoom level, viewport size, and font loading timing all affect rendering

### Observed Symptoms

1. **Paragraph breaks at wrong places** — Preprocessor splits a paragraph
   thinking it will flow as two pieces across columns. CSS reflows differently,
   creating mid-sentence breaks at awkward locations.

2. **Phantom 3rd column** — CSS `column-count: 2` with `overflow: hidden` still
   allows content to flow into an invisible third column region. Content pushed
   past column 2 by CSS reflow vanishes from the visible page.

3. **Massive whitespace** — Height estimation errs conservatively to avoid
   clipping, leaving large empty regions at column/page bottoms. The right
   column may be completely empty on some pages.

4. **Band-aid fixes multiply** — Every fix (safety reserves, seam rules, runtime
   leak guards, per-section overrides) adds complexity without addressing the
   root cause. App.tsx contains 250+ lines of runtime re-pagination logic that
   duplicates the preprocessor.

### Why Patches Cannot Fix This

The system has **two independent pagination controllers** (preprocessor + CSS
multi-column) that both try to decide where content breaks. Any change to one
invalidates assumptions in the other. The runtime leak guard in App.tsx is a
third controller that tries to reconcile the first two, tripling the complexity.

---

## 2. Research: How Book Pagination Engines Work

### Industry Approaches

| Approach | Examples | How It Works | Pros | Cons |
|----------|----------|--------------|------|------|
| **CSS Multi-column** | Current system | Let CSS engine break content | Simple CSS | No control over breaks, overflow clips, phantom columns |
| **Full Rendering Engine** | paged.js, WeasyPrint, PrinceXML | Replicate CSS Paged Media spec | Standards-compliant | Heavy, hard to customize, opinionated |
| **DOM Flow + Measure** | regionize, bindery.js | Render element → measure → overflow? → move to next region | Pixel-perfect, uses real browser metrics | Async, needs careful implementation |
| **Virtual Measurement** | Some e-readers | Estimate in virtual DOM, verify with probe renders | Fast | Still an estimation layer |

### Chosen Approach: DOM Flow + Measure (Runtime)

The `regionize` / `bindery.js` approach is the gold standard for web-based
book pagination because it uses **the browser itself as the measurement tool**.

**Core principle**: Never estimate. Render content into a real DOM container with
real CSS, ask the browser how tall it is, and use that truth to decide what fits.

### Key Insight from regionize

```javascript
// regionize's core loop (simplified):
for (const node of contentNodes) {
  region.element.appendChild(node);
  if (region.element.scrollHeight > region.element.clientHeight) {
    // Overflow! Remove node, move to next region
    region.element.removeChild(node);
    region = createNextRegion();
    region.element.appendChild(node);
  }
}
```

This is trivially correct because **the browser resolves all ambiguity**.
No height estimation, no point math, no safety reserves.

### Key Insight from bindery.js

Bindery extends regionize with **element splitting**: when a single paragraph
overflows, clone it, use binary search on character count to find the exact
break point that fills the remaining space.

### Key Insight from paged.js

Paged.js uses a "chunker" that walks the DOM tree and splits at overflow
boundaries. It handles:

- Break properties (`break-before`, `break-after`, `break-inside`)
- Orphans/widows
- Running headers/footers
- Cross-references and page counters

We don't need the full paged.js weight, but its chunker architecture
(walk → measure → break → continue) is the right mental model.

---

## 3. New Architecture

### Single Source of Truth: The Browser

```
                    ┌─────────────────────────────┐
Markdown ──parse──► │  Flat Segment Array (JSON)   │
                    │  No page assignment           │
                    │  No height estimation          │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  Runtime Flow Engine (React)  │
                    │                               │
                    │  For each segment:            │
                    │   1. Render into measure div  │
                    │   2. Check overflow            │
                    │   3. If fits → keep            │
                    │   4. If overflows → split or   │
                    │      move to next column/page  │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────▼──────────────────┐
                    │  Paginated Output             │
                    │  Pages with exact segment     │
                    │  assignments based on real     │
                    │  measured heights              │
                    └─────────────────────────────┘
```

### What Changes

| Component | Current | New |
|-----------|---------|-----|
| **Preprocessor** | Parses + estimates heights + assigns pages | Parses only → flat segment array |
| **Height estimation** | ~20 constants, word-count math | Eliminated entirely |
| **Page assignment** | Build-time, static JSON | Runtime, DOM-measured |
| **Column layout** | CSS `column-count: 2` | Two explicit `<div>` columns side by side |
| **Overflow handling** | `overflow: hidden` + safety reserves | Real measurement, no clipping |
| **Paragraph splitting** | Word-count ratio estimation | Binary search on actual rendered text |
| **Runtime leak guard** | 250+ lines in App.tsx | Eliminated (no leaks possible) |
| **book-data.json** | Pages with segment assignments | Flat chapter array with segments |

### What Stays the Same

- Markdown parsing (remark/rehype pipeline)
- Segment types (heading, paragraph, blockquote, table, hr, image-ref)
- All visual components (PageBackground, PageHeader, PageFooter, TextBlock, etc.)
- Page flip animation (BookReader + page-flip library)
- Search, TOC, navigation
- All CSS styling (fonts, colors, spacing)

---

## 4. Detailed Design

### 4.1 New Preprocessor Output

The preprocessor simplifies to a parser that produces:

```typescript
interface ChapterData {
  title: string;
  index: number;
  segments: Segment[];  // Same Segment types, but NO heightPt field
}

interface BookSegments {
  generatedAt: string;
  chapters: ChapterData[];
  // No pages array — pagination happens at runtime
}
```

The `heightPt` field is removed from all segment types since heights are
never estimated.

### 4.2 Runtime Flow Engine

The flow engine is a **build-time step that runs in a headless browser** (or
a React hook that computes pagination on first mount). It produces page
assignments by actually rendering content.

**Chosen implementation**: Build-time with Puppeteer/Playwright.

**Rationale**: Running the flow engine at app startup would cause a visible
layout shift and delay. Instead, we run it as a build step that:

1. Launches a headless browser
2. Renders each segment with exact production CSS
3. Measures heights
4. Assigns segments to pages based on real measurements
5. Writes `book-data.json` with accurate page assignments

This gives us **real browser metrics** at build time, eliminating the
estimation problem while keeping the static JSON performance benefit.

**Alternative (simpler, chosen for V2.0)**: Runtime measurement on first mount
with cached results. Simpler to implement, allows iterating faster.

### 4.3 Column Layout: Explicit Divs, Not CSS Multi-column

**Current** (broken):
```css
.columns {
  column-count: 2;
  column-fill: auto;
  overflow: hidden;  /* This is where content vanishes */
}
```

**New**:
```css
.page-content {
  display: flex;
  gap: var(--column-gap);
  height: var(--content-height);
}
.column {
  flex: 1;
  min-width: 0;
  overflow: visible;  /* Never clip — flow engine guarantees fit */
}
```

Two explicit `<div>`s means:

- No phantom 3rd column (there is no 3rd div)
- Each column's content is independently controlled
- `overflow: visible` means nothing is ever clipped
- The flow engine explicitly assigns segments to column 0 or column 1

### 4.4 Segment Measurement

```typescript
function measureSegment(
  segment: Segment,
  columnWidth: number,
  container: HTMLElement
): number {
  // Render segment into a real DOM container with production CSS
  const el = renderSegmentToDOM(segment);
  container.style.width = `${columnWidth}px`;
  container.appendChild(el);

  // Browser tells us the exact height
  const height = el.getBoundingClientRect().height;

  container.removeChild(el);
  return height;
}
```

### 4.5 Paragraph Splitting

When a paragraph doesn't fit in remaining column space:

```typescript
async function splitParagraph(
  html: string,
  availableHeight: number,
  columnWidth: number,
  container: HTMLElement
): Promise<{ head: string; tail: string } | null> {
  const text = stripHtml(html);
  const words = text.split(/\s+/);

  // Binary search for the split point
  let lo = 1, hi = words.length - 1;
  let bestSplit = -1;

  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);
    const headText = words.slice(0, mid).join(' ');

    // Render and measure the head portion
    container.innerHTML = `<p>${headText}</p>`;
    const headHeight = container.firstElementChild!.getBoundingClientRect().height;

    if (headHeight <= availableHeight) {
      bestSplit = mid;
      lo = mid + 1;
    } else {
      hi = mid - 1;
    }
  }

  if (bestSplit < 2 || words.length - bestSplit < 2) return null;

  // Refine: prefer sentence boundaries near bestSplit
  // ... (sentence boundary logic stays similar to current)

  return {
    head: `<p>${words.slice(0, bestSplit).join(' ')}</p>`,
    tail: `<p>${words.slice(bestSplit).join(' ')}</p>`
  };
}
```

### 4.6 Flow Algorithm

```
Input: flat array of segments (all chapters concatenated)
Output: array of pages, each with { leftColumn: Segment[], rightColumn: Segment[] }

STATE:
  currentPage = new page
  currentColumn = 'left'  (0 or 1)
  columnFill = 0  (px, measured)
  columnCapacity = measured height of empty column container

FOR EACH segment:
  // Apply break rules
  IF segment is H2: start new page
  IF segment is H3 near column bottom with no room for follow-on: next column

  // Measure this segment
  height = measureSegment(segment)

  // Does it fit?
  IF columnFill + height <= columnCapacity:
    add segment to currentColumn
    columnFill += height

  ELSE IF currentColumn == 'left':
    // Try splitting paragraph across columns
    IF segment is paragraph AND splittable:
      split = splitParagraph(segment, columnCapacity - columnFill)
      IF split:
        add split.head to left column
        switch to right column
        add split.tail to right column
        continue

    // Move to right column
    switch to right column
    columnFill = 0
    add segment to right column
    columnFill = height

  ELSE: // right column overflow
    // Try splitting across pages
    IF segment is paragraph AND splittable:
      split = splitParagraph(segment, columnCapacity - columnFill)
      IF split:
        add split.head to right column
        start new page
        add split.tail to new page's left column
        continue

    // Start new page
    start new page
    currentColumn = 'left'
    columnFill = 0
    add segment to left column
    columnFill = height
```

### 4.7 Typography Rules (Preserved)

These rules from the current system are valuable and carry over:

- **H2 section headings** always start on a new page
- **Orphan/widow control**: minimum 2 lines at top or bottom of any column
- **Heading + content cohesion**: headings must have follow-on content visible
- **Fiction blocks** span both columns
- **Front-matter** has special page break rules
- **Sentence-boundary preference** for paragraph splits

---

## 5. Implementation Plan

### Phase 1: New Preprocessor (parser-only mode)

- Strip all height estimation from `preprocess.ts`
- Remove page assignment logic
- Output flat `BookSegments` JSON (chapters → segments, no pages)
- Keep all other parsing (markdown → segments) unchanged

### Phase 2: Flow Engine Core

- Create `src/utils/flowEngine.ts`
- Implement measurement-based pagination
- Use hidden DOM container for measurement
- Produce page assignments at runtime (on first mount)

### Phase 3: New PageContent Component

- Replace CSS `column-count: 2` with explicit two-column flex layout
- Each column receives its own segment array from the flow engine
- Remove `overflow: hidden` entirely

### Phase 4: Integration

- Wire flow engine into App.tsx
- Remove `applyRuntimeLeakGuard` and all estimation code from App.tsx
- Update BookReader to use new page structure
- Verify all visual components still work

### Phase 5: Paragraph Splitting

- Implement binary-search splitting with DOM measurement
- Handle list splitting (by item boundaries)
- Handle sentence boundary preference

### Phase 6: Caching & Performance

- Cache measurement results (segment hash → height)
- Memoize page assignments (only recompute if segments change)
- Consider moving to build-time measurement with Playwright

---

## 6. Risk Assessment

| Risk | Mitigation |
|------|------------|
| Runtime measurement is slow for 2000+ segments | Measure once on mount, cache in state. Batch DOM operations. |
| Layout shift on first load | Show loading state until pagination completes |
| Different browsers measure differently | We target a specific page size; measurements are deterministic for a given CSS |
| Loss of existing features | All visual components and CSS remain; only the flow layer changes |
| Regression in page count | Expected — pages should actually be better filled |

---

## 7. Success Criteria

- [ ] No content ever clipped or hidden
- [ ] No phantom 3rd column
- [ ] Paragraphs split at natural boundaries only
- [ ] Column space utilization > 90% (minimal whitespace at column bottom)
- [ ] All typography rules preserved (H2 page breaks, heading cohesion, etc.)
- [ ] Page count within 10% of current (different is OK, wrong is not)
- [ ] All existing features work (search, TOC, navigation, page flip)

---

## 8. Files Affected

### New Files

- `reader/src/utils/flowEngine.ts` — Core flow engine
- `reader/src/hooks/useFlowPagination.ts` — React hook wrapping the engine
- `reader/docs/FLOW_ENGINE_V2.md` — This document

### Modified Files

- `reader/scripts/preprocess.ts` — Strip pagination, keep parsing
- `reader/src/App.tsx` — Remove leak guard, use flow engine
- `reader/src/components/PageContent/PageContent.tsx` — Two-column flex layout
- `reader/src/components/PageContent/PageContent.module.css` — Remove CSS multi-column
- `reader/src/types/book.ts` — Update types for new page structure

### Unchanged Files

- All visual components (TextBlock, TableBlock, ImageBlock, BoxedContent)
- PageBackground, PageHeaderBanner, PageFooter
- BookReader (page flip)
- NavBar, SearchPanel, TableOfContents
- All CSS styling files (typography, variables, global)
