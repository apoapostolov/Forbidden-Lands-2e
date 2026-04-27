#!/usr/bin/env python3
"""Analyze Book of Beasts entry-size benchmarks.

This script measures word-count ranges for the modern bestiary elements used
when drafting new monsters. It focuses on the current high-quality corpus in
`03-book-of-beasts/02-bestiary.md` and `03-book-of-beasts/04-legends.md`.

Outputs:
- JSON written to `scripts/analysis/book03_bestiary_size_stats.json`
- Markdown summary written to `scripts/analysis/book03_bestiary_size_stats.md`
- Console summary for quick review
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from statistics import mean, quantiles
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
BESTIARY_PATH = ROOT / "03-book-of-beasts" / "02-bestiary.md"
LEGENDS_PATH = ROOT / "03-book-of-beasts" / "04-legends.md"
OUTPUT_JSON = ROOT / "scripts" / "analysis" / "book03_bestiary_size_stats.json"
OUTPUT_MD = ROOT / "scripts" / "analysis" / "book03_bestiary_size_stats.md"

WORD_RE = re.compile(r"[A-Za-z0-9À-ÖØ-öø-ÿ]+(?:['’-][A-Za-z0-9À-ÖØ-öø-ÿ]+)*")
H3_RE = re.compile(r"^###\s+(.*)$", re.MULTILINE)
H4_ENCOUNTER_RE = re.compile(r"^####\s+Random Encounter:\s+(.*)$", re.MULTILINE)
HEADING_RE = re.compile(r"^#{3,4}\s+", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\|.*\|\s*$")
BULLET_RE = re.compile(r"^-\s+\*\*Terrain Types:\*\*")


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def normalize_text(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    text = text.replace("|", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def quartiles(values: list[int]) -> tuple[float, float]:
    if len(values) == 1:
        return float(values[0]), float(values[0])
    q1, _, q3 = quantiles(values, n=4, method="inclusive")
    return float(q1), float(q3)


def summarize(values: list[int]) -> dict[str, float | int]:
    vals = sorted(values)
    q1, q3 = quartiles(vals)
    return {
        "sample_size": len(vals),
        "minimum": min(vals),
        "maximum": max(vals),
        "average": mean(vals),
        "bottom_25_percentile": q1,
        "top_75_percentile": q3,
        "recommended_floor": math.ceil(q1),
        "recommended_target": round(mean(vals)),
        "healthy_upper_band": math.ceil(q3),
    }


def split_h3_sections(text: str) -> list[tuple[str, str]]:
    matches = list(H3_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        title = match.group(1).strip()
        body = text[start:end].strip()
        sections.append((title, body))
    return sections


def first_blockquote(section: str) -> str:
    lines = section.splitlines()
    quote_lines: list[str] = []
    started = False
    for line in lines:
        if line.startswith(">"):
            started = True
            quote_lines.append(re.sub(r"^>\s?", "", line).strip())
            continue
        if started:
            break
        if line.strip():
            break
    return normalize_text(" ".join(line for line in quote_lines if line))


def is_typical_vignette(text: str) -> bool:
    if not text:
        return False
    if count_words(text) > 35:
        return False
    sentence_count = len(re.findall(r"[.!?](?:\s|$)", text))
    return sentence_count == 1


def extract_section_between(section: str, start_heading: str, end_heading: str) -> str:
    start = section.find(start_heading)
    end = section.find(end_heading)
    if start == -1 or end == -1 or end <= start:
        return ""
    return section[start + len(start_heading):end].strip()


def extract_attacks_table_words(section: str) -> int | None:
    start = section.find("#### Monster Attacks")
    if start == -1:
        return None
    after = section[start:].splitlines()[1:]
    table_lines: list[str] = []
    for line in after:
        if HEADING_RE.match(line):
            break
        if TABLE_ROW_RE.match(line):
            table_lines.append(line)
    cleaned_rows = []
    for line in table_lines:
        stripped = line.strip()
        if re.fullmatch(r"\|\s*[-: ]+\|.*", stripped):
            continue
        cleaned_rows.append(stripped)
    if len(cleaned_rows) <= 1:
        return None
    return count_words(normalize_text(" ".join(cleaned_rows)))


def extract_description_words(section: str) -> int | None:
    attacks_index = section.find("#### Monster Attacks")
    if attacks_index == -1:
        return None
    lore_index = section.find("#### Lore Roll")
    if lore_index == -1 or lore_index <= attacks_index:
        return None
    after_attacks = section[attacks_index:lore_index].splitlines()
    collecting = False
    body_lines: list[str] = []
    for line in after_attacks:
        if collecting and line.startswith("####"):
            break
        if collecting:
            if TABLE_ROW_RE.match(line) or line.startswith("| ") or line.startswith("|---"):
                continue
            if not line.strip():
                body_lines.append("")
                continue
            body_lines.append(line.strip())
        if line.strip().startswith("|"):
            collecting = True
    # fallback: collect prose after table rows
    if not body_lines:
        in_table = False
        for line in after_attacks[1:]:
            if TABLE_ROW_RE.match(line):
                in_table = True
                continue
            if in_table and not line.strip():
                continue
            if in_table and line.strip() and not TABLE_ROW_RE.match(line):
                body_lines.append(line.strip())
    text = normalize_text(" ".join(body_lines))
    return count_words(text) if text else None


def extract_lore_rows(section: str) -> list[tuple[str, int]]:
    lore_index = section.find("#### Lore Roll")
    if lore_index == -1:
        return []
    after = section[lore_index:].splitlines()[1:]
    rows: list[tuple[str, int]] = []
    for line in after:
        if HEADING_RE.match(line):
            break
        if not TABLE_ROW_RE.match(line):
            continue
        stripped = line.strip()
        if re.fullmatch(r"\|\s*[-: ]+\|.*", stripped):
            continue
        cells = [normalize_text(cell) for cell in stripped.strip("|").split("|")]
        if not cells:
            continue
        if cells[0].upper() == "D6":
            continue
        data_cells = [cell for cell in cells[1:] if cell]
        if not data_cells:
            continue
        text = " ".join(data_cells)
        row_id = cells[0].strip()
        rows.append((row_id, count_words(text)))
    return rows


def extract_encounter_word_counts(section: str) -> list[dict[str, int | str]]:
    counts: list[dict[str, int | str]] = []
    matches = list(H4_ENCOUNTER_RE.finditer(section))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        body = section[start:end].strip()
        lines = body.splitlines()
        epigraph_lines: list[str] = []
        prose_lines: list[str] = []
        in_epigraph = True
        for line in lines:
            if BULLET_RE.match(line):
                break
            if in_epigraph and line.startswith(">"):
                epigraph_lines.append(re.sub(r"^>\s?", "", line).strip())
                continue
            if in_epigraph and not line.strip():
                continue
            in_epigraph = False
            prose_lines.append(line.strip())
        epigraph_text = normalize_text(" ".join(line for line in epigraph_lines if line))
        prose_text = normalize_text(" ".join(line for line in prose_lines if line))
        total_text = normalize_text(" ".join(part for part in [epigraph_text, prose_text] if part))
        counts.append(
            {
                "title": match.group(1).strip(),
                "epigraph_words": count_words(epigraph_text),
                "body_words": count_words(prose_text),
                "total_words": count_words(total_text),
            }
        )
    return counts


def analyze_bestiary() -> dict:
    text = BESTIARY_PATH.read_text(encoding="utf-8")
    sections = split_h3_sections(text)

    vignette_words: list[int] = []
    attack_table_words: list[int] = []
    description_words: list[int] = []
    lore_entry_words: list[int] = []
    lore_by_row: dict[str, list[int]] = {"1": [], "2": [], "3": []}
    encounter_total_words: list[int] = []
    encounter_body_words: list[int] = []
    encounter_epigraph_words: list[int] = []
    eligible_titles: list[str] = []

    for title, section in sections:
        if not title or title in {"Bestiary", "Using This Book"}:
            continue

        vignette = first_blockquote(section)
        if is_typical_vignette(vignette):
            vignette_words.append(count_words(vignette))

        attacks = extract_attacks_table_words(section)
        description = extract_description_words(section)
        lore_rows = extract_lore_rows(section)
        encounters = extract_encounter_word_counts(section)

        if attacks is not None and description is not None and lore_rows and encounters:
            eligible_titles.append(title)
            attack_table_words.append(attacks)
            description_words.append(description)
            for row_id, row_words in lore_rows:
                lore_entry_words.append(row_words)
                if row_id in lore_by_row:
                    lore_by_row[row_id].append(row_words)
            for encounter in encounters:
                encounter_total_words.append(int(encounter["total_words"]))
                encounter_body_words.append(int(encounter["body_words"]))
                encounter_epigraph_words.append(int(encounter["epigraph_words"]))

    if not all(
        [
            vignette_words,
            attack_table_words,
            description_words,
            lore_entry_words,
            encounter_total_words,
        ]
    ):
        raise RuntimeError("One or more measurement buckets came back empty.")

    return {
        "source": str(BESTIARY_PATH.relative_to(ROOT)),
        "eligible_monster_entries": eligible_titles,
        "measurements": {
            "typical_vignette": summarize(vignette_words),
            "monster_attacks_table": summarize(attack_table_words),
            "monster_description": summarize(description_words),
            "lore_roll_entry": summarize(lore_entry_words),
            "lore_roll_row_1": summarize(lore_by_row["1"]),
            "lore_roll_row_2": summarize(lore_by_row["2"]),
            "lore_roll_row_3": summarize(lore_by_row["3"]),
            "random_encounter_total": summarize(encounter_total_words),
            "random_encounter_body": summarize(encounter_body_words),
            "random_encounter_epigraph": summarize(encounter_epigraph_words),
        },
        "vignette_filter": {
            "max_words": 35,
            "required_sentence_count": 1,
            "reason": "Filters out legacy opening lore blocks so vignette stats represent the current short-form entry standard.",
        },
    }


def analyze_legends() -> dict:
    text = LEGENDS_PATH.read_text(encoding="utf-8")
    sections = split_h3_sections(text)
    legend_words: list[int] = []
    titles: list[str] = []

    for title, section in sections:
        if not title or title == "Legends":
            continue
        lines = []
        for line in section.splitlines():
            if line.startswith(">"):
                lines.append(re.sub(r"^>\s?", "", line).strip())
        legend_text = normalize_text(" ".join(line for line in lines if line))
        if legend_text:
            titles.append(title)
            legend_words.append(count_words(legend_text))

    if not legend_words:
        raise RuntimeError("Legend measurements came back empty.")

    return {
        "source": str(LEGENDS_PATH.relative_to(ROOT)),
        "eligible_legends": titles,
        "measurements": {"monster_legend": summarize(legend_words)},
    }


def build_markdown_report(payload: dict) -> str:
    bestiary = payload["bestiary"]
    legends = payload["legends"]
    rows = []

    def add_row(label: str, data: dict) -> None:
        rows.append(
            "| {label} | {sample} | {avg:.1f} | {q1:.1f} | {q3:.1f} | {floor} | {target} | {upper} |".format(
                label=label,
                sample=data["sample_size"],
                avg=data["average"],
                q1=data["bottom_25_percentile"],
                q3=data["top_75_percentile"],
                floor=data["recommended_floor"],
                target=data["recommended_target"],
                upper=data["healthy_upper_band"],
            )
        )

    add_row("Typical vignette", bestiary["measurements"]["typical_vignette"])
    add_row("Monster description", bestiary["measurements"]["monster_description"])
    add_row("Monster attacks table", bestiary["measurements"]["monster_attacks_table"])
    add_row("Lore Roll entry", bestiary["measurements"]["lore_roll_entry"])
    add_row("Lore Roll row 2", bestiary["measurements"]["lore_roll_row_2"])
    add_row("Lore Roll row 3", bestiary["measurements"]["lore_roll_row_3"])
    add_row("Random encounter total", bestiary["measurements"]["random_encounter_total"])
    add_row("Random encounter body", bestiary["measurements"]["random_encounter_body"])
    add_row("Monster legend", legends["measurements"]["monster_legend"])

    return "\n".join(
        [
            "# Book 03 Bestiary Size Stats",
            "",
            "Measured from the current high-quality bestiary corpus in `03-book-of-beasts/02-bestiary.md` and legends in `03-book-of-beasts/04-legends.md`.",
            "",
            "- **Recommended floor** = hard minimum for AI drafting (25th percentile rounded up)",
            "- **Recommended target** = average rounded to the nearest word",
            "- **Healthy upper band** = 75th percentile rounded up",
            "",
            "| Element | Sample | Average | 25th percentile | 75th percentile | Recommended floor | Recommended target | Healthy upper band |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
            *rows,
            "",
            "## Notes",
            "",
            "- Typical vignette measurements exclude legacy long-form opening lore blocks by requiring one sentence and no more than 35 words.",
            "- Random encounter totals include epigraph plus body text, but exclude the `Terrain Types` line.",
            "- Lore Roll entry counts are measured per table row result, not for the whole table at once.",
        ]
    )


def main() -> None:
    payload = {
        "bestiary": analyze_bestiary(),
        "legends": analyze_legends(),
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    report = build_markdown_report(payload)
    OUTPUT_MD.write_text(report + "\n", encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
