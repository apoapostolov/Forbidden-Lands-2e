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

If a follow-up balance patch is wanted, prefer `Option A`.

That is the clearest rule and the least likely to cause further hidden drift:

- thrown hybrid weapons stay flexible
- dedicated talent lanes stay meaningful
- the best answer is less often "take the hybrid weapon that stacks everything"

If the manuscript wants to preserve current thrown-weapon exuberance, then do nothing yet and only watch actual play after the base-table rebalance lands.

## Recommendation For Now

Do not integrate this proposal immediately.

Instead:

1. implement the base ranged weapon rebalance first
2. test whether thrown hybrids and late-game crossbows still dominate in play
3. only then decide whether `THROWING ARM` or `FAST SHOOTER` needs narrowing

That keeps the first correction clean and avoids solving three problems at once with one muddy patch.
