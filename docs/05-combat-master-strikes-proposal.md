<!-- markdownlint-disable MD013 -->

# Draft Proposal: Master Strikes

## Status

This document is a design record only. The rules below are not implemented in
`01-corebook/05-combat-and-damage.md` yet and should not be treated as
canonical until they are approved for the chapter.

## Goal

Master strikes are an optional close-combat pressure rule. Their purpose is to
make strong hits matter in space, tempo, and control, not just in damage.

The rule should do three things:

- reward a successful attack that lands hard enough to matter
- give the defender a meaningful choice between retreating and accepting a cost
- create stronger weapon identity for slash and stab without turning every hit
  into raw extra damage

The proposal is intentionally separate from the chapter so it can be tested,
edited, or discarded without losing the idea.

## Proposed Rule

A master strike is a successful close-combat attack that inflicts at least 3
points of damage after DODGE or PARRY, but before ARMOR is rolled.

ARMOR reduces the final damage as normal, but it does not cancel the master
strike once the threshold has been reached.

If a master strike occurs, the target must choose one of the following:

- BACK
- suffer the listed consequence for the strike type

If the target cannot BACK, or if backing is impossible or clearly
prohibitive, the consequence applies automatically.

## Proposed Strike Types

### SLASH

When a SLASH becomes a master strike, the target may BACK. If it does not, or
cannot, it suffers -2 to all DODGE attempts until the end of its next turn.

This makes slash the more controlling stroke. It pushes the target out of the
line, or leaves them worse able to slip the next attack.

### STAB

When a STAB becomes a master strike, the target may BACK. If it does not, or
cannot, it loses its next FAST action.

This keeps stab focused on opening space and stealing tempo rather than
stacking generic attack penalties.

### Monster physical attacks

When a monster's physical attack deals 3 or more damage to a single target,
the target may BACK. If it does not, or cannot, it suffers -2 to its next
attack until the end of its next turn.

This gives monsters a parallel pressure rule without forcing every monster
attack into the slash/stab framework.

## Why This Works

The proposal is meant to make close combat feel sharper and more dangerous by
adding forced space control.

It does not simply add damage. Instead, it creates a choice that matters in the
moment:

- step back and lose ground
- stay engaged and accept a tempo cost

That choice is especially strong in a system where position, reach, and action
economy already matter.

## Design Notes

- The rule is strongest when BACK actually changes weapon reach or engagement.
- The threshold is deliberately high enough that master strikes feel earned.
- SLASH and STAB should remain different from each other.
- Monster attacks need their own wording because not every monster strike fits
  a weapon type.
- This is meant to be optional. It should only enter the corebook after playtest
  confirms that it adds pressure without slowing the game down.

## Open Questions

- Should the threshold be measured before or after any non-armor reduction that
  happens during the attack?
- Should a defender who cannot BACK be forced into a different cost depending
  on terrain or weapon reach?
- Are there any other strike types that should later gain their own master
  strike rider?

## Next Step

If this proposal is approved, move the final wording into the combat chapter
and keep this file as the design record.
