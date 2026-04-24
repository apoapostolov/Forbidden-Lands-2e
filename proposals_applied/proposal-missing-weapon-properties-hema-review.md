<!-- markdownlint-disable MD013 -->

# Proposal: Missing Weapon Properties, HEMA Review

## Purpose

The current weapon feature list already covers reach, armor pressure, hooks, chains, and shield-breaking in a useful way.
What it does not yet cover is the smaller set of combat behaviors that HEMA treats as distinct weapon jobs:

- working around a shield line
- pressing a guard backward
- catching and binding
- fighting from the inside with a long weapon
- countering in tempo instead of simply hitting harder

This proposal reviews the missing space as a group, then separates the candidates that should become weapon properties from the ones that should stay as talents, tactics, or later exceptions.

## HEMA Read

HEMA is useful here, but only if it is used honestly.
It does not justify adding every historical trick as a new tag.
It does show that some weapon behaviors are real enough to deserve their own rule hook.

The important test is not “does this exist in historical fencing?”
The important test is “does this create a clear table decision without flattening nearby weapons?”

The second test is just as important:

- is this an always-on property
- is this a success-threshold rider
- is this a stance or mode
- is this better as a reaction or talent

## Audit Framework

The manuscript already has a strong base:

- `LONG-REACH` controls distance
- `CHAINED` makes parries worse
- `HOOK` supports shove pressure
- `POINTED` supports thrusting and parry pressure
- `TRAPPING` supports disarm pressure
- `SHIELD-BREAKER` handles hard object breaking
- `POLEARM` and the long-weapon rules already cover degraded inside-range fighting

That means new rules should fill a gap, not compete with those jobs.

For this audit, the candidates break into four rule layers:

- **property:** always on, written on the weapon line
- **critical rider:** triggers on `3+ ⚔️` or another success threshold
- **mode or stance:** changes reach or use state for a time
- **reaction or talent:** a counterplay rule that belongs in the action system

## Candidate Review

### 1. FLEXIBLE - IMPLEMENTED

**HEMA job:** A lash can work around the rim of a shield, not through it.

**Gameplay job:** Give whips and bladed whips a real identity against shield users without making shields worthless.

**Rule layer:** property

**Would apply to:** `WHIP`, `BLADED WHIP`

**Verdict:** Add.

Suggested rule text:

> **FLEXIBLE:** When a target uses a shield to PARRY this weapon, reduce the shield bonus by 1, to a minimum of 0. This does not affect parries made with weapons.

This is the cleanest missing property.
It is narrow, legible, and does not duplicate `CHAINED`.

### 2. PUSHING

**HEMA job:** Some weapons win by forcing the line back, not by landing clean cuts.

**Gameplay job:** Make certain weapons better at displacement and pressure.

**Rule layer:** critical rider

**Would apply to:** `LONG-REACH` spears, `POLEARM` haft weapons, `STAFF`, possibly `TRIDENT`

**Verdict:** Hold for now.

Suggested rule text:

> **PUSHING:** When this weapon hits with 3+ ⚔️, you may spend 1 ⚔️ to force the target one step back in the engagement line or prevent them from closing for their next action.

Reason:

- `HOOK` already supports `SHOVE`
- `BRACE` already supports stopping a rush
- `LONG-REACH` already keeps lower bands under pressure

A separate pushing tag would mostly repeat what the chapter already does with other wording.
If this ever becomes necessary, it should probably be a talent or a special polearm exception, not a universal weapon property.

### 3. ENTANGLING

**HEMA job:** Binding or snagging the enemy's weapon, limb, or shield edge.

**Gameplay job:** Give nets, lash weapons, and control weapons a stronger restraint identity.

**Rule layer:** critical rider

**Would apply to:** `TRIDENT`, `WHIP`, `BLADED WHIP`, maybe `FLAIL` if the design wanted more bind pressure

**Verdict:** Hold for now.

Suggested rule text:

> **ENTANGLING:** When this weapon hits with 3+ ⚔️, choose one: the target suffers -1 to ATTACK and PARRY, or -1 to DODGE and MOVE. If the target is entangled by the arms, use the first pair. If the target is entangled by the legs, use the second. The effect lasts until the target spends a FAST action to break free, until you use the weapon again to ATTACK, or until you choose to free the target.

Reason:

- `TRAPPING` already covers the important weapon-catch space
- a second restraint tag would blur the line between catch, bind, and disarm
- the game does not need two near-overlapping restraint properties unless a future weapon class demands it

If a stronger bind rule is needed later, it should be added where the weapon fiction truly demands it.

### 4. HALF-HAND

**HEMA job:** A long weapon can sometimes be shortened and worked from the middle or the hilt.

**Gameplay job:** Let long blades remain dangerous when the fight collapses.

**Rule layer:** mode or stance

**Would apply to:** `Bastard Sword`, `Longsword`, `2H LONGSWORD/CLAYMORE`, `Greatsword`

**Verdict:** Accept with restrictions, with one required constraint before manuscript integration.

Suggested rule text:

> **HALF-HAND:** When you are already within NEAR range of an enemy, you may spend a FAST action to shorten your grip and shift the weapon one band inward. The weapon stays at that shorter reach until you spend a FAST action to extend it again. You can only move one band at a time.

Reason:

- this is technique, not weapon essence
- the manuscript already models close-range degradation through specific rules like `POLEARM` fallback and `CUT IN / BACK`
- it works best as a sword-handling mode, not as a general reach trick
- `Bastard Sword` is the cleanest fit because its hybrid grip already invites shortening and extension

**Required constraint:** `HALF-HAND` must require that you are already at NEAR range or closer before you can shorten your grip. Without this, `HALF-HAND` as a guaranteed FAST action would bypass the risk of `CUT IN` entirely. `CUT IN` is a FAST action plus a MOVE roll to close against a longer-reach weapon — it has failure risk. If `HALF-HAND` functions from any range, a Bastard Sword user would close on a spearman for free without facing that roll. The proximity requirement keeps `CUT IN` doing its job: it handles the risky work of entering reach. `HALF-HAND` is the reward for already being there.

If the book ever wants this space, it should stay on bladed swords with enough grip to make the mode meaningful.

### 5. MASSIVE / SMASHING - IMPLEMENTED

**HEMA job:** Heavy impact can overwhelm guard, armor, and structure.

**Gameplay job:** Give oversized, brute-feeling weapons a clear identity against armor, gear, and guard.

**Rule layer:** critical rider

**Would apply to:** `HEAVY WARHAMMER`, `TWO-HANDED FLAIL`, `RUST CENSER`, possibly other oversized relic weapons with the same fantasy brute feel

**Verdict:** Accept with simplification.

Suggested rule text:

> **SMASHING:** When this weapon hits with 3+ ⚔️, it becomes a smashing hit: it also deals 1 damage to the target's armor, or to the weapon or shield used to PARRY it. Against unattended objects, count the rolled ⚔️ twice for damage and destruction.

Reason:

- `HEAVY`, `BLUNT`, `PIERCE ARMOR`, and `SHIELD-BREAKER` already cover most of this terrain
- a new smashing tag would mainly add another route to the same result
- that risks making heavy weapons too good at too many jobs

If the game later needs a stronger guard-break identity, it should be introduced on a single weapon line or through a talent, not as a broad tag.
This rider is strong enough to justify itself because it stays on weapons that are already odd, oversized, and more legend than workshop object.

### 6. RIPOSTE

**HEMA job:** Some weapons and styles answer cleanly after a missed attack.

**Gameplay job:** Reward counterplay and timing.

**Rule layer:** reaction or talent

**Would apply to:** weapons with `PARRYING`, especially `SAI/PARRYING DAGGER`, `RAPIER`, `BROADSWORD`, `LONGSWORD`, `SWORDBREAKER`, and similar dueling blades

**Verdict:** Hold for a talent or maneuver, not a weapon property.

Suggested rule text:

> **RIPOSTE:** After a PARRY with 3+ ⚔️ using a weapon that has `PARRYING`, you may spend 1 WP to make one immediate attack against the attacker. The riposte uses your normal reach and can be PARRIED or DODGED as usual.

Reason:

- riposte is a timing rule, not a material property
- it needs a clear trigger and a clear cost
- the current manuscript already gives that space to actions, initiative, and talents
- a weapon tag would be the wrong layer

If the game wants riposte behavior, it belongs in a talent or a specialized defensive action, not on the item line.

## Recommended Package

If this proposal is accepted, only one new property should be added now:

- `FLEXIBLE`

If the manuscript wants to preserve the other ideas:

- `PUSHING` and `ENTANGLING` should remain rider candidates, not broad tags
- `HALF-HAND` should be used only on bladed swords that can plausibly shift grip, with `Bastard Sword` as the clearest fit
- `SMASHING` should be kept only for oversized brute weapons
- `RIPOSTE` should remain a talent or maneuver

Those are the two candidates that clearly fill missing spaces without overlapping another rule family too hard.

## Why Not Add The Others

The rest of the candidates are real combat ideas, but they are not all good weapon properties.
Some are already covered by existing tags.
Some belong to talents.
Some belong to special maneuvers.
Some are better as critical riders than as always-on tags.

That distinction matters.
If every historical fighting idea becomes a weapon feature, the table becomes harder to read and the weapons lose identity.

## Balance View

### What The Rule Rewards

- shield users who keep good distance and angles
- flexible weapons that threaten the rim instead of just the ribs
- oversized brute weapons that can crush armor or gear on a strong hit
- weapons that feel different from chains, hooks, and thrusting blades

### What Players Will Probably Believe It Rewards

Players will expect flexible weapons to pressure shields without deleting them.
That is exactly what `FLEXIBLE` does.

They will also expect the other candidate ideas to show up only if they are worth the rules space.
That expectation is healthy.

### What The GM Will Likely Need To Manage

- whether a weapon is really `FLEXIBLE` or just `CHAINED`
- whether a proposed property is already covered by `HOOK`, `TRAPPING`, or `LONG-REACH`
- whether a behavior belongs in gear, a talent, a maneuver, or a rider instead

That is manageable if the rules stay narrow.

## Risks

### Too Many Tags

The biggest risk is bloat.
Weapon properties should explain the weapon's job, not list every possible thing it can ever do.

### Shield Deletion

If the flexible-weapon rule becomes too strong, shields stop being a meaningful choice.
That would damage both play and the fiction.

### Wrong Rule Layer

Several of these ideas are real, but not as item tags.
The wrong layer is a common source of rules drift.

## Recommended Revision

Add `FLEXIBLE` now.
Add `SMASHING` only on the oversized brute weapons that need it.

Keep the rest as follows:

- `PUSHING` - hold as a rider candidate
- `ENTANGLING` - hold as a rider candidate, `TRAPPING` already carries part of the space
- `HALF-HAND` - hold as a mode or stance, better than a broad property
- `RIPOSTE` - hold as a talent or maneuver, not a weapon property

The draft rule texts above are included so the design space is visible and can be compared against the current manuscript before anything is promoted.

That gives whips a real shield-interaction hook, blunt weapons a clean armor-and-gear pressure rider, and the rest of the table enough room to stay readable.
