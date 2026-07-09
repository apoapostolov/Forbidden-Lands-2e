<!-- markdownlint-disable MD013 -->

# Workshop — Agnostic Modular Extension Framework

> **STATUS: ACTIVE.** This is the skill's generative **workbench** — a growing library of ready-to-use, engine-agnostic rule sets built by applying the Reinvention Method (`references/18-reinvention-method.md`) to the patterns in `references/16-mechanical-primitives.md`. Each module is a *new* rule (not documentation of an existing one) — invented by transplanting proven patterns into fresh domains, calibrated for a target psychology, and stress-checked against the review path in `references/13-balance-and-synergy.md` and the felt-experience checks in `references/19-player-psychology-and-felt-experience.md`.

## What this folder is

The `references/` folder documents *what the Year Zero Engine is.* This folder extends it with *what the engine could be* — new rule sets that did not exist in either source game, built from the engine's own proven patterns and ready to drop into any YZE-family game.

Every workshop module is:

- **Engine-native.** Uses ⚔/💀, the push economy, Willpower/Faith, the success ladder, the activity menu, the typed D66, or another pattern from `16`. It fits the engine by construction — you will not need to invent a new dice type or parallel economy.
- **Genre-agnostic in its core.** Each module's bulk is the generic design space — the rule pattern, its choices, its pressure loop, its failure modes. A genre example shows it *in use*, but the rule pattern does not depend on the genre.
- **Pre-checked.** Each module carries the Reinvention recipe (which operator, which patterns, what calibration), so a designer can see *how it was built* and adjust it rather than treat it as a black box.
- **Drop-in.** Each module specifies its integration points (which engine systems it touches, what it requires, what it replaces) so a designer can install it without breaking the rest of the game.

## Quality bar

A workshop module is complete only when it includes:

- A runnable procedure that a GM can use at the table.
- A choice table with at least two calibrated settings.
- A handshake: prerequisites, inputs required from the host game, outputs the module creates, and systems touched.
- Integration notes, incompatibilities, and replace/stack rules.
- Failure modes and check notes using `13`, `19`, and `24`.
- At least one worked genre example.
- Publication-ready rule text or a rule-text template.

If a module provides a generator instead of full tables, the generator must be explicit enough to produce the table without designer invention.

## How to use a module

1. **Scan the library** below for a rule set that fits your design need.
2. **Read the module's Generic Design Space** first — that is the transferable core.
3. **Read the Worked Genre Example** to see the rule pattern calibrated and skinned.
4. **Re-skin for your genre** by swapping nouns (the `15-glossary-and-families.md` translation table shows how) and recalibrating the choices (using `17-dual-use-matrix.md` to target the psychology you want).
5. **Run the review path** (`13 §8`) and the felt-experience protocol (`19 §7`) on your build before shipping.

## How to contribute a new module

The workshop is meant to grow. A new module should follow the **module template** (see `00-module-template.md`):

1. **Generic Design Space** (the bulk) — the rule pattern abstracted away from any genre, with: the source patterns, the reinvention operator, the pressure loop it creates, the choices, the failure modes, and the integration points.
2. **Worked Genre Example** (a slice) — one concrete build in a chosen genre, showing the settings chosen, the nouns skinned, and a brief play example.
3. **Check notes** — how it passed the `13`/`19` checks, and known edge cases.

Apply the **Reinvention Ladder** from `SKILL.md`:
1. Identify the pattern (`16`).
2. Target the psychology (`17`).
3. Apply an operator (`18 §4`).
4. Run the composition checklist (`18 §5`) and the review path (`13 §8` + `19 §7`).

## Module index

> Each module is a single `.md` file, numbered `01-` through `19-`. Each follows the structure in `00-module-template.md`: a genre-agnostic **generic design space** (§2, the bulk) including a **NEW CONCEPTS** subsection (§2b) flagging every rule pattern that extends the core engine, a **Rules reference** subsection (§2c) with runnable procedures, and a **Handshake** section that states prerequisites, inputs, outputs, touched systems, incompatibilities, and replace/stack rules.

- `01-influence-and-political-power.md` — Political capital as a spendable, *decaying* pool with scandals as the bane-equivalent. *Worked example: Renaissance Florence.*
- `02-faction-relationship-web.md` — A multi-faction relationship graph with a propagation rule: helping one faction shifts standing with its allies and enemies. *Worked example: post-apoc warlords.*
- `03-social-combat-as-real-combat.md` — High-stakes social scenes as full tactical conflicts: the action budget, social-distance range bands, leverage as weapons, Composure as social HP. *Worked example: Regency high society.*
- `04-pursuit-and-chase.md` — Structured chases with a shared track-position ladder, the activity menu at combat cadence, typed-D66 Hazards, and resource-die countdowns. *Worked example: 1920s spycraft.*
- `05-investigation-and-clue-economy.md` — Clues as a capped pool earned via an inquiry activity menu and spent on a revelation ladder; risky inferences use the push. *Worked example: noir / cosmic horror.*
- `06-debt-and-obligation.md` — An *inverted* pool: debts grow when you take favors and must be paid down; called debts are the GM's pressure valve. Unifies financial/social/moral/supernatural debt. *Worked example: corporate space opera.*
- `07-corruption-and-taint.md` — A corruption spiral: forbidden power refuels you but grows a doom die up a 5-tier ladder; full milestone D66 tables and an atonement procedure. *Worked example: witch-hunting dark fantasy.*
- `08-spell-systems.md` — A catalog of 12 magic-system archetypes (Vancian/book, spell-as-skill, path/talent, psionic, folk/hedge, pact/summoning, divine/faith, verb-noun/free-form, item/relic, blood/sacrifice, rune/glyph, channeling/possession), each built engine-natively from the power layer + the patterns. The system-level typology that sits *above* individual spell design.
- `09-spell-forging.md` — Player-authored power design as a downtime project: a multi-day forging roll whose surplus ⚔ buy spell qualities from a player-authored Success Menu. Ships the rank/scope benchmarks, quality-cost table, the 10-check balance test, and reforging. *Worked example: high fantasy.*
- `10-stress-fear-and-trauma.md` — Stress, fear, panic, trauma scars, and recovery.
- `11-heat-wanted-and-exposure.md` — Law, surveillance, corporate attention, monster attention, and other escalating exposure.
- `12-vehicles-and-crews.md` — Ships, starships, caravans, mechs, trains, and other crewed vehicles.
- `13-rituals-projects-and-research.md` — Long-form projects: rituals, inventions, research, repairs, expeditions.
- `14-reputation-renown-and-legend.md` — Public identity, fame, infamy, rumor propagation, and legend growth.
- `15-territory-and-domain-play.md` — Turf, settlements, regional control, faction pressure, and seasonal turns.
- `16-companions-bonds-and-community.md` — Companions, dependents, patrons, party bonds, crew morale, and community strain.
- `17-monsters-threats-and-boss-architecture.md` — Boss/threat design from clocks, phases, tells, lairs, and consequence effects.
- `18-mystery-conspiracy-and-revelation.md` — Conspiracy webs, revelations, clue reliability, and mystery pressure.
- `19-genre-signature-conflicts.md` — Duels, debates, trials, raids, dogfights, ritual contests, and other set-piece conflict scripts.

## Composition guidance

- **Clean combinations:** Influence + Debt; Faction Web + Reputation; Heat + Chase; Vehicles + Crew Bonds; Rituals + Mystery; Monsters + Territory.
- **Requires shared caps:** Corruption + Spell Forging; Heat + Faction Web; Reputation + Influence; Stress + Powers; Vehicles + Boss Architecture.
- **Potential conflicts:** Social Combat plus ordinary social rolls can over-mechanize conversation; Clue Economy plus Mystery Web can double-charge for information; Territory plus Faction Web can duplicate faction-turn bookkeeping.
- **Default cap rule:** if two modules create the same kind of spendable pool, either merge them into one pool or make one a clock; do not let both independently refuel the same action.

## Module template

Use `00-module-template.md` as the skeleton for any new module. It encodes the structure above so every workshop entry is consistent and drop-in ready.
