<!-- markdownlint-disable MD013 -->

# New Rules Repository

## Contents

1. Purpose
2. How To Use This Repository
3. Design Boundary
4. Rule Entry Format
5. Repository Entries
6. Productive Pairings
7. Dangerous Pairings
8. Recommendation

## Purpose

This file is a repository of new monster-facing rule ideas that can be introduced in future bestiary entries.

Its purpose is to increase design-space flexibility, not raw power.

A new rule belongs here when it helps a monster do one of the following:

- create a different hunt pattern
- express a body type not yet fully covered
- make a lair or battlefield matter more
- create a clearer progression through the fight
- make a monster feel unfamiliar without becoming unreadable

This is not a dumping ground for stronger attacks.
It is a controlled shelf of mechanics that can make future monsters feel new.

## How To Use This Repository

When creating a new monster:

1. Start with the normal bestiary engine in `monster-design-engine.md`.
2. Check `monster-mechanics-taxonomy.md` to confirm whether the effect you want already exists in the current corpus.
3. Only come here if the monster still needs one additional mechanic to express its identity.
4. Use at most one repository rule on most monsters.
5. Use two only for major set-piece monsters, and only if the combination remains easy to run.

A repository rule should appear in the statblock exactly like any other special line:

- `PASSIVE`
- `SPECIAL DEFENSE`
- `SPECIAL WEAKNESS`
- `REGENERATE`
- or another short uppercase statblock label that already fits the manuscript

The rule should never read like a mini-subsystem chapter pasted into a monster.

## Design Boundary

Every rule in this repository must obey four limits.

### 1. Flexibility over power

The rule should open a new behavior pattern, not simply increase damage output or action economy.

### 2. One clear counterplay path

If a rule is unusual, the players must have a way to interrupt, exploit, outmaneuver, or learn it.

### 3. Concrete embodiment

The rule must arise from:

- a body
- a curse
- a hunger
- a lair
- a ritual condition
- a visible or inferable monster-state

### 4. Table usability

The GM should be able to run the rule from the statblock without needing a second worksheet.

## Rule Entry Format

Each rule entry in this repository includes:

- **Design job** — what problem the rule solves
- **Statblock form** — how it should appear inside a monster entry
- **Use when** — what kinds of monsters it fits
- **Counterplay** — how players can meaningfully respond
- **Warnings** — where the rule can go wrong

## Repository Entries

### WIND-UP

**Design job:**
Telegraph an apex attack one round early so the players respond before it lands.

**Statblock form:**
`WIND-UP:` The monster begins preparing a named attack. State the target or area now. The attack resolves at the start of the monster's next initiative unless the listed interruption condition occurs first.

**Use when:**

- the monster is huge
- the attack should feel inevitable unless disrupted
- the fight benefits from visible danger rather than surprise punishment

**Counterplay:**

- force the monster prone
- move the monster
- leave the marked area
- strike a weak point
- destroy an anchor sustaining the attack

**Warnings:**

- do not pair with excessive extra initiatives
- do not give several wind-up attacks to an ordinary monster
- interruption conditions must be concrete, not vague

### BREAKABLE

**Design job:**
Model armor, shell, bark, or ritual plating that visibly fails during the fight.

**Statblock form:**
`BREAKABLE:` The monster begins with a listed number of plates, scales, or shell segments. Each grants Armor Rating or another narrow defensive benefit. When the listed trigger occurs, one segment breaks.

**Use when:**

- the monster should feel heavily armored but not static
- you want progress to be visible before the kill
- tool choice should matter

**Counterplay:**

- land a heavy enough blow
- hit the weak seam
- use the material or element that cracks the armor fastest

**Warnings:**

- keep the segment count low
- do not combine with strong regeneration unless the weakness is very clear
- do not turn this into hit-point multiplication by another name

### ANCHOR CLUSTER

**Design job:**
Extend egg, phylactery, lesser-eye, and host logic into multi-point monster structures.

**Statblock form:**
`ANCHOR CLUSTER:` The monster has 2-4 linked anchors. Each intact anchor sustains one listed passive, attack bonus, or survival property. Anchors may be targeted separately.

**Use when:**

- the monster is brood-based
- the monster is shrine-bound
- the monster has several body nodes or external growths that matter
- the fight should progress by selective disablement

**Counterplay:**

- destroy or sever anchors
- divide party attention between body and anchors
- force the monster away from its anchors if the concept allows it

**Warnings:**

- each anchor should do one job only
- avoid more than four anchors
- do not require a table of sub-phases to run it

### SITE TRIGGERS

**Design job:**
Make a monster's lair or native terrain mechanically important without giving it extra turns.

**Statblock form:**
`SITE TRIGGERS:` In a named environment, the GM may replace a rolled monster attack with one listed site attack or site effect once per round.

**Use when:**

- the monster belongs to a well, bog, hive, cliff arch, crypt, or flooded ruin
- the place should matter as much as the body
- luring the monster out should be a valid tactic

**Counterplay:**

- leave the native site
- force the monster away from its trigger zone
- deny access to the terrain feature enabling the trigger

**Warnings:**

- site triggers replace attacks; they do not grant extra attacks
- keep the number of site triggers low
- a site trigger should feel like the place acting through the monster

### FEED

**Design job:**
Let a monster recover or sharpen itself by feeding on the newly fallen.

**Statblock form:**
`FEED:` When a living creature within a listed range becomes Broken, or when a fresh corpse is within reach, the monster may take a listed action to restore Strength or empower one named attack.

**Use when:**

- the monster is a corpse-eater
- the monster drinks fear, blood, or breath from the dying
- recovery should depend on battlefield events, not passive regeneration alone

**Counterplay:**

- drag bodies away
- deny the monster access to the Broken
- interrupt the feeding action
- choose retreat rather than becoming a food source inside its range

**Warnings:**

- keep the reward simple
- do not allow automatic feeding from every damage event
- do not stack heavy regeneration and heavy feeding on ordinary monsters

### MARK PREY

**Design job:**
Let a predator shape the fight around one victim without using a pile of penalties.

**Statblock form:**
`MARK PREY:` On a listed trigger, one victim is marked until a clear end condition. While marked, the monster gains one narrow hunting privilege against that victim.

**Use when:**

- the monster hunts by scent, blood, slime, eye contact, or terror
- the fight should feel like pursuit rather than random target selection
- one victim should suddenly become the center of danger

**Counterplay:**

- wash away or remove the mark
- break line of scent or sight
- force the monster to choose between the marked prey and immediate bodily danger

**Warnings:**

- usually only one marked victim at a time
- the privilege should be narrow
- avoid turning the mark into a whole secondary condition track

### SHED

**Design job:**
Let a monster discard one state, layer, or restraint by leaving part of itself behind.

**Statblock form:**
`SHED:` Once per fight, the monster may tear free of one restraint, grapple, or penalty by leaving behind skin, bark, membrane, antler velvet, or another named body layer.

**Use when:**

- the body naturally molts, sloughs, peels, cracks, or tears loose
- the creature should feel hard to pin down in a very physical way
- you want a surprise escape that still has visible cost

**Counterplay:**

- exploit the exposed softer body afterward
- treat the shed layer as a temporary clue, trophy, or weakness reveal
- punish the monster during or immediately after shedding if the fiction allows it

**Warnings:**

- once per fight is usually enough
- the shed should cost the monster something visible, such as lost Armor Rating or loss of a specific attack

### LATCHED TERROR

**Design job:**
Create monsters whose fear attacks intensify once they have established a psychological grip.

**Statblock form:**
`LATCHED TERROR:` If the monster's fear attack succeeds against a victim, one named follow-up attack gains a narrow bonus against that victim until the end of the next round.

**Use when:**

- the monster feeds on panic
- the creature hunts the shaken rather than the merely wounded
- the monster should feel like it closes once morale breaks

**Counterplay:**

- break line of sight
- remove distance pressure
- protect or reposition the affected victim before the follow-up lands

**Warnings:**

- keep the bonus narrow and short-lived
- do not stack multiple escalating fear bonuses on the same victim

### LAIR HUNGER

**Design job:**
Give the monster one behavior that only matters if the fight drags on inside its own territory.

**Statblock form:**
`LAIR HUNGER:` At the end of round three and each round after, if the monster remains in its native lair condition, one listed effect occurs.

**Use when:**

- the lair should become more dangerous over time
- the players should feel pressure to act decisively or retreat
- the monster's home gradually closes around intruders

**Counterplay:**

- leave the lair zone
- break the environmental condition sustaining the hunger
- shorten the fight instead of trading attrition

**Warnings:**

- use only on centerpiece encounters
- keep the end-of-round effect brief and concrete
- never let this become passive inevitability with no exit path

## Productive Pairings

These combinations tend to create new behavior without bloating the fight.

- `WIND-UP` + called-shot weakness
- `BREAKABLE` + heavy weapon ecology
- `ANCHOR CLUSTER` + `SITE TRIGGERS`
- `FEED` + fear-based predator or corpse-eater
- `MARK PREY` + ambush or darkness hunter
- `SHED` + `BREAKABLE` on a molting or skin-sloughing monster
- `LAIR HUNGER` + `SITE TRIGGERS` on a major lair boss

## Dangerous Pairings

These combinations are the most likely to become oppressive or cumbersome.

- `BREAKABLE` + strong regeneration + no clear weakness
- `ANCHOR CLUSTER` + several extra actions
- `SITE TRIGGERS` + full extra attack every round
- `FEED` + automatic healing from any damaged target
- `MARK PREY` + several stacked penalties
- `WIND-UP` + repeated no-dodge area attacks on a non-boss monster
- `LAIR HUNGER` + no practical way to leave the site

## Recommendation

Treat this file as a living repository of candidate bestiary-side rules.

A monster should usually borrow one idea from here, not several.
The aim is to widen the game's monster language so players encounter new forms of danger, new hunt patterns, and new lair behaviors.

The aim is not to make each new monster stronger than the last one.

The right test is simple:

- Does the rule make the monster feel new?
- Does it still feel like Forbidden Lands?
- Can the players understand and answer it in play?
- Would the rule still be worth using if it added no raw damage at all?

If the answer to the last question is yes, the rule probably belongs here.
