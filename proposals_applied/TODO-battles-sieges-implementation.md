<!-- markdownlint-disable MD013 -->

# TODO - Battles & Sieges Proposals Implementation

This file is optimized for a strong planner plus cheaper executor workflow.
Each prompt is documented well enough that a capable, lower-cost execution model
can pick up any prompt without hidden context.

## Current Focus

- Integrate all 12 accepted proposal sections (P5.1–P5.12) from the overhaul
  analysis into `02-gamemasters-guide/12-battles-and-sieges.md`, then run a full
  game balance audit.
- Canonical manuscript: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposals source: `proposals/proposal-battles-and-sieges-overhaul.md`

## Scope And Boundaries

- This pass owns: all 12 rule insertions from `## Part 5: Exact Proposed Rules`
  in the proposals file, the balance audit, and the chapter changelog entry.
- This pass explicitly does not own: other chapters, the Book of Beasts bestiary,
  the Player's Handbook skills chapter, or lore text outside chapter 12.

## Status

**All 12 prompts completed.** Balance audit written to
`proposals/audit-battles-sieges-post-integration.md`.

Chapter markdownlint: **0 errors** as of completion.

Two flags from the audit require monitoring but no immediate rule change:

- **P5.6 Battle Magic:** Two clarifications already applied (overcharge counts
  toward effective Power Level; area spells split PL across targets).
- **P5.12 Veterans:** Watch in extended campaign play. D12 tier reachable only
  after 12+ survived battles — rare in most campaigns. No cap change recommended now.

---

## Completed Prompt Queue

### [x] Prompt 1 — Terrain and High Ground

Insert the `### Terrain` subsection from P5.1 into chapter 12 under
`## Special Combat Conditions`, after the existing `### Commander Movement`
section.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.1 in `proposals/proposal-battles-and-sieges-overhaul.md`,
  lines 133–154
- The `## Special Combat Conditions` section currently ends at
  `### Commander Movement`. Insert Terrain as the next subsection.
- Skills to load before writing: `skills/forbidden-lands-writing/SKILL.md`
  and `skills/forbidden-lands-design/SKILL.md`

Inputs:

- Read `02-gamemasters-guide/12-battles-and-sieges.md` — find the exact text
  immediately after `### Commander Movement` to locate the insertion anchor.
- Read P5.1 proposal text in full from the proposals file.

Outputs:

- A new `### Terrain` subsection inserted in the chapter after
  `### Commander Movement`, matching the FL2E voice standard.

Validation:

- Confirm the new subsection is present in the chapter file.
- Run `npx -y markdownlint-cli2 --fix 02-gamemasters-guide/12-battles-and-sieges.md`
- Confirm the five terrain types (High Ground, Muddy, Forest, River, Prepared)
  are present with their exact mechanical effects.

Delegation notes:

- Do not cut any content. Rewrite for FL2E voice only.
- Do not add any terrain types or mechanics beyond P5.1.
- The Terrain section must not use the word "Chivalry" — use "Cavalry".
- No flowery language. Rules text should be brief, specific, physical.

---

### [x] Prompt 2 — Weather and Night Attack

Insert the `### Weather` subsection from P5.2 and the `### Night Attack`
subsection from P5.3 into chapter 12 immediately after `### Terrain`.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal sections: P5.2 (lines 155–177) and P5.3 (lines 178–197) in the
  proposals file.
- Insert both immediately after the Terrain subsection added in Prompt 1.
- Skills to load before writing: `skills/forbidden-lands-writing/SKILL.md`

Inputs:

- Read the chapter to confirm where `### Terrain` ends after Prompt 1 completes.
- Read P5.2 and P5.3 proposal text in full.

Outputs:

- `### Weather` subsection with D6 roll table and six conditions.
- `### Night Attack` subsection with sentry, torchlight, and SCOUTING roll rules.
- Both inserted in chapter immediately after `### Terrain`.

Validation:

- Confirm both subsections are present.
- Run markdownlint.
- Confirm the Weather table has 6 entries (1–6).
- Confirm Night Attack references sentries, torchlight, and the SCOUTING roll.

Delegation notes:

- Weather roll is at battle start, not daily.
- Night Attack SCOUTING roll difficulty is Commanding.
- Failure on the SCOUTING roll loses 1D3 base dice — this is an exact rule, do
  not soften it.

---

### [x] Prompt 3 — Champion's Duel

Insert the `### The Challenge` subsection from P5.4 into chapter 12 in
`### The General's Speech` section or immediately after it, before
`### Battle Turns`.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.4 (lines 198–215) in the proposals file.
- The Challenge is a pre-battle option. It belongs between The General's Speech
  and Battle Turns.
- Skills to load before writing: `skills/forbidden-lands-writing/SKILL.md`

Inputs:

- Read the chapter's `### The General's Speech` and `### Battle Turns` sections
  to find the exact insertion anchor.
- Read P5.4 proposal text in full.

Outputs:

- A new `### The Challenge` subsection inserted after The General's Speech.

Validation:

- Confirm the subsection is present.
- Run markdownlint.
- Confirm the "refused challenge" morale penalty is included.
- Confirm the PC champion alternate skill format rule is included.

Delegation notes:

- The morale stakes apply regardless of duel format (MELEE or alternate skill).
- Do not add a "skip the battle" outcome — the battle still occurs. This is
  stated explicitly in P5.4 and must not be changed.

---

### [x] Prompt 4 — Feigned Retreat

Insert the `### Feigned Retreat` subsection from P5.5 into chapter 12 under
`## Special Combat Conditions`, after `### Commander Movement`.

Note: If Prompts 1–3 have already added subsections after `### Commander
Movement`, place Feigned Retreat at the end of `## Special Combat Conditions`,
after Weather and Night Attack.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.5 (lines 216–231) in the proposals file.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`

Inputs:

- Read the chapter's `## Special Combat Conditions` section to find current
  end-of-section anchor.
- Read P5.5 proposal text in full.

Outputs:

- `### Feigned Retreat` subsection at end of `## Special Combat Conditions`.

Validation:

- Confirm the subsection is present.
- Run markdownlint.
- Confirm the Opposed roll (PERFORMANCE vs INSIGHT) is included.
- Confirm the "once per troop per battle" limit is stated.
- Confirm the pursuit die result is a free advantage D8.

Delegation notes:

- Feigned retreat is only for cavalry and skirmishers by default.
- Infantry exception requires GM discretion — state this exactly as written.
- If the retreat becomes genuine, the troop makes a morale roll that turn.

---

### [x] Prompt 5 — Battle Magic

Insert the `### Mages and Sorcerers in Battle` subsection from P5.6 into
chapter 12 under `## Battle Events`, immediately after `### The Important
Character Die` and before `### Commanders and Important Characters`.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.6 (lines 232–251) in the proposals file.
- Magic rules reference: `01-corebook/07-magic.md` — read the spell paths
  section before writing to confirm that the skill-substitution rules
  (INSIGHT for Mentalism, MANIPULATION for illusions, etc.) are accurate
  against the existing magic paths.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`,
  `skills/forbidden-lands-design/SKILL.md`

Inputs:

- Read chapter's Battle Events section to find the anchor after
  `### The Important Character Die`.
- Read P5.6 proposal text in full.
- Read `01-corebook/07-magic.md` — confirm which skills are used by which
  magic paths in the core rules, and adjust the Battle Magic skill list to
  match exactly. Do not invent skill pairings not supported by the magic rules.

Outputs:

- `### Mages and Sorcerers in Battle` subsection inserted in chapter.
- Skill pairings in the subsection verified against chapter 7.

Validation:

- Confirm the "sacrifice advantage die roll" mechanism is clear.
- Confirm the damage conversion (2 spell damage = 1 troop damage) is stated.
- Confirm the conditions-as-terrain rule is stated.
- Confirm the Broken mage clause is included.
- Run markdownlint.

Delegation notes:

- The mage replaces their advantage die roll with dice equal to the troop's
  remaining base dice — not the troop's advantage dice. This is exact. Do not
  change the dice source.
- Spell effects apply to one adjacent troop section only.

---

### [x] Prompt 6 — Aerial Units

Insert the `### Aerial Units` subsection from P5.7 into chapter 12 as a new
subsection in `## Special Combat Conditions` or in a new `## Notes on Unit
Types` section if one exists. Place it after the existing unit type notes.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.7 (lines 252–271) in the proposals file.
- Read the chapter to find the best placement — there may be a `## Unit Types`
  or similar section from the example units block that this can follow.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`,
  `skills/forbidden-lands-design/SKILL.md`

Inputs:

- Read chapter from line 580 to end to find best insertion point.
- Read P5.7 proposal text in full.

Outputs:

- `### Aerial Units` subsection in chapter with the four rules:
  Cannot Be Engaged, Charge from Above, Size Advantage Die, Vulnerability.

Validation:

- Confirm all four aerial unit rules are present.
- Confirm the "double damage from ranged critical successes" rule is exact:
  3+ successes on ranged attack = 2 damage instead of 1.
- Run markdownlint.

Delegation notes:

- Aerial units use the cavalry troop type with modifications.
- They are immune to polearm bonus against cavalry when charging.
- The vulnerability rule is precise: it triggers on 3 or more successes from
  a ranged attack, not from any critical hit in the personal combat sense.

---

### [x] Prompt 7 — Undead and Demonic Armies

Insert the `### Undead and Demonic Troops` subsection from P5.8 immediately
after `### Aerial Units` in the chapter.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.8 (lines 272–291) in the proposals file.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`,
  `skills/forbidden-lands-design/SKILL.md`

Inputs:

- Read chapter to confirm placement after the Aerial Units subsection.
- Read P5.8 proposal text in full.
- Note: The chapter uses "Misgrown" not "demon/demorph" — for consistency,
  confirm the heading uses "Undead and Misgrown Armies" rather than
  "Undead and Demonic Armies" if the chapter has changed the terminology
  systematically. If unsure, check `02-gamemasters-guide/12-battles-and-sieges.md`
  for how demonic forces are referred to.

Outputs:

- `### Undead and Demonic Troops` subsection (or `### Undead and Misgrown Troops`
  if terminology has been unified) with four rules:
  Morale Immunity, No Supplies, Commander Dependency, Demonic fear drain.

Validation:

- Confirm morale immunity is absolute for undead.
- Confirm commander dependency collapse (half base dice, then 1 per turn).
- Confirm demonic fear drain is -1 morale per turn for 3 turns.
- Run markdownlint.

Delegation notes:

- Undead do not rout — this is a hard rule, not a tendency.
- The "Commander Dependency" rule specifically applies only to undead, not to
  demonic troops. Demonic troops do not collapse but do not coordinate well.
- Do not conflate undead and demonic rules into one block.

---

### [x] Prompt 8 — Pursuit of Routing Troops

Insert the `### Pursuit` subsection from P5.9 into chapter 12 under
`## The Battle Sequence`, after `### Troop Regrouping`.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.9 (lines 292–309) in the proposals file.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`

Inputs:

- Read chapter's `### Troop Regrouping` section to find the insertion anchor
  (Pursuit follows immediately after regrouping).
- Read P5.9 proposal text in full.

Outputs:

- `### Pursuit` subsection inserted after `### Troop Regrouping`.

Validation:

- Confirm only cavalry can pursue.
- Confirm the cost of pursuit (cannot participate in main battle roll that turn).
- Confirm the pursuit roll is full dice against the routing troop's remaining
  base dice.
- Run markdownlint.

Delegation notes:

- Infantry cannot effectively pursue. State this explicitly.
- The pursuit is a conscious risk — the chapter narrative voice should
  acknowledge the trade-off (winning the flank vs. losing the center).
- The routing troop's soldiers removed by pursuit are removed permanently, not
  just demoralized.

---

### [x] Prompt 9 — Aftermath: Ransom and Post-Battle

Insert the full `## Aftermath` section from P5.10 into chapter 12 as a new
top-level section before `## New Talents` or at the end of the main rules
content.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.10 (lines 310–351) in the proposals file.
- The `## New Talents` section is currently near the end of the chapter before
  the example units. Insert `## Aftermath` before `## New Talents`.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`

Inputs:

- Read the chapter from line 450 to the end to find the current location of
  `## New Talents` and the exact insertion anchor.
- Read P5.10 proposal text in full.

Outputs:

- Full `## Aftermath` section with three subsections:
  `### Prisoners and Ransom`, `### Stripping the Dead`, `### Wounded`.

Validation:

- Confirm the ransom value table is present with 5 tiers.
- Confirm the stripping-the-dead mechanic uses the D6 roll per 10 base dice.
- Confirm the wounded Important Character rule (D6 roll, 5+ = survived broken).
- Run markdownlint.

Delegation notes:

- "PC" ransom is explicitly "Negotiated by the table" — do not assign a copper
  value to it.
- The 1-quarter-day stripping cost is an exact rule — do not simplify to
  "some time".
- The wounded roll applies only to Important Characters, not to all soldiers.

---

### [x] Prompt 10 — Expanded Death to Cowards

Replace the existing `Death to Cowards` paragraph in `### Morale Points` with
the expanded version from P5.11.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.11 (lines 352–371) in the proposals file.
- The current `Death to Cowards` is a bold paragraph inside `### Morale Points`,
  not its own subsection. The new version promotes it to `#### Death to Cowards`
  inside `### Morale Points`.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`,
  `skills/forbidden-lands-design/SKILL.md`

Inputs:

- Read the chapter's `### Morale Points` section in full to find the exact
  current `**Death to Cowards.**` paragraph text for the replacement anchor.
- Read P5.11 proposal text in full.

Outputs:

- Old `**Death to Cowards.**` paragraph replaced with the new `#### Death to
  Cowards` subsection containing: execution mechanics, army morale check, and
  post-battle morale check.

Validation:

- Confirm the execution selects up to 1D6 soldiers.
- Confirm all other troops make a morale check (success = +1, fail = -1).
- Confirm the post-battle morale check rule is present for the next session.
- Confirm the existing narrative closing line (the "borrowed loyalty" sentence)
  is present.
- Run markdownlint.

Delegation notes:

- The old paragraph is a flat block. The new version is a subsection. Adjust
  heading level to match the document's hierarchy without breaking parent
  sections.
- The "borrowed loyalty" closing sentence is new narrative content added by the
  proposal. It must be preserved exactly.

---

### [x] Prompt 11 — Veterans Tier

Add the Veterans advantage tier to chapter 12: a new row in the Advantage Dice
table and a new `### Veterans` subsection in the unit rules.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposal section: P5.12 (lines 372–391) in the proposals file.
- New table row: `| Veterans (survived 3+ battles intact) | +2 |` — add to
  the Advantage Dice table in `### Advantage Dice`.
- New subsection: `### Veterans` placed after the advantage dice table
  explanations.
- Skills to load: `skills/forbidden-lands-writing/SKILL.md`,
  `skills/forbidden-lands-design/SKILL.md`

Inputs:

- Read the chapter's `### Advantage Dice` section to find the exact table
  anchor and current list of explanatory paragraphs after it.
- Read P5.12 proposal text in full.

Outputs:

- New table row in Advantage Dice table for Veterans.
- New `### Veterans` subsection after advantage dice explanations.
- Three Veterans rules: die type upgrade, morale check waiver, commander-loss
  Formidable check.

Validation:

- Confirm the new row is in the advantage dice table.
- Confirm the die type upgrade path (D6→D8→D10→D12) is explicit.
- Confirm the first morale check waiver per engagement is stated.
- Confirm Veterans cannot be recruited — only earned.
- Run markdownlint.

Delegation notes:

- Veterans die type upgrade stacks with Well-trained (+1 advantage die).
  These are separate mechanics: die type vs. die count.
- The Formidable commander-loss check applies only when the commander is
  killed or captured — not when they move sections.
- The P5.12 proposal adds Veterans as +2 in the table. Confirm this matches
  the three-benefit description before committing.

---

### [x] Prompt 12 — Game Balance Audit

After all 11 proposal integrations are complete, run a comprehensive game
balance audit of `02-gamemasters-guide/12-battles-and-sieges.md` against the
existing FL2E rules system.

Context:

- Canonical chapter: `02-gamemasters-guide/12-battles-and-sieges.md`
- Full FL2E corebook: `01-corebook/` (especially chapters 03, 04, 05, 07)
- Skills to load: `skills/forbidden-lands-design/SKILL.md`,
  `skills/rpg-balance-analysis/SKILL.md`

Inputs:

- Read the full chapter (post all integrations).
- Read `01-corebook/05-combat-and-damage.md` — confirm battle mechanics
  do not create contradictions with personal combat rules.
- Read `01-corebook/07-magic.md` — confirm Battle Magic rules are consistent
  with magic paths and dice mechanics.
- Read `01-corebook/04-talents.md` — confirm new Commander, General, Engineer
  talents do not overlap poorly with existing talent trees.
- Read `proposals/proposal-battles-and-sieges-overhaul.md` — review Parts 1–4
  (balance analysis, authenticity gaps, simplicity critique, missing fantasy
  tropes) to check whether the 11 integrations have addressed the identified
  gaps.

Outputs:

Write a balance audit report as `proposals/audit-battles-sieges-post-integration.md` containing:

1. **Dominant strategies**: Are any unit types, advantages, or tactics clearly
   superior to all alternatives? List them with dice math.
2. **Underperforming options**: Which options are never worth taking? Why?
3. **Rule interaction conflicts**: Do any new rules (Aerial Units, Battle Magic,
   Veterans, Night Attack) interact in ways that create unintended power spikes?
4. **Cost calibration**: Are unit costs (per soldier, daily copper) proportional
   to their battlefield value? Show the math.
5. **Morale system**: Does Death to Cowards expanded create a dominant loop?
   Is it always better to use it or never use it?
6. **Proposals not yet implemented**: Identify any gaps from Parts 1–4 of the
   proposals file that were NOT addressed by P5.1–P5.12 and remain open issues.
7. **Recommended adjustments**: Specific numerical changes (die counts, costs,
   penalty values) with reasoning.

Validation:

- Confirm the audit report exists at the target path.
- Confirm it addresses all 7 sections above.
- Run markdownlint on the audit report.

Delegation notes:

- This is a research and writing task, not an editing task. Do not modify
  the chapter file during this audit.
- Mathematical reasoning should be explicit — show expected value calculations
  where relevant.
- Flag any rule that is unclear or ambiguous in its current form, even if
  it is not obviously broken.
- The RPG balance analysis skill has specific frameworks for evaluating
  dominant strategies and perceived vs. actual balance. Load it before writing.

---

## Working Rules

- Canonical source: `02-gamemasters-guide/12-battles-and-sieges.md`
- Proposals source: `proposals/proposal-battles-and-sieges-overhaul.md`
- All writing must follow `WRITING_GUIDE.md` — harsh, practical, physical, no
  AI tells.
- Load `skills/forbidden-lands-writing/SKILL.md` before any prose writing.
- Load `skills/forbidden-lands-design/SKILL.md` before any mechanics writing.
- Do not cut content. Rewrite for voice only.
- No rollback needed per prompt (no destructive operations) but chapter grows
  with each prompt — if a prompt produces a badly malformed insertion, revert
  with git before the next prompt.
- Run markdownlint after every edit to the chapter file.
- Each prompt must not proceed if its predecessor's validation has not passed.

## Decision Log

- 2025: All 12 proposals accepted for integration.
- 2025: Balance audit placed at end to avoid auditing an incomplete chapter.
- 2025: Terrain + Weather + Night are separate prompts; Weather and Night are
  grouped as Prompt 2 because they share an insertion block.
- 2025: Death to Cowards is a replacement, not an addition — flag before
  executing to confirm the old paragraph text exactly.

## Risks And Blockers

- Battle Magic skill pairings depend on chapter 7 — if the magic paths do not
  map cleanly to the proposed skills, the mage rules need adjustment before
  integration.
- Veterans die type mechanic (D6→D8 etc.) requires confirming that the base
  battle system uses fixed D6s. If the core rules already use different die
  types for some units, the Veterans upgrade path must be reconsidered.
- Death to Cowards replacement risk: the existing paragraph is embedded in a
  section with surrounding text. Read exact paragraph before replacing.

<!-- markdownlint-enable MD013 -->
