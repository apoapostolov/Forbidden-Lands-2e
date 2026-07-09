<!-- markdownlint-disable MD013 MD024 -->

# Investigation & Clue Economy — Clues as Currency

> **STATUS: WORKSHOP MODULE.** Treats clues as a spendable currency refueled by an investigation activity menu, with a risky-inference *push* that gates revelations behind player-driven inquiry — not a single Insight roll. *Core is generic; the worked example (noir / cosmic horror) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic design space
   - 2a. Rule overview
   - 2b. NEW CONCEPTS introduced
   - 2c. Rules reference (tables & procedures)
3. The pressure loop
4. Choices
5. Integration points
6. Failure modes & edge cases
7. Check notes
8. Worked genre example — Noir / cosmic horror

## 1. Origin — how this was built

- **Source patterns:** **P2 (capped pool refueled by risk)** — clues as the spendable pool; **P6 (activity menu)** — the investigation activities that *earn* the pool; **P1 (push-and-pay)** — the risky inference that *spends* the pool on a gamble; **P4 (typed D66)** — what a wrong inference costs (the backlash / fallout table). Optionally **P5 (resource die)** as an alternative pool model (see Choices).
- **Reinvention operator:** **Domain Transfer (P2) + Fusion.** Domain-transfer P2 from "personal resolve" (WP/Faith) to "evidence gathered" — clues *are* a capped pool that spends on agency (here: the agency to *act on a conclusion*) and refuels from engaging the system's risk rules. Then **fuse** P6 + P2 + P1: the activity menu *earns* the pool; spending the pool *unlocks* certainty; the push *spends* the pool on a gamble when certainty is short. The fusion produces a loop none of the patterns makes alone — mystery-solving as resource management.
- **Target psychology:** **Action-refuel** (`17` M1, action-earned column) — fuel comes from *doing the investigation*, so the game becomes *about* investigating. The push cost is **narrative/Trouble** (`17` M2) by default — a wrong inference makes the *story* worse (a false accusation, a contaminated scene), not the body — recalibrable to **harm/corruption** for horror.
- **Problem solved:** investigation in most RPGs is either (a) a single "Insight" or "Investigation" roll that hands the player the answer (no process, no texture, and a failed roll bricks the mystery — the classic brick-wall failure), or (b) pure GM-narrated deduction where the rules offer nothing and "finding the clue" is down to whether the player phrases the right question. This module gives deduction the same dramatic rhythm the push economy gives combat: a pool that fills from *what the players choose to do*, spends on *confidence to act*, and can be *gambled* when time runs short — so that "we don't know yet" is a *decision*, not a dead stop.

## 2. The generic design space

### 2a. Rule overview

The Clue Economy turns deduction into a resource loop. A party-shared **Clue pool** (a capped pool, P2) fills from *what the players choose to do* — an **investigation activity menu** (P6) whose mutually-exclusive demands make labor distribution the core tactic. The pool **spends on certainty**: revelations (a Connection, a Conclusion, a Conviction) have a clue cost, and meeting it converts evidence into a confirmed conclusion the GM ratifies as true.

The loop's signature beat is the **risky-inference push** (P1): when the party is short of a revelation's cost and time is running out, any PC may *gamble* — declare a conclusion beyond the evidence and roll the gap. Success confirms it for free; failure commits them to a false conclusion and fires a **Wrong Inference** backlash (P4, typed D66). So "we don't know yet" becomes a *priced decision*, not a dead stop — the same beat the push economy gives combat.

Pressure comes from the **Threat Clock**: a rising track that advances each Investigation Phase while the party works, making investigation time finite. Every extra phase of clue-gathering costs the antagonist's-plan clock a tick; every push skips that cost but gambles correctness. The clock is what makes the safe path (earn more) and the fast path (push now) genuinely rival choices.

The module triggers only for mysteries that deserve a scene — a hidden truth the PCs must uncover to act, finite time (the clock is rising), and real consequence for being wrong. For "do I find the key on the desk," use a single roll (`03 §11`); reserve the Clue Economy for mysteries with teeth — the engine's same gating instinct as Social Combat (`workshop/03`).

### 2b. NEW CONCEPTS introduced

- **NEW CONCEPT — Clue pool as gathered proof:** Core engine's capped pool (P2: WP/Faith) is *personal resolve* that spends on re-rolls and stunts. Here the pool is **domain-transferred to evidence**: clues are gathered facts that spend on *certainty to act on a conclusion*. The currency (P2) is recombination; the *application* — a clue economy where evidence buys revelations — is new: no core system treats gathered information as a spendable pool. *Extends the engine by making deduction a resource-management loop.*
- **NEW CONCEPT — Hard / soft clue split:** Core resources are single-tier (WP is WP; a Gear Die is a Gear Die). This module splits the clue pool into two tiers — **soft clues** (interchangeable, count toward any cost) and **hard clues** (specific, *named*, required for the highest revelations). No core resource has this dual-tier structure where a subset is type-locked. *Extends the resource model with a required-specific tier that defeats brute-force spending.*
- **NEW CONCEPT — Risky inference push (P1 applied to deduction):** The push (P1: re-roll by paying a cost) is core to attribute rolls and combat. Here it is **domain-transferred to deduction**: push a *conclusion beyond the evidence* — gamble that your intuition spans the clue-gap. The rule is recombination; the *application* — pushing a hypothesis, not a die — is new. *Extends the push from "try the action harder" to "act on less than you know."*
- **NEW CONCEPT — Threat Clock (rising investigation-pressure track):** Core time pressure is *random* (encounter tables, random rolls) or *binary* (a single deadline). The Threat Clock is a **deterministic rising track** that advances on a fixed trigger (+1 per Investigation Phase) and fires at a threshold — making investigation time finite and *knowable*, not random. No core system has a deterministic pressure clock tuned to an investigation cadence. *Extends the engine with a rising (not random) pressure source.*

### 2c. Rules reference (tables & procedures)

#### The Clue pool (P2 — counted form)

- **What it is:** a party-shared pool of solid evidence — fictional facts the table has named ("the robe fiber," "the gardener's alibi gap"), not abstract points.
- **Cap:** ~8 (choice: 4–5 for scarcity).
- **Two tiers:**
  - **Soft clues** — ordinary evidence. Interchangeable: any soft clue counts toward any revelation's cost.
  - **Hard clues** — specific, *named*, required evidence. Some revelations demand a named hard clue, not just N clues (see *Buying certainty*).
- **Spending** a clue = *deploying* that evidence to firm up a conclusion; it is converted into certainty, not consumed for a re-roll.

#### Alternative pool form — the Evidence die (P5)

Track clues as a single **Evidence die** (D6–D12) instead of a counted pool:

1. Each **spend** (buying a revelation, or the gap-cost of a push) **rolls** the Evidence die. On a 1–2, it **steps down** one rank (D12→D10→D8→D6).
2. Earning clues at a rich scene, or a successful **ANALYZE**, **steps it up** one rank (max D12).
3. At **D6, on a 1–2**, the evidence is **exhausted** — the trail is cold; the party must push or rest the case.

*The hard/soft split and the failure-yields-a-lead valve work identically on top of either form; only the counting changes. Choose the counted pool for tactical deduction, the resource die for atmospheric investigation.*

#### The investigation activity menu (P6)

The mystery is investigated in **Investigation Phases** — structured time blocks (an evening of work, a day of legwork), analogous to a travel Quarter Day (`06 §5`). Each phase, each PC picks **one** activity. The menu's demands are *mutually exclusive* — the party is always short of hands, and distributing labor is the core tactic (P6's signature tension).

**SEARCH** means combing a location for physical evidence — the crime scene, the suspect's rooms, the ditch where the body was found. Roll a core ability pool (INSIGHT, SCOUTING, INVESTIGATE, or equivalent). On a success, you earn soft clues: fibers, footprints, a misplaced letter, a stain. On a strong success, or at a rich scene, you may find a hard clue — the specific, named evidence a Conviction will later demand.

**QUESTION** means interviewing a witness, a suspect, or a contact. Roll a social ability (MANIPULATION, INSIGHT, PERFORMANCE, or equivalent). On a success, you earn soft clues: what they saw, what they heard, what they suspect. You also earn leads to new scenes — another witness, another location, another name. A QUESTION that goes well opens the next door; one that goes badly may close it.

**RESEARCH** means hitting the archives, the lore, the contacts, the public records. Roll a knowledge ability (LORE, BOOKLEARNIN', or equivalent). On a success, you earn soft clues and, if applicable, the *type* of threat you are facing — is this a cult? A serial killer? A corporate cover-up? RESEARCH contextualizes the evidence the other activities gather.

**SURVEIL** means tailing a person or staking out a place — watching, waiting, following. Roll STEALTH, SCOUTING, or equivalent. On a success, you earn soft clues: patterns, routines, meetings. On a strong success, you earn a hard clue: a witnessed act, something seen with your own eyes that cannot be denied. SURVEIL is how you get the specific damning fact.

**ANALYZE** means cross-referencing the clues you already have — lab work, collation, pattern-matching, consulting a specialist. Roll a knowledge or crafting ability (LORE, CRAFTING, or equivalent). ANALYZE does not earn new clues; it converts soft clues into hard ones, and clarifies what a clue *means*. The fiber becomes "imported Flemish wool, dyed with madder." The alibi gap becomes "he could not have been where he said he was." ANALYZE is the bridge between evidence and certainty.

**WATCH / COVER** means guarding the party's flank against interference while the others investigate. You earn no clues. Instead, you reduce the Threat Clock's tick this phase — you are running interference, keeping the antagonist's agent busy, watching for the tail. WATCH is the pressure-relief valve, bought at the cost of earning nothing toward the mystery.

**Activity resolution procedure:**

1. Roll a core ability pool (P1, `00 §3`) for the chosen activity; read on the success ladder (P3).
2. ⚔ earned scales clue yield (graded ~1 clue per ⚔, or flat 1/phase per the Earning choice).
3. **Failure still yields one soft clue** (a hunch, a lead) — the menu never returns nothing (anti-brick-wall, §6).
4. **Core clues** — evidence the plot *requires* to advance — auto-succeed: never gate a must-have behind a roll.

#### Buying certainty (P2 spend) — the revelation-cost table

Revelations have a **Clue Cost** — a threshold of evidence the party must deploy to act on a conclusion with confidence. Meeting the cost converts evidence into *certainty*; the GM confirms the conclusion as true.

| Revelation tier | Cost | Example |
| --- | --- | --- |
| **Connection** (a single link) | 1–2 soft | "The victims all attended the same theatre." |
| **Conclusion** (the shape of the truth) | 3–4 soft | "The disappearances are ritual sacrifices." |
| **Conviction** (who / where / how, actionable) | 4–5 soft + a named **hard clue** | "Castaigne is the cult leader; the rite is tonight at the theatre." |

*The hard-clue requirement on Convictions is the anti-brute-force spine: you cannot buy "who did it" with filler — you need the specific damning fact. ANALYZE exists to manufacture hard clues from soft ones.*

#### The push — risky inference (P1, numbered procedure)

When the party is short of a revelation's cost and wants to act *now* (the Threat Clock is rising), any PC may **push an inference**: declare a hypothesis beyond the evidence and roll the gap.

1. **Declare** the inference — a conclusion the evidence does not yet confirm.
2. **Size the pool to the gap:** count the missing clues (cost minus what the party holds). Roll an ability pool — typically **Wits + Investigate** — against a GM-set threshold that rises with the gap (≈ +1 threshold per missing clue). A 1–2 clue gap is rollable; a 4+ gap is near-hopeless.
3. **Success** — you were right (brilliant intuition / lucky leap). The conclusion is confirmed **as if spent** — **no clue cost**. One push per conclusion.
4. **Failure** — you were wrong, and you have *committed* to the false conclusion. Two costs fire:
   - Roll on the **Wrong Inference** table (below) — what being wrong costs.
   - **Burn clues:** having loudly committed to a theory, you've muddied the evidence — **lose 1–2 soft clues**.

*The push converts "we don't have enough" from a dead-end fail into a priced decision — exactly as the push does for a missed attack.*

#### The Wrong Inference table (P4, typed D66)

A failed push rolls a **typed D66** (Domain Transfer of P4 from crits/mishaps to *deductive error*). Tens = the axis of the error; Units = severity. The **Procedural** family (narrative cost) is built out in full below; the **Mythic** family (harm/Corruption cost, for cosmic horror) uses the same D66 ranges with swapped effects.

**Procedural family** (noir / procedural — narrative cost):

| D66 | Result | Rule effect |
| --- | --- | --- |
| 11–14 | **Wasted raid.** The false theory sends you to the wrong place at the wrong time. | Lose a phase; the Threat Clock still advanced. |
| 15–22 | **Stale lead.** A hunch you chased hard goes cold. | −1 soft clue; one source is spent. |
| 23–31 | **The threat buys time.** Your blunder costs the antagonist nothing. | Threat Clock +1. |
| 32–41 | **A false accusation / wrong door.** You name or raid the wrong party. | −2 soft clues; a Debt or vendetta is born. |
| 42–51 | **Scene contaminated.** Chasing the error, you've muddied a location. | −2 soft clues; that source yields nothing more. |
| 52–61 | **The culprit is wary.** They now know someone is hunting — and they're careful. | Future SURVEIL / QUESTION −1; the culprit takes a precaution. |
| 62–64 | **A witness silenced.** Someone who could have talked now can't. | Lose a named hard-clue source; −1 soft clue. |
| 65 | **The culprit comes for you.** Knowing you're close (but wrong), they strike first. | A direct confrontation — roll for Harm (`04`). |
| 66 | **The threat fires.** Your wrong inference was the last piece they needed. | The mystery becomes a crisis — the ritual completes / the killer strikes again. |

**Mythic family** (cosmic horror — harm / Corruption cost): same D66 ranges, effect swapped to the doom spiral. Severity maps to Corruption (`workshop/07`): *minor* (11–31) = a glimpse — nightmares, −1 to one attribute next phase; *costly* (32–61) = 1 Corruption (a glimpsed rite, an echoed chant) or attribute damage; *severe* (62–64) = a deeper wound; **65** = a permanent Mythos touch; **66** = the ritual completes and the manifestation costs 1d3 Corruption to all present. Build the rows on the same spine (TIME → EVIDENCE → EXPOSURE) with mythic nouns.

*This is the same one-architecture-many-effects trick as FL's crit families (`M3`): the kind of wrongness the genre cares about becomes the story.*

#### The Threat Clock (P14 analog — numbered procedure)

The mystery runs against a **Threat Clock**: a track (typically **6 segments**) representing the antagonist's advancing plan. It is the pressure source that makes *earning* clues costly (it costs time) and the *push* tempting (it costs no time but gambles correctness).

1. **When it ticks.** The clock ticks once per **Investigation Phase** — after every PC has resolved their activity for the phase. This is a *defined* trigger, not GM mood.
2. **How much it ticks.** **+1 segment** per phase by default (the Threat-Clock-speed choice: +1/phase = pressure-cooker; +1/session = relaxed). Two modifiers:
   - A **WATCH / COVER** activity taken this phase **reduces** the tick by 1 (minimum 0) — the pressure-relief valve, bought at the cost of earning no clues that phase.
   - A failed push's **Wrong Inference** result can **add** ticks (per the table: several rows advance the clock +1 or +2).
3. **What happens at threshold.** When the clock fills (all segments marked), the threat **fires**: the ritual completes, the killer strikes again, the trail goes cold, the mole exfiltrates. The mystery becomes a *crisis* — the consequences are now in play and must be dealt with, not prevented. Roll on the **Threat Consequence** table below (or choose the row that fits the fiction).

4. **What happens after firing.** The clock **resets to half** (3 segments) — the threat is not over; it has *escalated*. The party now races a new deadline while dealing with the consequences of the first firing. Each subsequent firing is worse (step down the table's severity column). The clock only reaches 0 (the threat is over) when the party *resolves* the source — confronts the culprit, disrupts the ritual, exposes the mole.

#### Threat Consequence table (D6)

Roll when the clock fills. The severity column applies if this is a *second or later* firing — the threat escalates each cycle until resolved.

| D6 | First firing (the threat advances) | Subsequent firings (the threat escalates) |
| --- | --- | --- |
| 1 | **A warning.** The antagonist's plan becomes visible — a body is found, a symbol is painted, a witness flees. No one is lost yet, but the stakes are now public. The party loses 1 soft clue (the scene is contaminated by the antagonist's move). | The antagonist sends a message — a threat, a taunt, a displayed victim. −1 to all social rolls with frightened NPCs for a phase. |
| 2 | **A setback.** A clue source is destroyed or lost — the witness is killed, the document is burned, the scene is compromised. Any hard clue that was *there* is now gone; the party must find another path. | A second source is lost. The investigation narrows — the GM removes one clue source from play. |
| 3 | **An escalation.** The antagonist gains ground — a new victim, a broader ritual, a deeper infiltration. The party's Standing with a faction investigating alongside them drops by 1 (they're seen as failing). | The antagonist secures an ally or resource. A faction the party needs shifts away (−1 Standing, propagates per `workshop/02` if using the web). |
| 4 | **A confrontation.** The antagonist or their agent appears — not the final confrontation, but a skirmish, a chase, a narrowly-escaped ambush. Resolve as a combat/chase scene. | The confrontation is worse — a tougher agent, a tighter ambush. The party must flee or fight at a disadvantage. |
| 5 | **A closing window.** The party's window to act *narrowrows* — the ritual nears completion, the killer prepares to flee, the mole's extraction is imminent. The clock's reset value is 4 segments, not 3. | The window is nearly shut. Reset is 5 segments. The next firing is likely the climax. |
| 6 | **The crisis.** The threat's plan completes a major stage — the ritual's first phase succeeds, the killer claims a significant victim, the mole escapes with the key secret. The party has *failed to prevent* this; they must now deal with the consequences AND continue the investigation. At a subsequent firing on a 6, this is the **climax** — the antagonist's plan completes fully; the party must confront or concede. | The climax. The antagonist wins this round decisively. The mystery becomes a disaster the party must now *survive* or *avenge*, not prevent. |

**GM guidance:** the table is a prompt, not a constraint. The point is that firing has *specific, escalating* consequences — not "the GM makes something bad happen." If a row doesn't fit the fiction, pick the one that does, but always make the firing *cost* the party something visible.

## 3. The pressure loop

- **Pressure:** the Threat Clock rises each phase; clues are finite; hard clues are scarce and must be *found* (not bought).
- **Decision:** *do we spend a phase earning more clues (safe, but the clock ticks), or push the inference now (risky, but free of time)? do we deploy our hard clue here or save it for the conviction?*
- **Consequence:** certainty bought (safe action) vs inference pushed (gambled action); clock advances; wrong inferences backlash and burn clues.
- **State change:** the hidden truth narrows; the antagonist's plan advances; the party's evidence and exposure both shift.
- **Loop shape:** **investigate → accumulate → conclude (spend) or push (gamble) → backlash/reward → act.** Runs at Phase cadence (slower than a Round; faster than a session) — a *strategic-deductive* resource.

## 4. Choices

| Choice | Setting A | Setting B | Psychology produced |
| --- | --- | --- | --- |
| **Pool scope** | Party-shared (one pool) | Per-investigator (each tracks own) | Collaborative deduction vs specialist competition |
| **Pool cap** | 8 (generous) | 4–5 (scarce) | Comfortable sleuthing vs tense scarcity |
| **Earning model** | 1 clue per ⚔ (flat) | Graded 1–3 by ⚔ (excellence-scaled) | Steady vs rewards high-skill investigation |
| **Hard/soft split** | On (some revelations need named hard clues) | Off (all clues are interchangeable) | Anti-brute-force spine vs pure resource puzzle |
| **Failure yield** | 1 soft clue always (a lead) | Nothing on a fail (strict) | Anti-brick-wall vs old-school dead-ends |
| **Push cost when wrong** | Narrative (Wrong Inference table: false leads, wasted raids) | Harm/Corruption (mythic backlash, attribute damage) | Procedural/noir vs horror |
| **Wrong-inference reveal** | Immediate (you learn fast, self-correct) | Delayed (you act on it; the twist comes later) | Self-correcting vs twist-generating |
| **Threat Clock speed** | +1/phase (pressure-cooker) | +1/session (relaxed) | Urgent vs deliberate |
| **Who authors the inference** | Player declares freely | GM offers a menu of candidate theories | Open deduction vs curated options |
| **Pool form** | Counted pool (P2) | Resource die, D6–D12, steps down on spend (P5) | Bookkeeping-light vs "evidence thinning" feel |

**Calibration guidance:** start with a party-shared pool cap 8, graded earning, hard/soft split **on**, failure-yields-a-lead **on**, push cost = narrative, threat clock +1/phase. The hard/soft split and the failure-yields-a-lead valve are the two non-negotiables — they are what prevent the two catastrophic failures in §6. Add per-investigator pools or harm-cost pushes only if investigation is a *pillar* of the campaign.

## 5. Integration points

- **Hooks into:** the social-conflict system (`03 §11`) — QUESTION is a social roll and can escalate into a full Social Combat (`workshop/03`) when an interview is high-stakes. Hooks into harm (`04`) — a harm-cost push (choice above) deals real damage; the Wrong Inference table (P4) is a sibling of the crit families. Hooks into travel/downtime (`06 §5`) — an Investigation Phase is structurally a Quarter Day and can nest inside one. Hooks into the faction web (`workshop/02`) — investigations *into* a faction shift Standing when concluded. Hooks into **Corruption** (`workshop/07`) — a mythic-cost push can climb the corruption ladder (the worked example uses this).
- **Requires:** a defined hidden truth (the GM knows who/what/why); a Threat Clock; a set of clue sources (locations, witnesses, records) the menu activities can target.
- **Replaces / extends:** the single "Insight"/"Investigation" roll — adds the economy and the push for mysteries that warrant a scene, leaving simple searches on the single roll.
- **Cross-refs:** `16` P1/P2/P4/P6 (+ P5 optional); `17` M1 (action-refuel) and M2 (push-cost type); `13 §8` (review path); `19` FE1/FE4 (the two failures this is engineered around).

## 5a. Handshake

- **Prerequisites:** inquiry scenes, time pressure, revelations or questions.
- **Inputs:** clue cap, inquiry activities, spend menu, risky inference trigger.
- **Outputs:** Clue pool, revelation ladder, inference procedure.
- **Touched systems:** GM, downtime, social, powers, heat.
- **Replaces or stacks:** replaces binary clue gates; stacks with `18-mystery-conspiracy-and-revelation.md` only if Clues buy inference rather than basic access.
- **Incompatibilities:** do not charge both Clues and required-roll success for the same mandatory fact.

## 6. Failure modes & edge cases

- **"The mystery is now solvable by brute force."** *(The critical investigation-design failure.)* If clues are too easy to farm, players grind activities to cap and buy the answer — deduction collapses into a resource tally, and the mystery has no teeth. **Fix (three layers):** (a) the **Threat Clock** makes every extra phase cost time the antagonist uses — grinding is not free. (b) **Clue decay:** witnesses go cold, scenes get contaminated — soft clues earned more than ~2 phases ago can't be spent (the GM marks them stale). (c) The **hard/soft split**: Convictions require a *named* hard clue, which cannot be brute-forced — you can't buy "who did it" with filler, you must *find the specific damning fact* (and ANALYZE it). (`13 §5.5` action-budget-abuse variant; `19` FE1 — if everything is buyable, the deduction is a false choice.)
- **"Players stuck with no clues."** *(The other critical investigation-design failure — the brick wall.)* If rolls fail and clues run dry, the party hits a dead end with nothing to spend and no way forward. **Fix (the module's built-in escape valves):** (a) the **push exists precisely for this** — you can always gamble an inference with zero clues; "stuck" is never terminal, it's a *priced decision*. (b) **Failure yields a lead:** a failed activity still produces one soft clue (a hunch, a new direction) — the menu never returns nothing. (c) **Core clues auto-succeed** — plot-critical evidence is never gated behind a roll. (`19` FE4 agency-collapse: a rule that removes the player from meaningful play; C3 flow channel — preserve a recovery/re-engagement valve.)
- **The face monopolizes.** If only the high-Insight/high-social PC earns clues, the rest watch. **Fix:** the activity menu is the cure by construction — P6's labor distribution guarantees every PC an investigation job (the muscle SURVEILs, the scholar RESEARCHes, the tough guards via WATCH). Ensure no activity is always-optimal.
- **"The push is always wrong" (or always right).** If pushing is reliably punished, players never gamble and the signature beat never fires; if reliably safe, it replaces earning. **Fix:** the push's success chance must be *real* (recompute the gap; a 1–2 clue gap should be rollable, not hopeless), and the cost *proportional* — not catastrophic-by-default. One push per conclusion prevents push-spam.
- **Brute-forcing the push.** Players push every inference to skip earning. **Fix:** failed pushes **burn clues** (you've muddied the evidence by committing to a theory) and the Wrong Inference costs *accumulate* (false accusations compound; mythic backlash stacks toward Corruption). Pushing is for when you *must* act short — not a free substitute for legwork.
- **The GM-fiat threat.** If the Threat Clock advances on GM whim, the pressure feels rigged (`19` FE5 "too unfair"). **Fix:** the clock ticks on a *defined* trigger (+1 per phase, full stop) and WATCH reduces it on a *defined* roll — never on mood.

## 7. Check notes

- **Math (`13 §3` / `§8` Stage 1):** clue-earning rate vs revelation costs should be tuned so a typical mystery resolves in 3–5 Investigation Phases (mirroring a 3–5 Round combat). At graded earning (~2–3 clues/phase across a party of 3–4) and Connection/Conclusion/Conviction costs of 2/4/5, a party reaches a Conclusion in ~2 phases and a Conviction in ~3–4 — provided they secure the hard clue. If mysteries drag, lower costs or raise earning; if they collapse too fast, raise the hard-clue bar or speed the clock.
- **Abuses (`13 §5` / Stage 2):** the brute-force risk is the main one — gated by the hard/soft split + Threat Clock + clue decay (three independent brakes, deliberately redundant). Push-spam is gated by clue-burn-on-fail + accumulating backlash. Verify a party cannot farm WATCH indefinitely (WATCH earns no clues, so it stalls deduction even as it slows the clock — a real tradeoff, not an abuse).
- **Synergy (`13 §7` / Stage 3):** the module hooks cleanly because it reuses P1/P2/P6 — no new dice type, no parallel economy. The one synergy to watch: a harm-cost push stacking with Corruption (`workshop/07`) can spiral faster than either alone — recompute the doom curve if both are on.
- **Felt experience (`19` §7 Stage C):** the **push** is the key psychology — it turns "we lack evidence" into a *decision*, defeating FE4 (agency collapse / the brick wall). The **hard/soft split** defeats FE1 (false choice): if every conclusion were buyable with filler, deduction would be meaningless. The **failure-yields-a-lead** valve preserves C3 (flow channel) — there is always a next move. Wrong Inference tables should be telegraphed (C2 perceived randomness): the GM foreshadows that a theory is thin before the push, so a wrong result feels *earned*, not random.

## 8. Worked genre example — Noir / cosmic horror

**The setting:** A gaslit 1920s city. Investigators pursue a cult of the Yellow Sign kidnapping victims for a summoning. Each phase the **Summoning Clock** (6 segments) advances; at 6, the King in Yellow manifests. Pushing a *wrong* inference doesn't just waste a raid — it exposes the pusher to mythic backlash (gaining **Corruption**, `workshop/07`).

**Settings chosen:** party-shared pool cap 8; graded earning (1–3 by ⚔); **hard/soft split ON**; failure-yields-a-lead ON; push cost = **harm/Corruption** (Mythic Backlash table, P4); wrong-inference reveal **delayed** (you act on the false theory — the twist lands later); threat clock +1/phase.

**The menu:** SEARCH / QUESTION / RESEARCH / SURVEIL / ANALYZE / **WARD** (the WATCH equivalent — wards the party against mythic attention, −1 clock tick, no clues).

**In use (excerpt):**

- **Phase 1** (clock 0→1). The party distributes labor. **Eleanor** SEARCHes the latest crime scene — Wits 4 + Investigate 2 = 6 dice, 2⚔ → earns 2 soft clues *and* finds a **hard clue**: a yellow silk robe-fiber caught on a nail. **Marcus** QUESTIONS the night-watchman — Empathy 3 + Manipulation 2 = 5 dice, 1⚔ → 1 soft clue (the watchman recalls a theatrical carriage) + a lead to the livery. **Sven** SURVEILs the suspect boarding house — fails the roll, but still gets **1 soft clue** (a hunch: visitors arrive only after midnight). **Mira** WARDS — earns no clues, but holds the clock to +1 (now 1). Pool: **4 soft + 1 hard** (the fiber).
- They spend 2 soft to buy the **Connection**: "the victims all attended the Castaigne Theatre." Confirmed. (Pool: 2 soft + 1 hard.)
- **Phase 2** (clock 1→2; Mira wards again, holds to 2). Eleanor **ANALYZEs** the robe-fiber — cross-references theatrical costumers. Success → the fiber traces to Castaigne's private tailor; this *converts* to a second hard clue ("the robe is Castaigne's") + 1 soft. Now they could reach the **Conviction** "Castaigne is the cult leader; the rite is tonight" — cost 4 + the named hard clue. They have 3 soft + 2 hard, but the Conviction needs *4 soft* alongside the hard clue. They are one short.
- **The push.** The clock is at 2 and rising; Marcus's player doesn't want to spend a Phase 3 earning one more clue. He **pushes the inference**: "It's Castaigne — we raid the theatre tonight." Roll the 1-clue gap: Wits 3 + Investigate 2 = 5 dice vs threshold 2... **fails.** He was wrong — or rather, *premature*. The Wrong Inference table (Mythic Backlash, P4) fires, delayed-reveal: the raid hits an empty theatre (Castaigne anticipated them), and in the dark Marcus glimpses the rite's reflection — gains **1 Corruption** (ties to `workshop/07`). The clock jumps +2 (now 4) as the real rite proceeds elsewhere, and the push **burns** 1 soft clue (the party's theory is now public and muddied). They must race the last two clock segments with a thinner pool — and now they *know* they were wrong, so the true Conviction is still in reach if they earn the final clue fast.

**Why this works in noir/cosmic horror:** the **hard/soft split** models the genre's core pleasure — the *specific damning detail* (the fiber, the tailor) is what cracks the case, not generic legwork. The **delayed wrong-inference reveal** produces the noir staple of the bad hunch that costs you. The **harm/Corruption push cost** ties investigation to the doom spiral: *thinking about the mythos hurts*, so pushing an inference is a literal bargain with ruin — exactly the cosmic-horror thesis that *knowledge has a price*. The Threat Clock makes every clue-earning phase a gamble against the summoning, so the push is always tempting and never safe.

**Re-skin for your genre:**
- **Procedural police drama:** drop the mythic cost; push cost = narrative (wrongful arrest, IA complaint, case closed); clock = the killer strikes again; hard clues = forensic evidence ANALYZE'd by the lab.
- **Academic conspiracy thriller:** menu = ARCHIVE / INTERVIEW / TRANSLATE / FIELDWORK / CROSS-REFERENCE / SECURE FUNDING; clock = a rival team publishing first; push = a risky public claim that may be retracted.
- **Monster-hunter (e.g., witch-hunting dark fantasy):** push cost = Corruption (`workshop/07`); RESEARCH reveals the creature's *type* (vulnerabilities); the conviction gates whether you bring the right bane to the fight.
- **Espionage / counterintel:** menu = BUG / TURN / BREAK / TAIL / ANALYZE / RUN COVER; clock = the mole exfiltrates; hard clue = the documented dead-drop; push = acting on thin intel, burning an asset if wrong.
- **Frontier mystery (Western):** menu = TRACK / ASK / RIDGE-SCOUT / CORRAL-WATCH; clock = the gang rides out at dawn; push = accusing the wrong homesteader (a hanging).
