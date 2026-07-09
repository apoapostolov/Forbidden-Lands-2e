<!-- markdownlint-disable MD013 MD024 -->

# Faction Relationship Web — A Living Graph of Power

> **STATUS: WORKSHOP MODULE.** A multi-faction relationship tracker modeling alliances, feuds, debts, and shifting standing as a *graph the PCs steer*. *Core is generic; the worked example (post-apoc warlords) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic design space
3. The pressure loop
4. Choices
5. Integration points
6. Failure modes & edge cases
7. Check notes
8. Worked genre example — Post-apoc warlords

## 1. Origin — how this was built

- **Source patterns:** **P14 (encounter engine with memory)** + **P4 (typed D66)** + a domain transfer of **P10 (inner fire, inverted)** for the bond tracks.
- **Reinvention operator:** **Fusion + Domain Transfer.** Fuse P14 (world-with-memory) with P4 (typed consequence) to model relationship *events*. Domain-transfer P10: a bond between two factions is a track that grows when cultivated and shrinks when stressed — like Pride, but bidirectional and shared.
- **Target psychology:** **Investment + entanglement** — a web the PCs cannot escape. Every action helps one faction and hurts another; neutrality is a position with costs.
- **Problem solved:** most RPG faction systems track "standing with Faction X" as an isolated number, producing siloed reputation grind. This module makes the *edges between factions* as tracked as the nodes — so helping A propagates through A's alliances to warm A's allies and chill A's enemies.

## 2. The generic design space

### 2a. Rule overview

A campaign has 3–7 factions. Each pair has a relationship scored on two axes: **Bond** (emotional/practical, −5 to +5) and **Debt** (directional, −3 to +3). The party has a **Standing** (−5 to +5) with each faction. When the party's Standing with A changes, it **propagates** through A's bonds to shift the party's Standing with A's allies and enemies. At each downtime, a D66 **Relationship Event** rolls to shift the graph under the party. Factions owed debts can **call them in** — the web's primary pressure valve.

### 2b. NEW CONCEPTS introduced

- **NEW CONCEPT — Propagation rule:** No core engine system propagates a standing change through a relationship graph. The propagation formula (§2c) makes the party's reputation with each faction a *function of its reputation with that faction's allies and enemies.* *Extends the engine by making reputation relational rather than siloed.*
- **NEW CONCEPT — Bidirectional Bond track:** Core reputation is a single party→faction vector. A Bond is a *faction↔faction* edge, tracked separately from the party's standing with either. *Extends the engine by adding a second layer of tracked relationship (between NPCs/factions, not just party↔faction).*
- **NEW CONCEPT — Directional Debt:** Debts are asymmetric (A owes B ≠ B owes A) and *callable* — a creditor can pull a future obligation. *Extends the engine by introducing a deferred-obligation rule pattern with a defined call procedure (§2c).*

### 2c. Rules reference (tables & procedures)

#### The graph

Track on a grid: factions on both axes. Upper triangle = Bond (−5 to +5). Lower triangle = Debt (−3 to +3, directional: a positive value in cell [A,B] means B owes A). Diagonal = n/a.

#### The party's Standing

Per faction: −5 (hunted) / −3 (enemy) / −1 (distrusted) / 0 (neutral) / +1 (welcome) / +3 (ally) / +5 (blood-pact). Starts at 0 for all unless the campaign specifies otherwise.

#### The propagation formula

When the party's Standing with Faction A changes by **Δ** (positive or negative), every other Faction B shifts its Standing with the party by:

> **ΔStanding_party[B] = floor(Δ × Bond[A,B] / 5)**, rounded toward zero, capped at ±Δ.

Worked examples:
- Party helps A, **Δ = +2**. Faction B has Bond[A,B] = +4 (allies). ΔStanding_party[B] = floor(2 × 4 / 5) = floor(1.6) = **+1**. B warms to the party.
- Same Δ = +2, but Faction C has Bond[A,C] = −3 (enemies). ΔStanding_party[C] = floor(2 × −3 / 5) = floor(−1.2) = **−1**. C cools to the party.
- Faction D has Bond[A,D] = +1 (corchoice). ΔStanding_party[D] = floor(2 × 1 / 5) = floor(0.4) = **0**. No shift — the bond is too weak to propagate.

**Propagation does not cascade:** only the *direct* allies/enemies of A shift. A's allies' *other* allies are not affected (this prevents graph-flip and keeps the math bounded). If using the "full propagation" choice (§4), allow one extra hop at half strength.

#### The Relationship Event table (full D66)

At each downtime boundary, roll D66 and apply. Roll twice if the choice is set to "1/session" cadence with a busy campaign.

| D66 | Event | Rule effect |
| --- | --- | --- |
| 11 | **Friction.** Two factions with Bond ≥ +2 bicker over a minor issue. | Bond between them −1. |
| 12 | **Trade dispute.** Two trading partners (Bond ≥ 0) quarrel. | Bond −1; one assumes Debt +1 to the other (unpaid goods). |
| 13 | **Border incident.** Two neighboring factions clash at a margin. | Bond −1; if already ≤ −2, drops to −3. |
| 14 | **Rumor.** A calumny spreads between two factions. | Bond −1; the rumor's source (a third faction) gains +1 Standing with the party if the party planted it. |
| 15 | **Cold shoulder.** One faction snubs another's envoy. | Bond −1; no Debt change. |
| 16 | **Old wound.** A historical grievance resurfaces. | Bond drops to −2 (if higher); if already ≤ −2, no change. |
| 21 | **Cultural exchange.** Two factions share a festival or ritual. | Bond +1. |
| 22 | **Marriage / merger.** Two factions formalize a tie. | Bond +1; one assumes Debt −1 to the other (dowry / merger terms). |
| 23 | **Mutual aid.** Two factions cooperate against a minor threat. | Bond +1. |
| 24 | **Trade boom.** A profitable exchange enriches both. | Bond +1; both gain +1 to their org Strength track (if using `07`). |
| 25 | **Shared victory.** Two factions win a joint operation. | Bond +2. |
| 26 | **Envoy.** A faction sends a respected figure to another. | Bond +1; the envoy's faction gains +1 Standing with the party if the party facilitated. |
| 31 | **Betrayal.** One faction breaks a pact with another. | Bond drops to −3; Debt inverts (if A owed B, now B owes A). |
| 32 | **Assassination.** A faction kills a figure of another. | Bond drops to −4; the victim faction calls its debts (§Debt Call). |
| 33 | **Raid.** One faction raids another's territory. | Bond −2; Debt +1 (the raider owes reparations, unenforced). |
| 34 | **Schism.** A faction splits internally; one half aligns with a rival. | Bond −2 with the rival's enemy; the schismatics' Standing with the party shifts by ±1 (GM: did the party back them?). |
| 35 | **Scandal.** A faction's leader is disgraced. | That faction's Bond with all others −1 for a season; the party's Standing with them −1 if they were allied. |
| 36 | **Defection.** A faction's ally switches sides. | Bond with old ally drops to −3; Bond with new ally +2. |
| 41 | **Shared threat.** A third-party threat aligns two enemies. | Bond +2 (temporary — reverts at next downtime if the threat passes). |
| 42 | **Famine / crisis.** A faction is weakened. | Their org Strength −1; Bond with allies +1 (rallying), Bond with enemies −1 (opportunism). |
| 43 | **Festival.** A multi-faction gathering. | All Bonds present shift +1; the party may roll a Public Act (`workshop/01`) for Influence. |
| 44 | **Election.** A faction's leadership changes. | Roll 1D6: 1–3 new leader is hostile (Bond with party's allies −1); 4–6 neutral/continuity. |
| 45 | **Revelation.** A secret about a faction emerges. | The faction's Standing with the party shifts by ±1 (GM: did the party know?). |
| 46 | **Migration.** A faction moves territory. | Bond with the new neighbors shifts ±1 (GM); Bond with the old neighbors −1. |
| 51 | **Debt called.** A faction calls a Debt owed by another. | Apply the Debt Call procedure (below). |
| 52 | **Debt called (on the party).** A faction calls a Debt the party owes. | The party must pay or refuse (§Debt Call). |
| 53 | **Favor offered.** A faction offers the party a favor — accepting it creates Debt. | Party gains +1 Standing now; gains Debt +1 to that faction. |
| 54 | **Bribe.** A faction offers the party resources to act for them. | Party gains the resource; if accepted, Standing with rival factions propagates −1. |
| 55 | ** Ultimatum.** A faction demands the party choose a side. | Party must shift Standing with one faction +1 and another −1 within the session, or lose +1 Standing with the issuer. |
| 56 | **Summit.** Multiple factions meet; the party may mediate. | Success: Bond between two factions +1, party Standing +1 with both. Failure: Bond −1, party Standing −1 with both. |
| 61 | **War declared.** Two factions enter open war. | Bond drops to −5; both call in debts to the party (§Debt Call). |
| 62 | **Siege.** One faction besieges another's stronghold. | Defender's org Strength −1 per session until relieved; the relieving faction gains Bond +2. |
| 63 | **Revolution.** A faction's underclass rises. | The faction's Bond with all others −1; the party's Standing shifts by ±1 (GM: which side did they back?). |
| 64 | **External invasion.** A new faction (GM-introduced) invades. | All existing factions' Bond with each other +1 (rallying); the party's Standing with the invader starts at −3. |
| 65 | **Collapse.** A faction falls. | Remove it from the graph; its debts are void; its Bond-allies lose 1 Standing with the party (blame); its Bond-enemies gain 1. |
| 66 | **Coronation / ascension.** A faction achieves dominance. | That faction's Bond with all others shifts to +2 (fealty) or −2 (defiance) by GM call; the party's Standing with them becomes the campaign's central tension. |

#### The Debt Call procedure

1. **When:** a faction (the creditor) with Debt ≥ +1 over the party (or over another faction the party needs) declares the call. This is a GM action, not a roll — the creditor *decides* to pull the obligation.
2. **The demand:** the creditor names what they want — a service, a vote, a non-aggression pact, a resource, access. The demand must be *proportionate* to the Debt (Debt +1 = a small favor; Debt +3 = a major ask).
3. **The party's options:**
   - **Pay:** perform the demand. The Debt steps down by 1 (or to 0 if the demand was major and the Debt was +1). Standing with the creditor +1 (good faith).
   - **Refuse:** the Debt is *voided* (you broke the obligation), but the creditor's Standing with the party drops to −3 and propagates: the creditor's Bond-allies drop the party by −1 each. You have made an enemy.
   - **Renegotiate:** roll a social conflict (`03 §11`) or Social Combat (`workshop/03`). Success converts the Debt to a smaller one or a different form; failure doubles it.
4. **Limit:** a faction may call at most one Debt per session. This prevents debt-spam (§6).

#### What shifts Standing — the trigger table

The propagation formula needs inputs: what player actions are worth ±1, ±2, or ±3? The GM applies these *as the party acts*, not retroactively. When an action clearly benefits or harms a faction's interests, shift Standing by the amount below, then propagate.

| Magnitude | Player action examples | Standing shift |
| --- | --- | --- |
| **Minor** | A kind word to a faction member; a small trade; passing on a useful rumor; refusing a rival's request. | ±1 |
| **Moderate** | A public favor (a rescue, a timely delivery, a sponsored event); a meaningful gift; brokering a minor deal; fighting alongside them once. | ±2 |
| **Major** | A costly sacrifice for the faction (risking life, reputation, or significant resources); brokering an alliance; destroying a rival of theirs; saving their leader. | ±3 |
| **Defining** | Single-handedly saving the faction from ruin; betraying them in a way that costs them dearly; founding or destroying a faction. | ±5 (cap; sets Standing to −5 or +5) |

**GM guidance — how to call shifts in play:**
- Don't shift for every nicety. Shift when the party does something a faction would *remember* and *talk about*.
- When in doubt, ask: "Would the faction's leadership hear about this by next week?" If yes, it's worth at least ±1. If it would dominate their next council meeting, ±2. If it changes their strategy, ±3.
- A single action can shift Standing with *multiple* factions (e.g. destroying the Coil's convoy helps the Pale Banner +2 and the Commune +1 — then propagate both).
- **Tell the players when you shift Standing.** Make the web's reactivity visible: "The Pale Banner has heard what you did. They're warming to you — +2." This is the system's payoff moment.

#### The faction turn at the table — procedure

Run this at the end of each session (or season, per the event-frequency choice). It takes 5–10 minutes.

1. **Apply the session's Standing shifts.** Go around the table: name each faction the party affected this session, and the shift (from the trigger table above). Update the Standing tracks. Propagate each shift through the graph (the propagation formula). Tell the players the results — "helping the Coil dropped you with the Banner."
2. **Step any called debts.** If a faction intends to call a debt next session, set up the fiction now (an envoy arrives, a letter is delivered). Don't spring it cold.
3. **Roll one Relationship Event (D66).** Narrate the result as in-fiction news the party hears: "There's been a marriage between the Commune and the Banner — they're closer now." Update Bonds/Debts per the table.
4. **Name the active tensions.** State plainly what each faction *wants* from the party next session — "The Coil is going to ask you for something. The Banner is watching you." This is the hook-generation step.
5. **Update any org Strength tracks** (if using `07`) — factions weakened by events step down; factions enriched step up.

**The faction turn is the web's heartbeat.** Without it, the graph is a static map; with it, the world moves while the PCs act. The 5-minute investment is what makes the campaign feel politically alive.

## 3. The pressure loop

- **Pressure:** standing propagates; debts come due; relationship events shift the graph.
- **Decision:** *help A (anger A's enemies) or stay neutral (gain nothing)? pay the called debt or refuse (make an enemy)?*
- **Consequence:** the graph shifts; doors open and close; debts shuffle.
- **State change:** the campaign's political landscape is a living thing the PCs steered.
- **Loop shape:** **act → propagate → debt/event → realign → act.** Session/season cadence.

## 4. Choices

| Choice | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Faction count** | 3–4 (manageable) | 6–7 (dense web) | Clear choices vs rich entanglement |
| **Propagation strength** | Half (formula as written) | Full (×2 before rounding) + 1 extra hop at half | Volatile vs stable |
| **Event frequency** | 1/session | 1/season | Constant churn vs strategic pacing |
| **Debt call initiator** | GM-driven (creditor decides) | Symmetric (party can call debts owed *to them*) | Pressure vs agency |
| **Standing range** | −5/+5 (wide) | −3/+3 (tight) | Deep feuds vs quick shifts |
| **Neutrality** | Allowed (no-op) | Costly (neutral party loses Standing with all sides each session) | Safe middle vs forced alignment |

**Default:** 4 factions, half propagation, 1 event/session, GM-driven calls, wide range, neutrality allowed.

## 5. Integration points

- **Hooks into:** org layer (`07`) — factions *are* orgs (P7 lifecycle); their Bond/Debt are the org's "events" beat. Influence module (`workshop/01`) — PC Influence is faction-specific. Encounter tables (`09 §4`) — high-standing factions send allies; low-standing send assassins. Campaign-state tracker (`09 §8`).
- **Requires:** 3–7 named factions with defined initial Bonds/Debts. Define the graph *before* play.
- **Replaces / extends:** flat Reputation trackers — adds the relational dimension.
- **Cross-refs:** `07` (org lifecycle, faction turn), `09` (campaign-state trackers), `12` (faction divergence cluster).

## 5a. Handshake

- **Prerequisites:** three or more factions or power centers.
- **Inputs:** faction list, Bond scale, Debt scale, Standing scale, event cadence.
- **Outputs:** relationship matrix, propagation rule, relationship events.
- **Touched systems:** faction/base, reputation, debt, encounters, territory.
- **Replaces or stacks:** replaces isolated faction ledgers; stacks with Influence as the PC-facing edge.
- **Incompatibilities:** merge turn procedures if `15-territory-and-domain-play.md` is also active.

## 6. Failure modes & edge cases

- **Graph explosion.** 7 factions = 21 edges × 2 = 42 numbers. **Fix:** cap at 4–5; abstract minor factions into a regional modifier.
- **Propagation cascade.** Full propagation + wide range can flip the graph in a session. **Fix:** half propagation (default); cap single-action Standing shifts at ±2.
- **The irrelevance trap.** If the party can ignore factions cost-free, the web is scenery. **Fix:** tie something the party *needs* to each faction.
- **Debt amnesia.** If debts are never called, they're bookkeeping. **Fix:** roll on the event table each session — rows 51–52 force a call; the GM should call at least one debt per session otherwise.
- **Neutrality dominance.** If neutrality is free and safe, rational players never take sides. **Fix:** the costly-neutrality choice, or make every session's event demand a response.

## 7. Check notes

- **Math:** propagation is bounded by Bond range (±5); worst-case single action propagates ±Δ through direct edges only. With 4 factions, max cascade depth is 1 hop (no cascade by default). The formula's `/5` divisor ensures weak bonds (±1) rarely propagate — only strong relationships (±3+) reliably shift the party's standing elsewhere.
- **Abuses (`13 §5`):** **debt-farming** (party calls every debt owed to them in one session). Gated by the one-call-per-session-per-faction limit. **Propagation-craft** (party helps A specifically to anger A's enemy B, then helps B to anger A) — this is *intended* play (the web's cross-pressure), not an abuse, but if it becomes a treadmill, add the costly-neutrality choice.
- **Felt experience (`19`):** propagation makes the world *feel reactive* (C5). Cognitive load (FE2) is the cost — cap factions to control it. Costly neutrality produces strong forced-choice feel (good for political genres, exhausting for others).

## 8. Worked genre example — Post-apoc warlords

**Setting:** irradiated ruins, three generations after the fall. Four warlords contest a river valley: **The Pale Banner** (zealot ex-soldiers), **The Coil** (tech-scavenger cartel), **The Long Grass** (nomad clan-riders), **The Concrete Commune** (fortified town-dwellers).

**Initial graph:**
- Pale Banner ↔ Long Grass: Bond −3 (ideological hatred). Debt 0.
- Pale Banner ↔ Concrete Commune: Bond +1 (mutual defense pact). Debt +2 (Commune owes Banner — broke a pact).
- Coil ↔ Concrete Commune: Bond +2 (trade partners). Debt −1 (Coil owes Commune a shipment).
- Coil ↔ Long Grass: Bond 0 (neutral). Debt 0.
- Pale Banner ↔ Coil: Bond −2 (Banner hates Coil's tech-worship). Debt 0.

**Party starts:** Standing 0 with all four.

**In use:**

- **Session 1.** Party brokers a water-purifier repair for the Commune (Coil tech, Commune labor). Coil likes this — party Standing with Coil +2. **Propagation:** Pale Banner (Bond[Coil,Banner] = −2) → ΔStanding_party[Banner] = floor(2 × −2 / 5) = floor(−0.8) = **−1**. Commune (Bond[Coil,Commune] = +2) → floor(2 × 2 / 5) = floor(0.8) = **0** (too weak to propagate). Party is now: Coil +2, Commune 0, Long Grass 0, Banner −1.
- **Session 3.** Party escorts a Long Grass bride-exchange across Banner territory — a risky diplomatic act. Standing with Long Grass +3. **Propagation:** Banner (Bond[LongGrass,Banner] = −3) → floor(3 × −3 / 5) = floor(−1.8) = **−2**. Party Banner Standing: −1 → −3. The Banner's preacher declares them *apostates.*
- **Session 5.** Downtime event roll: **51 (Debt called).** The Pale Banner calls the Commune's Debt (+2): "Honor our pact — deny these apostate drifters your water, or we abrogate the defense pact." The Commune must choose (the GM plays the Commune). The party must either repair the Commune-Banner Bond (how?) or accept that the Commune will turn on them. The graph is exerting force.

**Why post-apoc:** the web models warlord politics — *you cannot be friends with everyone because they hate each other.* Propagation makes every choice a commitment. Called debts make past favors into current traps.

**Re-skin:**
- **Court intrigue:** factions = Noble Houses; Bonds = marriages/feuds; Debts = treaties/oaths; events = royal marriages, assassinations.
- **Corporate:** factions = Megacorps; Bonds = partnerships/competition; Debts = contracts; events = mergers, hostile takeovers.
- **Colony/revolutionary:** factions = Moderates / Radicals / Foreign backers / Crown; events = regime crises.
- **Greek city-states:** factions = Poleis; Bonds = league alignments; Debts = tribute; events = Persian invasions reshaping all alignments.
