---
name: forbidden-lands-synergy-analysis
description: Use when auditing talent combinations, spell stacking, kin+profession builds, or any multi-rule interaction in Forbidden Lands 2E for balance-breaking potential. Triggers on questions like "is this combo broken", "what are the strongest builds", "does this talent stack with that spell", "can players exploit this", or any request to stress-test a rule interaction. Also use when designing new talents or spells that might create unintended synergy with existing content. This skill distinguishes between creative high-risk play (healthy) and one-decision dominant lines (unhealthy).
---

# Forbidden Lands Synergy Analysis

The Forbidden Lands engine encourages players to combine talents, spells, kin abilities, gear, and conditions in creative ways that tip dangerous situations in their favor. That is the game working as intended. The problem this skill exists to catch is different: combinations that require only a single obvious character-creation or advancement decision, carry no meaningful risk or tradeoff, and then quietly dominate the game from that point forward.

## When To Use It

- Auditing a proposed talent or spell for unintended interactions with existing rules.
- Stress-testing a character build for dominant lines.
- Reviewing a new rule or subsystem for synergy risk before it enters the manuscript.
- Answering player or designer questions about whether a specific combo is broken.
- Scanning the talent and spell chapters for systemic exploitation surfaces.
- Screening new spells, talents, gear effects, or magic item properties against the known Danger Zones using the **New Content Screener** (see Bundled References).

For new content review specifically, always run the New Content Screener intake protocol before applying full five-test analysis. The screener narrows the search space in under five minutes.

## Source Of Truth

Always ground analysis in the actual manuscript:

- `corebook/04-talents.md` — all talent paths, kin talents, general talents
- `corebook/07-magic.md` — all spells, casting rules, mishap tables, spell design rules
- `corebook/05-combat-and-damage.md` — action economy, stunts, initiative, armor
- `corebook/02-your-adventurer.md` — kin choice, profession choice, starting conditions, WP rules
- `corebook/03-skills.md` — skill rolls, pushing, opposed rolls
- `corebook/10-gear.md` — weapon properties, armor, crafting, poisons

Read the relevant sections before making claims. Do not argue from memory alone.

## Bundled References

Read on demand:

- `skills/forbidden-lands-synergy-analysis/references/new-content-screener.md` — **start here for any new rule review.** Mechanism Tag Table, Danger Zone Index, Pattern Library, Red Flag Keywords, Cross-Rule Interaction Log.
- `skills/forbidden-lands-synergy-analysis/references/exploitation-surface-catalog.md` — 67 worked synergy examples with five-test results and verdicts. Organized by exploitation surface category.
- `skills/forbidden-lands-design/references/design-manual.md` — pressure economy, WP economy, synergy framework, expansion framework
- `skills/rpg-balance-analysis/references/action-economy-synergy-and-campaign-scale.md` — action economy value, game-theory taxonomy, campaign-scale tests

## The Core Distinction

Healthy synergy and unhealthy synergy look similar in output but differ in input cost.

### Healthy synergy

The combo requires:

- deliberate setup in play (positioning, timing, resource spend)
- risk exposure (pushing, WP drain, mishap chance, condition vulnerability)
- coordination between multiple players or multiple turns
- a tradeoff that closes off other options

The payoff is dramatic and memorable because the cost was visible.

### Unhealthy synergy

The combo requires:

- a single character-creation or advancement decision
- no ongoing risk, setup, or meaningful tradeoff
- no coordination — it works every time, automatically
- nothing stops a player from choosing it once they know about it

The payoff is routine and dominant because the cost was invisible or absent.

## The Five Tests

Apply these sequentially to any suspected synergy. If a combo fails even one test, it needs correction.

### 1. Decision Cost Test

How many meaningful decisions does the player need to make to activate this combo?

- **Healthy:** Multiple decisions across play — positioning, resource spend, timing, risk acceptance.
- **Unhealthy:** One decision at character creation or advancement. The combo activates automatically from that point.

Count the decisions. If the answer is one, the combo is suspect.

### 2. Risk Exposure Test

What does the player risk when they use this combo?

- **Healthy:** WP drain, pushing banes, mishap exposure, condition vulnerability, positional danger.
- **Unhealthy:** Nothing meaningful. The combo either avoids all risk channels or refunds its own cost.

Trace the WP flow. If WP spent comes back through the same loop, the risk is cosmetic.

### 3. Opportunity Cost Test

What does the player give up by committing to this build?

- **Healthy:** Other strong talents, different kin abilities, alternative spell paths, gear flexibility.
- **Unhealthy:** Nothing important. The build still has access to most of what matters.

Check whether the combo leaves adjacent niches intact. If it also covers what other builds specialize in, it is too broad.

### 4. Repeatability Test

How often can the combo fire per session, per encounter, per Quarter Day?

- **Healthy:** Once or twice per encounter, with setup required each time.
- **Unhealthy:** Every round, automatically, with no cooldown or re-setup cost.

Multiply the per-use power by expected frequency. A moderate effect used every round is stronger than a devastating effect used once per session.

### 5. Campaign Erosion Test

Does the combo hollow out a pressure channel the campaign depends on?

- **Healthy:** The combo solves one problem well but leaves other pressures intact.
- **Unhealthy:** The combo removes an entire category of challenge — resource attrition, travel danger, injury fear, social opposition, action economy limits.

Name the pressure channel. If the combo deletes it rather than temporarily relieving it, the campaign will flatten.

## Exploitation Surface Categories

These are the structural areas where FL2E is most vulnerable to synergy abuse. Each one is detailed in the reference catalog.

1. **WP Economy Loops** — combinations that generate, refund, or multiply WP faster than the push-bane throttle intends.
2. **Action Compression Stacking** — talents or spells that grant extra actions, combined with effects that make those actions premium.
3. **Armor Bypass Chains** — stacking armor-ignore effects so that damage flows unimpeded every round.
4. **Recovery Collapse** — healing, attribute restoration, or condition removal that outpaces the attrition the campaign assumes.
5. **Defense Stacking** — layering dodge bonuses, damage reduction, and miss-forcing effects until the character is functionally invulnerable.
6. **Safe Casting Compression** — reducing spell risk (grimoire + safe casting + high rank) until magic becomes riskless universal problem-solving.
7. **Travel Pressure Bypass** — combining camp, shelter, food, and weather talents until the expedition loop stops mattering.
8. **Social Domination** — stacking manipulation bonuses, artifact dice, reputation leverage, and attitude-shifting effects until all NPC interactions collapse into auto-success.

## Analysis Method

For any suspected combo, follow this procedure:

### Step 1 — Identify the components

List every talent rank, spell, kin ability, gear property, and condition involved.

### Step 2 — Trace the interaction

Describe exactly how the pieces connect. Which rule feeds into which? What triggers what?

### Step 3 — Apply the five tests

Run the decision cost, risk exposure, opportunity cost, repeatability, and campaign erosion tests. Score each as healthy, borderline, or unhealthy.

### Step 4 — Check the pressure stack

Using the design manual's pressure economy framework, name which pressure channels the combo relieves and which it leaves intact.

### Step 5 — Compare to baselines

What does a character without this combo look like in the same situation? If the gap is enormous with no corresponding cost, the combo is dominant.

### Step 6 — Recommend

One of:

- **Clean** — the combo is strong but earned. No action needed.
- **Monitor** — the combo is borderline. Flag for GM awareness but do not change rules.
- **Cap** — add a frequency limit, WP ceiling, or cooldown to one component.
- **Restructure** — one component needs a redesign to close the loop.
- **Separate** — the components should not be available to the same character without a significant gate.

## Output Format

When reporting a synergy analysis, use this structure:

```
## [Combo Name]

**Components:** [list of talents, spells, kin, gear involved]
**Build cost:** [what character creation and advancement decisions are required]
**Activation cost:** [what the player spends each time they use it in play]

### How it works
[Describe the interaction chain]

### Five-test results
| Test | Result | Reasoning |
|------|--------|-----------|
| Decision cost | Healthy/Borderline/Unhealthy | ... |
| Risk exposure | ... | ... |
| Opportunity cost | ... | ... |
| Repeatability | ... | ... |
| Campaign erosion | ... | ... |

### Pressure channels affected
[Which pressures does this relieve or delete?]

### Baseline comparison
[What does the same situation look like without this combo?]

### Verdict
[Clean / Monitor / Cap / Restructure / Separate]

### Recommended correction
[If needed, what specific change fixes it?]
```

## What This Skill Does Not Do

- It does not replace the `forbidden-lands-design` skill for general rules design.
- It does not replace the `rpg-balance-analysis` skill for broad balance evaluation.
- It focuses specifically on multi-rule interactions and their exploitation potential.
- It assumes the individual rules are already well-designed; it tests what happens when they meet.
