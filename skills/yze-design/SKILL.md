---
name: yze-design
description: |
  Use when designing, abstracting, extrapolating, or INVENTING mechanics for the Year Zero Engine (YZE) by Free League Publishing — the D6 dice-pool RPG engine shared by Forbidden Lands 2E and Tales of the Old West 2E. Reverse-engineers both corebooks into one engine-agnostic design system in three layers: UNDERSTAND — core resolution, character, conflict, harm, power, travel, orgs, gear, GM procedures, philosophy, dials, the FL-vs-West divergence map; INVENT — 15 reusable mechanical primitives, a dual-use matrix showing how each produces opposite psychologies at different calibrations, and a 5-operator reinvention method for transplanting primitives into new systems; VALIDATE — an executable balance/synergy pipeline (math, exploits, breakpoints) plus a player-psychology layer (loss aversion, flow, perceived randomness, the abstraction-authenticity dial) and an integrating review protocol. Use it to build a new YZE game for any genre, invent rules from proven primitives, or stress-validate either for math and feel.
---

# YZE Design

An engine-agnostic design system for the **Year Zero Engine** (YZE) by Free League Publishing — the D6 dice-pool RPG engine instantiated by two corebooks:

- **Forbidden Lands 2E** (FL) — the *maximal* YZE: magic, hex journeys, strongholds, factions, mass combat, mercenaries, lifepaths.
- **Tales of the Old West 2E** (West) — the *minimal / no-magic* YZE: the Trouble/Faith variant, pointcrawl travel, town/property/outlaw-band downtime, hard historical authenticity.

Use this skill to understand the engine at depth, build a new YZE game for any genre, or design and stress-validate new rules.

## When To Use

Use it when you need to:

- abstract a YZE mechanic away from its setting skin (e.g. "what is Willpower Points, generically?")
- build a new YZE game for a new genre (sci-fi, modern, post-apoc, horror, historical)
- **invent a genuinely new mechanic** by transplanting a proven primitive into a new domain (sanity as a resource die; heat as an inverted metacurrency; a bridge crew as an activity menu)
- design or audit a new rule/subsystem so it fits the engine's pressure economy
- decide between two calibrated design options (hex vs pointcrawl; barter vs cash; WP vs Faith; magic on/off)
- **choose what a mechanism should *feel like*** (aggression vs caution; attrition vs drama; heroic peaks vs sustained agency)
- stress-test a rule for math, exploits, synergy, and table behavior
- understand *why* a YZE rule exists and what breaks without it

For game-specific design/authoring inside one repo, defer to the sibling skills (see **Reconciliation** below). `yze-design` owns the *generic engine*; they own the *instantiated game*.

## How To Use This Skill — The Abstraction Ladder

For every mechanic, climb four layers. Each reference file is organized to make this climb explicit.

1. **Source instance** — quote the concrete rule from each game, with `file:line` citation.
2. **Generic mechanism** — strip genre nouns; name the abstract procedure.
3. **Design intent** — what pressure/loop it serves, what breaks without it.
4. **Dials & instantiation recipe** — tunable parameters + how to re-skin, with FL and West shown as two calibrated points on each dial.

**When INVENTING a new mechanic (not just analyzing one), use the Reinvention Ladder** (see `16`–`18`):

1. **Identify the primitive** — which of the 15 patterns in `16` does this resemble? If none, you may be reinventing from scratch — re-check the palette.
2. **Find the target psychology** — scan the dual-use matrix in `17`; pick the calibration that produces the feel you want.
3. **Apply an operator** — Domain Transfer, Inversion, Recalibration, Fusion, or Abstraction-Climb (`18 §4`) — to transplant the primitive into your target domain.
4. **Run the composition checklist** (`18 §5`) and the validation pipeline (`13 §8`) before shipping.

**Always apply these output rules:**

- Replace every setting noun (Willpower Points, Faith, demons, hexes, dollars, Kin) with a canonical generic term. Map them in `15-glossary-and-taxonomy.md`.
- Capture FL-vs-West differences as rows in the **Divergence Map** (`12-divergence-map.md`): *decision · option A (FL) · option B (West) · trade-off · when to choose each*.
- Classify every rule as **General** / **Situational** / **Optional**, and tag it.
- Apply the medieval/historical-authenticity lens to combat, gear, economy, travel, and social systems.
- Cite your sources. Every generic claim must trace back to a rule in FL or West.

## Non-Negotiable Rules

1. **No setting nouns in the generic layer.** "Willpower Points" → "metacurrency"; "hex" → "travel unit"; "demon" → "power source." Glossary-map every one.
2. **Divergence is data, not noise.** Where the two games differ, record the row in the Divergence Map.
3. **Provenance-first.** Every reference file names the exact FL + West files (and chapter/section) it mines. Re-runnable, auditable.
4. **Balance methodology is executable.** Expected-success math, attrition curves, exploit taxonomy, synergy protocol, table-behavior lenses — formulas and checklists, not vibes.
5. **Never duplicate a sibling skill.** `yze-design` owns *generic methodology*. The game-specific analysis skills own their *instantiated catalogs*. Reference, do not copy.
6. **Forbid the inherited anti-patterns** (from FL's `system-design-map.md`, generalized): subsystem inflation, silent invalidation of existing rules, false realism, vague enforcement, misleading survivability, setting-laden generic language.

## Reference Library

Load these on demand. Each opens with a TOC, a `## Source provenance` block, and an `## Abstraction target` (the scoped design prompt). They are scaffolded stubs — structured for a two-pass fill (extract → abstract).

### Engine systems

- `references/00-engine-core.md` — **Load when** analyzing/altering the core resolution loop. Dice grammar (base/skill/gear dice), sixes-as-success, ones-as-bane, success ladders, pushing and its two cost models, difficulty/modifiers, opposed/group rolls, the metacurrency abstraction (WP/Faith).
- `references/01-character-model.md` — **Load when** building or reskinning the character model. Four attributes × four skills, per-attribute damage types, pride/faith, relationships/companions, encumbrance, kin/archetype vs lifepath generation.
- `references/02-progression-and-xp.md` — **Load when** designing advancement. XP award models, training costs (teacher vs self-taught), talent rank ladders (5-rank FL vs 2-rank West), milestones, downtime training, Legacy XP.
- `references/03-conflict-and-combat.md` — **Load when** designing combat/conflict. Time units, range/zones, reach bands, slow/fast action economy, reactive actions, melee/ranged/social conflict, the Duel/Face-Off special-conflict pattern, morale/rout, mounted combat.
- `references/04-harm-and-consequences.md` — **Load when** designing damage, injury, or environmental hazard. Attribute damage, Broken, coup-de-grace, the Critical-Injury table engine (D66 location×severity), conditions, environmental harm (fire/fall/drown/poison/disease/darkness), stabilization/death.
- `references/05-power-layer.md` — **Load when** designing magic/powers or deciding the on/off dial. Power taxonomy: Magic (slow), Power Words (fast/reactive), Rituals. Casting models (safe/chance/overcharge), mishap tables, ingredients/grimoires, Burn. Genre-fit guidance.
- `references/06-travel-and-downtime.md` — **Load when** designing the journey/survival loop. Hex (FL) vs pointcrawl (West) travel, Quarter-day/Shift procedures, activity menus, weather, forage/hunt/fish, making camp, recovery shifts.
- `references/07-base-faction-mass-scale.md` — **Load when** designing the downtime org layer. Strongholds, Towns/Property, Outlaw Bands, Mercenary Companies, Factions+Legacies, Mass Combat — abstracted as founding/functions/upkeep/events/scale-escalation.
- `references/08-gear-and-economy.md` — **Load when** designing gear/crafting/economy. Supply/scarcity tables, economy models (barter vs cash+capital vs gold/silver), crafting, weapon/armor feature grammar, quality tiers, artifact/legendary dice, consumables-as-resource-dice.
- `references/09-gm-procedures.md` — **Load when** designing GM tools/procedures. GM principles (7 FL principles generalized), encounter engines (D66 tables, reoccurring encounters), settlement/village generators, NPC statblock grammar, solo-play engine, consequence/fortune tracks.

### Design systems (meta)

- `references/10-design-philosophy.md` — **Load when** reasoning about *why* the engine works. Pressure economy, the 5 core loops (Expedition/Conflict/Recovery/Metacurrency/Base), "Nothing Is for Free," lethality & attrition as feature, tone/authenticity lens, the general/situational/optional layering principle.
- `references/11-design-dials-and-variants.md` — **Load when** choosing between calibrated options. Master dial catalog: magic on/off, lethality, metacurrency model, travel model, economy model, faction layer on/off, action-economy granularity — each with FL & West as two points + trade-offs.
- `references/12-divergence-map.md` — **Load when** you need to see every FL-vs-West decision in one place. The single highest-value original artifact; built incrementally from each system file.
- `references/13-balance-and-synergy.md` — **Load when** validating a new rule. Expected-success math, attrition/breakpoint curves, exploit-surface taxonomy, synergy stress-test protocol, table-behavior lenses. Owns the method; cites the game-specific catalogs.
- `references/19-player-psychology-and-felt-experience.md` — **Load when** a rule is technically sound but *feels* wrong, or to catch that before it ships. The experiential evaluative layer: felt-experience failure modes (false choice, decision fatigue, swinginess-as-unfairness, agency collapse, the "too X" family), the cognitive layer beneath `13 §7`'s lenses (loss aversion, perceived randomness, flow, tension rhythm, the agency ledger), the abstraction-vs-authenticity dial, and an integrating review protocol that orchestrates `10`'s warning signs + `13`'s pipeline + this file's psychology checks into one pass.
- `references/14-recipes-new-game-new-rule.md` — **Load when** starting a new game or rule from scratch. Two cookbooks: (1) Build a new YZE game for any genre. (2) Design + validate a new rule/subsystem (intent→math→exploit→integration→readability).
- `references/15-glossary-and-taxonomy.md` — **Load when** translating between generic and game-specific terms. Canonical generic↔FL↔West dictionary + master taxonomy of all engine systems.

### Generative layer — inventing new mechanics

> The files above let you *understand and configure* the engine. These three let you *extend it into new design space* — the "genius-level designer" layer. Read `16` first when inventing; it is the palette the other two build on.

- `references/16-mechanical-primitives.md` — **Load first when inventing a new mechanic.** The palette: 15 proven-portable patterns (dice-pool-with-push, capped metacurrency, graded success ladder, typed D66 tables, resource dice, activity menus, the org lifecycle, feature grammar, scale ladders, protected dials, dual generation, rule-layering, settlement-as-character, encounter-with-memory, the pressure loop). Each primitive is named, parameterized, and cross-linked to the systems it already powers.
- `references/17-dual-use-matrix.md` — **Load when** choosing *what a mechanism should feel like.* Shows that each primitive produces *opposite psychologies at different calibrations* (harm-refuel → aggression; success-refuel → caution; action-refuel → drama) — proven by FL and West being the same engine with opposite tones. The calibration→psychology lookup table.
- `references/18-reinvention-method.md` — **Load when** generating a genuinely new mechanic from old ones. Five operators (Domain Transfer, Inversion, Recalibration, Fusion, Abstraction-Climb), the composition checklist, anti-patterns, and five worked examples (sanity as a resource die, heat as an inverted push economy, social conflict as typed consequence families, a Doom protected dial, a starship bridge as activity menu). The core move: *take a primitive from system A, deploy it in system B, recalibrate to a target psychology.*

## Reconciliation With Sibling Skills

`yze-design` owns the **generic engine + philosophy + methodology**. Defer to game-specific skills for instantiated work:

- **Game-specific design** → `forbidden-lands-design` (FL), `western-rpg-design` (West).
- **Instantiated balance/synergy catalogs** → `forbidden-lands-synergy-analysis` (FL), `rpg-synergy-analysis` + `rpg-balance-analysis` (West).
- **Prose/voice/lore** → `forbidden-lands-writing-voice`, `western-writing`, `forbidden-lands-lore`.
- **Bestiary/encounter design** → `forbidden-lands-bestiary`.
- **Adventure design** → `adventure-writing`.

When a question is *about the engine itself*, `yze-design` leads and the game-specific skills supply instances. When a question is *about one game's implementation*, that game's skill leads and `yze-design` supplies the generic frame.

## Audit Checklist

Before finalizing any `yze-design` output, verify:

- [ ] **Generic layer has no setting nouns.** Every term is generic or glossary-mapped.
- [ ] **Two calibrated points shown.** FL and West both appear for any dial or trade-off.
- [ ] **Sources cited.** Every concrete rule claim has a `file:line` or chapter reference.
- [ ] **Divergence recorded.** Any FL-vs-West difference is a row in the Divergence Map.
- [ ] **Layer tagged.** Every rule is classified General / Situational / Optional.
- [ ] **Balance is executable.** Math, exploits, synergy, table-behavior are checked with formulas/protocols — not vibes.
- [ ] **No sibling duplication.** Generic methodology only; instantiated catalogs stay in their own skills.
- [ ] **Anti-patterns absent.** No subsystem inflation, silent invalidation, false realism, vague enforcement, or misleading survivability.
- [ ] **Authenticity lens applied** where the rule touches combat, gear, economy, travel, or social systems.
