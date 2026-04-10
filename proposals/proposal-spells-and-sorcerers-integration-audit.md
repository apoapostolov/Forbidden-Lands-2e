<!-- markdownlint-disable MD013 -->

# Proposal — Spells & Sorcerers Integration Audit

## Summary

This proposal audits the third-party supplement _Spells & Sorcerers_ (v1.01) against the integrated corebook Chapter 7 magic system and recommends which rules, subsystems, and spells to adopt as core rules.

The operating principle: add what fills genuine gaps. Reject what replaces things that already work. Every adoption must layer onto the existing system without rewriting it.

The corebook currently has 16 disciplines and approximately 300 spells. _Spells & Sorcerers_ has 17 disciplines and approximately 300 spells. Roughly 12% of S&S spells share names with corebook spells. The remaining 88% are novel content — but not all of it is compatible.

## Audit Scope

**Corebook Chapter 7** — 16 disciplines: General Spells, Healing, Shapeshifting, Awareness, Symbolism, Stone Song, Blood Magic, Death Magic, Elemental Magic, Ice Affinity, Nature, Swarm Magic, Magma Song, Mentalism, Oneiromancy, Magnetism.

**S&S Supplement** — 17 disciplines: General Spells, Healing, Wild Magic (new), Awareness, Symbolism, Stone Song, Magma Song, Blood Magic, Necromancy (renamed Death Magic), Demonic Magic (new), Fire Magic (new), Wind Magic (new), Water Magic (new), Ice Affinity, Mentalism, Oneiromancy, Magnetism.

**S&S Subsystems** — Rarity/Secretism classification, ingredient resource dice, sacrifice rule, individual spell learning, talent cap removal, discipline-specific casting mechanics (Fire intensity, Blood rot, Demonic mog, Oneiromancy sleep-casting, Mentalism influence, Symbolism drawn/air symbols, Stone Song reusable instruments).

---

## Part I — Subsystem Audit

### 1. Rarity and Secretism

**What it does.** S&S classifies each discipline on two axes: Rarity (Known / Strange / Disturbing / Prohibited) describing how the general population perceives the discipline, and Secretism (Initiation / Demonstration / Journey) describing how hard it is to find a willing teacher.

**Assessment: ADOPT as GM guidance.** This is a narrative framework, not a mechanical replacement. It does not change any XP cost, die roll, or casting rule. It gives GMs a structured way to answer "how hard is it to find a teacher for this?" and "how do townsfolk react when they see this magic?" — questions the corebook leaves to improvisation.

**Integration.** Add a two-column table to the introductory section of Chapter 7 listing each discipline's rarity and secretism tier. No mechanical weight. GMs use it as a reaction guide and campaign-planning tool.

| Discipline      | Rarity     | Secretism     |
| --------------- | ---------- | ------------- |
| General Spells  | —          | —             |
| Healing         | Known      | Initiation    |
| Shapeshifting   | Strange    | Demonstration |
| Awareness       | Strange    | Initiation    |
| Symbolism       | Disturbing | Demonstration |
| Stone Song      | Strange    | Demonstration |
| Blood Magic     | Prohibited | Journey       |
| Death Magic     | Prohibited | Journey       |
| Elemental Magic | Disturbing | Journey       |
| Ice Affinity    | Strange    | Initiation    |
| Nature          | Known      | Initiation    |
| Swarm Magic     | Disturbing | Demonstration |
| Magma Song      | Disturbing | Journey       |
| Mentalism       | Strange    | Demonstration |
| Oneiromancy     | Disturbing | Journey       |
| Magnetism       | Disturbing | Journey       |
| Demonic Magic   | Prohibited | Journey       |

---

### 2. Ingredient Resource Dice

**What it does.** S&S replaces the corebook's one-use ingredient model with a resource die that degrades on a 1–2 roll. Ingredients become durability-tracked resources instead of single-use consumables. A separate economic layer lets players upgrade die sizes for 3 silver per step.

**Assessment: REJECT.** The corebook's one-use model is clean and punishing in exactly the way the Forbidden Lands economy demands. Resource dice are elegant for things players carry in bulk (food, water, arrows, torches) where counting individual units is tedious. Spell ingredients are not that kind of resource. A druid carries mistletoe, a bone, a candle — discrete objects with narrative weight. Converting them to abstract die pools removes that physicality and contradicts the corebook's established "ingredient is spent" language across all 300+ spells. Adopting this would require rewriting every spell entry in Chapter 7.

---

### 3. Sacrifice Rule

**What it does.** A caster may voluntarily take attribute damage to gain temporary Willpower Points usable only for the spell being cast. Maximum WP gained equals the caster's rank in that discipline. The WP cannot be saved or transferred.

**Assessment: ADOPT with modification.** This is the best single subsystem in S&S. It creates desperate casting moments that fit the Forbidden Lands tone perfectly — a wounded sorcerer cutting into their own reserves to hurl one last spell. The rank cap prevents abuse. The one-spell restriction prevents stockpiling.

**Modification.** The S&S version lets the player choose which attribute takes the damage. That is a gift to optimizers — every player will find their cheapest attribute and sacrifice it forever. The fix is to remove the choice: the attribute is determined randomly at the moment of sacrifice by rolling a D8.

| D8  | Attribute Damaged |
| --- | ----------------- |
| 1–2 | Strength          |
| 3–4 | Agility           |
| 5–6 | Wits              |
| 7–8 | Empathy           |

Two faces per attribute means equal probability across all four. The caster decides _how much_ to sacrifice (up to their discipline rank), but not _where_ it lands. This preserves the dramatic desperation of the mechanic while making every sacrifice genuinely frightening — you might burn the stat you can least afford to lose.

**Integration.** Add a sidebar or short subsection to the casting rules in Chapter 7.

> **SACRIFICE:** When you cast a spell, you may sacrifice vitality to gain temporary Willpower Points for that spell alone. Declare how many points you sacrifice (maximum equal to your rank in the spell's discipline). For each point, roll a D8 and apply 1 point of damage to the indicated attribute (1–2 Strength, 3–4 Agility, 5–6 Wits, 7–8 Empathy). These WP vanish if not used on the triggering spell.

---

### 4. Individual Spell Learning

**What it does.** S&S introduces per-spell learning: when you gain a talent rank, you receive 2 free spells of that rank. Additional spells require finding the spell (teacher, grimoire, or self-study at 1 week per rank), passing an Intellect check, and paying XP equal to the spell's rank (or triple without a teacher). S&S also makes a teacher mandatory for talent rank 1 — the corebook's triple-XP solo option is removed.

**Assessment: PARTIALLY ADOPT.** The per-spell learning model adds meaningful choice ("which spells do I actually know?") without adding heavy bookkeeping. The Intellect check for self-study is elegant and uses an otherwise underused attribute check. But the mandatory-teacher-at-rank-1 rule contradicts the corebook's established triple-XP solo path, which exists specifically for campaigns where teachers are scarce — a core Forbidden Lands scenario.

**What to adopt:**

- **Free spells on rank gain:** When you increase a magical talent, you learn 2 spells of that rank or lower for free. This is a clean default that was previously undefined.
- **Individual spell learning:** Additional spells beyond the free allocation cost XP equal to the spell's rank. Without a teacher or grimoire, cost is tripled and requires 1 week of study per rank.
- **Grimoire as teaching tool:** A grimoire containing a spell counts as a teacher for learning that specific spell.

**What to reject:**

- **Mandatory teacher at rank 1.** The corebook's triple-XP solo path stays. In the Forbidden Lands, teachers can be dead, imprisoned, or hostile. Blocking solo learning at rank 1 punishes exactly the kind of desperate self-taught magic the setting encourages.
- **Intellect check requirement.** Adding a potential failure roll to XP expenditure creates feel-bad moments. You already paid the XP and the time. The check adds nothing the cost doesn't already handle.

---

### 5. Talent Cap Removal

**What it does.** S&S states that talent ranks should not be restricted to 3, allowing ranks 4–6.

**Assessment: ALREADY HANDLED.** The corebook already contains rank 4, 5, and 6 spells in every discipline. The talent cap is implicitly beyond 3. If anything, the corebook should add a brief clarifying note that magical talents can be raised above rank 3 (since the general talent rules cap at 3). This is a one-sentence errata, not a subsystem adoption.

---

### 6. Expanded Talent Access (Races and Professions)

**What it does.** S&S opens magical talent access to non-Druid/Sorcerer characters: Elves and Wolfkin can learn Wild Magic, Half-Elves can learn Awareness, Dwarves can learn Stone Song and Magma Song, Minstrels and Peddlers can learn Mentalism, Warriors and Riders can learn Magnetism.

**Assessment: ADOPT selectively.** The race-based access is well-reasoned and lore-consistent. Dwarves learning Stone Song is canonical. Elves having an affinity for nature magic is setting-appropriate. Warriors learning Magnetism (iron-singing) fits the discipline's martial flavor. Minstrels learning Mentalism matches their social manipulation role.

**What to adopt:**

| Discipline | Additional Access      | Rationale                                      |
| ---------- | ---------------------- | ---------------------------------------------- |
| Stone Song | Dwarves (any class)    | Canonical dwarven magic                        |
| Magma Song | Dwarves (any class)    | Extension of Stone Song tradition              |
| Awareness  | Half-Elves (any class) | Elven bloodline as sensory gift                |
| Mentalism  | Minstrels              | Social manipulation through magical persuasion |
| Magnetism  | Warriors, Riders       | Iron-singing as martial discipline             |

**What to reject:**

| Discipline | Access         | Reason for Rejection                                          |
| ---------- | -------------- | ------------------------------------------------------------- |
| Wild Magic | Elves, Wolfkin | Wild Magic is not adopted as a discipline (see Part II below) |
| Healing    | Druids only    | Already correct — Healing rites require druidic initiation    |

---

### 7. Discipline-Specific Casting Mechanics

These are assessed individually because each is tied to a specific discipline adoption decision.

#### A. Elemental Environment Bonus (Elemental Magic)

**Origin.** S&S introduced an intensity mechanic for its standalone Fire Magic discipline: ambient fire grants bonus dice. We are not adopting separate elemental disciplines, but the principle extends cleanly to all four elements in the corebook's Elemental Magic path.

**Assessment: ADOPT, expanded to all four elements.** The S&S version only covers fire and uses bonus dice that add mishap risk. The corebook model is cleaner: a flat Power Level bonus, no extra dice, no extra mishap exposure. The bonus does not apply to effects created by the spell itself — you cannot stand in your own Fireball to fuel a second one.

**Core principle.** Presence is not enough. The element must be acting on the caster. Each element has its own form of exposure — what it means for the caster to have surrendered some authority over their body to the element. The tiers reflect how deep that surrender goes.

The GM makes the final call on which tier applies. When in doubt, round down.

---

**FIRE — the caster must be at risk of burning**

A torch in hand or a campfire at a safe distance provides nothing. The fire must be large enough and close enough that catching alight is a genuine possibility — not hypothetical, but one stumble or wind-shift away.

| Tier | Requirement                                                                                                           | Power Level |
| ---- | --------------------------------------------------------------------------------------------------------------------- | ----------- |
| —    | Open flame of any kind at safe distance (torches, campfires, hearths)                                                 | No bonus    |
| +1   | Standing at arm's reach of a large fire; heat is painful; embers drift close; the skin tightens                       | +1 PL       |
| +2   | Inside a burning room; smoke obscures vision; staying requires a MOVE roll each round to avoid catching fire          | +2 PL       |
| +3   | A building or forest burns around the caster; catching fire is likely without active effort; survival is the question | +3 PL       |

---

**WATER — the caster must be submerged**

Rain, even heavy rain, does not qualify. Standing at the water's edge does not qualify. The element must have weight on the body and resistance against movement. Full submersion in violent water is not just a power source — it is a surrender of control to the element.

| Tier | Requirement                                                                                                                              | Power Level |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| —    | Any contact short of submersion (splashing, rain, waterskin poured over a hand)                                                          | No bonus    |
| +1   | Knee-deep in water — river, lake, sea, or flood; water pushes against the legs                                                           | +1 PL       |
| +2   | Waist-deep or deeper; chest-deep, swimming; the current, tide, or mass of water affects movement and balance                             | +2 PL       |
| +3   | Fully submerged for at least one round in strong current or stormy sea; the caster is underwater, unable to breathe, pulled by the water | +3 PL       |

---

**WIND — the caster must be airborne or in a gale; lightning required for the highest tier**

Indoors means nothing. Open air on a calm day means nothing. The wind must be working against the caster — pushing, redirecting, threatening footing or altitude. Air is the most accessible element and the most forgiving to channel, so its ceiling under natural conditions is +2. The third tier belongs to lightning: the sky turning on the caster, the element expressing itself as raw electrical violence rather than movement.

| Tier | Requirement                                                                                                                                                       | Power Level |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| —    | Any wind that does not threaten footing or direction (light breeze, open window, moving at speed)                                                                 | No bonus    |
| +1   | Exposed to sustained strong wind — cliff edge, mountain pass, open sea deck, hilltop in a squall; clothing snaps and tears, footing is uncertain                  | +1 PL       |
| +2   | Airborne by any means (Flight spell, great bird, jump from height) in strong wind; the wind affects trajectory and speed                                          | +2 PL       |
| +3   | Active lightning storm with strikes in the immediate area; the caster has been struck by lightning this scene, or is the highest point exposed to ongoing strikes | +3 PL       |

---

**EARTH — the caster must be enclosed by stone, or in the presence of the living rock**

Earth is everywhere underfoot, which makes proximity meaningless. The bonus does not come from touching soil or standing on rock. It comes from being _inside_ the earth — enclosed by it, with unbroken stone on all sides — or from the presence of lava, which is earth in its most primal state: the deep rock of the world turned liquid, carrying the full pressure of everything below.

A quarry does not qualify: the stone is broken open, sky is present, the element has been undone. A cellar or dungeon does not qualify: the stone is worked, the depth is shallow. But a volcanic passage with a flowing lava channel makes the walls themselves speak — even if the caster is standing in open air, the lava is the earth's own voice.

| Tier | Requirement                                                                                                                                                           | Power Level |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| —    | Any surface context — open ground, shallow cave with sky visible, worked stone floor, quarry, cellar, ruins                                                           | No bonus    |
| +1   | Inside a cave or tunnel where unworked rock walls press in from at least two sides and the ceiling is stone; no sky visible                                           | +1 PL       |
| +2   | Deep underground — a significant mine shaft, a natural cavern, a burial mound cut into bedrock; rock overhead in mass; the weight of the earth is felt                | +2 PL       |
| +3   | Lava is present and flowing — a volcanic tunnel, a magma chamber, a lava tube with an active channel; the rock is not dead stone but living, molten, and moving earth | +3 PL       |

---

**Notes:**

- Multi-element spells (Elemental Shield, Elemental Wall, Elemental Bolts, Elemental Ward, Control Element) use the bonus from whichever element the caster chose for that casting. Bonuses from multiple elements cannot stack.
- Elemental Infusion already grants WP based on Power Level — the environmental bonus applies before that calculation, making storm-casting or deep-earth rituals extremely powerful for high-rank specialists.
- A caster who engineers their environment deliberately — building a bonfire ring before a fight, choosing to engage enemies underground, wading into a river before casting Flood Wave — is playing the discipline correctly. This is intended.

#### B. Blood Rot (Blood Magic)

**What it does.** Blood used as an ingredient decays after 2 quarter days. Dead-creature blood cannot serve as an ingredient.

**Assessment: ADOPT.** This is a clean, flavorful constraint that makes Blood Magic feel more desperate and time-pressured. Two quarter days means blood drawn at dawn is useless by nightfall. The dead-blood restriction prevents battlefield harvesting from corpses. Both constraints reinforce the discipline's living-sacrifice theme.

**Integration.** Add one sentence to the Blood Magic discipline introduction:

> Blood used as a spell ingredient must be fresh — drawn from a living creature within the last two quarter days. Blood from the dead is useless.

#### C. Demonic Mog (Demonic Magic)

**Assessment: ADOPT if Demonic Magic is adopted** (see Part II). The mog substance is integral to the discipline's identity. It cannot exist without it.

#### D. Oneiromancy Sleep-Casting

**What it does.** All Oneiromancy spells must be cast while asleep. The caster must plan spells, targets, and WP allocation before sleeping.

**Assessment: REJECT.** The corebook's Oneiromancy discipline already has 23 spells that work with standard casting rules. Retroactively requiring sleep-casting for all of them would break existing characters. The S&S sleep-casting mechanic is interesting as a flavor option but not as a mandatory restriction. If specific S&S Oneiromancy spells are adopted, they can individually note "cast while sleeping" where appropriate.

#### E. Mentalism Influence

**What it does.** Mentalism spells use no ingredients. Instead, speaking with the target and using manipulative tone/gesture grants +1 Power Level (equivalent to the ingredient bonus).

**Assessment: ADOPT.** This is the cleanest discipline-specific mechanic in S&S. Mentalism already feels wrong with physical ingredients — a mind-controller crushing a beetle to boost their spell breaks the flavor. Replacing the ingredient bonus with a spoken-word requirement ("you must be able to speak to the target") is elegant and fits the social manipulation theme.

**Integration.** Add to the Mentalism discipline introduction:

> Mentalism spells require no physical ingredients. Instead, to gain the +1 Power Level that ingredients normally provide, you must speak directly to your target — your words, tone, and gestures channel the magical intent. The subject of conversation does not matter; what matters is the directed attention.

#### F. Symbolism Drawn vs Air-Drawn

**What it does.** S&S distinguishes between air-drawn symbols (invisible hand gestures, slow action, no ingredient cost, immediate) and surface-drawn symbols (visible on a surface, counts as ingredient, takes 1 minute per spell rank to inscribe, can persist as traps/wards).

**Assessment: ADOPT the drawn-symbol option only.** The corebook's Symbolism already works with standard casting. The air-drawn mode is just standard casting restated. But the drawn-symbol option — inscribing a visible symbol on a surface that persists until triggered — fills a genuine gap. It gives Symbolism users the ability to create wards, traps, and lasting marks. This is what Symbolism _should_ do and currently doesn't.

**Integration.** Add a short subsection to the Symbolism discipline:

> **INSCRIBED SYMBOLS:** Instead of casting a symbol spell immediately, you may inscribe it onto a surface. This takes one minute per spell rank and requires ink or a sharp tool. The inscribed symbol holds its power until triggered by a condition you set when inscribing (a creature crossing a threshold, a hand touching the mark, a spoken word). The spell resolves with the Power Level achieved when you inscribed it. An inscribed symbol is visible to anyone who looks, but its magical nature can only be detected with Perceive Magic or similar effects.

#### G. Stone Song Reusable Instruments

**What it does.** Stone Song ingredients are musical instruments (horn, drum, lute, harmonica) that are not consumed — they can be used indefinitely. The caster must play the instrument while casting.

**Assessment: ALREADY COMPATIBLE.** The corebook's Stone Song section already describes musical/vocal casting. The non-consumable nature of instruments is implicit (you don't destroy a horn by blowing it). No rules change needed. If desired, add a clarifying sentence:

> Stone Song instruments are not consumed by casting. The same horn or drum can channel a thousand spells.

---

## Part II — New Discipline Audit

### 1. Demonic Magic — ADOPT

**Gap filled:** The corebook has no demon-interaction discipline. Demons exist in the setting (Churmog, demonic corruption, misgrown). Druids can fight demons with Healing (Bend Demon). But no one can summon, bind, bargain with, or manipulate them. This is a genuine gap.

**S&S version (20 spells, ranks 1–6).** Centers on the substance "mog" — a corrosive lilac-green liquid that flows from the demon dimension Churmog. The discipline uses mog to alter bodies, bind demons, open portals, and corrupt living matter.

**Why it works:** Demonic Magic is self-contained. It introduces its own resource (mog), its own risk model (mog corrodes flesh, demons resist binding), and its own flavor (body horror, corruption, forbidden knowledge). It does not overlap with any existing discipline. It does not replace Death Magic, which deals with undead and the spirit world. Demonic Magic deals with a completely different axis of the supernatural — the living corruption that comes from outside the world rather than the death that comes from within it.

**What to adopt:**

- The mog substance and its properties (corrosive, flesh-bonding, demon-sourced)
- The entire spell progression from Generate Mog (rank 1) through the summoning and binding spells
- The D66 Demonic Magic mishap table
- Body alteration mechanics (grafting demon-flesh, growing extra limbs) as high-rank effects

**Integration notes:**

- Demonic Magic is a Sorcery discipline. Only Sorcerers can learn it.
- Rarity: Prohibited. Secretism: Journey. This is the most dangerous and reviled magic in the Forbidden Lands.
- The discipline needs its own mishap table. The S&S table is usable with minor editing for voice.
- Mog tracking: use the existing inventory system. Mog is carried in sealed containers. Units are discrete, not resource-die abstracted.

---

### 2. Fire Magic, Wind Magic, Water Magic — REJECT as separate disciplines

**Why.** The corebook already has Elemental Magic — a unified discipline covering fire, earth, wind, and water with 22 spells. Splitting this into four separate disciplines (Fire, Wind, Water, plus the existing earth-biased Stone Song) would:

- Force existing Elemental Magic users to choose a single element, losing the discipline's signature versatility
- Create five separate talent investments where one currently exists
- Fragment the spell list in ways that make each element's progression thin at high ranks
- Contradict the corebook's established lore: "Elemental magic is the art of manipulating the very building blocks of existence: earth, wind, water, and fire"

The S&S element-split model treats each element as a specialist path with 20+ spells. That is a valid design, but it is incompatible with the corebook's unified approach. The corebook's Elemental Magic already covers the key spells for each element: Combustion, Fireball, Tornado, Flood Wave, Elemental Shield (per-element variants), Elemental Wall (per-element variants), Summon Elemental (per-element variants), and the capstone Control Element.

**What to salvage.** Some S&S element-specific spells fill genuine gaps in the corebook's Elemental Magic list. These should be adopted as new Elemental Magic spells, not as separate disciplines:

| S&S Spell         | Element | Rank | Effect                                      | Gap Filled                                     |
| ----------------- | ------- | ---- | ------------------------------------------- | ---------------------------------------------- |
| Aquatic Breathing | Water   | 1    | Breathe underwater for 1 turn per PL        | Corebook has Water Breathing — DUPLICATE, skip |
| Fog / Dense Fog   | Water   | 2    | Create obscuring fog in a zone              | No vision-blocking water spell in corebook     |
| Pressure Jet      | Water   | 3    | Concentrated water blast, Weapon Damage 2   | No single-target water attack in corebook      |
| Deviation         | Wind    | 1    | Deflect one ranged attack per PL            | No reactive wind defense in corebook           |
| Impulse           | Wind    | 2    | Boost movement rate by 1 for 1 round per PL | No wind-movement buff in corebook              |
| Wall of Flame     | Fire    | 3    | Line of fire, damage to anyone crossing     | Corebook has Elemental Wall (Fire) — DUPLICATE |
| Asphyxiate        | Wind    | 3    | Area suffocation, 1 damage/round per PL     | Corebook has Suffocate — may overlap           |
| Fire Resistance   | Fire    | 2    | Reduce fire damage by PL for 1 turn         | No fire-specific defense in corebook           |

**Recommended additions to Elemental Magic:**

- **Deviation** (rank 1, Wind ingredient): As a fast action, deflect one incoming ranged attack. Each additional Power Level deflects one more attack. — _Fills the reactive wind-defense gap._
- **Dense Fog** (rank 2, Water ingredient): Fill one zone with impenetrable fog. All ranged attacks through or into the zone are impossible. Melee attacks suffer –2. Lasts one round per Power Level. — _Fills the vision-blocking gap._
- **Impulse** (rank 2, Wind ingredient): Boost your or one ally's Movement Rate by 1 for one round per Power Level. — _Fills the wind-mobility gap._
- **Fire Resistance** (rank 2, Fire ingredient): Reduce all fire damage taken by an amount equal to the Power Level for one turn. — _Fills the fire-defense gap._
- **Pressure Jet** (rank 3, Water ingredient): A concentrated stream of water strikes one target for damage equal to the Power Level. Armor applies. The target must make a MIGHT roll or be knocked prone. — _Fills the single-target water attack gap._

---

### 3. Wild Magic — REJECT as separate discipline

**Why.** The corebook already has Shapeshifting (23 spells, ranks 1–6) covering animal and humanoid transformation, and Nature (19 spells, ranks 1–6) covering plant/forest/weather magic. Wild Magic's spell list overlaps heavily with both. Its core theme — animal communion, beast control, wolf/bear/eagle forms — is already covered by Shapeshifting's animal transformation spells and Nature's Call of the Wild / Animal Whisperer effects.

**What to salvage.** Two S&S Wild Magic spells fill genuine gaps:

- **Inhabit Animal** (rank 3): Project your consciousness into a nearby animal, controlling its body while yours lies dormant. — _The corebook's Shapeshifting transforms your body. This spell leaves your body behind and possesses an existing animal. Different mechanic, different risk profile, different story potential._
- **Monster Form** (rank 5): Transform into a monster creature with full monster stats for a limited duration. — _The corebook's Shapeshifting covers animals and humanoids but not monsters. This is a high-risk, high-rank expansion that fits._

**Recommended additions to Shapeshifting:**

- **Inhabit Animal** (rank 3): Your mind enters a willing or unresisting animal within Near range. You control the animal's body and perceive through its senses. Your own body lies unconscious and defenseless. If the animal is killed, you wake with 1 point of damage to Wits. Lasts one turn per Power Level. Ingredient: A piece of the target animal (feather, hair, scale).
- **Monster Form** (rank 5): You transform into a monster of your choice. Use the monster's attributes, armor, and natural attacks. You retain your own Wits and Empathy. You cannot cast spells while transformed. If brought to Broken, you revert to your natural form. Lasts one round per Power Level. Ingredient: A piece of the target monster. — _The GM determines which monsters are eligible. Demons, undead, and unique creatures are excluded._

---

### 4. Necromancy — EVALUATE for name and spell differences

**What it does.** S&S renames Death Magic to "Necromancy" and provides a spell list that is approximately 85% different from the corebook's Death Magic list.

**Assessment: DO NOT RENAME.** "Death Magic" is the established corebook term. Renaming creates confusion for no mechanical benefit. However, several S&S Necromancy spells fill genuine gaps in the corebook's Death Magic discipline.

**Recommended additions to Death Magic:**

- **Talk to Corpses** (rank 1): Speak with a dead body and ask it questions. The corpse answers truthfully but only knows what it knew in life. Each Power Level grants one question. The corpse does not need to be fresh, but older corpses give shorter, vaguer answers. Ingredient: A candle. — _Fills the "communication with the dead" gap. The corebook's Séance (rank 2) contacts spirits in the realm of the dead, but there is no spell for questioning a physical corpse._
- **Corpse Servant** (rank 2): Animate a dead body as a mindless servant. The corpse follows simple commands (carry, dig, guard, attack). Strength equal to Power Level, Agility 1. Lasts one quarter day per Power Level. Ingredient: A bone. — _The corebook has Raise Undead at rank 3 for combat-capable undead. This lower-rank version creates weak, temporary servants for labor and simple tasks — a useful stepping stone._

---

## Part III — Shared Discipline Spell Audit

For each shared discipline, this section identifies S&S spells worth adopting into the corebook. Only spells that fill genuine mechanical gaps are listed. Renamed duplicates, weaker versions of existing spells, and spells that conflict with established corebook spells are excluded.

### General Spells

The corebook has 22 general spells. S&S has 17, with essentially zero overlap (different spell names, different mechanical concepts). The S&S general spells focus heavily on meta-magic: boosting, containing, nullifying, and transferring spell energy.

**Recommended adoptions:**

- **Empower Spell** (rank 1, Power Word): As a fast action, increase the Power Level of another caster's spell by 1. Your Empower Spell's Power Level must match or exceed the target spell's current Power Level. Usable reactively, breaking initiative order. Ingredient: Candle. — _Fills the "cooperative casting" gap. No corebook general spell lets one caster boost another's spell._

- **Contain Spell** (rank 3): Cast alongside another spell. The second spell is stored in an object and released later as a fast action. Lasts one quarter day per Power Level. Both spells can cause mishaps. Ingredient: Aquamarine. — _Fills the "spell trap / delayed casting" gap. The corebook's Bind Spell stores a spell in an item permanently; this is a temporary, tactical version._

- **Weaken Spell** (rank 3, Power Word): As a fast action, reduce the Power Level of a spell being cast in your presence by an amount equal to your Power Level. If reduced to 0 or below, the spell is nullified. Reactive, breaks initiative order. Ingredient: Iron ore. — _Fills the "counterspell" gap. The corebook has Dispel but it targets already-active spells. Weaken Spell targets spells at the moment of casting — a genuine tactical difference._

- **Transfer Energy** (rank 4): Transfer Willpower Points from your pool to another character (equal to Power Level), or steal WP from an unwilling target (equal to Power Level –1, resisted by target's WP pool). Ingredient: Bloody fabric. — _Fills the "WP economy manipulation" gap. No corebook spell allows WP transfer or theft._

- **Anti-Magic Zone** (rank 6, Ritual): For one day, all spells cast within the area reduce their Power Level by an amount equal to the ritual's Power Level. Affects all casters including yourself. Range: Long. Ingredient: Aquamarine. — _Fills the "area denial for magic" gap. The corebook has no zone-wide magic suppression effect._

### Healing

The corebook has 25 Healing spells — the most complete discipline. S&S adds 18 with approximately 5 shared.

**Recommended adoptions:**

- **Relieve Condition** (rank 1): Remove the effects of conditions (Hungry, Thirsty, Cold, Sleepy) from a target for one quarter day per Power Level. The conditions are still present but cause no damage or penalties for the duration. Cannot be used on yourself. Ingredient: Incense. — _Fills the "condition management" gap. The corebook's Healing spells cure damage and injuries but never address conditions directly._

- **Bend Demon** (rank 3): Deal damage to a demon's Wits equal to Power Level. If Broken, the demon is banished to its home dimension. Works on misgrown at half power. Ingredient: Sacred symbol. — _Note: the corebook already has Exorcise (rank 3) in Healing which deals with possession. Bend Demon is different — it is an offensive anti-demon attack, not a possession cure. Worth adopting as a distinct spell if Demonic Magic is also adopted, to give Healers a counter._

### Awareness

The corebook has 22 Awareness spells. S&S has 18 with approximately 3 shared.

**Recommended adoptions:**

- **Predict Moves** (rank 2): For one round per Power Level, you can predict one enemy's next action. The GM tells you the target's intended action before you choose yours. Ingredient: Animal bone. — _Fills the "tactical precognition" gap. No corebook Awareness spell grants combat-relevant foresight of a specific enemy's intent._

- **Transfer Senses** (rank 1): For one turn per Power Level, you can perceive through the senses of an animal you can touch. During this time your own senses are suppressed. Ingredient: A piece of the animal. — _Fills the "remote scouting through familiar" gap. Distinct from the corebook's Sixth Sense (which sharpens your own senses) and True Sight (which sees through illusions)._

### Symbolism

The corebook has 22 Symbolism spells. S&S has 23 with approximately 3 shared.

**Recommended adoptions:**

- **Warning** (rank 1): Inscribe a symbol that alerts you when a creature crosses a boundary you define. Range: Short. Duration: One quarter day per Power Level. Ingredient: Ink. — _Fills the "magical alarm" gap. No corebook spell provides passive boundary monitoring._

- **Animate Object** (rank 4): Bring an inanimate object to life. It obeys your verbal commands. Strength and Agility depend on the object's size (GM discretion). Lasts one turn per Power Level. Ingredient: A piece of the object's material. — _Fills the "object animation" gap. The corebook's Symbolism deals in marks, wards, and effects on creatures — not bringing objects to independent motion._

### Stone Song

The corebook has 23 Stone Song spells. S&S has 22 with only 1 shared.

**Note:** The corebook's Stone Song is already comprehensive, including the prospecting and mining spells integrated into Chapter 9. The S&S Stone Song list diverges heavily because S&S was written against the original Forbidden Lands rules, not our expanded corebook.

**Recommended adoptions:** None. The corebook's Stone Song is already the most complete version. The S&S spells that are novel tend to duplicate functionality already covered by our Magma Song or Magnetism disciplines.

### Blood Magic

The corebook has 23 Blood Magic spells. S&S has 21 with only 1 shared.

**Recommended adoptions:**

- **Blood Rot** mechanic (see subsystem section above — already recommended for adoption).

- **Create Bloodling** (rank 5): Create a small sentient creature from a pool of blood. The bloodling has Strength 1, Agility 3, and follows your commands. It can spy, deliver small objects, and squeeze through cracks. Lasts one quarter day per Power Level, or until destroyed. Ingredient: Blood. — _Fills the "blood-servant / familiar creation" gap. No corebook Blood Magic spell creates an independent entity._

### Death Magic

The corebook has 23 Death Magic spells. S&S has 20 as "Necromancy" with approximately 3 shared.

**Recommended adoptions:** Talk to Corpses and Corpse Servant (see Part II above).

### Ice Affinity

The corebook has 14 Ice Affinity spells — the smallest discipline. S&S has 22. This is the single largest gap between the two books.

**Recommended adoptions:**

- **Frost Armor** (rank 2): Coat yourself or a willing target in a shell of magical ice. Armor Rating equal to Power Level. Lasts one round per Power Level. Anyone striking the wearer in melee takes 1 cold damage. Ingredient: Ice or snow. — _Fills the "ice-based defense" gap. The corebook has offensive ice spells and Blizzard for area denial, but no ice armor._

- **Ice Prison** (rank 3): Encase a target in ice. The target is immobilized and cannot act. Breaking free requires a MIGHT roll with a penalty equal to the Power Level. Lasts until broken free or one turn per Power Level. Ingredient: Ice or snow. — _Fills the "single-target lockdown" gap. The corebook's Blizzard and Hail affect areas. This targets one creature._

- **Glacial Path** (rank 2): Create a path of ice across water, mud, or unstable terrain. The path is 2 meters wide and extends up to Near range per Power Level. Lasts one turn per Power Level. Ingredient: Ice or snow. — _Fills the "terrain creation" gap. The corebook's Ice Affinity spells damage and debuff but never create traversable terrain._

- **Shatter** (rank 4): Cause a frozen or ice-encased object or creature to shatter. Deals damage equal to twice the Power Level. Only works on targets already affected by cold or ice (frozen condition, ice prison, or natural ice). Ingredient: Ice or snow. — _Fills the "execute combo" gap — a payoff spell that rewards setting up cold conditions first._

### Magma Song

The corebook has 23 Magma Song spells. S&S has 21 with only 1 shared.

**Recommended adoptions:** None. The corebook's Magma Song is already comprehensive. The S&S version diverges heavily and fills no gaps not already covered.

### Mentalism

The corebook has 23 Mentalism spells. S&S has 21 with approximately 2 shared.

**Recommended adoptions:**

- **Influence mechanic** (see subsystem section above — already recommended for adoption).

- **Implant Memory** (rank 3): Plant a false memory in the target's mind. The memory must be plausible. The target believes it is real unless given strong evidence to the contrary. Resisted by the target's INSIGHT. Lasts until dispelled or the target succeeds an INSIGHT roll prompted by contradictory evidence. Ingredient: None (Influence). — _Fills the "memory manipulation" gap. The corebook has Thought Control (commands actions) and Fear (emotional manipulation), but nothing that alters what the target remembers._

- **Mind Shield** (rank 2): Grant yourself or a willing target resistance to Mentalism and other mind-affecting spells. The shield absorbs Power Level points of incoming mental spell Power Level before the spell takes effect. Lasts one turn per Power Level. Ingredient: None (Influence). — _Fills the "mental defense" gap. The corebook has no Mentalism spell that defends against other Mentalism spells. Currently there is no counterplay within the discipline._

### Oneiromancy

The corebook has 23 Oneiromancy spells. S&S has 16.

**Recommended adoptions:** None. The corebook's Oneiromancy is already the more complete version. The S&S spells that don't appear in the corebook are mostly reworkings of existing concepts or rely on the sleep-casting mechanic that we are not adopting.

### Magnetism

The corebook has 23 Magnetism spells. S&S has 21 with approximately 4 shared.

**Recommended adoptions:**

- **Magnetic Shield** (rank 2): Create a magnetic field around yourself that deflects metal weapons and projectiles. Grants Armor Rating equal to Power Level against metal weapons only. Lasts one round per Power Level. Ingredient: Iron ore. — _Fills the "metal-specific defense" gap. The corebook's Magnetism has offensive and utility spells but no defensive field._

---

## Part IV — Integration Summary

### Subsystems to Adopt

| Subsystem                                    | Type     | Effort  |
| -------------------------------------------- | -------- | ------- |
| Rarity / Secretism table                     | Additive | Low     |
| Sacrifice rule                               | Additive | Low     |
| Free spells on rank gain (2)                 | Additive | Low     |
| Individual spell learning                    | Additive | Low     |
| Expanded talent access                       | Additive | Low     |
| Blood rot (2 QD decay)                       | Additive | Minimal |
| Mentalism influence mechanic                 | Additive | Low     |
| Inscribed Symbols                            | Additive | Low     |
| Elemental environment bonus (all 4 elements) | Additive | Low     |
| Stone Song instrument note                   | Additive | Minimal |

### Subsystems to Reject

| Subsystem                    | Reason                                              |
| ---------------------------- | --------------------------------------------------- |
| Ingredient resource dice     | Replaces core model; contradicts 300+ spell entries |
| Mandatory teacher at rank 1  | Contradicts triple-XP solo path; punishes scarcity  |
| Intellect check for learning | Feel-bad on XP expenditure; cost is sufficient gate |
| Oneiromancy sleep-casting    | Breaks existing 23 corebook spells retroactively    |
| Talent cap (explicit note)   | Already implicit in corebook (rank 6 spells exist)  |

### New Discipline to Adopt

| Discipline    | Spells | Effort |
| ------------- | ------ | ------ |
| Demonic Magic | ~20    | High   |

### New Disciplines to Reject

| Discipline  | Reason                                                       |
| ----------- | ------------------------------------------------------------ |
| Fire Magic  | Covered by Elemental Magic; splitting weakens unified design |
| Wind Magic  | Covered by Elemental Magic                                   |
| Water Magic | Covered by Elemental Magic                                   |
| Wild Magic  | Covered by Shapeshifting + Nature                            |

### Spells to Adopt into Existing Disciplines

| Spell             | Discipline      | Rank | Gap Filled                        |
| ----------------- | --------------- | ---- | --------------------------------- |
| Empower Spell     | General         | 1    | Cooperative casting               |
| Contain Spell     | General         | 3    | Tactical delayed casting          |
| Weaken Spell      | General         | 3    | Counterspell at moment of casting |
| Transfer Energy   | General         | 4    | WP economy manipulation           |
| Anti-Magic Zone   | General         | 6    | Area magic suppression            |
| Relieve Condition | Healing         | 1    | Condition management              |
| Bend Demon        | Healing         | 3    | Offensive anti-demon attack       |
| Transfer Senses   | Awareness       | 1    | Remote scouting through animal    |
| Predict Moves     | Awareness       | 2    | Tactical combat precognition      |
| Warning           | Symbolism       | 1    | Magical alarm system              |
| Animate Object    | Symbolism       | 4    | Object animation                  |
| Talk to Corpses   | Death Magic     | 1    | Communication with dead bodies    |
| Corpse Servant    | Death Magic     | 2    | Temporary undead labor            |
| Create Bloodling  | Blood Magic     | 5    | Blood-servant creation            |
| Frost Armor       | Ice Affinity    | 2    | Ice-based defense                 |
| Glacial Path      | Ice Affinity    | 2    | Traversable ice terrain           |
| Ice Prison        | Ice Affinity    | 3    | Single-target lockdown            |
| Shatter           | Ice Affinity    | 4    | Execute combo payoff              |
| Implant Memory    | Mentalism       | 3    | Memory manipulation               |
| Mind Shield       | Mentalism       | 2    | Mental defense                    |
| Magnetic Shield   | Magnetism       | 2    | Metal-specific defense            |
| Inhabit Animal    | Shapeshifting   | 3    | Animal possession                 |
| Monster Form      | Shapeshifting   | 5    | Monster transformation            |
| Deviation         | Elemental Magic | 1    | Reactive wind defense             |
| Dense Fog         | Elemental Magic | 2    | Vision-blocking zone              |
| Impulse           | Elemental Magic | 2    | Wind-movement buff                |
| Fire Resistance   | Elemental Magic | 2    | Fire-specific defense             |
| Pressure Jet      | Elemental Magic | 3    | Single-target water attack        |

**Total: 28 new spells across 11 disciplines, plus 1 new discipline (Demonic Magic, ~20 spells).**

---

## Implementation Priority

### Phase 1 — Low Effort, High Value (subsystems)

1. Add Rarity/Secretism table to Chapter 7 introduction
2. Add Sacrifice rule sidebar to casting rules
3. Add free-spell-on-rank-gain rule to learning rules
4. Add individual spell learning rule to learning rules
5. Add expanded talent access table
6. Add Mentalism influence mechanic to Mentalism introduction
7. Add Inscribed Symbols subsection to Symbolism
8. Add Blood rot note to Blood Magic
9. Add Fire source bonus note to Elemental Magic
10. Add Stone Song instrument clarification

### Phase 2 — Medium Effort (spell adoptions)

1. Write and integrate 28 new spells into their respective disciplines
2. Update discipline spell tables with new entries
3. Verify no rank conflicts or duplicate mechanics with existing spells

### Phase 3 — High Effort (new discipline)

1. Write full Demonic Magic discipline (~20 spells, mishap table, mog rules, introductory prose)
2. Integrate into Chapter 7 discipline order
3. Add to talent access table and rarity/secretism table

---

## Open Questions for Review

1. ~~**Sacrifice damage distribution.**~~ Resolved: D8 random attribute table adopted. No player choice over sacrifice target.

2. **Demonic Magic scope.** The S&S version includes body alteration (grafting demon-flesh, extra limbs). How grotesque should this get in the corebook? The setting supports horror, but body-horror mechanics need careful handling.

3. **Ice Affinity expansion.** Four new spells are proposed. The corebook's Ice Affinity is intentionally small (14 spells) because the discipline is described as rare outside the Bitter Reach. Does expanding it conflict with that rarity intent, or does the rarity table (Strange / Initiation) adequately gate it?

4. **Rank disagreements.** Some S&S spells that share names with corebook spells have different ranks (e.g., S&S Telepathy at rank 1 vs. corebook rank 3). This proposal does not change any existing corebook spell ranks. Should any be re-evaluated?

5. **General Spells power budget.** Five new general spells are proposed, including the rank-6 Anti-Magic Zone. General spells are available to all casters regardless of discipline. Does adding a rank-6 general spell create too much power access for characters who have not invested deeply in a specific discipline?
