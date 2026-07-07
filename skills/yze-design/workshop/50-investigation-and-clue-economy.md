<!-- markdownlint-disable MD013 MD024 -->

# Investigation & Clue Economy — Clues as Currency

> **STATUS: WORKSHOP MODULE.** Treats clues as a spendable currency refueled by an investigation activity menu, with a risky-inference *push* that gates revelations behind player-driven inquiry — not a single Insight roll. *Core is generic; the worked example (noir / cosmic horror) is illustrative.*

## Contents

1. Origin — how this was built
2. The generic mechanism
3. The pressure loop
4. Dials
5. Integration points
6. Failure modes & edge cases
7. Validation notes
8. Worked genre example — Noir / cosmic horror

## 1. Origin — how this was built

- **Source primitives:** **P2 (capped metacurrency refueled by risk)** — clues as the spendable pool; **P6 (activity menu)** — the investigation activities that *earn* the pool; **P1 (push-and-pay)** — the risky inference that *spends* the pool on a gamble; **P4 (typed D66)** — what a wrong inference costs (the backlash / fallout table). Optionally **P5 (resource die)** as an alternative pool model (see Dials).
- **Reinvention operator:** **Domain Transfer (P2) + Fusion.** Domain-transfer P2 from "personal resolve" (WP/Faith) to "evidence gathered" — clues *are* a capped pool that spends on agency (here: the agency to *act on a conclusion*) and refuels from engaging the system's risk mechanics. Then **fuse** P6 + P2 + P1: the activity menu *earns* the pool; spending the pool *unlocks* certainty; the push *spends* the pool on a gamble when certainty is short. The fusion produces a loop none of the primitives makes alone — mystery-solving as resource management.
- **Target psychology:** **Action-refuel** (`17` M1, action-earned column) — fuel comes from *doing the investigation*, so the game becomes *about* investigating. The push cost is **narrative/Trouble** (`17` M2) by default — a wrong inference makes the *story* worse (a false accusation, a contaminated scene), not the body — recalibrable to **harm/corruption** for horror.
- **Problem solved:** investigation in most RPGs is either (a) a single "Insight" or "Investigation" roll that hands the player the answer (no process, no texture, and a failed roll bricks the mystery — the classic brick-wall failure), or (b) pure GM-narrated deduction where the rules offer nothing and "finding the clue" is down to whether the player phrases the right question. This module gives deduction the same dramatic rhythm the push economy gives combat: a pool that fills from *what the players choose to do*, spends on *confidence to act*, and can be *gambled* when time runs short — so that "we don't know yet" is a *decision*, not a dead stop.

## 2. The generic mechanism

### When it triggers

The Clue Economy is **not** for every search. It triggers when:

1. There is a **hidden truth** (a culprit, a motive, a plan, a nature) the PCs must uncover to act.
2. Time is **finite** — a threat advances while they investigate (see the Threat Clock below).
3. Being wrong has **consequence** (a false accusation, a wasted raid, a ritual completed).

For "do I find the key on the desk," use a single roll (`03 §11` / the core search rule). Reserve the Clue Economy for mysteries that *deserve* a scene — the engine's same gating instinct as Social Combat (`workshop/30`).

### The Clue pool (P2)

**Clues** are a party-shared pool (cap ~8) representing solid evidence gathered — not abstract "points," but fictional facts the table has named ("the robe fiber," "the gardener's alibi gap"). Spending a clue means *deploying that evidence* to firm up a conclusion.

- **Soft clues** — ordinary evidence. Interchangeable; any soft clue counts toward any revelation's cost.
- **Hard clues** — specific, *required* evidence. Some revelations demand a *named* hard clue, not just N clues (see "Buying certainty" below). The hard/soft split is the module's anti-brute-force spine (§6).

### Alternative pool form — clues as a resource die (P5)

Instead of a counted pool (cap 8), clues can be tracked as a single **Evidence die** (D6–D12, Domain Transfer of P5). Each *spend* (buying a revelation, or the gap-cost of a push) **rolls** the Evidence die; on a 1–2 it steps *down* (D12→D10→...). Earning clues at a rich scene or via ANALYZE steps it *up*. At D6 + 1–2, the evidence is **exhausted** — the party has run the trail dry and must push or rest the case.

This trades precision for texture: you stop counting clues and instead *feel the evidence thinning* — which suits a grim, attritional mystery (the "cold case" feel) where bookkeeping is unwanted. The hard/soft split and the failure-yields-a-lead valve work identically on top of either form; only the counting changes. Choose the counted pool for tactical deduction, the resource die for atmospheric investigation.

### The investigation activity menu (P6)

The mystery is investigated in **Investigation Phases** — structured time blocks (an evening of work, a day of legwork) exactly analogous to a travel Quarter Day (`06 §5`). Each phase, each PC picks **one** activity from the menu. The menu is built so the demands are *mutually exclusive* — the party is always short of hands, and distributing labor is the core tactic (P6's signature tension).

| Activity | What it does | Earns |
| --- | --- | --- |
| **SEARCH** | Comb a location for physical evidence | Soft clues (+ a hard clue on a strong success / at a rich scene) |
| **QUESTION** | Interview a witness, suspect, or contact | Soft clues (+ leads to new scenes) |
| **RESEARCH** | Archives, lore, contacts, public records | Soft clues (+ the *type* of threat, if applicable) |
| **SURVEIL** | Tail, stake out, observe a person/place | Soft clues (+ a hard clue: a witnessed act) |
| **ANALYZE** | Cross-reference existing clues (lab work, collation) | Converts soft → hard; clarifies what a clue *means* |
| **WATCH / COVER** | Guard the party's flank against interference | No clues — instead **reduces the Threat Clock tick** this phase |

Each activity is a core ability roll (P1, `00 §3`). Read on the success ladder (P3): ⚔ earned scales the clue yield; a failure still yields **one soft clue** (a hunch, a lead) — the menu never returns *nothing*, which is the anti-brick-wall guarantee (§6). **Core clues** — evidence the plot *requires* to advance — auto-succeed on the activity: the game never gates a must-have behind a roll.

### Buying certainty (P2 spend)

Revelations have a **Clue Cost** — a threshold of evidence the party must deploy to act on a conclusion with confidence. Spending clues to meet the cost = converting evidence into *certainty*; the GM confirms the conclusion as true.

| Revelation tier | Cost | Example |
| --- | --- | --- |
| **Connection** (a single link) | 1–2 soft | "The victims all attended the same theatre." |
| **Conclusion** (the shape of the truth) | 3–4 soft | "The disappearances are ritual sacrifices." |
| **Conviction** (who / where / how, actionable) | 4–5 + a named **hard clue** | "Castaigne is the cult leader; the rite is tonight at the theatre." |

The hard-clue requirement on Convictions is what stops brute force: you cannot buy "who did it" with filler evidence — you need the *specific* damning fact (ANALYZE exists to manufacture hard clues from soft ones).

### The push — risky inference (P1)

If the party is short of a revelation's cost and wants to act *now* (because the Threat Clock is rising), any PC may **push an inference**: declare a hypothesis beyond the evidence and roll the gap.

- Declare the inference. Roll an ability pool sized to the *gap* (missing clues) — typically Wits + Investigate, GM-set threshold.
- **Success** — you were right. Brilliant intuition / lucky leap. The conclusion is confirmed *as if spent* (no clue cost).
- **Failure** — you were wrong, and you've committed to the false conclusion. The cost fires: roll on the **Wrong Inference** table (P4, typed D66) — what being wrong *costs* you. And a failed push can **burn clues**: having loudly committed to a theory, you've muddied the evidence (lose 1–2 soft clues).

This is the engine's signature beat transplanted: the push converts "we don't have enough" from a dead-end fail into a *priced decision* — exactly as it does for a missed attack. One push per conclusion.

### The Wrong Inference table (P4)

A failed push rolls a **typed D66** (Domain Transfer of P4 from crits/mishaps to "deductive error"). Tens = *what the error wastes or exposes*; Units = *severity*. Families are typed by genre/cost — here the **Procedural** family (narrative cost):

| Tens (what's wasted) | Units 1–2 (minor) | Units 3–4 (costly) | Units 5–6 (severe) | 65/66 (climax) |
| --- | --- | --- | --- | --- |
| **1–2 TIME** (a wasted raid) | A wasted evening | A squandered phase | The threat advances +2 | The window closes |
| **3–4 EVIDENCE** (a burned clue) | A lead goes stale | −1 soft clue | −2 soft, a scene contaminated | The trail dies |
| **5–6 EXPOSURE** (you tipped the culprit) | The culprit is wary | The culprit accelerates | A witness silenced | The culprit comes for you |

For cosmic horror, swap to the **Mythic** family (harm/Corruption cost: glimpsed rite → 1 Corruption; echoed chant → nightmares/attribute damage; the 65/66 climax = a permanent Mythos touch). This is the same one-architecture-many-payloads trick as FL's crit families (`M3`): the *kind* of wrongness the genre cares about becomes the story.

### The Threat Clock (pressure source, P15)

The mystery runs against a **Threat Clock** (a P14/faction-clock analog): a track (typically 6 segments) representing the antagonist's advancing plan. Each Investigation Phase ticks it +1. At full, the threat *fires* — the ritual completes, the killer strikes again, the trail goes cold. The clock is what makes *earning more clues* costly (it costs *time*) and what makes the *push* tempting (it costs *no time* but gambles correctness). The **WATCH / COVER** activity is the pressure-relief valve — trade clues this phase to slow the clock.

## 3. The pressure loop

- **Pressure:** the Threat Clock rises each phase; clues are finite; hard clues are scarce and must be *found* (not bought).
- **Decision:** *do we spend a phase earning more clues (safe, but the clock ticks), or push the inference now (risky, but free of time)? do we deploy our hard clue here or save it for the conviction?*
- **Consequence:** certainty bought (safe action) vs inference pushed (gambled action); clock advances; wrong inferences backlash and burn clues.
- **State change:** the hidden truth narrows; the antagonist's plan advances; the party's evidence and exposure both shift.
- **Loop shape:** **investigate → accumulate → conclude (spend) or push (gamble) → backlash/reward → act.** Runs at Phase cadence (slower than a Round; faster than a session) — a *strategic-deductive* resource.

## 4. Dials

| Dial | Setting A | Setting B | Psychology produced |
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

- **Hooks into:** the social-conflict system (`03 §11`) — QUESTION is a social roll and can escalate into a full Social Combat (`workshop/30`) when an interview is high-stakes. Hooks into harm (`04`) — a harm-cost push (dial above) deals real damage; the Wrong Inference table (P4) is a sibling of the crit families. Hooks into travel/downtime (`06 §5`) — an Investigation Phase is structurally a Quarter Day and can nest inside one. Hooks into the faction web (`workshop/20`) — investigations *into* a faction shift Standing when concluded. Hooks into **Corruption** (`workshop/70`) — a mythic-cost push can climb the corruption ladder (the worked example uses this).
- **Requires:** a defined hidden truth (the GM knows who/what/why); a Threat Clock; a set of clue sources (locations, witnesses, records) the menu activities can target.
- **Replaces / extends:** the single "Insight"/"Investigation" roll — adds the economy and the push for mysteries that warrant a scene, leaving simple searches on the single roll.
- **Cross-refs:** `16` P1/P2/P4/P6 (+ P5 optional); `17` M1 (action-refuel) and M2 (push-cost type); `13 §8` (validation pipeline); `19` FE1/FE4 (the two failures this is engineered around).

## 6. Failure modes & edge cases

- **"The mystery is now solvable by brute force."** *(The critical investigation-design failure.)* If clues are too easy to farm, players grind activities to cap and buy the answer — deduction collapses into a resource tally, and the mystery has no teeth. **Fix (three layers):** (a) the **Threat Clock** makes every extra phase cost time the antagonist uses — grinding is not free. (b) **Clue decay:** witnesses go cold, scenes get contaminated — soft clues earned more than ~2 phases ago can't be spent (the GM marks them stale). (c) The **hard/soft split**: Convictions require a *named* hard clue, which cannot be brute-forced — you can't buy "who did it" with filler, you must *find the specific damning fact* (and ANALYZE it). (`13 §5.5` action-economy-abuse variant; `19` FE1 — if everything is buyable, the deduction is a false choice.)
- **"Players stuck with no clues."** *(The other critical investigation-design failure — the brick wall.)* If rolls fail and clues run dry, the party hits a dead end with nothing to spend and no way forward. **Fix (the module's built-in escape valves):** (a) the **push exists precisely for this** — you can always gamble an inference with zero clues; "stuck" is never terminal, it's a *priced decision*. (b) **Failure yields a lead:** a failed activity still produces one soft clue (a hunch, a new direction) — the menu never returns nothing. (c) **Core clues auto-succeed** — plot-critical evidence is never gated behind a roll. (`19` FE4 agency-collapse: a rule that removes the player from meaningful play; C3 flow channel — preserve a recovery/re-engagement valve.)
- **The face monopolizes.** If only the high-Insight/high-social PC earns clues, the rest watch. **Fix:** the activity menu is the cure by construction — P6's labor distribution guarantees every PC an investigation job (the muscle SURVEILs, the scholar RESEARCHes, the tough guards via WATCH). Ensure no activity is always-optimal.
- **"The push is always wrong" (or always right).** If pushing is reliably punished, players never gamble and the signature beat never fires; if reliably safe, it replaces earning. **Fix:** the push's success chance must be *real* (recompute the gap; a 1–2 clue gap should be rollable, not hopeless), and the cost *proportional* — not catastrophic-by-default. One push per conclusion prevents push-spam.
- **Brute-forcing the push.** Players push every inference to skip earning. **Fix:** failed pushes **burn clues** (you've muddied the evidence by committing to a theory) and the Wrong Inference costs *accumulate* (false accusations compound; mythic backlash stacks toward Corruption). Pushing is for when you *must* act short — not a free substitute for legwork.
- **The GM-fiat threat.** If the Threat Clock advances on GM whim, the pressure feels rigged (`19` FE5 "too unfair"). **Fix:** the clock ticks on a *defined* trigger (+1 per phase, full stop) and WATCH reduces it on a *defined* roll — never on mood.

## 7. Validation notes

- **Math (`13 §3` / `§8` Stage 1):** clue-earning rate vs revelation costs should be tuned so a typical mystery resolves in 3–5 Investigation Phases (mirroring a 3–5 Round combat). At graded earning (~2–3 clues/phase across a party of 3–4) and Connection/Conclusion/Conviction costs of 2/4/5, a party reaches a Conclusion in ~2 phases and a Conviction in ~3–4 — provided they secure the hard clue. If mysteries drag, lower costs or raise earning; if they collapse too fast, raise the hard-clue bar or speed the clock.
- **Exploits (`13 §5` / Stage 2):** the brute-force risk is the main one — gated by the hard/soft split + Threat Clock + clue decay (three independent brakes, deliberately redundant). Push-spam is gated by clue-burn-on-fail + accumulating backlash. Verify a party cannot farm WATCH indefinitely (WATCH earns no clues, so it stalls deduction even as it slows the clock — a real tradeoff, not an exploit).
- **Synergy (`13 §7` / Stage 3):** the module hooks cleanly because it reuses P1/P2/P6 — no new dice type, no parallel economy. The one synergy to watch: a harm-cost push stacking with Corruption (`workshop/70`) can spiral faster than either alone — recompute the doom curve if both are on.
- **Felt experience (`19` §7 Stage C):** the **push** is the key psychology — it turns "we lack evidence" into a *decision*, defeating FE4 (agency collapse / the brick wall). The **hard/soft split** defeats FE1 (false choice): if every conclusion were buyable with filler, deduction would be meaningless. The **failure-yields-a-lead** valve preserves C3 (flow channel) — there is always a next move. Wrong Inference tables should be telegraphed (C2 perceived randomness): the GM foreshadows that a theory is thin before the push, so a wrong result feels *earned*, not random.

## 8. Worked genre example — Noir / cosmic horror

**The setting:** A gaslit 1920s city. Investigators pursue a cult of the Yellow Sign kidnapping victims for a summoning. Each phase the **Summoning Clock** (6 segments) advances; at 6, the King in Yellow manifests. Pushing a *wrong* inference doesn't just waste a raid — it exposes the pusher to mythic backlash (gaining **Corruption**, `workshop/70`).

**Dials set:** party-shared pool cap 8; graded earning (1–3 by ⚔); **hard/soft split ON**; failure-yields-a-lead ON; push cost = **harm/Corruption** (Mythic Backlash table, P4); wrong-inference reveal **delayed** (you act on the false theory — the twist lands later); threat clock +1/phase.

**The menu:** SEARCH / QUESTION / RESEARCH / SURVEIL / ANALYZE / **WARD** (the WATCH equivalent — wards the party against mythic attention, −1 clock tick, no clues).

**In use (excerpt):**

- **Phase 1** (clock 0→1). The party distributes labor. **Eleanor** SEARCHes the latest crime scene — Wits 4 + Investigate 2 = 6 dice, 2⚔ → earns 2 soft clues *and* finds a **hard clue**: a yellow silk robe-fiber caught on a nail. **Marcus** QUESTIONS the night-watchman — Empathy 3 + Manipulation 2 = 5 dice, 1⚔ → 1 soft clue (the watchman recalls a theatrical carriage) + a lead to the livery. **Sven** SURVEILs the suspect boarding house — fails the roll, but still gets **1 soft clue** (a hunch: visitors arrive only after midnight). **Mira** WARDS — earns no clues, but holds the clock to +1 (now 1). Pool: **4 soft + 1 hard** (the fiber).
- They spend 2 soft to buy the **Connection**: "the victims all attended the Castaigne Theatre." Confirmed. (Pool: 2 soft + 1 hard.)
- **Phase 2** (clock 1→2; Mira wards again, holds to 2). Eleanor **ANALYZEs** the robe-fiber — cross-references theatrical costumers. Success → the fiber traces to Castaigne's private tailor; this *converts* to a second hard clue ("the robe is Castaigne's") + 1 soft. Now they could reach the **Conviction** "Castaigne is the cult leader; the rite is tonight" — cost 4 + the named hard clue. They have 3 soft + 2 hard, but the Conviction needs *4 soft* alongside the hard clue. They are one short.
- **The push.** The clock is at 2 and rising; Marcus's player doesn't want to spend a Phase 3 earning one more clue. He **pushes the inference**: "It's Castaigne — we raid the theatre tonight." Roll the 1-clue gap: Wits 3 + Investigate 2 = 5 dice vs threshold 2... **fails.** He was wrong — or rather, *premature*. The Wrong Inference table (Mythic Backlash, P4) fires, delayed-reveal: the raid hits an empty theatre (Castaigne anticipated them), and in the dark Marcus glimpses the rite's reflection — gains **1 Corruption** (ties to `workshop/70`). The clock jumps +2 (now 4) as the real rite proceeds elsewhere, and the push **burns** 1 soft clue (the party's theory is now public and muddied). They must race the last two clock segments with a thinner pool — and now they *know* they were wrong, so the true Conviction is still in reach if they earn the final clue fast.

**Why this works in noir/cosmic horror:** the **hard/soft split** models the genre's core pleasure — the *specific damning detail* (the fiber, the tailor) is what cracks the case, not generic legwork. The **delayed wrong-inference reveal** produces the noir staple of the bad hunch that costs you. The **harm/Corruption push cost** ties investigation to the doom spiral: *thinking about the mythos hurts*, so pushing an inference is a literal bargain with ruin — exactly the cosmic-horror thesis that *knowledge has a price*. The Threat Clock makes every clue-earning phase a gamble against the summoning, so the push is always tempting and never safe.

**Re-skin for your genre:**
- **Procedural police drama:** drop the mythic cost; push cost = narrative (wrongful arrest, IA complaint, case closed); clock = the killer strikes again; hard clues = forensic evidence ANALYZE'd by the lab.
- **Academic conspiracy thriller:** menu = ARCHIVE / INTERVIEW / TRANSLATE / FIELDWORK / CROSS-REFERENCE / SECURE FUNDING; clock = a rival team publishing first; push = a risky public claim that may be retracted.
- **Monster-hunter (e.g., witch-hunting dark fantasy):** push cost = Corruption (`workshop/70`); RESEARCH reveals the creature's *type* (vulnerabilities); the conviction gates whether you bring the right bane to the fight.
- **Espionage / counterintel:** menu = BUG / TURN / BREAK / TAIL / ANALYZE / RUN COVER; clock = the mole exfiltrates; hard clue = the documented dead-drop; push = acting on thin intel, burning an asset if wrong.
- **Frontier mystery (Western):** menu = TRACK / ASK / RIDGE-SCOUT / CORRAL-WATCH; clock = the gang rides out at dawn; push = accusing the wrong homesteader (a hanging).
