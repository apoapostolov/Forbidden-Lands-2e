#!/usr/bin/env python3
"""
PDF → Markdown conversion pipeline for Forbidden Lands RPG sourcebooks.

Usage:
    python scripts/pdf_to_markdown.py path/to/book.pdf path/to/output/ [--profile PROFILE]

Implements the cleanup passes from the pdf-to-rpg-markdown skill and writes
an OCR artifact audit report alongside the raw and cleaned markdown.

Pipeline:
    1. Extract with pymupdf4llm (column-aware)
    2. Pass 1 : Front matter and noise removal, including repeated page
                furniture inferred from page-sized chunks
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

import argparse
import re
import sys
from pathlib import Path

try:
    import wordninja  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - dependency fallback
    wordninja = None

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

DOCUMENT_PROFILES = {
    "default": {
        "description": "Generic RPG supplement cleanup profile",
        "footer_phrases": set(),
    },
    "corebook": {
        "description": "Large chaptered corebook with strong running-header patterns",
        "footer_phrases": {"forbidden lands"},
    },
    "supplement": {
        "description": "Standalone supplement with booklet-style repeated footers",
        "footer_phrases": set(),
    },
    "spell-compendium": {
        "description": "Spell-heavy manuscript with repeated spell metadata blocks",
        "footer_phrases": {"spells & sorcerers"},
    },
    "bestiary": {
        "description": "Creature-focused book with statblocks and monster attacks",
        "footer_phrases": set(),
    },
    "lifepath-generator": {
        "description": "Dense generator with many dice and matrix tables",
        "footer_phrases": set(),
    },
}

AUDIT_PATTERNS = {
    "picture_placeholders": re.compile(r"^\*\*==>.*<==\*\*$", re.MULTILINE),
    "picture_text_markers": re.compile(r"Start of picture text|End of picture text", re.IGNORECASE),
    "html_breaks": re.compile(r"<br\s*/?>", re.IGNORECASE),
    "page_number_lines": re.compile(r"^(?:#\s*)?[–—-]?\s*\d{1,3}\s*[–—-]?\s*$", re.MULTILINE),
    "all_caps_lines": re.compile(r"^[A-Z][A-Z\s&,'\-:]{4,}$", re.MULTILINE),
    "markdown_headings": re.compile(r"^#{1,6}\s", re.MULTILINE),
    "pipe_table_lines": re.compile(r"^\|.*\|$", re.MULTILINE),
    "double_blank_runs": re.compile(r"\n{3,}"),
    "spaced_heading_candidates": re.compile(r"^(?:#{1,6}\s+)?(?:[A-Za-z]\s){4,}[A-Za-z]$", re.MULTILINE),
}

PAGE_NUMBER_RE = re.compile(r"^#?\s*[–—-]?\s*\d{1,3}\s*[–—-]?\s*$")


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
            segmented = wordninja.split(collapsed) if wordninja else [collapsed]
            words.extend(segmented)

    reconstructed = " ".join(words)
    titled = smart_title_case(reconstructed)

    # Check against corrections dict
    return HEADING_CORRECTIONS.get(titled, titled)


def normalize_furniture_line(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def is_page_furniture_candidate(text: str) -> bool:
    stripped = text.strip()
    lowered = stripped.lower()
    if not stripped:
        return False
    if stripped.startswith("**==>") or "Start of picture text" in stripped or "End of picture text" in stripped:
        return False
    if stripped.startswith(("-", "*", "+")):
        return False
    if lowered.startswith(("e rank", "e range", "e duration", "e ingredient")):
        return False
    if ":" in stripped:
        return False
    if len(stripped) < 3 or len(stripped) > 80:
        return False
    if re.search(r"[.?!]", stripped):
        return False
    if stripped.startswith("|"):
        return False
    return True


def split_pages(lines: list[str]) -> list[list[str]]:
    pages: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if PAGE_NUMBER_RE.match(line.strip()):
            if current:
                pages.append(current)
            current = []
            continue
        current.append(line)
    if current:
        pages.append(current)
    return pages


def detect_repeated_page_furniture(
    pages: list[list[str]],
    top_window: int = 6,
    bottom_window: int = 6,
    min_count: int = 3,
) -> tuple[set[str], set[str]]:
    top_counts: dict[str, int] = {}
    bottom_counts: dict[str, int] = {}

    for page in pages:
        nonempty = [line for line in page if line.strip()]
        if not nonempty:
            continue

        top_seen: set[str] = set()
        for line in nonempty[:top_window]:
            normalized = normalize_furniture_line(line)
            if is_page_furniture_candidate(line) and normalized:
                top_seen.add(normalized)

        bottom_seen: set[str] = set()
        for line in nonempty[-bottom_window:]:
            normalized = normalize_furniture_line(line)
            if is_page_furniture_candidate(line) and normalized:
                bottom_seen.add(normalized)

        for item in top_seen:
            top_counts[item] = top_counts.get(item, 0) + 1
        for item in bottom_seen:
            bottom_counts[item] = bottom_counts.get(item, 0) + 1

    top_candidates = {item for item, count in top_counts.items() if count >= min_count}
    bottom_candidates = {item for item, count in bottom_counts.items() if count >= min_count}
    return top_candidates, bottom_candidates


# ---------------------------------------------------------------------------
# Pass 1: Front matter and noise removal
# ---------------------------------------------------------------------------
def pass1_noise_removal(lines: list[str], profile: dict | None = None) -> list[str]:
    out = []
    profile = profile or DOCUMENT_PROFILES["default"]
    footer_phrases = {p.lower() for p in profile.get("footer_phrases", set())}
    pages = split_pages(lines)
    repeated_top, repeated_bottom = detect_repeated_page_furniture(pages)
    in_toc = False
    page_lines: list[str] = []
    page_nonempty_index = 0
    page_nonempty_total = 0

    def flush_page(page_buffer: list[str]) -> None:
        nonlocal out, in_toc
        if not page_buffer:
            return
        nonempty_positions = [i for i, page_line in enumerate(page_buffer) if page_line.strip()]
        total_nonempty = len(nonempty_positions)
        seen_nonempty = 0
        for idx, line in enumerate(page_buffer):
            stripped = line.strip()
            normalized = normalize_furniture_line(line)

            # Table of contents: pipe-table rows with dot-leaders
            if re.search(r"\.{4,}", stripped) or "<br>" in stripped and "......" in stripped:
                in_toc = True
            if in_toc:
                if not stripped or re.match(r"^#{1,2}\s", stripped):
                    in_toc = False
                else:
                    continue

            if PAGE_NUMBER_RE.match(stripped):
                continue

            if stripped:
                seen_nonempty += 1
                if seen_nonempty <= 6 and normalized in repeated_top:
                    continue
                if total_nonempty - seen_nonempty < 6 and normalized in repeated_bottom:
                    continue

            if stripped.lower() in footer_phrases:
                continue

            # Common running footer style like "spells & sorcerers"
            if re.match(r"^[a-z0-9 &'\-]+$", stripped) and len(stripped) <= 32:
                if stripped == stripped.lower() and stripped.count(" ") >= 1:
                    continue

            # Copyright / distribution notices
            if re.match(r"^©\s*\d{4}", stripped):
                continue
            if re.match(r"^PDF distributed", stripped, re.IGNORECASE):
                continue
            if re.match(r"^All rights reserved", stripped, re.IGNORECASE):
                continue

            out.append(line)

    for line in lines:
        if PAGE_NUMBER_RE.match(line.strip()):
            flush_page(page_lines)
            page_lines = []
            continue
        page_lines.append(line)

    flush_page(page_lines)
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


def pass11_dropcap_repair(lines: list[str]) -> list[str]:
    """Repair a small set of high-confidence drop-cap OCR losses."""
    replacements = {
        "elcome ": "Welcome ",
        "his ": "This ",
        "othing ": "Nothing ",
        "ossessing ": "Possessing ",
        "aving ": "Having ",
        "agic ": "Magic ",
    }
    out: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        if not stripped or re.match(r"^(#{1,6}\s|>|\||[-*+]\s)", stripped):
            out.append(line)
            continue
        fixed = line
        for bad, good in replacements.items():
            if stripped.startswith(bad):
                indent = line[: len(line) - len(stripped)]
                fixed = indent + good + stripped[len(bad):]
                break
        out.append(fixed)
    return out


def collect_artifact_counts(text: str) -> dict[str, int]:
    return {name: len(pattern.findall(text)) for name, pattern in AUDIT_PATTERNS.items()}


def write_audit_report(
    raw_path: Path,
    clean_path: Path,
    raw_text: str,
    clean_text: str,
    profile_name: str,
) -> Path:
    raw_counts = collect_artifact_counts(raw_text)
    clean_counts = collect_artifact_counts(clean_text)
    report_path = raw_path.with_suffix("").with_suffix(".ocr-report.md")

    lines = [
        "# OCR Artifact Report",
        "",
        f"- Raw: `{raw_path.name}`",
        f"- Clean: `{clean_path.name}`",
        f"- Profile: `{profile_name}`",
        "",
        "## Raw Counts",
        "",
    ]
    for key in sorted(raw_counts):
        lines.append(f"- `{key}`: {raw_counts[key]}")
    lines.extend(["", "## Clean Counts", ""])
    for key in sorted(clean_counts):
        lines.append(f"- `{key}`: {clean_counts[key]}")
    lines.extend(["", "## Delta", ""])
    for key in sorted(raw_counts):
        delta = clean_counts[key] - raw_counts[key]
        lines.append(f"- `{key}`: {raw_counts[key]} -> {clean_counts[key]} ({delta:+d})")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ---------------------------------------------------------------------------
# Full pipeline
# ---------------------------------------------------------------------------
def run_pipeline(
    pdf_path: Path,
    output_dir: Path,
    reuse_raw: bool = False,
    profile_name: str = "default",
) -> Path:
    import pymupdf4llm

    profile = DOCUMENT_PROFILES.get(profile_name, DOCUMENT_PROFILES["default"])

    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / (pdf_path.stem + ".raw.md")
    clean_path = output_dir / (pdf_path.stem + ".md")

    if reuse_raw and raw_path.exists():
        print(f"[1/12] Reusing existing raw: {raw_path.name} ({raw_path.stat().st_size:,} bytes)")
        md = raw_path.read_text(encoding="utf-8")
    else:
        print(f"[1/12] Extracting {pdf_path.name} …")
        md = pymupdf4llm.to_markdown(str(pdf_path))
        raw_path.write_text(md, encoding="utf-8")
        print(f"       Raw markdown saved → {raw_path.name} ({len(md):,} chars)")
    print(f"       Profile        → {profile_name} ({profile['description']})")

    lines = md.splitlines(keepends=True)

    print("[2/12] Pass 1: noise removal …")
    lines = pass1_noise_removal(lines, profile=profile)

    print("[3/12] Pass 2: running headers …")
    lines = pass2_running_headers(lines)

    print("[4/12] Pass 3: spaced heading reconstruction …")
    lines = pass3_spaced_headings(lines)

    print("[5/12] Pass 4: picture block conversion …")
    lines = pass4_picture_blocks(lines)

    print("[6/12] Pass 5: heading hierarchy normalisation …")
    lines = pass5_heading_hierarchy(lines)

    print("[7/12] Pass 6: sidebar → blockquote …")
    lines = pass6_sidebars(lines)

    print("[8/12] Pass 7: paragraph joining …")
    lines = pass7_paragraph_joining(lines)

    print("[9/12] Pass 8: table <br> cleanup …")
    lines = pass8_table_br(lines)

    print("[10/12] Pass 9: whitespace normalisation …")
    lines = pass9_whitespace(lines)

    print("[11/12] Pass 10: loose bullet-list compaction …")
    lines = pass10_loose_lists(lines)

    print("[12/12] Pass 11: conservative drop-cap repair …")
    lines = pass11_dropcap_repair(lines)

    clean_text = "".join(lines)
    clean_path.write_text(clean_text, encoding="utf-8")
    report_path = write_audit_report(raw_path, clean_path, md, clean_text, profile_name)
    print(f"\nDone. Clean markdown → {clean_path}")
    print(f"      OCR report     → {report_path}")
    print(f"      Lines: {len(lines):,}  |  Chars: {sum(len(l) for l in lines):,}")
    return clean_path


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert RPG PDFs to cleaned markdown")
    parser.add_argument("pdf", help="Path to source PDF")
    parser.add_argument("output_dir", help="Output directory for raw and cleaned markdown")
    parser.add_argument("--reuse-raw", action="store_true", help="Reuse an existing .raw.md file")
    parser.add_argument(
        "--profile",
        default="default",
        choices=sorted(DOCUMENT_PROFILES.keys()),
        help="Cleanup profile tuned for document type",
    )
    args = parser.parse_args()

    pdf = Path(args.pdf)
    out = Path(args.output_dir)
    reuse_raw = args.reuse_raw

    if not reuse_raw and not pdf.exists():
        print(f"Error: {pdf} not found")
        sys.exit(1)

    run_pipeline(pdf, out, reuse_raw=reuse_raw, profile_name=args.profile)
