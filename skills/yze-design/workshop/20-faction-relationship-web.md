<!-- markdownlint-disable MD013 MD024 -->

# Faction Relationship Web — A Living Graph of Power

> **STATUS: WORKSHOP MODULE.** A multi-faction relationship tracker that models alliances, feuds, debts, and shifting standing as a *graph the PCs steer* — not a static list of "the dwarves hate the orcs." *Core is generic; the worked example (post-apoc warlords) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic mechanism
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — Post-apoc warlords

## 1. Origin — how this was built

- **Source primitives:** **P14 (encounter engine with memory)** + **P4 (typed D66)** + a domain transfer of **P10 (protected dial, inverted)** for the "bond" tracks.
- **Reinvention operator:** **Fusion + Domain Transfer.** Fuse the "world with memory" pattern (P14) with the "typed consequence table" (P4) to model *relationship events* as a living graph. Domain-transfer the protected-dial (P10) concept: a bond between two factions is a track that *grows when cultivated and shrinks when stressed* — like Pride, but bidirectional and shared.
- **Target psychology:** **Investment + entanglement** — produces a *web the PCs cannot escape*. Every action helps one faction and hurts another; neutrality is a position with costs. The graph makes the world feel *interconnected and reactive* rather than a list of independent quest-givers.
- **Problem solved:** most RPG faction systems track "the party's standing with Faction X" as an isolated number. That produces siloed reputation grind. Real political/factional play is *relational*: what matters is not just "do the Guilds like you" but "the Guilds like you, which means the Crown now suspects you, which means the Church (which fears the Crown) is warming to you." This module makes the *edges between factions* as tracked as the nodes.

## 2. The generic mechanism

### The graph

A campaign has **3–7 factions** (the sweet spot — fewer is static, more is bookkeeping). Each faction is a node. Every pair of factions has an **edge** describing their relationship, scored on two axes:

- **Bond (−5 to +5):** the emotional/practical relationship. −5 = open war, −1 = cold distrust, 0 = neutral, +1 = cordial, +5 = blood pact.
- **Debt (−3 to +3):** who owes whom. −3 = A owes B deeply, 0 = settled, +3 = B owes A deeply. Debt is *directional* and asymmetric.

Track edges on a simple grid (factions on both axes; Bond in the upper triangle, Debt in the lower).

### The party's standing

Each PC (or the party as a whole) has a **Standing** score (−5 to +5) with each faction — same scale as Bond. Standing is *what the faction thinks of you*; Bond is *what two factions think of each other.*

### The propagation rule (the core innovation)

**When the party's Standing with Faction A changes by ±N, every faction with a Bond to A shifts its Standing with the party by a fraction of N, in the direction of A's Bond.**

- Helping A (Standing +2) → factions that *like* A (Bond +3 or better) warm to you (+1 each); factions that *hate* A (Bond −3 or worse) cool to you (−1 each).
- This is the engine's "memory with consequences" pattern: your reputation *propagates* through the graph.

### Relationship events (the typed D66)

At each downtime boundary, roll on a **Relationship Event table** (D66, typed per the campaign's needs). Sample rows:
- `11–14` — a **minor friction** between two factions (Bond −1 between them).
- `21–23` — a **cross-faction marriage/merger** (Bond +1; one assumes a Debt to the other).
- `33–36` — a **betrayal** (Bond drops to −3; Debt inverts).
- `44–46` — a **shared threat** emerges that aligns two enemies (Bond +2, temporary).
- `61–66` — a **war breaks out** (Bond −5; both call in their debts to the party — see below).

### Debts as pressure

A faction owed a Debt by the party (or by another faction the party needs) can **call it in** once. This is the engine's "nothing is for free" (`10`) at faction scale: every favor the party accepted is a future obligation. Called debts are how the web *exerts force on the PCs* — they cannot be ignored without consequence (the creditor's Standing drops to −3 and their Bond-allies follow).

## 3. The pressure loop

- **Pressure:** standing propagates; debts come due; relationship events shift the graph under the party.
- **Decision:** *help A (and anger A's enemies) or stay neutral (and gain nothing)? pay the called debt or refuse (and make an enemy)?*
- **Consequence:** the graph shifts; new doors open, old ones close; debts shuffle.
- **State change:** the campaign's political landscape is a *living* thing the PCs steered into its current shape.
- **Loop shape:** **act → propagate → debt/event → realign → act.** Runs at session/season cadence.

## 4. Dials

| Dial | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Faction count** | 3–4 (manageable) | 6–7 (dense web) | Clear choices vs rich entanglement |
| **Propagation strength** | Full (±N mirrors to allies/enemies) | Half (round down) | Volatile/reactive vs stable/slow |
| **Event frequency** | 1/session | 1/season | Constant churn vs strategic pacing |
| **Debt call-in** | GM-driven (creditor decides) | Player-driven (party can call debts *owed to them*) | Symmetric pressure vs PC agency |
| **Standing range** | −5/+5 (wide) | −3/+3 (tight) | Room for deep feuds vs quick shifts |
| **Neutrality rule** | Allowed (no-op) | Costly (neutral parties lose Standing with *all* sides — "if you're not with us...") | Safe middle vs forced alignment |

**Calibration guidance:** start with 4 factions, full propagation, 1 event/session, GM-driven debt calls, wide range, neutrality allowed. Make neutrality costly only if you want a *polarized* campaign (good for civil-war / revolution genres).

## 5. Integration points

- **Hooks into:** the org layer (`07`) — factions *are* orgs (P7 lifecycle applies); their Strength/Bond/Debt tracks are the org's "events" beat. Hooks into the Influence module (`workshop/10`) — PC Influence is faction-specific. Hooks into encounter tables (`09 §4`) — high-standing factions send allies; low-standing send assassins. Hooks into the campaign-state tracker (`09 §8`).
- **Requires:** 3–7 named factions with defined initial Bonds/Debts. Define the graph *before* play.
- **Replaces / extends:** flat "Reputation" trackers — adds the relational dimension.
- **Cross-refs:** `07` (org lifecycle, faction turn), `09` (campaign-state trackers), `12` (the faction divergence cluster).

## 6. Failure modes & edge cases

- **Graph explosion.** Tracking every pair among 7 factions = 21 edges, each with Bond + Debt = 42 numbers. **Fix:** cap at 4–5 factions; abstract "minor factions" into a single regional modifier.
- **Propagation cascade.** With full propagation and wide range, one big action can flip the whole graph in a session, making the world feel *jittery*. **Fix:** halve propagation strength, or cap single-action Standing shifts at ±2.
- **The irrelevance trap.** If the party can ignore factions with no cost, the web becomes scenery. **Fix:** tie something the party *needs* (a resource, a location, a piece of knowledge) to each faction — you cannot progress without engaging.
- **Debt amnesia.** If debts are never called, they're just bookkeeping. **Fix:** the GM should call at least one debt per session — it is the web's primary pressure valve.
- **Neutrality dominance.** If neutrality is free and safe, rational players never take sides and the web never engages. **Fix:** the costly-neutrality dial, or simply make every session's event *demand* a response.

## 7. Validation notes

- **Math:** propagation is bounded by the Bond range (±5), so worst-case a single action propagates ±5 through a chain — but only across edges that exist. With 4 factions the maximum cascade depth is 3 hops. Playtest the cascade; if the graph flips too fast, halve propagation.
- **Exploits (`13 §5`):** the main risk is **debt-farming** (the party calling every debt owed to them in one session to trivialize an obstacle). Gate debt calls to one per session per faction, and require the debt to be *relevant* to the current ask.
- **Felt experience (`19`):** propagation is the key psychology — it makes the world *feel reactive* (C5 agency ledger). The cost is cognitive load (FE2 decision fatigue) if the graph is too dense; cap factions to control this. The costly-neutrality dial produces a strong *forced-choice* feel (good for political genres, exhausting for others).

## 8. Worked genre example — Post-apoc warlords

**The setting:** The irradiated ruins of a collapsed state, three generations after the fall. Four warlords contest a river valley: **The Pale Banner** (ex-soldier religious zealots), **The Coil** (tech-scavenger cartel), **The Long Grass** (nomad clan-riders), and **The Concrete Commune** (fortified town-dwellers).

**Initial graph:**
- Pale Banner ↔ Long Grass: Bond −3 (ideological hatred — zealots vs "heathen" nomads). Debt 0.
- Pale Banner ↔ Concrete Commune: Bond +1 (mutual defense pact). Debt +2 (Commune owes Banner — they broke a pact).
- Coil ↔ Concrete Commune: Bond +2 (trade partners — tech for food). Debt −1 (Coil owes Commune a shipment).
- Coil ↔ Long Grass: Bond 0 (neutral, opportunistic trade). Debt 0.
- Pale Banner ↔ Coil: Bond −2 (Banner hates Coil's "tech-worship"). Debt 0.

**Party starts:** Neutral (Standing 0) with all four. They are drifters.

**In use:**

- **Session 1.** The party brokers a water-purifier repair for the Concrete Commune (Coil tech, Commune labor). The Coil likes this — party Standing with Coil +2. **Propagation:** the Pale Banner (Bond −2 with Coil) cools to the party by −1. The Commune (Bond +2 with Coil) warms +1. The party is now: Coil +2, Commune +1, Long Grass 0, Pale Banner −1. *Their drift toward the Coil-Commune bloc is already being noticed by the Banner.*
- **Session 3.** The party escorts a Long Grass bride-exchange across Banner territory — a risky diplomatic act. Standing with Long Grass +3. **Propagation:** the Banner (Bond −3 with Long Grass) drops the party to −3 — the Banner's preacher declares them *apostates.* The Commune (Bond 0 with Long Grass) is unmoved.
- **Session 5.** The Pale Banner **calls the Commune's Debt** (+2): "Honor our pact — deny these apostate drifters your water, or we abrogate the defense pact." The Commune must choose. The PCs must either repair the Commune-Banner Bond (how?) or accept that the Commune will turn on them. The graph is *exerting force.*

**Why this works post-apoc:** the web models the reality of warlord politics — *you cannot be friends with everyone because they hate each other.* Propagation makes every choice a commitment. Called debts make past favors into current traps. The graph turns a sandbox into a *living political ecology.*

**Re-skin for your genre:**
- **Court intrigue:** factions = Noble Houses; Bonds = marriages/feuds; Debts = treaties/oaths; events = royal marriages, assassinations.
- **Corporate:** factions = Megacorps; Bonds = partnerships/competition; Debts = contracts/leverage; events = mergers, hostile takeovers.
- **Colony/revolutionary:** factions = Factions of the revolution (Moderates / Radicals / Foreign backers / Crown); Bonds = ideological alignment; Debts = political favors; events = regime crises.
- **Greek city-states:** factions = Poleis; Bonds = alliances (Delian/Peloponnesian leagues); Debts = tribute; events = Persian invasions reshaping all alignments at once.
