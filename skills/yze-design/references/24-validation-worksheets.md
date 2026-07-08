<!-- markdownlint-disable MD013 -->

# Validation Worksheets — Math, Tempo, Exploits, Feel

> **STATUS: FILLED.** Use these worksheets with `13-balance-and-synergy.md` and `19-player-psychology-and-felt-experience.md`. They make validation repeatable for agents: calculate the common deltas, flag dangerous changes, and produce the same verdict format each time.

## Contents

1. Dice math worksheet
2. Attrition worksheet
3. Resource-loop worksheet
4. Action-economy worksheet
5. Exploit worksheet
6. Table-burden worksheet
7. Felt-experience worksheet
8. Simulation-lite formulas
9. Inventory/transport/storage worksheet
10. Crafting/construction/investment worksheet
11. Combat validation worksheet
12. Final validation memo

## 1. Dice math worksheet

Fill for every rule that changes rolls:

- Baseline pool:
- Modified pool:
- Does it add dice, change target number, grant successes, reroll, auto-succeed, or alter push?
- Is the modifier permanent, scene-limited, use-limited, or paid per use?
- Does it cross the 50% competent line or 80% expert line?

Threshold warnings:

| Change | Risk |
| --- | --- |
| +1 die | Usually safe if scoped or paid; dangerous if permanent and broad |
| +2 dice | Equivalent to a strong talent; require scope, cost, or limited frequency |
| +3 dice | Breakpoint-crossing for starting PCs; usually Situational or Optional |
| Auto-success | Premium category; must be rare, narrow, costly, or story-gated |
| Target number improves from 6 to 5-6 | Massive per-die-rate shift; treat as system-level |
| Reroll after push | High risk; can erase push consequence |

## 2. Attrition worksheet

Use for harm, stress, supply, corruption, heat, debt, clue pools, and project clocks.

- Resource name:
- Starts at:
- Gains from:
- Spends on:
- Depletes/escalates on:
- Recovery method:
- Expected session change:
- Worst-case state:
- Is worst-case playable?

Warnings:

- A resource that only rises becomes doom without agency.
- A resource that only falls becomes bookkeeping unless depletion changes decisions.
- A resource that refills from the action it powers risks a free-refund loop.
- Recovery faster than pressure makes attrition cosmetic.

## 3. Resource-loop worksheet

Trace the loop as four beats:

1. **Pressure:** what hurts, runs out, escalates, or threatens?
2. **Decision:** what can the player choose?
3. **Cost:** what is spent, risked, delayed, damaged, exposed, or owed?
4. **State change:** what changes on the sheet, map, relationship web, or clock?

If any beat is missing, the rule is not a YZE pressure loop yet.

## 4. Action-economy worksheet

Use for combat, chases, social combat, vehicles, magic, reactions, and projects.

- Action type affected: SLOW / FAST / reaction / shift activity / downtime project.
- Does the rule reduce SLOW to FAST?
- Does it create a free action?
- Does it grant extra reactions?
- Does it let one character fill multiple activity-menu jobs?
- Does it compress recovery or crafting time?

Threshold warnings:

| Change | Verdict pressure |
| --- | --- |
| SLOW to FAST | Stronger than +1 die; require scope or cost |
| FAST to free | High exploit risk; require once/round or metacurrency |
| Extra reaction | Can create defense lock; require spent action budget |
| One PC fills two menu jobs | Can collapse party-labor puzzle |
| Time compression | Check economy and recovery loops, not just convenience |

## 5. Exploit worksheet

Mark every fired category from `13 §5`:

- Infinite/refund loop:
- Cap bypass:
- Silent stacking:
- Free resource:
- Action abuse:
- Push-cost avoidance:
- Mishap avoidance:
- Talent/rule invalidation:

Then answer:

- Does activation require 0-1 easy decisions?
- Is the effect repeatable per round/scene/session?
- Is the cost real at the moment of use?
- Does the rule replace or stack?
- Which pressure channel does it relieve?
- Does it relieve that channel temporarily or delete it?

Two or more "delete/free/repeatable/stacking" answers means Revise or Reject.

## 6. Table-burden worksheet

Score OK / Caution / Fail:

- Player-facing complexity:
- GM tracking:
- Frequency of rolls:
- Number of new states:
- Ambiguity:
- Sheet impact:
- Lookup burden:

Hard limits:

- A General rule should not add more than one persistent tracked state unless it is the game's signature mechanic.
- A Situational subsystem may add several states only when the scene is about that subsystem.
- A Campaign Mode may add a sheet or map, but must replace another layer's complexity or justify its campaign subject.

## 7. Felt-experience worksheet

Check against `19`:

- False choice: are options mechanically distinct?
- Decision fatigue: are there too many micro-choices?
- Swinginess: is variance framed as danger rather than unfairness?
- Agency collapse: can the player still act after the cost lands?
- Too weak/strong/slow/fiddly/punishing/safe: which "too X" applies?
- Identity: does the rule express the game's thesis?

Worst-case principle: catastrophic outcomes may be severe, but they should create play unless the game explicitly permits character exit.

## 8. Simulation-lite formulas

Use these without re-deriving math:

- **At least one success on n D6:** `1 - (5/6)^n`.
- **Expected raw successes on n D6:** `n / 6`.
- **At least two successes:** `1 - (5/6)^n - n*(1/6)*(5/6)^(n-1)`.
- **Resource die step chance:** contraction range / die size. Example: D8 depletes on 1-2 = 25%.
- **Rough expected rolls before one step:** die size / contraction range.
- **Persistent +1 die:** compare every common pool, not only the best case.
- **Auto-success:** treat as stronger than +3 dice for most medium pools because it deletes failure states.

Default pool landmarks:

| Dice | P(>=1 success) |
| --- | --- |
| 3 | 42% |
| 4 | 52% |
| 5 | 60% |
| 6 | 67% |
| 8 | 77% |
| 9 | 81% |

## 9. Inventory/Transport/Storage Worksheet

Use with `08-gear-and-economy.md`.

- Personal carry formula:
- Heavy/light/tiny rules:
- Container capacity added:
- Container downside: hand cost / action access / MOVE-STEALTH penalty / theft risk:
- Over-carry trigger:
- Failure choice:
- Group store die or stockpile:
- Transport required to justify it:
- Storage location:
- Spoilage/theft/event exposure:
- Does any cost get charged twice as lifestyle/upkeep and Resource Die?

Threshold warnings:

| Pattern | Risk |
| --- | --- |
| Capacity increase with no penalty | mandatory optimization |
| D10/D12 group stores with no transport | invisible bulk |
| Backpack gear instantly accessible in combat | access-cost deletion |
| Lifestyle/upkeep plus Resource Die for same food | double charge |
| Stockpile with no guard/storage/event exposure | invulnerable wealth |

## 10. Crafting/Construction/Investment Worksheet

Use with `08-gear-and-economy.md`.

- Asset or item:
- Cost band:
- Time band:
- Cost unit: cash / Capital / materials / labor / stores / SP:
- Required gates: talent / tools / function / specialist / location / staff:
- Persistent effect:
- Upkeep vector:
- Failure consequence:
- Expected payout or capability:
- Expected payback period:
- Can it be liquidated, sold, moved, or converted?
- Does it stack with other bonuses?
- What story pressure appears before it safely repays?

Threshold warnings:

| Pattern | Risk |
| --- | --- |
| Persistent broad +1 from cash alone | bonus inflation |
| Major asset pays back in 1 season safely | passive wealth engine |
| Capital transfers freely between assets | illiquidity deleted |
| Construction has no time cost | downtime economy collapse |
| Staff gives help without wage/housing/upkeep | free dice |
| Failed business only means "no profit" | no consequence loop |

## 11. Combat Validation Worksheet

Use with `03-conflict-and-combat.md`.

- Rule/action:
- Source analogue:
- Trigger:
- Action cost:
- Roll:
- Defense:
- Effect:
- Extra successes/stunts:
- Failure:
- Repeat limit:
- Recovery path:
- Replaces or stacks with:
- Decisive rolls per Round before/after:
- Reaction budget changed?
- Reload/ready/aim tax preserved?
- Baseline pool and modified pool:
- Expected damage/effect:
- Hits-to-Broken:
- Armor/cover interaction:
- Worst-case outcome:
- What can the target do next?

Threshold warnings:

| Pattern | Risk |
| --- | --- |
| SLOW attack becomes FAST with no penalty | doubled attack tempo |
| reaction becomes free | defense inflation |
| extra attack has no Round cap | combo chain |
| ranged weapon ignores reload/ready/cover | ranged dominance |
| multi-target attack has no full-Round/resource cost | encounter deletion |
| control move has no escape/recovery | agency collapse |
| armor and cover stack without action/position cost | grind |
| precision attack keeps full damage and full aim bonus | called-shot dominance |

## 12. Final validation memo

Use this exact structure:

- **Summary:** one sentence.
- **Layer:** General / Situational / Optional / Campaign Mode.
- **Math:** baseline, modified, breakpoint effect.
- **Tempo:** attrition/recovery/session cadence.
- **Exploit surface:** fired categories and fixes.
- **Synergy:** touched systems and replace/stack answer.
- **Table burden:** OK/Caution/Fail notes.
- **Felt experience:** target psychology and risk.
- **Verdict:** Ship / Ship with simplification / Revise-Cap / Revise-Restructure / Hold / Reject.
- **Required fix:** only if not Ship.
