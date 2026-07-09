<!-- markdownlint-disable MD013 -->

# Engine Core — Resolution, Dice Grammar, Pushing, Willpower

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the engine spine — every other reference file assumes this material.

## Contents

1. Source provenance
2. Abstraction target
3. Dice grammar (base, skill, gear dice; success and bane symbols)
4. Success ladders (levels of effort)
5. Difficulty and modifications
6. Pushing rolls — the two cost models
7. Willpower and Faith
8. Opposed and group rolls
9. Artifact / legendary dice
10. Divergence rows (FL vs West)
11. Rule choices and instantiation recipe
12. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/03-skills.md:1-258` — dice grammar, sixes-as-success, banes, levels of effort, pushing, WP, modifications, negative dice, difficulty, help, opposed/group rolls, gear, artifact dice, Pride, the 16 skills.
- `01-corebook/01-front-matter.md` — dice/symbol overview (⚔ success, 💀 bane, 🩸 damage).
- `skills/forbidden-lands-design/references/engine-math-and-rule-taxonomy.md` — expected-success math, system map.

**Tales of the Old West 2E (West):**
- `01-corebook/03-rolling-the-bones.md:1-312` — dice pool, success ladder (0 fail / 1 limited / 2 complete / 3+ critical), modifications (±3 cap, stack), difficulty ladder, pushing via Faith, **Trouble** (Safe/Risky/Desperate + outcome tables), Declared Effort, Hidden Bad Luck, group/opposed rolls, Faith economy, the 16 abilities.

## Abstraction target

Reverse-engineer the **core resolution loop** of YZE into a genre-agnostic procedure. The two games instantiate the same spine (D6 pool, sixes = success, push-once) but diverge sharply on **cost of pushing** (attribute damage vs. Faith/Willpower spend) and on the **failure tax** (banes-on-dice vs. the Trouble system). Capture both as calibrated points on a single failure-pressure choice, and produce a recipe for instantiating the core loop in any genre.

## 3. Dice grammar (base, skill, gear dice; success and bane symbols)

**The core procedure (both games):** When an action's outcome is uncertain, the acting character rolls a pool of ordinary six-sided dice (D6). Every **6 rolled is a success (⚔)**. At least one ⚔ is usually required to succeed; additional ⚔ upgrade the outcome.

**FL — three colored pools, composed separately:**
- **Base Dice** (attribute, white): count = *current* score in the rolled attribute. Damage reduces the live pool.
- **Skill Dice** (skill, maroon): count = skill level.
- **Gear Dice / Weapon Dice** (gear, black): count = the bonus of the gear used. FL `03-skills.md:33-39`.
- **Symbol semantics:** ⚔ = success on any color. 💀 (skull) appears on **Base and Gear dice only** — ones on Skill Dice are inert and can be rerolled. 💀 has *no effect on the first roll* — it only activates when you push. FL `03-skills.md:29-31, 71-73`.

**West — single unified pool, color-blind:**
- Roll **ability level + current attribute** D6. There is no color distinction and no separate gear-die type in the core pool; gear enters as flat **modification dice**. West `03-rolling-the-bones.md:11-15`.
- **Symbol semantics:** ⚔ = success. **1s** are *latent Trouble fuel* — but only counted on Risky/Desperate fails, and only *after* the roll resolves. There are no "banes" baked into the dice faces. West `03-rolling-the-bones.md:25-33, 90-101`.

**Generic abstraction:** a pool of D6 where **6 = success**, a small graded success ladder, and a **latent cost face** (FL's 💀, West's 1) whose meaning is realized only on a *decision* the player makes (push) or a *frame* the GM sets (Trouble exposure). The cost face is the engine's pressure valve — its *trigger* is the rule choice.

## 4. Success ladders (levels of effort)

**FL — "Levels of Effort" (threshold-upgrade model):** Default needs 1⚔. GM or player may raise the bar: **Challenging = 2⚔ (Great)**, **Difficult = 3⚔ (Critical)**. Falling short of a raised bar but rolling ≥1⚔ yields the *normal* result — no loss, just no perk. Surplus ⚔ beyond the threshold convert to richer detail/clues/positioning. FL `03-skills.md:19-27`.

**West — graded ladder (result-reading model):** The roll is read on a 0/1/2/3+ ladder by default:
- `0` Failure — situation may worsen.
- `1` Limited — achieved, but not cleanly/fully/safely.
- `2` Complete — achieved cleanly.
- `3+` Critical — achieved + extra advantage/insight/speed/leverage.
West `03-rolling-the-bones.md:41-48`. In **violent conflict or any rule that spends extra successes**, surplus ⚔ become **Stunts** (extra damage, crit, force movement, disarm, etc.). West `03-rolling-the-bones.md:50-52`.

**West also offers "Declared Effort"** — the player declares Standard/Bold/Desperate *before* rolling to aim for an upgraded payoff (1/2/3 ⚔ thresholds). Functionally a player-side mirror of FL's GM-side "raise the bar." West `03-rolling-the-bones.md:58-68`.

**Generic abstraction:** two complementary mechanics over the same spine — (a) a **graded success ladder** that reads the raw ⚔ count, and (b) a **threshold-raise mechanic** (GM-side or player-side) that trades risk for a richer payoff. FL front-loads the threshold; West front-loads the grade. Both converge on Stunts for surplus ⚔. **Layer:** the ladder is General; threshold-raising / Declared Effort is Optional (player-facing) or Situational (GM-facing).

**Carry-Forward Bonus (Optional general rule).** Many rules throughout the engine grant a bonus to a subsequent roll when you succeed — banked leverage in a social scene, a tactical advantage from a Feint, the upper hand from winning a Pointed Question. When a rule grants such a bonus, the bonus scales with the grade of the success that earned it:

- A **normal success** (1⚔, or 1 net ⚔ after an opposed roll's cancellation) grants **+1** to the next relevant roll.
- A **critical success** (3+⚔, or 3+ net ⚔ after cancellation) grants **+2** instead.

**Net successes in an opposed roll.** When the bonus is earned from an opposed roll (an attack vs a parry, a manipulation vs an insight, a feint vs a wits check), count the attacker's successes *after* the defender's successes cancel them — the remainder is the attacker's **net successes**. A defender who parries well can reduce a critical to a normal success (dropping the carry-forward from +2 to +1), or even reduce it to zero (no carry-forward at all). A critical that survives the defense — 3 or more net ⚔ — still grants +2.

**How to use it.** This rule does not activate on its own. It activates when another rule says "you gain a bonus to your next roll" or "the opponent takes a penalty to their next roll" — the bonus or penalty is +1 for a normal success, +2 for a critical. Only one carry-forward bonus can be banked at a time (the same stacking rule as the modification cap — see §5). The bonus applies to the next roll that is *relevant* to the action that earned it: a banked advantage from a Feint applies to your next attack; a penalty from a Pointed Question applies to the opponent's next roll in that scene. The GM is the judge of relevance.

**Where it already appears.** The workshop's Social Combat module (`workshop/03`) uses banked ±1 bonuses extensively (BUILD RAPPORT, GESTURE/PROPS, SMALL LIE, POINTED QUESTION, the "Expose a tell" stunt). With this core rule in place, those bonuses scale to ±2 on a critical — a Social Combat in which a speaker lands a 3-⚔ BUILD RAPPORT now softens the opponent by −2, not −1. The ceremonial-conflict pattern (`03 §12`) uses carry-forward margins between phases; this rule generalizes that pattern to any roll. **Layer:** Optional — adopt it per-campaign; Situational when a specific rule invokes it.

**Success Menu (Optional general rule).** Use sparingly, and only for **downtime or long-process rolls whose output the players can describe in advance** — making camp, crafting, building or improving a base, running a business season, researching, forging a new spell or ritual, negotiating a treaty. When such a roll succeeds with **2 or more ⚔**, each ⚔ **beyond the first** buys one entry from a **Success Menu**: a list of qualities, features, or effects the acting players declare they want the output to have.

**How to build the menu.** Before the roll, the acting player (and the table, for a shared project) states what they are trying to produce and **names the qualities they want** — e.g. for a camp: quiet, a cooking place, a watch post, dry shelter; for a spell: longer duration, a wider area, a second target; for a stronghold function: hidden, defensible, self-repairing. The GM ratifies the list (qualities must be *fictionally possible for the approach* and *not already guaranteed by a normal success*) and may set a cost in ⚔ for especially potent entries. The menu is **player-authored within GM constraints** — this is what distinguishes the Success Menu from Stunts, whose menu is fixed and game-authored for tactical combat use (`03 §9`).

**Reading the roll against the menu.** A **normal success (1⚔)** produces the baseline output — the thing exists and works, with no extra qualities. Each additional ⚔ spends on one menu entry of the player's choice, in any order. A critical (3+ ⚔, or 3+ net ⚔ after an opposed roll's cancellation) buys entries **and** leaves the output notably superior — the GM narrates the surplus. Unused ⚔ can be banked as a **Carry-Forward Bonus** (above) to a directly-following roll for the same project, if the GM judges that relevant.

**When not to use it.** Reserve the Success Menu for rolls where (a) the outcome is a *thing you build or establish* rather than a momentary action, (b) the players can name the desired qualities in advance, and (c) success is not meaningfully *opposed*. For combat, social scenes, and any roll with immediate opposition, use **Stunts** (`03 §9`) instead — Stunts are the combat-speed analogue. The two rules never stack on the same roll: a roll either reads its surplus ⚔ against a fixed stunt list (fast, tactical) or against a player-authored Success Menu (slow, generative), never both.

**Where it already appears.** FL's **MAKE CAMP** is the canonical instance: each extra ⚔ buys one *camp improvement* — Banked Fire, Dry Shelter, Raised Beds, Cooking Place, Watch Post, Quiet Camp, Animal Picket (`06 §9`; FL `08-journeys.md:503-529`). FL's stronghold functions and West's base/business construction are the same pattern at a larger turn scale. The rule generalizes these into an engine-level mechanic for any player-authored long-process output. **Layer:** Optional — adopt per-campaign; Situational when a downtime/long-process roll invokes it.

## 5. Difficulty and modifications

**Both games share the same modification ladder and cap** (identical table):

| Difficulty | Modification |
| --- | --- |
| Trivial | +3 |
| Simple | +2 |
| Easy | +1 |
| Average | 0 |
| Demanding | −1 |
| Hard | −2 |
| Formidable | −3 |

FL `03-skills.md:166-178`; West `03-rolling-the-bones.md:174-178, 198-206`. **Cap:** each *individual* modification is capped at ±3, but **multiple modifications for different reasons stack** without limit.

**A critical divergence in what modifications touch:**
- **FL:** modifications affect **Skill Dice only** — never Base or Gear Dice. If skill dice go below zero, roll **negative dice** (any ⚔ on a negative die cancels a real ⚔). FL `03-skills.md:152-162`.
- **West:** modifications add/subtract **generic dice** from the unified pool; there are no negative dice. West `03-rolling-the-bones.md:176-182`.

**Help from others (both):** up to 3 helpers, +1 each (max +3).
- FL gates the *total help bonus* by the **lowest Empathy** in the group (a social-trust limit). FL `03-skills.md:182-190`.
- West requires each helper to have ≥1 rank in the ability. West `03-rolling-the-bones.md:192-196`.

**Generic abstraction:** a flat ±3-per-source, stack-without-cap modification model with a 7-step difficulty ladder. The **choice** is *which die type* modifications touch (colored skill-only vs unified) and *how* help is gated (social-stat cap vs ability-rank floor). FL's negative dice are an optional pressure amplifier. **Layer:** General (the ladder + cap); the help gate is a design choice.

## 6. Pushing rolls — the two cost models

**The shared rule:** After any roll (failed *or* successful, if more ⚔ would increase effect), you may **push once** — reroll all dice that did not show a 6 (FL also excludes 💀 from the reroll). One push per roll, ever. FL `03-skills.md:59-83`; West `03-rolling-the-bones.md:74-83`.

**The two cost models — the engine's central divergence:**

| | **FL — "Bane self-harm"** | **West — "Faith spend"** |
| --- | --- | --- |
| **Cost trigger** | Pushing is *free* in currency; the cost is in the 💀 you already rolled. | Pushing costs **1 Faith Point** per push. |
| **What you pay** | Each 💀 on a **Base Die** = 1🩸 damage to the rolled attribute. Each 💀 on a **Gear Die** = the gear bonus drops by 1 (degrades toward broken). Skill-Die ones are *inert*. | Faith is spent from a capped pool; **no automatic harm** to attribute or gear from the push itself. |
| **Asymmetry** | Body and gear absorb the cost; the mind is untouched by the rule. | Faith/Willpower absorbs the cost; body/gear untouched unless Trouble says so. |
| **Failure amplifier** | A failed push with ≥3 💀 = "severe setback" (critical wounds, lost opportunities, hostile attention). FL `03-skills.md:97-101`. | A failed push adds **+1 Trouble** on top of whatever Trouble the roll already generated. West `03-rolling-the-bones.md:99`. |

FL `03-skills.md:59-101`; West `03-rolling-the-bones.md:74-83, 90-101`.

**Generic abstraction — "the push":** a single, optional reroll of non-success dice that converts a *latent* cost face into an *active* cost. The **cost model** is the choice:
- **Bane-self-harm** (FL): cost is *endogenous* — baked into the dice you already threw; you pay in body/gear. Produces gritty, attritional, physical pressure.
- **Currency-spend** (West): cost is *exogenous* — paid from a separate pool; you pay in agency-fuel. Produces dramatic, resource-management pressure without mandatory harm.
- **Hybrid** (recommended for new games): a currency cost *plus* a lighter bane or Trouble trigger, so pushing always costs *something* visible but isn't always injurious.

**Layer:** General (the push itself); the cost model is a **core rule choice** — see §11.

## 7. Willpower and Faith

Both games feature a **capped pool that converts risk/failure into future agency.** This is the engine's signature economy.

| | **FL — Willpower Points (WP)** | **West — Faith** |
| --- | --- | --- |
| **Cap** | 10 max. | 10 max. |
| **Starting/refresh** | Earned in play; refreshed from the Stronghold (rest = WP). | **4 per scenario**; resets to 4 at Turn of the Season; may carry within a season. |
| **Primary spend** | Powers **kin talents, profession talents, spells**. | Pays for **pushing** (1/push) and **buying off Trouble** (1:1). |
| **Refuel trigger** | **Damage refuels it:** 1 WP per 💀 on Base Dice when you push — *the act of taking harm generates agency.* | **Action/success refuels it:** 1 Faith on a 3-⚔ un-pushed roll; or by performing rituals/actions (pray, avenge, save a life, rest in a warm bed, etc.). West `03-rolling-the-bones.md:273-296`. |
| **Depletion state** | (no explicit "shaken" state) | **Shaken Faith** at 0: cannot push, cannot gain Faith; restored by a 4-⚔ roll or end-of-adventure. West `03-rolling-the-bones.md:298-307`. |
| **Thematic load** | "Willpower" = the grit to exert a talent. | "Faith" = belief that carries you through; loss-of-faith is a story beat. |

FL `03-skills.md:120-138`; West `03-rolling-the-bones.md:84-88, 258-311`.

**Generic abstraction:** a Willpower-style pool with four design choices — (1) **cap size**, (2) **spend target** (powers / push / trouble-buyoff / all), (3) **refuel trigger** (harm-earned vs action-earned vs success-earned), (4) **depletion penalty** (none vs a "shaken" lockout). FL and West are the two canonical points:
- **Harm-refueled** (FL): creates a virtuous damage loop — getting hurt fuels your comeback, but only if you survive. Favors aggressive, attritional play.
- **Action/success-refueled** (West): decouples agency from harm; rewards in-fiction behavior (rituals, relationships, Big Dream). Favors dramatic, character-driven play.

**Layer:** General (the pool exists); the refuel trigger is a **core rule choice**. The FL **Surge of Willpower** optional rule (convert 1 XP → 1 WP, once/session) is an Optional pressure-relief valve for WP-poor campaigns. FL `03-skills.md:130-134`.

## 8. Opposed and group rolls

**Opposed rolls (both, near-identical):** To beat a foe, roll your ability/skill and get ⚔, *and* get more ⚔ than the adversary — each enemy ⚔ cancels one of yours. Only the attacker may push. Dodging/parrying are *not* opposed rolls (they're defender actions). FL `03-skills.md:198-208`; West `03-rolling-the-bones.md:246-256`.

**Group rolls (both):**
- *Fail-together tasks* (e.g. sneaking): the character with the **lowest** relevant level rolls for the group; others may help (+1 each). One failure = group failure.
- *Succeed-together tasks* (e.g. tracking): the character with the **highest** level rolls; others help.
- *Everyone-must-personally-succeed tasks* (e.g. a group climb): everyone rolls; surplus ⚔ from one PC can cover a teammate who rolled 0 ⚔, if the fiction supports it.
FL `03-skills.md:144-150`; West `03-rolling-the-bones.md:230-240`. FL adds explicit group-stealth and group-scouting variants with tally thresholds. FL `03-skills.md:328-329, 358-359`.

**Only-one-chance rule (both):** once a roll (and any push) is resolved, the *same approach* cannot be retried for the same goal; something material must change (method, position, helper, tools, time pressure). FL `03-skills.md:140-142`; West `03-rolling-the-bones.md:242-244`.

**Generic abstraction:** opposed rolls resolve symmetric contests; group rolls distribute party labor via a highest/lowest selector that encodes the *kind* of task (sneak = weakest-link; track = strongest-link; climb = individual-with-cover). The "one chance" rule is what makes the push decision meaningful — you can't just reroll for free. **Layer:** General throughout.

## 9. Artifact / legendary dice

**FL only — artifact dice:** Master-crafted/magic items grant a **D8 (Mighty), D10 (Epic), or D12 (Legendary)** in addition to normal Gear Dice. Result **6+ = ⚔**, scaled: a D12 can yield up to 4 ⚔ on a 12. Artifact dice are **never degraded by wear**. FL `03-skills.md:232-252`. **Pride** is a parallel once-per-session *attribute-like* die (D8/D10/D12) added to a failed protective roll; it grows when unused and shrinks when it fails. FL `03-skills.md:254-258`.

**West:** no equivalent in the core pool. The nearest analogue is Faith (a player-side pressure-relief pool, not a success-scaling die).

**Generic abstraction:** an optional **legendary die** rule for high-tier outcomes — a single larger die (D8/D10/D12) read as 6+ = ⚔ with scaled multi-successes, immune to the normal degradation economy. This is the engine's "legendary gear" / "heroic moment" choice. FL artifact dice = legendary gear; FL Pride = the character's heroic-moment die. **Layer:** Optional (genre-dependent — omit for grounded/low-power games).

## 10. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Push cost model** | Bane self-harm (body/gear) | Faith spend (currency) | Gritty attrition vs resource drama | FL-style for survival/horror; West-style for dramatic/character-driven |
| **Cost face trigger** | 💀 on dice, always on push | 1s, only on Risky/Desperate fails | Endogenous vs frame-gated | Use banes when harm should feel inevitable; use Trouble when harm should feel *chosen* |
| **Failure amplifier** | Failed push + ≥3💀 = severe setback | Failed push = +1 Trouble | Mechanical severity vs narrative severity | Match the genre's relationship to failure |
| **Willpower/Faith refuel** | Harm-earned (1 WP/💀 on Base) | Action/success-earned | Virtuous damage loop vs behavior-reward loop | Harm-refuel for attritional games; action-refuel for dramatic games |
| **Willpower/Faith starting model** | Earned in play + stronghold rest | 4/scenario + reset at season | Slow-burn vs predictable budget | Use refresh-per-arc for paced drama; earned for sandbox grit |
| **Willpower/Faith depletion** | (no lockout) | Shaken Faith at 0 | No floor vs a despair beat | Add a lockout if you want a "hitting zero" story beat |
| **Modification target** | Skill Dice only (+ negative dice) | Unified pool | Colored precision vs simplicity | FL-style if you want gear/attribute/skill cleanly separable; West-style for speed |
| **Help gating** | Lowest Empathy caps bonus | Each helper needs ≥1 rank | Social-trust limit vs competence floor | Empathy-gate for relationship-heavy games; rank-gate for competence-focused |
| **Success ladder default** | Threshold model (1⚔ default, raise to 2/3) | Grade model (0/1/2/3+ read) | GM-sets-bar vs roll-reads-grade | Hybrid: read the grade, allow optional threshold-raising |
| **Legendary die** | Artifact dice + Pride | None | High-tier escalation vs flat power | Include for fantasy/pulp; omit for grounded/historical |
| **Failure-pressure layer** | Banes (mechanical, on dice) | Trouble tables (narrative, by exposure) | Mechanical tax vs narrative tax | Both work; Trouble + a bane-free pool is the lighter option |

## 11. Rule choices and instantiation recipe

Each rule choice has FL and West as two calibrated points. To build a new game, set each choice.

1. **Push-cost model** — bane-self-harm / currency-spend / hybrid. *(Affects tone: attritional vs dramatic.)*
2. **Cost-face trigger** — always-on-push / exposure-gated. *(Affects whether harm feels inevitable or chosen.)*
3. **Willpower/Faith refuel** — harm-earned / action-earned / success-earned / hybrid. *(Affects the virtuous loop.)*
4. **Willpower/Faith cap + refresh** — size; per-scenario reset vs earned-only. *(Affects pacing predictability.)*
5. **Willpower/Faith depletion** — none / shaken-lockout. *(Adds a despair beat if wanted.)*
6. **Modification target** — colored (skill-only + negatives) / unified. *(Precision vs speed.)*
7. **Help gating** — social-stat cap / rank floor / both / none. *(What "helping" requires.)*
8. **Success ladder** — grade-read / threshold-raise / both. *(How outcomes scale.)*
9. **Legendary die** — on/off + artifact + heroic-moment die. *(Power ceiling.)*
10. **Failure-pressure layer** — banes / Trouble tables / hybrid / none. *(How failure taxes.)*

**Instantiation recipe (any genre):**
1. Decide the push-cost model — this single choice does more to set tone than any other.
2. Choose the failure-pressure layer to be *consistent* with the push cost (e.g. bane-self-harm pairs naturally with banes; Faith-spend pairs with Trouble).
3. Pick the Willpower/Faith refuel to create the virtuous loop you want.
4. Set the modification model and help gate to your table's complexity tolerance.
5. Decide the success ladder and the legendary tier based on the genre's power ceiling.
6. Validate the whole against the math (see `13-balance-and-synergy.md` §3): default pool size, push rate, expected success, breakpoint.

## 12. Design intent

The core loop is engineered to make **every roll a decision** and **every failure a resource pressure.** Specifically:

- **Push-once, pay-a-cost** turns "I failed" from a dead end into "do I accept this, or do I double down and pay?" — the engine's central dramatic beat.
- **The latent cost face** (💀 / 1) means the *cost was already on the table* when you decided to push; you're not being punished, you're *cashing the check you wrote by rolling risky dice*.
- **Willpower refuels from risk/failure** so that getting hurt or struggling is never *just* loss — it also stocks your comeback. This is what keeps attritional games from becoming death spirals.
- **The "one chance" rule** makes the push decision load-bearing: you can't retry for free, so accepting a failure has weight.
- **Don't roll too often** (both books, emphatic): the engine only works when rolls are *dramatic peaks*, because pushing/damage/WP generation only matters when stakes are real. FL `03-skills.md:55-57`; West `03-rolling-the-bones.md:70-72`. Rolling for trivial tasks floods the economy and flattens the drama.

The divergence between FL and West is not accidental — it is the engine's proof that **the same spine produces opposite tones by swapping the cost model.** FL's bane-self-harm makes a game where the *body* is the currency; West's Faith-spend makes a game where *belief* is the currency. A new genre's job is to find *its* currency and wire the cost model to it.
