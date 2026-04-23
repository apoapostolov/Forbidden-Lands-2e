# Cleanup Issue Catalog

Eight recurring artifact classes found in RPG PDF extractions, with detection
grep commands, examples, and repair strategies.

## Audit Commands (Run First)

```bash
grep -n '###.*[A-Z] [a-z]' output.md          # spaced-character headings
grep -n ' S \| S$' output.md                   # missing possessives
grep -n '.\{500,\}' output.md                  # long lines (garbled tables)
grep -n '^- $' output.md; grep -B1 '^- '       # loose bullet lists
```

---

## Category 1: Spaced-Character Headings

PDF typesetting renders decorative headings with spaces between every letter:
`C H A P T E R  I  Y O U R  P L A Y E R`. Extraction preserves the spaces.

**Detection:** `###` lines where 20%+ of space-separated tokens are single letters.

**Fix approach:**

- Split on 2+ spaces to find word boundaries, collapse internal spaces:
  `YO U R` → `YOUR`
- Apply dictionary segmentation to the collapsed string
- Build a corrections dictionary for edge cases

**Examples:**

```
### He rba li st           → ### Herbalist
### Fa st Ac t ion s       → ### Fast Actions
### C H A P T E R  I       → ### Chapter I
```

**Corrections dictionary pattern:**

```python
HEADING_CORRECTIONS = {
    "Npcs And Abilities": "NPCs and Abilities",
    "Introduction To Rpgs": "Introduction to RPGs",
}
```

---

## Category 2: Missing Possessives and Apostrophes

PDF extraction drops possessive apostrophes, especially U+2019 typographic quotes.

**Pattern:** A heading containing `S` (space-S-space) or ` S` at end.

**Examples:**

```
### Man S Best Friend      → ### Man's Best Friend
### Carson S Folly         → ### Carson's Folly
```

**Critical:** Use U+2019 (`'`) not ASCII U+0027 (`'`) for consistency. Use
Python scripts for these replacements since the edit tool cannot match smart
quotes:

```python
content = content.replace(" S ", "\u2019s ")  # within heading context only
```

---

## Category 3: Broken / Truncated / Orphaned Headings

Column breaks split headings mid-word, creating fragments that appear as
separate headings.

**Truncated headings:**

```
### Erika Ga               → ### Erikaga
### Father Brayton Car Mody → ### Father Brayton Carmody
```

**Orphan heading fragments (column continuation):**

```
### Originals in           → (remove — not a real heading)
### ing, make a PRESENCE roll. → (remove — sentence fragment)
```

**Fix approach:** Cross-reference the PDF table of contents. For orphan
fragments, delete the line and collapse the blank lines around it.

---

## Category 4: Bold/Heading Confusion

Extraction sometimes merges bold inline markers with heading syntax.

**Examples:**

```
### Limited Effect** : You take 1 point of Vexes.
→ **Limited Effect** : You take 1 point of Vexes.

### Sneak Attacks Ambushes
→ ### Sneak Attacks & Ambushes
```

**Fix approach:** If `**` appears inside a `###` heading, convert it back to a
bold paragraph item.

---

## Category 5: Sidebar-Split Paragraphs and Orphaned Text

Two-column layouts interleave sidebar content with body text. Paragraphs break
mid-sentence; sidebar fragments appear orphaned between sections.

**Detection:** Text ending without terminal punctuation (`. ! ? : ;`), followed
by blank line, then lowercase continuation.

**Examples:**

```
selling your

wares to passers-by        → selling your wares to passers-by
```

**Fix approach:** Rejoin lines ending without punctuation when the continuation
is clearly the same sentence.

---

## Category 6: Running Headers Embedded in Content

Running headers appear on every page. The first occurrence is the real heading;
all others are artifacts — including occurrences embedded in paragraph text.

**Standalone variants:**

```
Appendix: your tale begins   (appeared 11+ times, between paragraphs)
```

**Embedded in prose:**

```
attribute point of Appendix: your tale begins your choice
→ attribute point of your choice
```

**Fix approach:** Build a list of known chapter/appendix titles. Search for
them both as standalone lines and as substrings in paragraph text. Use
case-insensitive matching.

---

## Category 7: Garbled Multi-Column Table Data

The hardest category. RPG books use 4-6 column layouts (roll, region,
attributes, abilities, narrative) that extract as merged run-together lines.

**Detection:** Lines > 500 characters containing multiple stat/ability patterns.

**Table-specific patterns (column bleed):**

_Multiple entries merged into one row:_

```
| 11 Calamity! 12 Broken Hearts - Someone you love... | - Roll D66 again... |
→ | 11 | Calamity! - Roll D66 again... |
→ | 12 | Broken Hearts - Someone you love deeply... |
```

_Data in header row (table continuation from new PDF page):_

```
| D66 Personal Fortunes 51 Love Blossoms - Someone... |     |
→ | D66 | Personal Fortunes |
→ | 51  | Love Blossoms - Someone has expressed... |
```

_Plain text that should be a table:_

```
2D6 Family Background 2 you. Everyone you loved is long lost...
→ | 2D6 | Family Background |
  | 2   | Everyone you loved is long lost... |
```

**Fix approach:**

1. Read the garbled text — the data is present, just in the wrong structure
2. Cross-reference the original PDF to determine intended column layout
3. Reconstruct using Python with exact string replacements
4. For Unicode-heavy content, use Python strings with `\u2019`, `\u2014`, etc.

---

## Category 8: Loose Bullet Lists

PDF extraction introduces blank lines between bullet items, creating "loose"
lists. Markdown renderers wrap each item in `<p>` tags.

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

**Scale:** 300+ loose list items are typical in an RPG corebook.

---

## Known Limitations

- Complex multi-span tables (merged cells, nested headers) need manual
  reconstruction
- Decorative single-word fonts may not be detected as headings
- Right-to-left, vertical, or rotated text is not handled
- OCR is not included — for scanned PDFs, run OCR first (e.g., pytesseract via md-anything)

---

## Chapter Split Script

After cleanup, split the single file into per-chapter files:

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

For non-`Chapter N` section books, use the heading-based split helper:

```bash
python3 scripts/split_markdown_sections.py path/to/file.clean.md output-dir --level 2
python3 scripts/split_markdown_sections.py path/to/file.clean.md output-dir --pattern '^## '
```
