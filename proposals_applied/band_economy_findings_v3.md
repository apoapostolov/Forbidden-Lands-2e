# Band Economy Findings V3 — Retainer + Repriced Contracts + Caster Utility

**Simulation:** `scripts/band_economy_sim.py`
**Runs:** 200 × 365 days per variant (9 total variants, 1,800 simulation-years)
**Date:** See `scripts/sim_results/*_latest.json` timestamps
**Status:** All three configurations positive-margin. Caster variant achieves 100% one-year survival.

---

## Setup

**Starting conditions:** 100 silver treasury. World is a 12×12 hex grid with mixed terrain and dynamically refreshed contracts.

**Three pay models compared:**

- **V1 Daily:** Full daily wages every day regardless of contract status (baseline)
- **V2 Retainer:** Weekly retainer when idle, full daily wages on active contract, 60% loot share
- **V3 Retainer+:** V2 structure with repriced contracts, garrison mode, caster premium, caster-specific contracts

---

## Full Three-Model Comparison

### Standard Warband (6 commons, 2 veterans, 1 named man)

| METRIC                  | V1 DAILY WAGES | V2 RETAINER  | V3 RETAINER+     |
| ----------------------- | -------------- | ------------ | ---------------- |
| Survival rate (1 year)  | 62.5%          | 83.5%        | **95.5%**        |
| Median final treasury   | 0s             | 54s          | **868s**         |
| P10 treasury            | 0s             | 0s           | 0s               |
| P90 treasury            | 192s           | 424s         | **1,518s**       |
| Mean annual income      | 1,509s         | 1,781s       | **2,676s**       |
| — Contracts             | 1,345s         | 1,617s       | **2,476s**       |
| — Bounties              | 131s           | 141s         | **197s**         |
| Mean annual expenses    | 3,113s         | 2,269s       | **2,195s**       |
| — Wages/Retainer        | 2,807s         | 1,708s       | **1,524s**       |
| — Food                  | 284s           | 339s         | 382s             |
| — Loot shares           | —              | 195s         | **267s**         |
| Net margin              | −106%          | −27%         | **+18%**         |
| Annual net cash flow    | −1,604s        | −488s        | **+481s**        |
| Days on contract        | 97d (26.5%)    | 111d (30.5%) | **234d (64.1%)** |
| Dead-time runway (100s) | ~8 days        | ~30 days     | ~30 days         |

### Small Band (4 commons, 1 veteran)

| METRIC                 | V1 DAILY WAGES | V2 RETAINER  | V3 RETAINER+     |
| ---------------------- | -------------- | ------------ | ---------------- |
| Survival rate (1 year) | 49.5%          | 78.0%        | **85.0%**        |
| Median final treasury  | 0s             | 95s          | **989s**         |
| P90 treasury           | 261s           | 590s         | **1,724s**       |
| Mean annual income     | 1,564s         | 1,724s       | **2,465s**       |
| Mean annual expenses   | 2,337s         | 1,879s       | **1,690s**       |
| Net margin             | −49%           | −9%          | **+31%**         |
| Annual net cash flow   | −773s          | −155s        | **+775s**        |
| Days on contract       | 100d (27.4%)   | 112d (30.8%) | **216d (59.3%)** |

### Warband with Initiate Caster (6 commons, 2 veterans, 1 named man, 1 caster)

| METRIC                 | V1 DAILY WAGES | V2 RETAINER | V3 RETAINER+     |
| ---------------------- | -------------- | ----------- | ---------------- |
| Survival rate (1 year) | 92.0%          | 96.5%       | **100.0%**       |
| Median final treasury  | 0s             | 0s          | **822s**         |
| P10 treasury           | 0s             | 0s          | 9s               |
| P90 treasury           | 0s             | 140s        | **1,532s**       |
| Mean annual income     | 1,340s         | 1,574s      | **3,675s**       |
| — Contracts            | 1,208s         | 1,406s      | **3,465s**       |
| Mean annual expenses   | 5,510s         | 3,088s      | **3,320s**       |
| — Wages/Retainer       | 5,183s         | 2,526s      | **2,548s**       |
| Net margin             | −312%          | −96%        | **+10%**         |
| Annual net cash flow   | −4,171s        | −1,515s     | **+356s**        |
| Days on contract       | 87d (23.9%)    | 98d (26.8%) | **243d (66.5%)** |

---

## V3 Mechanics — What Changed and Why

### 1. Contract Pricing Reform

**Problem confirmed in V2:** Contracts paid ~1.08× mission wage cost, leaving nothing to cover retainer periods. Garrison-short (21-day) contracts paid 80–150s against a 273s wage obligation — the captain would lose money by accepting them.

**V3 formula:** `floor = 13s/day × duration × 1.25`

| CONTRACT TYPE        | V2 RANGE | V3 RANGE | DELTA      |
| -------------------- | -------- | -------- | ---------- |
| Patrol (7d)          | 50–90s   | 110–165s | +83%       |
| Escort (5d)          | 60–130s  | 80–140s  | +8%        |
| Clearing (10d)       | 100–220s | 160–260s | +28%       |
| Garrison-short (21d) | 80–150s  | 340–500s | +241%      |
| Warchief Raid (14d)  | 200–450s | 225–380s | floor +12% |

The garrison-short correction (+241%) is the most significant individual fix. At the old rate, a captain working purely on 21-day garrison contracts would lose 120–180s per cycle. At the new rate, the same work produces roughly 40–200s surplus per cycle.

### 2. Protection Season (Garrison Mode)

A new 91-day contract type, `protection_season`, with a flat rate of 550–800s. The band remains on retainer during this period — not mission pay. Cost structure:

- Band daily cost at retainer: ~3.3s/day × 91d = ~300s wages
- Food: ~3.5s/day × 91d = ~319s
- Total band cost for 91 days: ~619s
- Income: 550–800s (pays in advance, not daily)

Net position ranges from −69s (low payout + high food costs) to +181s, with a median near +40–80s. This is _not_ a profit center on its own, but it:

- Provides a long unbroken period of contract coverage (64% of the year in V3 vs 27% in V1)
- Eliminates mercenary idle-time for three months, reducing morale risk
- Provides predictable income for foraging cost estimation

The simulation shows bands spending 234 days/year on active contracts in V3. A protection season contract (91 days) followed by two or three short clearing or patrol contracts covers most of the remaining working calendar.

### 3. Bounty Repricing

All bounty rates approximately doubled. Old rates were calibrated against a V1 economy where a clearing contract paid 100–220s; bounties at 5–15s were therefore meaningful relative rewards. At V3 contract rates, a 5–15s bounty is noise.

| BOUNTY TYPE         | V2 RANGE | V3 RANGE |
| ------------------- | -------- | -------- |
| Local criminal      | 5–15s    | 12–30s   |
| Named bandit        | 10–25s   | 25–60s   |
| Deserter            | 2–5s     | 5–12s    |
| Warlord enemy       | 50–200s  | 80–300s  |
| Professional breach | 10–30s   | 25–60s   |

Bounty income in V3 standard warband: 197s/year (vs 131s in V1, 141s in V2). The increase reflects both higher rates and higher contract volume (more missions = more opportunities to pick up bounties in the field).

### 4. Caster Economics

**V2 caster finding:** The caster's wage (6s/day mission, 8s/week retainer) was unrecoverable. Contracts did not pay enough extra to justify the additional fighter. The V2 caster warband median treasury was 0s after a full year despite 96.5% survival — the band was perpetually insolvent.

**V3 caster mechanisms:**

1. **Casualty reduction (−40%)**
   - Normal combat: 8% injury rate → 4.8%
   - Hard combat: 15% death rate → 9%
   - Fewer casualties means fewer replacement costs (~3–8s per man), fewer death-morale rolls, and longer band composition stability

2. **Contract premium (+35%)**
   - All standard contracts pay 35% more when the band has a caster
   - A clearing contract (160–260s) becomes 216–351s
   - A garrison-short (340–500s) becomes 459–675s
   - This directly offsets the mission-wage cost premium

3. **Caster-specific contracts**
   - `magical_commission` (12d, town employer): 280–420s — only accessible to caster bands
   - `ritual_ward` (8d, warchief employer): 185–300s — only accessible to caster bands
   - These represent work that a non-caster band simply cannot do

**V3 caster result:** 100% one-year survival. +356s annual net cash flow. Median treasury 822s. The caster earns their cost.

---

## Treasury Trajectory — V3 Standard Warband

| DAY | MEAN | P10 | P90    |
| --- | ---- | --- | ------ |
| 0   | 97s  | 95s | 97s    |
| 50  | 153s | 0s  | 384s   |
| 100 | 282s | 0s  | 623s   |
| 150 | 452s | 19s | 767s   |
| 200 | 525s | 34s | 914s   |
| 250 | 646s | 37s | 1,085s |
| 300 | 695s | 55s | 1,159s |
| 350 | 840s | 54s | 1,503s |

**Pattern:** Steady climb after day 50, accelerating after day 100 as bands clear their initial dead-time risk period. By month 6, a surviving band has typically completed one protection season (550–800s) and two or three short contracts — the cumulative surplus shows in the P50 rising past 450s by day 150.

Contrast with V1: median treasury was 0s at every measurement point throughout the year. The V3 treasury chart shows a band successfully operating as a going concern, not perpetually insolvent.

---

## Residual Problems

### What V3 does not fully fix

1. **P10 treasury still hits 0s by day 25.** Early-game luck still matters. A band that draws two travel-intensive low-pay contracts in the first two weeks can go insolvent before the garrison market opens. This is a feature of the simulation's starting randomness, not a structural flaw — bands can choose to move toward better contract pools.

2. **Contract income per mission day: 10.6s vs 13.0s total daily cost.** The contracts cover ~81% of mission-time costs. The surplus from contracts comes from garrison seasons and caster-premium contracts, not from the daily average. A band that only takes patrol and escort work and never takes a garrison arrangement will still run thin.

3. **Adept caster wages (15s/day) not tested.** The simulation uses initiate caster rates (6s/day). An adept caster doubles the daily cost. The caster-specific contracts and premium would need to scale further to justify adept rates. This is left for a separate proposal.

4. **85.0% small band survival** (vs 95.5% warband). Small bands are more vulnerable to early-game bad draws. The protection season contract is their escape — 91 days of guaranteed income from a single arrangement. Small bands that find and accept a garrison arrangement tend to survive long-term; those that do not face uneven competition for the patrol/escort/clearing pool.

---

## Design Validation

**Three-model progression tells a clear story:**

- V1: Insolvent. The system does not model a functional mercenary economy.
- V2: Survivable but marginal. Dead-time solved; contract pricing still broken.
- V3: Functional. All configurations positive-margin, caster justified, treasury accumulates.

**What "functional" means here is limited.** The simulation models one year. The Ravenlands is not a place where mercenaries grow rich — the P10 treasury at 0s reminds you that a string of bad luck still kills the band. The design target is a band that:

- Can survive a full year without extraordinary luck (V3: 95.5% standard, 100% caster)
- Accumulates a working treasury over time (V3: 868s median at year-end vs 0s in V1)
- Has decisions that matter (garrison vs. patrol, terrain selection during dead weeks, caster value vs. cost)

V3 delivers all three.

**The caster result is the strongest single finding.** V2 caster warband: −96% margin, 0s median treasury after 96.5% survival — technically alive, economically dead. V3 caster warband: +10% margin, 822s median treasury, 100% survival. The mechanism is explicit and testable: caster reduces casualty rate by 40%, negotiates +35% on contracts, unlocks contract types. Each component has a direct mechanical representation in the rules.

---

## Files

- `scripts/sim_results/v3_baseline_latest.json` — standard warband V3
- `scripts/sim_results/v3_small_latest.json` — small band V3
- `scripts/sim_results/v3_caster_latest.json` — warband + caster V3
- `proposals/proposal-band-pay-retainer-model.md` — full design proposal with V1/V2/V3 comparison
