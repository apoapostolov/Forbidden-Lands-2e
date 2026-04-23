# Book-Specific Issue Log: Gamemaster's Guide (2019)

**Source PDF:** `files/01.1. Gamemaster's Guide (2019).pdf`
**Output file:** `supplement-1-gamemaster-guide/01.1. Gamemaster's Guide (2019).md`
**Raw extraction:** `supplement-1-gamemaster-guide/01.1. Gamemaster's Guide (2019).raw.md`
**Conversion date:** 2025
**Profile used:** `supplement`
**Pipeline:** `scripts/pdf_to_markdown.py`

---

## Conversion Summary

The first conversion attempt used `markitdown` and produced a catastrophically garbled 1,920-line file where two-column pages were interleaved sentence-by-sentence (e.g., left column text and right column sidebar text merged into single lines of 900–7,722 characters).

**Resolution:** Reconverted from the source PDF using `pymupdf4llm` (column-aware extraction) via `scripts/pdf_to_markdown.py --profile supplement`. This produced a 5,031-line file with proper paragraph structure and 669 headings.

---

## Known Artifact Types in This Book

### 1. Two-column sidebar callouts embedded in body text (RESOLVED)

**Pattern:** The GM's Guide extensively uses a two-column layout with sidebar boxes (grey shaded, e.g. "FOR THE GM'S EYES ONLY", "CREATE YOUR OWN ADVENTURES", "THE HOLLOWS – AN ADVENTURE HUB", "ONCE AGAIN?"). These become `### Heading` + blockquote or prose blocks after conversion.

**Resolution:** Handled by `pymupdf4llm` column detection. Some sidebar headings were split across two `###` headings (e.g., `### Create Your` / `### Own Adventures`) — these were joined in post-processing.

**Remaining:** None after cleanup.

### 2. Mid-paragraph blank-line splits from page/column boundaries (RESOLVED)

**Count:** 44 instances found in initial converted output.
**Pattern:** A prose paragraph would end without terminal punctuation (e.g., `Feel free to`) then have one or more blank lines, then continue with a lowercase word (`block their path with underlings...`).
**Cause:** The paragraph joiner in Pass 7 handles within-page column breaks but not cross-page ones.
**Resolution:** Post-processing script detected these (line ending without `.!?:;,)` followed by blank lines, then lowercase continuation) and joined them.

### 3. Drop-cap artifacts (RESOLVED)

**Pattern:** Page-opening paragraphs have decorative large initial capitals that PDFs export as a separate character. Result: `ou are the Gamemaster` with `Y` appended to the next word (`Yplayers`).
**Resolution:** Fixed by targeted string replacement: `"Yplayers"` → `"players"` and `"ou are the Gamemaster"` → `"You are the Gamemaster"`.

### 4. Map image text extraction (RESOLVED — 1 partially)

**Pattern:** The book contains a large two-page territory map (Chapter 2 "Kin" section, page ~50) and a village map (The Hollows). The PDF renderer extracts text labels from these maps as body text.

**Map 1 (Territory map, L~916):** Labels like `ELVES CANIDE DWARVES ELVES ENTS CANIDE DWARVES...` with spaced characters for place names (`H a r m s m o o r`). Replaced with `<!-- MAP IMAGE -->` comment.

**Map 2 (Strange Events table misidentified as map, L~3686):** The "STRANGE EVENTS IN THE HOLLOWS D6 EVENT DETAILS 1 The Game A..." line was incorrectly flagged as a map label by the ALL-CAPS word detection regex. Restored as a `| D6 | Event | Details |` markdown table.

**Remaining:** The territory map produces garbled place-name labels. These are handled with `<!-- MAP IMAGE -->` placeholder. A hand-drawn illustration caption would need to be added manually if desired.

### 5. Truncated word fragments at column boundaries (RESOLVED)

**Pattern:** Words split mid-syllable across column or page breaks (e.g., `typi-` / `cal NPCs`; `sto-` / `ne wall`). The standard hyphen-EOL detection catches most, but cross-picture-block splits are missed.

**Instances fixed:**

- `Stats for several typi-` → rejoined with orphaned `cal NPCs can be found...` continuation
- `surrounded by a low sto-` → fixed to `stone wall`

### 6. Heading case inconsistencies (RESOLVED)

`pymupdf4llm` title-cases all-caps headings. Some came out incorrectly:

| Original (PDF)         | Wrong output           | Fixed to               |
| ---------------------- | ---------------------- | ---------------------- |
| FOR THE GM'S EYES ONLY | For the Gm's Eyes Only | For the GM's Eyes Only |
| HANDLING NPCS          | Handling Npcs          | Handling NPCs          |
| NON PLAYER CHARACTERS  | Non Player Characters  | Non-Player Characters  |
| NPCS IN GROUPS:        | NPCS IN GROUPS:        | **NPCs in Groups:**    |

### 7. Front matter credits garbled (PARTIALLY RESOLVED)

The credits page (title + credits in columns) produced merged inline text:
`Tomas Härenstam SETTING & ADVENTURE SITES Erik Granström`
→ Split into separate `## HEADING` / value pairs.

Some credits roles remain merged (e.g., `GRAPHIC DESIGN Christian Granath COVER ART Simon Stålenhag`) — partially resolved; these are cosmetic and low-priority.

### 8. All-H3 heading hierarchy (KNOWN ISSUE — unresolved)

The conversion produced 1 H1, 8 H2 (front matter credits), and 664 H3. The actual book structure is:

- **Chapter-level headings** (H2): The Gamemaster, History, Gods, Kin, Bestiary, Artifacts, Encounters, Adventure Sites, The Hollows, Weatherstone, Vale of the Dead
- **Section headings** (H3): Principles of the Game, First Session, etc.
- **Sub-section / NPC headings** (H4): Typical Alderlander, Let Them Live, etc.

The pipeline does not currently distinguish heading levels from PDF for this book because the PDF uses uniform font weights for all-caps headings at different sizes. A font-size-aware extraction pass would be needed to recover the hierarchy.

**Workaround:** Acceptable for first-pass manuscript work. A heading hierarchy pass can be done manually or by comparing against the TOC table extracted at the top of the file.

### 9. "Once Again?" sidebar table (NOT YET VERIFIED)

The sidebar `ONCE AGAIN?` (stronghold events re-roll guidance) may have its three bullet points merged into prose. Check around the `Events at the Stronghold` section.

### 10. Adventure site statblock formatting (NOT YET VERIFIED)

NPC/monster statblocks in the three adventure sites (The Hollows, Weatherstone, Vale of the Dead) use a two-column layout. Some may have misaligned `> **SKILLS:**` / `**TALENTS:**` blocks. Visual spot-check recommended at the adventure site chapters.

---

## Post-Processing Script Applied

```python
# Key transforms applied after scripts/pdf_to_markdown.py:
# 1. Join 44 mid-paragraph blank-line splits (non-punctuated line + blank + lowercase continuation)
# 2. Replace 2 map garbage lines with <!-- MAP IMAGE --> comment
# 3. Fix drop-cap: "Yplayers" → "players", "ou are the Gamemaster" → "You are the Gamemaster"
# 4. Heading fixes: Gm's → GM's, Handling Npcs → Handling NPCs, Non Player → Non-Player
# 5. Join split headings: "### Create Your\n### Own Adventures" → "### Create Your Own Adventures"
# 6. Fix typi- / cal NPCs orphan
# 7. Fix sto- / ne wall orphan
# 8. Fix mid-sentence split: "he is dead,\n\nbut" → "he is dead, but"
# 9. Fix front matter credits (partial)
# 10. Restore Strange Events table row incorrectly flagged as map image
```

---

## Lint Status

Run with: `markdownlint "supplement-1-gamemaster-guide/01.1. Gamemaster's Guide (2019).md"`

Not yet run. Expect MD041 (first heading not H1), MD022/MD023 (heading spacing), and MD033 if any HTML comments remain.
