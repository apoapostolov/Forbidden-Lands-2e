<!-- markdownlint-disable MD013 MD028 MD012 -->

# Battles & Sieges — Second Pass Proposal

**Date:** 2026-04-25
**Status:** Implementing
**Applies to:** `02-gamemasters-guide/12-battles-and-sieges.md`

---

## Summary

Second-pass audit of the chapter following integration of the first-pass overhaul and 12 campaign vignettes. This proposal identifies:

- missing procedural systems with no resolution checks
- underrepresented areas in authentic medieval war
- voice deficiencies (text too clean, too managerial, consequences described from too far away)
- balance observations and flags

The audit was conducted against the full chapter (post-vignette state, 1300+ lines), the FL2E design skill, and the RPG balance casebook. Changes are being implemented directly alongside this document.

---

## I. Mechanical Gaps Being Implemented

### M1. Morale Roll — Never Formally Defined

**Problem:** The chapter uses "morale roll" or "morale check" more than a dozen times without ever stating what a morale roll is. "The troop must make a morale roll" is used for Death to Cowards aftermath, the commander loss reaction, undead confrontations, and ordered retreat. Each GM must independently decide what this means. Inconsistency guaranteed.

**Fix:** Add formal morale roll definition inside the Morale Points section, directly before Death to Cowards — the first rule that requires a morale roll.

**Definition:** Roll the troop's current base dice. Each result of 1 removes that die permanently — those soldiers have broken and fled. Cannot be pushed. Morale points cannot be spent to nullify results (morale points protect during the battle roll; the morale roll is a cohesion test under separate pressure).

**Interaction with existing rules:** "Roll with only 1s applying" language already in the chapter (battle events tables) is now consistent with this definition. Starvation/duress conditions affect the battle roll specifically; the morale roll always uses only 1s.

---

### M2. No Quarter Declaration

**Problem:** Death to Cowards exists (execute your own fleeing men). The mirror — declare no prisoners against the enemy — does not. Both were real decisions in medieval warfare. The chapter is asymmetric: you can punish your own soldiers but the text has no rules for what happens when you tell your army the enemy will receive none.

**Fix:** Add "No Quarter" subsection after Death to Cowards (and its vignette), before Troop Regrouping.

**Mechanics:**

- Enemy troops that learn of the declaration gain the Fighting for Survival advantage die
- After battle: all enemy prisoners are executed unless order is reversed
- Reversing mid-battle: Demanding PERFORMANCE roll; failure means soldiers don't stop
- Future consequence: enemy commanders treat surrender offers as worthless; garrisoned defenders fight to the last

**Vignette:** Vara's declaration at the north tower. Twelve defenders. Four expected casualties. Nine actual casualties. Vara did not say it had been a mistake.

---

### M3. Ordered Retreat

**Problem:** The chapter has Feigned Retreat (a tactic, cavalry/skirmisher only) and implicit rout (morale collapse). There is no rule for a general deliberately withdrawing the army from the field to preserve it. This is arguably the most common decisive action in medieval warfare — the tactical retreat that saves an army for the next campaign. The Pursuit section implies it from the other side but never provides the rule for the retreating general.

**Fix:** Add "Ordered Retreat" subsection after Pursuit (and its vignette), before Special Combat Conditions.

**Mechanics:**

- General makes Demanding PERFORMANCE roll
- Each success holds one section in good order
- Unhelded sections make morale rolls as they fall back (permanent die loss on 1s)
- Zero successes: total rout, every section makes morale roll, army requires 1D6 days to reorganize
- Army loses all accumulated morale points but retains surviving troops
- Rearguard option: any section may be sacrificed to fight while rest withdraws

**Vignette:** Torkel's second engagement, four successes, rearguard of thirty left at tree line, eight came back that evening, Torkel's wine ration distributed.

---

### M4. Victory Conditions

**Problem:** The chapter never states what ends a battle. The implication is the destruction of all enemy troops, but a battle that ends because the enemy routs, or because darkness falls, or because a general concedes before total destruction, is a different outcome with different consequences. No guidance is given. GMs must infer everything.

**Fix:** Add "Victory and Defeat" subsection after Ordered Retreat.

**Conditions:**

- Rout: all active first-line troops destroyed or fled, reserve must advance or army concedes
- Concession: general calls Ordered Retreat or surrenders
- Night pause: battle stops at sundown, not a concession, resumes unless one side withdraws
- Siege fall: defenders no longer hold any wall section connecting interior to exterior, or formal surrender

---

### M5. Surrender Procedure

**Problem:** Ransoms exist. Formal surrender does not. There is no procedure for how a battle or siege formally ends through capitulation — what the general does, what it costs, what the victor can demand. The Prisoners and Ransom section covers the administrative aftermath but the act of surrendering has no rules.

**Fix:** Add "Surrender" subsection after Victory and Defeat.

**Mechanics:**

- Field surrender: white banner, all troop rolls cease, enemy decides to accept or continue
- Garrison surrender: messenger requests terms, 1D3 day negotiation, blockade continues during
- Terms: victor sets minimums (weapons, prisoners, fortress); additional terms extracted from the gap between desperation and refusal
- After inner breach: no further terms offered at GM discretion

---

### M6. Prisoners Without Ransom Value

**Problem:** The Prisoners and Ransom section lists copper values for Important Characters and named officers. Common soldiers with no ransom value are not addressed. The decision — release, labor, press, or execute — was one of the most consequential choices a general made after a battle in actual medieval warfare. Absent from the chapter entirely.

**Fix:** Add "Prisoners Without Ransom Value" subsection after the Vidar ransom vignette.

**Options:**

- Release on oath: costs nothing, worth the credibility of the man swearing
- Forced labor: supply reduction, continuous security risk
- Press into service: MANIPULATION vs. Wits, conditional loyalty, desertion likely
- Execute: clean, permanent, remembered by every army that hears about it; most soldiers don't carry it long

**Vignette:** After Krymark falls, 39 common soldiers, no value. Torkel takes their boots and releases them. Notes that this was the generous outcome because he had enough food to be generous, which was the part rarely in the songs.

---

### M7. Siege Tower Completion Condition

**Problem:** The Battering Ram has a clear resolution: "breaks the gate if all siege dice succeed." The Siege Tower says it "allows infantry to reach the wall top directly" — but there is no rule for when this happens or what changes. A siege tower that reaches the wall should have mechanical effect; currently it doesn't resolve to anything.

**Fix:** Add resolution condition to the Battering Rams and Siege Towers paragraph.

**Mechanic:** Cumulative successes equal to the target wall section's current advantage dice = tower contact. From that turn, the wall's attack-first quality and high-ground advantage dice no longer apply against the ascending troop.

---

### M8. Sortie Rules

**Problem:** Sorties are referenced in three vignettes (Holk's catapult vignette, siege blockade language, and the second Krymark sortie) but have no formal rules. When defenders send troops outside to attack a siege engine, how does this resolve? What roll? What counts as reaching the engine? What damage results?

**Fix:** Add "Sorties" subsection after Repairing Defenses.

**Mechanics:**

- Open-field battle, normal rules, no wall bonuses either side
- Win by 2+ successes to reach the target
- Engine damage: roll sortie base dice, each success strips one attack/siege die from the engine
- Engine at zero dice: destroyed, must be rebuilt from scratch
- Cost: every soldier outside is a soldier off the wall; besieging reserve troop may advance that turn

**Vignette:** Vidar's second sortie, day 18, twenty light soldiers, not for the catapult but for the crew. Reached the machine. One attack die stripped. Two engineers killed — one not Holk. Eight of twenty came back.

---

### M9. Commander Flight Consequence

**Problem:** No rule for what happens when a general's own troop is destroyed or routs. Medieval commanders sometimes fled with their troops; this was often decisive. The chapter treats the general as a strategic resource but has no consequence for the general's personal position being compromised.

**Fix:** Add commander flight rule to Commander Movement section.

**Mechanic:** If general's troop is destroyed or routes: Hard INSIGHT roll. Failure = flees with troop. Success = transfers to adjacent surviving section. A general who flees removes all speech-granted morale from every section AND removes the "Important Character present" advantage die from every section immediately.

---

## II. Voice Rewrites Being Implemented

### V1. Stripping the Dead

**Problem:** Current text is accurate and mechanical. "These are weapons, fragments of armor, coins, tools, and whatever the dead were carrying." This is an inventory list. The actual practice of stripping a battlefield was physically specific, practically motivated, and morally indifferent in ways the current prose does not convey.

**Rewrite:** What comes off first (boots), the logical order of the work, what doesn't survive (bent swords, split helmets), and the practical indifference of the people doing it.

---

### V2. Village Contributions — Percentage Death

**Problem:** "Roll a D6. The result is the percentage of the village's population that dies of starvation that week." Clean, mechanical, distant. Stays at the abstraction level. The chapter's supply section is mostly written from the general's eye: numbers, logistics, decisions. This consequence needs one concrete passage that gives the number a human scale.

**Rewrite:** D6 result of 4 against 200 people = 8 dead. Who they are. When the army is already gone. The village remembers.

---

### V3. Prisoners Without Ransom Value — Execute Option

**Problem:** The "execute" option in the new Prisoners section needed to be written with the same unapologetic directness as the chapter's other hard passages. "Executing common prisoners after a battle is not remarkable in the Ravenlands." Should land without apology or editorial judgment — the chapter's register throughout has been descriptive, not prescriptive. This passage must match that.

Handled in M6 implementation.

---

## III. Areas Not Implemented This Pass

The following were identified in the audit as genuine gaps but are deferred for scope and complexity reasons:

### U1. Ambush Rules

A prepared ambush — concealed force, target moving into prepared ground — is meaningfully different from both a night attack and a deployment advantage. Requires a concealment roll, a surprise round (attacker acts before defender assembles), and resolution mechanics. Deferred — needs playtesting to calibrate the surprise advantage correctly without making cavalry irrelevant in difficult terrain.

### U2. Non-Combatants in Sieges

Civilians inside besieged fortresses deplete food, generate political pressure, and could be expelled (with the attacker choosing to let them through or not). This was a constant feature of historical sieges. Deferred — mechanically complex enough to require its own subsection and the starvation math would need rebalancing around civilian consumption rates.

### U3. Field Fortification

Temporary earthworks, trenches, abatis, stakes — prepared positions dug during a campaign rather than constructed as permanent stronghold functions. The Terrain section has "Prepared Ground" for cavalry but permanent structure is the only formal option for serious defense. Deferred — fits naturally into an engineering expansion.

### U4. Post-Battle Disease

Armies camping on a battlefield or occupying ground with large numbers of unburied dead should check for disease. Currently disease is a siege-only mechanic. Deferred — can be appended to the Disease section cleanly once siege disease rules are playtested.

### U5. Mercenary Mid-Campaign Renegotiation

Mercenaries renegotiating terms mid-campaign, switching sides, or demanding advance payment after a victory. The Salaries section covers payment failure but the specific case of mercenary loyalty pressure during active operations is absent. Deferred — belongs in a dedicated mercenary faction pass.

---

## IV. Balance Audit

### Probability Baseline

The battle dice system uses D6 pools. Results of 6 = success (damage). Results of 1 = demoralization on base dice. All other results = nothing.

**Per die:**

| Result | Probability | Effect |
|---|---:|---|
| 6 | 16.7% | Success (1 damage if uncanceled) |
| 1 | 16.7% | Demoralization (morale loss or removed die) |
| 2–5 | 66.7% | No effect |

**Expected values per die:**

- Expected successes per die: 0.167
- Expected demoralization per die: 0.167

**3 base dice (60-man troop):** Expected 0.5 damage, 0.5 demoralization
**5 base dice (100-man troop):** Expected 0.83 damage, 0.83 demoralization

**3 protection dice (chainmail):** Expected 0.5 absorbed. Against an average-rolling troop (0.5 expected damage), chainmail absorbs all expected damage in most turns. The counter is numbers (more base dice) or siege engines (bypass protection entirely).

---

### Balance Finding 1: Armor Dominates Training at Equal Numbers — Intentional

A chainmail troop (3B, 1A, 3 prot) outperforms a well-trained unarmored troop (3B, 2A, 0 prot) in sustained engagement:

- Chainmail troop takes 0.17 expected damage per turn (0.67 incoming - 0.5 absorbed)
- Naked veteran troop takes 0.5 expected damage per turn

The chainmail troop also deals more damage per turn because it's not being attrited as fast.

**Verdict:** Intentional. Equipment cost (chainmail = 10 copper/unit/day vs. training requiring months) correctly reflects the historical reality that armor mattered more in the field than an individual's skill level. The system does not lie about this. It should not.

---

### Balance Finding 2: Veterans D12 — Flag for Future Pass

Veterans upgrade advantage dice: D6 → D8 → D10 → D12. The probability difference is significant:

| Die | P(success) | Relative to D6 |
|---|---:|---:|
| D6 | 16.7% | baseline |
| D8 | 37.5% | +125% |
| D10 | 50.0% | +200% |
| D12 | 58.3% | +250% |

A troop with 5 D12 advantage dice averages 2.92 advantage successes per turn. Against a troop with 5 D6 advantage dice (0.83 successes), the D12 troop cancels all opponent advantage AND deals 2.08 additional damage per turn. This is decisive. Combined with first-morale-check immunity, a D12 veteran troop is very difficult to break through attrition.

**Flag:** The current text does not cap Veterans advancement at D10. Consider whether D12 should be restricted to elite unit types (Iron Guard, Elite Dwarven Warriors, Griffon Riders) rather than achievable by any human infantry with enough survived engagements. This is a campaign-pacing question rather than a turn-by-turn balance issue. **Not implementing this pass** — requires discussion of campaign length assumptions.

---

### Balance Finding 3: PERFORMANCE Dependency — Flag

A general uses PERFORMANCE for:

- General's Speech (morale generation)
- REGROUP / Troop Regrouping rally
- Feigned Retreat (now: also Ordered Retreat)
- Night attack coordination (SCOUTING, not PERFORMANCE)

A general who maximizes PERFORMANCE dominates all of these subsystems simultaneously. The counterbalances are INSIGHT (deployment advantage, terrain reading) and SCOUTING (night attack). A pure PERFORMANCE general cannot scout or read terrain.

**However:** PERFORMANCE is available to push in all these rolls. INSIGHT is used in opposed rolls where pushing exposes the general to bane risk during the most important pre-battle moment. This creates a mild PERFORMANCE preference in character build.

**Optional rule flag (not implementing, flagging for consideration):** A general may not push PERFORMANCE more than once per engagement. This limits the upside of the single-skill-dominant build without removing the mechanic.

---

### Balance Finding 4: Disease Inside Sieges — Calibrated

For Vidar's garrison of 60: 1 die at start. On a result of 6, doubles to 2, then 4, then 8.

At 8 dice, expected deaths per week = 8 × (1/6) × 10 = 13.3 soldiers per week. Against a 60-man garrison, this kills the garrison in 4–5 weeks from the time the dice start doubling.

The Sewer function (1,120 copper, 16 days build) prevents doubling. This makes the Sewer the single most valuable defensive investment for a besieged garrison in a long siege. The copper cost is deliberately low relative to walls (800+ copper) — the Sewer is underpriced but undervalued by players because it has no visible combat function. The chapter correctly makes this available.

**Verdict:** Calibrated. The disease system correctly creates the historical condition where garrisons that held too long died of plague rather than battle.

---

### Balance Finding 5: Supply Timing vs. Catapult Window

- Catapult: 14 days build time
- 200-man attacking army: 200 supply units/day
- Pantry (5,000 units): 25 days of food for 200 soldiers

The catapult is finished at day 11–14. The pantry runs out at day 25. The catapult begins stripping wall advantage on day 12–15. Wall advantage is usually 1–2 dice for a standard stronghold. At 1 success/day against 2 advantage dice, the wall advantage is gone by day 13–17. The siege can turn to infantry assault around day 15–17, within the supply window.

A trebuchet (60 days) requires a standing supply line. It cannot be used by an army living off its pantry — 60 days × 200 units/day = 12,000 supply units. This correctly restricts trebuchets to well-supplied, logistics-supported armies (the major powers) rather than a warlord with a single pantry.

**Verdict:** Calibrated. The engine timeline scales correctly with the supply economics.

---

### Balance Finding 6: Tunnel Stability

2D6 successes required (average 7). Starting stability = higher die (average ~4.5). A 3-die troop averages 1.5 successes/day and 0.5 stability losses/day. Expected completion: 7 ÷ 1.5 = ~5 days. Expected stability at completion: 4.5 - (0.5 × 5) = 2. Usually survives, occasionally catastrophic.

Catastrophic failure (tunnel collapse destroying the troop inside) is rare but real. The "troop inside is destroyed" consequence is appropriately severe for what tunnel collapse means in practice.

**Gap identified (M-series):** No rule for an Important Character inside a collapsing tunnel. Does the GM's Important Character die carry on? Are they automatically Broken? The chapter destroys the troop but says nothing about the character.

**Fix (implementing as part of M7/tunnel clarification):** If an Important Character is inside a collapsing tunnel, they are Broken and must roll D6 for the Wounded Important Characters result (as after battle). On a result of 1, they die. The tunnel collapse is equivalent to a troop defeat.

---

### Balance Summary

| System | Assessment | Action |
|---|---|---|
| Base dice economy (5-die cap) | Healthy | None needed |
| Advantage dice cap (= base dice) | Healthy | None needed |
| Armor vs. training tradeoff | Intentional | Document only |
| Veterans D8/D10 | Healthy | None needed |
| Veterans D12 | Watch | Flag for future pass |
| Chainmail effectiveness | Intentional | Document only |
| Cavalry economics (5× cost) | Calibrated | None needed |
| Disease in sieges | Calibrated | None needed |
| Sewer investment value | Calibrated | None needed |
| Supply vs. catapult timeline | Calibrated | None needed |
| Trebuchet logistics requirement | Calibrated | None needed |
| Tunnel stability math | Calibrated | Add IC consequence |
| PERFORMANCE dominance risk | Flag | Optional rule noted |
| Morale roll definition gap | Critical fix | Implementing (M1) |

---

## V. Changelog

| Item | Status |
|---|---|
| M1: Morale roll definition | Implemented |
| M2: No Quarter | Implemented |
| M3: Ordered Retreat | Implemented |
| M4: Victory and Defeat | Implemented |
| M5: Surrender procedure | Implemented |
| M6: Prisoners without ransom value | Implemented |
| M7: Siege Tower completion | Implemented |
| M8: Sortie rules | Implemented |
| M9: Commander flight | Implemented |
| V1: Stripping the Dead rewrite | Implemented |
| V2: Village Contributions voice | Implemented |
| Tunnel collapse IC consequence | Implemented |
| U1–U5: Deferred items | Flagged only |
| Veterans D12 cap | Flagged only |
| PERFORMANCE push optional rule | Flagged only |
