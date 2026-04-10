# High-Confidence Correction List

This list is for corrections that are usually safe in Forbidden Lands OCR work.

It is not permission to rewrite anything that merely looks similar.

## Frequent Generic OCR Repairs

- `elcome` -> `Welcome`
- `his chapter` -> `This chapter`
- `othing` -> `Nothing`
- `ossessing` -> `Possessing`
- `agic` -> `Magic`

## Frequent Forbidden Lands Repairs

- `forbidden lands` -> `Forbidden Lands`
- `strongh old` -> `Stronghold`
- `willpow er` -> `Willpower`
- `agi lity` -> `Agility`
- `str ength` -> `Strength`
- `empat hy` -> `Empathy`

## Discipline and Supplement Phrases Seen in This Repo

- `spells & sorcerers`
- `towns & villagers`
- `battles & sieges`
- `legends & adventurers`

## Custom Glyph OCR Repairs

- In `Spells & Sorcerers`, a leading `E` before spell metadata is often a
  broken OCR read of a custom glyph bullet, not the actual letter `E`.
- Safe examples:
  `E RANK 1` -> `- Rank: 1`
  `E RANGE: Short` -> `- Range: Short`
  `E DURATION: Immediate` -> `- Duration: Immediate`
  `E INGREDIENT: Candle (1 roll)` -> `- Ingredient: Candle (1 roll)`
- Apply this only in spell metadata blocks, not in normal prose.

## Use Rule

Only apply these automatically when:

- the corrupted form is obvious
- the surrounding context matches
- the correction does not change a rule meaning

If any of those fail, preserve the damaged term and flag it.
