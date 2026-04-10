#!/usr/bin/env python3
"""
Split a markdown manuscript into section files using heading-based rules.

Usage:
    python3 scripts/split_markdown_sections.py path/to/file.md output-dir
    python3 scripts/split_markdown_sections.py path/to/file.md output-dir --level 2
    python3 scripts/split_markdown_sections.py path/to/file.md output-dir --pattern '^## '
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(text: str) -> str:
    slug = text.lower()
    slug = slug.replace("&", "and")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "section"


def find_heading_matches(lines: list[str], level: int | None, pattern: str | None) -> list[tuple[int, str]]:
    matches: list[tuple[int, str]] = []
    if pattern:
        regex = re.compile(pattern)
        for idx, line in enumerate(lines):
            if regex.match(line):
                title = re.sub(r"^#+\s+", "", line).strip()
                matches.append((idx, title))
        return matches

    if level is None:
        level = 2
    prefix = "#" * level + " "
    for idx, line in enumerate(lines):
        if line.startswith(prefix):
            title = line[len(prefix):].strip()
            matches.append((idx, title))
    return matches


def split_sections(source: Path, output_dir: Path, level: int | None, pattern: str | None) -> int:
    text = source.read_text(encoding="utf-8")
    lines = text.splitlines()
    matches = find_heading_matches(lines, level, pattern)
    if not matches:
        raise SystemExit("No matching section headings found.")

    output_dir.mkdir(parents=True, exist_ok=True)
    for i, (start, title) in enumerate(matches):
        end = matches[i + 1][0] if i + 1 < len(matches) else len(lines)
        body = "\n".join(lines[start:end]).rstrip() + "\n"
        filename = f"{i + 1:02d}-{slugify(title)}.md"
        (output_dir / filename).write_text(body, encoding="utf-8")
    return len(matches)


def main() -> int:
    parser = argparse.ArgumentParser(description="Split markdown into heading-based section files")
    parser.add_argument("source", help="Source markdown file")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument("--level", type=int, default=2, help="Heading level to split on")
    parser.add_argument("--pattern", help="Regex pattern for heading lines; overrides --level")
    args = parser.parse_args()

    count = split_sections(Path(args.source), Path(args.output_dir), args.level, args.pattern)
    print(f"Wrote {count} section file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
