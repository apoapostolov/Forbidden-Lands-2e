<!-- markdownlint-disable MD013 -->

# New Rules Repository

## Contents

1. Purpose
2. How To Use This Repository
3. Design Boundary
4. Rule Entry Format
5. Repository Entries
   1. Telegraph And Tempo
   2. Body, Hunger, And Decay
   3. Territory, Site, And Weather
   4. Brood, Corpses, And Linked Structures
   5. Curse, Identity, And Knowledge
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

This repository contains compact rules for individual entries. When the design
needs an encounter architecture rather than one special line, use the dedicated
modules instead:

- `tactical-adversary-architecture.md` for roles, objectives, position, and
  category-specific behavior
- `boss-phases-intent-and-attrition.md` for phase changes, linked attack-table
  states, telegraphs, multi-round power, reactions, and degrading attack tables
- `minions-troops-and-command.md` for force scale, formations, orders, morale,
  and mass attacks

Do not import both a full architecture and several unrelated repository rules.
Treat the architecture as the monster's primary experimental rule.

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

These entries are intentionally broader than the first repository pass.
They are meant to widen the monster design space into hunt logic,
territory law, body-state shifts, inherited curse behavior, and linked
encounter structures that still feel native to Forbidden Lands.

### Telegraph And Tempo

#### WIND-UP

**Design job:** Telegraph an apex action one round early so danger can be answered, not merely suffered.

**Statblock form:** `WIND-UP:` Name the attack, area, or target now. The effect resolves on the monster's next initiative unless the listed interruption occurs.

**Use when:** the monster is huge, ritualized, slow to commit, or should feel inevitable before it lands.

**Counterplay / warnings:** Give one clear interruption path. Do not stack several wind-ups on a normal monster.

#### TABLE SHIFT

**Design job:** Let an attack change the state that supplies the monster's next
attack, creating a stance, heat, locomotion, appetite, or manifestation cycle.

**Statblock form:** End the triggering result with `After resolving this attack,
move to Table B: [State].` Resolve the next attack from that table. Results on
the destination table may remain there or move to any other named table.

**Use when:** the monster's own actions materially change its body, permission,
defense, behavior, or available counterplay.

**Counterplay / warnings:** Mark the active table visibly. A transition grants
no extra attack. Use the full procedure in
`boss-phases-intent-and-attrition.md`; do not create several cosmetic tables or
claim random transition odds while selecting results freely.

#### FALSE KILL

**Design job:** Let a monster appear dead or spent before revealing a second, weaker, or altered phase.

**Statblock form:** `FALSE KILL:` The first time the monster is Broken, it instead collapses, molts, stiffens, or goes still. If the listed finishing condition is not met, it rises again at the start of the next round with the listed reduced profile.

**Use when:** the creature is corpse-cunning, cursed, insect-like, burial-bound, or remembered in folklore as "dead until handled right."

**Counterplay / warnings:** The finishing condition must be inferable from lore, anatomy, or custom. Do not turn this into a full second boss fight.

#### PERCH SHIFT

**Design job:** Make flying, climbing, or ambush predators feel three-dimensional without granting extra full turns.

**Statblock form:** `PERCH SHIFT:` After a named attack or missed attack, the monster may move immediately to one listed perch, branch, ledge, roofline, or wall hold within range.

**Use when:** the monster hunts from rafters, cliffs, dead trees, bell towers, or cavern ribs.

**Counterplay / warnings:** The usable perches must be visible and limited. Destroying or abandoning them should matter.

#### LINEBREAKER

**Design job:** Make heavy beasts and cavalry-like horrors punish tight formations.

**Statblock form:** `LINEBREAKER:` If the monster hits a target with a named shove, rush, or slam, one additional victim directly behind or beside the first suffers a listed effect.

**Use when:** the monster is built to charge, sweep, shoulder through doors, or trample through shield walls.

**Counterplay / warnings:** This should punish clustering, not create full area spam every round.

#### PACK RESPONSE

**Design job:** Give pack predators coordinated pressure without adding a separate pack subsystem.

**Statblock form:** `PACK RESPONSE:` When a victim escapes, stands, or flees a named attack, one allied beast within the listed range may immediately reposition or use one named follow-up attack.

**Use when:** the monster is written as hunting in twos, threes, or family packs.

**Counterplay / warnings:** Restrict this to a single follow-up and keep the pack size small enough to run cleanly.

#### BURROW WINDOW

**Design job:** Make a tunneling or surfacing creature vulnerable only in brief physical moments.

**Statblock form:** `BURROW WINDOW:` The monster may only be struck normally when surfacing, breaching, or anchoring itself to attack. Otherwise, attacks suffer the listed penalty or fail outright.

**Use when:** the monster lives under peat, scree, ice, dune, ash, or grave-loam.

**Counterplay / warnings:** The breach moment must happen regularly enough that the fight remains interactive.

### Body, Hunger, And Decay

#### BREAKABLE

**Design job:** Model shell, bark, plate, stone skin, or ritual armor that visibly fails during the fight.

**Statblock form:** `BREAKABLE:` The monster begins with a listed number of plates, scales, or hard segments. Each broken segment removes one listed protection.

**Use when:** the creature should feel armored but progressively exposed.

**Counterplay / warnings:** Keep the segment count low and the break triggers concrete.

#### FEED

**Design job:** Let a monster recover or sharpen itself by feeding on the newly fallen.

**Statblock form:** `FEED:` When a victim becomes Broken or a fresh corpse lies within reach, the monster may spend its next action to restore Strength or empower one named attack.

**Use when:** the creature drinks blood, breath, marrow, fear, or bodily heat.

**Counterplay / warnings:** Bodies must be removable. Feeding should cost tempo.

#### SHED

**Design job:** Let the monster escape one restraint or state by tearing free of a body layer.

**Statblock form:** `SHED:` Once per fight, the monster may discard a named outer layer to end one listed condition or restraint.

**Use when:** the creature molts, peels, sloughs, tears bark, or leaves hide behind.

**Counterplay / warnings:** The new exposed state should lose armor, change attacks, or reveal a weakness.

#### BLOOD SCENT

**Design job:** Make injured prey progressively less safe from pursuit.

**Statblock form:** `BLOOD SCENT:` The monster gains one listed benefit against any victim who has taken Strength damage or is bleeding from a named attack.

**Use when:** the creature hunts by smell, heat, spoor, or opened flesh.

**Counterplay / warnings:** Washing, cauterizing, mud-covering, or breaking line should be valid counterplay if the concept allows.

#### DRAG BELOW

**Design job:** Turn water, mud, ash, snow, or peat into the true killing surface.

**Statblock form:** `DRAG BELOW:` On a named hit or failed roll, the victim is pulled into the listed terrain state and suffers ongoing penalties or damage until freed.

**Use when:** the monster kills by immersion, suffocation, suction, or concealment rather than sheer blows.

**Counterplay / warnings:** Provide a rescue method and keep the terrain state easy to remember.

#### MOLT FRENZY

**Design job:** Create a visible shift from protected stage to violent exposed stage.

**Statblock form:** `MOLT FRENZY:` When the monster loses its final plate, shell, or skin layer, it immediately gains one listed offensive benefit and one listed defensive loss.

**Use when:** the creature becomes more dangerous precisely when it is finally opened.

**Counterplay / warnings:** The frenzy must feel risky, not just stronger in every direction.

#### FLESH ARMOR

**Design job:** Let a carrion monster build temporary protection out of what it has just eaten or plastered onto itself.

**Statblock form:** `FLESH ARMOR:` After feeding or entering a named body pile, the monster gains temporary Armor Rating or one narrow resistance until the layer is burned, hacked off, or worn away.

**Use when:** the creature hides in gore, packed mud, grave wrappings, or clotted hide.

**Counterplay / warnings:** The armor source must be visible and removable.

### Territory, Site, And Weather

#### SITE TRIGGERS

**Design job:** Make a monster's lair or native terrain mechanically important without giving it extra turns.

**Statblock form:** `SITE TRIGGERS:` In a named environment, the GM may replace one rolled attack each round with one listed site effect.

**Use when:** the creature belongs to a well, bog, crypt, cliff arch, hive, or flooded ruin.

**Counterplay / warnings:** Site triggers replace attacks. They do not create a second attack routine.

#### LAIR HUNGER

**Design job:** Give the monster one behavior that only matters if the fight drags on inside its own territory.

**Statblock form:** `LAIR HUNGER:` At the end of round three and each round after, if the monster remains in its native condition, one listed effect occurs.

**Use when:** the place itself should become progressively worse.

**Counterplay / warnings:** Best for centerpiece monsters with a clear way to break or leave the condition.

#### TERRITORIAL LINE

**Design job:** Turn invisible borders, scent marks, cairn lines, or root circles into meaningful map features.

**Statblock form:** `TERRITORIAL LINE:` When a victim crosses the named boundary, the monster gains one immediate listed privilege against that victim.

**Use when:** the creature defines a den, shrine perimeter, cliff edge, burial ring, or ford boundary.

**Counterplay / warnings:** The line should be observable by sign, not purely secret GM geometry.

#### SINKING GROUND

**Design job:** Make the battlefield physically degrade the longer the monster controls it.

**Statblock form:** `SINKING GROUND:` At the end of each round in a named site, one additional zone becomes deep mud, rotten boards, loose scree, thin ice, or similar bad footing.

**Use when:** the monster reshapes soft or unstable ground around itself.

**Counterplay / warnings:** Keep the map effect small, progressive, and easy to mark.

#### THRESHOLD BOUND

**Design job:** Give a monster old-world restrictions around hearths, holy rings, grave lines, oaths, or marked doors.

**Statblock form:** `THRESHOLD BOUND:` The monster cannot cross the named threshold type unless the listed condition is broken, invited, or profaned.

**Use when:** the creature is folkloric, cursed, domestic-haunting, burial-bound, or shrine-sensitive.

**Counterplay / warnings:** The threshold must exist in the fiction often enough to matter, but not so often that it trivializes the monster.

#### HUNGER WEATHER

**Design job:** Tie the monster's strength to weather that people in the world fear and track.

**Statblock form:** `HUNGER WEATHER:` During rain, thaw mist, hard frost, thunder, high wind, or another named condition, the monster gains one listed benefit.

**Use when:** the creature is inseparable from season, storm, or bad road weather.

**Counterplay / warnings:** The weather bonus should alter behavior, not simply inflate every number.

#### SALT-SHUN

**Design job:** Build a simple but material warding rule around salt, ash, lime, grave dust, or another common survival substance.

**Statblock form:** `SALT-SHUN:` The monster will not willingly cross a fresh line or circle of the named substance unless it first suffers the listed trigger or the ward is broken.

**Use when:** the creature belongs to the grave, damp, witch-lore, or corruption.

**Counterplay / warnings:** The ward should slow, redirect, or buy time, not solve the encounter alone.

### Brood, Corpses, And Linked Structures

#### ANCHOR CLUSTER

**Design job:** Extend egg, phylactery, lesser-eye, and host logic into multi-point monster structures.

**Statblock form:** `ANCHOR CLUSTER:` The monster has 2-4 linked anchors. Each intact anchor sustains one listed passive, attack, or survival property.

**Use when:** the creature is brood-based, shrine-bound, or spread across several vulnerable nodes.

**Counterplay / warnings:** Each anchor should do one job only.

#### NEST CLOCK

**Design job:** Put pressure on the party through hatching, awakening, flooding, or ripening rather than raw damage.

**Statblock form:** `NEST CLOCK:` At the end of each round after the listed trigger, advance the brood clock one step. At each step, one named complication occurs.

**Use when:** eggs, cocoons, pods, graves, sealed urns, or root bulbs matter.

**Counterplay / warnings:** Keep the clock short, usually three steps.

#### CARRION CALL

**Design job:** Make the dead attract additional trouble without turning the fight into endless summons.

**Statblock form:** `CARRION CALL:` When a creature dies in the listed range, one named scavenger, swarm, or lesser effect appears at the start of the next round unless the corpse is burned, lifted, or sanctified.

**Use when:** the monster's ecology involves scavengers, grubs, corpse-birds, or grave vermin.

**Counterplay / warnings:** Use small support threats only. This is pressure, not a full army engine.

#### BROOD SACRIFICE

**Design job:** Let a parent, hive queen, or curse-nest spend part of its own future to survive the present round.

**Statblock form:** `BROOD SACRIFICE:` The monster may destroy one egg, larva, host, or lesser spawn it controls to trigger one listed effect.

**Use when:** the creature is ruthless, reproductive, priest-queen-like, or sustained by living reserves.

**Counterplay / warnings:** The sacrifice must permanently cost the monster something.

#### CORPSE LIGHT

**Design job:** Turn the dead around the monster into omen, lure, or battlefield information.

**Statblock form:** `CORPSE LIGHT:` Corpses within the listed range begin to glow, whisper, sway, leak light, or point, granting the monster one narrow sensing or targeting benefit.

**Use when:** the monster is marsh-born, grave-fed, drowned, or spirit-touched.

**Counterplay / warnings:** Smothering, covering, turning, or sanctifying corpses should break the effect.

#### BONE PILE

**Design job:** Let a lair's remains act like stored terrain power.

**Statblock form:** `BONE PILE:` While within the listed range of an intact bone heap, pyre stack, skull wall, or ossuary floor, the monster gains one named benefit.

**Use when:** the creature nests in accumulated dead and has shaped the site over years.

**Counterplay / warnings:** The pile must be breakable, burnable, or avoidable.

### Curse, Identity, And Knowledge

#### MARK PREY

**Design job:** Let a predator shape the fight around one victim without using a pile of penalties.

**Statblock form:** `MARK PREY:` On a listed trigger, one victim is marked until a clear end condition. While marked, the monster gains one narrow hunting privilege against that victim.

**Use when:** the creature hunts by scent, blood, eye contact, slime, omen, or spoken name.

**Counterplay / warnings:** Usually keep one marked victim at a time.

#### LATCHED TERROR

**Design job:** Create monsters whose fear attacks intensify once they establish psychological grip.

**Statblock form:** `LATCHED TERROR:` If the monster's fear attack succeeds, one named follow-up attack gains a narrow bonus or rider against that victim until the end of the next round.

**Use when:** the creature hunts the shaken rather than the merely wounded.

**Counterplay / warnings:** Keep the bonus brief and specific.

#### CURSE ECHO

**Design job:** Make repeated contact with the same monster feel progressively worse without a heavy tracking ladder.

**Statblock form:** `CURSE ECHO:` If the same victim suffers the named effect again before dawn or before leaving the site, replace it with the stronger listed version.

**Use when:** the monster's harm is cumulative, haunting, or remembered by the body.

**Counterplay / warnings:** Usually use only two tiers.

#### STOLEN SHAPE

**Design job:** Let a monster wear a borrowed face, voice, or posture in a way that matters mechanically.

**Statblock form:** `STOLEN SHAPE:` After killing, kissing, drowning, or skinning a victim, the monster may imitate one listed outward trait until the disguise is broken by the listed condition.

**Use when:** the creature is a mimic, changeling, night-haunter, or skin-thief.

**Counterplay / warnings:** This should create suspicion, entry, or delay, not perfect omnipotent infiltration.

#### DEVOUR MEMORY

**Design job:** Attack knowledge, route memory, or social certainty instead of only flesh.

**Statblock form:** `DEVOUR MEMORY:` On a successful named attack, the victim forgets one narrow category until dawn, until ritual recovery, or until the monster is slain.

**Use when:** the monster feeds on names, roads, prayers, kin-faces, or burial knowledge.

**Counterplay / warnings:** Keep the forgotten category concrete and playable.

#### PAIN MIRROR

**Design job:** Make harming the monster dangerous until its hidden bond is exposed.

**Statblock form:** `PAIN MIRROR:` When the monster suffers damage, the attacker or bound victim suffers the listed lesser effect unless the mirror condition has first been broken.

**Use when:** the creature is tied to a hostage, twin-body, rune shell, or cursed vessel.

**Counterplay / warnings:** The bond must be discoverable. Never hide it completely from lore or scene clues.

#### RUNE INTERRUPT

**Design job:** Let a visible inscription, chant, knot, bell, or carved token sustain part of the monster's power.

**Statblock form:** `RUNE INTERRUPT:` One named passive or attack stops working if the listed mark, object, chant, or pattern is broken.

**Use when:** the monster is ritually sustained, dwarven-made, witch-bound, or shrine-fed.

**Counterplay / warnings:** The sustaining element should be visible enough to target or infer.

#### SILENCE FIELD

**Design job:** Make speech, prayer, command, or spell-language fail in a controlled area.

**Statblock form:** `SILENCE FIELD:` Within the listed range, speech carries poorly or not at all, and one named category of action suffers the listed restriction.

**Use when:** the creature is tied to burial hush, drowned depth, void, fog, or soul-pressure.

**Counterplay / warnings:** Keep the field local and specific. It should alter tactics, not cancel whole characters.

## Productive Pairings

These combinations tend to create new behavior without bloating the fight.

- `WIND-UP` + called-shot weakness
- `TABLE SHIFT` + `WIND-UP`
- `TABLE SHIFT` + `BREAKABLE`
- `FALSE KILL` + `RUNE INTERRUPT`
- `BREAKABLE` + heavy weapon ecology
- `SHED` + `MOLT FRENZY`
- `FEED` + `BLOOD SCENT`
- `SITE TRIGGERS` + `TERRITORIAL LINE`
- `LAIR HUNGER` + `SINKING GROUND`
- `ANCHOR CLUSTER` + `NEST CLOCK`
- `BROOD SACRIFICE` + `NEST CLOCK`
- `MARK PREY` + `PACK RESPONSE`
- `LATCHED TERROR` + `MARK PREY`
- `PAIN MIRROR` + `RUNE INTERRUPT`
- `THRESHOLD BOUND` + `SALT-SHUN`

## Dangerous Pairings

These combinations are the most likely to become oppressive or cumbersome.

- `BREAKABLE` + strong regeneration + no clear weakness
- `ANCHOR CLUSTER` + several extra actions
- `SITE TRIGGERS` + full extra attack every round
- `FEED` + automatic healing from any damaged target
- `MARK PREY` + several stacked penalties
- `WIND-UP` + repeated no-dodge area attacks on a non-boss monster
- `LAIR HUNGER` + no practical way to leave the site
- `FALSE KILL` + `REGENERATE` + hidden finishing condition
- `PACK RESPONSE` + too many bodies on the field
- `DEVOUR MEMORY` + crucial plot knowledge with no recovery path
- `SILENCE FIELD` + total magic negation across a large battlefield
- `PAIN MIRROR` + no discoverable bond clue

## Recommendation

Treat this file as a living repository of candidate bestiary-side rules.

A monster should usually borrow **one** idea from here.
Major monsters may borrow **two** if their interaction remains clean and discoverable.

The aim is to widen the game's monster language so players encounter:

- new hunt patterns
- new site pressures
- new body-state changes
- new curse structures
- new counterplay routes

The aim is not to make each new monster stronger than the last one.

The right test is simple:

- Does the rule make the monster feel new?
- Does it still feel like Forbidden Lands?
- Can the players understand and answer it in play?
- Would the rule still be worth using if it added no raw damage at all?

If the answer to the last question is yes, the rule probably belongs here.
