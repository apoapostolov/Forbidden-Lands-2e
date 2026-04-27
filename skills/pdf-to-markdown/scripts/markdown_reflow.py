#!/usr/bin/env python3
"""Reflow or unwrap Markdown paragraphs while preserving tables and lists.

Supports two modes:
- wrap:   break prose to a target width
- unwrap: join hard-wrapped prose into single lines

The script preserves tables, code fences, HTML comments, headings, and list
structure. It is intended for OCR cleanup and post-extraction normalization.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from textwrap import TextWrapper

try:
    from repair_flattened_tables import repair_flattened_tables_text
except ModuleNotFoundError:  # pragma: no cover - allow running from other roots
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from repair_flattened_tables import repair_flattened_tables_text

__version__ = "1.0.0"

LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)")
BLOCKQUOTE_RE = re.compile(r"^\s*>\s?")
TABLE_RE = re.compile(r"^\s*\|.*\|\s*$")


def is_blank(line: str) -> bool:
    return not line.strip()


def is_code_fence(line: str) -> bool:
    return line.strip().startswith("```")


def is_html_comment(line: str) -> bool:
    return line.strip().startswith("<!--")


def is_heading(line: str) -> bool:
    return line.lstrip().startswith("#")


def is_table_line(line: str) -> bool:
    return bool(TABLE_RE.match(line)) and line.count("|") >= 2


def is_list_line(line: str) -> bool:
    return bool(LIST_RE.match(line))


def is_blockquote_line(line: str) -> bool:
    return bool(BLOCKQUOTE_RE.match(line))


def is_special_line(line: str) -> bool:
    return (
        is_blank(line)
        or is_code_fence(line)
        or is_html_comment(line)
        or is_heading(line)
        or is_table_line(line)
    )


def split_blocks(lines: list[str]) -> list[tuple[str, list[str]]]:
    """Split lines into structural blocks the reflow step should respect."""
    blocks: list[tuple[str, list[str]]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip("\n")

        if is_blank(stripped):
            blocks.append(("blank", [line]))
            i += 1
            continue

        if is_code_fence(stripped):
            block = [line]
            i += 1
            while i < len(lines):
                block.append(lines[i])
                if is_code_fence(lines[i]):
                    i += 1
                    break
                i += 1
            blocks.append(("code", block))
            continue

        if is_html_comment(stripped):
            blocks.append(("comment", [line]))
            i += 1
            continue

        if is_table_line(stripped):
            block = [line]
            i += 1
            while i < len(lines) and is_table_line(lines[i]):
                block.append(lines[i])
                i += 1
            blocks.append(("table", block))
            continue

        if is_list_line(stripped):
            block = [line]
            i += 1
            while i < len(lines):
                nxt = lines[i]
                nxt_stripped = nxt.rstrip("\n")
                if (
                    is_blank(nxt_stripped)
                    or is_code_fence(nxt_stripped)
                    or is_html_comment(nxt_stripped)
                    or is_heading(nxt_stripped)
                    or is_table_line(nxt_stripped)
                    or is_list_line(nxt_stripped)
                    or is_blockquote_line(nxt_stripped)
                ):
                    break
                if not nxt_stripped.startswith(" "):
                    break
                block.append(nxt)
                i += 1
            blocks.append(("list", block))
            continue

        if is_blockquote_line(stripped):
            block = [line]
            i += 1
            while i < len(lines):
                nxt = lines[i]
                nxt_stripped = nxt.rstrip("\n")
                if (
                    is_blank(nxt_stripped)
                    or is_code_fence(nxt_stripped)
                    or is_html_comment(nxt_stripped)
                    or is_heading(nxt_stripped)
                    or is_table_line(nxt_stripped)
                    or is_list_line(nxt_stripped)
                    or not is_blockquote_line(nxt_stripped)
                ):
                    break
                block.append(nxt)
                i += 1
            blocks.append(("blockquote", block))
            continue

        block = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            nxt_stripped = nxt.rstrip("\n")
            if (
                is_blank(nxt_stripped)
                or is_code_fence(nxt_stripped)
                or is_html_comment(nxt_stripped)
                or is_heading(nxt_stripped)
                or is_table_line(nxt_stripped)
                or is_list_line(nxt_stripped)
                or is_blockquote_line(nxt_stripped)
            ):
                break
            block.append(nxt)
            i += 1
        blocks.append(("paragraph", block))
    return blocks


def unwrap_block(kind: str, block: list[str]) -> list[str]:
    if kind in {"blank", "code", "comment", "table"}:
        return block

    if kind == "blockquote":
        parts: list[str] = []
        for line in block:
            s = line.rstrip("\n")
            s = re.sub(r"^\s*>\s?", "", s).strip()
            if s:
                parts.append(s)
        joined = " ".join(parts)
        return [f"> {joined}\n"] if joined else ["\n"]

    if kind == "list":
        first = block[0].rstrip("\n")
        m = re.match(r"^(\s*(?:[-*+]\s+|\d+\.\s+))(.*)$", first)
        if not m:
            return block
        prefix = m.group(1)
        parts = [m.group(2).strip()] if m.group(2).strip() else []
        for line in block[1:]:
            s = line.rstrip("\n").strip()
            if s:
                parts.append(s)
        body = " ".join(parts)
        return [f"{prefix}{body}\n"] if body else [f"{prefix.rstrip()}\n"]

    if kind == "paragraph":
        parts = [line.rstrip("\n").strip() for line in block if line.strip()]
        joined = " ".join(parts)
        return [joined + "\n"] if joined else ["\n"]

    return block


def wrap_block(kind: str, block: list[str], width: int) -> list[str]:
    if kind in {"blank", "code", "comment", "table"}:
        return block

    if kind == "blockquote":
        parts: list[str] = []
        for line in block:
            s = re.sub(r"^\s*>\s?", "", line.rstrip("\n")).strip()
            if s:
                parts.append(s)
        text = " ".join(parts)
        if not text:
            return ["\n"]
        wrapper = TextWrapper(
            width=width,
            initial_indent="> ",
            subsequent_indent="> ",
            break_long_words=False,
            break_on_hyphens=False,
            replace_whitespace=True,
            drop_whitespace=True,
        )
        return [line + "\n" for line in wrapper.wrap(text)]

    if kind == "list":
        first = block[0].rstrip("\n")
        m = re.match(r"^(\s*(?:[-*+]\s+|\d+\.\s+))(.*)$", first)
        if not m:
            return block
        prefix = m.group(1)
        parts = [m.group(2).strip()] if m.group(2).strip() else []
        for line in block[1:]:
            s = line.rstrip("\n").strip()
            if s:
                parts.append(s)
        body = " ".join(parts)
        if not body:
            return [f"{prefix.rstrip()}\n"]
        wrapper = TextWrapper(
            width=width,
            initial_indent=prefix,
            subsequent_indent=" " * len(prefix),
            break_long_words=False,
            break_on_hyphens=False,
            replace_whitespace=True,
            drop_whitespace=True,
        )
        return [line + "\n" for line in wrapper.wrap(body)]

    if kind == "paragraph":
        text = " ".join(line.rstrip("\n").strip() for line in block if line.strip())
        if not text:
            return ["\n"]
        wrapper = TextWrapper(
            width=width,
            initial_indent="",
            subsequent_indent="",
            break_long_words=False,
            break_on_hyphens=False,
            replace_whitespace=True,
            drop_whitespace=True,
        )
        return [line + "\n" for line in wrapper.wrap(text)]

    return block


def process_text(text: str, mode: str, width: int = 75, start_line: int = 0) -> str:
    """Process Markdown text from the given 0-based line index onward."""
    fixed_text, _ = repair_flattened_tables_text(text)
    lines = fixed_text.splitlines(keepends=True)

    before = lines[:start_line]
    after = lines[start_line:]
    blocks = split_blocks(after)

    processed: list[str] = []
    for kind, block in blocks:
        if mode == "unwrap":
            processed.extend(unwrap_block(kind, block))
        elif mode == "wrap":
            processed.extend(wrap_block(kind, block, width=width))
        else:
            raise ValueError(f"Unknown mode: {mode}")

    result = "".join(before + processed)
    return result.rstrip("\n") + "\n"


def process_file(input_path: str, mode: str, start_line: int = 0, width: int = 75) -> str:
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
    return process_text(text, mode=mode, width=width, start_line=start_line)


def main() -> int:
    parser = argparse.ArgumentParser(description="Wrap or unwrap Markdown prose without touching tables.")
    parser.add_argument("file", help="Markdown file to process")
    parser.add_argument("--mode", choices=("wrap", "unwrap"), default="unwrap", help="Processing mode")
    parser.add_argument("--start-line", type=int, default=1, help="1-based line number to start processing from")
    parser.add_argument("--width", type=int, default=75, help="Target wrap width when mode=wrap")
    parser.add_argument("--write", action="store_true", help="Write changes back to the file")
    parser.add_argument("--version", action="version", version=__version__, help="Show the script version and exit")
    args = parser.parse_args()

    path = Path(args.file)
    zero_based_start = max(0, args.start_line - 1)
    result = process_file(str(path), mode=args.mode, start_line=zero_based_start, width=args.width)

    if args.write:
        path.write_text(result, encoding="utf-8")
        print(f"Written → {path}")
    else:
        sys.stdout.write(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
