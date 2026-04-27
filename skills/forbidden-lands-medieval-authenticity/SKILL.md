---
name: forbidden-lands-medieval-authenticity
description: >
  Comprehensive reference for authentic medieval northern European
  material culture, skills, and daily life, adapted for Forbidden Lands
  2E. Use when writing prose set in the Ravenlands or The Bitter Reach
  that needs physical detail, ambient competence, camp life, combat,
  craft, travel, survival, and social customs. Triggers on any request
  involving medieval realism, historical grounding, pre-industrial skill
  depiction, or sensory texture. Split into generic medieval content
  (applicable across most of the setting) and The Bitter Reach content
  (the Norse-inflected customs, law, religion, and hardship of the
  frozen north).
---

# Forbidden Lands Medieval Authenticity

A knowledge base of real-world skills, material culture, and daily life
for medieval northern European settings and fantasy settings that draw
on them. Everything a fighting man, cook, hunter, crafter, or
camp-follower knew how to do — the granular, physical, unglamorous
knowledge that makes fictional worlds feel inhabited rather than
described.

## When to Load Which Reference

Read only the document(s) relevant to the current scene or task.
Do not load the entire skill into context at once.

| Scene involves… | Load this reference |
| ----------------------------- | ---------------------------------------------------- |
| Camp, fire, shelter | `references/generic/campcraft-and-shelter.md` |
| Weapons, armor, medicine | `references/generic/equipment-health-maintenance.md` |
| Cooking, hunting, foraging | `references/generic/food-and-provisioning.md` |
| Smithing, crafting, chemistry | `references/generic/crafts-and-production.md` |
| Marching, terrain, nav | `references/generic/travel-and-navigation.md` |
| Battle, siege, fortify | `references/generic/warfare-and-tactics.md` |
| Winter, cold, hypothermia | `references/generic/cold-and-winter-survival.md` |
| Stealth, tracking, scout | `references/generic/stealth-and-scouting.md` |
| Fear, exhaustion, morale | `references/generic/morale-fear-leadership.md` |
| Generic repairs and muddle-through labor | `references/generic/trades-generic.md` |
| Trade-learned structural crafts | `references/generic/trades-specialized.md` |
| Artisans, medicine, and fine handwork | `references/generic/trades-specialized-artisans.md` |
| Fine crafts, maritime work, and production trades | `references/generic/trades-specialized-finecrafts.md` |
| Advanced textiles and metalwork | `references/generic/trades-specialized-advanced.md` |
| The Bitter Reach trade, law, customs | `references/the-bitter-reach/social-customs-and-law.md` |
| The Bitter Reach religion and daily life | `references/the-bitter-reach/culture-religion-daily-life.md` |
| Trauma, PTSD, breakdown | `references/generic/psychological-trauma.md` |
| The Bitter Reach trauma concepts | `references/the-bitter-reach/psychological-trauma.md` |
| Sexuality, atrocity, madness | `references/generic/uncomfortable-realities.md` |
| The Bitter Reach taboo topics | `references/the-bitter-reach/uncomfortable-realities.md` |
| Outlawry, banishment, wolves | `references/the-bitter-reach/outlawry.md` |
| Economy, barter, prices | `references/generic/village-economy-and-barter.md` |
| Full document map | `references/INDEX.md` |

For scenes that span domains (e.g., a winter ambush), load the two or
three most relevant files.

## Forbidden Lands Pairing Rule

This skill is not the setting authority.

- Load `forbidden-lands-lore` when the task depends on setting truth,
  place names, factions, kin, Bitter Reach history, or region-specific
  facts.
- Load `forbidden-lands-writing-voice` when drafting or revising
  manuscript-facing prose.

## Rendering Rules

These are the most important rules in the entire skill. They govern
how reference knowledge appears in prose.

### Integration with Prose

Skills do not appear as exposition. They appear as gesture, as
incidental detail, as the ambient competence of people who have done
these things ten thousand times.

**Wrong:** "He struck the fire-steel against the flint, which
produced sparks that landed on the prepared tinder of char-cloth,
which caught an ember that he then transferred to a nest of dried
grass."

**Right:** "He struck a light. The tinder caught on the second try.
He blew the nest to flame and set it in the fire-lay, feeding sticks
over it until it held."

The knowledge is in the background — in the precision of the gesture,
in the absence of fumbling, in the detail that appears only when
something goes wrong. When a man who has lit ten thousand fires does it
again, the prose does not notice. When the tinder is wet and the fire
fails on the twentieth try, the prose notices — because the failure is
the story.

### The Competence Tax

Every skill in this reference has failure modes. The failures are where
the narrative lives:

- The fire that will not catch in the rain.
- The boot that splits on the third day of a forced march.
- The wound that festers despite the healer's best work.
- The mule that develops saddle sores because someone loaded it wrong.
- The bread that breaks a tooth.
- The latrine that was dug uphill and fouls the water.

Competence is the baseline. Failure is the story. The reference defines
what competence looks like so that failure — when it comes — is
specific, physical, and consequential.

## Extension Rules

These rules govern how to add new content to this skill's reference
documents. They exist to prevent prompt overflow when editing large
files with AI assistance.

### Document Size Limits

- **Hard ceiling: 1800 lines per document.** No exceptions.
- **Soft warning: 1500 lines.** When a document reaches 1500 lines,
  plan the next topic split before adding more content.
- If adding content would push a document past 1800 lines, split the
  document by subtopic first, then add.

### Extension Procedure

Never hand-edit a reference document over 1000 lines in-place via an
AI prompt. Instead:

1. **Write a staging document.** Create `_expand_<topic>.md` as a
   sibling file with the new content.
2. **Review the staging document.** Verify accuracy, tone, and format.
3. **Merge with a Python script.** Write a short script that reads both
   files, inserts the new sections at the correct position, and writes
   the merged output.
4. **Lint.** Run `npx -y markdownlint-cli2 --fix <file>` on the result.
5. **Delete staging files.** Remove `_expand_*.md` and the merge script.

### Section Format Requirements

Every `##` section in a reference document must follow this pattern:

- **Bold lead sentence** stating the core principle or physical action.
- **Body paragraphs** with sensory, physical detail — what it looks
  like, sounds like, smells like, feels like.
- **Failure modes last.** What goes wrong and why. This is where the
  narrative value lives.

### Classification Rule

Before writing new content, classify it:

- **Generic:** Universal to pre-industrial northern European life.
  Goes in `references/generic/`.
- **The Bitter Reach:** Specific to the setting's frozen northern
  region, its Norse-inflected culture, religion, law, or customs.
  Goes in `references/the-bitter-reach/`.

If a topic has both generic and The Bitter Reach elements, split the
content accordingly.

### Cross-Linking

Every new `##` section must reference related sections in other
documents via inline cross-references. Use the format:

> See also: `campcraft-and-shelter.md` § Fire

Update the "See Also" header in affected documents when adding
cross-domain content.

### Creating New Documents

When a document must be split or a new topic area is needed:

1. Choose the correct subdirectory (`generic/` or
   `the-bitter-reach/`).
2. Follow the naming convention: `kebab-case-topic.md`.
3. Include the standard header (title, category, description, TOC,
   See Also links).
4. Include the extension-rules HTML comment in the footer.
5. Update `references/INDEX.md` with the new document.
6. Update the "When to Load Which Reference" table in this SKILL.md.
