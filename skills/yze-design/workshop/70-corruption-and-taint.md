<!-- markdownlint-disable MD013 MD024 -->

# Corruption & Taint — The Doom Spiral

> **STATUS: WORKSHOP MODULE.** A power-at-a-cost subsystem: using forbidden power *refuels* you in the short term (it is tempting — you gain metacurrency, potency, or escape from a bad roll) but climbs a **doom ladder** that eventually destroys, transforms, or un-mans you. *Core is generic; the worked example (witch-hunting dark fantasy) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic mechanism
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — Witch-hunting dark fantasy

## 1. Origin — how this was built

- **Source primitives:** **P5** (resource die — Corruption as a die that *grows*, steps *up*, the inverse of normal depletion), **P4** (typed D66 — corruption milestone tables: what befalls you at each tier), **P2** (capped metacurrency — corruption *refuels* your pool; that is the temptation), **P10** (protected dial — the Corruption die as an inverted Pride, growing when *used* not when *avoided*).
- **Reinvention operator:** **Inversion + Fusion** (Operators 2 + 4 from `18 §4`). Invert P5 (the die grows instead of depletes) and P10 (the die escalates when the forbidden power is *used*, the exact "Doom" pattern sketched in `18 §6` Worked 4). Fuse the inverted die with P4 for the milestone/consequence tables and with P2 for the temptation that drives the climb. This is the close cousin of `18`'s Doom protected dial, extended into a full five-tier spiral.
- **Target psychology:** **Power-at-a-cost / doom** (`17`, the inverted-P10 cell). Produces *characters who are slowly becoming what they fight.* The drama is the slide, not the single catastrophe — every use is a small betrayal of the character's stated self.
- **Problem solved:** the "cost of power" in many games is either a flat penalty (boring — players just avoid the power) or a single catastrophic mishap (swingy — no slow-burn dread). This module makes the cost a *climb*: a visible ladder with named rungs, where the temptation is real (power now) and the ruin is gradual, legible, and (crucially) *choosable*. It gives the power layer (`05`) the cost its forbidden options require.

## 2. The generic mechanism

### The Corruption die (inverted P5 / P10)

Each PC who can access forbidden power has a **Corruption die**. Unlike a normal resource die (which *depletes* — steps down on use), the Corruption die *grows* — it steps **up** as you stain yourself. The ladder is five rungs:

| Tier | Die | Name (generic) |
| --- | --- | --- |
| 0 | (none) | **Clean** |
| 1 | D6 | **Marked** |
| 2 | D8 | **Tainted** |
| 3 | D10 | **Warped** |
| 4 | D12 | **Lost** |
| 5 | — | **Gone** (transformation / removal from play) |

### The temptation (P2 fusion)

When a PC uses forbidden power and **gains a benefit from it** — refuels metacurrency, succeeds on a dark-casting roll, escapes a consequence via the forbidden source — they **roll the Corruption die**:

- On a **1–2**, nothing happens *this time* (the power came cheap).
- On a **3+**, the die **steps up one tier** (D6→D8→D10→D12).
- At **D12**, the next 3+ is a **milestone** — the character advances a tier on the doom ladder and rolls on the Corruption Milestone table (P4). At tier 5 the character is **Lost**: transformed, un-manned, or removed from play as the genre dictates.

This is the engine's push-and-pay inverted: where the push costs to convert a fail into a success, here the forbidden power *pays you* to convert a stain into a habit. The math inherits P5's proven step-die curve; only the polarity is reversed.

### Why inversion changes the math (a warning)

A normal resource die (P5) steps *down* — you have a long way to fall (D12→D6) and depletion is the slow crisis. The Corruption die steps *up* — and there are only four steps to the top (D6→D8→D10→D12→Lost). This is `18 §7`'s "inverting without re-balancing" anti-pattern in miniature: an inverted mechanic hits its climax *faster* than its parent hits empty. The cheapest-use range (1–2 = no step) and the benefit-only trigger are the brakes that keep the spiral at campaign cadence. Tighten either and the spiral accelerates dramatically — see Dials and Failure modes.

### The milestones (P4)

Each tier transition rolls on a **typed D66 Corruption Milestone table**. As with FL's crit families, the table is split into **families** by what the corruption *is* in your genre (physical / mental / social / spiritual / alien), and each entry carries: an *immediate effect* (the visible change), a *long-term effect* (a lasting tag — `08 §6`), and an *atonement cost* (see Dials). The `65`/`66` climax entries at each tier are the un-manning events: a permanent transformation, a loved one marked, a piece of your self eaten.

The point of the table — inherited from P4 — is that corruption is **specific and memorable**: "your shadow moves a half-second late" is a story beat; "−1 Wits" is a number. Tier 5's climax entries are how the character *leaves* play: become the monster, ascend as something inhuman, or simply break beyond repair. The families matter because the *kind* of ruin is the genre's signature — a body-horror game wants Flesh-family milestones; a psychic game wants Mind-family; a pact game wants Soul-family. One master table flattens this; the family set preserves it.

### Engine fit (why this isn't a parallel system)

A common failure of "corruption" subsystems is that they bolt on a parallel tracker — a separate tally, a separate roll, a separate economy — that lives beside the engine without touching it (`10 §10` subsystem inflation). This module avoids that by routing through primitives the engine already runs:

- The Corruption die **is** P5/P10 — the same step-die logic as food (FL) and Pride (FL), only inverted. No new die type, no new roll procedure.
- The temptation **is** P2 — it refuels the same WP/Faith pool the rest of the game uses. The forbidden power enters the engine's own economy, not a side-economy.
- The milestones **are** P4 — the same typed-D66 architecture as crits and mishaps. No new table grammar.
- The tier tags **are** P8 — they land in the same feature-grammar as weapons and talents.

The result is a subsystem that *feels* like the core loop because it *is* the core loop, inverted and fused — which is the engine's own trick for producing novelty (`12 §12`, `16 §6`). A designer installing this needs no new dice, no new currency, no new resolution mechanic — only the inversion (die grows) and the fusion (refuel + milestone table).

### The tells (corruption as public fiction)

A Corruption die on a character sheet is necessary but not sufficient — the doom ladder must also be *legible in the fiction* so the table (and the world) can react. Each tier carries a **tell**: a visible, narratable sign that grows more pronounced as the die steps up. Tier 1's tell is deniable (a chill, a bad dream); tier 4's is unmistakable (the shadow moves on its own). Tells matter for three reasons:

1. **They make the spiral shared drama.** Other PCs can see the stained character changing and must decide whether to intervene — confront, report, aid the atonement, or look away. This converts a solo tracker into party fiction.
2. **They create social consequence.** NPCs react to tells — a witch-hunter's Order may investigate its own; a village may shun or fear the tainted; a patron may withdraw support. The corruption thus ripples into the social and faction layers.
3. **They make tier 5 a visible approach, not a surprise.** A tier-4 character *looks* nearly lost; no one at the table can claim the end came without warning. This is the antidote to the "un-manning cliff" failure mode (§6).

Tells are fiction, not mechanics — they cost no dice and add no rolls. They are the GM's and table's job to voice. A milestone table entry can specify a tell (the Flesh-family *UNSETTLING* tag carries one), but the tier itself should always carry *some* narratable sign by default.

## 3. The pressure loop

- **Pressure:** the forbidden power is *useful* — it refuels your metacurrency (P2), boosts a roll, or buys off a consequence you couldn't otherwise escape. The pressure is the *need* the power answers (a fight going badly, a resource depleted, a failure that costs everything). Crucially, the need must be *real and recurring* — if legitimate options are always sufficient, the spiral never opens (see Failure modes).
- **Decision:** *do I use the forbidden power now — refueling myself, winning this moment — and roll the Corruption die? Or do I pay the legitimate cost (harm, retreat, accept the failure) and stay clean?* This is the engine's signature push-and-pay, flipped: the push *pays you*, the cost comes later. The deferral is the trap — the cost is probabilistic and future, the benefit is certain and now.
- **Consequence:** the Corruption die may step up; at milestones, a permanent tag lands; the character inches up the doom ladder. Every tier makes the *next* temptation harder to resist for two reasons: (a) the character has more sunk cost invested in the forbidden power, and (b) the higher die *pays more* on a refuel — a D12 casting that refuels 12 WP is far harder to foreswear than a D6 refueling 6. The spiral is self-reinforcing by construction.
- **State change:** the character's standing on the doom ladder changes — a visible, fiction-loaded state, not a hidden tally. Each tier also adds a *tell* (a fiction tag others can notice), so the party and the world begin to react to the stained character. At tier 5, the character leaves play.
- **Loop shape:** **need → yield (refuel) → stain → milestone → climb.** Runs at casting-cadence (faster than an org lifecycle; slower than a single roll). The spiral is *slow* by design — see Failure modes for the pacing trap. The loop closes only via atonement (stepping back down) or abandonment (tier 5).

## 4. Dials

| Dial | Setting A | Setting B | Psychology |
| --- | --- | --- | --- |
| **Die ladder** | D6→D8→D10→D12 (5 tiers) | D6→D8→D10 (4 tiers, tighter) | Slow burn vs fast ruin |
| **Step-up trigger** | 3+ on the Corruption die | 4+ (rarer) | Stains often vs stains sting |
| **Cheapest-use range** | 1–2 = no step (power came cheap) | Always steps (no cheap outs) | Forgiving vs inexorable |
| **What triggers a roll** | Only *gaining a benefit* from forbidden power | *Any* use, including failed castings | Temptation-driven vs contact-driven |
| **The temptation (P2)** | Forbidden use refuels metacurrency (WP/Faith) by the die's face value | Forbidden use grants +1 die to the roll or a free push | Fuel-loop vs peak-power |
| **Tier effects** | Cosmetic at T1, mechanical tags at T2–3, climax at T4–5 | Mechanical from T1 (sterner) | Slow dread vs immediate bite |
| **Milestone table families** | 3–5 typed families (physical/mental/social/spiritual/alien) | 1 master table | Rich flavor vs simple |
| **Atonement (step down)** | A **quest** or ritual steps the die down one tier | Cannot step down — only forward | Redeemable vs one-way |
| **Atonement availability** | Always available if you can secure the quest | Once per tier, GM-gated | Hopeful vs tragic |
| **Tier 5 resolution** | Character Lost (becomes NPC / monster / departs) | Player may sacrifice the power source to reset to T3 | Hard floor vs costly reprieve |
| **Corruption visibility** | Die shown on sheet; tier is public fiction | Hidden tracker revealed only at milestones | Tension-on-display vs slow reveal |

**Calibration guidance:** start with the 5-tier ladder (D6→D12), 3+ step trigger, 1–2 cheapest-use, benefit-only triggers, metacurrency refuel temptation, cosmetic-then-mechanical tiers, 3–5 milestone families, **quest-based atonement** (the redeemable dial). This is the classic doom spiral with a rope ladder back. Reserve the one-way (irredeemable) dial for grimdark genres where the slide *is* the tragedy.

## 5. Integration points

- **Hooks into the power layer (`05`):** this is the **cost the power layer needs.** Any forbidden spell, pact, alien implant, or psychic overchannel in `05` routes its cost through this subsystem instead of (or in addition to) the standard mana/mishap cost. The power layer defines *what counts as forbidden*; this module defines *what using it costs over time.* Without this, forbidden options are either free (broken) or flat-penalized (avoided).
- **Hooks into harm (`04`):** the Corruption die is a **parallel harm track.** Where `04` tracks wounds to the body, this tracks wounds to the *self.* A Corruption milestone can also deal a real condition (a Warped-tier mental corruption may impose a permanent phobia tag) — the two tracks intersect at the fiction but do not share a pool.
- **Hooks into metacurrency (`00 §7`):** the temptation fuse. Forbidden use refuels WP/Faith (P2). This is what makes the spiral *tempting* rather than punishing — the player feels the power working, *now*, and the cost is deferred and probabilistic. Wire the refuel amount to the Corruption die's face so the *riskier* (higher) die also *pays more* — a self-reinforcing trap.
- **Hooks into talents/identity (`01 §5`, `08 §6`):** Corruption milestones land **tags** (P8) on the character — permanent features (a tell, a weakness, a forbidden knack). These interact with the talent/feature grammar already in the game. At high tiers, corruption tags can *replace* benign talents (the character's identity is being overwritten).
- **Requires:** a defined list of what counts as *forbidden* in the genre; a Corruption die per qualifying PC; the milestone table(s); an atonement rule if redemption is in scope.
- **Replaces / extends:** any flat "corruption point" tally — replaces it with a step-die that inherits P5's proven curve and P10's escalation logic.
- **Cross-refs:** `05 §7` (magic mishaps — a sibling one-shot cost; this is the *chronic* cost), `04 §5` (typed D66, here as Corruption Milestones), `18 §6` Worked 4 (the Doom dial this extends), `16` P5/P10/P4/P2.

## 6. Failure modes & edge cases

- **"Players never use the forbidden power" (the wasted-subsystem failure).** If the temptation isn't real, players rationally stay clean and the whole module never triggers — the designer built a spiral no one enters. **Fix:** the *refuel* (P2) must be substantial and must answer a *real* need — make legitimate alternatives scarce or costly in the genre's pressure loops (a fight you can't win cleanly; a metacurrency pool that runs dry). The corruption must be the *easy* answer to a *hard* problem, not a marginal option. Tune the refuel amount up if the power goes unused.
- **"Players spiral to doom too fast" (the pacing failure).** An inverted depletion mechanic (Operator 2) hits its climax *faster* than a normal one depletes — `18 §7`'s anti-pattern warns of this. If the die steps up on every use, a player can hit tier 5 in a session. **Fix:** (a) widen the cheapest-use range (1–2 = no step), so ~33% of uses are "free" and the climb is probabilistic; (b) gate step-ups to *beneficial* uses only, not every casting; (c) raise the step trigger to 4+ for slower burn; (d) make atonement *available* — the rope ladder back. Recompute the breakpoints (`13 §4`) so a typical character sees tier 3–4 across a *campaign arc*, not an evening.
- **The atonement exploit.** If stepping the die back down is too easy, players farm redemption between uses and the spiral never advances — the cost is vaporized. **Fix:** atonement is a **quest or ritual**, not a rest — it costs fiction (time, risk, a story beat), never nothing. Gate it to once per tier and make the GM the arbiter of when an atonement opportunity even *exists* in the fiction.
- **Milestone-table fatigue.** If every minor casting prompts a D66 roll and a tag, the table becomes bookkeeping (`19` FE2). **Fix:** the milestone table fires only on **tier transitions**, not every use. Day-to-day corruption is just the die stepping; the table is the *climax* beat, like a critical injury — rare and loaded.
- **The un-manning cliff.** Tier 5 removing a character from play can feel punitive if it arrives without warning. **Fix:** the doom ladder is **public fiction** — the player can see tier 4 (D12) coming and *chooses* the final stain. Tier 5 is always a player decision, never a surprise ambush. Offer the "sacrifice the power source to reset to T3" dial for genres where the floor should be costly, not terminal.
- **Inconsistent cost model.** `18 §5` warns against mixing cost types. If the game's master cost is *harm* and corruption costs *metacurrency* (or vice versa), the subsystem feels incoherent. **Fix:** align corruption's cost type with the game's master cost model (`12` degree-of-freedom 1), or justify the exception explicitly. In most dark-fantasy calibrations corruption is its *own* cost type — which is fine, because it is the *dedicated* cost for the forbidden-power layer.
- **The lone-edgelord monopoly.** If only one PC has forbidden power, the corruption spiral is a solo mini-game the table watches. **Fix:** either give every PC a corruption vector (different sources — one's a pact, one's an implant, one's a bloodline), or wire corruption milestones to *party* fiction (your stain marks an ally; your transformation endangers the group) so the spiral is shared drama, not a sidebar.

## 7. Validation notes

- **Math (`13 §3`/`§4`):** with a 3+ step trigger and 1–2 cheapest-use, the expected steps-to-climb from Clean to tier 5 is roughly 4–5 *beneficial uses per tier* × 5 tiers ≈ 20–25 beneficial uses — a campaign's worth, not a session's. If playtesting shows faster spirals, widen the cheapest-use range or raise the trigger to 4+. Recompute after any dial change; inverted mechanics are sensitive to trigger width (`18 §7`).
- **Exploits (`13 §5`):** the atonement-farm exploit (above) is the primary one; gated by quest-cost and once-per-tier. A secondary exploit: "use the forbidden power only when the Corruption die is already D12" (no further step risk) — **fix** by ruling that a D12 rolling 3+ is the *milestone* itself, so there is no safe ceiling.
- **Synergy (`13 §6`):** the subsystem *should* synergize with the power layer (`05`) — it is the cost that makes forbidden options balanced. Check that forbidden power is *not* also gated by a separate heavy cost (double-charging makes it unused; see failure mode 1).
- **Felt experience (`19`):** the doom ladder must be **visible** (public die + tier fiction + tells) to produce dread rather than anxiety — `19` C5 agency ledger: the player must see the slide to *choose* it, and the table must see it to react to it. The temptation must **pay well** enough to be genuinely tempting (FE1 false choice avoided) — a refuel too small to matter is the same as no subsystem. Tier 5 must be a **player-chosen** outcome, never a GM ambush (FE5 fairness); the tells guarantee the approach is visible. The milestone table carries the *memorable-specific* psychology of P4 — "your reflection has been smiling when you aren't" is the point, not "−1 to a stat." The self-reinforcing trap (higher die pays more) is *intended* felt experience: the player should feel the power getting harder to forsake as they fall, which is the dramatic engine of the genre.
- **Table load (`13 §7`):** one extra die roll on each *beneficial* forbidden use (light — same cadence as a damage roll). The milestone D66 fires only on tier transitions (~4–5 times across a campaign per character), so the heavy table is rare. The Corruption die itself is a single step-die on the sheet — less bookkeeping than a point tally. Net: low ongoing load, occasional loaded beats. Acceptable.
- **Pipeline verdict (`13 §8`):** passes intent (clear power-at-a-cost drama), math (tunable spiral length, ~20–25 beneficial uses to tier 5), exploit (atonement gated; no safe ceiling at D12), synergy (feeds the power layer rather than duplicating its cost), table (one extra roll per beneficial use; milestone table only on tier transitions — acceptable load). Ship with the redeemable dial as default; the one-way dial is a genre variant, not the baseline.

## 8. Worked genre example — Witch-hunting dark fantasy

**The setting:** A grim theocracy where the Inquisition hunts witches — but the only reliable weapon against the dark is the dark itself. The PCs are inquisitors licensed to use the forbidden arts (maleficia) in the hunt. Every casting stains them; the Order's oldest members are no longer entirely human. The dramatic question is not *whether* the PCs will fall, but *how far* and *whether they can come back.*

**What counts as forbidden:** casting any maleficia spell from `05` (the inquisitor's necessary evil), or channeling a captured witch's power through yourself. Legitimate alternatives (steel, prayer, fire) exist but are often insufficient against true horrors — which is why the temptation is real.

**Dials set:** 5-tier ladder (D6→D8→D10→D12→Lost); 3+ step trigger, 1–2 cheapest-use; benefit-only triggers; **the temptation = casting maleficia refuels Willpower (WP) by the Corruption die's face** (a D8 casting that rolls an 8 refuels 8 WP — a desperate inquisitor's lifeline); cosmetic-then-mechanical tiers; **4 milestone families** (Flesh / Mind / Soul / Shadow); **quest-based atonement** (a pilgrimage, a confession, a burned grimoire) stepping the die down one tier, once per tier.

**The milestone table (excerpt — Flesh family, maleficia-flavored):**
- T2 (D8) roll 23: *a permanent tell* — your wounds heal too fast, and smell of iron and old roses. Tag: UNSETTLING (−1 to first-impression social rolls). Atone: burn a relic of a saint at a shrine.
- T3 (D10) roll 41: *a borrowed hunger* — you must consume raw meat weekly or take a harm. Tag: HUNGER. Atone: a three-day fast under a confessor's watch.
- T4 (D12) roll 65: *your shadow detaches* — it acts on its own, whispering, and obeys the GM during scenes you aren't watching. Climax tag: SHADOW-TWIN. Atone: track and bind the shadow in a set-piece rite (a full session).
- T5 (Lost): you become what you hunt — the inquisitor turns, becomes an NPC horror, and the Order sends the next party after them.

(The Mind and Soul families run parallel — Mind produces obsessions, compulsions, and lost memories; Soul produces estrangement from the divine, failed prayers, and the gradual inability to enter consecrated ground. Four families means a maleficia-user stained by *different* works manifests *different* ruin — which keeps the spiral from feeling uniform.)

**In use (excerpt):**

- **The fight going badly.** Inquisitor Marta is cornered by a coven-bred horror; her steel is useless and she's at 2 WP. She invokes *Tongue-of-Ash* (a maleficia), succeeds, and **gains the benefit** — escape + the spell refuels her WP by her Corruption die's face. She is at **tier 1 (D6)**, rolls it: a **5** (3+, steps up). She is now **tier 2 (D8), Marked → Tainted.** She rolls the Flesh milestone: a 23 — her wounds now heal wrong, and she carries the UNSETTLING tag. She escapes, richer in WP, poorer in self. The other players *see* the die step up on the sheet — the dread is public.
- **The refuel making it worse.** Later, desperate again and now at tier 3 (D10), Marta casts: the D10 refuels **10 WP** — a fortune. The player feels the trap: the more stained she is, the more the power *pays*, and the harder it is to stop. She rolls the die: **3+**, stepping to tier 4 (D12). The player *sees the cliff.*
- **Three sessions later.** Marta is **tier 3 again** — between sessions she undertook a **pilgrimage** (atonement quest, a session of play, real fiction cost) and stepped back from tier 4 to tier 3. The spiral breathes. But the HUNGER tag persists (atonement steps the *die*, not the tags — another reason to climb slowly).
- **The campaign's end.** Marta reaches **tier 4 (D12)** again, with no time for another pilgrimage. The final horror can only be stopped by a great working. The player **chooses** the last stain: rolls the D12, gets **3+**, hits tier 5. She becomes the thing that stops the horror — and then must be stopped in turn. The player rolls a new inquisitor. The Order continues.

**Why this works in dark fantasy:** the *refuel* temptation maps exactly onto the genre's core tension — the inquisitor *needs* the dark to fight the dark, and the power genuinely works (the WP refuel is real, the escape is real). The doom ladder makes the slide *legible* — the player always knows how close to the edge they are, and every tier transition is a story beat (P4's specific-and-memorable psychology). Atonement as pilgrimage fits the theocratic setting and keeps the spiral from feeling like a trap. Tier 5 as "become the monster" delivers the genre's signature tragedy: the hunter who becomes the hunted. The self-reinforcing trap (a higher die pays more WP, so the most-corrupted inquisitor is also the most desperate to keep casting) is *the* dramatic engine of witch-hunter fiction — the veteran who has fallen too far to climb back, and knows it.

**Calibration note for this genre:** dark fantasy wants the redeemable dial *on* (pilgrimages exist) but atonement to be *scarce* (a pilgrimage is a session of play, and the GM need not always offer one). The result is a spiral that breathes — advances and retreats — rather than a one-way slide, which matches the genre's moral texture (hope and ruin in tension, ruin usually winning). For a *grimdark* variant where the slide is inexorable, switch atonement off entirely: the spiral becomes a countdown, and tier 5 becomes the campaign's planned endpoint for every inquisitor.

**Re-skin for your genre:**
- **Cosmic horror (alien tech / psychic overexposure):** forbidden = alien artifacts or overchanneling psi; tiers = biological mutation / sanity erosion; tier 5 = ghoul-hood or ego-death; atonement = rare suppressants that are themselves dwindling (P5, non-inverted).
- **Cyberpunk (black ICE / untested cyberware):** forbidden = unregulated implants or daemon-summoning; tiers = cyber-psychosis / humanity loss; tier 5 = flatline or goon-hood; atonement = expensive therapy / firmware rollback.
- **Superhero (dark bargain / radioactive origin):** forbidden = the power that also poisons you; tiers = the power mutating you; tier 5 = villain-turn; atonement = the loved one who pulls you back (once).
- **Necromancy / death magic:** forbidden = animating the dead; tiers = the dead *recognizing* you, then *following* you, then *replacing* you; tier 5 = you join your own court of the unburied.
