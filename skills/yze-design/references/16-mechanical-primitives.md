<!-- markdownlint-disable MD013 MD024 -->

# Mechanical Primitives — The Reusable-Pattern Catalog

> This is the **palette** for the generative layer. The engine systems (`00`–`15`) document *what the engine is and how to configure it*. This file catalogs the ~15 load-bearing **patterns** that recur across both source games and are proven (by FL and West) to survive transplantation to new genres and new systems. `17-dual-use-matrix.md` shows what each pattern *does* at different calibrations; `18-reinvention-method.md` teaches how to combine and repurpose them. Read this file first when inventing new mechanics.

## Contents

1. Source provenance
2. Abstraction target
3. What is a "primitive"?
4. The primitive catalog (P1–P15)
5. How primitives compose
6. Invariant spine vs. composable surface
7. Design intent

## Source provenance

This file is a **synthesis over the engine systems documented in `00`–`15`**. Every primitive below is mined from the already-filled system files and cross-linked to where it is documented in depth. Primary evidence: both corebooks (see each system file's provenance). The empirical justification for calling these "primitives" is the **Divergence Map's synthesis** (`12 §12`): FL and West are the same invariant spine with five dials set to opposite ends — which means the *spine itself* is the reusable substrate, and each dial-setting *is* a primitive that has been proven to port.

**Definition of "proven to port":** a pattern appears in *both* source games (so it is not genre-specific), OR it appears in one and its *absence* in the other is the proof it is optional/additive (so it can be added to a third). The Divergence Map's "absence as data" principle (`12 §3`) applies.

## Abstraction target

The engine systems (`00`–`15`) answer *"what is the engine?"* and *"how do I configure it?"* This file answers the prior question a designer actually faces: *"what building blocks do I have to invent with?"* The goal is to lift the recurring patterns out of their home systems and present them as a **genre-neutral palette** — each one named, abstracted, parameterized, and tagged with the systems it already powers. A designer (human or AI) composing a new mechanic should be able to scan this catalog, pick a primitive, and instantiate it — rather than reinventing dice pools, push economies, or consequence tables from scratch.

This is the **palette** layer of the generative method. `17` is the **calibration** layer (what each primitive *does* at different settings). `18` is the **composition** layer (how to combine and repurpose them).

## 3. What is a "primitive"?

A **mechanical primitive** is a small, self-contained pattern of play that:

1. **Recur across at least two distinct systems** in the source games (so it is not a one-off subsystem).
2. **Is genre-neutral in structure** — its procedure abstracts cleanly away from its nouns.
3. **Carries its own internal tension** — it produces a decision, a cost, or a pressure *by design*, independent of flavor.
4. **Has identifiable parameters** — dials a designer can set when instantiating it.

A primitive is *not* a complete system. Combat is not a primitive; the **action economy** is. Magic is not a primitive; the **typed consequence table** is. Travel is not a primitive; the **activity menu** is. Primitives are the *atomic* patterns that combine into systems.

## 4. The primitive catalog (P1–P15)

Each entry: **Name** · **One-line definition** · **Core tension it creates** · **Parameters** · **Where it already powers systems** (cross-links to engine system files).

---

### P1 — Dice pool with push-and-pay

**Definition:** Roll n D6; sixes = success; after the roll you may reroll non-successes *once* by paying a cost extracted from a latent cost-face already on the dice.

**Core tension:** *Do I accept this failure, or double down and pay?* The push is the engine's signature dramatic beat — it converts a dead-end fail into a priced decision.

**Parameters:** (a) cost-face trigger — always-on-push (FL 💀) vs frame-gated (West 1s on Risky/Desperate); (b) cost *type* — self-harm / currency / gear-degradation / Trouble; (c) push limit (once, ever); (d) what excludes a die from the reroll.

**Powers:** the entire core resolution loop. `00 §3,§6`.

---

### P2 — Capped metacurrency refueled by risk

**Definition:** A pool (cap ~10) that spends on agency (pushes, talents, powers, trouble-buyoff) and refuels from *engaging the engine's risk mechanics* — taking harm, succeeding boldly, or performing in-fiction actions.

**Core tension:** *spend now for a peak, or hoard for the crisis I know is coming?* The refuel trigger is what makes the pool a *loop* rather than a countdown.

**Parameters:** (a) cap size; (b) spend targets; (c) **refuel trigger** — harm-earned (FL WP, virtuous damage loop) / success-earned (3-⚔ rolls) / action-earned (West Faith rituals); (d) depletion state (none / Shaken-lockout).

**Powers:** WP (FL), Faith (West), and — by direct reuse — *any* future pool you want to behave the same way (corruption, momentum, heat, favor). `00 §7`.

---

### P3 — Graded success ladder + threshold-raise

**Definition:** Read the raw success count on a 0/1/2/3+ ladder (fail / partial / full / critical), *and/or* allow a threshold to be raised before rolling to trade risk for a richer payoff.

**Core tension:** *settle for the safe win, or declare a bolder aim and risk getting nothing extra?*

**Parameters:** (a) number of rungs (3 or 4); (b) what surplus successes buy — Stunts / damage / clues / positioning / **carry-forward bonus** (+1 normal / +2 critical, banked for the next relevant roll, per `00 §4`) / **Success Menu entries** (each surplus ⚔ beyond the first buys one player-declared quality of a downtime or long-process output, per `00 §4`); (c) who sets the threshold (GM-side "Levels of Effort" FL / player-side "Declared Effort" West). *Note: Stunts (fixed, tactical, combat-speed) and the Success Menu (player-authored, generative, downtime-speed) are the two surplus-success spend modes — use Stunts for immediate opposed action, the Success Menu for authored long-process output, never both on the same roll.*

**Powers:** every ability roll in both games; the Stunts subsystem; combat damage scaling. `00 §4`.

---

### P4 — Typed D66 consequence table

**Definition:** A two-axis table (D66: Tens = location/category, Units = severity) producing immediate effect + long-term effect + healing/recovery time, with the `65`=maim / `66`=die climax split at the top.

**Core tension:** consequences are *specific and memorable* — "you are hamstrung" not "−2 to a stat." The table makes harm (or any failure) a story beat.

**Parameters:** (a) the **family set** — one master table (West crits) or a *family of typed tables*, one per damage/source type the genre cares about (FL's 8 crit families Slash/Blunt/Stab/Burn/Acid/Cold/Swallow/Horror; FL's 17 magic-mishap families); (b) the two axes' meanings; (c) count-modification (FL shifts the D66 roll ±10 per 💀).

**Powers:** critical injuries (`04 §5`), magic mishaps (`05 §7`), stronghold random events, faction fallout, town fortune rolls, vicissitudes. **This is the single most-reused pattern in the engine** — it appears in 6+ systems. Porting it to a new failure domain is the highest-leverage move a designer can make. `04 §5`.

---

### P5 — Resource die (depleting step-die)

**Definition:** A supply is tracked as a single die (D6–D12); each use rolls it; on a 1–2 (or wider) the die steps *down*; at D6 + 1–2 the supply is depleted. Finding/buying more steps the die *up*.

**Core tension:** *consumption is a gamble, not bookkeeping.* You don't count arrows; you roll the Arrows die and feel the supply thin.

**Parameters:** (a) die range (D6–D12); (b) **contraction (deplete) range** — 1–2 is the base default for most engine mechanics, but it is **not law**: a perishable or volatile supply contracts faster (FL's raw meat as food = 1–4; West's perishables similar). The contraction range is a **per-instance dial**: a more powerful or unstable resource can be set to 1–3, 1–4, even 1–5. *Interaction with die size:* a wider contraction range means the die steps down faster on each use, so a **larger starting die** is needed to retain the resource through multiple uses. Putting a powerful, fast-contracting resource in a small die guarantees it is spent after one use — sometimes desirable (a single-shot miracle), sometimes not. This interaction is load-bearing in the Vancian spell-slot pattern (`workshop/08` Archetype 1): a rank-1 spell in a D6 slot with contraction 1–2 depletes ~33% per cast; a rank-5 spell with contraction 1–4 in the same D6 slot is *certain* to be spent on first use, forcing the caster to invest in a larger slot die (D10–D12) to retain it. (c) what it models (FL default: food/water/arrows/torches; West optional module; *reusable for*: morale, faction strength, town prosperity, illness duration, sanity, **spell slots** per `workshop/08` #1).

**Powers:** FL consumables (default), West consumables (optional), and — by reinvention — any depleting stock. `01 §7`, `08 §10`.

---

### P6 — Activity menu (labor-distribution puzzle)

**Definition:** In a structured time block, each PC picks **one** activity from a fixed menu; the menu is designed so that critical demands (move / navigate / watch / supply / recover) are *mutually exclusive* — so the party is always short of hands.

**Core tension:** *you cannot do everything; who does what?* Distributes the party's labor so every PC has a job and the cost of specialization is visible.

**Parameters:** (a) menu breadth (FL's 14-row formal menu vs West's ~6–8 implicit jobs); (b) solo vs shared tagging; (c) what demands are mutually exclusive.

**Powers:** the journey/travel loop in both games (`06 §5`), and — by reinvention — heist planning, ship crew actions, heist/social-scene frameworks, research teams. **This is the most directly portable structural pattern.** `06 §5`.

---

### P7 — Five-beat org lifecycle

**Definition:** Any persistent player- or faction-owned entity runs on five beats: **founding (predicate gate + optional founding flaw) → functions (named improvements) → upkeep (resource obligation + degeneration table) → events (procedural/world pressure) → scale (climb a rung or cap).**

**Core tension:** *owning a thing is a commitment, not a trophy.* The org is alive and threatened; neglect costs it.

**Parameters:** (a) founding predicate (cleared site / spent Capital / recruited headcount / seat + basis of rule); (b) function list; (c) upkeep vectors (1–3); (d) event source (random D66 / procedural turn / tracked relationship); (e) **ladder ceiling** (the meta-dial — what the campaign is *about*).

**Powers:** Strongholds, Mercenary Companies, Factions, Outlaw Bands, Towns, Businesses, Property — *every* persistent org in both games. `07 §3`. **Proof-by-construction that one pattern scales from a single room to a polity.**

---

### P8 — Feature grammar (composable tags, not stat lines)

**Definition:** Items (weapons, armor, gear, *and characters via talents*) are defined by a set of composable **tags**, each of which gates an action, modifies a roll, or enables a rule — rather than by a monolithic stat block.

**Core tension:** *loadout drives tactical options.* Your weapon is what you can *do*, not a damage number.

**Parameters:** (a) tag-source layering (FL: tags double as action-prerequisites, e.g. Parrying→PARRY, Hook→SHOVE; West: three layers Features/Qualities/Conditions); (b) positive vs negative tags; (c) stacking rules.

**Powers:** all weapons/armor/gear (`08 §6`), the talent system (talents *are* feature tags on characters), NPC special abilities. `08 §6`.

---

### P9 — Scale ladder (escalation rungs)

**Definition:** Orgs climb rungs — **Solo → Party → Band → Company → Faction → Army → Polity** — each re-using the same lifecycle beats (P7) at a larger turn scale, until an abstraction-collapse mechanism collapses bookkeeping past a threshold.

**Core tension:** *a campaign can escalate in scope without changing engines.* The ladder lets a party grow into a power without a system switch.

**Parameters:** (a) which rungs are enabled (the **ceiling dial** — the campaign's most consequential scope decision); (b) turn scale per rung (Round/Shift/Season/Year); (c) abstraction-collapse threshold (~30–50 bodies → Host Play/Ledger).

**Powers:** the entire FL org stack; West caps at Company/Town by design. `07 §9`. **The ceiling is what the campaign is *about* — individuals, communities, or power.**

---

### P10 — Protected dial (per-session pressure-relief)

**Definition:** Each PC has a personal resource — a once-session escalating die (FL Pride) or a broad currency (West Faith) — wired to character identity, that converts a loss into a win or buys off failure.

**Core tension:** *the player's personal safety net, loaded with identity.* When it's spent/lost, that's a story beat, not just a number.

**Parameters:** (a) form (die added to roll vs currency spent); (b) scope (narrow — only protective rolls — vs broad — the whole loop); (c) escalation model (D8→D10→D12, grows when unused/successful, shrinks on failure); (d) identity load (a note vs a one-sentence belief).

**Powers:** Pride (FL), Faith (West), and — by reinvention — any per-PC "conviction/anchor" resource. `01 §5`, `00 §7`.

---

### P11 — Dual fast + deep generation

**Definition:** Character creation offers two paths — **fast** (pick an archetype/kin + age → 15 min) and **deep** (a lifepath that produces emergent backstory) — both calibrated to produce *equivalent-power* characters.

**Core tension:** *none — this is an accessibility pattern.* It serves two player populations without splitting the rules.

**Parameters:** (a) the fast-gen identity selector (kin / archetype / lineage / role); (b) age-as-sub-dial (trades attributes for skills/talents); (c) lifepath depth (number of "Livings"/formative-event rolls).

**Powers:** both games' character creation. `01 §8`.

---

### P12 — General / Situational / Optional layering

**Definition:** Rules are classified into three layers: **General** (always on, the core), **Situational** (applies in specific contexts), **Optional** (mode-switching modules). Optional rules are *explicitly labeled* so the core stays lean.

**Core tension:** *none — this is a complexity-management pattern.* It lets the engine ship a lean core while offering depth where wanted.

**Parameters:** (a) how big the Optional surface is (FL large; West small); (b) how Optional rules are flagged (callout boxes / appendix / dedicated book).

**Powers:** the entire architecture of both books. `10 §9`.

---

### P13 — Settlement-as-character

**Definition:** A settlement is modeled as a **character sheet for a place** — attributes (Aspects/vicissitude-variables), a state machine (Prosperity/Standing), internal-faction pressure gauges (Need/Heat/Feud), a resource economy, and a growth mechanism driven by player investment.

**Core tension:** *the town is a PC the whole table shares.* Investing in it is play, not bookkeeping.

**Parameters:** (a) who drives it (GM-authored generator FL / player-facing advancement tree West); (b) the attribute set; (c) the state-roll frequency (monthly vicissitudes vs seasonal Fortune).

**Powers:** FL Villages, West Your Town. `09 §5`.

---

### P14 — Encounter engine (weighted random table with memory)

**Definition:** A D66 matrix keyed by terrain/context, producing entries that are *situational* (modified by party state), with a **reoccurring-encounter** rule that lets surviving threats return — giving the sandbox memory.

**Core tension:** *the world is random but not forgetful.* Encounters feel emergent, not scripted, yet consequences persist.

**Parameters:** (a) matrix density (FL's 44 entries × 9 terrain columns vs authored-scenario encounters); (b) situational modifiers; (c) the memory mechanism (reoccurring table).

**Powers:** FL's encounter engine; West's faction clocks are a non-table instance of the same "world with memory" pattern. `09 §4`.

---

### P15 — Pressure-economy loop (the meta-primitive)

**Definition:** The engine's deep structure: every resource (time, body, gear, metacurrency, safety, org-strength) is under *pressure*; pressure forces a *decision*; the decision produces a *consequence* that changes *state*; the new state generates the next pressure.

**Core tension:** *ambition is tied to exposure.* This is not a mechanism but the *shape* of all the above primitives together.

**Parameters:** the *source* of pressure (the engine supports many: time blocks, harm, scarcity, faction clocks, weather, condition tracks).

**Powers:** everything. This is the engine's thesis as a pattern. `10 §3,§4`. **Read this primitive last — it is the meta-pattern the other 14 instantiate.**

---

## 5. How primitives compose

Primitives are not meant to be used in isolation. The engine's systems are *compositions*:

- **Combat** = P1 (push) + P3 (success ladder) + P8 (feature grammar) + P4 (crit table) + the action economy (a special-case labor-distribution puzzle akin to P6).
- **Magic** = P1 + P2 (WP fuel) + P4 (mishap families) + P8 (spell tags) + P5 (ingredients as resource die, sometimes).
- **A Stronghold** = P7 (lifecycle) + P8 (functions as tags) + P4 (events table) + P5 (upkeep as resource die, sometimes) + optionally P9 (climb a rung).
- **Travel** = P6 (activity menu) + P1 (per-activity rolls) + P4 (mishap tables) + P5 (food/water resource dice) + P14 (encounter engine).
- **A Town** = P13 (settlement-as-character) + P7 (lifecycle) + P4 (fortune rolls) + P14 (memory).

**The composition move is the core of `18-reinvention-method.md`.** A "new system" is usually a new composition of existing primitives — not a new primitive. Before inventing a mechanism from scratch, scan this catalog and ask: *which composition of P1–P15 already does what I need?*

## 6. Invariant spine vs. composable surface

The Divergence Map (`12 §12`) established that the engine is an **invariant spine + 5 dials**. This file reframes that finding for the *generative* layer:

- **The invariant spine** = P1 (push), P2 (metacurrency), P3 (success ladder), P15 (the pressure loop). These four appear in *every* YZE game and cannot be removed without breaking the engine.
- **The composable surface** = P4–P14. These are optional, mix-and-match, and genre-determined. A designer chooses which to instantiate and how to calibrate each.

**The genius-level move** (the subject of `18`) is recognizing that a primitive's *home system* is arbitrary. P4 (typed D66 tables) lives in "harm" in both books — but it works identically for *social* consequences, *research* backfires, *pilot* mishaps, *ritual* fallout. P6 (activity menu) lives in "travel" — but it powers *heist planning*, *starship crew actions*, *siege operations*. The primitive doesn't care what nouns you paste on it. **This is the engine's deepest kind of reuse, and it is what `17` and `18` are about.**

## 7. Design intent

This file exists because the engine systems (`00`–`15`), for all their completeness, answer the wrong first question for a *designer*. Those files say "here is the engine; configure it." A designer's actual first question is "what do I have to build with?" Without a named palette of proven-portable patterns, a designer (especially an AI) will either (a) reinvent primitive mechanics badly from scratch, or (b) copy a whole system verbatim when only one of its primitives was needed.

The primitives catalog solves both failure modes:

- **It prevents reinvention.** "I need a way to track dwindling sanity" → reach for P5 (resource die), don't invent a new track. "I need ship combat to feel different from melee" → reach for P8 (feature grammar) with new tags, don't write a new combat system.
- **It prevents over-cloning.** "I want magic in my sci-fi game" → reach for P4 (typed D66 tables, the mishap pattern) + P2 (metacurrency fuel), *not* the whole FL magic chapter. The primitive is the *transferable unit*, not the system.

The 15 primitives below are not exhaustive — they are the ones the two source games *prove* port. A designer who internalizes this catalog and then applies `18`'s composition method can generate novel mechanics that nonetheless inherit the engine's hard-won balance and feel — which is what "genius-level designer, but reproducible" means.
