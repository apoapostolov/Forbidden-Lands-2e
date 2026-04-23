# Calibration Examples

These examples show the kind of transformation the OCR workflow should aim for.

## Example 1: Footer Removal

Before:

```md
3

towns & villagers

## INTRODUCTION
```

After:

```md
## Introduction
```

## Example 2: Heading Recovery

Before:

```md
## **TYPE OF GOVERNMENT**
```

After:

```md
#### Type of Government
```

## Example 3: Table Recovery

Before:

```md
D66 WEALTH GEAR 11-16 Too much debt. -2 21-26 In debt. -1
```

After:

```md
| D66   | Wealth         | Gear |
| ----- | -------------- | ---- |
| 11-16 | Too much debt. | -2   |
| 21-26 | In debt.       | -1   |
```

## Example 4: Drop-Cap Repair

Before:

```md
elcome to Spells & Sorcerers...
```

After:

```md
Welcome to Spells & Sorcerers...
```

## Example 5: Safe Restraint

Before:

```md
The arrival of the ailanders and aslenes...
```

Preferred handling:

- preserve if confidence is uncertain
- correct only if the same document repeatedly confirms the intended term

The point is not to look clever. The point is to avoid silent invention.

---

## Example 6: RPG Statblock Attribute Line — Heading to Bold Inline

**Problem:** Extractor promotes the NPC/monster attribute line to an `###` heading.

Before:

```md
### Strength 4, Agility 3, Wits 3, Empathy 2
```

After:

```md
**Strength 4, Agility 3, Wits 3, Empathy 2**
```

**Rule:** A line that reads `Strength N, Agility N, Wits N, Empathy N` is
never a section heading. It is a paragraph attribute summary. Demote it to bold
inline unconditionally.

---

## Example 7: Hybrid Skills Heading — Normalize to Blockquote

**Problem:** Extractor produces a heading+bold hybrid for the NPC skills line,
or strips the blockquote prefix from an already-bold SKILLS line.

Before (heading hybrid):

```md
### **skills:** Melee 3, Crafting 2, Insight 1
```

Before (orphaned, no blockquote):

```md
**SKILLS:** Melee 3, Crafting 2, Insight 1
```

After (both cases):

```md
> **SKILLS:** Melee 3, Crafting 2, Insight 1
```

**Rule:** SKILLS, TALENTS, and ARMOR are blockquoted bold labels in this
format. GEAR is bold without a blockquote. None are headings.

---

## Example 8: MD028 — Consecutive Blockquotes with Blank Line Between

**Problem:** Reconstructed statblocks have a blank line between consecutive
`> **SKILLS:**` and `> **TALENTS:**` lines, triggering MD028.

Before:

```md
> **SKILLS:** Melee 3, Crafting 2

> **TALENTS:** Path of Blood 2
```

After:

```md
> **SKILLS:** Melee 3, Crafting 2
> **TALENTS:** Path of Blood 2
```

**Rule:** Adjacent blockquote lines that are semantically one block (same NPC
statblock) must have no blank line between them. This is both a lint requirement
and a visual rendering requirement.

---

## Example 9: Adventure Site Flat Hierarchy — Numbered Location at Wrong Level

**Problem:** A numbered location entry that is semantically H4 appears at H3
because the extractor used a single level for all headings in the chapter.

Before:

```md
### Background

### Getting Here

### 1. the Wall

The wall surrounds the village...

### 2. the Watchtowers
```

After:

```md
### Background

### Getting Here

### Locations

#### 1. the Wall

The wall surrounds the village...

#### 2. the Watchtowers
```

**Rule:** Numbered list entries inside a named section (Locations, Monsters and
NPCs, Events) are always one level below the section heading. If the section
is `###`, the entries are `####`.

---

## Example 10: Two-Column Splice — Scrambled NPC Block

**Problem:** A two-column PDF layout places NPC A's statblock in the right
column at the same vertical position as NPC B's description in the left column.
The extractor serializes both columns together, mixing prose and stats.

Before (broken — prose under wrong NPC):

```md
#### Midwife Nirvea

She is the village healer...

#### Count Nepola

**Strength 2, Agility 3, Wits 4, Empathy 3**

> **SKILLS:** Healing 3, Lore 2
> **TALENTS:** Path of Healing 2
> **GEAR:** Herbs (3), Knife

Count Nepola was once a powerful noble...

#### The "Village Idiot" Perko

**Strength 4, Agility 2, Wits 2, Empathy 2**
```

After (correct — each NPC's prose before its statblock):

```md
#### Midwife Nirvea

She is the village healer...
**Strength 2, Agility 3, Wits 4, Empathy 3**

> **SKILLS:** Healing 3, Lore 2
> **TALENTS:** Path of Healing 2
> **GEAR:** Herbs (3), Knife

#### Count Nepola

Count Nepola was once a powerful noble...
**Strength 4, Agility 2, Wits 2, Empathy 2**
```

**Rule:** Every NPC entry must have: heading → prose description → attribute
line → blockquoted SKILLS → blockquoted TALENTS → bold GEAR. If the prose is
missing before the statblock, the NPC was likely spliced from the wrong column.
Fix by PDF comparison only.
