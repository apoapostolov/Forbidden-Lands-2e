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

> Each module is a single `.md` file, numbered `01-` through `07-`. Each follows the structure in `00-module-template.md`: a genre-agnostic **generic design space** (§2, the bulk) including a **NEW CONCEPTS** subsection (§2b) flagging every mechanism that extends the core engine, and a **Mechanical reference** subsection (§2c) with the actual runnable tables, formulas, and procedures — followed by one **worked genre example** (§8).

- `01-influence-and-political-power.md` — Political capital as a spendable, *decaying* pool with scandals as the bane-equivalent. *Worked example: Renaissance Florence.*
- `02-faction-relationship-web.md` — A multi-faction relationship graph with a propagation rule: helping one faction shifts standing with its allies and enemies. *Worked example: post-apoc warlords.*
- `03-social-combat-as-real-combat.md` — High-stakes social scenes as full tactical conflicts: the action economy, social-distance range bands, leverage as weapons, Composure as social HP. *Worked example: Regency high society.*
- `04-pursuit-and-chase.md` — Structured chases with a shared track-position ladder, the activity menu at combat cadence, typed-D66 Hazards, and resource-die countdowns. *Worked example: 1920s spycraft.*
- `05-investigation-and-clue-economy.md` — Clues as a capped metacurrency earned via an inquiry activity menu and spent on a revelation ladder; risky inferences use the push. *Worked example: noir / cosmic horror.*
- `06-debt-and-obligation.md` — An *inverted* metacurrency: debts grow when you take favors and must be paid down; called debts are the GM's pressure valve. Unifies financial/social/moral/supernatural debt. *Worked example: corporate space opera.*
- `07-corruption-and-taint.md` — A corruption spiral: forbidden power refuels you but grows a doom die up a 5-tier ladder; full milestone D66 tables and an atonement procedure. *Worked example: witch-hunting dark fantasy.*

## Module template

Use `00-module-template.md` as the skeleton for any new module. It encodes the structure above so every workshop entry is consistent and drop-in ready.
