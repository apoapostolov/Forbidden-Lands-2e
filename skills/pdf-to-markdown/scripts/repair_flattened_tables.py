#!/usr/bin/env python3
"""Repair flattened OCR tables in markdown files.

This is a thin compatibility wrapper around the shared generic repair helper in
`scripts/pdf_to_markdown.py` so the table fixer stays in sync with the main
PDF-to-Markdown pipeline.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from pdf_to_markdown import repair_flattened_tables_text


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair flattened OCR tables")
    parser.add_argument("file", help="Markdown file to inspect")
    parser.add_argument("--write", action="store_true", help="Write changes back to the file")
    args = parser.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding="utf-8")
    fixed, changed = repair_flattened_tables_text(text)

    print(f"Detected and repaired {changed} flattened table line(s).")
    if args.write and changed:
        path.write_text(fixed, encoding="utf-8")
        print(f"Wrote updated file: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
