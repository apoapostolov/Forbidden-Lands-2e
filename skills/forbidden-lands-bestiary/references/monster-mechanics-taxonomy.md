<!-- markdownlint-disable MD013 -->

# Monster Mechanics Taxonomy

## Contents

1. Purpose
2. Scope
3. Reading The Taxonomy
4. Attack Delivery Classes
5. Targeting Patterns
6. Range And Scale Patterns
7. Damage Expressions
8. Condition And Special-Effect Catalog
9. Defense Catalog
10. Weakness And Counterplay Catalog
11. Structure Templates
12. Escalation Patterns
13. Design Use Rules
14. Quick Composition Matrix

## Purpose

This document catalogs the mechanical vocabulary already used by the Forbidden Lands 2E bestiary.

Use it when you need to answer questions such as:

- what kinds of monster attacks already exist in the corpus
- which riders feel common, rare, or apex-only
- how control, poison, fear, and environmental pressure are normally expressed
- what defense packages the game already supports
- what kind of weakness language feels native to the engine

This is the fast-reference companion to `monster-design-engine.md`.

The design engine explains the logic.
This taxonomy lists the parts.

## Scope

The taxonomy covers mechanics drawn from the combined bestiary corpus in:

- `02-gamemasters-guide/06-bestiary.md`
- `03-book-of-beasts/02-bestiary.md`

It covers:

- attack delivery methods
- target selection logic
- range bands
- damage expressions
- conditions and special effects
- defenses and vulnerabilities
- structural templates for monster families

It does not cover:

- encounter-writing logic
- RESOURCES formatting rules
- voice or prose style

## Reading The Taxonomy

Each category below should be read as a design bucket, not a rigid law.

A single monster often uses several buckets together.

For example:

- a dragon uses direct strikes, a sweep, a fear attack, and a called-shot weakness
- a bog undead may combine partial immateriality, fear, drowning, and COLD
- a swarm may combine capped incoming damage, broad-area attacks, and armor degradation

The important question is not whether a monster uses multiple buckets.
The important question is whether those buckets all point at the same body, curse, hunger, or hunting logic.

## Attack Delivery Classes

### 1. Direct strike

The baseline physical attack.

**Form:**

- one target
- attack roll
- Weapon Damage 1 or 2
- often blunt, slash, or stab damage

**Typical use:**

- claws
- bite
- slam
- fist
- horn
- wing or tail strike

**Examples:**

- Gray Bear `PAW STRIKE!`
- Greater Golem `CRUSHING ATTACK!`
- Iron Dragon `TAIL ATTACK!`
- Air Spirit `WIND SLAM!`

### 2. Multi-target sweep

One bodily motion threatens several adventurers at once.

**Form:**

- all adventurers within NEAR range, sometimes two targets
- moderate Base Dice
- often Weapon Damage 1
- riders are common

**Typical use:**

- tail sweep
- wing buffet
- body slam
- trunk or root sweep
- swarm mass attack

**Examples:**

- Dragon `TAIL ATTACK!`
- Ent `SWEEPING BLOW!`
- Manticore `SWEEPING ATTACK!`
- Swarming Death `BROAD MASS ATTACK!`

### 3. Projectile or emitted shot

The monster attacks at range with a body-grown or supernatural projectile.

**Form:**

- SHORT range is common, NEAR also appears
- attack roll against one target or many targets
- damage plus poison, paralysis, or acid is common

**Typical use:**

- spikes
- spit
- breath bolts
- thrown stones
- barbs

**Examples:**

- Manticore `TAIL SPIKE!`
- Amoeba `ACID SPIT!`
- Ent `ROCK THROW!`
- Air Spirit `SHARD OF SKY!`

### 4. Cloud, breath, or emanation

The monster projects a substance, force, or aura into an area.

**Form:**

- all targets within NEAR or SHORT range
- usually calls for MOVE or ENDURANCE, or directly applies poison, disease, or fear
- often cannot be DODGED when expressed as atmosphere rather than impact

**Typical use:**

- poison breath
- spore cloud
- dust blind
- smothering fog
- toxic spray
- shriek or roar as mass fear

**Examples:**

- Mummy `BREATH OF DEATH!`
- Mire Drake `TOXIC ATTACK!`
- Strangling Vine `POISONOUS CLOUD!`
- Possessor `SMOTHERING FOG!`

### 5. Touch, gaze, or directed curse

A non-weapon attack aimed at one victim.

**Form:**

- one target within ARM'S LENGTH, NEAR, or SHORT
- often bypasses normal physical logic
- usually inflicts fear, paralysis, poison, attribute loss, or magical effect

**Typical use:**

- death touch
- gaze attack
- telepathic compulsion
- petrification sequence
- dream assault

**Examples:**

- Death Magister `PARALYZING TOUCH!`
- Ghost `TOUCH OF DEATH!`
- Thought-Kraken `MIND LOCK!`
- Snake Queen passive gaze

### 6. Grapple-and-hold

The attack is valuable because it changes the target's state, not because of immediate damage.

**Form:**

- one target hit or failed evade
- target becomes GRAPPLED
- follow-up pressure occurs in later rounds or in later attacks

**Typical use:**

- tentacles
- roots
- jaws
- claws that pin rather than tear

**Examples:**

- Giant Squid `SLIMY TENTACLE!`
- Ent `GNARLY ROOTS!`
- Pale Ape `HOOKING ARM!`
- Thought-Kraken `GRASPING TENTACLES!`

### 7. Drag, drown, swallow, or engulf

The monster moves the victim into a lethal interior or environment.

**Form:**

- one target
- hit or failed MOVE
- repeated damage or drowning follows
- escape method may be BREAK FREE, cutting out, killing the monster, or surfacing

**Examples:**

- Drakewyrm `DEVOURING ATTACK!`
- Amoeba `ABSORBING ATTACK!`
- Bog Man `DROWNING ATTACK!`
- Amphibian drowning procedure

### 8. Fear assault

The bestiary's most common supernatural non-physical attack class.

**Form:**

- fear attack with explicit Base Dice or strength expression
- one target or everyone in a range band
- may add one clear rider such as COLD, prone, or a thematic follow-up

**Examples:**

- Bloodling `HORRIBLE MIST!`
- Bog Man `HATEFUL SHRIEK!`
- Dragon `DRAGON ROAR!`
- Thought-Kraken `LIFE DRAIN!`

### 9. Action-denial attack

The main point is to remove the victim's ability to act cleanly.

**Form:**

- ENDURANCE or MOVE failure, or successful special attack
- victim loses actions, speech, sight, or effective tempo

**Examples:**

- Amoeba `REEKING CLOUD!`
- Swarming Death `DISTRACTING ATTACK!`
- Imp `TONGUETWISTING ATTACK!`
- Mara nightmare attacks

### 10. Battlefield-state attack

The monster changes what the battlefield allows.

**Form:**

- alters visibility, air, food, armor value, magical functionality, or space safety
- often affects several adventurers at once

**Examples:**

- Star-Watcher anti-magic gaze
- Rat King `BEFOULING ATTACK!`
- Swarming Death armor-halving mass attack
- Possessor suffocating fog

### 11. Abstracted summon or invocation attack

The effect is described as calling spirits, dead, or cosmic force, but the mechanic remains a standard attack or fear attack.

**Design note:**

The books rarely create separate summoned statblocks inside monster attacks.
They usually abstract the event into one effect roll.

**Examples:**

- Mummy `UNHOLY SUMMONING!`
- several spirit and undead fear attacks framed as visions or summoned dead

## Targeting Patterns

The bestiary reuses a stable set of target-selection logics.

| Pattern | Typical Meaning | Examples |
| --- | --- | --- |
| chosen adventurer | the creature is intelligent, opportunistic, or tactically aware | many demons, dragons, kraken-like minds |
| nearest adventurer | brute instinct or immediate body priority | trolls and simple beasts |
| adventurer with highest Strength | predator chooses biggest prey or strongest body | drakewyrm, bloodling, mummy-like elites |
| adventurer with lowest Strength | sadistic or exploitative predator choosing the weak | bloodling throat bite |
| one GRAPPLED victim | combo finisher after a hold | Pale Ape, Rock-Hanger |
| everyone within NEAR | sweep, roar, poison cloud, telepathic pulse | dragons, swarms, specters |
| everyone within SHORT | larger-area projectile or swarm pressure | swarms, fogs, thought effects |
| all at ARM'S LENGTH | body-zone threat for close fighters | Snake Hair, crushing flurries |

### Design rule

Target-selection is part of monster personality.

- **highest Strength** implies predatory challenge or threat recognition
- **lowest Strength** implies cruelty or opportunism
- **nearest** implies brute instinct
- **all in range** implies scale, aura, or atmospheric threat
- **one GRAPPLED victim** implies an attack-chain monster

## Range And Scale Patterns

### Default rule

Monster attacks default to ARM'S LENGTH unless the text says otherwise.

### Common range bands

| Range | Typical Monster Use |
| --- | --- |
| ARM'S LENGTH | claws, bite, slam, hold, sting, eyes within reach |
| NEAR | roar, breath, spikes, mind pressure, roots, tentacles, mass sweeps |
| SHORT | spit, thrown victim, storm shard, swarm spread, telekinetic fling |
| LONG | very rare for attacks; more common for passives such as telepathy or detection |

### Scale markers

Range often signals the type of monster.

- **ARM'S LENGTH** suggests a bodily predator
- **NEAR** suggests a dominant local threat
- **SHORT** suggests spatial control or supernatural projection
- **LONG** is usually reserved for passives, detection, or setup effects rather than ordinary attack tables

## Damage Expressions

### Damage type catalog

The books rely on a small set of damage expressions.

| Damage Expression | Meaning |
| --- | --- |
| blunt force | impact, crush, slam, throw, fall, body mass |
| slash wound | claws, teeth, blades, ripping jaws, mandibles |
| stab wound | stings, spikes, tongues, barbs, puncture |
| non-typical damage | supernatural or internal body collapse that does not map neatly to a weapon form |
| direct attribute loss | poison, petrification gaze, disease, mental assault, or special passives |

### Ongoing damage packages

Recurring forms include:

- 1 damage every round while on fire
- 1 damage every round while swallowed or engulfed
- drowning or suffocation pressure each round
- passive regeneration for the monster itself
- repeated squeeze damage while GRAPPLED

### Damage conversion and modification

Common special expressions:

- half damage from some weapon classes
- no damage from some weapon classes
- double damage from an element or magic
- Armor Rating halved for a targeted weak spot or swarm seep attack
- incoming damage capped at 1 against a swarm body

## Condition And Special-Effect Catalog

This section lists the recurring outcomes monsters inflict.

### Core physical-control effects

| Effect | Normal Delivery | What It Does In Play | Common Examples |
| --- | --- | --- | --- |
| GRAPPLED | hit by hold, tentacle, roots, jaws | target loses freedom and often becomes setup for later harm | squid, ape, serpent, kraken |
| prone / thrown to ground | successful heavy hit or sweep | target loses position and tempo | dragon tail, giant smash, earth spirit strike |
| thrown to NEAR / SHORT | hit by slam, throw, tail, telekinetic force | breaks formation and follow-up plans | death knight, giant, golems |
| swallowed / engulfed | devour or absorb attack | target takes ongoing internal damage and faces altered escape rules | drakewyrm, amoeba |
| dragged underwater | drowning or bog attack | converts fight into drowning pressure | amphibians, bog man, sea creatures |

### Fear and mind-pressure effects

| Effect | Normal Delivery | Notes |
| --- | --- | --- |
| fear attack | roar, shriek, vision, telepathy, death aura | most common non-physical monster pressure |
| fear attack plus COLD | undead, ghostly, or death-linked entities | common undead pressure pattern across the corpus |
| fear attack plus prone | gaze or shock wave | body collapses under psychic force |
| fear attack plus command or compulsion | rare but present through special items or unique monsters | should stay exceptional |

### Poison and disease effects

| Effect | Delivery | Common Ratings | Examples |
| --- | --- | --- | --- |
| paralyzing poison | sting, spike, touch, cloud | Potency 6-10 | manticore, spider, death magister |
| lethal poison | spit, bite, toxic cloud, demonic secretion | Potency 7-10 | mire drake, basilisk, skolopendra |
| sleeping poison | spores, breath, bite, dream-linked attack | Potency 4-8 | mummy breath, basilisk lesser form, spiders |
| disease | bite, bile, filth, spores, plague wave | Virulence 6-9 | troll, bog hag, rat king, possessor |
| fungal or demonic infection | demonic contact or fog | Virulence 9 range common | possessor, bloodling lines |

### Tempo, perception, and speech effects

| Effect | Typical Delivery | Notes |
| --- | --- | --- |
| unable to act until next round point | nausea, distraction, nightmare, sensory overload | strong tempo theft without new subsystem |
| fights as in darkness | dust, blindness, soot, shadow | reduces effectiveness without inventing a new blinded track |
| unable to speak | tongue curse or dream effect | matters because speech and casting are socially and magically important |
| cannot do anything but scream | nightmare horror | severe but usually one-target and scene-shaped |
| magic quenching | anti-magic passive or gaze | rare, boss-grade, should stay rare |

### Bodily transformation and deterioration

| Effect | Typical Delivery | Notes |
| --- | --- | --- |
| COLD | undead fear, death touch, icy gaze | standard state marker in undead and winter-horror space |
| Agility loss toward petrification | gaze at start of rounds | used for basilisk/medusa-like pressure families |
| Empathy loss | poison, hagcraft, basilisk corruption | rare and should stay meaningful |
| Wits damage | special fear or magical aftermath | usually tied to powerful rare resources or mind assaults |
| hallucination / dream contamination | demon poison, mara smoke, memory mucus | often expressed through narrative fallout rather than a formal track |

### Supply and environment effects

| Effect | Typical Delivery | Notes |
| --- | --- | --- |
| FOOD contamination | plague mist, befouling demon or vermin attack | extends monster pressure into logistics and settlement strain |
| suffocation / drowning air | fog, smothering gas, underwater drag | still expressed with existing drowning rules |
| impassable patch or dangerous ground | acid, collapse, constriction field | usually short-duration and concrete |
| armor seep or armor halving | insect or corrosion logic | useful but should stay anatomically justified |
| gear damage amplification | earth, stone, or corrosive body logic | mostly defensive-side pressure |

## Defense Catalog

### 1. Plain Armor Rating

The simplest model.

**Use when:**

- the monster is physically durable in obvious ways
- it does not need a puzzle defense
- the fight should stay direct

### 2. Armor plus passive penalty

The monster is armored and awkward to target or hurt correctly.

**Examples:**

- missiles at penalty through an airy body
- attacks at penalty against a transparent or shifting form

### 3. Partial immunity

The monster still takes damage, but not equally from all sources.

**Sub-types:**

- half damage from physical weapons
- half damage from nonmagic weapons
- no damage from piercing or stabbing weapons
- normal damage only from magic, fire, copper, blessed iron, or similar keyed tools

### 4. Element-feeding defense

Instead of resisting an element, the monster heals from it.

**Examples:**

- acid-fed golem
- fire-fed golem

**Design use:**

- creates strong surprise
- rewards observation and lore
- should be signaled clearly enough that the table can learn it

### 5. Regeneration

The monster regains Strength each round or at end of round.

**Best paired with:**

- a known weakness
- a called shot
- a limited-duration vulnerability

### 6. Return-after-banishment

The creature is not permanently destroyed by ordinary combat.

**Examples:**

- ghosts
- maras and specters with purge conditions
- phylactery-bound undead

### 7. Anchor or host defense

The true defense lies outside the visible body.

**Examples:**

- basilisk egg
- host-dependent possessor
- phylactery-backed magister

### 8. Weak-point defense

The monster is durable until a precise body zone is targeted.

**Examples:**

- dragon scale gap
- iron dragon airway organs
- golem joints or eyes
- star-watcher lesser eyes
- giant scorpion eyes

### 9. Damage-cap body model

One attack cannot deal more than a limited amount.

**Examples:**

- swarm body capped at 1 damage per attack except for fire logic

### 10. Hidden or positional defense

The monster is vulnerable only when surfaced, exposed, or revealed.

**Examples:**

- Tunneler breach-only strikes
- Rock-Hanger stone camouflage
- buried or submerged ambush bodies

## Weakness And Counterplay Catalog

Weaknesses in Forbidden Lands are usually concrete.

### Material weaknesses

Common materials already in the engine include:

- copper
- silver
- gold
- wood
- blessed iron or holy-worked metals
- magic weapons

### Elemental weaknesses

Most common:

- fire
- cold
- bright light
- water
- soil contact

### Anatomical weaknesses

Most common forms:

- target the eyes
- target the joints
- target the airway or gill-like breathing organ
- strike the scale gap or seam
- sever or wound the tail to alter behavior

### Anchor weaknesses

The monster is tied to:

- an egg
- a phylactery
- a host
- a location or atmospheric seam
- a brood mass or corpse pile

### Social, symbolic, or taboo weaknesses

Mostly concentrated in demon-generation and deeply uncanny monsters.

Examples from demon tables and special monsters include aversion or damage from:

- holy symbols
- children
- elves or dwarves
- music
- sight of a taboo presence

These belong to the engine, but should be used carefully. They work best for demonic and folkloric entities rather than for every supernatural creature.

### Environmental weaknesses

Examples:

- sunlight on troll-like bodies
- strong light on mist-like bodies
- surfaced vulnerability for burrowers
- inability to function well on land or in open day

## Structure Templates

### Standard six-attack monster

**Use when:** one body, one threat identity, no need for procedural generation.

### No-monster-attacks creature

**Use when:** the creature is dangerous through weapons, numbers, role, or terrain rather than monster asymmetry.

### Humanoid band template

**Use when:** tactics, gear, and role matter more than supernatural mechanics.

### Variant ladder family

**Use when:** hatchling/adult/elder or caste variants should scale one concept across several encounter weights.

### Swarm entity

**Use when:** damage-cap logic, area pressure, and collective-body identity are central.

### Multi-part boss

**Use when:** sub-targets, lesser eyes, tail organs, or layered kill conditions matter.

### Site-bound horror

**Use when:** the place itself is part of the monster's identity and defense.

### Procedural monster generator

**Use when:** you need a family of unique monsters built from tables but still constrained by the same engine verbs.

## Escalation Patterns

These are the main native ways the bestiary increases monster danger.

### Safe escalation methods

- add a second initiative card
- broaden target count
- widen range from ARM'S LENGTH to NEAR or SHORT
- add a clear rider such as GRAPPLED, prone, poison, or fear
- upgrade Potency or Virulence by 1-2 steps
- add one discoverable weak point instead of raw immunity
- turn a successful hit into an ongoing loop
- let the battlefield become dangerous to remain in

### Higher-risk escalation methods

Use carefully.

- no-dodge attacks
- repeated area fear at high dice values
- host-jumping or reform mechanics
- attack-cap defenses plus area pressure
- multi-target grapple effects
- anti-magic passives

### Usually non-native escalation methods

Avoid unless there is overwhelming evidence.

- many triggered reactions per round
- multiple nested status tracks on one target
- passive damage auras plus strong area attacks plus high armor with no weakness
- free counterattacks after every miss
- spell-like lists of unrelated powers on one monster

## Design Use Rules

### Rule 1: riders should match anatomy

Do not add paralysis to a wing buffet unless the anatomy or curse explains it.

Good pairings:

- sting -> poison
- root or tentacle -> GRAPPLED
- roar or gaze -> fear
- engulfing slime -> suffocation, corrosion, absorption
- swarm seep -> armor degradation

### Rule 2: area attacks should usually be lighter per target

Area attacks usually trade peak damage for spatial pressure.

If an area attack also has high damage, it should normally:

- have a resist roll
- be limited-use
- be apex-tier
- or trade raw damage for fear, prone, poison, or another rider

### Rule 3: fear is the default psychic language

If the effect is horror, dread, despair, soul pressure, death-memory, prophecy, nightmare, or scale shock, start with a fear attack before inventing anything else.

### Rule 4: Potency and Virulence are precious design tools

Use them instead of bespoke toxin systems.

### Rule 5: the rarer the defense, the clearer the weakness

If the monster has:

- regeneration
- host-jumping
- element-feeding
- banishment-only survival
- anti-magic passives

then it should usually also have a clear investigative answer.

## Quick Composition Matrix

Use this as a starting template.

| Monster Goal | Recommended Core Package |
| --- | --- |
| Large apex beast | one direct strike, one sweep, one fear pulse, one throw, one hold or devour attack, one weak point |
| Ambush horror | hidden or site-bound defense, one hold attack, one fear attack, one tempo-theft attack |
| Swarm menace | damage-cap body, broad area attacks, distraction or poison cloud, fire weakness |
| Demonic infiltrator | passives for disguise or host logic, fear or poison touch, one mobility trick, one taboo or material weakness |
| Undead lord | partial immunity, fear-based attacks, one command or summoning-flavored attack, anchor or purge condition |
| Burrower or underwater hunter | positional vulnerability, drag or grapple, drowning or engulf loop, terrain-tied ambush rule |
| Intelligent hunter-beast | targeted prey selection, one mobility-control attack, one finisher against held prey, moderate armor |

If a new monster cannot be described through one of these package rows or a close variation, it may be drifting away from the engine and should be audited against `monster-design-engine.md` before use.
