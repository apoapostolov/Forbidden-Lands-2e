<!-- markdownlint-disable MD013 -->

# Balance and Synergy — The Generic Check Method

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This file owns the *executable check method* for any YZE rule or new game. It does **not** hold the instantiated catalogs (which exact talent breaks which game) — those live in the game-specific skills (see §9 Reconciliation). Use this file as the *how to check*; load the siblings for the *what was found*.

## Contents

1. Source provenance
2. Abstraction target
3. Expected-success math (the dice-pool probability core)
4. Attrition and breakpoint curves
5. The abuse families
6. The synergy stress-test protocol
7. Table-behavior lenses
8. The full playtest checks (intent → math → abuse → synergy → table → verdict)
9. Reconciliation with game-specific skills
10. Rule Choices and Build Recipe
11. Design intent

## Source provenance

**Mathematical backbone (the engine's probability core):**
- `01-corebook/03-skills.md:103-118` — the FL **Chance of Success** table (1–10 dice, base vs pushed). This is the single most-cited artifact in the whole system: it *is* the engine's published probability model.
- `skills/forbidden-lands-design/references/engine-math-and-rule-families.md:474-667` — the full derivation: per-die rates, the binomial core, pushed-lifecycle math by die type, the mixed-pool table (Base/Skill/Gear composition), design implications.
- `skills/forbidden-lands-design/references/engine-math-and-rule-families.md:588-666` — pushed bane-load and expected Willpower/Faith gain; the `2/9`, `11/36`, `1/6` per-die lifecycle rates.
- `skills/forbidden-lands-design/references/realism-audit-synergy-and-change-scenarios.md:312-394` — five mathematical change scenarios (per-die-rate shifts, resource-die longevity, recovery compression, auto-success vs die bonus, action-cost reduction) showing how sensitive the engine is.

**Synergy & abuse method (the interaction-analysis half):**
- `skills/forbidden-lands-design/references/willpower-synergy-spells-and-recovery-analysis.md:161-323` — the rule set interaction matrix; talent path risk categories; the spell-system volatility model; recovery as a logistical network.
- `skills/forbidden-lands-design/references/realism-audit-synergy-and-change-scenarios.md:192-311` — the proposal-audit method (7 stages + verdict classes); the five synergy classes; the proposal synergy-review questions.
- `skills/forbidden-lands-synergy-analysis/SKILL.md:44-208` — the **healthy vs unhealthy** distinction; the **Five Tests** (Decision Cost / Risk Exposure / Opportunity Cost / Repeatability / Campaign Erosion); the six-step analysis method; the verdict ladder.
- `skills/forbidden-lands-synergy-analysis/references/new-content-screener.md` — the decision tree: rule tagging, danger-zone cross-reference, overlap questions, red-flag keywords, fix templates, the seven abstract synergy patterns (A–G).
- `skills/rpg-balance-analysis/SKILL.md` — the four-lens balance model (mathematical / perceived / table / campaign), the psychological and game-theory checks.
- `skills/rpg-synergy-analysis/SKILL.md` — the West-side mirror of the Five Tests and six-step method.

**Instantiated catalogs (referenced, NOT duplicated):**
- `skills/forbidden-lands-synergy-analysis/references/exploitation-surface-catalog/` — the FL exploit catalog (10 files, ~191 worked entries across the eight abuse-surface categories).
- `skills/rpg-synergy-analysis/` and `skills/rpg-balance-analysis/` — the West-side balance/synergy method.

## Abstraction target

Own the **generic balance & synergy methodology** for YZE: how to *measure* whether a rule is balanced (expected-success math, attrition curves, breakpoints), how to *find* its abuses (the abuse families), how to *stress* its interactions (the synergy protocol), and how to *read* its table behavior (the lenses). The deliverable is an **executable review path** that any new rule or new game can be run through, end to end, to a verdict.

This file is the *transferable method*. The math is engine-specific and reproduced here in full (it is the backbone every YZE game shares). The *abuse families* are the abstract shape of the FL catalog, with its categories generalized and its detection heuristics given — but the actual "talent X breaks Y" entries stay in the sibling skills. Apply the Abstraction Ladder (source instance → common pattern → design intent → choices) to each of: the math, the abuse families, the synergy protocol, the table lenses, and the review path.

The companion `14-recipes-new-game-new-rule.md` restates §8 below as a maker's checklist. This file owns the *what to check and how*; that file owns the *go build one*.

## 3. Expected-success math (the dice-pool probability core)

This is the engine's mathematical spine. Every YZE game instantiates it; the numbers are invariant because the resolution grammar is invariant (n D6, count sixes). Source: `engine-math-and-rule-families.md:474-667`, reproduced against the FL corebook table at `01-corebook/03-skills.md:103-118`.

### 3.1 The binomial core

A pool of `n` identical D6, each succeeding on a 6. Per-die success probability `p`, failure `q = 1 − p`.

- **P(≥ 1 success) = 1 − qⁿ = 1 − (1 − p)ⁿ**
- **P(≥ k successes) = Σᵢ₌ₖⁿ C(n,i) · pⁱ · qⁿ⁻ⁱ** (binomial tail)
- **Expected successes E = n · p**

For the **initial (unpushed) roll**, every die is identical — color (Base/Skill/Gear) does not matter until push enters. So `p = 1/6`, `q = 5/6`, and:

- P(≥1) = 1 − (5/6)ⁿ
- E = n/6

`engine-math-and-rule-families.md:496-504, 557-575`.

### 3.2 The push lifecycle — where composition starts to matter

The push (reroll all non-6 dice once; FL also locks the cost face) changes the per-die success probability, and **differently by die type**, because the cost face (a 1) is locked on Base/Gear dice but inert on Skill dice. `engine-math-and-rule-families.md:506-555`.

**Skill die after one legal push** (the 1 rerolls, never counts as a cost face):
- P(success) = 1/6 + (5/6)·(1/6) = **11/36 ≈ 0.3056**
- P(blank) = 25/36

**Base or Gear die after one legal push** (the 1 *locks* as a cost face and cannot become a success):
- P(success) = 1/6 + (4/6)·(1/6) = **2/9 ≈ 0.2222**
- P(cost face) = **1/6** (the locked 1)
- P(blank) = 11/18

**The hidden central asymmetry:** adding one **Skill die** to a pushed pool is strictly stronger than adding one Base or Gear die — higher success rate *and* no cost-face exposure *and* no gear wear. A bonus that resolves as a skill-type die is worth more than its face-value die count. `engine-math-and-rule-families.md:547-555, 670-678`.

### 3.3 The FL Chance-of-Success table — the engine's published backbone

This table is reproduced verbatim from `01-corebook/03-skills.md:103-118`. It is the engine's *public* probability model: the **base column is the homogeneous `1/6` model** (exact match); the **pushed column is the homogeneous `2/9` bane-bearing model** (exact match to within rounding — it understates skill-heavy pools and overstates nothing). Both columns are computed from the formulas in §3.1–3.2.

| NUMBER OF DICE | CHANCE OF SUCCESS (1/6, base) | PUSHED ROLL (2/9) |
| -------------- | ----------------------------- | ----------------- |
| 1              | 17%                           | 29%               |
| 2              | 31%                           | 50%               |
| 3              | 42%                           | 64%               |
| 4              | 52%                           | 74%               |
| 5              | 60%                           | 81%               |
| 6              | 67%                           | 87%               |
| 7              | 72%                           | 90%               |
| 8              | 77%                           | 93%               |
| 9              | 81%                           | 95%               |
| 10             | 84%                           | 96%               |

**Read the table as three facts:** (1) the engine is *steep* — going from 1 to 4 dice roughly triples your success odds; (2) pushing is worth ~+8 to +12 percentage points at small pools and compresses at large ones; (3) **P(≥1) flattens near 1.0 around 8–10 dice**, so any rule that reliably assembles a 10-die pool has effectively deleted the failure chance. `01-corebook/03-skills.md:105-118`.

### 3.4 Threshold steepness — why Challenging/Difficult are walls, not steps

The success ladder raises the required successes (Normal 1⚔ / Challenging 2⚔ / Difficult 3⚔; West reads the grade 0/1/2/3+). P(≥k) falls off a cliff as k rises. Homogeneous `1/6` initial roll:

| Dice | P(≥1) | P(≥2) | P(≥3) |
| ---- | ----- | ----- | ----- |
| 4    | 52%   | 13%   | 1.6%  |
| 6    | 67%   | 26%   | 6.2%  |
| 8    | 77%   | 40%   | 13%   |
| 10   | 84%   | 52%   | 22%   |

`engine-math-and-rule-families.md:563-575`. **Design consequence (the single most important math fact for balance):** because 2⚔ and 3⚔ thresholds are steep, a rule that grants **one automatic success** is far stronger than a rule that adds **one die** — especially on medium pools. At 6 dice, +1 die moves P(≥2) from 26% to ~40%; one auto-success moves it to *guaranteed*. **Auto-success is a premium effect category; treat it as such.** `realism-audit-synergy-and-change-scenarios.md:364-377`.

### 3.5 How pool composition changes expected outcome (the mixed-pool table)

Same total dice, different Base/Skill/Gear split → same initial P(≥k), **different** pushed P(≥k) *and* different cost-face load. The engine is not balanced on raw die count; it is balanced on composition. `engine-math-and-rule-families.md:634-667`. Representative rows (B/S/G = Base/Skill/Gear; pushed values assume one legal push; EBaseBanePush = expected attribute damage from pushed Base dice; EWPpush = expected Willpower/Faith gained):

| B/S/G | Init 1+ | Push 1+ | Init 2+ | Push 2+ | EBaseBanePush | EWPpush |
| ----- | ------- | ------- | ------- | ------- | ------------- | ------- |
| 2/2/0 | 52%     | 71%     | 13%     | 28%     | 0.33          | 0.33    |
| 3/2/0 | 60%     | 77%     | 20%     | 38%     | 0.50          | 0.50    |
| 4/2/0 | 67%     | 82%     | 26%     | 47%     | 0.67          | 0.67    |
| 3/3/0 | 67%     | 84%     | 26%     | 50%     | 0.50          | 0.50    |
| 4/3/1 | 77%     | 90%     | 40%     | 64%     | 0.67          | 0.67    |
| 3/3/2 | 77%     | 90%     | 40%     | 64%     | 0.50          | 0.50    |

**Read it twice:** `4/3/1` and `3/3/2` have identical success rates — but `4/3/1` generates more Willpower/Faith (more Base dice) while `3/3/2` generates more gear wear (more Gear dice). **Composition is a design lever, not just a math input.** When you design a bonus, the question is never only "how many dice" — it is "what *kind* of dice, what cost channel do they activate on push, and do they produce Willpower/Faith, gear loss, or neither." `engine-math-and-rule-families.md:656-717`.

### 3.6 How pushing changes the *cost* outcome (the Willpower/Faith loop)

For `m` pushed **Base** dice (the only dice that feed the Willpower/Faith in FL's model):
- **Expected Willpower/Faith gain = m/6**; P(≥1 gain) = 1 − (5/6)ᵐ.
- **Expected attribute damage = m/6** (same rate — gain and harm are the *same* die face).
- A character pushing 4 Base dice is already **>50% likely** to take ≥1 damage *and* gain ≥1 Willpower/Faith.

`engine-math-and-rule-families.md:610-631`; `willpower-synergy-spells-and-recovery-analysis.md:40-63`. This is the virtuous damage loop: pushing hurts *and* fuels the comeback in the same action. **Any rule that reduces Base-die cost without also touching Willpower/Faith gain distorts the economy** — it severs the loop's symmetry. `engine-math-and-rule-families.md:680-685`.

### 3.7 The sensitivity warning (from the change scenarios)

The engine is **mathematically sharp**: small input changes detonate the tier system. Calibrated examples (`realism-audit-synergy-and-change-scenarios.md:317-394`):

- **Per-die rate 1/6 → 2/6:** a 6-die pool's P(≥1) jumps 67%→91%, P(≥3) jumps 6%→32%. A "modest" per-die buff makes Challenging routine.
- **Auto-success vs +1 die:** auto-success dominates on medium pools (see §3.4).
- **Action-cost reduction (slow→fast, fast→free):** often stronger than a numeric buff, because it changes opportunity structure, not output. Analyze action-cost changes *before* numeric buffs.
- **Recovery compression (care halves time):** one of the strongest tempo effects; repeatable "care-equivalents" are high-impact even when they look small.

**Rule of method:** whenever a proposal changes `p`, grants successes, compresses actions, or compresses recovery, recompute the table in §3.3/3.4 against the new values before judging balance. Never eyeball it.

## 4. Attrition and breakpoint curves

### 4.1 The attrition model

YZE does not have hit points. It has **layered resource pools** that deplete and feed each other, and whose depletion is *non-linear* because pools double as die-count. The model (`willpower-synergy-spells-and-recovery-analysis.md:420-543`):

1. **Attribute pool** — current attribute score *is* the Base-Die count. Damage shrinks the live pool → shrinks future success → invites more pushing → invites more damage. This is the engine's most elegant loop: damage doesn't only move you toward death, it sharpens every future decision.
2. **Willpower/Faith pool** — capped (10), earned from risk (FL) or action/success (West), spent on exceptions. Earned rate ≈ pushed-Base-dice/6.
3. **Gear pool** — gear-bonus dice and durability; degrades on pushed Gear banes; produces risk *without* Willpower/Faith payoff.
4. **Time pool** — Quarter-Days / Shifts; the travel and recovery clock. Every activity spends it; scarcity is what makes camp, forage, and haste meaningful.

A session is a **depletion curve** across all four. The campaign is the curve's slope over many sessions, modulated by recovery (which is itself a logistics puzzle, not a rest button — `willpower-synergy-spells-and-recovery-analysis.md:454-496`).

### 4.2 The breakpoint — definition and computation

> **Breakpoint** = the pool size `n*` at which expected success drops below a chosen threshold `T`. It is the *minimum competence floor* the engine guarantees, and the *maximum abuse ceiling* it tolerates.

**To compute a breakpoint for a new rule:**

1. **Fix the threshold** `T` (the game's design target — see §10). Canonical YZE targets: `T = 0.50` for "a competent character usually succeeds at a normal task"; `T = 0.80` for "an expert reliably succeeds."
2. **Fix the model** — initial (`p = 1/6`) or pushed (`p = 2/9` bane-bearing, `11/36` skill-type). Use the model the rule actually triggers.
3. **Solve** `1 − (1 − p)ⁿ ≥ T` for the largest `n` that *fails* — that `n` is the threshold's lower edge; `n* = n+1` is the breakpoint (the smallest pool that *meets* `T`).
   - Closed form: `n* = ⌈ ln(1−T) / ln(1−p) ⌉`.
4. **For a multi-success breakpoint** (Challenging/Difficult), solve the binomial tail `Σᵢ₌ₖⁿ C(n,i)pⁱqⁿ⁻ⁱ ≥ T` numerically for `n`.

**Calibrated breakpoints from the engine (p = 1/6, initial):**

| Threshold T | Breakpoint n* (initial) | Breakpoint n* (pushed, 2/9) |
| ----------- | ----------------------- | --------------------------- |
| P(≥1) ≥ 50% | 4 dice                  | 3 dice                      |
| P(≥1) ≥ 80% | 9 dice                  | 7 dice                      |
| P(≥2) ≥ 50% | 9 dice                  | 7 dice                      |

Read this as: **a starting character with a 4-die pool sits exactly on the 50% competence line** — that is the engine's intended baseline tension. A rule that hands out +3 dice for free pushes a marginal character past the breakpoint into reliable success. A rule that *removes* 3 dice (e.g. a difficulty step) drops an expert back to coin-flip. **Both are balance-relevant and both should be flagged by §8.**

### 4.3 Using breakpoints to check a new rule

For any new rule, ask: **does it move a typical pool across a breakpoint, and is that movement gated?**

- A **+1 die talent, gated by Willpower/Faith and situational** — fine; it nudges, doesn't cross.
- A **+3 die talent, passive, always-on** — it crosses the 50% breakpoint for a starting character; this is a balance event. Either gate it (cost/situation/limit) or reduce it.
- An **auto-success** — it *deletes* the breakpoint for that task; treat as a premium, rare, costly effect (§3.4).
- A **recovery rule** that moves the attrition curve's slope — recompute the session-length depletion: if a typical party now ends a session *higher* on resources than it started, the attrition spine is broken (`willpower-synergy-spells-and-recovery-analysis.md:504-529`).

### 4.4 Resource-die longevity (a calibrated attrition sub-tool)

For stepdown resource dice (`D12 → D10 → D8 → D6 → lost`, depleting on a 1–2), expected hard uses before loss ≈ **18**. This is the engine's template for "meaningful but not annoying" depletion — durable enough for expedition tools, still finite. Use it as the reference point when designing any new consumable/resource-depletion rule. `realism-audit-synergy-and-change-scenarios.md:335-345`.

## 5. The abuse families

This generalizes the **eight categories** of the FL exploit catalog (`forbidden-lands-synergy-analysis/SKILL.md:119-131`; catalog at `references/exploitation-surface-catalog/`). Each entry below gives the **generic definition** and a **detection heuristic** — the test you run to catch it in any new rule. The instantiated "which talent does this in FL" findings stay in the sibling skill; this is the *shape* to watch for.

### 5.0 The master distinction (load before the categories)

**Healthy synergy vs unhealthy synergy look similar in output but differ in input cost** (`rpg-synergy-analysis/SKILL.md:35-68`, `forbidden-lands-synergy-analysis/SKILL.md:44-68`):
- **Healthy:** requires deliberate in-play setup (positioning, timing, resource spend), real risk exposure, coordination, a tradeoff that closes other options. Payoff is dramatic *because the cost was visible*.
- **Unhealthy:** requires a single character-creation/advancement decision, no ongoing risk or tradeoff, no coordination, works automatically every time. Payoff is routine and dominant *because the cost was invisible*.

Every category below is unhealthy only when it fires **without gate**. The detection heuristic for all of them is the same first question: *does activating this require one easy decision or many hard ones?* (`forbidden-lands-synergy-analysis/references/exploitation-surface-catalog/01-foundations.md:9-24` — the decision-cost ladder: 0–1 decisions + per-round activation = the danger zone; 3+ decisions + per-use cost = the sweet spot.)

### 5.1 Infinite-loop combos (resource-refund loops)

**Definition:** spend X to get X (or more) back under a condition Y the character already achieves by doing the thing. Cost and trigger are the same activity — fighting refunds the resource spent fighting. Catalog pattern **A — The Free Refund** (`new-content-screener.md:614-624`).

**Detection heuristic:** trace the resource flow. If resource spent returns through the *same* loop that spent it, the cost is cosmetic. Concretely: does the rule grant Willpower/Faith (or action, or healing) on a trigger the character already hits every round? If yes and ungated → abuse.

### 5.2 Cap-bypass (exceeding a designed ceiling)

**Definition:** a rule lets a value exceed a cap the engine enforces elsewhere (Willpower/Faith cap, per-round action cap, simultaneous-buff cap, armor-stack limit, dice-pool size). The cap exists as a brake; bypassing it removes the brake.

**Detection heuristic:** list every cap the engine sets (Willpower/Faith max, free actions/round, bound buffs, damage-reduction layers, dodge frequency). Does the new rule let any value exceed or ignore one? Does it create a *second* source of a capped effect (e.g. a second grimoire-equivalent, a second always-on armor source)? If yes → abuse unless hard-gated.

### 5.3 Silent-stacking (additive layers without a "replace, don't stack" clause)

**Definition:** multiple sources of the same kind of bonus/reduction that each apply separately with no rule saying "take the higher" or "does not stack." Catalog pattern **G — The Stacking Gate** (`new-content-screener.md:671-680`): spell-armor + worn-armor + ward + immunity = three gates each must be beaten.

**Detection heuristic:** for every bonus/reduction the rule grants, ask "replace or stack?" against every existing source of the same effect. If the text doesn't say *replace*, players will stack it. Default fix: "this replaces (does not stack with) other sources of [X]."

### 5.4 Free-resource generation (Willpower/Faith / supply / wealth from nothing)

**Definition:** the rule produces a spendable resource without a proportional cost in risk, time, or another resource. The FL catalog's **WP Economy Loops** category (`SKILL.md:123`) and the broader **economy-bypass** tag (`new-content-screener.md:166`). Because the FL talent chapter defaults to a **1-Willpower/Faith-unit price point** for most bursts (`willpower-synergy-spells-and-recovery-analysis.md:93-126`), *even one unit of free generation distorts dozens of talents at once.*

**Detection heuristic:** does the rule grant Willpower/Faith, supply, crafted goods, or healing without consuming an action, taking a risk, or spending a comparable resource? Does it passively grant >1 Willpower/Faith unit per round? If yes → abuse. (FL guardrail: no passive ability should grant >1 WP/round — `new-content-screener.md:744`.)

### 5.5 Action-economy abuse (free / extra / compressed actions)

**Definition:** the rule grants additional actions, converts slow→fast or fast→free, or grants ally/reactive actions, breaking the opportunity-cost structure. Catalog category **Action Compression Stacking** (`SKILL.md:124`); tags `ACTION-GRANT`, `ACTION-FREE` (`new-content-screene.md:134-135`). Action-economy advantages *outscale raw dice bonuses* because they change not just output but *opportunity structure* (`willpower-synergy-spells-and-recovery-analysis.md:264-278`).

**Detection heuristic:** count the actions the rule yields per round. Is there a per-round limit? Does it stack with other action sources? Does it convert an action type without a per-use cost? Multiply per-use power by expected frequency — a moderate effect every round beats a devastating one once/session. (`new-content-screener.md:480-495`.)

### 5.6 Push-cost avoidance (severing the risk-power exchange)

**Definition:** the rule reduces or removes the cost of pushing (bane damage, gear wear, Willpower/Faith spend) without removing the *benefit* of pushing. This severs the loop symmetry in §3.6 — the engine's signature "ambition costs something" contract. Catalog pattern **C — The Risk Bypass** (`new-content-screener.md:631-640`).

**Detection heuristic:** does the rule let a character push (or gain push-equivalent rerolls) with reduced/no cost-face consequence, or refund the cost? Does it grant *extra* pushes? Any rule that permits repeated pushing makes *every* bane-softener, success-converter, and refund loop much more dangerous than it looks alone (`realism-audit-synergy-and-change-scenarios.md:273-281`). Pair-test it with §5.1 and §5.4.

### 5.7 Mishap / consequence avoidance (removing the failure tax)

**Definition:** the rule reduces or removes the engine's failure-pressure layer — FL's banes and mishaps, West's Trouble — without replacing it. The pressure layer is what makes magic "volatile leverage" rather than "riskless utility" (`willpower-synergy-spells-and-recovery-analysis.md:324-371`); the safe-casting + grimoire + rank-advantage package is already a risk-control system, and any *additional* stabilizer risks collapsing it (`realism-audit-synergy-and-change-scenarios.md:283-294`).

**Detection heuristic:** does the rule reduce mishap dice/severity, allow casting without rolling, extend a zero-dice threshold, or buy off Trouble? Does it stack with existing stabilizers? If it can reduce a task to zero failure pressure, it converts unstable leverage into dominant utility → abuse.

### 5.8 Talent / spell / rule invalidation (silent overwriting)

**Definition:** the new rule makes an existing rule, talent path, or spell discipline redundant or pointless — not by being better, but by *covering its niche for free*. This is one of the six forbidden inherited anti-patterns (silent invalidation). It also runs in reverse: a rule that *duplicates* an existing rule (rule bloat) is the same disease.

**Detection heuristic:** for the new rule's effect, name the existing rules that already do it. Does the new rule do it cheaper, easier, or more broadly? Does the build that takes it still have access to the adjacent niches other builds specialize in (the opportunity-cost test, §6)? If a character can take this and still cover what specialists cover, it invalidations them → restructure or separate.

### 5.9 The seven abstract patterns (the root causes)

Every unhealthy abuse in the FL catalog traces to one or more of seven root patterns (`new-content-screener.md:608-680`). When a detection heuristic above fires, name the pattern — the pattern dictates the fix template:

| Pattern | Shape | Catalog fix |
| ------- | ----- | ----------- |
| **A — Free Refund** | spend X, get X back from the same activity | make trigger rare or refund partial |
| **B — Unscoped Amplifier** | multiply *all* of a resource/roll/spell | name the scope ("X-school only") |
| **C — Risk Bypass** | remove the cost that made it fair ("without X") | reduce partially, don't remove |
| **D — Self-Maintaining Zone** | one cast, permanent no-action effect | require maintenance (per-round cost / concentration / recast) |
| **E — One-Decision Build** | one creation choice multiplies all later choices | apply to one named category, not all |
| **F — Invisible Attacker** | attack from a state the target can't retaliate from, no cost to maintain | require new positioning/stealth roll after each attack |
| **G — Stacking Gate** | multiple sequential reduction layers each with their own roll | layers *replace*, take the higher |

## 6. The synergy stress-test protocol

A step-by-step protocol for stress-testing any new rule's interactions. It generalizes the six-step method (`rpg-synergy-analysis/SKILL.md:117-152`, `forbidden-lands-synergy-analysis/SKILL.md:132-165`) and the proposal-audit integration check (`realism-audit-synergy-and-change-scenarios.md:132-143`). Run it in order; stop early only when a step forces a redesign.

### Step 1 — Map the touch surface

List **every rule set the new rule touches.** Use the rule-type families (`engine-math-and-rule-families.md:342-473`) as the checklist: resolution, push, action-budget, damage-state, recovery, resource, travel-pressure, exception, advancement, economy/access. A rule that touches **two or more** of {Willpower/Faith, recovery, spell/power, travel pressure} is **system-level, not local** — review it as such (`willpower-synergy-spells-and-recovery-analysis.md:210-218`, `realism-audit-synergy-and-change-scenarios.md:140-143`).

### Step 2 — Enumerate the interactions

For each touched rule set, list the specific existing rules it connects to (talents, spells, gear properties, conditions, the push loop, the recovery network). Describe the chain: *which rule feeds which, what triggers what* (`rpg-synergy-analysis/SKILL.md:122-125`).

### Step 3 — Apply the "more than the sum of parts?" test

For each interaction, ask: **does this combo produce more effect than the sum of its parts?** Concretely, run the **overlap questions** (`new-content-screener.md:368-402`):
- **(A) Does it make an existing danger cheaper?** (lower cost, fewer decisions, no kin/profession gate)
- **(B) Does it increase an existing danger's output?** (higher power, more targets, longer duration, more damage)
- **(C) Does it remove an existing brake?** (kills a cooldown, bypasses a per-turn limit, negates concentration)

0 yes → proceed. 1 yes on a Monitor/Clean zone → **Cap**. 1 yes on a Cap/Restructure zone → **Restructure**. 2+ yes → **Reject or Separate**.

### Step 4 — If yes, is it gated by cost / time / risk?

For every "more than the sum" interaction, apply the **Five Tests** (`rpg-synergy-analysis/SKILL.md:64-116`, `forbidden-lands-synergy-analysis/SKILL.md:71-118`). Score each Healthy / Borderline / Unhealthy:

1. **Decision Cost** — how many meaningful decisions to activate? (0–1 = danger zone; 4+ = sweet spot)
2. **Risk Exposure** — what does the player risk? (if cost refunds through the same loop, risk is cosmetic)
3. **Opportunity Cost** — what does the player give up? (if the build still covers adjacent niches, too broad)
4. **Repeatability** — how often per session/encounter/turn? (per-use power × frequency; a moderate every-round effect beats a devastating once/session one)
5. **Campaign Erosion** — does it hollow out a pressure channel the campaign depends on? (name the channel; if it *deletes* rather than *relieves*, the campaign flattens)

**If a combo is "more than the sum of parts" AND fails the gating tests (cost/time/risk absent or cosmetic) → it is an abuse.** This is the protocol's core verdict rule.

### Step 5 — Pressure-channel audit

Name every pressure channel the combo relieves and every channel it leaves intact (`forbidden-lands-synergy-analysis/SKILL.md:148-151`, `new-content-screener.md:52-64`). The engine's channels: resource attrition, injury fear, action scarcity, Willpower/Faith scarcity, time pressure, mishap risk, social resistance, environmental hostility. **A combo that deletes a channel (not temporarily relieves) breaks the campaign spine.**

### Step 6 — Baseline comparison

What does a character *without* this combo look like in the same situation? If the gap is enormous with no corresponding cost, the combo is dominant (`rpg-synergy-analysis/SKILL.md:139-142`).

### Step 7 — Verdict and fix

One of (`rpg-synergy-analysis/SKILL.md:144-152`, `new-content-screener.md:683-694`):
- **Clean** — strong but earned; no action.
- **Monitor** — borderline; flag for GM awareness.
- **Cap** — add a frequency limit, resource ceiling, or cooldown. (Apply a fix template: per-round limit, per-QD limit, WP-capped activation, non-refundable cost, re-roll-after-trigger, exclude-from-stacking, restrict-bind/restrict-God-Spell, lock-to-scope, escalating cost, require-resistance — `new-content-screener.md:519-606`.)
- **Restructure** — redesign the rule pattern to close the loop; re-run from Step 2.
- **Separate** — the components must not be available to one character without a significant gate.

### Step 8 — Red-flag keyword scan (the fast filter)

Before shipping, scan the rule text for the red-flag vocabulary (`new-content-screener.md:406-437`): "free action," "any die roll," "without rolling," "no mishap," "gain WP," "ignore armor," "per Power Level," "zone/area," "persistent/lasts until," "does not count as an action," "automatically succeed," "cannot be targeted," "stack with," "in addition to," "all allies/all enemies," "daily/at dawn," "hidden/remain hidden," "immunity." **Two or more in one rule → run the full Five Tests.** This is the cheapest pre-filter in the whole method.

## 7. Table-behavior lenses

Balance is not only "is the math fair." A rule that is mathematically balanced but unplayable, ambiguous, or GM-punishing is still broken. Read every rule through these lenses, generalized from both design skills' checklists (`rpg-balance-analysis/SKILL.md:13-90`, `realism-audit-synergy-and-change-scenarios.md:88-191`). Score each **OK / Caution / Fail**.

### 7.1 Mathematical balance
Odds, expected value, risk/reward, frequency of use. (Run §3 + §4.) Does it hit the breakpoint targets? Does it shift the per-die rate?

### 7.2 Perceived balance
What *feels* fair/powerful regardless of math. Does it create resentment, regret, false hope, or a fantasy-vs-payoff gap? Is the choice legible *before* commitment? (`rpg-balance-analysis/SKILL.md:22-29, 36-48`.) A mathematically fair rule that *feels* unfair is unstable.

### 7.3 Table balance — complexity & GM burden & speed
- **Player-facing complexity:** how much must the player hold in head to use it? (FL's colored-dice model is more precise; West's unified pool is faster — `00-engine-core.md` §5.)
- **GM burden:** does the GM track another timer, condition, or exception? Does the rule resolve in one sentence or require repeated interpretation? (`realism-audit-synergy-and-change-scenarios.md:146-160`.)
- **Speed in live play:** how many rolls, lookups, and decisions per resolution? "Don't roll too often" is an engine axiom (`00-engine-core.md:205`) — a rule that adds rolls floods the economy and flattens drama.

### 7.4 Ambiguity risk
Where two reasonable readings produce different outcomes. Does the rule *say* replace-or-stack, per-round-or-per-QD, resisted-or-not? Unstated → table dispute. (`realism-audit-synergy-and-change-scenarios.md:154-160, 161-170`.)

### 7.5 Recoverability & permanence
- **Recoverability:** if the rule's outcome is bad, can the character/party recover, and how fast? A rule whose failure state is "you are functionally unusable" must *say so honestly* (retirement-default vs fatal) — hidden non-playability is forbidden (`realism-audit-synergy-and-change-scenarios.md:55-71`).
- **Permanence:** how long does the effect last? Permanent/always-on effects are the highest-risk surface (catalog pattern D). Does it decay, require maintenance, or end on a condition?

### 7.6 Player agency after the rule lands
Does the rule create meaningful choice, or remove a character from useful play? Does it force the GM into soft correction to keep the game humane? Does it reward anti-social-but-optimal play? (`rpg-balance-analysis/SKILL.md:50-61, 86-90`.) A rule that *requires* GM mercy to remain fun is a failed rule.

### 7.7 Catastrophic-outcome playability
When the worst case fires (a Broken chain, a lethal critical, a mass-control landing), is the *resulting state* still playable, or does it end the session/campaign? Survival-with-cost is good design; hidden non-playability dressed as "survivable" is bad design (`realism-audit-synergy-and-change-scenarios.md:74-87`). Apply the practical realism test: *what decision does this make sharp? what abstraction does it replace? what is the new table burden? does it preserve campaign movement? if it cripples a character, is that honestly labeled?* (`realism-audit-synergy-and-change-scenarios.md:62-71`.)

### 7.8 Campaign balance
Long-term incentives, recovery loops, attrition pacing, scaling over many sessions (`rpg-balance-analysis/SKILL.md:30-35`). A fun edge case that is unsafe at campaign scale is still unsafe. Run §4's attrition curve over a multi-session horizon.

### 7.9 Verdict lens overlay
Map the lens results to the audit verdict classes (`realism-audit-synergy-and-change-scenarios.md:172-181`): **Accept now / Accept with simplification / Hold for broader rewrite / Reject for now / Reject as wrong chapter or wrong rule type.** Note the structural-rejection reasons specifically — *wrong problem, wrong chapter, wrong rule type, too much system impact for too little gain* — because "I dislike it" is not a usable verdict (`realism-audit-synergy-and-change-scenarios.md:396-439`).

## 8. The full playtest checks (intent → math → abuse → synergy → table → verdict)

This is the file's **key deliverable** — the end-to-end checklist any new rule passes through. It is the "check a new rule" half of `14-recipes-new-game-new-rule.md` (Recipe B), restated here with the executable detail. Run the stages in order; a fail at any stage loops back to redesign at that stage. For agent-run check, use `24-validation-worksheets.md` as the form layer for Stages 1-4 and report in `24 §9` format.

### Stage 0 — Intent & source check (gate)
- **What pressure / decision / loop does this rule serve?** If none, **reject** (rule bloat — one of the six forbidden anti-patterns). (`realism-audit-synergy-and-change-scenarios.md:92-99`.)
- **Does an existing rule already do this?** If yes, **reject as duplication** or fold into the existing rule. Identify the *chapter that owns the problem* and the *rule type* — a proposal solving a Chapter-8 problem in Chapter-6 language, or a talent problem with a general-rule patch, is a warning sign. (`realism-audit-synergy-and-change-scenarios.md:100-131`.)
- **Write the one-sentence rule summary** (strip all flavor): "Grants 1 WP when the character takes Strength damage." If you can't summarize it in one sentence, it does too much — split it. (`new-content-screener.md:97-118`.)

### Stage 1 — Math
- Run §3. Compute the rule's effect on expected successes (does it change `p`, grant successes, add dice?). Recompute the §3.3/3.4 tables against the new values.
- Run §4. Compute the breakpoint shift: does it move a typical pool across the 50% / 80% competence line? Is the shift gated?
- Check the §3.7 sensitivity cases: per-die-rate shift, auto-success, action-cost change, recovery compression.
- Fill `24 §1` and use the threshold warnings there for +1 die, +2 dice, auto-success, target-number shifts, and rerolls.

### Stage 2 — Abuse
- Run §5. Tag the rule's rule pattern (`new-content-screener.md:122-172`) and cross-reference the danger zones. Run the §5.9 pattern match. Run the §6 Step 8 red-flag keyword scan.
- For each fired tag/pattern, apply the detection heuristic. Does it cross into abuse territory *ungated*?

### Stage 3 — Synergy
- Run the §6 protocol in full: map the touch surface → enumerate interactions → "more than the sum?" → gated by cost/time/risk? → Five Tests → pressure-channel audit → baseline comparison.
- **Mandatory:** any rule touching {Willpower/Faith, recovery, spell/power, travel pressure} is system-level — do not let it ship as "local."

### Stage 4 — Table
- Run the §7 lenses. Score each OK/Caution/Fail. Pay special attention to: ambiguity (does it *say* replace-or-stack?), recoverability/permanence (is the worst case playable?), and GM burden (another timer?).
- Fill `24 §6` and `24 §7`. A General rule that adds multiple persistent states is a Caution unless it is the game's signature rule.

### Stage 5 — Layer & voice
- Classify the rule **General / Situational / Optional** and tag it.
- Place the voice correctly: design rationale stays in design docs; only native rulebook prose crosses into the corebook (`realism-audit-synergy-and-change-scenarios.md:161-170`).

### Stage 6 — Verdict
One of (combining the §6 Step 7 ladder and §7.9 audit classes):
- **Ship (Accept now)** — passes math, abuse, synergy, and table. Add to manuscript.
- **Ship with simplification (Accept with simplification)** — passes but is heavier than it needs to be; trim before adding.
- **Revise — Cap** — fails one test moderately; apply a fix template (`new-content-screener.md:519-606`) and re-run from Stage 1.
- **Revise — Restructure** — fails the rule pattern itself; redesign and re-run from Stage 0.
- **Hold** — depends on a broader rewrite not yet done; queue it.
- **Reject** — wrong problem / wrong chapter / wrong rule type / too much system impact for too little gain. Reject *structurally*, not impressionistically.

### Review path output format
Deliver the verdict in the screener's structured format (`new-content-screener.md:701-732`): Summary (one sentence) · Tags · Danger Zones Hit · Overlap answers (cheaper/stronger/brake-removed) · Red Flags · Five-Test results · Pattern Match · Verdict · Recommended Fix · (if Cap+) a catalog entry for the game-specific exploit catalog. **The catalog entry goes to the sibling skill, not this file** — see §9.

## 9. Reconciliation with game-specific skills

**This file owns the *method*.** It tells you *how to check* a rule. It does **not** tell you *what was found* in any specific game — that is the instantiated catalogs' job, and duplicating them here would violate the no-sibling-duplication rule and bloat this file past usefulness.

| If the question is… | Load… | Because… |
| --- | --- | --- |
| *How do I check if a rule is balanced?* | **This file** (`13`) | It owns the math, the abuse families, the synergy protocol, the lenses, the review path. |
| *Which FL talent combos break X? / Is this FL combo broken?* | `forbidden-lands-synergy-analysis` (+ its `exploitation-surface-catalog/`, 10 files, ~191 worked entries) | It owns the instantiated FL exploit findings and the FL-specific Five-Test verdicts. |
| *Which West combos break X? / Is this West build broken?* | `rpg-synergy-analysis` + `rpg-balance-analysis` | They own the West-side Five Tests and the four-lens balance model. |
| *How do I design a new FL rule in FL voice?* | `forbidden-lands-design` | Game-specific design/authoring. |
| *How do I design a new West rule?* | `western-rpg-design` | Game-specific design/authoring. |
| *How do I build a brand-new YZE game for a new genre?* | `14-recipes` Recipe A + this file's review path (Recipe B) | `14` owns the build procedure; this file owns the check procedure. |

**Division of labor, stated once:** when a question is *about the engine itself* (the math, the method, the families), `yze-design` leads and the game-specific skills supply instances. When a question is *about one game's implementation* (which exact talent, which exact spell), that game's skill leads and `yze-design` supplies the generic frame. **Never reproduce a sibling's catalog entries here.** When this file's review path (§8) produces a Cap+ verdict on a game-specific rule, the catalog entry it writes goes into *that game's* exploit catalog, not into this file.

## 10. Rule Choices and Build Recipe

For a **new game**, set the balance targets first; then every new rule is checked against them. The targets are the choices.

1. **Default pool size** — the competent-character baseline (FL ≈ 4–6 dice; West ≈ ability + attribute). This sets where the session's "normal task" sits on the §3.3 curve.
2. **Competence thresholds** — the `T` values for the §4 breakpoints. Canonical: `T = 0.50` (a competent character usually succeeds at a normal task), `T = 0.80` (an expert reliably succeeds). State them explicitly so §4 breakpoints are computable.
3. **Push-cost model** — bane-self-harm (FL) / currency-spend (West) / hybrid (`00-engine-core.md` §6, §11 choice 1). This determines which §3.2 per-die rate (2/9 bane-bearing vs the currency model's reroll-without-lock) the pushed column uses, and which cost channel the §5.6 detection heuristic watches.
4. **Willpower/Faith refuel model** — harm-earned / action-earned / success-earned / hybrid (`00-engine-core.md` §7, choice 3). This sets the §3.6 loop's symmetry and which §5.1/5.4 heuristics apply.
5. **Failure-pressure layer** — banes / Trouble / hybrid / none (`00-engine-core.md` choice 10). This sets what §5.7 (mishap/consequence avoidance) guards.
6. **Lethality & recoverability posture** — how fast damage → Broken → critical → retirement, and how fragmented recovery is. This sets the §7.5/7.7 catastrophic-outcome thresholds. (FL: fragmented recovery, real retirement pressure; West: comparable but Trouble-mediated.)
7. **Power-layer on/off & ceiling** — none / low / medium / high (`05-power-layer.md`, choice). This sets whether §5.7's magic-stabilizer heuristics apply at all.
8. **Action-economy granularity** — how many action types, what converts to what. This sets the §5.5 detection thresholds.

**Instantiation recipe for balance:** (1) set choices 1–2 (this fixes the math backbone and the breakpoints); (2) set choices 3–5 (this fixes which abuse categories are even *in scope* — a no-magic, no-banes game has no §5.7 magic-stabilizer surface); (3) set choices 6–8 (this fixes the table lenses' calibration); (4) **then** check every new rule through the §8 review path against these targets. A rule is "balanced" only *relative to its game's stated thresholds* — there is no absolute balance, only "does this hit the breakpoints and pass the lenses the choices defined."

## 11. Design intent

Balance, in this engine, is not "is this rule fair." It is: **does this rule produce the table behavior the engine intends — every roll a decision, every failure a resource pressure, every gain a paid cost — without abusable edge cases that delete a pressure channel.** The methodology in this file exists to make that check *executable instead of intuitive.*

The engine works because its pressure layers stack — pushing hurts, the Willpower/Faith matters, magic stays risky, recovery stays fragmented, critical injuries stay consequential (`willpower-synergy-spells-and-recovery-analysis.md:580-589`). That stack is the design spine. The math (§3) is sharp on purpose: small input changes detonate the tier system, which is *why* every numeric change must be recomputed, not eyeballed. The breakpoints (§4) exist so a designer can tell, in advance, whether a bonus crosses the competence line. The abuse families (§5) and synergy protocol (§6) exist because the engine's fragility lives at its *couplings* — where rule sets meet (`realism-audit-synergy-and-change-scenarios.md:410-418`: Willpower/Faith, action budget, injury conversion, recovery compression, travel-pressure removal). The table lenses (§7) exist because a rule can be mathematically clean and still be unplayable, ambiguous, or GM-punishing. The review path (§8) stitches them into one verdict so no rule ships on vibes.

The final test of any rule is the one the engine itself was built around: **does ambition still cost something after this rule lands?** If the answer is no — if the rule lets a character get more for less, for free, forever, from one decision — the rule fails, regardless of how the math looks in isolation. That is the methodology's whole purpose: to catch the moment a rule stops costing something, before it reaches the table.
