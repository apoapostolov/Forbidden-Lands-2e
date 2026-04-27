<!-- markdownlint-disable MD013 -->

# Monster Design Engine

## Contents

1. Purpose
2. Scope
3. Unified Bestiary Logic
4. Core Combat Contract
5. Statblock Grammar
6. Attack Grammar
7. Defense, Weakness, And Survival Grammar
8. Monster Structure Models
9. Legend Design And Placement
10. Design Constraints And Red Flags
11. AI Construction Workflow
12. Quick Audit Checklist

## Purpose

This document explains how the Forbidden Lands 2E bestiary engine works as one combined monster corpus.

It is meant for technical monster creation, not prose polishing.
Use it when an AI or designer needs to build a new monster whose attacks, passives, weaknesses, and combat behavior feel native to the existing bestiary.

This document answers six practical questions:

- what a monster is allowed to do mechanically
- how the bestiary expresses those mechanics in the current engine
- what kinds of asymmetry are normal versus dangerous
- how to construct a new monster without turning it into a spell list with teeth
- when a monster should also receive a legend
- where that legend belongs in the manuscript being worked on

## Scope

This is a design-logic reference for:

- monster combat procedure
- monster statblock construction
- monster attack construction
- passives, defenses, and weaknesses
- structural models such as swarms, anchors, variants, and no-monster-attacks creatures
- legends tied to monster entries
- compatibility boundaries for new monster design

This is not the main prose-formatting guide.
For entry order, encounter design, resources, and lore-roll formatting, use `skills/forbidden-lands-bestiary/SKILL.md`.

## Unified Bestiary Logic

The bestiary should be treated as one engine, not as two competing rule families.

Some entries are simpler and more foundational.
Some entries are more explicit, more modular, or more adventurous in presentation.
That difference matters historically, but it does not help an AI create better monsters.

For monster creation purposes, all of the following belong to one shared system:

- the base monster combat rules
- the six-attack table model
- no-monster-attacks exceptions
- humanoid band models
- procedural demon construction
- passive lines such as `PASSIVE`, `SPECIAL DEFENSE`, and `SPECIAL WEAKNESS`
- anchor logic such as eggs, phylacteries, hosts, and lesser eyes
- variant ladders such as hatchling, adult, elder, caste, or sex-based forms
- legends as long-memory lore attached to important monsters

The correct design question is never:

> Is this from the older bestiary layer or the newer one?

The correct design question is:

> Does this mechanic behave like it belongs to the same monster engine?

## Core Combat Contract

### Shared baseline

- Monsters are GM-controlled and otherwise behave like NPCs.
- Some monsters lack Wits and Empathy and therefore cannot take damage to them.
- Monsters can perform monster attacks.
- A monster attack is normally a slow action.
- Default range is ARM'S LENGTH unless the attack says otherwise.
- Every extra `⚔️` beyond the first increases damage by 1.
- Monster attack rolls cannot be pushed.
- Monster Strength is durability, not offensive output scaling.
- A wounded monster does not lose offensive effectiveness.
- A Broken monster is dead or dying. No critical injury roll is made.

### Global monster exceptions

These baseline exceptions define the subsystem.

| Rule | Baseline Monster Logic |
| --- | --- |
| Fear | Monsters are immune to fear attacks and to spells that damage Wits or Empathy. |
| Parry | Monster attacks normally cannot be PARRIED unless the attack says otherwise. |
| Dodge | Monster attacks normally can be DODGED unless the attack says otherwise. |
| Grapple | Monsters cannot normally be GRAPPLED unless stated otherwise. |
| Shove | Four-legged or many-legged monsters resist being knocked prone; large bipeds require extra `⚔️`. |
| Disarm | Weapon-using monsters can be DISARMED, but large Strength gaps increase the success requirement. |
| Feint | Monsters cannot be FEINTED. |
| Hidden combinations | The advanced hidden-combination rules are not used against monsters or by them. |

### Controlled escalation tools

The engine uses a few reliable escalation levers.

- additional initiative cards for harder monsters
- wider attack ranges
- more targets per attack
- riders that inflict fear, poison, disease, or forced movement
- passives that alter what counts as a valid answer
- special weaknesses that let players reduce or bypass monster defenses
- site-bound pressure that changes how an existing attack behaves

The engine does **not** usually escalate monsters by giving them many free actions, layered interrupts, or long lists of triggers.

## Statblock Grammar

The statblock carries more design logic than it first appears.

### Attribute logic

There are three broad attribute profiles.

#### 1. Full-minded monsters

These have Strength, Agility, Wits, and Empathy.
Use this profile when the monster:

- reasons like a person
- manipulates, deceives, or schemes
- has a social or telepathic identity
- is vulnerable to mind-facing play

Examples:

- Bog Hag
- Thought-Kraken
- Night Bride
- Death Magister

#### 2. Reduced-mind monsters

These have Strength and Agility, sometimes Wits, but omit Empathy or most higher cognition.
Use this profile when the monster:

- behaves according to instinct or fixed supernatural compulsion
- threatens bodies more than negotiations
- should resist social control by simply lacking the required interiority

Examples:

- Amoeba
- Gray Bear
- Swarming Death

#### 3. No-monster-attacks fighters

Some creatures are structurally part of the bestiary but explicitly do **not** use monster attacks.
Instead, they fight as normal combatants or custom NPCs.

Examples:

- Amphibians
- Insectoids
- many undead troops and skeleton-like humanoids
- humanoid bands such as archers, hunters, poisoners, and road champions

Use this model when the creature is dangerous because of equipment, group tactics, role, or environment rather than monster asymmetry.

### Armor bands

Armor Rating is not random.
The corpus clusters into stable durability bands.

| Armor Band | Typical Meaning | Common Users |
| --- | --- | --- |
| 0 | unarmored, immaterial, or body not defended by armor but protected by another rule | ghosts, maras, amoebas, shapeshifters |
| 1-3 | light hide, feathers, skin, or lightly protected intelligent beings | harpies, pale apes, lesser predators |
| 4-6 | serious natural armor or dense body | trolls, ents, demons, large beasts |
| 7-8 | elite or heavily armored monster | drakes, golems, apex predators |
| 9-12 | colossal or near-legendary shell, scale, or stone body | dragons, star-watchers, great armored horrors |

Armor alone is rarely the full defense package for powerful monsters.
High-end monsters usually add at least one of these:

- half damage from certain weapon classes
- immunity to specific damage types
- a targetable weak spot
- regeneration
- return-after-banishment logic
- a bound object, host, brood node, or phylactery

### Passive and special-line grammar

The current corpus uses several recurring statblock labels.
These are not decorative.
They correspond to repeatable design jobs.

- `PASSIVE`
- `SPECIAL DEFENSE`
- `SPECIAL WEAKNESS`
- `REGENERATE`
- `SPECIAL`

| Label | Mechanical Job |
| --- | --- |
| PASSIVE | always-on rule that shapes positioning, perception, targeting, or encounter texture |
| SPECIAL DEFENSE | unusual damage handling, gear punishment, element-feeding, or another defensive exception |
| SPECIAL WEAKNESS | called-shot, anchor, or exploitable body or site rule |
| REGENERATE | recurring Strength recovery per round or under a named stimulus |
| SPECIAL | short catch-all for legacy entries when the function is clear and narrow |

Examples:

- a dragon's scale-gap that halves armor for one strike
- a golem that regains Strength from a named element
- a star-watcher whose lesser eyes can be destroyed separately
- a tunneler that can only be struck where it breaks the surface
- a death magister that reforms if the phylactery survives

## Attack Grammar

Monster attacks are built from a small number of reusable attack families.

### Numeric baselines

The corpus shows stable pressure bands.

| Base Dice | Typical Role |
| --- | --- |
| 5-6 | minor fear pulse, harassment, lesser area pressure, weak hold, swarm nuisance |
| 7-8 | standard monster attack band; most signature attacks live here |
| 9-10 | elite single-target pressure, stronger area control, serious poison or fear delivery |
| 11-12 | apex attacks, boss finishers, hard throws, devour loops, high-end fear assaults |

| Weapon Damage | Typical Meaning |
| --- | --- |
| 1 | default damage, especially when paired with a rider |
| 2 | heavy bite, sting, slam, or execution attack |
| 3 | rare and exceptional; usually reserved for procedural monsters or especially huge strikes |

Potency and Virulence also cluster.

| Rating Band | Typical Role |
| --- | --- |
| 6-7 | common dangerous poison or disease |
| 8-9 | elite, military, or apex-tier toxin or infection |
| 10+ | boss-grade or strongly supernatural delivery |

Fear attacks follow similar escalation.

| Fear Dice | Typical Role |
| --- | --- |
| 5-7 | ordinary monster terror effect |
| 8-10 | strong boss or signature horror effect |
| 11-12 | apex soul-shock, death-vision, or life-drain intensity |

### Family 1: direct strike attacks

These are the default physical attacks.

Form:

- attack roll
- one target, sometimes two
- Weapon Damage 1 or 2
- often a rider such as prone, thrown, or GRAPPLED

Examples:

- Gray Bear `PAW STRIKE!`
- Ent `SWEEPING BLOW!`
- Greater Golem `CRUSHING ATTACK!`
- Air Spirit `WIND SLAM!`

### Family 2: sweep and area attacks

These are extremely common.

Form:

- all adventurers within NEAR or SHORT range
- moderate Base Dice
- damage 1 is common
- prone, throw, fear, poison cloud, or distraction often attached

Examples:

- Dragon `TAIL ATTACK!`
- Manticore `RAIN OF SPIKES!`
- Swarming Death `BROAD MASS ATTACK!`
- Giant Specter `WHIRLWIND ATTACK!`

### Family 3: throw and knockdown attacks

Forced movement is one of the defining signatures of the bestiary.

Common riders:

- thrown to NEAR range
- thrown to SHORT range
- thrown to the ground
- prone after hit

Examples:

- Death Knight `POWER ATTACK!`
- Giant `CANNONBALL!`
- Iron Dragon `TAIL ATTACK!`
- Earth Spirit `BACKHAND OF STONE!`

### Family 4: grapple, hold, drag, and crush loops

Many monsters convert a successful hit into ongoing bodily pressure.

Common loop pattern:

1. hit or successful special attack
2. target becomes GRAPPLED, dragged, submerged, or swallowed
3. the victim suffers repeated damage, drowning, or positional helplessness until escape or monster death

Examples:

- Giant Squid `TENTACLE HUG!`
- Sea Serpent `DEATHLY EMBRACE!`
- Pale Ape `HOOKING ARM!` leading into `BONE CRACK!`
- Rock-Hanger `GRASPING TENDRILS!` into `REEL AND BITE!`
- Thought-Kraken `GRASPING TENTACLES!`

### Family 5: engulf, devour, absorb, and drowning loops

This is the more severe form of the grapple family.

Common pattern:

- special attack targets a victim by range or attribute priority
- victim fails a MOVE roll or gets hit by an attack
- victim is swallowed, dragged under, absorbed, or otherwise moved into a lethal internal space
- inside-space damage repeats each round
- the inside of the monster often has altered armor logic

Examples:

- Drakewyrm `DEVOURING ATTACK!`
- Amoeba `ABSORBING ATTACK!`
- Bog Man `DROWNING ATTACK!`
- Amphibian drowning attacks in water
- Sea Serpent underwater drag patterns

### Family 6: fear attacks

Fear is the most common non-physical attack family in the corpus.

Its uses are broader than horror flavor.
Fear attacks represent:

- supernatural aura
- visions of death
- soul pressure
- telepathic assault
- overwhelming scale
- prophecy or cosmic insignificance

Examples:

- Ghost `TOUCH OF DEATH!` and `GHOST SCREAM!`
- Bloodling `HORRIBLE MIST!`
- Bog Man `VENGEANCE OF THE GODS!`
- Thought-Kraken `LIFE DRAIN!`
- Star-Watcher `SOUL GLARE!`

### Family 7: poison, disease, paralysis, and corruption delivery

Monsters heavily use the existing poison and disease engine instead of inventing bespoke affliction systems.

Delivery methods include:

- on hit if damage is dealt
- on hit regardless of damage
- on failed MOVE or ENDURANCE roll in an area cloud
- by touch or gaze
- as a passive attack condition

Examples:

- manticore spikes delivering paralyzing poison
- a bog hag's diseased belly magic
- a rat king's plague and befouling attacks affecting both bodies and supplies
- a mire drake's lethal toxic cloud
- a mummy's death-chill expressed through paralysis

### Family 8: action denial and tempo attacks

Several monsters remove the target's ability to act effectively.

Patterns include:

- victim unable to act until the same point next round
- victim unable to speak for a Quarter Day
- victim fights as in darkness
- victim must spend time breaking free, recovering breath, or standing up

Examples:

- Amoeba `REEKING CLOUD!`
- Mara nightmare attacks
- Imp `TONGUETWISTING ATTACK!`
- Air Spirit `DUST BLIND!`
- Swarming Death `DISTRACTING ATTACK!`

### Family 9: battlefield-state attacks

Some monsters alter terrain, atmosphere, or the validity of normal tactics.

Examples:

- smothering fog and drowning-air effects
- darkness or dust blindness
- anti-magic gaze or magic suppression
- aerosol poison clouds
- food contamination
- armor-halving swarm attacks

Examples in the corpus:

- Possessor `SMOTHERING FOG!`
- Rat King `BEFOULING ATTACK!`
- Swarming Death `BROAD MASS ATTACK!`
- Star-Watcher central gaze quenching magic

## Defense, Weakness, And Survival Grammar

Monster durability is built from combinations, not one number.

### Model 1: plain armor

Simple beasts and straightforward bruisers often rely mostly on Armor Rating.

Examples:

- Gray Bear
- Ent
- Wyvern

### Model 2: armor plus called weak point

This is one of the most common high-tier solutions.

Pattern:

- the monster has large armor
- a specific body point may be targeted at a penalty
- attacks against that point ignore or reduce armor

Examples:

- Dragon scale gap
- Iron Dragon airways
- Golem eyes or joints
- Star-Watcher lesser eyes
- Giant scorpion eyes

### Model 3: partial immunity matrix

These monsters are not universally immune.
They have damage-conversion logic.

Common patterns:

- half damage from physical attacks
- no damage from piercing or stabbing weapons
- double damage from fire or magic
- physical attacks ineffective unless magic, copper, or a blessed material is used

Examples:

- Amoeba: half from physical weapons, none from piercing, double from fire
- Shapeshifter: half from nonmagic physical, none from stabbing, double from magic
- Mummy: half from physical, none from stabbing, double from fire
- Bloodling: full vulnerability only to copper when materialized
- Ghosts, specters, and maras: limited vulnerability to fire or magic, often with banish-return logic

### Model 4: regeneration or element-feeding

The corpus uses regeneration sparingly, but clearly.

Examples:

- Troll recovers 1 Strength per round
- Rock Troll recovers 1 Strength per round
- Grave Bat heals 1 lost Strength at end of each round
- certain golems recover Strength from a matching element instead of taking damage

### Model 5: return-after-defeat logic

Some monsters are not truly solved by reducing Strength to zero.

Examples:

- ghosts and giant specters are only banished unless PURGE UNDEAD is used
- a death magister reforms if the phylactery remains intact
- a possessor tries to abandon a dying host and move into another body
- a basilisk loses its magic if the bound egg is destroyed

### Model 6: anchor or host logic

Some monsters depend on an external support object or body-state.

Examples:

- basilisk egg
- death magister phylactery
- possessor host body
- bloodling mist-versus-body state
- lesser eyes, brood organs, or other local anchors on advanced monsters

### Model 7: perception and targeting restrictions

Some monsters invalidate normal targeting assumptions.

Examples:

- Air Spirit: missiles through the heart-body suffer a penalty
- Tunneler: can only be struck where it breaks the surface
- Rock-Hanger: indistinguishable from stone until it acts
- Transparent demon results: all attacks against the demon suffer a penalty

## Monster Structure Models

The corpus uses repeatable structural templates.

### 1. Standard monster-attacks brute or predator

The monster has:

- ordinary statblock
- six-entry attack table
- one or more special lines
- one clear body identity

Examples:

- Gray Bear
- Manticore
- Ent
- Dread Raptor

### 2. Intelligent humanoid band

These do not use monster attack tables.
They are built with:

- DIFFICULTY
- ROLE
- GEAR
- TALENTS
- TACTICS

Examples:

- Black-Fletch Archer
- Clan Hunter
- Horse Warrior
- Poisoner

### 3. No-monster-attacks kin or troop creature

These appear in the bestiary but fight through normal combat procedures or custom activity notes.

Examples:

- Amphibians
- Insectoids
- skeleton-like undead and similar troop monsters

### 4. Procedural generator monster

The demon is the clearest example.

Its engine is assembled from:

- form table
- ability table
- attack table
- special ability table
- weakness table

This shows that the bestiary can support procedural monsters as long as every generated result still maps cleanly onto the same underlying verbs: Armor Rating, fear attack, poison Potency, regeneration, extra initiative, and material weaknesses.

### 5. Swarm entity

Swarm monsters use body-count logic rather than duelist logic.

Common features:

- cap on damage taken from one attack
- large-area threat bands
- reduced single-body legibility
- attack descriptions that treat the swarm as one collective organism

Examples:

- Swarming Death
- hatchling masses and similar insect-pressure models

### 6. Variant ladder monster

The corpus supports monsters presented as developmental or caste variants.

Examples:

- Giant Spider hatchling, adult male, elder female
- caste-coded insectoid structures
- age or sex variants that increase poison, size, or narrative role

### 7. Multi-part or body-zone monster

These monsters have sub-targets, detachable advantages, or body sections that matter.

Examples:

- Star-Watcher lesser eyes
- Dragon scale gap
- Golem joints and eyes
- Sea Serpent tail effects

### 8. Site-bound or atmosphere-bound monster

These are monsters whose mechanics are inseparable from where they dwell.

Examples:

- Mara attacking sleepers
- Thought-Kraken in wells and flooded vaults
- Bog Man in bog water and roots
- Air Spirit around gibbets and exposed heights
- Tunneler beneath the earth surface

The fight is partly against the site, not just the body.

## Legend Design And Placement

Legends are part of the monster-creation pipeline, not optional garnish.

A legend is a half-page to one-page lore writeup about old mysteries, old tales, inherited warnings, sacred explanations, local customs, old crimes, long memory, or pre-Blood Mist beliefs tied to a monster.

A legend should make the monster feel older than the current adventure.

### What a legend is for

A strong legend does one or more of the following:

- gives the monster historical depth
- shows what people believe the monster means
- ties the monster to cult practice, taboo, trade custom, road lore, or settlement fear
- preserves pre-Blood Mist memory or distorted memory from the old ages
- provides atmosphere without becoming a rule explainer

A legend is not a Monster Description written again.
It is not an ecology paragraph in older clothing.
It is what the world remembers, misremembers, or refuses to forget.

### Core legend rules

A legend should usually be:

- **half a page to one page** in manuscript terms
- written as 2 to 4 paragraphs
- focused on long memory, not present-tense encounter procedure
- rooted in one monster-specific truth, fear, or social function
- willing to preserve uncertainty

A legend may:

- contain conflicting explanations
- show cult or regional interpretation
- explain why a village has a practice or taboo
- preserve a partial truth about a weakness without naming the mechanic

A legend must not:

- read like a statblock commentary
- explain mechanics in rules language
- spoil the full puzzle of the monster in direct terms
- drift into generic epic myth with no local material anchor

### Preferred legend subjects

The best legends usually revolve around one of these:

- why a people fears or honors the monster
- what old profession or order learned to live with it
- what bargain, taboo, offering, or road custom grew around it
- what ancient crime, burial, war, rite, or divine slight made it part of the land
- what the world before the Blood Mist believed about it, and what survived badly into the current age

### Legend voice

Legends are manuscript-facing prose.
Use `forbidden-lands-writing-voice` for diction and rhythm.

The voice should feel like:

- old explanation carried forward by human mouths
- priestly memory, hill-lore, guild custom, clan inheritance, or roadside warning
- physical and social detail first, abstract cosmology second

A legend may sound authoritative, but it should rarely sound final.
It may say what people believe without proving whether the belief is correct.

### Legend placement rule

Use the manuscript structure already present.

#### If the manuscript has a Legends chapter

Add the legend to that chapter.
Use the chapter's legend format rather than nesting the legend inside the monster entry.

Typical format in a Legends chapter:

```markdown
### Monster Name

> _Legend text in multi-paragraph blockquote form._
```

#### If the manuscript has no Legends chapter

Place the legend directly after the monster entry, after the RESOURCES block.
Use an H4 section such as:

```markdown
#### Legend

> _Legend text._
```

The point is not the exact label.
The point is that the legend should travel with the monster if the manuscript has nowhere else to house it.

### When a monster should receive a legend

A monster should usually receive a legend if it:

- is ancient, sacred, cursed, or culturally important
- shapes settlement practice, cult habit, trade custom, or road behavior
- has a relationship to old ruins, pre-Blood Mist memory, or inherited taboo
- is likely to appear in a manuscript with a Legends chapter or legend-bearing appendix

A purely functional beast or minor hazard does not always need one.
A monster that changes what people build, avoid, offer, or whisper about usually does.

## Design Constraints And Red Flags

A new monster is likely compatible when it obeys these constraints.

### Constraint 1: express weirdness through existing verbs first

Prefer:

- fear attack
- Potency or Virulence
- MOVE roll to evade
- ENDURANCE roll to resist
- thrown to range
- GRAPPLED
- prone
- COLD
- damage to a normal attribute

Do **not** invent a bespoke subsystem if an existing verb already carries the load.

### Constraint 2: give the monster one primary engine

A good monster usually has:

- one main pressure identity
- one secondary wrinkle
- one weakness or counterplay hook

A monster with four equally central gimmicks usually stops feeling native.

### Constraint 3: resistances should create inquiry, not dead ends

Good:

- half damage from slashing, but weak joints can be targeted
- only magic hurts it, but fire also works
- it reforms unless the phylactery is handled

Bad:

- immune to almost everything with no clear investigative path
- multiple stacked immunities with no offsetting weakness

### Constraint 4: large monsters should dominate space, not just numbers

If the creature is huge, give it:

- sweeps
- throws
- area fear
- drag, trample, or crush patterns
- multi-target coverage

Do not only increase Base Dice and Armor Rating.

### Constraint 5: hard control needs limits

Paralysis, sleep, drowning, swallow, or speech-loss can be used.
But they should usually be bounded by one of these:

- one target
- a resist roll
- short range
- a visible tell
- a rescue method
- internal weakness once the victim is inside

### Constraint 6: avoid bookkeeping-heavy stacking

The engine does not like:

- stacking multi-round debuff ladders
- per-target counters on several simultaneous riders
- multiple persistent zones from one creature
- reaction suites that trigger off many different player actions

### Constraint 7: tie mechanics to body, curse, or site logic

Every major effect should answer the question:

**Why can this monster do this?**

Good answers:

- the tail injects venom
- the wings create a dust-blind storm
- the swarm enters armor gaps
- the spirit's central eye quenches magic
- the host demon needs bodies to survive
- the thing has lived in that well or cairn long enough to reshape the place around it

## AI Construction Workflow

Use this order when designing a new monster.

### Step 1: define the monster's threat identity in one sentence

Examples:

- A quarry-haunting stone beast that pins prey to rock and feeds on the panic of climbing victims.
- A corpse-mist that can only act through wet cloth and gutter-water.
- A brood guardian that grows stronger as eggs remain intact.

If the sentence contains three separate engines, the concept is too diffuse.

### Step 2: choose the structure model

Pick one:

- standard monster-attack brute or predator
- intelligent humanoid band
- no-monster-attacks troop creature
- swarm
- multi-part boss
- site-bound supernatural hunter
- variant ladder family
- procedural generator template

### Step 3: choose the durability package

Pick one main defense and at most one support defense.

Examples:

- Armor 6 plus called-shot weak point
- half damage from nonmagic weapons plus fire vulnerability
- low armor plus host-jump persistence
- regeneration plus sunlight weakness

### Step 4: assign primary pressure channels

Pick one primary and one secondary channel.

Common channels:

- forced movement
- grapple or devour
- fear
- poison or disease
- action denial
- battlefield alteration
- anti-magic or anti-supply pressure

### Step 5: draft the six attacks by role, not by spectacle

A reliable distribution is:

- 2 direct physical attacks
- 1 area or sweep attack
- 1 control or hold attack
- 1 fear or supernatural pressure attack
- 1 apex or identity-defining attack

### Step 6: assign a discoverable weakness

A weakness can be:

- anatomical
- material
- elemental
- host-based
- anchor-based
- environmental

The key is that it should reward observation, lore, or tactical courage.

### Step 7: make the lore roll and resources point at the same truth

The corpus works best when:

- the Lore Roll hints at how the monster really functions
- the RESOURCES block proves the same anatomy or curse from the carcass side

### Step 8: decide whether the monster needs a legend

Ask:

- does this monster carry inherited fear, taboo, or sacred weight?
- would people build customs, shrines, trade clauses, or avoidance behavior around it?
- does the creature need pre-Blood Mist memory to feel complete?

If yes, draft a legend and place it in the Legends chapter or after the entry, depending on manuscript structure.

### Step 9: perform the native-feel audit

Ask:

- Does this still resolve mostly through existing verbs?
- Does the monster feel physical, cursed, or embodied rather than abstract?
- Does its defense package invite inquiry rather than resignation?
- Is there one memorable engine rather than several equal gimmicks?
- Would a GM be able to run it without a side document at the table?
- Would the legend deepen the monster's world-weight rather than merely repeat the description?

## Quick Audit Checklist

Use this before approving a new monster.

- Is the monster's core identity one sentence long?
- Does it use a known structure model?
- Does it have only one main defense package?
- Are most attacks in the 7-10 Base Dice range unless this is an apex creature?
- Does it rely on forced movement, fear, poison, grapple, or battlefield state rather than flat bonus inflation?
- Is its weirdest rule expressed through an existing engine verb when possible?
- Does it have one real weakness or counterplay hook?
- Does it avoid excessive triggered reactions or stacked counters?
- Do Lore Roll and RESOURCES both point at the same anatomy, curse, or ecology?
- If the monster has a legend, does that legend add memory, taboo, or old explanation rather than repeating present-tense description?
- Would it still feel like Forbidden Lands if the prose were removed and only the rules remained?
