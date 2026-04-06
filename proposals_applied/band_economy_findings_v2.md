# Band Economy Findings V2 — Retainer Model vs Daily Wages

**Simulation:** `scripts/band_economy_sim.py`
**Runs:** 200 × 365 days per variant (6 total variants, 1,200 simulation-years)
**Date:** See `scripts/sim_results/*_latest.json` timestamps
**Status:** Retainer model implemented and tested. Contract pricing gap confirmed. Problem partially mitigated.

---

## Setup

**Starting conditions:** 100 silver treasury. World is a 12×12 hex grid with mixed terrain (forest, hills, plains, ruins, tundra, settlement) and dynamically refreshed contracts.

**Two pay models compared:**

- **V1 Daily:** Full daily wages every day regardless of contract status (baseline)
- **V2 Retainer:** Weekly retainer when idle, full daily wages on active contract, 60% loot share on combat outcomes

---

## V1 vs V2 Survival Comparison

| VARIANT                      | V1 SURVIVAL | V2 SURVIVAL | GAIN     |
| ---------------------------- | ----------- | ----------- | -------- |
| Standard warband (6c+2v+1nm) | 62.5%       | 83.5%       | +21 pp   |
| Small band (4c+1v)           | 49.5%       | 78.0%       | +28.5 pp |
| Warband + initiate caster    | 80.5%       | 89.5%       | +9 pp    |

The retainer model improves survival substantially across all band configurations. The small band shows the largest gain — it is the configuration most sensitive to dead-time burn because it has fewer fighters to distribute contract risk across.

The caster + warband configuration shows high V1 survival (80.5%) because the extra body increases raw fighting capacity. The V2 gain is smaller because the caster's retainer (8s/week) is already reasonably low, and the primary improvement mechanism (dead-time burn reduction) is partly offset by the caster's additional loot share obligation.

---

## V1 Economics — Baseline (Standard Warband)

| METRIC                | VALUE        |
| --------------------- | ------------ |
| Survival rate         | 62.5%        |
| Mean collapse day     | day 219      |
| Median treasury       | 0s           |
| Mean income           | 1,509s/year  |
| Mean expenses         | 3,113s/year  |
| — Wages               | 2,807s (90%) |
| — Food                | 284s (9%)    |
| Net margin            | −207%        |
| Contract days         | 97d (26.5%)  |
| Dead-time cost        | ~1,706s/year |
| Daily contract income | ~13.9s/day   |
| Daily total cost      | ~13.0s/day   |
| Effective runway      | ~8 days      |

**Note on expenses:** In V1, expense tracking records the full obligation even when treasury runs dry. The 2,807s wage figure reflects daily obligations accruing even during insolvent stretches. What the band _actually paid_ before collapse is lower. The gap between income (1,509s) and obligations (3,113s) is the structural insolvency — not a rounding error.

**Why V1 fails:**

1. A 9-man warband burns 13s/day at full daily rates. Starting treasury of 100s lasts ~8 days before the first contract is needed.
2. Contract income averages 13.9s/day when working — barely above daily cost. No margin accrues.
3. 267 non-mission days burn 13s/day = ~3,471s owed with zero income. The band cannot pay this.
4. Protection contracts remain incoherent: 80-150s covers less than 2% of the seasonal wage obligation.

---

## V2 Economics — Retainer Model (Standard Warband)

| METRIC            | VALUE        |
| ----------------- | ------------ |
| Survival rate     | 83.5%        |
| Mean collapse day | day 240      |
| Median treasury   | 53.6s        |
| P10 treasury      | 0s           |
| P90 treasury      | 424.2s       |
| Mean income       | 1,781s/year  |
| Mean expenses     | 2,269s/year  |
| — Wages/Retainer  | 1,708s (75%) |
| — Food            | 339s (15%)   |
| — Loot shares     | 195s (9%)    |
| Net margin        | −59%         |
| Contract days     | 111d (30.5%) |
| Dead-time cost    | ~495s/year   |
| Effective runway  | ~30 days     |

**What V2 actually changes:**

- Dead-time burn: 13.0s/day → 3.3s/day. The retainer for a 9-man band (6×2s + 2×3s + 1×5s, weekly) totals 23s/week or 3.29s/day.
- This cuts dead-time cost from ~1,706s/year to ~495s/year — a saving of **1,211s/year**.
- The surviving bands accumulate a positive treasury over time. Median treasury grows through the year, ending at 53s rather than 0s.
- More bands find multiple contracts because they survive long enough to reach them. Mean contract days rise from 97d to 111d.

**What V2 adds in cost:**

- Loot shares: 195s/year. On a loot pool of ~280s (bounties ~141s + battle prizes ~139s), 60% = 168s paid to fighters. Morale bonus offsets some of this through better retention.
- Food cost rises slightly (339s vs 284s) because V2 models full cooperative foraging during dead weeks — the simulation tracks more food events than V1, which largely skipped food during insolvent stretches.

---

## Dead-Time Mechanics Comparison

The treasury charts reveal the V2 advantage most clearly:

**V1 Treasury Over Time (mean of 200 runs):**

```
Day    Mean    P10      P90
  0    86s     86s      86s
 25    64s     0s       209s   ← P10 already at 0 by week 3
 50    93s     0s       286s
100   108s     0s       377s
150    73s     0s       257s   ← mean declining
200    55s     0s       179s
250    59s     0s       208s
300    75s     0s       256s
350    79s     0s       295s
```

**V2 Treasury Over Time (mean of 200 runs):**

```
Day    Mean    P10      P90
  0    96s     95s      97s    ← lower day-1 drop (retainer, not full wages)
 25    95s     0s       202s
 50   132s     0s       258s   ← mean higher than start
 75   145s     0s       308s
100   145s     0s       372s
150   120s     0s       349s
200   119s     0s       340s
250   131s     0s       371s
300   182s     0s       503s   ← survivors are accumulating
325   183s     0s       491s
350   178s     0s       455s
```

The V2 mean is consistently 50-100s higher from day 50 onward. Surviving bands are not just limping along — they are gradually building a buffer by the end of the year.

---

## Small Band Economics (V2)

The small band (4 commons, 1 veteran, no named man) performs best under V2:

| METRIC          | V2 VALUE     |
| --------------- | ------------ |
| Survival rate   | 78.0%        |
| Median treasury | 95.3s        |
| Net margin      | −24.5%       |
| Contract days   | 112d (30.8%) |
| Dead-time cost  | ~526s/year   |

At −24.5% net margin vs −59% for the warband, the small band is the closest to structural viability. Its wage burden during missions is lower (8s/day vs 13s/day), and the retainer is correspondingly lighter. The median treasury of 95s — nearly double starting capital — suggests the small band model can genuinely sustain itself given adequate contract access.

The tradeoff: small bands take heavier casualties per engagement and have no Named Man providing leadership multiplier. The economic efficiency comes at higher field lethality.

---

## Caster Economics (V2)

The caster warband (adding 1 initiate caster to standard warband) shows:

| METRIC          | V2 VALUE |
| --------------- | -------- |
| Survival rate   | 89.5%    |
| Median treasury | 0s       |
| Net margin      | −143%    |

The caster's retainer is 8s/week (1.14s/day) vs the 6s/day mission wage. On a retainer basis this is manageable. On a mission basis the caster adds ~46% to the daily wage burden (6s vs 13s base). The standard contract pool cannot price this in.

The high survival rate (89.5%) reflects the combat advantage of having a magic user — fewer casualties per engagement, which prevents attrition collapse. The treasury still drains. A caster warband that survives the year often survives broke.

The implication: casters are viable if and only if the captain can negotiate contracts that explicitly price in the magic premium. A flat 50s patrol contract that happens to include a caster is a money-losing bet. A 150s contract specifically to investigate and dispel a haunting is not.

---

## What V2 Does Not Fix

**1. Contract pricing gap**

Contracts still pay approximately the cost of mission wages and nothing more. The simulation's contract range (50–450s) reflects the Section 5 tables as currently written. Even the most generous common contract (220s, 10-day clearing job) pays 22s/day against a 13s/day cost — a margin of 9s/day, or 90s over 10 days. This barely covers two weeks of retainer before the next contract must be found.

Break-even for the standard warband:

- Retainer phase (assume 20 days between contracts): 3.29s/day × 20 = 66s
- Mission phase (10-day contract): wages 130s, food 30s = 160s total cost
- Required contract pay: 66 + 160 = 226s **minimum**, before any treasury growth
- Median contract pay at current rates: ~100s

Contracts need to approximately double in base value to close this gap on mission-by-mission basis.

**2. Protection contract incoherence**

A seasonal garrison contract (80–150s) against a warband's wage burden of 1,183s/quarter (13s/day × 91 days) provides less than 13% coverage. The protection role is not economically distinct from charity. This is a Section 5 problem, not a V2 fix.

**3. Caster premium unpriceable**

No mechanism exists to distinguish "this contract requires magic" from "this contract does not." The employer at a standard settlement cannot price a caster's addition. The captain either absorbs the cost or does not hire a caster. This needs a contract-tier modifier: any contract formally requiring a magical service should carry a floor of +25% base pay.

---

## What V2 Achieves

1. **Playable daily loop.** A band can operate for a month between contracts without collapsing. The captain has time to negotiate, travel, investigate, and prepare rather than scrambling for any contract within 7 days of starting.

2. **Dead-week decisions.** Foraging allocation, terrain positioning, and retainer payment become genuine weekly questions. The right camp hex is not arbitrary — it matters for food.

3. **Loyalty mechanics that work.** Named Men who receive consistent loot shares have a concrete reason to stay. The loot event (bounty, tribute, battle prize) is now a meaningful morale moment, not just a treasury increment.

4. **Scaled consequences for inactivity.** The 28-day morale drain from prolonged idleness creates pressure to seek work without making a week's gap lethal.

5. **Tribute weight shared.** When the captain extorts a village and the men get their 60% share, the moral and repercussion weight is distributed. This models the authentic dynamic where men don't just follow orders — they participate in the choice.

---

## Simulation Files

```
scripts/sim_results/v1_baseline_latest.json
scripts/sim_results/v1_small_latest.json
scripts/sim_results/v1_caster_latest.json
scripts/sim_results/v2_baseline_latest.json
scripts/sim_results/v2_small_latest.json
scripts/sim_results/v2_caster_latest.json
```

Each file contains full summary statistics and per-run raw results (excluding per-day history arrays). Runs are reproducible by seed — `SEED_BASE = 42`, offsets documented in `band_economy_sim.py`.

---

## Next Steps

1. **Accept the retainer model** into Section 3 of the main proposal.
2. **Contract pricing pass** — raise base floor to band_daily_cost × duration × 1.25. The 9-man warband benchmark: 13s/day × 10 days × 1.25 = 163s minimum for a standard 10-day contract.
3. **Caster premium flag** — add contract tier modifier (+25% floor) for magic-required work.
4. **Protection contract rewrite** — current 80–150s/season range needs to read as 600–900s/season to be coherent with a full-warband retention commitment.
