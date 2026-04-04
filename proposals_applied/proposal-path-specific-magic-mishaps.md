<!-- markdownlint-disable MD013 -->

# Proposal - Path-Specific Magic Mishaps

Goal: replace the single generic mishap table with one mishap table per magical path, while preserving the same D66 option density as the original table. Every path should feel distinct, but no path should feel thinner than the system it replaced.

## Design Principles

- Keep the current casting engine: Willpower, overcharge, and mishap risk all stay intact.
- Keep the existing D66 modifier logic based on the number of `💀` rolled.
- Match the original mishap table's 20 result bands exactly.
- Make every result matter immediately, shortly after, or strategically.
- Tie every backlash to the actual theme of the path.
- Reserve some low-to-mid bands for item damage, local environmental spill, and same/nearby-hex stray discharge instead of repetitive self-condition results.
- Reserve `66` for the signature catastrophe of that discipline.

## Core Rule Change

When a spell causes a mishap, roll on the mishap table for the path used to cast that spell.

- A Healing spell uses the Healing mishap table.
- A Blood spell uses the Blood mishap table.
- A general spell uses the General Spells mishap table.
- If a spell belongs to multiple themes because of custom content, use the table that best matches the spell's dominant effect.

Keep the current modifier ladder:

| Rolled `💀` | Modifier |
| --- | --- |
| 1 | `-10` |
| 2 | `+0` |
| 3-4 | `+10` |
| More | `+10` per each additional two `💀` |

## Result Bands

Each path below uses the same result bands as the original mishap table:

- `01-02`
- `03-04`
- `05-06`
- `11-13`
- `14-15`
- `16-21`
- `22-23`
- `24-25`
- `26-31`
- `32-33`
- `34-35`
- `36-41`
- `42-45`
- `46`
- `51`
- `52-55`
- `56`
- `61`
- `62-64`
- `65`
- `66`

Editorial preference for the least interesting bands:

- `14-15`: item trouble
- `16-21`: environmental change in `NEAR` or `FAR`
- `22-23`: stray discharge at a random location in the same or a nearby hex

## General Spells Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The spell discharges elsewhere: at a random place in the same or a nearby hex, a ward flares, an object is hurled, a door seals, a light bursts, or another brief magical disturbance causes alarm. |
| 03-04 | You are swollen with your own importance and cannot bear counsel or contradiction. Suffer `1` point of Empathy damage. |
| 05-06 | The spell floods you with demonic visions, impossible formulas, and broken voices. Suffer `1` point of Wits damage. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Loose power races under your skin. Roll three extra Base Dice on your next General Spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your magic permanently alters your appearance. The GM decides how, but the change should reflect uncontrolled general sorcery rather than one specific path. |
| 22-23 | A `NEAR` or `FAR` area is fouled by unstable magic: drifting lights, warped echoes, deadened sound, crawling sparks, false shadows, or bitter static. The area is difficult to read, and `SCOUTING` and `STEALTH` there are at `-2` for one Quarter Day. |
| 24-25 | The spell drains your energy, inflicting `1` point of Agility damage. |
| 26-31 | The magic bites into your body and you suffer `1` point of Strength damage. |
| 32-33 | Your grasp on broad spellcraft falters. All General Spells count as one rank lower for `D6` days. Talents reduced to zero still allow you to chance cast rank `1` General Spells. |
| 34-35 | One scroll, grimoire, warding mark, ritual tool, or packet of reagents within `NEAR` range is smeared, scorched, spilled, or otherwise spoiled. |
| 36-41 | The spell bursts outward in a naked display of raw sorcery: lights, voices, shockwaves, frost-smoke, sparks, or shadow-rifts, depending on the magic worked. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Your spell is noticed across the veil. Before the next Quarter Day ends, the GM introduces one pathless magical complication: a demon's spoor, a hungry spirit, a warped omen, a hostile scout, or another sign that uncontrolled power has drawn attention. |
| 46 | Raw magical filth settles into flesh. You and one random other creature within `ARM'S LENGTH` are exposed to a magical disease with Virulence `2 +` the Willpower spent on the spell. |
| 51 | The effect also catches a friend, neutral, mount, or other unintended nearby target. |
| 52-55 | The spell blinds you. You act as if in total darkness for the next full day. |
| 56 | The spell ravages your mind. Immediately roll for a Horror critical injury. |
| 61 | The force of the magic breaks your body. Immediately roll for a Blunt critical injury. |
| 62-64 | The spell backfires. A protective spell leaves you exposed, a binding loosens, a disguise slips, a transfer runs the wrong way, a living spell turns hostile, or another General Spell effect twists against its purpose. |
| 65 | The spell tears loose the structures that keep your will, name, and magic aligned. You survive, but your self is broken into echo, ward, and hunger. You are no longer fit for ordinary adventuring unless bound, restored, or reclaimed by extraordinary means. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Healing Magic Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The blessing spills elsewhere: at a random place in the same or a nearby hex, wounds knit wrongly, a corpse twitches, or a sickbed flares into panicked commotion. |
| 03-04 | The suffering around you becomes unbearable. For one Quarter Day, you cannot willingly leave a Broken ally behind. |
| 05-06 | The veil hangs too thin around you. Whispers of the dead follow you, and `STEALTH` and `MANIPULATION` are both at `-2` until dawn. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Restless grace crackles through you. Roll three extra Base Dice on your next Healing spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your touch leaves a holy or uncanny mark on skin, eyes, or voice. |
| 22-23 | A `NEAR` or `FAR` area turns thick with cloying pollen, overripe rot, or corpse-sweet air, imposing `-2` to `SCOUTING` and `STEALTH` there for one Quarter Day. |
| 24-25 | Your hands will not stop trembling. Your next `HEALING` roll or Healing spell is at `-2`. |
| 26-31 | The grace of the spell clings where it should not. Until your next rest, you cannot recover attributes by ordinary rest. |
| 32-33 | Your healing gift falters. All Healing spells count as one rank lower for `D6` days. |
| 34-35 | Herbs, bandages, poultices, and healing draughts within `NEAR` range spoil, clot, or lose their virtue. |
| 36-41 | A pale saint-light spills from your hands and wounds, and your breath carries the sweet rot of opened graves. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Demons or undead sense the miracle and are drawn toward you within the next Quarter Day. |
| 46 | The healing turns septic. You and one random other creature within `ARM'S LENGTH` are exposed to a magical disease with Virulence `2 +` the Willpower spent on the spell. |
| 51 | The spell leaps to the wrong body. An enemy, rival, or unintended bystander also gains the effect or relief. |
| 52-55 | The light blinds you for the rest of the day. |
| 56 | The spell ravages your spirit. Roll immediately on the Horror critical injury table. |
| 61 | Life-force snaps through your bones. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell inverts: healing wounds instead, calm turns to numbness, purge spreads the affliction, or preservation becomes stasis. |
| 65 | You become the vessel of what answered from beyond. Your body survives, but something hungry and half-restored now wears it; only powerful ritual aid, binding, or mercy can end the fate. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Shapeshifting Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The call lands elsewhere: at a random place in the same or a nearby hex, wolves howl, birds scatter, or a herd stampedes without clear cause. |
| 03-04 | The pack sense goes wrong. Mounts, hunting beasts, and tame animals on your side do not trust your commands this scene. |
| 05-06 | Beast-instinct jumps the leash. At the start of the next encounter, you must spend your first fast action mastering yourself or immediately follow one strong impulse: chase, flee, feed, or defend. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Beast-force crawls in your skin. Roll three extra Base Dice on your next Shapeshifting spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | One beast-feature lingers after the spell: eyes, claws, scent, fur, or voice. |
| 22-23 | A `NEAR` or `FAR` area erupts with animal panic, territorial musk, and warning cries; beasts there will not stay calm for one Quarter Day. |
| 24-25 | Your limbs keep the wrong gait. `MOVE` is at `-2` until your next rest. |
| 26-31 | You reek of predator or prey. Animals react badly to you, and `ANIMAL HANDLING` is at `-2` for one Quarter Day. |
| 32-33 | Your shifting gift falters. All Shapeshifting spells count as one rank lower for `D6` days. |
| 34-35 | Reins, leashes, leather straps, and fur-lined gear within `NEAR` range reek of beast-scent, causing mounts and animals to shy or snap. |
| 36-41 | Your face and limbs flicker through wrong half-forms: fang, muzzle, claw, hide, or predator eyes showing through in jolts. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | The wrong predator answers your call and comes hunting. |
| 46 | Nearby beasts panic, bolt, or turn aggressive for the next Quarter Day. |
| 51 | The spell catches a friend too: an ally inherits a beast-trait, panic response, or feral instinct. |
| 52-55 | You lose speech and can only snarl, bark, hiss, or howl until dawn. |
| 56 | Your mind frays under the wild. Roll immediately on the Horror critical injury table. |
| 61 | Bones wrench and snap in the change. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: you half-shift, lose self-command, turn on allies, or cannot fully shed the beast. |
| 65 | The beast takes you for good. Your human mind is buried under fang, hide, and hunger, and your character becomes a monstrous animal unless the party can reverse it by extreme means. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Awareness Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The vision breaks loose elsewhere: at a random place in the same or a nearby hex, an omen, ghost-light, or impossible sign causes alarm. |
| 03-04 | Plain speech becomes hard. Until your next rest, you cannot cleanly lie, bluff, or hide your immediate purpose. |
| 05-06 | A false omen takes root in your mind. The GM names the misleading sign openly; until it is disproved or until dawn, rolls that rely on reading the current situation are at `-2`. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Too much knowing sparks in you. Roll three extra Base Dice on your next Awareness spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your eyes, voice, or shadow now bear a telltale omen of prophecy or second sight. |
| 22-23 | A `NEAR` or `FAR` area fills with omens, whispers, and half-seen traces; all `STEALTH` there is at `-2` for one Quarter Day. |
| 24-25 | Your focus splits in two. Your next `SCOUTING`, `INSIGHT`, or `LORE` roll must ignore one success. |
| 26-31 | Your thoughts leak into the air. Nearby allies and enemies can read your mood and intent for one scene. |
| 32-33 | Your sight beyond sight dims. All Awareness spells count as one rank lower for `D6` days. |
| 34-35 | Maps, letters, seals, and hidden notes within `NEAR` range shed ink, reveal secrets, or become unreadable under too much truth. |
| 36-41 | Your eyes glaze white and fix on things no one else can see, while your head turns toward hidden truths with dreadful certainty. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Spirits, seers, or unseen watchers notice your opened mind. |
| 46 | The air fills with echoes of past and future. Everyone nearby suffers `-2` to `SCOUTING` and `STEALTH` for one Quarter Day. |
| 51 | The insight is shared by the wrong person. A rival, enemy, or bystander learns part of what you just learned. |
| 52-55 | You are blinded by too much vision and count as in total darkness for a full day. |
| 56 | Your mind buckles under revelation. Roll immediately on the Horror critical injury table. |
| 61 | The seizure of insight batters your body. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: you receive false certainty, lose the right memory, expose a hidden plan, or spoil the timing of an ally's action. |
| 65 | You see too much and do not come back whole. Your mind locks into prophecy, terror, and impossible truths; the character can no longer function as an adventurer unless somehow restored by extraordinary intervention. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Symbolism Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The sign lands elsewhere: at a random place in the same or a nearby hex, a doorway seals, a ward flares, or an illusion bursts into view. |
| 03-04 | Your words twist in your own mouth. Spoken coordination and `MANIPULATION` are at `-2` until dawn. |
| 05-06 | Nearby signs answer you without leave. For one scene, doors, masks, mirrors, and marked things in sight may flare or react at the GM's call. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Unstable sigils crawl over your skin. Roll three extra Base Dice on your next Symbolism spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your magic permanently alters your face, voice, scent, or shadow with a symbolic tell. |
| 22-23 | A `NEAR` or `FAR` area is branded by glowing signs, false shadows, or crawling sigils, drawing eyes and ruining concealment for one Quarter Day. |
| 24-25 | Sigils burn into your fingertips. Fine hand work, lockpicking, and similar tasks are at `-2` until your next rest. |
| 26-31 | Your shadow and reflection no longer agree with you. `STEALTH` is at `-2` for one Quarter Day. |
| 32-33 | Your runes and signs fail you. All Symbolism spells count as one rank lower for `D6` days. |
| 34-35 | Scrolls, doors, locks, masks, or marked gear within `NEAR` range are overwritten with the wrong sign, seal, or ward. |
| 36-41 | Runes crawl over your skin, gear, and shadow, burning for a heartbeat like cut lines of light. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | A hostile thing from beyond notices the breach or mark you made. |
| 46 | Wards, marks, or illusions nearby begin misfiring for the next Quarter Day. |
| 51 | A friend or ally is also caught in the command, fear, illusion, or silence. |
| 52-55 | A sign flashes in your eyes and blinds you for a day. |
| 56 | Your mind reels under broken meaning. Roll immediately on the Horror critical injury table. |
| 61 | The recoil twists your bones and stance. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: the command catches you, the portal miskeys, the silence encloses you, or the illusion turns on allies. |
| 65 | The sign rewrites you instead. Your true face, voice, and self are sealed beneath a living symbol, and what remains is an omen-ridden shell unless the curse is broken. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Stone Song Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The song strikes elsewhere: at a random place in the same or a nearby hex, a wall cracks, a tunnel settles, or a standing stone splits. |
| 03-04 | Ancestral murmurs fill your ears. You cannot hear quiet speech well enough for whispered plans or stealthy coordination until dawn. |
| 05-06 | Mountain-pride hardens in you. You cannot willingly yield ground or retreat this scene unless an ally drags you off. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Stone hums in your bones. Roll three extra Base Dice on your next Stone Song spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your skin, eyes, or voice take on a stony cast. |
| 22-23 | A `NEAR` or `FAR` area shifts with dust, loose stone, or sudden heaving ground, becoming `ROUGH` for one Quarter Day. |
| 24-25 | Your steps go stone-heavy. `RUN` becomes a slow action until your next rest. |
| 26-31 | Grit and iron cling to you. Climbing, swimming, and sneaking are all at `-2` for one Quarter Day. |
| 32-33 | The mountain grows deaf to you. All Stone Song spells count as one rank lower for `D6` days. |
| 34-35 | Stoneware, locks, blades, hinges, and worked metal within `NEAR` range jam, crack, or turn heavy as lead. |
| 36-41 | Dust lifts around your feet, pebbles quiver, and your voice comes back with the weight of a cavern mouth. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | The song reaches something old below: spirit, construct, or thing under the earth. |
| 46 | Stone dust, cracks, and falling shards turn the zone dangerous for one Quarter Day. |
| 51 | A friend, mount, or ally is also trapped, struck, or walled off by the mishap. |
| 52-55 | Flying grit blinds you for a full day. |
| 56 | The weight of the deep breaks your mind. Roll immediately on the Horror critical injury table. |
| 61 | The mountain snaps your bones. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: the wrong wall falls, the wrong passage seals, the wrong weapon wakes, or the ground betrays your side. |
| 65 | The mountain keeps you. Flesh turns to living stone from the feet upward until you stand as a breathing statue, aware but nearly helpless, unless some mighty unmaking frees you. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Blood Magic Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The blood-call spills elsewhere: at a random place in the same or a nearby hex, beasts panic, wounds reopen, or blood runs where it should not. |
| 03-04 | Every oath feels thin as paper. Until dawn, you cannot spend WP to aid or protect another without first passing `INSIGHT`. |
| 05-06 | Blood wells from eyes, gums, or nose. `MANIPULATION` and `STEALTH` are at `-2` until cleaned and bandaged. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Your veins crackle with violent power. Roll three extra Base Dice on your next Blood Magic spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your body gains a visible blood-mark, heat-shimmer, or unsettling mutation. |
| 22-23 | A `NEAR` or `FAR` area becomes slick with blood-mist, copper stink, and panic; `MOVE` there is at `-2` for one turn. |
| 24-25 | Your pulse hammers wrong. Your next `MELEE` or `MARKSMANSHIP` roll must be pushed if it can be. |
| 26-31 | You carry the smell of fresh blood. Trackers, predators, and blood-hungry things gain `+2` to find you for one day. |
| 32-33 | Your blood-art falters. All Blood Magic spells count as one rank lower for `D6` days. |
| 34-35 | One set of bandages, one waterskin, or one bloodied item within `NEAR` range grows hot, slick, or foul and becomes useless until cleaned or replaced. |
| 36-41 | Your blood beads, threads, or steams in the air around you as though tugged by an unseen hand. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | A demon smells your blood and takes interest. |
| 46 | A blood-borne magical disease spreads to you and one random other creature at `ARM'S LENGTH`, with Virulence `2 +` the Willpower spent on the spell. |
| 51 | The spell catches another body as well: ally, enemy, or vessel. |
| 52-55 | Blood bursts into your eyes and blinds you for a day. |
| 56 | Your soul recoils from what you have worked. Roll immediately on the Horror critical injury table. |
| 61 | The blood-force breaks your frame. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: the bond reverses, the curse rebounds, the vessel rejects you, or the flesh-shaping twists your own body. |
| 65 | Your blood crowns a new horror. Flesh and will split into a ravening blood-thing wearing your shape, and the character is effectively lost unless contained and remade by brutal means. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Death Magic Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The grave-breath spills elsewhere: at a random place in the same or a nearby hex, a grave is disturbed, livestock panic, or a charnel stench spreads. |
| 03-04 | The warmth of the living feels far away. You cannot benefit from `PERFORMANCE` or comforting words until dawn. |
| 05-06 | The dead keep speaking to you. Quiet rest, stealth, and concentration are all at `-2` until your next sleep. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Grave-cold clings to you. Roll three extra Base Dice on your next Death Magic spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your face, breath, or shadow grows corpse-like in some lasting way. |
| 22-23 | A `NEAR` or `FAR` area dims, chills, and reeks of grave-dust; plants wither and open flames burn low for one Quarter Day. |
| 24-25 | Grave-cold settles in your limbs. You count as `COLD` until you warm yourself by fire, spell, or proper shelter. |
| 26-31 | Animals and mounts shy from you. Handling them is at `-2` for one Quarter Day. |
| 32-33 | Your death-craft falters. All Death Magic spells count as one rank lower for `D6` days. |
| 34-35 | One ration cache, herb pouch, waterskin, or candle bundle within `NEAR` range spoils, blackens, or gutters out. |
| 36-41 | Your flesh pales, your breath smokes cold, and the smell of grave-earth rolls outward from you. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Your magic attracts a hungry dead thing, wraith, or demon. |
| 46 | Rot, spoilage, or contagion spreads through the immediate area for one Quarter Day. |
| 51 | The dead touch a friend or wrong victim as well. |
| 52-55 | Death-smoke blinds you for a full day. |
| 56 | The necrotic force ravages your mind. Roll immediately on the Horror critical injury table. |
| 61 | Death snaps through your body. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: your drain hits you, the corpse rises hostile, the darkness traps allies, or the wrong soul is stirred. |
| 65 | Death settles into you and will not leave. You remain animate, but only as a corpse-bound thing of cold will and grave-hunger; the character is lost unless the party can somehow drag them back to life. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Elemental Magic Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The spell discharges elsewhere: at a random place in the same or a nearby hex, a stray fireball, waterspout, gust-blast, or earth-heave hits without warning. |
| 03-04 | The wrong element answers your mood. At the GM's call, nearby fire gutters, wind gusts, water sloshes, or earth shifts around you for one scene. |
| 05-06 | Natural cover no longer trusts you. The next time you shelter behind stone, water, flame, or windbreak, it fails, shifts, or exposes you. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Wild elemental charge builds in you. Roll three extra Base Dice on your next Elemental spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | The element leaves a lasting mark on your body, scent, or voice. |
| 22-23 | A `NEAR` or `FAR` area erupts in rogue flame, mud, razor wind, or sudden floodwater and becomes a fresh tactical hazard. |
| 24-25 | One element clings to you violently: soaked, smoking, dust-caked, wind-lashed, or burning-hot. Relevant actions are at `-2` until you clear it. |
| 26-31 | Your next Elemental spell is unstable. If you cast one before your next rest, its mishap D66 roll gains `+10`. |
| 32-33 | Your command of the elements falters. All Elemental spells count as one rank lower for `D6` days. |
| 34-35 | Metal grows hot or numbingly cold, paper chars, oils spill, waterskins burst, or loose gear is flung from hands within `NEAR` range. |
| 36-41 | Fire, ash, spray, grit, or gale crowns you in a sudden mantle of raw, unruly element. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | An elemental spirit or analogous being is drawn to the disturbance. |
| 46 | The zone becomes unstable with sparks, waves, cracks, or violent gusts for one Quarter Day. |
| 51 | The elemental force also catches a friend or wrong target. |
| 52-55 | Flash, ash, spray, or sand blinds you for a day. |
| 56 | The wild surge tears at your mind. Roll immediately on the Horror critical injury table. |
| 61 | The elemental force breaks your bones. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: fire spreads wrong, the ground opens under allies, the air leaves your lungs, or the flood splits your line. |
| 65 | The elements unmake your human form. You become a raging knot of fire, flood, gale, or broken earth, no longer fit for play unless some epic binding or restoration is achieved. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Ice Affinity Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | Winter breaks loose elsewhere: at a random place in the same or a nearby hex, a door freezes shut, a stream skins over, or a sudden frost kills the warmth. |
| 03-04 | Speech above a whisper hurts, and shouted coordination is impossible until dawn. |
| 05-06 | Winter seizes you in a shiver-fit. At the start of the next encounter, you lose your first fast action unless fully warmed. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Killing cold nests in you. Roll three extra Base Dice on your next Ice spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Frost leaves a lasting mark on hair, eyes, breath, or skin. |
| 22-23 | A `NEAR` or `FAR` area turns slick with ice, white with rime, or half-blinded by frost haze for one Quarter Day. |
| 24-25 | Your grip goes numb. Bows, picks, and delicate hand tasks are at `-2` until you warm your hands. |
| 26-31 | Hoarfrost clings to your tracks and breath. `STEALTH` is at `-2`, and tracking you is `+2`, for one Quarter Day. |
| 32-33 | Your winter-craft falters. All Ice Affinity spells count as one rank lower for `D6` days. |
| 34-35 | Waterskins freeze, bowstrings stiffen, oils thicken, and metal rims bite bare skin within `NEAR` range. |
| 36-41 | Rime races over your skin and gear, and your eyes shine with a hard winter glaze. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Predators, hunters, or winter spirits find your trail. |
| 46 | A whiteout, glaze, or bitter chill grips the area for the next Quarter Day. |
| 51 | A friend is trapped, frozen, or cut off by the miscast ice. |
| 52-55 | Snow glare or ice-flash blinds you for a full day. |
| 56 | The frozen calm cracks your mind. Roll immediately on the Horror critical injury table. |
| 61 | The cold seizes and breaks your body. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: the wrong path freezes over, allies are trapped, supplies freeze, or your shelter fails. |
| 65 | Winter takes you alive. Your body becomes a cold-bound idol of ice and half-stopped breath, preserved but unplayable unless the party can thaw and restore what the cold has claimed. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Nature Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The green spills elsewhere: at a random place in the same or a nearby hex, roots buckle a path, bees swarm, or a tree bursts into violent bloom. |
| 03-04 | Green mercy blunts your will. Until dawn, you cannot willingly destroy a harmless plant, nest, or beast without first passing `INSIGHT`. |
| 05-06 | Leaves whisper in your ear. You cannot keep still enough for patient watch or careful aim; `SCOUTING` and `MARKSMANSHIP` are at `-2` for one scene. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Wild sap and storm-power surge in you. Roll three extra Base Dice on your next Nature spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | The green leaves a lasting mark on your body or scent. |
| 22-23 | A `NEAR` or `FAR` area overgrows, fogs over, or fills with stinging brush, roots, and pollen for one Quarter Day. |
| 24-25 | Roots and briars seem to catch at your ankles. `RUN` becomes a slow action until your next rest. |
| 26-31 | Pollen, sap, and leaf-scent cling to you. `STEALTH` is at `-2` and beasts notice you easily for one Quarter Day. |
| 32-33 | Nature turns from you. All Nature spells count as one rank lower for `D6` days. |
| 34-35 | One wooden tool, one bow or bundle of shafts, or one wrapped food cache within `NEAR` range sprouts, mildews, splits, or tangles. |
| 36-41 | Leaves, roots, spores, or thorny shoots stir and lean toward you as if the wild itself has marked you. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Spirits, predators, or territorial beasts are drawn in. |
| 46 | Growth, fog, vermin, or bad weather turn the area hostile for one Quarter Day. |
| 51 | A friend is also struck, tangled, lost, or exposed by the backlash. |
| 52-55 | Spores, pollen, fog, or sap blind you for a day. |
| 56 | The wild's indifference crushes your mind. Roll immediately on the Horror critical injury table. |
| 61 | Branch, root, or lightning batters your body. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: friendly growth traps you, the wrong path opens, the servant turns feral, or stormfire falls where it should not. |
| 65 | The wild roots you where you stand. Flesh, bark, thorn, and nest merge into one living shrine of the green, and your character is no longer a free adventurer unless torn back out of it. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Swarm Magic Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The swarm spills elsewhere: at a random place in the same or a nearby hex, a storehouse, camp, or byre erupts with sudden infestation. |
| 03-04 | Hive-thought bleeds out of you. Nearby creatures can read your mood from the buzzing around you. |
| 05-06 | Your skin will not stop crawling. In the next encounter, you must spend your first fast action brushing at yourself unless harmed first. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | The hive hums through your bones. Roll three extra Base Dice on your next Swarm spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | You gain a lasting insectile tell: scent, chittering breath, skittering shadow, or blackened eyes. |
| 22-23 | A `NEAR` or `FAR` area fills with stinging insects, crawling vermin, or choking moth-clouds for one Quarter Day. |
| 24-25 | Crawling bodies distract your hands and eyes. `MARKSMANSHIP`, locks, and delicate work are at `-2` until you clear them off. |
| 26-31 | You carry a pheromone trail. Vermin, swarms, and things that feed on them can track you at `+2` for one day. |
| 32-33 | Your swarm-craft falters. All Swarm spells count as one rank lower for `D6` days. |
| 34-35 | One ration bag, one bedroll, one saddlebag, or one packet of papers within `NEAR` range is infested, webbed, or nibbled through. |
| 36-41 | A living mantle of flies, beetles, rats, or spiders boils over you before scattering underfoot. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | A greater swarm, giant vermin, or swarm-feeding horror is drawn to you. |
| 46 | Infestation, webs, stink, or larval spill fouls the area for one Quarter Day. |
| 51 | A friend is also cocooned, bitten, revealed, or cut off by the swarm. |
| 52-55 | Insects flood your eyes and blind you for a day. |
| 56 | The hive tears at your reason. Roll immediately on the Horror critical injury table. |
| 61 | Swarm-weight and panic batter your body. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: your swarm turns, allies are infested, webs trap the wrong side, or your body starts to come apart into vermin. |
| 65 | The colony claims you as host and throne. Your body becomes a crawling nest ruled by a hive-will, and your character is effectively gone unless burned out, cut open, or miraculously purged. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Magma Song Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The magma-song lashes out elsewhere: at a random place in the same or a nearby hex, a hearth flares, a vent opens, or a sudden burst of fire scorches the wrong place. |
| 03-04 | Your temper rises like a vent. `MANIPULATION` is at `-2`, but intimidation gains `+1`, until dawn. |
| 05-06 | You leave ember-traces behind. Flammable things you linger near may begin to smoke or kindle at the GM's call this scene. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Fire, ash, and pressure build in you. Roll three extra Base Dice on your next Magma Song spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your body takes a lasting volcanic mark. |
| 22-23 | A `NEAR` or `FAR` area fills with ash, smoke, cinders, steam, or fresh heat-cracks and becomes a new hazard. |
| 24-25 | Heat-shimmer ruins your eye and hand. Ranged attacks and fine work are at `-2` until you cool down. |
| 26-31 | Smoke lives in your lungs. `STEALTH`, speech, and long exertion are at `-2` until your next rest. |
| 32-33 | Your magma-song falters. All Magma Song spells count as one rank lower for `D6` days. |
| 34-35 | Metal turns searing, wax and glue soften, paper chars, and drink turns hot in hand within `NEAR` range. |
| 36-41 | Heat blooms around you, cinders leak from your mouth, and ember-light shows in the seams of your skin. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Something ancient below notices your call. |
| 46 | Smoke, ash, embers, or softening stone make the area hazardous for one Quarter Day. |
| 51 | A friend is also scorched, cut off, or exposed by the mishap. |
| 52-55 | Ash and glare blind you for a day. |
| 56 | The fury of the deep ravages your mind. Roll immediately on the Horror critical injury table. |
| 61 | The backlash breaks your body. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: lava breaks wrong, wildfire spreads, steam bursts on allies, or your escape route melts. |
| 65 | The deep fire hollows you out. You remain standing as a cracked shell full of heat and molten light, a walking eruption rather than a playable person unless somehow quenched and restored. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Mentalism Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The thought-strike lands elsewhere: at a random place in the same or a nearby hex, panic, confusion, or shared hallucination seizes a small group. |
| 03-04 | Your tone goes wrong and cold. `MANIPULATION` is at `-2` except for threats and raw commands. |
| 05-06 | A false certainty lodges in your mind. The GM states the wrong assumption openly; until it is disproved or until dawn, rolls that rely on that assumption are at `-2`. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Unstable thought-power churns in you. Roll three extra Base Dice on your next Mentalism spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | Your eyes, voice, or manner are permanently altered in some unsettling mental way. |
| 22-23 | A `NEAR` or `FAR` area fills with false whispers, mirrored doubles, or creeping doubt; command and coordination there suffer `-2` for one turn. |
| 24-25 | Your attention skips at the wrong moment. You lose one success from your next `LORE`, `INSIGHT`, or `MANIPULATION` roll. |
| 26-31 | Your surface thoughts leak into your face and voice. Deception is impossible until dawn. |
| 32-33 | Your mind-craft falters. All Mentalism spells count as one rank lower for `D6` days. |
| 34-35 | Written orders, letters, tally marks, masks, mirrors, or tokens within `NEAR` range shift meaning, show lies, or become briefly untrustworthy. |
| 36-41 | Your stare goes utterly wrong, and your voice lands in other minds a breath before your lips move. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Other minds, spirits, or hostile thinkers notice the breach. |
| 46 | Illusion, confusion, or mental static spills into the area for one Quarter Day. |
| 51 | A friend or wrong witness is also caught in the mind-working. |
| 52-55 | A snap of white pain blinds you for a day. |
| 56 | The feedback ravages your mind. Roll immediately on the Horror critical injury table. |
| 61 | The seizure of will breaks your frame. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: your command binds you, your disguise slips, the wrong memories are cut loose, or your double turns on you. |
| 65 | Your self is overwritten. Something clever still speaks through your mouth, but your own will is gone beneath command, echo, and borrowed thought unless violently restored. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Oneiromancy Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The dream spills elsewhere: at a random place in the same or a nearby hex, sleepers wake screaming, fall comatose, or wander in their sleep. |
| 03-04 | Sleep keeps pulling at you. If you spend a Quarter Day idle, you nod off unless shaken awake. |
| 05-06 | Sleepers murmur your name. Resting or sneaking near sleeping folk is at `-2` for one Quarter Day. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Dream-stuff clings to you. Roll three extra Base Dice on your next Oneiromancy spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | You carry a lasting dream-mark: distant eyes, sleepwalking habits, sand in the voice, or cold from the other side. |
| 22-23 | A `NEAR` or `FAR` area falls under a drowsy hush, nightmare murmur, or drifting sandman haze for one Quarter Day. |
| 24-25 | Waking lag clings to you. Your first action in the next encounter loses one success or is taken at `-2`, GM's call. |
| 26-31 | Dream-stain clouds the real world. `SCOUTING` and `INSIGHT` are at `-2` until you sleep again. |
| 32-33 | Your dream-craft falters. All Oneiromancy spells count as one rank lower for `D6` days. |
| 34-35 | Charms, maps, letters, sketches, candles, and timepieces within `NEAR` range blur, dim, stop, or become dream-touched and unreliable. |
| 36-41 | The light dims around you and dream-images bleed across your face and shadow like a waking nightmare. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Something from dream or astral dark notices and approaches. |
| 46 | Dreams spill into waking life around you for one Quarter Day. |
| 51 | A friend is also caught in sleep, prophecy, or dream-leak. |
| 52-55 | You wake blind for the next full day. |
| 56 | Nightmare ravages your mind. Roll immediately on the Horror critical injury table. |
| 61 | Your sleeping body thrashes itself to harm. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: you sleepwalk, prophecy misleads you, dream travel lands wrong, or a created dream-form turns loose. |
| 65 | You do not fully wake again. Your body lingers, but your self is lost in dream, nightmare, and wandering sleep unless the party can find and reclaim you beyond the veil of rest. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Magnetism Mishaps

| D66 | Effect |
| --- | --- |
| 01-02 | The pull strikes elsewhere: at a random place in the same or a nearby hex, a bell peals, a gate slams, a cart overturns, or armor is yanked from its rack. |
| 03-04 | The field pulls your sense of direction askew. Leading the way or navigating is at `-2` until dawn. |
| 05-06 | You cannot easily let go of held metal. Dropping or handing off metal gear takes a slow action for one scene. |
| 11-13 | The spell drains `1D3` extra WP from you. |
| 14-15 | Static rage clings to you. Roll three extra Base Dice on your next Magnetism spell, but if that casting causes a mishap its D66 roll gains `+10`; until then, you cannot benefit from `SLEEP`. |
| 16-21 | The field leaves a lasting metallic tell in your body or gear. |
| 22-23 | A `NEAR` or `FAR` area becomes a violent pull-field of clattering metal, flying nails, and slamming hinges for one turn. |
| 24-25 | Iron drags at your gait. If you wear armor or carry heavy metal, `MOVE` is at `-2` until your next rest. |
| 26-31 | Static crackles over you. `STEALTH` is at `-2`, and small metal objects cling to your clothes and skin. |
| 32-33 | Your iron-craft falters. All Magnetism spells count as one rank lower for `D6` days. |
| 34-35 | Blades leap, mail tugs, buckles snap, keys jump rings, and iron tools wrench from belts within `NEAR` range. |
| 36-41 | Nails, buckles, blades, and iron scraps twitch and rattle toward you as though claimed by a buried force. This triggers a `FEAR` attack against all unprepared non-allied witnesses. |
| 42-45 | Something metal-bound, warlike, or arcane takes notice. |
| 46 | Nearby metal becomes unstable, flying, dragging, or clattering for one Quarter Day. |
| 51 | A friend is also pinned, disarmed, dragged, or exposed. |
| 52-55 | Flashing sparks blind you for a day. |
| 56 | The magnetic surge ravages your mind. Roll immediately on the Horror critical injury table. |
| 61 | The recoil batters your bones and joints. Roll immediately on the Blunt critical injury table. |
| 62-64 | The spell backfires: armor crushes, weapons whirl loose, polarity flips, or the wrong target is hurled. |
| 65 | Iron claims your flesh. Metal fuses into bone and sinew until you become a locked, half-living relic of strain and magnetism, no longer fit for adventuring unless broken apart and remade. |
| 66 | Your magic tears open a rift to another dimension, and a demon drags you through it. Make a new character. After `D66` days, the old one may return as a changed NPC. |

## Shared Severity Logic

After the rebalance pass, the integrated tables follow this common danger ladder:

- `01-02`: stray discharge elsewhere
- `03-06`: social, perceptual, or coordination trouble
- `11-15`: extra strain and unstable magical carry-over
- `16-23`: lasting tell or local area disturbance
- `24-31`: direct tactical impairment
- `32-35`: path degradation or meaningful item loss
- `36-46`: spectacle, notice, contamination, or zone pressure
- `51-64`: collateral harm, sensory denial, critical injury, or full backfire
- `65-66`: catastrophic loss

This matters because extra `💀` add `+10` to the mishap result. The table must therefore escalate in a way that players can feel and trust.

## Why This Works Better

- Every path still uses the same `20` D66 result bands as the original system.
- General spells now have their own mishap table instead of borrowing another discipline's identity.
- Lower bands now hold outcomes that are disruptive without being silently campaign-wrecking.
- Stronger visual effects, notice from hostile powers, hard collateral damage, and critical injuries now sit where escalating mishaps should land.
- Each discipline still fails in its own idiom instead of collapsing back into one generic mishap voice.

## Audit Revisions

- `11-13` is now consistently extra `WP` drain instead of spectacle.
- `36-41` now holds the major visible backlash and `FEAR` attack band.
- `42-45` now carries outside notice, pursuit, or approaching complication.
- `61` now consistently carries blunt critical injury instead of open-ended referee threat.
- `65` remains path-themed catastrophe and `66` remains the hard core fate.
- Stone Song, Ice Affinity, and Magnetism had their lowest bands retuned so the gentlest slot does not carry the sharper tactical punishment.
- Shapeshifting `05-06` now preserves player agency by forcing a cost to master the impulse instead of handing full temporary control to the GM.

## Restored `66` Core Fate

- `66` now matches the core fate across every path mishap table: the caster is dragged through a rift by a demon, the player makes a new character, and the old one may return after `D66` days as a changed NPC.
- `65` is reserved for path-themed catastrophic fates that leave the caster ruined, transformed, possessed, bound, or otherwise lost to ordinary adventuring.
