# TOC Navigation Fix Guide

**Status:** Investigation Complete — Ready for implementation  
**Priority:** HIGH (blocks proper chapter navigation)  
**Estimated Effort:** 30–45 minutes

---

## Problem Statement

Clicking TOC entries navigates to *nearly* correct pages but with an offset. The chapter content appears correctly, but the page counter doesn't match the TOC page reference.

**Examples:**
- TOC: "1. Introduction" → page 8 (1-based PDF numbering)
- Navigation: `entry.page - 1 = 7` (array index)
- Result: Lands on correct chapter, but display number doesn't align with TOC expectation

---

## Root Cause

The `src/data/toc.json` file uses PDF page numbering (which includes cover pages, blank pages, etc.), but the reader's `book-data.json` array is paginated differently during preprocessing.

**Evidence:**
1. TOC entry "2. Your Adventurer" → page 18 (PDF)
2. Array index = 18 - 1 = 17
3. Actual display page for this content = ~5 (display index)
4. **Offset: ~12 pages**

**Why:**
- PDF has front matter, cover, blank pages in the first ~10–15 pages
- Preprocessing script excludes/reorders content
- TOC references PDF page numbers, not array indices
- Simple subtraction of 1 doesn't account for this offset

---

## Solution Options

### Option A: Build a Page Mapping (Recommended)

**Approach:**
1. Generate a map in the preprocess script that maps PDF page numbers → array indices
2. Store this map in `book-data.json`
3. Update `TableOfContents.tsx` to use the map when navigating

**Steps:**

**File: `scripts/preprocess.ts`**
- After paginating all content, build a `pageNumberToIndex` map:
  ```typescript
  const pageMapping: Record<number, number> = {} // PDF page -> array index
  bookData.pages.forEach((page, index) => {
    pageMapping[page.pageNumber] = index
  })
  ```
- Add to `book-data.json` output:
  ```typescript
  bookData.pageMapping = pageMapping
  ```

**File: `src/app-types/book.ts`**
- Update `BookData` interface:
  ```typescript
  interface BookData {
    pages: PageData[]
    toc: TocEntry[]
    totalPages: number
    pageMapping: Record<number, number> // NEW
  }
  ```

**File: `src/components/TableOfContents/TableOfContents.tsx`**
- Update navigation handler:
  ```typescript
  onNavigate(bookData.pageMapping[entry.page] ?? entry.page - 1)
  ```

**Pros:**
- Accurate for all pages
- Maintainable (mapping is source of truth)
- Survives preprocessor changes

**Cons:**
- Requires changes to multiple files
- Adds ~1KB to JSON payload

---

### Option B: Regenerate toc.json with Array Indices (Simpler)

**Approach:**
1. Update preprocess script to also output corrected TOC with array indices
2. Replace current `toc.json` with corrected version
3. Keep navigation as-is (simple `entry.page - 1`)

**Steps:**

**File: `scripts/preprocess.ts`**
- After building TOC matches, rewrite page numbers:
  ```typescript
  const correctedToc = toc.map(entry => ({
    ...entry,
    page: findPageIndexForContent(entry.title, pages)
  }))
  writeFileSync(TOC_FILE, JSON.stringify(correctedToc, null, 2))
  ```

**Pros:**
- Simplest change (one file, one loop)
- No changes needed to TableOfContents.tsx
- Smaller JSON payload

**Cons:**
- Trickier to match TOC entries to preprocessed pages
- May require fuzzy title matching

---

## Recommended Implementation: Option A

**Why:** Explicit mapping is more reliable than title-based matching, and the code is clearer.

---

## Implementation Checklist

- [ ] Update `scripts/preprocess.ts` to generate page mapping
- [ ] Update `src/app-types/book.ts` BookData interface
- [ ] Update `book-data.json` generation to include mapping
- [ ] Update `src/components/TableOfContents/TableOfContents.tsx` navigation
- [ ] Test: Click "1. Introduction" (should land on actual page 8 equivalent)
- [ ] Test: Click "2. Your Adventurer" (should land on actual page 18 equivalent)
- [ ] Verify page counter matches expectations
- [ ] Rebuild and commit

---

## Testing Strategy

1. **Manual Testing:**
   - Click first TOC entry (Map: The Forbidden Lands) → verify page counter
   - Click middle entry (around chapter 5) → verify alignment
   - Click last entry (Appendix) → verify it works

2. **Automated Check (Optional):**
   - Add test in preprocess script that verifies no page number appears twice
   - Add test that checks TOC entries are in ascending page order

---

## Quick Debug Commands

```bash
# Rebuild preprocessed data
npm run preprocess

# Check page mapping in book-data.json
jq '.pageMapping | keys | sort | .[0:10]' src/data/book-data.json

# Grep for specific page in mapping
jq '.pageMapping | to_entries[] | select(.value == 42)' src/data/book-data.json
```

---

## Files to Modify

- `scripts/preprocess.ts` — generate mapping
- `src/app-types/book.ts` — add pageMapping type
- `src/components/TableOfContents/TableOfContents.tsx` — use mapping
- `src/data/book-data.json` — auto-generated, will include mapping

---

## Expected Outcome

After implementation:
- Clicking any TOC entry navigates to the exact page shown in the TOC
- Page counter displays match TOC page references
- Navigation works across all 11 chapters
- No more "off by" errors

