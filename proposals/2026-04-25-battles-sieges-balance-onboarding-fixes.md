# Battles & Sieges — Balance and Onboarding Fixes

**Proposal date:** 2026-04-25
**Chapter:** `02-gamemasters-guide/12-battles-and-sieges.md`
**Status:** Implemented same session

## Summary

24 targeted fixes across three categories: game balance, structural onboarding, and prose trimming. No rules are redesigned. All changes retain intent. All mechanical content is preserved or clarified. The chapter lint remains at 0 errors after implementation.

---

## Issues and Resolutions

| ID | Severity | Section | Issue | Fix |
|---|---|---|---|---|
| H1 | High | Siege Engines | Battering Ram requires all 3 siege dice to succeed in the **same roll** — probability ≈0.46% per turn. Defenders damage the ram before this ever fires. | Change to cumulative model: total of 3 successes across turns breaks the gate. Matches Siege Tower model. |
| H2 | High | Supplies | Foraging says "Sum the results. Multiply by 10" but every other resolution in the system counts only 6s. Reader confusion guaranteed. | Explicit callout: "Add all die results together — every result counts, not just 6s." |
| H3 | High | Ranged Troops | Friendly Fire punishes results of 1 on **advantage dice**, but advantage die 1s have no effect anywhere else in the system (they simply don't count as successes). Creates unique consequence for 1s that exists nowhere else. | Tie friendly fire penalty to base dice only, consistent with how 1s work everywhere. |
| M1 | Medium | Ranged Troops | "do not lose morale from results of 1" — ambiguous: does demoralization not trigger, or does it trigger but is free to absorb? | Rewrite: "results of 1 on their base dice do not trigger demoralization." |
| M2 | Medium | Ambush | "cannot use its speed advantage" — undefined term. No mechanic called "speed advantage" exists. Skirmishing cavalry has "mobility advantage" (defined). Standard cavalry in broken ground already loses attack roll from Terrain rules. | Replace with: "loses its attack roll for the first two turns"; add that skirmishing cavalry also loses mobility advantage. |
| M3 | Medium | Troop Dice | "Veterans waive the first morale check" — does waive mean skip the roll or automatic success? Can matter for rules that track whether a roll was made. | Rewrite: "automatically pass." |
| M4 | Medium | Sieges | Blockade ratio "three to one" doesn't specify unit of measurement — soldiers, base dice, or sections all produce different answers. | Specify: "three soldiers for every one soldier in the defending garrison." |
| M5 | Medium | Order of Battle | "re-enter when ordered" leaves no procedure for how a withdrawn troop re-enters — no roll, no turn cost, no restriction specified. | Add: general may order re-entry at the start of any subsequent turn, no roll required, troop cannot fight the same turn it advances. |
| M6 | Medium | Battle Sequence | Troop Regrouping: Important Character roll skill not specified. General uses "PERFORMANCE or MANIPULATION" but IC roll is just "roll separately." | Add: "PERFORMANCE or MANIPULATION, the same as the general." |
| M7 | Medium | Siege Engines | Siege Tower tracks against wall section's "current" advantage dice. If catapult strips wall to 0, tower completes immediately at 0=0 on first turn — never needs to be built. | Change "current" to "original" — tower tracks against wall's original height regardless of catapult damage. |
| M8 | Medium | Battle Sequence | General's Speech push: "every 1 on a push is a failure that the troops will remember" — flavor with no mechanic. Push consequences need to be rules, not atmosphere. | Concrete consequence: each result of 1 on any pushed die removes 1 morale point from any one troop of the general's choice. |
| L1 | Low | Battle Sequence | Death to Cowards loyalty check triggers "at the start of the next session" — the only mechanic in the chapter that crosses real-world session structure rather than in-game time. | Change to "within 1D3 days following the battle." |
| L2 | Low | New Talents | Chief of Riders Rank 2 jumps D8 → D12, skipping D10. Veterans use D6→D8→D10→D12. No note clarifying the skip is intentional. | Add: "D10 is intentionally skipped" to prevent table argument. |
| L3 | Low | Example Units | Dwarven Crossbowman: "Dwarf infantry when switched to melee weapon (+1)" — makes the Dwarf advantage conditional on weapon, contradicting the advantage table which lists Dwarf unconditionally. | Remove conditional: "Dwarf (+1)." |
| L4 | Low | Terrain | River Crossing: "on the crossing turn only. Once across, they roll normally" — doesn't say how long a crossing takes. | Add: "A crossing takes one battle turn." |
| L5 | Low | Special Combat | Feigned Retreat: "requires a capable officer present in the troop" — undefined game term. | Replace with: "an Important Character present in the troop." |
| O1 | Onboarding | Battle Sequence | "morale points" first used in General's Speech with no definition. Defined fully three sections later. | Add forward reference: "see Morale Points below for how they work." |
| O2 | Onboarding | Battle Sequence | Battle Surrender and Siege Surrender and Parley are separate sections; no cross-reference connecting them. | Add sentence at end of battle Surrender: "For surrender negotiations during an ongoing siege, see Surrender and Parley under Sieges." |
| O3 | Onboarding | Stronghold | "Income is calculated weekly." repeated in consecutive sentences (once at end of first paragraph, once at start of next). | Remove duplicate opening sentence from second paragraph. |
| P1 | Prose | Village Contributions | The D6 mortality rule paragraph runs five sentences past its mechanical content into atmospheric commentary. Rules voice ends at "eight dead." The rest is padding. | Trim to: "A result of 4 against a village of two hundred people is eight dead. The village will remember." |
| P2 | Prose | Village Contributions | Deterioration paragraph restates what the limits already established, then tells the GM what the rules already imply. "Taking more is possible" adds nothing — the limits are already stated as limits. | Trim to one sentence of consequence. |
| P4 | Prose | Battle Sequence | Deployment: "at least until the condition is met" — vague. No "condition" is referenced. Creates an open rule question. | Remove the trailing clause: "any advantage that does not apply to every soldier in that troop is lost." |
| V1 | Voice | Battle Sequence | Morale Points vignette: "This calculation was correct. It was not a calculation he had made quickly" — "calculation" doubled in three words. | Rewrite: "He had not made it quickly." |
| V2 | Voice | Aftermath | Aftermath opening: "The routing troop abandons the field" — assumes route as the only battle end condition. Battles also end by concession, night, or siege fall. | Broaden: "The fighting ends — by rout, concession, or nightfall." |

---

## Notes on Non-Obvious Fixes

**H1 — Battering Ram model change.** The all-in-one-roll requirement is a mathematical dead end. The battering ram has 3 siege dice; defenders damage it by scoring successes, and results of 1 on siege dice absorb damage. In practice the ram is destroyed in 2–3 turns before the gate breaks. Changing to cumulative successes preserves the feel (the ram chips away at the gate over time) and makes it a viable option against defenders without engineer support. The total required is still 3, which matches the starting siege dice count.

**M7 — "original" vs "current" advantage dice.** Changing "current" to "original" for siege tower tracking makes catapults and towers fully independent systems. A catapult strips defensive advantage; a tower physically scales the wall. They serve different functions and should not shortcut each other. If catapult strips the wall and then a tower scales it, the fight at the top still happens — the catapult just means defenders arrive there with fewer dice.

**L1 — Session boundary.** The rule works the same whether it fires at session start or after 1D3 campaign days. The session-based trigger was editorial convenience, not design intent. In-game time makes the chapter internally consistent.
