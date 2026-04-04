<!-- markdownlint-disable MD013 -->

# Proposal - Realistic Critical Injuries

Goal: make catastrophic injuries feel more realistic, more feared, and more consequential without adding a slow medical minigame. The core change is simple: `65` no longer means "dead on the spot." It means "you survived the killing blow badly enough to carry it for the rest of your life." `66` remains the result for immediate destruction that no field treatment can realistically reverse.

Scope for this draft: rework the existing physical critical injury framework that already lives in Chapter 6. This proposal is written to slot into the current slash, stab, blunt, and burn structure first. Wider new families such as poison, corrosion, freezing, and swallow trauma are useful future material, but they should not be treated as part of the core integration pass unless Chapter 6 is being rebuilt more broadly.

## Design Principles

- Keep the core trigger unchanged: you still roll a critical injury when Broken.
- Keep the table readable at the table: one extra roll only on the rarest catastrophic result.
- Separate survivable catastrophe from true annihilation.
- Make permanent injuries medically plausible for the damage type that caused them.
- Let some outcomes leave a character alive but mechanically hanging on by reducing the governing attributes to `1`.
- Preserve value for existing recovery tools such as `PHYSICIAN`, `LUCKY`, and `REGENERATION`.
- Stay inside existing Chapter 6 and Chapter 7 procedures wherever possible instead of introducing parallel subsystems.

## Core Rule Change

When a PC rolls `65` on a physical critical injury table, do not resolve the old immediate-death result. Instead:

1. The victim suffers a catastrophic wound and falls helpless.
2. The victim must still be saved with a `HEALING` roll if the entry is marked lethal.
3. If saved, roll on the matching permanent injury subtable for that damage type.
4. The permanent injury result replaces the old `65` result.
5. A `66` result is still immediate death or unrecoverable bodily destruction.

This creates three clear end states:

- `63-64`: lethal but often survivable with fast aid.
- `65`: survivable catastrophe with permanent consequences.
- `66`: true terminal trauma.

Compatibility note:

- `LUCKY` rank `4` still downgrades permanent injury to long healing.
- `PHYSICIAN` rank `3` can still turn a permanent injury into a healed result if initial care was applied in time.
- `MEND WOUNDS` still heals a critical injury, but it does not regrow limbs or erase catastrophic bodily loss beyond what the spell already allows.
- `REGENERATION` remains the premium magical answer to permanent ruin.

## Recommended Rework To The Parent Tables

Use the following parent-table logic.

| Table | `65` result | `66` result |
| --- | --- | --- |
| Slash | Catastrophic slash trauma. `HEALING` within `D6 rounds`; on success roll on Permanent Injuries - Slash. | Decapitation or full cranial destruction. Immediate death. |
| Stab | Catastrophic penetrating trauma. `HEALING` within `D6 rounds`; on success roll on Permanent Injuries - Stab. | Heart destroyed or brain transfixed. Immediate death. |
| Blunt | Catastrophic crushing trauma. `HEALING` within `D6 rounds`; on success roll on Permanent Injuries - Blunt. | Skull pulped, neck snapped beyond recovery, or torso crushed. Immediate death. |
| Burn | Catastrophic burn or frost trauma. `HEALING` within `D6 rounds`; on success roll on Permanent Injuries - Burn. | Body destroyed beyond survival. Immediate death. |

Notes:

- The short time limit reflects the fact that these are "would have died without immediate intervention" injuries.
- If the table already had a harsher or more specific time limit that better fits the wound, keep the harsher limit.
- Magic that explicitly reverses permanent injuries still works as written.

## Permanent Injury Severity Bands

These subtables should feel like a downward slide from grievous disability to attribute-collapse survival.

| Band | Range | Severity | Use |
| --- | --- | --- | --- |
| I | `11-26` | Survivable maiming | Lasting penalties, chronic pain, reduced load or speed, but still playable. |
| II | `31-46` | Major structural loss | Lost eye, crushed joint, ruined hand, organ damage, fertility loss, or partial paralysis. |
| III | `51-62` | Severe crippling | Lost limb, pelvic/spinal damage, catastrophic brain trauma, or dependence on constant care. Some results here should retire the adventurer by default. |
| IV | `63-66` | Attribute-collapse survival | The character lives, but one or more governing attributes are permanently reduced to `1`. These results are often retirement-default even when survival is technically possible. |

## Permanent Injuries - Slash

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-12 | Deep abdominal scarring | `-1` to `ENDURANCE`; each failed disease roll also inflicts `1` Agility damage. |
| 13-14 | Ruined forearm | Cannot use two-handed weapons; `-2` to tasks needing fine hand work with that arm. |
| 15-16 | Loss of one eye | `-2` to `MARKSMANSHIP`; `-1` to `SCOUTING`. |
| 21-22 | Split jaw | `-2` to `MANIPULATION`; eating hard rations takes twice as long. |
| 23-24 | Slashed hamstring | `RUN` is always a slow action; `-1` to `MOVE`. |
| 25-26 | Opened flank | `-1` to `MIGHT` and `ENDURANCE`; armor above rating `6` causes pain and fatigue after one Quarter Day. |
| 31-32 | Lost hand | Cannot use shields or two-handed weapons with that side; climbing and swimming are `-2`. |
| 33-34 | Lost foot | `RUN` is always a slow action; forced marches count as one category harsher. |
| 35-36 | Loss of hearing in one ear | `-2` to `SCOUTING` when sound is the main clue, and `SCOUTING` to notice unseen approach is `-1`. |
| 41-42 | Severed arm above elbow | That arm is lost; most martial careers continue only with major adaptation. |
| 43-44 | Severed leg above knee | You cannot travel or fight effectively without a crutch, mount, or prosthetic support. |
| 45-46 | Neck scarring and airway collapse | `-2` to `ENDURANCE`; after any sprint, charge, or forced march, take `1` Strength damage. |
| 51-52 | Chronic abdominal hernia | Every heavy lift, grapple, or forced march requires `ENDURANCE`; failure inflicts `1` Strength damage. |
| 53-54 | Facial disfigurement | `-3` to `MANIPULATION` except intimidation, which gains `+1`. |
| 55-56 | Loss of dominant arm | That arm is gone and your `Agility` is permanently reduced to `1` unless magic restores the limb. |
| 61-62 | Belly-ruin | `-2` to `ENDURANCE` and `MOVE`; without a full Quarter Day of rest each day, lose `1` Strength by nightfall. |
| 63-64 | Neck-broken remnant | Alive and lucid, but your `Strength` and `Agility` are both permanently reduced to `1`. Retirement from active adventuring is the default. |
| 65-66 | Body-ruined remnant | The body barely holds together; your `Strength` and `Agility` are both permanently reduced to `1`, and each day of overland travel inflicts `1` Strength damage unless you ride or are carried. Retirement from active adventuring is the default. |

## Permanent Injuries - Stab

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-12 | Punctured bowel with adhesions | `-1` to `ENDURANCE`; disease rolls from tainted food or water are at `-2`. |
| 13-14 | Damaged kidney | After each forced march or day without full water, take `1` Strength damage. |
| 15-16 | Collapsed lung scar | `-2` to `ENDURANCE`; `RUN` twice in one round is impossible. |
| 21-22 | Ruined groin | `-1` to `MOVE`; any result that inflicts groin or hip trauma adds `+10` on future critical injury rolls. |
| 23-24 | Nerve-pierced hand | `-2` to one-handed weapon use on that side and to all delicate hand work. |
| 25-26 | Nerve-pierced foot | `RUN` is always a slow action; stealth in rough terrain is `-1`. |
| 31-32 | Destroyed eye | `-2` to `MARKSMANSHIP` and `SCOUTING`; ranged ambushes against you gain `+1`. |
| 33-34 | Reopened bleeding | At the end of any combat where you took Strength damage, roll `ENDURANCE` or suffer `1` extra Strength damage. |
| 35-36 | Scarred throat | `-2` to `MANIPULATION`; power words and shouted coordination cannot be used above a rasp. |
| 41-42 | Transfixed shoulder | Two-handed weapons cannot be used; shields on that side give one less Armor. |
| 43-44 | Ruined liver or spleen | `-2` to resist poison, disease, and alcohol; recovery from any sickness takes one extra success. |
| 45-46 | Pierced pelvis | `MOVE` and `ENDURANCE` are both `-2`; riding and long marches inflict `1` Agility damage per Quarter Day. |
| 51-52 | Loss of hand or forearm | The limb is gone; treat as a severe martial disability. |
| 53-54 | Loss of foot or lower leg | Movement beyond cautious travel requires support, prosthetics, or a mount. |
| 55-56 | Shredded bowel and bladder | Your `Strength` is permanently reduced to `1`; infection, diet, and strain now threaten to Break you immediately. |
| 61-62 | Spinal puncture | Your `Agility` is permanently reduced to `1`. |
| 63-64 | Penetrating brain trauma | Your `Strength` and `Agility` are both permanently reduced to `1`; memory and speech problems may remain as roleplay fallout. Retirement from active adventuring is the default. |
| 65-66 | Heart kept beating, life not restored | The body survives on the edge of failure; your `Strength` and `Agility` are both permanently reduced to `1`. Retirement from active adventuring is the default. |

## Permanent Injuries - Blunt

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-12 | Crushed ribs that healed badly | `-1` to `ENDURANCE`; each failed `ENDURANCE` roll also inflicts `1` Strength damage. |
| 13-14 | Permanently dislocated shoulder | Two-handed weapons are impossible without bracing; climbing is `-2`. |
| 15-16 | Crushed elbow | `-2` to melee attacks or crafting that use that arm. |
| 21-22 | Crushed knee | `RUN` is always a slow action; `MOVE` is `-2`. |
| 23-24 | Pelvic fracture | Riding, sprinting, and forced marches each inflict `1` Agility damage unless you rest afterward. |
| 25-26 | Facial bone collapse | `-2` to `MANIPULATION`; helmets and face protection no longer fit properly. |
| 31-32 | Rattled wits | `-1` to all `Wits` rolls and `SCOUTING`; each horror critical adds `+10`. |
| 33-34 | Crushed hand | Cannot use shields or two-handed weapons on that side; delicate work is impossible. |
| 35-36 | Crushed foot | `RUN` becomes a slow action, and forced marches count as one category harsher for you. |
| 41-42 | Destroyed hip | Without a crutch or mount you cannot take part in a forced march and cannot keep pace with healthy walkers for more than one Quarter Day. |
| 43-44 | Damaged spine | `MIGHT`, `MOVE`, and `ENDURANCE` are each `-1`; heavy armor counts as one step heavier for you. |
| 45-46 | Skull-bruised wits | `Wits` maximum is reduced by `1`; memory, speech, or concentration deficits should be chosen with the player. |
| 51-52 | Arm rendered useless | The arm remains attached but cannot bear weight or fight effectively. |
| 53-54 | Leg rendered useless | The leg remains attached but cannot support travel or combat without aid. |
| 55-56 | Half-lamed | Below-the-waist movement requires assistance, cart transport, or a custom brace or chair. |
| 61-62 | Severe brain damage | The character survives, but reliable judgment, speech, and independence are gone. Retirement from active adventuring is the default. |
| 63-64 | High spinal paralysis | Your `Agility` is permanently reduced to `1`. Retirement from active adventuring is the default unless the campaign can support constant accommodation. |
| 65-66 | Crushed-torso remnant | Your `Strength` and `Agility` are both permanently reduced to `1`. Retirement from active adventuring is the default. |

## Permanent Injuries - Burn

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-12 | Contracture scars | `-1` to `MOVE`; armor rubs painfully after one Quarter Day of wear. |
| 13-14 | Heat-spoiled skin | Forced march, heat, and heavy armor each become one category harsher for you. |
| 15-16 | Burn blindness in one eye | `-2` to `MARKSMANSHIP`; bright light inflicts `-1` to all `SCOUTING`. |
| 21-22 | Dead nerves in one hand | Fine tool use is impossible; two-handed weapons are `-1`. |
| 23-24 | Dead nerves in one foot | `RUN` is always a slow action; balancing rolls are `-2`. |
| 25-26 | Airway burn | `-2` to `ENDURANCE`; smoke, dust, and cold weather trigger coughing fits. |
| 31-32 | Full facial scarring | `-3` to `MANIPULATION` except intimidation, which gains `+1`. |
| 33-34 | Ceaseless pain | Once per Quarter Day after a forced march, hard fight, or heavy labor, suffer `-1` to Strength-based rolls until you rest. |
| 35-36 | Partial hand amputation | That hand cannot hold a shield or a weapon securely. |
| 41-42 | Partial foot amputation | March pace is reduced and `RUN` is always slow. |
| 43-44 | Torso scar plate | You cannot wear rigid body armor; if forced to, take `1` Strength damage per Quarter Day. |
| 45-46 | Withered loins | The injury carries long-term personal consequences and leaves you fragile to cold, heat, and exhaustion. |
| 51-52 | Arm amputation | That arm is lost to the burn or frostbite. |
| 53-54 | Leg amputation | That leg is lost to the burn or frostbite. |
| 55-56 | Extensive body scarring | `MOVE`, `ENDURANCE`, and `MANIPULATION` are all `-1`; all weather is one category harsher. |
| 61-62 | Multi-limb contracture | You remain alive but cannot travel or fight without constant assistance. Retirement from active adventuring is the default. |
| 63-64 | Burned lungs and brain | Your `Strength` and `Agility` are both permanently reduced to `1`. Retirement from active adventuring is the default. |
| 65-66 | Living cinder | Your `Strength` and `Agility` are both permanently reduced to `1`, and all weather counts as one category harsher for you. Retirement from active adventuring is the default. |

## Future Expansion - Additional Damage Families

The current core book routes non-typical physical harm through Burn and handles poison separately. Because of that, the following material should be treated as future expansion, not as part of the first integration pass for this proposal.

If Chapter 6 is later rebuilt to split non-typical harms into their own parent tables, the families below are the right direction:

| Table | `65` result | `66` result |
| --- | --- | --- |
| Horror | Permanent terror. Roll on Permanent Trauma - Horror. | The mind or heart gives way entirely. Death or permanent `Wits 1` and `Empathy 1`. |
| Poison | Catastrophic venom or toxin. Roll on Permanent Injuries - Poison. | Total organ collapse or irreversible wit-ruin. Death or permanent helplessness. |
| Acid / Corrosion | Catastrophic corrosive harm. Roll on Permanent Injuries - Acid / Corrosion. | Destruction beyond survival. |
| Cold / Freeze | Catastrophic freezing harm. Roll on Permanent Injuries - Cold / Freeze. | Whole-body freezing, unsurvivable tissue death, or terminal collapse. |
| Swallow | Catastrophic maw-and-gut harm. Roll on Permanent Injuries - Swallow. | The victim is crushed, drowned, digested, or suffocated beyond rescue. |

## Critical Injuries - Horror

Design note: this table should model durable trauma responses seen after life-threatening events, especially intrusive memories and nightmares, avoidance and emotional numbing, hypervigilance and exaggerated startle, irritability and anger, concentration problems, detachment, and a bleak or foreshortened sense of the future. It should not drift into comic quirks or arbitrary phobias.

| D66 | Trauma | Lethal | Time Limit | Effects During Healing | Healing Time |
| --- | --- | --- | --- | --- | --- |
| 11-16 | Shaking hands | No | - | `-1` to all `Agility` rolls. | D6 |
| 21-26 | Intrusive flashbacks | No | - | The first clear reminder of the trauma each encounter costs you your next fast action unless you pass `INSIGHT`. | D6 |
| 31-36 | Sleepless vigilance | No | - | A Quarter Day spent sleeping only counts as `SLEEP` if the camp is secure and someone else stands watch. | D6 |
| 41-46 | Emotional withdrawal | No | - | `-2` to `MANIPULATION` when comforting, bonding with, or trusting others. | 2D6 |
| 51-52 | Exaggerated startle response | No | - | If surprised, charged, or struck by a sudden noise, you drop what is in one hand or lose your next fast action. | 2D6 |
| 53-54 | Mind-fugue | No | - | The first time you suffer damage or a fear attack in an encounter, roll `INSIGHT` or lose your next slow action. | 2D6 |
| 55-56 | Survivor's guilt | No | - | Whenever an ally becomes Broken, dies, or is abandoned, you suffer `1` Empathy damage. | 3D6 |
| 61-62 | Rage spiral | No | - | When cornered, grabbed, or ambushed, you must push your first violent roll if able. | 3D6 |
| 63-64 | Catatonic withdrawal | No | - | You do not speak, initiate action, or respond except to direct handling. | D6 |
| 65 | Lasting terror | No | - | Roll on Permanent Trauma - Horror. | Permanent |
| 66 | Broken mind or stopped heart | Yes | - | Death, or if the table wants survival, your `Wits` and `Empathy` are both permanently reduced to `1`. | - |

## Critical Injuries - Poison

Use this for venoms, inhaled toxins, alchemical poisons, and magical toxins that attack blood, nerves, lungs, or organs rather than just burning tissue.

| D66 | Injury | Lethal | Time Limit | Effects During Healing | Healing Time |
| --- | --- | --- | --- | --- | --- |
| 11-16 | Violent vomiting | No | - | You cannot recover Strength and must consume one extra ration of water each day. | D6 |
| 21-26 | Gut convulsions | No | - | `-1` to `MIGHT` and `ENDURANCE`. | D6 |
| 31-36 | Tremor | No | - | `-2` to `MARKSMANSHIP`, `SLEIGHT OF HAND`, and other delicate hand work. | D6 |
| 41-46 | Numb extremity | No | - | One limb is unreliable; either `RUN` becomes a slow action or two-handed weapons cannot be used. | 2D6 |
| 51-52 | Poison-burned lung | Yes | D6 days | `-2` to `ENDURANCE` and `MOVE`. | D6 |
| 53-54 | Liver shock | Yes | D6 days | Resistance rolls against disease, alcohol, and dehydration are at `-2`. | 2D6 |
| 55-56 | Seizure fit | Yes | D6 hours | The first time each day you take attribute damage, roll `ENDURANCE` or collapse and lose your next round. | 2D6 |
| 61-62 | Organ crisis | Yes | D6 hours | You cannot recover Strength or Agility except through magic. | 2D6 |
| 63-64 | Paralytic poisoning | Yes | D6 rounds | You cannot `MOVE`, `PARRY`, or `DODGE`. | D6 |
| 65 | Catastrophic poisoning | Yes | D6 hours | Roll on Permanent Injuries - Poison. | Permanent |
| 66 | Total organ collapse | Yes | - | Your organs fail beyond rescue. | - |

## Critical Injuries - Acid / Corrosion

Use this when the harm is true corrosion: acid, alchemical solvent, monster bile, or similar tissue-destroying fluid.

| D66 | Injury | Lethal | Time Limit | Effects During Healing | Healing Time |
| --- | --- | --- | --- | --- | --- |
| 11-16 | Surface chemical burns | No | - | `-1` to `MANIPULATION` or `MOVE`, depending on the hit location. | D6 |
| 21-26 | Mouth burns | No | - | `-1` to `MANIPULATION`; eating is slow and painful. | D6 |
| 31-36 | Eye splash | No | - | `-1` to `MARKSMANSHIP` and `SCOUTING`. | 2D6 |
| 41-46 | Scarred airway | Yes | D6 days | `-2` to `ENDURANCE` and `MOVE`. | D6 |
| 51-52 | Deep facial burns | Yes | D6 days | `-2` to `MANIPULATION`. | D6 |
| 53-54 | Deep abdominal burns | Yes | D6 hours | `1` point of damage at each roll for `MIGHT` and `ENDURANCE`. | D6 |
| 55-56 | Corroded hand or foot | Yes | D6 days | Two-handed weapons cannot be used, or `RUN` becomes a slow action. | 2D6 |
| 61-62 | Acid aspiration | Yes | D6 hours | `-2` to `ENDURANCE`, and you cannot shout above a rasp. | 2D6 |
| 63-64 | Perforated gut | Yes | D6 hours | Disease with Virulence `6`. | 2D6 |
| 65 | Catastrophic corrosion | Yes | D6 rounds | Roll on Permanent Injuries - Acid / Corrosion. | Permanent |
| 66 | Corroded through | Yes | - | Vital organs are destroyed beyond survival. | - |

## Critical Injuries - Cold / Freeze

Use this for freezing injury specifically, not just "weather exposure." This table should focus on frostbite, freezing nerve damage, circulation collapse, lung injury, and tissue death.

| D66 | Injury | Lethal | Time Limit | Effects During Healing | Healing Time |
| --- | --- | --- | --- | --- | --- |
| 11-16 | Numb fingers | No | - | Fine hand work is at `-1`. | D6 |
| 21-26 | Numb toes | No | - | `RUN` becomes a slow action. | D6 |
| 31-36 | Shivering collapse | No | - | `-1` to `MOVE` and `ENDURANCE`. | D6 |
| 41-46 | Frostbitten flesh | No | - | `-2` to `MANIPULATION` or `MOVE`, depending on the hit location. | D6 |
| 51-52 | Freezing lung | Yes | D6 days | `-2` to `ENDURANCE` and `MOVE`. | D6 |
| 53-54 | Deadened nerves | Yes | D6 days | Each pushed `Strength` roll that shows at least one 💀 inflicts `1` extra Strength damage. | D6 |
| 55-56 | Severe frostbite | Yes | D6 days | `RUN` becomes a slow action or two-handed weapons cannot be used, depending on the site. | 2D6 |
| 61-62 | Freezing delirium | Yes | D6 hours | `-2` to `Wits`, and you cannot reliably distinguish friend from foe without an `INSIGHT` roll. | D6 |
| 63-64 | Circulatory collapse | Yes | D6 rounds | You fall unconscious and begin dying unless rewarmed and treated. | D6 |
| 65 | Catastrophic freezing | Yes | D6 hours | Roll on Permanent Injuries - Cold / Freeze. | Permanent |
| 66 | Frozen solid | Yes | - | Whole-body freezing kills you outright. | - |

## Critical Injuries - Swallow

Use this when a victim is Broken while swallowed, pinned in a gullet, crushed in a crop, or churning in a monster's gut. This is mixed trauma: crushing, suffocation, infection, digestive chemistry, and panic in total confinement.

| D66 | Injury | Lethal | Time Limit | Effects During Healing | Healing Time |
| --- | --- | --- | --- | --- | --- |
| 11-16 | Choked and bruised | No | - | `-1` to `ENDURANCE`. | D6 |
| 21-26 | Cracked ribs | No | - | `-1` to `MOVE` and `MELEE`. | 2D6 |
| 31-36 | Acid-scarred flesh | No | - | `-1` to `MANIPULATION` or `MOVE`, depending on where the fluids burned you. | D6 |
| 41-46 | Aspirated filth | No | - | `-1` to `ENDURANCE`, and swimming or drowning checks are at an additional `-1`. | D6 |
| 51-52 | Crushed arm | No | - | Two-handed weapons cannot be used. | 2D6 |
| 53-54 | Crushed leg | No | - | `RUN` becomes a slow action. | 2D6 |
| 55-56 | Gut-rot infection | Yes | D6 days | Disease with Virulence `6`. | 2D6 |
| 61-62 | Air-starved | Yes | D6 rounds | `-2` to `Wits` and `ENDURANCE`. | D6 |
| 63-64 | Pelvic or spinal crush | Yes | D6 hours | `-2` to `MOVE` and `MELEE`. | 2D6 |
| 65 | Catastrophic gut-maw harm | Yes | D6 rounds | Roll on Permanent Injuries - Swallow. | Permanent |
| 66 | Crushed, drowned, or digested | Yes | - | You do not come back out alive. | - |

## Permanent Trauma - Horror

This is the catastrophic follow-up table for `65` on the Horror main table.

| D66 | Permanent Trauma | Lasting Effect |
| --- | --- | --- |
| 11-16 | Night terrors | After each Quarter Day spent sleeping, roll `INSIGHT`. On a failure, the sleep does not count as `SLEEP`, and you wake the camp. |
| 21-26 | Never off watch | You are never off watch. You gain `+1` to `SCOUTING` to notice ambush or unseen approach, but you cannot recover `Wits` from sleep unless another person relieves you and you are in a secure shelter. |
| 31-36 | Exaggerated startle response | The first sudden noise, charge, or fear effect in each encounter costs you your next fast action unless you pass `INSIGHT`. |
| 41-46 | Avoidance loop | When confronted with a clear reminder of the original horror, roll `INSIGHT`. On a failure, you must withdraw, freeze, or refuse to engage for one round. |
| 51-54 | Emotional numbing | You no longer gain Willpower from `PERFORMANCE`, comfort, or acts of fellowship, and all `MANIPULATION` rolls to form or repair bonds are at `-2`. |
| 55-56 | Mind-fugue under stress | The first time in an encounter that you suffer damage or a fear attack, roll `INSIGHT` or lose your next slow action as the world goes distant and unreal. |
| 61-62 | Survivor's guilt | Whenever an ally becomes Broken, dies, or is left behind, suffer `1` Empathy damage and lose `1` WP. |
| 63-64 | Rage reaction | When cornered, surprised, or physically grabbed, you must push your first violent roll if able. If no enemy is reachable, you lash out verbally or physically at the nearest creature. |
| 65 | Sleep will not keep you | You cannot benefit from ordinary sleep without herbs, drink, narcotics, magic, or a trusted watcher to soothe you. Without help, every dawn costs you `1` Wits. |
| 66 | Fractured self | Your `Wits` and `Empathy` are both permanently reduced to `1`. You can still speak and make choices, but any further mental damage Breaks you immediately. Retirement from active adventuring is often the soundest choice. |

## Permanent Injuries - Poison

This is the catastrophic follow-up table for `65` on the Poison main table.

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-16 | Damaged gut and appetite | Food sits badly. You must consume one extra ration during each full day of travel or suffer `1` Strength damage by nightfall. |
| 21-26 | Hand tremor | `MARKSMANSHIP`, `SLEIGHT OF HAND`, and delicate crafting are at `-2`. |
| 31-36 | Nerve pain | At the start of each encounter, roll `ENDURANCE`. On a failure, one limb is wracked with pain and suffers `-2` to related actions for the fight. |
| 41-46 | Liver or kidney damage | Alcohol, disease, dehydration, and forced march resistance rolls are all at `-2`. |
| 51-54 | Scarred lungs | `ENDURANCE` is `-2`, and inhaled smoke, spores, or gas immediately inflict `1` extra Strength damage. |
| 55-56 | Falling fits | The first time each day that an attribute reaches `0`, roll `ENDURANCE`. On a failure, you collapse and lose your next round. |
| 61-62 | Ruined hand or foot | A poisoned limb withers or is amputated; treat as loss of hand or foot, depending on the original wound. |
| 63-64 | Half-lamed | The toxin leaves lasting nerve death. `MOVE` and one of `MELEE` or `MARKSMANSHIP` are both `-2`, and travel without a crutch, litter, or mount is slow. |
| 65 | Organ-ruin remnant | Your `Strength` is permanently reduced to `1`. Active adventuring usually ends unless the campaign can support constant care. |
| 66 | Wit-ruined by poison | Your `Strength` and `Agility` are both permanently reduced to `1`, and tremor or confusion may remain as roleplay fallout. Retirement from active adventuring is the default. |

## Permanent Injuries - Acid / Corrosion

This is the catastrophic follow-up table for `65` on the Acid / Corrosion main table.

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-16 | Scarred mouth and gullet | `MANIPULATION` is `-2`, and shouting warnings or power words is impossible above a rasp. |
| 21-26 | Scarred gullet | Eating takes twice as long, hard rations are painful, and every forced march requires `ENDURANCE` or inflicts `1` Strength damage from retching and exhaustion. |
| 31-36 | Scarred lungs from aspiration | `ENDURANCE` is `-2`, and any smoke, dust, drowning, or sprint test is rolled at an additional `-1`. |
| 41-46 | Blinded eye | `MARKSMANSHIP` is `-2` and `SCOUTING` is `-1`. |
| 51-54 | Facial and neck disfigurement | `MANIPULATION` is `-3` except intimidation, which gains `+1`. Helmets and face coverings must be specially altered to fit. |
| 55-56 | Abdominal adhesions | Heavy lifting, grappling, and forced marching require `ENDURANCE`; failure inflicts `1` Strength damage. |
| 61-62 | Destroyed hand | The hand is lost or permanently unusable. |
| 63-64 | Destroyed foot or lower leg | The foot is lost or permanently unusable; travel now requires a crutch, prosthetic, or mount. |
| 65 | Gullet-ruined remnant | Your `Strength` is permanently reduced to `1`, and ordinary food or drink can no longer be taken comfortably. Active adventuring usually ends unless the campaign can support constant accommodation. |
| 66 | Corrosive ruin | Your `Strength` and `Agility` are both permanently reduced to `1`. |

## Permanent Injuries - Cold / Freeze

This is the catastrophic follow-up table for `65` on the Cold / Freeze main table.

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-16 | Cold hypersensitivity | Treat all environmental cold as one step harsher than it is for you. |
| 21-26 | Numb fingers | Fine hand work is at `-2`, and you cannot comfortably use bows or two-handed weapons in cold weather. |
| 31-36 | Numb toes | `RUN` is always a slow action, and balancing or climbing in cold conditions is at `-2`. |
| 41-46 | Stiffened joints | `MOVE` is `-1` normally and `-2` in winter or rain. |
| 51-54 | Neuropathic pain | At first exposure to bitter cold each day, suffer `1` Agility damage unless you pass `ENDURANCE`. |
| 55-56 | Failing blood | Each time you become `COLD`, you immediately take `1` extra Strength damage and recover that Strength only after a full Quarter Day in dry shelter and warmth. |
| 61-62 | Loss of fingers or hand | One hand is partly or wholly lost to frostbite. |
| 63-64 | Loss of toes or foot | One foot is partly or wholly lost to frostbite. |
| 65 | Recurrent freezing injury | Your `Agility` is permanently reduced to `1`, and each time you become `COLD` you also take `1` Strength damage. Winter campaigning becomes near-impossible without unusual support. |
| 66 | Multi-site freezing ruin | Your `Strength` and `Agility` are both permanently reduced to `1`. Retirement from active adventuring is the default. |

## Permanent Injuries - Swallow

This is the catastrophic follow-up table for `65` on the Swallow main table.

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 11-16 | Filth-scarred lungs | `ENDURANCE` is `-2`, and choking or drowning time limits against you are halved. |
| 21-26 | Crushed rib cage | `MOVE` and `ENDURANCE` are both `-1`; sprinting or climbing inflicts `1` Strength damage. |
| 31-36 | Gut-burn adhesions | `MIGHT` and `ENDURANCE` are both `-1`, and tainted food or disease rolls are at `-2`. |
| 41-46 | Destroyed eye | Stomach acid, beak, or crushing pressure costs you an eye. |
| 51-54 | Ruined arm | Teeth, grinding plates, or muscular crushing render one arm lost or useless. |
| 55-56 | Ruined leg | The maw or gut crushes one leg beyond proper recovery. |
| 61-62 | Air-starved wits | `Wits` maximum is reduced by `1`, and all `LORE`, `INSIGHT`, and spellcasting rolls are at `-1` when calm thought is needed. |
| 63-64 | Pelvic or spinal crush | Your `Agility` is permanently reduced to `1`. |
| 65 | Gut-leaking remnant | Your `Strength` is permanently reduced to `1`. Active adventuring usually ends unless the campaign can support constant care. |
| 66 | Broken by the gut | Your `Strength` and `Agility` are both permanently reduced to `1`. Retirement from active adventuring is the default. |

## Recovery, Prosthetics, And Collapse States

- Mundane prosthetics should restore dignity and limited function, not erase penalties.
- A wooden leg should let a character walk; it should not make them a normal runner.
- A hook, brace, or splint should restore one narrow use case, not full versatility.
- When a result says an attribute is permanently reduced to `1`, the character remains alive and playable, but any damage to that attribute Breaks them immediately.
- For physical ruin, reduce `Strength`, `Agility`, or both depending on the injury.
- For catastrophic horror survival, reduce `Wits` and `Empathy` to `1`.
- If a result leaves the adventurer unable to travel, fight, or act without constant aid, the player and GM should treat retirement from active adventuring as the default unless both want to carry that burden into play.

Editorial recommendation:

- Results that still permit travel, speech, and independent action may stay as playable permanent injuries.
- Results that remove independent movement, reliable judgment, or basic self-care should say outright that retirement from active adventuring is the default.
- The table should not hide retirement behind the word "playable." Some survivors live on, but no longer as practical adventurers.

Recommendation: after any Band IV result, state the exact permanent attribute floor immediately so the player knows the character is still alive, still playable, and now hanging on by a thread.

## Interaction With Existing Recovery Rules

- `LUCKY` rank `4` still matters because it downgrades permanent results into long healing.
- `PHYSICIAN` rank `3` still matters because it can convert permanent results into healed ones when applied in time.
- `MEND WOUNDS` still heals the critical injury itself, but it does not regrow a severed or destroyed body part.
- `REGENERATION` remains the premium magical answer to permanent harm.
- Lesser healing should keep you alive, but should not casually erase amputation, spinal injury, or organ failure.

## Why This Works Better

- It makes `65` memorable without making every catastrophic hit a corpse.
- It makes damage type matter: slash maims differently from stab, blunt, and burn.
- It produces serious but believable consequences instead of only "fine," "dead," or a small permanent penalty.
- It gives the table a real spectrum between heroic rescue and living, mechanically fragile survival.

<!-- markdownlint-enable MD013 -->
