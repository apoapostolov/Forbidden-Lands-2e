# Mercenary Economy Model — Design Audit (Updated V7)

**Scope:** `proposals/proposal-mercenary-band-management.md` — economic model, caster costs, barter/liquidity, and player-facing silver linings.

**Audit status:** All items below have been implemented. V7 simulation results confirm the model is in the target zone.

---

## Simulation Results Summary

| Model                 | Variant                   | Survival  | Margin    | Treasury P50 | Treasury P10 |
| --------------------- | ------------------------- | --------- | --------- | ------------ | ------------ |
| V3 (baseline)         | Standard warband          | 95.5%     | +18.0%    | 868s         | 57s          |
| V6 (struggling world) | Standard warband          | 88.5%     | +3.6%     | 474s         | 0s           |
| **V7 (audit model)**  | **Standard warband**      | **94.0%** | **+2.8%** | **435s**     | **0s**       |
| V7                    | Small band                | 88.0%     | +22.1%    | 642s         | 0s           |
| V7                    | Warband + Initiate caster | 100.0%    | −2.5%     | 431s         | 0s           |

**V7 income breakdown (standard warband, mean):** contracts 1,924s + bounties 172s + call-up 77s + windfall 43s + tribute 6s = 2,222s total
**V7 expense breakdown:** wages 1,511s + food 385s + loot shares 219s + maintenance 10s + injury treatment 12s = 2,159s total
**Net:** +63s/year. Survival 94%. P10 treasury at year-end is 0s — roughly a quarter of bands spend the year on the edge.

---

## 1. Perpetual Struggle — RESOLVED

**What the audit found:** V3 at +18% margin, 868s median treasury. Protection (season) at 550–800s against ~625s costs generated +250–500s net per contract and acted as a circuit breaker against the rest of the model's natural pressure.

**What was changed:**

- **Protection season repriced: 550–800s → 310–420s.** Fee now covers retainer wages (~310s) only. Food is on the band. At mid-range pay (365s) in forest terrain with 70% foragers, the band breaks even on food and nets ~195s. In plains or ruins, they take a loss. The season is a holding arrangement, not a cash contract.
- **Combat call-up added:** When a real engagement happens during a protection season, the captain invoices mission pay (full daily rate per active day) plus a threat bonus of 30–80s per resolved fight. The sim models this as 2 days mission pay + ~55s avg bonus. Mean call-up income: 77s/year.
- **Equipment maintenance added:** 1.5s/man/season if 3+ engagements occurred. Mean cost: ~10s/year for a standard warband. Scales with roster.
- **Injury treatment added:** 3s per combat casualty. Mean cost: ~12s/year. Scales with fight frequency.
- **Winter scarcity added:** Q4 (days 274–364) contract availability halved (55% → 27.5%). Patrol/escort/clearing volume drops. Garrison and protection unaffected. Bands without a protection season locked in going into winter face a lean quarter.
- **Windfall events added:** 8.3% chance per non-garrison contract completion. Mean windfall income: 43s/year.

**V7 result:** +2.8% margin (+63s/year), 94% survival, P10 = 0s. The model runs lean but not ruinous. Roughly a quarter of bands spend significant periods with empty or negative treasury. The failure cases (6% collapse) now cluster to bands that go months without a contract in winter. Both outcomes — scraping through and collapsing — follow from real decisions the captain can see coming.

---

## 2. Casters — RESOLVED

**What the audit found:** The math already breaks Adept+ at coin rates but the text was soft about it.

**What was changed:**

- **Caster coin sustainability section added** after Hiring a Caster. States the arithmetic explicitly: an Adept at 12–18s/day = 360–540s/month, exceeding a normal warband's contract income by month 2. End-of-period check: if projected 30-day coin cost exceeds 25% of mean income over the last 60 days, the caster sets a 14-day deadline.
- **Master coin terms stated outright as unsustainable.** 750+s/month against a protection season that pays 310–420s for 91 days. Text now says this clearly.
- **V7 caster band result:** 100% survival, –2.5% margin (–80s/year). An Initiate caster on coin terms at this model's contract rates costs just enough to push a caster band slightly negative on mean expectation. Individual runs vary — strong windfall or call-up months offset the caster cost. This is the intended pressure point.

---

## 3. Barter — RESOLVED

**What the audit found:** A single treasury meant goods and coin were mechanically identical.

**What was changed:**

- **In-kind payment rule added** to the FIELD NON-PAYMENT section: first consecutive in-kind pay = no consequence; second = +1 difficulty on next non-payment check; third = roll immediately at standard difficulty.
- The existing goods payment table (Payment in Goods, Section 5) already had conversion delays and discounts by category. The in-kind payment rule creates the mechanical tension: goods are slow, silver is immediate, and men waiting for coin do not wait indefinitely.

_(The two-line silver/goods balance sheet remains a recommended GM tracking practice rather than a hard mechanical rule; the in-kind non-payment escalation covers the functional need.)_

---

## 4. Silver Linings — RESOLVED

**What was built:**

| Mechanic                                                        | Location                     | Mean Annual Value           |
| --------------------------------------------------------------- | ---------------------------- | --------------------------- |
| Windfall table (D6, contract completion)                        | Section 3 / after Loot Share | 43s                         |
| Ransom mechanics (captive value, negotiation, resolution)       | Section 3 / after Windfall   | Captive-dependent (25–400s) |
| Combat call-up during protection season                         | Section 5 / garrison prose   | 77s                         |
| Reputation → opening rates (+5% per Renown above 2)             | Section 5 / negotiations     | Scales with band age        |
| Named Man contact-sourcing (3+ months + Loyalty 5, once/season) | Section 7                    | Contract-dependent          |

The windfall and call-up mechanics together contribute ~120s/year to the V7 mean income. That is roughly 5.4% of total income — enough to matter in a lean year, not enough to replace contract discipline.

---

## Summary — Before and After

| Area                       | V3 Status                | V7 Status                                     |
| -------------------------- | ------------------------ | --------------------------------------------- |
| Base margins               | +18% — too comfortable   | +2.8% — near break-even                       |
| Protection season          | 550–800s profit contract | 310–420s retainer-only; combat earns extra    |
| Maintenance / injury costs | Not modelled             | ~22s/year combined; scales with activity      |
| Winter scarcity            | Not modelled             | Q4 availability halved                        |
| Caster coin sustainability | Text was soft            | Arithmetic stated; deadline mechanic added    |
| Barter friction            | No teeth                 | In-kind escalation rule added                 |
| Windfall events            | Sketch only              | Full table with triggers                      |
| Ransom                     | Referenced only          | Full mechanics: tiers, logistics, negotiation |
| Reputation → pay           | Not connected            | +5%/Renown above 2 on employer opening offer  |
| Named Man value            | Combat only              | Contact-sourcing (once/season mechanic)       |

The V7 model sits where V3's audit said it should: survival high enough that the band is a viable campaign spine, margins low enough that every protection season accepted and every fight avoided is a real decision with consequences the players can feel.
