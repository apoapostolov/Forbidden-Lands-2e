# Mercenary Economy Model — Design Audit

**Scope:** `proposals/proposal-mercenary-band-management.md` — economic model, caster costs, barter/liquidity, and player-facing silver linings.

---

## 1. Perpetual Struggle — Current Model is Too Comfortable

**What the simulation shows:**

V3: 95.5% survival, +18% margin, 868s median treasury at year end. This is a going concern, not a struggling warband. The V3 caster band hits 100% survival and 822s median.

**Root cause: one contract type does most of the work.** The `protection_season` pays 550–800s flat for 91 days during which wages are retainer only (~300s). That is a single contract generating +250–500s net surplus. It acts as a circuit breaker against the rest of the model's natural pressure. Remove it or restrict access and the entire year goes lean. The simulation shows it covering 64% of the year in contracts — that is not desperate scrambling, that is steady employment.

**What needs to change to restore the intended feel:**

- **Cap protection seasons at one per year, and make it GM-offered, not band-sought.** Garrison contracts should come from a lord who decides the band is worth keeping, not from the band shopping a market. This transforms it from a reliable income floor into a political achievement.
- **Add two recurring expense categories the simulation does not model:** equipment maintenance (weapons/armor degrade at ~1–2s per man per season of active service) and injury treatment (field injuries cost FOOD and coin to manage beyond basic recovery). A 9-man band that fights hard for a season should expect 8–15s in maintenance and 5–20s in healer costs. Small individually, substantial across a year.
- **Add a winter liquidity crisis.** Foraging drops to near-zero in winter. Contracts in winter should be scarcer — most employers do not run operations in the freeze. Three months of retainer-only spending with suppressed contract supply changes the annual math significantly.

**Net effect:** With garrison seasons capped and maintenance/injury costs added, expected annual margins likely drop from +18% to low single digits or break-even. The simulation's P10 treasury (already 0s) would extend — the failure cases would become more common and the median would fall. This is the zone where playing the band feels dangerous.

---

## 2. Casters — The Math Already Works, the Text Does Not Enforce It

**The numbers, honestly:**

At current proposal rates:

- **Initiate** at full V3 employment (~220 mission days): 220×3s + 145×(8/7)s = **~826s/year**. More expensive than a Named Man (~434s/year) but sustainable for a band in good standing. Coin terms make sense.
- **Adept** at full employment: 220×7.5s + 145×(12/7)s = **~1,899s/year**. This exceeds the entire wage bill for 6 commons + 2 veterans at V3 rates (~1,100s/year). You cannot hire an Adept at coin rates and break even. The math already says agenda.
- **Master** at 25+s/day: **9,100+s/year minimum**. This is not a financial question. This is a category error. No working captain can afford a Master at coin rates.

**The problem is the proposal treats coin and agenda as equivalent options.** The text says "Agenda terms as common as coin" for Adepts, and "many will not answer to coin alone" for Masters — but these are soft framings. The rule should state harder: Adepts are unsustainable at coin rates beyond 30 days of active contract work for a standard warband. Masters are not coin-hirable by anyone running a band on contracts.

**Specific mechanical addition needed:** A **caster sustainability check** — at the end of each month of coin terms with an Adept or Master, the captain must confirm they can afford the next month's projected wages before the caster confirms they are staying. If the projection fails, the caster does not leave immediately — they set a deadline. This creates visible pressure without arbitrary breakage.

**Initiate coin rates** are intentionally within reach and should stay there for bands in good standing. The point is that Initiates are the entry drug — affordable, keeps the captain from going entirely agenda-dependent. Then the Adept they want costs something they cannot pay, and the political deal is born.

---

## 3. Barter — Rich Structure, No Friction Mechanics

**What exists:** The goods payment table is structurally complete — 25+ goods types, silver equivalents, transfer conditions, spoilage notices.

**What is missing: the treasury gap.**

The proposal currently has one treasury (silver). Goods sit alongside silver as "silver equivalent" but there is no mechanical separation. This means taking a horse in payment behaves identically to taking coin. The illiquidity problem has no teeth.

**What to add: a two-line balance sheet.**

Every session, the captain tracks:

- **Silver treasury** — liquid. Pays wages, buys food, recruits.
- **Goods inventory** — valued in silver equivalent but not spendable as-is.

**Liquidity conversion rules:**

| GOODS CATEGORY | CONVERSION TIME | DISCOUNT | WHERE SELLABLE |
| --- | --- | --- | --- |
| Horses, mules, draft animals | Immediate at next settlement | 0–10% loss | Any town+ |
| Bulk materials (iron, grain, pelts) | 1 quarter-day per sale | 15–20% loss unless at appropriate market | Specific terrain |
| Immovable property (houses, fields) | Cannot convert without presence; weeks | Negotiated | Settlement only |
| Time-pledges (expert, wise, craftsman) | Cannot be resold; use it or lose it | — | N/A |
| Seasonal rights (hunting, timber) | Convert through labor investment | Labor cost ≈ 30% of value | On-site only |

**The key tensions this creates:**

- A band accepts grain and leather in payment because it is what the village has. Now wages are due in three days. The grain is being eaten (reducing ration cost) but cannot pay a man in leather. The captain must either march toward a market while the clock runs, or explain to the men.
- A band holds two horses and a salt cache worth 55s combined. They have 8s in silver. Retainer is due. They can sell the horses today for 36s but they wanted to use them for transport. This is the decision the system should produce.

**Mechanic for in-kind payment:** On any pay day where the silver treasury is insufficient but goods inventory covers the gap, the captain may make the payment in-kind. Men accept once without consequence. Second consecutive in-kind payment: roll FIELD NON-PAYMENT at −1 difficulty (slightly worse). Third: standard non-payment. This is not punitive — it is realistic. Men understand lean times. They do not accept permanent subsistence.

---

## 4. Silver Linings — Where to Build Them

The model needs **extraordinary income events** to function as intended: riches by exception, not by flow. Currently these exist in sketch form (windfalls, treasure discovery, ransom). They need to be mechanically real enough that players can chase them and feel them when they land.

### a) The Windfall Table — give it numbers and triggers

When the band completes a contract involving a significant defeat (cleared an occupied structure, ended a named threat), the GM rolls on a windfall event table. Most results are nothing — the enemy was already stripped. A minority produce extraordinary finds: a war chest, a captive worth ransoming, a hidden stockpile, a piece of intelligence worth selling. These should range 50–250s in value when they occur. They should occur roughly once per dozen contracts. Rare enough to feel like luck. Common enough that a band always knows it might happen.

One good windfall event covers two weeks of wages. Players notice and remember those moments.

### b) Ransom — full mechanics needed

The proposal mentions ransom and the goods table lists "a captive already held" as payment. But the ransom mechanics for a captive *the band takes* are not developed. Taking a valuable captive during a contract — a local lord's son, a warchief's lieutenant, a merchant-factor traveling under escort — and running a ransom negotiation is exactly the kind of episodic windfall the model needs.

A ransom should take 1D3 weeks to resolve, require at least one MANIPULATION roll against graduated difficulty (family poor → wealthy → lord), and pay 50–400s depending on who you have. It is logistically inconvenient (feeding a hostile captive, deterring rescue), which is why it is not routine income. But handled right, it buys two months of operation.

### c) Reputation as an economic variable — currently missing

The band builds Standing with settlements and Renown over time, but neither currently connects to contract rates. As the band's reputation grows, employers compete for their service and the gap between floor and ceiling rates widens. A band at Renown 4–5 should be negotiating garrison contracts at 650–900s, not 550–800s, and should have employers come to them rather than the reverse.

Mechanically simple: add a Renown bonus to contract pay (+5% per Renown point above 2). A band starting at Renown 2 sees standard rates. By Renown 5 they are seeing +15% on every contract. It is not enough to make them comfortable — the expense side never stops growing — but it makes visible progress feel real.

### d) Named Man sourcing — currently one-directional

Named Men consume loyalty events and respond to triggers. They do not generate economic value beyond their combat role. One addition would change the table feel: **Named Men can source contracts.** When a Named Man has served 3+ months and their Loyalty is 5+, they may roll MANIPULATION once per season to pull in a contract from their own connections — a contact from their history, a debt owed to them, a reputation that precedes the band. The contract type and value matches their background.

This gives players who invest in a Named Man a visible economic return, and it shifts the band's outlook from purely defensive (keep everyone paid) to forward-looking (what does this man know that might turn into work).

---

## Summary

| Area | Status | Action |
| --- | --- | --- |
| Base margins too comfortable | V3 at +18%; should be ~0% | Restrict garrison seasons; add maintenance and injury costs |
| Caster coin math | Already breaks Adept+ at year-scale | Text must say this plainly; add sustainability check |
| Barter table | Structurally complete | Add two-line balance sheet + in-kind payment mechanic |
| Windfall events | Mentioned, not mechanically developed | Build windfall roll table with triggers |
| Ransom | Referenced, not developed | Full mechanics needed |
| Reputation → pay | Not connected | Simple Renown bonus on contract negotiations |
| Named Man value | Combat and loyalty events only | Named Man contact-sourcing for contracts |

None of this requires the base pay model to change. The spending rates and retainer structure are sound. What the system needs is more costs that emerge from play (maintenance, injuries, liquidity conversion) and more exceptional income events that feel like genuine luck — because the daily grind never quite covers the widening gap.
