#!/usr/bin/env python3
"""
Fix Weatherstone and Vale of the Dead sections in 09-adventure-sites.md:
  - Heading hierarchy (### → ####) for all sub-entries
  - Statblock normalisation (TALENTS/GEAR split, SKILLS blockquote)
  - Column-splice reconstruction (Dalb/Esgar, Ferebald/Dyndria,
    Kalmax/Xugg, Nasura Kak/Horlo, Ghosts/Scrome/Harama,
    Locations/#10/Monsters ordering)
"""

import re

FILEPATH = '2-gamemasters-guide/09-adventure-sites.md'

with open(FILEPATH, 'r', encoding='utf-8') as f:
    content = f.read()

original = content  # keep for diff check


def check(label, old, new):
    """Replace and report whether the target was found."""
    if old not in content:
        print(f'  MISS: {label!r}')
        return content
    return content.replace(old, new)


# ═══════════════════════════════════════════════════════════════════════════════
# WEATHERSTONE
# ═══════════════════════════════════════════════════════════════════════════════

print('Weatherstone fixes...')

# ── 1. Crane location: strip Dalb's spliced stats/text ─────────────────────
content = content.replace(
    '> _The drop from the rock down to the moat is dizzyingly high. '
    'A thick copper chain, green with verdigris, swings back and forth, '
    'chiming in the wind, where it hangs from its weather-beaten windlass._\n\n'
    'night, he is very lucky as no less than two groups arrive shortly after one another.\n\n'
    '**STRENGTH 3, AGILITY 4, WITS 6, EMPATHY 6**\n\n'
    '> **SKILLS:** Performance 5\n\n'
    '**GEAR:** Pipe, lute Since the tower is so tall',
    '> _The drop from the rock down to the moat is dizzyingly high. '
    'A thick copper chain, green with verdigris, swings back and forth, '
    'chiming in the wind, where it hangs from its weather-beaten windlass._\n\n'
    'Since the tower is so tall'
)

# ── 2. Ferebald/Dyndria column splice ───────────────────────────────────────
# Ferebald's stats appeared under Dyndria; need to move them up under Ferebald.
content = content.replace(
    '### Brother Ferebald\n\n'
    'A gnarly and brooding Rust Brother and historian who can tell many tales of '
    'Alderland and the history of the Rust Brothers. Ferebald knows about '
    "Algarod\u2019s wretched past, and believes the king\u2019s undead existence "
    'is a disgrace. Ferebald has secretly joined Esgar and his compatriots to try '
    'to kill Algarod as an act of mercy.\n\n'
    '### Dyndria the Bard\n\n'
    'Dyndria plays the fiddle and seems to be a jovial woman with a taste for food '
    'and drink. She claims to be here because she has been paid to play.\n\n'
    'In fact, Dyndria is a thief and assassin hired by the rulers of Alderland, '
    'south of the Iron Lock. The new royal family wants to remove any traces of '
    "Algarod\u2019s line since political rebels have revealed that the old king "
    'still roams Ravenland If Dyndria manages to take '
    "Algarod\u2019s head to the Iron Lock, she will be richly rewarded and awarded "
    'citizenship in Alderland \u2013 or so she believes. Dyndria dreams of present '
    'day Alderland, but knows nothing about it. She has hinted to Esgar that she '
    'is a thief and would like to be part of any secret raid against the '
    'stronghold, but she has not divulged her true intentions.\n\n'
    '**Strength 3, Agility 4, Wits 2, Empathy 3**\n\n'
    '> **SKILLS:** Stealth 3, Marksmanship 2, Move 2, Melee 1, Manipulation 2, Performance 2\n\n'
    '**TALENTS:** Path of Poison 1, Lightning Fast 1 **GEAR:** Sling, dagger, leather armor, fiddle, D6 copper\n\n'
    '**Strength 2, Agility 2, Wits 4, Empathy 2**\n\n'
    '> **SKILLS:** Lore 3, Insight 2, Melee 1\n\n'
    '**TALENTS:** Path of Blood 1, Herbalist 1 **GEAR:** Knife, parchment and pen, D8 copper\n\n'
    '### King Algarod',

    '#### Brother Ferebald\n\n'
    'A gnarly and brooding Rust Brother and historian who can tell many tales of '
    'Alderland and the history of the Rust Brothers. Ferebald knows about '
    "Algarod\u2019s wretched past, and believes the king\u2019s undead existence "
    'is a disgrace. Ferebald has secretly joined Esgar and his compatriots to try '
    'to kill Algarod as an act of mercy.\n\n'
    '**Strength 2, Agility 2, Wits 4, Empathy 2**\n'
    '> **SKILLS:** Lore 3, Insight 2, Melee 1\n'
    '> **TALENTS:** Path of Blood 1, Herbalist 1\n'
    '**GEAR:** Knife, parchment and pen, D8 copper\n\n'
    '#### Dyndria the Bard\n\n'
    'Dyndria plays the fiddle and seems to be a jovial woman with a taste for food '
    'and drink. She claims to be here because she has been paid to play.\n\n'
    'In fact, Dyndria is a thief and assassin hired by the rulers of Alderland, '
    'south of the Iron Lock. The new royal family wants to remove any traces of '
    "Algarod\u2019s line since political rebels have revealed that the old king "
    'still roams Ravenland If Dyndria manages to take '
    "Algarod\u2019s head to the Iron Lock, she will be richly rewarded and awarded "
    'citizenship in Alderland \u2013 or so she believes. Dyndria dreams of present '
    'day Alderland, but knows nothing about it. She has hinted to Esgar that she '
    'is a thief and would like to be part of any secret raid against the '
    'stronghold, but she has not divulged her true intentions.\n\n'
    '**Strength 3, Agility 4, Wits 2, Empathy 3**\n'
    '> **SKILLS:** Stealth 3, Marksmanship 2, Move 2, Melee 1, Manipulation 2, Performance 2\n'
    '> **TALENTS:** Path of Poison 1, Lightning Fast 1\n'
    '**GEAR:** Sling, dagger, leather armor, fiddle, D6 copper\n\n'
    '#### King Algarod'
)

# ── 3. Monsters section open: The Treasure Hunters + Dalb + Esgar splice ───
# Current: empty Esgar heading before Monsters; Dalb entry contains Esgar text;
# Dalb's own stats are in the Crane location.
content = content.replace(
    '### The Treasure Hunters\n\n'
    'A motley crew of treasure hunters, led by Esgar Farthing, arrives shortly '
    'before the adventurers. They are looking for the war chest and King '
    "Algarod\u2019s sword. It will soon be evident that the treasure hunters have "
    'different agendas. This group, or just some of its members, can be used as '
    'antagonists or potential allies in Weatherstone.\n\n'
    '### Esgar Farthing\n\n'
    '### Monsters and Npcs\n\n'
    'The monsters and NPCs that the adventurers can meet at Weatherstone are described below.\n\n'
    '### Dalb, the Bard\n\n'
    'A man in his fifties with greying, unkempt hair, wearing a green tunic, gray '
    'hose and knitted finger gloves to protect against the cold. Constantly with a '
    'pipe in the corner of his mouth, Dalb is a person who can enchant any audience '
    'with so simple a means as his green eyes and husky voice. The bard (who is not '
    'what he seems to be, see the boxed text \u201cWho is Dalb?\u201d) has struck '
    'camp outside Weatherstone to lure adventurers to their doom within. This '
    'A muscular and loud man who presents himself as a travelling merchant '
    'specializing in \u201crare goods.\u201d Esgar is really a simple mercenary '
    'who has heard about the treasure in Weatherstone and intends to find it, at '
    'any price. He lacks empathy and is planning to double-cross his companions at '
    'the first and best opportunity.\n\n'
    '**Strength 5, Agility 3, Wits 2, Empathy 2**\n\n'
    '> **SKILLS:** Melee 3, Might 3, Manipulation 2, Move 1\n\n'
    '**TALENTS:** Path of the Blade 1, Threatening 1 **GEAR:** Longsword, large shield, chainmail, D6 silver\n\n'
    '### Kordomar Sulam',

    '### Monsters and NPCs\n\n'
    'The monsters and NPCs that the adventurers can meet at Weatherstone are described below.\n\n'
    '#### The Treasure Hunters\n\n'
    'A motley crew of treasure hunters, led by Esgar Farthing, arrives shortly '
    'before the adventurers. They are looking for the war chest and King '
    "Algarod\u2019s sword. It will soon be evident that the treasure hunters have "
    'different agendas. This group, or just some of its members, can be used as '
    'antagonists or potential allies in Weatherstone.\n\n'
    '#### Dalb, the Bard\n\n'
    'A man in his fifties with greying, unkempt hair, wearing a green tunic, gray '
    'hose and knitted finger gloves to protect against the cold. Constantly with a '
    'pipe in the corner of his mouth, Dalb is a person who can enchant any audience '
    'with so simple a means as his green eyes and husky voice. The bard (who is not '
    'what he seems to be, see the boxed text \u201cWho is Dalb?\u201d) has struck '
    'camp outside Weatherstone to lure adventurers to their doom within. This '
    'night, he is very lucky as no less than two groups arrive shortly after one another.\n\n'
    '**Strength 3, Agility 4, Wits 6, Empathy 6**\n'
    '> **SKILLS:** Performance 5\n'
    '**GEAR:** Pipe, lute\n\n'
    '#### Esgar Farthing\n\n'
    'A muscular and loud man who presents himself as a travelling merchant '
    'specializing in \u201crare goods.\u201d Esgar is really a simple mercenary '
    'who has heard about the treasure in Weatherstone and intends to find it, at '
    'any price. He lacks empathy and is planning to double-cross his companions at '
    'the first and best opportunity.\n\n'
    '**Strength 5, Agility 3, Wits 2, Empathy 2**\n'
    '> **SKILLS:** Melee 3, Might 3, Manipulation 2, Move 1\n'
    '> **TALENTS:** Path of the Blade 1, Threatening 1\n'
    '**GEAR:** Longsword, large shield, chainmail, D6 silver\n\n'
    '#### Kordomar Sulam'
)

# ── 4. Kordomar TALENTS/GEAR ────────────────────────────────────────────────
content = content.replace(
    '**TALENTS:** The Path of the Arrow 1, Sharpshooter 1 **GEAR:** Longbow, dagger, leather armor, D6 copper',
    '> **TALENTS:** The Path of the Arrow 1, Sharpshooter 1\n'
    '**GEAR:** Longbow, dagger, leather armor, D6 copper'
)

# ── 5. Skeleton Soldiers: split GEAR and BONY ───────────────────────────────
content = content.replace(
    '**GEAR:** Broadsword, studded leather **BONY:** Skeletons never take more than 1 point of Damage from STABS and arrows.',
    '**GEAR:** Broadsword, studded leather\n\n'
    '**BONY:** Skeletons never take more than 1 point of Damage from STABS and arrows.'
)

# ── 6. Skeleton Bodyguards: split GEAR and BONY ─────────────────────────────
content = content.replace(
    '**GEAR:** Chainmail, large shield, longsword **BONY:** Skeletons never take more than 1 point of Damage from STABS and arrows.',
    '**GEAR:** Chainmail, large shield, longsword\n\n'
    '**BONY:** Skeletons never take more than 1 point of Damage from STABS and arrows.'
)

# ── 7. Weatherstone heading changes (### → ####) ────────────────────────────
# Apply within the Weatherstone section only.
# We identify the section by its boundaries and do targeted replacements.
# Top-level H3 section headers that MUST stay at ###:
#   Background, Recommended Reading, Getting Here, Legend, Locations,
#   Monsters and NPCs (already fixed above), Events

ws_h3_to_h4 = [
    '### The Yellow-eyed Deer',
    '### The Tired Treasure Hunter',
    '### 1. Watchtower',
    '### Who Is Dalb?',
    '### 2. the Main Gate',
    '### When the Undead Have Risen',   # appears twice — both should be ####
    '### 3. the House of Knights',
    '### 4. the Ravine',
    '### 5. the Laboratory',
    '### 7. Drawbridge',
    '### 8. Guard Post and Servants\u2019 Quarters',
    '### 9. Algarod\u2019s Tower',
    '### Rustbite, Magical Longsword',
    '### When the Undead Arise',
    '### 10. Crane',
    '### Kordomar Sulam',
    '### Undead Soldiers',
    '### Skeleton Soldiers',
    '### Skeleton Bodyguards',
    '### The Scorpion Beast',
    '### Harpies',
    '### Dalb\u2019s Tale',
    '### The Moat',
    '### Attack of the Harpies',
    '### The Harpies Negotiate',
    '### The Dead Rise!',
    '### The Bard\u2019s Song',
    '### Fire!',
    '### King Algarod\u2019s March',
]

# Also handle these with potential straight apostrophes
ws_h3_to_h4_straight = [
    "### 8. Guard Post and Servants' Quarters",
    "### 9. Algarod's Tower",
    "### Dalb's Tale",
    "### The Bard's Song",
    "### King Algarod's March",
    "### 6. the Theater Tower and the Harpies' Nest",
    "### Who Is Dalb?",  # no apostrophe but keep here too
]

for h in ws_h3_to_h4 + ws_h3_to_h4_straight:
    content = content.replace(h + '\n', h.replace('### ', '#### ', 1) + '\n')

# ── 8. The Treasure Hunters event (Events section version) ──────────────────
# Already handled by blanket ### → #### since the heading is unique in Events.
# But we need to make sure it's changed in Events too (not just in Monsters).
# Since we renamed the Monsters one to ####, the Events version still needs:
content = content.replace(
    '### The Treasure Hunters\n\n'
    'The treasure hunters led by Esgar Farthing enter Weatherstone',
    '#### The Treasure Hunters\n\n'
    'The treasure hunters led by Esgar Farthing enter Weatherstone'
)


# ═══════════════════════════════════════════════════════════════════════════════
# VALE OF THE DEAD
# ═══════════════════════════════════════════════════════════════════════════════

print('Vale of the Dead fixes...')

# ── 1. Fix Locations/Monsters transition: restore location #10 and fix order ─
# Current (garbled):
#   - CREATURES: Harama the glutton.
#   piece of treasure (for instance...)
#   One can also speak with the dead...
#   - CREATURES: Ghosts.
#   - TREASURES: Roll on the treasures tables on page 186.
#   ### Monsters and Npcs
#   - TREASURES: Harama's soup stone.
#   ### 10. the Graves
#   ... The graves text... "he will award the guests with a The monsters and NPCs..."
#   ### Kalmax
#
# Want:
#   - CREATURES: Harama the glutton.
#   - TREASURES: Harama's soup stone.
#   #### 10. the Graves
#   ... full text ... "piece of treasure (for instance...)"
#   One can also speak with the dead...
#   - CREATURES: Ghosts.
#   - TREASURES: Roll on the treasures tables on page 186.
#   ### Monsters and NPCs
#   The monsters and NPCs intro...
#   #### Kalmax

content = content.replace(
    '- CREATURES: Harama the glutton.\n\n'
    'piece of treasure (for instance, one of the four key artifacts of the _Raven\u2019s Purge_ campaign).\n\n'
    'One can also speak with the dead and glean information about the history of the Forbidden Lands and other places that the GM finds it suitable to reveal. The information is several hundred years old, of course.\n\n'
    '- CREATURES: Ghosts.\n'
    '- TREASURES: Roll on the treasures tables on page 186.\n\n'
    '### Monsters and Npcs\n\n'
    '- TREASURES: Harama\u2019s soup stone.\n\n'
    '### 10. the Graves\n\n'
    '> _On closer examination, the surfaces of the tombstones have crumbled beyond all legibility. The stone doors to the mountain crypts loom larger still when you approach them, impossible to budge without a span of oxen._\n\n'
    'The graves of the valley can be found here and there. There is some burial gold to be found behind the stone doors that only Scrome can open, unless the characters are using magic. If someone manages to steal the gold, Scrome can send a couple of ghosts after the thieves, ruining their everyday lives by causing confusion, poisoning their food and destroying their belongings. In other words, the burial treasure becomes cursed. If one helps Scrome reclaim the crumhorn, he will award the guests with a The monsters and NPCs that the adventurers can meet in the Vale of the Dead are described below. Monsters and creatures not detailed here have the same stats as listed in the Kin and Bestiary chapters.\n\n'
    '### Kalmax',

    '- CREATURES: Harama the glutton.\n'
    '- TREASURES: Harama\u2019s soup stone.\n\n'
    '#### 10. the Graves\n\n'
    '> _On closer examination, the surfaces of the tombstones have crumbled beyond all legibility. The stone doors to the mountain crypts loom larger still when you approach them, impossible to budge without a span of oxen._\n\n'
    'The graves of the valley can be found here and there. There is some burial gold to be found behind the stone doors that only Scrome can open, unless the characters are using magic. If someone manages to steal the gold, Scrome can send a couple of ghosts after the thieves, ruining their everyday lives by causing confusion, poisoning their food and destroying their belongings. In other words, the burial treasure becomes cursed. If one helps Scrome reclaim the crumhorn, he will award the guests with a piece of treasure (for instance, one of the four key artifacts of the _Raven\u2019s Purge_ campaign).\n\n'
    'One can also speak with the dead and glean information about the history of the Forbidden Lands and other places that the GM finds it suitable to reveal. The information is several hundred years old, of course.\n\n'
    '- CREATURES: Ghosts.\n'
    '- TREASURES: Roll on the treasures tables on page 186.\n\n'
    '### Monsters and NPCs\n\n'
    'The monsters and NPCs that the adventurers can meet in the Vale of the Dead are described below. Monsters and creatures not detailed here have the same stats as listed in the Kin and Bestiary chapters.\n\n'
    '#### Kalmax'
)

# ── 2. Kalmax/Xugg column splice ─────────────────────────────────────────────
content = content.replace(
    '### Xugg and Other Orcs\n\n'
    'The orcs in the Vale of the Dead are clanless orcs who have been hired for protection by the whiners.\n\n'
    '**Strength 3, Agility 4, Wits 3, Empathy 3**\n\n'
    '> **SKILLS:** Endurance 3, Melee 4, Move 2, Scouting 3, Survival 3, Animal Handling 3\n\n'
    '**Strength 4, Agility 2, Wits 2, Empathy 2**\n\n'
    '> **SKILLA:** Melee 2, Might 1\n\n'
    '**GEAR:** Scimitar, studded leather armor **GEAR:** Short spear, broadsword, leather armor, riding horse\n\n'
    '### Nasura Kak',

    # Kalmax stats go under Kalmax (above), orcs get their own clean entry
    '**Strength 3, Agility 4, Wits 3, Empathy 3**\n'
    '> **SKILLS:** Endurance 3, Melee 4, Move 2, Scouting 3, Survival 3, Animal Handling 3\n'
    '**GEAR:** Short spear, broadsword, leather armor, riding horse\n\n'
    '#### Xugg and Other Orcs\n\n'
    'The orcs in the Vale of the Dead are clanless orcs who have been hired for protection by the whiners.\n\n'
    '**Strength 4, Agility 2, Wits 2, Empathy 2**\n'
    '> **SKILLS:** Melee 2, Might 1\n'
    '**GEAR:** Scimitar, studded leather armor\n\n'
    '#### Nasura Kak'
)

# ── 3. Nasura Kak/Horlo column splice ────────────────────────────────────────
content = content.replace(
    '### Nasura Kak\n\n'
    '### Horlo\n\n'
    'The clanless orcs have been hired by the whiners to keep enemies away. In '
    'return, they are receiving food and fermented juice. The orc leader, Horlo, '
    'is a scarred battle tested orc from the Isir clan. He was driven away by '
    'Eldag the Ravager after an orc woman chose Horlo over the chieftain. Horlo '
    'rightly considers himself to have been wrongfully cast out and wants nothing '
    'more than to return to the Isir and kill Eldag. He may start negotiations '
    'with strangers if he thinks that they can be of use in this endeavour. Horlo '
    'and his two Isir companions, Chren and Argana, are the most capable fighters '
    'among the orcs and they never get severely drunk. If Horlo becomes angry he '
    'will start foaming at the mouth, producing green froth that makes his bite '
    'poisonous.\n\n'
    '**Strength 5, Agility 4, Wits 3, Empathy 2**\n\n'
    '> **SKILLS:** Might 3, Melee 4, Manipulation 2\n\n'
    '**GEAR:** Scimitar, shield, chainmail, D6 copper, necklace with teeth The '
    'chieftain of the whiners is called Nasura Kak. She and her people want '
    'nothing other than to live in peace and quiet inside the mountain. Like all '
    'whiners, she and her kin are terrified of tall-folk who want to take them for '
    'their sweetmeat. Nasura wants to keep the crumhorn away from Scrome at any '
    'cost, since his tunes cause their protective hollow-rock to wither as well as '
    'being grating on the sensitive ears of whiners.\n\n'
    '**Strength 2, Agility 4, Wits 3, Empathy 2**\n\n'
    '> **SKILLS:** Melee 2, Stealth 2, Manipulation 3\n\n'
    '**GEAR:** Shortsword, knife, studded leather armor\n\n'
    '### Whiners',

    '#### Nasura Kak\n\n'
    'The chieftain of the whiners is called Nasura Kak. She and her people want '
    'nothing other than to live in peace and quiet inside the mountain. Like all '
    'whiners, she and her kin are terrified of tall-folk who want to take them for '
    'their sweetmeat. Nasura wants to keep the crumhorn away from Scrome at any '
    'cost, since his tunes cause their protective hollow-rock to wither as well as '
    'being grating on the sensitive ears of whiners.\n\n'
    '**Strength 2, Agility 4, Wits 3, Empathy 2**\n'
    '> **SKILLS:** Melee 2, Stealth 2, Manipulation 3\n'
    '**GEAR:** Shortsword, knife, studded leather armor\n\n'
    '#### Horlo\n\n'
    'The clanless orcs have been hired by the whiners to keep enemies away. In '
    'return, they are receiving food and fermented juice. The orc leader, Horlo, '
    'is a scarred battle tested orc from the Isir clan. He was driven away by '
    'Eldag the Ravager after an orc woman chose Horlo over the chieftain. Horlo '
    'rightly considers himself to have been wrongfully cast out and wants nothing '
    'more than to return to the Isir and kill Eldag. He may start negotiations '
    'with strangers if he thinks that they can be of use in this endeavour. Horlo '
    'and his two Isir companions, Chren and Argana, are the most capable fighters '
    'among the orcs and they never get severely drunk. If Horlo becomes angry he '
    'will start foaming at the mouth, producing green froth that makes his bite '
    'poisonous.\n\n'
    '**Strength 5, Agility 4, Wits 3, Empathy 2**\n'
    '> **SKILLS:** Might 3, Melee 4, Manipulation 2\n'
    '**GEAR:** Scimitar, shield, chainmail, D6 copper, necklace with teeth\n\n'
    '#### Whiners'
)

# ── 4. Ghosts/Scrome/Harama column splice ────────────────────────────────────
content = content.replace(
    '### Ghosts\n\n'
    'There are some hundred ghosts in the valley that normally exist in harmony '
    'with nature and death. Ever since Scrome\u2019s crumhorn was stolen, the '
    'atmosphere in the valley has changed. The ghosts have become increasingly '
    'restless and even dangerous. What was once a place of peace has become a '
    'death trap since the whiners\u2019 theft.\n\n'
    'Stats for ghosts can be found on page 94 of the Bestiary.\n\n'
    'speak to Scrome, one must defeat him or return the crumhorn to him. In the '
    'latter case, he will be very grateful and bestow a gift on the adventurers, '
    'possibly an artifact, maybe even the crown Stanengist (see the _Raven\u2019s '
    'Purge_ campaign book).\n\n'
    'If Scrome\u2019s second eye is reinserted (see page 144), he becomes a '
    'completely different and considerably more dangerous giant.\n\n'
    '**Strength 24, Agility 2, Wits 3, Empathy 2**\n\n'
    '> **ARMOR:** 3 (skin)\n\n'
    '### Scrome\n\n'
    'The one-eyed giant Scrome is usually of a peaceful and caring nature, but '
    'now he is angry and suspicious of all intruders since he has been robbed. He '
    'also harbors an indistinct fear for his other self and asks the strangers if '
    'they \u201cbring the eye.\u201d Scrome is very old, not too clever and '
    'basically immortal. Not even the eye is vulnerable, since it is covered by '
    'thick glass. The giant\u2019s only weak spot is a tattoo on the top of his '
    'head, put there by the one who once upon a time turned him into a guardian. '
    'It keeps Scrome alive and should it be destroyed, he would age and wither to '
    'dust in minutes.\n\n'
    'Scrome cares for the undead and tries to make them feel at home, among other '
    'means by playing an old crumhorn. He also plays with them, as if in a doll '
    'house, and builds enclosures by laying out rocks on the ground. If angered, '
    'he may lose his cool and become incredibly dangerous. He has perfect recall, '
    'no real concept of time and remembers Zygofer very well, though he seems to '
    'think that he has only been gone for a couple of days. To **GEAR:** Wooden club\n\n'
    '### Harama the Glutton\n\n'
    'Harama is a shapeless, very voracious mass of tissue that reminds one of a '
    'grotesquely fat human whose limbs and features have multiplied and shifted '
    'around. The creature can fight at the place where it\u2019s encountered with '
    'a colossal cleaver, but it cannot move. It is constantly in pain and hateful '
    'of all living things. Soothing its pain with healing magic or music will calm '
    'it down, and may prompt it to speak of Zygofer. It may then remember who it '
    'once was.\n\n'
    'Harama was once the human servant and chef of Zygofer during his studies in '
    'the valley. The sorcerer couldn\u2019t keep from experimenting on him after '
    'aquiring his first slivers of necromantic knowledge. Scrome became upset and '
    'drove Zygofer and Martea from the valley. The giant feels sorry for Harama, '
    'and lets him stay and allows the undead to feed him, more often than not '
    'using recipes mumbled by Harama himself. In sympathy, Scrome has told Harama '
    'about his tattoo.\n\n'
    'If the adventurers help Harama die, he may give them his magical soup stone '
    'as thanks. It is buried in the old herbarium outside the kitchen.\n\n'
    'be overtly hostile towards them. It is up to the adventurers to convince the '
    'giant of their good intentions.\n\n'
    '**Strength 6, Agility 2, Wits 3, Empathy 2**\n\n'
    '> **SKILLS:** Melee 2, Lore 2, Manipulation 2\n\n'
    '**GEAR:** Cleaver, soup stone **HARAMA\u2019S** soup stone looks like a piece '
    'of shimmering, milky agate shaped like the egg of a goose. Putting it in a '
    'soup or stew while cooking will make the food so delicious that anyone who '
    'eats it will become temporarily sympathetic to the chef. The chef gets +3 on '
    'all rolls for MANIPULATION directed towards people who have eaten of the meal.',

    '#### Ghosts\n\n'
    'There are some hundred ghosts in the valley that normally exist in harmony '
    'with nature and death. Ever since Scrome\u2019s crumhorn was stolen, the '
    'atmosphere in the valley has changed. The ghosts have become increasingly '
    'restless and even dangerous. What was once a place of peace has become a '
    'death trap since the whiners\u2019 theft.\n\n'
    'Stats for ghosts can be found on page 94 of the Bestiary.\n\n'
    '#### Scrome\n\n'
    'The one-eyed giant Scrome is usually of a peaceful and caring nature, but '
    'now he is angry and suspicious of all intruders since he has been robbed. He '
    'also harbors an indistinct fear for his other self and asks the strangers if '
    'they \u201cbring the eye.\u201d Scrome is very old, not too clever and '
    'basically immortal. Not even the eye is vulnerable, since it is covered by '
    'thick glass. The giant\u2019s only weak spot is a tattoo on the top of his '
    'head, put there by the one who once upon a time turned him into a guardian. '
    'It keeps Scrome alive and should it be destroyed, he would age and wither to '
    'dust in minutes.\n\n'
    'Scrome cares for the undead and tries to make them feel at home, among other '
    'means by playing an old crumhorn. He also plays with them, as if in a doll '
    'house, and builds enclosures by laying out rocks on the ground. If angered, '
    'he may lose his cool and become incredibly dangerous. He has perfect recall, '
    'no real concept of time and remembers Zygofer very well, though he seems to '
    'think that he has only been gone for a couple of days. To speak to Scrome, '
    'one must defeat him or return the crumhorn to him. In the latter case, he '
    'will be very grateful and bestow a gift on the adventurers, possibly an '
    'artifact, maybe even the crown Stanengist (see the _Raven\u2019s Purge_ '
    'campaign book).\n\n'
    'If Scrome\u2019s second eye is reinserted (see page 144), he becomes a '
    'completely different and considerably more dangerous giant.\n\n'
    '**Strength 24, Agility 2, Wits 3, Empathy 2**\n'
    '> **ARMOR:** 3 (skin)\n'
    '**GEAR:** Wooden club\n\n'
    '#### Harama the Glutton\n\n'
    'Harama is a shapeless, very voracious mass of tissue that reminds one of a '
    'grotesquely fat human whose limbs and features have multiplied and shifted '
    'around. The creature can fight at the place where it\u2019s encountered with '
    'a colossal cleaver, but it cannot move. It is constantly in pain and hateful '
    'of all living things. Soothing its pain with healing magic or music will calm '
    'it down, and may prompt it to speak of Zygofer. It may then remember who it '
    'once was.\n\n'
    'Harama was once the human servant and chef of Zygofer during his studies in '
    'the valley. The sorcerer couldn\u2019t keep from experimenting on him after '
    'aquiring his first slivers of necromantic knowledge. Scrome became upset and '
    'drove Zygofer and Martea from the valley. The giant feels sorry for Harama, '
    'and lets him stay and allows the undead to feed him, more often than not '
    'using recipes mumbled by Harama himself. In sympathy, Scrome has told Harama '
    'about his tattoo.\n\n'
    'If the adventurers help Harama die, he may give them his magical soup stone '
    'as thanks. It is buried in the old herbarium outside the kitchen.\n\n'
    '**Strength 6, Agility 2, Wits 3, Empathy 2**\n'
    '> **SKILLS:** Melee 2, Lore 2, Manipulation 2\n'
    '**GEAR:** Cleaver, soup stone\n\n'
    '**HARAMA\u2019S SOUP STONE:** Looks like a piece of shimmering, milky agate '
    'shaped like the egg of a goose. Putting it in a soup or stew while cooking '
    'will make the food so delicious that anyone who eats it will become '
    'temporarily sympathetic to the chef. The chef gets +3 on all rolls for '
    'MANIPULATION directed towards people who have eaten of the meal.'
)

# ── 5. Wrath of Scrome event: fix truncated ending ──────────────────────────
content = content.replace(
    'He will view the adventurers as part of the intrusion that has disrupted the '
    'harmony of the valley from the first time they meet, and\n\n'
    '### Night of the Ghosts',
    'He will view the adventurers as part of the intrusion that has disrupted the '
    'harmony of the valley from the first time they meet, and he will be overtly '
    'hostile towards them. It is up to the adventurers to convince the giant of '
    'their good intentions.\n\n'
    '#### Night of the Ghosts'
)

# ── 6. Vale of the Dead heading changes (### → ####) ─────────────────────────
vale_h3_to_h4 = [
    '### The Bounty Hunters',
    '### The Stone Chantress and the Dwarves',
    '### Kalmax and the Riders',
    '### 1. Highvale',
    '### 2. Yard and Distillery',
    '### 3. the Temple of Silence',
    '### 4. Embalming Chamber',
    '### 5. Whiner Dwellings',
    '### 6. Mountain Crevice',
    '### 7. the Exit',
    '### 8. the Vale of the Dead',   # location within the site
    '### 9. Harama\u2019s Kitchen',
    "### 9. Harama's Kitchen",       # straight apostrophe variant
    '### Whiners',
    '### The Wrath of Scrome',
    '### Night of the Ghosts',       # handled above with content, but just in case
    '### Captured!',
    '### The Flooding',
    '### Kalmax and the Treasure',
    '### Morme!',
    '### Dance of the Unquiet',
]

for h in vale_h3_to_h4:
    content = content.replace(h + '\n', h.replace('### ', '#### ', 1) + '\n')

# ─── SHARED CLEANUP ──────────────────────────────────────────────────────────
# Fix any remaining "### Monsters and Npcs" → "### Monsters and NPCs"
content = content.replace('### Monsters and Npcs\n', '### Monsters and NPCs\n')

# ─── WRITE ───────────────────────────────────────────────────────────────────
if content == original:
    print('WARNING: no changes made — all replacements missed')
else:
    changed = sum(1 for a, b in zip(original.splitlines(), content.splitlines()) if a != b)
    print(f'Writing file ({changed} lines changed)...')
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Done.')
