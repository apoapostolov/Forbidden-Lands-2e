# Forbidden Lands Reader — Architecture & Pagination Guide

## Overview

The Forbidden Lands Reader is a React-based digital book viewer that converts Markdown source files into a paginated, multi-column layout matching the original PDF design. It uses a **dual-layer estimation system**:

1. **Preprocessor Layer** (TypeScript): Parses Markdown chapters, estimates content heights in points (pt), and assigns segments to logical pages/columns
2. **Renderer Layer** (CSS multi-column): Uses CSS `column-count: 2` to reflow content at runtime, creating the actual visual layout

This dual-layer approach is powerful but can create **phantom space bugs** if estimations don't match runtime rendering. This document explains the system and common issues.

---

## Architecture Layers

### Layer 1: Preprocessor (`scripts/preprocess.ts`)

**Purpose**: Convert `.md` files → JSON paginated segments
**Input**: 11 markdown chapters in `/corebook/`
**Output**: `/src/data/book-data.json` (336 pages, ~2,000+ segments)

**Key Responsibilities**:

- Parse Markdown → segment objects (headings, paragraphs, lists, images)
- Estimate height of each segment in typographic points (pt)
- Assign segments to logical pages/columns based on height estimates
- Apply layout rules (e.g., "level 2 headings start on new pages")
- Handle complex segments (lists with per-item splitting, paragraph continuation)

**Flow**:

```
01-front-matter.md ─┐
02-your-adventurer  ├─► parse + estimate heights ─► assign to pages ─► book-data.json (337 pages)
...                 │
11-appendix.md  ────┘
```

### Layer 2: Runtime Renderer (`src/components/PageContent/`)

**Purpose**: Render segments as multi-column layout
**Technology**: CSS `column-count: 2`, `column-gap: 19px`, `column-fill: auto`

**Key Responsibilities**:

- Position absolute header banner (64px)
- Position absolute footer (decorative skull + page number overlay, ~95-120px)
- Render `.columns` container with `height: 648px` (available space for content)
- CSS multi-column layout reflows segments across 2 columns
- PageFlip animation for page transitions

**Flow**:

```
App state (currentPage index)
         ↓
   PageContent (reads segments from book-data.json[currentPage])
         ↓
   .columns (CSS multi-column reflow)
         ↓
   Visible: left column | right column
```

---

## Understanding the Original Phantom Space Bug

### The Discovery

During development, users reported that entire sections of text were "missing" between pages when reading:

- Specific pages were blank or had only partial content
- Expected text (e.g., "### ALTERNATIVE METHOD" heading + paragraphs) appeared nowhere in the final render
- Content existed in source files and in the JSON data but didn't display on screen

### Why This Bug Was Insidious

1. **The data was correct**: Running `book-data.json` queries showed segments properly assigned to pages
2. **The HTML was rendering**: DevTools showed content in DOM, positioned at correct coordinates
3. **No errors or warnings**: No console errors, no TypeScript issues, no network problems
4. **Time-dependent**: Only happened at specific page boundaries where content accumulated over columns
5. **Browser-specific**: Identical viewport could hide/reveal the bug depending on scaling and zoom

### The Debugging Journey

| Phase | Hypothesis                               | Investigation                                     | Result                         |
| ----- | ---------------------------------------- | ------------------------------------------------- | ------------------------------ |
| 1     | CSS clipping at column height boundaries | Checked `overflow` and `column-fill` reflow       | Partially correct              |
| 2     | Height estimation too aggressive         | Tuned COLUMN_HEIGHT_PT and safety reserves        | Helped, but not root cause     |
| 3     | Heading/paragraph spacing rules          | Relaxed `break-inside` constraints                | Helped, but symptoms persisted |
| 4     | **Dual-layer height mismatch** ✓         | Compared preprocessor estimates vs runtime layout | **ROOT CAUSE FOUND**           |

### Root Cause: Dual-Layer Height Mismatch

```
Preprocessor Layer (TypeScript):
──────────────────────────────
Assumption: Each column has 528pt clean space
  528pt = COLUMN_HEIGHT_PT (full available height)

Action: Assign segments based on pt estimates
  Segment 1: 100pt → Col 1 (total: 100pt)
  Segment 2:  250pt → Col 1 (total: 350pt)
  Segment 3: 200pt → Col 1 (total: 550pt > 528pt!)
              ↓ Overflow to Column 2
           → Col 2 (total: 22pt)

Result: "Segment 3 chunk at 22pt of Col 2" assigned
────────────────────────────────────────────

CSS Runtime Layer:
──────────────────────────────
Actual dimensions:
  Container: 648px height
  Header:    64px (positioned absolute, top)
  Footer:    95px (positioned absolute, bottom)
  Content:   648px - 64px - 95px = 489px

Content reflow:
  Segment 3 is assigned to Col 2 at 22pt offset
  At 11.6pt/line, that's ≈ 200px visual position
  PROBLEM: 200px + 200px segment crosses into footer
  Footer covers pixels 553-648 (648 - 95)
                ↓
  Result: Content at 520–553px is clipped by overflow:hidden
────────────────────────────────────────────

User Experience:
  ❌ "Segment 3" is completely invisible
  ❌ Users report "missing" content
  ❌ But DevTools show it's in DOM
  ❌ Content exists in book-data.json
```

### The Fix: Safety Reserve & Targeted Guards

Since the mismatch exists in the fundamental layer relationship, the mitigation is **conservative estimation + targeted seam fixes**:

1. **Global safety buffer** (`RENDER_SAFETY_PT = 8`):
   - Reduce effective column height from 528pt to 520pt
   - Create 8pt buffer to absorb header/footer variance
   - Trade-off: Page count increases by ~40 pages

2. **Heading space reservation** (for chapters 2+):
   - H3/H4 headings reserve 72–180pt for following paragraph
   - Prevents headings from landing in footer-overlap zone

3. **Targeted seam fixes** (for known problem areas):
   - Chapter 2 "ALTERNATIVE METHOD": Force to page start
   - Chapter 1 h3/h4 headings: No reservation (brief sections)

### Why We Can't Perfectly Solve This

The preprocessor can never have perfect information because:

- Paragraph heights vary based on browser font rendering and zoom
- Header/footer pixel dimensions don't directly map to points
- CSS `column-fill: auto` reflow is dynamic and interactive
- Multi-column layout breaks at unpredictable boundaries

**Design Decision**: Accept conservative estimation and add targeted rules for known problem seams.

---

## The Phantom Space Problem

### Root Cause

The preprocessor estimates available height per column as **528pt** (the `COLUMN_HEIGHT_PT` constant). However, at runtime:

- Header banner occupies ~48pt at the top of content flow
- Footer occupies ~67pt at the bottom (positioned absolute but affects text reflow calculations)
- **Actual available space**: ≈ 528 - 48 - 67 = **413pt** (not 528pt)

When the preprocessor assigns content to the last 70-80pt of a column, that content gets:

1. Allocated to the logical page/column in `book-data.json` ✓
2. Rendered by CSS multi-column layout ✓
3. **Clipped by `overflow: hidden` on the container** ✗ (disappears from view)

### Example Scenario

| Layer          | Event                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| Preprocessor   | Assigns "The standard method..." paragraph to page 9, column 2, starting at offset 520pt (total = 528pt available) |
| Runtime CSS    | Content reflows and would render at pixel position 520-550px                                                       |
| Runtime Footer | Footer positioned absolutely, covers pixel positions 495-612px                                                     |
| Result         | Text is hidden behind footer; appears "missing" to user                                                            |

---

## Pagination Constants & Estimation

### Core Constants (in `preprocess.ts`)

```typescript
// Layout dimensions
const COLUMN_HEIGHT_PT = 528; // estimated available space per column
const RENDER_SAFETY_PT = 8; // reserve to absorb header/footer variance
const PAGE_HEIGHT = 907; // pixels (from PDF)
const PAGE_MARGIN_V = 35; // pixels

// Typography
const LINE_HEIGHT_PT = 11.6; // 8pt body text × 1.45 line-height
const WORDS_PER_COL_LINE = 8; // fit estimate for column width
const PARA_MARGIN_PT = 6; // space after each paragraph

// List-specific
const LIST_WORDS_PER_COL_LINE = 7; // narrower due to indent/bullet
const LIST_ITEM_EXTRA_PT = 2.5; // li marker + spacing
const LIST_BLOCK_EXTRA_PT = 10; // ul/ol margin adjustment

// Safety thresholds
const MIN_SPLIT_LINES = 2; // minimum lines to show when splitting paragraphs
const MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT = 35; // ensure heading isn't orphaned
```

### Height Estimation Functions

**Paragraph/Text**:

```typescript
function textHeightPt(str: string, wordsPerLine = WORDS_PER_COL_LINE): number {
  const words = str.split(/\s+/).filter(Boolean).length;
  const lines = Math.max(1, Math.ceil(words / wordsPerLine));
  return lines * LINE_HEIGHT_PT + PARA_MARGIN_PT;
}
```

**Headings**:

```typescript
const headingHeights: Record<number, number> = {
  1: 38, // # (chapter title)
  2: 28, // ## (section)
  3: 22, // ### (subsection)
  4: 16, // #### (sub-subsection)
};
```

---

## Layout Rules & Break Behavior

### Automatic Page/Column Breaks

The `addSegment()` function applies rules for when to force breaks:

#### 1. Level 2 Headings (`##`)

```typescript
// Rule: every ## section heading starts on a new page
if (seg.type === "heading" && (seg as HeadingSegment).level === 2) {
  if (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0) {
    flush(); // end current page
    currentPage = newPage(pageNumber, chTitle, chIdx);
  }
}
```

**Rationale**: Major section breaks are visually important; starting on a fresh page provides clear visual hierarchy.

#### 2. Heading + Next Content Reservation

```typescript
// Calculate how much space the heading + its following content needs
const headingNextReservationPt =
  seg.type === "heading"
    ? nextSeg?.type === "paragraph"
      ? (seg as HeadingSegment).level >= 3
        ? Math.min((nextSeg as ParagraphSegment).heightPt + 18, 180) // ### and ####
        : Math.min((nextSeg as ParagraphSegment).heightPt, 72) // ##
      : MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT
    : 0;

const headingNeedsNextColumn =
  seg.type === "heading" &&
  colFill + seg.heightPt + headingNextReservationPt > effectiveColumnHeight;
```

**Rationale**: Prevents orphaned headings floating in the tail-space of a column. A heading should not be placed at bottom of column unless its first paragraph can follow immediately.

#### 3. Paragraph Continuation

When a paragraph doesn't fit in remaining column space:

**Left column (colNum === 0)**: Allow split across both columns on same page
**Right column (colNum === 1)**: Split across columns on next page

Constraints:

- Head portion must have ≥ 2 lines
- Tail portion must have ≥ 2 lines (left column) or ≥ 1 line (right column)
- Avoid splitting mid-sentence (look for sentence boundaries)

#### 4. List Item Splitting

Lists can be split by item count rather than character count:

```typescript
if (pSeg.isListSegment && pSeg.itemLiHtmls && pSeg.itemHeights) {
  // Count how many top-level items fit in remaining space
  let splitAt = 0
  let cumHeight = 0
  for (let k = 0; k < heights.length; k++) {
    if (colFill + cumHeight + heights[k] > effectiveColumnHeight) break
    cumHeight += heights[k]
    splitAt = k + 1
  }
  // Require ≥ 2 items in head, ≥ 1 in tail
  if (splitAt >= 2 && remaining >= 1) { ... }
}
```

**Rationale**: Keeps related list items together; splitting by item boundary is cleaner than splitting mid-item.

### Targeted Seam Fixes

Certain sections are prone to falling into phantom space at specific page boundaries. These get explicit guards:

#### Chapter 2: "ALTERNATIVE METHOD"

```typescript
if (
  chIdx === 1 && // Chapter 2
  seg.type === "heading" &&
  (seg as HeadingSegment).level === 3 &&
  (seg as HeadingSegment).text === "ALTERNATIVE METHOD" &&
  (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0)
) {
  flush();
  currentPage = newPage(pageNumber, chTitle, chIdx);
  colFill = 0;
  colNum = 0;
}
```

**Rationale**: This heading + its first paragraphs kept landing at the unstable 8→9 page boundary where the footer overlap caused clipping. Force it to start on a fresh page to guarantee visibility.

#### Front-Matter Layout Rules

```typescript
// Keep CREDITS on page 1; fiction content starts on page 2
if (
  chIdx === 0 &&
  (seg as ParagraphSegment).isFiction &&
  !pageAlreadyHasFiction
) {
  if (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0) {
    flush();
    currentPage = newPage(pageNumber, chTitle, chIdx);
  }
}

// Keep fiction on pages 1-2; "FORBIDDEN LANDS" h3 starts page 3
if (chIdx === 0 && seg.text === "FORBIDDEN LANDS" && isLevel3Heading) {
  if (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0) {
    flush();
    currentPage = newPage(pageNumber, chTitle, chIdx);
  }
}
```

---

## CSS Layer (`PageContent.module.css` & `TextBlock.module.css`)

### Multi-Column Container (`PageContent.module.css`)

```css
.columns {
  columns: 2;
  column-gap: 19px;
  column-fill: auto;
  height: 648px; /* Available space after header (64px) + footer (95px) */
  overflow: hidden; /* Clip anything that spills below */
  break-inside: auto; /* Allow multi-column reflow */
}

/* Allow natural column/page breaks for headings and blocks */
h3,
h4 {
  break-after: auto; /* Don't force heading + next para to stay together */
}
```

**Critical**: `overflow: hidden` prevents content outside the 648px boundary from rendering. This is where phantom space bugs manifest.

### Text Block (`TextBlock.module.css`)

```css
.block {
  break-inside: auto; /* Allow splitting across columns */
  page-break-inside: auto;
}

.block ul,
.block ol,
.block li {
  break-inside: auto;
  page-break-inside: auto;
}
```

**Purpose**: Relax CSS break constraints so long lists and paragraphs can flow naturally across column boundaries instead of being forced into overflow.

---

## Debugging & Troubleshooting

### When Content Appears "Missing"

1. **Check preprocessor data** (fastest):

   ```bash
   cd reader
   node -e "const d=require('./src/data/book-data.json');const t='search text';for(const p of d.pages){if(p.segments.some(s=>s.html.includes(t))){console.log(t,'=> page',p.pageNumber);break;}}"
   ```

   If text shows up in data, the issue is render-layer (CSS).
   If text doesn't show up, the issue is paginator-layer.

2. **Check paginator height estimates**:
   - Run: `npm run preprocess` with debug output
   - Look for segments with unexpectedly large `heightPt` values
   - Compare against actual text length and column width

3. **Check CSS multi-column height**:
   - Open browser DevTools
   - Inspect `.columns` element
   - Check: `computed height` vs `scrollHeight`
   - If `scrollHeight > height` and `overflow: hidden`, content is clipped

4. **Add temporary debug overlay**:
   ```typescript
   // In PageContent/index.tsx, add to render:
   <div style={{position: 'absolute', bottom: 10, left: 10, fontSize: '10px', color: 'red'}}>
     scrollH: {columnsRef.current?.scrollHeight} | clientH: {columnsRef.current?.clientHeight}
   </div>
   ```

### Common Symptoms & Fixes

| Symptom                             | Cause                                  | Fix                                                       |
| ----------------------------------- | -------------------------------------- | --------------------------------------------------------- |
| Content missing at page boundaries  | Phantom space (header/footer overlap)  | Increase `RENDER_SAFETY_PT` or add targeted seam rule     |
| Heading orphaned at bottom of page  | `headingNeedsNextColumn` not triggered | Reduce `headingNextReservationPt` threshold               |
| List split awkwardly mid-item       | List-splitting logic not working       | Check `itemLiHtmls` and `itemHeights` generation          |
| Page count inflated (>400 pages)    | Overly conservative safety reserves    | Decrease `RENDER_SAFETY_PT` or `headingNextReservationPt` |
| Heading + text separated across gap | Missing break rule for that section    | Add targeted named rule in `addSegment()`                 |

---

## Data Structure: `book-data.json`

### Top-Level Schema

```typescript
interface BookData {
  chapters: Chapter[];
  pages: Page[];
  toc: TocEntry[];
}

interface Chapter {
  index: number;
  title: string;
  startPage: number;
}

interface Page {
  pageNumber: number; // 1-based (visible page in reader, matches footer)
  chapterTitle: string;
  chapterIndex: number;
  segments: Segment[];
}

type Segment = HeadingSegment | ParagraphSegment | ImageSegment;

interface HeadingSegment {
  type: "heading";
  level: 1 | 2 | 3 | 4;
  text: string;
  heightPt: number;
  id?: string;
}

interface ParagraphSegment {
  type: "paragraph";
  html: string; // sanitized HTML
  heightPt: number;
  isChapterOpener?: boolean;
  isFiction?: boolean;
  isListSegment?: boolean; // true if sourced from markdown list
  itemLiHtmls?: string[]; // per-item HTML if list segment
  itemHeights?: number[]; // per-item height estimate
}

interface ImageSegment {
  type: "image";
  src: string;
  alt?: string;
  heightPt: number;
  width?: number;
  height?: number;
}
```

### Example Page Data

```json
{
  "pageNumber": 10,
  "chapterTitle": "Your Adventurer",
  "chapterIndex": 1,
  "segments": [
    {
      "type": "heading",
      "level": 3,
      "text": "ALTERNATIVE METHOD",
      "heightPt": 22,
      "id": "alternative-method"
    },
    {
      "type": "paragraph",
      "html": "<p>The standard method for creating a character...</p>",
      "heightPt": 58.6,
      "isChapterOpener": false,
      "isFiction": false
    },
    {
      "type": "paragraph",
      "html": "<p>Some of your ancestors came with the armies...</p>",
      "heightPt": 52.4,
      "isChapterOpener": false,
      "isFiction": false
    }
  ]
}
```

---

## Known Issues & Mitigations

### Issue 1: Header/Footer Variance (FIXED)

**Problem**: Header and footer dimensions vary slightly based on browser zoom and font rendering. Paginator's fixed 528pt estimate didn't account for this.

**Mitigation**: Added `RENDER_SAFETY_PT = 8` constant to reduce effective column height to 520pt, creating a buffer zone as insurance.

**Trade-off**: Page count increases slightly (≈ +40 pages due to conservative estimates), but correctness is guaranteed.

### Issue 2: Orphaned Headings (FIXED)

**Problem**: Headings could land at the bottom of columns without room for following text, violating readability.

**Mitigation**: `headingNeedsNextColumn` logic ensures a heading + its first paragraph(**reservation**) fit together in the next column.

**Code**:

```typescript
const headingNextReservationPt = /* calculated space for heading + first para */
const headingNeedsNextColumn = colFill + heading.height + reservation > columnHeight
```

### Issue 3: Specific Boundary Seams (FIXED)

**Problem**: Chapter 2's "ALTERNATIVE METHOD" section kept landing at the unstable 8→9 page boundary where footer overlap clips the first paragraph.

**Mitigation**: Added explicit named rule to force this section to always start on a fresh page.

**Code** (in `addSegment()`):

```typescript
if (chIdx === 1 && seg.text === 'ALTERNATIVE METHOD' && (page has content)) {
  flush()
  currentPage = newPage()
}
```

### Issue 4: Chapter 1 Layout Waste (FIXED)

**Problem**: In front-matter Chapter 1, level 3-4 headings like "DISCOVER ADVENTURE SITES" (h4) and "RAVENLAND - THE FORBIDDEN LAND" (h3) were being pushed to next pages even though space remained on the current page.

**Root Cause**: Heading reservation logic was designed for chapter content where large h3/h4 sections need full paragraph protection. In Chapter 1 (front-matter), these headings introduce brief subsections with natural visual breaks; the large 180pt reservation was unnecessary and wasted space.

**Mitigation**: Added chapter-aware logic to eliminate heading space reservations for h3/h4 in Chapter 1 only:

```typescript
const headingNextReservationPt =
  seg.type === "heading"
    ? nextSeg?.type === "paragraph"
      ? chIdx === 0 && (seg as HeadingSegment).level >= 3
        ? 0 // Chapter 1 h3/h4: no space reservation
        : (seg as HeadingSegment).level >= 3
          ? Math.min((nextSeg as ParagraphSegment).heightPt + 18, 180) // Chapter 2+
          : Math.min((nextSeg as ParagraphSegment).heightPt, 72)
      : MIN_PARAGRAPH_ROOM_AFTER_HEADING_PT
    : 0;
```

**Result**:

- "DISCOVER ADVENTURE SITES" now on page 3 (was page 4)
- "RAVENLAND - THE FORBIDDEN LAND" now on page 4 (was page 5)
- Overall page count: 336 pages (reduced by 1)

### Issue 5: Phantom Space at Page Boundaries (MONITORING)

**Status**: Mitigated by `RENDER_SAFETY_PT = 8` constant and Chapter 2 "ALTERNATIVE METHOD" targeted seam fix. Monitor for regressions if heading reservation logic is further adjusted.

---

## Running & Building

### Regenerate Paginated Data

```bash
cd reader
npm run preprocess
```

Output: `src/data/book-data.json` (337 pages, 11 chapters)

### Build for Production

```bash
npm run build
```

Output: `/dist/` (optimized JS + CSS bundle)

### Run Development Server

```bash
npm run dev
```

Server listens on `http://localhost:5173` (or next available port)

---

## Extending the System

### Adding a New Targeted Seam Fix

If a section keeps landing in phantom space:

1. Identify the chapter index (`chIdx`) and heading text
2. Add a rule in `addSegment()`:
   ```typescript
   if (
     chIdx === TARGET_CHAPTER &&
     seg.type === "heading" &&
     (seg as HeadingSegment).level === TARGET_LEVEL &&
     (seg as HeadingSegment).text === "EXACT TEXT" &&
     (currentPage.segments.length > 0 || colNum !== 0 || colFill > 0)
   ) {
     flush();
     currentPage = newPage(pageNumber, chTitle, chIdx);
     colFill = 0;
     colNum = 0;
   }
   ```
3. Regenerate: `npm run preprocess`
4. Verify: Check whether the section now starts on a fresh page
5. Document the fix in this file (add to "Known Issues" section)

### Tuning Height Estimation

To adjust pagination balance:

- **Increase page count**: Decrease `COLUMN_HEIGHT_PT` or increase `RENDER_SAFETY_PT`
- **Decrease page count**: Increase `COLUMN_HEIGHT_PT` or decrease `RENDER_SAFETY_PT` (⚠️ risk phantom space)
- **Adjust list spacing**: Tune `LIST_ITEM_EXTRA_PT` and `LIST_BLOCK_EXTRA_PT`
- **Change heading behavior**: Modify `headingNextReservationPt` calculation

Always regenerate and visual-verify after tuning:

```bash
npm run preprocess && npm run dev
```

---

## Version History & Notable Changes

### Current Version: Phantom Space Fix + Chapter 1 Layout Optimization

- Added `RENDER_SAFETY_PT = 8` safety reserve to absorb header/footer variance
- Implemented heading + next-content reservation logic for chapters 2+
- Disabled heading space reservation for Chapter 1 h3/h4 headings (brief sections don't need guards)
- Added targeted seam fix for Chapter 2 "ALTERNATIVE METHOD"
- Fixed URL hash indexing (0-based → 1-based for user-facing numbers)
- Relaxed CSS `break-inside` constraints to allow natural multi-column reflow
- Current page count: 336 pages

### Previous Issue: Aggressive Break Constraints

- CSS had global `break-inside: avoid-column` that forced long blocks together
- Result: blocks couldn't split naturally across columns; content was shunted to overflow
- Fix: Changed to `break-inside: auto` and removed over-constraining rules

---

## References & Contacts

- **Source**: `/reader/scripts/preprocess.ts` (main paginator logic)
- **Styles**: `/reader/src/components/PageContent/PageContent.module.css`
- **Build Output**: `/reader/src/data/book-data.json`

For questions or issues, refer to the troubleshooting section above or add a comment in the relevant code file.
