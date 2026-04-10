#!/usr/bin/env python3
"""
Repair a narrow class of flattened one-line OCR tables in markdown files.

Usage:
    python3 scripts/repair_flattened_tables.py path/to/file.md
    python3 scripts/repair_flattened_tables.py path/to/file.md --write
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROLL_TOKEN_RE = re.compile(r"\b(?:\dD\d+|D\d+|(?:\d{1,2}|[<>]=?\d+)(?:-\d{1,2})?)\b")
HEADER_START_RE = re.compile(r"^(?:\*\*)?(D\d+|3D6|2D6|D6\+)(?:\b|\s)", re.IGNORECASE)


def normalize_header_tokens(prefix: str) -> list[str]:
    tokens = prefix.strip().split()
    return [token.strip("*") for token in tokens if token.strip("*")]


def split_rows(rest: str) -> list[tuple[str, str]]:
    matches = list(ROLL_TOKEN_RE.finditer(rest))
    if len(matches) < 2:
        return []
    rows: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(rest)
        roll = match.group(0)
        payload = rest[match.end():end].strip()
        if not payload:
            return []
        rows.append((roll, payload))
    return rows


def line_to_table(line: str) -> list[str] | None:
    stripped = line.strip()
    if stripped.startswith("|") or not HEADER_START_RE.match(stripped):
        return None

    first_roll = ROLL_TOKEN_RE.search(stripped)
    if not first_roll:
        return None

    prefix = stripped[:first_roll.start()].strip()
    rest = stripped[first_roll.start():].strip()
    header_tokens = normalize_header_tokens(prefix)
    if len(header_tokens) < 2:
        return None

    rows = split_rows(rest)
    if len(rows) < 2:
        return None

    roll_header = header_tokens[0]
    value_header = " ".join(header_tokens[1:])
    out = [
        f"| {roll_header} | {value_header} |",
        "| --- | --- |",
    ]
    for roll, payload in rows:
        out.append(f"| {roll} | {payload} |")
    return out


def process_text(text: str) -> tuple[str, int]:
    changed = 0
    out_lines: list[str] = []
    for line in text.splitlines():
        table = line_to_table(line)
        if table:
            out_lines.extend(table)
            changed += 1
        else:
            out_lines.append(line)
    return "\n".join(out_lines) + "\n", changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair simple flattened OCR tables")
    parser.add_argument("file", help="Markdown file to inspect")
    parser.add_argument("--write", action="store_true", help="Write changes back to the file")
    args = parser.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding="utf-8")
    fixed, changed = process_text(text)

    print(f"Detected and repaired {changed} flattened table line(s).")
    if args.write and changed:
        path.write_text(fixed, encoding="utf-8")
        print(f"Wrote updated file: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
