<!-- markdownlint-disable MD013 -->

# Proposal: Plug-and-Play Rebalance of Ranged Weapons

## Source

This proposal is inspired by a community discussion on Reddit:

- <https://www.reddit.com/r/ForbiddenLands/comments/1rz3xe2/rebalance_of_ranged_weapons/>

It does not copy that chart outright. It adapts the useful design pressure from the discussion to this manuscript's current weapon table, gear chapter, and existing `War bow` crafting logic.

## Purpose

Ranged weapons in the current manuscript have three problems:

1. weapon bonus is too generous across much of the table
2. crossbows pay a loading cost, but still compete too much through raw accuracy inflation rather than through distinct battlefield role
3. bows already have a good design answer for draw weight in Chapter 10, yet Chapter 5 still makes them read more like flat accuracy upgrades than like different tools

The goal is to rebalance ranged weapons with direct number changes only. This should remain plug-and-play:

- no new subsystems
- no new action types
- no new ammunition rules
- no new mounted-combat rules

## Design Direction

The balance logic behind this proposal is simple:

- keep thrown weapons useful, but do not let them become strict upgrades over their melee cousins
- compress weapon bonus so `+3` does not become the default answer to ranged combat
- let crossbows win through damage and ease of use, not just through oversized bonus
- let stronger bows live in the already existing `War bow` logic in Chapter 10, where draw weight and strength cost are already modeled

## Current Problems

### Bonus Inflation

In the current Chapter 5 table, most serious ranged weapons sit at `+2` or `+3`. In this engine, that is expensive power. Extra Gear Dice sharply increase hit rate and stunt ceiling, especially on already competent archers.

This has two bad effects:

- light and moderate ranged weapons become too reliable
- crossbows differentiate themselves by inflated accuracy instead of distinct rhythm and damage

### Throwing Axe Pressure

The current `Throwing Axe` is `+2`, Damage `2`, at Near range. That makes it unusually efficient for a weapon that is still also a melee sidearm. It crowds the `Throwing Knife` and makes the `Throwing Spear` less distinct than it should be.

### Bow Role Confusion

This manuscript already contains a good answer for stronger bows:

- `Longbow` as the larger self-bow
- `Recurve Bow` as the shorter long-range bow
- `War bow` as the heavy-draw upgrade that costs strength and training

That is enough design space already. The ranged table should support that structure, not flatten it under high default accuracy.

## Proposed Ranged Weapon Table

This proposal changes only the numbers that need changing.

| WEAPON            | GRIP | BONUS | DAMAGE | RANGE | COST | FEATURES                                                                                              |
| ----------------- | ---- | ----- | ------ | ----- | ---- | ----------------------------------------------------------------------------------------------------- |
| Rock              | 1H   | —     | 1      | Near  | —    | Light, Ranged (Blunt)                                                                                 |
| Throwing Knife    | 1H   | +1    | 1      | Near  | 1    | Light, Pointed, Melee/Ranged                                                                          |
| Throwing Axe      | 1H   | +1    | 2      | Near  | 2    | Edged, Melee/Ranged                                                                                   |
| Throwing Spear    | 1H   | +1    | 2      | Short | 2    | Pointed, Melee/Ranged                                                                                 |
| Sling             | 1H   | +1    | 1      | Short | 1    | Light, Ranged (Blunt), Ready, Stones/Bullets                                                          |
| Blowgun           | 1H   | +1    | 1      | Short | 3    | Light, Ranged (Pointed), Ready, Blowgun darts, Armor Rating x2, Can remain hidden during ambush round |
| Short Bow         | 2H   | +1    | 1      | Short | 6    | Light, Ranged (Pointed), Ready, Arrows                                                                |
| Recurve Bow       | 2H   | +1    | 1      | Long  | 12   | Light, Ranged (Pointed), Ready, Arrows                                                                |
| Longbow           | 2H   | +1    | 1      | Long  | 12   | Tough, Ranged (Pointed), Ready, Arrows                                                                |
| Light Crossbow    | 2H   | +2    | 2      | Long  | 24   | Ranged (Pointed), Load, Quarrels/Bolts                                                                |
| Heavy Crossbow    | 2H   | +2    | 3      | Long  | 40   | Heavy, Ranged (Pointed), Load x2, Quarrels/Bolts                                                      |
| Windlass Crossbow | 2H   | +2    | 3      | Long  | 40   | Heavy, Ranged (Pointed), Load x2, Quarrels/Bolts, Windlass                                            |

## What This Changes

### Throwing Axe

Change `Throwing Axe` from `+2` to `+1`.

This keeps it strong without letting it outshine every other thrown sidearm.

### Throwing Spear

No change.

The current manuscript already gives it the right identity:

- better reach than the axe
- same damage
- also usable in melee

That is enough. It also already has a strong talent path in `HARPOONER`, so it does not need a further baseline push here.

### Bows

Change `Short Bow`, `Recurve Bow`, and `Longbow` from `+2` to `+1`.

This does three things:

1. it stops ordinary bows from behaving like near-premium precision weapons
2. it preserves range and durability differences already present in the chapter
3. it leaves room for the existing `War bow` upgrade to matter

This proposal does **not** collapse bows into one single `Bow` entry. That would cut against existing Chapter 10 fiction and crafting support.

### Crossbows

Change `Light Crossbow`, `Heavy Crossbow`, and `Windlass Crossbow` from `+3` to `+2`.

Also change `Light Crossbow` range from `Short` to `Long`.

This gives crossbows a cleaner role:

- easier and steadier than bows
- slower than bows
- harder-hitting than bows
- longer-ranged than light bows

The `Light Crossbow` should not feel like a short-range curiosity if it already pays the load cost. It should feel like the accessible military or hunting shooter: slower than a bow, easier to use well, and dangerous at real range.

## Why Not Go Further

The Reddit thread also points toward collapsing bow types into a simpler `Bow` / `War Bow` split. That has merit in a lighter hack, but this manuscript already has:

- lore and flavor for short bow, recurve bow, and longbow
- crafting distinctions
- a `War bow` upgrade rule that already models heavy draw and strength demand

Because of that, a full consolidation would create more rewrite work than balance value.

## Interaction With Existing Chapter 10 Rules

This proposal is meant to work with current gear logic, not against it.

### War Bow

Keep the existing `War bow` rule in Chapter 10.

That rule already does the right job:

- stronger bow
- more damage
- real strength cost
- training ceiling tied to `Might`

If ordinary bows move down to `+1`, the `War bow` upgrade becomes more meaningful and more honest.

### Composite Bow

The `Composite Bow` table entry in Chapter 10 must drop from `+3` to `+2` in the same implementation pass.

The crafting rule does not change. The rule upgrades a Short Bow by `+1` weapon die. At the old baseline (`+2`), the result was `+3`. At the new baseline (`+1`), the result is `+2`. The table entry must reflect that, or the Composite Bow will sit three times above any regular bow with no cost increase — on par with a pre-nerf crossbow.

The crafting demands and moisture weakness remain as written.

### Throwing Weapons and Melee Talents

No new rule is needed here in the first pass, but this proposal must be read honestly against the current talent stack.

Thrown melee/ranged weapons already live in a useful compromise space. If later testing shows talent overlap causes abuse, that should be handled in a separate weapon-talent proposal rather than hidden inside the ranged table.

In this manuscript, `THROWING ARM` explicitly stacks with other weapon talents. That means:

- `Throwing Axe` can stack with `AXE FIGHTER`
- `Throwing Spear` can stack with `HARPOONER`

That is the main reason this proposal reduces the `Throwing Axe` bonus and leaves the `Throwing Spear` alone.

## Expected Balance Effects

### From the Player Side

- skilled archers still feel skilled because `MARKSMANSHIP` remains the main engine
- bows feel less like effortless precision weapons
- crossbows hit hard without also being the most accurate answer by default
- thrown weapons remain practical without crowding proper melee weapons

### From the GM Side

- fewer ranged attacks land with stacked bonus inflation
- armor matters a little more again
- ranged specialists still exist, but the table is less likely to tilt around them

## Risks

### Blowgun Outlier

Once other ranged bonuses are compressed, the `Blowgun` at `+2` stands out more sharply.

That may still be correct because it is:

- short-ranged
- low damage
- highly niche
- strongly tied to poison delivery and stealth

But it should be watched.

### Long-Range Light Crossbow

Moving the `Light Crossbow` to `Long` makes it more attractive. That is intended. If testing shows it crowds bows too much, the first correction should be price or supply pressure, not a return to `+3` / `Short`.

### Late-Game Crossbow Rhythm

This proposal improves crossbow balance at the base-table level, but it does not fully solve late-talent crossbow pressure.

`SHARPSHOOTER` applies to bows and crossbows alike, while `FAST SHOOTER` rank `4` turns crossbow reload into a FAST action. At that point, a loaded crossbow can begin to behave like a steadier hard-hitting bow that no longer pays its old action tax in the same way.

That is probably acceptable for high-rank play, but it should be named plainly. The proposal fixes baseline inflation. It does not fully rebalance endgame ranged talent stacks.

## Design Skill Pass

Using the repo's `forbidden-lands-design` skill, this proposal passes the main integration checks:

### Current Mechanics

- ranged accuracy is currently inflated in Chapter 5
- Chapter 10 already contains the real heavy-draw solution through `War bow`
- weapon crafting and weapon flavor already distinguish short bow, recurve bow, and longbow

### Design Logic

The strongest part of the proposal is that it does not invent new rules. It works by reducing bonus inflation and by letting existing subsystems carry more of the differentiation:

- action cost
- range band
- damage
- crafting access
- draw-strength upgrades

### Gameplay Logic

At the table, this should produce cleaner choices:

- bows are frequent and mobile
- crossbows are slower but harder-hitting
- thrown weapons remain practical sidearms rather than best-in-slot ranged answers

### Integration Points

The proposal fits cleanly with:

- Chapter 5 ranged actions and load/ready timing
- Chapter 10 bow, crossbow, `War bow`, and `Composite bow` rules
- `FAST SHOOTER`
- `SHARPSHOOTER`
- `THROWING ARM`
- `HARPOONER`
- `AXE FIGHTER`

### Design Risks

The design pass found one important limit:

- this proposal is safe as a first-pass table rebalance
- it is not a full talent-stack rebalance

That boundary should stay explicit.

## Balance Skill Pass

Using the repo's `rpg-balance-analysis` skill, the proposal looks broadly sound, with two pressure points that should stay visible.

### Mathematical Effect

Reducing a weapon from `+2` to `+1`, or from `+3` to `+2`, removes one Gear Die. In this engine that matters.

For one-success attacks, one extra die typically changes hit chance by about `3%` to `8%` depending on pool size. Around common attack pools:

- `5` dice to `6` dice: `59.81% -> 66.51%`
- `6` dice to `7` dice: `66.51% -> 72.09%`
- `7` dice to `8` dice: `72.09% -> 76.74%`

For two-success outcomes, one extra die is also significant:

- `6` dice to `7` dice: `26.32% -> 33.02%`
- `7` dice to `8` dice: `33.02% -> 39.53%`
- `8` dice to `9` dice: `39.53% -> 45.73%`

So the proposal is not cosmetic. It meaningfully compresses ranged reliability.

### What Players Will Feel

Players will feel three immediate changes:

- ordinary bows no longer feel effortlessly accurate
- crossbows still feel dangerous because their damage remains high
- thrown axes stop feeling suspiciously better than too many other sidearms

That is a good perception outcome. The rule promise and the actual table effect are closer together.

### What The GM Will Need To Manage

The GM will still need to watch:

- talent-stack specialists using thrown hybrid weapons
- late-game crossbow builds with `FAST SHOOTER`
- whether `Light Crossbow` at `Long` starts to crowd the recurve bow in actual play

### Balance Verdict

The proposal is good as a baseline ranged-weapon correction.

It should be accepted as:

- a table rebalance
- a bonus compression pass
- a niche-cleanup pass

It should **not** be described as a complete ranged balance solution, because the real remaining volatility lives in talent stacking, not in the base table alone.

## Recommended Implementation Scope

Implement only these direct Chapter 5 changes:

1. `Throwing Axe` bonus `+2 -> +1`
2. `Short Bow` bonus `+2 -> +1`
3. `Recurve Bow` bonus `+2 -> +1`
4. `Longbow` bonus `+2 -> +1`
5. `Light Crossbow` bonus `+3 -> +2`
6. `Light Crossbow` range `Short -> Long`
7. `Heavy Crossbow` bonus `+3 -> +2`
8. `Windlass Crossbow` bonus `+3 -> +2`

No other rules text needs to change unless later testing shows a second-order problem.

## Acceptance Recommendation

Accept with one caution:

- keep the bow family as three entries in this manuscript
- use the existing `War bow` rule as the heavy-draw solution
- treat this as a number rebalance, not a taxonomy rewrite
- if later testing shows a remaining problem, audit talents before changing the weapon table again

That gives the manuscript the cleanest gain for the least editorial cost.
