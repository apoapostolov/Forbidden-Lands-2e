# Army Muster, Maintenance, and Field Rosters Proposal

**Status:** Proposal
**Target:** `02-gamemasters-guide/11-politics-of-the-forbidden-lands.md`
**Related chapter:** `02-gamemasters-guide/12-battles-and-sieges.md`

---

## The problem

Chapter 11 already knows how a faction calls levy, hires mercenaries, raises stores, and enters `Muster` or `Campaign`. Chapter 12 already knows how troops fight once battle begins.

What is missing is the layer between those two truths.

Right now there is no persistent army record in Chapter 11. A faction can raise contingents, but it cannot cleanly keep a named host in being across several turns, note where that host is on the map, track who commands it, mark how it is being fed, or record when it is beginning to fray from long service, poor pay, and bad roads. The premade factions therefore have forces in principle but not actual field rosters.

That gap matters because most wars in the Ravenlands are decided before the first battle roll. They are decided by whether a host can be gathered at all, whether it can stay together for a second week, whether it reaches the field late, and whether it returns home still recognizably under command.

## Design targets

The added system should do five things.

1. Give the faction sheet a clear place to record armies at disposal.
2. Give every active army its own roster that can persist across turns.
3. Add at least two recurring army procedures in Chapter 11: one for provisions and one for maintenance.
4. Make army travel playable on the campaign map without inventing a second movement engine.
5. Give the premade factions ongoing rosters that reflect the actual military weight they can keep in motion.

## Design decisions

### 1. Do not build a second war game

Chapter 12 already contains troop math, battle lines, supply units, movement pace, and siege procedure. The new Chapter 11 material should not replace those rules.

Instead, Chapter 11 should answer these questions before Chapter 12 starts:

- which armies exist
- which troops are in them
- where they are
- who commands them
- how they are fed
- how they are paid or otherwise held in service
- what strain they are already carrying into battle

### 2. Treat armies as persistent rosters, not single rolls

A successful `Call Levy` roll should no longer end with "the faction has troops now" as an abstract truth.

It should instead produce or reinforce a named army roster.

That roster should hold:

- army name
- commander
- base
- current position
- current duty
- supply line
- weekly provision load
- weekly pay load
- weeks in the field
- unpaid weeks
- hungry weeks
- the actual battle forms used in `BATTLES & SIEGES`

### 3. Keep army scale modest

The Ravenlands should not drift toward giant imperial field armies as a normal case.

The common military bodies should be:

- garrisons and road guards
- small raid columns
- small or middling field hosts
- only rare great hosts for Alderstone, Stonegarden, Zertorme at full call, or similar campaign-defining events

Most rosters should sit at roughly two to five Chapter 12 troops. Anything larger should be rare enough to feel like a real change in the state of the land.

### 4. Use existing pillars to limit army sprawl

`Reach` should decide how many armies a faction can keep moving without becoming confused and late.

That uses an existing pillar instead of inventing a new command-stat or army-cap track.

### 5. Use load bands in Chapter 11, exact math in Chapter 12

Chapter 11 should not ask the GM to do full daily arithmetic for every host on every turn.

It should use rough weekly bands such as `Light / Heavy / Crushing` for provision load and pay load. Once Chapter 12 begins, the exact troop math and daily supply rules already in that chapter take over.

This keeps Chapter 11 fast enough for faction play while still preserving a clean handoff into battle.

## Proposed Chapter 11 additions

### Faction sheet expansion

Add an `ARMIES AT DISPOSAL` block to the faction sheet so the main sheet can always answer:

- what standing armies and garrisons exist
- what muster hosts or raid columns are in the field
- what bases, routes, and burdens they depend on

### New section: `Armies at Disposal`

Add a new core section after `Retainers, Levy, and Mercenaries`.

That section should contain:

1. **What an army is** — the difference between a contingent and a kept field force.
2. **Army scale in the Ravenlands** — guidance for garrisons, small hosts, field hosts, and rare great hosts.
3. **Army commands and Reach** — how many separate armies a faction can keep moving cleanly.
4. **The army roster** — a reusable record format.
5. **Forming, joining, and dismissing armies** — how levy, retainers, and mercenaries become a named host.
6. **Provisions** — weekly feeding and supply pressure.
7. **Maintenance** — weekly pay, discipline, remount, and service strain pressure.
8. **Army travel** — weekly movement using the existing `BATTLES & SIEGES` pace rather than replacing it.

### New recurring procedures

#### Provisions

Run once per active army each campaign week, and for any standing army kept away from base in other modes of rule.

Use `Hearth + Provision` or `Reach + Relay`.

Possible outcomes:

- the army is properly fed
- it keeps a reserve week in hand
- it feeds itself by worsening burden in a supplying settlement
- it becomes hungry and carries that state forward to Chapter 12

#### Maintenance

Run once per army kept in being.

Use `Mandate + Discipline` or `Hearth + Provision`, with `Treasury` backing when coin is the real answer.

Possible outcomes:

- the army stays together cleanly
- unpaid weeks begin to accumulate
- levy goes home
- a troop loses quality edge or morale before battle
- Mandate or Force is damaged by grievance, desertion, or visible disorder

### New travel bridge

Do not invent a fresh map scale.

Instead:

- derive weekly army travel from the existing `BATTLES & SIEGES` quarter-day rates
- make the slowest element set the host's pace
- make wagons and siege engines matter
- call for a travel roll only when road control, concealment, timing, or hostile ground actually matters

Anchor the weekly table to **10 hexes** for a foot host on good ground. That reflects five real travel days and two more lost to logistics, stragglers, baggage, crossings, and getting a large armed body to move as one. Recalculate the rough-ground, winter, and mounted values from that anchor rather than preserving the earlier 7-hex pace.

## Proposed premade-faction changes

Each premade faction should gain an `Armies at Disposal` block with named ongoing rosters.

These should not all be full field armies. Some should be:

- seat garrisons
- rider screens
- punitive columns
- watch circuits
- shrine escorts
- forest wards

That keeps the roster truthful to the setting and gives the GM immediate usable forces instead of only a list of possible bodies.

## What stays in Chapter 12

Chapter 12 should keep ownership of:

- troop dice
- morale points in battle
- exact daily supply rules
- siege engines
- battlefield movement and conditions
- battle events

The new Chapter 11 layer should only prepare armies for that chapter and carry consequences back out of it.

## Recommended implementation order

### Phase 1

Integrate the persistent army layer into Chapter 11:

- faction-sheet block
- `Armies at Disposal` section
- army roster
- provisions procedure
- maintenance procedure
- army travel guidance

### Phase 2

Add army rosters to the premade factions.

### Phase 3

If needed in a later pass:

- add one worked army example in Chapter 11
- add one explicit cross-reference in Chapter 12 back to army rosters
- add optional faction-to-battle conversion examples for a levy host, a mercenary host, and a cult host

## Promotion standard

This proposal is ready for promotion when Chapter 11 can do all of the following without GM invention:

- keep a named host in being across several turns
- show how that host is fed and maintained
- move that host across the map
- hand that host into Chapter 12 without rebuilding it from scratch
- show at a glance what armies the premade factions already have on foot
