#!/usr/bin/env python3
"""
Fix ch09 adventure sites:
1. Restructure The Hollows heading hierarchy (### → #### for sub-items)
2. Reconstruct the jumbled Monsters and NPCs section in correct order
3. Fix all NPC statblock headings (### Strength → **Strength**) across ch09
"""
import re

filepath = "/home/apoapostolov/git-public/Forbidden-Lands-2e/2-gamemasters-guide/09-adventure-sites.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# STEP 1: Heading level changes within The Hollows section
# ============================================================

hollows_marker = '\n## The Hollows\n'
weatherstone_marker = '\n## Weatherstone\n'

h_start = content.index(hollows_marker)
w_start = content.index(weatherstone_marker)

before_hollows = content[:h_start]
hollows = content[h_start:w_start]
after_hollows = content[w_start:]

# Numbered location headings: ### N. → #### N.
hollows = re.sub(r'^### (\d+)\. ', r'#### \1. ', hollows, flags=re.MULTILINE)

# Named sub-headings within Locations
hollows = hollows.replace('### Strange Events in the Hollows\n', '#### Strange Events in the Hollows\n')
hollows = hollows.replace('### Who Does What?\n', '#### Who Does What?\n')

# The Undead appears twice (once in Locations, once in Monsters and NPCs) — both → ####
hollows = hollows.replace('### The Undead\n', '#### The Undead\n')

# Fix Monsters and Npcs capitalization (stays H3)
hollows = hollows.replace('### Monsters and Npcs\n', '### Monsters and NPCs\n')

# NPC entries → ####
hollows = hollows.replace('### Mrs. Pollmor\n', '#### Mrs. Pollmor\n')
hollows = hollows.replace('### Brewmaster Yawim\n', '#### Brewmaster Yawim\n')
hollows = hollows.replace('### Rust Brother Sturkas\n', '#### Rust Brother Sturkas\n')
hollows = hollows.replace('### Midwife Nirvea\n', '#### Midwife Nirvea\n')
hollows = hollows.replace('### The "village Idiot" Perko\n', '#### The "Village Idiot" Perko\n')
hollows = hollows.replace('### Count Nepola\n', '#### Count Nepola\n')
hollows = hollows.replace('### Countess Ursula\n', '#### Countess Ursula\n')

# Events sub-headings → ####
hollows = hollows.replace('### The Beer War\n', '#### The Beer War\n')
hollows = hollows.replace('### The Raven Sister\n', '#### The Raven Sister\n')
hollows = hollows.replace('### The Attack\n', '#### The Attack\n')
hollows = hollows.replace('### The Dwarves\n', '#### The Dwarves\n')
hollows = hollows.replace('### The Secret of the Crypt\n', '#### The Secret of the Crypt\n')

content = before_hollows + hollows + after_hollows

# ============================================================
# STEP 2: Replace the entire Monsters and NPCs block in The Hollows
# ============================================================
# After step 1, the section is now named "### Monsters and NPCs"
# Find the block from "### Monsters and NPCs" to just before "### Events"

npc_start_marker = '\n### Monsters and NPCs\n'
events_marker = '\n### Events\n'

npc_start_pos = content.index(npc_start_marker)
events_pos = content.index(events_marker, npc_start_pos)

# The new clean Monsters and NPCs block
new_npc_block = '''
### Monsters and NPCs

The most prominent individuals in the village, as well as the princely couple Ursula and Nepola, are described below. The other inhabitants are presented in a table.

#### Mrs. Pollmor

The village elder, Mrs. Pollmor, is an elderly woman whose family has run the village for generations. She makes sure that the wall is decently functional, runs a militia, maintains the well, keeps the river clean, is responsible for fire protection, tends to the temple and sees to it that the latrines are emptied, as well as collecting taxes from those who don\u2019t contribute to the aforementioned chores. Mrs. Pollmor is known as \u201cThe Bailiff\u201d among those who dislike her. Ever since her man passed away she has become increasingly introverted and, aside from the occasional visit to Dead Man\u2019s Hand, keeps to her rocking chair in front of the fireplace at home. Mrs. Pollmor lives in the shadow of her great-grandmother, who is held up as the founder of the village. With age, she has also become greedy and mean. She abuses her power and skirts her sense of justice more and more to misappropriate benefits for herself. The innkeeper, Olm and Ness, the blacksmith, are hoping that the conflict between the elder and Yawim, the brewmaster, will kindle an ember in the frozen heart of Mrs. Pollmor.

**Strength 2, Agility 2, Wits 4, Empathy 3**

> **SKILLS:** Lore 2, Insight 3, Manipulation 4

**GEAR:** A large bronze amulet with a piece of amber at its centre \u2013 a sign of her office (worth D6 silver coins)

#### Brewmaster Yawim

The brewmaster Yawim is an angry dwarf who was driven out of the Meromannian clan many years ago, when it was revealed that he had been using a human recipe for making mead. Yawim drifted around for a while and ended up in The Hollows, where he settled. Over the years, he has developed a burning hatred towards all dwarves, repressing the fact that he himself belongs to this kin. He shaves every morning, simmering with rage.

Yawim possesses exceptional brewing skills and runs the Three Skulls Tavern, which has become very popular in a short amount of time. Yawim\u2019s rich beer is known far and wide and, through his grand plans for trade, the dwarf has wound up on a collision course with the elder. He dislikes Mrs. Pollmor\u2019s leadership and finds her increasing taxation of his brewery business extremely provocative. Yawim is constantly on the look-out for new allies, hoping to one day challenge the village elder for her office.

Yawim is a beardless dwarf with a shaved head and a gut that grows ever larger in step with his fondness for beer. He is boisterous and always close to laughter or anger.

**Strength 4, Agility 2, Wits 3, Empathy 3**

> **SKILLS:** Melee 3, Crafting 2, Insight 1, Manipulation 2

**GEAR:** Axe, ornamented chalice made from the horn of a minotaur hanging in a chain from his belt (worth D6 gold coins)

#### Rust Brother Sturkas

Few know Sturkas\u2019s name and most of the villagers only speak of him as \u201cthe Rust Brother\u201d \u2013 usually with a hint of fear in their voices. Sturkas is a large, dark-haired man, dressed in a yellow and red cloak adorned with details of rusted iron. His face is disfigured by the scars of innumerable battles. To the outside world, he strictly adheres to the laws of the Rust Brothers, but in truth, he is remorseful of cruel acts in his younger years. He turns a blind eye to the midwife and her witchcraft, and secretly cares for the \u201cvillage idiot\u201d, Perko. Should he, however, discover that the midwife is a Raven Sister he will resolutely act according to the regulations of the Rust Brothers \u2013 i.e., kill her. The Rust Brother is on Mrs. Pollmor\u2019s side in the escalating conflict in the village, but may choose to switch sides if he feels that it suits him.

**Strength 4, Agility 3, Wits 3, Empathy 2**

> **SKILLS:** Melee 3, Crafting 2, Insight 1, Manipulation 2

> **TALENTS:** Path of Blood 2

**GEAR:** Longsword, chainmail

#### Midwife Nirvea

Midwife Nirvea is secretly a Raven Sister and the only person, except for Vike, who had been in contact with the outside world even before the Blood Mist dispersed. The villagers see her only as a wise woman who delivers their children, provides them with medications and gives them advice. Nirvea has been on the run since her temple was put to the flame by the Rust Brothers, and hopes to one day find the strength to leave The Hollows and seek out her fellow sisters. She may consider joining the adventurers as a healer. She despises the Rust Brother Sturkas and everything he stands for, and will attempt to kill him if the opportunity arises.

Nirvea appears older than her 40 years and is dressed in dirty sheets of cloth and a hood. She speaks with consideration, softly and slowly.

**Strength 2, Agility 3, Wits 3, Empathy 3**

> **TALENTS:** Path of Healing 2, Path of Sight 1

> **SKILLS:** Lore 2, Insight 2, Healing 4

**GEAR:** Satchel with herbs (Gear Bonus +2 to HEALING), leather pouch with raven bones for divinations

#### The \u201cVillage Idiot\u201d Perko

One morning almost ten years ago, Perko\u2019s parents were gone when he woke up. It is said that they were taken to the \u201cother side\u201d by ghosts and that Perko became wraithbit (half-undead) at the same time. Ever since that day, Perko has lived on the alms of the villagers and because of this, they consider it their right to mock and humiliate the boy.

Perko drifts aimlessly around town and is mostly ignored by the villagers. For this reason, he knows many of the villagers\u2019 secrets, and would surely have been a great source of information if he hadn\u2019t gone mute after his parents\u2019 disappearance.

Perko is a teenage boy with dirty, cut-off tights and a muddy tunic. His hair straggles in all directions and his stare is maniacal. He stuffs his pockets with dead birds, messy muck, insects and other items of interest that he gladly offers as gifts to those he meets.

**Strength 2, Agility 3, Wits 3, Empathy 1**

> **SKILLS:** Move 2, Sleight of Hand 3

**GEAR:** Nothing of value

#### Count Nepola

Nepola was ordered by Zygofer to muster his soldiers in the battle against King Algarod, which raged over three hundred years ago. The count refused, since he had heard of the sorcerer\u2019s abominable experiments, and stood neutrally aside during the battle.

Zygofer\u2019s revenge was of the cruelest kind. Nepola was buried alive and condemned to remain in the world in eternal undeath. By quenching the green flame that burns in the grave\u2019s brazier, the adventurers can free Nepola and send him to the realm of death.

The count is a tall and proud man with a bronze crown and a trimmed mantle. His ethereal face tells of sorrow and regret.

**Strength 5, Agility 3, Wits 3, Empathy 2**

> **ARMOR:** None. Ghosts are undead creatures, but immaterial, and can only be injured by fire or magic. Even if the ghost is defeated it will only be banished for a quarter of a day before it returns. The only way to permanently banish the ghost is through the spell PURGE UNDEAD (see page 124 in the _Player\u2019s Handbook_ ).

**FOR MONSTER ATTACKS**, see page 94.

#### Countess Ursula

Ursula was persuaded by Zygofer to betray her husband Nepola in exchange for her son\u2019s life. The treacherous sorcerer broke his promise and buried both the son and the countess alive with the count. As a ghost, she is forced to guard her husband\u2019s sarcophagus and make sure that he is never allowed to flee his prison. She gladly tells her story, but leaves out the part of her betrayal against the count. She pleads with graverobbers to avenge the wrongs that Zygofer has committed against her family.

She is bound by Zygofer\u2019s magic to prevent anyone from freeing her husband from his prison. Should the adventurers try to open the count\u2019s sarcophagus, she will try to convince them not to. See more under Events, below.

**Strength 6, Agility 3, Wits 3, Empathy 3**

> **ARMOR:** See above.

**FOR MONSTER ATTACKS**, see page 94 in the Bestiary chapter.

#### The Undead

The undead that haunt The Hollows take many shapes. Some are just ethereal ghosts, others are decayed corpses of the dead who have risen from their graves. The undead keep within the walls of the village and are only active at night. In proximity to the old temple site they become especially active. For ideas on what the undead may be up to, see the table entitled Strange Events in The Hollows on page 196.

For stats for the undead, see the Bestiary in Chapter 5.
'''

content = content[:npc_start_pos] + new_npc_block + content[events_pos:]

# ============================================================
# STEP 3: Global statblock fix — ### Strength … → **Strength …**
# Applies to Weatherstone and Vale of the Dead sections
# (The Hollows NPC block was replaced cleanly above)
# ============================================================

# Any line that is just "### Strength N, ..." headings
content = re.sub(
    r'^### (Strength \d.*?)$',
    r'**\1**',
    content,
    flags=re.MULTILINE
)

# Fix "### **skills:** ..." → "> **SKILLS:** ..."
content = re.sub(
    r'^### \*\*skills:\*\* (.*?)$',
    r'> **SKILLS:** \1',
    content,
    flags=re.MULTILINE
)

# Fix orphaned "**SKILLS:** ..." lines that should be blockquotes
# (cases where TALENTS is already in a blockquote but SKILLS is not)
# Pattern: line starts with "**SKILLS:**" without a ">" prefix
content = re.sub(
    r'^(?!>)\*\*SKILLS:\*\* (.*?)$',
    r'> **SKILLS:** \1',
    content,
    flags=re.MULTILINE
)

# ============================================================
# STEP 4: Write the result
# ============================================================

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. Verifying key sections...")

# Quick verification
with open(filepath, 'r', encoding='utf-8') as f:
    content_check = f.read()

# Check no "### Strength" headings remain
remaining = re.findall(r'^### Strength', content_check, re.MULTILINE)
print(f"Remaining '### Strength' headings: {len(remaining)} (should be 0)")

# Check The Hollows H2 is present
has_h2 = '## The Hollows\n' in content_check
print(f"## The Hollows H2 present: {has_h2}")

# Check numbered locations are ####
sample_loc = '#### 1. the Wall' in content_check or '#### 1. ' in content_check
print(f"Numbered locations at #### level: {sample_loc}")

# Check Monsters and NPCs heading
has_monsters = '### Monsters and NPCs\n' in content_check
print(f"### Monsters and NPCs heading present: {has_monsters}")

# Check NPC entries are ####
has_pollmor = '#### Mrs. Pollmor\n' in content_check
print(f"#### Mrs. Pollmor present: {has_pollmor}")

# Check Events sub-headings are ####
has_beer_war = '#### The Beer War\n' in content_check
print(f"#### The Beer War present: {has_beer_war}")

print("\nDone!")
