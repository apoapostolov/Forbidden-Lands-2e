<!-- markdownlint-disable MD013 -->

# Proposal: Follow-Up Balance Pass for Ranged Talent Stacks

## Purpose

This proposal is a follow-up to
[proposal-ranged-weapons-plug-and-play-rebalance.md](/home/apoapostolov/git-public/Forbidden-Lands-2e/proposals/proposal-ranged-weapons-plug-and-play-rebalance.md).

The weapon-table rebalance corrects baseline bonus inflation.
It does not fully solve the stronger source of ranged imbalance in this manuscript:

- talent stacking
- action compression
- hybrid melee/ranged weapons that benefit from more than one talent lane

This document isolates those issues so they can be judged separately.

## Main Problem

The current manuscript lets some ranged options become much stronger than the base weapon table suggests, because the real leverage lives in talents.

The most important stacks are:

1. `THROWING ARM` + `AXE FIGHTER`
2. `THROWING ARM` + `HARPOONER`
3. `FAST SHOOTER` + `SHARPSHOOTER`
4. high-bonus crafted ranged weapons + the stacks above

## Why This Matters

The visible Reddit criticism about javelins and throwing knives becoming better than their melee cousins is not really just a table complaint.

It is a talent complaint hiding behind a weapon table complaint.

The real question is:

- when does a hybrid weapon become a useful compromise
- and when does it become the best answer in too many scenes

## Current Talent Pressure

### Throwing Axe

`Throwing Axe` already combines:

- melee usability
- ranged usability
- decent damage

Then `THROWING ARM` can stack with `AXE FIGHTER`.

That means one weapon can benefit from:

- generic thrown accuracy
- axe accuracy
- later axe critical pressure

Even after the base-table rebalance, this remains a strong line.

### Throwing Spear

`Throwing Spear` is even more delicate because `HARPOONER` does more than add accuracy.

It adds:

- +1 to attack
- ongoing bleed pressure
- later artifact support

That means the weapon is not just accurate. It carries a strong damage-over-time identity and a control identity.

This is likely acceptable because the weapon is supposed to be specialist gear, but it should remain a conscious niche rather than a silent dominant line.

### Bows And Crossbows

`SHARPSHOOTER` supports both bows and crossbows.

`FAST SHOOTER` changes cadence:

- bows and slings lose the READY tax early
- crossbows lose much of the RELOAD tax at rank `4`

That creates a late-game effect where crossbows can become hard-hitting, long-ranged, and no longer meaningfully slower in the same way.

That is where the real crossbow pressure lives, not only in the base table.

## Balance Analysis

### What The Rule Rewards

The current talent structure rewards:

- specialization
- action compression
- hybrid-weapon efficiency

### What Players Will Believe It Rewards

Players will often read it as:

- "this weapon is both flexible and best in class"
- "I can solve both melee and ranged scenes with one talent path"
- "late-game crossbows are just better bows"

That belief is not always mathematically exact, but it is close enough to shape behavior.

### What The GM Must Manage

The GM must quietly absorb:

- overly efficient thrown sidearms
- ranged specialists who dominate from safety
- endgame cadence where crossbows stop feeling costly enough

If the system relies on encounter shaping alone to restrain those lines, the balance is not robust.

## Proposed Corrections

These are listed from smallest fix to largest.

## Option A: Clarify Hybrid Weapon Talent Boundaries

Add a narrow rule note:

> A thrown melee weapon can benefit from either its melee weapon talent or `THROWING ARM` on a given attack, not both, unless a talent explicitly says otherwise.

### Option A Strengths

- smallest rules change
- directly answers the Reddit concern
- reduces dominant hybrid stacking

### Option A Weaknesses

- overrides the current explicit text of `THROWING ARM`
- may disappoint players already built around stacked identities

## Option B: Keep Stacking, But Narrow What Counts

Keep the current stacking text in principle, but exclude some effects from carrying over to thrown attacks.

For example:

- accuracy modifiers may stack
- automatic critical effects or other rider effects from melee talents do not apply unless the talent explicitly says they do

### Option B Strengths

- preserves the fantasy of overlap
- reduces the sharpest abuse

### Option B Weaknesses

- more wording complexity
- easier to forget at the table

## Option C: Leave Thrown Weapons Alone, Fix Crossbow Cadence Only

Accept that thrown-weapon overlap is part of the manuscript's style, and instead restrict the strongest late-game cadence issue.

Possible change:

> `FAST SHOOTER` rank `4` reduces crossbow reload by one step, but cannot reduce `Load` below a SLOW action.

### Option C Strengths

- very small change
- directly protects the bow versus crossbow distinction

### Option C Weaknesses

- does not address thrown hybrid dominance
- weakens a late-rank talent payoff

## Recommended Direction

**Apply `Option C` to `FAST SHOOTER` rank 4 concurrently with the table changes. Do not defer it.**

The `Light Crossbow` range correction (Short → Long) combined with `FAST SHOOTER` rank 4 produces a character who fires `+3` effective, Damage 2, Long range every round with no penalty. A fully invested Longbow archer at the same talent cost fires `+2` effective, Damage 1, Long per round, or twice per round with Agility damage pressure on movement. The Light Crossbow with `FAST SHOOTER` 4 + `SHARPSHOOTER` costs the same talent investment but produces better results across every metric. The table change reduces the problem from `+4` effective to `+3`; it does not fix the action economy gap.

**Option C text for `FAST SHOOTER` rank 4:**

> `FAST SHOOTER` rank 4: Reloading a crossbow is now a FAST action. Shooting it still costs a SLOW action.

Crossbow cadence stays at one shot per round. Bows retain their value through volume: `FAST SHOOTER` rank 3 lets bow users fire twice per round.

**For `THROWING ARM` + `AXE FIGHTER`, prefer a targeted text amendment over `Option A`.**

`Option A` overrides explicit manuscript text — `THROWING ARM` currently reads: "stacks with other weapon talents (like AXE FIGHTER)." Removing that stacking will feel like a nerf to players who built around it in good faith.

A narrower clarification achieves the same result without that problem:

> When you throw a melee weapon, `THROWING ARM`'s attack bonus stacks with `AXE FIGHTER`'s attack bonus and Artifact Die. `AXE FIGHTER`'s automatic critical effect (rank 2) and EXECUTIONER interaction (rank 4) do not apply on a throw.

This keeps the stacking sentence intact and preserves the fantasy. It blocks only the rider effects that imply melee wound control which you do not have when the weapon is airborne.

## Recommendation For Now

1. Implement the base ranged weapon rebalance.
2. Apply the `FAST SHOOTER` rank 4 Option C fix in the same integration pass — not after playtesting.
3. Amend `THROWING ARM` text to specify that rider effects from melee talent ranks do not carry over on throws.
4. Test whether the remaining thrown hybrid pressure still feels dominant after those changes.

That keeps the first correction clean without leaving a known live problem in place.
