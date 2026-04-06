ry<!-- markdownlint-disable MD013 -->

# Audit: Ranged Weapon Rebalance and HEMA Properties

## Scope

This document audits four proposals as a group before any of them are promoted to the manuscript:

- [proposal-ranged-weapons-plug-and-play-rebalance.md](proposal-ranged-weapons-plug-and-play-rebalance.md)
- [proposal-ranged-weapons-plug-and-play-rebalance-acceptance-summary.md](proposal-ranged-weapons-plug-and-play-rebalance-acceptance-summary.md)
- [proposal-missing-weapon-properties-hema-review.md](proposal-missing-weapon-properties-hema-review.md)
- [proposal-ranged-talents-balance-follow-up.md](proposal-ranged-talents-balance-follow-up.md)

The current manuscript weapon table and talent text were verified before this audit. Proposals have not yet been implemented.

---

## I. Ranged Weapon Table Rebalance

### What It Does

It removes one Gear Die from eight weapons. No new rules, no new features. The framing — correcting inflated baselines — is correct. The problem is real.

Bows at `+2` and crossbows at `+3` mean heavy talent investment stacks onto an already bloated base. That compresses the mathematical space between an untalented archer and an archer build. The nerf direction is right.

### What It Gets Right

**Bows to `+1`.** A Short Bow at `+1` / Damage 1 / Short is not a strong standalone weapon — and that is correct. Bows derive their value from the talent platform: `FAST SHOOTER`, `SHARPSHOOTER`, `BOWYER`, `HORSEBACK FIGHTER`. Players who invest the talent costs get the payoff. Players who do not invest carry a niche situational tool. That is the right tradeoff for a ranged weapon in a melee-dominant combat system.

**Light Crossbow range correction.** Moving Light Crossbow from Short to Long is the most meaningful change in the proposal. At `+2` / Damage 2 / Long post-nerf, the Light Crossbow becomes the accessible military shooter: slower than a bow, easier to use well at distance. The current Short range forces users into positions that negate the weapon's core value.

**Throwing Axe to `+1`.** Throwing Axe at `+2` / Damage 2 / Near is an outlier not because `+2` is too many dice in isolation, but because `THROWING ARM` explicitly stacks with `AXE FIGHTER`. Lowering the pool from `+4` effective (weapon + TA + AXE FIGHTER) to `+3` is a modest but genuine compression.

### Critical Gap: Composite Bow Is Not Addressed

The `Ch10` gear table hardcodes `Composite Bow` at `+3`, Damage 1, Long, 40 silver.

The crafting rule explains why: "They gain +1 weapon die and increase their range in one category" — applied to a Short Bow currently at `+2`, that equals `+3`.

If Short Bow drops to `+1`, the derived post-upgrade value should be `+2`. But without explicitly updating the table entry, the result post-implementation would be:

| Weapon | Bonus | Damage | Range | Cost |
|---|---|---|---|---|
| Short Bow | +1 | 1 | Short | 6 |
| Recurve Bow | +1 | 1 | Long | 12 |
| **Composite Bow** | **+3** | **1** | **Long** | **40** |
| Light Crossbow | +2 | 2 | Long | 24 |

A Composite Bow at `+3` / Damage 1 / Long would be three times the gear bonus of a regular bow and on par with pre-nerf crossbows. The `BOWYER` talent at rank 4 lets you craft Composite Bows with Weapon Bonus up to three points above normal base value — applied to a `+3` pre-existing table entry, that is a theoretical `+6`. This is not a hypothetical edge case; it is a direct consequence of accepting the bow rebalance without adjusting the derived table entry.

**Required fix, non-negotiable:** When the proposal is implemented, the Composite Bow table entry must drop to `+2`. The crafting rule text (Short Bow → upgrade → +1 weapon die) does not need to change; the result of applying that rule at the new baseline is the fix.

### Blowgun Creates an Inverted Hierarchy

Post-proposal, `Short Bow` sits at `+1` / Damage 1 / Short / 6 silver. `Blowgun` is `+2` / Damage 1 / Short / 3 silver.

The proposal leaves Blowgun unchanged. After implementation, Blowgun unambiguously outperforms a Short Bow in raw gear bonus at half the cost. The Blowgun's sole defensive disadvantage is the `Armor Rating x2` property — two complete layers of armor are fully effective against it.

This is not catastrophic. But the proposal creates a hierarchy inversion and does not acknowledge it. Either Blowgun drops to `+1` in the same pass, or the inconsistency should be documented as a deliberate tradeoff.

> User comments: I prefer the +1.

---

## II. Acceptance Summary Critique

The summary accepts all eight changes, defers bow consolidation, talent interaction cleanup, and the throwing knife/spear melee taxonomy. It rejects spreading `Might` requirements to more weapons.

**The rejection of Might-gating is correct.** Adding a Strength/Might requirement to more weapons ripples into every talent, kin modifier, and profession that touches those weapons. The War Bow already demonstrates how much text that rule requires. The proposal is right to keep gating exceptions narrow.

**The deferral of talent interaction cleanup is the riskiest decision in this proposal suite.** The summary argues that base table changes should be tested before touching talents. That logic is sound in principle. In practice, the Light Crossbow range correction plus `FAST SHOOTER` rank 4 creates a specific problem that does not need playtesting data to evaluate — it can be analyzed now. Deferring the talent fix while deploying the range fix accepts a live known problem. See Section IV for the full analysis.

**The Composite Bow gap is not mentioned anywhere in the summary.** This is a documentation failure with real downstream consequences.

---

## III. HEMA Weapon Properties

### FLEXIBLE — Accept as written

Reducing the opponent's shield `PARRY` bonus by 1 against whip and bladed whip attacks is correctly calibrated. It does not nullify shields. With `WHIP FIGHTER` rank 1 giving `+1`, the net against a shielded opponent is mild. If the opponent also has `DEFENDER` rank 1 (`+1` to all PARRYs), `FLEXIBLE` cancels it back to baseline rather than creating advantage. The rule layers cleanly.

No synergy concerns. No blocking issues.

### SMASHING — Accept with the stated narrow scope, flag a synergy

The `3+⚔️` trigger for 1 damage to armor/weapon/shield is expensive probability. Restricting `SMASHING` to `Heavy Warhammer`, `Two-Handed Flail`, and `Rust Censer` keeps it off dual-purpose weapons and prevents a light weapon from both hitting normally and destroying defenses cheaply.

One synergy worth naming for playtesters, even though it does not block acceptance:

`HAMMER FIGHTER` rank 2 guarantees at least 1 point of damage to the enemy even if armor absorbs all damage. `SMASHING` adds 1 damage to the armor item on `3+⚔️`. These are independent effects against different targets and do not double-count. But a `HAMMER FIGHTER` Heavy Warhammer user simultaneously guarantees minimum HP damage, degrades equipment on big swings, and can add `HEAVY WEAPON FIGHTER` as a third stacking option. The combination is powerful, but that is correct for full talent investment.

Flag for playtest. Not a blocker.

### HALF-HAND — Accept with an additional constraint required

The accepted version needs a tighter ruling on the interaction with `CUT IN`.

`CUT IN` is a FAST action plus a MOVE roll to close against an enemy with longer reach. It has failure risk — fail the roll and you stay at distance, exposed. `HALF-HAND` as a FAST action with no roll requirement bypasses that risk entirely. A Bastard Sword user versus a spearman would go from a FAST action plus a dice risk to a guaranteed FAST action repositioning effect.

This does not obsolete `CUT IN` entirely — other weapons still need it, and `INSIDE THE GUARD` keys off `CUT IN` explicitly — but it removes the tension point from the weapon most likely to use `HALF-HAND`.

**Required constraint:** `HALF-HAND` should only function when already at near or arm's length range. It lets you maintain a shortened grip inside someone's reach; it does not let you enter that range without contest. `CUT IN` still does the risky work of closing, and `HALF-HAND` becomes the reward for having already succeeded.

As currently written in the proposal, `HALF-HAND` slightly undermines the reach combat subsystem. The fix is one sentence: "You must already be within NEAR range to shorten your grip."

### PUSHING / ENTANGLING / RIPOSTE — Correctly held

`PUSHING` duplicates effects already covered by `COMBAT EXPERIENCED`. `ENTANGLING` overlaps with grapple. `RIPOSTE` belongs as a talent maneuver, not a weapon property — similar to how `INSIDE THE GUARD` handles the counter-attack flow. None of these belong as weapon features.

---

## IV. Talent Stacks

### THROWING ARM + AXE FIGHTER

The explicit stacking text is the real problem, not the weapon number.

The manuscript currently reads: "When you throw your weapons, the throwing arm talent stacks with other weapon talents (like AXE FIGHTER)."

Option A from the talent follow-up proposes restricting stacking outright. The problem with Option A is that it contradicts text players have already read and built around. Removing stacking after explicitly advertising it will be experienced as a nerf with no in-fiction justification.

The correct fix is a targeted clarification, not a blanket restriction. The stacking text should remain but specify what "stacks" means on a throw:

- THROWING ARM's attack bonus and range extension combine with AXE FIGHTER's attack bonus: **stacks.**
- AXE FIGHTER rank 2 auto-crit (slash wound): **does not apply on a throw.** The flavor text of rank 2 implies wound control you lose when you release the weapon.
- AXE FIGHTER rank 3+ Artifact Die: **stacks.** This is a pure probability boost with no flavor implication. Excluding it would feel arbitrary.
- AXE FIGHTER rank 4 EXECUTIONER interaction: **does not apply on a throw.** It follows from the auto-crit not applying.

This is a narrower fix than Option A. It does not require removing the stacking sentence. It preserves the fantasy of throwing your axe with lethal skill while blocking the specific rider effect that makes the combination feel unearned.

### FAST SHOOTER rank 4 + Light Crossbow

This is the most dangerous interaction in the set, and it should not be deferred.

Post-proposal state with both talents at rank 4:

- FAST action: Load crossbow
- SLOW action: SHOOT at `+3` effective, Damage 2, Long range — every single round with no penalty

A fully invested Longbow archer with the same talent investment (FAST SHOOTER + SHARPSHOOTER) fires at `+2` effective, Damage 1, Long per round — or twice per round with FAST SHOOTER rank 3, but with Agility damage on zone movement.

The Light Crossbow with FAST SHOOTER 4 + SHARPSHOOTER costs the same talent investment but produces higher per-shot damage, one more gear die, and zero round-penalty. The weapon table change reduces this from `+4` effective (pre-proposal) to `+3` effective (post-proposal). That is measurable improvement, but it does not fix the action economy gap.

Option C is the correct targeted fix: `FAST SHOOTER` rank 4 reduces crossbow Load to a FAST action, but SHOOT with a crossbow still costs a SLOW action. One shot per round, same as always. Bows retain comparative value through volume: FAST SHOOTER rank 3 lets bow users fire twice per round at the cost of movement pressure.

**This fix should be applied concurrently with the table changes, not deferred.** Deploying the range correction while leaving the action economy hole open is worse than the current state in at least one configuration.

### THROWING ARM + HARPOONER

This one is fine. The talent follow-up analysis is correct.

Throwing Spear at `+1` / Damage 2 / Short + THROWING ARM rank 1 (`+1`) + rank 2 (LONG range) + HARPOONER rank 1 (`+1`) = `+3` effective, Damage 2, Long, bleed on `2⚔️`. The setup cost is 4 talent ranks across two trees. The Throwing Spear must be recovered after each throw. The bleed requires `2⚔️` — not trivial at a 3-die pool. The bleed-to-break-then-death timer creates dramatic pressure rather than a one-shot end state.

This is a strong specialist niche. It is not a dominant strategy.

---

## V. Findings Summary

| Finding | Severity | Required Action |
|---|---|---|
| Composite Bow entry (`+3`) not updated when Short Bow drops to `+1` | **Critical** | Drop to `+2` before implementation; update acceptance summary |
| Blowgun (`+2`) inverts hierarchy over Short Bow (`+1`) post-nerf | **Moderate** | Drop Blowgun to `+1` in same pass, or document as accepted tradeoff |
| FAST SHOOTER 4 + Light Crossbow action economy problem | **High** | Apply Option C concurrently; do not defer |
| THROWING ARM explicit stacking text contradicted by Option A blanket restriction | **Moderate** | Amend text to narrow "stacks" to attack roll and Artifact Die only; exclude auto-crit riders on throws |
| HALF-HAND bypasses CUT IN risk when used to close | **Moderate** | Add proximity requirement: HALF-HAND only functions at NEAR or ARM'S LENGTH already established |
| SMASHING + HAMMER FIGHTER simultaneous pressure | **Informational** | Flag for playtest; not a blocker |
| Acceptance summary is silent on Composite Bow gap | **Documentation gap** | Update summary before integration |

---

## VI. Implementation Order

Do not treat these proposals as one independent batch.

The correct sequence:

1. **Fix Composite Bow entry** before implementing anything else. The table in Ch10 must drop from `+3` to `+2`.
2. **Apply the weapon table changes** (Ch05 ranged weapon table, Ch10 Composite Bow entry, Blowgun if dropped).
3. **Apply Option C to FAST SHOOTER rank 4** in the same pass as the table changes. Crossbow Load stays a FAST action, but SHOOT with a crossbow is still a SLOW action.
4. **Amend THROWING ARM text** to specify riders. One clause, not a rewrite.
5. **Add proximity constraint to HALF-HAND** before writing HALF-HAND into the manuscript.
6. **Flag SMASHING + HAMMER FIGHTER** synergy in GM notes when those properties go live.
