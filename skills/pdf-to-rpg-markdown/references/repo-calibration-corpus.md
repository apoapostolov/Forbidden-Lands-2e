# Repo Calibration Corpus

This reference grounds the OCR workflow in real repo examples instead of
abstract advice.

Each example shows a recurring artifact pattern and the kind of recovery the
clean manuscript should aim for.

## Example 1: Title Page and Footer Noise

Source:

- `temp-work/towns-and-villagers/Forbidden Lands - Towns and Villagers.raw.md`

Raw:

```md
# orbidden F lands

TOWNS & VILLAGERS

FORBIDDEN LANDS

2

towns & villagers

## INTRODUCTION
```

Clean:

```md
## Towns & Villagers

### Introduction
```

Why it matters:

- the raw extractor preserved decorative title fragments and page furniture
- the clean file restores a navigable manuscript title and removes footer noise

## Example 2: Drop-Cap and Split-Word Repair

Source:

- `temp-work/spells-and-sorcerers/Forbidden Lands-spells_and_sorcerers_eng_1_01.raw.md`

Raw:

```md
did not find in the rules and the list of spells a way to be present in the game sessions.

elcome to Spells & Sorcerers, a new supplement from Xiphos Games Studio for **Forbidden** W **Lands** .
```

Clean:

```md
Welcome to **Spells & Sorcerers**, a new supplement from Xiphos Games Studio for **Forbidden Lands**.
```

Why it matters:

- raw OCR often leaves floating fragments from a previous paragraph
- decorative drop caps commonly remove the opening letter of the next paragraph
- the safe repair is selective, not a blind global rewrite

## Example 3: Heading Reordering and Structural Recovery

Source:

- `temp-work/battles-and-sieges/Forbidden Lands - Battles & Sieges - (OEF, 2024-12-15).raw.md`

Raw:

```md
## ARMY LINES

## GAME TIME

As in the original rules, battles are resolved in 15-minute increments...
```

Clean target:

```md
## Game Time

As in the original rules, battles are resolved in 15-minute increments...

## Army Lines

In essence, lines represent the depth of an army on the battlefield...
```

Why it matters:

- extraction order can drift around headings in dense layouts
- a cleaner manuscript may need local structural reordering, not just formatting

## Example 4: One-Line Table to Real Table

Source:

- `temp-work/spells-and-sorcerers/Forbidden Lands-spells_and_sorcerers_eng_1_01.raw.md`

Raw:

```md
||**DESCRIPTION**<br>**COST**<br>**TIME**<br>Learn a new magic talent<br>3 XP<br>Aquarter day...
|---|---|
```

Clean:

```md
| Description | Cost | Time |
| --- | --- | --- |
| Learn a new magic talent | 3 XP | A quarter day |
| Increase a magic talent by 1 level | New level x 3 | A quarter day per level |
```

Why it matters:

- image-derived table text often arrives as a vertical `<br>` stack
- the goal is not to preserve the OCR shape but to recover the playable table

## Example 5: Generator Table Recovery

Source:

- `temp-work/legends-and-adventurers/Forbidden_Lands_Legends_and_Adventurers_5th_printing.raw.md`

Raw:

```md
||**D66**<br>**KIN**<br>11–22<br>Alderlander Human<br>23–31<br>Aslene Human...
|---|---|
```

Clean:

```md
| **D66** | **Kin** |
|---|---|
| 11–22 | Alderlander Human |
| 23–31 | Aslene Human |
| 32–34 | Ailander Human |
```

Why it matters:

- generator books live or die on table integrity
- even a simple two-column table should be reconstructed, not left as a vertical OCR dump

## Example 6: Complex Matrix Requires Restraint

Source:

- `temp-work/towns-and-villagers/Forbidden Lands - Towns and Villagers.raw.md`

Raw:

```md
|**TOWN SIZE**<br>**D66**<br>**SIZE**<br>**LOCATIONS**<br>**MODIFIER**...|**GENERAL CONDITION OF THE TOWN**...
|---|---|
```

Clean handling:

- split into two separate tables
- keep the left-side and right-side structures distinct
- do not pretend the raw extraction was a single coherent two-column table

Why it matters:

- matrix-style page layouts often need editorial reconstruction, not mechanical cleanup

## Example 7: Safe Restraint on Ambiguous Terms

Observed in repo cleanup:

- `ailanders and aslenes`
- mixed slash markers like `[kin/character]`
- corrupted but still interpretable proper nouns

Preferred approach:

- repair when repeated evidence supports the correction
- preserve the best recovered form when confidence is uncertain
- note ambiguity instead of silently inventing lore

## How To Use This Corpus

When cleaning a new file:

1. identify which example class it resembles
2. reuse the same style of repair
3. do not generalize a hard edit beyond the artifact class it demonstrates

This corpus is a calibration set, not a license to guess.
