<!-- markdownlint-disable MD013 -->

# Proposal - Balance Adjustments For Integrated Path Mishaps

Goal: review the integrated mishap tables after the reorder pass and identify what still needs tuning now that the safer results sit lower and the party-threatening results sit higher.

## Summary Judgment

The integrated mishap tables are in much better shape after the reorder.

The current band logic now broadly matches player-facing danger:

- `01-02` stray discharge elsewhere
- `03-06` social, perceptual, or coordination trouble
- `11-15` extra strain and unstable carry-over
- `16-23` lasting tell or local area disturbance
- `24-31` direct tactical impairment
- `32-35` path degradation or item loss
- `36-46` spectacle, notice, disease, or zone pressure
- `51-64` collateral harm, sensory denial, critical injury, or full backfire
- `65-66` catastrophic loss

That is the right spine for a mishap engine that adds `+10` as the magic gets more out of hand.

The previous major problems have already been corrected structurally:

- the old generic table is no longer flattening every discipline into the same failure voice
- general spells now have their own table instead of borrowing another path's identity
- low results are no longer mixed randomly with high-party-cost outcomes
- item loss, spectacle, outside notice, blindness, and critical injuries now sit far enough up the ladder to feel like escalation

The remaining work is smaller.
It is mostly about outlier rows that were still a little too harsh for their exact slot after the reorder.

## What Was Tuned In This Pass

### Stone Song

Problem:

- `03-04` previously forbade retreat unless an ally dragged the caster away
- from a player point of view, that can be more dangerous than many later bands because it traps the character inside the current fight

Change:

- `03-04` now carries the quieter communication penalty
- the forced-stand-ground result moved up to `05-06`

Why this is better:

- the earliest Stone Song band now creates inconvenience rather than tactical imprisonment
- the harsher commitment-to-position result still appears early, but no longer in the gentlest slot

### Ice Affinity

Problem:

- losing your first fast action in the next encounter is a meaningful tactical hit
- it was competing with a much softer speech-and-coordination penalty

Change:

- `03-04` now holds the speech penalty
- `05-06` now holds the shiver-fit that steals the first fast action unless fully warmed

Why this is better:

- the lower band now hurts table coordination and atmosphere rather than action economy
- the more dangerous combat-facing effect still remains low, but no longer in the least severe slot

### Magnetism

Problem:

- “cannot easily let go of held metal” is often a combat or escape problem, not just color
- navigation trouble until dawn is usually less immediately dangerous

Change:

- `03-04` now carries the navigation penalty
- `05-06` now carries the metal-grip interference

Why this is better:

- the softer exploratory penalty now lives in the softer slot
- the more immediate positional or equipment problem sits one rung higher

### Shapeshifting

Problem:

- the original `05-06` beast-impulse result could read as full referee control over the character's next encounter

Change:

- the row now forces a first fast action to master yourself, or else the impulse takes over

Why this is better:

- the mishap still feels feral
- the player keeps one clear point of agency
- the row is now costly without feeling like total temporary character seizure

## Current Balance Read

From a player and party point of view, the current integrated tables now mostly respect the right order of pain:

1. harmless spill elsewhere
2. embarrassment, omen error, social awkwardness, or minor coordination trouble
3. extra resource drain and risky magical carry-over
4. visible tell or local environmental trouble
5. immediate body penalties and tactical impairment
6. temporary loss of path strength or destruction of meaningful gear
7. spectacle, pursuit, contamination, and widening scene pressure
8. collateral targeting, blindness, horror injury, blunt injury, or full backfire
9. catastrophic loss at `65-66`

That progression is defensible both mathematically and psychologically.

Why the psychology matters:

- players will tolerate low-band setbacks if they feel inconvenient rather than arbitrary
- they accept higher-band brutality if the ladder clearly warned them by escalating in recognizable steps
- once low-band results start quietly deleting turns, forcing bad positioning, or breaking major assets, the whole mishap table feels unfair instead of dangerous

The revised ordering now does a better job of preserving trust.

## Remaining Watch Points

The tables are now good enough to integrate, but a later micro-pass may still be worthwhile on these recurring patterns:

1. first-fast-action loss effects
   - these are strong because they hit initiative tempo directly
   - keep them rare in `03-06`
2. hard item spoilage
   - the current placement is much better, but individual rows should keep damaging one meaningful item or one local bundle, not a whole expedition
3. wrong-target results
   - these are correctly high, but they should always read as trouble, not as a second free offensive effect
4. `65`
   - this remains catastrophic and retirement-default by design
   - that is acceptable, but each path should keep a sliver of path-appropriate reversibility so `66` still stands alone as the absolute severance result

## Recommended Acceptance

Accept now:

- the integrated path-by-path mishap structure
- the restored General Spells mishap table
- the reordered severity ladder
- the targeted low-band tuning for Stone Song, Ice Affinity, Magnetism, and Shapeshifting

Do later only if playtesting shows a problem:

- further micro-ranking among `03-06`
- path-by-path tightening of single item-loss rows
- a final catastrophe wording sweep for `65`

This is now a sound integrated mishap system rather than a generic table copied into many headings.

<!-- markdownlint-enable MD013 -->
