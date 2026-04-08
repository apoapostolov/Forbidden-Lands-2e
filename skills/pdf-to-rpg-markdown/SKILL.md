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

## Manual AI Polish (Phase 3)

The automated pipeline (Passes 1-9) handles roughly 80% of
extraction artifacts. The remaining 20% require contextual AI
judgment — they are ambiguous, context-dependent, or involve
data mangled beyond what deterministic regex can reconstruct.

This phase is performed chapter-by-chapter after splitting.
Fix scripts live in `scripts/` and operate on files in
`corebook/`. The reference scripts for this project are:

- `fix_all_headings.py` — 108 heading fixes across all chapters
- `fix_remaining.py` — structural fixes across ch03–ch10
- `fix_ch10_v5.py` — garbled lifepath table parser
- `fix_loose_lists.py` — bullet list compaction (automatable)

### Issue Catalog

Below is the complete catalog of issues encountered and fixed
during manual polish, with enough detail for a future AI to
identify and apply the same fixes on another document.

---

### Category 1: Spaced-Character Headings (Automated + Manual)

The automatic pass (Pass 3) handles most spaced headings, but
some headings use partial spacing, mixed capitalization, or
embedded punctuation that the automated detector misses.

**Detection:** `###` lines that contain 2+ single-character
tokens with spaces between them, but that also have normal
words mixed in.

**Examples fixed (exact replacements):**

```text
### He rba li st           → ### Herbalist
### Bron C Buster          → ### Bronc Buster
### L ucky                 → ### Lucky
### P is to Leer           → ### Pistoleer
### Rabble Ro User         → ### Rabble Rouser
### Hay Maker              → ### Haymaker
### Light Footed           → ### Light-Footed
### Lock Picker            → ### Lockpicker
### L aw                   → ### Law
```

**Examples fixed (regex, for inconsistent spacing):**

```text
### Fa st Ac t ion s       → ### Fast Actions
### c on fl ic t mod ific at ion s → ### Conflict Modifications
### O ve rw at ch          → ### Overwatch
### He at st ro ke         → ### Heatstroke
### Fi re                  → ### Fire
### LIF E IN TO WN         → ### Life in Town
### SAL AR IE S IN THE O LD WE ST → ### Salaries in the Old West
```

**Fix approach:** Write exact replacements for headings that can
be identified uniquely. Use regex with `\s*` between known
character groups for headings with inconsistent spacing. The
regex patterns match `re.IGNORECASE` and anchor at `^###`.

**AI judgment required:** Determining the intended heading text
when the spaced characters form ambiguous words (e.g., is
`Ro User` → `Rouser` or `Ro-User`?). Cross-reference the PDF
table of contents or page headers.

---

### Category 2: Missing Possessives and Apostrophes

PDF extraction frequently drops or mangles possessive
apostrophes, especially when the PDF uses typographic (smart)
quotes (U+2019).

**Examples fixed:**

```text
### Man S Best Friend      → ### Man's Best Friend
### Your Horse S Tackle    → ### Your Horse's Tackle
### Bron C Bustin          → ### Bronc Bustin'
### Adventure 1 - Founder S Day → ### Adventure 1 - Founder's Day
### Carson S Folly         → ### Carson's Folly
### King S People in...    → ### King's People in...
### Rockcliffe S Lie       → ### Rockcliffe's Lie
```

**Pattern:** When a heading contains ` S ` (space-S-space) or
` S` at end, the `S` is almost always a possessive `'s` that
was extracted as a separate token.

**Critical encoding detail:** The output must use U+2019 (RIGHT
SINGLE QUOTATION MARK `'`) not ASCII U+0027 (`'`) to match the
rest of the document. The VS Code `replace_string_in_file` tool
cannot match U+2019 — use Python scripts via the terminal.

---

### Category 3: Broken / Truncated / Orphaned Headings

PDF column breaks split headings mid-word, creating fragments
that appear as separate `###` lines.

**Truncated headings (line break mid-name):**

```text
### Erika Ga               → ### Erikaga
### Father Brayton Car Mody → ### Father Brayton Carmody
### Francisco Castellano S → ### Francisco Castellanos
### Don a Lmc Ginn         → ### Dona McGinn
### Marion Freeman and Jimmy H Arles Den
                           → ### Marion Freeman and Jimmy Harlesden
```

**Orphan heading fragments (stubs from next-column continuation):**

```text
### Originals in           → (removed, not a real heading)
### ing, make a PRESENCE roll. → (removed, sentence fragment)
### a little oasis amid... → (removed, prose fragment)
### What is your           → (removed, merge with next heading)
```

**Overgrown headings (two fragments merged from adjacent columns):**

```text
### pire, the Middle East and North Africa The Ottoman Em
                           → (removed, garbled cross-column text)
```

**Fix approach:** Cross-reference the PDF to determine the
intended heading. For truncated names, check the character
index or NPC roster. For orphan fragments, simply delete the
line and collapse blank lines.

---

### Category 4: Bold/Heading Confusion

pymupdf4llm sometimes merges bold markers with heading syntax.

**Examples:**

```text
### Limited Effect** : You take 1 point of Vexes.
→ **Limited Effect** : You take 1 point of Vexes.

### Sneak Attacks Ambushes
→ ### Sneak Attacks & Ambushes
```

**Fix approach:** If the line has `**` inside a `###` heading,
it was likely a bold inline term, not a heading. Convert back
to `**bold**` paragraph text.

---

### Category 5: Sidebar-Split Paragraphs and Orphaned Text

Two-column layouts interleave sidebar content with body text.
The result is a paragraph that starts, breaks off where the
sidebar intruded, then resumes — often with the sidebar content
appearing as an orphaned block between the two halves.

**Example (ch05 — poison description split across Falling):**

The text about poison resistance (`ability. To resist the
poison you need to get as many successes as the Potency
rating...`) appeared orphaned between the "Falling" and
"Falling from your Horse" sections. The fix:

1. Removed the orphaned paragraph from its wrong location
2. Rejoined it to the RESILIENCE ability text where it
   belonged (the text `you must roll your RESILIENCE` was
   followed by garbled heading text instead of its proper
   continuation)

**Example (ch05 — Lethal Poison heading extracted as garbled
inline text):**

```text
you must roll your RESILIENCE L e t h a l po i so n
→ you must roll your RESILIENCE ability. To resist the
  poison... [full paragraph] ...limited effect of the poison.

### Lethal Poison
```

**Example (ch06 — paragraph split at column break):**

```text
selling your

wares to passers-by  → selling your wares to passers-by
```

**Example (ch09 — sidebar name artifact in paragraph):**

```text
V e da  m on r oe Obedience was once enslaved
→ Obedience was once enslaved
```

**Fix approach:** Search for mid-sentence line breaks (text
ending without terminal punctuation, blank line, then lowercase
continuation). Also search for garbled spaced text appearing at
the start of a paragraph — these are sidebar artifacts that
leaked into the wrong column.

---

### Category 6: Running Headers Embedded in Content

Pass 2 removes standalone running headers, but some survive
because they are embedded inside paragraph text or appear as
non-obvious variants.

**Standalone variants (ch10 — 11+ instances):**

```text
Appendix: your tale begins
```

These appeared on lines by themselves between paragraphs,
lowercase (not matching the actual heading).

**Embedded in paragraph text:**

```text
attribute point of Appendix: your tale begins your choice
→ attribute point of your choice
```

**Production notes (layout artifacts never meant for print):**

```text
**Need a Chapter spread here??? Will blend into Chapter 10
otherwise...**
→ (removed entirely)
```

**Fix approach:** Build a list of known chapter headers and
appendix titles. Search for them as standalone lines and as
substrings within paragraphs. Use case-insensitive matching
since running headers may differ in case from the actual
heading.

---

### Category 7: Garbled Multi-Column Lifepath/Table Data

The hardest category. RPG books present lifepath tables with
4-6 columns (roll number, region, attributes, abilities,
narrative) in decorative layouts. pymupdf4llm extracts these as
single run-together text lines of 500+ characters interleaving
all columns.

**Identifying garbled blocks:** Lines with 3+ occurrences of
`Grit \d`, 3+ of `Docity \d`, and length > 500 characters.

**Parsing algorithm (Docity boundary method):**

1. Identify the last attribute in the game's stat block
   (DOCITY in this game) as the entry terminal marker
2. Find all `Docity \d` occurrences in the garbled line
3. After each Docity match, consume any trailing ability
   tokens (`ABILITY_NAME \d`) to find the true entry boundary
4. Split the line into entry chunks at these boundaries
5. For each chunk, extract:
   - **Roll number**: first standalone digit
   - **Attributes**: named patterns like `Grit 2`, `Quick 1`
   - **Abilities**: known ability names + digit
     (e.g., `FIGHTIN' 2`, `SHOOTIN' 1`)
   - **Region name**: match against a known region list and
     strip from narrative (use `\bEurope\b(?!an)` to avoid
     stripping "European" from narrative text)
   - **Narrative**: everything remaining after stripping
     stats, abilities, and region names
6. Format each entry as a numbered bold paragraph with
   attribute and ability lines

**Result:** 6 garbled blocks → 54 clean structured entries
(9 entries each for 9-roll blocks, 6 for 6-roll blocks).

**Smart quote gotcha:** Ability names like FIGHTIN', SHOOTIN',
ANIMAL HANDLIN' use U+2019 (RIGHT SINGLE QUOTATION MARK), not
ASCII U+0027. All regex patterns must match the actual Unicode
character or the parser will fail to identify ability tokens,
leaving them in the narrative text.

**Additional ch10 fixes applied after parsing:**

- `|**Te ` → `|**The ` (article truncation in table headers)
- `Pacifc` → `Pacific` (OCR-style typo)
- `**Te ` → `**The ` (bold text article truncation)
- ` Te ` → ` The ` (mid-sentence article truncation)
- Duplicate-column table headers (same header repeated in
  adjacent pipe cells) collapsed to a single header
- Remaining standalone `Appendix: your tale begins` lines
  removed after lifepath block reformatting

---

### Category 8: Loose Bullet Lists

PDF extraction often introduces blank lines between bullet list
items, creating "loose" lists. Markdown renderers treat loose
lists differently (wrapping each item in `<p>` tags), producing
excessive vertical spacing.

**Detection:** A bullet line (`- ...`) followed by a blank line
followed by another bullet line (`- ...`).

**This is fully automatable.** The fix script
`fix_loose_lists.py` handles it:

1. Walk through lines sequentially
2. When a bullet item is followed by a blank line and then
   another bullet item (or indented continuation), remove the
   blank line
3. Preserve blank lines around list boundaries (before first
   item and after last item)

**Scale:** 343 blank lines removed across 7 chapters in this
project.

**When to apply:** As a final pass after all other fixes, since
earlier fixes may introduce or remove list items. Can also be
added to the automated pipeline as Pass 10.

---

### Workflow

1. **Audit all chapters**: Search for common artifact patterns
   across all files using terminal `Select-String` (Windows) or
   `grep` (Linux). Key patterns to search for:
   - `###.*[A-Z] [a-z]` (spaced characters in headings)
   - `### .* S ` or `### .* S$` (missing possessives)
   - Lines > 500 chars with ability names (garbled tables)
   - Known running header text as substrings
   - `^- ` followed by blank line followed by `^- `
     (loose bullet lists)
2. **Write targeted fix scripts** in `scripts/`: Python scripts
   with exact string replacements and regex patterns for each
   category. Group fixes by chapter or by issue type.
3. **Test incrementally**: Run each script, verify output, and
   use `git checkout -- corebook/filename.md` to revert if
   results are wrong. Complex parsers (like lifepath tables)
   may need multiple iterations — keep versioned scripts
   (v2, v3, v4, v5) to track what was tried.
4. **Move scripts to `scripts/`**: Fix scripts are reference
   artifacts, not chapter content. Keep them in `scripts/` for
   future reuse.
5. **Verify**: Spot-check 3-5 fixed sections against the
   original PDF to confirm accuracy.

### Manual Polish Checklist

After Phase 3, verify:

- [ ] No spaced-character headings remain
- [ ] No missing possessives (`S` as standalone token)
- [ ] No broken or truncated headings remain
- [ ] No orphaned single-line text fragments between sections
- [ ] No running headers embedded in paragraph text
- [ ] Character/place names are spelled correctly throughout
- [ ] Garbled table blocks are reformatted as readable markdown
- [ ] Bullet lists are compact (no blank lines between items)
- [ ] Smart quotes (U+2019, U+201C, U+201D) are consistent
      throughout (do not mix with ASCII equivalents)
- [ ] Fix scripts are in `scripts/`, not in chapter directories
