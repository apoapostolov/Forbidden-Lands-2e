<!-- markdownlint-disable MD013 MD024 -->

# Player Psychology and Felt Experience

> This is the **experiential** evaluative layer — the complement to `10`'s designer-side Warning Signs and `13`'s design-side playtest checks. Those files catch rules that are *broken* (internally inconsistent, abusable, ambiguous, GM-punishing). This file catches rules that are *sound on paper but feel awful* — balanced but boring, fair but frustrating, evocative but exhausting. Read it alongside `13 §7` (table-behavior lenses) and `18 §5` (composition checklist); it supplies the *why* behind their *what*.

## Contents

1. Source provenance
2. Abstraction target
3. Scope boundary — what this file does NOT duplicate
4. Felt-experience failure modes (the player-side complement)
5. The cognitive layer — why rules feel the way they do
6. The abstraction-vs-authenticity choice
7. The felt-experience review protocol (integrating 10 + 13 + this file)
8. Design intent

## Source provenance

This file is the experiential evaluative layer's sole deliverable, scoped to avoid duplication. It is the *psychology* consequence of `10` (philosophy) and `13` (balance). The cognitive principles are not sourced from the two corebooks (which are silent on player psychology) — they are standard, well-established findings (loss aversion, the flow channel, perceived-randomness gaps) restated in the engine's vocabulary and tied to its specific rules. Where a principle explains a lens already in `13 §7`, the cross-link is explicit and the lens is not reproduced.

## Abstraction target

`10 §10` answers *"is this rule well made?"* `13 §8` answers *"is this rule mathematically sound and abuse-free?"* Neither answers the question a player actually asks at the table: ***"does this feel good?"*** A rule can pass both prior checks and still produce a bad experience — a fair roll that *feels* rigged, a meaningful choice that *feels* like guessing, an authentic procedure that *feels* like homework.

This file delivers four things, each genuinely missing from the prior evaluative layers:

1. **Felt-experience failure modes** — the player-side complement to `10`'s designer-side warning signs. Where `10` catches rule bloat and silent invalidation, this catches *false choice, decision fatigue, swinginess-as-unfairness, agency collapse,* and the user's "too X" list (too overcomplicated / random / unfair / confusing / abstract).
2. **The cognitive layer** — the *why* behind `13 §7.2` (perceived balance) and `13 §7.6` (player agency). Loss aversion, the flow channel, perceived-vs-actual randomness, tension/payoff rhythm. Brief, actionable, tied to engine rules.
3. **The abstraction-vs-authenticity choice** as a managed decision — when abstraction kills genre feel vs when authenticity becomes simulationist bloat. Touched in `10 §8` (the authenticity lens) but not as a *choice to set*.
4. **A felt-experience review protocol** that *orchestrates* `10`'s warning signs + `13`'s review path + this file's psychology checks into a single pass, so a reviewer runs one integrated review, not three disconnected ones.

## 3. Scope boundary — what this file does NOT duplicate

To keep this file lean (and honor the no-duplication rule), this file **does not reproduce**:

- **`10 §10`'s seven Warning Signs** (rule bloat, silent invalidation, false realism, vague enforcement, misleading survivability, setting-laden language, sibling-skill duplication). Those are *craft-side* failures. This file's failure modes are *player-side experiential* failures — a different axis. A rule can pass every craft check and still feel awful.
- **`13 §7`'s nine table-behavior lenses.** Two of them (7.2 perceived balance, 7.6 player agency) touch psychology as *scoring rubrics*. This file supplies the *cognitive explanation* for why a rule scores poorly on those lenses — it does not re-score them.
- **`18 §5`'s composition checklist** for reinvented rules. That checklist runs *before* shipping; this file's protocol runs *on* the shipped or proposed rule.

**The test for whether something belongs here:** *is it about how the rule feels to a player, independent of whether it is mathematically fair or well made?* If yes, it belongs here. If it's about math or integration, it belongs in `13` or `10`.

## 4. Felt-experience failure modes (the player-side complement)

These are the experiential failure modes `10` and `13` do not name. Each is the player-side mirror of a craft concern, but distinct. A rule that triggers one is not *broken* — it is *un-fun*, which is often worse.

### FE1 — False choice (the illusion of agency)

**The failure:** the rule presents a decision, but one option is so obviously dominant (or so obviously disastrous) that there is no real choice. The player goes through the motions of deciding.

**Why it feels bad:** the brain detects the manufactured agency. The rule *looks* meaningful but plays on rails. This is the experiential cousin of `13 §5.5` (action-budget abuse) and `10 (b)` (silent invalidation) — but here the rule isn't *abusable*; it's just *empty*.

**Detection:** "Is there any situation where a reasonable player picks the subordinate option?" If no, the choice is false. Fix by making the options genuinely situational (cost-varied, risk-varied, fiction-gated) or by collapsing the choice into a single procedure.

**Engine tie-in:** the push decision (P1) is the engine's *good* example — pushing is sometimes right and sometimes wrong, depending on stakes, pool, and remaining 💀. The FL "Levels of Effort" threshold (raise to 2/3⚔) is a *false-choice* risk: players always raise when the payoff is worth it and never when it isn't, unless the GM varies the risk opaquely. Hybrid success ladders (`00 §4`) mitigate this.

### FE2 — Decision fatigue (too many micro-choices)

**The failure:** the rule demands a decision every Round / every roll / every Quarter Day, and the decisions are individually small. Over a session, the cumulative cognitive load exceeds the payoff.

**Why it feels bad:** the player's working memory saturates; later decisions become default-selections rather than judgments. The rule *feels* like a tax even if each instance is "meaningful."

**Detection:** count the decisions the rule adds per session. If >1 per Round or >3 per Quarter Day, and each decision's stakes are small, it's fatigue risk. Consolidate, automate, or move to a slower turn.

**Engine tie-in:** the activity menu (P6) is deliberately once-per-time-block to avoid this — it's the engine's own fatigue-prevention pattern. A reinvented menu that fires every Round is probably a mistake.

### FE3 — Swinginess perceived as unfairness

**The failure:** the rule produces high-variance outcomes (a D66 table with catastrophic rows, a push that can crit or fail). Mathematically fair; *feels* rigged when the bad row hits, because the player's loss-aversion system weights the loss at ~2× the equal-magnitude gain (`13 §3` confirms the math; this is the *experience* of it).

**Why it feels bad:** humans are not probability calibrators. A 1-in-36 crit-fail *feels* like a betrayal, not a fair roll, because we remember the hit and forget the 35 non-hits.

**Detection:** does the rule's worst case arrive without warning and without counterplay? If both, the swing will *feel* unfair regardless of odds. Fix with (a) telegraphing (the GM foreshadows), (b) counterplay (the player can mitigate after seeing the danger), or (c) a "spend to reroll" valve (the engine's push/P10 inner fire exists precisely for this).

**Engine tie-in:** this is *why* P1 (push) and P10 (inner fire) exist — they are the engine's swing-absorption layer. A reinvented high-variance rule *without* a push/inner-fire counterpart is an FE3 bug.

### FE4 — Agency collapse (the rule removes you from play)

**The failure:** the rule's failure state takes the character (or player) out of meaningful participation — stunned for D6 Rounds, fully controlled, perma-Broken without recovery, killed without counterplay.

**Why it feels bad:** the player sits at the table doing nothing. This overlaps `13 §7.6` (player agency) and `13 §7.7` (catastrophic-outcome playability) but is distinct: those score *whether the rule allows agency*; this names *the felt experience of losing it*, which is corrosive in proportion to its duration.

**Detection:** what is the *maximum duration* a player can be removed from meaningful play by this rule? If >1 Round without a recovery action, or >1 scene without a recovery path, it's FE4.

**Engine tie-in:** FL's "Broken but healable" and West's "Death Roll the dying player makes" are both FE4 mitigations — they keep the player *doing something.* A rule that removes a player for a full session is an FE4 failure even if it's "realistic."

### FE5 — The "too X" family (the user's list)

These are the generic felt-experience failures, each a different way a rule can work as written and still feel bad:

- **Too overcomplicated** — the rule requires holding >3 interacting pieces in head to resolve (cf. `13 §7.3` complexity, but here it's the *felt* cognitive load, not a scoring rubric). Fix: collapse to one decision; push detail into a reference.
- **Too random** — outcomes swing wider than the player's input matters. The player feels their choices don't steer the fiction. (Overlaps FE3; the distinction is variance-vs-agency, not variance-vs-fairness.) Fix: make player skill/choices widen or narrow the variance band, not eliminate it.
- **Too unfair** — the rule's costs fall asymmetrically on one player, or its benefits accrue to whoever triggers it first. Detectable by asking "would the player on the losing end of this call it fair?" Fix: symmetric cost/benefit or a compensating valve.
- **Too confusing** — two reasonable readings produce different outcomes (`13 §7.4` ambiguity risk — again, the *felt* version). Fix: state replace-vs-stack, per-Round-vs-per-Shift, resisted-or-not, explicitly.
- **Too abstract** — see §6, the abstraction-authenticity choice.

## 5. The cognitive layer — why rules feel the way they do

This section supplies the *explanatory* layer beneath `13 §7.2` (perceived balance) and `13 §7.6` (player agency). The lenses score; this explains the scores.

### C1 — Loss aversion (losses weigh ~2× gains)

Players feel a loss roughly twice as intensely as an equal gain. Consequences for the engine:

- A push that costs 1 WP *feels* worse than a successful push that gains an effect *feels* good — even at equal expected value. The engine's harm-refuel loop (P2, FL) works *because* it converts the felt loss (damage) into a compensating gain (WP), rebalancing the felt ledger.
- A rule whose failure state *takes something away* (attributes, gear, WP) will *feel* more punitive than its odds justify. Mitigate with partial recovery, "fail-forward" fiction, or a compensating micro-gain.
- **Design rule:** when a rule imposes a loss, ask what the player *gains* in felt terms, not just EV. FL's "pushing earns WP even on a fail" is not a math balance — it is a *psychology* balance.

### C2 — Perceived vs actual randomness

Humans detect patterns in random sequences and read clumps as bias. A 1-in-6 banes chance will, over a session, produce streaks that *feel* like the dice are rigged. Consequences:

- Avoid rules whose variance is *invisible* until it spikes. Telegraph variance (the GM names the risk before the roll), or give the player a *post-roll* valve (push, inner fire, Faith-buyoff — the engine's existing tools).
- The engine's *good* design here is West's **Trouble exposure declaration** (Safe/Risky/Desperate, set *before* the roll): it makes the variance *chosen,* which reframes the resulting bad outcome as the player's bet, not the dice's betrayal.
- **Design rule:** any rule with >1 catastrophic row on a D66 needs either telegraphing, counterplay, or a buyoff valve. Raw variance without a valve is FE3.

### C3 — The flow channel (challenge vs skill)

Players enter "flow" (engagement, time distortion) when challenge roughly matches skill. Too-easy rules bore; too-hard rules frustrate. The engine's dice-pool is a self-tuning flow engine:

- A larger pool (more skill) raises expected success (the FL table, `13 §3.3`), so skilled characters *reliably* flow on easy tasks — but the GM raises the threshold (Levels of Effort) to re-enter the channel.
- The push (P1) is a *flow-recovery* rule: when a roll falls outside the channel (a fail), the push offers a second engagement rather than a dead stop.
- **Design rule:** a rule that removes the push (or its equivalent recovery valve) collapses the flow channel — failures become dead stops rather than re-engagements. `13 §5.6` (push-cost avoidance) names this as an abuse surface; it is *also* a flow-channel failure.

### C4 — Tension and payoff rhythm

A session has a shape: rising tension, a climax, a release. Rules that ignore this shape *feel* wrong even when individually fine:

- Too many rolls in the rising phase dilutes tension ("don't roll too often," `00`). Too few in the climax starves it.
- A payoff schedule that is too slow (XP drip, gear that never improves) feels like grinding. Too fast trivializes advancement. The engine's converged XP budget (`02 §3`: 1–3/session + milestones) is the empirical sweet spot.
- **Design rule:** map the rule to the session's tension curve. Does it fire at the rising phase (good — builds pressure), the climax (good — resolves it), or the release (often bad — extends the session past its natural end)? Trouble tables (P4) fire at rising/climax; stronghold events (P7 beat 4) fire at the *downtime* between sessions by design.

### C5 — The agency ledger

Players maintain a running (often unconscious) sense of "did my choices matter this session?" A rule that resolves a major outcome *independent* of player choice — a pure-random faction event that wipes the party's work, a cutscene-style scripted defeat — debits the ledger. A rule that lets player choices *steer* the outcome credits it.

- **Design rule:** any rule with large stakes must connect its outcome to at least one prior player choice. FL's "encounter table modified by Reputation and terrain" (P14) credits the ledger — the party's prior choices shaped the odds. A version that rolled without modifiers would feel arbitrary by comparison.

## 6. The abstraction-vs-authenticity choice

`10 §8` names the authenticity lens; this section treats it as a *choice to set deliberately*, because it is the most common source of "too abstract" and "too overcomplicated" failures (FE5).

**The two failure poles:**

- **Too abstract** — the rule reduces a rich fiction to a number with no handle. "Take 2 Stress" feels like a spreadsheet; "you suffer 2 Hurts" feels like a wound. The fix is *naming* (`01 §4`: named damage types are free genre-loading). The deepest form of this failure is a rule whose terms are so generic the table cannot picture the fiction.
- **Too authentic** (simulationist bloat) — the rule models so much detail that play stops while the table consults the model. The FL HEAT/TEMP weather system (felt-vs-actual temperature, clothes modifiers, seasonal adjustment) is authentic; a rule that added windchill charts, humidity, and altitude sickness on top would be bloat. The fix is *deciding what detail serves a decision* and cutting the rest.

**The decision rule (the choice's setting procedure):**

1. **What decision does this detail serve?** If none, it is decoration or bloat. Cut it. (`10 §10c` false realism is the craft-side version of this test.)
2. **What consequence does the detail produce?** If the consequence is identical to a simpler model, the detail is bloat. (E.g. if a D6 weather roll and a D66 weather roll produce the same play, the D66 is bloat.)
3. **Can a player picture the fiction from the rule's terms?** If not, it is too abstract — add a name, a sensory handle, or a fictional trigger.
4. **Does the detail block or enable a meaningful choice?** Detail that *enables* a choice (cover ratings let you choose where to stand) is authenticity that earns its cost; detail that merely *describes* (cover ratings that modify nothing) is decoration.

**The calibration (FL and West as the two points):**

| Pole | FL calibration | West calibration | What it produces |
| --- | --- | --- | --- |
| **Simulationist** (max authenticity) | Hex-crawl + HEAT/TEMP + typed crit families + Resource Dice | The 1870s documentary ledger (prices, distances, weights) | The world simulates itself; the dice are the world. High fidelity, high bookkeeping. |
| **Dramatist** (min necessary machinery) | (FL leans simulationist) | Pointcrawl + prose weather-killers + Trouble | The GM dramatizes the world; the dice dramatize the scene. Low bookkeeping, high GM-authority. |

**The default for a new game:** start dramatist, add close-detail procedure *only where it enables a decision.* Every added rule pattern must answer "what choice does this make sharper?" or it is bloat. This is `10 §8`'s sniff-test restated as a *budgeting* rule: abstraction is the default; authenticity is an expense you justify per line item.

## 7. The felt-experience review protocol (integrating 10 + 13 + this file)

This is the file's integrating artifact. It orchestrates the three evaluative layers into a single review pass, so a proposed rule is checked for *design soundness* (`10`), *mathematical soundness* (`13`), and *experiential soundness* (this file) in one sequence rather than three disconnected audits.

**Run these stages in order. Each stage can reject; later stages only run if earlier ones pass.**

### Stage A — Craft review (`10 §10` Warning Signs)
Run the rule against the seven warning signs (rule bloat, silent invalidation, false realism, vague enforcement, misleading survivability, setting-laden language, sibling-skill duplication). **Reject** if any sign triggers unmanaged. *Catches: rules that shouldn't exist or are broken where they join the rest of the game.*

### Stage B — Mathematical review (`13 §8` Review Path)
Run intent → math → abuse → synergy. **Reject** if the rule fails the math, introduces an abuse (§5 families), or breaks synergy (§6 protocol). *Catches: rules that are abusable or numerically unsound.*

### Stage C — Felt-experience review (this file, §4 + §5)
Run the rule against FE1–FE5, then read it through C1–C5. **Reject (or revise)** if the rule triggers a felt-experience failure *that the craft and math reviews did not catch.* Specifically ask:
- *False choice?* Is there a dominant option?
- *Decision fatigue?* How many times per session does this fire, and how small is each instance?
- *Swinginess-as-unfairness?* Is there telegraphing / counterplay / a buyoff valve for the worst case?
- *Agency collapse?* What is the maximum duration of removal from meaningful play?
- *Too X?* (overcomplicated / random / unfair / confusing / abstract)
- *Loss-aversion check (C1)?* What does the player *gain* in felt terms when they lose?
- *Flow channel (C3)?* Does the rule preserve a recovery/re-engagement valve, or turn failures into dead stops?
- *Tension rhythm (C4)?* Where in the session arc does this fire?
- *Agency ledger (C5)?* Does the outcome connect to a prior player choice?

*Catches: rules that are sound on paper but feel awful — the gap `10` and `13` leave open.*

### Stage D — Abstraction-authenticity setting (this file, §6)
Set the choice: is each detail in the rule earning its cost (enabling a decision / producing a distinct consequence / giving a fictional handle)? **Cut** decoration and bloat; **add names** where the rule is too abstract.

### Stage E — Verdict
One of: **Ship** (passes A–D) / **Revise** (fails one stage, fixable in-place) / **Hold** (fails a stage, needs rethink) / **Reject** (fails structurally — wrong problem, wrong layer, wrong engine fit). Map to `13 §7.9`'s verdict classes.

**The protocol's guarantee:** a rule that passes A–D is well made, mathematically sound, abuse-free, *and* experientially good. That four-fold pass is what "balanced" actually means at the table — and no single prior file delivered it.

## 8. Design intent

This file exists because the engine's two prior evaluative layers (`10` philosophy, `13` balance) are craft-facing. They answer "is this rule well-built?" A rule can be well-built and still produce a bad session — because sessions are had by *players*, whose experience is governed by cognition (loss aversion, flow, perceived randomness) and rhythm (tension curves, agency ledgers) that the craft layers do not model.

This experiential layer was scoped to close exactly this gap and nothing else. The four deliverables — felt-experience failure modes, the cognitive layer, the abstraction-authenticity choice, and the integrating protocol — are deliberately complementary, not duplicative: every failure mode (FE1–FE5) is distinct from `10`'s warning signs; every cognitive principle (C1–C5) explains a lens in `13 §7` without re-scoring it; the abstraction-authenticity choice turns `10 §8`'s sniff-test into a budgeting procedure; and the review protocol *orchestrates* rather than replaces the prior review paths.

With this file, the skill's evaluative axis is complete: a rule can now be judged for **design soundness** (`10`), **mathematical soundness** (`13`), and **experiential soundness** (this file), in a single integrated pass. Together with the generative axis (`16`–`18`) and the understanding axis (`00`–`15`), this completes the skill's design loop: **understand → invent → judge.** The loop is closed.
