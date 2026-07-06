<!-- markdownlint-disable MD013 MD024 -->

# Dual-Use Matrix — One Mechanism, Many Psychologies

> This is the **calibration** layer of the generative method. `16` gave the palette of primitives; this file shows that each primitive *changes what the game is about* depending on how its dials are set — proven empirically by FL and West, which are the same engine producing opposite tones. Read this when you need to choose *what a mechanism should feel like*, not just *which mechanism to use*.

## Contents

1. Source provenance
2. Abstraction target
3. What "dual-use" means here
4. The matrix (primitive × calibration × psychology)
5. Case studies — five mechanisms, opposite psychologies
6. The calibration principles
7. Design intent

## Source provenance

This file is the **direct intellectual consequence** of `12-divergence-map.md`. The Divergence Map proved that FL and West are the same spine with five dials turned to opposite ends — which *is* the dual-use finding. This file extracts the method behind that finding: *how* to set a primitive's dials to produce a target psychology.

Every claim below is grounded in the calibrated points FL and West already provide. The "psychology" column is the new contribution — naming *what the mechanism feels like* at each calibration, so a designer can choose a tone deliberately rather than discovering it by accident.

## Abstraction target

The design-dials layer says: "set dial 1 (push-cost model) and the tone follows." This file makes that claim *actionable and exhaustive* across the primitives. The deliverable is a **matrix** showing, for each load-bearing primitive, the different psychologies it produces at different calibrations — with FL and West as two proven points and the genre-guidance for hitting each psychology in a new game.

**The core claim:** *there are no "good" or "bad" calibrations of a primitive — only calibrations that produce the psychology you want and calibrations that don't.* A mechanism that produces "aggression" in one game produces "caution" in another, *with the mechanism unchanged.* Genius-level design is knowing which calibration produces which psychology, and choosing deliberately.

## 3. What "dual-use" means here

**Dual-use** = the same primitive, at different parameter settings, serves *opposite* design purposes or produces *opposite* player psychologies. This is not abstraction-for-its-own-scope; it is the engine's most powerful design move, and the two source games are a worked example of it:

- FL and West run the **same core loop** (D6 pool, push-once, metacurrency). FL feels *gritty and attritional*; West feels *dramatic and character-driven*. The difference is *one dial* (push-cost model: harm vs currency), not a different engine.
- The **same D66 table architecture** (P4) produces "specific memorable harm" (FL crit families) *or* "punchy location-based results" (West master table) *or* "magical backlash spirals" (FL mishap families) *or* "faction events" — depending on what you put in the cells and how many families you build.
- The **same activity menu** (P6) produces "survival labor puzzle" (FL travel) *or* "heist crew coordination" (reinvention) *or* "starship bridge actions" (reinvention).

The matrix below names the **psychology** each calibration produces, so a designer can target a feel.

## 4. The matrix (primitive × calibration × psychology)

For each primitive (from `16`), the FL calibration, the West calibration, the psychology each produces, and the genre guidance.

### M1 — Metacurrency refuel (P2)

| Calibration | Refuel trigger | Psychology produced | Genre fit | Source |
| --- | --- | --- | --- | --- |
| **Harm-earned** (FL) | 1 WP per 💀 on Base dice when pushing | **Virtuous damage loop / aggression.** Getting hurt stocks your comeback — so risk-taking is rewarded. Players push into danger because pain = fuel. | Survival, horror, berserker, "fight from the ropes" | FL WP |
| **Success-earned** | 1 per 3-⚔ un-pushed roll | **Excellence loop / caution.** Playing well *without* risking produces fuel — so careful, high-skill play is rewarded. Players avoid pushing (which would lose the bonus). | Skilled-professional, mystery, heist | West (partial) |
| **Action/ritual-earned** (West) | Faith from rituals, relationships, Big Dream actions | **Drama loop / investment.** Fuel comes from *being the character* — praying, avenging, resting with a lover. Players pursue story beats because the story pays out. | Character-driven, dramatic, relational | West Faith |
| **Hybrid** | Two triggers | **Balanced.** Pain and drama both fuel; neither dominates. | Default for new games | (recommended) |

**The dual-use insight:** "a metacurrency refueled by X" produces a game *about X.* Harm-refuel makes a game about damage; success-refuel makes a game about skill; action-refuel makes a game about character. Choose the refuel trigger to choose the game's *subject.* `00 §7`.

### M2 — Push cost (P1)

| Calibration | Cost type | Psychology produced | Genre fit |
| --- | --- | --- | --- |
| **Self-harm** (FL) | 💀 damage to attributes/gear | **Attritional / physical.** The body is the stakes. Pushing always risks lasting harm. | Survival, horror, war |
| **Currency-spend** (West) | 1 Faith per push | **Resource-management / dramatic.** Belief is the stakes. Pushing is a budget choice, not a blood cost. | Dramatic, pulp, heist |
| **Narrative (Trouble)** (West, layered) | Trouble on Risky/Desperate fails | **Consequentialist / fictional.** Pushing makes the *story* worse, not the body. | Narrative, scandal, investigation |
| **Hybrid** | Currency + light harm/Trouble | **Visible-cost-without-mandatory-injury.** Pushing always costs *something,* rarely cripples. | Default for new games |

**The dual-use insight:** the cost type *is* the genre's currency. FL's body-as-currency and West's belief-as-currency are the same mechanism expressing opposite theses about what matters. A new genre's job is to name its currency. `00 §6`.

### M3 — Typed consequence table (P4)

| Calibration | Family set | Psychology produced | Genre fit |
| --- | --- | --- | --- |
| **Single master table** (West) | One D66 table, location × severity | **Anatomical / punchy.** "Where did I get hit?" is the story. Fast, memorable, low-prep. | Action, pulp, any genre where harm is harm |
| **Family of typed tables** (FL crits) | 8 families (Slash/Blunt/Stab/Burn/Acid/Cold/Swallow/Horror) | **Damage-type-specific / tactical.** The *kind* of wound matters — fire feels different from cold. | Survival, horror, tactical combat |
| **Per-discipline families** (FL mishaps) | 17 families, one per magic discipline | **Source-specific / flavorful.** Magic feels dangerous and *specific* — a Healing mishap is septic, a Stone Song mishap is geological. | High fantasy, kitchen-sink magic |
| **Count-modified gradient** (FL) | D66 roll shifts ±10 per 💀 | **Escalating doom.** More banes doesn't mean more damage — it means *sliding toward character-ending rows.* | Horror, grimdark |

**The dual-use insight:** *the number of tables is the depth of genre flavor.* One table = "harm is harm." Many tables = "the *type* of harm is the story." Same architecture, opposite payload. A designer chooses the family count to set how much the *kind* of failure matters. `04 §5`, `05 §7`.

### M4 — Activity menu breadth (P6)

| Calibration | Breadth | Psychology produced | Genre fit |
| --- | --- | --- | --- |
| **Formal, 14-row** (FL) | Each PC picks 1 of 14 tagged activities per Quarter Day | **Labor-puzzle / survival-as-play.** Travel *is* the game; distributing labor is the core tactic. | Hexcrawl, exploration, survival |
| **Implicit, ~6–8 jobs** (West) | Jobs named by the fiction (riding, hunting, breaking camp) | **Genre-textured / connective.** Travel is the connective tissue between dramatic scenes. | Dramatic, episodic, pursuit |
| **Reinvented: heist crew** | Roles: Hacker, Wheel, Face, Muscle, Hacker | **Coordination / planning-as-play.** The menu is the crew; specialization is the heist. | Heist, caper, team-based |
| **Reinvented: bridge crew** | Roles: Helm, Tactical, Engineering, Comms, Medical | **Bridge-drama / station-play.** The menu is the bridge; each station is a decision point. | Space opera, starship |

**The dual-use insight:** the activity menu's *content* sets what the game is *about doing together.* FL's menu makes the game about surviving a landscape; a heist menu makes it about executing a plan; a bridge menu makes it about running a ship. Same pattern, opposite subject. `06 §5`.

### M5 — Org ladder ceiling (P9, the meta-dial)

| Calibration | Ceiling | Psychology produced | Genre fit |
| --- | --- | --- | --- |
| **Full ladder** (FL) | Through Polity; base → band → company → faction → army → polity | **Saga / power-fantasy.** The campaign is about *becoming a power.* Scope grows without end. | Epic fantasy, political, conquest |
| **Capped at Company/Town** (West) | Stops at the personal/community scale | **Community / relational.** The campaign is about *people and a place.* Scope stays intimate. | Frontier, dynasty, community drama |
| **Capped at Band** | Stops at the party + retainer scale | **Personal / fellowship.** The campaign is about *the characters.* No org layer at all. | Noir, monster-hunter, road-trip |

**The dual-use insight:** *the ceiling is what the campaign is about.* FL's high ceiling = "you will become a power." West's cap = "you will build a life." A low ceiling is not a limitation; it is a *focus statement.* `07 §9`.

### M6 — Success ladder (P3)

| Calibration | Model | Psychology produced | Genre fit |
| --- | --- | --- | --- |
| **Threshold (GM-sets-bar)** (FL) | 1⚔ default; GM raises to 2/3 for demanding tasks | **Calibrated-difficulty / old-school.** The GM decides what's hard; players feel the world push back. | Traditional, sandbox |
| **Grade (roll-reads)** (West) | 0 fail / 1 partial / 2 full / 3+ crit — read after rolling | **Fiction-first / narrative.** The roll *tells* you how it went; the fiction interprets. | PbtA-adjacent, narrative |
| **Both / hybrid** | Grade + optional player Declared Effort | **Player-authorship / bold-play.** Players can *declare* a bigger aim and risk the threshold. | Default for new games |

**The dual-use insight:** who sets the difficulty (GM vs roll vs player) sets *who authors the fiction.* Threshold = GM-authored world; Grade = roll-authored fiction; Declared Effort = player-authored ambition. Same dice, different authority. `00 §4`.

### M7 — Protected dial (P10)

| Calibration | Form + scope | Psychology produced | Genre fit |
| --- | --- | --- | --- |
| **Die, narrow** (FL Pride) | D8/D10/D12 added to one protective roll/session | **Peak moments / heroic.** Once a session, you are the hero. Loss is a story beat. | Lethal one-shots, heroic |
| **Currency, broad** (West Faith) | Pool spent across the whole loop | **Sustained agency / dramatic.** You have budget to be the character all session. Depletion is despair. | Dramatic arcs, character-study |
| **Hybrid** | Small pool + escalating die | **Both peaks and pacing.** A daily budget + a session climax. | Default for new games |

**The dual-use insight:** the *form* (die vs currency) sets the *rhythm* of heroism — peaks vs sustained. A die produces a spike; a currency produces a curve. `01 §5`.

### M8 — Simulation register (spatial model + consequence source)

| Calibration | Register | Psychology produced | Genre fit |
| --- | --- | --- | --- |
| **Mechanical simulationism** (FL) | Hex-crawl; D66 weather; Resource-die food; typed crit families; vicissitude tables | **Deterministic / systemic.** The world simulates itself; the dice are the world. | Sandbox, survival, wargame-adjacent |
| **Narrative dramatism** (West) | Pointcrawl; prose weather-killers; profession-based hunting; Trouble halts; Fortune rolls | **Scenic / authorial.** The GM dramatizes the world; the dice dramatize the scene. | Narrative, dramatic, episodic |

**The dual-use insight:** this is degree-of-freedom 3 from `12 §12`. *Does the world simulate itself, or does the GM dramatize it?* Same pressures, opposite expression. A genre picks its register to set how much *machinery* sits between player and fiction.

## 5. Case studies — five mechanisms, opposite psychologies

These are the cleanest examples of dual-use in the engine. Each shows *one mechanism, two calibrations, two opposite psychologies, both proven.*

### Case 1 — The push, in two registers

**Same mechanism:** reroll non-successes once.
- **FL:** the reroll is free; you pay in 💀 already on the dice → *the body is the stakes; aggression is rational.*
- **West:** the reroll costs 1 Faith → *belief is the stakes; budgeting is the skill.*
**Both are "the push."** Neither is the "real" version. The choice of cost type *is* the choice of genre.

### Case 2 — The D66 table, in three payloads

**Same architecture:** D66, Tens/Units, `65`/`66` climax.
- **West crits:** one anatomical table → *where you got hit is the story.*
- **FL crits:** 8 typed families → *what kind of wound is the story.*
- **FL mishaps:** 17 per-discipline families → *what went wrong with your magic is the story.*
**Same table.** The payload (one vs many families) sets whether the *type* of consequence matters.

### Case 3 — The activity menu, in two subjects

**Same structure:** each PC picks one job per time block from a menu of mutually-exclusive demands.
- **FL travel:** HIKE/LEAD/WATCH/FORAGE/HUNT/CAMP/... → *surviving a landscape is the game.*
- **Reinvented as heist:** HACKER/WHEEL/FACE/MUSCLE/LOOKOUT → *executing a plan is the game.*
**Same menu.** The job list sets the subject.

### Case 4 — The org lifecycle, at two ceilings

**Same five beats:** founding → functions → upkeep → events → scale.
- **FL, full ladder:** the org climbs to a polity → *the campaign is about becoming a power.*
- **West, capped:** the org is a saloon or town → *the campaign is about building a life.*
**Same lifecycle.** The ceiling sets the campaign's scope and subject.

### Case 5 — The metacurrency, refueled three ways

**Same pool:** cap 10, spends on agency.
- **Harm-refuel (FL):** pain stocks your comeback → *aggression.*
- **Success-refuel:** excellence stocks your future → *caution.*
- **Action-refuel (West):** drama stocks your soul → *investment.*
**Same pool.** The refuel trigger sets the loop's *emotion.*

## 6. The calibration principles

Read the matrix enough times and four principles emerge. These are the *rules of thumb* for producing a target psychology deliberately.

### Principle 1 — The cost type *is* the genre's currency.

Whatever a player *spends to push / act / survive* becomes what the game is *about.* Body → survival. Belief → drama. Time → heist/planning. Reputation → social. Name the currency, wire the cost model to it, and the tone follows. (`M1`, `M2`.)

### Principle 2 — The refuel trigger *is* the loop's emotion.

Whatever *stocks the pool* becomes the behavior the game rewards. Harm-refuel rewards aggression. Success-refuel rewards caution. Action-refuel rewards investment. You are not designing a pool; you are designing a *behavioral incentive.* (`M1`, `M5`.)

### Principle 3 — The number of tables *is* the depth of genre flavor.

One consequence table = "harm is harm." Many typed tables = "the *kind* of harm is the story." The family count sets how much *specificity* the genre wants. Don't build 17 tables for a pulp game; don't build 1 for a survival-horror game. (`M3`.)

### Principle 4 — The ceiling *is* the campaign's subject.

How high the org ladder climbs determines whether the campaign is about individuals, communities, or power. A cap is a focus statement, not a limitation. (`M5`.)

### Meta-principle — Every primitive is a dial, not a verdict.

There are no "right" calibrations. FL and West prove that opposite calibrations of the same primitive both produce excellent games. The designer's job is *not* to find the correct setting; it is to *choose deliberately* the psychology each primitive produces, and to ensure the choices are *consistent* (the consistency rules are the subject of `18`).

## 7. Design intent

This file exists because the engine systems documented the dials but did not name what they *do to the player.* A designer reading `00 §11` learns that "push-cost model" is a dial with two points — but not that those two points produce *opposite psychologies* (aggression vs caution), or that the choice *is* the choice of genre.

The dual-use matrix makes the engine's most important property — *that the same mechanism produces opposite games at opposite calibrations* — into a *lookup table* rather than an insight you have to rediscover each time. With this file, a designer who wants "a game about the cost of ambition" can scan M1–M2 and see exactly which refuel and cost calibrations produce it, with FL or West as proof it works.

This is the **second** of the three generative layers. `16` gave the palette; this file gives the calibration map. `18` teaches the final move: *composition* — taking primitives from their home systems and re-purposing them in foreign systems to invent genuinely new mechanics, which is what "genius-level designer, reproducible" ultimately means.
