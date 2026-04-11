# Life Path Generator — Coverage Audit and Open Proposals

**Scope.** This audit compares the life path generator (`proposal-cycle-based-life-path-generator-final.md`) against the standard character creation method in Chapter 02 (`corebook/02-your-adventurer.md`) to identify mechanical elements that are missing, underspecified, or handled differently enough to cause problems at the table.

**Method.** Every numbered step in the standard method was cross-referenced against the life generator's output. Every table, rule, and worked example was checked for internal consistency. The simulation (`scripts/lifepath_simulation.py`) was consulted for statistical validation where relevant.

---

## What the Generator Already Covers

These elements are present and require no further work:

| Element                                   | How Covered                                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------------------- |
| Kin selection                             | D66 table with all 10 kin                                                             |
| Home region                               | Kin-based D6 tables                                                                   |
| Childhood foundation                      | 10 tables (one per kin), 6 entries each, with skills, favored attributes, hooks       |
| Age bracket (attributes, talents, cycles) | Young/Adult/Old table matching standard method budgets                                |
| Skill marks and final ranks               | Mark→rank conversion table (1/2/3/5/7)                                                |
| Turn resolution                           | Turn test, success/failure, event/mishap tables — all 12 paths × 7 tables = 84 tables |
| Wear and consequences                     | Consecutive-failure tracking, 3-tier consequence system                               |
| Advancement and departure                 | End-of-cycle roll, forced-life table, narrowing tax                                   |
| Mustering out                             | All 12 paths have 6-entry mustering-out tables                                        |
| Unfinished business                       | Short Errand / Life Quest system tied to Wear                                         |
| Choose profession                         | Qualification rules, profession talent seed                                           |
| Pride and Dark Secret                     | Tagged events (20 Pride / 16 Dark Secret across all tables) plus profession fallback  |
| Resource dice                             | "Take Resource Dice from your profession entry as normal"                             |
| Languages, Willpower, appearance          | "Follow the rest of this chapter without change"                                      |
| Relationships                             | "Determine Pride, Dark Secret, and relationships" defers to standard step             |
| How Did You Meet?                         | D66 table, 18 entries, complete coverage                                              |

---

## Issue 1 — No Gear Floor

**Severity: High.**

The standard method guarantees every character a weapon, trade goods, and silver. A Fighter always starts with a one-handed weapon, studded leather, one trade good, and D6 silver. A Druid always gets a staff or knife, one trade good, and D6 silver.

The life generator replaces this with: "Use the gear and silver from the life generator instead of adding the profession's ordinary starting gear and silver on top." But gear from the generator is entirely random. A character's only guaranteed gear source is one mustering-out roll (D6). Many results yield no weapon, no armor, and no silver — only contacts, rivals, scars, or rumors.

**Edge case.** A Fighter who rolls through events that grant only skills and contacts, then musters out with result 4 ("One rival who remembers the same battle differently") ends play with zero equipment.

**Proposal.** Add a gear-floor rule after the mustering-out step:

> **Starting Gear Floor.** After mustering out, compare what the life generator gave you against the minimum starting gear for your chosen profession. If the generator did not provide a weapon, take the cheapest weapon listed in your profession's starting gear. If it did not provide armor (for professions that start with armor), take your profession's starting armor. Every character starts with a waterskin and a travel backpack regardless of rolls.

This preserves the life generator's fiction-first approach — you keep everything the dice gave you — while ensuring no character walks into session one unarmed and unequipped.

---

## Issue 2 — No Guaranteed Silver

**Severity: Moderate.**

Standard method silver by profession: D6 (Druid, Fighter, Hunter, Rider), D8 (Minstrel, Sorcerer), D10 (Rogue), 3D6 (Peddler). Every character gets at least one die of silver.

Life generator silver comes from event rolls and mustering-out only. Some paths' mustering-out tables include silver on only 1–2 of 6 results. A character could finish the generator with zero silver.

**Proposal.** Add a minimum silver clause to the gear-floor rule:

> If the life generator did not grant you any silver, roll your profession's starting silver die once. This is the last coin from the last job.

---

## Issue 3 — Reputation and Standing Not Initialized

**Severity: Moderate.**

Standard method (Chapter 02, lines 1142–1173): every character starts with Reputation 6 and Standing +1 in their home settlement. The life generator creates a home region (lines 69–85) but never assigns Reputation or Standing values.

Some events modify Standing (e.g., Sorcerer Fourth Turn result 6: "+1 Standing in one settlement"; Minstrel Mishap result 2: "Lower Standing by 1"). These modifiers assume a base value exists but the generator never sets one.

**Proposal.** Add one sentence to the Choose Profession section, after the profession talent seed paragraph:

> Your home region determines your home settlement. You start with Reputation 6 and Standing +1 there, modified by any Standing changes from the life generator.

---

## Issue 4 — Favored Attributes Are Not Key Attributes

**Severity: Low. Original proposal withdrawn.**

Every childhood foundation lists "favored attributes" (e.g., Squire: Strength and Empathy favored). The standard method has a separate cap rule: a kin key attribute can be raised to 5, a profession key attribute can be raised to 5, and if both overlap the cap is 6. The original audit proposed making favored attributes serve as kin key attributes for cap purposes. That proposal is wrong. Analysis:

1. **Favored attributes do not reliably include the kin key attribute.** Across 60 childhood foundations, the kin key attribute appears in only 35 of them. Wolfkin (key: Agility) include it in only 2 of 6 foundations — 67% of Wolfkin characters would lose their kin key attribute under the proposal. Half-Elf, Elf, and Orc each miss in 3 of 6.

2. **Two favored attributes as key attributes would be overpowered.** Each foundation lists two. The standard method gives one. Granting two key attributes would let characters raise two attributes to 5, or one to 6 with profession overlap — strictly stronger than the standard method allows.

3. **The existing rules already work.** The Choose Profession section says "Spend attribute points by age as normal." The standard method's attribute cap references "the key attribute for your kin," which is defined in the kin entry in Chapter 02 and has not been overridden. No new rule is needed.

**Revised proposal.** Add one clarifying sentence to the childhood foundation preamble to prevent confusion:

> Favored attributes are narrative guidance — they suggest where childhood pushed hardest. They do not replace your kin's key attribute for the attribute point cap. Use the key attribute listed in your kin entry as normal.

---

## Issue 5 — Sorcerer and Druid Spell Selection

**Severity: Moderate.**

The standard method's Sorcerer and Druid entries specify how many starting spells or paths a character begins with. The life generator's event tables reference magical knowledge (Sorcerer Second Turn: "Grimoire Fragment"; Druid Fourth Turn: "Plague Work" involving Healing) but never specify a starting spell count or selection rule.

The Choose Profession section defers to "the profession rules already in this chapter" for the profession talent, but spell selection is typically tied to profession talents (e.g., a Sorcerer with Path of Blood at Rank 1 knows specific spells). The profession talent seed grants 1 mark toward a profession talent, which for Sorcerers and Druids would be a magical path — but the rules don't explicitly confirm this grants access to the path's spells.

**Proposal.** No new rule needed if the existing profession rules in Chapter 02 already state that "having Rank 1 in a magical path talent grants access to that path's spells." Confirm that the cross-reference is sufficient. If Chapter 02 does not make this connection explicit, add:

> Sorcerers and Druids who receive marks in a magical path talent (from the profession talent seed or from advancement benefits) begin play with access to the spells of that path at the granted rank level, following the normal rules for magical paths in Chapter 07.

---

## Issue 6 — Rider Mount Guarantee

**Severity: Low.**

The standard method states that Riders always start with a riding horse. The life generator's Rider event tables include mount-related fiction (Third Turn: "You broke a beast no one else wanted"; Mustering-Out result 5: "A pack animal or riding beast"). But gaining a mount is not guaranteed — it depends on specific rolls.

The Choose Profession section says "Use the gear and silver from the life generator instead of adding the profession's ordinary starting gear and silver on top." Strictly read, this means a Rider who never rolled a mount-related event starts without a horse.

**Proposal.** The gear-floor rule from Issue 1 should cover this if written to include profession-defining items:

> If your profession's standard starting gear includes a mount (Rider) or instrument (Minstrel), and the life generator did not provide one, you start with that item. The road left you with at least this much.

---

## Issue 7 — Event-Granted Gear Specificity

**Severity: Low.**

Several events grant gear in narrative terms: "a serviceable weapon," "a mount," "herbs," "ritual tools." The standard method lists specific items with defined game stats (e.g., "one-handed weapon of your choice," "studded leather armor"). Narrative gear descriptions leave the GM and player to negotiate at the table.

**Proposal.** This is a feature, not a bug, as long as the gear-floor rule ensures minimum viability. The narrative descriptions create richer fiction than "pick from list." No rule change needed, but a sidebar or design note could acknowledge the intent:

> Gear granted by events and mustering-out should be interpreted as specific items during play. "A serviceable weapon" means a real weapon from the gear chapter — the player and GM agree on what fits the fiction. When in doubt, pick the simplest version.

---

## Issue 8 — Talent Mark Cap at Character Creation

**Severity: Low.**

The profession talent seed grants 1 mark toward a profession talent. Advancement benefits may grant additional marks in the same talent (up to 3 marks possible if a character stayed in the same profession path for 3+ cycles and rolled talent results each time). With the new mark→rank table, 3 marks = Rank 3.

The standard method caps starting profession talent at Rank 1 (or Rank 2 if a general talent slot is traded). A life-generator character who accumulated 3+ marks in a profession talent through seed + advancement could theoretically start with that talent at Rank 3 — exceeding the standard method's ceiling.

The simulation shows this is rare (mean talents granted: 1.37–1.89 across all ages, with max talent rank mean ~1.14–1.19), but it is possible.

**Proposal.** Two options:

**(A) Cap it.** Add: "No talent gained through the life generator may exceed Rank 2 at the end of character creation. Excess marks are lost." This preserves exact parity with standard method.

**(B) Allow it.** Accept that the life generator's randomness occasionally produces a Rank 3 talent as a rare reward for sustained focus. The tradeoff: the character paid for that concentration with narrowing taxes and reduced skill breadth. This is the design-consistent option — the generator already allows R4–R5 skills that the standard method cannot produce, so allowing rare R3 talents is thematically parallel.

**Recommendation:** Option B. The statistical rarity (under 5% of characters) and the narrative cost (staying in one path long enough to accumulate 3 talent marks) make this an earned outlier, not a balance exploit.

---

## Issue 9 — Waterskin and Backpack Assumption

**Severity: Trivial.**

Standard method (line 744 of Chapter 02): "You are assumed to have a waterskin and a travel backpack unless the GM says otherwise." The life generator never states this assumption.

**Proposal.** Fold into the gear-floor rule: "Every character starts with a waterskin and a travel backpack regardless of rolls."

---

## Issue 10 — Childhood Foundation Hooks and Starting Contacts

**Severity: Informational.**

Every childhood foundation includes a narrative hook (e.g., "One former master still remembers his service," "Your family owes a debt to a healer"). These function as starter contacts, enemies, or debts. The turn events then add more.

The standard method does not explicitly track contacts and enemies as a numbered resource — it treats them as fiction. The life generator creates a richer web (the simulation shows Adults average 1.77 contacts, 1.25 rivals, 0.79 enemies) but has no mechanic for using contacts during play beyond "the GM incorporates them."

**Proposal.** No rule change needed. This is a strength of the generator. A brief design note in the final chapter text could frame it:

> The contacts, rivals, enemies, rumors, and scars accumulated during the life generator are not points to spend. They are the world's grip on your character. The GM should treat them as live threads — people who might appear, debts that might come due, places that might matter. The more fiction the generator built, the more the world already knows your name.

---

## Summary Table

| #   | Issue                               | Severity      | Action                                                 |
| --- | ----------------------------------- | ------------- | ------------------------------------------------------ |
| 1   | No gear floor                       | High          | Add gear-floor rule                                    |
| 2   | No guaranteed silver                | Moderate      | Add minimum silver clause                              |
| 3   | Reputation/Standing not initialized | Moderate      | Add one sentence to Choose Profession                  |
| 4   | Favored attributes ≠ key attributes | Low           | Clarifying sentence only (original proposal withdrawn) |
| 5   | Sorcerer/Druid spell access         | Moderate      | Confirm cross-reference or add clause                  |
| 6   | Rider mount / Minstrel instrument   | Low           | Fold into gear-floor rule                              |
| 7   | Event gear specificity              | Low           | Design note only                                       |
| 8   | Talent mark cap                     | Low           | Allow it (Option B)                                    |
| 9   | Waterskin and backpack              | Trivial       | Fold into gear-floor rule                              |
| 10  | Contact/enemy fiction framing       | Informational | Design note only                                       |
