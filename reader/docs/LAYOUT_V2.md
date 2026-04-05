# Layout V2 — CSS Architecture

The reader reproduces the Forbidden Lands core book layout using a CSS system
derived from the original PDF metrics. This document describes the visual
layout pipeline: page geometry, column model, span-all zones, and per-element
styling.

For the flow/pagination engine that assigns segments to pages, see
[FLOW_ENGINE_V2.md](FLOW_ENGINE_V2.md).

---

## 1. Page Geometry

Source: `src/styles/variables.css`

The page dimensions match the printed PDF exactly:

```
481.89 × 680.32 pt  →  642 × 907 px  (at 96 dpi, 1 pt = 1.333 px)
```

| Property          | CSS Variable      | Value  |
| ----------------- | ----------------- | ------ |
| Page width        | `--page-width`    | 642 px |
| Page height       | `--page-height`   | 907 px |
| Horizontal margin | `--page-margin-h` | 76 px  |
| Vertical margin   | `--page-margin-v` | 35 px  |
| Column gap        | `--column-gap`    | 19 px  |

Content area = 642 − 2×76 = **490 px** wide.

---

## 2. Column Model

Source: `src/components/PageContent/PageContent.module.css`

### Explicit Two-Column Flex (not CSS multi-column)

The V2 layout uses two real `<div>` elements side by side, not
`column-count: 2`. The flow engine assigns segments to left/right columns
explicitly before rendering.

```
┌──────────────────────────────────────────────┐
│                 spanAllWrap                    │  ← H2 frame, fiction
├─────────────────────┬────────────────────────┤
│     .column (left)  │  gap  │ .column (right) │
│     235 px          │ 19 px │ 235 px          │
│                     │       │                 │
│                     │       │                 │
└─────────────────────┴───────┴─────────────────┘
```

Column width = floor((490 − 19) / 2) = **235 px**

### No Clipping

All containers use `overflow: visible`. The flow engine guarantees that
measured content fits within the column height. No content is ever clipped.

### Column Break Marker

The flow engine concatenates left + right segments with a special `__column_break__`
HR marker between them. `PageContent.tsx` splits on this marker:

```typescript
// splitByColumnBreak() extracts:
//   spanAll — H2, blockquote-after-H2, H1, fiction paragraphs
//   left    — segments before __column_break__
//   right   — segments after __column_break__
```

---

## 3. Span-All Zone

Some elements render full-width above the two-column layout:

| Element              | Trigger                                    | CSS Wrapper                                      |
| -------------------- | ------------------------------------------ | ------------------------------------------------ |
| H2 section headings  | `seg.type === 'heading' && level === 2`    | `.spanAllWrap` with `.sectionHeadingPage` parent |
| Blockquote after H2  | `seg.type === 'blockquote'` preceded by H2 | `.spanAllWrap` + `.fictionAfterH2Wrap`           |
| Front-matter fiction | `isFiction && chapterIndex === 0`          | `.frontMatterFictionWrap`                        |

The span-all zone sits above `.columns` in the flexbox stack:

```html
<main class="sectionHeadingPage">
  <div class="spanAllWrap">
    <div class="headingWrap spanAllWrap">  <!-- H2 -->
    <div class="segmentWrap fictionAfterH2Wrap spanAllWrap">  <!-- fiction -->
  </div>
  <div class="columns">
    <div class="column">…left…</div>
    <div class="column">…right…</div>
  </div>
</main>
```

The flow engine measures span-all content and deducts its height from the
available column height for that page.

---

## 4. Section Heading Pages

When a page starts with an H2, the header banner is hidden. This gives an
extra 80 px of vertical space (the sectionHeadingContentHeight: 771 px
vs normal 691 px).

### H2 Decorative Frame

`.spanAllWrap :global(h2.section-heading)::before` renders the chapter
header overlay image as a pseudo-element:

- Image: `/assets/decorations/chapter-header-overlay.png`
- Natural aspect ratio: 1009 / 387
- Width: 106% (110% on `.sectionHeadingPage`)
- Centered via `transform: translate(-50%, -50%)`
- `z-index: -1` (behind the text)

The flow engine reserves a minimum of 160 px for the frame height, since
the CSS module styles aren't visible in the measurement container.

### Bleed

`.sectionHeadingPage` extends the frame beyond the content margin:

```css
--section-frame-bleed: clamp(12px, 2vw, 20px);
width: calc(100% + (2 * var(--section-frame-bleed)));
margin-left: calc(-1 * var(--section-frame-bleed));
```

---

## 5. Typography Classes

Source: `src/styles/typography.css`

### Headings

| Level | Class              | Font             | Size          | Tracking | Transform |
| ----- | ------------------ | ---------------- | ------------- | -------- | --------- |
| H1    | `.chapter-title`   | `--font-chapter` | 31 px (23 pt) | 0.08em   | uppercase |
| H2    | `.section-heading` | `--font-chapter` | 21 px (16 pt) | 0.08em   | uppercase |
| H3    | `.subsection`      | `--font-heading` | 15 px (11 pt) | 0.04em   | uppercase |
| H4    | `.bold-label`      | `--font-label`   | 12 px (9 pt)  | 0.04em   | uppercase |

### Body

| Class            | Font                 | Size         | Line-height | Alignment |
| ---------------- | -------------------- | ------------ | ----------- | --------- |
| `.body-text`     | `--font-body`        | 11 px (8 pt) | 1.45        | justify   |
| `.flavour-text`  | `--font-body` italic | 11 px        | 1.65        | inherit   |
| `.fiction-intro` | `--font-body` italic | 16 px        | 1.72        | center    |

### Drop Cap

`.chapter-opener::first-letter` — 52 px (39.4 pt), floated left,
applied to the first paragraph after chapter fiction.

---

## 6. Special Page Types

### Front-Matter (chapter index 0)

- **Page 1 (Credits)**: `.frontMatterCreditsPage` — centered body text,
  explicit column break at "ILLUSTRATIONS & GRAPHICS" H3, spacer below H2
  frame (`.creditsColumnsOffset`)
- **Page 2 (Fiction)**: All consecutive `isFiction` paragraphs on one page,
  `.frontMatterFictionWrap` with 15 px / 1.66 line-height
- **Page 3+**: Normal two-column layout, triggered by "FORBIDDEN LANDS" H3

### Section Heading Pages

Any page that starts with an H2:

- Header banner hidden
- Column height increased to 771 px
- H2 frame + fiction deducted from available column space
- `.sectionHeadingPage` wrapper provides bleed

---

## 7. Segment Rendering

Source: `src/components/PageContent/PageContent.tsx`

Each segment is rendered by the `renderSegment()` function, which maps
segment types to React components:

| Segment Type | Component                           | Wrapper Classes                                                   |
| ------------ | ----------------------------------- | ----------------------------------------------------------------- |
| `heading`    | `<h1>`–`<h4>` with typography class | `.headingWrap`, optionally `.spanAllWrap`                         |
| `paragraph`  | `<TextBlock>`                       | `.segmentWrap`                                                    |
| `blockquote` | `<TextBlock variant="blockquote">`  | `.segmentWrap`, optionally `.spanAllWrap` + `.fictionAfterH2Wrap` |
| `table`      | `<TableBlock>`                      | `.segmentWrap`                                                    |
| `hr`         | `<hr class="gold-rule">`            | (no wrapper)                                                      |
| `image-ref`  | `<ImageBlock>`                      | `.segmentWrap`                                                    |

### Span-All Detection

A segment goes into the span-all zone if:

- It is an H2 heading (`level === 2`)
- It is a blockquote directly after an H2

### Chapter Opener Detection

The first paragraph after a blockquote-after-H2 gets `isChapterOpener = true`,
which triggers the drop-cap first-letter style.

---

## 8. CSS Modules

The layout uses CSS Modules for scoped class names. Global typography
classes (`.body-text`, `.section-heading`, etc.) are referenced via
`:global()` selectors inside scoped module selectors.

### Key Files

| File                     | Purpose                                             |
| ------------------------ | --------------------------------------------------- |
| `variables.css`          | Design tokens — page geometry, fonts, colors        |
| `typography.css`         | Global typography classes (body, headings, fiction) |
| `PageContent.module.css` | Layout: columns, span-all, section heading, credits |
| `global.css`             | Resets, font loading, html/body setup               |

---

## 9. Vertical Space Budget (Normal Page)

```
907 px  total page height
 35 px  top margin (--page-margin-v)
 80 px  header banner + margin (64 + 16)
691 px  content area (columns)
 66 px  footer + padding (62 + 4)
 35 px  bottom margin (--page-margin-v)
-------
907 px
```

### Section Heading Page

```
907 px  total page height
 35 px  top margin
  0 px  no header banner
771 px  raw content area
        minus H2 frame (~160 px)
        minus fiction (variable)
        = effective column height
 66 px  footer + padding
 35 px  bottom margin
-------
907 px
```
