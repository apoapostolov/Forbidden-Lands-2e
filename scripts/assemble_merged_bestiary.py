#!/usr/bin/env python3
"""
Assemble 02-bestiary-merged.md from 02A, 02B, and the merge instruction file.

Keeps all entries except: Crab Spider, Green Slime, Grave Servitor, Black Digester.
Replaces draft RESOURCES blocks with uplifted versions from the merge file.
Adds variant openers for Air Spirit and Earth Spirit.
Humanoid bands get a gear-loot line instead of a RESOURCES block.
"""

import re
import sys

BASE = '/home/apoapostolov/git-public/Forbidden-Lands-2e/03-book-of-beasts'

with open(f'{BASE}/02A-creatures-of-the-forbidden-lands.md', encoding='utf-8') as f:
    a_text = f.read()
with open(f'{BASE}/02B-monsters-of-the-forbidden-lands.md', encoding='utf-8') as f:
    b_text = f.read()
with open(f'{BASE}/02-bestiary-third-party-merge.md', encoding='utf-8') as f:
    merge_text = f.read()

NOT_INCLUDE = {'Crab Spider', 'Green Slime', 'Grave Servitor', 'Black Digester'}

HUMANOID_BANDS = {
    'Road Champion', 'Black-Fletch Archer', 'Cutpurse', 'Wise-Hand',
    'Shield Knight', 'Town Guard', 'Clan Hunter', 'Horse Warrior', 'Poisoner',
}

VARIANT_OPENERS = {
    'Air Spirit': (
        'An Air Spirit is the wrathful cousin of the canonical Nature Spirit '
        'in the wind: it does not patron the bridge or the pasture, only the '
        'cliff, the gibbet, and the headland where the weather changes faster '
        'than the people on it.'
    ),
    'Earth Spirit': (
        'An Earth Spirit is the wrathful cousin of the canonical Nature Spirit '
        'in the stone: it does not patron the road or the marsh, only the '
        'broken cairn, the bitten quarry, and the grave opened for gain.'
    ),
}

# Map entry names to the corresponding section heading in the merge file
MERGE_LOOKUP = {
    'Air Spirit':   'Air Spirit (Variant of Nature Spirit)',
    'Earth Spirit': 'Earth Spirit (Variant of Nature Spirit)',
    'Bog Hag':      'Bog Hag (Variant of Bog Man)',
}

SKIP_HEADINGS = {
    'Creatures of the Forbidden Lands',
    'Using This Chapter',
    'New Statblock Elements',
    'Monsters of the Forbidden Lands',
}


def split_h3_entries(text):
    """Split text on ### headings; return dict {name: full_entry_text}."""
    entries = {}
    pattern = re.compile(r'^(### .+)$', re.MULTILINE)
    positions = [(m.start(), m.group(1)[4:].strip()) for m in pattern.finditer(text)]
    for i, (pos, name) in enumerate(positions):
        if name in SKIP_HEADINGS:
            continue
        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        entries[name] = text[pos:end].rstrip()
    return entries


def get_merge_sections(merge_text):
    """Split merge file on ### headings; return dict {name: section_text}."""
    entries = {}
    pattern = re.compile(r'^(### .+)$', re.MULTILINE)
    positions = [(m.start(), m.group(1)[4:].strip()) for m in pattern.finditer(merge_text)]
    for i, (pos, name) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(merge_text)
        entries[name] = merge_text[pos:end].rstrip()
    return entries


def extract_resources_from_section(section_text):
    """Return the uplifted RESOURCES blockquote from a merge file section."""
    idx = section_text.find('> **RESOURCES**')
    if idx == -1:
        return None
    return section_text[idx:].rstrip()


def strip_draft_resources(entry_text):
    """Remove draft RESOURCES blockquote (everything from '> **RESOURCES**' to end)."""
    idx = entry_text.find('> **RESOURCES**')
    if idx != -1:
        return entry_text[:idx].rstrip()
    return entry_text


def add_variant_opener(entry_text, opener):
    """Prepend opener to the first plain prose paragraph (not bullet/quote/heading/table)."""
    lines = entry_text.split('\n')
    result = []
    inserted = False
    for line in lines:
        stripped = line.strip()
        if (
            not inserted
            and stripped
            and not stripped.startswith('#')
            and not stripped.startswith('>')
            and not stripped.startswith('-')
            and not stripped.startswith('|')
        ):
            result.append(opener + ' ' + line.lstrip())
            inserted = True
        else:
            result.append(line)
    return '\n'.join(result)


# ── Parse entries ──────────────────────────────────────────────────────────────
a_entries = split_h3_entries(a_text)
b_entries = split_h3_entries(b_text)
merge_sections = get_merge_sections(merge_text)

# 02A: split into creature entries and humanoid band entries
a_creatures = {k: v for k, v in a_entries.items()
               if k not in HUMANOID_BANDS and k not in NOT_INCLUDE}
a_humanoids = {k: v for k, v in a_entries.items() if k in HUMANOID_BANDS}

# 02B: drop NOT_INCLUDE entries
b_monsters = {k: v for k, v in b_entries.items() if k not in NOT_INCLUDE}

# ── Process 02B monsters ───────────────────────────────────────────────────────
processed_b = {}
for name, text in b_monsters.items():
    # Strip existing draft RESOURCES block
    clean = strip_draft_resources(text)
    # Add variant opener where required
    if name in VARIANT_OPENERS:
        clean = add_variant_opener(clean, VARIANT_OPENERS[name])
    # Fetch uplifted RESOURCES from merge file
    merge_name = MERGE_LOOKUP.get(name, name)
    section = merge_sections.get(merge_name)
    if section:
        resources = extract_resources_from_section(section)
        if resources:
            clean = clean + '\n\n' + resources
        else:
            print(f'WARNING: RESOURCES block not found in section for {merge_name}', file=sys.stderr)
    else:
        print(f'WARNING: merge section not found for {name!r} (looked up as {merge_name!r})', file=sys.stderr)
    processed_b[name] = clean

# ── Process 02A creature entries ───────────────────────────────────────────────
processed_a_creatures = {}
for name, text in a_creatures.items():
    section = merge_sections.get(name)
    if section:
        resources = extract_resources_from_section(section)
        if resources:
            processed_a_creatures[name] = text + '\n\n' + resources
        else:
            print(f'WARNING: RESOURCES block not found for creature {name}', file=sys.stderr)
            processed_a_creatures[name] = text
    else:
        print(f'WARNING: merge section not found for creature {name!r}', file=sys.stderr)
        processed_a_creatures[name] = text

# ── Process 02A humanoid bands ─────────────────────────────────────────────────
processed_a_humanoids = {}
for name, text in a_humanoids.items():
    processed_a_humanoids[name] = (
        text.rstrip() + '\n\nWhat they carry is what is left when they fall.'
    )

# ── Build output file ──────────────────────────────────────────────────────────
output_lines = [
    '# Third-Party Bestiary — Merged Ready File',
    '',
    'Ready for integration into `02-bestiary.md` (Book of Beasts, Chapter 2).',
    '',
    'Excluded entries: Crab Spider, Green Slime, Grave Servitor, Black Digester.',
    'RESOURCES blocks replaced with uplifted versions from `02-bestiary-third-party-merge.md`.',
    'Air Spirit and Earth Spirit carry variant-opener sentences per merge instructions.',
    '',
    '---',
    '',
    '## Monsters of the Forbidden Lands',
    '',
]
for name in sorted(processed_b.keys()):
    output_lines.append(processed_b[name])
    output_lines.append('')

output_lines += [
    '---',
    '',
    '## Creatures of the Forbidden Lands',
    '',
]
for name in sorted(processed_a_creatures.keys()):
    output_lines.append(processed_a_creatures[name])
    output_lines.append('')

output_lines += [
    '---',
    '',
    '## Humanoid Bands',
    '',
]
for name in sorted(processed_a_humanoids.keys()):
    output_lines.append(processed_a_humanoids[name])
    output_lines.append('')

output = '\n'.join(output_lines)
output_path = f'{BASE}/02-bestiary-merged.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Written: {output_path}')
print(f'  02B monsters  ({len(processed_b)}): {sorted(processed_b.keys())}')
print(f'  02A creatures ({len(processed_a_creatures)}): {sorted(processed_a_creatures.keys())}')
print(f'  02A humanoids ({len(processed_a_humanoids)}): {sorted(processed_a_humanoids.keys())}')
