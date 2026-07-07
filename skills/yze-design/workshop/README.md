<!-- markdownlint-disable MD013 -->

# Workshop — Aagnostic Subsystem Library

> **STATUS: ACTIVE.** This is the skill's generative **workbench** — a growing library of ready-to-use, engine-agnostic subsystems built by applying the Reinvention Method (`references/18-reinvention-method.md`) to the primitives in `references/16-mechanical-primitives.md`. Each module is a *new* mechanic (not a documentation of an existing one) — invented by transplanting proven patterns into fresh domains, calibrated for a target psychology, and stress-validated against the pipeline in `references/13-balance-and-synergy.md` and the felt-experience checks in `references/19-player-psychology-and-felt-experience.md`.

## What this folder is

The `references/` folder documents *what the Year Zero Engine is.* This folder extends it with *what the engine could be* — new subsystems that did not exist in either source game, built from the engine's own proven primitives and ready to drop into any YZE-family game.

Every workshop module is:

- **Engine-native.** Uses ⚔/💀, the push economy, the metacurrency, the success ladder, the activity menu, the typed D66, or another primitive from `16`. It fits the engine by construction — you will not need to invent a new dice type or parallel economy.
- **Genre-agnostic in its core.** Each module's bulk is the generic design space — the mechanism, its dials, its pressure loop, its failure modes. A genre example shows it *in use*, but the mechanism does not depend on the genre.
- **Pre-validated.** Each module carries the Reinvention recipe (which operator, which primitives, what calibration), so a designer can see *how it was built* and adjust it rather than treat it as a black box.
- **Drop-in.** Each module specifies its integration points (which engine systems it touches, what it requires, what it replaces) so a designer can install it without breaking the rest of the game.

## How to use a module

1. **Scan the library** below for a subsystem that fits your design need.
2. **Read the module's Generic Design Space** first — that is the transferable core.
3. **Read the Worked Genre Example** to see the mechanism calibrated and skinned.
4. **Re-skin for your genre** by swapping nouns (the `15-glossary-and-taxonomy.md` translation table shows how) and recalibrating the dials (using `17-dual-use-matrix.md` to target the psychology you want).
5. **Run the validation pipeline** (`13 §8`) and the felt-experience protocol (`19 §7`) on your instantiation before shipping.

## How to contribute a new module

The workshop is meant to grow. A new module should follow the **module template** (see `00-module-template.md`):

1. **Generic Design Space** (the bulk) — the mechanism abstracted away from any genre, with: the source primitives, the reinvention operator, the pressure loop it creates, the dials, the failure modes, and the integration points.
2. **Worked Genre Example** (a slice) — one concrete instantiation in a chosen genre, showing the dials set, the nouns skinned, and a brief play example.
3. **Validation notes** — how it passed the `13`/`19` checks, and known edge cases.

Apply the **Reinvention Ladder** from `SKILL.md`:
1. Identify the primitive (`16`).
2. Target the psychology (`17`).
3. Apply an operator (`18 §4`).
4. Run the composition checklist (`18 §5`) and the validation pipeline (`13 §8` + `19 §7`).

## Module index

> Each module is a single `.md` file, numbered `NN-`. The numbering is by cluster (politics/relationships/combat-extensions/abstract-systems), not priority.

### Politics & power

- `10-influence-and-political-power.md` — A political-capital system: convert fictional standing into a spendable influence pool (calibrated on the dual-use matrix). *Worked example: Renaissance Florence.*

### Relationships & factions

- `20-faction-relationship-web.md` — A multi-faction relationship tracker that models alliances, feuds, debts, and shifting standing as a graph the PCs steer. *Worked example: post-apoc warlords.*

### Combat extensions

- `30-social-combat-as-real-combat.md` — Treats social scenes as full tactical conflicts with the action economy, positioning, "attacks," and a Broken-equivalent — not a single opposed roll. *Worked example: Regency high society.*
- `40-pursuit-and-chase.md` — A structured chase subsystem with track-position, the activity menu, and escalating stakes. *Worked example: 1920s spycraft.*

### Abstract reusable systems

- `50-investigation-and-clue-economy.md` — A clue-as-currency system: clues are a tracked resource that refuels the deductive push, gating revelations behind player-driven inquiry. *Worked example: noir / cosmic horror.*
- `60-debt-and-obligation.md` — A debt tracker that turns favors, loans, and oaths into active pressure (an inverted metacurrency). *Worked example: corporate space opera.*
- `70-corruption-and-taint.md` — A corruption spiral: using forbidden power refuels you but climbs a doom ladder (resource die + typed consequence families, inverted polarity). *Worked example: witch-hunting dark fantasy.*

## Module template

Use `00-module-template.md` as the skeleton for any new module. It encodes the structure above so every workshop entry is consistent and drop-in ready.
