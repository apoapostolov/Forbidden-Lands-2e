---
name: pdf-to-rpg-markdown
description: |
  Use when converting a tabletop RPG rulebook PDF into clean, structured
  markdown. Covers the full pipeline: column-aware extraction with
  pymupdf4llm, multi-pass cleanup (spaced headings, sidebars, tables,
  paragraph joining, attribution formatting), and final normalization.
  Handles two-column layouts, spaced-letter chapter titles, picture-text
  blocks, fiction blockquotes, and running headers. Output matches
  professional corebook markdown standards.
---

# PDF to RPG Markdown

This skill documents a proven pipeline for converting tabletop RPG
rulebook PDFs into clean, structured markdown suitable for version
control, AI-assisted editing, and web rendering.

## Why This Skill Exists

PDF-to-markdown conversion for RPG books is harder than it looks.
RPG rulebooks use two-column layouts, decorative headings with
spaced-out letters, sidebar callout boxes, inline tables rendered
as images, fiction epigraphs, and running chapter headers on every
page. Naive text extraction produces unusable output with
interleaved columns, merged words, and lost structure.

This skill records the extraction and cleanup pipeline that
produces corebook-quality markdown from these challenging PDFs.

## Tool Stack

### Extraction: pymupdf4llm

**Why not pdfplumber or marker?** pdfplumber extracts text
line-by-line and merges two-column content into single lines,
producing interleaved left/right column text that is nearly
impossible to fix algorithmically. pymupdf4llm is column-aware
and produces markdown with correct paragraph flow, italic
detection, bold detection, heading markup, and image placeholders.

**Installation:**

```bash
pip install pymupdf4llm wordninja
```

**Basic extraction:**

```python
import pymupdf4llm
from pathlib import Path

md = pymupdf4llm.to_markdown(str(Path("rulebook.pdf")))
Path("rulebook.pymupdf.md").write_text(md, encoding="utf-8")
```

pymupdf4llm produces markdown with:

- `##` headings from detected heading fonts
- `**bold**` from bold spans
- `_italic_` from italic spans
- `|...|` pipe tables from detected table structures
- `**==> picture [...] <==**` placeholders for images
- `**----- Start/End of picture text -----**` for text inside images
- Page content in reading order (column-aware)

### Cleanup: wordninja

wordninja provides dictionary-based word segmentation for
reconstructing spaced-out heading text (e.g., `T H E  W I L D  W E S T`
→ `The Wild West`). Without it, naive space-removal produces
concatenated gibberish (`THEWILDWEST`).

## Cleanup Pipeline

The cleanup runs as a sequence of independent passes, each
addressing one class of PDF extraction artifact. Order matters:
earlier passes normalize structure that later passes depend on.

### Pass 1: Front Matter and Noise Removal

Remove non-content elements that pymupdf4llm extracts faithfully
but that do not belong in the manuscript:

- **Page numbers**: patterns like `–7–`, `– 88 –`, `# – 14 –`
- **Copyright lines**: `© 2024...`, `PDF distributed exclusively...`
- **Table of contents**: pipe-table rows with dot leaders (`......`)
  and `<br>` continuation lines

### Pass 2: Running Headers

RPG PDFs repeat `Chapter N - Title` on every page as a running
header. The cleanup must:

1. Convert the **first occurrence** of each chapter header into a
   `## Chapter N - Title` heading
2. Remove all subsequent occurrences (they are running headers)

Use a dictionary to track seen chapter keys (normalized to
lowercase with collapsed whitespace).

### Pass 3: Spaced Heading Reconstruction

PDF typesetting often renders decorative headings with spaces
between every letter: `C H A P T E R  I I  Y O U R  P L A Y E R`.
pymupdf4llm faithfully preserves these spaces.

**Detection:** A heading line is "spaced" if more than 20% of its
space-separated tokens are single alphabetic characters.

**Reconstruction algorithm:**

1. Split on 2+ spaces to find definite word boundaries
2. For each group, collapse internal spaces: `YO U R` → `YOUR`
3. If the collapsed string is longer than 3 characters, run
   `wordninja.split()` to segment it: `YOUR` → `['YOUR']`,
   `PLAYERCHAACTER` → `['PLAYER', 'CHARACTER']`
4. Apply smart title case (preserving acronyms like RPG, NPC, GM
   and lowercasing articles/prepositions)
5. Check against a corrections dictionary for known edge cases

**Guard against false positives:** Text containing sentence
punctuation (`.?!,;`) is never a spaced heading — it is a quote
or attribution that happens to have short words.

### Pass 4: Picture Block Conversion

pymupdf4llm marks image regions with:

- `**==> picture [W x H] intentionally omitted <==**` — remove these
- `**----- Start/End of picture text -----**<br>` — extract the
  text between these markers

For picture text blocks:

1. Split on `<br>` tags
2. Strip bold markers
3. If the content looks like tabular data (header words like
   Action, Range, Damage, Result, etc.), convert to a pipe table
4. Otherwise, emit as plain text
5. Short blocks (≤2 lines, all under 40 chars) are likely captions
   — remove them

### Pass 5: Heading Hierarchy Normalization

pymupdf4llm detects headings by font size but does not know the
document's intended hierarchy. Fix this:

- `## Chapter N - Title` → keep as `##` (apply title case to
  the title portion)
- `## **bold text**` → `### bold text` (section heading)
- `## non-chapter text` → `### text` (subsection)
- `## "quote text"` or `## **"quote"**` → `> *"quote"*`
  (chapter epigraph, not a heading)
- `## Chapter [Roman word]...` → remove (duplicate from spaced
  heading reconstruction)

**Attributions:** Bold all-caps standalone lines (e.g.,
`**THOMAS HORN JR., EXECUTED ON...**`) become
`> — THOMAS HORN JR., EXECUTED ON...`

Short `###` headings that follow a blockquote and contain a
name (e.g., `### F Scott Fitzgerald`) are also attributions:
`> — F. SCOTT FITZGERALD`

### Pass 6: Sidebar Conversion

Italic paragraphs (`_italic text longer than 20 chars_`) become
blockquotes: `> _italic text_`. These represent PDF sidebar
callout boxes that pymupdf4llm detected as italic spans.

### Pass 7: Paragraph Joining

PDF column breaks cause paragraphs to split mid-sentence across
lines or even across blank lines. The joiner must:

1. Skip structural lines (headings, blockquotes, tables, lists,
   code fences)
2. For text lines, accumulate content until the line ends with
   sentence-terminal punctuation (`. ! ? : ; " ' )`)
3. Join across a **single blank line** if the current line does
   not end a sentence and the line after the blank is also text
4. Join when the next line starts with a lowercase letter
   (continuation of a sentence)

### Pass 8: Inline Table Cleanup

Replace `<br>` tags inside pipe table cells with spaces.

### Pass 9: Whitespace Normalization

- Strip trailing whitespace from all lines
- Collapse 3+ consecutive blank lines to 2
- Ensure a blank line before and after every heading
- Trim leading/trailing blank lines from the document

## Output Quality Checklist

After running the pipeline, verify:

- [ ] No page number artifacts remain
- [ ] No running headers remain (each chapter header appears once)
- [ ] Spaced headings are properly reconstructed (spot-check 3-5)
- [ ] Chapter hierarchy: `#` book title → `##` chapters → `###` sections
- [ ] Fiction epigraphs are blockquote italic: `> *"quote"*`
- [ ] Attributions are blockquote em-dash: `> — NAME`
- [ ] Sidebar text is in blockquotes
- [ ] Tables are proper pipe tables with header and alignment rows
- [ ] Paragraphs flow naturally with no mid-sentence breaks
- [ ] No `<br>` tags remain in body text
- [ ] No `**==> picture` placeholders remain
- [ ] No `**----- Start/End of picture text -----**` markers remain

## Splitting Into Chapter Files

After cleanup, split the single markdown file into per-chapter files:

1. Find all `## Chapter N - Title` headings
2. Extract content from each heading to the next (or end of file)
3. Write as `NN-kebab-case-title.md` (e.g., `01-welcome-to-the-old-west.md`)

```python
import re
from pathlib import Path

text = Path("rulebook.final.md").read_text(encoding="utf-8")
lines = text.split("\n")
chapters = []
for i, line in enumerate(lines):
    m = re.match(r"^## Chapter (\d+)\s*-\s*(.+)$", line)
    if m:
        chapters.append((i, int(m.group(1)), m.group(2).strip()))

for idx, (start, num, title) in enumerate(chapters):
    end = chapters[idx + 1][0] if idx + 1 < len(chapters) else len(lines)
    slug = title.lower().replace(" ", "-").replace("&", "and")
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    filename = f"{num:02d}-{slug}.md"
    Path(f"corebook/{filename}").write_text(
        "\n".join(lines[start:end]).rstrip() + "\n",
        encoding="utf-8"
    )
```

## Known Limitations

- **Complex multi-span tables** (merged cells, nested headers)
  often extract as run-together text. Manual table reconstruction
  may be needed for the most complex tables.
- **Decorative fonts** used for single words or short phrases may
  not be detected as headings by pymupdf4llm.
- **Right-to-left text, vertical text, and rotated elements** are
  not handled.
- **OCR is not included.** If the PDF contains scanned images
  rather than selectable text, use a separate OCR tool first
  (e.g., pytesseract via the md-anything approach).

## Corrections Dictionary

Maintain a game-specific corrections dictionary for heading
reconstruction edge cases that wordninja cannot handle:

```python
HEADING_CORRECTIONS = {
    "Npcs And Abilities": "NPCs and Abilities",
    "Introduction To Rpgs": "Introduction to RPGs",
    "Don'T Roll Too Often": "Don't Roll Too Often",
    "Non Player Characters": "Non-Player Characters",
}
```

Add entries as they surface during quality review. This is cheaper
and more reliable than trying to make the algorithm perfect.
