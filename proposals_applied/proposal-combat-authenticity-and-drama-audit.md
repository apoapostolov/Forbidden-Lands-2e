<!-- markdownlint-disable MD013 -->

# Proposal: Combat Authenticity And Drama Audit

## Purpose

This proposal audits the current combat engine in `corebook/05-combat-and-damage.md` and identifies what is still missing if the goal is harsh, credible, dramatic fantasy violence rather than clean tactical sport.

The question is not whether the current system already has enough actions. It does.

The real question is whether the system reliably produces the kinds of battlefield moments this genre wants:

- lines breaking
- men giving ground
- shields and spears holding a charge
- wounded fighters trying to survive rather than fighting like automatons
- surrender, panic, and pursuit mattering before everyone is dead

## Current Strengths

The present combat rules already do several things well.

### The engine is dangerous fast

The core loop is sharp:

- rerolled initiative each round
- two-action economy
- reactive defense burning future tempo
- damage landing directly on attributes
- critical injuries turning defeat into long-term cost

That already gives combat weight.

### The manuscript already supports many maneuvers

The system is not missing basic melee vocabulary. It already has:

- shove
- disarm
- grapple
- feint
- retreat
- intercept
- mounted charge
- weapon-length control
- prone play
- cover

Many more specialized maneuvers are already delegated to talents, especially `COMBAT EXPERIENCED`, `DIRTY FIGHTING`, `PATH OF THE BODY`, and `PATH OF THE SHIELD`.

### The gear game is strong

Weapons, shields, armor, helmets, cover, long-reach weapons, and short-reach weapons all matter in play. This is one of the strongest parts of the manuscript's combat identity.

## Real Gaps

The current engine still has four meaningful holes.

### 1. Fights lack a rout and surrender layer

The rules do a good job of showing how people get hurt. They do a weaker job of showing how fights end before total slaughter.

Right now, a conflict usually keeps going until:

- one side is dead
- one side is Broken
- someone uses `FLEE`
- or the GM improvises a surrender

That is functional, but it leaves out one of the most genre-authentic parts of brutal premodern violence: once a side loses nerve, the fight changes shape immediately.

### 2. Spears and polearms can control distance, but they do not yet feel properly braced

The manuscript already models reach well. That part is good.

What is still missing is the classic dramatic moment of a fighter setting a spear, halberd, or pike to receive the rush. `INTERCEPT` exists, but it is a general trap action, not a distinct polearm answer to a charge or closing attack.

### 3. There is no basic "fight carefully and survive" action

The system has `DODGE`, `PARRY`, and `INTERCEPT`, but no simple default stance for:

- buying time
- covering a withdrawal
- weathering a stronger foe
- holding ground while waiting for allies

That means the defensive player often has to keep attacking or simply hope their reactions are enough.

### 4. Group combat has little baseline line-fighting support

There are shield talents and helping rules, but no plain core rule for two or more fighters deliberately holding together as a line.

In this genre, that matters. A shield beside another shield should matter before talents enter the picture.

## Recommendation

Add three small core rules and one optional morale module.

Do not add a large stunt menu.
Do not add hit locations.
Do not add called shots as a universal subsystem.
Do not add fatigue bookkeeping to every round.

The current engine is already dense enough. The right answer is to deepen pressure, not widen procedure.

## Proposed Additions

## 1. Hold Fast

This is the missing baseline defensive choice.

### Rule Text Draft

**HOLD FAST:** Fast action. You give up ground slowly and focus fully on staying alive. Until the start of your next turn, choose one:

- gain `+1` to **PARRY**
- gain `+1` to **DODGE**

While you HOLD FAST, enemies also need one extra `⚔️` to **SHOVE**, **DISARM**, or **GRAPPLE** you.

The effect ends early if you:

- `RUN`
- `CHARGE`
- `SHOOT`
- or make any slow attack action

### Why It Helps

This adds a real defensive posture without creating another mini-game.

It makes these scenes work cleanly:

- duelist buying a heartbeat
- shieldman holding a doorway
- wounded fighter trying not to die before help arrives
- rear-guard action during retreat

### Why It Does Not Break Existing Talents

It does not replace `DEFENDER` or `FAST FOOTWORK`. Those talents still win on repeated reactions, free reactions, and stronger numbers.

This is only a baseline choice.

## 2. Brace

This is the missing spear-and-polearm drama rule.

### Rule Text Draft

**BRACE:** Fast action. Requires a `POINTED` weapon with `POLEARM` or `LONG-REACH`.

You set your weapon and wait for the enemy to come on. Until the start of your next turn, the first enemy who moves into your reach by `RUN`, `CHARGE`, `RETREAT`, or a successful `MOVE` roll to cut distance triggers an immediate `STAB` attack from you.

This attack:

- happens before the enemy's attack resolves
- does not cost another action
- can be `PARRIED` or `DODGED` as normal

If the BRACE attack deals any `🩸`, the target must stop where the attack caught them unless they spend `1 WP` to press through.

You cannot both **BRACE** and **INTERCEPT** in the same round.

### Why It Helps

This gives long weapons a dramatic battlefield identity without rewriting the reach engine.

It creates authentic moments:

- spear receiving a rush
- halberd stopping a reckless swordsman
- pike wall making a mounted charge feel dangerous

### Why It Stays Manageable

This is one trigger, one attack, one sentence of consequence.
It does not create a second reaction economy.

## 3. Lock Shields

This is the missing low-level formation rule.

### Rule Text Draft

**LOCK SHIELDS:** Fast action. Requires a shield and at least one ally in the same zone also using a shield and taking this action.

Until the start of your next turn:

- ranged attacks against you and the participating allies suffer `-1`
- enemies need one extra `⚔️` to **SHOVE** any of you
- if an enemy moves into *arm's length* with one of you, they are considered engaged with all of you who locked shields

The effect ends for any participant who:

- `RUNS`
- `RETREATS`
- falls prone
- or makes a `SHOVE`

### Why It Helps

This adds basic shield-line logic without needing facings, grids, or exact adjacency.

It supports:

- hall fighting
- shield walls
- bodyguard play
- raiders holding a breach

### Why It Belongs In Core

This is too basic and too genre-central to live only behind talents.
Talents should improve line-fighting, not create it from nothing.

## 4. Morale, Rout, And Surrender

This should be an optional but strongly recommended module.

### Rule Text Draft

**MORALE CHECKS (OPTIONAL):** Kin, beasts, hirelings, and ordinary NPC foes do not always fight to the death.

Make a `MORALE` check for a side when one of these happens:

- its leader is Broken or killed
- half its fighters are Broken, dead, or have fled
- it suffers a fear effect, monstrous display, or catastrophic injury in plain sight
- it is clearly outmatched and has no path to victory

Roll `INSIGHT` for disciplined or fanatical foes, `MIGHT` for savage ones, or `ANIMAL HANDLING` for trained beasts. The GM rolls once for the side's leader or best fighter.

On a failure, the side must immediately choose one:

- fall back and attempt to flee
- throw down weapons and surrender
- cower, bargain, or break formation

Monsters, undead, demons, and true zealots are usually immune unless a specific stat block says otherwise.

### Why It Helps

This is the single biggest drama gain in the proposal.

It makes space for:

- prisoners
- negotiations at swordpoint
- chases after a broken enemy
- ugly victories that stop before extermination
- battlefield fear mattering outside horror tables

It also reconnects `SOCIAL CONFLICT` to violent conflict instead of leaving them as mostly separate modes.

## Things Missing But Not Recommended For Core Right Now

These are real design spaces, but they should not be added in this pass.

### Called shots

They sound authentic, but in this manuscript they would mostly duplicate:

- damage-type critical tables
- weapon features
- `COMBAT EXPERIENCED`
- specific weapon talents

They would add procedure faster than they add drama.

### Universal bleeding rules for all wounds

The game already has strong injury pressure. Making every meaningful hit cause bleed tracking would add recurring bookkeeping and would push too much of the game's danger into timers instead of immediate action choice.

Specific bleeding rules through criticals, spears, monsters, and magic are enough.

### Full hit-location or armor-zone rules

Helmets already add head protection drama. Going further would slow the game and complicate equipment too much for the current engine.

### Round-by-round fatigue

The game already has attrition through pushed rolls, conditions, broken attributes, and injuries. Combat fatigue as its own universal track would duplicate existing pressure.

## Integration Notes

## Chapter 5

This proposal belongs primarily in `corebook/05-combat-and-damage.md`.

Add:

- `HOLD FAST` under fast actions
- `BRACE` under fast actions or the long-reach section
- `LOCK SHIELDS` under shields or fast actions
- `MORALE CHECKS` near `FLEEING THE CONFLICT` or just after `SOCIAL CONFLICT`

## Chapter 4

Talent check:

- `DEFENDER` and `FAST FOOTWORK` remain valuable
- `PATH OF THE SHIELD` still does things no core shield-line rule does
- `COMBAT EXPERIENCED` still owns aggressive stunts
- polearm users gain more identity without requiring new talents

## Chapter 10

No gear rewrite is strictly required, but the proposal makes these items feel better:

- shields
- long spears
- pikes
- halberds
- poleaxes

That is a sign the additions fit the manuscript rather than fight it.

## Audit Verdict

### Accept now

- `HOLD FAST`
- `BRACE`
- `MORALE CHECKS`

### Accept with simplification

- `LOCK SHIELDS`

This is worth doing, but only if kept abstract and zone-based. The moment it starts asking where exactly everyone stands, it becomes the wrong rule for this engine.

### Reject for now

- called shots
- universal bleeding
- hit locations
- fatigue track

## Final Recommendation

If only one thing is added, add `MORALE CHECKS`.

If two things are added, add `MORALE CHECKS` and `BRACE`.

If the chapter gets a fuller combat pass, add all four rules above and stop there. That would make the system feel more like desperate, dirty, premodern fighting without turning it into a simulation exercise.
