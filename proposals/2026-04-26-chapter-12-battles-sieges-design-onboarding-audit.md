# Chapter 12 Audit: Battles & Sieges Design, Onboarding, and Coverage

## Purpose

This proposal audits `02-gamemasters-guide/12-battles-and-sieges.md` as:

- a battle subsystem
- a siege and campaign subsystem
- a teaching chapter for first-use GMs
- a handoff target from Chapter 11 rather than a replacement for it

The goal is not to rewrite the chapter from scratch. The goal is to identify what already works, where the design is incomplete or hard to run, what military topics are still missing, and which fixes would yield the most value for the least manuscript sprawl.

## Scope and boundaries

This audit treats Chapter 11 and Chapter 12 as separate but linked jobs.

### Chapter 11 already owns

The following should remain primarily in `11-politics-of-the-forbidden-lands.md`:

- faction-scale war preparation
- levy, retainers, and mercenary sourcing
- weekly army upkeep and campaign burden
- occupation as political state
- settlement damage and postwar fallout
- the larger transition from feud to open war

### Chapter 12 should own

The following should be fully runnable inside `12-battles-and-sieges.md`:

- troop-scale battle procedure
- tactical battlefield decisions
- siege procedure once the investment is active
- immediate logistical and morale pressure during campaign movement and battle
- immediate aftermath of the fight or fall of a place
- player-character and named-character participation in battle scenes

This distinction matters because some apparent gaps are not real gaps. They are already carried by Chapter 11 and should not be duplicated.

## Executive judgment

Chapter 12 is strong. Its main problems are not weak ideas. Its main problems are:

1. a few genuine procedure holes
2. one or two scale contradictions
3. onboarding overload caused by dense section sequencing
4. several tactical subjects that are implied, but not formalized enough to run cleanly

The chapter already has the right overall shape. It does not need replacement. It needs sharpening.

## What the chapter already does well

### Design strengths

- The chapter connects battle, siege, hunger, disease, pay, prisoners, sack, and occupation into one campaign logic.
- Attrition matters before the clash, during the clash, and after the clash.
- Siege rules feel materially different from open battle instead of being open battle with walls stapled onto it.
- The chapter gives named characters real influence without collapsing the mass battle back into ordinary skirmish play.
- The aftermath material is harsh, practical, and useful. It understands that the fighting is not the end of the war.

### Onboarding strengths

- The chapter opener teaches scale and mood fast.
- Most examples now teach by visible consequence rather than out-of-world mechanics language.
- The chapter usually explains rules in practical order inside each subsection.
- The prose sounds like a game book about iron, grain, fear, mud, and authority rather than a system memo.

## Onboarding and voice analysis

Chapter 12 is trying to do three jobs at once:

1. teach a GM how to run one battle tonight
2. support campaign warfare over time
3. provide a wartime reference chapter for troops, functions, talents, and events

All three jobs are valid. The problem is that the chapter does not always signal when it changes from one job to another.

### Current onboarding friction

| Area | What the reader gets | Why it slows learning |
|---|---|---|
| Early battle core | Order of battle, troop dice, morale, and battle sequence | Good material, but a first-use GM still lacks one compact turn loop |
| Mid-chapter conditions | Terrain, weather, night attack, feigned retreat, ambush | Useful tactical modules arrive before the core sequence feels fully locked in |
| Siege layer | Clear and substantial | Comes before the reader has had a worked battle example that proves the base engine |
| Campaign pressure | Supplies, movement, disease, salaries | Strong material, but it further stretches the chapter from immediate use into long-form reference |
| Reference material | talents, unit catalog, special troop types, stronghold war functions | Valuable, but heavy after the reader has already absorbed multiple subsystems |

### Voice findings

The chapter's voice is mostly right. It is strongest when it does one of these things:

- states a battlefield truth plainly
- gives the rule that follows from that truth
- shows the human cost in one hard example

It is weakest when onboarding and reference burdens pile up together. Then the reader can feel the manuscript pulling in two directions at once:

- native rulebook prose
- compendium-style support material

That is not a sentence-level voice problem. It is a chapter-organization problem.

### Onboarding proposals

#### Proposal A: add a short quickstart at the start of the chapter

A compact subsection near `### What This Chapter Is` should explain the minimum runnable path:

1. build troops
2. divide into left, center, right
3. deploy and roll INSIGHT
4. roll the speech and assign morale
5. resolve range approach if relevant
6. run the battle turn loop
7. end on rout, retreat, surrender, or nightfall
8. resolve aftermath

This would help the chapter teach itself before it expands into siege, logistics, and catalog material.

#### Proposal B: separate core rules from support modules more clearly

The chapter would benefit from stronger signals such as:

- **Core battle rules**
- **Advanced battlefield conditions**
- **Siege rules**
- **Campaign pressure rules**
- **Optional spotlight rules**
- **Reference material**

This does not require a rewrite. It requires clearer framing.

#### Proposal C: include one worked battle-turn example

The chapter has many good examples, but it still lacks one compact worked procedure example showing:

- morale distribution
- ranged approach turns
- melee resolution
- protection
- demoralization
- regroup attempt
- resulting battlefield state

That example would teach more than several additional atmospheric inserts.

## Full game design analysis

## Battle engine

The battle engine has the right bones:

- three sections
- troop-scale dice pools
- morale as staying power rather than abstract courage alone
- command presence as real force multiplication
- tactical conditions that matter materially

The main design issue is not the existence of too many moving parts. It is that several of the most important transitions are not formalized tightly enough.

### Major battle-system issues

#### 1. Demoralization uses two scales at once

In `#### Morale Points`, the text says each result of 1 on a base die triggers demoralization, and the number shown on that die equals the number of soldiers fleeing. It then says each fleeing group becomes one lost base die.

That creates a contradiction.

A base die is not one soldier. It is twenty infantry, five cavalry, or one monster unit at the chapter's stated scale. The rule currently tries to be exact and abstract at the same time.

**Recommendation:** choose one scale and state it cleanly.

Best option: treat each demoralization result as one fleeing group, and define a fleeing group as one base die's worth of the troop's unit type.

#### 2. The battle turn is explained but not yet operationalized

`#### Battle Turns` and `#### The Battle Roll` explain the loop, but not in strict table order.

A GM still has to infer:

- when commanders move
- when reserves replace battered troops
- when ranged-only turns stop
- when winning sections pivot
- when pursuit is chosen instead of pivot
- when regroup attempts happen relative to casualties and morale loss

**Recommendation:** add a numbered battle-turn procedure.

#### 3. Reserve use needs a real rule, not only implications

The chapter explains replacement but does not cleanly define reserve commitment as a tactical decision.

Missing answers include:

- when reserves can be committed
- whether they enter on the same turn or next turn
- whether a reserve may relieve a pressured front before collapse
- whether a general may refuse to commit reserves without conceding immediately

**Recommendation:** add a `Commit Reserves / Relieve the Line` subsection.

#### 4. Breakthrough exploitation is underdefined

The text says a victorious section pivots inward, but does not fully explain:

- when the pivot happens
- whether the bonus is automatic flank or rear pressure
- whether pursuit can replace pivot
- whether a winning troop may instead strike a reserve, baggage, or siege asset

This matters because exploiting success is one of the main reasons battlefield tactics exist in the first place.

**Recommendation:** add a `Winning a Section` rule.

#### 5. Friendly fire exists, but its resolution is not fully anchored

The chapter correctly states that skirmishers firing into allied melee risk harming allies. It does not yet clearly state how that damage is resolved inside the troop system.

**Recommendation:** state whether these casualties become direct troop damage, demoralization, or both. Keep it simple.

## Siege engine and siege loop

The siege rules are good and often excellent. They understand:

- compression on the wall
- engine protection and engineering dependency
- civilian pressure
- sortie necessity
- disease as a siege weapon without intention

The weak point is not the existence of siege content. The weak point is that several classic siege transitions need one more layer of procedure.

### Major siege-system issues

#### 1. Relief army versus siege line is not yet formalized

The chapter covers:

- blockade
- sortie
- surrender and parley
- siege engines
- supply runs

It does not yet provide a clean procedure for the classic case where:

- defenders are inside
- besiegers are outside
- a relief force arrives from beyond the ring

That is one of the most important military situations the chapter should support.

**Recommendation:** add a `Relief of a Siege` procedure.

#### 2. Gate and breach fighting need a compact transition rule

The chapter explains walls, towers, and assault well enough, but the transition from:

- wall or gate advantage
- to breach or broken gate
- to courtyard or interior fighting

is still too dependent on GM improvisation.

**Recommendation:** add a short `Breach and Gate Fighting` procedure that explains how sections remap once the wall or gate no longer defines the whole fight.

#### 3. Counter-siege methods are thinner than assault methods

Attackers get a rich toolbox. Defenders get fewer formal responses than the chapter's own logic suggests.

The chapter would benefit from clearer support for:

- countermine response to tunnels
- fire attacks against towers and rams
- engine sabotage beyond general sortie language
- deliberate abandonment of outer wall to preserve an inner defense
- artillery counterfire when both sides have engines or elevated ranged assets

These do not all need major subsystems, but they need at least explicit GM-facing procedures or options.

#### 4. Siege-engine information visibility is unclear

The rules do not clearly say how openly progress toward engine completion should be tracked from the defender's point of view.

In practice defenders can see towers being built, hear mining, and judge when a ram is close to mattering. The text should decide whether cumulative engine progress is:

- openly tracked
- estimated by observation
- hidden and GM-judged

**Recommendation:** prefer open or estimate-based tracking. Full secrecy adds little and confuses sortie timing.

## Campaign pressure and logistics

This is one of the chapter's strongest areas. The supply system, hunger rules, weekly disease logic, and pay failure all feel like real wartime pressures.

The main improvement need here is not new brutality. It is better connection between pressure and immediate player-facing choices.

### Strengths to preserve

- hunger as both combat weakness and desertion risk
- foraging depletion over time
- forced march and poor sleep stacking into demoralization
- disease as a weekly siege and battlefield-camp pressure
- payment failure as a path to mutiny, looting, and contract collapse

### Pressure-system gaps

#### 1. Baggage, camp, and rear-area vulnerability are still light

The chapter understands supply lines, but it says much less about:

- baggage train attacks
- camp raids
- beasts breaking loose
- siege-camp security
- panic in the rear affecting battle outcome

This matters because medieval warfare often turned on what happened behind the line.

#### 2. Waterborne and crossing operations are still thin

The chapter mentions:

- sea-access blockades
- river crossings
- supply lines by road and route

It does not yet strongly support:

- ferry seizure and defense
- boat-borne relief or escape
- contested crossing beyond one crossing-turn penalty
- assault against waterside walls or gates

For the Ravenlands, this feels like a real omission.

## Audit on missing military tactics and strategy coverage

The chapter does not need to become a historical warfare treatise. It does need to cover the tactical decisions its own scope invites.

### Highest-value missing subjects

| Missing or undercovered subject | Why it matters | Suggested treatment |
|---|---|---|
| Reserve commitment and line relief | One of the central command decisions in battle | Add a formal rule |
| Breakthrough exploitation | Winning a section should change the battle in a clear way | Add a `Winning a Section` procedure |
| Siege relief battles | Common and dramatic campaign event | Add a dedicated procedure |
| Counter-siege methods | Defenders need more than endurance and sortie | Add compact optional rules |
| Screening, scouting, and pickets before battle | Deployment intelligence currently leans too heavily on INSIGHT alone | Add a short recon subrule or battlefield scouting option |
| River, ferry, and water operations | Fits the setting and campaign scale | Add a compact operations subsection |
| Rear-area and baggage vulnerability | Strong logistics chapter deserves tactical rear pressure too | Add one campaign-battle bridge rule |
| Controlled fallback from outer wall to inner defense | Important for strongholds with layered defenses | Add a breach/fallback note under sieges |

### Subjects that may remain optional modules

These are useful, but should not be required for the chapter to function:

- command friction from bad signals or misunderstood orders
- dust, smoke, and noise as recurring battlefield information penalties beyond weather
- artillery duels as their own distinct minigame
- morale contagion from nearby allied collapse across sections

These fit as optional advanced rules if space allows.

## Audit on missing procedural checks and rules

These are the places where the GM is most likely to stop and ask what exactly happens next.

### Must-fix procedural holes

| Section | Missing or unclear point | Why it matters |
|---|---|---|
| `Morale Points` | exact demoralization conversion | current wording mixes soldier count and troop-scale abstraction |
| `Battle Turns` | full turn order | first-use GMs need a checklist |
| `Troop Replacement` | reserve commitment timing | affects one of the chapter's biggest tactical choices |
| `Battle Line Sections` | pivot/exploitation timing | defines how victories spread across the field |
| `Ranged Troops and Range` | friendly-fire resolution | without this, the rule creates pause instead of pressure |

### Important clarifications

| Section | Clarification needed |
|---|---|
| `Commander Movement` | define adjacency for section transfer |
| `Victory and Defeat` | explain whether refusing to commit reserves counts as immediate concession or next-turn concession |
| `Blockade` | define what counts as relief forces being near enough to matter |
| `Siege Engines` | decide whether progress is tracked openly, visibly estimated, or kept hidden |
| `Walls` | clarify when a wall section stops functioning as a wall and becomes ordinary fought-over ground |

## Promotion-ready proposals for improvement

The most useful changes are not huge rewrites. They are targeted additions and one genuine correction.

## Must-fix before calling the chapter fully stable

### 1. Correct the demoralization rule

This is the single clearest rules problem in the chapter.

### 2. Add a numbered battle-turn procedure

This is the single clearest onboarding improvement.

### 3. Add a `Winning a Section` rule

This strengthens the tactical engine without bloating it.

### 4. Add a `Commit Reserves / Relieve the Line` rule

This gives the chapter one of the battlefield decisions it currently implies rather than supports.

### 5. Add a `Relief of a Siege` procedure

This closes one of the most important missing campaign-military situations.

## Strong should-fix additions

### 6. Add a brief quickstart near the chapter opening

This improves first use and does not threaten the existing structure.

### 7. Add a compact `Breach and Gate Fighting` transition rule

This reduces improvised handling during sieges.

### 8. Add a small counter-siege options section

Even a half-page of defender responses would improve siege play.

## Optional advanced modules if space permits

### 9. Add battlefield screening and picket rules

Useful if the chapter wants stronger pre-battle intelligence play.

### 10. Add rear-area and baggage pressure rules

Useful if campaign war wants to feel even more materially vulnerable.

### 11. Add water-operation rules

Useful if river, ford, ferry, and coast warfare are expected to recur.

## Suggested insertion points

| Proposal | Suggested landing place |
|---|---|
| Quickstart | after `### What This Chapter Is` |
| Battle-turn procedure | after `#### Battle Turns` |
| Winning a section | after `#### The Battle Roll` or after `#### Pursuit` |
| Commit reserves / relieve line | after `#### Troop Replacement` |
| Friendly-fire clarification | inside `#### Ranged Troops and Range` |
| Relief of a siege | after `#### Sorties` or after `#### Blockade` |
| Breach and gate fighting | after `#### Walls` or `#### Siege Engines` |
| Counter-siege methods | after `#### Sorties` |
| Water operations | after `### Campaign Movement` or inside `### Supplies` |
| Rear-area pressure | near `#### Cutting the Supply Line` |

## Recommended implementation order

If the chapter is being revised in stages, use this order.

### First pass: fix what most affects clarity and correctness

1. demoralization correction
2. battle-turn procedure
3. reserve commitment rule
4. winning-a-section rule
5. friendly-fire clarification

### Second pass: close the biggest military coverage gap

1. relief-of-siege procedure
2. breach and gate fighting procedure
3. counter-siege methods

### Third pass: improve onboarding and optional depth

1. quickstart framing
2. water operations
3. rear-area and baggage pressure
4. screening and picket options

## Final judgment

Chapter 12 is already a serious and usable warfare chapter. It does not need rescue. It needs tightening.

Its strongest qualities should be preserved:

- harsh logistical logic
- practical battle consequences
- real moral cost
- meaningful named-character participation
- clean handoff from Chapter 11 without duplication

The best revision path is not expansion for its own sake. It is to:

- correct the one clear scale error
- add a few missing procedures at the exact points where live play would otherwise stall
- mark the chapter's core path more clearly for first-use GMs
- cover the handful of important tactical situations the current draft still leaves mostly to GM instinct

If those changes land, Chapter 12 should become both easier to teach and harder to break.
