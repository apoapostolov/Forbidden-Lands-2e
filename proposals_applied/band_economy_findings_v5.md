# Band Economy Findings V5 — Additive Pay Model (V6 Simulation)

**Simulation:** `scripts/band_economy_sim.py`
**Runs:** 200 × 365 days per variant (15 total variants, 3,000 simulation-years)
**Pay model tested:** V6 — additive retainer + mission pay, −30% contract rates, haggle mechanic
**Reference baseline:** V3 (the established viable model)

---

## What V6 Tests

The V3 model ran retainer during idle and full daily wages during mission
(exclusive modes). The proposal now states mission pay is **additive** — fighters
draw their weekly retainer continuously and on top of that earn the daily mission
rate when work is active.

V6 combines this additive pay rule with a harder contract market:

| Change         | Detail                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------- |
| Additive pay   | On active work: retainer (3.29s/day) + mission pay (6.50s/day) = **9.79s/day**              |
| Idle/travel    | Retainer only (3.29s/day) — same as V3                                                      |
| Contract floor | −30% off V3 rates (patrol 7d: 77–116s vs V3's 110–165s)                                     |
| Haggle         | Captain rolls 2d6 at contract acceptance — any 6 upgrades to −20% floor (~31% of contracts) |

The question: does the additive pay rule break viability within V3-priced or V6-priced contracts?

---

## Results — V6 vs V3 Head-to-Head

### Standard Warband (6 commons, 2 veterans, 1 named man)

| METRIC                | V3 RETAINER+     | V6 ADDITIVE PAY |
| --------------------- | ---------------- | --------------- |
| Survival rate (1 yr)  | **95.5%**        | 88.5%           |
| Median final treasury | **868s**         | 474s            |
| P10 treasury          | 0s               | 0s              |
| P90 treasury          | **1,518s**       | 887s            |
| Mean annual income    | **2,676s**       | 1,926s          |
| — Contracts           | **2,476s**       | 1,728s          |
| — Bounties            | **197s**         | 192s            |
| Mean annual expenses  | 2,195s           | **1,856s**      |
| — Wages/Retainer      | 1,524s           | **1,252s**      |
| — Food                | 382s             | **359s**        |
| — Loot shares         | 267s             | **219s**        |
| Net margin            | **+18.0%**       | +3.6%           |
| Annual net cash flow  | **+481s**        | +70s            |
| Days on contract      | **234d (64.1%)** | 225d (61.8%)    |
| Dead-time runway      | ~30 days         | ~30 days        |

### Small Band (4 commons, 1 veteran)

| METRIC                | V3 RETAINER+ | V6 ADDITIVE PAY |
| --------------------- | ------------ | --------------- |
| Survival rate (1 yr)  | 85.0%        | **85.0%**       |
| Median final treasury | 989s         | 563s            |
| P90 treasury          | 1,724s       | 947s            |
| Mean annual income    | 2,465s       | 1,816s          |
| Mean annual expenses  | 1,690s       | **1,519s**      |
| Net margin            | +31.4%       | **+16.4%**      |
| Annual net cash flow  | +774s        | +297s           |
| Days on contract      | 216d (59.3%) | 218d (59.7%)    |

### Warband with Initiate Caster

| METRIC                | V3 RETAINER+ | V6 ADDITIVE PAY |
| --------------------- | ------------ | --------------- |
| Survival rate (1 yr)  | **100.0%**   | **100.0%**      |
| Median final treasury | 822s         | 459s            |
| P10 treasury          | 9s           | 0s              |
| P90 treasury          | 1,532s       | 929s            |
| Mean annual income    | 3,675s       | 2,684s          |
| Mean annual expenses  | 3,320s       | 2,782s          |
| Net margin            | **+9.7%**    | −3.6%           |
| Annual net cash flow  | +356s        | −97s            |
| Days on contract      | 243d (66.5%) | 236d (64.6%)    |

---

## Pay Model Arithmetic

Daily wage cost per man on active work:

| FIGHTER TYPE    | RETAINER (daily equiv.) | MISSION PAY | V6 TOTAL (additive) | V3 TOTAL (exclusive) |
| --------------- | ----------------------- | ----------- | ------------------- | -------------------- |
| Common          | 0.29s/day               | 0.50s/day   | **0.79s/day**       | 1.00s/day            |
| Veteran         | 0.43s/day               | 1.00s/day   | **1.43s/day**       | 2.00s/day            |
| Named Man       | 0.71s/day               | 1.50s/day   | **2.21s/day**       | 3.00s/day            |
| Initiate Caster | 1.14s/day               | 3.00s/day   | **4.14s/day**       | 6.00s/day            |

The additive model is **cheaper than V3** per mission day (9.79s vs 13.0s for the standard warband) but V6's −30% contract floor cuts income by roughly the same proportion. The two factors nearly cancel but not exactly — income falls faster than cost, compressing margin.

Standard warband: contract income/day on active work = 7.7s vs 9.79s mission cost = −2.1s gross per mission day. The positive margin (+3.6%) survives entirely because garrison contracts (protection season) pay retainer-rate wages while generating contract income.

---

## What V6 Loses Relative to V3

**Income pressure dominates.** The main damage is the −30% contract floor:

- V3 patrol (7d): 110–165s → V6 patrol (7d): 77–116s (−29%)
- V3 garrison-short (21d): 340–500s → V6: 238–350s (−30%)
- V3 protection season (91d): 550–800s → V6: 385–560s (−30%)

A V6 band on a protection season earns 472s median vs V3's 675s median, while paying the same retainer wages for 91 days. The garrison margin narrows from roughly +40–80s to roughly −20 to +80s.

**The caster band breaks even.** The caster's premium (+35% on standard contracts) and caster-specific contract access still apply. But at −30% base rates with the additive wage stack, the caster costs more than the contracts recover. Median treasury remains positive (459s) and survival stays at 100% — the band does not collapse — but systemic profitability disappears. This is a meaningful indicator: V6 is viable for non-caster bands but caster investment becomes a strategic question, not a guaranteed payoff.

**The haggle roll helps at the margin.** At ~31% success per contract, haggling recovers a fraction of the contract income lost. A band with 200+ contract days and ~200 contract events per year recovers perhaps 60–70 events at the higher (−20%) tier. This adds roughly 8–15s per recovered contract in upside. Without the haggle mechanic, V6 standard warband margin would likely go negative.

---

## What V6 Preserves

| Check                             | V3 Status | V6 Status          |
| --------------------------------- | --------- | ------------------ |
| Positive margin, standard warband | +18.0% ✓  | +3.6% ✓            |
| Positive margin, small band       | +31.4% ✓  | +16.4% ✓           |
| Positive margin, caster warband   | +9.7% ✓   | −3.6% ✗            |
| 85%+ survival, standard warband   | 95.5% ✓   | 88.5% — borderline |
| 85%+ survival, small band         | 85.0% ✓   | 85.0% ✓            |
| 100% survival, caster warband     | 100% ✓    | 100% ✓             |
| Positive P10 treasury at year-end | 0s (no)   | 0s (no)            |
| Treasury accumulates over time    | Yes ✓     | Yes (slowly) ✓     |

**Verdict: V6 is not as good as V3, but it is not broken.** Two of three configurations remain positive-margin. The caster band goes slightly negative on annual margin but still operates as a going concern — the 100% survival rate means the caster band finds work and doesn't collapse, it just runs thin.

---

## Which Gap to Close

If V6 is the intended simulation (additive pay + harder market), the caster band result is the most actionable gap. Two adjustments that each individually close the gap:

1. **Raise caster-specific contract rates by 15%.**
   `magical_commission` from 196–294s to 226–338s and `ritual_ward` from 130–210s to 150–242s. Both remain plausible rates. Effect: expected caster-band margin rises from −3.6% to approximately +2–4%.

2. **Add one additional caster-only contract type** (e.g. field apothecary: 10d, 165–245s) that is available from any tier settlement. Increases caster-band contract days by ~15d and adds 200s in expected annual income.

Neither change is needed for non-caster bands — small and standard warband margins remain positive without intervention.

If the intent is that V6 represents a deliberately harder world where caster bands must work harder to justify the cost, the current result is also a defensible design position.

---

## Design Validation

| Model                          | Survival  | Margin    | Function               |
| ------------------------------ | --------- | --------- | ---------------------- |
| V1 daily wages                 | 62.5%     | −106%     | Insolvent              |
| V2 retainer                    | 83.5%     | −27%      | Survivable, marginal   |
| V3 repriced+                   | 95.5%     | +18%      | Functional, solid      |
| V5 half mission pay            | 96.5%     | +31%      | High-margin prosperous |
| **V6 additive + tight market** | **88.5%** | **+3.6%** | **Functional, lean**   |

V6 sits between V2 (just barely marginal) and V3 (solid). It is the hardest viable market tested. The additive pay rule does not break the model when contracts are priced at −30% off V3. It does eat into margin. A captain in V6 economy needs garrison work and cannot afford to stay idle.

The fundamental design property from V3 survives: **retainer extends runway**, garrison contracts provide the floor, short active contracts provide the surplus. V6 narrows all three of those margins simultaneously, which is why the result is tighter but still functional.
