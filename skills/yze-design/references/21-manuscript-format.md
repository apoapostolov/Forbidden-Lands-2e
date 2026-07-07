<!-- markdownlint-disable MD013 MD024 -->

# Manuscript Format — Engine-Level Formatting Conventions

> **STATUS: FILLED.** The formatting convention for all published YZE text — rulebook chapters, talent descriptions, maneuver lists, adventure text, examples of play. These rules are **engine-level**: they apply to any YZE game (FL, West, or a new genre), because both source books follow them. Game-specific chrome (FL's statblock table layout, West's 8-column NPC table) stays with the game-specific skills; this file owns the conventions that are true everywhere. Load alongside `20-publication-voice.md` (which handles jargon→prose *translation*; this file handles *formatting*).

## Contents

1. Why this file exists
2. The master rule — paragraph format for maneuvers, tables for rolls
3. Action and maneuver names
4. Skill and ability names
5. Action type (SLOW / FAST)
6. Attribute names
7. Game-state terms
8. Symbols
9. Rule-voice principles
10. What stays a table vs what becomes paragraphs
11. Worked examples — table vs paragraph

## 1. Why this file exists

This file codifies the formatting conventions both source books already follow — conventions that were implicit in the source material but not stated as rules in the skill. Without them, an AI writing YZE text produces inconsistent output: sometimes a maneuver is a paragraph, sometimes a table; sometimes a skill name is capitalized, sometimes not; sometimes the action type is stated, sometimes omitted. This file makes the implicit explicit so every piece of published text is consistent.

These are **engine-level** conventions. They apply to Forbidden Lands, Tales of the Old West, and any new YZE game built with this skill. Game-specific layout choices (how FL lays out a statblock table, how West formats its 8-column NPC roster) are owned by the game-specific skills (`forbidden-lands-design`, `western-rpg-design`); this file owns only what is true at the engine level.

## 2. The master rule — paragraph format for maneuvers, tables for rolls

**Maneuvers, actions, and spend options are written as paragraphs, not tables.** A maneuver entry is a bolded ALL-CAPS name followed by a well-written rule-voice paragraph that explains what it does, what to roll, and what happens on success — all in one flowing paragraph, not broken into table columns.

**Tables are reserved for two purposes only:**
1. **Roll tables** — D66, D6, or any table where you roll and read a row (critical-injury tables, encounter tables, mishap tables, event tables, Fallout tables).
2. **Reference tables** — compact lookup references where the reader needs to scan values (the position ladder, the Corruption die ladder, the Standing-shift trigger magnitudes, the spend-cost schedule if it's purely numeric).

If a list of things has a "What it does" column and an "Effect" column, it should be paragraphs. If a list of things has a "D66" column and a "Result" column, it should be a table.

## 3. Action and maneuver names

**ALL-CAPS, bolded.** Every named action, maneuver, reaction, stunt, or move is written in ALL-CAPS and bolded when first introduced and when referenced as a game term.

- **SLASH**, **STAB**, **DODGE**, **PARRY**, **GRAPPLE**, **SHOVE** (FL combat)
- **ALL-OUT ATTACK**, **CALLED STRIKE**, **BLOCK**, **PROTECT ANOTHER** (West combat)
- **SPEECH**, **REVELATION**, **APPEAL TO VALUE**, **QUIP**, **DEFLECT** (Social Combat)
- **DRIVE**, **NAVIGATE**, **SHOOT**, **REPAIR**, **JOCKEY** (Pursuit)
- **SEARCH**, **QUESTION**, **RESEARCH**, **SURVEIL**, **ANALYZE** (Investigation)

This matches both source books: FL bolds and ALL-CAPS its action names (`**SLASH:**`, `**DODGE:**`); West uses Title Case bold for some (`**All-Out Attack:**`) but the engine convention — what is true across both — is ALL-CAPS. Use ALL-CAPS for the generic layer.

**When referencing another action in running text:** also ALL-CAPS. "A failed PUBLIC DECLARATION triggers a Scandal Roll." "You cannot also DRIVE this Round." "The opponent loses their next FAST action."

## 4. Skill and ability names

**ALL-CAPS in running text.** Skill and ability names are always written in ALL-CAPS when they appear in rules text, because they are game terms the reader must recognize.

- "Roll MELEE to attack."
- "Roll INSIGHT opposed against the opponent's MANIPULATION."
- "Roll SURVIVAL, NAVIGATION, or STREETWISE."
- "Roll FIGHTIN' for a block, MOVE for a dodge."

This matches West's convention (FIGHTIN', SHOOTIN', MOVE, LABOR — always ALL-CAPS). FL uses _italics lowercase_ for skills in some contexts (_melee_, _move_), but the engine-level convention — what works for both — is ALL-CAPS. A game may adopt italics-lowercase as its own style choice (FL does), but the generic engine layer uses ALL-CAPS.

**Generic vs game-specific names.** When writing engine-agnostic text, use the generic skill names from `15-glossary-and-taxonomy.md` (MANIPULATION, PERFORMANCE, INSIGHT, MELEE, MARKSMANSHIP, etc.). When writing for a specific game, use that game's names (FIGHTIN', SHOOTIN', PRESENCE, PERFORMIN').

## 5. Action type (SLOW / FAST)

**Stated inline in the paragraph, ALL-CAPS, never in a table column.** Every maneuver entry states whether it is a SLOW action or a FAST action as part of the first sentence.

- "**SLASH** is a SLOW action that..."
- "**QUIP** is a FAST action — a quick jab..."
- "**DEFLECT** is a reaction used when an attack lands on you."

When referencing action types in running text, also ALL-CAPS: "the opponent loses their next FAST action," "you cannot also take a SLOW action this Round," "reactions cost your FAST action."

This matches both source books, which state the action type inline ("This is a FAST action," "a SLOW action") rather than in a separate column.

## 6. Attribute names

**ALL-CAPS in running text.** Attribute names are game terms.

- "Roll STRENGTH plus MELEE."
- "Damage reduces your GRIT."
- "Roll WITS or EMPATHY."

When writing engine-agnostic text, use the generic attribute names (STRENGTH, AGILITY, WITS, EMPATHY). When writing for a specific game, use that game's names (GRIT, QUICK, CUNNING, DOCITY for West).

## 7. Game-state terms

**Capitalized when they are named game states.** A term that refers to a specific mechanical condition is capitalized, because it is a defined game state, not a descriptive word.

- **Broken** — the state when an attribute reaches 0.
- **Shaken** — West's state when Faith reaches 0.
- **Prone**, **Stunned**, **Exhausted**, **Freezing** — named conditions.
- **Dark Secret**, **Big Dream**, **Pardner** — named character elements.

Do not capitalize generic descriptive words: "the character is damaged," "you lose standing." Capitalize only when the word IS the rule: "the character is Broken," "you gain 1 Willpower."

## 8. Symbols

Use the engine's symbols consistently, matching FL's convention:

- **⚔** — success (a six rolled on any die).
- **💀** — bane (a one rolled on a Base or Gear die, FL).
- **🩸** — damage (one point of attribute damage).

Write "1⚔" for "one success," "2💀" for "two banes," "1🩸" for "one damage." In running text: "roll three ⚔ to succeed," "each 💀 deals 1🩸 to the attribute."

West does not use 💀 (it uses the Trouble system instead), so 💀 appears only in FL-style or generic-bane contexts. When writing for a West-style game, use "1s" and "Trouble" instead.

## 9. Rule-voice principles

Published YZE rules text follows these voice principles (drawn from both source books and the sibling writing skills):

1. **Second person.** Address the reader directly: "you roll," "you take damage," "you may push the roll." The reader is the player or GM. Never third-person ("the character rolls") unless describing an NPC.

2. **Declarative.** State the rule, don't explain the design. "When you push a roll, each 💀 on a Base Die deals 1🩸 to the attribute you used." Not: "the push-cost model extracts a bane-self-harm cost to create attritional pressure."

3. **Consequence-first.** Lead with what happens, then the condition. "You take 1🩸 to Strength for every 💀 you roll on a Base Die when you push." Not: "the bane activation sequence triggers upon the push decision."

4. **One paragraph, one rule.** Each maneuver, each rule, each procedure gets its own paragraph. Do not nest multiple rules in a single block. If a paragraph has more than one rule, split it.

5. **No design commentary.** Never explain *why* the rule exists in the published text. That belongs in design notes, not in the manuscript the player reads. (The *why* lives in this skill's `references/` files; the published text states only the *what* and the *how*.)

6. **Plain English.** Short sentences. Active voice. Concrete nouns. No academic phrasing, no AI transition padding (see `20-publication-voice.md` §5, the blacklist).

## 10. What stays a table vs what becomes paragraphs

**The decision rule:**

| If the content is... | Use... | Because... |
| --- | --- | --- |
| A list of maneuvers/actions a player can choose from | **Paragraphs** with bolded ALL-CAPS names | The reader needs to understand each option's full procedure, not scan a grid |
| A list of spend options (what a resource buys) | **Paragraphs** with bolded ALL-CAPS names | Same — each option is a mini-rule, not a data point |
| A D66 / D6 roll table (roll and read a row) | **Table** | The reader is scanning for their rolled result; a table is the correct scan format |
| A reference lookup (die ladder, position ladder, magnitude scale) | **Table** | The reader is looking up a value; a table is the correct lookup format |
| A cost schedule (XP costs, training times) | **Table** | The reader is looking up a number; a table is the correct format |
| A set of modifiers (difficulty ladder, environmental modifiers) | **Table or paragraphs** — use paragraphs if each modifier needs explanation; use a table if each is a simple numeric pair | Context-dependent |

**The test:** does the reader need to *understand a procedure* (paragraph) or *look up a value* (table)? If procedure → paragraphs. If value → table.

## 11. Worked examples — table vs paragraph

### Wrong (table for maneuvers)

| Action | Type | Roll | Effect |
| --- | --- | --- | --- |
| **SLASH** | Slow | MELEE | Deals Weapon Damage. Can be parried or dodged. |
| **STAB** | Slow | MELEE | Deals Weapon Damage. Higher crit chance. |
| **DODGE** | Fast | MOVE | Cancel 1⚔ per ⚔ rolled. |

### Right (paragraphs for maneuvers)

**SLASH** is a SLOW action. Roll MELEE to attack with an edged weapon. If you succeed, you deal Weapon Damage to the opponent. A SLASH can be PARRIED or DODGED.

**STAB** is a SLOW action. Roll MELEE to attack with a pointed weapon. If you succeed, you deal Weapon Damage. A STAB has a lower Crit Rating than a SLASH — it is more likely to inflict a critical injury. A STAB can be PARRIED or DODGED.

**DODGE** is a FAST action — a reaction used when an attack lands on you. Roll MOVE. Each ⚔ you roll cancels one of the attacker's ⚔, reducing the damage. You cannot DODGE if you have already spent both your actions this Round.

### Right (table for a roll result — this IS a table)

| D66 | Result | Effect |
| --- | --- | --- |
| 11–14 | Lost composure | −1 Influence with the audience. |
| 15–22 | Sharp retort fled | Opponent's point stands uncontested. |
| 65 | Breakdown | −3 Influence; a Dark Secret may be exposed. |
| 66 | Social destruction | Influence drops to −3; finished in this constituency. |

The difference: the roll table is a lookup — the reader rolled a 15 and needs to find "Sharp retort fled." The maneuver list is a procedure — the reader needs to understand what SLASH does, what to roll, what happens, and how it interacts with defense. A table cannot convey that; a paragraph can.
