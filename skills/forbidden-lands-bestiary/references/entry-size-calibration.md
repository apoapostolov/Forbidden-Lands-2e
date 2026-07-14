<!-- markdownlint-disable MD013 -->

# Entry Size Calibration

## Purpose

This file sets corpus-based word-count floors for the main written parts of a high-quality monster entry.

The goal is not to make every entry the same length.
The goal is to stop AI drafts from collapsing into undersized stubs that technically fill every heading but fail to carry weight, texture, or usable table information.

These numbers come from measured Book of Beasts material, not preference alone.

## Sources And Method

Measured source:

- `03-book-of-beasts/02-bestiary.md`, including its Legends section

The values below were preserved from the project's earlier corpus analysis. The
analysis script and generated reports are not part of the trimmed public
repository. Treat the figures as drafting diagnostics, not immutable law.

Method used:

- **Average** = mean word count of the measured sample
- **Bottom 25%** = 25th percentile of the measured sample
- **Top 75%** = 75th percentile of the measured sample
- **Recommended floor** = bottom 25% rounded up; this is the hard AI minimum

For drafting purposes:

- use the **recommended floor** as the bare minimum
- use the **recommended target** as the normal aim
- use the **healthy upper band** when the entry benefits from extra weight without turning baggy

## Calibration Table

| Element | Sample | Average | Bottom 25% | Top 75% | Recommended floor | Recommended target | Healthy upper band |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Typical vignette | 41 | 12.3 | 11.0 | 14.0 | 11 | 12 | 14 |
| Monster description | 34 | 187.8 | 96.8 | 278.8 | 97 | 188 | 279 |
| Monster attacks table | 34 | 257.4 | 144.2 | 372.2 | 145 | 257 | 373 |
| Lore Roll entry | 102 | 22.9 | 16.2 | 28.0 | 17 | 23 | 28 |
| Lore Roll row 2 | 34 | 24.9 | 21.2 | 28.0 | 22 | 25 | 28 |
| Lore Roll row 3 | 34 | 28.8 | 23.2 | 31.0 | 24 | 29 | 31 |
| Random encounter total | 68 | 167.5 | 143.0 | 197.8 | 143 | 168 | 198 |
| Random encounter body | 68 | 141.4 | 127.0 | 156.5 | 127 | 141 | 157 |
| Monster legend | 56 | 191.8 | 111.8 | 270.0 | 112 | 192 | 270 |

## Hard Rules By Entry Part

### Flavor vignette

- **Hard minimum:** 11 words
- **Normal target:** 12 words
- **Healthy range:** 11-14 words

The vignette must still be one sentence.
This floor exists to prevent dead-on-arrival fragments that name an object but create no image.

If the line rises far above the healthy band, check whether it has stopped being a vignette and become a mini-description.

### Monster description

- **Hard minimum:** 97 words
- **Normal target:** 188 words
- **Healthy upper band:** 279 words

If the description falls below 97 words, it usually means one of these failures has occurred:

- ecology is missing
- behavior is missing
- social or historical weight is missing
- the text is repeating the statblock instead of adding context

### Monster attacks table

- **Hard minimum:** 145 words total
- **Normal target:** 257 words total
- **Healthy upper band:** 373 words total

This is the total size of the six-row table, not a per-row target.

At floor level, a six-row table averages roughly 24 words per row.
At target level, it averages roughly 43 words per row.

If the table is far below floor, the attacks usually suffer from one of these problems:

- rows are mechanically vague
- riders are omitted
- range or targeting is unclear
- attack identity is too repetitive from row to row

### Lore Roll entry

- **Generic hard minimum per row:** 17 words
- **Row 1 hard minimum:** 12 words
- **Row 2 hard minimum:** 22 words
- **Row 3 hard minimum:** 24 words

Rows 2 and 3 need more room because they carry hint architecture, not just fact labeling.
A two-success hint that is too short usually becomes either obvious spoiler text or useless fog.
A three-success hint that is too short usually loses either flavor or direction.

### Monster legend

- **Hard minimum:** 112 words
- **Normal target:** 192 words
- **Healthy upper band:** 270 words

A legend below floor usually feels like a description stub rather than inherited memory.
The floor matters because a legend must carry:

- old explanation
- social practice or taboo
- regional or cult framing
- some weight of time

### Random encounter

- **Hard minimum:** 143 words total, excluding `Terrain Types`
- **Normal target:** 168 words total
- **Healthy upper band:** 198 words total
- **Body-text floor inside that total:** 127 words

The encounter total includes:

- the epigraph
- the encounter body

It excludes:

- the title
- the `Terrain Types` line

If the body falls below 127 words, the encounter usually stops being a dilemma and becomes a prompt.

## How To Use These Numbers In AI Drafting

Use this command logic mentally when drafting:

- **floor** = do not go under this without a deliberate reason
- **target** = what a normal strong draft should roughly hit
- **upper band** = extra room available before the text starts to bloat

These are drafting controls, not beauty laws.

A strong entry may exceed the upper band if the added material remains dense and useful.
A weak entry does not become strong by hitting the number alone.

But an AI draft that misses the floor usually arrives thin in exactly the same ways every time.

## Special Note On Vignettes

The vignette measurements deliberately filter out legacy long-form opening lore blocks.

Filter used by the analyzer:

- one sentence only
- 35 words maximum

This keeps the vignette calibration tied to the current short-form entry standard rather than to older description-style openings.

## Recommendation

When assigning an AI drafting task, state the floor explicitly.

Example:

- vignette: minimum 11 words
- description: minimum 97 words
- attacks table: minimum 145 words total
- Lore Roll row 2: minimum 22 words
- Lore Roll row 3: minimum 24 words
- random encounter: minimum 143 words total
- legend: minimum 112 words

That wording is not cosmetic.
It is part of the quality control.
