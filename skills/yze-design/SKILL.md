---
name: yze-design
description: |
  Use when designing, abstracting, extrapolating, or INVENTING rules for the Year Zero Engine (YZE) by Free League Publishing — the D6 dice-pool RPG engine shared by Forbidden Lands 2E and Tales of the Old West 2E. Reverse-engineers both corebooks into one engine-agnostic design studio in four layers: UNDERSTAND — core resolution, character, conflict, harm, power, travel, orgs, gear, GM procedures, philosophy, design choices, the FL-vs-West divergence map; ORCHESTRATE — route work into analysis, host-game adaptation, complete-game build, rule invention, or playtest checks; INVENT — reusable patterns, advanced pattern blends, a dual-use matrix, and a 5-operator reinvention method for transplanting patterns into new systems; VALIDATE/PUBLISH — executable math, abuse checks, attrition, table-feel, naming, and publication-handoff procedures. Use it to build complete YZE games, extend existing YZE-style games, invent modular rules, validate balance/feel, name the game in flavorful language, and write publication-ready rules.
---

# YZE Design

An engine-agnostic design system for the **Year Zero Engine** (YZE) by Free League Publishing — the D6 dice-pool RPG engine instantiated by two corebooks:

- **Forbidden Lands 2E** (FL) — the *maximal* YZE: magic, hex journeys, strongholds, factions, mass combat, mercenaries, Life Events.
- **Tales of the Old West 2E** (West) — the *minimal / no-magic* YZE: the Trouble/Faith variant, pointcrawl travel, town/property/outlaw-band downtime, hard historical authenticity.

Use this skill to understand the engine at depth, extend an existing YZE-style game without breaking its identity, build a complete new YZE game for any genre, or design and stress-validate new rules.

## When To Use

Use it when you need to:

- abstract a YZE rule away from its setting skin (e.g. "what is Willpower Points, generically?")
- build a new YZE game for a new genre (sci-fi, modern, post-apoc, horror, historical)
- adapt or extend an existing YZE game by preserving its cost model, loop weights, optional surface, and native voice
- **invent a genuinely new rule** by transplanting a proven pattern into a new realm (sanity as a supply die; Heat as inverted Willpower; a bridge crew as a list of jobs)
- design or audit a new rule set so it fits the engine's pressure economy
- decide between two calibrated design choices (hex vs pointcrawl; barter vs cash; Willpower vs Faith; magic on/off)
- **choose what a mechanism should *feel like*** (aggression vs caution; attrition vs drama; heroic peaks vs sustained agency)
- stress-test a rule for math, exploits, synergy, and table behavior
- understand *why* a YZE rule exists and what breaks without it

For game-specific design/authoring inside one repo, defer to the sibling skills (see **Reconciliation** below). `yze-design` owns the *generic engine*; they own the *instantiated game*.

## How To Use This Skill — The Abstraction Ladder

For every mechanic, climb four layers. Each reference file is organized to make this climb explicit.

1. **Source instance** — quote the concrete rule from each game, with `file:line` citation.
2. **Flavorful generic rule** — strip setting-only nouns, but keep language that sounds like a game: Race, Life Events, Willpower, Menace, Holdings and Territory.
3. **Design intent** — what pressure/loop it serves, what breaks without it.
4. **Choices & naming recipe** — tunable choices + how to re-skin and rename, with FL and West shown as two calibrated points.

**When INVENTING a new rule (not just analyzing one), use the Reinvention Ladder** (see `16`–`18`):

1. **Identify the pattern** — which of the 15 patterns in `16` does this resemble? If none, you may be reinventing from scratch — re-check the palette.
2. **Find the target psychology** — scan the dual-use matrix in `17`; pick the calibration that produces the feel you want.
3. **Apply an operator** — Realm Transfer, Inversion, Recalibration, Fusion, or Abstraction-Climb (`18 §4`) — to transplant the pattern into your target realm.
4. **Run the composition checklist** (`18 §5`), the final checks (`13 §8`), and the naming check (`26`) before shipping.

**Always apply these output rules:**

- Replace every setting-only noun (demons, hexes, dollars, named factions, setting-specific peoples) with a flavorful generic term, then rename it for the target genre. Map terms in `15-glossary-and-taxonomy.md` and use `26-naming-the-game.md` before writing final rules. Do **not** flatten flavorful names into technical ones: Willpower, Faith, Pride, Menace, Race, Life Events, Holdings and Territory, Riches in the Land, Strange Devices, Powers and Traditions, Blood Price, Circle of Power, and Larger-Than-Life Play are preferred over sterile labels.
- Capture FL-vs-West differences as rows in the **Divergence Map** (`12-divergence-map.md`): *decision · option A (FL) · option B (West) · trade-off · when to choose each*.
- Classify every rule as **General** / **Situational** / **Optional**, and tag it.
- Apply the medieval/historical-authenticity lens to combat, gear, economy, travel, and social systems.
- Cite your sources. Every generic claim must trace back to a rule in FL or West.

## Non-Negotiable Rules

1. **No sterile framework nouns in game-facing rules.** "Metacurrency" → Willpower/Faith/Nerve; "protected dial" → Pride/Faith/Inner Fire; "domain control" → Holdings and Territory; "resource extraction loop" → Riches in the Land. Glossary-map and name every one.
2. **Divergence is data, not noise.** Where the two games differ, record the row in the Divergence Map.
3. **Provenance-first.** Every reference file names the exact FL + West files (and chapter/section) it mines. Re-runnable, auditable.
4. **Balance methodology is executable.** Expected-success math, attrition curves, abuse checks, synergy protocol, table-behavior lenses — formulas and checklists, not vibes.
5. **Never duplicate a sibling skill.** `yze-design` owns *generic methodology*. The game-specific analysis skills own their *instantiated catalogs*. Reference, do not copy.
6. **Forbid the inherited anti-patterns** (from FL's `system-design-map.md`, generalized): rule bloat, silent invalidation of existing rules, false realism, vague enforcement, misleading survivability, setting-laden generic language, and sterile framework naming.
7. **Maneuvers are paragraphs, not tables.** Action lists, spend options, and move menus are written as bolded ALL-CAPS name + rule-voice paragraph. Tables are reserved for D66 roll results and reference lookups only. (See `21-manuscript-format.md`.)
8. **Names are ALL-CAPS.** Action/maneuver names (`**SLASH**`), skill/ability names (`MELEE`, `INSIGHT`), attribute names (`STRENGTH`), and action types (`SLOW` / `FAST`) are ALL-CAPS in running text. Action type is stated inline in the paragraph, never in a table column.

## Reference Library

Load these on demand. Reference files are filled design tools, not stubs. Each opens with a TOC, a `## Source provenance` block, and an `## Abstraction target` where source-backed derivation matters; newer orchestration and worksheet files are procedural harnesses and state their assumptions directly.

### Orchestration

- `references/22-design-orchestrator.md` — **Load first for any substantial task.** Routes the request into five modes: analyze existing rule, adapt existing YZE game, build complete new game, invent rule set, validate/audit rule set. Defines mandatory outputs, stop-and-ask gates, five-loop proof, host-game extension contract, naming pass, and publication handoff.
- `references/23-compatibility-profiles.md` — **Load when choosing a genre target or extending a host game.** Agnostic YZE compatibility profiles for survival fantasy, cinematic horror, mystery/investigation, space opera, post-apoc survival, military/squad, mythic fantasy, political/social drama, heist/crime, mecha/vehicle, and cozy/community. FL/West remain the source-backed anchors; these are design archetypes.
- `references/24-validation-worksheets.md` — **Load when checking math, attrition, supply/upkeep loops, action budget, abuse risks, table burden, or felt experience.** Reusable worksheets, threshold warnings, and quick-math formulas.

### Engine systems

- `references/00-engine-core.md` — **Load when** analyzing/altering the core resolution loop. Dice grammar (base/skill/gear dice), sixes-as-success, ones-as-bane, success ladders, pushing and its two cost models, difficulty/modifiers, opposed/group rolls, Willpower/Faith.
- `references/01-character-model.md` — **Load when** building or reskinning the character model. Four attributes × four skills, per-attribute damage types, pride/faith, relationships/companions, encumbrance, Race/archetype vs Life Events generation, and What Skills Do procedures.
- `references/02-progression-and-xp.md` — **Load when** designing advancement, talents, or paths. XP award models, training costs (teacher vs self-taught), Talents and Paths (race talents, profession talents, path talents, general talents, gifts, tricks, secrets, masteries), milestones, downtime training, Legacy XP.
- `references/03-conflict-and-combat.md` — **Load when** designing combat/conflict or validating combat changes. Time units, range/zones, reach bands, slow/fast action budget, reactive actions, melee/ranged/social conflict, the Duel/Face-Off special-conflict pattern, morale/rout, mounted combat, plus the integrated combat validation harness for attacks, defenses, damage, armor, cover, reload, reach, reactions, special attacks, duels, morale, and fight-ending states.
- `references/04-harm-and-consequences.md` — **Load when** designing damage, injury, or environmental hazard. Attribute damage, Broken, coup-de-grace, the Critical-Injury table engine (D66 location×severity), conditions, environmental harm (fire/fall/drown/poison/disease/darkness), stabilization/death.
- `references/05-power-layer.md` — **Load when** designing magic/powers or deciding whether powers exist. Power families: Magic (slow), Power Words (fast/reactive), Rituals. Casting models (safe/chance/overcharge), mishap tables, ingredients/grimoires, Burn, Powers and Traditions, Blood Price, Circle of Power. Genre-fit guidance.
- `references/06-travel-and-downtime.md` — **Load when** designing the journey/survival loop, pursuit, mounts, or traps. Hex (FL) vs pointcrawl (West) travel, Quarter-day/Shift procedures, activity menus, weather, forage/hunt/fish, making camp, recovery shifts, mount-as-participant, field pursuit/manhunts, and trap procedures.
- `references/07-base-faction-mass-scale.md` — **Load when** designing the downtime org layer. Strongholds, Holdings and Territory, Riches in the Land, Towns/Property, Outlaw Bands, Mercenary Companies, Factions+Legacies, Mass Combat — abstracted as founding/functions/upkeep/events/scale-escalation, with control, claims, roads, watchtowers, prospecting, deposit dice, depletion, hauling, and operating sheets.
- `references/25-season-downtime-and-enterprises.md` — **Load when** designing period-based downtime: weeks, months, seasons, years, businesses, families, factions, settlements, routes, banks, ranches, mines, organizations, and management play. Generalizes the West Investment Cycle (Assess → Invest → Operate → Reckon → Reinvest) into a core YZE enterprise engine with sheets, activity menus, season rolls, family/faction procedures, hard-season contraction, and validation checks.
- `references/08-gear-and-economy.md` — **Load when** designing gear, inventory, transport, crafting, construction, property, investment, trade, gambling, Strange Devices, or economy. Supply/scarcity tables, economy models (barter vs cash+capital vs gold/silver), weapon/armor feature grammar, quality tiers, artifact/legendary dice, consumables-as-resource-dice, carry limits, containers, pack animals, wagons/boats, group stores, stockpiles, storage functions, crafting gates, stronghold functions, property Status, town amenities, Capital, loans, salaries, cargo runs, market rolls, gambling scenes, contraptions/inventions with charges and misfires, upkeep, payback, and economic validation.
- `references/09-gm-procedures.md` — **Load when** designing GM tools/procedures. GM principles (7 FL principles generalized), encounter engines (D66 tables, reoccurring encounters), settlement/village generators, civic/legal/reputation procedures, NPC statblock grammar, solo-play engine, consequence/fortune tracks.

### Design systems (meta)

- `references/10-design-philosophy.md` — **Load when** reasoning about *why* the engine works. Pressure economy, the 5 core loops (Expedition/Conflict/Recovery/Willpower/Base), "Nothing Is for Free," lethality & attrition as feature, tone/authenticity lens, the general/situational/optional layering principle.
- `references/11-design-dials-and-variants.md` — **Load when** choosing between calibrated options. Master choice catalog: magic on/off, lethality, Willpower model, travel model, economy model, faction layer on/off, action-budget granularity, plus Larger-Than-Life Play (vigor, resolve, menace, extras, champions, monsters, mobs, broken shields, show of force) — each with FL & West as two points + trade-offs.
- `references/12-divergence-map.md` — **Load when** you need to see every FL-vs-West decision in one place. The single highest-value original artifact; built incrementally from each system file.
- `references/13-balance-and-synergy.md` — **Load when** validating a new rule. Expected-success math, attrition/breakpoint curves, exploit-surface taxonomy, synergy stress-test protocol, table-behavior lenses. Owns the method; cites the game-specific catalogs.
- `references/19-player-psychology-and-felt-experience.md` — **Load when** a rule is mathematically sound but *feels* wrong, or to catch that before it ships. The experiential evaluative layer: felt-experience failure modes (false choice, decision fatigue, swinginess-as-unfairness, agency collapse, the "too X" family), the cognitive layer beneath `13 §7`'s lenses (loss aversion, perceived randomness, flow, tension rhythm, the agency ledger), the abstraction-vs-authenticity choice, and an integrating review protocol that orchestrates `10`'s warning signs + `13`'s checks + this file's psychology checks into one pass.
- `references/20-publication-voice.md` — **Load whenever you write text a player or GM will read** (rulebook chapters, talent descriptions, adventure text, GM guidance, examples of play). The translation layer between this skill's internal designer/AI vocabulary (pressure loops, deltas, propagation, friction levers) and publication-ready prose for an 18–33 audience of GMs and players. Contains the jargon→prose dictionary, a blacklist of AI/design-theory tells, an OK-list of terms players already know, six register rules, and worked before/after transformations. Defers to the sibling writing skills (`forbidden-lands-writing-voice`, `western-writing`, `adventure-writing`) for fiction voice and adventure structure.
- `references/21-manuscript-format.md` — **Load whenever you format published rules text** — maneuver lists, action descriptions, statblock grammar, any text a player reads. The engine-level formatting convention: ALL-CAPS bold for action/maneuver names, ALL-CAPS for skill/ability/attribute names, SLOW/FAST stated inline (never in a table column), **paragraph format** for maneuver/action lists (not tables), tables reserved for D66 roll results and reference lookups only, symbols (⚔💀🩸), game-state capitalization, and the six rule-voice principles. Complements `20-publication-voice.md` (which handles jargon→prose translation; this file handles *formatting*).
- `references/26-naming-the-game.md` — **Load whenever creating a new YZE game, renaming a generic rule for a genre, or converting analysis into rules text.** Owns the flavorful naming system: analytical name → flavorful generic name → genre-specific name. Provides the forbidden blandness list, preferred generic names (Race, Life Events, Willpower, Menace, Holdings and Territory, Riches in the Land, Strange Devices, Powers and Traditions), genre naming procedure, worked genre renames, and final naming check.
- `references/14-recipes-new-game-new-rule.md` — **Load when** starting a new game or rule from scratch. Two cookbooks: (1) Build a complete YZE game package for any genre. (2) Design + validate a new rule or rule set (intent→math→abuse check→integration→naming→readability).
- `references/15-glossary-and-taxonomy.md` — **Load when** translating between generic and game-specific terms. Canonical generic↔FL↔West dictionary + master taxonomy of all engine systems.

### Generative layer — inventing new rules

> The files above let you *understand and configure* the engine. These three let you *extend it into new design space* — the "genius-level designer" layer. Read `16` first when inventing; it is the palette the other two build on.

- `references/16-mechanical-primitives.md` — **Load first when inventing a new rule.** The palette: 15 proven-portable core patterns plus advanced compositions (clocks/fronts, relationship edges, revelation ladders, stance tracks, heat/wanted pressure, vow/oath engines, crew-role menus, vehicle-as-character, territory control, rumor economies, reputation propagation, ritual/project tracks). Each entry names its shape test, choices, math/tempo notes, and transplants.
- `references/17-dual-use-matrix.md` — **Load when** choosing *what a rule should feel like.* Shows that each pattern produces *opposite psychologies at different calibrations* (harm-refuel → aggression; success-refuel → caution; action-refuel → drama) — proven by FL and West being the same engine with opposite tones. The calibration→psychology lookup table.
- `references/18-reinvention-method.md` — **Load when** generating a genuinely new rule from old ones. Five operators (Realm Transfer, Inversion, Recalibration, Fusion, Abstraction-Climb), the composition checklist, anti-patterns, and five worked examples (sanity as a supply die, Heat as an inverted push economy, social conflict as typed consequence families, Doom as Menace, a starship bridge as jobs). The core move: *take a pattern from system A, deploy it in system B, recalibrate to a target psychology, then name it with `26`.*

### Workshop — drop-in rules library

> The `references/` folder documents the engine. The `workshop/` folder **extends** it: a growing library of ready-to-use, engine-agnostic rules modules built by applying the Reinvention Method (`18`) to the patterns (`16`). Each module is genre-agnostic in its **core** (the bulk of the file) with one **worked genre example** showing it calibrated and skinned. Read `workshop/README.md` for the index and usage method; `workshop/00-module-template.md` for the structure every module follows. Drop a module into any YZE-family game by setting its choices and renaming its nouns (per `15` and `26`).

- `workshop/01-influence-and-political-power.md` — Political capital as a spendable, *decaying* pool (inverted P2 + P4 scandals). *Example: Renaissance Florence.* Use for: court intrigue, corporate politics, any game where standing is currency.
- `workshop/02-faction-relationship-web.md` — A multi-faction relationship graph: alliances/feuds/debts as tracked *edges*, with reputation propagation (P14 + P4 + inverted P10). *Example: post-apoc warlords.* Use for: any campaign where factions matter relationally, not just as isolated quest-givers.
- `workshop/03-social-combat-as-real-combat.md` — High-stakes social scenes as full tactical conflicts: the action budget, social-distance "range bands," leverage as weapons, Composure as social HP, a Broken-equivalent (the combat engine realm-transferred). *Example: Regency high society.* Use for: diplomacy, courtroom, interrogation, high-society genres.
- `workshop/04-pursuit-and-chase.md` — Structured chases with track-position, the activity menu (P6 spine), and escalating stakes. Resolves pursuit as a multi-Round scene, not a single roll. *Example: 1920s spycraft.* Use for: heists, monster-hunts, starship, any genre with signature chases.
- `workshop/05-investigation-and-clue-economy.md` — Clues as a capped pool earned via inquiry jobs and spent on a revelation ladder; risky inferences use the push. *Example: noir / cosmic horror.* Use for: mysteries, procedurals, research-driven campaigns.
- `workshop/06-debt-and-obligation.md` — Debt as inverted Willpower: debts grow when you take favors and must be paid down; called debts are the GM's pressure valve. Unifies financial/social/moral/supernatural debt. *Example: corporate space opera.* Use for: any game where obligations are the engine of plot.
- `workshop/07-corruption-and-taint.md` — A corruption spiral (P5 + P10 inverted + P4 milestones): forbidden power refuels you but grows a doom die; 5 tiers from whispers to transformation; atonement can step it back down. *Example: witch-hunting dark fantasy.* Use for: dark fantasy, cosmic horror, psychic-overload, "power at a cost" genres.
- `workshop/08-spell-systems.md` — A catalog of 12 magic-system archetypes (Vancian/book, spell-as-skill, path/talent, psionic, folk/hedge, pact/summoning, divine/faith, verb-noun/free-form, item/relic, blood/sacrifice, rune/glyph, channeling/possession), each built engine-natively from the power layer (`05`) + the patterns. Ships the 2-axis typology (acquisition × expression), full archetype builds with NEW CONCEPT flags, and a decision procedure for picking one. Use for: any game designing *how* its magic works at the system level, before designing individual spells.
- `workshop/09-spell-forging.md` — Player-authored power design as a downtime project: a multi-day forging roll whose surplus ⚔ buy spell qualities from a player-authored Success Menu (`00 §4` applied to the power layer). Ships the rank/scope benchmarks, quality-cost table, the 10-check balance test, reforging (iterative authorship), and the RISKY tag. *Example: high fantasy.* Use for: any game with a power layer where players should design, not just pick, their spells.
- `workshop/10-stress-fear-and-trauma.md` — Stress, fear, panic, trauma scars, and recovery built from resource dice, typed fallout, and recovery projects. Use for: horror, war, survival, supernatural pressure.
- `workshop/11-heat-wanted-and-exposure.md` — Escalating attention from law, surveillance, corporations, monsters, or gods. Use for: crime, heists, cyberpunk, monster-hunting, rebellion.
- `workshop/12-vehicles-and-crews.md` — Vehicles as crewed orgs: ships, starships, caravans, mechs, trains, and rigs. Use for: space opera, naval, mecha, road campaigns.
- `workshop/13-rituals-projects-and-research.md` — Long-form invention, ritual, research, expeditions, and construction projects. Use for: occult, science, crafting, domain campaigns.
- `workshop/14-reputation-renown-and-legend.md` — Public identity, fame, infamy, rumor propagation, and legend growth. Use for: heroic, political, outlaw, celebrity, mythic games.
- `workshop/15-territory-and-domain-play.md` — Turf, domain maps, seasonal pressure, faction moves, and territorial consequences. Use for: warbands, gangs, politics, kingdom play.
- `workshop/16-companions-bonds-and-community.md` — Dependents, party bonds, patrons, crew morale, community obligations, and shared recovery. Use for: found-family, settlement, military, cozy, and tragedy games.
- `workshop/17-monsters-threats-and-boss-architecture.md` — Threat design from patterns rather than stat inflation: clocks, phases, tells, lairs, and consequence effects. Use for: horror, boss fights, kaiju, nemeses.
- `workshop/18-mystery-conspiracy-and-revelation.md` — Deeper mystery play: webs, revelations, red herrings, conspiracy clocks, and clue reliability. Use for: investigation-heavy campaigns.
- `workshop/19-genre-signature-conflicts.md` — Templates for duels, debates, chases, trials, raids, rituals, dogfights, debates, and other signature set-piece conflicts.

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
- [ ] **Two calibrated points shown.** FL and West both appear for any major choice or trade-off.
- [ ] **Sources cited.** Every concrete rule claim has a `file:line` or chapter reference.
- [ ] **Divergence recorded.** Any FL-vs-West difference is a row in the Divergence Map.
- [ ] **Layer tagged.** Every rule is classified General / Situational / Optional.
- [ ] **Balance is executable.** Math, exploits, synergy, table-behavior are checked with formulas/protocols — not vibes.
- [ ] **No sibling duplication.** Generic methodology only; instantiated catalogs stay in their own skills.
- [ ] **Anti-patterns absent.** No rule bloat, silent invalidation, false realism, vague enforcement, misleading survivability, or sterile framework naming.
- [ ] **Authenticity lens applied** where the rule touches combat, gear, economy, travel, or social systems.
- [ ] **Maneuvers are paragraphs.** Action lists and move menus use bolded ALL-CAPS name + paragraph, not tables. Tables reserved for roll results and reference lookups only.
- [ ] **Names are ALL-CAPS.** Actions (`**SLASH**`), skills (`MELEE`), attributes (`STRENGTH`), action types (`SLOW`/`FAST`) — all ALL-CAPS in running text. Action type stated inline, not in a column.
