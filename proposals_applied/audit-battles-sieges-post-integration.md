<!-- markdownlint-disable MD013 -->

# Post-Integration Balance Audit — Battles & Sieges Chapter 12

**Scope:** 12 rules integrated from `proposals/proposal-battles-and-sieges-overhaul.md`
into `02-gamemasters-guide/12-battles-and-sieges.md`.

**Method:** Rule-by-rule analysis against the base battle system. Each section notes the
interaction, identifies any stacking, edge case, or dominant-strategy concern, and records
a verdict with any outstanding flags.

---

## Summary Verdicts

| ID | RULE | VERDICT |
|---|---|---|
| P5.1 | Terrain | PASS — five types, well-bounded |
| P5.2 | Weather | PASS — probabilistic (1-in-6), table broad enough |
| P5.3 | Night Attack | PASS — conditional on sentries, binary structure |
| P5.4 | Champion's Duel | PASS — opt-in, morale stakes proportional |
| P5.5 | Feigned Retreat | PASS — once per troop, opposed roll risk |
| P5.6 | Battle Magic | FLAG — translation table has gaps; see notes |
| P5.7 | Aerial Units | PASS — distinct from ground cavalry |
| P5.8 | Undead and Misgrown | PASS — immunity trade-off is clear |
| P5.9 | Pursuit | PASS — tactical cost enforced |
| P5.10 | Aftermath | PASS — post-battle scaffolding, not game-mechanical |
| P5.11 | Death to Cowards expanded | PASS — increased risk matches increased stakes |
| P5.12 | Veterans | FLAG — die upgrade pace needs GM discipline |

---

## Detailed Analysis

### P5.1 — Terrain

**What it does:** Five terrain types affect base dice (High Ground adds +1 advantage die;
Muddy/Wet reduces cavalry base dice by 1; Forest/Broken blocks cavalry attack; River
Crossing halves base dice on crossing turn; Prepared Ground removes 2 cavalry base dice).

**Stacking concern:** High Ground + Flanking + Important Character = +3 advantage dice on
the turn of engagement, which is within the existing +5 cap. No stacking violation.

**Dominant strategy check:** Prepared Ground at −2 base dice is the most powerful single
terrain modifier. It requires 24 hours of preparation, which means the attacker gets a
strategic choice: deny the preparation window by attacking early (before it's ready) and
fight on unprepared ground, or wait and face the penalty. This is a useful tension. It does
not automatically favor defenders — cavalry-heavy attackers who avoid the prepared section
nullify it entirely.

**Edge case:** What if all three sections are Prepared Ground? The rule says "the ground in
front of their line." A disciplined GM interprets this as covering the defensive frontage,
not blocking off side approaches. No rule change needed; GM judgment sufficient.

**Verdict:** PASS.

---

### P5.2 — Weather

**What it does:** D6 at battle start. On 1 (16.7% probability), roll again for condition.
Six conditions on D6.

**Probability analysis:** Any specific adverse weather condition has a 2.8% base probability
(1/6 × 1/6). This is low enough that weather is memorable when it occurs without dominating
preparation. GMs who want more weather can roll a D6 at the start of each quarter day of
a long battle.

**Condition balance:**

- Heavy rain/snow: ranged penalty + cavalry slow. Targets two already-conditional troop types.
  Reasonable.
- Dense fog: halves advantage dice both sides, blocks first-turn flanking. Equalizer for
  disadvantaged armies. Reasonable.
- Bitter cold: −1 starting morale everywhere + broadened demoralization. A flat army-wide
  penalty is a meaningful escalation. This condition has the most teeth.
- Crosswind: ranged only, directional. Very narrow effect; may have no impact if no ranged
  troops are present.
- Dust: delayed fog. Interesting because the first 2 turns are normal, then disruption begins.
- Unseasonable heat: exhaustion on turn 3+. Incentivizes fast aggressive battles. Reasonable.

**Flag:** The crosswind condition (result 4) is the weakest — if neither side fields light
ranged weapons, it has no effect. Consider whether a fallback ("if no ranged troops are
present, reroll once") is needed. Not mandatory; the GM can narrate it as irrelevant and
move on.

**Verdict:** PASS.

---

### P5.3 — Night Attack

**What it does:** No sentries = free first turn for attacker. Sentries = halved advantage
dice both sides for 2 turns. Torchlight removes the defender's penalty. Commanding SCOUTING
roll: failure costs attacker 1D3 base dice to confusion.

**Balance check:** The free first turn for no-sentinel defense is high-value but requires
the defending player to genuinely neglect the sentry rule. It is not a default ambush —
it requires a specific preparation failure. The incentive to maintain sentries is clear.

**The SCOUTING roll risk:** Losing 1D3 base dice before the first attack roll is substantial.
Average loss = 2 base dice. This makes night attacks risky for the attacker unless they
have a skilled commander. The risk/reward is appropriate: a night attack that succeeds
cleanly is devastating; a botched one weakens the attacker immediately. This is correct design.

**Torchlight interaction:** A defender who lights the field removes their own penalty but
silhouettes the attackers. The rule does not give the defender an attack bonus for this —
it only removes their disadvantage. If the intent is that torchlight is an active asset
(not just a neutralizer), a future proposal could add +1 advantage die for defenders in
torchlight for turns 2+. Not needed now.

**Verdict:** PASS.

---

### P5.4 — Champion's Duel

**What it does:** Pre-battle opt-in single combat. Refusal costs 1D3 morale across all
troops. Victory/loss shifts morale equal to the victor's current Strength. Battle still
occurs afterward.

**Morale swing analysis:** The average PC Strength is around 4 (standard character).
A champion victory therefore moves 4 morale points. In the context of the base battle,
the General's Speech typically generates 1–3 morale points per troop. A 4-point swing
to the winner distributed freely across all troops is significant but not decisive — it
does not end a battle before it begins. Correct weight.

**Refusal cost (1D3 across all troops):** Average 2 morale lost. This is lower than the
victory swing, which means the game theory slightly favors refusing for an army with
very few morale points (they risk less by refusing and losing 2 than by fighting and
losing 4). A strong army rationally accepts; a weak army might rationally refuse. This
asymmetry is plausible and produces interesting decisions.

**PC alternate skills:** Allowing MANIPULATION for a verbal contest opens the mechanic to
non-combat characters. This is good for player variety. The morale stakes are unchanged,
which is correct — a verbal victory before battle should carry the same weight.

**Verdict:** PASS.

---

### P5.5 — Feigned Retreat

**What it does:** Opposed PERFORMANCE vs INSIGHT. Success: troop gains a free D8 pursuit
die next turn (not subject to base dice cap) on re-entry. Failure: genuine retreat +
morale roll. Once per troop per battle. Cavalry and skirmishers only.

**Stacking concern:** The D8 pursuit die is "not subject to base dice cap." This means it
adds to the troop's total dice that turn. Combined with normal base dice (up to 5D6) plus
advantage dice (up to 5 more), the pursuit die is one extra die. On a full-strength cavalry
troop with all five advantage dice and five base dice, this is 11 dice total on the re-entry
turn. That is a significant burst turn. Given that the troop spent the previous turn
withdrawing (not attacking), the net two-turn investment is approximately neutral — one
turn missed, one turn enhanced. The mechanic is cost-balanced.

**Failure condition:** A genuine retreat + morale roll on failure is a real risk. This
prevents the Feigned Retreat from being a free tactical option. Combined with once-per-troop
limits, the risk/reward is appropriate.

**Edge case — feigning with a weakened troop:** A troop at 2 base dice feigning retreat
and succeeding returns with a D8 bonus. At 2D6 + 1D8, their output is modest. The
mechanic does not become more powerful as troops weaken. Correct.

**Verdict:** PASS.

---

### P5.6 — Battle Magic

**What it does:** Mage sacrifices their advantage die contribution for the turn. Casts a
spell using WP and Chapter 7 rules. GM translates: 2 effective Power Level of damage = 1
troop damage; conditions become Demoralized, reduced base dice, or forced morale roll for
1D3 turns; range scales from near to long.

**Integration concern (FLAG):** The FL2E magic system does not use skill rolls for spells
— it uses WP to determine Power Level, then rolls base dice equal to WP spent to check
for overcharge and mishap. The conversion rule (2 PL = 1 troop damage) creates a
translation layer. This layer is functional but relies on the GM to apply it consistently.

**Specific gaps:**

1. **Overcharge interaction:** If the mage overcharges (results of 6 on spell dice), the
   Power Level increases. The current rule says "effective Power Level applied to direct
   harm." Does overcharge count? Answer: yes — it should. Effective Power Level includes
   overcharge. This should be stated explicitly.

2. **Mishap during battle:** If the mage rolls a 1 (skull) during the battle turn, a magic
   mishap occurs. Mishaps are personal, not troop-level. A mishap during a battle turn
   could immediately incapacitate the mage (e.g., Broken), which removes the advantage die
   they were contributing for all future turns. This is correct and no rule change is needed —
   the personal risk of casting in battle is already built into the mishap system.

3. **Area spells:** Some spells affect multiple targets at once. A spell that affects an
   entire "short range" area applied to an enemy troop section is more powerful than the
   conversion table implies. The rule says "per 2 PL applied to harm." For area spells,
   GM should adjudicate whether the damage is split across all troops in the section or
   applied to one. This needs a clarifying sentence.

**Recommendation:** Add to the Battle Magic section:

- "Overcharge successes count as part of the effective Power Level for damage conversion."
- "Area spells that would affect multiple troops split their effective Power Level equally
  across affected troops, rounded down per troop."

These can be added in a minor revision. The core mechanic is sound.

**Verdict:** FLAG — minor clarifications needed.

---

### P5.7 — Aerial Troops

**What it does:** Classified as cavalry. Cannot be engaged in melee by ground forces until
they descend. Aerial charge = flanking/rear attack; polearm Attacks First does not apply.
Size advantage die applies if larger. Ranged suppression: 3+ successes = double damage.
Daily cost 2× equivalent ground cavalry.

**Power level check:** Aerial troops that charge from above receive flanking without
needing to execute a flanking maneuver. This is a significant advantage. It is partially
offset by: (a) ranged troops can double their damage against them on a good roll, (b) once
they land and engage, they fight as cavalry and can be counter-engaged normally, (c)
their daily cost is doubled.

**Dominant strategy concern:** An aerial troop that repeatedly charges and withdraws before
being engaged could deal consistent flanking-advantage attacks every turn. The Feigned
Retreat rule mitigates this somewhat (the feigned retreat is limited to once per troop per
battle). However, aerial troops do not need to use Feigned Retreat to withdraw — they can
simply fly clear if not engaged. This could become a sustained rotation that is difficult
to counter without ranged troops.

**Recommendation:** Add: "An aerial troop that withdraws from melee after attacking must
spend 1 morale point to break contact cleanly. Without that cost, they are forced to
remain engaged for 1 additional turn." This applies the standard cavalry withdrawal logic
to aerial troops and prevents cost-free harassment loops.

This is a non-blocking flag — aerial units are rare enough in the Ravenlands that the
dominant strategy is unlikely to emerge in normal play. The rule can be added at the
GM's discretion.

**Verdict:** PASS with optional recommendation.

---

### P5.8 — Undead and Misgrown Armies

**What it does:** No morale, no supplies. Controller dependency: loss of controlling
character → half base dice immediately, then −1/turn until inert. Feral hordes exempt from
controller dependency but cannot receive orders. Demonic presence: −1 morale/turn to
enemies for first 3 turns. Fearless troops immune.

**Balance check — morale immunity:** A troop that cannot be Demoralized and never flees is
very strong. The trade-off: it still takes base dice damage normally, it still needs to be
fielded in numbers, and the controller dependency creates a specific vulnerability. The
"kill the necromancer" mission objective becomes mechanically meaningful. This is correct
design — it creates a high-value target.

**Controller dependency timing:** Half base dice lost immediately on controller death is a
large single-turn swing. If the controller is a PC (an NPC necromancer leading an allied
undead force, for example), this creates significant jeopardy around protecting that
character. The rule creates appropriate narrative stakes.

**Demonic presence stacking:** A force with both Misgrown and undead would apply the
−1 morale/turn effect once, not twice. The rule should be read as applying to the army
as a whole, not per troop or per creature. This is the correct interpretation — a single
ruling from the GM suffices.

**Verdict:** PASS.

---

### P5.9 — Pursuit

**What it does:** Cavalry only. Pursuing cavalry rolls full dice vs routing troop's
remaining base dice. Each success removes soldiers permanently. Pursuing cavalry
cannot participate in the main battle roll that turn.

**Tactical cost check:** Removing cavalry from the main battle roll is the enforcement
mechanism. At 5 base cavalry dice + 5 advantage dice, the cost of missing one main battle
roll is significant. On a turn where the main battle is tight, sending cavalry to pursue
can lose the center. This is correct and creates real decisions.

**Permanent removal:** Unlike normal morale losses (which can be rallied), pursuit-killed
soldiers are permanently removed. This makes routing genuinely dangerous at the campaign
level, not just in the immediate engagement. Correct severity.

**Edge case — routing of a 1-die troop:** A troop routing with only 1 base die remaining
loses all soldiers on a single success from pursuit cavalry. Given that 5+ attack dice vs
1 defense die is nearly guaranteed to produce at least 1 success, this is correct — a
single soldier group cannot outrun a cavalry force. Appropriate.

**Verdict:** PASS.

---

### P5.10 — Aftermath

**What it does:** Introduces three post-battle resolution elements: ransom table for
captured characters (5 tiers), stripping the dead (D6 trade goods per 10 base dice of
destroyed troops, costs a quarter day), wounded character roll (D6: 1 = death, 2–4 =
1D3 weeks care, 5–6 = normal recovery; healing character present = D6+1).

**Economic check — stripping the dead:** Average D6 = 3.5 goods per 10 base dice. A
major battle that destroys 5 full troops (50 base dice total) yields an average of 17.5
trade goods from the dead. This is meaningful loot for an adventuring party but not so
large it warps the economy. Reasonable.

**Wounded character roll:** On D6, results are:

- 1/6 chance of death (16.7%)
- 3/6 chance of extended recovery (50%)
- 2/6 chance of normal recovery (33.3%)

With healing care (D6+1): death becomes impossible (minimum 2), recovery options shift to
50% extended / 50% normal. The healing care bonus is therefore significant — it changes
the worst outcome from lethal to inconvenient. This creates an incentive to have a healer
present in battle and reward the investment.

**Ransom values:** The table runs from 10 copper (common soldier) to 2,000+ copper (general
or lord). The base economy of the game uses copper per day costs (soldiers at 5–35 copper/
day). A general's ransom (2,000+) represents roughly 2 months of a full company's wages.
This is a plausible negotiating value. Not game-breaking.

**Verdict:** PASS.

---

### P5.11 — Death to Cowards (Expanded)

**What it does (revised):** Executes 1D6 soldiers per turn. Each remaining troop rolls
morale: success adds 1 morale point, failure loses 1 morale point. Next-session morale
check for the whole army; failure causes 1D3 base dice of desertion.

**Original version vs expanded:** The original gave a flat +1 morale per executed group to
remaining troops. The expanded version creates a split result — some troops respond with
increased loyalty, others with decreased loyalty, reflecting realistic psychological
division. This is more tactically complex and more narratively accurate.

**Math check:** Expected morale outcome per turn of execution, assuming 3 troops in the
army and a 50% morale roll success rate: +1.5 morale gained by successes, −1.5 morale
lost by failures. Net expected = 0. The mechanic is not a reliable morale generator — it
is a gamble with morale. This is correct. A general ordering executions is not doing it
for the expected value; they are doing it because they have no better option.

**Next-session morale check:** The post-battle desertion mechanic adds long-term cost to
a short-term gamble. The 1D3 base dice of desertion (average 2) is a meaningful loss of
strength for the long campaign.

**Verdict:** PASS.

---

### P5.12 — Veterans

**What it does (integrated):** 3+ battles survived intact → Veterans status. Advantage
dice upgrade D6 → D8 → D10 → D12 (each tier requires 3 more battles). First morale
check per engagement waived. Commander loss triggers Formidable morale check. Cannot
be purchased, only earned.

**Power level check (FLAG):** The advantage dice upgrade is the most mechanically
significant element. Comparing D6 to D8 advantage dice: a D8 succeeds on 6, 7, or 8 —
three out of eight faces, or 37.5%. A D6 succeeds on 6 — one out of six faces, or 16.7%.
A Veterans troop with 5 advantage dice (D8s each) has an expected 1.875 successes from
advantage. A fresh troop with 5 advantage dice (D6s) has expected 0.83 successes. This is
a 2.25× multiplier on advantage dice effectiveness for Veterans. That is a large
difference.

**Mitigating factors:**

- Veterans cannot be purchased, so the army cannot field an all-Veterans force at the
  start of a campaign.
- The upgrade requires 3 survived battles intact — attrition will remove many troops
  before they earn it.
- The base dice (from numbers) are unchanged. A Veterans troop still needs bodies.
- The first morale check immunity is a once-per-engagement benefit, not a sustained one.

**Concern:** At D10 and D12 advantage dice (6+ battles survived), the troop becomes
significantly more powerful than fresh recruits. A D12 succeeds on 6–12 — seven out of
twelve faces, or 58.3%. This is nearly three times better than a fresh D6 advantage die.
For a long campaign in which the party has nurtured specific troops across many battles,
this creates a powerful and narratively meaningful reward. The concern is whether it creates
an imbalanced dominant line — a small core of Veterans that cannot be lost.

**Recommendation:** Consider whether the maximum should be capped at D10 (not D12) in
play, or whether D12 requires more than 9 battles to reach. The proposal said
D6→D8→D10→D12 but did not specify intervals for D10→D12. If D10→D12 also requires 3+
battles, reaching D12 means 12+ battles of survival — rare in most campaigns. This is
probably the intended cadence. No change required unless playtesting reveals dominance.

**Verdict:** FLAG — watch in extended campaign play. Mechanically sound for most campaign
lengths. No immediate change needed.

---

## Outstanding Actions

| ID | ACTION |
|---|---|
| P5.6 | Add overcharge clarification: "Overcharge successes count toward effective Power Level for damage conversion" |
| P5.6 | Add area spell clarification: "Area spells split effective Power Level equally across affected troops, rounded down" |
| P5.7 | Optional: add aerial disengagement cost (1 morale to break contact cleanly) if playtesting reveals harassment loops |
| P5.12 | Monitor Veterans advantage dice in extended campaign play; consider D12 tier cap if dominance emerges |

---

## Overall Assessment

The twelve integrated rules hold together. They build on the existing dice pool system
without contradicting it. The most significant mechanical additions — Pursuit, Feigned
Retreat, Veterans — each carry clear costs. The most narratively significant additions —
Death to Cowards, Aftermath, The Challenge — deepen the human weight of the battle layer
without adding mechanical complexity the GM must track during the fight.

Battle Magic is the only rule that required design adaptation during integration: the
original proposal assumed a skill-based magic system, but FL2E uses WP and Power Level.
The adaptation is functional. The two clarifications flagged above should be added in
the next chapter revision pass.

Veterans is the only rule with long-term power level uncertainty. It is the intended
reward for caring about your soldiers across a campaign. The uncertainty is a feature
of the design, not a flaw in it.

---

*Audit completed after integration of all 12 rules into `02-gamemasters-guide/12-battles-and-sieges.md`.*
*Source proposal: `proposals/proposal-battles-and-sieges-overhaul.md`.*
