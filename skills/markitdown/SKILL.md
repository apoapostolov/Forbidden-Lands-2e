# MarkItDown — PDF/Doc to Markdown Conversion

Convert PDFs, Word docs, Excel, PowerPoint, and more to Markdown with good structural fidelity.

## Quick Use

```bash
# Basic conversion
markitdown /path/to/document.pdf

# Output to file
markitdown /path/to/document.pdf output.md

# Pipe from stdin
cat document.pdf | markitdown

# Get help
markitdown --help
```

## Wrapper Location

`/home/apoapostolov/.openclaw/workspace/scripts/markitdown`

## Installation (if needed)

```bash
MARKITDOWN_DIR="/home/apoapostolov/git-ext/markitdown"
cd "$MARKITDOWN_DIR"
uv venv --python 3.12 .venv
uv pip install -e 'packages/markitdown[all]'
```

## What It Handles

| Format | Notes |
|--------|-------|
| PDF | Text extraction with table/column preservation |
| Word (.docx) | Preserves formatting |
| Excel (.xlsx) | Each sheet becomes a section |
| PowerPoint (.pptx) | Slide content extracted |
| Images | OCR via tesseract if `ocr` extra installed |
| HTML, CSV, JSON, XML | Direct conversion |
| EPUBs | Reflowable text |
| ZIP archives | Iterates over contents |
| YouTube URLs | Transcription |

## When to Use MarkItDown vs Other Tools

| Tool | Best for |
|------|----------|
| **markitdown** | Two-column layouts, weapon/stat tables, mixed-format docs |
| **pymupdf4llm** | Deep integration, custom extraction pipelines |
| **pdftotext** | Fast plain-text dump, no structure needed |
| **md-anything** | Scanned PDFs (OCR), mixed media docs |

Markitdown wins on table/column fidelity for RPG sourcebooks. For complex multi-pass cleanup workflows, see the Post-Extraction Cleanup section below.

---

# Post-Extraction Cleanup

Extraction produces ~80% clean output. The remaining 20% needs targeted fixes. This section is tool-agnostic — apply these patterns after any PDF-to-markdown conversion.

## Cleanup Issue Catalog

### Category 1: Spaced-Character Headings

PDF typesetting renders decorative headings with spaces between every letter: `C H A P T E R  I  Y O U R  P L A Y E R`. Extraction faithfully preserves the spaces.

**Detection:** `###` lines where 20%+ of space-separated tokens are single letters.

**Fix approach:**
- Split on 2+ spaces to find word boundaries, then collapse internal spaces: `YO U R` → `YOUR`
- Apply dictionary segmentation to the collapsed string
- Build a corrections dictionary for edge cases that algorithmic fixes cannot handle

**Examples:**
```
### He rba li st           → ### Herbalist
### Bron C Buster          → ### Bronc Buster
### Fa st Ac t ion s       → ### Fast Actions
### SAL AR IE S IN THE O LD WE ST → ### Salaries in the Old West
```

**Corrections dictionary pattern:**
```python
HEADING_CORRECTIONS = {
    "Npcs And Abilities": "NPCs and Abilities",
    "Introduction To Rpgs": "Introduction to RPGs",
    "LIF E IN TO WN": "Life in Town",
}
```

---

### Category 2: Missing Possessives and Apostrophes

PDF extraction drops or mangles possessive apostrophes, especially when the PDF uses typographic (smart) quotes U+2019.

**Pattern:** A heading containing ` S ` (space-S-space) or ` S` at end — the `S` is almost always a possessive `'s` extracted as a separate token.

**Examples:**
```
### Man S Best Friend      → ### Man's Best Friend
### Your Horse S Tackle    → ### Your Horse's Tackle
### Carson S Folly         → ### Carson's Folly
### Founder S Day          → ### Founder's Day
```

**Critical:** Use U+2019 (`'`) not ASCII U+0027 (`'`) — the edit tool cannot match smart quotes; use Python scripts via terminal for these replacements.

---

### Category 3: Broken / Truncated / Orphaned Headings

Column breaks split headings mid-word, creating fragments that appear as separate headings.

**Truncated headings (line break mid-name):**
```
### Erika Ga               → ### Erikaga
### Father Brayton Car Mody → ### Father Brayton Carmody
### Francisco Castellano S → ### Francisco Castellanos
```

**Orphan heading fragments (next-column continuation):**
```
### Originals in           → (remove — not a real heading)
### ing, make a PRESENCE roll. → (remove — sentence fragment)
### a little oasis amid... → (remove — prose fragment)
```

**Overgrown headings (two fragments merged from adjacent columns):**
```
### pire, the Middle East and North Africa The Ottoman Em
                           → (remove — garbled cross-column text)
```

**Fix approach:** Cross-reference the PDF table of contents or NPC/character index. For orphan fragments, delete the line and collapse blank lines.

---

### Category 4: Bold/Heading Confusion

Extraction sometimes merges bold inline markers with heading syntax.

**Examples:**
```
### Limited Effect** : You take 1 point of Vexes.
→ **Limited Effect** : You take 1 point of Vexes.

### Sneak Attacks Ambushes
→ ### Sneak Attacks & Ambushes
```

**Fix approach:** If `**` appears inside a `###` heading, it was likely a bold inline term, not a heading — convert back to `**bold**` paragraph text.

---

### Category 5: Sidebar-Split Paragraphs and Orphaned Text

Two-column layouts interleave sidebar content with body text. Paragraphs break mid-sentence; sidebar fragments appear orphaned between sections.

**Examples:**
```
selling your

wares to passers-by  → selling your wares to passers-by

you must roll your RESILIENCE L e t h a l po i so n
→ you must roll your RESILIENCE ability. To resist the poison...

V e da  m on r oe Obedience was once enslaved
→ Obedience was once enslaved
```

**Fix approach:** Search for:
- Text ending without terminal punctuation (`. ! ? : ;`), blank line, then lowercase continuation
- Garbled spaced text at the start of a paragraph (sidebar artifact)

---

### Category 6: Running Headers Embedded in Content

Running headers (e.g., `Chapter 7 - The West in the 1870s`) appear on every page. The first occurrence is the real heading; all others are artifacts.

**Standalone surviving variants:**
```
Appendix: your tale begins
```
(appeared 11+ times in one document, lowercase, between paragraphs)

**Embedded in paragraph text:**
```
attribute point of Appendix: your tale begins your choice
→ attribute point of your choice
```

**Production notes (layout artifacts):**
```
**Need a Chapter spread here??? Will blend into Chapter 10
otherwise...**
→ (remove entirely)
```

**Fix approach:** Build a list of known chapter headers and appendix titles. Search for them as standalone lines AND as substrings within paragraphs. Use case-insensitive matching.

---

### Category 7: Garbled Multi-Column Table Data

The hardest category. RPG books use lifepath/table layouts with 4-6 columns (roll number, region, attributes, abilities, narrative) that extract as single run-together lines of 500+ characters.

**Identifying garbled blocks:**
- Lines > 500 characters containing 3+ stat/ability patterns (e.g., `Grit \d`, `Docity \d`)
- Pipe tables where cells contain multiple logical entries

**Table-specific patterns (two-column PDF bleed):**

*Column-swapped descriptions:*
```
| 03 A Rival is Dead ger of blame... circumstances. The fin | - Someone you have crossed... |
→ | 03 | A Rival is Dead - Someone you have crossed... |
```

*Multiple entries merged into one row:*
```
| 11 Calamity! 12 Broken Hearts - Someone you love... | - Roll D66 again... |
→ | 11 | Calamity! - Roll D66 again, but the Tens die result is automatically 0. |
→ | 12 | Broken Hearts - Someone you love deeply loves you no more... |
```

*Data in header row (table continuation from new PDF page):*
```
| D66 Personal Fortunes 51 Love Blossoms - Someone has expressed... |     |
→ | D66 | Personal Fortunes |
→ | 51  | Love Blossoms - Someone has expressed their love for you... |
```

*Plain text that should be a table:*
```
2D6 Family Background 2 you. Everyone you loved is long lost...
3 Your family was big until the curse...
4 You have lived alone...
→ | 2D6 | Family Background | ... |
```

**Fix approach:**
1. Read the garbled text — it contains all the data, just in the wrong structure
2. Cross-reference the original PDF to determine intended column layout
3. Reconstruct using Python with exact string replacements
4. For Unicode-heavy content (smart quotes, em-dashes), use Python strings with `\u2019`, `\u2014`, etc.

---

### Category 8: Loose Bullet Lists

PDF extraction introduces blank lines between bullet items, creating "loose" lists. Markdown renderers wrap each item in `<p>` tags, adding excess vertical spacing.

**Detection:** `- ...` followed by blank line followed by `- ...`

**This is fully automatable:**
```python
lines = content.split('\n')
result = []
skip_blank = False
for line in lines:
    if line.strip() == '':
        skip_blank = False
        result.append(line)
    elif line.startswith('- ') and skip_blank:
        result.pop()  # remove previous blank line
        result.append(line)
        skip_blank = True
    elif line.startswith('- '):
        skip_blank = True
        result.append(line)
    else:
        skip_blank = False
        result.append(line)
content = '\n'.join(result)
```

**Scale:** 300+ loose list items across a typical RPG corebook.

---

## Cleanup Workflow

1. **Audit** — Search across all files for artifact patterns:
   ```
   grep -n '###.*[A-Z] [a-z]' output.md          # spaced headings
   grep -n ' S \| S$' output.md                   # missing possessives
   grep -n '.\{500,\}' output.md                  # long lines (garbled tables)
   grep -n '^- $' output.md; grep -B1 '^- '       # loose bullet lists
   ```

2. **Fix in order** — Structured fixes first (headings, page numbers, running headers), then paragraph/text fixes, then table reconstruction.

3. **Write targeted scripts** — For complex issues (lifepath tables, multi-row compression), write Python fix scripts. Keep them in `scripts/` for reference.

4. **Verify** — Spot-check 3-5 fixed sections against the original PDF.

---

## Splitting Into Chapter Files

After cleanup, split the single markdown file into per-chapter files:

```python
import re
from pathlib import Path

text = Path("rulebook.md").read_text(encoding="utf-8")
lines = text.split("\n")
chapters = []
for i, line in enumerate(lines):
    m = re.match(r"^## Chapter (\d+)\s*-\s*(.+)$", line)
    if m:
        chapters.append((i, int(m.group(1)), m.group(2).strip()))

for idx, (start, num, title) in enumerate(chapters):
    end = chapters[idx + 1][0] if idx + 1 < len(chapters) else len(lines)
    slug = re.sub(r"[^a-z0-9-]", "", title.lower().replace(" ", "-"))
    Path(f"corebook/{num:02d}-{slug}.md").write_text(
        "\n".join(lines[start:end]).rstrip() + "\n", encoding="utf-8"
    )
```

---

## Quality Checklist

After cleanup, verify:

- [ ] No page number artifacts remain (`–7–`, `– 88 –`, `# – 14 –`)
- [ ] No running headers remain (each chapter header appears once)
- [ ] No spaced-character headings remain
- [ ] No missing possessives (`S` as standalone token in headings)
- [ ] No broken or truncated headings remain
- [ ] No orphaned text fragments between sections
- [ ] No running headers embedded in paragraph text
- [ ] Tables are proper pipe tables with header and alignment rows
- [ ] No description text in numeric columns, no numeric data in description columns
- [ ] No mid-sentence paragraph breaks
- [ ] Bullet lists are compact (no blank lines between items)
- [ ] No `<br>` tags in body text
- [ ] No `**==> picture` placeholders or picture text markers remain
- [ ] Smart quotes (U+2019, U+201C, U+201D) are consistent throughout
- [ ] Spot-check 3-5 sections against the original PDF

---

## Known Limitations

- **Complex multi-span tables** (merged cells, nested headers) may need manual reconstruction
- **Decorative single-word fonts** may not be detected as headings
- **Right-to-left, vertical, or rotated text** is not handled
- **OCR not included** — for scanned PDFs, run OCR first (e.g., pytesseract via md-anything)
