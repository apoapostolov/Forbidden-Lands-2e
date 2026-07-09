<!-- markdownlint-disable MD013 -->

# [Module Name] — [One-line description]

> **STATUS: WORKSHOP MODULE.** A workshop module is not an essay, a pitch, or a list of intentions. It is a runnable, modular rule set built from YZE patterns: procedures, rolls, costs, menus, tables, choices, integration contracts, check notes, and a worked reskin. A designer should be able to drop the module into a host game, rename the nouns, set the choices, and run a table scene without inventing the missing rules.

## The Workshop Quality Bar

A complete module must pass this bar before it belongs in the workshop:

1. **Runnable procedure:** at least one numbered procedure that tells the GM when the module starts, what players choose, what is rolled, what changes, and when the procedure ends.
2. **Concrete state:** named tracks, pools, clocks, dice, tags, edges, or sheet fields. The module must say where the state lives and who updates it.
3. **Resolution checks:** explicit roll formulas, target numbers or success interpretation, push/Trouble behavior, failure results, and consequences for 0 / 1 / 2+ successes where relevant.
4. **Menus:** at least one action, investment, spend, move, or project menu with enough options to run varied play. A menu is written as bolded ALL-CAPS move names with rule paragraphs, not as vague bullets.
5. **Tables:** at least one event/fallout/opportunity table and one reference/choice table. If the module uses a D66 family, ship the family or ship a generator procedure precise enough to create every missing entry.
6. **Pressure loop:** the rule set must create a recurring decision under scarcity. If it only grants benefits, it is not a YZE rule set yet.
7. **Integration contract:** state whether the module replaces or stacks with host rules, what inputs it needs, what outputs it creates, and what caps prevent collisions.
8. **Failure modes:** name abuse risks, pacing risks, table-burden risks, and tone risks, with fixes.
9. **Checks:** include math/tempo checks, attrition checks, action-budget checks, and felt-experience checks.
10. **Worked reskin:** include one concrete genre implementation with terms mapped, settings chosen, a short play example, and a note on what would change in a second genre.
11. **Publication handoff:** include player-facing rule text, GM-facing procedure text, quick-reference entries, and character/base/sheet fields.

**Minimum density test:** a major module normally needs 150+ lines, 3+ tables or table-equivalent lists, 1+ numbered procedure, 1+ move menu, 1+ consequence engine, 1+ choice table, and 1+ worked example. A short module can be smaller only if the rule pattern is deliberately narrow and still runnable.

**Forbidden shallow patterns:**

- "Use this for horror/politics/heists" without a roll procedure.
- "Create a table of consequences" without giving the table or a full generator.
- "The GM decides a cost" without a cost ladder or calibration.
- "Build parallel families" without at least one complete family and a method for the rest.
- A new pool that only gives bonuses and has no upkeep, cap, risk, expiry, or hard choice.
- A scene type that names roles but never says what a round looks like.
- A rule set with no sheet fields, no state change, and no ending condition.
- A reskin example that only swaps nouns and does not set choices or show play.

## Contents

1. Origin — how this was built
2. Drop-in summary
3. The generic design space
   - 3a. Rule overview
   - 3b. NEW CONCEPTS introduced
   - 3c. Core state
   - 3d. Setup procedure
   - 3e. Scene / turn / period procedure
   - 3f. Resolution checks
   - 3g. Menus
   - 3h. Tables and generators
4. The pressure loop
5. Choices
6. Integration points
7. Handshake
8. Module composition
9. Failure modes & edge cases
10. Check notes
11. Publication handoff
12. Worked genre example — [Genre]
13. Module audit checklist

## 1. Origin — how this was built

- **Source pattern(s):** P# from `16-mechanical-primitives.md` (e.g. P2 capped pool, P4 typed D66, P5 resource die, P6 activity menu, P7 org lifecycle).
- **Advanced composition(s):** one or more of `16`'s clocks/fronts, relationship edges, revelation ladders, heat pressure, crew-role menus, vehicle-as-character, rumor economies, project tracks, etc.
- **Reinvention operator:** Domain Transfer / Inversion / Recalibration / Fusion / Abstraction-Climb from `18 §4`.
- **Target psychology:** one cell from `17`'s dual-use matrix, stated as behavior: caution, desperation, ambition, paranoia, teamwork, rivalry, stewardship, etc.
- **Host problem:** the recurring table problem this rule set solves.
- **Signature test:** if this is a signature rule, name the play behavior it changes. If it does not change behavior, downgrade it to a reskin of an existing pattern.

## 2. Drop-in summary

This section is the one-page GM handoff.

- **Use when:** [campaign situations, genres, and scene types where this module earns its table time.]
- **Do not use when:** [campaigns where this adds bookkeeping without pressure.]
- **Requires:** [host-game inputs: time unit, skill, attribute, harm model, Willpower/Faith, faction layer, travel layer, base layer.]
- **Creates:** [new tracks, pools, actions, sheet fields, GM tables, event procedures.]
- **Primary loop:** [one sentence: players spend/choose/risk X to gain Y while Z worsens.]
- **Resolution grammar:** [attribute + skill + gear + module modifier; or opposed roll; or resource die; or D66 table.]
- **Default layer:** General / Situational / Optional / Campaign Mode.
- **Stacking default:** replace / stack / exclusive / requires cap.

## 3. The Generic Design Space

### 3a. Rule overview

Write 2-4 paragraphs that strip away genre nouns and explain the rule set as an abstract machine. Name the resource, the loop, and the core decision.

The overview is not enough by itself. It is the conceptual handle. The runnable content starts in §3c and must contain the actual rules.

### 3b. NEW CONCEPTS introduced

Every rule pattern that does **not** already exist in the core engine (`references/00`-`15`) is flagged here.

- **NEW CONCEPT — [name]:** [one-line definition, why it extends the engine, and which pattern/operator produced it.]

Pure recombination of existing patterns is not flagged. If a concept is an application of an operator, name the operator but flag only the new application.

### 3c. Core state

Define every persistent state object.

| State | Range / type | Starts at | Changes when | Visible to players? | Stored on |
| --- | --- | --- | --- | --- | --- |
| [Track] | 0-6 clock | 0 | [trigger] | yes/no | sheet / map / GM log |
| [Pool] | capped points 0-5 | [value] | earned/spent | yes | character / org |
| [Die] | D6-D12 resource die | D8 | rolled on use | yes | party sheet |
| [Edge] | -3 to +3 relation | 0 | faction move | maybe | faction web |

State must change in play. A module with no state change is normally an encounter procedure, not a rule set.

### 3d. Setup procedure

Use a numbered list. A GM must be able to install the module from this section alone.

1. **Choose the host layer:** PC scene, travel block, downtime period, faction turn, base turn, or campaign season.
2. **Map the host terms:** choose the governing ATTRIBUTE, SKILL, time unit, harm family, Willpower/Faith, and existing consequence table.
3. **Create the state:** add the tracks/pools/dice/edges from §3c to the appropriate sheet.
4. **Set the starting values:** give default starts and campaign-start alternatives.
5. **Choose the choice pack:** low / standard / high intensity from §5.
6. **Install limits:** caps, once-per-period rules, stacking limits, no-free-refund rules.
7. **Seed pressure:** add the first event, rival, clock segment, debt call, omen, project obstacle, or shortage.

### 3e. Scene / turn / period procedure

Ship the active play loop. Pick the template that fits and fill it in.

**Scene procedure template**

1. **Frame the pressure:** name the immediate stake, consequence family, and end condition.
2. **Declare positions:** assign range bands, social distance, vehicle stations, faction stances, project roles, or other module positions.
3. **Choose actions:** each involved PC chooses one module move or a normal host action.
4. **Resolve rolls:** roll using §3f; apply successes, banes/Trouble, and opposition.
5. **Spend resources:** allow spends only from the listed spend menu.
6. **Advance state:** update tracks, clocks, pools, relationship edges, damage, or exposure.
7. **Trigger fallout:** if a threshold is crossed, roll or choose from the consequence table.
8. **Check end condition:** victory, escape, collapse, concession, depletion, timeout, or escalation.

**Period procedure template**

1. **Look back:** apply upkeep, wounds, debts, weather, market shifts, faction moves, or previous consequences.
2. **Assess:** reveal the current risk/opportunity picture with one roll or table.
3. **Choose strategy:** pick a stance, choice, route, posture, project focus, or investment.
4. **Commit resources:** pay costs before the roll when the pressure is about risk; after the roll only when the module is about opportunity.
5. **Operate:** resolve weekly/monthly/seasonal activities.
6. **Reckon:** make the core roll or resource-die check.
7. **Payout and fallout:** pay profit, progress, harm, heat, reputation, debt, or loss.
8. **Reinvest:** allow recovery, repair, improvement, relationship mending, or expansion.
9. **Seed next period:** record one unresolved pressure that will matter next time.

### 3f. Resolution checks

State the roll grammar exactly.

- **Default roll:** ATTRIBUTE + SKILL + gear/tool + help (cap +3 unless module says otherwise) + module modifiers.
- **Difficulty:** use `00-engine-core.md` modifier bands. Avoid hidden target numbers unless the host game already uses them.
- **Push / Trouble:** say whether this roll can be pushed. Long-period economy rolls usually cannot be pushed unless the push creates debt, exposure, or lasting harm.
- **0 successes:** [hard consequence; no progress; fallout table; state worsens.]
- **1 success:** [baseline success; cost paid; state holds.]
- **2 successes:** [success + one menu pick.]
- **3+ successes:** [success + additional menu picks, scale effect, or D66 tens modifier.]
- **Banes / Trouble:** [attribute damage, gear damage, heat, stress, resource die step-down, faction offense, project flaw.]
- **Opposed use:** [if relevant: opponent rolls X; ties mean Y.]
- **Resource-die use:** [roll die; 1-2 step down / deplete; 6+ boon; exact thresholds.]

Do not write "resolve normally" for the module's central roll. A module exists because its resolution is interesting.

### 3g. Menus

Every menu option must say trigger, cost, roll if any, effect, and consequence. Write action/move names as bolded ALL-CAPS paragraphs.

**Action / spend menu minimum:** ship 6-12 options for a central scene module; 4-8 options for a narrow downtime module.

**[MOVE NAME].** [Action type or time cost, if relevant.] [Cost.] Roll [formula] or spend [resource]. On success, [effect]. For each extra success, [menu pick]. On failure or Trouble, [consequence].

**Common menu families**

| Family | Options to include | Pressure it creates |
| --- | --- | --- |
| Action menu | attack, defend, maneuver, assist, recover, abuse, retreat | action scarcity |
| Spend menu | boost roll, avoid harm, buy clue, reduce heat, call favor, seize tempo | capped-resource scarcity |
| Investment menu | safety, output, growth, secrecy, staff, reserves, reputation | future-vs-present scarcity |
| Fallout menu | harm, debt, exposure, loss, rivalry, delay, flaw, obligation | consequences with teeth |
| Recovery menu | rest, repair, therapy, reconciliation, ritual cleansing, legal cover | time scarcity |

### 3h. Tables and generators

Tables are required when the module creates recurring uncertainty. They are especially important for fallout, events, opportunities, rumors, critical outcomes, market shifts, panic, scandals, project complications, and faction moves.

**D66 family standard**

- 11-16: pressure from the environment or situation.
- 21-26: pressure from an ally, dependent, crew, or internal weakness.
- 31-36: pressure from a rival, monster, authority, enemy, or external actor.
- 41-46: opportunity with a cost.
- 51-56: success that creates a new obligation.
- 61-64: major boon with a hook.
- 65: permanent mark, scar, promotion, public change, or campaign-state shift.
- 66: catastrophic or legendary result, still playable unless the module explicitly handles character exit.

If the table is not D66, explain why the smaller table is enough. A D6 table is acceptable for a narrow procedure used rarely. A core recurring module should normally use D66 or several complete D6/D12 families.

**Generator standard**

If you use a generator instead of a full table, it must include:

1. a roll grammar;
2. result bands;
3. 6+ noun lists or effect lists;
4. consequence severity;
5. a worked generated result;
6. a rule for repeating or escalating old results.

## 4. The Pressure Loop

Name the loop's shape and write it as state transitions.

**Loop sentence:** Players choose [risky action/investment] to gain [benefit], which raises/depletes [pressure state], forcing [future hard choice].

**State transition map**

| Beat | Player choice | Roll / cost | State changes | Next pressure |
| --- | --- | --- | --- | --- |
| Tempt | [what looks attractive] | [cost] | [pool + / track -] | [risk introduced] |
| Commit | [what is risked] | [roll] | [success/failure state] | [new constraint] |
| Consequence | [who absorbs it] | [table/check] | [harm/heat/debt/etc.] | [recovery needed] |
| Recovery | [repair or push on] | [time/resource] | [pressure relieved or banked] | [loop restarts] |

**Five-loop proof:** say whether the module touches Expedition, Conflict, Recovery, Willpower/Faith, and Base. If a loop is inactive, explicitly collapse it with a reason.

## 5. Choices

Each choice must include effects, not just adjectives.

| Choice | Low | Standard | High | Warning |
| --- | --- | --- | --- | --- |
| Intensity | trigger once/session | trigger once/adventure or period | trigger every scene/turn | high intensity can crowd the host loop |
| Lethality / collapse | consequence is delay or cost | consequence injures state | consequence can remove actor/org | high collapse needs recovery rules |
| Resource cap | 3 | 5 | 7+ | caps above 5 weaken scarcity |
| Recovery speed | scene | session/period | arc/season | slow recovery can create despair |
| Event frequency | on threshold only | once/period | every failed roll | too frequent becomes noise |
| Bonus size | +1 die narrow | +1 die broad or +2 narrow | +2 broad / persistent | persistent broad bonuses need cost/cap/risk |
| GM load | one track + one table | 2-3 tracks + table family | map/web + several tables | high load needs reference sheet |

Every module should also include one genre-specific choice pack:

| Pack | Use for | Starting state | Event cadence | Recovery | Tone |
| --- | --- | --- | --- | --- | --- |
| Lean | action-forward games | low pressure | only on miss/threshold | fast | pulpy |
| Standard | campaign play | moderate pressure | once per scene/period | moderate | tense but fair |
| Harsh | horror/survival/political tragedy | high pressure | every period + threshold | slow | costly, paranoid |

## 6. Integration Points

State what the module touches and how hard.

| Host system | Replace / stack / ignore | Required cap | Notes |
| --- | --- | --- | --- |
| Core resolution | [replace/stack] | [modifier cap] | [e.g. uses normal dice pool] |
| Push / Trouble | [replace/stack] | [once per roll] | [push creates X] |
| Willpower/Faith | [replace/stack] | [cap] | [avoid two currencies doing same job] |
| Harm / recovery | [replace/stack] | [healing limit] | [critical table family] |
| Action budget | [replace/stack] | [slow/fast/free limit] | [free actions are dangerous] |
| Travel / downtime | [replace/stack] | [time unit] | [when it fires] |
| Base / faction | [replace/stack] | [turn cadence] | [org state changed] |
| Advancement | [replace/stack] | [XP gate] | [new talents or unlocks] |

**Replace vs stack rule:** if a host game already has a rule that answers the same table question, replace it or merge them. Do not stack two full systems that both tax the same attention, harm, heat, social standing, or downtime period unless the module ships a shared cap.

## 7. Handshake

- **Prerequisites:** [systems the host game must already have.]
- **Inputs:** [host-game terms to map: skill, attribute, Willpower/Faith, time unit, consequence family, faction standing, travel scale, base scale.]
- **Outputs:** [new pools, tracks, actions, tables, sheet fields, GM procedures.]
- **Touched systems:** [resolution, push, Willpower/Faith, harm, recovery, action budget, travel, base, powers, advancement.]
- **Replaces or stacks:** [explicit replace/stack rule.]
- **Incompatibilities:** [modules or host rules that need caps or merging.]
- **Sheet fields:** [character sheet, party sheet, org sheet, map, faction web, GM clock.]
- **GM prep:** [what the GM must prepare before the session.]
- **Player-facing load:** [what players must track themselves.]

## 8. Module Composition

Every module must say how it combines with other workshop modules.

| Combined with | Works cleanly? | Required cap / merge | Failure risk |
| --- | --- | --- | --- |
| [Module] | yes/no/with cap | [shared pool, max modifier, event cadence] | [why] |

**Composition rules of thumb**

- If two modules both create a spendable pool, either merge the pools or make one a spend menu inside the other.
- If two modules both create end-of-period events, alternate them or combine into one D66 table.
- If two modules both grant persistent +1 dice, cap total broad persistent bonuses at +2.
- If two modules both create social standing, decide which one owns public identity and which one owns private obligation.
- If a module turns downtime into play, do not also run a full downtime module every week unless the campaign is explicitly about management.

## 9. Failure Modes & Edge Cases

Run the module against `13 §5` and `19 §4`.

| Failure mode | Symptom | Fix |
| --- | --- | --- |
| Free-resource engine | players can loop actions for net gain | add cap, cost, event trigger, or once-per-period limit |
| Broad permanent bonus | one choice dominates all rolls | narrow scope, require upkeep, or make it spendable |
| Action-budget leak | free/fast option becomes mandatory | limit to once/round, add cost, or make it replace an action |
| Agency collapse | failure removes meaningful choices | add concession, retreat, recovery, or partial success |
| Death spiral | bad result makes recovery impossible | create relief valve or floor |
| Bookkeeping drag | state updates exceed drama | collapse tracks, reduce event cadence, or move to period play |
| Noun-only reskin | setting words change but behavior does not | alter choices, costs, consequence family, or loop weight |
| GM fiat gap | procedure says "decide" too often | add table, cost ladder, or decision tree |

## 10. Check Notes

Use `24-checks-worksheets.md`.

- **Dice math:** does a competent actor sit near the intended success band? If not, state the intended genre posture.
- **Attrition:** how many scenes/periods before the key resource depletes under ordinary use?
- **Resource loop:** where does the resource enter, leave, cap, expire, and become risky?
- **Action budget:** does any option grant a free action, extra action, or persistent modifier?
- **Abuse surface:** can players farm resources, avoid consequences, stack bonuses, or reset clocks?
- **Table burden:** how many things must players and GM track at once?
- **Felt experience:** does the module create the target psychology without creating false choices or despair?
- **Playability after catastrophe:** after the worst ordinary result, what can players still do?

## 11. Publication Handoff

Write this section in rulebook prose, not design jargon.

- **Player rule:** [publication-ready text explaining when the player can use it, what they roll/spend, and what happens.]
- **GM procedure:** [when to call it, what to prepare, how to adjudicate consequences, how to end the scene/period.]
- **Quick reference:** [trigger, roll, costs, success, failure, fallout, recovery.]
- **Sheet fields:** [exact labels and ranges.]
- **Example callout:** [short example of play.]
- **Designer note:** [optional; explain why the rule exists and how to tune it.]

## 12. Worked Genre Example — [Genre]

This must be concrete enough that another AI can reskin from it.

### Terms mapped

| Generic term | Genre term | Host-game hook |
| --- | --- | --- |
| [Pressure] | [e.g. Heat, Fear, Suspicion] | [existing rule/table] |

### Settings chosen

| Choice | Setting | Reason |
| --- | --- | --- |
| Intensity | Standard | [why] |

### Installation

1. Add [sheet field].
2. Use [skill] for the core roll.
3. Trigger [table] when [threshold].
4. Recover by [procedure].

### Play example

Write a short 1-2 turn/scene example:

- the GM frames the pressure;
- a player chooses from the module menu;
- the roll is made;
- state changes;
- a consequence or opportunity appears;
- the table has a clear next decision.

### Second-genre reskin note

Explain what changes when the same module is used in a different genre: not only nouns, but choices, consequence family, event cadence, and recovery speed.

## 13. Module Audit Checklist

Before shipping, answer yes to every item:

- [ ] The module has a runnable setup procedure.
- [ ] The active scene/turn/period procedure has start, choices, roll, state change, fallout, and end condition.
- [ ] Every new state object has range, start value, trigger, visibility, and sheet location.
- [ ] The core roll has exact dice grammar and 0 / 1 / 2+ success interpretation.
- [ ] Push/Trouble behavior is explicit.
- [ ] There is at least one full menu with costs and consequences.
- [ ] There is at least one event/fallout/opportunity table or a complete generator.
- [ ] Choices have rules effects, not just tone labels.
- [ ] The pressure loop has a cost, cap, risk, or expiry.
- [ ] The module states replace/stack behavior for host systems.
- [ ] The module includes incompatibilities and composition caps.
- [ ] Failure modes name both abuse risks and felt-experience risks.
- [ ] Checks includes math, attrition, resource loop, action budget, abuse, table burden, and felt checks.
- [ ] Publication handoff includes player rule, GM procedure, quick reference, and sheet fields.
- [ ] Worked example maps terms, sets choices, shows play, and explains at least one alternate reskin.
