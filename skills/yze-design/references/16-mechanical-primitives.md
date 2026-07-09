<!-- markdownlint-disable MD013 MD024 -->

# Reusable Patterns — The Reusable-Pattern Catalog

> This is the **palette** for the generative layer. The engine systems (`00`–`15`) document *what the engine is and how to configure it*. This file catalogs the ~15 load-bearing **patterns** that recur across both source games and are proven (by FL and West) to survive transplantation to new genres and new systems. `17-dual-use-matrix.md` shows what each pattern *does* at different calibrations; `18-reinvention-method.md` teaches how to combine and repurpose them. Read this file first when inventing new rules.

## Contents

1. Source provenance
2. Abstraction target
3. What is a "pattern"?
4. The pattern catalog (P1–P15)
5. Advanced compositions (AC1-AC12)
6. How patterns compose
7. Invariant spine vs. composable surface
8. Design intent

## Source provenance

This file is a **synthesis over the engine systems documented in `00`–`15`**. Every pattern below is mined from the already-filled system files and cross-linked to where it is documented in depth. Primary evidence: both corebooks (see each system file's provenance). The empirical justification for calling these "patterns" is the **Divergence Map's synthesis** (`12 §12`): FL and West are the same invariant spine with five choices set to opposite ends — which means the *spine itself* is the reusable substrate, and each shapeting *is* a pattern that has been proven to port.

**Definition of "proven to port":** a pattern appears in *both* source games (so it is not genre-specific), OR it appears in one and its *absence* in the other is the proof it is optional/additive (so it can be added to a third). The Divergence Map's "absence as data" principle (`12 §3`) applies.

## Abstraction target

The engine systems (`00`–`15`) answer *"what is the engine?"* and *"how do I configure it?"* This file answers the prior question a designer actually faces: *"what building blocks do I have to invent with?"* The goal is to lift the recurring patterns out of their home systems and present them as a **genre-neutral palette** — each one named, abstracted, set by choice, and tagged with the systems it already powers. A designer (human or AI) composing a new rule should be able to scan this catalog, pick a pattern, and instantiate it — rather than reinventing dice pools, push economies, or consequence tables from scratch.

This is the **palette** layer of the generative method. `17` is the **calibration** layer (what each pattern *does* at different settings). `18` is the **composition** layer (how to combine and repurpose them).

## 3. What is a "pattern"?

A **reusable pattern** is a small, self-contained pattern of play that:

1. **Recur across at least two distinct systems** in the source games (so it is not a one-off rule set).
2. **Is genre-neutral in structure** — its procedure abstracts cleanly away from its nouns.
3. **Carries its own internal tension** — it produces a decision, a cost, or a pressure *by design*, independent of flavor.
4. **Has identifiable choices** — choices a designer can set when instantiating it.

A pattern is *not* a complete system. Combat is not a pattern; the **action budget** is. Magic is not a pattern; the **typed consequence table** is. Travel is not a pattern; the **activity menu** is. Patterns are the *atomic* patterns that combine into systems.

## 4. The pattern catalog (P1–P15)

Each entry: **Name** · **One-line definition** · **Core tension it creates** · **Choices** · **Where it already powers systems** (cross-links to engine system files).

---

### P1 — Dice pool with push-and-pay

**Definition:** Roll n D6; sixes = success; after the roll you may reroll non-successes *once* by paying a cost extracted from a latent cost-face already on the dice.

**Core tension:** *Do I accept this failure, or double down and pay?* The push is the engine's signature dramatic beat — it converts a dead-end fail into a priced decision.

**Choices:** (a) cost-face trigger — always-on-push (FL 💀) vs frame-gated (West 1s on Risky/Desperate); (b) cost *type* — self-harm / currency / gear-degradation / Trouble; (c) push limit (once, ever); (d) what excludes a die from the reroll.

**Powers:** the entire core resolution loop. `00 §3,§6`.

---

### P2 — Capped Willpower/Faith refueled by risk

**Definition:** A pool (cap ~10) that spends on agency (pushes, talents, powers, trouble-buyoff) and refuels from *engaging the engine's risk rules* — taking harm, succeeding boldly, or performing in-fiction actions.

**Core tension:** *spend now for a peak, or hoard for the crisis I know is coming?* The refuel trigger is what makes the pool a *loop* rather than a countdown.

**Choices:** (a) cap size; (b) spend targets; (c) **refuel trigger** — harm-earned (FL WP, virtuous damage loop) / success-earned (3-⚔ rolls) / action-earned (West Faith rituals); (d) depletion state (none / Shaken-lockout).

**Powers:** WP (FL), Faith (West), and — by direct reuse — *any* future pool you want to behave the same way (corruption, momentum, heat, favor). `00 §7`.

---

### P3 — Graded success ladder + threshold-raise

**Definition:** Read the raw success count on a 0/1/2/3+ ladder (fail / partial / full / critical), *and/or* allow a threshold to be raised before rolling to trade risk for a richer payoff.

**Core tension:** *settle for the safe win, or declare a bolder aim and risk getting nothing extra?*

**Choices:** (a) number of rungs (3 or 4); (b) what surplus successes buy — Stunts / damage / clues / positioning / **carry-forward bonus** (+1 normal / +2 critical, banked for the next relevant roll, per `00 §4`) / **Success Menu entries** (each surplus ⚔ beyond the first buys one player-declared quality of a downtime or long-process output, per `00 §4`); (c) who sets the threshold (GM-side "Levels of Effort" FL / player-side "Declared Effort" West). *Note: Stunts (fixed, tactical, combat-speed) and the Success Menu (player-authored, generative, downtime-speed) are the two surplus-success spend modes — use Stunts for immediate opposed action, the Success Menu for authored long-process output, never both on the same roll.*

**Powers:** every ability roll in both games; the Stunts rule set; combat damage scaling. `00 §4`.

---

### P4 — Typed D66 consequence table

**Definition:** A two-axis table (D66: Tens = location/category, Units = severity) producing immediate effect + long-term effect + healing/recovery time, with the `65`=maim / `66`=die climax split at the top.

**Core tension:** consequences are *specific and memorable* — "you are hamstrung" not "−2 to a stat." The table makes harm (or any failure) a story beat.

**Choices:** (a) the **family set** — one master table (West crits) or a *family of typed tables*, one per damage/source type the genre cares about (FL's 8 crit families Slash/Blunt/Stab/Burn/Acid/Cold/Swallow/Horror; FL's 17 magic-mishap families); (b) the two axes' meanings; (c) count-modification (FL shifts the D66 roll ±10 per 💀).

**Powers:** critical injuries (`04 §5`), magic mishaps (`05 §7`), stronghold random events, faction fallout, town fortune rolls, vicissitudes. **This is the single most-reused pattern in the engine** — it appears in 6+ systems. Porting it to a new failure domain is the highest-leverage move a designer can make. `04 §5`.

---

### P5 — Resource die (depleting step-die)

**Definition:** A supply is tracked as a single die (D6–D12); each use rolls it; on a 1–2 (or wider) the die steps *down*; at D6 + 1–2 the supply is depleted. Finding/buying more steps the die *up*.

**Core tension:** *consumption is a gamble, not bookkeeping.* You don't count arrows; you roll the Arrows die and feel the supply thin.

**Choices:** (a) die range (D6–D12); (b) **contraction (deplete) range** — 1–2 is the base default for most engine rules, but it is **not law**: a perishable or volatile supply contracts faster (FL's raw meat as food = 1–4; West's perishables similar). The contraction range is a **per-instance choice**: a more powerful or unstable resource can be set to 1–3, 1–4, even 1–5. *Interaction with die size:* a wider contraction range means the die steps down faster on each use, so a **larger starting die** is needed to retain the resource through multiple uses. Putting a powerful, fast-contracting resource in a small die guarantees it is spent after one use — sometimes desirable (a single-shot miracle), sometimes not. This interaction is load-bearing in the Vancian spell-slot pattern (`workshop/08` Archetype 1): a rank-1 spell in a D6 slot with contraction 1–2 depletes ~33% per cast; a rank-5 spell with contraction 1–4 in the same D6 slot is *certain* to be spent on first use, forcing the caster to invest in a larger slot die (D10–D12) to retain it. (c) what it models (FL default: food/water/arrows/torches; West optional module; *reusable for*: morale, faction strength, town prosperity, illness duration, sanity, **spell slots** per `workshop/08` #1).

**Powers:** FL consumables (default), West consumables (optional), and — by reinvention — any depleting stock. `01 §7`, `08 §10`.

---

### P6 — Activity menu (labor-distribution puzzle)

**Definition:** In a structured time block, each PC picks **one** activity from a fixed menu; the menu is designed so that critical demands (move / navigate / watch / supply / recover) are *mutually exclusive* — so the party is always short of hands.

**Core tension:** *you cannot do everything; who does what?* Distributes the party's labor so every PC has a job and the cost of specialization is visible.

**Choices:** (a) menu breadth (FL's 14-row formal menu vs West's ~6–8 implicit jobs); (b) solo vs shared tagging; (c) what demands are mutually exclusive.

**Powers:** the journey/travel loop in both games (`06 §5`), and — by reinvention — heist planning, ship crew actions, heist/social-scene frameworks, research teams. **This is the most directly portable structural pattern.** `06 §5`.

---

### P7 — Five-beat org lifecycle

**Definition:** Any persistent player- or faction-owned entity runs on five beats: **founding (predicate gate + optional founding flaw) → functions (named improvements) → upkeep (resource obligation + degeneration table) → events (procedural/world pressure) → scale (climb a rung or cap).**

**Core tension:** *owning a thing is a commitment, not a trophy.* The org is alive and threatened; neglect costs it.

**Choices:** (a) founding predicate (cleared site / spent Capital / recruited headcount / seat + basis of rule); (b) function list; (c) upkeep vectors (1–3); (d) event source (random D66 / procedural turn / tracked relationship); (e) **ladder ceiling** (the meta-choice — what the campaign is *about*).

**Powers:** Strongholds, Mercenary Companies, Factions, Outlaw Bands, Towns, Businesses, Property — *every* persistent org in both games. `07 §3`. **Proof-by-construction that one pattern scales from a single room to a polity.**

---

### P8 — Feature grammar (composable tags, not stat lines)

**Definition:** Items (weapons, armor, gear, *and characters via talents*) are defined by a set of composable **tags**, each of which gates an action, modifies a roll, or enables a rule — rather than by a monolithic stat block.

**Core tension:** *loadout drives tactical options.* Your weapon is what you can *do*, not a damage number.

**Choices:** (a) tag-source layering (FL: tags double as action-prerequisites, e.g. Parrying→PARRY, Hook→SHOVE; West: three layers Features/Qualities/Conditions); (b) positive vs negative tags; (c) stacking rules.

**Powers:** all weapons/armor/gear (`08 §6`), the talent system (talents *are* feature tags on characters), NPC special abilities. `08 §6`.

---

### P9 — Scale ladder (escalation rungs)

**Definition:** Orgs climb rungs — **Solo → Party → Band → Company → Faction → Army → Polity** — each re-using the same lifecycle beats (P7) at a larger turn scale, until a large-scale rule pattern collapses bookkeeping past a threshold.

**Core tension:** *a campaign can escalate in scope without changing engines.* The ladder lets a party grow into a power without a system switch.

**Choices:** (a) which rungs are enabled (the **ceiling choice** — the campaign's most consequential scope decision); (b) turn scale per rung (Round/Shift/Season/Year); (c) large-scale threshold (~30–50 bodies → Host Play/Ledger).

**Powers:** the entire FL org stack; West caps at Company/Town by design. `07 §9`. **The ceiling is what the campaign is *about* — individuals, communities, or power.**

---

### P10 — Inner fire (per-session pressure-relief)

**Definition:** Each PC has a personal resource — a once-session escalating die (FL Pride) or a broad currency (West Faith) — wired to character identity, that converts a loss into a win or buys off failure.

**Core tension:** *the player's personal safety net, loaded with identity.* When it's spent/lost, that's a story beat, not just a number.

**Choices:** (a) form (die added to roll vs currency spent); (b) scope (narrow — only protective rolls — vs broad — the whole loop); (c) escalation model (D8→D10→D12, grows when unused/successful, shrinks on failure); (d) identity load (a note vs a one-sentence belief).

**Powers:** Pride (FL), Faith (West), and — by reinvention — any per-PC "conviction/anchor" resource. `01 §5`, `00 §7`.

---

### P11 — Dual fast + deep generation

**Definition:** Character creation offers two paths — **fast** (pick an archetype/kin + age → 15 min) and **deep** (a lifepath that produces emergent backstory) — both calibrated to produce *equivalent-power* characters.

**Core tension:** *none — this is an accessibility pattern.* It serves two player populations without splitting the rules.

**Choices:** (a) the fast-gen identity selector (kin / archetype / lineage / role); (b) age-as-sub-choice (trades attributes for skills/talents); (c) lifepath depth (number of "Livings"/formative-event rolls).

**Powers:** both games' character creation. `01 §8`.

---

### P12 — General / Situational / Optional layering

**Definition:** Rules are classified into three layers: **General** (always on, the core), **Situational** (applies in specific contexts), **Optional** (mode-switching modules). Optional rules are *explicitly labeled* so the core stays lean.

**Core tension:** *none — this is a complexity-management pattern.* It lets the engine ship a lean core while offering depth where wanted.

**Choices:** (a) how big the Optional surface is (FL large; West small); (b) how Optional rules are flagged (callout boxes / appendix / dedicated book).

**Powers:** the entire architecture of both books. `10 §9`.

---

### P13 — Settlement-as-character

**Definition:** A settlement is modeled as a **character sheet for a place** — attributes (Aspects/vicissitude-variables), a state machine (Prosperity/Standing), internal-faction pressure gauges (Need/Heat/Feud), a resource economy, and a growth rule pattern driven by player investment.

**Core tension:** *the town is a PC the whole table shares.* Investing in it is play, not bookkeeping.

**Choices:** (a) who drives it (GM-authored generator FL / player-facing advancement tree West); (b) the attribute set; (c) the state-roll frequency (monthly vicissitudes vs seasonal Fortune).

**Powers:** FL Villages, West Your Town. `09 §5`.

---

### P14 — Encounter engine (weighted random table with memory)

**Definition:** A D66 matrix keyed by terrain/context, producing entries that are *situational* (modified by party state), with a **reoccurring-encounter** rule that lets surviving threats return — giving the sandbox memory.

**Core tension:** *the world is random but not forgetful.* Encounters feel emergent, not scripted, yet consequences persist.

**Choices:** (a) matrix density (FL's 44 entries × 9 terrain columns vs authored-scenario encounters); (b) situational modifiers; (c) the memory rule pattern (reoccurring table).

**Powers:** FL's encounter engine; West's faction clocks are a non-table instance of the same "world with memory" pattern. `09 §4`.

---

### P15 — Pressure-economy loop (the meta-pattern)

**Definition:** The engine's deep structure: every resource (time, body, gear, Willpower/Faith, safety, org-strength) is under *pressure*; pressure forces a *decision*; the decision produces a *consequence* that changes *state*; the new state generates the next pressure.

**Core tension:** *ambition is tied to exposure.* This is not a rule pattern but the *shape* of all the above patterns together.

**Choices:** the *source* of pressure (the engine supports many: time blocks, harm, scarcity, faction clocks, weather, condition tracks).

**Powers:** everything. This is the engine's thesis as a pattern. `10 §3,§4`. **Read this pattern last — it is the meta-pattern the other 14 instantiate.**

---

## 5. Advanced compositions (AC1-AC17)

These are not new core patterns. They are repeatable 2-3 pattern fusions that occur often enough in new-game design that an agent should recognize them by name. Use them after choosing a core pattern, not before.

| ID | Composition | Shape test | Use when | Do not use when | Choices | Math/tempo notes | Example transplants |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AC1** | Clocks/fronts | A threat advances in visible segments | Time pressure matters more than exact distance | The threat should be random, not telegraphed | Segment count, tick trigger, reveal level | 4-6 segments for scenes, 8-12 for arcs | monster hunt, siege, scandal, storm |
| **AC2** | Relationship edges | The important state is between entities | Factions, patrons, crews, families matter | Only one reputation score matters | Edge scale, propagation, decay | Propagation should round toward zero | faction bonds, party trust, patron favor |
| **AC3** | Revelation ladder | Information unlocks in ordered layers | Mysteries must progress under failed rolls | Players can solve by free conversation alone | clue cost, inference risk, false lead cost | Never gate mandatory progress behind one roll | conspiracies, research, ruins, diagnosis |
| **AC4** | Stance track | Current posture changes legal actions | Tactics hinge on aggression/caution/cover | It only adds a passive bonus | stance count, switch cost, lock triggers | Switching as FAST is strong; free switching is suspect | duel guard, stealth exposure, social posture |
| **AC5** | Heat/wanted pressure | Attention rises from risky action | Crime, rebellion, surveillance, monster scent | Consequences should be immediate only | cap, tick trigger, cooldown, thresholds | Heat should rise on success too | law attention, corp trace, divine wrath |
| **AC6** | Vow/oath engine | A promise grants power and creates debt | Identity and obligation should bind rules | The promise is pure flavor | vow scope, breach trigger, atonement | Breach must cost play, not only narration | paladin oath, crew code, revolutionary cell |
| **AC7** | Crew-role menu | A group asset needs simultaneous jobs | Ships, mechs, squads, heists, rituals | One specialist should own the scene | station list, unfilled-slot cost | No PC should cover two critical roles for free | bridge crew, siege team, surgery team |
| **AC8** | Vehicle-as-character | A machine has stats, harm, upkeep, growth | Vehicle is a co-star | It is only transport | attributes, criticals, stations, repair | Damage must route back to crew/base | starship, mech, caravan, train |
| **AC9** | Territory control | Map regions have pressure and ownership | Turf, domains, fronts, patrols matter | Location is only backdrop | region stats, turn length, contest action | Seasonal turns prevent bookkeeping flood | gang turf, kingdom, wasteland route |
| **AC10** | Rumor economy | Public story spreads and mutates | Fame, fear, myths, propaganda matter | Private reputation is enough | rumor die, spread trigger, distortion table | Snowballing needs decay or backlash | outlaw legend, saint cult, celebrity |
| **AC11** | Reputation propagation | One act affects connected groups | Social web should feel alive | Factions are isolated quest boards | bond scale, propagation formula, caps | Cap propagated shifts below direct shifts | politics, trade guilds, clans |
| **AC12** | Ritual/project track | A long task accumulates progress and risk | Invention, research, magic, repair need scenes | A single roll is enough | threshold, roll cadence, mishap trigger | Too many rolls floods Willpower/Faith | spell forging, cure research, fortress build |
| **AC13** | Life Events | A character's past is generated as gains, scars, debts, and unfinished business | Backstory should produce rules-facing hooks | Background should be pure player-authored color | turn count, mark thresholds, Wear, mustering out | Deep and fast generation must produce equal power | war record, academy years, prison stretch |
| **AC14** | Menace pool | GM pressure is a visible spendable pool | Heroic play needs dramatic counterpressure | The GM should act only through hidden fiction | starting pool, gain triggers, spend menu, cap | Menace should buy pressure, not cancel success | villain budget, divine wrath, corp response |
| **AC15** | Holdings and Territory | Claims on a map/social space have control, labor, routes, and contest | Owning land/turf should create play | The base is only a rest spot | Control score, claim state, worker units, road/watch bonuses | Run monthly/seasonally to avoid bookkeeping flood | gang turf, colony, estate, ship network |
| **AC16** | Riches in the Land | A find has a deposit die, yield, hauling, depletion, and recovery | Resources should be worked over time | Loot should be one-and-done | deposit die, yield type, depletion trigger, hauling risk | Heavy exploitation rolls depletion twice | mine, salvage field, data vault, herb grove |
| **AC17** | Strange Devices | A crafted object has charges, upkeep, misfire, rare parts, and repair | Gear should feel wondrous but unsafe | It is just a normal weapon tag | charge model, misfire table, repair gate, legality | Strong/reliable/cheap/discreet/easy: pick two | alchemy, gadget, alien tool, prototype |

Each composition should still cite its core pattern parents. Example: Heat/wanted pressure is usually P2 inverted + P4 threshold fallout + AC1 clock behavior.

## 6. How patterns compose

Patterns are not meant to be used in isolation. The engine's systems are *compositions*:

- **Combat** = P1 (push) + P3 (success ladder) + P8 (feature grammar) + P4 (crit table) + the action budget (a special-case labor-distribution puzzle akin to P6).
- **Magic** = P1 + P2 (WP fuel) + P4 (mishap families) + P8 (spell tags) + P5 (ingredients as resource die, sometimes).
- **A Stronghold** = P7 (lifecycle) + P8 (functions as tags) + P4 (events table) + P5 (upkeep as resource die, sometimes) + optionally P9 (climb a rung).
- **Travel** = P6 (activity menu) + P1 (per-activity rolls) + P4 (mishap tables) + P5 (food/water resource dice) + P14 (encounter engine).
- **A Town** = P13 (settlement-as-character) + P7 (lifecycle) + P4 (fortune rolls) + P14 (memory).

**The composition move is the core of `18-reinvention-method.md`.** A "new system" is usually a new composition of existing patterns — not a new pattern. Before inventing a rule pattern from scratch, scan this catalog and ask: *which composition of P1–P15 already does what I need?*

## 7. Invariant spine vs. composable surface

The Divergence Map (`12 §12`) established that the engine is an **invariant spine + 5 choices**. This file reframes that finding for the *generative* layer:

- **The invariant spine** = P1 (push), P2 (Willpower/Faith), P3 (success ladder), P15 (the pressure loop). These four appear in *every* YZE game and cannot be removed without breaking the engine.
- **The composable surface** = P4–P14. These are optional, mix-and-match, and genre-determined. A designer chooses which to instantiate and how to calibrate each.

**The genius-level move** (the subject of `18`) is recognizing that a pattern's *home system* is arbitrary. P4 (typed D66 tables) lives in "harm" in both books — but it works identically for *social* consequences, *research* backfires, *pilot* mishaps, *ritual* fallout. P6 (activity menu) lives in "travel" — but it powers *heist planning*, *starship crew actions*, *siege operations*. The pattern doesn't care what nouns you paste on it. **This is the engine's deepest kind of reuse, and it is what `17` and `18` are about.**

## 8. Design intent

This file exists because the engine systems (`00`–`15`), for all their completeness, answer the wrong first question for a *designer*. Those files say "here is the engine; configure it." A designer's actual first question is "what do I have to build with?" Without a named palette of proven-portable patterns, a designer (especially an AI) will either (a) reinvent pattern rules badly from scratch, or (b) copy a whole system verbatim when only one of its patterns was needed.

The patterns catalog solves both failure modes:

- **It prevents reinvention.** "I need a way to track dwindling sanity" → reach for P5 (resource die), don't invent a new track. "I need ship combat to feel different from melee" → reach for P8 (feature grammar) with new tags, don't write a new combat system.
- **It prevents over-cloning.** "I want magic in my sci-fi game" → reach for P4 (typed D66 tables, the mishap pattern) + P2 (Willpower/Faith fuel), *not* the whole FL magic chapter. The pattern is the *transferable unit*, not the system.

The 15 patterns below are not exhaustive — they are the ones the two source games *prove* port. The advanced compositions are the next layer up: common fusions that let an agent build genre-specific systems without inventing a parallel engine. A designer who internalizes both layers and then applies `18`'s composition method can generate novel rules that nonetheless inherit the engine's hard-won balance and feel — which is what "genius-level designer, but reproducible" means.
