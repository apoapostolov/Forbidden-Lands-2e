# Band Economy Simulation — V4 Findings

**Model:** V4 — Retainer-Wage (5-Day Week) + Employer Cost-Cutting  
**Runs:** 200 × 365 days | Starting treasury: 100s  
**Contracts/bounties:** V3 pricing (floor = daily_wage × duration × 1.25)

---

## What V4 Tests

V4 asks: what happens if retainer is set to a **5-day working week** — full daily wage × 5, not the deep-discount flat rate from V2 — while the employer offsets dead-time costs through food subsidies?

Three changes over V3:

| Change | Mechanic | Effect |
|---|---|---|
| Retainer-wage | Fighters paid 5 of 7 days during dead weeks (casters: 4 of 7) | Dead-time cost rises sharply |
| Garrison food subsidy | Employer boards the band during protection-season contracts (food cost = 0) | Reduces garrison contract costs by ~145s |
| Settlement billet | Idle in a settlement hex: food cost −30% | Minor savings on idle days |

---

## Results

### Standard Warband (6 common + 2 veteran + 1 Named Man)

| Model | Survives | Margin | Contract days | Treasury P50 |
|---|---|---|---|---|
| V1 daily wages | 62.5% | −106.3% | 97d / 26.5% | 0s |
| V2 flat retainer | 83.5% | −27.4% | 111d / 30.5% | 54s |
| **V3 repriced** | **95.5%** | **+18.0%** | **234d / 64.1%** | **868s** |
| V4 retainer-wage | 88.0% | −29.1% | 223d / 61.0% | 285s |

### Small Band (4 common + 1 veteran)

| Model | Survives | Margin | Contract days | Treasury P50 |
|---|---|---|---|---|
| V1 daily wages | 49.5% | −49.4% | 100d / 27.4% | 0s |
| V2 flat retainer | 78.0% | −9.0% | 112d / 30.8% | 95s |
| **V3 repriced** | **85.0%** | **+31.4%** | **216d / 59.3%** | **989s** |
| V4 retainer-wage | 69.5% | −0.0% | 196d / 53.6% | 386s |

### Warband + Caster

| Model | Survives | Margin | Contract days | Treasury P50 |
|---|---|---|---|---|
| V1 daily wages | 92.0% | −311.4% | 87d / 23.9% | 0s |
| V2 flat retainer | 96.5% | −96.3% | 98d / 26.8% | 0s |
| **V3 repriced** | **100.0%** | **+9.7%** | **243d / 66.5%** | **822s** |
| V4 retainer-wage | 99.0% | −40.6% | 221d / 60.4% | 141s |

### Dead-Time Burn (standard warband)

| Model | Retainer rate | Runway on 100s |
|---|---|---|
| V1 | 13.0s/day (full daily) | ~8 days |
| V2 | 3.3s/day (flat discount) | ~30 days |
| **V4** | **9.3s/day (5/7 of daily)** | **~11 days** |

---

## What the Numbers Mean

### V4 is not crippled. V4 is expensive.

V4 survival for the standard warband drops 7.5 percentage points from V3 (88.0% vs 95.5%). Its margin goes from +18% to −29%. Food costs collapse from ~381s to ~145s per year — garrison subsidy and billet discount work. But the retainer-wage increase swamps those savings.

Dead-time wages in V4: ~841s/year. In V2: ~495s/year. In V1: ~1706s/year.  
V4 sits between V2 and V1, much closer to V1.

**The garrison food subsidy alone saves roughly 235s per year in food costs.** That is real. But it does not offset 346s of extra retainer.

### The caster band holds up best

V4 caster warband survives at 99.0% — nearly identical to V3's 100%. The caster's 4-day retainer rate (24s/week vs a 5-day rate of 30s/week) keeps caster dead-time manageable. The garrison and billet subsidies further reduce food costs from 427s (V3) to 190s (V4). Result: V4 is painful for casters too, but not catastrophic.

### The small band breaks even

V4 small band margin: −0.0% (effectively zero). Treasury P50: 386s. This is the closest V4 gets to viability — a 5-man band spending 53.6% of the year on contract, with food costs nearly eliminated (121s vs 332s in V3), barely covering the higher retainer.

---

## Design Verdict

V4 retainer-wage is **not viable as a design default.** The 5-day rate is too expensive relative to V3 contract income for standard and caster warbands. The cost-cutting measures (garrison subsidy, billet discount) work correctly but cannot compensate.

**What V4 does prove:**

1. The garrison food subsidy is a meaningful mechanic worth keeping. 235s food savings per year is roughly 27 days of V3 retainer cost — enough to matter in a tight season.
2. Caster specialist rate (4-day retainer, not 5-day) is worth the design space. It differentiates caster contracts narratively and reduces the fiscal penalty of carrying magical support.
3. Settlement billet discount is marginal (food is already cheap in V4 due to high foraging). It may have more impact under V2 or in a V5 with terrain-sensitive foraging.

---

## Employer Cost-Cutting: Findings and Proposals

### Implemented in V4 (simulated)

**Garrison food subsidy** — employer boards the band during protection-season deployments. Full food cost removed. This is the strongest lever: a single protection contract saves ~145s in food alone (91 days × reduced food cost). Recommended to keep.

**Settlement billet discount** — idle bands in a settlement hex pay 30% less for food. Lower impact than garrison subsidy; primarily useful during long idle stretches. Worthwhile as a low-maintenance rule element.

**Caster specialist rate** — casters on 4/7 retainer instead of 5/7. Justified: a caster maintains private practice and earns side income between deployments. Reduces adept caster dead-time cost from 75s/week to 60s/week.

### Proposed (not simulated)

**Named Man agenda waiver** — a Named Man pursuing an active Agenda may surrender their retainer in exchange for the captain's active support of that Agenda. Mutual: the captain gains reduced salary obligation; the Named Man gains narrative leverage. This is unquantifiable in a gold simulation but directly supports the loyalty-over-gold design intention.

**Advance payment buydown** — employer pays a lump retainer advance at contract start instead of weekly disbursement. The band receives 3–4 weeks of retainer upfront. Treasury runway extends; the captain can bridge a bad idle stretch without non-payment morale damage. Asymmetric benefit: employer spends the same total but the band survives longer.

**Surplus forage sale** — in exceptional terrain (forest, wetland), a band at full forager allocation produces surplus food. Sell surplus at 50% food price per unit back to locals. Small cash trickle (~10–20s/month in best terrain). Requires terrain-specific foraging tracking, currently outside the simulation's scope.

---

## Recommendation

Keep V3 as the canonical baseline. V4 numbers confirm that the retainer-wage concept requires better contract income to sustain itself — the V3 contract floor is necessary but not sufficient at 5-day retainer costs. If a future revision wants to implement a 5-day retainer, contract income would need to increase by ~25–35% to restore V3-level margins.

The garrison food subsidy and caster specialist rate from V4 are worth integrating into the proposal regardless of which retainer model is adopted. Both are narratively grounded and mechanically clean.
