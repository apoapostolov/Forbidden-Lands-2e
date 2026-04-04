<!-- markdownlint-disable MD013 -->

# Rewrite Calibration Examples

## Contents

1. Purpose
2. Example 1: Gear Rule Rewrite
3. Example 2: Injury Naming Rewrite
4. Example 3: Proposal Tone Rewrite
5. Reusable Rewrite Lessons

## Purpose

This reference gives the writing skill concrete before-and-after pairs drawn from this repo.

Use it when the AI needs more than abstract style guidance.
It shows what a real improvement looks like in manuscript terms:

- harder diction
- cleaner paragraph jobs
- stronger rule hooks
- less modern or design-document language

## Example 1: Gear Rule Rewrite

Source:

- `corebook/10-gear.md`
- commit `5086e0d`

### Before

Every adventurer learns the worth of shabby little things that never earn a verse in any song. A short shovel, a hand pick, a hammer, a pry-iron, a few wedges, nails, cord, scraps of leather, a knife, a flask of oil. Each piece is cheap. Being without them can make or break an adventurer.

`Makeshift Tools` is such a kit. It is not a builder's chest or a smith's bench in a sack, only a mean bundle of rough field gear for digging, prying, staking, patching, and other ugly work on the road. These kits are commonly thrown together from offcuts, poor iron, scrap wood, and whatever straps and bits can be spared. That is why they cost little, and why they rarely stay whole for long.

Track `Makeshift Tools` with a `D8` Resource Die when bought. Roll the die after any significant use: digging through roots, snow, rubble, or loose earth; prying open lids, boards, doors, or stones; driving stakes; cutting away debris; making rough camp repairs; or patching harness, carts, shields, boats, and the like. On a roll of 1 or 2, something splits, dulls, bends, cracks, or is used up.

If a task calls for a proper hand tool and you have only `Makeshift Tools`, you may still attempt the work. With a `D8` Resource Die, the roll is at `-1`. With a `D6` Resource Die, the roll is at `-2`. This only applies when `Makeshift Tools` stands in for a real tool of the same general kind. It never replaces a forge, a full workshop, or a proper craftsman's set.

### After

Every adventurer learns the worth of the ugly little things that never earn a verse in any song. A short shovel. A hand pick. A hammer. A pry-iron. A few wedges, nails, cord, scraps of leather, a knife, a flask of oil. None of it is fine, and none of it is meant to last, but being without such things can break a journey.

`Makeshift Tools` is such a kit. It is not a builder's chest, a mason's roll, or a smith's bench in a sack. It is a rough bundle of field gear for digging, prying, staking, patching, and other mean roadwork. Most such kits are thrown together from offcuts, poor iron, scrap wood, and whatever straps and bits can be spared. That is why they are cheap. That is also why they fail.

Track `Makeshift Tools` with a `D8` Resource Die when bought. Roll the die after any hard or significant use: digging through roots, snow, rubble, or loose earth; prying at lids, boards, doors, or stones; driving stakes; cutting away debris; making rough camp repairs; or patching harness, carts, shields, boats, and the like. On a roll of `1-2`, something splits, dulls, bends, cracks, or is spent.

If a task calls for a proper hand tool and you have only `Makeshift Tools`, you may still attempt the work. With a `D8` Resource Die, the roll is at `-2`. With a `D6` Resource Die, the roll is at `-3`. This only applies when the kit can stand in for the same general kind of tool. It never replaces a forge, a workshop, or a true craftsman's set.

### What Changed

- The opening became more concrete and more rhythmic.
- The sentence fragments in the item list create weight without drifting into purple prose.
- `Can make or break an adventurer` became `can break a journey`, which is harsher and more local to the chapter's travel-and-gear logic.
- `builder's chest or a smith's bench` became `builder's chest, a mason's roll, or a smith's bench`, which sharpens object identity.
- `cost little` became `are cheap`, which is plainer and stronger.
- `rarely stay whole for long` became `fail`, which ends harder.
- The rules paragraph improved terminology precision with `hard or significant use` and formatted `1-2`.
- The substitution penalty became stricter and more honest about the item's limits.

### Lesson

When revising gear prose, make the object feel handled, cheap, worn, and specific.
Then make the rule blunt.

## Example 2: Injury Naming Rewrite

Source:

- `proposals/proposal-realistic-critical-injuries.md`
- commit `5086e0d`

### Before

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 33-34 | Chronic pain syndrome | Once per Quarter Day, the GM may impose `-1` to all Strength-based rolls until you rest or are numbed. |
| 45-46 | Infertility and endocrine damage | The injury carries long-term personal consequences and leaves you fragile to cold, heat, and exhaustion. |
| 63-64 | Quadriplegic scar survivor | Alive and lucid, but your `Strength` and `Agility` are both permanently reduced to `1`. |
| 65 | Feeding-tube survivor | Your `Strength` is permanently reduced to `1`, and ordinary food or drink can no longer be taken comfortably. |

### After

| D66 | Permanent Injury | Lasting Effect |
| --- | --- | --- |
| 33-34 | Ceaseless pain | Once per Quarter Day after a forced march, hard fight, or heavy labor, suffer `-1` to Strength-based rolls until you rest. |
| 45-46 | Withered loins | The injury carries long-term personal consequences and leaves you fragile to cold, heat, and exhaustion. |
| 63-64 | Neck-broken remnant | Alive and lucid, but your `Strength` and `Agility` are both permanently reduced to `1`. Retirement from active adventuring is the default. |
| 65 | Gullet-ruined remnant | Your `Strength` is permanently reduced to `1`, and ordinary food or drink can no longer be taken comfortably. Active adventuring usually ends unless the campaign can support constant accommodation. |

### What Changed

- Clinical modern labels were replaced with names that still carry authentic bodily meaning.
- The revised names sound like field language, not a chart in a hospital.
- `Survivor` became `remnant` in the most catastrophic cases, which better matches the manuscript's harshness.
- The effect text also improved, not just the label.
- Open-ended GM imposition became a triggered rule tied to existing game pressures such as forced march and heavy labor.
- The most catastrophic results now state retirement pressure honestly instead of pretending they are fully ordinary adventurer outcomes.

### Lesson

For injury text, keep the anatomy real but the naming pre-modern, hard, and brief.
If the effect is campaign-ending for many characters, say so plainly.

## Example 3: Proposal Tone Rewrite

Source:

- `proposals/proposal-kind-retirement-after-crippling-injury.md`

### Draft Shape To Avoid

If an injury leaves an adventurer difficult to play without slowing the story, or simply no longer enjoyable for the player, the table should treat retirement as an honorable outcome.

The adventurer has not failed. They have survived.

They may:

- remain with the company as a trusted follower NPC
- keep the camp, stores, horses, or stronghold accounts
- become a guide, quartermaster, healer's assistant, watch-keeper, or counselor

### Manuscript-Facing Direction

Some wounds leave a scar and a limp. Those still belong on the road. Others leave a body alive but end a warrior's days of marching, fighting, and sleeping in the rain. When such a wound is rolled, the player may let the adventurer step away from danger with honor.

The companion has not failed. They have endured. They may keep the camp, tend the stores, watch the horses, advise the company, or take shelter in a hall, temple, or village where other hands can care for them.

### What Changed

- The revised version removes proposal-talk such as `difficult to play` and `enjoyable for the player`.
- It keeps the humane core, but moves the language toward world truth and in-setting dignity.
- The list is compressed into prose because the passage is tone-setting, not procedure-heavy.
- `trusted follower NPC` becomes a story-facing description rather than a rules label.

### Lesson

When promoting proposal prose toward manuscript voice, remove design-room framing first.
Then restate the same humane intent in world-facing language.

## Reusable Rewrite Lessons

1. Replace modern abstraction with material consequence.
2. Give each paragraph one job.
3. End harder.
4. Use existing rule hooks instead of free-floating GM advice.
5. If a line sounds like design commentary, it is not ready for the manuscript.
6. If a label sounds clinical, corporate, or therapeutic, rework it.
7. Preserve kindness by changing the framing, not by importing modern tone.

<!-- markdownlint-enable MD013 -->
