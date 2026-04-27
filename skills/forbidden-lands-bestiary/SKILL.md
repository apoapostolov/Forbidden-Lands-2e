---
name: forbidden-lands-bestiary
description: |
  Use when auditing, writing, or rewriting bestiary entries for the
  Forbidden Lands 2E repo — including random encounters, RESOURCES
  blocks, Lore Roll tables, statblocks, monster descriptions, and
  Monster Attacks tables. Captures the mandatory encounter and
  resources design standards worked out across the Gamemaster's Guide
  and Book of Beasts rewrites so the same quality is reproducible on
  any new monster entry without re-explaining the task. Also load when
  adding a new monster from scratch, migrating a first-edition monster
  to second-edition format, or auditing an existing entry for template
  smell, trope encounters, or flat resources.
---

# Forbidden Lands Bestiary

This skill captures the full format standard, design mandate, and
quality bar for bestiary entries in the Forbidden Lands 2E repo.

Load it alongside `forbidden-lands-writing-voice` for voice,
`forbidden-lands-lore` for setting facts, and
`forbidden-lands-design` when new mechanics need rules integration.

Descriptions, Lore Roll tables, Random Encounters, and Legends are
**lore-bearing prose sections**. Treat them as setting text, not filler.
If you draft or approve any of those sections without
`forbidden-lands-lore`, you are skipping a mandatory companion skill.

This skill now has two layers:

- the **entry-construction layer** in this file
- the **technical monster-engine layer** in `references/`

If the task is about creating, auditing, or extending monster mechanics,
load the reference library as well.

---

## When To Load This Skill

Load this skill when the task involves any of the following:

- writing or rewriting a bestiary entry
- designing a new monster from scratch
- migrating a first-edition monster into second-edition format
- auditing monster attacks, passives, weaknesses, or special defenses
- checking whether a monster's mechanics fit the current engine
- proposing extensions to the bestiary subsystem itself

If the task is mainly about combat balance across talents, spells, or
cross-rule exploits, also load `forbidden-lands-synergy-analysis`.

---

## Mandatory Companion Flow

The following flow is mandatory.

These are not optional nice-to-haves.
They are the load-bearing procedure for the sections that most often go
wrong.

### Hard rule

If the task touches **Monster Description**, **Lore Roll**,
**Random Encounters**, or **Legend**, load `forbidden-lands-lore`
before drafting, rewriting, or approving the text.

### Section-by-section flow

| Section | Mandatory companion skill(s) | Mandatory reference(s) | Why | Recommended size |
| --- | --- | --- | --- | --- |
| H3 Heading | none beyond this skill | this file | keeps naming consistent and prevents article/epithet drift | n/a |
| Flavor vignette | `forbidden-lands-writing-voice` | embedded calibration below | keeps the line physical and inside measured size limits | 14 words |
| Statblock | `forbidden-lands-design` when creating or changing rules | `references/monster-design-engine.md`, `references/monster-mechanics-taxonomy.md` | keeps attributes, passives, defenses, and special lines native to the engine | n/a |
| Monster Attacks table | `forbidden-lands-design` when creating or changing rules | `references/monster-design-engine.md`, `references/monster-mechanics-taxonomy.md`, embedded calibration below | keeps the six attacks mechanically distinct, correctly scaled, and long enough to carry real identity | 284 words total |
| No Monster Attacks section | `forbidden-lands-design` when creating or changing rules | `references/monster-design-engine.md`, `references/monster-mechanics-taxonomy.md` | confirms the creature truly belongs to the no-monster-attacks model rather than being underbuilt | brief explanatory prose; no corpus average |
| Monster Description | `forbidden-lands-lore`, `forbidden-lands-writing-voice` | embedded calibration below | descriptions almost always carry kin, place, cult, history, taboo, or settlement logic | 207 words |
| Lore Roll | `forbidden-lands-lore` | `references/lore-roll-rules.md`, embedded calibration below | row 2 and row 3 are survival clues carried through world knowledge | Row 1: 12 words; Row 2: 28 words; Row 3: 32 words |
| Random Encounters | `forbidden-lands-lore` | `references/random-encounter-design-rules.md`, embedded calibration below | encounters almost always depend on local practice, settlement truth, taboo, kin pressure, trade custom, or regional facts | 185 words total; body 156 words |
| Resources blockquote | `forbidden-lands-design` | this file, `references/resources-design-guide.md`, `references/monster-design-engine.md` when mechanics shift | prevents generic +1 template junk and ties the harvest to anatomy, curse, or physiology | n/a |
| Legend | `forbidden-lands-lore`, `forbidden-lands-writing-voice` | `references/monster-design-engine.md`, embedded calibration below | legends are inherited memory and setting-weight, not free-floating mood text | 211 words |

Recommended sizes in the table are calculated as 110% of the measured corpus average, rounded up to a whole word. Nonprose structural elements are marked n/a.

---

## Workflow: Rewriting an Existing Entry

When given a monster entry to rewrite:

1. Read the entry in full. Note its existing statblock, Monster
   Attacks, Lore Roll, encounters, and resources.
2. Load `forbidden-lands-lore` before touching Description, Lore Roll,
   Random Encounters, or Legend. Treat this as mandatory, not
   conditional.
3. Load `references/monster-design-engine.md` and
   `references/monster-mechanics-taxonomy.md` if the monster's attacks,
   defenses, or weaknesses are being changed rather than merely restyled.
4. Check the mandatory calibration defaults in this file before
   drafting any size-sensitive section.
5. Draft the two new encounters. For each, identify which of the
   seven design patterns applies. Confirm the epigraph shows a
   physical scene, not a summary.
6. Draft the new RESOURCES block. Identify the one or two abilities
   or physical facts that make this monster distinct. Build the
   mechanic from those facts up. Check the canonical potion table.
7. Check the Lore Roll rows for format (three rows, LORE ROLL header,
   correct spoiler graduation, and the mandatory row-2/row-3 hint law
   when a hidden weakness is essential). Rewrite if they use INSIGHT or
   Results of Insight as the column name. Consult
   `references/lore-roll-rules.md`.
8. Do not alter statblocks, Monster Attacks tables, or prose
   descriptions unless those are explicitly in scope.
9. Validate with markdownlint-cli2 before submitting.

---

## Workflow: Writing a New Entry from Scratch

1. Establish the monster's core mechanical identity: what it does
   that no other monster does. Write this down first.
2. Load `forbidden-lands-lore` before drafting Description, Lore Roll,
   Random Encounters, or Legend.
3. Read `references/monster-design-engine.md` before drafting rules,
   and `references/monster-mechanics-taxonomy.md` if you need to check
   whether the proposed attacks or defenses already exist in the corpus.
4. Write the statblock from the mechanic outward. Special abilities
   must follow from the identity.
5. Write six Monster Attacks. Each should feel physically distinct
   from the others and should flow from how the creature moves and
   feeds.
6. Use the mandatory calibration defaults in this file while drafting so
   the entry parts do not collapse below the measured floor or drift far
   below the corpus averages.
7. Write the prose description. Focus on ecology, behavior, and
   origin rumors. Do not repeat what the statblock already states.
8. Write three Lore Roll rows using `references/lore-roll-rules.md`.
   Start with public knowledge, then a deductive non-spoiler hint, then
   a stronger directional hint.
9. Write two encounters using the design mandate and
   `references/random-encounter-design-rules.md`. Use two different
   pressure patterns.
10. Write the RESOURCES block. Derive from the monster's specific
   abilities.
11. Write the vignette last. One sentence. Physical. Shows the monster
   already present.

If the monster requires a new subsystem-side mechanic rather than a new
combination of existing parts, consult
`references/new-rules-repository.md` before inventing one.

If the manuscript supports legends, also consult
`references/monster-design-engine.md` for legend-placement and
legend-construction rules.

If the monster should carry inherited memory, taboo, cult meaning, road
warning, or old explanation, draft a Legend with `forbidden-lands-lore`
already loaded. Do not treat Legend as detachable flavor.

### Escalation rule for encounter realism

If a random encounter depends on bodily ugliness, social cruelty,
economic pressure, burial custom, atrocity weight, starvation,
midwifery, punishment, or other pre-industrial material stress, also
load the relevant `medieval-authenticity-reference` document.

### Approval gate

Do not approve a draft of Description, Lore Roll, Random Encounters, or
Legend until all of the following are true:

- `forbidden-lands-lore` was loaded and used
- the size calibration in this file was checked
- the Lore Roll law was checked if a Lore Roll exists
- the random encounter law was checked if random encounters exist

---

## Mandatory Calibration Defaults

These values are copied directly from the measured corpus and are
**mandatory defaults**, not optional hints.

Use them even if `references/entry-size-calibration.md` is not open.
That reference remains the deeper explanation and methodology file, but
the numbers below are already part of the core skill.

| Element | Corpus average | Hard minimum | Default target | Healthy upper band |
| --- | ---: | ---: | ---: | ---: |
| Typical vignette | 12.3 | 11 | 12 | 14 |
| Monster description | 187.8 | 97 | 188 | 279 |
| Monster attacks table | 257.4 | 145 | 257 | 373 |
| Lore Roll row 2 | 24.9 | 22 | 25 | 28 |
| Lore Roll row 3 | 28.8 | 24 | 29 | 31 |
| Random encounter total | 167.5 | 143 | 168 | 198 |
| Random encounter body | 141.4 | 127 | 141 | 157 |
| Monster legend | 191.8 | 112 | 192 | 270 |

Interpretation:

- **hard minimum** = do not go under this unless there is a deliberate and defensible reason
- **default target** = the normal drafting aim
- **healthy upper band** = room available before the section usually starts to bloat

---

## Technical Reference Library

Use the following files depending on the job.

### `references/monster-design-engine.md`

Load when you need the design logic of the combined bestiary engine:

- what monster attacks are doing systemically
- how defenses, weak points, and passives are structured
- how legends fit the monster pipeline and manuscript structure
- what design constraints a new monster should respect

### `references/monster-mechanics-taxonomy.md`

Load when you need a fast catalog of existing mechanics:

- attack families
- targeting logic
- ranges and damage bands
- conditions, special effects, defenses, and weaknesses
- structure templates for swarms, variants, anchors, and site monsters

### `references/new-rules-repository.md`

Load when the task is not just to create a monster, but to extend the
monster engine itself. This repository covers compatible new mechanics
that can appear in future monster statblocks in order to widen the design
space without simply raising power.

### `references/entry-size-calibration.md`

The calibration values from this file are already embedded in this
skill and are mandatory.

Load the reference when assigning or auditing drafting length and you
need the full methodology, sample notes, or failure explanations.

This file provides measured Book of Beasts word-count floors for:

- vignettes
- monster descriptions
- Monster Attacks tables
- Lore Roll rows
- random encounters
- legends

Use it whenever an AI draft risks becoming technically complete but too
thin to carry scene weight, clue density, or usable attack identity.

### `references/random-encounter-design-rules.md`

Load whenever writing or auditing random encounters.
This reference is mandatory whenever encounters are in scope.

This is the strict encounter-law reference. It formalizes the manuscript's
required encounter style:

- medieval material reality
- discomfort and pressure
- unexpected realistic situations
- moral or physical trade-offs
- player-facing choices that should provoke argument, not easy consensus

### `references/lore-roll-rules.md`

Load whenever writing or auditing Lore Roll tables.
This reference is mandatory whenever a Lore Roll is in scope.

This file governs:

- clue graduation across rows 1-3
- measured row-size floors
- spoiler discipline
- the mandatory hint structure for monsters whose hidden weakness is the
   only normal way to defeat them

### `references/resources-design-guide.md`

Load whenever writing or auditing RESOURCES blocks.

This is the corpus-grounded reference for designing new monster resources.
Use it alongside the Resources Design Mandate section of this file. It
provides:

- harvest mechanics syntax (verb selection, talent selection, skill selection)
- material taxonomy (biological fluids, biological solids, supernatural
  essences, intact artifacts)
- effect type taxonomy with scale guidelines (Artifact Dice, Potency, flat
  bonuses, attribute restoration)
- consequence design patterns (duration, physical cost, social cost,
  faction notice, ecological cost, double-dose penalty)
- canonical potion ingredient table with full monster-ingredient-potion mapping
- RARE designation rules
- intact regardless rules
- design decision checklist
- a worked example of deriving resources from monster identity
- forbidden patterns

This reference supersedes the summary in the Resources Design Mandate
section when in conflict; both should be consulted for any new RESOURCES block.

---

## Canonical Entry Format

Every monster entry follows this structure exactly, in this order.

### 1. H3 Heading

```markdown
### Monster Name
```

Single proper noun. No articles, no epithets unless they are the
established name (e.g. **Death Knight**, not **the Death Knight**).

---

### 2. Flavor Vignette

```markdown
> _One sentence. A physical object, a smell, a sound, or a single
> observed action. No mood summary. No adjective stacks._
```

The vignette is the reader's first contact with the monster. It does
not describe the monster directly. It shows a corner of a scene the
monster already occupies — a locked fold with frost on the latch, a
smell that reaches the village before the troll does, a hat drifting
down before the screaming starts.

**Measured size rule:** A typical vignette has a hard minimum of **11
words**, a corpus average of **12.3**, a default target of **12**, and
a healthy upper band around **14**. If it drops below 11 words, it
usually stops making an image.

**Forbidden in the vignette:**

- Named emotional states ("terror gripped the farm")
- Summary of monster type ("a fearsome predator")
- Passive constructions that remove the physical actor
- More than one sentence

---

### 3. Statblock

Statblock entries are a bullet list. No blank lines between bullets.
Bold-prefix labels. Fullcaps for attribute and skill names.

```markdown
- **ATTRIBUTES:** Strength X, Agility X, Wits X, Empathy X
- **SKILLS:** Skill 1 X, Skill 2 X
- **ARMOR RATING:** X (brief material note)
- **MOVEMENT:** X
- **SPECIAL ABILITY NAME:** Description. One sentence or two.
```

Only include attribute rows that are present. Not all monsters have
Wits and Empathy. Omit what is absent rather than writing "None."

**Special ability entries** use a FULLCAPS bold prefix. If the
ability triggers on a roll, the roll results appear as an inline table
directly beneath the bullet:

```markdown
- **REGENERATE:** A Troll recovers one point of lost Strength each round.
- **STENCH:** All enemies within ARM'S LENGTH suffer one point of
  damage to Agility each round because of the Troll's horrible stench.
- **SUNLIGHT:** A Troll suffers one point of damage per round in
  direct sunlight.
```

If a special ability has multiple outcomes on a die roll (e.g. a
disease or poison result table), those outcomes appear as a table
directly after the ability bullet, before the next bullet:

```markdown
- **TAIL:** If an attack against the tail (–2 penalty) draws blood,
  roll a D6 each time the Sea Serpent attacks.

| D6  | RESULT                                       |
| --- | -------------------------------------------- |
| 1–3 | The beast attacks the nearest adventurer.    |
| 4–6 | The beast attacks itself instead.            |
```

---

### 4. Monster Attacks Table (H4)

```markdown
#### Monster Attacks

| **D6** | **ATTACK**                                                   |
| ------ | ------------------------------------------------------------ |
| 1      | **ATTACK NAME!** Description of attack.                      |
| 2      | **ATTACK NAME!** Description of attack.                      |
| 3      | **ATTACK NAME!** Description of attack.                      |
| 4      | **ATTACK NAME!** Description of attack.                      |
| 5      | **ATTACK NAME!** Description of attack.                      |
| 6      | **ATTACK NAME!** Description of attack.                      |
```

- Always six rows.
- Column headers are bold.
- Attack name is bold, fullcaps, followed by exclamation mark.
- Attack description states Base Dice, Weapon Damage, damage type
  (slash wound / blunt force), and any condition (GRAPPLED, prone,
  thrown to SHORT range, etc.).
- The table has a hard minimum of **145 words total**, a target of
   **257**, and a healthy upper band around **373**. If it falls well
   below floor, the rows usually become repetitive or mechanically vague.
- If the monster has no Monster Attacks (e.g. Undead, which fight as
  normal combatants), replace the table with:

```markdown
#### No Monster Attacks

[Explanation of how the monster fights instead.]
```

---

### 5. Monster Description

One or more prose paragraphs after the attacks table. This is the
GM-facing description of the monster's ecology, behavior, origin
rumors, and notable traits. Written in manuscript voice (see
`forbidden-lands-writing-voice`). No H-subheadings inside it.

**Mandatory companion skill:** `forbidden-lands-lore`.
Descriptions are lore-bearing prose. They should be checked for kin,
geography, religion, institutions, post-Blood Mist logic, and local
social practice even when no obvious proper noun appears at first glance.

**Measured size rule:** The description has a corpus average of
**187.8** words, a hard minimum of **97**, a default target of **188**,
and a healthy upper band around **279**. Below floor, AI drafts usually
repeat the statblock instead of adding ecology, habit, and world weight.

---

### 6. Lore Roll Table (H4)

```markdown
#### Lore Roll

| D6 | LORE ROLL                                                    |
| -- | ------------------------------------------------------------ |
| 1  | Row 1 text.                                                  |
| 2  | Row 2 text.                                                  |
| 3  | Row 3 text.                                                  |
```

- Three rows. The D6 column uses values 1, 2, and 3.
- Column header for results is **LORE ROLL**, not INSIGHT, not RESULT.
- Row 1 is safe public knowledge — what any traveler might know.
- Row 2 is a solid in-world hint at a weakness or pattern, framed
  through song, rumor, old observation, or herder wisdom. It should
  require the players to think; it must not give away the mechanic.
- Row 3 is a more directional hint. It can include a narrative effect
  (what happens when the solution is applied) but must not state
  mechanic words (no roll names, no stat names) or feel like spoilers.
  It can carry atmosphere — what the old woman said, what the archer-
  king's lore teaches, what the Rust Brothers found in the catacomb.
- Use the measured row floors from
   `references/entry-size-calibration.md`: **row 1 minimum 12 words**,
   **row 2 minimum 22 words**, **row 3 minimum 24 words**. Row 2 has a
   corpus average of **24.9** words; row 3 has a corpus average of
   **28.8** words.
- Use `references/lore-roll-rules.md` as the strict law.
- **Mandatory companion skill:** `forbidden-lands-lore`.
  Lore Roll rows are inherited world knowledge. They should be written
  as setting-bearing clues, not generic hint text.
- If a monster's hidden weakness is the only normal way to defeat it,
   then **row 2 must contain a non-spoiler hint** and **row 3 must
   contain a stronger flavorful hint**. This is mandatory. Row 2 should
   still require deduction; row 3 should still sound like world-lore,
   not rules text.

---

### 7. Random Encounters (H4, two minimum)

Each encounter is a separate H4 section:

```markdown
#### Random Encounter: Title

> _Epigraph — one sentence, physical and concrete._

Body text. One or two paragraphs.

- **Terrain Types:** Type A, Type B
```

**Epigraph rules:** Same as the vignette. One sentence. Physical
object, smell, sound, or observed action. The title and epigraph
together should make a GM want to run the scene.

**Body text rules:** See *Encounter Design Mandate* below and the full
strict reference in `references/random-encounter-design-rules.md`.

**Mandatory companion skill:** `forbidden-lands-lore`.
Random encounters almost always rely on local beliefs, place logic,
settlement practice, kin pressure, trade custom, taboo, or regional
memory. Draft them with the lore skill loaded even when the scene looks
"generic" at first.

**Measured size rule:** Each encounter has a corpus average of
**167.5** words total excluding `Terrain Types`, a hard minimum of
**143**, a default target of **168**, and a healthy upper band around
**198**. The body text itself has a corpus average of **141.4** words,
with a hard minimum of **127** and a healthy upper band around **157**.
Below floor, the encounter usually becomes a premise instead of a
dilemma.

**Terrain Types:** Bold prefix, comma-separated, no period.

---

### 8. Resources Blockquote

```markdown
> **RESOURCES**
>
> [Resources paragraph]
```

See *Resources Design Mandate* below.

---

### 9. Legend (Optional but strongly preferred)

If the manuscript has a dedicated Legends chapter, create the legend as a
separate entry there.

If the manuscript has no Legends chapter, place the legend directly after
the monster entry, after the RESOURCES block.

If the monster is important enough to shape regional memory, cult
practice, taboo, or old road-lore, the entry should usually receive a
legend.

**Mandatory companion skill:** `forbidden-lands-lore`.
Legends are not optional flavor mist. They are setting memory. Use the
lore skill to check place names, factions, cult practice, pre-Blood Mist
logic, regional framing, and whether the belief sounds like the
Ravenlands instead of generic dark fantasy.

**Measured size rule:** A legend has a corpus average of **191.8**
words, a hard minimum of **112**, a default target of **192**, and a
healthy upper band around **270**.

---

## Encounter Design Mandate

This is the hardest part to get right. Read every word.

For the full mandatory rule set, load
`references/random-encounter-design-rules.md`.
The summary below is not a looser alternative. It is the short form of
the same law.

### The Core Rule

Every encounter must present an **unexpected moral or physical
dilemma**. Not a fight prompt. Not a village in distress. Not a
monster that needs to be killed.

The encounter may be grim, uncomfortable, light-hearted, humorous, or
faux-dangerous.
If it is grim, it should usually center on **one dominant discomfort
register**, not a heap of them.

Common registers include:

- material
- bodily
- social
- moral
- reputational
- decisional

The encounter must arise from a believable pre-industrial arrangement:

- food, water, labor, toll, burial, kin, shrine, or road custom
- a working compromise already under strain
- a physical bind already in place before the adventurers arrive

The monster should be a force inside that situation, not the whole
scene by itself.

If the encounter can be summarized as "monster is nearby, fight or
flee," it fails the mandate.

### Anti-Patterns (Forbidden)

These are tropes from basic fantasy roleplaying. None of them are
permitted in this manuscript:

- Villagers ask adventurers to kill the monster.
- Monster attacks the farm/village/road directly.
- Survivor tells adventurers where the monster is.
- Adventurers find obvious monster lair with treasure inside.
- Straightforward rescue with no moral weight.
- Any encounter where the obvious action is also the only action.

### Design Patterns (Required)

Use one or more of these per encounter:

1. **The victim is not innocent.** The person being harmed caused
   the problem, profits from the problem, or knows more than they
   say. The adventurers must decide whether innocent bystanders
   still matter.

2. **Saving one damns another.** Rescuing A directly causes harm to
   B. The adventurers cannot save both. There is no third option.

3. **The monster is the symptom.** The real problem is a human
   choice, a practice, a long silence. The monster is just the part
   that makes noise. Killing the monster changes nothing.

4. **The villagers are complicit.** The community knows. They have
   benefited, or they have let it happen, or they have no better
   choice. They are not asking for justice; they are asking for
   quiet.

5. **The pay is generous; the price is worse.** The adventurers
   are offered real silver for a job that will cost them something
   they cannot get back — time, knowledge, neutrality, a witness
   relationship.

6. **The monster cannot leave; the adventurers cannot stay.** A
   physical constraint (terrain, season, condition) turns the
   encounter into a timed decision rather than a tactical problem.

7. **A person has already decided.** The farmer's daughter has
   stacked the straw. The fisherman's wife has tied herself to the
   mast. The adventurers are too late to prevent the decision; they
   can only choose whether to honor or override it. This transfers
   the moral weight from the monster to the person.

### Epigraph Construction

The epigraph must not explain what the encounter is. It must show one
physical detail that makes the scene feel already real. The GM should
be able to picture the scene before reading the body text.

**Good:** *Three copper coins on the table. His daughter of ten sleeps
on the hearthrug with the dog beside her.*

**Bad:** *A farmer's old sheepdog has been turned by a nightwarg and
the farmer is afraid.*

The bad version summarizes. The good version places you inside the
scene.

---

## Resources Design Mandate

### The Core Rule

Every RESOURCES block must be **unique to that monster's specific
ability or physiology**. No two monsters produce the same category
of bonus through the same mechanic.

### The Forbidden Pattern

This pattern is banned in every form:

> *A dose may be used in a potion that gives +1 to [SKILL] for one
> Quarter Day.*

Variations are also banned:

- "+1 to X against Y"
- "+1 to X in Z terrain"
- "one dose restores 1 point of X"
- Any flat +1 bonus to any roll

**Why:** +1 to a Year Zero roll requires at least five base dice to
matter statistically. A flat +1 on fewer dice is mechanically
invisible. It is a template written to fill space, not a game tool.

### Required: Mechanics Tied to the Monster

The resource must derive from what the monster *does*, not from what
category the monster belongs to.

Examples (from the manuscript):

| Monster | Ability | Resource Mechanic |
| ------- | ------- | ----------------- |
| Nightwarg | Dissolves at dawn; bite frosts flesh | Night-shadow: D10 Artifact Die to SNEAK at night; frosts every wound |
| Strangling Vine | Paralyzing spores; flesh-eating root | Spores: Potency 8 poison; root-fibre: living rope, ignores 3 Armor Rating |
| Sea Serpent | Self-devours when tail is cut | Tail-gland draws serpents; crown-horn whistle calls serpent once |
| Troll | Regeneration; mineral feces | Bile: D3 Strength restore; mineral nodule: reforges broken weapon |
| Wyvern | Warm blubber; pinion attack | Blubber: smokeless warmth; pinion-bone: +2 DODGE vs flyers; oil: D8 Artifact Die on aerial shots |
| Undead/Ghoul | Disease bite; bone structure | Grave-salt: threshold barrier (also traps living); ghoul tooth: understand dead speech |

### Acceptable Bonus Scales

When a bonus to a roll is appropriate:

- **+2 or better** — minimum meaningful bonus in Year Zero
- **D8 Artifact Die** — strong, narrow use, appropriate for rare ingredients
- **D10 Artifact Die** — exceptional, restricted to one specific act
- **Potency 8–12** — for poisons and paralytic agents
- **D3 attribute restoration** — for healing ingredients

### Canonical Potion Ingredients

These are established in the Corebook. When these monsters appear,
their resources must name the ingredient. Do not invent a different
effect:

| Monster | Ingredient | Potion |
| ------- | ---------- | ------ |
| Giant | Giant's blood | Drops of Strength |
| Troll | Troll's blood | Healing Decoction |
| Troll | Troll's tooth | Elixir of Wisdom |
| Troll | Troll's gastric juice | Bellyfull |
| Dragon | Dragon's blood | Elixir of Life |
| Dragon | Dragon's scale | Iron Juice |
| Dragon | Dragon's tooth | Decoction of Cunning |
| Gryphon | Gryphon's feather | Quick Nectar |
| Hydra | Hydra's blood | Healing Water |
| Hydra | Hydra's acid | Refreshing Decoction |
| Ghoul | Ghoul's bones | Longwalk |
| Sea Serpent | Sea serpent's gall | Quenching Swig |
| Insectoid | Insectoid's blood | Honey of Embers |
| Manticore | Manticore's blood | Calming Decoction |
| Drakewyrm | Drakewyrm's acid | Intoxicating Decoction |

When the monster's resource names the canonical ingredient, it should
also describe a secondary use or a narrative property unique to the
monster — the ingredient substitution is not sufficient on its own.

### Resources Block Structure

The block always opens with the harvest mechanic:

> An adventurer with the ALCHEMIST talent, with a HEALING roll,
> [harvests / draws / preserves / gathers] [quantity] of [material]
> per ⚔️ rolled[, plus [other material] per kill].

Then names each material and its specific mechanical or narrative use.

---

## Workflow: Rewriting an Existing Entry

When given a monster entry to rewrite:

1. Read the entry in full. Note its existing statblock, Monster
   Attacks, Lore Roll, encounters, and resources.
2. Load `forbidden-lands-lore` before touching Description, Lore Roll,
   Random Encounters, or Legend. Treat this as mandatory, not
   conditional.
3. Load `references/monster-design-engine.md` and
   `references/monster-mechanics-taxonomy.md` if the monster's attacks,
   defenses, or weaknesses are being changed rather than merely restyled.
4. Check the mandatory calibration defaults in this file before
   drafting any size-sensitive section.
5. Draft the two new encounters. For each, identify which of the
   seven design patterns applies. Confirm the epigraph shows a
   physical scene, not a summary.
6. Draft the new RESOURCES block. Identify the one or two abilities
   or physical facts that make this monster distinct. Build the
   mechanic from those facts up. Check the canonical potion table.
7. Check the Lore Roll rows for format (three rows, LORE ROLL header,
   correct spoiler graduation, and the mandatory row-2/row-3 hint law
   when a hidden weakness is essential). Rewrite if they use INSIGHT or
   Results of Insight as the column name. Consult
   `references/lore-roll-rules.md`.
8. Do not alter statblocks, Monster Attacks tables, or prose
   descriptions unless those are explicitly in scope.
9. Validate with markdownlint-cli2 before submitting.

---

## Workflow: Writing a New Entry from Scratch

1. Establish the monster's core mechanical identity: what it does
   that no other monster does. Write this down first.
2. Load `forbidden-lands-lore` before drafting Description, Lore Roll,
   Random Encounters, or Legend.
3. Read `references/monster-design-engine.md` before drafting rules,
   and `references/monster-mechanics-taxonomy.md` if you need to check
   whether the proposed attacks or defenses already exist in the corpus.
4. Write the statblock from the mechanic outward. Special abilities
   must follow from the identity.
5. Write six Monster Attacks. Each should feel physically distinct
   from the others and should flow from how the creature moves and
   feeds.
6. Use the mandatory calibration defaults in this file while drafting so
   the entry parts do not collapse below the measured floor or drift far
