#!/usr/bin/env python3
"""Merge 02-bestiary-merged.md into 02-bestiary.md.

Rules:
  - Monster/creature entries inserted alphabetically among existing monsters.
  - A new ## Humanoid Bands chapter is added after all monster entries,
    before ## Legends.
  - Legend blocks merged alphabetically into the existing ## Legends section.
  - ## Encounters section preserved unchanged.
  - Output overwrites 02-bestiary.md; original backed up as .bak.
"""

from pathlib import Path

BASE     = Path("03-book-of-beasts")
BESTIARY = BASE / "02-bestiary.md"
MERGED   = BASE / "02-bestiary-merged.md"

# ── helpers ────────────────────────────────────────────────────────────────────

def sort_key(name: str) -> str:
    """Alphabetical sort key: strip leading 'The ', normalise punctuation."""
    k = name.strip()
    if k.lower().startswith("the "):
        k = k[4:]
    return k.lower().replace("-", " ").replace("'", "").replace(".", "")


def extract_blocks(lines: list) -> list:
    """Split a list of lines into (name, block_lines) pairs on ### headings.

    Lines before the first ### heading are returned as ("__pre__", lines).
    Each block_lines list INCLUDES the leading ### line.
    """
    blocks = []
    cur_name = None
    cur_lines = []

    for line in lines:
        if line.startswith("### "):
            if cur_lines:
                blocks.append((cur_name or "__pre__", cur_lines))
            cur_name = line[4:].strip()
            cur_lines = [line]
        else:
            cur_lines.append(line)

    if cur_lines:
        blocks.append((cur_name or "__pre__", cur_lines))

    return blocks


def clean_block(lines: list) -> list:
    """Strip trailing --- separators and normalise to exactly one blank line."""
    lines = list(lines)  # copy

    # Strip trailing blank lines
    while lines and lines[-1].strip() == "":
        lines.pop()

    # Strip trailing --- separator if present
    if lines and lines[-1].strip() == "---":
        lines.pop()

    # Strip blank lines again
    while lines and lines[-1].strip() == "":
        lines.pop()

    # Add exactly one trailing blank line
    lines.append("\n")
    return lines


def good_blocks(lines: list) -> list:
    """extract_blocks + filter __pre__ + clean each block."""
    return [
        (name, clean_block(blk))
        for name, blk in extract_blocks(lines)
        if name != "__pre__"
    ]


# ── parse bestiary.md ──────────────────────────────────────────────────────────

def parse_bestiary(path: Path):
    """Return (front_matter, monster_blocks, legend_blocks, legends_hdr, encounters).

    front_matter   : list[str]        lines before ### Amphibian
    monster_blocks : list[(str, [str])]
    legend_blocks  : list[(str, [str])]
    legends_hdr    : list[str]        ["## Legends\n"]
    encounters     : list[str]        everything from ## Encounters onward
    """
    raw = path.read_text(encoding="utf-8").splitlines(keepends=True)

    legends_i = encounters_i = first_monster_i = None
    for i, line in enumerate(raw):
        s = line.strip()
        if s == "## Legends"    and legends_i    is None: legends_i    = i
        if s == "## Encounters" and encounters_i is None: encounters_i = i
        if s == "### Amphibian" and first_monster_i is None: first_monster_i = i

    if any(x is None for x in [legends_i, encounters_i, first_monster_i]):
        raise ValueError(f"Section boundaries not found in {path}")

    front_matter   = raw[:first_monster_i]
    monster_raw    = raw[first_monster_i:legends_i]
    legends_raw    = raw[legends_i:encounters_i]
    encounters_raw = raw[encounters_i:]

    # Parse monster blocks; attach known non-monster sub-headings to predecessor
    NON_MONSTER = {"No Monster Attacks"}
    raw_blocks = extract_blocks(monster_raw)
    monster_blocks = []
    for name, blk in raw_blocks:
        if name in NON_MONSTER and monster_blocks:
            # Reattach to the preceding monster's block
            prev_name, prev_blk = monster_blocks[-1]
            monster_blocks[-1] = (prev_name, prev_blk + blk)
        elif name not in ("__pre__",):
            monster_blocks.append((name, clean_block(blk)))

    # Parse legend blocks (skip the "## Legends\n" header line itself)
    legend_blocks = good_blocks(legends_raw[1:])

    return front_matter, monster_blocks, legend_blocks, legends_raw[:1], encounters_raw


# ── parse bestiary-merged.md ───────────────────────────────────────────────────

def parse_merged(path: Path):
    """Return (monster_blocks, humanoid_blocks, legend_blocks)."""
    raw = path.read_text(encoding="utf-8").splitlines(keepends=True)

    monsters_i = creatures_i = humanoids_i = legends_i = None
    for i, line in enumerate(raw):
        s = line.strip()
        if s == "## Monsters of the Forbidden Lands"  and monsters_i  is None: monsters_i  = i
        if s == "## Creatures of the Forbidden Lands" and creatures_i is None: creatures_i = i
        if s == "## Humanoid Bands"                   and humanoids_i is None: humanoids_i = i
        if s == "## Legends"                          and legends_i   is None: legends_i   = i

    if any(x is None for x in [monsters_i, creatures_i, humanoids_i, legends_i]):
        raise ValueError(f"Section boundaries not found in {path}")

    def section(start, end):
        return good_blocks(raw[start + 1 : end])

    monster_blocks  = section(monsters_i, creatures_i) + section(creatures_i, humanoids_i)
    humanoid_blocks = section(humanoids_i, legends_i)
    legend_blocks   = section(legends_i, len(raw))

    return monster_blocks, humanoid_blocks, legend_blocks


# ── merge and write ────────────────────────────────────────────────────────────

def merge():
    print(f"Reading {BESTIARY} …")
    front_matter, exist_monsters, exist_legends, legends_hdr, encounters = parse_bestiary(BESTIARY)

    print(f"Reading {MERGED} …")
    new_monsters, humanoids, new_legends = parse_merged(MERGED)

    # Merge and sort
    all_monsters = sorted(exist_monsters + new_monsters, key=lambda x: sort_key(x[0]))
    humanoids    = sorted(humanoids,                     key=lambda x: sort_key(x[0]))
    all_legends  = sorted(exist_legends  + new_legends,  key=lambda x: sort_key(x[0]))

    # Build output
    out = []

    # 1. Unchanged front matter (intro, D66 table)
    out.extend(front_matter)

    # 2. All monster/creature entries, alphabetical
    for _, blk in all_monsters:
        out.extend(blk)

    # 3. New Humanoid Bands chapter
    out.append("## Humanoid Bands\n")
    out.append("\n")
    for _, blk in humanoids:
        out.extend(blk)

    # 4. Legends section
    out.extend(legends_hdr)   # "## Legends\n"
    out.append("\n")
    for _, blk in all_legends:
        out.extend(blk)

    # 5. Encounters section (completely unchanged)
    out.extend(encounters)

    # Backup and write
    bak = BESTIARY.with_suffix(".md.bak")
    bak.write_bytes(BESTIARY.read_bytes())
    print(f"Backed up  → {bak}")

    BESTIARY.write_text("".join(out), encoding="utf-8")
    print(f"Written    → {BESTIARY}")

    # Summary
    print(f"\n  Monsters : {len(exist_monsters):3d} existing + {len(new_monsters):3d} new"
          f" = {len(all_monsters):3d} total (sorted alphabetically)")
    print(f"  Humanoids: {len(humanoids):3d} new entries in new chapter")
    print(f"  Legends  : {len(exist_legends):3d} existing + {len(new_legends):3d} new"
          f" = {len(all_legends):3d} total (sorted alphabetically)")


if __name__ == "__main__":
    import sys
    import os
    # Allow running from repo root or from scripts/
    if not BESTIARY.exists():
        os.chdir(Path(__file__).parent.parent)
    if not BESTIARY.exists():
        print(f"ERROR: {BESTIARY} not found. Run from repo root.", file=sys.stderr)
        sys.exit(1)
    merge()
