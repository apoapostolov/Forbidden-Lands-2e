<!-- markdownlint-disable MD013 -->

# Balance Audit: Cycle-Based Life Path Generator

## Overview

This audit runs 10,000 simulated characters through the life path generator and compares the results against the standard method baseline from Chapter 2. The simulation models the full system: childhood foundations, turn tests, mark accumulation, mark→rank conversion, narrowing tax, thresholds, advancement rolls, forced departures, and crisis paths.

The standard method is the calibration target. A life-path character should arrive at the table roughly as capable as a standard-method character — broader in some places, narrower in others, but never so weak or so strong that the two cannot adventure together.

## Diagnostic Summary

The life path generator is structurally sound. Its core loop — resolve turns, accumulate marks, convert marks to ranks — produces interesting characters with plausible variety. The narrowing tax works. Thresholds gate paths without strangling choice. Crisis paths appear at sensible rates.

Five problems need correction before the system can ship.

| Issue                                               | Severity | Root Cause                                                               |
| --------------------------------------------------- | -------- | ------------------------------------------------------------------------ |
| Characters are too weak compared to standard method | Critical | Mark→rank thresholds too steep for the mark budget                       |
| Survival and Endurance dominate all builds          | High     | Hard-lesson lists funneled into the same two skills                      |
| Wear tiers are meaningless                          | High     | Failure rate × turn count overwhelms the 0–1 / 2–3 / 4+ breakpoints      |
| Talent grants are far too rare                      | Moderate | Only 2-in-6 chance per advancement roll; no baseline guarantee           |
| Pride tag rate too low                              | Low      | Only ~6% per qualifying event; Young characters often finish without one |

## Raw Data

### Cross-Age Comparison

| Metric                 | Young (2 cycles) | Adult (3 cycles) | Old (4 cycles) | Standard Method           |
| ---------------------- | ---------------- | ---------------- | -------------- | ------------------------- |
| Total marks budget     | 8                | 12               | 16             | 8 / 12 / 16 skill points  |
| Mean max skill rank    | 2.01             | 2.31             | 2.61           | 3 / 3 / 4 (optimized)     |
| % reaching Rank 3+     | 8.0%             | 30.7%            | 59.1%          | ~100% (deliberate)        |
| % reaching Rank 4+     | 0.0%             | 0.1%             | 1.7%           | 0 / 0 / ~100% for Old     |
| Mean skills ≥ Rank 1   | 5.95             | 7.67             | 9.08           | 3–5 / 5–7 / 6–9           |
| Mean talent grants     | 0.32             | 0.47             | 0.65           | 1 / 3 / 5 general talents |
| Mean Wear              | 3.25             | 5.35             | 7.26           | n/a                       |
| % at 4+ Wear           | 42.2%            | 87.4%            | 97.2%          | n/a                       |
| Turn test success rate | 45.8%            | 46.5%            | 48.2%          | n/a                       |

### Skill Rank Distribution (Old characters, N=2,500)

| Skill        | R0    | R1    | R2    | R3    | R4+  |
| ------------ | ----- | ----- | ----- | ----- | ---- |
| Survival     | 3.7%  | 14.7% | 52.9% | 28.0% | 0.6% |
| Endurance    | 11.6% | 24.5% | 48.7% | 14.6% | 0.6% |
| Insight      | 16.5% | 29.6% | 43.3% | 10.4% | 0.2% |
| Move         | 21.2% | 39.0% | 35.8% | 4.0%  | 0.0% |
| Scouting     | 25.3% | 42.0% | 30.1% | 2.7%  | 0.0% |
| Healing      | 40.8% | 31.9% | 22.9% | 4.4%  | 0.0% |
| Manipulation | 37.9% | 34.4% | 25.1% | 2.6%  | 0.0% |
| Stealth      | 50.2% | 30.3% | 17.6% | 1.9%  | 0.0% |
| Melee        | 42.1% | 45.2% | 12.6% | 0.1%  | 0.0% |
| Crafting     | 45.3% | 39.3% | 15.0% | 0.4%  | 0.0% |
| Marksmanship | 58.8% | 32.8% | 8.4%  | 0.0%  | 0.0% |
| Performance  | 83.0% | 14.9% | 2.1%  | 0.2%  | 0.0% |

### Wear Distribution

| Wear Range | Young | Adult | Old   |
| ---------- | ----- | ----- | ----- |
| 0–1        | 7.8%  | 0.6%  | 0.1%  |
| 2–3        | 50.0% | 12.0% | 2.7%  |
| 4+         | 42.2% | 87.4% | 97.2% |

### Path Usage (all ages combined)

| Path     | Usage % | Type                      |
| -------- | ------- | ------------------------- |
| Fighter  | 16.7%   | Profession (no threshold) |
| Rogue    | 16.5%   | Profession (no threshold) |
| Hunter   | 16.3%   | Profession (no threshold) |
| Rider    | 9.6%    | Profession (threshold)    |
| Peddler  | 9.2%    | Profession (threshold)    |
| Druid    | 8.2%    | Profession (threshold)    |
| Minstrel | 7.8%    | Profession (threshold)    |
| Sorcerer | 6.0%    | Profession (threshold)    |
| Laborer  | 3.3%    | Crisis                    |
| Drifter  | 3.0%    | Crisis                    |
| Outcast  | 2.9%    | Crisis                    |
| Captive  | 2.8%    | Crisis                    |

## Detailed Analysis

### 1. Characters Are Too Weak (Critical)

**The problem.** A standard-method Adult can place 12 skill points deliberately, capping one or two skills at Rank 3. A life-path Adult with the same 12-mark budget reaches Rank 3 only 30.7% of the time. The median max rank for Adults is 2. For Old characters, 57.4% reach Rank 3 but only 1.7% exceed it — the standard method lets every Old character place one skill at Rank 4 by design.

The mark→rank table is the root cause. Reaching Rank 3 costs 4 marks in a single skill. With 12 marks spread across 6 normal skills and 3 hard-lesson skills per path — plus path changes, event-table variety, and failure funneling — concentration is almost impossible.

**Why it matters.** A life-path character who sits down next to a standard-method character will be broader but noticeably less competent in their core calling. The Fighter who lived through three cycles of war should not be worse at Melee than the Fighter who spent five minutes at the character sheet.

**Proposed fix: lower the Rank 3 threshold from 4 marks to 3.**

| Marks | Current Rank | Proposed Rank |
| ----: | -----------: | ------------: |
|     1 |            1 |             1 |
|     2 |            2 |             2 |
|     3 |            2 |         **3** |
|     4 |            3 |             3 |
|     5 |            3 |         **4** |
|     6 |            3 |             4 |
|     7 |            4 |         **5** |
|     8 |            4 |             5 |
|     9 |            4 |             5 |
|    10 |            5 |             5 |

**Effect.** The Rank 3 breakpoint drops from 4 to 3 marks. A focused Adult (12 marks) can now reliably reach one skill at Rank 3, sometimes Rank 4. An Old character (16 marks) can reach Rank 4 with realistic concentration and Rank 5 only if the entire life bends toward a single skill — which the narrowing tax already discourages.

**Why this works and doesn't break anything.** The narrowing tax and mark-spread mechanics are strong enough safety valves. Even with the easier thresholds, a character spending marks across 9 skill slots per path won't accidentally stack. The mark system's job is to prevent deliberate point-stacking, and it still does that — the player does not choose where marks go. The table does.

### 2. Survival and Endurance Dominate All Builds (High)

**The problem.** Survival appears on every hard-lesson list in the game. Endurance appears on 10 of 12. When a character fails a turn test, they gain a mark from the hard-lesson list — and across all paths, that mark almost always lands on Survival or Endurance. Over a full life, the failure funnel transforms all characters into generic survivalists.

Old characters show the damage clearly: Survival reaches mean 2.77 marks (Rank 2 guaranteed, frequent Rank 3), while path-defining skills like Marksmanship (0.50), Performance (0.19), and Sleight of Hand (0.27) barely reach Rank 1.

**Why it matters.** The life path generator should make characters who feel like their path. A Minstrel whose highest skill is Survival doesn't feel like a Minstrel. A Rogue whose best rank is Endurance doesn't feel like a Rogue.

**Proposed fix: diversify hard-lesson lists so each path's failure mode is thematic.**

Current pattern (nearly universal):

```text
Hard-Lesson Skills: [Survival or Endurance], [Survival or Endurance], [Path Skill]
```

Proposed pattern (path-specific):

| Path     | Current Hard-Lessons            | Proposed Hard-Lessons                      |
| -------- | ------------------------------- | ------------------------------------------ |
| Druid    | Survival, Healing, Insight      | Healing, Insight, **Lore**                 |
| Fighter  | Endurance, Survival, Healing    | Endurance, **Melee**, **Might**            |
| Hunter   | Survival, Scouting, Endurance   | Scouting, **Survival**, **Marksmanship**   |
| Minstrel | Insight, Move, Manipulation     | Insight, **Performance**, **Manipulation** |
| Peddler  | Insight, Survival, Manipulation | Insight, Manipulation, **Crafting**        |
| Rider    | Move, Survival, Endurance       | Move, **Animal Handling**, **Endurance**   |
| Rogue    | Survival, Endurance, Stealth    | Stealth, **Sleight of Hand**, **Move**     |
| Sorcerer | Insight, Survival, Healing      | Insight, **Lore**, **Healing**             |
| Captive  | Endurance, Survival, Insight    | Endurance, **Might**, **Insight**          |
| Drifter  | Survival, Move, Insight         | Survival, Move, **Scouting**               |
| Laborer  | Endurance, Crafting, Insight    | **Might**, Crafting, **Endurance**         |
| Outcast  | Survival, Endurance, Scouting   | **Stealth**, Survival, **Scouting**        |

**Design rule.** At least two of the three hard-lesson skills should appear on the path's normal skill list. This makes failure consolidate marks into the path's identity rather than draining them into generic survivalism.

### 3. Wear Tiers Are Meaningless (High)

**The problem.** Wear accumulates from every failed turn test. With a ~48% success rate and 6–14 resolved turns, expected Wear is:

- Young: 6 turns × 0.52 failure rate ≈ 3.1 Wear
- Adult: 10 turns × 0.52 ≈ 5.2 Wear
- Old: 14 turns × 0.52 ≈ 7.3 Wear

The three-tier system (0–1 / 2–3 / 4+) was designed to make Wear feel like a meaningful fiction dial. In practice, 42% of Young characters and 97% of Old characters land in the maximum tier. The middle tier barely exists for Adults and is nonexistent for Old characters. There is no meaningful variation.

**Why it matters.** If every character ends up at 4+ Wear, the tier system adds complexity without adding decision weight. It also inflates the Unfinished Business rules, since Wear 4+ forces a Life Quest — and nearly every character hits that.

**Proposed fix: count Wear only on consecutive failures, not every failure.**

Under this rule, Wear accumulates only when a character fails two or more turn tests in a row (within the same cycle). A single failure followed by a success resets the streak. This models accumulated hardship rather than individual bad luck.

Expected Wear under consecutive-failure rule:

- Young: ~1.0 Wear (geometric series with p≈0.52 per turn, 6 turns)
- Adult: ~1.8 Wear
- Old: ~2.6 Wear

This produces the intended distribution:

| Wear Range | Young (est.) | Adult (est.) | Old (est.) |
| ---------- | ------------ | ------------ | ---------- |
| 0–1        | ~55%         | ~25%         | ~10%       |
| 2–3        | ~35%         | ~45%         | ~40%       |
| 4+         | ~10%         | ~30%         | ~50%       |

Now the tiers actually differentiate. Young characters mostly walk away clean. Adults carry moderate scars. Old characters have real accumulated damage. The fiction works.

**Alternative fix (simpler): raise the tier breakpoints to 0–3 / 4–6 / 7+.** This requires no rule change, only adjusting the numbers in the Wear table. The downside is that it makes the 4+ tier feel less dramatic and wastes the "Wear from every failure" rule's narrative weight.

**Recommended: consecutive-failure rule.** It's more interesting at the table and better models what Wear is supposed to represent — sustained hardship, not individual stumbles.

### 4. Talent Grants Are Far Too Rare (Moderate)

**The problem.** The standard method grants Young characters 1 general talent, Adults 3, and Old characters 5. The life path generator grants a mean of 0.32 / 0.47 / 0.65 talents from advancement benefits. That's a 3× deficit for Young, 6× for Adult, and 8× for Old.

The math: you get one advancement roll per cycle. A talent appears on results 1–2 (33% chance). Over 2–4 cycles, expected talent grants are 0.66 / 1.0 / 1.33 — still far below the standard method, and the simulation shows even lower because failed advancement rolls (forced departures) eliminate the benefit entirely.

**Why it matters.** Talents define play identity more than skill ranks do. A Fighter without Defender, a Rogue without Lightning Fast, a Minstrel without Lucky — these characters feel unfinished. The life path generator produces characters with rich histories but thin mechanical identities.

**Proposed fix: two changes working together.**

**Fix 4a: guaranteed profession talent seed.** At the end of life path generation, after choosing a final profession, the character gains 1 mark in one talent from that profession's list. This is not an advancement benefit — it is a baseline grant that ensures every life-path character starts with at least one talent.

This matches the standard method's implicit guarantee: even a Young character gets 1 general talent.

**Fix 4b: increase talent yield on advancement.** Change the advancement benefit table so results 1–3 grant a talent (50% instead of 33%). Results 4–6 remain contacts, gear, and rumors.

Combined expected talent marks (not counting profession seed):

- Young: 2 cycles × 0.50 = 1.0 (+ 1 seed = 2 total marks toward talents)
- Adult: 3 × 0.50 = 1.5 (+ 1 seed = 2.5)
- Old: 4 × 0.50 = 2.0 (+ 1 seed = 3.0)

With mark→rank conversion, this yields:

- Young: 1 talent at Rank 1–2
- Adult: 1–2 talents at Rank 1–2
- Old: 2–3 talents at Rank 1–2

Still below the standard method's raw count, but life-path characters compensate with broader skill spreads, fiction elements (contacts, rivals, scars, rumors), and narrative weight that standard-method characters don't have.

### 5. Pride Tag Rate Too Low (Low)

**The problem.** Only 14.9% of Young characters and 33.1% of Old characters encounter a Pride-tagged event during generation. The Dark Secret rate (39–70%) is healthier because mishaps are frequent and carry higher tag density.\*

The root cause is probability: ~18 events are tagged as potential Pride across 12 paths, but each character only resolves 6–14 turns and encounters a Pride-tagged event only if the right table result comes up.

**Proposed fix: add Pride tags to at least one Third Turn event in every profession path.** The Third Turn ("Rise") is thematically the right place for pride — it represents promotion, discovery, and recognition. Currently not all paths have Pride tags on their Third Turn events.

If each path's Third Turn table has at least 2 Pride-tagged events (out of 6), the encounter rate rises to roughly:

- Young: ~30% (one Third Turn per life)
- Adult: ~50%
- Old: ~65%

This still leaves Pride as a meaningful choice, not a guarantee.

## What Does Not Need Fixing

**The narrowing tax works.** Only 3.3% of Old characters stay in the same path for all 4 cycles. The -1 penalty to turn tests and +1 to mishaps is enough to push variety without forbidding commitment.

**Thresholds work.** Gated paths (Druid, Sorcerer, Minstrel, Peddler, Rider) appear at 6–10% each, while no-threshold paths (Fighter, Rogue, Hunter) appear at 16–17%. The gates filter without locking — characters who earn marks in the right skills during childhood or early cycles can access gated paths naturally.

**Crisis path rates are healthy.** Crisis paths (Captive, Drifter, Laborer, Outcast) appear at 3–4% each, totaling ~12% of all cycle-slots for Adult/Old characters. This is enough to make them a real threat without making them the norm.

**Skill diversity is broader than standard method.** Life-path characters average 6–9 skills with at least Rank 1, compared to 3–5 for standard method. This breadth is a feature, not a bug — it reflects a lived history. The problem is not spread; it's that the peaks are too low.

**The childhood foundation is well-calibrated.** Two marks in two skills is exactly right for a pre-cycle bonus. It gives direction without locking a build.

## Implementation Checklist

If all five fixes are accepted:

- [ ] Update the mark→rank table in Skill Ranks and Marks (3→R3 instead of 4→R3)
- [ ] Update the design rationale paragraph below the table
- [ ] Revise all 12 hard-lesson lists to follow the diversification rule
- [ ] Change the Wear rule to consecutive failures only, or raise tier breakpoints
- [ ] Update the Unfinished Business Wear thresholds if tier breakpoints change
- [ ] Revise all 12 advancement benefit tables: results 1–3 = talent, 4–6 = contact/gear/rumor
- [ ] Add "profession talent seed" rule after Choose Profession
- [ ] Add at least 2 Pride tags to every profession path's Third Turn table
- [ ] Update both worked examples (Jorrh, Torvin) to reflect new numbers
- [ ] Re-run simulation to confirm revised numbers hit targets

## Simulation Details

**Tool:** `scripts/lifepath_simulation.py`
**Seed:** 42 (reproducible)
**Population:** 10,000 characters (25% Young, 50% Adult, 25% Old)
**Model:** All 12 paths with exact skill lists, turn tests at attribute 3 + skill rank, d6 pool mechanics, narrowing tax, thresholds with 35% fiction-gate fallback, advancement rolls, forced departures, childhood foundation pairs.
**Limitations:** Event tables modeled stochastically (80% normal list / 20% event extras with player optimization), not as exact D6 lookups. Talent mark accumulation from repeated advancement in same path not tracked at individual talent level. Attribute variation not modeled (fixed at 3).
