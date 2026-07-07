<!-- markdownlint-disable MD013 MD024 -->

# Debt & Obligation — The Inverted Metacurrency

> **STATUS: WORKSHOP MODULE.** Turns favors, loans, oaths, and pacts into *active pressure* — an **inverted metacurrency** where the pool *grows* when you accept help and must be *paid down*. Where Willpower/Faith refuels you, Debt depletes you. Every favor accepted is a hook the GM can pull; every oath is a constraint on the next choice. *Core is generic; the worked example (corporate space opera) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic mechanism
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — Corporate space opera

## 1. Origin — how this was built

- **Source primitives:** **P2 (capped metacurrency refueled by risk)**, **inverted polarity**; **P4 (typed D66)** for what a creditor *demands* when the debt is called; **P5 (resource die)**, optional, for debts that have *size* rather than a flat cost.
- **Reinvention operator:** **Inversion (Operator 2) + Domain Transfer (Operator 1).** Take P2 — a cap-~10 pool you *spend down* and *refill by engaging risk* — and invert both its direction and its polarity. The Debt pool **grows when you accept a favor** (you accrue it; the refuel trigger is inverted from "risk refills" to "acceptance fills"). You **pay it down by settling** the obligation. You want it *low*, not high. Then Domain-Transfer the whole thing off the personal-pool substrate (WP/Faith track a character's resolve) onto a **relationship ledger** (Debt tracks what one party owes *another*). The inversion is what makes it feel new; the domain transfer is what makes it *relational* rather than internal.
- **Target psychology:** **Entrapment / obligation** — the mirror-image of P2's refuel psychologies (`17` M1). Where harm-refuel produces *aggression* (pain = fuel, so push into danger) and action-refuel produces *investment* (drama = fuel), inverted-P2 produces **a weight that compounds**: every favor makes the next choice narrower. The player is always answering "what does this cost me *later*?"
- **Problem solved:** both source games model obligation thinly. West has **loans** (`08 §4`) — 5–10% interest/season, collateral, foreclosure — but only *financial*, and only as a balance-sheet line, not active pressure. FL has oaths and favors as pure fiction with no teeth. Neither makes "I owe someone" a *trackable pressure that comes due in play.* For genres where entanglement is the engine of the plot (noir, corporate, heist, feudal, supernatural-pact), the absence is a real gap. This module closes it by unifying financial debt, social favors, moral oaths, and supernatural pacts onto one track — and giving the GM a lever ("call the debt") that turns past generosity into present constraint.

## 2. The generic mechanism

### The Debt track

Each PC (and optionally the party as a whole) has a **Debt** score, 0–10. Debt is *bad*: you want it low. It rises when you accept help you cannot pay for up front; it falls when you settle what you owe. Unlike WP/Faith, **you do not choose to spend Debt** — it is inflicted on you by need, and removed by fulfillment.

### The four debt types

A Debt is always one of four types. The type determines *how it accrues* and *how it is paid down*. (This is P4's family-set parameter, M3: one master track, four typed demand families.)

| Type | Accrues when… | Paid down by… | The fiction |
| --- | --- | --- | --- |
| **Financial** | You take a loan, buy on credit, default on a bill | Paying principal+cost, surrendering collateral, laboring it off | Money owed. West's loans are the native instance. |
| **Social** | You ask a favor you cannot immediately return ("you owe me one") | Returning a comparable favor, an introduction, a vouching | A favor owed to a person or faction. |
| **Moral** | You swear an oath, make a vow, give your word | Acting consistently with the oath over time; formally releasing it | A constraint on *future action*, not a one-time payment. |
| **Supernatural** | You make a pact, accept a boon, bind yourself to a power | The scheduled sacrifice, the geas fulfilled, the soul-installment | A metaphysical lien. The creditor is not always human. |

Each individual Debt is recorded as **(Type, Creditor, amount 1–3)**. The PC's total Debt is the sum, capped at 10.

### Accrual

When a PC accepts a favor, loan, oath, or pact, add its **amount** (1 for a small favor, 2 for a substantial one, 3 for a life-altering one) to Debt. The GM and player agree the amount at the moment of acceptance — *the price is named up front, never retconned.* If Debt is already at 10, the PC cannot take new favors until some is paid down (the character is maxed out — see *Debt 10* below).

### Paying down Debt

Debt is reduced by **settling** the obligation in-fiction:
- **Financial:** pay the amount in capital/cash; or surrender the collateral; or work it off (a downtime activity, P6).
- **Social:** perform a return favor for the creditor of comparable weight.
- **Moral:** the oath does *not* pay down per-act; it is paid down only by a **formal release** (the oath is fulfilled, the sworn-to party absolves you, or the oath's term expires). Until then it sits on the track as a standing constraint — *every act consistent with it costs nothing; every act against it risks a Break (see Calling).*
- **Supernatural:** deliver the scheduled sacrifice/boon, or complete the geas.

Paying down reduces Debt by the amount settled. **A debt that is called and refused does not pay down** — it converts to consequence (below).

### Calling a debt — the GM's lever

This is the core innovation. At any point the fiction warrants — a creditor needs something, a deadline arrives, a faction turns the screw — the GM **calls** one of the PC's outstanding debts. A called debt must be **settled now** or **refused**:

- **Settle now:** pay the down-cost immediately (do the mission, hand over the collateral, perform the favor). Debt drops by the amount.
- **Refuse:** the debt does *not* pay down. Instead roll on the **Demand** table (P4) — the creditor extracts a specific consequence regardless, and the PC's standing with that creditor (and their allies, per the faction web `20`) takes a hit.

The point of calling is not punishment — it is **turning a past favor into a present scene.** Every debt on the sheet is a hook the GM can pull when the plot needs one.

### The Demand table (P4, typed D66)

When a debt is called and *refused* (or when a creditor escalates), roll D66. Tens = the *nature* of the demand; Units = the *severity.* Build one typed family per debt type you enable; below is the generic skeleton.

| Roll | Demand (generic) | Severity |
| --- | --- | --- |
| `11–13` | A **small task** the creditor insists on now (an errand, a delivery, a lie told) | Light — annoying, not costly |
| `21–24` | **Access** revoked or granted conditionally — a door closes until you comply | Moderate — blocks a resource |
| `31–34` | A **collateral call** — the creditor takes a named asset, contact, or property | Moderate — loss of a thing |
| `41–44` | A **betrayal demanded** — you must act against an ally or your own interest | Heavy — a moral test |
| `51–54` | **Public leverage** — the creditor exposes a secret or calls in allies against you | Heavy — reputational damage |
| `61–64` | **Escalation** — the debt is sold/transferred to a worse creditor, or the term tightens | Severe — the trap closes |
| `65` | **Foreclosure** — the creditor seizes the collateral outright and the debt becomes permanent | Climax — a thing is lost for good |
| `66` | **Indenture** — the PC is bound to service until the debt is cleared by a major act | Climax — freedom is the stakes |

Typed families reskin the rows: a *supernatural* `41–44` is a geas to do the forbidden thing; a *social* `65` is a public shaming that breaks the relationship permanently. The `65/66` climax split is P4's signature architecture, unchanged (`04 §5`).

### Debt 10 — the cap state

When a PC hits **Debt 10**, they are **maxed out** — they cannot accept new favors, and at the next downtime the GM rolls on the Demand table at +1 severity per point over... no: at 10 the PC is in **foreclosure-equivalent** crisis. The GM calls *every* outstanding debt in a single cascade, or the PC enters an **Indenture** (row 66) with their largest creditor until the total is brought below 7. Debt 10 is the "Broken" of this system — the moment obligation overwhelms agency. It should be rare and dramatic, not routine.

## 3. The pressure loop

- **Pressure:** Debt creeps up whenever the party needs something they cannot afford (in money, favors, or leverage); called debts force immediate settlement or consequence.
- **Decision:** *do I accept this favor (and the future hook) or struggle on without it? when the debt is called, do I settle now (paying the down-cost) or refuse (and roll the Demand)?*
- **Consequence:** settling frees capacity but consumes resources/time; refusing extracts a Demand consequence and damages the creditor relationship.
- **State change:** the PC's web of obligation shifts — some debts clear, new ones accrue, standing with creditors (and their faction allies, `20`) moves.
- **Loop shape:** **accept → accrue → called → settle-or-refuse → accept.** Runs at session/downtime cadence (strategic, like Influence `10`), not Round cadence — though a *called* debt resolves in a single scene.

## 4. Dials

| Dial | Setting A | Setting B | Psychology produced |
| --- | --- | --- | --- |
| **Debt types enabled** | Financial only (West-native) | All four (financial + social + moral + supernatural) | Narrow/economic vs full entanglement |
| **Demand table** | One generic table | One typed family per enabled debt type (P4, M3) | "Debt is debt" vs "the *kind* of obligation is the story" |
| **How debts are called** | GM-driven (creditor decides, ≥1/session) | Dice-driven (roll at downtime: 1/recent-favor it comes due) | Authorial pressure vs emergent/fair pressure |
| **What happens at Debt 10** | Indenture (bound to service until <7) | Foreclosure cascade (all debts called at once) | Slow grind vs sudden crisis |
| **Cap** | 10 (standard P2) | 6 (tight — pressure fast) | Room to maneuver vs always-on-the-edge |
| **Debt granularity** | Fixed points (each favor = 1–3) | Resource-die-per-debt (P5: a D6–D12 "size" die, steps down as you pay installments) | Simple accounting vs "chipping away" texture |
| **Who tracks** | Per-PC | Party-shared (one Debt pool for the whole crew/ship) | Personal obligation vs collective burden |
| **Moral-oath cost model** | Oath pays down only on formal release (constraint model) | Oath pays down per consistent act (behavior-reward model) | Standing constraint vs drip-clearance |
| **Player-driven calling** | Off (only creditors call) | On (PCs can call debts *owed to them* by NPCs) | One-way pressure vs symmetric leverage |

**Calibration guidance:** start with **all four types, one generic Demand table, GM-driven calling (≥1/session), Indenture at 10, cap 10, fixed points, per-PC tracking, constraint-model oaths, calling off for PCs.** Add typed Demand families only if obligation is a *pillar* of the campaign (it adds a table per type). Turn on player-driven calling for heist/caper genres where the crew *uses* owed favors as currency.

## 5. Integration points

- **Hooks into:** the **faction relationship web** (`workshop/20`) — a faction-to-faction or faction-to-PC Debt on that module's edge is *this* module's Debt at org scale; calling it is how the web exerts force (the warlord example in `20 §8` is a called debt). Hooks into **Influence** (`workshop/10`) — a called debt can be bought off by spending Influence with the creditor (or, inverted, *refusing* a called debt costs Influence via the scandal mechanic). Hooks into the **org layer** (`07`) — an org's upkeep obligation (P7) is a standing Debt the org owes its sponsors. Hooks into the **economy** (`08`) — West's loans become the *financial* debt type, with interest modeled as slow accrual (+1 Debt/season the loan is outstanding) rather than a separate balance sheet.
- **Requires:** named **creditors** (who you owe), a sense of the **downtime cadence** (when calling/accrual fires), and agreement on which debt types are in play.
- **Replaces / extends:** flat "you owe me a favor" fiction — adds a trackable, callable pressure. Replaces West's standalone loan rules with the unified track (a loan is just financial Debt).
- **Cross-refs:** `00 §7` (P2 metacurrency, here inverted), `04 §5` + `16` P4 (typed D66, here as the Demand table), `16` P5 (optional resource-die granularity), `18 §4` Operator 2 (Inversion) + Operator 1 (Domain Transfer), `17` M1 (the refuel psychology being inverted).

## 6. Failure modes & edge cases

- **"Players never take favors and starve."** If Debt is too punishing or calling too frequent, players rationally refuse every favor and the loop never starts — the party grinds through scarcity with no help, and the module is dead weight (`19` FE1 false choice; the pressure loop `15` P15 never engages). **Fix:** make favors *clearly worth* their Debt (a favor that solves a real problem for 1–2 Debt is a good deal), and guarantee the GM calls *at most* one debt/session early on so accepting feels safe-ish. The accrual must feel like a fair trade, not a trap.
- **"Players take everything and are buried."** The opposite failure: if favors are cheap and calling is rare, PCs accept everything, hit Debt 10, and the cascade makes them unplayable (`19` FE5 "too unfair"; `18 §7` "inverting without re-balancing" — an inverted/snowballing pool hits its climax *faster*, so the math must be recomputed). **Fix:** name the price up front (amount 1–3 agreed at acceptance), enforce the cap (no new favors at 10), and call at least one debt per session so Debt *moves down* as well as up. The track must be a two-way valve, not a ratchet.
- **Creditor amnesia.** If debts are never called, they are just bookkeeping — past favors with no teeth (the same trap the faction web's "debt amnesia" names, `20 §6`). **Fix:** the GM commits to calling ≥1 debt/session; an uncalled debt older than a full arc either auto-resolves or auto-escalates.
- **Debt-as-universal-solvent.** If *every* problem is solvable by taking a favor, Debt becomes a bypass currency that trivializes the engine's other loops (`13 §5.5`). **Fix:** favors are gated by *creditor capability and willingness* — a creditor only lends what they have and what suits them; you cannot borrow your way past a problem no one wants to help with.
- **Oath-paralysis.** If moral oaths are too broadly worded ("never lie"), every scene generates a Break risk and the PC is unplayable. **Fix:** oaths are *specific* (sworn to a named party, about a named subject, with a defined release condition); a too-broad oath is renegotiated or it is the kind of oath that *should* define the character.
- **The GM-fiat call.** If calling is pure GM whim, players feel targeted (`19` FE5). **Fix:** call only debts that are *on the sheet* (never invent a debt retroactively), and tie escalation to fiction (a deadline, a creditor's need) the players can see coming. The dice-driven calling dial (above) is the fair-pressure fix for tables that want it.

## 7. Validation notes

- **Math (`13 §3`, with the inversion caveat from `18 §7`):** an inverted pool (grows on accrual, climax at cap) hits its crisis *faster* than a depleting pool hits empty, because accrual is player-driven and frequent. Recompute the breakpoints: at ~1–2 favors/session and 1+ call/session, a PC cycling between 3 and 7 Debt is healthy; a PC parked at 9–10 is in endgame. If Debt routinely hits 10 by session 3, either raise the cap, lower favor amounts, or call more aggressively so it pays down. The rule of thumb: **Debt should feel like it moves both ways every session.**
- **Exploits (`13 §5`):** the main risks are debt-farming (taking favors to game a creditor relationship — gated by the cap and by creditor willingness) and the universal-solvent (above). The "call every debt at 10" cascade prevents hoarding-at-cap as a safe strategy. Player-driven calling (if enabled) is gated to one call/session per creditor to prevent the crew dumping all owed-favors at once.
- **Felt experience (`19`):** the key psychology is that **Debt makes the past matter** — every favor accepted is a seed the GM can grow into a scene (C5 agency ledger: the player's *past* choices constrain their *present*). The price-named-up-front rule prevents FE1 (false choice) and FE5 (unfairness): players always know what they are getting into. The Demand table must feel *specific and memorable* (P4's core property) — "the creditor sells your debt to the syndicate" is a story beat, not "−2 standing." Validate by checking that called debts produce scenes, not arithmetic.

## 8. Worked genre example — Corporate space opera

**The setting:** A handful of PCs crew a freighter in the grip of **Vance-Meridian**, the mega-corp that funded their ship, installed their cybernetics, and forged the false identities they live under. They are not employees; they are *assets carrying a balance.* Every job is a payment; every favor from a fixer is another line on the ledger.

**Dials set:** all four types enabled; one typed Demand family per type (financial / social / moral / supernatural — the last reskinned as "neuro-contract" clauses wired to their cybernetics); GM-driven calling, ≥1/session; Indenture at 10; cap 10; fixed points; **party-shared Debt pool** (the *ship* owes, and the crew is jointly liable); constraint-model oaths; player-driven calling **on** (the crew leans on favors *owed to them* as often as they are called).

**The crew's starting ledger (shared Debt 6/10):**
- **Financial Debt 3** to Vance-Meridian — the ship mortgage + cybernetic installment (accrues +1/season it is unpaid).
- **Social Debt 2** to a station fixer — she forged their papers; they owe her "two more, of her choosing."
- **Moral Debt 1** — the medic swore an oath to the ship's AI to never let a patient die if salvageable (a standing constraint on away-mission triage).

**In use (excerpt):**

- **Session 2.** The freighter's drive fails mid-run. They cannot afford the repair. The GM offers: a Vance-Meridian drydock does it "on account" — **+2 financial Debt** (now 8). The crew accepts; the price is named up front. The drive is fixed. They limp on.
- **Session 3.** The fixer **calls one of her social debts**: "I need this crate delivered to the lunar embargo zone. No questions." The crew can **settle now** (run the crate, Debt −1) or **refuse** (roll Demand). They run it — a short heist scene, Debt drops to 7. *A past favor just became a present mission — exactly the module's purpose.*
- **Session 4.** The Vance-Meridian accrual fires at downtime: +1 financial (now 8). The medic faces a triage call where saving the patient means violating cover — the **moral oath** constrains her (she must save them or risk an oath-Break). The crew is creeping toward 10.
- **Session 5.** Debt hits **10** after they take one more favor to escape a patrol. **Indenture fires:** Vance-Meridian's repo-clause activates — the crew must complete *one major uncompensated run* (the GM's next session) before any Debt can pay down and before they can take any new favor. The campaign's next arc is *the debt coming due.* The crew now actively hunts ways to pay down — a risky salvage job that clears 3 Debt if they pull it off.

**Why this works in corporate space opera:** the **party-shared pool** models the reality that the *ship* is the indebted entity and the crew is jointly liable — a classic corp-asset dynamic. The **financial type** is the native instance (the mortgage, the cybernetics), but the **supernatural-as-neuro-contract** reskin lets the corp's "behavioral clauses" (wired into their implants) function as pacts with a non-human creditor. Player-driven calling models the crew *using* their owed favors as leverage — the fixer owes *them* one now, and they pull it when they need a paper trail scrubbed. Debt becomes the engine of the plot: the campaign is literally *about working off what they owe.*

**Re-skin for your genre:**
- **Noir / crime:** financial = loan-shark debt; social = favors owed to the outfit; moral = the one line you swore you'd never cross; supernatural reskinned as a snitch-informant pact. Per-PC tracking; GM-driven calling.
- **Feudal / oath-and-blood:** financial = liege-lord's dues; social = fealty favors; moral = sworn oaths (the dominant type); supernatural = a blood-pact or geas. Constraint-model oaths; tight cap 6.
- **Supernatural / pact-magic:** supernatural is the dominant type (every spell is a Debt to the power that grants it); the Demand table *is* the price of magic. Debt 10 = the power claims you.
- **Heist / crew:** party-shared pool; player-driven calling on; the crew's owed-favors are heist *assets* they call in — Debt is both a resource and a trap.
