# Balance Audit — Design Critique and Fix Revisions

**Source:** `proposals/balance-audit-system-design-mercenary-band.md`
**Method:** Four-axis evaluation per issue — problem identification, severity rating,
fix quality, blind spots. Fixes revised where the original proposal was flawed.

---

## Issues Revised

### #1 — MORALE Trigger Pile-Up

**Problem identification:** Correct. The 3-positive / 7-negative asymmetry and the absence of
a weekly cap or floor are real.

**Fix flaw:** The original cap ("GM and captain agree which two are most significant") introduces
subjective adjudication into a system that exists to remove it. The disease was ambiguity;
the prescription was more ambiguity.

**Revision:** Replace count cap with a net movement cap. Triggers fire in severity order,
highest first, and stop after the score moves 3 in one direction per week. Remaining triggers
are noted as active grievances for check difficulty but do not move the score. No judgment call.

**Added:** Recovery path from MORALE 1. A positive trigger at MORALE 1 raises the score to 2
without requiring a check first. The floor is a pressure cooker, not a trap with no exit.

---

### #2 — Trigger vs. Check Boundary

**Problem identification:** Correct.

**Fix flaw:** The voluntary check is a free action. A captain with MANIPULATION 4 + skill 3
rolls 7 dice against difficulty 1–2 and clears grievances routinely. Becomes a dominant play
pattern.

**Revision:** Voluntary check costs a Quarter Day (the captain addresses the men). Once per
week maximum. Difficulty is set by the single most severe active grievance — cannot cherry-pick
the easiest one.

---

### #3 — Atrocity + Plunder + COLD-BLOODED

**Problem identification:** Correct. The single most exploitable dominant strategy in the
proposal.

**Severity:** Escalated from High to **Critical**. A playtest group will discover and ride this
exploit by session 2.

**Fix flaw:** Once-per-season cap still gives one free atrocity per season as optimal play.
The minimum plunder threshold (1s commons, 3s Named Men) is fiddly and will be gamed.

**Revision:** The +1 MORALE trigger from atrocity-with-plunder fires only when MORALE is 2
or below. At MORALE 3+, the men are functional — they do not need blood-money to hold
together. The atrocity still produces plunder (economic benefit), still triggers Standing and
Reputation consequences, but does not move MORALE when the band is already stable. This makes
the atrocity-plunder trigger a desperation tool, not a routine optimization.

Plunder condition: replaced with "plunder distributed at the band's stated archetype share."
The existing loot share mechanic validates the distribution. No new threshold needed.

COLD-BLOODED scope fix retained — personal immunity, not band suppression.

---

### #4 — Grievance Difficulty Undefined

**Problem identification:** Perfect. Priority 1 is correct.

**Fix flaw:** Minor. "Atrocity ordered, plunder distributed" at difficulty 1 double-discounts
atrocities. The plunder already offsets the MORALE trigger (Issue #3). Reducing the grievance
difficulty too is compounding the discount.

**Revision:** Change "Atrocity ordered, plunder distributed" from difficulty 1 to difficulty 2.
An atrocity is an atrocity. Plunder offsets the trigger, not the grievance.

---

### #5 — Four Social Currency Systems

**Problem identification:** Correct.

**Fix flaw:** "Take the higher plus 1" stacking cap uses an unexplained magic number. Why +1?

**Revision:** Remove the stacking formula. Reputation and Allegiance operate on different
negotiation axes. Reputation adjusts the opening offer floor. Allegiance adjusts the
negotiation difficulty. They do not touch the same number and cannot stack because they work
on different stages of the same interaction. Feud > Standing precedence rule retained.

---

### #6 — Loyalty 1–3 vs. Loyalty 5

**Problem identification:** Correct.

**Fix flaw:** The "settled" mechanic (absorb one Minor grievance, doesn't persist across
seasons) adds a new tracked state per Named Man per month to solve a problem that doesn't
exist. Loyalty 3 is already the best state. A positive trigger at the cap needs no reward.

**Revision:** Cut the settled mechanic. Loyalty caps at 3. Positive triggers at the cap
do nothing. The fiction is that a loyal man who is treated well stays loyal.

---

### #7 — Occupation Economic Bypass

**Fix quality:** Sound. No revision needed.

**Added blind spot:** Settlement drain. A settlement occupied and drained should be
mechanically weaker for at least one season afterward. Added to the fix.

---

### #8 — Allegiance 4 Winter Bypass

**Fix quality:** The cleanest fix in the document. No revision needed.

---

### #9 — Reputation + Caster Premium

**Fix flaw:** Same magic number problem as #5. "Take the higher plus 5s flat" has no
derivation. 5s is dust at high contract values and 5% at low ones.

**Revision:** Caster premium adjusts the contract type range (casters attract different
work). Reputation adjusts the opening offer within that range. They operate on separate
axes and do not require a stacking formula. The 1.5× ceiling is retained as an emergency
brake.

---

### #10 — Loyalty Decay Rate

**Fix flaw:** Fear-Held at 2/week means the entire Named Man roster hits Loyalty 1 within
seven days of entering MORALE depression. No decision space. No captain action possible.
It is a cliff, not a mechanic.

**Revision:** Fear-Held fires weekly at 1/week (same speed as standard), but the Loyalty
floor in a Fear-Held band is 0, not 1. Loyalty 0 means the Named Man actively considers
defection or sabotage. Same speed, higher stakes. That is the Fear-Held identity.

---

### #11 — In-Kind / Non-Payment

**Severity:** Downgraded from Medium to **Low**. This is a text clarity issue, not a
balance problem. No exploit exists.

**Fix flaw:** The four-stage interaction model (weeks 1–2 safe, week 3 in-kind only, week 4
both fire) is too complex for live play.

**Revision:** One rule: in-kind payment satisfies the non-payment threshold. The in-kind
escalation is the only mechanic that governs goods-payment. The non-payment table governs
no-payment. They are two systems for two failure modes and should not overlap.

---

### #12 — Wolfkin Pack Bonus

**Severity:** Downgraded from Medium to **Low**. The D3 adds ~2 fighters on average to
a 7–14 person band. It accelerates growth by one recruitment cycle. Functional, not broken.

**Fix quality:** Correct as written. No revision needed beyond severity adjustment.

---

## Issues Not Revised

- **#7** — Fix is sound. Settlement drain note added.
- **#8** — Ship as-is.
- **#12** — Ship as-is minus severity.

---

## Meta Observation

The audit never addresses the GM's decision fatigue across all 12 systems simultaneously.
Each fix adds a rule. Twelve fixes add twelve rules. The proposal is already the densest
subsystem in the repo. Some of these issues exist because the proposal has too many
interacting subsystems. The answer to "four social currencies are hard to track" is not
"here is a priority rule for when they conflict" — it is "do you need four?"

This critique does not propose consolidation. That is a separate design task. But the
question should be on record.
