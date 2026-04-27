"""Quick debug: run each pass independently and report line counts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pdf_to_markdown import (
    pass1_noise_removal,
    pass2_running_headers,
    pass3_spaced_headings,
    pass4_picture_blocks,
    pass5_heading_hierarchy,
    pass6_sidebars,
    pass7_paragraph_joining,
    pass8_table_br,
    pass9_whitespace,
    pass10_loose_lists,
    pass11_dropcap_repair,
    pass12_flattened_tables,
)

raw = Path(sys.argv[1])
lines = raw.read_text(encoding="utf-8").splitlines(keepends=True)
print(f"Raw:   {len(lines)} lines  {sum(len(l) for l in lines):,} chars")

stages = [
    ("Pass 1 noise",    pass1_noise_removal),
    ("Pass 2 headers",  pass2_running_headers),
    ("Pass 3 spaced",   pass3_spaced_headings),
    ("Pass 4 pictures", pass4_picture_blocks),
    ("Pass 5 hierarchy",pass5_heading_hierarchy),
    ("Pass 6 sidebars", pass6_sidebars),
    ("Pass 7 joining",  pass7_paragraph_joining),
    ("Pass 8 table br", pass8_table_br),
    ("Pass 9 flattened tables", pass12_flattened_tables),
    ("Pass 10 whitespace", pass9_whitespace),
    ("Pass 11 loose lists", pass10_loose_lists),
    ("Pass 12 dropcaps", pass11_dropcap_repair),
]

for name, fn in stages:
    prev = len(lines)
    lines = fn(lines)
    chars = sum(len(l) for l in lines)
    delta = len(lines) - prev
    print(f"{name:<20}  {len(lines):5} lines  {chars:>10,} chars  ({delta:+d})")
