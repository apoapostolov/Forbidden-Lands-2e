# Mercenary Band Economy: V1 Findings

**Simulation:** `scripts/band_economy_sim.py`
**Model:** V1 — Daily wages (always active)
**Runs:** 200 × 365 days each
**Starting treasury:** 100 silver

---

## Summary of Results

### Standard Warband (6 common + 2 veteran + 1 named man)

| Metric                    | Value                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------- |
| Survival rate (full year) | **68%**                                                                               |
| Mean collapse day         | 228                                                                                   |
| Median final treasury     | 0s                                                                                    |
| P10 final treasury        | 0s                                                                                    |
| P90 final treasury        | 233s                                                                                  |
| Net margin                | **−9%/year**                                                                          |
| % runs ending broke       | 0% (treasury floor reached, not technically zero — collapses at size < 3 or morale 1) |

### Small Band (4 common + 1 veteran, no named man)

| Metric            | Value         |
| ----------------- | ------------- |
| Survival rate     | **55%**       |
| Mean collapse day | 204           |
| Net margin        | **−44%/year** |

The smaller band spends relatively more on food per man (less forager throughput), earns nearly equivalent contract income, and has no named man to provide morale stability. It is strictly worse.

### Warband + Initiate Caster (adds 6s/day)

| Metric            | Value         |
| ----------------- | ------------- |
| Survival rate     | **79.5%**     |
| Mean collapse day | 231           |
| Net margin        | **−12%/year** |

The caster band has unexpectedly better survival — not because of the caster's value, but because it starts with one additional body. That extra man absorbs one more casualty before the size-collapse threshold is hit. This is not viability; it's a larger buffer before death.

---

## Annual Cash Flow (Standard Warband, mean across all runs)

### Income

| Source           | Annual Mean | % of Total |
| ---------------- | ----------- | ---------- |
| Contracts        | 1,383s      | 91%        |
| Bounties         | 110s        | 7%         |
| Tribute (forced) | 31s         | 2%         |
| **Total**        | **1,524s**  | —          |

### Expenses

| Source    | Annual Mean | % of Total |
| --------- | ----------- | ---------- |
| Wages     | 1,407s      | 90%        |
| Food      | 136s        | 9%         |
| **Total** | **1,566s**  | —          |

**Net: −42s/year** (income undercovers expenses by 2.7%).

---

## Time Allocation

| Activity                      | Days/Year | %     |
| ----------------------------- | --------- | ----- |
| On contract                   | 98        | 26.9% |
| Traveling to work             | 48        | 13.1% |
| Idle / no contract found      | 84        | 23.0% |
| Unaccounted (collapsed bands) | 135       | 37%   |

**Dead time total (travel + idle): 132 days/year.**

---

## Core Problems Identified

### 1. Dead time is the primary economic failure mode

The band burns **14.3s/day in wages** regardless of whether it is working. With 132 days of dead time per year, that is **~1,893s spent with zero income**. Annual contract income is only 1,383s total. The band structurally costs more in idle time than it earns from working.

**Root cause:** The proposal has no mechanism to reduce daily costs when the band has no contract. Full wages accrue every day, whether or not the men are actually performing any work.

---

### 2. Contract income barely covers daily costs when active

- Daily income while on contract: **14.1s/day**
- Daily total cost (wages + food): **14.3s/day**
- Contract coverage: **98.1%** — there is essentially no margin

When a contract pays, it almost exactly covers wages. There is no surplus to cover dead time, casualties, equipment replacement, or any contingency. One bad engagement wipes any reserve.

---

### 3. Protection contracts are economically incoherent

The proposal states a warband protection contract (1 season) pays **80–120s equivalent**. The warband's wages alone for 91 days = **1,306s**. The protection contract covers **7.3% of wages**. Even if food and shelter are included as in-kind payment, the settlement would need to provide free board for 9+ armed men at a value of ~13s/day — which would bankrupt most villages.

These contracts are currently unplayable as primary income. They are designed as prestige or stability trades, but the text does not flag them as such.

---

### 4. The caster economy has no premium

An Initiate caster (6s/day midpoint) costs **2,190s/year**. An Adept costs **5,475s/year**. Neither the contract types nor the bounty tables provide a caster-premium multiplier. A band with a caster must earn the extra wage cost from the same contract pool as a band without one.

The Adept's annual wage cost (5,475s) exceeds the entire annual income of the standard warband (1,524s) by more than 3×. There is no economic path to hiring one.

---

### 5. Break-even requires contracts to pay ~4× more than they currently do

| Variable                          | Value                       |
| --------------------------------- | --------------------------- |
| Annual expenses (wages only)      | ~5,484s                     |
| Mean days on contract             | 98                          |
| Required daily rate to break even | **55.8s/day**               |
| Actual daily rate on contract     | **14.1s/day**               |
| Gap                               | **41.7s/day (~297% short)** |

Closing the gap requires either contracts paying ~4× more OR the band being on contract ~4× more of the year (i.e., always working, no dead time).

---

### 6. Tribute pressure is real but numerically small

Tribute income is only 2% of total (31s/year mean). But when the band has no contract and no incoming work, the simulation shows them turning to tribute extraction **precisely because it is the only available income**. This is an emergent pressure the system creates without intending to: captains who follow the rules will still be economically incentivized toward extortion because no other income exists during idle periods.

---

## Treasury Over Time (Baseline)

Mean treasury at 25-day checkpoints across all runs:

| Day | Mean (s) | P10 | P90 |
| --- | -------- | --- | --- |
| 0   | 87       | 86  | 87  |
| 25  | 72       | 0   | 202 |
| 50  | 96       | 0   | 277 |
| 75  | 106      | 0   | 308 |
| 100 | 101      | 0   | 281 |
| 125 | 86       | 0   | 317 |
| 150 | 56       | 0   | 194 |
| 175 | 47       | 0   | 147 |
| 200 | 54       | 0   | 210 |
| 225 | 48       | 0   | 171 |
| 250 | 55       | 0   | 205 |
| 300 | 83       | 0   | 288 |
| 350 | 85       | 0   | 336 |

The P10 band hits 0 by day 25 and stays there. Median stays near 0 or below through the year. The P90 band is the outlier — a lucky run that found early high-paying contracts and maintained surplus. Most bands are grinding at empty.

---

## Design Verdict

**The V1 daily-wages model is not a sustainable economy.** It creates a system where:

- Most bands collapse before year-end unless they get extremely lucky contract timing in the first 30 days
- Surviving bands carry near-zero treasury most of the year, one engagement away from collapse
- The only way to operate without collapse is to always be on contract — which the world does not support
- Tribute/extortion is structurally incentivized as a fallback whether or not the captain chooses it morally

The system correctly identifies the _structure_ of the pressure (pay, feed, find work) but misaligns the numbers enough that the pressure becomes an inevitable death spiral rather than a meaningful tension.

**See:** `proposals/proposal-band-pay-retainer-model.md` for the V2 fix proposal.
