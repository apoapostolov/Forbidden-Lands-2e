<!-- markdownlint-disable MD013 -->

# New Content Screener

## Purpose

This document is the intake protocol for evaluating new rules — spells, talents, kin abilities, gear properties, and magic item effects — before they enter the manuscript. It answers the question: _does this new thing plug into an existing dangerous synergy, duplicate a known broken pattern, or open a new one?_

It is designed to be fast. An AI or designer should be able to screen a new rule in under five minutes using the Mechanism Tag Table, then escalate to full five-test analysis only if a tag fires.

---

## Intake Protocol (Run This First)

For every new rule being evaluated, work through these five steps in order.

### Step 1 — Summarize the Mechanism

Write one sentence describing what the rule **does mechanically**, not what it is thematically. Strip the flavour.

Examples:

- "Grants WP when the caster takes damage."
- "Reduces the target's effective armor by 2."
- "Allows an additional attack as a fast action."
- "Forces an NPC to comply with the caster's stated demand."

If you cannot summarize it in one sentence, the rule is doing too much — flag that before continuing.

### Step 2 — Tag It

Match the summary against the **Mechanism Tag Table** below. Assign every tag that applies. A rule can have multiple tags.

### Step 3 — Look Up Each Tag

Each tag maps to one or more **Danger Zones** in the catalog. Read the listed entries.

### Step 4 — Ask the Overlap Questions

For each matched Danger Zone, answer the three overlap questions:

1. **Does the new rule make an existing Danger Zone entry cheaper to activate?**
   (Lower WP cost, fewer decisions, shorter setup, no longer requires specific kin/path.)
2. **Does the new rule increase the output of an existing Danger Zone entry?**
   (Higher Power Level, more targets, longer duration, additional damage, wider area.)
3. **Does the new rule remove an existing brake on a Danger Zone entry?**
   (Eliminates a cooldown, bypasses a per-QD limit, removes a monster immunity clause, negates a concentration requirement.)

If any answer is yes, escalate to full five-test analysis.

### Step 5 — Check New Pattern Risk

Even if no existing Danger Zone fires, ask: does this rule **combine with anything** in the manuscript to create a new loop the catalog has not mapped? Quick-test:

- Does this rule grant a resource (WP, actions, healing, dice)?
  → Does anything existing **amplify** that resource?
- Does this rule remove a cost or risk?
  → Does anything existing **stack** with that removal?
- Does this rule affect multiple targets or persist over time?
  → Does anything existing **compound** persistence or multi-targeting?

If yes to any: add the new combo to the exploitation-surface-catalog.md before finalizing the rule.

---

## Mechanism Tag Table

| Tag                  | Applies When                                                                   | Primary Danger Zones                           | Secondary Risk                                                         |
| -------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------- | ---------------------------------------------------------------------- |
| **WP-GRANT**         | Rule gives WP to one or more characters                                        | WP Economy Loops, Kin+Spell Interactions       | Cross with any WP-multiplying effect                                   |
| **WP-REFUND**        | Rule returns WP already spent                                                  | WP Economy Loops                               | Any per-use cost becomes free                                          |
| **WP-MULTIPLY**      | Rule multiplies the effect of WP spent                                         | WP Economy Loops, Cross-Category Superbuilds   | Touches every path simultaneously                                      |
| **ACTION-GRANT**     | Rule grants an extra action (fast, slow, or free)                              | Action Compression Stacking, Temporal Exploits | Cross with high-damage or high-effect abilities                        |
| **ACTION-FREE**      | Rule allows an action that normally costs speed as a free action               | Action Compression Stacking                    | Cross with armor bypass, forced criticals                              |
| **ARMOR-IGNORE**     | Rule causes attacks to ignore or reduce armor                                  | Armor Bypass Chains                            | Cross with any forced-critical effect                                  |
| **ARMOR-REDUCE**     | Rule reduces armor rating temporarily or permanently                           | Armor Bypass Chains                            | Cross with high-damage weapons                                         |
| **CRITICAL-FORCE**   | Rule causes or guarantees a critical injury independent of the attack roll     | Armor Bypass Chains                            | Cross with Executioner talent                                          |
| **HEAL-ATTRIB**      | Rule restores one or more attribute points                                     | Recovery Collapse                              | Cross with Living Spell, Prepare Magic                                 |
| **HEAL-CRITICAL**    | Rule removes or reverses a critical injury                                     | Recovery Collapse                              | Cross with Inner Peace, Regeneration                                   |
| **HEAL-PERSIST**     | Rule heals over time or without caster action                                  | Recovery Collapse                              | Cross with safe casting, Living Spell                                  |
| **DODGE-BONUS**      | Rule adds dice, automatic successes, or free uses to Dodge                     | Defense Stacking                               | Cross with Rat's Reflexes, Hard to Catch                               |
| **DAMAGE-REDUCE**    | Rule reduces incoming damage                                                   | Defense Stacking                               | Cross with Elemental Shield, Path of Fate                              |
| **INVULN-PHYSICAL**  | Rule makes character immune or near-immune to physical damage                  | Defense Stacking                               | Requires GM-only enemy countermeasures                                 |
| **MISHAP-REMOVE**    | Rule reduces or eliminates mishap dice when casting                            | Safe Casting Compression                       | Cross with grimoire, high talent rank                                  |
| **MISHAP-NEGATE**    | Rule negates mishap effects after they occur                                   | Safe Casting Compression                       | Allows unlimited safe high-rank casting                                |
| **RANK-REDUCE**      | Rule reduces effective spell rank for casting purposes                         | Safe Casting Compression                       | Stacks with grimoire for zero-dice casts                               |
| **DURATION-EXTEND**  | Rule extends the duration of another effect                                    | Temporal Exploits, General Spell Amplifiers    | Cross with any buff or persistent damage spell                         |
| **PERSIST-ZONE**     | Rule creates a persistent zone effect                                          | General Spell Amplifiers                       | Cross with any healing, damage, or buff spell                          |
| **TARGET-MULTI**     | Rule allows one spell or ability to affect multiple targets                    | Party Composition Exploits, Social Domination  | Cross with forced-compliance, forced-critical, or forced-Break effects |
| **COMPLIANCE-FORCE** | Rule causes NPCs to comply without a Manipulation roll                         | Social Domination, Spell-On-Spell Stacking     | Cross with Mass Spell, Path of Influence                               |
| **MIND-CONTROL**     | Rule controls or rewrites NPC/character behavior                               | Social Domination, Spell-On-Spell Stacking     | Duration + permanence are the key risks                                |
| **DEATH-BYPASS**     | Rule prevents death, converts death to an advantage, or provides a backup body | Spell-Path Internal Synergies                  | Cross with any self-destruct or martyr strategy                        |
| **REROLL-ANY**       | Rule allows rerolling any die roll (including dice the character did not roll) | Spell-On-Spell Stacking                        | The most universally powerful mechanism                                |
| **DARKNESS-GRANT**   | Rule creates or extends magical darkness                                       | Kin+Spell Interactions                         | Cross with Goblin Nocturnal                                            |
| **TRAVEL-BYPASS**    | Rule negates travel hazards, camp needs, or food/water costs                   | Travel Pressure Bypass                         | Cross with Nature, Forest, Swarm paths                                 |
| **TRAIN-TIME**       | Rule accelerates or skips time-gated advancement                               | Temporal and Dream Exploits                    | Cross with Dream Palace                                                |
| **BODY-ALTER**       | Rule transforms the caster into another creature or body                       | Spell-Path Internal Synergies                  | Cross with Primal Strength, Body Swap                                  |
| **TALENT-GRANT**     | Rule gives another character use of a talent they do not have                  | Party Composition Exploits                     | Cross with any Restructure-verdict talent                              |
| **INGREDIENT-SKIP**  | Rule allows bypassing ritual ingredient requirements                           | Safe Casting Compression, Epic Magic           | Removes cost gating from expensive rituals                             |
| **PREPARE-HOLD**     | Rule allows pre-loading spells or effects for later instant discharge          | General Spell Amplifiers                       | Cross with safe casting, Time Stop                                     |
| **FEAR-IMMUNE**      | Rule grants immunity to or reduction of fear attacks                           | Condition and Tempo Manipulation               | Watch for stack count; three sources covers party                      |
| **CONDITION-IMMUNE** | Rule grants immunity to a game condition (Broken, bleeding, stunned, etc.)     | Condition and Tempo Manipulation               | Cross with Berserker, rampage mechanics                                |

---

## Danger Zone Quick-Reference Index

Use this when a tag fires. Each Danger Zone lists the existing catalog entries most likely to be affected by new content that shares the mechanism.

### WP Economy Loops

**Existing Restructure/Cap entries:** Half-Elf Psychic Power + Any WP-Hungry Path, Psychic Power + Blood Channeling, Blood Channeling + Time Stop, Mountains' Blessing (Stone Song), Absorb Magical Residue + ambient magic.

**What to watch for in new content:**

- Any "gain WP when X" where X is a common in-play event (taking damage, hitting an enemy, entering a zone).
- Any "multiply WP effect" regardless of mechanism.
- Any temporary WP that does not expire at end of round.
- WP costs that refund on success — these feel fair but function as net-zero costs.

**New content auto-escalation triggers:**

- The new rule grants more than 1 WP per round as a passive effect.
- The new rule interacts with Psychic Power (any Half-Elf automatically amplifies it).
- The new rule allows WP above Empathy to persist between scenes.

---

### Action Compression Stacking

**Existing Cap/Monitor entries:** Blood Channeling + Time Stop, Path of Blade R2 + Enemy R4, Commander Rank 4, Time Stop + Prepared Spells.

**What to watch for:**

- "As a fast action instead of slow action" — this doubles action efficiency.
- "Free action once per round" — free actions are almost always undercosted.
- "Extra slow action" — any additional slow action doubles available spell output.
- Action grants that are not WP-gated (i.e., cost nothing to trigger).

**New content auto-escalation triggers:**

- The rule grants a free action with no per-round limit.
- The rule lets a slow-action ability become a fast action unconditionally.
- The rule grants additional actions during Time Stop (which already grants 1+PL extras).

---

### Armor Bypass Chains

**Existing Clean/Monitor/Cap entries:** Blade R1+R3, Killer R3, Arrow R1+R5 (Cap).

**What to watch for:**

- Any "ignore armor" or "target's armor does not apply."
- Any "reduce target armor by N permanently."
- Any "this attack always deals at least N damage regardless of armor."
- Critical injury effects that ignore the normal critical roll prerequisite.

**New content auto-escalation triggers:**

- The new rule stacks armor bypass with an existing bypass (two ignore-armor effects on one attack).
- The new rule forces a critical injury + an existing attack can already bypass armor.
- The new rule removes armor from a target permanently (cross-check with Bane, Death Magic R5).

---

### Recovery Collapse

**Existing Restructure entries:** Living Spell + Healing Trance, Living Spell + Invigorate, Prepare Magic + Healing Arsenal.

**Existing Monitor entries:** Elf Inner Peace + Druid Healing, Healing Trance Rank 4.

**What to watch for:**

- Any healing effect that triggers without caster action (passive healing).
- Any healing effect with no once-per-QD limit.
- Any critical injury removal that requires no ingredients or ritual.
- Any "fully restore attributes" effect that is repeatable within the same scene.

**New content auto-escalation triggers:**

- The new rule heals on trigger (entering a zone, completing an action, per round) with no caster cost.
- The new rule stacks with Living Spell (zone-wide application + persistence).
- The new rule removes a critical injury without a ritual or Quarter Day cost.
- The new rule restores both attributes and WP simultaneously.

---

### Defense Stacking

**Existing Cap/Monitor entries:** Rat's Reflexes + Hard to Catch (Cap), Halfling Hard to Catch + Path of Fate, Swarm Form.

**What to watch for:**

- "Dodge as a free action" — cross-check with Rat's Reflexes immediately.
- "Add [attribute] as automatic successes to Dodge" — cross-check with Hard to Catch.
- "Reduce incoming Strength damage by N" — cross with Elemental Shield, Path of Fate R2.
- "Take maximum 1 damage per attack" — Swarm Form territory.
- "Cannot be targeted by ranged attacks" — removes an entire damage channel.

**New content auto-escalation triggers:**

- The new rule adds another unlimited dodge per round (already have Rat's Reflexes at R5).
- The new rule stacks WP-as-successes with a dodge (Hard to Catch already does this).
- The new rule makes the character immune to one damage type (cross with Swarm Form immunity + elemental double-damage).

---

### Safe Casting Compression

**Existing Restructure entries:** Grimoire + Safe Casting + High Talent Rank, Half-Elf Sorcerer Superbuild, Grimoire + Prepare Magic.

**What to watch for:**

- Any rule that reduces effective spell rank for any purpose.
- Any rule that reduces the dice rolled before checking for mishaps.
- Any rule that redirects or negates mishap consequences.
- Any item that functions like a second grimoire (stacking -1 rank).

**New content auto-escalation triggers:**

- The new rule reduces spell rank by any amount — it stacks with grimoire.
- The new rule reduces mishap severity (mild mishap instead of severe) — this is equivalent to negating risk.
- The new rule allows casting without rolling at all, even for minor spells.
- The new rule allows reducing dice to zero — this is the core break point.

---

### Social Domination

**Existing Monitor entries:** Path of Influence + Face + Reputation, Mass Spell + Serenity, Geas + Serenity + Influence (Cap), Serenity + Path of Influence.

**What to watch for:**

- Any "target does X without a Manipulation roll" or "no resistance roll."
- Any "+N dice to Manipulation" that is passive, always-on.
- Any "affect multiple targets" with a social or domination spell.
- Permanent or indefinite NPC behavior modification.

**New content auto-escalation triggers:**

- The new rule removes the Manipulation roll entirely (Serenity already does this — a second source is a redundancy exploit).
- The new rule extends Serenity or Geas duration.
- The new rule adds dice to Manipulation unconditionally (cross with Influence R1 +2 dice + Face R4 D8 + Reputation bonus — it is already near auto-success).
- The new rule allows social control against monsters or demons (existing rules restrict this for good reason).

---

### General Spell Amplifiers

**Existing Restructure entries:** Living Spell + Healing Trance, Living Spell + Invigorate, Grimoire + Prepare Magic.

**What to watch for:**

- Any ability that converts a targeted spell into an area or zone effect.
- Any ability that extends a non-persistent spell into a persistent (days or weeks) effect.
- Any ability that reduces a ritual to a standard action.
- Any ability that allows holding pre-cast spells for instant discharge.

**New content auto-escalation triggers:**

- The rule applies to any non-ritual spell (Living Spell equivalent).
- The rule reduces casting time by more than one step (ritual → standard action, rather than ritual → fast action with a cost).
- The rule allows stacking multiple pre-cast spells (Prepare Magic already holds up to PL — a second source doubles the arsenal).

---

### Kin + Spell Interactions

**Existing Restructure entries:** Psychic Power + Blood Channeling, Psychic Power + Serenity.

**Existing Cap entries:** Goblin Nocturnal + Darkness.

**What to watch for:**

- New spells that multiply, amplify, or double-down on existing kin talent effects.
- New kin abilities that scale with spell Power Level (anything that reads "gain N per Power Level" is a Psychic Power proxy).
- New kin abilities that interact with darkness, hiding, or magical conditions that map to existing kin-specific bonuses.
- New spells that create conditions (darkness, intoxication, fear, specific terrain) that specific kin are already hard-coded to benefit from.

**New content auto-escalation triggers:**

- The new rule scales with Power Level and a Half-Elf can amplify Power Level via Psychic Power.
- The new spell creates a named condition an existing kin has a hardcoded bonus for.
- The new kin ability grants WP or multiplies WP — immediate cross-check with Psychic Power.

---

### Temporal and Dream Exploits

**Existing Cap/Monitor/Clarify entries:** Time Stop + Prepared Spells (Cap), Dream Palace + Training (Clarify), Sandman + Dream Palace (Cap), Future Dream (Monitor).

**What to watch for:**

- Any rule that "freezes time," "grants extra turns," or "takes no time in the fiction."
- Any dream or sleep state where in-dream activities produce real-world advancement.
- Any time-skip mechanic that bypasses the normal Quarter Day cost of activities.
- Any "undo" mechanic on actions or rolls.

**New content auto-escalation triggers:**

- The new rule grants slow actions (cross with Time Stop which already grants 1+PL).
- The new rule allows in-dream skill or talent advancement with no XP requirement.
- The new rule rewinds a failed action to before it was attempted (harder version of Fate Weaving).

---

### Death Bypass and Resurrection

**Existing Restructure entries:** Eternal Life + Clone.

**What to watch for:**

- Any "prevents death" effect without a clear once-per-campaign or once-per-session limit.
- Any "restore to life" effect that does not cost a significant permanent resource.
- Any backup-body or identity-transfer mechanic.
- Any effect that triggers on death and makes the character more powerful.

**New content auto-escalation triggers:**

- The new rule provides a death-prevention effect that can be recast between deaths (renewable insurance).
- The new rule converts death into power (lich form, berserker frenzy, etc.) without a corresponding permanent cost.
- The new rule allows consciousness transfer — stacks with Clone to provide multiple backup identities.

---

## The New-Rule Verdict Matrix

After running the intake protocol, determine which of these five situations applies.

| Situation                                                                                                           | Verdict                | Action                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------- |
| No tags fire. No new patterns detected.                                                                             | **Safe**               | Add to manuscript. No changes needed.                                                                     |
| Tags fire, but overlap questions all say no (cheaper/higher/brake-removed).                                         | **Flag for record**    | Add to catalog as a Monitor entry. Rule is fine as written. Keep this cross-reference for future reviews. |
| One overlap question is yes. Existing Danger Zone is Monitor or Clean.                                              | **Cap**                | Add a frequency limit, WP ceiling, or explicit exception clause to the new rule. Then re-run intake.      |
| One overlap question is yes. Existing Danger Zone verdict is Cap or Restructure.                                    | **Restructure**        | The new rule duplicates or amplifies a known problem. Redesign the mechanism before adding.               |
| Multiple overlap questions are yes, or a new pattern creates a zero-decision, zero-risk, per-round activation loop. | **Reject or Separate** | Send back to design with specific diagnosis. The rule should not enter the manuscript in current form.    |

---

## Pattern Library

These are the five abstract patterns that underlie all unhealthy synergies in the catalog. Every Restructure verdict in the catalog traces back to one or more of these.

### Pattern A: The Free Refund

**Template:** _Spend X to get X back under condition Y, where Y is something the character already achieves routinely._

**Examples:** Fencer WP recovery per kill (kill is expected each round), Blood Channeling granting WP usable next round, Adrenaline Rush R5 WP on Break.

**Recognition cue:** The cost and the trigger are in the same activity. Fighting grants WP from fighting.

**Safe version:** Condition Y should be rare (not guaranteed each turn) or the refund should be partial (recover half, not all).

---

### Pattern B: The Amplifier With No Target Scope

**Template:** _Multiply the effect of all WP spent, regardless of which talent or spell receives it._

**Examples:** Psychic Power (multiplies every WP spend), Fate Weaving (rerolls any die).

**Recognition cue:** The word "any" in the rule description. Universal amplifiers have no natural scope limit.

**Safe version:** Amplifiers should name a specific talent, spell school, or action type. "Multiply WP spent on Blood Magic" is healthy. "Multiply WP spent on anything" is not.

---

### Pattern C: The Risk Bypass

**Template:** _Remove the cost or danger that makes the underlying ability appropriately costed._

**Examples:** Safe casting at zero dice removes the entire mishap structure. Eternal Life removes death as a consequence. Rat's Reflexes removes the "one dodge per round as an action" constraint.

**Recognition cue:** The rule says "without X" where X is the cost the original ability was balanced around.

**Safe version:** Risk reduction should be partial, not total. "Reduce mishap dice by 1" is different from "cast without rolling."

---

### Pattern D: The Persistent Zone That Self-Maintains

**Template:** _Convert a one-time effect into a permanent zone that activates without caster action._

**Examples:** Living Spell + Healing Trance (zone heals everyone without caster), Stabilize Magic Zone + Cloud of Death (persistent kill corridor).

**Recognition cue:** After setup, the zone operates without the caster spending actions, WP, or attention.

**Safe version:** Zone effects should require ongoing caster maintenance (concentration, WP per round, or re-casting). If the caster is free to do other things, the zone is too independent.

---

### Pattern E: The One-Decision Everything Build

**Template:** _A single character creation choice (kin, profession, or one talent) activates a mechanism that multiplies every subsequent advancement decision._

**Examples:** Half-Elf Psychic Power (amplifies every talent and spell simultaneously), Goblin Nocturnal + Darkness (one spell creates permanent darkvision advantage for entire build).

**Recognition cue:** The rule description reads "all," "any," "every time," or "whenever" without a specific named scope.

**Safe version:** Kin and profession multipliers should apply to one defined category — not to all talents, not to all spells, not to all skills at once.

---

## Red Flag Keywords

Scan any new rule text for these phrases. Each one warrants at least a second look. Two or more in the same rule warrants full five-test analysis.

| Keyword or Phrase                      | Why It Is A Red Flag                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| "free action"                          | Free actions are additive. Two free actions per round is an extra fast action.                         |
| "any die roll"                         | Universal reroll authority removes randomness as a balance tool.                                       |
| "without rolling"                      | Removes the random-failure mechanic the ability was costed around.                                     |
| "no mishap"                            | Safe casting already exists. A second source stacks.                                                   |
| "gain WP"                              | Cross-check every WP-GRANT against Psychic Power and existing WP loops.                                |
| "ignore armor"                         | Cross-check with existing armor-bypass stacks immediately.                                             |
| "per Power Level"                      | Any per-PL scaling interacts with Psychic Power's PL amplification.                                    |
| "zone" or "area"                       | Cross-check with Living Spell and Stabilize Magic Zone.                                                |
| "persistent" or "lasts until"          | Duration without decay requires maintenance cost.                                                      |
| "does not count as an action"          | Equivalent to granting a free action.                                                                  |
| "regardless of target's armor"         | Stacks with existing bypass effects.                                                                   |
| "automatically succeed"                | Check what existing auto-succeed rules cover the same territory.                                       |
| "without offering anything"            | Social compliance without roll → Serenity territory.                                                   |
| "cannot be targeted"                   | Full immunity to an attack channel requires scrutiny.                                                  |
| "as a power word" / "as a fast action" | Check Prepare Magic interaction.                                                                       |
| "may be cast as a ritual"              | If it wasn't already a ritual, check why the time cost is being removed.                               |
| "once per campaign"                    | Once-per-campaign is a legitimate safety valve. Once-per-session is borderline.                        |
| "may be recast"                        | Renewable backup bodies, renewable insurance, renewable dominance.                                     |
| "while unconscious" or "after death"   | Death-bypass territory.                                                                                |
| "transfer to another body"             | Clone + Body Swap territory.                                                                           |
| "stack with"                           | Any rule that explicitly states it stacks needs extra scrutiny — designer was aware of an interaction. |
| "in addition to"                       | Additive instead of replacing. Usually fine, but check against high-output existing abilities.         |

---

## Cross-Rule Interaction Log

Use this section to record combinations found during intake reviews of new content. This becomes an ongoing record of all interactions flagged, cleared, or corrected over time. Add entries as new content is screened.

Format per entry:

```text
**[New Rule Name]** × **[Existing Rule Name]**
Tag(s): [mechanism tags that fired]
Overlap: [which overlap question said yes, or "none — cross-reference only"]
Verdict: [Safe / Cap / Restructure / Reject]
Resolution: [rule text change made, or "none needed"]
```

### Recorded Entries

Empty — populate as new content is screened.
