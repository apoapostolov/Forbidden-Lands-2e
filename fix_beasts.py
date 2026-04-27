#!/usr/bin/env python3
import sys
import re

path = "03-book-of-beasts/02-bestiary.md"

try:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: {path} not found")
    sys.exit(1)

original = content

# FIX 1: Basilisk Monster Attacks - merged header/separator row
# Look for the merged line pattern
match = re.search(r'\| D6 \| \*\*ATTACK\*\* \|\| --- \| -+\s*\|', content)
if match:
    merged_line = match.group(0)
    print(f"FIX 1 FOUND: {merged_line[:80]}...")
    replacement1 = "| D6 | **ATTACK** |\n| --- | --- |"
    content = content.replace(merged_line, replacement1, 1)
    print("FIX 1 APPLIED")
else:
    print("FIX 1 NOT FOUND - checking raw...")
    idx = content.find("| D6 | **ATTACK** || --- |")
    if idx >= 0:
        # Get the full line
        newline_idx = content.find("\n", idx)
        if newline_idx == -1: newline_idx = len(content)
        merged_line = content[idx:newline_idx]
        print(f"Found partial match at index {idx}: {repr(merged_line[:100])}")
        replacement1 = "| D6 | **ATTACK** |\n| --- | --- |"
        content = content.replace(merged_line, replacement1, 1)
        print("FIX 1 APPLIED (using partial match logic)")
    else:
        print("Pattern for FIX 1 not found at all")

# FIX 2: Bog Man - remove the vestigial "Interfering Worshipers" block
old2 = """\n#### Random Encounter: Interfering Worshipers\n\n> _The terrain is becoming increasingly wet and boggy, and the virgin forest gradually gives way to hanging mangroves and strange bushes with serpentine root systems growing out of stinking ponds. Cold veils of mist float over the bog and you hear the call of a blackthroated loon coming from somewhere ahead of you._\n\nBog men are highly attracted to valuable and magical items which they desperately want to drag down into the bog as offerings to the ever-demanding gods. In combat they always target the adventurer who carries the largest number of treasures or magical items. It could be gold or silver coins, magic weapons, and artifacts \u2013 whatever the GM deems most appropriate, but Bog men have a special fondness for shiny objects. In a crisis situation, the Bog men can always be lured away from a fight by throwing a shiny piece of treasure into the bog.\n\n### Bugbear"""

new2 = "\n### Bugbear"

if old2 in content:
    content = content.replace(old2, new2, 1)
    print("FIX 2 APPLIED")
else:
    print("FIX 2 NOT FOUND - trying alternate search...")
    # Try finding the heading alone to debug
    idx = content.find("#### Random Encounter: Interfering Worshipers")
    if idx >= 0:
        print(f"Heading for FIX 2 found at index {idx}")
        # Look for the end of the block (Bugbear)
        end_idx = content.find("### Bugbear", idx)
        if end_idx >= 0:
            print(f"Ending '### Bugbear' found at {end_idx}. Removing block.")
            content = content[:idx] + "### Bugbear" + content[end_idx + len("### Bugbear"):]
            print("FIX 2 APPLIED (using fuzzy boundary logic)")
        else:
            print("Could not find '### Bugbear' after the heading.")
    else:
        print("Heading for FIX 2 not found")

if content != original:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FILE WRITTEN")
else:
    print("NO CHANGES MADE")
