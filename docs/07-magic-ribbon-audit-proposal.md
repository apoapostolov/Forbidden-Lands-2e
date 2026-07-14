<!-- markdownlint-disable MD013 -->

# Draft Proposal: Chance and Safe Casting Ribbon Audit

## Status

**Implemented in `01-corebook/07-magic.md`.** This document is retained as the allocation and design audit. The corebook chapter is authoritative where its final wording differs from this record.

This audit assigns every spell in the chapter one of three decisions:

- **CHANCE:** add a narrow benefit that applies only when the spell is chance cast and the caster accepts a guaranteed mishap.
- **SAFE:** add a narrow limitation that applies only when safe casting removes at least one casting die.
- **NONE:** add no casting-mode text. This is an intentional decision, not an incomplete row.

## Portfolio Rule

The chapter currently contains 396 spells across General Spells and seventeen disciplines. This proposal uses the requested allocation exactly:

| Decision | Spells | Share of All Spells | Share of Ribboned Spells |
| --- | ---: | ---: | ---: |
| CHANCE | 99 | 25.0% | 75.0% |
| SAFE | 33 | 8.3% | 25.0% |
| NONE | 264 | 66.7% | — |
| **Total** | **396** | **100%** | **132 ribboned spells** |

Thus exactly one spell in three receives a ribbon, and exactly three ribboned spells in four use chance casting.

## Governing Constraints

- Treat CHANCE effects as situational rewards, not automatic Power Level increases.
- Prefer information, movement, timing, setup, rescue, and conditional finishers over raw damage.
- Make every CHANCE effect worth considering but not worth a guaranteed mishap on every casting.
- Require every CHANCE effect to create a concrete option, alter a consequential roll, preserve a resource, or reveal information that can change a decision.
- Let an effect last at least one turn (15 minutes) when it is meant to support later action. A round-long effect is acceptable only when it can be exploited immediately in combat.
- Do not count atmospheric detail, information already supplied by the base spell, delayed failure without time to intervene, or convenience already purchasable with Power Level as a reward.
- Reserve SAFE limitations for broad spells that remain useful after being narrowed.
- Do not add SAFE limitations merely to tax mastery.
- Avoid ribbons on most epic spells, dense reactions, permanent transformations, and spells already carrying several subprocedures.
- A spell may receive at most one proposed mode in this pass. No spell receives both.
- Resolve the base spell normally before resolving a CHANCE effect unless its wording necessarily changes targeting or geometry.

## Reading the Tables

During implementation, insert selected text under a **CHANCE CASTING:** or **SAFE CASTING:** label. Rows marked NONE should remain unchanged.

## Allocation by Discipline

| Discipline | Total | Chance | Safe | None | Ribbon Share |
| --- | ---: | ---: | ---: | ---: | ---: |
| General Spells | 26 | 7 | 2 | 17 | 34.6% |
| Healing Magic | 27 | 7 | 2 | 18 | 33.3% |
| Shapeshifting | 24 | 6 | 2 | 16 | 33.3% |
| Awareness | 25 | 6 | 2 | 17 | 32.0% |
| Symbolism | 24 | 6 | 2 | 16 | 33.3% |
| Stone Song | 23 | 6 | 2 | 15 | 34.8% |
| Blood Magic | 24 | 6 | 2 | 16 | 33.3% |
| Death Magic | 23 | 5 | 2 | 16 | 30.4% |
| Elemental Magic | 27 | 7 | 2 | 18 | 33.3% |
| Ice Affinity | 17 | 4 | 2 | 11 | 35.3% |
| Nature | 19 | 5 | 1 | 13 | 31.6% |
| Swarm Magic | 23 | 6 | 2 | 15 | 34.8% |
| Magma Song | 23 | 5 | 2 | 16 | 30.4% |
| Mentalism | 25 | 6 | 2 | 17 | 32.0% |
| Oneiromancy | 23 | 6 | 2 | 15 | 34.8% |
| Magnetism | 23 | 6 | 2 | 15 | 34.8% |
| Demonic Magic | 20 | 5 | 2 | 13 | 35.0% |

## Complete Spell Audit

### General Spells

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Empower Spell | 1 | CHANCE | The allied spell may use your position as its point of origin for range and line of sight if you are within NEAR range of its caster. |
| Magical Seal | 1 | CHANCE | The first time the seal reduces a hostile spell, its protected subject and the seal's caster learn the spell's discipline and the exact position from which it was cast. They retain this knowledge even if the source was unseen or the caster is elsewhere. |
| Pass Magical Resilience | 1 | NONE | — |
| Prestidigitation | 1 | SAFE | The trick can affect only you, your voice, and objects you carry; it cannot directly alter another creature or its perceptions. |
| Sense Magic | 1 | SAFE | Range becomes NEAR, and the spell cannot detect magic protected by OBSCURE MAGIC. |
| Copy Magic | 2 | CHANCE | When the spell is copied, learn one required ingredient, target restriction, or other concrete limitation of the copied spell. |
| Dispel Magic | 2 | CHANCE | If the opposing spell is reduced to Power Level 0, its collapsing magic marks its caster for one turn (15 minutes). You know the marked caster's direction while within SHORT range, and the mark negates visual concealment against you. |
| Extend Magic | 2 | NONE | — |
| Hold Magic | 2 | CHANCE | If damage breaks your concentration, the held spell persists for one turn (15 minutes) before ending. You need not spend actions to maintain it during that turn, but you cannot resume or further extend it. |
| Obscure Magic | 2 | NONE | — |
| Bind Magic | 3 | NONE | — |
| Contain Spell | 3 | NONE | — |
| Prepare Magic | 3 | CHANCE | If the prepared spell expires unused, recover 1 WP committed to it; no more than 1 WP can be recovered this way. |
| Stabilize Magic Zone | 3 | NONE | — |
| Stabilize Spell | 3 | NONE | — |
| Transfer | 3 | NONE | — |
| Call Familiar | 4 | NONE | — |
| Living Spell | 4 | NONE | — |
| Mass Spell | 4 | NONE | — |
| Quicken Ritual | 4 | NONE | — |
| Unearth Magic | 4 | CHANCE | You also learn whether the unearthed residue was chiefly protective, harmful, controlling, or transformative, and whether it was used within the last day. |
| Absorb Magical Residue | 5 | NONE | — |
| Create Artifact | 5 | NONE | — |
| Anti-Magic Zone | 6 | NONE | — |
| God Spell | 6 | NONE | — |
| Transcendence | 6 | NONE | — |

### Healing Magic

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Cleanse Spirit | 1 | CHANCE | After healing, the target cannot suffer further Wits or Empathy damage from the same creature, spell, or fear effect for one turn (15 minutes). This protection ends after it prevents damage once. |
| Healing Hands | 1 | CHANCE | You suspend the effect and time limit of one lethal critical injury affecting the target for one turn (15 minutes). The injury is not healed, and its lethal clock resumes when the turn ends. |
| Nature's Cure | 1 | CHANCE | You identify the poison or disease, its current Potency or Virulence, and the most likely route by which the target contracted it. |
| Preserve | 1 | SAFE | The spell can affect only non-living material and cannot suspend a living creature. |
| Relieve Condition | 1 | NONE | — |
| Rinse | 1 | NONE | — |
| Banish Demon | 2 | CHANCE | After the spell inflicts its Strength damage, a true demon that remains unbroken is banished if its current Strength is no greater than the damage just suffered. The demon's wounded substance tears open a rift that drags it back to the world from which it came. The rift then closes. |
| Immunity | 2 | SAFE | The spell affects only one target. Choose poison or disease when you cast it. The spell protects against the chosen category, not both. |
| Mend Self | 2 | NONE | — |
| Mend Wounds | 2 | CHANCE | Before the end of the next round, the target may GET UP once without spending a fast action. |
| Purge Undead | 2 | CHANCE | An unbroken undead whose remaining Strength is no greater than the damage just suffered falls prone and loses its next fast action. |
| Bend Demon | 3 | NONE | — |
| Calm Emotions | 3 | CHANCE | Choose one affected creature. One ongoing fear, rage, coercion, or supernatural agitation affecting it remains suppressed for one turn (15 minutes), even if a new hostile action ends the spell for everyone else. The suppressed effect returns afterward if its duration has not expired. |
| Invigorate | 3 | NONE | — |
| Lift Curse | 3 | NONE | — |
| Rejuvenation | 3 | NONE | — |
| Resurrection | 3 | NONE | — |
| Rite of Passage | 3 | NONE | — |
| Serenity | 3 | NONE | — |
| Weathermaster | 3 | NONE | — |
| Healing Trance | 4 | NONE | — |
| Regeneration | 4 | NONE | — |
| Tranquility | 4 | NONE | — |
| Holy Ward | 5 | NONE | — |
| Purge Magic | 5 | NONE | — |
| Restoration | 5 | NONE | — |
| Restore Life | 6 | NONE | — |

### Shapeshifting

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Animal Speech | 1 | CHANCE | After answering the normal questions, the animal volunteers one urgent sensory impression concerning danger, food, young, or territory. |
| Befriend Animal | 1 | NONE | — |
| Cat's Paw | 1 | NONE | — |
| Hawk's Eye | 1 | CHANCE | The first SCOUTING roll made through the enhanced sight gains one automatic ⚔️. Declare the roll before the spell ends. |
| Nature's Watch | 1 | CHANCE | On its first alarm, the watching animals reveal the intruders' number, direction, broad size, and whether they bear visible weapons. You learn this even if the SCOUTING roll gains no additional ⚔️. |
| Bear's Claw | 2 | CHANCE | If the strike inflicts damage, the target is also subjected to a SHOVE with one ⚔️. |
| Beastmaster | 2 | SAFE | The spell affects only a calm or unthreatened animal and cannot order it to attack, enter obvious danger, or abandon its young. |
| Deer's Dash | 2 | NONE | — |
| Dolphin's Dive | 2 | NONE | — |
| Winged Descent | 2 | CHANCE | You may bring one falling creature or LIGHT carried object within ARM'S LENGTH down safely with you. |
| Animal Form | 3 | SAFE | You may assume only the form of an animal you have personally observed for at least a Quarter Day. |
| Bat's Claws | 3 | NONE | — |
| Call Animal | 3 | NONE | — |
| Inhabit Animal | 3 | NONE | — |
| Primal Soul | 3 | NONE | — |
| Wolf's Nose | 3 | CHANCE | You can distinguish one particular individual's trail from other members of the same kin or species without an additional roll. |
| Animal Animosity | 4 | NONE | — |
| Hibernate | 4 | NONE | — |
| Primal Agility | 4 | NONE | — |
| Primal Strength | 4 | NONE | — |
| Humanoid Form | 5 | NONE | — |
| Monstrous Form | 5 | NONE | — |
| Rat's Reflexes | 5 | NONE | — |
| Summon Beasts | 6 | NONE | — |

### Awareness

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Lightbringer | 1 | NONE | — |
| Recall Memory | 1 | CHANCE | The target can recover one sensory fragment from a memory erased, magically altered, or normally inaccessible through trauma. The spell also reveals that the memory was interfered with, but does not undo the alteration. |
| Transfer Senses | 1 | NONE | — |
| True Sight | 1 | CHANCE | Choose one creature or object examined during the spell. You learn whether magic currently disguises, transforms, or controls it and, if so, the discipline and Power Level of that effect. |
| True Strike | 1 | NONE | — |
| Words on the Wind | 1 | CHANCE | You may isolate one known voice or recurring sound from surrounding noise even when several sounds overlap. |
| Compel Truth | 2 | NONE | — |
| Farsight | 2 | SAFE | You may view only a place you have personally visited; Power Levels cannot overcome lack of first-hand familiarity. |
| Portent | 2 | NONE | — |
| Predict Moves | 2 | CHANCE | You also learn the target, route, or destination the enemy currently means to use. |
| Speak to the Wind | 2 | SAFE | The recipient must be somewhere within your current map hex. |
| True Path | 2 | NONE | — |
| Visions of the Past | 2 | NONE | — |
| Divination | 3 | NONE | — |
| Guide | 3 | NONE | — |
| Intuition | 3 | NONE | — |
| Telepathy | 3 | CHANCE | Ask one direct yes-or-no question while reading a mind. You hear the target's first instinctive answer before they can deliberately suppress or reframe it. |
| Tongues | 3 | NONE | — |
| Block Reading | 4 | NONE | — |
| Mind Focus | 4 | NONE | — |
| Mold Memory | 4 | NONE | — |
| Fate Weaving | 5 | NONE | — |
| Locate | 5 | CHANCE | You also learn the direction in which the target most recently moved. If the target is stationary, you sense that instead. |
| Time Sending | 5 | NONE | — |
| Undo | 6 | NONE | — |

### Symbolism

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Arcane Mark | 1 | NONE | — |
| Entice | 1 | CHANCE | Before moving toward the symbol, the victim drops one LIGHT or TINY object held in a hand of the caster's choice. |
| Horrify | 1 | CHANCE | A victim suffering Wits damage cannot willingly move closer to the symbol until the end of its next turn. |
| Inscribe | 1 | CHANCE | One page or symbol may remain invisible except to one named observer until the next dawn. |
| Paralyze | 1 | CHANCE | An affected victim also cannot take reactive actions until its next turn in the initiative order. |
| Warning | 1 | CHANCE | When triggered, the symbol conveys the direction of the danger and whether it is one creature, a group, or an environmental event. |
| Blind | 2 | NONE | — |
| Falsify Magic | 2 | NONE | — |
| Illusion | 2 | SAFE | The illusion must be motionless and cannot produce speech, changing sounds, or a moving concealment. |
| Mind Trick | 2 | NONE | — |
| Sleep | 2 | NONE | — |
| Portal | 3 | CHANCE | Until the first creature passes through, the far side of the portal is invisible and makes no sound to observers there. |
| Power Rune | 3 | NONE | — |
| Puppeteer | 3 | NONE | — |
| Vanish | 3 | NONE | — |
| Animate Object | 4 | SAFE | The object can perform only one simple repeated action chosen when cast and cannot interpret new instructions. |
| Blink | 4 | NONE | — |
| Hold | 4 | NONE | — |
| Recall | 4 | NONE | — |
| Silence | 4 | NONE | — |
| Bend Reality | 5 | NONE | — |
| Improved Illusion | 5 | NONE | — |
| Polymorph | 5 | NONE | — |
| Runweaver's Gift | 6 | NONE | — |

### Stone Song

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Dust from the Deep | 1 | CHANCE | While inside the dust, you can hear the direction of moving creatures within NEAR range even though you cannot see them. |
| Reinforce | 1 | CHANCE | If the reinforced barrier would be destroyed, breached, or forced open, it remains standing and impassable until the end of the next round, then collapses. This delay occurs only once. |
| Stone Fist | 1 | NONE | — |
| Stun | 1 | NONE | — |
| Voice of the Mountain | 1 | SAFE | The mountain can answer only about the present and events within the last day, regardless of Power Level. |
| Open | 2 | CHANCE | The opening is quiet. Any trap the spell would trigger is delayed until the end of the next round, giving those present time to withdraw, block it, or attempt to disarm it. |
| Pass Crack | 2 | NONE | — |
| Stone Storm | 2 | CHANCE | Loose stone remains churned at the target's position, making that immediate area ROUGH until the end of the next round. |
| Stonesmith | 2 | SAFE | The construction must be crude, stationary, and load-bearing; it cannot contain moving parts, traps, or fine sealed mechanisms. |
| Wither | 2 | NONE | — |
| Earthquake | 3 | CHANCE | If the spell tears down a wall or fortification, you choose the direction in which the rubble falls. The breach is left passable instead of becoming ROUGH. |
| Iron Song | 3 | NONE | — |
| Mountains' Blessing | 3 | NONE | — |
| Petrify | 3 | NONE | — |
| Summon Golem | 3 | NONE | — |
| Animate Weapon | 4 | CHANCE | Once during the duration, the weapon may take one fast action without costing you an action, following your most recent command. |
| Call Meteor | 4 | NONE | — |
| Earthen Pillar | 4 | NONE | — |
| Machine Soul | 4 | NONE | — |
| Raise Land | 5 | NONE | — |
| Repurpose | 5 | NONE | — |
| Way of the Mountain | 5 | NONE | — |
| Ancestral Guardian | 6 | NONE | — |

### Blood Magic

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Blood Oath | 1 | CHANCE | When the subject first knowingly acts against the oath, you sense that the oath was breached and the direction to the subject, but not the distance. |
| Blood Tap | 1 | CHANCE | If no spell uses the granted Power Levels during the normal one-round window, retain 1 of them for one turn (15 minutes). The remaining granted Power Levels are lost normally. |
| Firewalker | 1 | SAFE | Choose heat or cold when cast. The spell grants immunity only to the chosen extreme. |
| Heroism | 1 | NONE | — |
| Stir the Blood | 1 | CHANCE | Choose whether the spell brings out lust, fear, or rage instead of leaving the dominant emotion to the GM. The GM still determines how the victim expresses it. |
| Bind Demon | 2 | CHANCE | A demon that successfully resists still cannot cross the pentagram or approach within ARM'S LENGTH of it for one turn (15 minutes). Attacking the demon from inside this boundary ends the protection. |
| Blood Bond | 2 | CHANCE | Before choosing the transfer, you learn whether either participant carries a blood-borne poison, disease, or supernatural contamination. |
| Darkvision | 2 | SAFE | The sight works only in natural darkness and cannot penetrate magical darkness, supernatural fog, or deliberate magical concealment. |
| Hand of Blood | 2 | NONE | — |
| Immolate | 2 | CHANCE | A burning target sheds bright light and cannot benefit from darkness or visual concealment until the flames are extinguished. |
| Bind Soul | 3 | NONE | — |
| Blood Channeling | 3 | NONE | — |
| Blood Curse | 3 | NONE | — |
| Blood Warrior | 3 | NONE | — |
| Meld Flesh | 3 | NONE | — |
| Blood Vessel | 4 | NONE | — |
| Break Flesh | 4 | NONE | — |
| Call Demon | 4 | NONE | — |
| Repel | 4 | NONE | — |
| Clone | 5 | NONE | — |
| Create Bloodling | 5 | NONE | — |
| Demonic Pact | 5 | NONE | — |
| Redirecting Barrier | 5 | NONE | — |
| Life Bond | 6 | NONE | — |

### Death Magic

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Befoul | 1 | NONE | — |
| Chill of the Grave | 1 | CHANCE | One TINY or LIGHT exposed object carried by the victim freezes to its hand, clothing, or nearby surface until freed with a fast action. |
| Contaminate | 1 | NONE | — |
| Feign Death | 1 | SAFE | The spell can affect only the caster. |
| Ghoulish Glare | 1 | NONE | — |
| Bane Blade | 2 | NONE | — |
| Death's Mercy | 2 | NONE | — |
| Hand of Doom | 2 | CHANCE | A target suffering damage cannot speak or shout until the end of its next turn. |
| Raise the Dead | 2 | NONE | — |
| Speak to the Dead | 2 | CHANCE | Before answering questions, the dead involuntarily yields one sensory fragment from the final minute of its life. |
| Curse of Undeath | 3 | NONE | — |
| Darkness | 3 | SAFE | Range becomes NEAR, and the spell suppresses only nonmagical light sources. |
| Steal Life | 3 | NONE | — |
| Terror | 3 | CHANCE | A victim Broken by the spell must flee from you by the safest available route for one turn (15 minutes) or until prevented from fleeing. The compulsion ends early if you or an ally attacks that victim again. |
| Weight of Ages | 3 | CHANCE | If the aging makes the victim lose an attribute point, you choose the affected attribute instead of the victim. |
| Cloud of Death | 4 | NONE | — |
| Disintegrate | 4 | NONE | — |
| Possess | 4 | NONE | — |
| Wraithform | 4 | NONE | — |
| Bane | 5 | NONE | — |
| Death's Embrace | 5 | NONE | — |
| Eternal Life | 5 | NONE | — |
| The Bells of Death | 6 | NONE | — |

### Elemental Magic

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Combustion | 1 | CHANCE | Choose the direction of the first smoke plume; until the next round it obscures one border adjacent to the burning object. |
| Deviation | 1 | CHANCE | Redirect the projectile against another creature within ARM'S LENGTH of its original target. Resolve the original attack roll against the new target, who may DODGE or PARRY normally. |
| Flaming Blade | 1 | NONE | — |
| Sunder | 1 | CHANCE | If the object is part of a larger barrier, mechanism, or structure, the damage also exposes a breach, access point, or disabled joint. The next MIGHT or CRAFTING roll made to pass through or sabotage the structure gains two Base Dice. |
| Suffocate | 1 | NONE | — |
| Water Breathing | 1 | SAFE | The spell affects only the caster and cannot add targets. |
| Dense Fog | 2 | NONE | — |
| Fire Resistance | 2 | NONE | — |
| Flight | 2 | SAFE | The spell affects only the caster, Movement Rate is 1, and the caster must land at the end of the round. |
| Heat of the Moment | 2 | NONE | — |
| Impulse | 2 | NONE | — |
| Parch | 2 | NONE | — |
| Rock Storm | 2 | NONE | — |
| Wind Blast | 2 | CHANCE | Each target moved by the blast drops one held TINY or LIGHT object of your choice. The objects land one zone downwind from their bearers. |
| Elemental Shield | 3 | NONE | — |
| Fireball | 3 | CHANCE | Choose one creature or ARM'S-LENGTH patch within the secondary blast area that the flames curl around and do not attack. |
| Flood Wave | 3 | CHANCE | The wave also extinguishes ordinary fires in its path. Choose one victim that takes damage. Before knocking the victim prone, the wave carries them one zone toward an edge or exit you choose. |
| Pressure Jet | 3 | CHANCE | The struck position remains flooded or slick and counts as ROUGH until the end of the next round. |
| Stoneskin | 3 | NONE | — |
| Tornado | 3 | NONE | — |
| Elemental Infusion | 4 | NONE | — |
| Elemental Wall | 4 | NONE | — |
| Summon Elemental | 4 | NONE | — |
| Elemental Bolts | 5 | NONE | — |
| Elemental Ward | 5 | NONE | — |
| Liquid Form | 5 | NONE | — |
| Control Element | 6 | NONE | — |

### Ice Affinity

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Arrows of Ice | 1 | CHANCE | The first arrow that hits leaves a visible frost mark, granting +1 die to track that target until the next Quarter Day. |
| Winter Grip | 1 | CHANCE | Affected targets leave no tracks on snow or ice for the full duration unless they choose to. |
| Condense Water | 2 | CHANCE | Ignore the doubled Power Level requirement in desert terrain. The condensed water is cool and potable even when drawn from foul air, smoke, or salt spray. |
| Frost Armor | 2 | NONE | — |
| Glacial Path | 2 | NONE | — |
| Zone of Cold | 2 | SAFE | The temperature change affects only one NEAR-sized zone within range. |
| Armor of Ice | 3 | NONE | — |
| Winter's Call | 3 | NONE | — |
| Crystalize | 4 | NONE | — |
| Encase | 4 | NONE | — |
| Mold Ice | 4 | SAFE | The ice can form only simple stationary shapes without moving parts, sealed locks, or fine mechanisms. |
| Shatter | 4 | CHANCE | A creature damaged by the spell remains supernaturally brittle until the end of the next round. The first physical attack that damages it during that time ignores its Armor Rating. |
| Wall of Ice | 4 | NONE | — |
| Citadle of Ice | 5 | NONE | — |
| Glacial Snap | 5 | NONE | — |
| Hailstorm | 5 | NONE | — |
| Boreal Slave | 6 | NONE | — |

### Nature

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Plant Growth | 1 | CHANCE | The new growth visibly reveals poisoned soil, plant disease, or a place where vegetation has been unnaturally suppressed. |
| Tracelessness | 1 | CHANCE | For one turn, leave a single false trail departing in a direction chosen at casting before the land erases the true trail. |
| Blocking Branch | 2 | NONE | — |
| Call Lightning | 2 | NONE | — |
| Fog | 2 | CHANCE | Choose one creature per Power Level when casting. Those creatures can see within the fog without its ranged-attack or visibility penalties for the spell's full duration. |
| Glade | 2 | NONE | — |
| Strider | 2 | SAFE | Only the caster gains the increased travel rate; companions must travel normally. |
| Bark Skin | 3 | NONE | — |
| Break Wood | 3 | NONE | — |
| Mend Wood | 3 | NONE | — |
| Voice of the Forest | 3 | CHANCE | When the first message is sent, the trees also convey the direction of the nearest fire, mass felling, or immediate threat to the forest. |
| Chain Lightning | 4 | NONE | — |
| Forest Door | 4 | CHANCE | The door remains ajar until the end of the next round, allowing one additional creature to follow without counting against Power Level. |
| Nature's Power | 4 | NONE | — |
| Nature's Weapon | 4 | NONE | — |
| Animate Tree | 5 | NONE | — |
| Nature's Blessing | 5 | NONE | — |
| Wonder | 5 | NONE | — |
| Sky Beam | 6 | NONE | — |

### Swarm Magic

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Fireflies | 1 | CHANCE | One swarm can settle on a visible target, outlining it and denying visual concealment for one turn (15 minutes) or until the target spends a slow action scattering the swarm. |
| Harass | 1 | CHANCE | The insects leave a distinctive scent on the target for one Quarter Day, even if the spell ends early. Attempts to track the target by scent gain two Base Dice. |
| Hivemind | 1 | CHANCE | Once during the duration, learn the direction of the largest nearby concentration of living creatures detected by the insects. |
| Infest | 1 | NONE | — |
| Mouth Swarm | 1 | CHANCE | A target suffering Wits damage cannot speak clearly until the end of its next turn. |
| Worm Food | 1 | NONE | — |
| Carapace | 2 | CHANCE | You may shed the carapace to ignore one successful SHOVE or forced-movement effect; doing so ends the spell. |
| Elytra | 2 | NONE | — |
| Pheromones | 2 | SAFE | The spell affects insects only and grants no bonus to MANIPULATION against humanoids. |
| Stink Bug Serenade | 2 | NONE | — |
| Brain Parasite | 3 | NONE | — |
| Create Hive | 3 | NONE | — |
| Insect Swarm | 3 | NONE | — |
| Lord of Flies | 3 | NONE | — |
| Probe Area | 3 | SAFE | The insects explore only one location per Power Level and cannot continue past a dead end to find replacements. |
| Consume | 4 | NONE | — |
| Swarm Form | 4 | NONE | — |
| Wasp Launcher | 4 | NONE | — |
| Web | 4 | CHANCE | Until the web is destroyed, you sense the direction and rough size of any creature touching or struggling against it. |
| Evolve | 5 | NONE | — |
| Giant Insect | 5 | NONE | — |
| Insect Plague | 5 | NONE | — |
| Everswarm | 6 | NONE | — |

### Magma Song

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Combustion | 1 | NONE | — |
| Fertile Ash | 1 | NONE | — |
| Fire's Friend | 1 | SAFE | The spell protects only the caster and cannot add further targets. |
| Hearth | 1 | CHANCE | Wet clothing, bedrolls, and ordinary fuel within NEAR range become dry enough for immediate use. |
| Mold Stone | 1 | SAFE | The material can form only rough, non-mechanical shapes and cannot produce weapons, fine tools, or sealed containers. |
| Fire Memory | 2 | CHANCE | After stone melts, its exposed flow lines reveal one nearby crack, hollow, or structural weakness. |
| Mend the Cracks | 2 | NONE | — |
| Molten Armor | 2 | CHANCE | The first metal weapon that strikes the armor suffers 1 point of item damage after resolving the attack. |
| Steam Flight | 2 | NONE | — |
| Water Memory | 2 | NONE | — |
| Absorb Lava | 3 | NONE | — |
| Firestorm | 3 | NONE | — |
| Firewall | 3 | NONE | — |
| Magma Cascade | 3 | NONE | — |
| Summon Fire Wyrm | 3 | NONE | — |
| Call Mineral | 4 | NONE | — |
| Dragon Breath | 4 | NONE | — |
| Geyser | 4 | CHANCE | Steam obscures the target's zone until the end of the next round after the geyser resolves. |
| Magma Tunneling | 4 | CHANCE | The passage leaves one stable handhold, shelf, or air gap per zone crossed, chosen as the tunnel forms. |
| Molten Seat | 5 | NONE | — |
| Volcanic Eruption | 5 | NONE | — |
| Volcanic Transportation | 5 | NONE | — |
| Last Stand | 6 | NONE | — |

### Mentalism

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Compartmentalize Mind | 1 | NONE | — |
| Mental Strength | 1 | NONE | — |
| Mind Over Body | 1 | NONE | — |
| Traceless | 1 | SAFE | The spell alters only the caster and cannot include additional people or creatures. |
| Wordplay | 1 | CHANCE | The target immediately reveals, through a word or gesture, which interpretation it accepted. |
| Amnesia | 2 | CHANCE | Until someone presents clear contradictory evidence, the victim does not notice that time or memory is missing. |
| Confusion | 2 | NONE | — |
| Mind Blast | 2 | CHANCE | A target suffering Wits damage cannot take reactive actions until its next turn in the initiative order. |
| Mind Shield | 2 | NONE | — |
| Mirror Images | 2 | CHANCE | The first attacker to destroy an image must direct its next single-target attack against another remaining image, if one remains in its reach or range. |
| Truth Sense | 2 | CHANCE | You gain one additional revelation beyond those granted by Power Level. It identifies what the subject most urgently wants hidden about the matter being examined. |
| Break Mind | 3 | NONE | — |
| False Shape | 3 | NONE | — |
| Fata Morgana | 3 | SAFE | The illusion must be motionless and silent and cannot react to observers. |
| Geas | 3 | CHANCE | Before the compulsion begins, the target must state aloud how it literally understands the required action. |
| Implant Memory ✦ | 3 | NONE | — |
| Time Stop | 3 | NONE | — |
| Body Swap | 4 | NONE | — |
| Mass Confusion | 4 | NONE | — |
| Meditate | 4 | NONE | — |
| Mirror Clone | 4 | NONE | — |
| Impart Talent | 5 | NONE | — |
| Improved Fata Morgana | 5 | NONE | — |
| Mold Time | 5 | NONE | — |
| Mind Seed | 6 | NONE | — |

### Oneiromancy

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Daydream | 1 | NONE | — |
| Nightmares | 1 | CHANCE | If the spell Breaks a victim's Wits, roll twice for that victim's critical fear injury and choose which result applies. |
| Premonition | 1 | CHANCE | When a premonitioned action is abandoned, receive one sensory omen indicating its immediate cause of failure, not the full hidden situation. |
| Quickened Dreams | 1 | CHANCE | During the power nap, affected sleepers wake immediately if a hostile creature enters NEAR range or violence begins there. They cannot be surprised by that threat. |
| Restorative Sleep | 1 | NONE | — |
| Dream Visit | 2 | SAFE | You observe from one fixed vantage point chosen on arrival. Additional Power Levels cannot be spent to communicate. |
| Lullaby | 2 | SAFE | Range becomes NEAR, and you must sing without interruption for the full turn before the sleep takes effect. |
| Mara | 2 | NONE | — |
| Probe Dream | 2 | CHANCE | After one answer, ask one immediate clarifying question that does not count against the spell's Power Level limit or require another turn (15 minutes). |
| Sleepwalker | 2 | NONE | — |
| Contagious Dreams | 3 | NONE | — |
| Dream Link | 3 | CHANCE | If the intended target is awake when the ritual begins, the spell waits for their next sleep for up to one day and enters the first dream they have. You know whether the link is waiting, established, or expired. |
| Dream Travel | 3 | NONE | — |
| Prophetic Dreams | 3 | NONE | — |
| Sand Sleep | 3 | CHANCE | Choose one affected creature that may be awakened normally by touch instead of only by you. |
| Dream Palace | 4 | NONE | — |
| Endless Nightmare | 4 | NONE | — |
| Magic Dream | 4 | NONE | — |
| Manifest Dream | 4 | NONE | — |
| Astral Dream | 5 | NONE | — |
| Sandman | 5 | NONE | — |
| Wish | 5 | NONE | — |
| Future Dream | 6 | NONE | — |

### Magnetism

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Iron Will | 1 | SAFE | The spell can manipulate only unattended metal and locks or mechanisms no creature is actively holding or resisting. |
| Magnetic Map | 1 | CHANCE | You also sense the direction of the nearest major magnetic anomaly, large iron deposit, or strongly magnetized structure. |
| Magnetize | 1 | CHANCE | For one day, you can sense the direction to the magnet while within the same hex. |
| Path of Iron | 1 | NONE | — |
| Stanch Blood | 1 | NONE | — |
| Attract | 2 | NONE | — |
| Deflect Metal | 2 | NONE | — |
| Disarm | 2 | CHANCE | A flung weapon sticks to the nearest suitable iron surface at its landing point and requires a fast action to pull free. |
| Launch Weapon | 2 | CHANCE | If the attack is parried with a metal weapon or shield, the launched weapon sticks to it. The defender must drop that item or spend a fast action pulling the two apart. |
| Repel | 2 | NONE | — |
| Arrow Storm | 3 | NONE | — |
| Bloodshock | 3 | NONE | — |
| Fling | 3 | CHANCE | Before moving the target, choose one unsecured TINY or LIGHT metal object they carry. It is torn free and lands where the target stood. |
| Magnetic Flight | 3 | NONE | — |
| Sense Metal | 3 | SAFE | The spell detects metal objects only and grants no vision of creatures through iron in their blood. |
| Blade Sphere | 4 | NONE | — |
| Fixate | 4 | NONE | — |
| Floating Shield | 4 | NONE | — |
| Telekinesis | 4 | NONE | — |
| Absorb Metal | 5 | NONE | — |
| Hold Together | 5 | CHANCE | When the spell ends, each affected item repairs 1 point of item damage or lost Armor Rating that it suffered while the spell was active. Completely destroyed or missing material cannot be restored. |
| Mold Gravity | 5 | NONE | — |
| Reverse Spell | 6 | NONE | — |

### Demonic Magic

| Spell | Rank | Decision | Proposed Ribbon or Limitation |
| --- | ---: | --- | --- |
| Corrosive Touch | 1 | CHANCE | The corroded point remains visibly weak for one turn (15 minutes). The first physical attack directed at that point gains two Base Dice and ignores 1 point of Armor Rating. |
| Generate Mog | 1 | NONE | — |
| Sense Corruption | 1 | SAFE | Range is limited to NEAR and the spell reveals presence only, not direction. |
| Demon Tongue | 2 | CHANCE | While conversing with a demon, learn its dominant present appetite. The first MANIPULATION roll during the spell that offers, threatens, or exploits that appetite gains two Base Dice. This does not reveal whether the demon lies. |
| Dissolve | 2 | CHANCE | The dissolving surface briefly outlines adjoining hollows, seams, and mechanisms within ARM'S LENGTH before collapsing. |
| Mog Blade | 2 | NONE | — |
| Mog Ward | 2 | NONE | — |
| Call Misgrown | 3 | NONE | — |
| Demon Sight | 3 | NONE | — |
| Graft Flesh | 3 | NONE | — |
| Mog Spray | 3 | CHANCE | Choose one narrow route through the sprayed area where the residue does not settle until the end of the next round. |
| Compel Demon | 4 | CHANCE | Before obeying, the demon must state one literal ambiguity or loophole it perceives in the command. |
| Demon Limb | 4 | NONE | — |
| Reshape Body | 4 | SAFE | You can choose only gills or bodily compression. The spell cannot increase your attributes or create armor. |
| Tear the Veil | 4 | NONE | — |
| Flesh Abomination | 5 ✦ | NONE | — |
| Mog Flood | 5 | NONE | — |
| Summon Demon | 5 | NONE | — |
| Apotheosis | 6 | NONE | — |
| Churmog Gate | 6 | NONE | — |

## Playtest and Maintenance Order

1. Playtest one low-rank CHANCE effect, one combat-control CHANCE effect, one information CHANCE effect, and one SAFE limitation before testing the more unusual cases.
2. Check whether players remember the mode text and whether guaranteed mishaps remain exceptional choices.
3. Revise any effect that is always correct, never chosen, duplicates Power Level scaling, or exceeds a normal action's value.
4. Recount after adding or removing spells. Preserve approximately one-third coverage and the three-to-one CHANCE-to-SAFE ratio rather than treating 99 and 33 as permanent numbers.

## Maintenance Boundary

Future revisions should preserve the portfolio unless play reveals a problem. Any change that alters action economy, bypasses a spell's defining limit, or contradicts a discipline rule should receive focused review rather than being treated as a wording correction.
