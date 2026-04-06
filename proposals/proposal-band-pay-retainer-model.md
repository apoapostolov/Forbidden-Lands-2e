---
proposal: Band Pay Model — Retainer, Mission Pay, and Loot Shares
type: Economy Overhaul
status: Proposed
target: proposals/proposal-mercenary-band-management.md — Section 3 (Pay and Provisions)
depends: Section 3 (Field Non-Payment), Section 5 (Contracts), Section 7 (Named Men)
simulation: scripts/band_economy_sim.py — model v2_retainer
findings: analysis/band_economy_findings_v1.md
---

# RETAINER, MISSION PAY, AND LOOT SHARES

## The Problem

The V1 daily-wages model runs all fighters at full daily pay regardless of whether the band has work. A nine-man warband costs 14.3 silver every day it exists. On the 132 days a year (simulation mean) when no contract is active and the band is traveling or searching, that is nearly 1,900 silver burned with zero intake. Annual contract income is roughly 1,380 silver. The band structurally costs more in transit than it earns working.

The result is a system where any captain who does not find a contract within seven days of starting goes insolvent. The math does not describe a difficult profession. It describes an impossible one. The table pressure becomes not "how do you manage a band" but "when do you run out of money." That is not an interesting question.

The underlying truth in the profession is simpler and harsher: men fight when there is a fight. Between fights, they exist on less. They know this when they join. The veteran who has been riding a company through the Ravenlands for four seasons does not expect the same coin in a winter billet as he expects before a raid. He expects to eat and to know his captain is good for the difference when the job comes.

This proposal replaces the single-rate daily wage with a three-part pay structure: **retainer**, **mission pay**, and **loot share**.

---

## The Three-Part Pay Structure

### 1. Retainer (Dead Weeks)

When the band has no active contract — traveling between jobs, in camp between engagements, waiting on word from an employer — fighters receive a **weekly retainer** rather than a daily wage. This is not full pay. It is acknowledgment that they are committed to the band, will not take other work, and will be ready when the call comes.

**Weekly retainer rates:**

| FIGHTER TYPE    | RETAINER (per week) | FULL DAILY PAY (× 7 days) | RETAINER AS % OF FULL |
| --------------- | ------------------- | ------------------------- | --------------------- |
| Common          | 2 silver            | 7 silver                  | 29%                   |
| Veteran         | 3 silver            | 14 silver                 | 21%                   |
| Named Man       | 5 silver            | 21 silver                 | 24%                   |
| Initiate Caster | 8 silver            | 42 silver                 | 19%                   |
| Adept Caster    | 12 silver           | 105 silver                | 11%                   |

Retainer is paid weekly. It is not prorated by day — a man who is retained for five days of the week is retained for the full week for purpose of the retainer fee. Partial weeks at the start or end of a contract are settled on the last day.

**Food during retainer weeks:** The band forages for itself. Men are not on assignment; they have time. Assign the majority of the band as foragers during non-operational days. This covers most or all food costs in decent terrain. In settlement hexes or tundra, the shortfall is purchased from the treasury. See the forager table (Section 4).

**Non-payment threshold during retainer:** 14 days without retainer payment (vs. 7 days for mission pay). Men on retainer have lower immediate expectations — they are not working hard for you. The grievance accumulates slower. But it accumulates.

---

### 2. Mission Pay (Active Contract)

From the day a contract is formally accepted to the day it concludes — whether by completion, breach, or dissolution — fighters receive **full daily wages**. This covers:

- The march to the operational area
- The engagement itself
- Any time spent in the operational hex until the objective is resolved or the employer releases the band

**Daily wages during mission:**

| FIGHTER TYPE    | DAILY WAGE (silver) |
| --------------- | ------------------- |
| Common          | 1                   |
| Veteran         | 2                   |
| Elite           | 3                   |
| Named Man       | 3                   |
| Initiate Caster | 6                   |
| Adept Caster    | 15                  |

Non-payment during mission time: **3 days** unpaid triggers a roll on the Field Non-Payment table (Section 3). The men are working. They expect to be paid for it soon and will not wait.

---

### 3. Loot Share (Combat Outcome)

When the band completes work that produces a material windfall — a bounty paid, goods taken from defeated enemies, tribute successfully extracted, a deceased warlord's treasury recovered — that windfall is divided. It does not all go to the treasury.

This is not charity. It is the reason men fight hard rather than hold back. A man who knows his captain pockets everything still goes to battle. A man who knows there was a haul and he got nothing will have questions the next time blades come out.

**Loot pool:** The full windfall from the event (bounty coin, tribute silver, plunder). Does not include base contract pay — that is wages, not loot.

**Division:**

| SHARE RECIPIENT                    | % OF LOOT POOL |
| ---------------------------------- | -------------- |
| Leader (captain's cut + band fund) | 40%            |
| Named Men collectively             | 30%            |
| Veterans collectively              | 20%            |
| Commons collectively               | 10%            |

Per-man within tier:

- 1 Named Man gets the full 30% of pool.
- 2 Named Men split the 30% equally (15% each).
- Veterans and commons similarly divide their tier's share equally.

**Example:** A band of 6 commons, 2 veterans, 1 named man recovers a 100s bounty.

- Captain: 40s
- Named man: 30s
- Each veteran: 10s
- Each common: 1.67s

The common's cut is small. He knows it is small. That is the nature of rank. What matters is that it is _something_, that the captain paid it without being asked, and that it arrived the same day as the veterans' share.

**If the treasury cannot pay loot shares:** Morale −1. This is treated the same as non-payment. The captain who took 40s for themselves when the men got nothing has created a problem that does not resolve without either coin or a credible explanation.

**What counts as a loot event:**

- A bounty collected and paid
- Tribute extracted (forced or negotiated)
- Goods taken from a defeated enemy force
- A found cache or hoard recovered during a contract

Base contract pay does not trigger the loot split. It goes to the treasury to fund wages and provisioning.

---

## Non-Payment Thresholds (Updated)

| CONDITION            | THRESHOLD               | TABLE                                                   |
| -------------------- | ----------------------- | ------------------------------------------------------- |
| Retainer unpaid      | 14 days                 | Field Non-Payment (Section 3)                           |
| Mission pay unpaid   | 3 days                  | Field Non-Payment (Section 3) — rolled at +1 difficulty |
| Loot shares withheld | Immediate (first event) | Standard MORALE −1; second event triggers full roll     |

The difficulty adjustment on mission non-payment reflects that men are actively engaged, tired, and watching. Patience runs shorter when the work is current.

---

## Foraging During Dead Weeks

When no active contract is running, the band sustains itself through cooperative foraging. This is not the limited 30% assignment used during a contract — it is the band's primary activity between jobs.

**Dead-week forager allocation:** Assign up to 70% of total band strength as foragers for the Morning Quarter Day. The remainder handle camp maintenance, equipment, and perimeter.

Use the standard forager table (Section 4) with the higher forager count. In forest and hill terrain, a warband of 9 with 6–7 foragers covers its own food needs with a surplus. In plains, roughly break-even. In ruins or tundra, a shortfall must be purchased.

This creates a terrain decision during dead weeks: bands in bad terrain want to move toward forests or hills to reduce food costs, even if that costs travel time. The foraging calculus is the reason experienced bands camp near forests between contracts rather than setting up permanently near settlement roads.

---

## Integration Notes

**Section 3 (Pay and Provisions):** Replace the single daily-rate table with the retainer/mission/loot structure above. The Field Non-Payment table is unchanged; only the thresholds that trigger it shift.

**Section 5 (Contracts):** Contract acceptance is the trigger point for switching from retainer to mission pay. Record the contract start date. If a contract is disputed (breach, abandonment), mission pay ceases on the breach date and reverts to retainer pending the next arrangement.

**Section 7 (Named Men):** Named Men are the primary beneficiaries of the loot split beyond the captain. Their 30% collective share at single-Named-Man strength (the typical warband) means they receive a significant windfall on successful engagements. This directly reinforces their Loyalty — a Named Man getting their cut consistently is a Named Man who has reason to stay. Flag this in the Named Man Loyalty Score rule: consistent loot payment is equivalent to the "paid on time" morale bonus for Named Man loyalty purposes.

**Section 9 (Atrocities):** Tribute extracted from a settlement is a loot event under this proposal. The captain who extracts tribute but does not distribute the loot split has two problems: the standard Atrocity consequences from the settlement, and an internal MORALE hit from their own men who expected a share. Both arrive simultaneously.

---

## Design Note: What This Solves and What It Does Not

**What the retainer model solves:**

The V1 model's primary failure is burning full wages during dead time. At 14.3s/day, a band that goes 7 days without a contract from its starting treasury of 100s is insolvent. The retainer model reduces dead-time burn to ~3.3s/day, extending the runway to ~30 days and making the basic operating loop viable.

**What the retainer model does not solve alone:**

Contract reward rates. The V2 retainer model improves survival substantially but leaves contracts paying barely above their own wage cost. A full fix requires both the retainer model and a contract pricing pass.

---

## Contract Pricing Reform

**Formula:** `floor pay = band_daily_cost × duration_days × 1.25`

For the standard nine-man warband (daily cost: 13s):

| CONTRACT TYPE         | OLD RANGE   | NEW RANGE    | DURATION | EMPLOYER    |
| --------------------- | ----------- | ------------ | -------- | ----------- |
| Patrol (weekly)       | 50–90s      | 110–165s     | 7d       | Town        |
| Escort                | 60–130s     | 80–140s      | 5d       | Town        |
| Clearing              | 100–220s    | 160–260s     | 10d      | Town        |
| Protection (season)   | 80–150s     | 550–800s     | 91d      | Town        |
| Warchief Raid         | 200–450s    | 225–380s     | 14d      | Warchief    |
| Garrison (short)      | —           | 340–500s     | 21d      | Warchief    |
| Magical Commission    | —           | 280–420s     | 12d      | Town        |
| Ritual Ward           | —           | 185–300s     | 8d       | Warchief    |

**Protection season (fundamental change):** The old "garrison duty" at 80–150s was incoherent — it covered less than 10% of a quarter's wages. The protection season is reframed as: the employer pays a flat fee in advance for having the band available for the quarter. The band remains on **retainer pay** during this arrangement, not mission pay. Daily cost during the season: ~3.3s/day + food. Income: 550–800s flat. Net position: +150s to +400s for the quarter.

**Caster premium:** Bands with a caster negotiate +35% on standard contracts. Employers who want military outcomes improved by magic pay for it. Caster-only contract types (magical commission, ritual ward) are available to bands with at least one caster.

**Bounties repriced:** All bounty rates approximately doubled to reflect a functional mercenary economy:

| BOUNTY TYPE          | OLD RANGE | NEW RANGE |
| -------------------- | --------- | --------- |
| Local criminal       | 5–15s     | 12–30s    |
| Named bandit         | 10–25s    | 25–60s    |
| Deserter             | 2–5s      | 5–12s     |
| Warlord enemy        | 50–200s   | 80–300s   |
| Professional breach  | 10–30s    | 25–60s    |

---

## Caster Utility (Combat)

Casters provide a concrete tactical benefit in field engagements: **casualty rate reduced by 40%** across all combat the band participates in. This represents protective magic, forewarning, and the morale advantage of having someone in the band who can do things no blade can.

The caster's financial case in the V3 model:

- **Mission wage:** 6s/day — covered by the 35% premium on contracts
- **Retainer:** 8s/week (1.14s/day) — negligible
- **Combat value:** fewer casualties means fewer replacements (~3–8s each), fewer death morale hits, longer band longevity
- **Caster contracts:** magical commissions (280–420s/12d) and ritual wards (185–300s/8d) are only accessible to caster bands — these are contracts that cannot be taken otherwise

An initiate caster costs roughly 29s/week on mission and 8s/week on retainer. Against a band earning 35% more on contracts and avoiding ~40% of casualties, this cost is justified.

---

## Simulation Results (200 runs × 365 days)

**Standard nine-man warband: 6 commons, 2 veterans, 1 named man. Starting treasury: 100s.**

| METRIC                  | V1 DAILY WAGES | V2 RETAINER  | V3 RETAINER+REPRICED |
| ----------------------- | -------------- | ------------ | -------------------- |
| Survival rate (1 year)  | 62.5%          | 83.5%        | **95.5%**            |
| Median final treasury   | 0s             | 54s          | **868s**             |
| Mean annual income      | 1,509s         | 1,781s       | **2,676s**           |
| Mean annual expenses    | 3,113s         | 2,269s       | **2,195s**           |
| Net margin              | −106%          | −27%         | **+18%**             |
| Days on contract (mean) | 97d (26.5%)    | 111d (30.5%) | **234d (64.1%)**     |
| Dead-time runway (100s) | ~8 days        | ~30 days     | ~30 days             |

**Small band (4 commons, 1 veteran):**

| METRIC                | V1    | V2    | V3         |
| --------------------- | ----- | ----- | ---------- |
| Survival rate         | 49.5% | 78.0% | **85.0%**  |
| Median final treasury | 0s    | 95s   | **989s**   |
| Net margin            | −105% | −25%  | **+31%**   |

**Warband with initiate caster (6c+2v+1nm+1ca):**

| METRIC                | V1    | V2    | V3          |
| --------------------- | ----- | ----- | ----------- |
| Survival rate         | 92.0% | 96.5% | **100.0%**  |
| Median final treasury | 0s    | 0s    | **822s**    |
| Net margin            | −106% | −27%  | **+10%**    |

**Key findings:**

V3 is the first model where all three configurations show positive net margin and meaningful treasury accumulation by year-end. The caster variant achieves 100% one-year survival — the caster's combat utility (−40% casualties) combined with the +35% contract premium and caster-specific contract access brings the cost into alignment with the value delivered.

The protection season contract is the single most impactful change. In the simulation, V3 bands spend 64% of the year on active contracts (including garrison seasons) vs 27% in V1. This is the direct effect of the protection season making stable multi-month arrangements viable for employers and financially sensible for captains.

**Full findings saved to:** `analysis/band_economy_findings_v2.md`

---

## Simulation Parameters

**V2 Retainer Model constants used in `scripts/band_economy_sim.py`:**

```
RETAINER_WEEKLY:
  common:           2s/week
  veteran:          3s/week
  named_man:        5s/week
  caster_initiate:  8s/week
  caster_adept:     12s/week

LOOT_MEN_SHARE:     60%  of loot pool paid to fighters
LOOT_TIER:
  named_man:        50% of men's share
  veteran:          30% of men's share
  common:           20% of men's share

BATTLE_PRIZE_PCT:   10%  of contract pay treated as battle prize (loot event trigger)

Dead-time forager allocation:  70% of band
Mission forager allocation:    30% of band

Non-payment thresholds:
  retainer: 14 days
  mission:   3 days
```

**Results:** `scripts/sim_results/v2_retainer_latest.json`

---

## Acceptance Checklist

- [ ] Retainer rate table replaces daily wage in Section 3
- [ ] Mission pay definition added to Section 3 (contract-start-to-close)
- [ ] Loot share table added to Section 3
- [ ] Non-payment thresholds updated (retainer 14 days; mission 3 days)
- [ ] Dead-week foraging allocation updated to 70% in Section 4 note
- [ ] Named Man Loyalty rule updated to include loot-payment parity
- [ ] Section 9 (Atrocities) updated to flag tribute as loot event
