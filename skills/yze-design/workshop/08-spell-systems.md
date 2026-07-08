<!-- markdownlint-disable MD013 MD024 -->

# Spell Systems — The Magic-System Archetype Catalog

> **STATUS: WORKSHOP MODULE.** A system-level typology of *how magic works* in roleplaying games — not a list of spells, but a catalog of the **archetypes** by which a game acquires, stores, and expresses magical power. Each archetype is built engine-natively from the power layer (`05`) and the primitives (`16`), so a designer can drop any of them into a YZE-family game. Sits *above* individual spell design (`09-spell-forging.md`): pick your system here, then design spells there.

## Contents

1. Origin — how this was built
2. The generic design space
   - 2a. The two-axis typology (acquisition × expression)
   - 2b. NEW CONCEPTS introduced
   - 2c. The 12 archetype builds
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — A multi-system setting (the Concordat)

## 1. Origin — how this was built

- **Source primitive(s):** the entire power layer (`05`) — its on/off dial, its taxonomy (Standard/Reactive/Ritual), its casting-risk model (safe/chance/overcharge), its fuel (the core metacurrency), its gating (ingredient/grimoire/teacher), its mishap families, its rank ladder. Plus **P5** (resource die — for slot/Vancian and blood-magic fuel), **P8** (feature grammar — for path/talent magic and relic tags), **P6** (activity menu — for verb-noun free-form casting), **P4** (typed D66 — for pact and possession consequences), **P10** (protected dial — for faith and channeling), and **P2** (capped metacurrency — the spine every archetype shares).
- **Reinvention operator:** **Abstraction-Climb** (Operator 5 from `18 §4`). The power layer (`05`) documents *one* instantiated magic system (FL's: 17 disciplines, talent-rank-gated, WP-fueled, per-discipline mishaps). This module climbs one rung up the abstraction ladder to ask: *what are the archetypal ways a game can make magic work, and how does each map onto the engine's existing primitives?* The climb reveals that most RPG magic systems are **recombinations of the same few primitives** with different acquisition/expression axes — and that the engine already supports most of them with minimal extension.
- **Target psychology:** **variety of fantasy feel** — a Vancian wizard, a pact warlock, a faith cleric, and a verb-noun mage all *feel* different to play because their acquisition (how you got power) and expression (how you spend it) differ, even when the underlying dice are identical. This module gives a designer a controlled vocabulary for *that* difference, so the magic system can be tuned for tone before any spell is written.
- **Problem solved:** `05` ships a single, monolithic instance (FL's path/talent model). A designer building a new game is left to invent "how magic works" from scratch — or to clone FL wholesale. This module provides a third path: a catalog of the **archetypes** the RPG tradition has proven (D&D Vancian, Ars Magica verb-noun, BRP spell-as-skill, Warhammer pact, Burning Wheel skill-and-fork, etc.), each abstracted onto the engine, each with its NEW CONCEPTS flagged so the designer knows what they're adding.

## 2. The generic design space

### 2a. The two-axis typology (acquisition × expression)

Every magic system in RPG design is a point on two axes. Naming the axes is the module's core contribution — once you can locate a system on both, you can build it from the primitives.

**Axis 1 — ACQUISITION (how the character got the power, and how they get *more*):**

- **Studied** — learned from books/teachers; advancement is research (FL's disciplines, D&D's wizard spellbooks, Ars Magica's arts).
- **Innate** — born with it; advancement is maturation/practice (psionics, sorcerer bloodlines, mutant powers).
- **Granted** — given by an external source that can withdraw it (deities, patrons, spirits; faith/pact magic).
- **Found** — acquired by encountering objects/places (relics, found spellbooks, consumed tomes, inscribed runes).

**Axis 2 — EXPRESSION (how the character spends the power in play):**

- **Slot / consumable** — powers are prepared charges that deplete on use and refresh on rest (Vancian magic, spell slots, power-point pools that empty).
- **Skill / rolled** — each power is a skill you roll; no slots, just dice (BRP, Call of Cthulhu, Burning Wheel's spell-as-skill).
- **Path / talent** — powers unlocked by climbing a discipline tree; the tree *is* the spellbook (FL's model, D&D 4e's power lists).
- **Free-form / composed** — improvise from component techniques + forms at cast time (Ars Magica's verb+noun, Mage's spheres, Magicka's elements).
- **Channeled / surrendered** — you let something else cast *through* you (possession, mediumship, divine channeling); control is the cost.

A system is one cell on each axis. FL's magic is **Studied × Path/Talent**. D&D's wizard is **Studied × Slot**. A psion is **Innate × Slot** (power points). A warlock is **Granted × Path** (pact boons). Ars Magica is **Studied × Free-form**. A faith cleric is **Granted × Path** (with a devotion gate). The 12 archetypes in §2c are the proven cells of this grid — the combinations RPG design keeps returning to.

**The grid in one view** (archetype number in parens; blank = rare/unproven):

| | **Slot/Consumable** | **Skill/Rolled** | **Path/Talent** | **Free-form** | **Channeled** |
| --- | --- | --- | --- | --- | --- |
| **Studied** | Vancian/Book (1) | Spell-as-Skill (2) | Path/Talent (3) | Verb-Noun (8) | — |
| **Innate** | Psionic (4) | — | (Path via bloodline) | — | — |
| **Granted** | — | — | Divine/Faith (7), Pact (6) | — | Channeling (12) |
| **Found** | — | Folk/Hedge (5, community-found) | Item/Relic (9) | Rune/Glyph (11) | — |

Plus two cross-cutting archetypes that layer a **cost model** over any cell: **Blood/Sacrifice (10)** (the cost IS the fuel — overlays any archetype) and **Folk/Hedge (5)** (a *calibration* of any archetype to low power and community binding). These twelve cover the overwhelming majority of published RPG magic systems.

### 2b. NEW CONCEPTS introduced

This module is mostly **recombination** — the engine's power layer (`05`) plus the primitives already cover most archetypes. The genuinely new mechanics are:

- **NEW CONCEPT — The acquisition × expression typology:** `05` documents one instantiated system (FL's Studied × Path/Talent). This two-axis grid is the abstraction-climb that names *the space of possible systems* the engine can instantiate. No core file maps this space. *Extends the engine with a design-space map for the power layer's structural choices, parallel to how `12` maps the core dials.*
- **NEW CONCEPT — Spell slots as resource dice (Archetype 1, Vancian):** The engine's resource die (`16` P5, `08 §10`) models *depleting consumables* (arrows, food). Here it is domain-transferred to **prepared spell slots**: each memorized spell is a resource die that steps down when cast, refreshed by rest/study. No core system models spell capacity as a step-die. *Extends P5 from physical supplies to cognitive capacity.*
- **NEW CONCEPT — Pact debt track (Archetype 6, Pact/Summoning):** The engine has Influence (`workshop/01`) and Debt (`workshop/06`) as separate tracks. A pact fuses them: the patron's favor is a spendable pool (like Influence) that *grows as a debt* (like `06`'s inverted metacurrency) — each favor called raises the debt, and the patron can **call the debt** to compel service. No core system links a spendable resource to an inverted debt on the same track. *Extends the engine by welding `workshop/01`'s spendable standing to `workshop/06`'s inverted metacurrency, with the patron as the debt-holder.*
- **NEW CONCEPT — Free-form composition menu (Archetype 8, Verb-Noun):** The engine's **Success Menu** (`00 §4`) fires once per downtime roll. Verb-noun casting needs a *combat-speed* composition: pick a verb + a noun + spend Power Level, resolve immediately. This is the Success Menu domain-transferred from downtime to tactical time, with the menu being the verb/noun lists and the PL cost being the "price." *Extends the Success Menu from slow authorship to fast tactical composition.*
- **NEW CONCEPT — Advancing relic (Archetype 9, Item/Relic):** FL's artifact dice (`00 §9`) are *fixed* magic items. An advancing relic grows new tags over time as its wielder invests in it — it is a **settlement-as-character** (`16` P13) scaled to an item: the relic has a "lifecycle" (founding→functions→upkeep→events→scale) like an org (`07`). No core gear system models an item that levels up. *Extends P13/P7 from settlements/orgs to personal artifacts.*

*Everything else is pure recombination: spell-as-skill uses the core skill roll; path/talent IS FL's model; psionics uses the metacurrency; faith uses P10 (protected dial); blood magic uses the Burn override (`05 §5`); runes use the inscribed-symbols subsystem (`05 §6` Gate D); channeling uses possession + P4 consequences. Only the five mechanisms above are genuine engine extensions, and each is flagged at its archetype.*

### 2c. The 12 archetype builds

Each archetype: a one-line definition, its grid cell, what it borrows from the engine, what (if anything) is new, the casting procedure in brief, and the genre feel it produces. Where an archetype needs a NEW CONCEPT, it is marked. Treat each as a **drop-in specification** — set the `05` dials as indicated, add the flagged new mechanic, swap the nouns.

---

### 1. Vancian / Book Magic — Studied × Slot/Consumable

**Definition:** Spells are **prepared** (memorized from a text) into a limited set of **slots**; casting consumes the slot; rest/study refills them. The classic D&D wizard.

**Grid cell:** Studied × Slot.

**Engine borrow:** P5 (resource die) as the slot model — *new application*, see below. Grimoires (`05 §6` Gate B) as the texts. The casting-risk dial (`05 §4`) — overcharge on the roll, mishap on 💀.

**NEW CONCEPT — Spell slots as resource dice:** Each day, a caster prepares a number of spells equal to their slot capacity (a function of rank/level). Each prepared spell is tracked as a **resource die** (D6–D12 by spell rank). When cast, roll the spell's resource die: on a result in the spell's **contraction range**, the slot **steps down** (D12→D10→D8→D6); at D6 + contraction, the spell is **expended** and must be re-memorized. On a roll outside the contraction range, the spell remains (the slot held). *This makes spell capacity a depleting stock that thins over an adventure, exactly as arrows thin (`01 §7`) — the Vancian "I'm running out of spells" dread, engine-native.*

**NEW CONCEPT — Per-spell contraction range (the slot-size vs spell-power interaction):** The engine's base resource-die contraction range is 1–2 (`16` P5), but it is **not law** — perishable or volatile resources contract faster (FL's raw meat = 1–4). A spell's **contraction range scales with its power**: a rank-1 spell contracts on 1–2 (standard); a rank-3 spell on 1–3; a rank-5 spell on 1–4; a rank-6 mythic spell on 1–5 (it tears the slot apart to hold that much power). *This creates a load-bearing tactical interaction:* a larger slot die (D10, D12) is needed to retain a powerful spell across multiple casts — a rank-5 spell (contraction 1–4) placed in a D6 slot is *almost certain* to be spent on the first cast (only a 5–6 holds), forcing the caster to either invest in a bigger slot or accept the spell as a one-shot. Putting a minor spell in a large slot is conversely safe (a rank-1 spell in a D12 slot with contraction 1–2 depletes only ~33%/cast and survives ~3 casts on average). The caster's daily preparation is thus a **slot-allocation puzzle**: which spells go in which-size slots, given that powerful spells demand large slots to be reusable.

**Casting procedure:** (1) The spell must be **prepared** (memorized that day from a grimoire — a Quarter Day of study at rest, per `05 §6`) and **placed in a slot** of sufficient die size (the caster chooses which slot each spell occupies at preparation; a slot's die size is set by the caster's level/rank — more advanced casters have larger slots). (2) Cast per the `05 §4` casting-risk dial (overcharge: roll WP dice, ⚔ = +PL, 💀 = mishap). (3) Roll the spell's **slot resource die**: if the result falls in the spell's **contraction range** (1–2 for rank 1; 1–3 for rank 3; 1–4 for rank 5; 1–5 for rank 6), the slot **steps down** one die size toward expended. (4) At rest, re-memorize: restore each prepared spell's resource die to its rank-default.

**Genre feel:** the scholarly wizard who must choose what to prepare each day, runs dry by dungeon level 3, and treasures the grimoire. High-fantasy, dungeon-crawl, OSR.

---

### 2. Spell-as-Skill — Studied × Skill/Rolled

**Definition:** Each spell is a **skill** (like MELEE or STEALTH); casting is a skill roll against difficulty; no slots, no memorization, no separate power resource — the skill *is* the magic. BRP, Call of Cthulhu, RuneQuest, Burning Wheel's "spell as skill with a fork."

**Grid cell:** Studied × Skill.

**Engine borrow:** the core skill roll (`00 §3`) — attribute + skill level, sixes = success. The success ladder (`00 §4`) reads the result (0 fail / 1 partial / 2 full / 3+ critical). Pushing (`00 §6`) for re-rolls at a cost. **No separate casting roll, no WP cost** — the spell is just a skill the character has.

**What's new:** nothing mechanical — this is the *simplest* archetype, subtracting from FL rather than adding. The only design work is deciding **what attribute** each spell family uses (a fireball might be a PRESENCE + Pyromancy roll; a charm is EMPATHY + Enchantment) and **what the cost of failure is** (since there's no casting mishap table, failure is read on the Trouble/ladder: a botched fireball scatters, a botched charm backfires — the GM uses `00 §10`'s failure-pressure layer).

**Casting procedure:** (1) The caster has the spell as a skill at rank 0–5. (2) Roll attribute + skill vs difficulty. (3) Read on the success ladder: 0 = failure (Trouble fires), 1 = partial (works but with a complication), 2 = full, 3+ = critical (extra effect or bonus). (4) Push if desired (attribute damage or Trouble). Power Level = the spell's rank (or the margin of success, if the designer wants excellence to scale effect).

**Genre feel:** the grounded, low-fantasy mage whose magic is a craft like any other — unreliable, skill-dependent, no flashier than swordplay. Low-magic, historical, gritty, Call-of-Cthulhu-style "magic is dangerous and rare."

---

### 3. Path / Talent Magic — Studied × Path/Talent

**Definition:** Spells are **unlocked by climbing a discipline talent tree**; the talent rank gates which spells you can cast; the tree *is* the spellbook. **This is FL's own model** (`05 §8`).

**Grid cell:** Studied × Path/Talent.

**Engine borrow:** the full FL power layer — discipline talents (rank 1–6), the casting-risk dial, WP fuel, per-discipline mishap families, the rank ladder, grimoires/ingredients. This archetype is `05` instantiated as-is.

**What's new:** nothing — this *is* the documented instance. Listed here for completeness and to locate it on the grid (so a designer can see it as *one choice among twelve*, not the default).

**Casting procedure:** the `05 §4` procedure verbatim — spend WP, choose safe/chance/overcharge, roll the casting dice, ⚔ = +PL, 💀 = mishap on the discipline's table.

**Genre feel:** the specialist caster whose identity is their discipline (the Pyromancer, the Necromancer). High-fantasy, class-based, "wizard school" genres. Pair with `09-spell-forging.md` for player-authored spell invention within the tree.

---

### 4. Psionic / Innate — Innate × Slot/Consumable

**Definition:** Mental powers **born into** the character (mutation, bloodline, awakening); fueled by an internal **power-point pool** that depletes and refills with rest; no books, no teachers, no external source. D&D's psion, many sci-fi psychics.

**Grid cell:** Innate × Slot.

**Engine borrow:** P2 (capped metacurrency) — the power-point pool is the core metacurrency (WP/Faith), recolored as "psionic focus" or "mental strain." The casting-risk dial (`05 §4`) — but **default to safe-cast only** (psionics is reliable; the variance is in the pool, not the roll). The talent ladder (`05 §8`) — but advancement is **practice/maturation**, not study (no grimoires, no teachers).

**What's new:** the **mental-strain cost model** — a calibration of the push cost (`00 §6`). Where FL's push costs body (attribute damage) and West's costs currency (Faith), psionics' push costs **a mental attribute specifically** (Wits/Empathy) and carries a **strain track**: each push beyond the pool marks strain; at strain ≥ rank, the psion is **Burned Out** (cannot use powers until a full rest). This is a push-cost variant, not a new primitive — but it produces the distinctly "psionic" feel (overextension = headache, nosebleed, collapse).

**Casting procedure:** (1) Spend power points (metacurrency) on the effect — each power has a cost. (2) Safe-cast by default: the effect fires at the purchased PL. (3) To **overextend**, push: spend no points but take mental-attribute damage equal to the cost; mark strain. (4) At strain ≥ rank, Burned Out. Rest clears strain and refills the pool.

**Genre feel:** the psychic whose power is intimate and bodily — the nosebleed, the migraine, the burnout. Sci-fi, modern paranormal, superhero, x-men-style.

---

### 5. Folk / Hedge Magic — Studied-or-Found × Low-Calibration (overlay)

**Definition:** A **calibration**, not a separate cell — folk magic is *any* archetype dialed to **low power, slow casting, community binding, and everyday utility**. The village cunning-folk, the hedge-witch, the kitchen-witch. Earthsea, Warhammer's hedge-wizards, Witcher folk signs.

**Grid cell:** overlays any (usually Studied × Skill or Path).

**Engine borrow:** the full power layer at **Low density** (`05 §10`) — single tier (Standard spells only), safe-cast only, a single generic mishap table, rank ladder capped at 1–3. Plus the **activity menu** (`16` P6) — folk magic is cast in *downtime* (brewing, knotting, chanting over a hearth), not in combat rounds.

**What's new:** the **community-binding mechanic** — a folk caster's power is tied to a **constituency** (their village, kin, land). The caster has a **Standing** score with that community (reusing `workshop/01`'s Influence): high Standing makes their folk magic reliable (a +1 or safe-cast bonus when working *for* the community); low/lost Standing makes it falter. Leaving the community weakens the magic; serving it strengthens it. This welds `workshop/01` to the power layer — no core system ties spell potency to community standing.

**Casting procedure:** (1) Folk spells are **rituals in miniature** — they take a Turn or Quarter Day, not an action. (2) Roll the relevant skill (Survival, LORE, a folk-craft skill) vs difficulty. (3) Apply **community Standing** as a modifier (±1 to ±3). (4) Effects are small, practical, and symbolic (a charm that wards a threshold, a brew that heals a child's fever, a knot that binds a promise) — never battlefield magic.

**Genre feel:** the wise-woman, the hedge-priest, the keeper of old ways — magic as *folk practice*, not spectacle. Low-fantasy, historical, folk-horror, pastoral, "the magic is in the soil and the hearth."

---

### 6. Pact / Summoning Magic — Granted × Path/Slot

**Definition:** Power is **borrowed from a bound or summoned entity** (demon, fey, eldritch patron, ancestor spirit); the entity grants boons in exchange for service, payment, or sacrifice; the **bargain is the cost**. D&D's warlock, Warhammer's chaos pacts, many dark-fantasy summoners.

**Grid cell:** Granted × Path (boons) or Slot (summons).

**Engine borrow:** P2 (the patron's favor as a metacurrency pool), `workshop/06` (debt — the inverted metacurrency), `workshop/01` (spendable standing). The summoning itself uses the org model (`07 §5`) — a summoned entity is a temporary "band member" with its own stat block. Mishap families (`05 §7`) for when a summoning goes wrong.

**NEW CONCEPT — Pact debt track:** The caster has a **Pact** with a patron. The patron's **Favor** is a spendable pool (like Influence, `workshop/01`) — spend Favor to power pact magic (each spell costs Favor points). But each Favor spent also **raises the Pact Debt** (an inverted track, `workshop/06`): the more you call on the patron, the more you owe. The patron can **call the debt** at any time (GM's pressure valve) to compel a service — and refusing a called debt risks **breach** (lose access to the patron's boons, or suffer a consequence from `05 §7`'s pact-mishap family). Summoning a *specific entity* (vs. drawing on generic favor) is a ritual that binds the entity into service for a scene — but bound entities can **turn** if the binding weakens (roll on a summoning-mishap D66).

**Casting procedure:** (1) Spend Favor (the patron's pool) on the boon — each pact power has a Favor cost. (2) Raise Pact Debt by the same amount (the bargain deepens). (3) Effects are the patron's gifts (themed to the patron — a demon's fire, a fey's glamour, an ancestor's guidance). (4) At intervals (GM's call, or when Debt crosses a threshold), the patron **calls the debt**: the caster must perform a service or suffer breach. (5) **Summoning** is a separate ritual (one Turn or longer): bind an entity into service; it acts as an allied NPC with its own agenda that may conflict with the caster's.

**Genre feel:** the warlock whose power is a deal with something dangerous — every casting deepens the owed, every summoning risks betrayal. Dark fantasy, eldritch, gothic, "power at a price" (pairs with `workshop/07` corruption).

---

### 7. Divine / Faith Magic — Granted × Path (with devotion gate)

**Definition:** Power **granted by a deity or sacred principle**; gated by **devotion** (the caster must act in accord with the divine will); falling from favor loses the power; restored by atonement. D&D's cleric/paladin, many religious-magic systems.

**Grid cell:** Granted × Path.

**Engine borrow:** P10 (protected dial — the faith resource, `01 §5`). The path/talent model (`05 §8`). The casting-risk dial (`05 §4`) — but **safe-cast by default** (divine magic is reliable when granted). The **devotion gate** is the new structural element.

**NEW CONCEPT (calibration, not primitive) — Devotion as access gate:** Faith is P10 (already in the engine). The new move is making **devotion the access gate** for the power layer: the caster has a **Devotion** track (a measure of alignment with their deity's principles — a 1–5 or a tracked fiction of "have I lived the faith?"). Casting requires Devotion ≥ the spell's rank; casting itself does not cost Devotion, but **violating the faith** (acting against the deity's principles) **lowers Devotion** — and at Devotion below a spell's rank, that spell fails or is withheld. Atonement (a quest, a confession, a sacrifice) restores Devotion. This is the moral-fiber-as-mechanic pattern: power flows from *being* the faithful thing, not from knowing the spell.

**Casting procedure:** (1) Check Devotion ≥ spell rank (the access gate). (2) Spend WP/Faith per `05 §4` (safe-cast default). (3) Effect fires (themed to the deity — healing, protection, smiting, truth). (4) **Fall from favor:** if the caster violates the faith (GM judgement, player-narrated), Devotion drops; spells above the new Devotion fail until atonement. (5) **Atonement:** a quest or act of redress restores Devotion.

**Genre feel:** the cleric, the paladin, the chosen — power that flows from conviction and is lost by its betrayal. High-fantasy with active gods, religious fantasy, crusader genres. Distinct from pact (Archetype 6) in that the *principle* grants power, not a bargained entity — devotion, not debt.

---

### 8. Verb-Noun / Free-Form Magic — Studied × Free-form

**Definition:** The caster **improvises** spells by combining **techniques** (verbs — create, destroy, transform, perceive, control) with **forms** (nouns — fire, mind, body, space, time) at cast time; no fixed spell list, just component arts. Ars Magica, Mage: the Ascension, Magicka.

**Grid cell:** Studied × Free-form.

**Engine borrow:** P8 (feature grammar — verbs and nouns are composable tags), P3 (the success ladder reads the improvised roll), the casting-risk dial (`05 §4`). The **Success Menu** (`00 §4`) for the composition — *new application*, see below.

**NEW CONCEPT — Free-form composition menu:** Verb-noun casting is the **Success Menu at combat speed**. Before rolling, the caster declares a **verb** (their rating in that technique) and a **noun** (their rating in that form); the spell's power and scope come from combining them. The casting roll's ⚔ become "menu points" spent on the composition's qualities — range, duration, area, intensity — *at cast time*, not in downtime. This is the Success Menu (`00 §4`) domain-transferred from slow authorship to fast tactical composition: the menu is the verb/noun ratings, the spend is the ⚔, the output is the improvised spell. Each verb and noun is learned as a separate talent (rank 1–5); combining a rank-3 Create with a rank-2 Fire lets you improvise a fire-creation effect scaled to the lower rating.

**Casting procedure:** (1) Declare **verb + noun** (e.g., "Create Fire," "Transform Body," "Perceive Mind"). (2) Roll the **lower of the two ratings** + attribute, vs difficulty set by the ambition of the effect (the GM uses `09-spell-forging.md`'s scope benchmarks to set this). (3) Spend the roll's ⚔ on the composition's qualities (range, duration, area, targets) — this is the Success Menu spend, resolved immediately. (4) 💀 = mishap (a free-form mishap table — the spell warps, the verb inverts, the noun runs wild). (5) No spell list — every casting is invented, bounded only by the caster's verb/noun ratings.

**Genre feel:** the *mage* who never casts the same spell twice, who thinks in techniques and forms — creative, expressive, high-variance. Ars-Magica-style high fantasy, Mage-style modern occult, "magic as art."

---

### 9. Item / Relic Magic — Found × Path (advancing items)

**Definition:** Magic lives in **objects**, not in the caster; the wielder's skill is in *using* relics, not casting spells; relics may be **found, earned, or grown**. D&D's artificer and magic items, FL's artifact dice (`00 §9`), many MMO gear-magic systems.

**Grid cell:** Found × Path (the relic's "path" is its function tree).

**Engine borrow:** FL's artifact dice (`00 §9`) as the baseline. P8 (feature grammar — relic tags). The crafting gates (`08 §5`). The **org lifecycle** (`07 §3`, P7) — *new application*, see below.

**NEW CONCEPT — Advancing relic (item-as-character):** An advancing relic is a **settlement-as-character** (`16` P13) scaled to a personal item. The relic has a **lifecycle**: it is **found** (founding — a predicate gate: the wielder must be "worthy" or bonded), it has **functions** (named powers, unlocked as tags over time), it demands **upkeep** (a resource obligation — feeding it, attuning to it, keeping its secret), it faces **events** (the relic reveals a new property, or draws enemies), and it can **scale** (awaken to a higher tier, becoming legendary). The wielder invests downtime in the relic (like investing in a stronghold, `07 §4`) to unlock new tags — the relic *levels up with the character*, not as a fixed magic item.

**Casting procedure:** (1) The relic is **wielded**, not cast — using its power is an action (SLOW for major effects, FAST for minor), gated by the wielder's skill with that relic type. (2) The relic's current **tags** (its unlocked functions) determine what it can do. (3) Rolls use the wielder's skill + the relic's bonus (artifact die, `00 §9`). (4) **Advancement:** in downtime, the wielder invests (a ritual of attunement, a quest to unlock a sealed function, feeding the relic a rare material) to add a new tag — following the `09-spell-forging.md` Success Menu and 10-check to keep advancement balanced.

**Genre feel:** the artificer, the relic-bearer, the keeper of an heirloom that grows with them — magic as *heritage and craft*, not as personal power. High-fantasy with legendary weapons, artificer genres, "the sword is the hero."

---

### 10. Blood / Sacrifice Magic — Overlay (cost IS the fuel)

**Definition:** A **cost-model overlay** — power paid for in **harm, sacrifice, or life**; the cost is not a side effect (like Burn) but the *primary* fuel. Warhammer's dark magic, many blood-magic systems, Malazan.

**Grid cell:** overlays any (usually Path or Slot).

**Engine borrow:** the **Burn** override (`05 §5`) — FL's self-harm-to-fuel mechanic. Taken to its extreme: blood magic *primary* fuel is harm, not WP. The casting-risk dial (`05 §4`) — but **chance-cast only** (blood magic is inherently risky). P4 (the blood-mishap family). **Corruption** (`workshop/07`) as the doom spiral for repeated use.

**What's new (calibration, not primitive):** the **harm-as-fuel economy**. Where FL's Burn is a *fallback* (cast without WP by taking damage), blood magic makes harm the *default*: each spell's cost is stated in **attribute damage** (or sacrifice — see below), not in WP. The caster may still spend WP to *reduce* the harm (each WP absorbs 1 point of the cost), but WP is the *alternative*, not the primary. This inverts FL's economy (WP primary, Burn fallback) to (harm primary, WP mitigation). Additionally: **sacrifice** scales the effect — a willing sacrifice (the caster's own blood, an animal, a captured foe) adds +1 to +3 PL based on the value/sentience of the sacrifice, gating the highest tiers behind what the caster is willing to kill.

**Casting procedure:** (1) State the spell's **blood cost** (attribute damage, by rank). (2) Optionally spend WP to absorb part of the cost (1 WP per point absorbed). (3) Take the remaining damage (caster chooses the attribute, or rolls randomly per Burn, `05 §5`). (4) For greater effect, declare a **sacrifice**: +1 PL for a significant animal, +2 for a sentient foe, +3 for a willing loved one (the morality is the cost). (5) Each casting risks **Corruption** (`workshop/07`) — the doom spiral for those who pay in blood too often.

**Genre feel:** the blood-mage, the sacrificer, the one who pays in flesh — grim, costly, transgressive. Dark fantasy, horror, "the power is real but the price is yourself."

---

### 11. Rune / Glyph Magic — Found × Free-form (encoded)

**Definition:** Magic **encoded in inscribed symbols**; runes are *prepared* (carved, painted, tattooed) and **triggered** later (by touch, threshold, condition); the rune IS the spell, suspended. FL's Symbolism discipline, many dwarf/rune-fantasy systems.

**Grid cell:** Found × Free-form (the rune is "found" in the sense of being pre-prepared; "free-form" in that runes combine like verb-noun).

**Engine borrow:** the **Inscribed Symbols** subsystem (`05 §6` Gate D) — FL's "trap/contingency" pattern, made the *primary* casting mode rather than a sub-discipline. P8 (feature grammar — runes are composable tags). The crafting gates (`08 §5`) — inscribing requires tools, materials, time.

**What's new (calibration):** runes make the inscribed-symbol subsystem the **whole system** rather than a side feature. A runecaster's primary activity is **inscribing** (a downtime craft — carving a rune takes a Turn or Quarter Day, per `08 §5`'s crafting gates), and their combat activity is **triggering** (a FAST action to activate a prepared rune). Runes **combine** like verb-noun (Archetype 8): a rune of Fire + a rune of Ward makes a fire-ward; the runecaster's art is knowing the combinations. A rune, once inscribed, **holds its power indefinitely** until triggered — making runecasters the "prepared battlefield" caster (they set the ground before the fight). The limit is **inscription capacity**: a surface, an item, or the runecaster's own body can hold only so many runes (a capacity track, like spell slots but for *inscribed* rather than *memorized* spells).

**Casting procedure:** (1) **Inscribe** in downtime: choose a rune (or combination), spend the materials and time (crafting gates, `08 §5`), roll the inscription skill. (2) The rune **waits** on its surface until triggered. (3) **Trigger** (FAST action, or autonomously on a set condition — crossing a threshold, a spoken word): the rune's effect fires at its inscribed PL. (4) Most runes are **single-use** (the inscription burns out when triggered); some (tattooed, masterwork) are **reusable** but weaker. (5) Inscription failure = a flawed rune (rolls on a rune-mishap D66 — the rune triggers wrongly, backfires, or becomes a hazard).

**Genre feel:** the runecaster, the dwarven glyph-wright, the trap-layer — magic as *craft and preparation*, the battlefield shaped before the blade is drawn. Norse fantasy, dwarf-centric, dungeon-defense, "the magic is in the writing."

---

### 12. Channeling / Possession — Granted × Channeled (surrendered control)

**Definition:** The caster is a **vessel**; a spirit, deity, or ancestor **rides** them during casting; power flows through, but **control is surrendered** to the rider. Mediums, oracles, trance-casters, voodoo possession, Warhammer's loa.

**Grid cell:** Granted × Channeled.

**Engine borrow:** P10 (protected dial — the channel as the "conviction" resource), P4 (typed D66 — what the rider does while in control, and the possession consequences), the casting-risk dial (`05 §4`) — but **the rider rolls, not the caster**.

**NEW CONCEPT (calibration) — Surrendered agency:** The defining mechanic of channeling is that **the player loses control of their character during the channel**. When the caster opens themselves, the rider (a spirit, deity, ancestor) takes the wheel: the *GM* rolls the casting dice and decides the effect's expression, within the negotiated bounds of the pact. The caster's player chooses *when* to open and *which* rider to invite, but not *what the rider does* once present. This is the agency-collapse-as-feature pattern (`19` FE4, deliberately inverted): the tension is that power flows *through you but not from you*, and the rider may act against your interests (a capricious spirit, a demanding ancestor). A strong pact (high relationship with the rider, built over time) gives the caster more influence over the rider's choices; a weak pact leaves the rider free. **Possession consequences** (P4 D66): each channel risks the rider *staying* (extended possession), **damaging** the vessel (attribute damage from the strain of channeling), or **leaving a mark** (a permanent tag — a tell, a compulsion, a Corruption stain per `workshop/07`).

**Casting procedure:** (1) The caster **opens** (a SLOW action — inviting the rider). (2) The **GM rolls** the casting dice (using the rider's power rating, not the caster's skill) and describes the effect — within the bounds of the pact (the caster negotiated these in advance: "I invite the Wolf; the Wolf may fight my foes but may not harm my allies"). (3) The rider's effect fires (often stronger than the caster could manage alone — the rider is more powerful than the vessel). (4) **Possession roll** (P4): risk of extended stay, vessel damage, or a lasting mark. (5) The rider **departs** (usually) — but a strong failure means they *stay*, and the caster must exorcise or bargain for release.

**Genre feel:** the medium, the houngan, the oracle in trance — power that comes *through* you from something you cannot fully control. Voodoo, spirit-medium, oracle, "the gods ride their horses."

---

## 3. The pressure loop

- **Pressure:** every archetype constrains a different resource — slots (1), skill variance (2), rank/talent investment (3), the pool and strain (4), community standing (5), pact debt (6), devotion (7), verb-noun ratings and mishap (8), relic upkeep and attunement (9), blood/sacrifice (10), inscription capacity (11), the rider's will (12).
- **Decision:** *prepare what? push the roll or hold the resource? call the patron/deity/rider now or save them? pay in blood or in WP? inscribe defensively or offensively?* Each archetype forces a different decision shape.
- **Consequence:** slots deplete, pools drain, debts deepen, devotion wavers, blood is spent, riders leave marks. The state change is always *a resource moves*, but which resource is the archetype's signature.
- **Loop shape:** each archetype produces a distinct rhythm — Vancian is *prepare→adventure→deplete→rest*; pact is *bargain→spend→owe→serve*; faith is *devote→cast→falter→atone*; channeling is *open→surrender→risk→recover*. The loop shape is the archetype's fingerprint.

## 4. Dials

Each archetype has its own dials (noted in §2c). The cross-cutting dials that apply to *choosing* among archetypes:

| Dial | Options | What it sets |
| --- | --- | --- |
| **Acquisition axis** | Studied / Innate / Granted / Found | Where power comes from — sets advancement model and gating |
| **Expression axis** | Slot / Skill / Path / Free-form / Channeled | How power is spent — sets the resource model and combat cadence |
| **Density** (from `05 §10`) | None / Low / Medium / High | How much of the power-layer apparatus to instantiate |
| **Cost model** | WP (currency) / Harm (body) / Debt (owed) / Devotion (moral) / Control (surrendered) | What the player pays — sets the feel |
| **Mishap flavor** | Per-discipline / Per-archetype / Generic Trouble | How failure pressures |
| **Advancement** | Study (books) / Practice (time) / Service (patron/deity) / Investment (relic) / Sacrifice | How the caster grows |
| **Multi-system or single** | One archetype / several coexisting | Whether all casters use the same system or different ones (see §8) |

**Calibration guidance:** pick the archetype whose **feel** matches the genre first (Vancian for dungeon-crawl, faith for religious fantasy, pact for dark fantasy, verb-noun for "magic as art," folk for low/pastoral), *then* set density and cost model to match. Do not pick by mechanical elegance — pick by fantasy tone, then verify the mechanics support it.

## 5. Integration points

- **Hooks into:** the entire power layer (`05`) — every archetype is an instantiation of `05` with its dials set. Hooks into `09-spell-forging.md` for designing individual spells *within* a chosen archetype. Hooks into `workshop/07` (corruption) for blood, pact, and channeling consequences. Hooks into `workshop/01` (influence) and `workshop/06` (debt) for pact and folk-magic community-standing. Hooks into the crafting layer (`08 §5`) for relics and rune-inscription. Hooks into the base/org layer (`07`) for summoning and advancing relics.
- **Requires:** a power layer turned **on** (`05 §10`), except for the zero-instance West. The acquisition/expression choice is made *before* designing individual spells.
- **Replaces / extends:** `05`'s monolithic instance — this module exposes the *space* of systems FL is one point in. A game using FL's path/talent magic verbatim does not need this module; a game building its own magic uses this to pick the archetype, then `09` to design the spells.
- **Cross-refs:** `05` (power layer — the host); `09-spell-forging.md` (individual spell design); `16` P2/P4/P5/P6/P8/P10/P13 (composed primitives); `17` (feel calibration); `12` (the divergence map as a model for *this* typology's grid); `workshop/01`, `06`, `07` (pact/folk/blood integration).

## 6. Failure modes & edge cases

- **"The archetype feels like FL with the serial numbers filed off."** If a Vancian or pact or faith system plays identically to FL's path/talent magic, the archetype's distinctive mechanic (slots, debt, devotion) is not load-bearing. **Fix:** the NEW CONCEPT for each archetype (slot resource dies, pact debt, devotion gate, surrendered agency, etc.) must *mechanically* differ from a plain WP spend — if it doesn't, you haven't built the archetype, you've reskinned path/talent. (`19` FE1 — false choice: if the archetype is cosmetic, the "choice" of system is illusory.)
- **"Vancian slots make casters too weak / too strong."** If slots deplete too fast, casters are useless after one fight; if too slow, they never feel the scarcity. **Fix:** calibrate the resource-die deplete range (1–2 standard; 1 for generous, 1–3 for harsh) and the slot capacity (rank + 1 per tier). Test against the attrition curve (`13 §3`) — a caster should run dry near the *end* of a session's intended encounters, not the first.
- **"Pact debt spirals out of control."** If the patron calls debts too often, the caster is enslaved; if too rarely, the debt is toothless. **Fix:** the patron calls debt at *thresholds* (not GM whim) — e.g., when Debt ≥ 2× the caster's rank. Service should be *a scene or side-quest*, not a campaign takeover. (Cross-ref `19` FE5 — "too unfair"; `workshop/06` §6 on called-debt calibration.)
- **"Faith magic punishes roleplay."** If the GM is sole judge of "violation," devotion becomes a stick to punish players for playing their character. **Fix:** devotion violations should be *player-declared* or *clearly codified* (the faith's tenets are written down, like a paladin's oath) — the GM enforces the codex, not their mood. Atonement must be *achievable*, not punitive.
- **"Verb-noun casting is too open / too slow."** If any combination is allowed, players find abusive combos (Create Time); if too restricted, it's just path/talent with extra steps. **Fix:** verb and noun ratings gate the combos (you can't Create Time if your Time noun is rank 0), and the GM uses `09`'s scope benchmarks to set difficulty by ambition. Resolution must be fast — the Success Menu spend at cast time should be quick (a few ⚔ on 2–3 qualities), not a negotiation. Pre-print "rotes" (common combinations with pre-statted effects) for speed.
- **"Blood magic makes the caster a liability."** If every spell costs attribute damage, the blood-mage is always wounded and becomes dead weight. **Fix:** the WP-absorption valve (spend WP to reduce harm) lets blood-mages pace themselves; sacrifice (not self-harm) should be the high-end fuel, so the caster isn't *required* to bleed for every spell. The Corruption spiral (`workshop/07`) is the long-term cost, not per-cast damage.
- **"Channeling removes player agency too often."** If the rider takes over every combat, the player watches. **Fix:** channeling should be *episodic* (the caster opens in crisis moments, not every fight), the rider's actions should be *bounded by the pact* (negotiated in advance, so the player retains indirect control), and the rider must *depart* reliably unless the possession roll fails. The tension is the *risk* of lost control, not its常态. (`19` FE4 — agency collapse: do not make this the default state.)

## 7. Validation notes

- **Math (`13 §3`):** each archetype's resource curve should be tested — Vancian slot depletion over a session; pact debt accumulation vs service frequency; faith devotion thresholds; blood-magic harm throughput vs recovery. Use the expected-success math and the attrition curves. The key invariant: *no archetype should let a caster cast indefinitely without engaging the engine's risk mechanics* (pushing, harm, debt, devotion) — that is the universal balance line.
- **Exploits (`13 §5`):** verb-noun combo abuse (Create Time) is the main exploit — gated by ratings + scope benchmarks. Pact-debt exploit (call-favor-then-ignore-debt) is gated by the breach consequence. Relic-tag stacking is gated by `09`'s reforging RISKY escalation. Blood-magic sacrifice-abuse (farm sacrifices) is gated by Corruption (`workshop/07`) and the GM's judgement on what counts as a "significant" sacrifice.
- **Synergy (`13 §7`):** the cross-archetype integrations are the synergy risks — a pact mage who also uses blood magic could pay debts in harm; a faith caster with a relic could have two power sources. Verify these are *intended* (multi-system settings, §8) or *gated* (a caster picks one archetype).
- **Felt experience (`19`):** the **archetype's distinctive mechanic must be load-bearing** — slots must *feel* scarce, debt must *feel* owed, devotion must *feel* moral, channeling must *feel* surrendered. If the mechanic is invisible in play, the archetype is cosmetic (FE1 false choice). The NEW CONCEPTS (slot resource dies, pact debt, devotion gate, free-form menu, advancing relic, surrendered agency) are what produce the feel — they are not optional flavor, they are the archetype's identity.

## 8. Worked genre example — A multi-system setting (the Concordat)

**The setting:** the Concordat — a high-fantasy city where multiple magical traditions coexist, each a different archetype. The power layer is at **High density** (`05 §10`). This example shows the typology's real power: *different casters in the same game use different archetypes*, each tuned to its fantasy feel.

**The archetypes in play:**

- **The Collegium (Path/Talent, Archetype 3):** the approved, scholarly mages. Discipline talents, WP-fueled, per-discipline mishaps — FL's model verbatim. The establishment. Their magic is *studied and reliable*.
- **The Cunning-Folk (Folk/Hedge, Archetype 5):** village witches practicing low magic, bound to their communities. Community-standing-gated, ritualistic, small effects. Their magic is *humble and rooted*.
- **The Pact-Bound (Pact/Summoning, Archetype 6):** warlocks who have bargained with the thing in the city's catacombs. Favor pool + rising debt + called service. Their magic is *powerful but owed*.
- **The Faithful (Divine/Faith, Archetype 7):** clerics of the Concordat's civic gods. Devotion-gated, safe-cast, themed to their deity. Their magic is *granted and moral*.
- **The Artificers' Guild (Item/Relic, Archetype 9):** crafters who wield and grow advancing relics. Relic-tagged, attunement-invested. Their magic is *crafted and inherited*.

**In use (a scene):** A Concordat crisis — a demonic incursion. The **Collegium mage** casts a studied ward (path/talent, WP-fueled, reliable). The **Cunning-woman** brews a folk-charm to protect the neighborhood's children (community standing grants her a +1 — she has served this street for years). The **Pact-Bound warlock** calls on his patron for a blast of abyssal fire — Favor spent, Debt rises; the GM notes the Debt is near threshold, and next session the patron will call a service. The **Faithful cleric** prays for a banishment — Devotion check passes (she has lived her faith this week), the spell fires. The **Artificer** levels her grandfather's relic-sword — its newly-unlocked WARD-tag flares. Five casters, five archetypes, five distinct feels — all in the same engine, all balanced by the same primitives.

**Why the typology earns its keep here:** without this module, a designer building the Concordat would either (a) make everyone a path/talent caster with different flavor (flat — the warlock feels like the cleric feels like the mage), or (b) invent five bespoke subsystems (inconsistent, unbalanced, a maintenance nightmare). The typology gives *controlled, validated difference* — each archetype's distinctive mechanic (slots, debt, devotion, standing, relic-advancement) is what makes the warlock *feel* like a warlock and the cleric *feel* like a cleric, while the underlying dice and balance are shared.

**Re-skin for your genre:**

- **Single-archetype game:** pick one archetype and set the others to "none" — a pure Vancian dungeon-crawl, a pure folk-magic pastoral, a pure pact dark-fantasy. The typology helps you *choose* deliberately rather than defaulting to FL's path/talent.
- **Sci-fi:** Psionic (4) for mental powers; Item/Relic (9) reskinned as "tech/gadgets" that advance with the user; Folk (5) reskinned as "street-tech" bound to a community. Drop the Studied archetypes unless there's a "lab" institution.
- **Modern occult:** Verb-Noun (8) for Mage-style sphere magic; Pact (6) for urban-warlock pacts; Channeling (12) for mediumship. Faith (7) reskinned as "conviction ideology."
- **Dark fantasy / horror:** Blood (10) + Pact (6) + Channeling (12) + Corruption (`workshop/07`) — every caster pays in something dear. The doom spiral is the genre.
