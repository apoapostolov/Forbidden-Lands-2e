#!/usr/bin/env python3
"""
PDF → Markdown conversion pipeline for Forbidden Lands RPG sourcebooks.

Usage:
    python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output/

Implements all 9 cleanup passes from the pdf-to-rpg-markdown skill, plus
Pass 10 (loose bullet list compaction).

Pipeline:
    1. Extract with pymupdf4llm (column-aware)
    2. Pass 1 : Front matter and noise removal
    3. Pass 2 : Running header deduplication
    4. Pass 3 : Spaced heading reconstruction
    5. Pass 4 : Picture block conversion / removal
    6. Pass 5 : Heading hierarchy normalisation
    7. Pass 6 : Sidebar (italic paragraph) → blockquote
    8. Pass 7 : Paragraph joining across column-break fragments
    9. Pass 8 : Inline <br> removal from table cells
   10. Pass 9 : Whitespace normalisation
   11. Pass 10: Loose bullet-list compaction
"""

import re
import sys
import shutil
from pathlib import Path

import wordninja

# ---------------------------------------------------------------------------
# Game-specific heading corrections
# ---------------------------------------------------------------------------
HEADING_CORRECTIONS = {
    # Drop-cap title reconstruction fixes
    "Or Bidden F Lands": "Forbidden Lands",
    "Orbidden F Lands": "Forbidden Lands",
    "Orbidden Lands": "Forbidden Lands",
    # Forbidden Lands attribute / skill truncations
    "Willpow Er": "Willpower",
    "Wil Lpower": "Willpower",
    "Wil Lpow Er": "Willpower",
    "Str Ength": "Strength",
    "Agi Lity": "Agility",
    "Empat Hy": "Empathy",
    "Know The Land": "Know the Land",
    "Abi Lity": "Ability",
    # Common FL chapter/section names that wordninja mangles
    "Str Ongh Old": "Stronghold",
    "Strongh Old": "Stronghold",
    "Forbid Den Lands": "Forbidden Lands",
    "Mercenaries": "Mercenaries",
    "Th E Wil D": "The Wild",
    "Cr Itical": "Critical",
    "Crit Ical": "Critical",
    # Generic RPG terms
    "Npcs And Abilities": "NPCs and Abilities",
    "Introduction To Rpgs": "Introduction to RPGs",
    "Non Player Characters": "Non-Player Characters",
}

# Words that should remain lowercase in title case (unless starting the heading)
LOWERCASE_WORDS = {
    "a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet",
    "at", "by", "in", "of", "on", "to", "up", "as", "is", "it",
}

# Words that should stay ALL-CAPS in title case
ALLCAPS_WORDS = {"RPG", "NPC", "GM", "PC", "FL", "D6", "D66"}


# ---------------------------------------------------------------------------
# Utility: smart title case
# ---------------------------------------------------------------------------
def smart_title_case(text: str) -> str:
    words = text.split()
    result = []
    for i, word in enumerate(words):
        upper = word.upper()
        if upper in ALLCAPS_WORDS:
            result.append(upper)
        elif i == 0 or word.lower() not in LOWERCASE_WORDS:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)


# ---------------------------------------------------------------------------
# Pass 3 helper: reconstruct a spaced heading
# ---------------------------------------------------------------------------
def is_spaced_heading(text: str) -> bool:
    """Return True if >20% of space-tokens are single alpha chars and no sentence punctuation."""
    # Never reconstruct if it looks like a sentence
    if re.search(r"[.?!,;]", text):
        return False
    tokens = text.split()
    if len(tokens) < 3:
        return False
    single_alpha = sum(1 for t in tokens if len(t) == 1 and t.isalpha())
    return single_alpha / len(tokens) > 0.20


def reconstruct_spaced_heading(text: str) -> str:
    """Turn 'Y O U R  A D V E N T U R E R' into 'Your Adventurer'."""
    # Split on 2+ spaces → definite word group boundaries
    groups = re.split(r"  +", text)
    words = []
    for group in groups:
        collapsed = group.replace(" ", "")
        if not collapsed:
            continue
        if len(collapsed) <= 3:
            words.append(collapsed)
        else:
            segmented = wordninja.split(collapsed)
            words.extend(segmented)

    reconstructed = " ".join(words)
    titled = smart_title_case(reconstructed)

    # Check against corrections dict
    return HEADING_CORRECTIONS.get(titled, titled)


# ---------------------------------------------------------------------------
# Pass 1: Front matter and noise removal
# ---------------------------------------------------------------------------
def pass1_noise_removal(lines: list[str]) -> list[str]:
    out = []
    in_toc = False
    for line in lines:
        stripped = line.strip()

        # Table of contents: pipe-table rows with dot-leaders
        if re.search(r"\.{4,}", stripped) or "<br>" in stripped and "......" in stripped:
            in_toc = True
        if in_toc:
            if not stripped or re.match(r"^#{1,2}\s", stripped):
                in_toc = False
            else:
                continue

        # Page numbers: –N–, - N -, # – N –, bare standalone digit(s)
        if re.match(r"^#?\s*[–—-]\s*\d+\s*[–—-]\s*$", stripped):
            continue
        if re.match(r"^-\s*\d+\s*-$", stripped):
            continue
        if re.match(r"^\d{1,3}$", stripped):
            continue

        # Copyright / distribution notices
        if re.match(r"^©\s*\d{4}", stripped):
            continue
        if re.match(r"^PDF distributed", stripped, re.IGNORECASE):
            continue
        if re.match(r"^All rights reserved", stripped, re.IGNORECASE):
            continue

        out.append(line)
    return out


# ---------------------------------------------------------------------------
# Pass 2: Running header deduplication
# ---------------------------------------------------------------------------
def pass2_running_headers(lines: list[str]) -> list[str]:
    """Keep the first occurrence of each chapter-level heading; remove repeats."""
    seen: set[str] = set()
    out = []
    for line in lines:
        stripped = line.strip()
        # Candidate running header: all-uppercase line, or "Chapter N - Title"
        key = re.sub(r"\s+", " ", stripped.lower())
        is_chapter = re.match(r"^##\s+chapter\s+", stripped, re.IGNORECASE)
        is_allcaps_line = (
            stripped
            and stripped == stripped.upper()
            and len(stripped) > 4
            and re.match(r"^[A-Z\s\-–:]+$", stripped)
        )
        if is_allcaps_line and not stripped.startswith("#"):
            if key in seen:
                continue
            seen.add(key)
        if is_chapter:
            if key in seen:
                continue
            seen.add(key)
        out.append(line)
    return out


# ---------------------------------------------------------------------------
# Pass 3: Spaced heading reconstruction
# ---------------------------------------------------------------------------
def pass3_spaced_headings(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        m = re.match(r"^(#{1,4})\s+(.+)$", line)
        if m:
            hashes, content = m.group(1), m.group(2)
            # Strip bold markers before testing
            bare = re.sub(r"\*\*(.+?)\*\*", r"\1", content).strip()
            if is_spaced_heading(bare):
                new_content = reconstruct_spaced_heading(bare)
                out.append(f"{hashes} {new_content}\n")
                continue
        out.append(line)
    return out


# ---------------------------------------------------------------------------
# Pass 4: Picture block removal / extraction
# ---------------------------------------------------------------------------

TABLE_KEYWORDS = re.compile(
    r"\b(action|range|damage|result|bonus|modifier|penalty|roll|type|effect|"
    r"skill|attribute|weapon|armor|armour|speed|initiative|strength|agility|"
    r"wits|empathy|willpower)\b",
    re.IGNORECASE,
)


def picture_text_to_table(lines_in_block: list[str]) -> list[str]:
    """Try to turn picture text into a pipe table if it looks tabular."""
    if not lines_in_block:
        return []
    header = lines_in_block[0]
    if TABLE_KEYWORDS.search(header) and len(lines_in_block) >= 2:
        cols = [c.strip() for c in header.split() if c.strip()]
        rows = []
        for row_line in lines_in_block[1:]:
            cells = row_line.split("|") if "|" in row_line else [row_line]
            rows.append("| " + " | ".join(c.strip() for c in cells) + " |")
        header_row = "| " + " | ".join(cols) + " |"
        sep_row = "| " + " | ".join("---" for _ in cols) + " |"
        return [header_row, sep_row] + rows
    return lines_in_block


START_PICTURE_RE = re.compile(r"\*\*-+\s*Start of picture text\s*-+\*\*(<br>)?", re.IGNORECASE)
END_PICTURE_RE   = re.compile(r"\*\*-+\s*End of picture text\s*-+\*\*(<br>)?",   re.IGNORECASE)


def _flush_picture_block(picture_text_lines: list[str], out: list[str]) -> None:
    if not picture_text_lines:
        return
    all_short = all(len(l) < 40 for l in picture_text_lines)
    if len(picture_text_lines) <= 2 and all_short:
        return  # discard caption
    converted = picture_text_to_table(picture_text_lines)
    out.extend(l + "\n" for l in converted)


def _extract_parts(raw_text: str) -> list[str]:
    """Split on <br>, strip bold markers, return non-empty parts."""
    parts = []
    for part in re.split(r"<br>", raw_text):
        part = re.sub(r"\*\*", "", part).strip()
        if part:
            parts.append(part)
    return parts


def pass4_picture_blocks(lines: list[str]) -> list[str]:
    """Remove image placeholders and convert/discard picture text blocks.

    Handles all three pymupdf4llm layouts:
      A) Start on own line, End on own line
      B) Start on own line, content+End on same next line
      C) Start+content+End all on one line
    """
    out: list[str] = []
    in_picture_text = False
    picture_text_lines: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Image placeholder: drop entirely ──────────────────────────────
        if re.match(r"^\*\*==>.*<==\*\*", stripped):
            i += 1
            continue

        sm = START_PICTURE_RE.search(stripped)
        em = END_PICTURE_RE.search(stripped)

        # ── Layout C: Start AND End on the same line ───────────────────────
        if sm and em:
            content_between = stripped[sm.end(): em.start()]
            _flush_picture_block(_extract_parts(content_between), out)
            i += 1
            continue

        # ── Layout A/B start: Start marker found ───────────────────────────
        if sm and not em:
            in_picture_text = True
            picture_text_lines = []
            # Anything after the Start marker on the same line
            after = stripped[sm.end():]
            picture_text_lines.extend(_extract_parts(after))
            i += 1
            continue

        # ── End marker found (layout A: own line; layout B: line has content first) ─
        if em:
            if in_picture_text:
                before = stripped[: em.start()]
                picture_text_lines.extend(_extract_parts(before))
                _flush_picture_block(picture_text_lines, out)
                picture_text_lines = []
                in_picture_text = False
            # else: stray End marker — just drop it
            i += 1
            continue

        # ── Inside picture text block ──────────────────────────────────────
        if in_picture_text:
            picture_text_lines.extend(_extract_parts(stripped))
            i += 1
            continue

        out.append(line)
        i += 1
    return out


# ---------------------------------------------------------------------------
# Pass 5: Heading hierarchy normalisation
# ---------------------------------------------------------------------------

ARTICLE_WORDS = {"a", "an", "the", "and", "but", "or", "of", "in", "on", "to", "at",
                 "for", "by", "with", "from", "into", "over", "as"}

EPIGRAPH_RE = re.compile(r'^#+\s+["\u201c]')
ATTRIBUTION_RE = re.compile(r"^\*\*[A-Z][A-Z '\-,\.]+\*\*$")


def heading_title_case(text: str) -> str:
    words = text.split()
    result = []
    for i, w in enumerate(words):
        if w.upper() in ALLCAPS_WORDS:
            result.append(w.upper())
        elif i == 0:
            result.append(w.capitalize())
        elif w.lower() in ARTICLE_WORDS:
            result.append(w.lower())
        else:
            result.append(w.capitalize())
    return " ".join(result)


def pass5_heading_hierarchy(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        stripped = line.strip()

        # ## "quote" or ## **"quote"** → epigraph blockquote
        if EPIGRAPH_RE.match(stripped):
            content = re.sub(r"^#+\s+", "", stripped)
            content = re.sub(r"^\*\*(.+)\*\*$", r"\1", content)
            out.append(f"> *{content}*\n")
            continue

        # ## **bold text** → ### bold text
        m = re.match(r"^(##)\s+\*\*(.+)\*\*$", stripped)
        if m:
            text = m.group(2).strip()
            out.append(f"### {heading_title_case(text)}\n")
            continue

        # ## non-chapter text → ### text (keep ## for actual "Chapter N" lines)
        m = re.match(r"^(##)\s+(.+)$", stripped)
        if m:
            text = m.group(2).strip()
            is_chapter = re.match(r"^chapter\s+[\dIVXivx]+", text, re.IGNORECASE)
            is_book_title = lines.index(line) < 20  # first 20 lines → likely book title
            if not is_chapter and not is_book_title:
                out.append(f"### {heading_title_case(text)}\n")
                continue

        # Bold all-caps free-standing line → attribution
        if ATTRIBUTION_RE.match(stripped):
            content = re.sub(r"^\*\*(.+)\*\*$", r"\1", stripped)
            out.append(f"> \u2014 {content}\n")
            continue

        out.append(line)
    return out


# ---------------------------------------------------------------------------
# Pass 6: Sidebar (long italic paragraph) → blockquote
# ---------------------------------------------------------------------------
def pass6_sidebars(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        stripped = line.strip()
        # _italic text longer than 20 chars_ → > _italic text_
        m = re.match(r"^_(.{20,})_$", stripped)
        if m:
            out.append(f"> _{m.group(1)}_\n")
            continue
        out.append(line)
    return out


# ---------------------------------------------------------------------------
# Pass 7: Paragraph joining
# ---------------------------------------------------------------------------
STRUCTURAL_LINE_RE = re.compile(r"^(#{1,4}\s|>|[-*+]\s|\||\s*```|\s*$)")
SENTENCE_END_RE = re.compile(r'[.!?:;"\')\u201d]\s*$')


def pass7_paragraph_joining(lines: list[str]) -> list[str]:
    """Join continuation fragments split by column breaks."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        if STRUCTURAL_LINE_RE.match(stripped) or not stripped:
            out.append(line)
            i += 1
            continue

        # Accumulate this text line
        current = stripped
        j = i + 1

        while j < len(lines):
            next_line = lines[j].rstrip()

            # Join if next line (no blank separator) starts lowercase
            if next_line and not STRUCTURAL_LINE_RE.match(next_line):
                if not SENTENCE_END_RE.search(current):
                    # Continuation with no blank line
                    current = current.rstrip() + " " + next_line.lstrip()
                    j += 1
                    continue
                elif next_line and next_line[0].islower():
                    current = current.rstrip() + " " + next_line.lstrip()
                    j += 1
                    continue

            # Join across a single blank line if no sentence-end and next is text
            if not next_line:
                if j + 1 < len(lines):
                    after_blank = lines[j + 1].rstrip()
                    if (after_blank
                            and not STRUCTURAL_LINE_RE.match(after_blank)
                            and not SENTENCE_END_RE.search(current)):
                        current = current.rstrip() + " " + after_blank.lstrip()
                        j += 2
                        continue
            break

        out.append(current + "\n")
        i = j
    return out


# ---------------------------------------------------------------------------
# Pass 8: Inline <br> cleanup in table cells
# ---------------------------------------------------------------------------
def pass8_table_br(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        if line.startswith("|"):
            line = re.sub(r"<br\s*/?>", " ", line)
        out.append(line)
    return out


# ---------------------------------------------------------------------------
# Pass 9: Whitespace normalisation
# ---------------------------------------------------------------------------
def pass9_whitespace(lines: list[str]) -> list[str]:
    # Strip trailing whitespace
    lines = [l.rstrip() + "\n" for l in lines]

    # Ensure blank line before/after headings
    spaced: list[str] = []
    for i, line in enumerate(lines):
        if re.match(r"^#{1,4}\s", line.strip()):
            if spaced and spaced[-1].strip():
                spaced.append("\n")
            spaced.append(line)
            if i + 1 < len(lines) and lines[i + 1].strip():
                spaced.append("\n")
        else:
            spaced.append(line)

    # Collapse 3+ consecutive blank lines → 2
    out: list[str] = []
    blank_count = 0
    for line in spaced:
        if not line.strip():
            blank_count += 1
            if blank_count <= 2:
                out.append(line)
        else:
            blank_count = 0
            out.append(line)

    # Trim leading/trailing blank lines
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    out.append("\n")

    return out


# ---------------------------------------------------------------------------
# Pass 10: Loose bullet-list compaction
# ---------------------------------------------------------------------------
def pass10_loose_lists(lines: list[str]) -> list[str]:
    """Remove blank lines between consecutive bullet items."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        # If this is a bullet line followed by blank then another bullet
        if re.match(r"^[-*+]\s", line.strip()):
            if (i + 2 < len(lines)
                    and not lines[i + 1].strip()
                    and re.match(r"^[-*+]\s", lines[i + 2].strip())):
                i += 2  # skip the blank
                continue
        i += 1
    return out


# ---------------------------------------------------------------------------
# Full pipeline
# ---------------------------------------------------------------------------
def run_pipeline(pdf_path: Path, output_dir: Path, reuse_raw: bool = False) -> Path:
    import pymupdf4llm

    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / (pdf_path.stem + ".raw.md")
    clean_path = output_dir / (pdf_path.stem + ".md")

    if reuse_raw and raw_path.exists():
        print(f"[1/11] Reusing existing raw: {raw_path.name} ({raw_path.stat().st_size:,} bytes)")
        md = raw_path.read_text(encoding="utf-8")
    else:
        print(f"[1/11] Extracting {pdf_path.name} …")
        md = pymupdf4llm.to_markdown(str(pdf_path))
        raw_path.write_text(md, encoding="utf-8")
        print(f"       Raw markdown saved → {raw_path.name} ({len(md):,} chars)")

    lines = md.splitlines(keepends=True)

    print("[2/11] Pass 1: noise removal …")
    lines = pass1_noise_removal(lines)

    print("[3/11] Pass 2: running headers …")
    lines = pass2_running_headers(lines)

    print("[4/11] Pass 3: spaced heading reconstruction …")
    lines = pass3_spaced_headings(lines)

    print("[5/11] Pass 4: picture block conversion …")
    lines = pass4_picture_blocks(lines)

    print("[6/11] Pass 5: heading hierarchy normalisation …")
    lines = pass5_heading_hierarchy(lines)

    print("[7/11] Pass 6: sidebar → blockquote …")
    lines = pass6_sidebars(lines)

    print("[8/11] Pass 7: paragraph joining …")
    lines = pass7_paragraph_joining(lines)

    print("[9/11] Pass 8: table <br> cleanup …")
    lines = pass8_table_br(lines)

    print("[10/11] Pass 9: whitespace normalisation …")
    lines = pass9_whitespace(lines)

    print("[11/11] Pass 10: loose bullet-list compaction …")
    lines = pass10_loose_lists(lines)

    clean_path.write_text("".join(lines), encoding="utf-8")
    print(f"\nDone. Clean markdown → {clean_path}")
    print(f"      Lines: {len(lines):,}  |  Chars: {sum(len(l) for l in lines):,}")
    return clean_path


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/pdf_to_markdown.py <pdf> <output-dir> [--reuse-raw]")
        sys.exit(1)

    pdf = Path(sys.argv[1])
    out = Path(sys.argv[2])
    reuse_raw = "--reuse-raw" in sys.argv

    if not reuse_raw and not pdf.exists():
        print(f"Error: {pdf} not found")
        sys.exit(1)

    run_pipeline(pdf, out, reuse_raw=reuse_raw)
