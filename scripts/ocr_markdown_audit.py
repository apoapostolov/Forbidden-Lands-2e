#!/usr/bin/env python3
"""
Audit raw or cleaned OCR markdown for common RPG PDF extraction artifacts.

Usage:
    python scripts/ocr_markdown_audit.py path/to/file.raw.md
    python scripts/ocr_markdown_audit.py path/to/file.raw.md path/to/file.clean.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = {
    "picture_placeholders": re.compile(r"^\*\*==>.*<==\*\*$", re.MULTILINE),
    "picture_text_markers": re.compile(r"Start of picture text|End of picture text", re.IGNORECASE),
    "html_breaks": re.compile(r"<br\s*/?>", re.IGNORECASE),
    "page_number_lines": re.compile(r"^(?:#\s*)?[–—-]?\s*\d{1,3}\s*[–—-]?\s*$", re.MULTILINE),
    "all_caps_lines": re.compile(r"^[A-Z][A-Z\s&,'\-:]{4,}$", re.MULTILINE),
    "markdown_headings": re.compile(r"^#{1,6}\s", re.MULTILINE),
    "pipe_table_lines": re.compile(r"^\|.*\|$", re.MULTILINE),
    "double_blank_runs": re.compile(r"\n{3,}"),
    "spaced_heading_candidates": re.compile(r"^(?:#{1,6}\s+)?(?:[A-Za-z]\s){4,}[A-Za-z]$", re.MULTILINE),
    "dropcap_damage_candidates": re.compile(r"^(?:[a-z]{2,}|[A-Z][a-z]{1,3})\b", re.MULTILINE),
}


def count_lines(text: str, pattern: re.Pattern[str]) -> int:
    return len(pattern.findall(text))


def summarize(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {name: count_lines(text, pattern) for name, pattern in PATTERNS.items()}


def format_report(label: str, counts: dict[str, int]) -> list[str]:
    lines = [f"## {label}", ""]
    for key in sorted(counts):
        lines.append(f"- `{key}`: {counts[key]}")
    lines.append("")
    return lines


def delta_report(raw_counts: dict[str, int], clean_counts: dict[str, int]) -> list[str]:
    lines = ["## Delta", ""]
    for key in sorted(raw_counts):
        delta = clean_counts.get(key, 0) - raw_counts[key]
        lines.append(f"- `{key}`: {raw_counts[key]} -> {clean_counts.get(key, 0)} ({delta:+d})")
    lines.append("")
    return lines


def write_report(raw_path: Path, clean_path: Path | None) -> Path:
    raw_counts = summarize(raw_path)
    report_lines = [
        "# OCR Markdown Audit",
        "",
        f"- Raw: `{raw_path}`",
    ]
    if clean_path:
        report_lines.append(f"- Clean: `{clean_path}`")
    report_lines.append("")
    report_lines.extend(format_report("Raw Artifact Counts", raw_counts))
    if clean_path:
        clean_counts = summarize(clean_path)
        report_lines.extend(format_report("Clean Artifact Counts", clean_counts))
        report_lines.extend(delta_report(raw_counts, clean_counts))

    report_lines.extend(
        [
            "## Interpretation",
            "",
            "- High `picture_placeholders`, `picture_text_markers`, or `html_breaks` means image-text cleanup is still needed.",
            "- High `all_caps_lines` often indicates surviving running headers or flattened labels.",
            "- High `spaced_heading_candidates` suggests decorative heading reconstruction remains incomplete.",
            "- High `double_blank_runs` usually indicates layout noise rather than real manuscript spacing.",
            "- `pipe_table_lines` rising after cleanup is often good if flattened tables were reconstructed.",
            "",
        ]
    )

    report_path = raw_path.with_suffix("").with_suffix(".ocr-report.md")
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    return report_path


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("Usage: python scripts/ocr_markdown_audit.py <raw.md> [clean.md]")
        return 1

    raw_path = Path(sys.argv[1])
    clean_path = Path(sys.argv[2]) if len(sys.argv) == 3 else None

    if not raw_path.exists():
        print(f"Error: raw file not found: {raw_path}")
        return 1
    if clean_path and not clean_path.exists():
        print(f"Error: clean file not found: {clean_path}")
        return 1

    report_path = write_report(raw_path, clean_path)
    print(f"Wrote OCR audit report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
