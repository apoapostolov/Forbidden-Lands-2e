<!-- markdownlint-disable MD013 -->

# Boss Phases, Intent, And Attrition

## Contents

1. Purpose
2. Design Position
3. Boss Contract
4. Phase Architectures
5. Linked Attack Tables And State Machines
6. Intent And Telegraphs
7. Powering Attacks Across Rounds
8. Strength-Band Attack Dice
9. Damage-State Models
10. Reactions And Interrupt Windows
11. Anatomy, Anchors, And Objectives
12. Phase Transition Procedure
13. Category-Specific Boss Logic
14. Worked Encounter Chassis
15. Balance Budgets
16. Failure Modes
17. Construction And Audit Procedure

## Purpose

Use this reference to design centerpiece enemies whose fights develop across
time rather than merely repeating a six-result attack table until Strength
reaches zero.

This module adds controlled support for:

- multiple combat phases
- linked attack tables representing combat states, stances, and cycles
- declared enemy intent
- attacks that gather force across rounds
- attack tables whose available results change with current Strength
- destructible body parts and external anchors
- limited reactions and interrupt windows
- objectives that change the enemy rather than only damage it

These mechanisms are optional extensions to the normal monster engine. Use
them for named leaders, apex beasts, major monsters, and demons whose defeat
should be a situation with changing priorities. Do not apply them to every
dangerous creature.

## Design Position

Forbidden Lands already makes monsters asymmetric through unpushable attacks,
special defenses, unusual bodies, and extra initiative. Extend that asymmetry
through information and state, not through hidden punishment.

A good boss fight asks a different question in each phase:

1. What is this thing preparing?
2. What can we change before it happens?
3. What did hurting it expose, destroy, or provoke?
4. Do we finish it, flee, bargain, rescue someone, or solve the site?

Treat videogame encounter design as a source of temporal structure. Translate
it into physical signs, short rules, and sandbox consequences. Do not import
invisible cooldowns, invulnerability cutscenes, mandatory damage races, or
precise movement puzzles that only make sense on a fixed digital arena.

## Boss Contract

Before adding a phase rule, write the following contract in plain language.

| Question | Required Answer |
| --- | --- |
| Phase identity | What materially changes in the body, purpose, command, curse, or site? |
| Tell | What can the adventurers perceive before the new danger resolves? |
| Trigger | What starts the change: Strength loss, destroyed anchor, elapsed rounds, broken oath, prey escape, or deliberate enemy choice? |
| Player lever | What action besides ordinary damage can alter, delay, redirect, or exploit the change? |
| Cost | What does the boss spend: an attack, position, armor, followers, stored power, secrecy, or control of the site? |
| End state | What does defeat, escape, surrender, banishment, or incomplete victory leave behind? |

Reject a phase that only says the enemy gains more dice. A numeric increase is
acceptable as the consequence of an observable change, but it is not a phase
identity by itself.

## Phase Architectures

Choose one architecture. Major campaign foes may combine two, but one must
remain primary.

### 1. Threshold phase

Change the profile when current Strength crosses a stated fraction of maximum
Strength. Half Strength is the clearest threshold. Use thirds only for a very
large foe with enough Strength that each band lasts more than one successful
attack.

Use when injury changes locomotion, exposed anatomy, courage, discipline, or
the stability of a manifested form.

### 2. Broken-part phase

Change the profile when a targetable body part is disabled. The players choose
which capability to remove and which transition to provoke.

Use when the enemy has wings, eyes, a weapon limb, a shell, a crown of horns,
ritual chains, or several independently vulnerable heads.

### 3. Anchor phase

Change the profile when an external object, host, rune, altar, banner, nest, or
terrain feature is disturbed. The enemy may be difficult to damage while its
anchors stand, but the anchors must be visible, inferable, and reachable.

Use for demons, undead, shrine guardians, brood creatures, and human enemies
whose cohesion depends on a standard, officer, drum, or fortified position.

### 4. Objective phase

Change the profile when the adventurers rescue a captive, close a gate, remove
a resource, cross a boundary, complete a rite, or force the enemy away from
its prey.

Use when killing the enemy is not the only or most important victory condition.

### 5. Clock phase

Change the profile at a declared round or after a repeated battlefield event.
Show the progression with physical signs: a gate bows inward, rain fills the
grave trench, eggs split, or the furnace reaches white heat.

Use a three-step clock. Longer clocks rarely justify the tracking burden.

### 6. Behavior phase

Change the profile when the enemy's goal changes. A predator may abandon
territorial warning and begin feeding; a captain may order retreat; a demon may
stop bargaining and attempt possession.

Use when morale, appetite, duty, or self-preservation should matter more than a
hit-point threshold.

### 7. Resource-spend phase

Let the enemy voluntarily consume something finite: brood, armor plates,
captives, stored blood, spell seals, command tokens, or escape routes. Spending
the resource produces a strong effect but makes later victory easier or changes
the aftermath.

### 8. Reversal phase

The apparent advantage becomes a new vulnerability. A shattered shell frees a
fast body but removes armor. A grounded flier gains a savage close attack but
loses safe perches. A demon fully manifests to strike and can finally be harmed
by ordinary weapons.

Reversal is usually stronger than simple escalation because it creates a new
decision rather than a larger number.

## Linked Attack Tables And State Machines

Use linked attack tables when the enemy's own actions change what it can do on
its next attack. Each table represents a concrete state: blazing or cindering,
airborne or grounded, stalking or feeding, shielded or exposed, embodied or
dispersed, disciplined or desperate.

This structure adds depth and unpredictability without requiring more actions.
The monster still attacks at its normal initiative. Only the table used for the
next attack changes.

### Core procedure

1. Mark one attack table as the starting table.
2. Whenever the monster attacks, roll on or choose from the active table.
3. Resolve the selected attack completely, including damage, movement, riders,
   and costs.
4. Apply any transition statement at the end of that attack.
5. Mark the destination table as active.
6. Use the destination table for the monster's next attack, including another
   initiative later in the same round if the monster acts more than once.

Use the exact transition phrase:

`After resolving this attack, move to Table B: Cindering.`

If an attack has no transition statement, remain on the current table. A
transition never grants an immediate extra attack unless the entry explicitly
spends another initiative or action to do so.

### No hard table limit

The procedure places no hard limit on the number of linked tables. A monster
can theoretically use any finite network of states. In practice:

- use two tables for a clear alternating stance, heat cycle, or exposed/recovery
  rhythm
- use three tables for a staged hunt, locomotion cycle, or manifestation path
- use four tables only for an exceptional centerpiece whose states are strongly
  signaled and materially different
- use more only when the tables form a simple generated system and the GM has a
  compact state map

Infinite conceptual design space does not justify infinite table handling. If
the GM cannot identify the active state from one token and one visible fictional
description, reduce the network.

### Table identity contract

Each table must state:

- **State:** what is physically, mentally, socially, or supernaturally true
- **Tell:** what players can perceive about that state
- **Permission:** what the state can do that other states cannot
- **Loss:** what the state lacks, risks, or cannot do
- **Transitions:** which attacks or external events move to other tables

Do not split one ordinary six-attack table into several cosmetic lists. A new
table is justified only when the state changes at least two of the following:

- attack functions
- range or mobility
- target-selection logic
- defense or vulnerability
- objective or appetite
- available counterplay
- relationship to terrain or allies

### Transition forms

#### Deterministic transition

One attack always moves to another table. Use this for expenditure, exposure,
landing, shedding, weapon breakage, completed orders, and other certain state
changes.

Example: a furnace burst always exhausts the elemental and moves from Blazing
to Cindering.

#### Probabilistic transition

Several results on the current table move to another table. The number of such
results determines the chance when attacks are rolled.

On a D6 table:

- one transition result gives a one-in-six chance
- two transition results give a one-in-three chance
- three transition results give a one-in-two chance
- four transition results give a two-in-three chance

Use this for uncertain reignition, regaining footing, recovering courage,
finding prey, reforming a body, or losing control.

#### Conditional transition

Move only if the attack meets a stated condition: inflicts damage, reaches the
anchor, catches fire, retains its target, is not DODGED, or consumes a resource.

State the fallback. If the condition fails, normally remain on the current
table.

#### Chosen transition

The attack lets the GM choose a destination representing an intelligent stance
or deliberate bodily act. The choice must occur after the stated cost and must
not silently counter information the players acted upon.

#### Player-forced transition

An adventurer's action, damage type, called shot, terrain change, bargain,
command disruption, or ritual can move the enemy to another table. Put this in
the special weakness or state rule, not only inside an attack result.

#### Clock transition

Move at the end of a stated round or when a visible clock fills. Use attack
transitions for the enemy's internal rhythm and clock transitions for the site
or external pressure.

### State-network shapes

#### Toggle

`A ⇄ B`

Use for hot/cold, shield/spear, corporeal/mist, flying/grounded, or
aggressive/guarding. This is the easiest structure to learn.

#### One-way escalation

`A → B → C`

Use for progressive manifestation, collapsing discipline, a ritual nearing
completion, or anatomy that cannot be restored during the fight.

#### Recovery loop

`A → B → A`

Use when a powerful state spends itself and a weaker state has a chance or task
to recover. The fire elemental example uses this shape.

#### Branch

`A → B or C`

Use when one action produces distinct states: the beast either secures prey or
is driven off; the captain commits reserves or withdraws; the demon chooses a
host or manifests.

#### Hub

`B ← A → C`, with returns to A

Use when one neutral or watchful state can commit to several specialized
stances. Keep the hub transitions deliberate and the specialized states narrow.

#### Cycle

`A → B → C → A`

Use for repeated locomotion, feeding, weather, breath, or ritual rhythms.
Players should be able to anticipate the next broad state even though the
specific attack remains uncertain.

### Rolling versus choosing attacks

Linked tables create probability only when attacks are rolled. If the GM may
normally select attacks, choose one procedure before combat:

- **Rolled state machine:** always roll on linked tables; use this when
  transition uncertainty is central.
- **Fictional selection:** the GM may choose any legal result, but must choose
  according to declared intent, body state, and objective; use this for tactical
  leaders.
- **Limited selection:** roll, then allow one reroll or a choice between adjacent
  results when a special ability permits it.

Never claim a 50% reignition chance while allowing the GM to select one of the
three reignition results whenever convenient.

### Table dice and state

Linked tables may use the same die or different dice. Use the same die when the
state changes capabilities but not breadth. Use different dice when the state
also changes the number of available actions.

Do not confuse two separate mechanisms:

- **Active table** answers which state supplies the attack list.
- **Attack die** answers which numbered results are currently available.

A wounded elemental might be on `Table B: Cindering` and roll D6 there. A large
construct might be on `Table A: Upright` but roll D8 instead of D10 because its
Strength has fallen. If combining linked tables with Strength-band dice, give
every table valid results from 1 through the smallest possible die.

### Transition timing and simultaneous initiative

Apply the transition after the entire attack resolves and after all simultaneous
effects in that initiative segment are determined. Mark the new state before
the next initiative segment.

If the monster has several initiatives, a transition on its first attack changes
the table used on its later initiative. This is a feature, not an extra action.

If the monster becomes Broken during the same simultaneous segment in which it
would transition, resolve Broken normally. Do not use the destination table to
grant a death attack unless a stated and telegraphed rule provides one.

### External changes while an attack is pending

If players force a state change after an intent is declared but before the
attack resolves, check whether the destination state can still perform that
attack.

- If the required anatomy, resource, or position is gone, interrupt it.
- If the new state contains a weaker version, use the stated interrupted result.
- If the change does not affect the enabling fiction, resolve the attack and
  remain in or move from the new state as explicitly stated.

Do not let one token occupy two states. Resolve contradictory transitions in
this priority order:

1. Broken or banished state
2. player-forced destruction or removal of the enabling feature
3. attack's own paid transition
4. end-of-round clock transition

### Defense changes

A table state may alter Armor Rating, resistance, movement, or a weak point, but
write those changes in a state line above the table. Do not hide a defense
change inside one of six attack results.

Example:

`CINDERING: Armor Rating is reduced by 2. The elemental cannot fly or use attacks
with SHORT range. Water attacks inflict one additional damage.`

This gives players useful information as soon as the state visibly changes.

### Counterplay and prediction

Linked tables reward observation only if states are legible.

- Describe the new state every time the active table changes.
- Let Lore or prior observation reveal likely transitions without listing exact
  probabilities in prose.
- Let players deliberately force or delay at least one transition when the
  cycle contains a severe attack.
- Make the weaker state meaningfully exploitable rather than merely lower in
  damage.
- Preserve uncertainty inside the state through the attack roll.

The goal is layered prediction: players learn the current family of threats but
do not know the exact next result.

### Fire elemental recovery loop

This example uses two D6 tables. It begins on `Table A: Blazing`. The elemental
is dangerous and mobile while Blazing. Its largest attack exhausts the fire and
moves it to `Table B: Cindering`. Cindering attacks are weaker, Armor Rating is
reduced by 2, and results 4-6 reignite it after resolving, producing an exact
50% chance of returning to Blazing when attacks are rolled.

#### Table A: Blazing

**State:** Flame fills the body and streams from every joint. It has its normal
Armor Rating and movement.

| D6 | Monster Attack |
| --- | --- |
| 1 | **LASHING FLAME!** The elemental strikes one target at ARM'S LENGTH with 7 Base Dice and Weapon Damage 1. A target suffering damage catches fire. |
| 2 | **HEAT-SHOVE!** A pulse attacks all targets at ARM'S LENGTH with 6 Base Dice and Weapon Damage 1. Anyone suffering damage is driven to NEAR range. |
| 3 | **BLAZING PURSUIT!** The elemental moves one range band or one zone toward the nearest burning target, then attacks it with 8 Base Dice and Weapon Damage 1. |
| 4 | **FIRE-LANE!** The elemental declares a straight lane to NEAR range. Exposed targets in it suffer an attack with 7 Base Dice and Weapon Damage 1. |
| 5 | **DEVOUR THE FLAME!** The elemental consumes one unattended fire within NEAR range, restores 1 lost Strength, and moves beside that fire. If no fire exists, it uses LASHING FLAME instead. |
| 6 | **FURNACE BURST!** Fire detonates around the elemental. All other creatures within NEAR range suffer an attack with 10 Base Dice and Weapon Damage 1; anyone suffering damage catches fire. After resolving this attack, move to Table B: Cindering. |

#### Table B: Cindering

**State:** The body collapses into red-black coals and dragging ash. Reduce its
Armor Rating by 2. It cannot fly, use SHORT-range attacks, or consume fire with
DEVOUR THE FLAME.

| D6 | Monster Attack |
| --- | --- |
| 1 | **ASHEN SWIPE!** The elemental attacks one target at ARM'S LENGTH with 5 Base Dice and Weapon Damage 1. The target is smeared with visible hot ash even if no damage penetrates armor. |
| 2 | **CHOKING CINDERS!** One target within NEAR range must make an ENDURANCE roll. On failure, the target cannot perform a slow action on its next turn while coughing and clearing its eyes. |
| 3 | **SEEK KINDLING!** The elemental makes no damaging attack. It moves one range band or one zone toward the largest visible fire or combustible pile and remains Cindering. Adventurers can move, extinguish, or trap the fuel. |
| 4 | **EMBER BITE!** The elemental attacks one target at ARM'S LENGTH with 5 Base Dice and Weapon Damage 1. After resolving this attack, flame returns; move to Table A: Blazing. |
| 5 | **KINDLING LEAP!** Sparks carry the elemental to an unattended fire or burning target within NEAR range. It attacks that target with 6 Base Dice and Weapon Damage 1. After resolving this attack, move to Table A: Blazing. |
| 6 | **FLASH REIGNITION!** All creatures at ARM'S LENGTH face a fear attack with 5 Base Dice as the elemental erupts back into flame. After resolving this attack, move to Table A: Blazing. |

Water, smothering earth, or removal of every usable fire may force the elemental
to remain Cindering even when results 4-6 occur, if the entry establishes that
dependency. If so, state the rule as a SPECIAL WEAKNESS and reveal it through
steam, guttering coals, and Lore. Do not add the dependency secretly after the
players commit to the tactic.

### Additional state-machine patterns

#### Predator: Stalk → Pounce → Feed or Recover

The Stalk table isolates and marks prey. A pounce result moves to the Pounce
table. Successful seizure moves to Feed; a DODGED pounce moves to Recover. Feed
can heal or drag but exposes the beast. Recover contains lower-pressure movement
and a probabilistic return to Stalk.

#### Armored monster: Guarded ⇄ Exposed

Guarded attacks use shield, shell, or facing and contain one committed strike
that moves to Exposed. Exposed attacks are faster but lose armor; several
results turn the protected body toward the threat and return to Guarded.

#### Demon: Influence → Vessel → Manifest

Influence attacks manipulate signs and followers. A possession result moves to
Vessel. Damage to the host or a completed rite may force Manifest. Manifest has
the strongest physical attacks but permits ordinary targeting and includes
banishment transitions.

#### Human leader: Command ⇄ Desperate

Command attacks are orders, formation moves, and prepared volleys. Loss of the
standard, failed morale, or a personal charge moves to Desperate. Desperate
attacks include bargaining, escape, dueling, rallying, or an attempt to recover
the standard and return to Command.

### State-machine audit

Before approval, verify:

- the starting table is explicit
- the active state can be marked with one token
- every destination table exists
- every state has a visible tell and a meaningful loss
- every transition occurs at a precise time
- no transition grants an unstated extra action
- probabilistic claims match the actual number of transition results
- the GM cannot freely select results while claiming random transition odds
- severe states have a player-forced or player-delayed transition
- defense changes appear above the table
- the network cannot enter a state with no legal attack or exit unless that is
  an intentional defeat, dormancy, or escape state
- repeating the cycle remains interesting on its third occurrence

## Intent And Telegraphs

Use intent when an attack would otherwise be too punishing, arbitrary, or hard
to answer. Intent is declared fictional information, not a promise that the
enemy will ignore changing circumstances.

### Intent procedure

1. At the end of one of the boss's turns, name the visible preparation and mark
   the intended target, zone, route, or effect.
2. State what ordinary observation reveals. Do not reveal exact dice unless the
   group prefers open mechanics.
3. Let the effect resolve on the boss's next turn if its enabling condition
   remains true.
4. If players disrupt the condition, apply the listed interrupted result. Do
   not secretly substitute an equally strong punishment.

### Telegraph quality

Use all three layers for severe effects.

- **Sensory tell:** breath drawn, forelimbs braced, bow line raised, runes
  brightening, wind falling silent.
- **Spatial tell:** a target, lane, zone, anchor, or direction becomes obvious.
- **Behavioral tell:** followers scatter, the beast gives ground, the demon
  protects one seal, or the captain calls a recognizable order.

### Intent forms

| Intent | What It Pressures | Typical Answers |
| --- | --- | --- |
| Line | everyone in a charge, breath, or missile lane | scatter, take cover, block the lane, brace |
| Zone | one area will become dangerous | leave, fortify, extinguish, collapse a border |
| Marked prey | one victim is selected | guard, conceal, exchange position, break the mark |
| Anchor | the boss will feed from or defend an object | seize, move, spoil, or bait the anchor |
| Threshold | a site clock will complete | race the objective, withdraw, accept the change |
| Counter-intent | the boss waits for a declared player behavior | feint the behavior, spend another resource, force commitment |

### Honest retargeting

If the intended target becomes impossible, use one of these outcomes:

- the attack is lost
- the boss releases a weaker area effect
- the boss preserves part of the gathered power as stated by the rule
- the boss redirects only if a visible conduit or body motion makes that fair

Never declare a target and then freely choose another target at full force.

## Powering Attacks Across Rounds

Use stored power to create anticipation, movement, and interruption. Track one
kind of token per enemy. Most enemies should hold no more than three.

### WITHDRAW AND GATHER

**Statblock form:** `WITHDRAW AND GATHER:` When this result is rolled, the enemy
makes no attack. It retreats from ARM'S LENGTH to NEAR range, or moves one zone
toward a named source of force, and gains one Charge. Its next damaging attack
spends that Charge and gains +3 Base Dice. It cannot hold more than one Charge
from this rule or gain Charge from this result while already holding it.

This implements the cadence of a low attack-table result that creates a
stronger next turn. The lost attack and disclosed intention pay for the bonus.

Required counterplay:

- pursue and force the enemy away from its power source
- take cover or spread out
- provoke an early discharge against a poor target
- damage the organ, weapon, anchor, or stance holding the Charge
- flee the threatened area

Do not combine +3 Base Dice with increased Weapon Damage and an unavoidable
area attack. Choose one payoff channel.

### LOCK ON

The enemy marks a target it can perceive. On its next turn, its named attack
gains +2 Base Dice and one spatial privilege against that target. Breaking
line of sight, entering suitable cover, changing shape or scent, or forcing the
enemy to defend itself removes the mark.

### INHALE OR PRIME

The enemy spends its slow action filling a sac, winding an engine, drawing a
great bow, or opening a gate. Place one visible token. On its next turn it may
spend the token for an area attack. Hitting the relevant organ or mechanism
before then causes the interrupted result: usually lost power, self-damage, or
a smaller uncontrolled release.

### GATHER THE DEAD

The enemy spends its attack drawing from corpses, fear, blood, or broken
followers within a stated range. Remove or mark those sources. The next attack
gains a defined benefit. Adventurers can drag away, sanctify, burn, or screen
the sources.

### AIM THE FORMATION

A human officer or intelligent monster spends its action coordinating a volley,
charge, shield advance, or net cast. The ordered allies act on their normal
turn, but the order grants one group benefit. Silencing the order, breaking the
signal, engaging the officer, or disrupting formation cancels it.

### COOLING OR RECOVERY

After using an apex attack, the enemy exposes a weakness, loses armor, cannot
use that attack on its next turn, or must move to a recovery site. Cooldown is
worth tracking only when it creates a player opportunity.

## Strength-Band Attack Dice

The standard rule states that monsters do not become weaker when wounded. A
Strength-band attack die is therefore an explicit exception for an enemy whose
injury should reduce access to powerful actions. State the exception in the
entry.

### Attrition Die procedure

Build one attack table numbered 1-12. Roll a die determined by the enemy's
current Strength band.

| Current Strength | Attrition Die | Available Results |
| --- | --- | --- |
| more than three quarters of maximum | D12 | 1-12 |
| more than half, up to three quarters | D10 | 1-10 |
| more than one quarter, up to half | D8 | 1-8 |
| one quarter or less | D6 | 1-6 |

For a shorter three-state version, use D10 above half Strength, D8 at half or
less, and D6 at one quarter or less.

Place attacks by capability:

| Results | Design Function |
| --- | --- |
| 1-2 | survival, withdrawal, warning, failed exertion, or setup |
| 3-4 | basic bodily attack that remains plausible while crippled |
| 5-6 | reliable signature pressure |
| 7-8 | mobile, coordinated, or anatomy-dependent attack |
| 9-10 | full-body or high-control attack lost after serious injury |
| 11-12 | apex expression available only while nearly intact |

Do not make results 1-6 worthless. A badly wounded enemy remains dangerous;
it simply loses actions requiring intact anatomy, confidence, concentration,
or stored force. Results 1-6 should still vary target, position, and consequence.

### Example D10 degrading table

| D10 | Attack Function |
| --- | --- |
| 1 | Withdraw and Gather: no attack; retreat and empower the next attack |
| 2 | Guard the Wound: gain a narrow defense and reposition toward escape |
| 3 | Snap: standard single-target attack |
| 4 | Shove Aside: low damage plus forced movement |
| 5 | Hook and Hold: grapple or restrain one target |
| 6 | Desperate Sweep: light pressure against nearby targets |
| 7 | Bounding Rush: move before striking and knock prone |
| 8 | Rending Sequence: two linked bodily motions against one exposed target |
| 9 | Crushing Circuit: high dice and a strong control rider |
| 10 | Unbroken Catastrophe: telegraphed apex area attack |

At half Strength roll D8, naturally removing 9-10. At one quarter Strength roll
D6, removing 7-10. This is preferable to remembering conditional rerolls.

### Table-shape rules

- Put injury-dependent attacks high on the table.
- Put escape, defense, and core anatomy low on the table.
- Do not put all non-damaging results low; otherwise injury makes the enemy
  harmless too quickly.
- Do not use a D12 ladder if maximum Strength is so low that one hit crosses
  several bands.
- Recalculate the die after simultaneous damage at the end of the initiative
  segment, not in the middle of resolving one attack.
- If the GM chooses attacks instead of rolling, respect the current range of
  available results.

## Damage-State Models

Strength-band dice are one option. Choose the model that best explains the foe.

### Degradation

The enemy loses mobility, complex attacks, command, or supernatural stability
as Strength falls. This rewards sustained damage and makes victory feel
material.

### Exposure

The enemy loses defense but keeps offense. Reduce Armor Rating, remove a
resistance, or expose a called-shot target. Use for shells, armor, ritual skins,
and siege bodies.

### Frenzy

The enemy loses defense or judgment but gains one offensive privilege. Give it
one gain and one loss. Never increase dice, damage, targets, speed, and actions
together.

### Desperation

The enemy gains escape, hostage-taking, feeding, bargaining, or terrain-breaking
results at low Strength. This changes the stakes without merely making it more
lethal.

### Instability

The enemy's effects become broader but less controlled. Randomize direction,
make allies valid targets, expose anchors, or cause site damage. Use for demons,
elementals, constructs, and collapsing magic.

### Discipline collapse

Human enemies lose formation benefits, obey fewer orders, seek cover, surrender,
or flee as leaders and comrades fall. Do not model trained humans as monsters
that fight without self-preservation unless fanaticism, coercion, or immediate
necessity explains it.

## Reactions And Interrupt Windows

Triggered enemy reactions are expensive because they add action economy and
slow play. Use one named reaction, at most once per round, and identify what it
replaces or costs.

### Reaction models

| Model | Cost | Example |
| --- | --- | --- |
| Replace fast action | the enemy loses its next fast action | sidestep, shield turn, tail guard |
| Spend stored token | consumes Charge, Command, brood, or anchor power | emergency ward, lunge |
| Replace next attack | strong reaction prevents the next monster attack | collapse a tunnel, interpose a hostage |
| Once per phase | no recurring bookkeeping after use | shed skin, break chain, leap to perch |
| Sacrifice defense | immediate effect permanently lowers armor or exposes a part | shell block, wing screen |

### Fair trigger rule

Key the reaction to a narrow observable event: crossing a marked line, striking
an anchor, approaching a nest, attacking the commander, or leaving cover. Do
not use “whenever an adventurer acts” or several different triggers.

### Player interrupt windows

An interrupt window is a chance to answer a telegraphed action before it
resolves. State:

- the enabling feature
- the actions that can plausibly disrupt it
- any required roll and difficulty
- the partial result on failure
- what happens to the enemy's spent action

Accept creative interventions that attack the same fictional dependency. The
listed answer is a guarantee, not an exhaustive command puzzle.

## Anatomy, Anchors, And Objectives

### Part tracks

Give a part 1-4 Strength and a target penalty appropriate to its size and
exposure. Damage to a part does not also reduce main Strength unless the entry
says so. State what disabling it removes and what transition it causes.

Useful parts include:

- locomotion: wing, foreleg, burrowing claws, root mass
- perception: eye cluster, scent fan, echo bladder
- delivery: venom sac, breath organ, weapon limb, voice chamber
- defense: shell plate, shield arm, mist mantle
- control: crown, reins, command drum, binding chain

Use no more than three targetable parts. More turns the creature into a separate
board game.

### Anchor economy

Each anchor should sustain one property. Destroying the furnace removes
regeneration; breaking the banner removes formation; closing the breach removes
reinforcements. Do not make four anchors all duplicate generic invulnerability.

### Objective attacks

Let the boss attack objectives as well as characters: destroy a bridge, carry
away a captive, extinguish a ward, breach a gate, corrupt a spring, or reach a
corpse. This forces prioritization without inflating damage.

## Phase Transition Procedure

Resolve a transition in this order:

1. Finish the current simultaneous initiative segment.
2. State the visible transformation and update the battlefield.
3. Remove expired tokens, attacks, defenses, and parts.
4. Add the new rule package; do not retain old rules unless explicitly stated.
5. Reveal information the characters could directly perceive.
6. Apply one transition effect only if it was telegraphed or paid for by the
   boss's next action.
7. Reassess intent, morale, and escape goals.

Do not grant an automatic full attack simply because a threshold was crossed.
A transition may move the boss, shed a condition, or alter terrain, but any
free harmful effect must be small and stated in advance.

## Category-Specific Boss Logic

### Human leaders

Build phases from morale, formation, reserves, authority, and escape plans.
Human leaders should command ordinary actions, reveal prepared ground, call a
reserve once, offer terms, abandon followers, or lose obedience. Avoid giving
them unexplained monster immunities.

### Apex beasts

Build phases from warning, pursuit, injury, protection of young, exhaustion,
feeding, and escape. A beast's attack pattern should become simpler as anatomy
fails. It may become more desperate, but it should not tactically solve every
player response unless its senses and experience explain that intelligence.

### Monsters

Build phases from anatomy, supernatural metabolism, site dependence, and
discoverable weak points. Monsters can violate normal combat assumptions, but
each violation needs a body or curse that players can learn.

### Demons

Build phases from manifestation, anchors, bargains, names, possession, and
instability. A demon can change rule logic more radically than a beast, but its
radical effects require clearer symbols, taboos, or ritual dependencies.

## Worked Encounter Chassis

### Human: the bridge captain

**Primary engine:** command integrity.

- While the banner stands and the captain can be heard, one troop may receive
  an order each round.
- The captain may spend an attack to call `BRACE THE SPAN`, telegraphing a
  coordinated shove against anyone entering the bridge lane.
- At half troop Strength, discipline collapses. The captain must choose between
  holding the bridge, ordering withdrawal, or burning it.
- Cutting the banner rope, silencing the horn, offering credible quarter, or
  reaching the supply wagons changes the fight without attacking the captain.

### Beast: the scarred cliff-lion

**Primary engine:** hunt cadence.

- At high Strength roll D10 on its attack table.
- Result 1 is `WITHDRAW AND GATHER`: it bounds to a visible ledge and gains +3
  Base Dice on its next pounce.
- At half Strength use D8; the long bounding attacks vanish from the table.
- At one quarter Strength use D6; it guards its injured foreleg, snaps, shoves,
  and seeks a route to its den.
- Destroying ledges, reaching cover, threatening the den, or leaving its
  territory changes its choice of prey.

### Monster: the kiln-backed pilgrim

**Primary engine:** destructible furnace anatomy.

- Phase one has Armor Rating 8. Its back kiln primes a NEAR cone of ash one
  round before release.
- The kiln has Strength 3 and can be targeted from behind. Breaking it cancels
  the primed attack and reduces armor to 5.
- Phase two is faster and uses exposed iron limbs; it loses ash attacks but can
  feed from any open flame to regain one Strength instead of attacking.
- Extinguishing the shrine furnaces denies healing but plunges the site into
  darkness.

### Demon: the guest beneath the oathstone

**Primary engine:** partial manifestation through three promises.

- Each intact oathstone lets the demon use one group of results: possession,
  fear, or bodily violence.
- Breaking a stone removes those results but releases the named oath's social
  consequence into the settlement.
- At half Strength the demon manifests fully: ordinary weapons can harm it, but
  its D12 table becomes unstable and results 11-12 can strike demon and
  adventurers alike.
- Speaking its accepted name during a telegraphed possession attempt interrupts
  the attack, but reveals who in the settlement taught the name.

## Balance Budgets

Budget the whole round, not each rule in isolation.

### Threat budget

Count a feature as major if it does one of the following:

- grants another full attack
- threatens three or more targets with serious damage
- denies a meaningful turn
- bypasses armor or ordinary defense
- restores several Strength
- prevents ordinary damage
- changes several zones at once

A normal boss turn should contain one major feature or two moderate features.
Do not stack three major features in one resolution.

### Information discount

A telegraph does not make unlimited power fair. It permits a stronger effect
only when players have practical answers. If avoiding the attack requires an
action, abandoning an objective, or exposing an ally, the telegraph has already
created pressure before damage occurs.

### Phase budget

Two substantial phases are enough for most set pieces. Three phases require a
short first or final phase. Do not restore the boss to full Strength at every
transition. Prefer changing defenses, attack access, position, or objectives.

### Control budget

No single character should routinely lose more than one meaningful turn. If a
victim is swallowed, possessed, pinned, or removed from the main battlefield,
give that player decisions inside the state and give allies rescue options.

### Bookkeeping budget

For one boss, track at most:

- one phase marker
- one shared token type
- three targetable parts or anchors
- one persistent battlefield clock

Use fewer when troops, hazards, or several allied monsters are also active.

## Failure Modes

### The cinematic interruption

The boss becomes invulnerable and acts while players watch. Replace it with a
short transition at the end of a segment and preserve legal player action.

### The secret wipe

The boss releases a lethal effect with no warning. Add intent, environmental
signs, a weaker first occurrence, or lore that teaches the pattern.

### The punishment menu

Every player response triggers a counter. Keep one reaction and let successful
counterplay succeed.

### The health-bar reset

Each phase restores full Strength. Use one total Strength track, a small bounded
recovery, or separate vulnerable parts. Length alone is not depth.

### The false choice

The telegraph points to cover, but the attack destroys all cover or follows the
target without cost. Honor the stated geometry and dependencies.

### The wounded supercomputer

An injured animal or collapsing construct continues using every complex attack
at full efficiency. Use degradation, exposure, or changed behavior when the
fiction demands it.

### The low-roll dead turn

A setup result does nothing and creates no immediate decision. Move the enemy,
mark intent, expose a source, alter position, or create a clear next-round
threat. The absence of damage should still change play.

## Construction And Audit Procedure

1. Write one boss identity and one phase question.
2. Choose one phase architecture.
3. Decide whether the normal D6 table, a strength-band die, or selected attacks
   best expresses the change.
4. Write the strongest effect first, then its tell, enabling condition,
   interrupt, and cost.
5. Add one damage-state model.
6. Add no more than one reaction.
7. Give each part or anchor one clear mechanical job.
8. Simulate three rounds at high Strength and three at low Strength.
9. Check whether melee, ranged, social, lore, movement, and support-focused
   characters each have at least one meaningful contribution.
10. Remove any rule whose only function is extending combat length.

Approve the design only if:

- each phase changes decisions rather than only numbers
- the strongest attack is warned and answerable
- setup results spend real tempo
- current Strength or destroyed anatomy visibly changes available behavior
- a failed interrupt worsens the situation without automatically ending it
- the enemy retains a motive to flee, bargain, feed, or complete an objective
- the GM can run the state from the statblock and a few tokens
