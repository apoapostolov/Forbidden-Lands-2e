<!-- markdownlint-disable MD013 -->

# Proposal: Acceptance Summary for Plug-and-Play Ranged Weapon Rebalance

## Scope

This document decides what from
[proposal-ranged-weapons-plug-and-play-rebalance.md](/home/apoapostolov/git-public/Forbidden-Lands-2e/proposals/proposal-ranged-weapons-plug-and-play-rebalance.md)
should move into the manuscript, what should be deferred, and what should be rejected.

It also takes into account the visible Reddit discussion on the source thread:

- one objection that javelins and throwing knives can become better than their melee cousins if the table is not careful
- one objection that collapsing all bows into one entry erases real differences
- one broad agreement that ranged weapons likely do need a rebalance

## Acceptance Verdict

Accept the table rebalance in principle, with limits.

## Accept

These changes are clean, local, and fit the existing manuscript:

1. `Throwing Axe` bonus `+2 -> +1`
2. `Short Bow` bonus `+2 -> +1`
3. `Recurve Bow` bonus `+2 -> +1`
4. `Longbow` bonus `+2 -> +1`
5. `Light Crossbow` bonus `+3 -> +2`
6. `Light Crossbow` range `Short -> Long`
7. `Heavy Crossbow` bonus `+3 -> +2`
8. `Windlass Crossbow` bonus `+3 -> +2`

These are acceptable because they:

- reduce bonus inflation
- preserve current rules language
- preserve current crafting and flavor support
- improve niche clarity without adding procedure

## Accept With Editorial Care

When integrated, the Chapter 5 weapon table should not over-explain the change.

Do not add balancing rationale to the manuscript. Just change the numbers.

If Chapter 10 text is touched at all, it should only be to keep descriptive prose from contradicting the new battlefield roles.

## Defer

These ideas should not be folded into the same implementation pass:

### Bow Consolidation

Do not replace `Short Bow`, `Recurve Bow`, and `Longbow` with one generic `Bow` entry.

This repo already supports those distinctions through:

- fiction
- crafting
- equipment flavor
- the existing `War bow` rule

The Reddit objection on this point is sound. In this manuscript, that consolidation would cost more than it would solve.

### Talent Interaction Cleanup

Do not try to solve `THROWING ARM`, `HARPOONER`, `AXE FIGHTER`, `FAST SHOOTER`, and `SHARPSHOOTER` in the same table patch.

That is a second design layer and should be handled in a separate proposal.

### Knife And Spear Melee Taxonomy

The Reddit criticism is correct that any ranged rebalance can expose awkward relationships between:

- `Throwing Knife` and melee knife entries
- `Throwing Spear` and melee spear entries

But that is a broader melee/ranged taxonomy issue, not a reason to reject the ranged rebalance itself.

## Reject For Now

Reject these source-thread ideas for this manuscript:

### New Attribute Requirements For More Weapons

Do not spread `Might` requirements across heavy melee weapons just because `War bow` already uses strength gating.

That would be a wider realism patch with unclear downstream value.

The current manuscript already has one good explicit draw-strength exception. It does not need a cascade of new stat gates without a much larger design pass.

## Integration Recommendation

If implemented, only these places should change:

1. [05-combat-and-damage.md](/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/05-combat-and-damage.md)
   update the ranged weapon table
2. [10-gear.md](/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/10-gear.md)
   only if a nearby descriptive sentence becomes misleading after the new numbers
3. [CHANGELOG.md](/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/CHANGELOG.md)
   record the rebalance under `Unreleased`

## Final Recommendation

Promote the base weapon-table rebalance.

Do not promote:

- bow consolidation
- new stat gates
- talent rewrites
- melee taxonomy cleanup

Treat this as a narrow correction to ranged baseline numbers, nothing more.
