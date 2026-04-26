# Third-Party Bestiary Merge — Audit & Uplift Pass

This document is a **merge instruction set** for folding the draft files
`02A-creatures-of-the-forbidden-lands.md` and
`02B-monsters-of-the-forbidden-lands.md` into the canonical
`02-bestiary.md` of Book of Beasts.

It contains:

1. A **duplicate map** identifying which draft entries collide with
   canonical entries in `02-bestiary.md` and must not be merged.
2. For every kept entry: an **uplifted RESOURCES block** that satisfies
   the canonical pattern (≥3 named items, at least one RARE, mechanics
   tied to physiology, second-use penalty, in-world faction or village
   reaction; no flat +1 bonuses).
3. For every kept entry: a **Legends epigraph block** ready to drop into
   the `## Legends` index of `02-bestiary.md`.
4. **Patches** to any broken statblock terminology, and small encounter
   tightening notes where required.

Where a kept entry's existing draft text is already canonical-quality
(statblock fields, Monster Attacks D6 table, prose paragraph, Lore Roll
D6, two Random Encounters with epigraph + body + Terrain Types), the
merge AI should copy it verbatim from the draft and **replace only the
RESOURCES block** with the version below, then add the Legends epigraph
to the `## Legends` section in entry order.

---

## 1. Duplicate Map

| Draft Entry | Source | Verdict | Canonical Analog | Rationale |
| --- | --- | --- | --- | --- |
| Crab Spider | 02A | NOT TO INCLUDE | Giant Spider (Hatchling) | Same niche, same scale, same hunting behavior; canonical hatchling entry already covers ambush web-spider. |
| Green Slime | 02A | NOT TO INCLUDE | Amoeba | Functional subset of the canonical Amoeba; corrosive lurker with no flavor distinct enough to justify a second entry. |
| Grave Servitor | 02A | NOT TO INCLUDE | Tupilaq / Walking Dead | Canon already covers the bound-corpse soldier (Walking Dead, kept below) and the named-target revenant (Tupilaq). |
| Black Digester | 02B | NOT TO INCLUDE | Amoeba | Mechanically the canonical Amoeba with a "split on slash" trick. The split mechanic is a footnote, not a creature. Fold it into the Amoeba entry as a GM note if desired. |
| Air Spirit | 02B | KEEP-AS-VARIANT | Nature Spirit | Canon Nature Spirit is the bridge-and-pasture god. Air Spirit is a wrathful elemental tied to gibbets, cliffs, and weather-headlands. Distinct enough to keep, but the entry should open by naming it as the cousin a Nature Spirit is not. |
| Earth Spirit | 02B | KEEP-AS-VARIANT | Nature Spirit | As above. Quarry-and-cairn elemental, slow and territorial, distinct from the road-and-marsh patron. Keep. |
| Bog Hag | 02B | KEEP-AS-VARIANT | Bog Man | Bog Man is restless dead in the mire. Bog Hag is a shapeshifter midwife at the seam of witch and grave-thing. Different role, different tools, kept. |
| Wereboar / Werewolf | 02B | KEEP | Shapeshifter | Canon Shapeshifter is an amorphous mimic, not a lycanthrope. Lycanthropes are a distinct cycle of cursed kin, kept. |
| Tunneler | 02B | KEEP | Iron Dragon | Smaller subterranean kin; canonical Iron Dragon is world-rooted, cataclysmic. Tunneler is a road-cellar predator; kept. |
| Giant Scorpion | 02B | KEEP | Skolopendra | Skolopendra is the abyss-worm cousin. Giant Scorpion is the surface chitin-thing. Kept. |
| Clay Golem / Iron Golem | 02B | KEEP | Greater Golem | Canon Greater Golem is the dwarven oath-prison. Clay and Iron are size-and-purpose variants suited to chapels, foundries, and treasuries; kept. |
| Death Magister | 02B | KEEP | Mummy / Vampyr | Canon mummy is dynastic remains; vampyr is blood-cursed. Death Magister is the lich type — sorcerer who outlived grief; kept. |
| Walking Dead | 02A | KEEP | (no canonical analog) | Canon has Tupilaq, Mummy, and Bog Man, but no plain shambling revenant in numbers. Kept. |
| Carrion Wing, Ape-Man, Bugbear, Giant Centipede, Crawling Claw, Little Gargoyle, Glass Ooze, Goblin, Tunnel Maw, Hell Hound, Night-Pup, Ogre, Giant Rat, Giant Toad, Fear-Drinker, Corpse Ogre, Warlock of the Black Tower | 02A | KEEP | (no canonical analog) | Lesser-foe gangs and singular minor monsters. No collision with canon. Kept. |
| Road Champion, Black-Fletch Archer, Cutpurse, Wise-Hand, Shield Knight, Town Guard, Clan Hunter, Horse Warrior, Poisoner | 02A | KEEP | (humanoid; exempt from duplicate rule) | Humanoid variants are explicitly exempt; these are people, not monsters, and serve as the bestiary's human-foe roster. Kept. |
| Pale Ape, Star-Watcher, Snake Queen, Thought-Kraken, Rock-Hanger, Night Bride, Grave Bat | 02B | KEEP | (no canonical analog) | All distinct in role and ecology from any canonical entry. Kept. |

---

## 2. Statblock & Terminology Patches

These are repairs that must be made to the draft text before merge. They
are small.

- **02B Iron Golem, Monster Attacks row 4:** if the draft row reads
  `CMBAL CLAP`, replace with `IRON CLAP` (current draft already reads
  `IRON CLAP` — verify before merge; an earlier session may have left
  the typo `CYMBAL CLAP` in some local copies).
- **02B Tunneler, opening prose:** keep as drafted.
- **02A NUMBER APPEARING fields:** the draft uses an en-dash ranges
  like `1–6`. Canon uses `1–6` (en-dash) consistently. No change.
- **All draft RESOURCES blocks:** replace wholesale with the uplifted
  blocks below. The draft blocks have only two named items, no RARE
  marker, and several flat `+1` bonuses (e.g., `heart-stone`,
  `boar hide`). Those are not canonical and must go.
- **02B Air Spirit and Earth Spirit:** prepend a one-sentence opener
  naming each as a wrathful elemental cousin to the canonical Nature
  Spirit, distinct in temper and ground (see uplifted prose below).

---

## 3. Uplifted Entries — 02A Creatures

For every entry below, the draft statblock, prose, and (where present)
Random Encounters in `02A-creatures-of-the-forbidden-lands.md` are
canonical-quality and should be copied verbatim. Add the **RESOURCES
block** to each natural creature, and add the **Legends epigraph** to
the `## Legends` section of `02-bestiary.md` in entry order.

Humanoid bands (Road Champion, Black-Fletch Archer, Cutpurse, Wise-Hand,
Shield Knight, Town Guard, Clan Hunter, Horse Warrior, Poisoner) take a
**GEAR HARVEST** sidebar instead of RESOURCES; humans do not yield
alchemical components in the canonical sense, but their kit is the
practical reward. Each humanoid band still gets a Legends epigraph for
the index.

### Carrion Wing

**Legends epigraph:**

> _The Bloodmarch riders say the carrion wing is the hangman's bird,
> drawn to the smell of a man who has stopped fighting. They will not
> shoot one in the open sky for fear it carries the soul of a coward
> and the soul will fly home with the arrow._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or ALCHEMIST talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **white pinion (RARE)**, **hooked beak**, or **gut-stone**, from a
> slain carrion wing. The bird's hooked spear is found beside the
> body, intact regardless of dice rolled.
>
> **White pinion (RARE):** A single primary feather, white at the root
> and ash at the tip. Bound to an arrow shaft by a HUNTER over a
> Quarter Day, it grants a D10 Artifact Die to one MARKSMANSHIP roll
> made against a target above ground level (cliff, roof, tower, or
> bird in flight). The arrow returns to the quiver if it misses, but
> the next time the hunter sleeps under open sky a carrion wing will
> circle camp at dawn and refuse to leave for a Quarter Day. The
> Bloodmarch clans pay forty silver for any white pinion brought
> unblooded.
>
> **Hooked beak:** Black horn the length of a man's thumb. Set into a
> spear or hooked weapon by a SMITH, it grants a D8 Artifact Die to
> one MELEE attack made to disarm or pull a foe from cover or saddle.
> The hook drinks blood: after first use, the wielder must succeed on
> an ENDURANCE roll or take the HUNGRY condition until they next eat
> meat.
>
> **Gut-stone:** A pebble swallowed by the bird to grind bone. Carried
> in a pouch, it grants a D8 Artifact Die to one SCOUTING roll made on
> upland or cliff ground. Iron Guard sergeants confiscate them on
> sight; they take a gut-stone as proof its bearer has been near the
> high gallows.

### Ape-Man

**Legends epigraph:**

> _The hill-folk on the western slopes do not name the ape-men out
> loud, only point at the cave mouth and turn the face away. They are
> not kin, the old wives say, but they were once near enough to kin
> that the gods turned the world's back on them, and now they take
> tools because they remember what tools are for and not why._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER talent, with a HEALING or SURVIVAL
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **flint-fang (RARE)** or **knuckle-hide**, from a slain ape-man. The
> ape-man's bone club is found beside the body, intact regardless of
> dice rolled.
>
> **Flint-fang (RARE):** A canine tooth blacker than common bone, sharp
> enough to score iron. Hafted into a knife or spear by a SMITH, it
> grants a D10 Artifact Die to one MELEE attack against an unarmored
> foe or one HUNT roll made against a hill-creature. The bearer
> dreams of the ape-man's last hunt every night for a moon and wakes
> HUNGRY. Druids burn flint-fangs on sight as kin-defilement.
>
> **Knuckle-hide:** Coarse skin from the back of the hand. A TANNER
> works it into a glove or grip-wrap over a Quarter Day; the wearer
> gains a D8 Artifact Die to one MIGHT roll made for climbing or
> hauling each Quarter Day. The glove never washes clean, and dogs
> will not let the wearer near a flock.
>
> **Bone club:** Whatever the ape-man was carrying. A heavy weapon of
> long-bone and flint chip; it counts as a Heavy Weapon (damage 2,
> two-handed) and grants a D8 Artifact Die to the wielder's first
> attack of any fight. After first use the wielder must succeed on a
> WITS roll or strike the nearest ally instead of the foe.

### Bugbear

**Legends epigraph:**

> _The forest-edge folk call the bugbears the ones who came in by the
> back door. They were never given a place at the gods' table and
> have not forgotten it. Where a wolf will run, a bugbear will wait;
> where a man will count his iron, a bugbear will count the men._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or TANNER talent, with a HEALING or
> CRAFTING roll, recovers one of the following per ⚔️ rolled, player's
> choice: **musk-gland (RARE)** or **shoulder-mantle**, from a slain
> bugbear. The bugbear's heavy cudgel and hide coat are found beside
> the body, intact regardless of dice rolled.
>
> **Musk-gland (RARE):** A swollen sac at the throat that smells of
> wet bark and old blood. Smeared on a campsite, it keeps wolves,
> hounds, and bears at bay for one full night; one bugbear yields D3
> applications. Anyone sleeping in the smear must succeed on an
> ENDURANCE roll or wake with the HUNGRY condition. Beast-handlers
> will not take the musk into their kennels at any price.
>
> **Shoulder-mantle:** Thick neck-and-shoulder hide. Worked by a
> TANNER over one Quarter Day, it yields a hooded cloak that grants a
> D8 Artifact Die to one STEALTH roll made in forest or scrubland and
> wards off the COLD condition for one journey leg. The cloak smells
> of bugbear to any other bugbear within a stretch.
>
> **Heavy cudgel:** The bugbear's own. Knotted oak and iron-shod, it
> counts as a Heavy Weapon (damage 2, blunt). Wielded against a
> shield, it deals one extra Gear damage on a hit. The Iron Guard
> takes such a club as proof its bearer is a forest-raider; the Raven
> Sisters will exchange one for an ENDURANCE charm.

### Giant Centipede

**Legends epigraph:**

> _They breed where the cellar floor stays wet and the stone never
> sees the sun. The miller's wife will tell you to keep the lamp
> close and the foot bare, because the boot lets the bite under the
> skin without the wearer ever knowing they were bitten._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or HUNTER talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **paralytic milk (RARE)**, **chitin plate**, or **leg-spike**, from
> a slain giant centipede.
>
> **Paralytic milk (RARE):** A thin venom milked from the head fangs.
> Brewed by a POISONER, it yields one paralyzing poison of Potency 7;
> one centipede yields a single dose. The brewer must succeed on an
> ENDURANCE roll or take 1 point of damage to Agility for the next
> stretch. Hedge healers buy paralytic milk for childbirth ease and
> will testify against any seller who let the dose go to a Poisoner
> instead.
>
> **Chitin plate:** Banded shell sections from the back. A SMITH binds
> three plates into a buckler over a Quarter Day; the buckler counts
> as a small shield (Armor Rating 1) and grants a D8 Artifact Die to
> one PARRY made against a slashing weapon. The buckler smells of
> damp cellar in any closed room and unsettles dogs.
>
> **Leg-spike:** A single barbed leg, longer than a finger. Used as a
> caltrop, one spike denies one zone of ground for a stretch; any
> creature crossing must succeed on a MOVE roll or take 1 point of
> damage and the BLEEDING condition. After use the spike rots and
> cannot be reused.

### Crawling Claw

**Legends epigraph:**

> _The grave-warden in Margelda keeps a jar of severed fingers in lime
> by his door, and every village child knows why. He cuts them off
> the dead before he closes the cairn. He says he has lived to be old
> by knowing what a hand will do once a sorcerer has called it by
> name._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a HEALING
> or LORE roll, recovers one of the following per ⚔️ rolled, player's
> choice: **bound-finger (RARE)** or **knuckle-rune**, from a slain
> crawling claw. The ring or thumb-band the claw was bound by is
> found tangled in its tendons, intact regardless of dice rolled.
>
> **Bound-finger (RARE):** A single finger, still warm to the touch.
> Sewn into a glove, it grants the wearer a D10 Artifact Die to one
> SLEIGHT OF HAND roll made to pick a lock, slip a pocket, or open a
> sealed box; one claw yields D3 fingers. After use, the wearer must
> succeed on a WITS roll or speak the name of the dead the finger
> came from aloud, in their own voice. Druids hang any wearer caught
> with a bound-finger from the nearest tree without trial.
>
> **Knuckle-rune:** A symbol scored into the back of one knuckle.
> Copied onto wax over a chest or door by an ALCHEMIST, the seal
> grants a D8 Artifact Die to one MANIPULATION roll made by the next
> person to lie about the seal's contents. The rune fades on the
> third such use and cannot be copied twice from the same claw.
>
> **Binding ring:** Whatever the sorcerer used to fix the claw to its
> task. Worn by an adventurer, it grants a D8 Artifact Die to one
> LORE roll concerning death magic, but the wearer must succeed on an
> ENDURANCE roll each dawn or wake with one finger numb until noon.
> The Raven Sisters will buy a binding ring for thirty silver and
> ask no question.

### Little Gargoyle

**Legends epigraph:**

> _The little gargoyles were carved by the cathedral-stonemen of
> Lochrann to keep the rain off the saints. The masons never agreed
> what woke them. Some say it was the saints' patience running out.
> Some say it was the rain remembering how the masons had spoken to
> their wives._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or SMITH talent, with a CRAFTING or
> LORE roll, recovers one of the following per ⚔️ rolled, player's
> choice: **acid-tongue (RARE)** or **stone-eye**, from a smashed
> little gargoyle.
>
> **Acid-tongue (RARE):** A blackened length of cured-stone tongue,
> still slick. Snapped over a lock, manacle, or hinge, it eats
> through the iron in one stretch; one gargoyle yields a single
> tongue. Anyone splashed by the acid takes 1 point of damage to
> Strength. Temple wardens take possession of any acid-tongue brought
> within a stretch of consecrated stone, no questions, no return.
>
> **Stone-eye:** A flat polished pebble where the gargoyle's eye sat.
> Set into a watch ring by a SMITH, it grants a D8 Artifact Die to
> one SCOUTING roll made to spot a hidden watcher on a roof, ledge,
> or upper window. The wearer's own eyes water in any building still
> consecrated to a god, and a temple sister will know on sight.
>
> **Mortar-grit:** A handful of crushed stone-flesh. Mixed into a
> wall section by a BUILDER over a Quarter Day, it grants a D8
> Artifact Die to one CRAFTING roll made on the wall and unsettles
> beasts within a stretch of it.

### Glass Ooze

**Legends epigraph:**

> _The miners on the Halberg shaft put their dead in the ooze rather
> than carry the bodies up. They said the ooze kept the cousins
> better than the priest could have. Every now and then a cousin
> looks back out of the corridor air, and the new shift is told not
> to wave._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST talent, with a HEALING roll,
> recovers one of the following per ⚔️ rolled, player's choice:
> **clear lens (RARE)** or **suspended coin**, from a slain glass
> ooze.
>
> **Clear lens (RARE):** A palm-sized disc of the ooze's body,
> hardened in dry air. Held to one eye for a stretch, it grants a
> D10 Artifact Die to one INSIGHT roll made to detect lies, glamour,
> or assumed shapes; one ooze yields a single lens. The lens
> shatters at first use and the user must succeed on an ENDURANCE
> roll or weep clear oil for the next Quarter Day. The Raven Sisters
> will trade a healing potion for any unblooded clear lens.
>
> **Suspended coin:** Whatever the ooze had been carrying inside its
> body — coins, buckles, knife heads, a wedding ring. Roll one
> standard coin per Senses success on the search roll, plus one
> personal trinket of GM choice. A trinket recognized by anyone in
> the next settlement triggers a moral debt; the locals expect the
> finder to return it or explain why not.
>
> **Digesting jelly:** A jar of slow translucent matter. Smeared on
> rope, hinge, or skin, it dissolves the bond it touches over one
> Quarter Day. After use the jar must be sealed in lead or glass
> within a stretch, or it eats through its own container.

### Goblin

**Legends epigraph:**

> _The goblins are the ones who remember every torch-house door we
> ever forgot to bar. The grandmothers of Margelda keep one window
> shut even on hot nights; they say the goblins counted the one we
> left open and have not forgotten the count._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or ALCHEMIST talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **night-eye paste (RARE)** or **goblin tongue**, from a slain
> goblin. The goblin's short bow, knife, or spear is found beside
> the body, intact regardless of dice rolled.
>
> **Night-eye paste (RARE):** Yellow grease wrung from the eye-ducts.
> Smeared under the eyes, it grants a D10 Artifact Die to one
> SCOUTING roll made in full dark and one MARKSMANSHIP roll made
> without lamp-light, both within the same Quarter Day; one goblin
> yields a single dose. The user weeps yellow for the next dawn and
> any goblin within a stretch will smell them out. Iron Guard
> sergeants flog men caught wearing the paste under a watch helm.
>
> **Goblin tongue:** A small black tongue, kept dry. Bitten between
> the teeth before a parley, it grants a D8 Artifact Die to one
> MANIPULATION or INSIGHT roll made against another goblin or
> goblin-ally. The user spits black for a stretch after, and any
> village child who sees them spit will repeat the story.
>
> **Goblin gear:** The goblin's own knife or short bow. Worn by
> another goblin, it grants no benefit; worn by a non-goblin, the
> wielder must succeed on an INSIGHT roll once per fight or hesitate
> at the wrong moment, costing the first action of that round.

### Tunnel Maw

**Legends epigraph:**

> _The quarry boys at Storfall hung a salt-bell on a rope across the
> arch above the loading yard. They said the maw could not stand the
> sound of salt. Twice a season the bell goes silent before the
> first scream comes up the road. The boys never replace the rope
> the same day._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or ALCHEMIST talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **clinging-feeler (RARE)** or **gripping pad**, from a slain tunnel
> maw.
>
> **Clinging-feeler (RARE):** A long pale tendril, still trying to
> close. Bound to a hook or grappling line by a HUNTER over a
> Quarter Day, it grants a D10 Artifact Die to one MOVE roll made
> for climbing, swinging, or arresting a fall; one maw yields a
> single feeler. Any other maw within a stretch of the bound feeler
> goes still and silent for one Quarter Day, but the bearer attracts
> a second maw within the next week if they sleep in cave-dark. The
> Stoneborn will trade a forge-favor for any clinging-feeler bound
> to dwarven climbing irons.
>
> **Gripping pad:** A puckered disc from the underside of a feeler.
> Set into a glove or boot sole by a TANNER, it grants a D8 Artifact
> Die to one MIGHT roll made to hold ground, brace a door, or stop a
> shove. After first use the pad smells of cellar water and dogs
> will not approach the wearer for the rest of the day.
>
> **Cave-throat membrane:** The wet sleeve of skin that lines the
> creature's throat. Stretched and dried by an ALCHEMIST, it yields
> one waterproof scroll-case that protects writings from rain, river,
> or splash for one full season; the case spoils at season's end and
> bleeds black ink on whatever it held.

### Hell Hound

**Legends epigraph:**

> _The Iron Guard hunt down a hell hound the way they hunt a heretic.
> Both leave a track only the wrong kind of priest can read, and the
> ground after a hell hound has been there will not take seed for
> three years and one feast day._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or HUNTER talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **brimstone gland (RARE)** or **fire-hide**, from a slain hell
> hound. The hound's iron collar, if any, is found in the ash beside
> the body, intact regardless of dice rolled.
>
> **Brimstone gland (RARE):** A red-orange sac at the throat. Lit
> from a lantern flame, it grants a D10 Artifact Die to one MELEE or
> MARKSMANSHIP attack made with a flame-touched weapon and ignites
> the strike-zone for one round; one hound yields a single gland.
> The wielder must succeed on an ENDURANCE roll after the fight or
> take 1 point of damage to Wits as the smell stays in the lungs.
> The Druids will not allow a brimstone gland within a stretch of
> any consecrated grove.
>
> **Fire-hide:** A square of cured pelt. Sewn into a cloak by a
> TANNER over a Quarter Day, it wards off one COLD condition per
> journey leg and grants a D8 Artifact Die to one ENDURANCE roll
> made against fire or smoke. The cloak smells of pitch in any
> closed room.
>
> **Iron collar:** A black-iron neck band. Worn by a hound or beast,
> it grants the master a D8 Artifact Die to one ANIMAL HANDLING roll
> per Quarter Day; the beast's eyes turn yellow over a moon's worth
> of wear, and any temple priest will refuse to bless a beast so
> collared.

### Night-Pup

**Legends epigraph:**

> _The night-pups are a pack-mother's first try. The hill folk in
> the Marges leave a slab of cold meat at the cave-mouth in late
> winter for the pups, because a pack that loses a litter early hunts
> the children who walk to the ice-well alone._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER talent, with a HEALING or SCOUTING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **shadow-milk (RARE)** or **black pelt**, from a slain night-pup.
>
> **Shadow-milk (RARE):** A black fluid drained from the gums, sweet
> and cold. Drunk before sundown, it grants a D10 Artifact Die to one
> STEALTH or MOVE roll made between sundown and midnight; one pup
> yields a single dose. The drinker's breath shows black in cold air
> for a Quarter Day, and a wolfshadow within a stretch will mark the
> drinker as kin and refuse to attack until the breath fades. The
> Howling Path will pay twenty silver for each fresh dose; the Iron
> Guard takes shadow-milk as evidence of cult.
>
> **Black pelt:** A small cured hide. Worked by a TANNER, it yields
> a hood that grants a D8 Artifact Die to one SCOUTING roll made at
> night and wards off COLD for one journey leg. The hood smells of
> wet wolf to any horse.
>
> **Milk-tooth:** A loose canine. Strung on a thong, it grants a D8
> Artifact Die to one CHILDBIRTH HEALING roll made for a kin-mother
> in winter. After use the tooth crumbles to soot.

### Ogre

**Legends epigraph:**

> _The ogre that came to Two-Bridge village in the year of the cold
> lambing did not eat the priest. It ate the priest's fence, the
> priest's cart, and the priest's cousin, and then it sat on the
> bridge for three days waiting for the priest to come back. The
> village still leaves a basket on the bridge in the cold lambing
> month._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or BUTCHER talent, with a HEALING or
> CRAFTING roll, recovers one of the following per ⚔️ rolled,
> player's choice: **ogre marrow (RARE)** or **broad-back hide**,
> from a slain ogre.
>
> **Ogre marrow (RARE):** Yellow fat scraped from the long bones.
> Eaten hot, it grants a D10 Artifact Die to one MIGHT roll and
> wards off the HUNGRY condition for one full journey leg; one ogre
> yields D3 doses. The eater must succeed on a WITS roll after the
> meal or take 1 point of damage to Empathy until the next sunrise
> as the dead ogre's appetite settles into them. Druids burn ogre
> marrow on sight as kin-corruption.
>
> **Broad-back hide:** Heavy thick skin from the shoulders. Worked by
> a TANNER over two Quarter Days, it yields a leather hauberk
> (Armor Rating 4) and grants a D8 Artifact Die to one ENDURANCE
> roll made against blunt damage each fight. The hide reeks of meat
> and unsettles draught beasts.
>
> **Bone club:** Whatever the ogre carried — a tree, a beam, a
> shaped femur. Counts as a Heavy Weapon (damage 3, two-handed). The
> club requires Strength 5 to lift; lesser users suffer a –2 penalty
> to all attacks with it and a –1 penalty to MOVE while carrying it.

### Giant Rat

**Legends epigraph:**

> _A village that finds rats in the granary loft has had two harvests
> stolen and not noticed the first. The grain-keepers of Vond say
> rats keep their own account-books, scratched in the dust under
> sacks, and that the rat-king reads them aloud in the next village
> downstream._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or HUNTER talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **rat-bile (RARE)** or **gnaw-tooth**, from a slain giant rat.
>
> **Rat-bile (RARE):** A green fluid wrung from the gallbladder.
> Brewed by a POISONER, it yields one disease-flux poison of Virulence
> 6; one rat yields a single dose. The brewer must succeed on an
> ENDURANCE roll or take the SICK condition for the next Quarter Day.
> Iron Guard captains hang sellers caught moving rat-bile through a
> walled town.
>
> **Gnaw-tooth:** An incisor harder than oak. Set into a chisel or
> awl by a SMITH, it grants a D8 Artifact Die to one CRAFTING roll
> made on wood, leather, or bone. After three uses the tooth wears to
> a stub and the user must succeed on a WITS roll or wake the next
> dawn with the HUNGRY condition that no meal will satisfy until they
> share the next bread they eat with another mouth.
>
> **Belly-grease:** Rendered rat fat. Smeared on a hinge, lock, or
> trap, it grants a D8 Artifact Die to one SLEIGHT OF HAND roll made
> to open or set the device. The grease reeks of midden for a stretch
> after.

### Giant Toad

**Legends epigraph:**

> _The toad-pools at Marsen are old enough that the toad-mother has
> a name nobody dares write down. The fishers cast a net into the
> reeds before they cross, and if the net comes back chewed, they
> walk the long way around the marsh and apologize to the road._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or HUNTER talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **tongue-glue (RARE)** or **wart-extract**, from a slain giant
> toad.
>
> **Tongue-glue (RARE):** A clear sticky paste milked from the
> tongue-base. Coated on a rope, hook, or weapon-haft, it grants a
> D10 Artifact Die to one MELEE roll made to grapple, disarm, or
> bind; one toad yields D3 applications. After use, the user's hand
> sticks to the weapon for one Quarter Day and they cannot draw or
> sheathe it cleanly. Hedge healers buy tongue-glue at four silver
> per dose for marsh-fever poultices.
>
> **Wart-extract:** Yellow grease scraped from the back warts.
> Brewed by an ALCHEMIST, it yields one Potency 5 sleep poison; one
> toad yields a single dose. The brewer must succeed on an
> ENDURANCE roll or fall asleep within a stretch of finishing the
> brew, no matter the hour.
>
> **Webbed foot:** A single broad foot. Worn over a boot in deep
> mire, it grants a D8 Artifact Die to one MOVE roll made on bog,
> reed, or shallow water each Quarter Day. The foot rots within
> three days and cannot be cured.

### Fear-Drinker

**Legends epigraph:**

> _The Raven Sisters say the fear-drinkers are the cousins the vampyr
> houses do not invite to the funeral. They drink the same hot blood
> but they prefer it taken from someone who is begging. A vampyr
> will kill a man fast for shame; a fear-drinker will let him live
> three nights to keep the cup full._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **panic-blood (RARE)** or **rictus-tooth**, from a slain
> fear-drinker.
>
> **Panic-blood (RARE):** A thick black ichor drained from beneath
> the heart. Drunk in a single swallow, it grants a D10 Artifact Die
> to one fear attack the drinker makes within the same fight; one
> fear-drinker yields a single dose. The drinker takes the SCARED
> condition until the next sunrise, and any companion who sees them
> drink loses 1 Empathy-tied trust until they earn it back. The
> Raven Sisters will not bind the wounds of any adventurer they have
> seen drink panic-blood within a fortnight.
>
> **Rictus-tooth:** A single eye-tooth, longer than the others.
> Sewn into the lining of a hood or coif, it grants a D8 Artifact Die
> to one INSIGHT roll made to read fear or panic in another
> creature. The wearer wakes each dawn with the dry-mouth of a man
> who has been screaming in his sleep.
>
> **Charm-cuff:** Whatever silver or copper the fear-drinker wore at
> the wrist. Worn by another, it grants a D8 Artifact Die to one
> MANIPULATION roll made to calm a panicked crowd or animal. After
> three uses the cuff turns black and any priest will know it on
> sight as cursed metal.

### Corpse Ogre

**Legends epigraph:**

> _A man named Ull paid a battlefield necromancer to wake his
> brother's body for one more season's labor on the family wall.
> Ull is in the wall now and the corpse ogre is on the third
> village. The brother is not in either._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's choice:
> **stitched sinew (RARE)** or **corpse-tallow**, from a slain corpse
> ogre.
>
> **Stitched sinew (RARE):** Long cured cord taken from the seamed
> belly. Used as bowstring, harness, or binding by a CRAFTSMAN, it
> grants a D10 Artifact Die to one MARKSMANSHIP, ANIMAL HANDLING, or
> RESTRAINT roll. One ogre yields a single length. The user dreams
> of the corpse ogre's last living memory each night for a moon and
> wakes EXHAUSTED. Druids will burn any tool strung with stitched
> sinew that they recognize.
>
> **Corpse-tallow:** Yellow fat rendered from the limbs. Burned in a
> watch-lamp, it grants a D8 Artifact Die to one SCOUTING roll made
> on a watch and reveals undead within a stretch as faint blue
> outlines for the duration of the watch. The smell drives off the
> living within the same stretch; allies must succeed on an
> ENDURANCE roll to share the watch.
>
> **Battlefield-iron:** Whatever the corpse ogre carried — a broken
> sword, a salvaged spear, a billhook. Counts as a normal weapon of
> its type but bears the mark of its first owner; the next person
> from the deceased's line who sees the weapon will demand it back,
> and may have a claim worth listening to.

### Walking Dead

**Legends epigraph:**

> _The Aslene riders will not cross a field where a walking dead
> still stands. They say the field has not finished asking what was
> taken from it and is gathering the answer. The riders go around
> and pay the long-track tax in silence._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a HEALING
> or LORE roll, recovers one of the following per ⚔️ rolled, player's
> choice: **grave-salt (RARE)** or **shroud-thread**, from a slain
> walking dead. Whatever clothing or token the body carried in life
> is found about it, intact regardless of dice rolled.
>
> **Grave-salt (RARE):** Pale crystal scraped from the inside of the
> mouth. Cast across a doorway or grave, it prevents one walking
> dead from rising or crossing the threshold for a full season; one
> body yields D3 pinches. The caster must say the dead's name aloud
> at the casting; if the name is unknown, the salt fails and turns to
> water. The Raven Sisters will trade a healing tincture for a pinch
> of grave-salt taken from a body the seller did not bury.
>
> **Shroud-thread:** Dry sinew running through the linen.
> Twisted into a charm-cord by a TAILOR, it grants a D8 Artifact Die
> to one INSIGHT or LORE roll made about the dead the thread came
> from, and the thread sometimes answers a yes-or-no question once
> per Quarter Day if held to the asker's tongue. After the third
> question the thread is finished.
>
> **Token:** Whatever the walking dead carried in life — a wedding
> ring, a child's tooth, a coin from a foreign king. Returned to the
> dead's family, it earns one favor of stronghold scale. Kept, it
> rouses one walking dead within a stretch every dark moon.

### Warlock of the Black Tower

**Legends epigraph:**

> _A warlock of the Black Tower walked into Margelda one autumn,
> bought a hen from the priest's wife, paid in old coin, and
> walked out again. The hen laid black eggs for a week and then
> stopped laying for the rest of her life. The priest's wife still
> calls that the cheap year._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a HEALING
> or LORE roll, recovers one of the following per ⚔️ rolled, player's
> choice: **bound familiar (RARE)** or **grimoire leaf**, from a
> slain warlock. The warlock's staff and grimoire are found beside
> the body, intact regardless of dice rolled.
>
> **Bound familiar (RARE):** The small creature the warlock kept —
> raven, cat, hare, viper — is now masterless and wary. Befriended
> over a Quarter Day with the AWARENESS of an ANIMAL HANDLER, the
> familiar grants its new keeper a D10 Artifact Die to one INSIGHT
> or SORCERY roll per Quarter Day; one warlock yields one familiar.
> The familiar will not stay with a master who has not killed
> something larger than itself within the past moon. The Druids
> will buy the familiar for forty silver and a healing potion.
>
> **Grimoire leaf:** A single page torn from the warlock's book. Read
> by a SORCERER once per Quarter Day, it grants a D8 Artifact Die
> to one Power Level 1 spell of the same path the warlock used.
> After three readings the page goes blank.
>
> **Warlock's staff:** The warlock's own. Used as a focus by another
> SORCERER, it grants a D8 Artifact Die to one casting per fight, but
> the wielder must succeed on a WITS roll after the fight or lose
> their next Willpower point gained. The Raven Sisters will burn
> the staff and the wielder's writing-hand at the wrist if both come
> within reach.

### Humanoid Bands (02A) — Gear Harvest & Legends

For Road Champion, Black-Fletch Archer, Cutpurse, Wise-Hand, Shield
Knight, Town Guard, Clan Hunter, Horse Warrior, and Poisoner, **no
RESOURCES block is added**. Instead, each band's GEAR field already
lists what is taken from the body. Add a line to each entry's prose:
"What they carry is what is left when they fall." The Legends epigraphs
below should be added to the `## Legends` section in entry order.

**Road Champion:**

> _The road champions are the survivors of the bad years between the
> Blood Mist's lifting and the first new lords. They learned that a
> well-mended shirt is worth a knighthood and that a knighthood is
> worth a well-mended shirt. They will tell you which one for a cup
> of beer._

**Black-Fletch Archer:**

> _Some of them are elf-trained and some only wear the look. The way
> to know is the second arrow. An elf-trained killer has already
> nocked it before the first one lands. The other has only the look._

**Cutpurse:**

> _The cutpurse is the hardest profession in the Forbidden Lands to
> die in old. The good ones leave the trade and become millers. The
> bad ones leave the trade and become cutpurses again in the next
> village down the river._

**Wise-Hand:**

> _A wise-hand is what a hedge-priest becomes when she cannot afford
> to fail twice. The villages keep one because the temple is far and
> the temple does not love them as the wise-hand does. The wise-hand
> knows it._

**Shield Knight:**

> _The shield knight is the road-lord's wall made flesh. He does not
> serve a god. He serves the gate. When the gate falls he kills the
> next man through it whether the man is enemy, kin, or his own
> lord, because the gate is what he serves._

**Town Guard:**

> _A town guard is a frightened man with a spear, ten frightened
> friends, and a wage that arrives twice a year. He is more loyal to
> his cousin in the next pair than to the lord whose seal he wears.
> Anyone who plans a fight with town guards must plan against the
> cousin first._

**Clan Hunter:**

> _The clan hunter does not work alone. Hawk, hound, wolf, or bad
> boar; the beast is half her courage and most of her plan. The
> clans say a hunter who outlives her beast is a hunter no longer,
> only a woman in the woods, and the woods will tell her that
> themselves before the next moon._

**Horse Warrior:**

> _The horse warriors of the Bloodmarch were riding the open ground
> before the Blood Mist came and they were riding it again the
> morning the mist lifted. They take the open country with them
> wherever they go. In a city street they are men. On the steppe they
> are weather._

**Poisoner:**

> _The poisoners are the ones who watched their fathers die of bad
> arrows and decided the arrows had been bad enough. They keep the
> trade in the family because the trade is what kept the family
> alive. They will not poison kin. They will poison anyone who has
> ever called them kin and changed their mind._

---

## 4. Uplifted Entries — 02B Monsters

For every entry below, the draft statblock, prose, Monster Attacks D6
table, Lore Roll D6 table, and Random Encounters in
`02B-monsters-of-the-forbidden-lands.md` are canonical-quality and
should be copied verbatim. The merge AI must:

1. Replace each draft RESOURCES block wholesale with the version below.
2. Add the Legends epigraph block to the `## Legends` section of
   `02-bestiary.md` in entry order.
3. For Air Spirit and Earth Spirit, prepend the variant-opening
   sentence given below to the prose paragraph.

### Tunneler

**Legends epigraph:**

> _The tunneler is what the Stoneborn did not finish. The dwarven
> halls below Stoneberg stop at a wall the elders will not name; on
> the other side of the wall the tunnelers turn the stone into road
> and the road into nothing. The dwarves say the wall is what is
> left of the apology._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or HUNTER talent, with a HEALING
> or CRAFTING roll, recovers one of the following per ⚔️ rolled,
> player's choice: **acid gland (RARE)** or **burrow-claw**, from a
> slain tunneler. The carapace plating along the back is found
> intact beside the body, regardless of dice rolled.
>
> **Acid gland (RARE):** A swollen yellow sac at the throat, kept in
> stoppered glass. Broken at a doorway, lock, or gate, it eats
> through worked wood or soft iron in one stretch; one tunneler
> yields a single gland. Anyone splashed by the acid takes 1 point
> of damage to Strength. The Stoneborn forge-masters will pay
> sixty silver for an unbroken gland; the Iron Guard takes
> possession of any gland brought within a stretch of a town gate.
>
> **Burrow-claw:** A single sickle-claw from the foreleg. Bound to
> a digging tool by a SMITH over a Quarter Day, it grants a D8
> Artifact Die to one CRAFTING or SURVIVAL roll involving earth,
> clay, or trenching each Quarter Day. The tool calls a tunneler
> within nine days if used in a settled field; the wielder must
> succeed on an INSIGHT roll to feel the call coming.
>
> **Carapace plate:** Banded shell from the back. A SMITH binds
> three plates into a buckler over a Quarter Day; the buckler
> counts as a small shield (Armor Rating 1) and grants a D8
> Artifact Die to one PARRY made against piercing weapons. The
> buckler smells of damp clay and unsettles draught beasts.

### Pale Ape

**Legends epigraph:**

> _The pale apes were here when the first miners came up the
> Halberg. The miners brought lamps and the apes learned to dread
> them. The miners brought salt and the apes learned to love it. The
> miners are gone and the salt is gone and the apes have remembered
> the lamp and forgotten the salt and that is why the children of
> the village above the shaft do not sing on the path home._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or TANNER talent, with a HEALING or
> CRAFTING roll, recovers one of the following per ⚔️ rolled,
> player's choice: **white pelt (RARE)**, **knuckle-bone**, or
> **cave-tongue**, from a slain pale ape.
>
> **White pelt (RARE):** A full hide bleached by cave-dark. Worn as
> a cloak, it grants a D10 Artifact Die to one SCOUTING roll made
> in cave-dark or snow-glare each Quarter Day; one ape yields a
> single pelt. The cloak is recognizable to any Stoneborn at thirty
> paces and the dwarves will demand it back as kin-relic. Refuse
> and a Stoneborn smith will close the next forge-door against the
> wearer for a season.
>
> **Knuckle-bone:** A heavy finger-bone. Ground into grease by a
> CHEF or ALCHEMIST, it grants one adventurer a D8 Artifact Die on
> one MIGHT roll involving climbing, hauling, or bracing stone.
> After use the eater wakes the next dawn with the HUNGRY condition
> that no meal will satisfy until they have eaten under open sky.
>
> **Cave-tongue:** A flat dark tongue, kept dry. Bitten between the
> teeth before a parley with another pale ape or a feral kin-cousin,
> it grants a D8 Artifact Die to one MANIPULATION roll. The bearer
> spits black for a stretch and any temple priest who sees the spit
> will refuse them sanctuary for the rest of the day.

### Star-Watcher

**Legends epigraph:**

> _The Raven Sisters do not name the star-watchers. They name the
> places where the star-watchers settle and they go around. The
> sisters say a name given to a thing that watches the sky is a
> name borrowed by the sky, and the sky has too many names already._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a
> HEALING or LORE roll, gathers one of the following per ⚔️ rolled,
> player's choice: **void-lens (RARE)**, **eye-stone**, or
> **gaze-ash**, from a slain star-watcher.
>
> **Void-lens (RARE):** A lesser eye, shucked and dried in shadow.
> Set into a bronze frame by a SMITH over a Quarter Day, it creates
> a hand lens that snuffs one magical effect of Power Level 1 once
> per Quarter Day; one watcher yields D3 lenses. The bearer must
> succeed on a WITS roll after each use or take 1 point of damage
> to Wits as the lens drinks the user's own ordered passage. The
> Raven Sisters will trade a healing tincture and a single
> sworn-truth for an unblooded void-lens.
>
> **Eye-stone:** A small dried lens, the size of a coin. Ground
> into dust and breathed before a watch, it grants a D8 Artifact
> Die to one SCOUTING or LORE roll involving stars, omens, or
> portals during that watch. The user's eyes water under any roof
> for the rest of the night.
>
> **Gaze-ash:** Pale dust from the central gaze cavity. Cast across
> a doorway or page, it prevents one Power Level 1 magical
> intrusion (sending, scrying, or compulsion) for a full season.
> The doorway or page bears a faint blue mark thereafter that any
> Sorcerer or Druid will recognize.

### Air Spirit (Variant of Nature Spirit)

**Variant opener (prepend to prose paragraph):**

> An Air Spirit is the wrathful cousin of the canonical Nature Spirit
> in the wind: it does not patron the bridge or the pasture, only
> the cliff, the gibbet, and the headland where the weather changes
> faster than the people on it.

**Legends epigraph:**

> _The cliff shrines on the Aslene coast were built to keep the air
> spirits busy. The shepherds say a spirit with a shrine to mind has
> no time for shepherds. The spirits agree, but only on the days the
> shrines are still standing._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the DRUID or SORCERER talent, with a HEALING
> or LORE roll, catches one of the following per ⚔️ rolled,
> player's choice: **storm-glass (RARE)**, **wind-knot**, or
> **gallows-wisp**, from a banished air spirit.
>
> **Storm-glass (RARE):** A clear lens of frozen air, thumb-sized.
> Hung in a window or gatehouse, it warns of violent weather one
> Quarter Day before the storm strikes for one full season; one
> spirit yields a single glass. The glass shatters at season's end
> and any creature within a stretch of the shattering takes 1 point
> of damage to Wits. The Raven Sisters will trade a Quarter Day of
> sanctuary for any unbroken storm-glass; the Druids will burn the
> household of any seller who lets one go to a sea-raider.
>
> **Wind-knot:** A length of corded air, kept in a sealskin pouch.
> Loosed from the pouch, it grants a D8 Artifact Die to one MOVE
> roll or one MARKSMANSHIP shot from a bow that same round. The
> pouch holds D3 knots from one spirit. After loosing the last
> knot, the bearer's hair stands up under any helm for a Quarter
> Day, and dogs will not approach.
>
> **Gallows-wisp:** A pale strand of wind taken from a gibbet
> shrine. Tied to a gate-post or watch-fire, it grants a D8
> Artifact Die to one SCOUTING roll made by the watch over one
> night. The wisp brings the dreams of the last man hanged at the
> gibbet to the watcher; the watcher must succeed on a WITS roll
> at dawn or refuse to stand the same watch for nine days.

### Earth Spirit (Variant of Nature Spirit)

**Variant opener (prepend to prose paragraph):**

> An Earth Spirit is the wrathful cousin of the canonical Nature
> Spirit in the stone: it does not patron the road or the marsh,
> only the broken cairn, the bitten quarry, and the grave opened
> for gain.

**Legends epigraph:**

> _The dwarves of Stoneberg say the earth spirits are the stone's
> own grief. The stone has been mined and shaped and sold for an
> age and now and again the grief catches up. The dwarves do not
> apologize. They do, however, walk the long way around._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the DRUID or SMITH talent, with a HEALING or
> CRAFTING roll, gathers one of the following per ⚔️ rolled,
> player's choice: **heart-stone (RARE)**, **grave-dust**, or
> **cairn-fragment**, from a settled earth spirit.
>
> **Heart-stone (RARE):** A single black stone the size of a fist,
> still warm. Built into a stronghold wall, gate, or hearth by a
> BUILDER over a Quarter Day, it grants the wall section a D10
> Artifact Die to one defense roll per attack on the stronghold,
> for one full season; one spirit yields a single heart-stone. The
> wall section bleeds water in the first frost of the next season
> and the stone must be replaced or removed. The Stoneborn will
> trade a forge-favor for any heart-stone built into dwarven
> mortar; the Druids will demand its return to the cairn that was
> broken to make it.
>
> **Grave-dust:** A pinch of fine ash from the spirit's body.
> Thrown across a doorway, it grants a D8 Artifact Die to one
> INSIGHT roll made to detect sorcery, trespass, or kin-debt over
> broken ground. The dust is gone after one casting.
>
> **Cairn-fragment:** A shard of cut stone from the spirit's
> shoulder. Bound to a hammer or pick by a SMITH, it grants a D8
> Artifact Die to one CRAFTING roll made on stone or earth. After
> three uses the fragment cracks; the wielder must replace it with
> stone taken in apology from the cairn the spirit rose from, or
> the tool turns brittle and breaks at the next blow.

### Giant Scorpion

**Legends epigraph:**

> _The masons of the Hollow Quarry kept a giant scorpion in the
> deep cut for a generation. They fed it the workers who stole, and
> their work cost less stone than any other quarry in the Marges.
> When the masons died of plague the scorpion ate the priest who
> came to bless the bodies. The quarry has not been worked since,
> and the stone there is the cheapest in the country to anyone with
> the nerve._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or ALCHEMIST talent, with a HEALING
> roll, recovers one of the following per ⚔️ rolled, player's
> choice: **venom sac (RARE)**, **eye-plate**, or **claw-hook**,
> from a slain giant scorpion.
>
> **Venom sac (RARE):** A swollen black gland from the tail.
> Brewed by a POISONER, it yields one paralyzing poison of Potency 7;
> one scorpion yields a single dose. The brewer must succeed on an
> ENDURANCE roll or take 1 point of damage to Agility for the next
> Quarter Day. Hedge healers buy venom sacs for childbirth pain at
> three silver per dose; the Iron Guard hangs sellers caught moving
> venom through a walled town.
>
> **Eye-plate:** A polished disc from the side of the carapace.
> Set in a helm or shield by a SMITH, it grants a D8 Artifact Die to
> one SCOUTING roll made to spot ambush in stone or ruin ground.
> The plate fogs in any temple consecrated to a sun-aligned god and
> the wearer is recognizable by it.
>
> **Claw-hook:** A single pincer-tip, hardened. Hafted to a polearm
> or boarding hook by a SMITH, it counts as a Heavy Weapon (damage
> 2, two-handed) and grants a D8 Artifact Die to one MELEE roll
> made to disarm or grapple in close ground. The hook chips the
> first time it strikes worked iron; the Stoneborn will retrim the
> hook for a meal and a story.

### Clay Golem

**Legends epigraph:**

> _A clay golem is what a temple builds when the temple has stopped
> trusting its own faithful. The dwarven word for it is the same
> word as the dwarven word for "promise broken at the altar". The
> dwarves do not build clay golems. The dwarves do not have any
> word for "promise broken at the altar" that is not the word for
> "clay golem"._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or SMITH talent, with a CRAFTING
> roll, gathers one of the following per ⚔️ rolled, player's
> choice: **sigil shard (RARE)**, **kiln-dust**, or **bound
> tongue**, from a slain clay golem.
>
> **Sigil shard (RARE):** A fragment of the inscription that bound
> the golem, taken from the brow or the heel. Pressed into wax over
> a chest or door by a SMITH or SORCERER, it grants a D10 Artifact
> Die to one SLEIGHT OF HAND or CRAFTING roll made to seal or
> ward it; one golem yields a single shard. The seal holds against
> any thief save the golem's original maker; once broken, the shard
> blackens and any temple priest within a stretch will know the
> seal was the golem's. The Druids will burn the shard and the
> seller's hand if the seal protected stolen tithe.
>
> **Kiln-dust:** A handful of fired-clay grit from the body. Mixed
> into mortar by a BUILDER, it grants a D8 Artifact Die to one
> CRAFTING roll made on the wall section and unsettles draught
> beasts within a stretch for one season.
>
> **Bound tongue:** A small clay disc from inside the mouth, often
> still mouthing the maker's command. Held to a sleeper's lips, it
> answers one yes-or-no question once per Quarter Day in the
> sleeper's own voice. After the third question the disc crumbles.
> The Raven Sisters will demand the disc on first sight as
> kin-defilement.

### Iron Golem

**Legends epigraph:**

> _The iron golems are the dwarves' apology to the elves for the
> cataclysm of the long forge. The dwarves do not call them an
> apology. The elves do not call them an apology either. The
> golems stand in the doorways of forges no living dwarf or elf
> has opened in three centuries, and the doorways stay shut, which
> is a kind of apology that does not require either party to bow._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SMITH talent, with a CRAFTING roll,
> gathers one of the following per ⚔️ rolled, player's choice:
> **furnace-heart (RARE)**, **smoke-lung**, or **furnace-scale**,
> from a slain iron golem.
>
> **Furnace-heart (RARE):** A blackened iron core from the chest
> cavity, still warm. Built into a forge by a SMITH over two Quarter
> Days, it grants the forge a D10 Artifact Die to one CRAFTING roll
> per Quarter Day involving steel, blade, or armor work, for one
> full season; one golem yields a single heart. The forge runs hot:
> at season's end the SMITH must succeed on an ENDURANCE roll or
> take 1 point of damage to Strength as the heart goes cold. The
> Stoneborn forge-masters will trade a finished blade for any
> furnace-heart and will not haggle the price.
>
> **Smoke-lung:** A bellows-shaped organ from the body. Fitted into
> a forge bellows by a SMITH, it reduces one weapon or armor
> CRAFTING project by one Quarter Day. After three projects the
> lung blackens and must be replaced; the spent lung is taken by
> the Stoneborn as proof of work for forge-rights.
>
> **Furnace-scale:** A square of iron skin. Built into armor by a
> SMITH, it grants a D8 Artifact Die to one ENDURANCE roll against
> heat, fire, or smoke each Quarter Day. The armor smells of pitch
> in any closed room, and any temple priest will refuse to bless
> the wearer until the scale is removed.

### Bog Hag (Variant of Bog Man)

**Legends epigraph:**

> _A bog hag is the marsh's apology for not having a midwife. The
> villages around Lake Varda say so out loud and the bog hags say
> so without speaking. Half the children in those villages were
> caught in the bog hag's hands first and the village's hands
> second, and the village pretends it does not know which children._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or DRUID talent, with a HEALING
> roll, draws one of the following per ⚔️ rolled, player's choice:
> **hag-tooth (RARE)**, **reed skin**, or **borrowed face**, from a
> slain bog hag.
>
> **Hag-tooth (RARE):** A single curved tooth, kept dry. Ground
> into powder, it grants a D10 Artifact Die to one HEALING roll
> involving childbirth, miscarriage, or swamp-fever, with a Potency
> 7 bonus against marsh-born disease; one hag yields D3 doses. The
> healer must succeed on an EMPATHY roll after the casting or grow
> attached to the patient for one full season and refuse to leave
> their side until that season ends. The Raven Sisters demand any
> hag-tooth on sight and trade a sanctuary night for it.
>
> **Reed skin:** A patch of gray skin from the cheek or throat.
> Worn beneath the tongue, it grants a D8 Artifact Die to one
> MANIPULATION roll made while speaking as another person. After
> the third use the skin rots and the wearer's own voice goes hoarse
> for a stretch.
>
> **Borrowed face:** A glamour-mask the hag had been wearing — the
> face of a midwife, widow, or matron she had observed. Worn over
> one's own face for one Quarter Day by a SORCERER or DRUID, it
> grants the wearer the borrowed face's appearance and a D8
> Artifact Die to one INSIGHT or MANIPULATION roll made by anyone
> who knew the original. After use, the original (if living) wakes
> from a black sleep and remembers a stranger's day in their own
> body. The Druids will burn the wearer of a stolen face within a
> stretch of any village they enter.

### Death Magister

**Legends epigraph:**

> _The Raven Sisters do not name a death magister. They name the
> village that sheltered one and they do not pass through that
> village again. They say a magister cannot be killed by a sister
> who has eaten that village's bread, and the bread is always the
> first thing the magister gave to the village._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a
> HEALING or LORE roll, gathers one of the following per ⚔️ rolled,
> player's choice: **phylactery ash (RARE)**, **grave-nail**, or
> **shroud-ink**, from a slain death magister whose phylactery has
> already been broken.
>
> **Phylactery ash (RARE):** Black grit from the broken vessel.
> Mixed into ink, it grants a D10 Artifact Die to one LORE roll
> concerning necromancy, death magic, or the dead, and the writing
> done in the ink cannot be magically read by any living
> necromancer for one full season; one magister yields a single
> jar. The ink stains the writer's tongue black for a Quarter Day
> and any temple priest will know the stain on sight. The Druids
> will burn the writing and the writer's hand at the wrist if both
> come within reach.
>
> **Grave-nail:** A long iron spike from the magister's coffin or
> shroud-wrappings. Driven into a corpse before sundown, it
> prevents that corpse from rising as undead for the season; one
> magister yields D3 nails. The driver must say the dead's name
> aloud at the driving; if the name is unknown, the nail rusts to
> dust.
>
> **Shroud-ink:** A dry vial of black ink the magister wrote with.
> Used to copy one Power Level 1 spell of necromancy by a SORCERER,
> it grants a D8 Artifact Die to that spell's first casting. The
> caster must succeed on a WITS roll after the casting or wake the
> next dawn unable to remember the spell.

### Snake Queen

**Legends epigraph:**

> _The serpent-cult of Wyrm hides snake queens in spring caves and
> shrine courts and old bath-houses where the tile has gone to ruin.
> The cult say the queens are kin. The Iron Guard say the queens
> are abomination. The villages downstream say the spring water has
> never been cleaner, and they pay the cult's tithe and ask no other
> question._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or SORCERER talent, with a
> HEALING roll, gathers one of the following per ⚔️ rolled,
> player's choice: **shed crown scale (RARE)**, **venom tear**, or
> **mirror-fragment**, from a slain snake queen.
>
> **Shed crown scale (RARE):** A single golden scale shed from the
> diadem of serpents. Worn in a pouch around the neck, it grants a
> D10 Artifact Die to one INSIGHT or SCOUTING roll made against
> deception, glamour, or hidden watchers, and one INSIGHT roll per
> Quarter Day made to pierce another snake queen's gaze; one queen
> yields a single scale. After three uses the scale tarnishes and
> the wearer's own eyes turn gold-green for a moon, and any
> serpent-cultist will know them on sight. The Congregation of the
> Serpent will pay sixty silver for the return of any shed crown
> scale taken from a recognized queen.
>
> **Venom tear:** A drop of clear venom milked from the tear-duct.
> Brewed by a POISONER, it yields one paralyzing poison of Potency 7;
> one queen yields a single dose. The brewer must succeed on an
> ENDURANCE roll or take 1 point of damage to Agility for the next
> Quarter Day.
>
> **Mirror-fragment:** A shard of bronze mirror the queen kept by
> her. Worn in a brooch or set into a shield boss, it grants a D8
> Artifact Die to one PARRY made against a snake queen's gaze attack
> or any glamour-bound foe. The bearer's own reflection in still
> water shows a serpent's face for one Quarter Day after each use.

### Thought-Kraken

**Legends epigraph:**

> _The thought-krakens were old when the elves were young. The
> Raven Sisters say so without joy. They say a thought-kraken
> answers any question once and demands the questioner as the
> answer's keeper for the rest of the questioner's life. The
> sisters do not ask thought-krakens questions. They send their
> apprentices instead._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the SORCERER or ALCHEMIST talent, with a
> HEALING or LORE roll, gathers one of the following per ⚔️ rolled,
> player's choice: **brain pearl (RARE)**, **whisper ink**, or
> **memory-tendril**, from a slain thought-kraken.
>
> **Brain pearl (RARE):** A small white sphere taken from the
> central mass. Crushed under the tongue, it grants a D10 Artifact
> Die to one INSIGHT or LORE roll concerning lies, hidden motive,
> or memory; one kraken yields D3 pearls. The crusher must succeed
> on a WITS roll after the use or lose one personal memory of the
> last week, GM's choice. The Raven Sisters will not bind the
> wounds of any adventurer they have seen crush a brain pearl
> within a fortnight.
>
> **Whisper ink:** A vial of black ink the kraken bled when struck.
> Used to write one short message, the message is heard once in the
> reader's mind and then vanishes from the page; one kraken yields
> a single vial. The writer's voice carries oddly for the rest of
> the day; anyone who hears the writer must succeed on an INSIGHT
> roll or assume the writer is lying.
>
> **Memory-tendril:** A short cured length of dried tentacle. Worn
> against the temple by a SORCERER, it grants a D8 Artifact Die to
> one LORE roll concerning a place, person, or event the wearer
> has not seen but the tendril has. After three uses the tendril
> rots and the wearer dreams the kraken's last hunt for nine
> nights.

### Rock-Hanger

**Legends epigraph:**

> _The smugglers above the Halberg crossing pay the rock-hanger in
> goat and silver. The Iron Guard pays the smugglers in gallows.
> The rock-hanger pays neither and waits at the arch for whoever
> comes next._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or TANNER talent, with a HEALING
> roll, gathers one of the following per ⚔️ rolled, player's
> choice: **ceiling tooth (RARE)**, **tendril cord**, or **stone
> mantle**, from a slain rock-hanger.
>
> **Ceiling tooth (RARE):** A long curved tooth from the inverted
> mouth. Hung above a doorway or watch-post by a CRAFTSMAN, it
> grants a D10 Artifact Die to one SCOUTING roll made to spot
> overhead ambush, and a free reroll on the watch's first SCOUTING
> roll each night, for one full season; one rock-hanger yields a
> single tooth. The tooth darkens at season's end and must be
> burned in salt or the next ambush comes from below instead. The
> Stoneborn will trade a forged hook for any unblooded ceiling
> tooth.
>
> **Tendril cord:** A long strand of dried tendril. Used as rope
> by a CRAFTSMAN over a Quarter Day, it grants a D8 Artifact Die to
> one CLIMB or hauling effort each Quarter Day for the cord's
> length of work. After three days of use the cord brittles and
> snaps; the next attempt to use it is the failure that kills the
> climber.
>
> **Stone mantle:** A square of carapace from the back. Bound to a
> shield or buckler by a SMITH, it grants a D8 Artifact Die to one
> PARRY made from above (against a charging mounted foe, falling
> stone, or a dropped weapon). The mantle adds 1 to the shield's
> weight; the bearer's MOVE rolls take a –1 penalty for as long as
> the shield is carried.

### Night Bride

**Legends epigraph:**

> _The night brides walk at the seam between bargain and want. The
> grandmothers of the Aslene clans say the night bride does not
> come uninvited. She comes when a household has stopped saying out
> loud what it does at night, and she takes what the household has
> stopped naming. The grandmothers say this and then they tell
> their grand-daughters to leave the front door unlatched anyway._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the ALCHEMIST or SORCERER talent, with a
> HEALING roll, recovers one of the following per ⚔️ rolled,
> player's choice: **mirror-splinter (RARE)**, **kiss-ash**, or
> **vow-ribbon**, from a slain night bride.
>
> **Mirror-splinter (RARE):** A shard of bronze the bride wore at
> her throat. Kept in a purse or sewn in a cuff, it grants a D10
> Artifact Die to one INSIGHT roll made against glamour, charm, or
> assumed identity, and a free reroll on the next ENDURANCE roll
> made to resist a charm; one bride yields a single splinter. The
> splinter darkens after three uses and the bearer dreams of the
> bride's last bridegroom for nine nights. The Raven Sisters will
> trade sanctuary for any unblooded mirror-splinter.
>
> **Kiss-ash:** A pinch of dry ash from the bride's lips. Blown in
> a sleeper's face, it grants a D8 Artifact Die to one
> MANIPULATION roll made before dawn against that sleeper. The
> sleeper wakes with the SCARED condition and the user takes 1
> point of damage to Empathy for the next Quarter Day.
>
> **Vow-ribbon:** A length of black silk the bride had bound to
> her wrist. Tied to a wedding gift, oath-token, or contract, it
> grants a D8 Artifact Die to one MANIPULATION roll made to
> persuade the gift's recipient to honor the oath the gift carried.
> The ribbon rots within nine days and the recipient remembers a
> stranger present at the oath whether the stranger was there or
> not.

### Grave Bat

**Legends epigraph:**

> _The grave bats are the cousins the vampyr houses do not invite
> to the funeral and the wolfshadow packs do not invite to the
> hunt. They roost where the dead are stacked badly and they feed
> on the sick, the screaming, and the sleeping. The plague-criers
> of the Marges say the grave bats are the only honest bell in a
> bad year, because the bell rings only when the dead are still
> dying._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or ALCHEMIST talent, with a HEALING
> roll, gathers one of the following per ⚔️ rolled, player's
> choice: **blood membrane (RARE)**, **grave pollen**, or
> **fang-cord**, from a slain grave bat.
>
> **Blood membrane (RARE):** A square of cured wing-skin. Sewn
> into a hood or cloak by a TANNER over a Quarter Day, it grants a
> D10 Artifact Die to one STEALTH roll made at night or under a
> roof each Quarter Day, and the wearer heals 1 point of lost
> Strength after each fight in which they took at least 1 point
> of damage; one bat yields a single membrane. The membrane reeks
> of crypt and any temple priest within a stretch will refuse the
> wearer sanctuary until the cloak is burned. The Raven Sisters
> will not heal a wearer they recognize.
>
> **Grave pollen:** A handful of dry spore from the underside of
> the wings. Blown into a lantern flame, it grants a D8 Artifact
> Die to one fear attack made within the same fight or one attempt
> to unsettle the dead. The user must succeed on an ENDURANCE roll
> after the casting or take the SICK condition for the next Quarter
> Day.
>
> **Fang-cord:** A length of sinew strung with three small fangs.
> Worn at the throat, it grants a D8 Artifact Die to one INSIGHT
> roll made to detect undead, vampyrs, or wolfshadows within a
> stretch, once per Quarter Day. After three uses the cord
> blackens and any vampyr or wolfshadow within a stretch will mark
> the wearer as kin and refuse to attack until the cord is burned.

### Wereboar

**Legends epigraph:**

> _The wereboars are old farm gods that were never paid off. The
> villages around the Marges still leave salt and apples at certain
> stones in certain months, and they will not say which stones to a
> stranger. The villagers know which children of theirs were sired
> in months when the salt was not left, and they keep an eye on
> those children when the moon is full and the slaughter is bad._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or ALCHEMIST talent, with a HEALING
> roll, gathers one of the following per ⚔️ rolled, player's
> choice: **silver-bound tusk (RARE)**, **tusk marrow**, or **boar
> hide**, from a slain wereboar after sunrise has returned the
> body to human form. Whatever silver chain or rope was used to
> bind the wereboar in life is found beside the body, intact
> regardless of dice rolled.
>
> **Silver-bound tusk (RARE):** A boar's tusk wrapped with silver
> wire by a SMITH over a Quarter Day. Set into a blade hilt or
> spear haft, it grants a D10 Artifact Die to one MELEE attack
> made against any lycanthrope or shapeshifter, and the weapon
> deals normal damage to ordinary-weapon-resistant kin; one
> wereboar yields a single tusk. The wielder dreams of the
> wereboar's last meal each full moon for the rest of their life.
> The Druids will trade a healing tincture for any silver-bound
> tusk; the Howling Path will hunt the wielder.
>
> **Tusk marrow:** Yellow fat from the inside of a tusk. Eaten
> hot, it grants a D8 Artifact Die to one MIGHT or ENDURANCE roll
> in the same Quarter Day. The eater must succeed on a WITS roll
> or take the HUNGRY condition until they next eat raw meat.
>
> **Boar hide:** Heavy bristled skin from the back. Worked by a
> TANNER over a Quarter Day, it yields a leather hauberk (Armor
> Rating 4) and grants a D8 Artifact Die to one ENDURANCE roll
> against any charge attack. The hide reeks of wet boar and
> unsettles village dogs.

### Werewolf

**Legends epigraph:**

> _The Howling Path tells the children of the Aslene clans that the
> first werewolf was a man who could not stop running after his own
> shadow under a moon that would not set. The story does not say
> whether he caught the shadow. The story says he was still running
> at sunrise and that his cousins still see the print of his foot
> in the morning frost in certain valleys. The cousins do not
> follow the print._

**RESOURCES block:**

> **RESOURCES**
>
> An adventurer with the HUNTER or ALCHEMIST talent, with a HEALING
> roll, gathers one of the following per ⚔️ rolled, player's
> choice: **silvered fang (RARE)**, **moon-tuft**, or **wolf
> tooth**, from a slain werewolf after sunrise has returned the
> body to human form. The chain or rope used to bind the werewolf
> in life is found beside the body, intact regardless of dice
> rolled.
>
> **Silvered fang (RARE):** A canine tooth dipped in silver by a
> SMITH over a Quarter Day. Set into a blade hilt, arrow head, or
> ring, it grants a D10 Artifact Die to one MELEE or MARKSMANSHIP
> attack made against any lycanthrope or shapeshifter; one werewolf
> yields D3 fangs. The wielder dreams of the werewolf's last hunt
> each full moon for nine moons. The Howling Path will hunt the
> wielder; the Raven Sisters will trade sanctuary for any silvered
> fang taken from a kin-cousin and returned to the family.
>
> **Moon-tuft:** A small handful of pale fur from the throat or
> shoulders. Burned in a watch-fire, it grants a D8 Artifact Die
> to one SCOUTING or SURVIVAL roll made at night for the watch's
> length. The fire smells of wet wolf and any beast within a
> stretch grows uneasy.
>
> **Wolf tooth:** A small canine, kept dry. Set into a blade hilt
> or strung on a necklace by a TANNER, it grants a D8 Artifact Die
> to one fear attack or one ENDURANCE roll against cold, hunger,
> or panic each Quarter Day. After three uses the tooth crumbles
> and the bearer wakes the next dawn HUNGRY.

---

## 5. Final Merge Notes for the Cheaper AI

When folding this document into `02-bestiary.md`, the merge AI should:

1. **Insert each kept entry** into the main bestiary in alphabetical
   order, after the existing canonical entries and before the
   `## Legends` section.
2. **Use the draft text** from `02A-creatures-of-the-forbidden-lands.md`
   and `02B-monsters-of-the-forbidden-lands.md` for the entry header,
   epigraph, statblock bullets, Monster Attacks D6 table, prose
   paragraph, Lore Roll D6 table, and Random Encounters.
3. **Replace the draft RESOURCES block wholesale** with the uplifted
   RESOURCES block in this document. For 02A creatures that lacked a
   RESOURCES block, add the uplifted block at the end of the entry,
   in canonical position (after the prose, before the next entry).
4. **Skip humanoid bands' RESOURCES** — those entries take their
   GEAR-as-loot line and no RESOURCES block. The humanoid Legends
   epigraphs in section 3 still go into the `## Legends` section.
5. **Append each kept entry's Legends epigraph** to the `## Legends`
   section of `02-bestiary.md` in alphabetical order. Use the
   `### Name` + blockquote format already established in canon.
6. **Drop all NOT TO INCLUDE entries** without comment. Do not preserve
   them in the merged file.
7. **Update the D66 monster table** at the head of the canonical
   bestiary to include the new entries. The kept count is 17 (02B) +
   18 (02A creatures) + 9 (02A humanoid bands) = 44 new entries; the
   table will need to be expanded to a D666 or split into a creatures
   table and a monsters table at the merge AI's discretion. Suggested
   split: monsters (full canonical entries) keep the D66 table and
   are renumbered alphabetically; creatures (lesser foes and humanoid
   bands) take a separate D66 lesser-foes table appended below.
8. **Run markdownlint** on the merged file. The drafts and this
   document are lint-clean; merge errors are most likely to come from
   table-row alignment after renumbering.

End of audit and merge instruction set.
