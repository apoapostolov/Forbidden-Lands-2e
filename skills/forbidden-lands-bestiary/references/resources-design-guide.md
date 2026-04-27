# Resources Design Guide

Corpus-grounded reference for designing RESOURCES blocks in Forbidden Lands 2E
bestiary entries. Derived from analysis of every RESOURCES block in
`02-gamemasters-guide/06-bestiary.md` and `03-book-of-beasts/02-bestiary.md`.

---

## The Canonical Rules Text

Both books state the harvest rules in the same words:

> A vanquished monster can be harvested for what the body holds. Each
> description names the talent and skill required and the resources available.
> Make the roll. Each ⚔️ lets the player choose one resource from the list.
>
> Resources marked **(RARE)** can only be taken on a roll of two or more ⚔️
> total. With a single success, the item has been spoiled or destroyed in the
> fight and cannot be recovered. Some items are always recoverable regardless
> of the roll; these are noted as **intact regardless of dice rolled**.

---

## Block Structure

Every RESOURCES block follows this exact structure:

```markdown
> **RESOURCES**
>
> [One or two framing sentences naming the talent and skill, and naming all
> available resources.]
>
> **Material Name (RARE if applicable).** [Description and uses.]
>
> **Material Name.** [Description and uses.]
>
> **Material Name.** [Description and uses.]
```

### Framing sentence grammar

Standard form:

> An adventurer with the [TALENT] talent, with a [SKILL] roll,
> [harvest verb] one of the following per ⚔️ rolled, player's choice:
> **material A (RARE)**, **material B**, or **material C**.

With supplemental harvest:

> An adventurer with the [TALENT] talent, with a [SKILL] roll,
> [harvest verb] one of the following per ⚔️ rolled, player's choice:
> **material A** or **material B (RARE)**, [plus a second sentence naming
> an additional separately-obtained item].

The framing sentence names every item in the block in bold. If an item is
RARE, that marker appears in the framing sentence as well as in the item entry.

---

## Harvest Verb Selection

The verb reflects the physical nature of the material. Match the verb to the
source material.

| Verb | Use for |
| --- | --- |
| draws | Fluids from glands, veins, organs, or reservoirs |
| recovers | Solid items extracted from the body |
| gathers | Scattered, diffuse, or multiple-piece materials (ash, dust, crystals) |
| catches | Ephemeral or escaping materials (spirit essences, air, mist) |
| scrapes | Surface deposits (grave-salt, bog-tar, wall-crust) |
| strips | Structural mass removal (dragon-iron from carcass) |
| cuts | Precise anatomical harvesting (feathers, horns, tongues) |

Do not use "collects," "obtains," "takes," or other generic terms.

---

## Talent Selection

The talent gate determines who can harvest the resource and how difficult it
is to access. Select on the basis of the material, not the monster category.

| Talent | Use for |
| --- | --- |
| ALCHEMIST | Most biological fluids, poisons, processed extracts, alchemical ingredients |
| HUNTER | Pelts, bones, claws, practical anatomical parts |
| SMITH | Structural metal, forged parts, structural stone |
| TANNER | Hides, leather-craft materials |
| CRAFTER | Worked organic material (sinew, cord, chitin) |
| SORCERER | Supernatural essences, bound demonic material, spirit residue |
| DRUID | Nature spirits, nature-bound material, plant material |
| HEALER | Medicinal and restorative biological material |

Dual talent options ("ALCHEMIST or HUNTER") are legitimate when the material
could reasonably be obtained by either craft. Use them to broaden access for
common materials. Restrict to a single talent for materials where the harvesting
method is genuinely specialized.

---

## Skill Selection

Match the skill to the physical act of harvesting. Do not default to HEALING
for every block.

| Skill | Use for |
| --- | --- |
| HEALING | Anatomical precision, biological fluids, medical extraction |
| CRAFTING | Structural, worked, or shaped materials |
| SURVIVAL | Wilderness materials, tracking-related harvests |
| LORE | Occult, necromantic, or supernatural materials |
| SCOUTING | Materials discovered through careful observation or terrain search |
| INSIGHT | Non-physical or emotionally-resonant materials (ghost residue) |

HEALING is the most common. When HEALING appears with a SMITH or TANNER
talent, that is a signal the material is primarily biological even if it has
craft uses.

---

## Item Count

Most entries have three items. A smaller subset has two. The count should
match the mechanical richness of the monster.

- **Three items**: standard for most monsters
- **Two items**: appropriate for simpler monsters or when a third item would
  require inventing a mechanic not rooted in the creature's abilities
- **Four items**: rare; acceptable only when a separate "intact regardless"
  item supplements a two-item roll table (the intact item is not part of the
  per-⚔️ choice)

Do not inflate to three items if the third item would be generic or recycled
from another monster.

---

## RARE Designation

A RARE item can only be taken on a roll of two or more ⚔️. A single ⚔️
destroys or spoils it.

**Apply RARE to:**

- Items with D10 Artifact Dice or other very powerful effects
- Single-dose items with no replacement pathway
- Canonical potion ingredients (most are RARE)
- Items that would break encounters if readily accessible
- Items that factions hunt actively

**Do not apply RARE to:**

- Utility items with modest bonuses (D8 Artifact Die or lower)
- Items the player might plausibly need in every session
- Items whose only function is to be sold

Typical blocks have one RARE item out of three. Having two RARE items is
acceptable when both warrant it. Having all three RARE is unusual and signals
the monster is exceptionally dangerous to harvest.

---

## Intact Regardless of Dice Rolled

Some items are recovered automatically, independent of the roll. These are
physical objects the monster carried, wore, or was bound by — they are not
biological resources.

**Use "intact regardless of dice rolled" for:**

- Weapons the monster was fighting with
- Binding tokens (rings, cords, knucklebones, cages)
- Equipment the monster wore (collars, chains, armor-pieces)
- Structural artifacts central to the monster's nature (portal-stones, blood-stones, bone flutes)
- Treasure the monster guarded as part of its identity (grave-tokens, grave-treasure)

**Do not use it for:**

- Biological materials (organs, glands, fluids)
- Magical essences tied to the creature's life-force
- Anything that would logically be destroyed in the fight

Intact items appear after the main per-⚔️ harvest sentence, introduced as
a separate clause ("plus the [item name] found beside the body, intact
regardless of dice rolled").

---

## Effect Type Taxonomy

### Artifact Dice

The standard bonus mechanism. Adds to a single roll.

| Die | Appropriate for |
| --- | --- |
| D8 | Common solid materials, utility effects, moderate bonuses |
| D10 | Rare materials, powerful restricted effects |
| D12 | Exceptional materials; very rare in the corpus |

D8 is the workhorse. Most RESOURCES items that grant a roll bonus use D8.
D10 appears on RARE items or items tied to the monster's most distinctive
ability. D12 is unusual; the giant specter's star-ash (for healing magic)
is the only D12 in the corpus.

### Potency for Poisons and Paralytic Agents

| Potency | Appropriate for |
| --- | --- |
| 6 | Minor toxins, degraded or small-creature venoms |
| 7 | Standard venom from spiders, scorpions, centipedes, snake queens |
| 8 | Strong paralysis from soldiers, strangling vine, insectoid, manticore |
| 9 | Potent corrosive or neurological agents (abyss worm acid) |
| 10–12 | Exceptional; elder female giant spider (10–12); stacked strangling vine (12) |

Do not invent a Potency 5 or lower poison from a dangerous monster.
Do not give a minor creature a Potency 9 or higher without strong
anatomical justification.

### Attribute Restoration

Attribute restoration is high-value and should be reserved for materials
tied to the monster's most powerful regenerative or life-force ability.

- **D3 attribute restoration**: the correct scale; used for troll blood,
  giant blood, dragon blood, hydra blood, tupilaq unmaking-cream
- **Full restoration** of STRENGTH and AGILITY: very exceptional; only
  the tupilaq's unmaking-cream achieves this, and it cannot touch
  critical injuries

Do not grant flat attribute restoration without tying it to a cost or a
specific biological origin (regeneration, dragon-life, monster vitality).

### Flat Structural Bonuses

Flat bonuses to Armor Rating or Weapon Damage are acceptable when they come
from a SMITH, TANNER, or CRAFTER process that produces a physical item.

- "+2 Armor Rating" from worked dragon scale, stitched into armor: acceptable
- "+2 to DODGE" from pinion-bone set into a shield: acceptable
- "+1 to [SKILL] for one Quarter Day": forbidden; too small to matter

The minimum meaningful flat bonus in Year Zero is +2. Do not write +1 to any
skill roll unless it is paired with a D8 Artifact Die or another effect.

---

## Material Taxonomy

### Biological Fluids

Blood, bile, ichor, saliva, venom, milk, acid, oil, fat, juice.

These are the most common materials. Every monster has some fluid that can
be drawn. The effect should derive from what that fluid does inside the
monster's body.

**Design rule**: If the fluid paralyzes prey inside the monster, it paralyzes
as a poison coating. If the fluid regenerates the monster, it restores
attributes in a drinker. If the fluid marks or attracts prey, it does the
same as a tool.

### Biological Solids

Teeth, claws, bones, horns, scales, feathers, hide, sinew, chitin, tongue,
eyes, membranes, glands.

These yield structural tools: weapons, armor components, rope, lenses,
cordage. Their effects follow from how they functioned in the monster's body.

**Design rule**: Eye material gives vision in darkness or detection effects.
Bone material gives weapons or structural reinforcement. Hide material gives
armor or environmental resistance. Teeth set into weapons give attack bonuses
tied to the monster's own biting.

### Supernatural Essences

Shadow-residue, grave-frost, cold-seam dust, echo-fragments, storm-glass,
spirit-musk, panic-blood, metamorph-secretion, brain pearl.

These come from monsters whose nature is not purely physical. The material
is the embodiment of the monster's specific supernatural property.

**Design rule**: The essence must do something the monster was doing.
A fear-drinker's panic-blood amplifies fear attacks. A nightwarg's night-shadow
grants stealth at night. A shapeshifter's secretion grants disguise. Never
assign a supernatural essence an effect unrelated to the creature's ability.

### Intact Artifacts

Weapons, binding tokens, cages, stones, flutes, staffs, grimoires, collars.

These are defined above under "Intact Regardless of Dice Rolled." They are
the physical objects the monster carried, not the monster's biology.

---

## Consequence Design

Every item in a RESOURCES block should have at least one of the following
consequence types. Most have two. The consequences ground the material in
the setting and make the choice to use it meaningful.

### Duration

Almost all effects are time-limited. Common durations:

- **One combat**: single-use weapon coatings, burst effects
- **One stretch**: short-duration effects requiring active presence
- **One Quarter Day**: standard medium-duration effects
- **One night / one journey leg**: travel-scale effects
- **One season**: long-term crafted items (stitched armor, built items)

Do not write effects with unlimited or permanent duration. Every effect ends.

### Physical Cost to User

A significant minority of items impose a physical or mental toll:

- 1 point of attribute damage (Wits, Agility, Empathy, Strength)
- A condition (HUNGRY, COLD, SCARED, SICK, THIRSTY, EXHAUSTED, BLEEDING)
- A recovery condition (must sleep, must eat raw meat, eyes weep for a day)
- Fever, nausea, or involuntary physical symptom

The physical cost appears after the stated benefit, not before. It should be
proportionate to the benefit's power: D10 Artifact Die items warrant real
costs; D8 items may have minor inconveniences.

### Social Cost / Faction Notice

Many items bring faction attention. This is one of the most consistent
patterns in the corpus:

- Iron Guard recognizes and confiscates, or hangs the bearer
- Raven Sisters demand, purchase, or burn
- Rust Brothers purchase without questions, or hunt for
- Druids burn the item, the wearer's hand, or both
- Stoneborn recognize and demand return
- Congregation of the Serpent purchases at above-market rates
- The Howling Path hunts any user of anti-lycanthrope materials

Assign faction notice based on what the faction cares about:

| Faction | What draws their attention |
| --- | --- |
| Iron Guard | Anti-law weapons, corrosive agents, chaos items, cult evidence |
| Raven Sisters | Death-magic items, stolen grave-goods, binding tokens |
| Rust Brothers | Demonic material, occult fluids, anything with no questions asked |
| Druids | Kin-defilement, corrupt nature, stolen spirit-goods |
| Stoneborn | Dwarven kin-goods, dragon materials, cave-creature bones |
| Congregation of the Serpent | Serpent-related materials, petrification agents |
| Howling Path | Anti-lycanthrope materials, silver-worked items from their kin |

Do not assign faction notice to every item. Reserve it for the most
consequential resources, typically RARE items and intact artifacts.

### Ecological Cost

Some materials attract more monsters, damage the land, or trigger setting-level
consequences:

- Carrying the scent calls more of the same creature
- Burying a material at a site kills the land for seasons
- Using an attractor material near a living colony starts combat

Use ecological costs to make the decision to keep or use a material meaningful
beyond its mechanical benefit.

### Double-Dose Penalty

A substantial number of items include a rule for what happens if the material
is used twice within the same Quarter Day or the same day. The second use
is always worse than the first:

- Greater physical damage
- The beneficial effect reverses
- A condition appears that the first dose does not cause
- Permanent attribute loss

Write double-dose penalties for:

- Attribute-restoring fluids (dragon blood, troll blood, giant blood)
- Potent transformation items (horn powder, metamorph-secretion)
- Any item where "more is better" would be exploitable

---

## Canonical Potion Ingredients

The following are established. If one of these monsters appears, the resources
block must name the canonical ingredient and its potion. A secondary use must
also appear — the canonical ingredient is not sufficient on its own.

| Monster | Ingredient | Potion |
| --- | --- | --- |
| Giant | Giant's blood | Drops of Strength |
| Troll | Troll's blood | Healing Decoction |
| Troll | Troll's gastric juice | Aqua Fortis of the Smiths |
| Troll | Troll's tooth | Elixir of Wisdom |
| Rock Troll | Troll's blood (all three troll variants) | Tincture of Earth-Hide |
| Water Troll | Brackish-bile (troll blood variant) | Tincture of Earth-Hide |
| Dragon | Dragon's blood | Elixir of Life |
| Dragon | Dragon's scale | Tincture of Earth-Hide |
| Dragon | Dragon's tooth | Tooth Powder of the Stoneborn |
| Iron Dragon | Dragon's blood / scale / tooth (canonical) | Same as Dragon |
| Mire Drake | Dragon's blood / scale / tooth (canonical) | Same as Dragon |
| Undead Dragon | Corrupt-marrow (corrupted blood) / grave-scale / tooth | Corrupted variants |
| Gryphon | Gryphon's feather | Quick Nectar |
| Hydra | Hydra's blood | Healing Water |
| Hydra | Spent acid (hydra's acid) | Refreshing Decoction |
| Ghoul / Undead | Ghoul's bones | Longwalk |
| Sea Serpent | Serpent's gall | Quenching Swig |
| Insectoid | Worker blood | Honey of Embers |
| Swarming Death | Insect-ichor | Insect Brew of the Hive-Mind |
| Manticore | Manticore blood | Calming Decoction |
| Drakewyrm | Stomach acid | Intoxicating Decoction |
| Twisted Ent | Blackened ruby | Demon-Heart Tincture |
| Giant Spider | Giant spider's venom | Porridge of Prophecy |

When writing a resources block for any monster on this table, mark the
ingredient as **(RARE, canonical)** in the framing sentence. In the item entry,
note it as "The canonical alchemical ingredient for [Potion Name] (see the
Corebook)" or "The bound alchemical ingredient for [Potion Name] (see
_Alchemical Potions_)."

---

## Design Decision Checklist

Before writing a RESOURCES block, answer these questions:

**1. What is the monster's most distinctive ability?**

Write it down. The primary RARE resource must derive from that ability.
If the monster paralyzes prey: paralytic agent. If it regenerates: restorative
fluid. If it moves unseen at night: stealth-granting essence. If it deceives
or mimics: voice or face material.

**2. What does the monster's body physically contain that a person could use?**

Glands, eyes, horns, hide, fat, sinew, bone, teeth, feathers, chitin, scales —
all are valid if the effect follows from the organ's function.

**3. Does this monster appear on the canonical potion table?**

If yes, include the canonical ingredient marked correctly.

**4. What does the monster's ecology or origin suggest for a secondary effect?**

A cave creature's material should have underground or darkness effects. A
coastal creature's material should have water or cold effects. A demon's
ichor should have supernatural or warding effects.

**5. Is there a faction that would want this?**

Almost always yes. Assign the appropriate faction and the appropriate
consequence (will pay / will confiscate / will burn the bearer).

**6. What is the physical or social cost of using each item?**

Every item needs at least one consequence. Duration alone is not a consequence.

**7. Are any items actually the same effect in different words?**

If two items in the block produce a D8 Artifact Die to the same class of
roll under the same conditions, one of them is a duplicate. Rewrite or cut.

---

## Forbidden Patterns

These patterns appear in no corpus entry and must not appear in new ones:

- "+1 to [SKILL] for one Quarter Day" — flat +1 to any skill roll
- "restores 1 point of [attribute]" — flat 1-point restoration without a die
- "useful ingredient in potions" — vague ingredient with no defined use
- "[material] can be sold for silver" — only as a secondary tag on an
  otherwise-specified item; never as the sole description of an effect
- Effects completely unrelated to the monster's stated biology or ability
- Items that replicate exactly what another monster's item already does

---

## Worked Example: Deriving Resources from Monster Identity

**Monster**: Hypothetical cave leech. Special ability: it numbs the flesh at
the bite so the victim does not notice blood loss until the leech detaches.
It also secrets a hardening slime over its eggs.

**Step 1 — Distinctive ability**: numbing bite; hardening secretion.

**Step 2 — Physical contents**: numbing-gland at the jaw; hardening-slime
from the body surface; blood reservoir from a gorged specimen.

**Step 3 — Canonical table**: no match.

**Step 4 — Ecology**: cave creature; parasitic; cold-water environment.

**Step 5 — Faction hooks**: Hedge healer wants a numbing agent. Iron Guard
would confiscate anything that suppresses pain awareness (makes soldiers
less functional in a fight). Rust Brothers might want the hardening slime
for sealing.

**Step 6 — Costs**: numbing agent impairs the user's own pain-awareness;
hardening slime could immobilize as well as seal; blood reservoir is
perishable.

**Result**:

- **Jaw-gland extract (RARE).** Potency 7 numbing agent. Applied to a
  wound-dressing before binding, it removes the BLEEDING condition for
  one stretch — the wound closes but the patient cannot feel whether it
  holds. HEALING rolls on the patient take a –1 penalty until the
  dressing is changed. A dose rubbed onto a blade's edge makes the first
  strike of combat inflict no immediate damage, but the damage appears in
  full after the stretch ends; hedge healers buy it for midwifery and
  bone-setting and will not say where they source it.

- **Hardening-slime.** A thick clear gel the leech secretes over its egg
  clusters. Applied to rope or leather and left to cure over a Quarter
  Day, it raises that item's resistance to cutting by 1 Armor Rating
  for one full season. A CRAFTER applying it to a mold produces a
  casting material that sets stone-hard in one stretch without fire;
  Stoneborn forges pay in trade for a full jar.

- **Blood reservoir.** A swollen sac from a gorged specimen. Contains
  D3 units of the leech's last host's blood, still warm. An ALCHEMIST
  with a HEALING roll can identify the host species; if the host was
  humanoid, the ALCHEMIST can determine the blood-type and whether the
  host was diseased. Useful to a healer tracing a plague route. Useless
  after one stretch — the blood goes cold and tells nothing.

---

## Structural Template

```markdown
> **RESOURCES**
>
> [Monster's material holds its [property] long after [death/dissolution/
> the fight]. / A slain [monster name]'s [part] and its [part] each have
> distinct uses.] An adventurer with the [TALENT] talent, with a [SKILL]
> roll, [verb] one of the following per ⚔️ rolled, player's choice:
> **material A (RARE)**, **material B**, or **material C**[, plus the
> **intact item** found beside the body, intact regardless of dice rolled].
>
> **Material A (RARE).** [One or two sentences: what the material is.
> Primary mechanical use with duration. Secondary use or narrative fact.
> Faction or ecological consequence.]
>
> **Material B.** [One or two sentences: what the material is. Primary
> mechanical use with duration. Secondary use or optional world-hook.]
>
> **Material C.** [One or two sentences: what the material is. Primary
> mechanical use with duration.]
```

---

## Anti-Pattern: The Harvesting Roll Mismatch

A common failure mode is assigning the wrong skill to the harvest action.

If the material is being drawn from an organ, the roll should be HEALING.
If the material is being cut or shaped, the roll may be CRAFTING.
If the material is being tracked or found in the environment, SURVIVAL or
SCOUTING.

If the ALCHEMIST talent is specified alongside CRAFTING (not HEALING), the
material is something that requires craft more than biology — ground powder,
rendered oil, extracted resin. If HEALING appears with SMITH, the material
is primarily biological even though a smith uses it.

Do not assign LORE as the sole skill for a physical harvest. LORE may
accompany HEALING for supernatural or undead materials (ghost residue,
crawling claw, death magister ash), but LORE alone implies the harvesting
is entirely ritual rather than physical.
