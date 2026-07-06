<!-- markdownlint-disable MD013 MD024 -->

# Reinvention Method — How to Invent New Mechanics from Old Ones

> This is the **composition** layer of the generative method — the final, highest-value layer of the skill. `16` gave the palette of proven-portable primitives; `17` showed how each primitive changes psychology at different calibrations. This file teaches the move that defines "genius-level design, reproducible": **take a primitive out of its home system and deploy it in a foreign system to produce a genuinely new mechanic that inherits the engine's balance and feel.** Read this when the task is *invent a new mechanic*, not *configure an existing one*.

## Contents

1. Source provenance
2. Abstraction target
3. The core move — primitive transplantation
4. The five reinvention operators
5. The composition checklist
6. Worked examples (five full reinventions)
7. Anti-patterns (what NOT to do)
8. Design intent

## Source provenance

This file is the generative *consequence* of `16` (primitives) and `17` (dual-use). The method it teaches is abstracted from the empirical fact that FL and West are *themselves* reinventions of each other — the same primitives, transplanted and recalibrated, producing opposite games. Every operator below is a generalization of a move the source designers actually made.

Cross-links to the engine systems: `13-balance-and-synergy.md` (validate the reinvented mechanic before shipping), `14-recipes-new-game-new-rule.md` Recipe B (the validation pipeline this file's output must pass), `10-design-philosophy.md` §10 (the Warning Signs this file's anti-patterns extend).

## Abstraction target

The recipes layer (`14` Recipe A) assembles a new game from documented dials — *it does not invent new mechanics.* This file closes that gap. The deliverable is a **reproducible ideation method**: a small set of *operators* that take a primitive (from `16`) and a target domain, and produce a candidate mechanic — plus a composition checklist and worked examples showing the operators in action.

**The thesis:** *almost no "new mechanic" is actually new.* Most are *transplants* — a primitive from one system, redeployed in another, recalibrated to produce a target psychology. The genius-level move is not invention ex nihilo; it is *recognition* — seeing that the activity-menu primitive (which powers travel) also powers heist planning; that the typed-D66 primitive (which powers crits) also powers social-consequence spirals; that the resource-die primitive (which powers food) also powers sanity. This file teaches that recognition as a method.

## 3. The core move — primitive transplantation

**One sentence:** *to invent a mechanic, take a primitive that already works in system A, ask "what other resource/pressure/decision in my game has the same shape," and redeploy the primitive there with new nouns and a recalibrated psychology.*

**Why this works (and why it's better than inventing from scratch):**

1. **The primitive is pre-balanced.** P1–P15 have been stress-tested in two published games. A transplant inherits their math and feel; an invention starts from zero.
2. **The primitive is pre-playtested for fun.** The push, the resource die, the activity menu *feel good* — that's why they recur. A transplant inherits the feel; an invention gambles.
3. **The primitive is engine-consistent.** It already uses ⚔/💀, the success ladder, the push economy, the metacurrency. A transplant fits the engine by construction; an invention has to be made to fit.
4. **The transplant produces *novelty in composition, not in mechanism.* ** The newness comes from *where* you put the primitive, not *what* it is. This is the engine's own trick: FL's novelty over West is *calibration and composition,* not new mechanisms.

**The risk:** a transplant can be *wrong* — the primitive's tension may not match the target domain, or the composition may break the engine's pressure loop. That's what the composition checklist (§5) and the validation pipeline (`13 §8`) are for.

## 4. The five reinvention operators

These are the *moves* a designer makes. Each is a generalization of moves the source designers made between FL and West. Apply them to a primitive from `16` to generate a candidate mechanic.

### Operator 1 — DOMAIN TRANSFER

**Move:** Take a primitive that powers system A and deploy it unchanged in system B, where system B has the same *shape* of resource/pressure/decision as A.

**The recognition test:** "Does system B have a [depleting stock / mutually-exclusive labor / typed consequence / capped refueling pool / five-beat lifecycle]?" If yes, the matching primitive ports.

**Examples:**
- P5 (resource die) lives in *food* (FL). Transfer to **sanity** → a Sanity die (D6–D12) that steps down on use and depletes at D6+1–2. *Same mechanic, new domain.*
- P5 (resource die) → **morale** (a band's Morale die), **town prosperity** (a Prosperity die), **illness duration** (a Disease die that steps *down* as you recover).
- P6 (activity menu) lives in *travel.* Transfer to **heist planning** → a menu of crew roles (Hacker/Wheel/Face/Muscle/Lookout), each a mutually-exclusive job per planning phase.
- P6 (activity menu) → **starship bridge** (Helm/Tactical/Engineering/Comms/Medical), **siege operation** (Sappers/Archers/Commanders/Sappers/Relief), **court intrigue** (Spy/Steward/Champion/Diplomat/Chronicler).
- P4 (typed D66) lives in *harm.* Transfer to **social consequence** → a Social Fallout table (Tens = relationship affected, Units = severity), with families for Rival / Patron / Lover / Faction.

**Domain transfer is the workhorse operator.** Most "new mechanics" are domain transfers of P4, P5, P6, or P7.

### Operator 2 — INVERSION

**Move:** Take a primitive and reverse its direction or its cost/benefit polarity, producing the *opposite* psychology.

**The recognition test:** "What happens if the pool fills instead of empties / the cost becomes a benefit / the table produces boons instead of consequences?"

**Examples:**
- P5 (resource die) normally *depletes* (steps down). **Invert** → a *Rumor* die that *grows* (steps up) as you spread a legend, generating bigger payoffs the longer you invest. Same mechanic, opposite polarity → opposite feel (attrition → snowball).
- P1 (push) normally costs. **Invert** the cost polarity → a "Momentum" push where successful pushes *earn* instead of costing (a snowball-combat variant). Same primitive, inverted economy.
- P10 (protected dial) — FL's Pride *grows* when unused. **Invert** → a "Doom" die that *grows* when you *do* use a forbidden power, producing an escalating-corruption variant.

**Inversion is the highest-leverage novelty operator** — one reversal produces a mechanic that *feels* new (because the psychology is opposite) while being *technically* familiar (so it's balanced).

### Operator 3 — RECALIBRATION (from `17`)

**Move:** Take a primitive, keep its domain, but change its calibration to produce a target psychology from the dual-use matrix (`17`).

**The recognition test:** Scan `17`'s matrix; find the psychology you want; set the dials to the calibration that produces it.

**Examples:**
- You want a game about *caution,* not aggression. Recalibrate P2 (metacurrency) from harm-refuel (FL) to success-refuel. *Same pool, opposite behavior.*
- You want harm to feel *specific.* Recalibrate P4 (typed table) from a single master table (West) to a family of 6 typed tables. *Same architecture, deeper flavor.*
- You want the campaign to be *about community.* Recalibrate P9 (org ladder) by capping the ceiling at Town. *Same lifecycle, focused subject.*

**Recalibration is what FL and West did to each other.** It is the most proven move in the engine.

### Operator 4 — FUSION (composition)

**Move:** Combine two or more primitives to produce a composite mechanic neither could produce alone.

**The recognition test:** "What decision would emerge if primitive X and primitive Y shared a resource pool / triggered each other / opposed each other?"

**Examples:**
- Fuse P2 (metacurrency) + P4 (typed table) → a *Corruption* system: pushing dark powers refuels your pool (P2, harm-style) but rolls on a Corruption table (P4) that produces specific moral injuries. The fusion produces a doom spiral neither primitive makes alone.
- Fuse P6 (activity menu) + P1 (push) → a *Crew Stress* system: each unfilled menu slot at the end of a phase generates a "stress push" the GM makes against the party. The menu *itself* becomes a pressure source.
- Fuse P5 (resource die) + P7 (org lifecycle) → a *Faction Strength* die: the org's overall vigor is a D12 that steps down on failed upkeep events and depletes when the org collapses — a single die replacing a bookkeeping-heavy stat block.

**Fusion is where genuine novelty lives.** Most "signature" mechanics of a new game are fusions of 2–3 primitives around a shared fiction (corruption, heat, momentum, doom, renown).

### Operator 5 — ABSTRACTION-CLIMB

**Move:** Take a primitive that operates at one *scale* and deploy it at a higher or lower scale (using P9's ladder logic).

**The recognition test:** "Does this primitive work the same at the party / org / faction / polity scale, just with a different turn length?"

**Examples:**
- P1 (push-and-pay) operates at *character* scale (a roll). **Climb** to *faction* scale → a faction can "push" a Season-Turn roll by accepting Burden (the faction-scale cost face). Same primitive, scale-jumped.
- P4 (typed table) operates at *character* harm. **Climb** to *settlement* scale → a Settlement Vicissitude table is exactly P4 at the place-scale (FL already does this).
- P10 (protected dial) operates per-PC. **Climb** to *party* scale → a shared "Renown" die the whole party escalates and spends together.

**Abstraction-climb is the engine's scale-escalation trick** — the same primitive powers character, party, org, faction, and polity play, just on different turn lengths.

## 5. The composition checklist

Before shipping a reinvented mechanic, verify:

- [ ] **Primitive identified.** Which of P1–P15 is this a transplant/inversion/fusion of? (If "none," you may be reinventing from scratch — go back to `16` and check.)
- [ ] **Domain match.** Does the target domain have the same *shape* (depleting stock / mutually-exclusive labor / typed consequence / etc.) as the primitive's home? (Domain Transfer test.)
- [ ] **Psychology targeted.** Which cell of `17`'s matrix does this calibration produce? Is it the one you want?
- [ ] **Cost-consistency.** Does the reinvented mechanic's cost type match the game's master cost model (`12` degree-of-freedom 1)? (A harm-cost game and a currency-cost game should not mix cost types without intent.)
- [ ] **Pressure-loop integrity.** Does the mechanic *add* a pressure→decision→consequence loop, or does it *short-circuit* one? (If it removes a decision, it's probably bad — see `10 §10` subsystem inflation.)
- [ ] **Engine fit.** Does it use ⚔/💀, the success ladder, the push economy, the metacurrency? (If it introduces a new dice type or a parallel economy, justify it.)
- [ ] **Validation passable.** Will it survive `13 §8`'s pipeline (intent → math → exploit → synergy → table → verdict)? Run the check.
- [ ] **Anti-pattern scan.** Does it trigger any of `10 §10`'s Warning Signs or §7 below?

## 6. Worked examples (five full reinventions)

Each shows the operator, the primitive, the transplant, and the result.

### Worked 1 — Sanity as a Resource Die (Domain Transfer, P5)

**Problem:** "I want sanity tracking in my horror game, but hate bookkeeping."
**Operator:** Domain Transfer.
**Primitive:** P5 (resource die), which powers food in FL.
**Move:** Sanity is a D8. Every time you witness something shattering, roll the Sanity die; on 1–2 it steps down (D8→D6). At D6+1–2 you break. Therapy / rest / safety steps it back up.
**Why it works:** sanity has the same *shape* as food (depleting stock, refuelable, "running out" is the crisis). The transplant inherits P5's pre-balanced depletion curve and its "consumption is a gamble" feel — which is *exactly* right for horror (each witness roll is terrifying).
**Calibration (`17`):** deplete range 1–2 standard; widen to 1–3 for grindhouse horror.
**Validate:** `13 §8` — math (expected sanity length), exploit (can you farm refuels? gate them), table (one extra roll per scene — acceptable).

### Worked 2 — Heat as a Push Economy (Domain Transfer + Fusion, P1 + P2)

**Problem:** "I want a cyberpunk 'Heat' tracker that feels like the core loop, not a separate tally."
**Operator:** Domain Transfer + Fusion.
**Primitives:** P1 (push) + P2 (metacurrency), inverted polarity on the refuel.
**Move:** Heat is a pool (cap 10). Every illegal action *rolls the Heat pool* like a push — sixes = "the law notices" (a consequence). Heat *grows* with crimes (snowball, Operator 2 inversion). You can "cool" Heat by laying low (action-refuel, inverted: action *reduces* the pool).
**Why it works:** Heat has the same shape as a metacurrency (capped pool, spends/earns), but inverted (you want it *low*). The fusion with P1 makes crimes *risky in the engine's own grammar* — you roll Heat like you roll dice, sixes hurt. It feels like the core loop because it *is* the core loop, inverted.
**Calibration (`17`):** refuel = action-earned (laying low), inverted polarity.
**Validate:** `13 §8` — math (how fast does Heat hit cap?), exploit (can you alternate crime/lay-low infinitely? add escalating cool-downs).

### Worked 3 — Social Conflict as Typed Consequence Families (Domain Transfer, P4)

**Problem:** "I want social conflict to produce *specific* consequences, not just '−2 to a stat.'"
**Operator:** Domain Transfer.
**Primitive:** P4 (typed D66 table), which powers FL's 8 critical-injury families.
**Move:** Build a **Social Fallout** table — D66, Tens = relationship affected (Patron / Rival / Lover / Faction / Community / Self), Units = severity (1–2 embarrassment ... 6–6 rupture). Build 3–5 *typed families* by social context (Court / Street / Underworld / Family / Professional), each with its own flavor.
**Why it works:** social harm has the same shape as physical harm (typed by source, scaled by severity, with a maim/die climax at 65/66 — here: "ostracism" / "permanent enmity"). The transplant inherits P4's "specific and memorable" psychology without inventing a new resolution system.
**Calibration (`17`):** family count 3–5 (medium density) — enough that the *kind* of social harm matters, not so many it's bookkeeping.
**Validate:** `13 §8` — exploit (can you avoid social conflict entirely? ensure the table triggers on failures in social scenes).

### Worked 4 — A "Doom" Protected Dial (Inversion, P10)

**Problem:** "I want a dark-fantasy mechanic where using power *feels* like a bargain with ruin."
**Operator:** Inversion.
**Primitive:** P10 (protected dial), which powers FL Pride (grows when unused, spends for a peak).
**Move:** A **Doom** die (D8/D10/D12). Every time you cast a forbidden spell, the Doom die is rolled; on a 6+ it *grows* (D8→D10→D12). At D12, the next 6+ triggers a catastrophe (the GM rolls on a Doom table = P4). You can *spend* Doom down by undertaking penance (a quest).
**Why it works:** Pride grows when *avoided*; Doom grows when *used.* Exact inversion. The transplant inherits P10's escalation logic but flips its polarity — producing a doom-spiral instead of a hero-arc. Same primitive, opposite feel.
**Calibration (`17`):** inverted P10 + fused with P4 (Doom table) at the climax.
**Validate:** `13 §8` — math (how many casts to D12?), exploit (can you farm penance? gate it to quests), table (does the doom spiral feel earned or punitive?).

### Worked 5 — Starship Bridge as Activity Menu (Domain Transfer, P6)

**Problem:** "I want starship combat to feel like a crew, not a pilot."
**Operator:** Domain Transfer.
**Primitive:** P6 (activity menu), which powers FL travel.
**Move:** Each bridge Round, each PC picks **one** station action from a menu: **Helm** (maneuver/evade), **Tactical** (fire/lock-on), **Engineering** (power to systems/repair), **Comms** (jam/scan/hail), **Medical** (treat/boost). Critically — the menu is designed so that *a ship cannot do all of these well at once* (P6's mutually-exclusive-labor principle). Power rerouted to weapons means less for shields; the medic can't also be the gunner.
**Why it works:** bridge crew has the same shape as travel (a party distributing labor across mutually-exclusive demands in a time block). The transplant inherits P6's "coordination is the tactic" psychology — which is *exactly* what bridge drama wants.
**Calibration (`17`):** formal menu (FL-style, 5 stations), each station with its own action list.
**Validate:** `13 §8` — table (does each station feel meaningful? ensure no station is always-optimal), synergy (do station combinations produce exploits? e.g. Engineering always-powers-Tactical).

## 7. Anti-patterns (what NOT to do)

These extend `10 §10`'s Warning Signs into the generative layer.

- **Reinventing a primitive from scratch.** If your "new mechanic" is a depleting track / a labor menu / a consequence table / a capped pool — you are reinventing P5/P6/P4/P2. Stop. Use the primitive; don't rebuild it. *(Wastes effort; produces an un-balanced variant.)*
- **Transplant without domain-match.** Forcing a primitive into a domain that lacks its required shape. (P5 resource die only works where there is genuinely a *depleting stock with a "running out" crisis* — not every track qualifies.) *(Mechanic feels wrong; the shape mismatch shows.)*
- **Inconsistent cost model.** A reinvented mechanic whose cost type contradicts the game's master cost model (`12` degree-of-freedom 1) without intent. A harm-cost game with a currency-cost subsystem feels incoherent. *(Breaks engine consistency — `10 §10` "silent invalidation.")*
- **Fusion that removes decisions.** A composite mechanic that *eliminates* a decision the engine previously required. (E.g. a fusion that makes pushing free removes the engine's signature tension.) *(Short-circuits the pressure loop.)*
- **Abstraction-climb that breaks scale.** Lifting a character-scale primitive to faction-scale without adjusting the turn length / cost threshold. *(The mechanic feels trivial at the new scale — "pushing a faction roll for free.")*
- **Over-fusion.** Combining 4+ primitives into one mechanic. The engine's sweet spot is 2–3 primitive compositions; beyond that the mechanic becomes inscrutable and un-validatable. *(Violates the "meaningful decision, not a solved problem" principle.)*
- **Inverting without re-balancing.** An inversion (Operator 2) changes the math, not just the feel. A snowball mechanic (inverted depletion) hits its climax *faster* than a depletion mechanic hits empty — recompute the breakpoints (`13 §4`). *(Produces a mechanic that spirals unexpectedly fast.)*

## 8. Design intent

This file exists because the original brief asked for a "genius-level designer" skill — and the engine systems (`00`–`15`), for all their rigor, produce an *analyst*, not a designer. An analyst can describe and configure; a designer *invents.* This file is the bridge.

The file's central claim — that *most new mechanics are transplants, not inventions* — is both a humbling and an empowering one. Humbling, because it says genius-level design is less about *inspiration* than *recognition* (seeing that sanity is a resource die; that heat is an inverted metacurrency; that a bridge crew is an activity menu). Empowering, because recognition is *teachable* in a way inspiration is not: the five operators, the palette of 15 primitives, and the dual-use matrix together form a *method* that an AI or a human can apply deliberately.

The method's guarantee: a mechanic produced by these operators will (a) inherit a primitive's pre-balanced math and pre-playtested feel, (b) fit the engine by construction (because the primitive already uses ⚔/💀 and the push economy), and (c) produce a *targetable* psychology (because `17` maps calibrations to feels). The method's risk: a bad transplant or an inconsistent fusion can break the engine's pressure loop — which is why the composition checklist (§5) and the validation pipeline (`13 §8`) are non-negotiable.

**The three generative files together — `16` (palette), `17` (calibration), `18` (composition) — complete the skill's design loop.** The engine systems (`00`–`15`) let you *understand and configure* the engine. The generative layer (`16`–`18`) lets you *extend* it into genuinely new design space, reproducibly. Together they make the skill what the brief asked for: a tool that turns the YZE's hard-won design intelligence into a transferable, generative method.
