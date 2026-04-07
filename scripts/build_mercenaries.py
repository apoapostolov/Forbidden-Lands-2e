#!/usr/bin/env python3
"""Build the Mercenaries chapter from its constituent parts.

Run from repo root:
    python3 scripts/build_mercenaries.py

Concatenates corebook/mercenaries/*.md in the defined order
and writes the result to corebook/mercenaries-of-forbidden-lands.md
"""

import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
PARTS_DIR = REPO / "corebook" / "mercenaries"
OUTPUT = REPO / "corebook" / "12-mercenaries-of-forbidden-lands.md"

PARTS = [
    "01-introduction.md",
    "02-recruitment-and-pay.md",
    "03-extortion-and-tribute.md",
    "04-contracts-and-bounties.md",
    "05-campaign-life.md",
    "06-named-men.md",
    "07-hired-casters.md",
    "08-special-rules.md",
    "09-serving-in-anothers-company.md",
    "10-host-play.md",
    "11-appendix-a-integration.md",
    "12-appendix-b-meet-the-band.md",
    "13-appendix-c-premade-bands.md",
]


def build():
    sections = []
    for part in PARTS:
        path = PARTS_DIR / part
        if not path.exists():
            print(f"ERROR: missing part file {path}", file=sys.stderr)
            sys.exit(1)
        text = path.read_text(encoding="utf-8").rstrip("\n")
        sections.append(text)

    merged = "\n\n".join(sections) + "\n"
    OUTPUT.write_text(merged, encoding="utf-8")

    total_lines = merged.count("\n")
    print(f"Built {OUTPUT.name} ({total_lines} lines) from {len(PARTS)} parts")


if __name__ == "__main__":
    build()
