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

**Body text rules:** See *Encounter Design Mandate* below.

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

---

## Encounter Design Mandate

This is the hardest part to get right. Read every word.

### The Core Rule

Every encounter must present an **unexpected moral or physical
dilemma**. Not a fight prompt. Not a village in distress. Not a
monster that needs to be killed.

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
2. Load `forbidden-lands-lore` for any setting facts (kin, places,
   institutions, named NPCs) the encounter will reference.
3. Load `references/monster-design-engine.md` and
   `references/monster-mechanics-taxonomy.md` if the monster's attacks,
   defenses, or weaknesses are being changed rather than merely restyled.
4. Draft the two new encounters. For each, identify which of the
   seven design patterns applies. Confirm the epigraph shows a
   physical scene, not a summary.
5. Draft the new RESOURCES block. Identify the one or two abilities
   or physical facts that make this monster distinct. Build the
   mechanic from those facts up. Check the canonical potion table.
6. Check the Lore Roll rows for format (three rows, LORE ROLL header,
   correct spoiler graduation). Rewrite if they use INSIGHT or
   Results of Insight as the column name.
7. Do not alter statblocks, Monster Attacks tables, or prose
   descriptions unless those are explicitly in scope.
8. Validate with markdownlint-cli2 before submitting.

---

## Workflow: Writing a New Entry from Scratch

1. Establish the monster's core mechanical identity: what it does
   that no other monster does. Write this down first.
2. Read `references/monster-design-engine.md` before drafting rules,
   and `references/monster-mechanics-taxonomy.md` if you need to check
   whether the proposed attacks or defenses already exist in the corpus.
3. Write the statblock from the mechanic outward. Special abilities
   must follow from the identity.
4. Write six Monster Attacks. Each should feel physically distinct
   from the others and should flow from how the creature moves and
   feeds.
5. Write the prose description. Focus on ecology, behavior, and
   origin rumors. Do not repeat what the statblock already states.
6. Write three Lore Roll rows. Start with public knowledge, graduate
   to strong hint, graduate to directional narrative hint.
7. Write two encounters using the design mandate. Use two different
   design patterns.
8. Write the RESOURCES block. Derive from the monster's specific
   abilities.
9. Write the vignette last. One sentence. Physical. Shows the monster
   already present.

If the monster requires a new subsystem-side mechanic rather than a new
combination of existing parts, consult
`references/new-rules-repository.md` before inventing one.

If the manuscript supports legends, also consult
`references/monster-design-engine.md` for legend-placement and
legend-construction rules.

---

## Related Skills

- `forbidden-lands-writing-voice` — voice, diction, anti-AI prose rules
- `forbidden-lands-lore` — setting facts, kin, institutions, geography
- `forbidden-lands-design` — rules integration, mechanic design
- `forbidden-lands-synergy-analysis` — balance review for new monster
   mechanics with combo or exploitation risk
- `rpg-balance-analysis` — when new mechanics need balance audit
