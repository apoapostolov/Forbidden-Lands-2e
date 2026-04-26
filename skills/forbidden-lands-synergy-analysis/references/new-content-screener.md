<!-- markdownlint-disable MD013 -->

# New Content Screener

## Purpose

This document is the professional decision tree for designing, auditing, and approving new rules for Forbidden Lands 2E.

It serves two users:

1. **An AI generating new rules** — run this tree before presenting a draft. Every rule that exits this tree should be safe to playtest.
2. **A designer asking an AI to audit rules** — feed the proposed rule and ask the AI to run this tree. The output is a structured verdict with specific risks identified.

The tree is grounded in 151 worked synergy examples from the exploitation-surface-catalog.md. Every danger zone, pattern, and red flag below is derived from actual rule interactions confirmed against the manuscript.

---

## How To Use This Document

**If you are creating a new rule:**

1. Start at Step 1 (Design Identity Check)
2. Work through all seven steps in order
3. Exit with a verdict: Safe, Flag, Cap, Restructure, or Reject

**If you are auditing an existing rule or proposal:**

1. Start at Step 3 (Mechanism Tagging)
2. Work through Steps 3-7
3. Exit with a structured verdict and fix recommendations

**If you are doing a quick screen (under 5 minutes):**

1. Write the one-sentence mechanism summary (Step 2)
2. Tag it (Step 3)
3. Check red flags (Step 6)
4. If no tags fire and no red flags hit, the rule is likely Safe

---

## Step 1 — Design Identity Check

Before writing any mechanic, answer these three questions.
If any answer is "no," stop and redesign.

### Does this rule preserve the pressure economy?

Forbidden Lands works because ambition costs something.
Every gain should require a risk, a resource, a time cost,
or a tradeoff that closes off another option.

**Pressure channels the game depends on:**

| Pressure Channel | What It Does | What Breaks It |
| --- | --- | --- |
| Resource attrition | Forces rationing, foraging, trade | Unlimited supply, infinite crafting |
| Injury fear | Makes violence a real decision | Cheap healing, death bypass, armor stacking |
| Action scarcity | Forces turn-by-turn choices | Free actions, extra slow actions, Commander spam |
| WP scarcity | Makes talents and spells cost something | WP refund loops, passive WP generation |
| Time pressure | Makes Quarter Days matter | Travel bypass, instant recovery, dream training |
| Mishap risk | Makes magic dangerous | Safe casting at zero dice, mishap negation |
| Social resistance | Makes NPCs autonomous | Auto-compliance, mind control without resistance |
| Darkness and weather | Makes the wilderness hostile | Environmental immunity, permanent light, Firewalker |

**Rule:** If the new mechanic removes a pressure channel
entirely (not temporarily), it must be redesigned
or gated behind extreme cost.

### Does this rule require a meaningful decision?

Count the decisions needed to use the rule in play:

- **0 decisions** = automatic, passive, always-on → highest risk
- **1 decision** = one-time setup at character creation → high risk
- **2-3 decisions** = build + play setup → moderate risk
- **4+ decisions** = per-use cost, positioning, timing → low risk

**Rule:** Abilities at 0-1 decisions that activate
per-round need hard limits (per-QD, WP ceiling,
target cap, or situational trigger).

### Does this rule respect the recovery curve?

The game assumes:

- attributes recover slowly (rest, healing, camp)
- critical injuries linger (days to permanent)
- WP is earned through desperation, not passive income
- dead is dead (resurrection is epic-tier and rare)

**Rule:** Any mechanic that accelerates recovery
must pay a proportional cost. Fast healing needs
WP + action + risk. Free healing breaks the game.

---

## Step 2 — Mechanism Summary

Write one sentence describing what the rule does
mechanically. Strip all flavor and theme.

Good:

- "Grants 1 WP when the character takes Strength damage."
- "Allows a second melee attack as a fast action."
- "Reduces the target's armor by 2 per Power Level."
- "Forces an NPC to obey one command without a roll."

Bad:

- "The warrior channels ancestral fury."
  (What does it do mechanically?)
- "The spell creates a protective ward."
  (What dice, what duration, what cost?)

**Rule:** If you cannot summarize the mechanic
in one sentence, it is doing too much.
Split it into two abilities or simplify.

---

## Step 3 — Mechanism Tagging

Match the summary against this table.
Assign every tag that applies. A rule can have multiple tags.

### Mechanism Tag Table

| Tag | Applies When | Primary Danger Zone |
| --- | --- | --- |
| **WP-GRANT** | Gives WP to characters | WP Economy, Kin+Spell |
| **WP-REFUND** | Returns WP already spent | WP Economy |
| **WP-MULTIPLY** | Multiplies effect of WP spent | WP Economy, Superbuilds |
| **ACTION-GRANT** | Gives an extra action | Action Compression |
| **ACTION-FREE** | Makes something cost no action | Action Compression |
| **ARMOR-IGNORE** | Attacks bypass or reduce armor | Armor Bypass |
| **ARMOR-REDUCE** | Temporarily or permanently lowers AR | Armor Bypass |
| **ARMOR-STACK** | Adds armor from a new source | Defense Stacking |
| **CRITICAL-FORCE** | Guarantees critical injury | Armor Bypass |
| **HEAL-ATTRIB** | Restores attribute points | Recovery Collapse |
| **HEAL-CRITICAL** | Removes critical injuries | Recovery Collapse |
| **HEAL-PERSIST** | Heals over time without caster action | Recovery Collapse |
| **DODGE-BONUS** | Adds dice or free uses to Dodge | Defense Stacking |
| **DAMAGE-REDUCE** | Reduces incoming damage by N | Defense Stacking |
| **INVULN** | Immunity to a damage type or attack | Defense Stacking |
| **MISHAP-REDUCE** | Reduces or removes mishap dice | Safe Casting |
| **RANK-REDUCE** | Lowers effective spell rank | Safe Casting |
| **DURATION-EXTEND** | Extends effect duration | Temporal, Spell Amplifiers |
| **PERSIST-ZONE** | Creates a persistent area effect | Spell Amplifiers |
| **TARGET-MULTI** | Affects multiple targets | Party Exploits, Social |
| **COMPLIANCE-FORCE** | NPC obeys without Manipulation roll | Social Domination |
| **MIND-CONTROL** | Controls or rewrites NPC behavior | Social Domination |
| **DEATH-BYPASS** | Prevents death or provides backup body | Death Bypass |
| **REROLL-ANY** | Rerolls any die roll | Spell Stacking |
| **DARKNESS-GRANT** | Creates or extends magical darkness | Kin+Spell |
| **TRAVEL-BYPASS** | Negates travel hazards or costs | Travel Pressure |
| **TRAIN-TIME** | Skips time-gated advancement | Temporal Exploits |
| **BODY-ALTER** | Transforms into another creature | Spell-Path Internal |
| **TALENT-GRANT** | Gives another character a talent | Party Exploits |
| **BIND-ELIGIBLE** | Can be bound to an item via Bind Magic | Bind Magic |
| **INITIATIVE-MOD** | Modifies initiative order or actions | Initiative Exploitation |
| **STEALTH-LOOP** | Maintains stealth after attacking | Assassination Loops |
| **MOUNT-ACTION** | Grants mount independent actions | Mounted Combat |
| **FEAR-IMMUNE** | Grants fear immunity or reduction | Condition Manipulation |
| **CONDITION-IMMUNE** | Grants immunity to a game condition | Condition Manipulation |
| **ECONOMY-BYPASS** | Creates wealth or goods without cost | Crafting and Economy |
| **GRAPPLE-ENHANCE** | Improves grapple attack or effects | Grapple Exploitation |

**Rule:** If zero tags apply, the rule is probably safe.
Proceed to Step 6 (Red Flags) as a final check.
If 3+ tags apply, the rule is high-risk —
proceed directly to full five-test analysis (Step 7).

---

## Step 4 — Danger Zone Cross-Reference

For each tag that fired, check these specific danger zones.
Each zone lists what the catalog has already proven dangerous.

### WP Economy

**Known Restructure verdicts:**

- Psychic Power multiplies all WP (universal amplifier)
- Blood Channeling generates WP that feeds itself
- Safe-cast Blood Tap converts Strength to PL at zero risk

**Escalation triggers for new content:**

- Grants >1 WP/round passively
- Interacts with Psychic Power (Half-Elf auto-amplifies)
- Allows WP above Empathy to persist between scenes
- Refunds WP on a condition the character already achieves

### Action Compression

**Known Cap verdicts:**

- Lightning Fast R5 + Commander = party acts before
  enemies exist
- Time Stop + prepared spells = unlimited alpha strike

**Escalation triggers:**

- Grants free action with no per-round limit
- Converts slow action to fast unconditionally
- Grants extra actions inside Time Stop
- Grants ally actions without WP cost

### Armor Bypass

**Known Cap verdicts:**

- Arrow R5 forced critical + Arrow R1 armor ignore
- Bane R5 strips all defenses + bypass talent = zero AR

**Escalation triggers:**

- Stacks armor bypass with an existing bypass source
- Forces critical + existing attack already ignores armor
- Removes armor permanently (not per-attack)

### Defense Stacking

**Known Restructure verdicts:**

- Elemental Ward damage halving + Stoneskin + worn armor
  = triple reduction gate
- Stoneskin + Bark Skin + chain = AR 15+

**Escalation triggers:**

- Adds armor from a spell source (stacking question)
- Makes dodge unlimited AND adds artifact die
- Removes ranged attacks as a damage channel
- Grants damage-type immunity at low rank or cost

### Safe Casting

**Known Restructure verdicts:**

- Grimoire + high rank = zero dice = no mishap
- Stabilize + Grimoire + path rank = extends zero-dice
  threshold to dangerous spells

**Escalation triggers:**

- Reduces spell rank by any amount (stacks with Grimoire)
- Reduces mishap severity instead of count
- Allows casting without rolling for any spell
- Creates a second Grimoire-equivalent item or ability

### Recovery Collapse

**Known Restructure verdicts:**

- Living Spell + Healing Trance = zone heals without
  caster action
- Prepare Magic + healing = fast-action hospital

**Escalation triggers:**

- Healing triggers without caster action (passive zone)
- Healing has no per-QD limit
- Critical injury removal without ritual or ingredients
- Restores both attributes AND WP simultaneously

### Bind Magic

**Known Cap verdicts:**

- Bind Arsenal: 5-6 daily buffs from items = superhero
- Bind Firewalker: 1 WP/day = permanent fire immunity
- Bind Attribute Buffs: 4 WP = +4 to all attributes daily

**Escalation triggers:**

- New buff spell is bindable at PL 1 for low WP cost
- Bound effect grants immunity to a damage type
- Bound effect stacks with cast version of same spell
- No stated limit on simultaneous bound items

### Initiative Exploitation

**Known Cap verdicts:**

- Lightning Fast R5 + Commander R3 = party blitz
- Surprise + Commander = 2-3 actions before victims act

**Escalation triggers:**

- Grants bonus actions on winning initiative
- Grants ally-affecting abilities during bonus turn
- Stacks with surprise rules (+3 dice to all initiative)

### Assassination and Stealth

**Known Restructure verdicts:**

- Stalker R5 + Backstabber R3 + Killer R3 =
  hidden, auto-Break, armor-ignore, repeat

**Escalation triggers:**

- Maintains stealth after attacking without a new roll
- Combines armor bypass with stealth-attack bonus
- Has no per-round limit on stealth attacks

### Social Domination

**Known Cap verdicts:**

- Words R4 prevents INSIGHT = no social counterplay
- God Spell + Mass Serenity = 25-person mind control

**Escalation triggers:**

- Removes Manipulation roll entirely
- Extends forced-compliance duration
- Adds to Manipulation unconditionally
- Works on monsters or demons (existing rules restrict)

### Mounted Combat

**Known Clarify verdicts:**

- Horseback R4 + Melee Charge R4: do both triggers stack?
- Heavy Cavalry R5 + mount attributes: text ambiguity

**Escalation triggers:**

- Grants mount independent attacks with no WP cost
- Allows rider to act while mount also acts
- Uses mount attributes to pay rider ability costs

### God Spell Amplification

**Known Restructure verdicts:**

- God Spell + Living Spell = year-long stronghold buff
- God Spell + Restore Life = mass resurrection

**Escalation triggers:**

- New spell becomes campaign-breaking at 3x PL
- New spell affects settlement at 5x targets
- Interacts with Living Spell for persistent God-level zone

### Condition and Death Immunity

**Known verdicts:**

- Lucky R5 + Physician R5 = cannot die (Monitor)
- Pain Resistant R5 + Unbreakable = double Broken
  recovery (Clarify)

**Escalation triggers:**

- Prevents death without once-per-session limit
- Converts death into power without permanent cost
- Stacks with existing condition immunity
- Grants multiple types of immunity from one source

---

## Step 5 — Overlap Questions

For each matched Danger Zone, answer three questions:

### Question A — Does it make an existing danger cheaper?

Lower WP cost, fewer decisions, shorter setup,
no longer requires specific kin or profession.

**Example:** A new talent that grants a free dodge
per round makes Rat's Reflexes cheaper to replicate.

### Question B — Does it increase existing danger output?

Higher Power Level, more targets, longer duration,
additional damage, wider area.

**Example:** A new spell that triples buff duration
makes Hold Magic + Invigorate much stronger.

### Question C — Does it remove an existing brake?

Eliminates a cooldown, bypasses a per-QD limit,
removes a monster immunity clause, negates a
concentration requirement.

**Example:** A new item that maintains concentration
for free removes Hold Magic's action lock.

**Decision rule:**

- 0 yes answers → proceed to Step 6
- 1 yes answer, matched zone is Monitor/Clean → **Cap**
- 1 yes answer, matched zone is Cap/Restructure → **Restructure**
- 2+ yes answers → **Reject or Separate**

---

## Step 6 — Red Flag Keyword Scan

Scan the rule text for these phrases.
Each hit warrants a second look.
Two or more in the same rule → full five-test analysis.

| Keyword | Why It Is Dangerous |
| --- | --- |
| "free action" | Additive; two = extra fast action |
| "any die roll" | Universal reroll removes randomness |
| "without rolling" | Removes failure-chance cost |
| "no mishap" | Safe casting already exists; stacks |
| "gain WP" | Cross with Psychic Power and WP loops |
| "ignore armor" | Cross with existing armor bypass |
| "per Power Level" | Psychic Power amplifies per-PL scaling |
| "zone" / "area" | Cross with Living Spell, Stabilize |
| "persistent" / "lasts until" | Duration without decay needs cost |
| "does not count as an action" | Equivalent to granting a free action |
| "regardless of armor" | Stacks with existing bypass effects |
| "automatically succeed" | Check what auto-succeed already covers |
| "cannot be targeted" | Full channel immunity needs scrutiny |
| "may be recast" | Renewable insurance, dominance |
| "while unconscious" / "after death" | Death-bypass territory |
| "transfer to another body" | Clone + Body Swap territory |
| "stack with" | Designer was aware of an interaction |
| "in addition to" | Additive, not replacing |
| "all allies" / "all enemies" | Party-wide effects multiply value |
| "bound to item" / "bind" | Cross with Bind Magic Arsenal |
| "daily" / "at dawn" | Renewable with no limiting cost |
| "hidden" / "remain hidden" | Cross with stealth assassination loops |
| "immunity" | Full immunity to any channel is suspect |
| "PL 1" + "immunity" | Low-rank immunity safe-casts trivially |

---

## Step 7 — Full Five-Test Analysis

Apply these five tests to any rule that reached
this step. If a rule fails even one test, it
needs correction.

### Test 1 — Decision Cost

How many meaningful decisions does the player
make to activate this rule in play?

| Decisions | Risk Level | Guidance |
| --- | --- | --- |
| 0 (passive) | Critical | Must have hard per-QD limit |
| 1 (build choice) | High | Must have per-use WP cost |
| 2-3 (build + play) | Moderate | Standard design |
| 4+ (per-use setup) | Low | Sweet spot |

### Test 2 — Risk Exposure

What does the player risk when they use this rule?

- **Healthy:** WP drain, pushing banes, mishap, position
- **Unhealthy:** Nothing. The cost refunds or the risk
  is zero.

Trace the WP flow. If WP spent comes back through
the same loop, the risk is cosmetic.

### Test 3 — Opportunity Cost

What does the player give up to get this rule?

- **Healthy:** Other strong talents, spell paths, gear
- **Unhealthy:** Nothing important. Build still covers
  other niches.

Check whether the combo leaves adjacent specializations
intact. If it does everything, it costs too little.

### Test 4 — Repeatability

How often can the rule fire?

| Frequency | Expected Power |
| --- | --- |
| Once/campaign | Can be very strong |
| Once/session | Can be strong |
| Once/encounter | Should be moderate |
| Once/QD | Should be moderate |
| Per round | Must be weak per use |
| Per attack | Must be minimal per use |

Multiply per-use power by expected frequency.
A moderate effect every round is stronger than
a devastating effect once per session.

### Test 5 — Campaign Erosion

Does the rule hollow out a pressure channel?

Name the channel (from Step 1's table).
If the rule deletes the channel rather than
temporarily relieving it, the campaign flattens.

**Scoring:**

| Result | Verdict |
| --- | --- |
| Passes all 5 | **Safe** |
| Fails 1, minor | **Flag for record** |
| Fails 1, moderate | **Cap** — add limit |
| Fails 2 | **Restructure** — redesign |
| Fails 3+ | **Reject** — do not add |

---

## Step 7B — Fix Templates

When a rule needs correction, use these proven fixes
drawn from the catalog's 151 worked examples.

### Fix: Add per-round limit

> "This ability may be used once per round."

Fixes: unlimited dodge, unlimited free action,
unlimited bash, unlimited Commander grants.

### Fix: Add per-QD limit

> "This ability may be used once per Quarter Day."

Fixes: renewable immunity, daily attribute buffs,
repeated stealth assassination loops.

### Fix: Cap WP per activation

> "You may spend a maximum of [N] WP on this ability."

Fixes: Psychic Power multiplication, Heavy Cavalry
unlimited success elimination, Commander mass grants.

### Fix: Make cost non-refundable

> "WP spent on this ability cannot be recovered
> by any means until the next Quarter Day."

Fixes: WP refund loops, circular WP generation,
fight-grants-WP-that-fights patterns.

### Fix: Require re-rolling after trigger

> "After using this ability, you must succeed on
> a [SKILL] roll to maintain the effect."

Fixes: permanent stealth after attack, indefinite
zone without concentration, fire-and-forget buffs.

### Fix: Exclude from stacking

> "This effect replaces (does not stack with)
> other sources of [armor/damage reduction/bonus]."

Fixes: triple armor gate, double artifact die on dodge,
multiple bound buffs, spell armor + worn armor.

### Fix: Restrict Bind Magic eligibility

> "This spell cannot be bound to an item using
> Bind Magic."

Fixes: bound immunity at PL 1, bound attribute
buffs, bound daily healing, Bind Arsenal.

### Fix: Restrict God Spell eligibility

> "God Spell cannot be applied to this spell."

Fixes: year-long Living Spell zones, mass
resurrection, 25-target mind control.

### Fix: Lock to specific scope

> "This bonus applies only to [named spell school /
> named talent path / named action type]."

Fixes: universal amplifiers (Psychic Power, Fate
Weaving), "any die roll" rerolls.

### Fix: Escalating cost for repeat use

> "Each additional use in the same [round/encounter/QD]
> costs [N] more WP than the previous."

Fixes: Arrow R5 multi-critical, fast-action stab spam,
Commander grant stacking.

### Fix: Require awareness or resistance roll

> "The target may resist with [INSIGHT/ENDURANCE].
> On success, the effect fails."

Fixes: WP theft via Transfer, auto-compliance
(Serenity), forced emotional states.

---

## The Five Patterns Behind All Unhealthy Synergies

Every Restructure verdict in 151 catalog entries
traces back to one or more of these abstract patterns.
If your new rule matches any pattern, redesign.

### Pattern A — The Free Refund

_Spend X to get X back under condition Y,
where Y is something the character already achieves._

- **Recognition:** Cost and trigger are the same activity.
  Fighting grants WP from fighting.
- **Fix:** Condition Y must be rare (not guaranteed/round)
  or refund must be partial (half, not full).

### Pattern B — The Unscoped Amplifier

_Multiply the effect of all WP (or all rolls,
or all spells) regardless of source._

- **Recognition:** The word "any" in the description.
- **Fix:** Named scope. "Blood Magic only" not "any spell."

### Pattern C — The Risk Bypass

_Remove the cost that makes the ability fair._

- **Recognition:** "Without X" where X is the original
  balancing cost (mishap, WP, action, time, injury).
- **Fix:** Reduce risk partially. "Reduce mishap by 1"
  not "cast without rolling."

### Pattern D — The Self-Maintaining Zone

_One-time cast creates a permanent effect
that operates without caster action._

- **Recognition:** After setup, the zone runs itself.
- **Fix:** Require ongoing maintenance (WP/round,
  concentration, or re-casting).

### Pattern E — The One-Decision Build

_One creation choice multiplies every subsequent
advancement decision._

- **Recognition:** "All," "any," "every time," "whenever"
  without a named scope.
- **Fix:** Multiplier applies to one named category,
  not all abilities.

### Pattern F — The Invisible Attacker

_Attack from a state where the target cannot retaliate,
with no cost to maintain that state._

- **Recognition:** Hidden + attack + stay hidden,
  or out-of-range + attack + enemy cannot close.
- **Fix:** Require a new stealth or positioning roll
  after each attack. Or give targets a reactive
  detection attempt.

### Pattern G — The Stacking Gate

_Multiple sequential damage reduction layers where
each layer has its own separate roll._

- **Recognition:** Spell armor + physical armor + Ward +
  immunity. Three gates that each must be beaten.
- **Fix:** Spell armor replaces (not stacks with)
  physical armor. Choose the higher value.

---

## The Verdict Matrix

After completing the tree, deliver one of these verdicts.

| Situation | Verdict | Action |
| --- | --- | --- |
| No tags. No red flags. Passes 5 tests. | **Safe** | Add to manuscript |
| Tags fire but no overlap. Passes tests. | **Flag** | Add to manuscript. Log in catalog as Monitor |
| 1 overlap yes. Matched zone is Monitor. | **Cap** | Apply one Fix Template. Re-run Step 5 |
| 1 overlap yes. Matched zone is Cap+. | **Restructure** | Redesign mechanism. Re-run from Step 2 |
| 2+ overlaps or fails 3+ tests. | **Reject** | Send back with specific diagnosis |

---

## Verdict Report Format

When delivering a verdict, use this structure:

```text
## Rule: [Name]

**Summary:** [One-sentence mechanism from Step 2]

**Tags:** [List of mechanism tags from Step 3]

**Danger Zones Hit:** [List from Step 4, or "None"]

**Overlap Questions:**
- Cheaper: [Yes/No — explain]
- Stronger: [Yes/No — explain]
- Brake removed: [Yes/No — explain]

**Red Flags:** [Keywords found, or "None"]

**Five-Test Results:**
- Decision Cost: [0-5 decisions] — [Pass/Fail]
- Risk Exposure: [description] — [Pass/Fail]
- Opportunity Cost: [description] — [Pass/Fail]
- Repeatability: [frequency] — [Pass/Fail]
- Campaign Erosion: [channel affected] — [Pass/Fail]

**Pattern Match:** [A-G or "None"]

**Verdict:** [Safe / Flag / Cap / Restructure / Reject]

**Recommended Fix:** [Specific fix template, or "None needed"]

**Catalog Entry:** [If Cap+ — write the catalog entry
for exploitation-surface-catalog.md]
```

---

## Quick-Reference Design Guardrails

These are the hard limits derived from 151 catalog
entries. Any new rule that violates a guardrail must
justify the violation or be redesigned.

### WP Guardrails

- No passive ability should grant >1 WP per round
- No ability should multiply WP spent universally
- WP refund loops (spend X, trigger returns X) are
  banned unless the trigger is rare and not combat-linked
- Half-Elf Psychic Power interacts with everything —
  always check new WP costs against it

### Action Economy Guardrails

- Free actions: maximum 1 per round per character
  unless explicitly gated by WP
- Slow-to-fast conversion: requires WP cost per use
- Commander grants: 1 grant per ally per round,
  regardless of number of Commanders
- Lightning Fast bonus actions: cannot include
  Commander or other ally-affecting grants

### Defense Guardrails

- Spell armor replaces worn armor (higher value wins);
  does not stack
- Maximum 2 simultaneous bound buffs per character
- Damage-type immunity requires PL 3+ and is
  not safe-castable at zero dice
- Unlimited dodges per round: must still consume
  action economy (not truly free)

### Safe Casting Guardrails

- Zero-dice casting should carry a flat 1-in-6
  mishap chance (recommendation)
- Grimoire reduces rank for mishap only, not for
  safe-cast threshold (recommendation)
- No second Grimoire-equivalent should exist
- Stabilize + Grimoire should not stack
  (only the better reduction applies)

### Assassination Guardrails

- Stealth after attack: always requires a new
  opposed STEALTH vs SCOUTING roll
- Armor bypass + stealth bonus: choose one per attack,
  not both
- Auto-Break + armor ignore + repeat from stealth:
  if all three combine, Restructure

### Social Guardrails

- Forced compliance (no Manipulation roll): target
  always gets a resistance roll (INSIGHT/ENDURANCE)
- Permanent behavior modification: target gets daily
  resistance roll with cumulative +1
- Party-wide social buffs: cap at +2 total from
  all talent sources combined

### Bind Magic Guardrails

- Maximum 2 active bound buffs per character
- Immunity effects cannot be bound below PL 3
- Bound effect does not stack with cast version
  (take the higher)
- Attribute buff bound items cap at PL 1 (+1 only)

### Mounted Combat Guardrails

- Mount acts independently only if rider spends WP
- Rider cannot use Commander grants while mount
  also acts independently in the same round
- Mount attribute substitution applies only to the path
  that grants it (not all abilities)

### Ranged DPS Guardrails

- Forced critical (Arrow R5): maximum once per round
  regardless of number of shots
- Multi-shot rounds: maximum 3 ranged attacks per round
  from any combination of talents and spells
- Extended range shots: target always gets +2 to defense

---

## Cross-Rule Interaction Log

Record combinations found during intake reviews.
This becomes the running audit trail.

Format per entry:

```text
**[New Rule Name]** × **[Existing Rule Name]**
Tag(s): [mechanism tags that fired]
Overlap: [which question said yes, or "none"]
Verdict: [Safe / Flag / Cap / Restructure / Reject]
Resolution: [rule text change, or "none needed"]
```

### Recorded Entries

_Populate as new content is screened._
