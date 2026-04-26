#!/usr/bin/env python3
"""Join hard-wrapped prose paragraphs back to single long lines.

Preserves all structural/special Markdown lines exactly:
  - blank lines
  - headings  (# ## ### ####)
  - blockquotes (> ...)
  - list items (- * + / 1. ...)
  - table rows  (| ...)
  - code fences (```)
  - HTML comments (<!--)

Consecutive regular-prose lines between structural markers are joined
with a single space into one line, which removes all MD013-driven
hard-wrap breaks.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


_LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)")


def _is_blank(line: str) -> bool:
    return not line.strip()


def _is_blank_blockquote(line: str) -> bool:
    """A bare '>' or '> ' with no further content."""
    return line.strip() in (">",)


def _is_blockquote(line: str) -> bool:
    return line.lstrip().startswith(">")


def _is_special(line: str) -> bool:
    s = line.strip()
    if not s:
        return True                          # blank
    if s.startswith("#"):
        return True                          # heading
    if _LIST_RE.match(line):
        return True                          # list item
    if s.startswith("|") and s.count("|") >= 2:
        return True                          # table row
    if s.startswith("```"):
        return True                          # code fence toggle
    if s.startswith("<!--"):
        return True                          # HTML comment
    # NOTE: blockquotes are handled separately in unwrap()
    return False


def _strip_bq_prefix(line: str) -> str:
    """Remove the leading '> ' or '>' prefix from a blockquote line."""
    s = line.rstrip("\n")
    if s.startswith("> "):
        return s[2:]
    if s.startswith(">"):
        return s[1:]
    return s


def unwrap(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_code = False
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Toggle code fence state
        if stripped.startswith("```"):
            in_code = not in_code
            out.append(line)
            i += 1
            continue

        # Inside a code block: pass through verbatim
        if in_code:
            out.append(line)
            i += 1
            continue

        # Blank blockquote line (bare ">"): pass through as paragraph separator
        if _is_blank_blockquote(line):
            out.append(line)
            i += 1
            continue

        # Non-blank blockquote line: join consecutive non-blank blockquote lines
        if _is_blockquote(line):
            bq_para: list[str] = []
            while i < len(lines):
                current = lines[i]
                if not _is_blockquote(current) or _is_blank_blockquote(current):
                    break
                bq_para.append(_strip_bq_prefix(current).strip())
                i += 1
            joined = " ".join(p for p in bq_para if p)
            if joined:
                out.append("> " + joined + "\n")
            continue

        # Structural / special line: pass through as-is
        if _is_special(line):
            out.append(line)
            i += 1
            continue

        # Regular prose line: collect all consecutive prose lines
        para: list[str] = []
        while i < len(lines):
            current = lines[i]
            if (
                in_code
                or _is_special(current)
                or _is_blockquote(current)
                or current.strip().startswith("```")
            ):
                break
            para.append(current.rstrip("\n").strip())
            i += 1

        joined = " ".join(p for p in para if p)
        if joined:
            out.append(joined + "\n")
        elif not para:
            # No para lines were collected — advance to avoid infinite loop
            out.append(line)
            i += 1

    result = "".join(out)
    # Normalize to a single trailing newline
    return result.rstrip("\n") + "\n"


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.md> [--dry-run]", file=sys.stderr)
        return 1

    path = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv

    original = path.read_text(encoding="utf-8")
    result = unwrap(original)

    if dry_run:
        sys.stdout.write(result)
        return 0

    path.write_text(result, encoding="utf-8")
    orig_lines = original.count("\n")
    new_lines = result.count("\n")
    print(f"Written → {path}  ({orig_lines} lines → {new_lines} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
