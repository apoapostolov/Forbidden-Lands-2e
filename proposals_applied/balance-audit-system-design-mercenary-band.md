# Mercenary Band Management — Balance and System Design Audit

**Scope:** `proposals/proposal-mercenary-band-management.md` — full system design, all sections.
**Sister document:** `proposals_applied/audit-mercenary-economy-model.md` (V7 economy results and cost
model).
**Focus:** Modifier stacking, system synergies, dominant strategies, mechanical ambiguities, and GM
tracking burden — not the economy numbers (those are covered in the V7 audit).

---

## Index

| #   | Issue                                                          | Severity |
| --- | -------------------------------------------------------------- | -------- |
| 1   | MORALE trigger pile-up — no weekly cap                         | High     |
| 2   | MORALE trigger vs. MORALE check — undefined boundary           | High     |
| 3   | Atrocity + plunder + COLD-BLOODED — dominant atrocity loop     | High     |
| 4   | "Outstanding grievances" — difficulty is undefined             | High     |
| 5   | Four parallel social currency systems                          | High     |
| 6   | Loyalty scale inconsistency — 1–3 table vs. Loyalty 5 text     | High     |
| 7   | Occupation as economic bypass                                  | Medium   |
| 8   | Allegiance 4 + winter scarcity bypass                          | Medium   |
| 9   | Reputation + caster premium — additive or multiplicative       | Medium   |
| 10  | Named Man Loyalty decay rate under sustained MORALE depression | Medium   |
| 11  | In-kind payment / non-payment interaction gap                  | Medium   |
| 12  | Wolfkin recruitment D3 pack bonus — settlement tap bypass      | Medium   |
| 13  | DRILL bonus — no expiry, no cap on repetition                  | Low      |
| 14  | XP on 1 rewards reckless play                                  | Low      |
| 15  | Vengeance oath +1 MANIPULATION — stacks with no ceiling        | Low      |
| 16  | Loot share archetype — no downgrade or renegotiation mechanic  | Low      |
| 17  | Flyting refusal auto-escalates — binds players with no exit    | Low      |

---

## 1. MORALE Trigger Pile-Up — SEVERITY: High

**Systems involved:** MORALE triggers table (Section 1), MORALE scale (1–5)

The MORALE triggers table lists 10 separate events. The table places no weekly cap on how many
can fire simultaneously. In a plausible active-campaign week, four or more events can fire at once:

- Won engagement, few casualties (+1)
- Paid on time, once per season (+1)
- 20%+ casualties (−1)
- Named Man killed (−1)

That week nets 0. The same week in a collapsing band fires instead:

- Late payment, 3+ days (−1)
- Broken contract, leader fault (−2)
- Fellowship abandoned band (−2)
- Atrocity ordered, no plunder (−1)

Total: −6 in one week. MORALE 4 becomes −2, which is below the scale floor. Whether MORALE
floors at 1 is not stated. Whether a band at MORALE 1 that receives a further −2 trigger has any
different consequence than one that becomes MORALE 1 by one step is not stated.

The positive side has three triggers capable of firing. The negative side has seven. A captain who
avoids every negative this week cannot accumulate faster than +1, because "paid on time" is
once per season and "proved decisive value" is contextually rare. The trigger table is structurally
weighted to generate pressure more easily than relief.

**Worst case:** A GM running a bad-luck week applies every applicable trigger in one accounting.
A band at MORALE 3 goes to MORALE at or below 1 in a single event sequence. There is no
mechanical friction preventing this.

**Open Questions:**

1. Is there a cap on how many MORALE triggers can apply per week, or per event sequence?
2. Does MORALE floor at 1 and stay functional, or does going below 1 indicate instant dissolution?
3. Can positive triggers accumulate above MORALE 5? If not, is the ceiling explicitly stated?
4. Is "Paid on time (once per season)" meant to be the only reliable positive trigger? If so, is
   the resulting asymmetry — three positives, seven negatives — intentional design or an artifact
   of the table growing over drafts?

**Proposed Rule Change:**

**Net movement cap.** All applicable MORALE triggers fire each week, ranked by severity (largest
modifier first). The score stops moving after a net change of 3 in either direction. Remaining
triggers do not adjust the score but are recorded as active grievances — they exist for MORALE
check difficulty (see Issue #4) and are visible to the captain and GM. No subjective selection
of which triggers count.

**Floor.** MORALE cannot drop below 1 through trigger applications alone. A trigger that would
push MORALE to 0 or below holds the band at MORALE 1. Band dissolution is a MORALE check
failure at MORALE 1 during an engagement, not a trigger outcome.

**Ceiling.** MORALE cannot exceed 5. Positive triggers earned above the ceiling are lost.

**Recovery from MORALE 1.** A positive trigger at MORALE 1 (BROKEN) raises the score to 2
without requiring a MORALE check. The floor is a pressure state, not a trap with no mechanical
exit. The captain still faces the BROKEN check if an engagement fires before a positive trigger
arrives.

---

## 2. MORALE Trigger vs. MORALE Check — Undefined Boundary — SEVERITY: High

**Systems involved:** MORALE triggers table, MORALE check mechanic (Section 1, Section 6)

The proposal uses two separate mechanisms:

- **MORALE triggers** — automatic adjustments to the MORALE score when listed events occur.
- **MORALE checks** — rolled MANIPULATION by the leader against a difficulty derived from
  "outstanding grievances."

Where triggers are clear ("Named Man killed → −1"), checks are opaque. The text says a check
fires before a "dangerous assignment" when MORALE is below 3 (WAVERING) and at MORALE 1
before any engagement (BROKEN). COLUMN 6 of the Discipline/Punishment section says "a sentence
stated and not carried out costs MORALE −1." This is a trigger, not a check. Section 9 says
"the band must check MORALE" after an ordered massacre with no gain. That is a check. The
boundary is not consistent.

**Specific ambiguity:** Does a single event — say, late payment — produce:
(a) an automatic −1 trigger, with no roll,
(b) a MORALE check the leader must pass to prevent a consequence, or
(c) both an automatic trigger AND a possible check?

The text implies (a) for the trigger table and (c) for the Atrocity section, but the two
mechanisms are never reconciled.

**Worst case:** GMs apply both to the same event, double-penalising the captain: the band drops
−1 from the trigger and then must also pass a check or drop further. Alternatively, GMs apply
neither, uncertain which mechanism applies.

**Open Questions:**

1. Which events produce automatic triggers only, which require a check, and which produce both?
2. Is the MORALE check a named alternative to the trigger, or a separate consequence that layers
   on top?
3. If a check fails, does the band lose an additional MORALE step, or does the failure produce a
   narrative consequence (argument, refusal, desertion) that the GM arbitrates?
4. Can the captain voluntarily call a check to address an existing grievance before a trigger fires?

**Proposed Rule Change:**

**Triggers are automatic.** Events in the MORALE Triggers table adjust the score without a roll.
They happen when the listed condition happens.

**Checks are called by context.** Three situations call for a MORALE check: leading a dangerous
assignment when MORALE is WAVERING (3 or below), leading any engagement when MORALE is BROKEN
(1), or ordering an atrocity without material gain (Section 9). In each case the leader rolls
MANIPULATION against difficulty set by outstanding grievances (see Issue #4 fix).

**One or the other, not both.** A late payment produces the automatic −1 trigger. It does not
also produce a MORALE check. Where Section 9 specifically calls for a check after an atrocity
causing a score change, both apply in sequence — the score drops from the trigger first, then
the leader rolls the check. This is the exception, not the rule, and Section 9 must state it
explicitly where it applies.

**Voluntary check.** The captain may voluntarily call a MORALE check once per week, at the
cost of one Quarter Day (the captain addresses the assembled men). Difficulty is set by the
single most severe active grievance — the captain cannot choose which grievance to address.
On success, that grievance is cleared. On failure, nothing changes and the attempt is noted.
The men saw the captain try and fail.

---

## 3. Atrocity + Plunder + COLD-BLOODED — Dominant Atrocity Loop — SEVERITY: Critical

**Systems involved:** MORALE triggers (Section 1), Atrocities (Section 9), Loot share archetypes
(Section 3), Talent integration — COLD-BLOODED (Section 10)

Three separate rules combine into a dominant strategy:

**Rule A:** MORALE trigger table: "Atrocity ordered, men gained plunder = +1 MORALE."

**Rule B:** Tyrant loot share archetype: captain takes 60% of haul. Named Men take 20%. Commons
take 8%. The "men gained plunder" condition is met even at 8% commons share — the text does not
specify a minimum plunder threshold.

**Rule C:** Section 10 Talent Integration: "Fellowship members with COLD-BLOODED do not trigger
MORALE penalties from ordered atrocities."

Combined: a Tyrant captain with COLD-BLOODED can order atrocities every contract, distribute the
plunder (commons receive 8% even from a Tyrant share), gain +1 MORALE each time, and suffer
no personal MORALE penalty from the COLD-BLOODED clause. The result is a band that improves
MORALE through repeated atrocities provided the plunder is distributed.

Section 9's "Plunder" note says: "Short-term MORALE gain from atrocity plunder does not offset
the Reputation consequences." This is a narrative caution, not a mechanical cap. MORALE still
rises. Named Men with civilian-harm Triggers still check Loyalty. But the captain running the
loop is not losing MORALE — they are gaining it.

**Worst case:** A Tyrant captain with COLD-BLOODED reaches MORALE 5 within a season through
systematic atrocity, even as their Reputation collapses. The only counterpressure is Loyalty
checks on Named Men with civilian-harm Triggers — but at MORALE 5, new recruitment is easy and
loyalty-1 departures are individually low-cost. The system designed to punish atrocity becomes
the fastest path to a stable high-MORALE band.

**Open Questions:**

1. Does "men gained plunder" require a minimum plunder quantity or value, or does any non-zero
   distribution satisfy the trigger?
2. Is COLD-BLOODED's MORALE immunity intended to cover the full Atrocity section, or only the
   one trigger line in the trigger table?
3. Is there a ceiling on how many times the atrocity-with-plunder trigger can fire per season,
   or per operation?
4. Do Named Men with civilian-harm Triggers check Loyalty even when the MORALE trigger fires
   positive? The text says "regardless of plunder" — does that clause take priority over the +1
   MORALE trigger, or do both outcomes apply simultaneously?
5. Does the COLD-BLOODED immunity stack with a Tyrant archetype, or is the intent that the
   Tyrant's men still feel it even if the leader does not?

**Proposed Rule Change:**

**Conditional trigger.** The +1 MORALE trigger from "atrocity ordered, men gained plunder"
fires only when MORALE is currently 2 or below. At MORALE 3 or higher, the men are functional —
they do not need blood-money to hold together. The atrocity still produces plunder (economic
benefit), still triggers Standing and Reputation consequences, still forces Named Man Loyalty
checks on civilian-harm Triggers. It does not move MORALE when the band is already stable.
This makes the atrocity-plunder trigger a desperation tool, not a routine optimization.

**Plunder condition.** "Men gained plunder" is satisfied when plunder is distributed at the
band's stated archetype share. The existing loot share mechanic validates the distribution. No
separate minimum threshold is needed — the archetype shares are the threshold.

**COLD-BLOODED scope.** COLD-BLOODED means the fellowship member does not personally trigger
additional MORALE penalties beyond those already on the trigger table. It does not suppress
the band's aggregate trigger result. The −1 from "atrocity ordered, no plunder" still fires on
the band. Named Men with civilian-harm Triggers still roll against Loyalty regardless of the
MORALE direction. COLD-BLOODED affects the leader's personal contribution to the result —
nothing else.

---

## 4. "Outstanding Grievances" — Difficulty Is Undefined — SEVERITY: High

**Systems involved:** MORALE check mechanic (Section 1), MANIPULATION rolls

The text says MORALE checks at WAVERING and BROKEN use the leader's MANIPULATION against
difficulty derived from "outstanding grievances." This phrase appears in the text as the
difficulty reference without a numeric definition anywhere in the proposal.

A GM must know the number to run the roll. As written, there is no mapping from grievance
type, count, or severity to a difficulty integer between 1 and 5.

**Worst case:** Every GM invents their own scale. An atrocity at one table produces difficulty 1.
At another it is difficulty 4. The MORALE check becomes a GM discretion fiat rather than a
mechanical outcome.

**Open Questions:**

1. Is difficulty meant to equal the number of unaddressed grievances? Or their severity sum?
2. Is there a reference difficulty for specific grievance types — one for unpaid wages, a
   different one for a Named Man killed, a different one for an ordered atrocity?
3. Is the difficulty meant to be fixed per check context (e.g., WAVERING assignment check is
   always difficulty 2, BROKEN engagement check is always difficulty 3) independent of current
   grievances?
4. Is there a maximum difficulty cap? If three simultaneous grievances each suggest difficulty 2,
   does the captain face difficulty 6, or is it bounded?

**Proposed Rule Change:**

Add a GRIEVANCE DIFFICULTY table to the MORALE Check rules:

| GRIEVANCE                                  | DIFFICULTY |
| ------------------------------------------ | ---------- |
| Late wages, 7 or fewer days                | 1          |
| Named Man killed in action                 | 1          |
| Atrocity ordered, plunder distributed      | 2          |
| Late wages, 8–14 days                      | 2          |
| Mission pay unpaid 3+ days                 | 2          |
| Atrocity ordered, no plunder               | 2          |
| Retainer unpaid 15+ days                   | 3          |
| Contract broken through captain's decision | 3          |
| Fellowship abandoned the band              | 3          |

**Stacking.** Take the highest single grievance's difficulty, then add 1 for each additional
active grievance beyond the first. Cap at 4. Three grievances of difficulty 2, 1, and 1 produce
difficulty 4 (2 + 1 + 1 = 4, capped). Do not sum all grievance difficulties directly.

**Clearing.** An addressed grievance is removed at the start of the following week. Addressing
means the captain has taken a concrete action — paid the wages, publicly acknowledged the Named
Man's loss, made restitution. An apology without action does not clear a grievance.

---

## 5. Four Parallel Social Currency Systems — SEVERITY: High

**Systems involved:** Standing (Section 4), Feud Track (Section 4), Allegiance (Section 5),
Reputation/Renown (Section 8 and Section 10)

The proposal runs four independent social scores:

- **Standing** — per settlement. Affects tribute access, gate entry, shelter.
- **Feud Track** — per settlement. Affects when enemies organize and attack.
- **Allegiance** — per employer (0–4 scale). Affects contract terms, audience access, advance pay.
- **Reputation/Renown** — band-wide. Affects opening contract rates and bounty spread.

A single act can hit all four at once. Demanding tribute from a settlement: Standing −1, Feud
Track +1. If the settlement has a relationship with an active employer, it may affect Allegiance.
The Atrocity section says reputation spreads via the rumor system, which affects Reputation.

At maximum stacking: a Reputation 5 band with Allegiance 3 to their primary employer and
Standing +2 at that employer's settlements gets +15% opening contract rates, −1 difficulty on
negotiation terms, +1 Standing at all employer-connected settlements (per Allegiance 3). This
band is structurally insulated from most of the economic pressure the model is designed to apply.
Even if Feud Track advances at multiple villages, the Allegiance and Reputation buffers mean
the band has no shortage of work and consistently favorable terms from established employers.

**GM tracking burden:** At campaign scale, the band may interact with a dozen settlements and
five employers. Tracking four scores × N actors is the upper bound of what a GM can sustain
without a dedicated reference sheet. The proposal provides no summary tracking tool.

**Worst case:** The GM stops tracking one or two of the four systems under session pressure.
The economic model loses a meaningful pressure axis. Alternatively, the GM tracks all four but
interaction resolution becomes so complex that sessions slow at each social encounter.

**Open Questions:**

1. Are Standing and Feud Track intended to be tracked for every settlement the band contacts,
   or only significant ones above a threshold of interaction?
2. Can Allegiance Standing buffers (Allegiance 3 grants +1 at employer-connected settlements)
   directly counteract Feud Track advancement from tribute demands at those same settlements?
3. If yes, is MORALE under simultaneous Standing +2 and Feud Track +3 at the same settlement
   resolved by Standing, Feud Track, or some combination?
4. Is a tracking reference meant to be supplied alongside this proposal, or is the expectation
   that the GM builds their own?
5. At what Allegiance + Reputation combination is it impossible for the model's economic
   pressure to reach the band through normal play?

**Proposed Rule Change:**

**Conflict resolution.** When Standing and Feud Track produce opposite outcomes at the same
settlement, Feud Track takes precedence. Standing measures the settlement's disposition; Feud
Track measures whether they have already organized a response. A band with Standing +2 and Feud
Track 3 will find the gate civil and the ambush already planned.

**Allegiance coverage.** Allegiance 3's Standing bonus (+1 at employer-connected settlements)
applies only to settlements within the employer's recognized sphere of influence. It does not
apply to settlements the band has damaged through independent tribute demands or atrocities,
even if those settlements have a prior relationship with the employer. The employer's interest
covers the employment, not the band's conduct outside it.

**Tracking reference.** GM tracks Standing and Feud Track only for settlements the band has
visited more than once. Single-contact settlements carry no score until a second interaction.
Add a sidebar per settlement with: name, Standing, Feud Track, notes on recent contact. Allegiance
and Reputation are band-level scores tracked on the band sheet, not per settlement.

**Cap on stacked bonuses.** Reputation and Allegiance operate on different axes of the same
negotiation and do not require a stacking formula. Reputation adjusts the employer's opening
offer floor — what the employer puts on the table before anyone speaks. Allegiance adjusts
the MANIPULATION difficulty for negotiating above that floor. They do not touch the same number.
A Reputation 5 band at Allegiance 3 walks in to a higher floor and negotiates from there at
reduced difficulty, but neither bonus inflates the other.

---

## 6. Loyalty Scale Inconsistency — Loyalty 1–3 vs. Loyalty 5 — SEVERITY: High

**Systems involved:** Loyalty score table (Section 7), Named Man Connections mechanic (Section 7),
Loyalty change triggers

The Loyalty score table defines three states:

- **Loyalty 3** — trusted, will not betray short of direct refused command
- **Loyalty 2** — reliable, will leave if triggered
- **Loyalty 1** — self-interested, will sell information or remain neutral

The Named Man Connections mechanic (Section 7, "Named Man Connections") requires:
"After three or more months of continuous service and **Loyalty 5**."

Loyalty 5 does not exist in the table. The scale is 1–3.

The Loyalty change triggers include two positive events:

- "+1 if the leader demonstrates genuine regard for the named man's wellbeing"
- "+1 on a consistent basis if loot shares are paid immediately after every combat haul"

If Loyalty starts at 3 and a positive event fires, where does it go? The text does not define
Loyalty 4 or Loyalty 5, nor does it explicitly cap Loyalty at 3.

**Worst case:** The Named Man Connections mechanic becomes inaccessible because Loyalty 5 is
unreachable. Or GMs extend the scale to 5, altering the meaning of each tier without guidance.
Or the +1 positive triggers are effectively meaningless for a Loyalty 3 Named Man because there
is nowhere for the bonus to go.

**Open Questions:**

1. Is Loyalty 5 a text error that should read Loyalty 3?
2. If the scale extends to 5, what are the meanings of Loyalty 4 and 5?
3. Is there a cap on Loyalty, and does the Named Man Connections mechanic require that cap to be
   increased above 3 to be usable?
4. Do the +1 "wellbeing" and +1 "paid immediately" triggers have an explicit ceiling, or do they
   continue beyond Loyalty 3 into undefined territory?

**Proposed Rule Change:**

**Text correction.** In the Named Man Connections mechanic, change "Loyalty 5" to "Loyalty 3,
sustained across three or more consecutive months of service without the Named Man dropping
below Loyalty 3 at any point in that period."

**Loyalty ceiling.** Loyalty caps at 3. Positive triggers do not push it above 3. A Named Man
already at Loyalty 3 who receives a positive trigger gains no further mechanical benefit. The
fiction is that a loyal man treated well stays loyal — there is no further movement because
there is no further need.

**Clarification on positive trigger frequency.** "Demonstrated genuine regard for the Named
Man's wellbeing" fires once per Named Man per notable event — not once per week passively. The
captain must take a specific visible action. Paying all wages consistently is covered by the
"immediate loot distribution" trigger. The two triggers are distinct and both require active
captain behavior.

---

## 7. Occupation as Economic Bypass — SEVERITY: Medium

**Systems involved:** Occupation rules (Section 4), V7 economy model, Feud Track

The occupation rule states a held settlement yields 1D6 silver per week. It also reduces the
band's food cost by the hex forager yield of the settlement's terrain.

V7 economy numbers for reference: a standard warband earns ~43s per week mean income against
~41.5s per week mean costs. Net weekly margin is approximately +1.2s.

Occupation value in forest terrain: 1D6 silver/week (mean 3.5s) plus forager-equivalent food
savings. Five foragers in forest terrain yield 8 FOOD per day at the core rules rate. Eight FOOD
at market price (1s/day per unit as used in V7) is 8s/day food savings — the figure is extreme
because it represents cost of feeding the band if all food were purchased rather than foraged,
but even a partial food offset worth 3–5s/week puts each occupied settlement's combined value
at 6–9s/week.

Two occupied settlements: 12–18s/week in combined occupation value against a 1.2s mean weekly
margin. The band under two occupations operates at approximately 10–17s/week net positive rather
than 1.2s — a 10× to 15× improvement in weekly margin, achieved through occupation rather than
contract work.

The Feud Track is the counterweight: occupation accrues Standing damage and Feud Track
advancement, eventually triggering reprisals. But the Feud Track acts on a delay. A band that
anticipates the Feud response can occupy, extract for 2–4 weeks, and withdraw before the
threshold is reached — then move to the next settlement.

**Worst case:** A mobile band implementing a systematic occupy-extract-withdraw pattern does not
need contracts to sustain itself. With two active occupations at any time (staggered to avoid
Feud Track overflow), the band operates indefinitely without the contract system. The winter
scarcity mechanic becomes irrelevant. The entire V7 model's pressure calibration is bypassed.

**Open Questions:**

1. Is the 1D6 silver per week from occupation scaled against the full extraction potential of a
   settlement, or against the marginal extraction above subsistence?
2. Is there a minimum occupation duration before the band can extract? Or can extraction begin
   immediately on holding the settlement?
3. Does the Feud Track advance during occupation even if the band is not demanding tribute —
   simply presence and control?
4. Is the occupy-extract-withdraw loop a known intended use of the occupation mechanics, or a
   byproduct that was not modelled in V7?
5. Should occupation yield be added to the V7 simulation as a pressure relief valve, or capped
   to keep the contract model primary?

**Proposed Rule Change:**

**Yield reduced to 1D3 silver per week.** Occupation presses a settlement for what it can spare
above subsistence. At 1D6, the long-run mean of 3.5s/week is roughly 8% of a standard warband's
weekly income — low in isolation but compounding across two held settlements. At 1D3 (mean 2s),
one occupied settlement contributes ~5s/week combined with other foraging activity, which is
meaningful but not economy-replacing.

**No passive food credit.** Occupation does not reduce band food costs. The band still forages
or purchases. An occupied settlement's food value is only available if the captain assigns a
specific foraging Quarter Day to extraction, treated as a standard provisionment action using
the settlement's terrain type. The settlement does not feed the band by being held.

**Feud Track advances during occupation.** Each full week of occupation advances the Feud Track
by 1 at that settlement, independent of tribute demands. Presence under arms is not neutral.
This means the practical extraction window before Feud Track consequences fire is 2–3 weeks at
most (Feud Track 3 triggers organized response), consistent with the occupy-extract-withdraw
pressure the mechanic is designed to produce.

**Settlement drain.** A settlement that has been occupied and extracted from is mechanically
weaker for one season afterward. Its available foraging yield, trade goods, and recruitable
population are reduced by one step (GM determines the specifics for the settlement's size and
type). This prevents the occupy-withdraw-reoccupy cycle from being cost-free across multiple
visits. The settlement remembers.

---

## 8. Allegiance 4 (Sworn) + Winter Scarcity Bypass — SEVERITY: Medium

**Systems involved:** Allegiance system (Section 5), V7 winter scarcity mechanic

Allegiance 4 (Sworn) grants: "Employer covers one advance payment per season without a posted
contract." This fires once per season, at the employer's discretion.

The V7 model's winter scarcity mechanic (Q4, days 274–364) cuts contract availability from 55%
to 27.5%. This is the model's primary pressure quarter: bands without a protection season locked
in going into Q4 face low contract volume and risk empty treasury.

A Sworn band begins Q4 eligible for one free advance from their sworn employer. The advance pay
scale is "equivalent to advance payment terms for a standard contract" — not explicitly defined,
but implied by context as 30–40% of the contract's estimated value. For a mid-range contract
(patrol at ~100–125s), that is 30–50s applied to a quarter where the mean weekly cost runs
~40s/week. A 30–50s advance covers nearly one week of full costs in the quarter designed to be
difficult.

Additionally, Allegiance 2 reduces Negotiating Terms difficulty by 1. In Q4 when fewer contracts
exist, a Sworn band (Allegiance 4, implying they passed through Allegiance 2) gets easier terms
on whatever limited work is available.

**Worst case:** A band that has achieved Sworn status by end of Y1 or early Y2 is insulated from
the exact quarterly pressure V7 was calibrated to apply. The winter squeeze — intended to force
decisions, create tension around protection seasons, and punish bands without a plan — does not
reach a Sworn band at the same intensity.

**Open Questions:**

1. Is the Sworn advance payment intended as a full cushion against Q4 pressure, or as a partial
   offset that still leaves the band making hard decisions?
2. Does the Sworn advance count toward the employer's contract obligation, or is it a separate
   goodwill payment with no contract attached?
3. If the Sworn advance is 30–50s against ~160s Q4 costs, that is a 19–31% offset. Is this the
   intended magnitude?
4. Does Allegiance decay during a season when no contract is taken — i.e., can an inactive Sworn
   band hold Allegiance 4 indefinitely and repeatedly collect Q4 advances?

**Proposed Rule Change:**

**Sworn advance ceiling.** The Q4 advance payment at Allegiance 4 equals one full week of
retainer wages for the band's current tier: 28–40 silver for a Warband, 21s for a Skirmisher
band. Not a percentage of a hypothetical contract value — a flat week. It covers one week of
costs in a lean quarter, not the quarter.

**Active service requirement.** The Q4 advance fires only if the band was on active contract
for the sworn employer at any point in Q3. An employer who did not deploy the band in the
preceding quarter is not obligated to fund their winter, even at Sworn tier.

**Allegiance decay.** Allegiance decreases by 1 at the end of any season in which the band
completed no contract for that employer. Sworn status requires active investment. An Allegiance
4 band that sits idle for a full season enters the next season at Allegiance 3, ineligible for
the Q4 advance until they rebuild the relationship through another completed contract.

---

## 9. Reputation + Caster Premium — Additive or Multiplicative — SEVERITY: Medium

**Systems involved:** Reputation opening rates (Section 5), Caster contract premium (Section 7.5),
contract type base rates

The proposal states two separate contract rate bonuses:

- **Reputation:** +5% per Renown above 2 on employer's opening offer. Renown 5 = +15%.
- **Caster band premium:** "A band with a caster negotiates 35% more on standard contracts."

Applied to the same contract at Renown 5 with a caster:

- **Additive:** Base × (1 + 0.15 + 0.35) = Base × 1.50
- **Multiplicative:** Base × 1.15 × 1.35 = Base × 1.5525

At a standard patrol opening rate of ~100–125s, additive produces 150–187s. Multiplicative
produces 155–194s. The difference is small at this range but grows at higher contract values.

The more significant question is whether these stack at all. The caster premium produces
"108–190 silver" for an escort in the text's own example (from a base of 80–140s = ×1.35). The
Reputation adjustment is applied separately from the negotiation table. If the GM applies the
caster premium to the already-Reputation-adjusted opening offer, it compounds.

The caster premium is also ungated — it applies automatically without a roll, while Reputation
accrual requires time and successful contracts. A Renown 5 caster band at the start of Y3 may
have opening offers 50%+ above base on every contract.

**Worst case:** A Renown 5 caster band accepting a major warchief assault (base 280–420s) opens
at 406–609s if both bonuses stack multiplicatively. The V7 caster variant at –2.5% margin
assumes a standard contract mix without Reputation scaling. At Renown 5, the same band is firmly
positive.

**Open Questions:**

1. Are the Reputation and caster bonuses applied additively to the same base, or does one apply
   first as the new base for the second?
2. Is there a ceiling on combined contract rate bonuses?
3. At what Renown level does the model's economic pressure become effectively nil for a caster
   band?
4. Does the caster premium apply to the contract type's floor, ceiling, or to the GM's stated
   opening offer?

**Proposed Rule Change:**

**Separate axes.** Reputation and the caster premium operate on different stages of the same
contract interaction. They do not stack because they do not touch the same number.

- **Reputation** adjusts the employer's opening offer. For each point of Renown above 2, add 5%
  to the base contract type range. This is applied before anyone speaks. Reputation 5 = +15%
  floor.
- **Caster premium** adjusts the contract type the employer is willing to offer. A band with a
  caster attracts work that a non-caster band would not be offered — assault and clearance
  contracts where magical support is a material factor. The premium is not a percentage on the
  same patrol; it is access to a higher-value job category.

When both qualities are present and the contract type is already the highest available, the
caster premium provides no additional percentage. The Reputation adjustment applies to whatever
contract type the band received.

**Opening offer ceiling.** No contract opens above 1.5× its stated type ceiling regardless of
applied bonuses. A patrol ceiling of 165s cannot open above 247s on first approach. Terms
negotiation may push beyond this; the opening offer is bounded.

---

## 10. Named Man Loyalty Decay Rate — SEVERITY: Medium

**Systems involved:** Loyalty score (Section 7), MORALE scale, Loyalty change triggers

The Loyalty change triggers include: "−1 per MORALE step the band falls below 3, each week."

Parsed: at MORALE 2, every Named Man loses 1 Loyalty per week. At MORALE 1, every Named Man
loses 2 Loyalty per week (one step from MORALE 3 to MORALE 2, another from MORALE 2 to
MORALE 1).

The scale runs 1–3. A Named Man at Loyalty 3 who enters a two-week MORALE 2 period drops to
Loyalty 1. At MORALE 1 for two weeks, a Loyalty 3 Named Man drops to Loyalty −1 — off the
bottom of the scale. The text does not say what happens below Loyalty 1.

Even in a Trust-Held band (Loyalty decay halved), the same Named Man drops from Loyalty 3 to
Loyalty 1 in four weeks at MORALE 2. In a Fear-Held band (decay at double rate), they drop to
Loyalty 1 in one week.

**Interaction with base recovery:** Loyalty recovers +1 only on two conditions — demonstrated
genuine regard for the Named Man's wellbeing, or consistent immediate loot distribution. Neither
fires frequently. A band in a MORALE 2+ slump will not likely be winning enough to distribute
loot, and "demonstrated genuine regard" requires a specific act the player must initiate.

**Worst case:** A band entering a MORALE depression loses its senior Named Men (the Loyalty 3
ones) within two to four weeks as recoverable allies. After that, only Loyalty 1 Named Men
remain — defined as willing to sell information or remain neutral in a crisis. The band becomes
operationally headless during exactly the period it most needs Named Man support. This may
be intended, but the speed of the spiral seems to undercut the Trust-Held band's "stay" mechanic
(which requires Loyalty 3 to fire at all).

**Open Questions:**

1. Is the −1 per MORALE step per week trigger cumulative or per-step? At MORALE 1, does a
   Named Man lose 1 Loyalty per week (MORALE 1 step below 3) or 2 Loyalty per week (two steps
   below 3)?
2. Is there a minimum Loyalty below which no further decay is applied?
3. Does the Trust-Held halved decay rate interact with the MORALE-step formula — is it halved
   per step, or is the total weekly loss halved?
4. Can the "stay" mechanic (Loyalty 3 Named Man spending to hold band together once per season)
   fire at MORALE 1, where the spend conditions are most urgent but Loyalty 3 may already be
   gone?

**Proposed Rule Change:**

**Flat decay rate.** Loyalty decay from MORALE depression is 1 per week when the band is below
MORALE 3. It does not scale with how many steps below 3 the band sits. At MORALE 2: 1 Loyalty
lost per week. At MORALE 1: also 1 Loyalty lost per week. The step count determines when decay
begins, not its magnitude.

**Loyalty floor.** Loyalty does not fall below 1 from MORALE depression alone. A Named Man
already at Loyalty 1 continues receiving the decay trigger each week but does not go lower —
they are already at the floor. Only an active trigger event (Trigger activated, ordered atrocity
witnessed, betrayal) drops them out of service.

**Trust-Held decay cadence.** In a Trust-Held band, Loyalty decay from MORALE depression fires
every two weeks rather than every week. Not half per week — every other week. A Loyalty 3 Named
Man in a Trust-Held band at sustained MORALE 2 reaches Loyalty 1 after four weeks.

**Fear-Held: same speed, lower floor.** In a Fear-Held band, decay fires at the standard rate
of 1 per week. The difference is the floor: Fear-Held Loyalty can reach 0. Loyalty 0 means the
Named Man actively considers defection or sabotage — they are no longer passively self-interested
but weighing whether to act against the band. The captain has the same time to respond as in
a standard band, but the consequences of failure are worse. That is the Fear-Held identity:
same speed, higher stakes.

---

## 11. In-Kind Payment / Non-Payment Interaction Gap — SEVERITY: Low

**Systems involved:** In-kind payment rule (Section 3, FIELD NON-PAYMENT), Non-payment D6
table (Section 3)

The in-kind payment rule creates a three-stage escalation:

- First week in-kind: no consequence
- Second consecutive in-kind: +1 difficulty on next non-payment check
- Third consecutive in-kind: roll immediately at standard difficulty

The Field Non-Payment D6 table fires after "14 days unpaid" for retainer, or "3 consecutive
days unpaid" for mission pay.

**The gap:** Does paying in-kind count as "paid" for the non-payment table threshold? The text
does not say. If in-kind satisfies "paid," then the non-payment table never fires while the
band is receiving any goods payment — only the in-kind escalation applies. A captain who can
supply goods indefinitely avoids the non-payment table entirely.

**Counter-question:** If in-kind does NOT satisfy "paid," then a captain paying in wool cloth
and grain simultaneously triggers both the in-kind escalation AND approaches the non-payment
table threshold. By week 3, the in-kind rolls AND the non-payment table fires. The consequences
may overlap (the in-kind roll produces a "SHAKEN" result; the non-payment table also produces
a "SHAKEN" result — do they apply twice?).

**Secondary gap:** The in-kind counter resets each season. The non-payment threshold presumably
resets when coin pay resumes. Can a captain reset the in-kind counter by making one coin payment
at the end of the third week, then resuming in-kind at week 1 of the new season? The text is
silent.

**Open Questions:**

1. Does in-kind payment satisfy the "paid" condition for non-payment table threshold purposes?
2. If both the in-kind consequences and the non-payment table fire for the same event, do both
   consequences apply or does one take precedence?
3. Can alternating one coin payment and several in-kind payments systematically reset both
   counters?
4. Is there a mechanism by which a captain who pays in-kind indefinitely eventually faces coin
   demand from the men — separate from the in-kind escalation rolls?

**Proposed Rule Change:**

**In-kind payment satisfies the non-payment threshold.** While the captain is providing goods
payment, the non-payment table does not fire. The in-kind escalation table is the only mechanic
that governs goods-payment consequences. The non-payment table governs no-payment consequences.
They are two systems for two different failure modes. They do not overlap and do not both fire
for the same event.

If the captain stops paying entirely — no coin, no goods — the non-payment table fires on its
standard threshold (14 days retainer, 3 days mission). The in-kind counter resets when any coin
payment is made.

---

## 12. Wolfkin Recruitment Pack Bonus — SEVERITY: Low

**Systems involved:** Kin and Recruitment table (Section 2), Settlement tapping rules

The Kin and Recruitment section states: "When you recruit a wolfkin, roll D3. That many additional
wolfkin may accompany them as Common fighters at the same terms, with no additional recruitment
roll."

Standard recruitment taps the source settlement for one year. The wolfkin pack bonus adds 1–3
fighters with "no additional recruitment roll." The text does not specify whether the extras
tap the settlement or are treated as an extension of the initial recruitment.

A wolfkin-adjacent area could supply 2–4 fighters per single roll — multiplying effective
recruitment throughput without incrementally consuming the settlement cooldown.

**Interaction with band growth:** A 7-man Warband wanting to reach 14-man numbers can do so
through wolfkin recruitment in 3–4 recruitment attempts rather than the 6–8 it would take for
a typical half-roll average from human settlement draws. The settlement tap cooldown, which is
the designed limiting mechanism on band growth, does not slow wolfkin expansion at the same rate.

**Open Questions:**

1. Do the pack bonus wolfkin count as drawing from the same settlement for tapping purposes, or
   are they treated as wild companions with no settlement origin?
2. Is the pack bonus a "bring their brothers" fiction mechanic (no settlement tap) or a shared
   settlement draw compressed into one roll?
3. Does the D3 result replace or supplement the initial candidate die? (i.e., is the total
   wolfkin recruited 1 + D3, or does the D3 determine the total?)
4. Can a band exploit wolfkin-dense hexes to fill out to Warband size without triggering any
   settlement's year-long cooldown?

**Proposed Rule Change:**

**Pack bonus draws from the same settlement.** The D3 wolfkin who join in response to the
initial recruitment are drawn from the same community as the first recruit. The settlement is
tapped for the full year regardless of how many arrived — tapping reflects community disruption,
not headcount. A D3 result of 3 means four wolfkin were found and available; they do not each
tap the settlement separately.

**D3 is additional, not total.** The D3 roll determines the number of additional wolfkin beyond
the initial recruit. If D3 = 2, the band gains the initial recruit plus 2 companions = 3 wolfkin
from one settlement tap.

**Wildland wolfkin.** Wolfkin encountered as wanderers in a hex with no settlement origin —
beyond the frontier, in deep wilderness, in ruins — do not tap any settlement, but the standard
recruitment MANIPULATION roll still applies for the initial recruit. Pack bonus still fires on
a D3 result above 1. The GM determines when wolfkin qualify as wildland rather than settlement-
linked.

---

## 13. DRILL Bonus — No Expiry or Cap — SEVERITY: Low — RESOLVED

**Systems involved:** DRILL activity (Section 6, Quarter Day Activities), Veteran fighter
advancement

The DRILL mechanic states: after three successful full weeks of drilling, Veteran fighters gain
+1 to their MELEE for the season. The bonus is awarded per season of consistent drill. There is
no stated cap on how many seasons the bonus can be re-applied, and no stated floor below Veteran
tier at which the bonus is inaccessible.

If the band drills every season for three seasons, Veteran MELEE advances from 2 to 5 (+1 per
season). MELEE 5 at Veteran tier is above the Elite tier baseline (MELEE 3 at creation), meaning
long-running drilled Veterans outperform freshly recruited Elites on combat rolls.

The TRAINING GROUNDS bonus (reduces COMMAND roll difficulty) compounds with this: three
seasons of drilled Veteran fighters at MELEE 5 becomes the dominant staffing strategy when
combat reliability is the primary concern.

**Open Questions:**

1. Is the +1 MELEE from DRILL cumulative across seasons, or does it apply once (Veterans are
   "trained" permanently after the first successful drill cycle)?
2. Is there a cap on MELEE advancement through DRILL?
3. Does the DRILL bonus expire at the season boundary and require re-earning, or does it persist
   until the campaign ends?
4. Is the TRAINING GROUNDS requirement intentionally gating early-game DRILL, or is the bare-camp
   drill field (one QD labor, 40 WOOD) effectively an equal alternative?

**Proposed Rule Change:**

**DRILL grants trained status, not MELEE advancement.** Remove the sentence "Veteran fighters
gain +1 to their MELEE for the season." Replace with: Veteran fighters who complete a DRILL
cycle are **trained** for the season. Trained fighters do not check MORALE when casualties reach
the standard threshold during engagements that season — they hold.

**No MELEE advancement through DRILL.** Skill advancement for Named Men occurs through XP only.
DRILL makes common fighters more reliable, not statistically more lethal. An Elite Named Man
with MELEE 3 who has drilled for three seasons still has MELEE 3.

**Trained status expires.** Trained status ends at the season boundary. The next season's trained
status requires a new three-week DRILL cycle to earn. It does not accumulate.

**TRAINING GROUNDS vs. field drill.** Both routes produce the same trained status outcome. The
TRAINING GROUNDS reduces the COMMAND roll difficulty by 1 for the DRILL check — it is a ease-
of-achievement advantage, not a gating requirement.

**STATUS: RESOLVED.** Integrated into proposal: DRILL now grants trained Veteran status (no MORALE check on casualties that season). MELEE advancement through DRILL removed. Trained status expires at season boundary.

---

## 14. Named Man XP on a 1 Rewards Reckless Play — SEVERITY: Low — RESOLVED

**Systems involved:** Named Man Advancement (Section 7), XP awards table

The XP awards table for Named Men gives:

- On a 1 (worst result): **3 XP** and a critical injury roll
- On a 5 (good result): **3 XP** — no injury
- On a 4–3 (moderate): **2 XP**
- On a 2 (poor): **0 XP**
- On a 6 (best): **5 XP**

The result on a 1 ties with a 5 result and beats a 4–3 result. A Named Man who rolls 1 every
engagement earns 3 XP per fight and accumulates critical injuries at the same time. A Named Man
who rolls 3–4 repeatedly earns less XP than one who keeps getting hurt.

Because Named Men advance toward eligible full-character transitions at 15 XP, and the 1-result
gives 3 XP with a critical injury, the fastest advancement path includes frequent worst-case
outcomes — which is the opposite of incentive design for a Named Man the players want to keep.

The pairing of "high XP + injury" on a 1 may be intentional (hardship builds story) but it
creates a structural tension: the GM is rewarded for putting Named Men in harm's way frequently,
and the players are rewarded for a Named Man surviving significant damage.

**Open Questions:**

1. Is the 3 XP on a 1 intentional — the fiction of learning through survival after near-death —
   or should the worst result yield 0 or 1 XP?
2. Does the full character transition require spending XP at the 2:3 rate from any XP total, or
   specifically require the Named Man to have _earned_ 15 XP rather than accumulated it from
   a mix of results?
3. Is the intent that injury-accumulating Named Men advance faster and arrive at the full
   character sheet with more persistent wounds — a deliberate backstory-generation mechanic?

**Proposed Rule Change:**

**Change XP on a 1 to 1 XP.** The critical injury is already the engagement's consequence — it
does not need to be paired with an advancement reward that ties fast progression to harm. 1 XP
marks that the Named Man survived; it does not honor the outcome.

Revised XP table:

| ROLL | XP  | ADDITIONAL CONSEQUENCE |
| ---- | --- | ---------------------- |
| 6    | 5   | —                      |
| 5    | 3   | —                      |
| 4–3  | 2   | —                      |
| 2    | 0   | —                      |
| 1    | 1   | Roll critical injury   |

**Note on transition pacing.** At 1 XP on a 1, a Named Man reaching 15 XP through injury alone
would require 15 worst-case results — impractical given that critical injuries accumulate
permanent effects. In practice, the transition threshold is reached through a mix of results
weighted toward play, not toward damage.

**STATUS: RESOLVED.** Integrated into proposal: XP on a 1 reduced from 3 XP to 1 XP. Critical injury consequence unchanged.

---

## 15. Vengeance Oath — +1 MANIPULATION Stacks With No Ceiling — SEVERITY: Low — RESOLVED

**Systems involved:** Blood Oaths — Vengeance oath (Section 6 Optional), MANIPULATION attribute

The vengeance oath grants: "the oathed party gains a permanent +1 MANIPULATION when attempting
to gather information specifically about the oath target."

The blood oath rules do not cap successive vengeance oath bonuses when multiple oaths are sworn
against multiple targets. Each sworn vengeance adds +1 MANIPULATION to information-gathering
against that specific target. A character with three vengeance oaths against three targets has
MANIPULATION +1 for information on Target A, +1 for Target B, +1 for Target C.

In narrow practice this is fine — the bonus applies per named target only. But a Named Man
who swears vengeance against the major faction or warchief the band is contracted to destroy
gains +1 MANIPULATION on intelligence gathering that likely covers the entire operation.

**More significant gap:** The vengeance oath cannot be dissolved. It cannot be broken. It cannot
be traded away. A Named Man with a vengeance oath will refuse contracts protecting the target.
This means a player character Named Man transitioning to full character (per the advancement
rules) carries an irremovable obligation that may conflict with future player-chosen contracts.
Post-transition, the player is bound by an NPC rule that was not their choice.

**Open Questions:**

1. Does the +1 MANIPULATION from a vengeance oath apply to the specific target only, or to any
   information gathering connected to that target's faction or organization?
2. Can multiple vengeance oaths sworn against the same target stack into +2 or +3 MANIPULATION?
3. On Named Man transition to full character, does the vengeance oath obligation transfer to
   the player's character intact, or is the player given the option to have the character renounce
   it with consequences?
4. What is the mechanism for a vengeance oath sworn against a target who is subsequently killed —
   does the oath discharge on target death, or does it persist ("unfinished" against the target's
   heirs or successors)?

**Proposed Rule Change:**

**Named individual only.** The +1 MANIPULATION bonus applies to information gathering about
the specific named person. Not their organization, their faction, or people connected to them.
An oath against Warchief Harald applies when asking where Harald sleeps. It does not apply when
asking about the disposition of Harald's garrison.

**No stacking against one target.** Multiple vengeance oaths sworn against the same individual
do not stack. The second oath confirms the first; the bonus remains +1.

**Discharge on witnessed death.** The oath discharges when the oathed party personally witnesses
the target's death or receives verifiable proof — a physical token of identity, a credible
witness the oathed party trusts. Hearsay does not discharge the oath. On discharge, the
obligations lapse: the Named Man may take contracts involving that target's faction without
rolling against Loyalty.

**Named Man transition.** When a Named Man becomes a full player character, the player chooses:
Honor the oath (it carries forward under player control, +1 MANIPULATION intact), Renounce it
(the character loses the +1 MANIPULATION permanently and takes −1 to Reputation in settlements
where the original oath was known), or Hold it (obligation exists but is not actively pursued —
the character may accept conflicting contracts but rolls at +1 difficulty on any check directly
involving the oath's subject).

**STATUS: RESOLVED.** Integrated into proposal: +1 applies to named individual only; no stacking on one target; oath discharges on confirmed death; Named Man transition offers Honor/Renounce/Hold choice.

---

## 16. Loot Share Archetype — No Downgrade or Renegotiation Mechanic — SEVERITY: Low — RESOLVED

**Systems involved:** Band archetypes (Section 1), Loot share tables

Four loot share archetypes are defined:

- **Tyrant:** Captain 60%, Named Men 20%, Veterans 12%, Commons 8%
- **Standard:** Captain 40%, Named Men 25%, Veterans 20%, Commons 15%
- **Fraternal:** Captain 25%, Named Men 25%, Veterans 28%, Commons 22%
- **Kin-Clan:** Captain 15%, Named Men 20%, Veterans 30%, Commons 35%

Archetype is declared at band formation. No mechanic in the proposal addresses when or whether
it can change. A Tyrant taking 60% has no forced renegotiation trigger if the band prospers,
if a new Named Man joins who operates under different expectations, or if the men calculate that
their cut does not match their risk over time.

Conversely, a Fraternal band that enters financial difficulty has no mechanism for the captain
to renegotiate upward — no "temporary Tyrant override" during loan-debt seasons. The captain
simply takes 25% of a smaller haul and cannot unilaterally claim more to cover costs without
violating the archetype standard.

**Interaction with Named Man Triggers:** Named Man Trigger 6 is "Witness to the leader taking
more than their promised share of plunder." This implies violation of the stated archetype is
a loyalty trigger. But it does not imply that the stated archetype can ever be renegotiated —
only violated. There is no legal path to change the split.

**Open Questions:**

1. Can a captain declare an archetype change between contracts, and if so, what — if anything —
   is required (Named Man consent, MANIPULATION roll, season transition)?
2. Can individual Named Men renegotiate their personal share outside the archetype structure?
3. Is the intent that archetype is permanent for the band's lifetime, or that it should shift
   naturally as band conditions change?
4. What happens when a Kin-Clan band's founding members are mostly dead and the survivor
   composition no longer reflects kin demographics — does the archetype persist by inertia, or
   does it become contested ground?

**Proposed Rule Change:**

**Archetype may be renegotiated once per season.** At any season boundary, the captain may call
a council. Named Men state their position; anonymous fighters do not vote but their presence is
a factor. The captain makes a MANIPULATION roll:

- Moving toward a more equal split (Tyrant → Standard, Standard → Fraternal, Fraternal → Kin-Clan):
  difficulty 2, reduced by 1 for each Named Man at Loyalty 3. Minimum difficulty 1.
- Moving toward a harder split (any direction favoring the captain's share):
  difficulty 3. Named Men at Loyalty 1 who oppose the change roll against Loyalty immediately.

On success, the archetype shifts one tier in the declared direction. On failure, the archetype
holds and the attempt is noted; a second failed attempt in the same season costs MORALE −1.

**Archetype does not shift unilaterally.** Taking more than the stated share without a council
remains Trigger 6 for Named Men. A council is the only legal path to change the split.

**Demographic drift.** When the majority of a Kin-Clan band's surviving fighters no longer share
the founding kin, the archetype is treated as contested: the MANIPULATION difficulty for shifting
it away from Kin-Clan drops to 1. This is a GM call based on band composition.

**STATUS: RESOLVED.** Integrated into proposal: once-per-season council procedure added with MANIPULATION difficulty formula for both shift directions. Demographic drift provision included.

---

## 17. Flyting Refusal Auto-Escalates — SEVERITY: Low — RESOLVED

**Systems involved:** Arguments and Escalation — optional subsystem (Section 6)

The flyting rules state: "The other party may accept or refuse [flyting]. Refusal pushes the
argument one stage forward immediately — declining the word-fight in front of witnesses reads
as an admission the man's mouth is not worth hearing."

This creates a forced-choice trap. If a character accepts flyting, they make an opposed
PERFORMANCE roll they may lose. If they refuse, the argument escalates one stage regardless.

For a player character who is not optimised for PERFORMANCE (most fighter-type PCs), a Stage 3
argument means: accept flyting (likely lose the PERFORMANCE roll), or refuse and auto-escalate
to Stage 4 (combat). There is no neutral action. The only way out is to not be a party to the
argument in the first place, but at Stage 3 (drawn weapons), the escalation has already involved
them.

**Interaction with Stage 4 D6 roll:** Stage 4 with no intervention has a 1-in-6 chance of
producing a dead participant. A player character with poor PERFORMANCE who refuses flyting at
Stage 3 will auto-escalate to Stage 4 and then roll this die. The choice was forced, not played.

**Open Questions:**

1. Is refusing flyting allowed to be a valid tactical choice for a PC who is physically stronger
   but socially weak — i.e., is "win by fighting instead" a legitimate refusal outcome?
2. Should refusal of flyting produce a different consequence than automatic stage escalation —
   for example, the crowd's opinion shifts (NPC Standing adjustment) but the stage does not move?
3. Is the flyting mechanic intended specifically for NPC-vs-NPC disputes the PCs can intervene
   in, or for PC-vs-NPC and PC-vs-PC disputes equally?
4. Can a PC decline to participate in flyting by removing themselves from the scene, and if so
   at what stage is that still physically possible?

**Proposed Rule Change:**

**Refusal holds the stage.** A character who refuses flyting does not automatically push the
argument to the next stage. The stage holds. However:

- Any Named Man watching notes the refusal. The GM records it; it may color later interactions
  between that Named Man and the refuser. No immediate mechanical change.
- The refuser's next intervention roll in this argument is at +1 difficulty. They declined the
  word-fight in front of the company and the crowd's expectations are already engaged.

**Accepting flyting is the lower-cost path.** A character who refuses and then loses the Stage
4 fight has given the company nothing to respect before the blood hit the ground. Accept flyting,
lose the PERFORMANCE roll, and the company saw you try. The social cost of a clean loss in
flyting is lower than the cost of refusing and then losing anyway.

**Withdrawing before Stage 4.** A character who removes themselves from the vicinity before any
blow is struck — sits down, sheathes their weapon, walks away — exits the argument at no
mechanical cost up through Stage 3. At Stage 4, steel is moving. Leaving at that point is flight,
which the company treats as such. Withdrawal at Stage 3 before the blow is clean. Withdrawal at
Stage 4 after it has started is not.

**STATUS: RESOLVED.** Integrated into proposal: refusal holds stage (no auto-advance); refuser takes +1 difficulty on next intervention roll; clean withdrawal permitted at Stage 3 or below.

---

## Summary — Open Items By Priority

### Resolve Before Integration

These items create fundamental ambiguity that will produce table-breaking inconsistency
across groups. They require a mechanically complete answer before the proposal goes into the
corebook.

| Priority | Issue                                 | Minimum Required Fix                                                                             |
| -------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 1        | #3: Atrocity loop (CRITICAL)          | Conditional trigger at MORALE ≤2 only; archetype-share plunder condition; COLD-BLOODED scope fix |
| 2        | #4: Grievance difficulty undefined    | A numeric mapping from grievance type/count to difficulty 1–5; atrocity+plunder raised to 2      |
| 3        | #1: MORALE trigger pile-up / no floor | Net movement cap of 3/week; severity-ranked firing order; recovery path from MORALE 1            |
| 4        | #2: Trigger vs. check boundary        | Voluntary check costs QD, once/week max, targets highest-severity grievance                      |
| 5        | #6: Loyalty scale 1–3 vs. Loyalty 5   | Cap at 3; no settled mechanic; positive triggers at cap do nothing                               |

### Address Before Playtest

These items may create dominant strategies or significant play friction. They do not break
the system but they produce predictable degenerate outcomes at experienced tables.

| Priority | Issue                                          | Core Question                                                                                |
| -------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------- |
| 6        | #5: Four social currency systems               | Separate axes — Reputation adjusts floor, Allegiance adjusts difficulty; no stacking formula |
| 7        | #7: Occupation economic bypass                 | Yield at 1D3; Feud Track advances; settlement drain after extraction                         |
| 8        | #9: Reputation + caster premium stacking       | Separate axes — Rep adjusts offer, caster adjusts contract type; 1.5× ceiling retained       |
| 9        | #10: Loyalty decay spiral in MORALE depression | Fear-Held at 1/week to floor 0; same speed, higher stakes                                    |

### Clarify in Final Draft

These remaining items are low-severity loose ends that benefit from a clear answer but will not
break play if left as GM judgment.

Issues #8, #11, #12 — see individual entries above.

Issues #13, #14, #15, #16, #17 — **RESOLVED.** Proposed rule changes integrated into the band management proposal.
