---
name: forbidden-lands-design
description: Design, audit, explain, or expand Forbidden Lands 2E rules and supplements. Use for mechanics, professions, talents, spells, lifepaths, journeys, strongholds, gear, campaign procedures, player experience, sandbox play, playtesting, and cross-chapter integration. Trigger whenever new content must feel native to the Year Zero engine and remain balanced, playable, psychologically satisfying, and useful in emergent play.
---

<!-- markdownlint-disable MD013 -->

# Forbidden Lands Design

Design for decisions under pressure. Preserve the engine's survival logic while
giving players visible information, consequential choices, and several viable
ways to change their situation.

## Establish Authority

1. Read the relevant files in `01-corebook/`.
2. Search the whole manuscript for the rule term and adjacent mechanics.
3. Treat published manuscript text as current authority; use bundled references
   as design analysis, not as a substitute for source verification.
4. Inspect `../../CHANGELOG.md` and recent history when intent may have changed.
5. Load `forbidden-lands-lore` for setting facts and
   `forbidden-lands-writing-voice` for manuscript prose.
6. Load `forbidden-lands-synergy-analysis` for combinations, dominant
   strategies, or new player-facing options.

Do not rely on remembered first-edition rules, other Year Zero games, or an
earlier proposal when the manuscript differs.

## Route the Task

Read only the references needed for the task:

| Need | Reference |
| --- | --- |
| System loops, chapter ownership, integration surfaces | `references/system-design-map.md` |
| Dice pools, pushing, thresholds, probabilities, rule taxonomy | `references/engine-math-and-rule-taxonomy.md` |
| Full system design doctrine and proposal audit | `references/design-manual.md` |
| Willpower, spells, talents, recovery, coupled systems | `references/willpower-synergy-spells-and-recovery-analysis.md` |
| Injuries, journeys, gear, logistics, expansion space | `references/injuries-journeys-gear-and-expansion-space.md` |
| Realism, agency, change scenarios, interaction audit | `references/realism-audit-synergy-and-change-scenarios.md` |
| Agency, fairness, mastery, spotlight, frustration, onboarding | `references/player-psychology-and-table-experience.md` |
| Factions, rumors, sites, travel, freeform GM procedure | `references/sandbox-and-freeform-campaign-design.md` |
| Book architecture, option coverage, gates, usability, release scope | `references/supplement-architecture-and-development.md` |
| Test hypotheses, scenario matrices, metrics, regression | `references/playtest-and-balance-protocol.md` |

For engine-independent Year Zero construction methods, use `yze-design`;
return here to apply Forbidden Lands constraints.

## Define the Design Contract

Before drafting, write a compact contract:

- **Player promise:** What new fantasy, decision, or capability becomes real?
- **Campaign job:** Which recurring loop or sandbox pressure gains depth?
- **User:** Which player archetype, GM task, or campaign phase benefits?
- **Trigger:** When does the rule enter play?
- **Cost:** What time, action, resource, risk, access, or opportunity is paid?
- **Payoff:** What state changes, and how visibly?
- **Counterplay:** What can another actor, the world, or bad circumstances do?
- **Exit:** How does the effect end, recover, expire, or escalate?
- **Ownership:** Which chapter teaches it and which chapters reference it?

Reject a feature whose promise is only “more realism,” “more options,” or “more
detail.” State the table behavior it changes.

## Model the Complete Loop

Trace:

`signal → player interpretation → choice → resolution → consequence → world response → next choice`

Audit every link:

1. The signal must reveal enough to support an informed gamble.
2. At least two responses must be genuinely viable.
3. Resolution must use familiar grammar or justify a new procedure.
4. Consequences must change future play, not merely decorate the scene.
5. The world response must be legible enough for players to learn from it.
6. The next choice must remain playable after failure.

If the rule has no signal, it feels arbitrary. If it has no next choice, it is
an outcome table rather than a game loop.

## Protect the Forbidden Lands Pressure Stack

Check how the addition affects:

- dice pools, pushing, Banes, and gear damage
- Willpower generation and spending
- fast and slow actions
- attribute damage, Broken states, conditions, and critical injuries
- recovery time, care, shelter, and magical healing
- resource dice, encumbrance, tools, mounts, and silver
- Quarter Days, weather, navigation, camp, and expedition range
- profession, kin, Pride, Dark Secret, relationships, and lifepath identity
- talents, spell paths, artifacts, hirelings, and strongholds
- information, reputation, faction leverage, and access

A new option may relieve pressure. It must not permanently erase a core pressure
channel without becoming a major campaign reward with visible consequences.

## Design Choices, Not Taxes

A meaningful choice has:

- two or more plausible options
- different advantages, costs, and future consequences
- enough information to reason about the tradeoff
- no universally correct answer across ordinary situations
- a result the player can connect to the decision

Avoid:

- mandatory maintenance with one correct response
- a weak option included only to make another option look attractive
- “choice” between participation and character ruin
- costs paid by one player for benefits enjoyed mainly by another
- repeated micro-decisions whose answer rarely changes

Compress routine competence. Spend rules weight where tension, identity, or
campaign direction can change.

## Balance at Four Scales

1. **Use:** Is the effect worth its immediate cost?
2. **Scene:** Does it dominate actions, invalidate counterplay, or monopolize
   spotlight?
3. **Session:** Does repetition make the optimal line automatic?
4. **Campaign:** Does it erase attrition, bypass advancement, collapse a niche,
   or force every informed player to take it?

Balance is not equal damage. Compare access, reliability, breadth, frequency,
risk, setup, counterplay, and narrative authority. A spectacular narrow ability
can be healthy; a modest universal passive often is not.

For rare or prestigious identities, preserve the broad entry profession and add
a limited, legible gate into the specialist option. Do not replace common
lifepath entry points merely to make rare content visible.

## Design for Player Psychology

Protect:

- **Agency:** choices alter outcomes and remain meaningful after setbacks.
- **Competence:** investment creates recognizable mastery without automatic
  victory.
- **Fairness:** danger is telegraphed, procedures are consistent, and severe
  consequences follow understandable causes.
- **Discovery:** rumors and clues invite inference instead of delivering answers.
- **Expression:** several identities and approaches remain effective.
- **Belonging:** support abilities create shared victories without reducing a
  player to another character's modifier.
- **Spotlight:** no option routinely consumes disproportionate table time or
  resolves other characters' signature problems.

Harshness is compatible with fairness. Hidden odds, retroactive exceptions, and
unavoidable agency loss are not made fair by a grim tone.

## Design for Sandbox and Freeform Play

Prefer content that generates situations:

- actors with aims, resources, constraints, and visible methods
- locations with needs, opportunities, hazards, and several approaches
- rumors that point toward decisions rather than plots
- clocks or pressure tracks that advance because actors act
- consequences that alter routes, prices, loyalties, safety, or information
- reusable procedures that help the GM answer unplanned player choices

Do not require a prescribed scene order, a protected villain, a mandatory clue,
or one “correct” moral conclusion. Prepare causes and pressures; let play supply
the plot.

## Integrate the Manuscript

For every approved rule:

1. Name the teaching location.
2. List every affected chapter, table, example, index entry, and summary.
3. Reuse canonical terms exactly.
4. Add an example where timing or interpretation could be disputed.
5. State defaults, limits, exceptions, and GM authority explicitly.
6. Separate core procedure from optional variants.
7. Check whether character creation, advancement, NPCs, and lifepaths expose
   the option in proportion to its intended rarity.

## Test Before Recommending

Use three passes:

### Analytical pass

Calculate probabilities, action value, resource flow, maximum stacking, and
repeat frequency. Compare against at least two existing baselines.

### Adversarial pass

Assume an optimizer combines the option with the strongest legal kin, profession,
talent, spell, gear, party support, downtime, and stronghold effects. Test both
strict and permissive readings.

### Experience pass

Run or simulate ordinary, expert, unlucky, and resource-starved situations. Ask
what each participant knows, chooses, feels, and does next. Record confusion,
dead time, spotlight, perceived fairness, and whether failure produces play.

Do not use “the GM can fix it” as a balance mechanism. GM judgment is for
fictional uncertainty, not routine repair of incomplete rules.

## Verdict Format

Report:

1. **Current rule and evidence**
2. **Design contract**
3. **Loop and integration map**
4. **Mathematical and synergy findings**
5. **Player-experience findings**
6. **Sandbox consequences**
7. **Edge cases and failure modes**
8. **Recommendation**
9. **Manuscript-ready text**, when requested
10. **Validation plan**

Distinguish facts from inference and recommendation. Quote only enough source
text to identify the rule.

## Final Quality Gate

- [ ] The feature makes a specific promise and fulfills it in play.
- [ ] The trigger, cost, resolution, consequence, duration, and exit are clear.
- [ ] Failure changes the situation without routinely ending participation.
- [ ] At least two viable approaches remain.
- [ ] The strongest combination has been tested.
- [ ] No profession, kin, talent, or party role loses its reason to exist.
- [ ] Bookkeeping and lookup cost match the importance of the decision.
- [ ] The GM receives a procedure, not merely advice.
- [ ] Sandbox actors and locations can react without a scripted plot.
- [ ] Cross-chapter references and terminology are complete.
- [ ] The prose is concise enough to use at the table.
