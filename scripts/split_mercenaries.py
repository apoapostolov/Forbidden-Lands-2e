#!/usr/bin/env python3
"""One-time script: split 12-mercenaries-of-forbidden-lands.md into parts.

Run from repo root:
    python scripts/split_mercenaries.py

Creates temp-work/mercenaries-of-forbidden-lands/*.md part files and replaces chapter
references with bolded all-caps name format.
"""

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SOURCE = REPO / "corebook" / "12-mercenaries-of-forbidden-lands.md"
PARTS_DIR = REPO / "temp-work" / "mercenaries-of-forbidden-lands"

# Chapter name mapping (number -> ALL-CAPS name)
CHAPTER_NAMES = {
    "2": "YOUR ADVENTURER",
    "3": "SKILLS",
    "4": "TALENTS",
    "5": "COMBAT AND DAMAGE",
    "6": "CRITICAL INJURIES",
    "7": "MAGIC",
    "8": "JOURNEYS",
    "9": "THE STRONGHOLD",
    "10": "GEAR",
    "11": "APPENDIX",
}

# Section groupings: (output_filename, list_of_H2_header_prefixes_to_include)
# Order matters — first match wins. None means "everything before first H2".
PART_DEFS = [
    ("introduction.md", [None, "What This Chapter Is", "The Band"]),
    ("recruitment-and-pay.md", ["Recruitment and Quality", "Pay, Provisions, and Consequences"]),
    ("extortion-and-tribute.md", ["Village Extortion and Tribute"]),
    ("contracts-and-bounties.md", ["Contracts and Bounties"]),
    ("campaign-life.md", ["Campaign Life"]),
    ("named-men.md", ["Named Men"]),
    ("hired-casters.md", ["Hired Casters"]),
    ("special-rules.md", ["Wanted Men", "Atrocities", "New Stronghold Function"]),
    ("serving-in-anothers-company.md", ["Serving in Another"]),
    ("host-play.md", ["Host Play"]),
    ("XX-appendix-integration.md", ["Appendix A"]),
    ("appendix-a-meet-the-band.md", ["Appendix B"]),
    ("appendix-b-premade-bands.md", ["Appendix C"]),
]


def parse_sections(lines):
    """Split lines into sections keyed by H2 header (or None for preamble)."""
    sections = []
    current_key = None
    current_lines = []

    for line in lines:
        if line.startswith("## "):
            if current_lines or current_key is not None:
                sections.append((current_key, current_lines))
            current_key = line[3:].strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_key, current_lines))

    return sections


def match_section(key, prefixes):
    """Check if a section key matches any of the given prefixes."""
    if key is None:
        return None in prefixes
    return any(p is not None and key.startswith(p) for p in prefixes)


def replace_chapter_refs(text):
    """Replace chapter number references with bolded all-caps name format."""

    # Pattern: **Chapter N — Name.** (Appendix A style headers)
    def repl_header(m):
        num = m.group(1)
        name = CHAPTER_NAMES.get(num)
        if name:
            return f"**{name}** chapter."
        return m.group(0)
    text = re.sub(r'\*\*Chapter\s+(\d+)\s*—\s*[^.]+\.\*\*', repl_header, text)

    # Pattern: "Chapter N" (standalone, not already handled)
    def repl_chapter(m):
        num = m.group(1)
        name = CHAPTER_NAMES.get(num)
        if name:
            return f"the **{name}** chapter"
        return m.group(0)
    text = re.sub(r'Chapter\s+(\d+)', repl_chapter, text)

    # Pattern: "(ChNN)" or "(ChNN optional rules)" -> (the **NAME** chapter) or (the **NAME** chapter, optional rules)
    def repl_ch_paren(m):
        num = m.group(1).lstrip("0")
        extra = m.group(2) or ""
        name = CHAPTER_NAMES.get(num)
        if name:
            if extra.strip():
                return f"(the **{name}** chapter, {extra.strip()})"
            return f"(the **{name}** chapter)"
        return m.group(0)
    text = re.sub(r'\(Ch(\d+)\s*([^)]*)\)', repl_ch_paren, text)

    # Pattern: "from ChNN" or "in ChNN" (without parens)
    def repl_ch_inline(m):
        prefix = m.group(1)
        num = m.group(2).lstrip("0")
        name = CHAPTER_NAMES.get(num)
        if name:
            return f"{prefix}the **{name}** chapter"
        return m.group(0)
    text = re.sub(r'(from |in |see )Ch(\d+)', repl_ch_inline, text)

    return text


def main():
    if not SOURCE.exists():
        print(f"ERROR: {SOURCE} not found", file=sys.stderr)
        sys.exit(1)

    lines = SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)
    sections = parse_sections(lines)

    PARTS_DIR.mkdir(parents=True, exist_ok=True)

    for filename, prefixes in PART_DEFS:
        part_lines = []
        for key, sec_lines in sections:
            if match_section(key, prefixes):
                # Strip leading/trailing blank lines between merged sections
                if part_lines:
                    # Add a blank separator between merged sections
                    while part_lines and part_lines[-1].strip() == "":
                        part_lines.pop()
                    part_lines.append("\n")
                part_lines.extend(sec_lines)

        # Strip trailing whitespace
        content = "".join(part_lines).rstrip() + "\n"

        # Replace chapter references
        content = replace_chapter_refs(content)

        outpath = PARTS_DIR / filename
        outpath.write_text(content, encoding="utf-8")
        line_count = content.count("\n")
        print(f"  {filename}: {line_count} lines")

    print(f"\nWrote {len(PART_DEFS)} part files to {PARTS_DIR}/")


if __name__ == "__main__":
    main()
