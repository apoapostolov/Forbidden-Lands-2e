<!-- markdownlint-disable MD013 -->

# Recipes — New Game, New Rule

> **STATUS: FILLED (Pass-2).** This is the SYNTHESIS file that makes the skill actionable end-to-end. Two cookbooks: Recipe A builds a new YZE game for any genre; Recipe B designs and validates a single new rule or subsystem. Both are step lists whose every step cites the reference file that owns the deep detail — this file owns the *go build one*, the siblings own the *how each system works*. Read alongside `10-design-philosophy.md` (the gate every step's output must pass) and `13-balance-and-synergy.md` (the validation engine both recipes end in).

## Contents

1. Source provenance
2. Abstraction target
3. Recipe A — Build a new YZE game for any genre
4. Recipe B — Design and validate a new rule/subsystem
5. Worked examples
6. Design intent

## Source provenance

Synthesis file — draws on all of `00`–`13`. Primary evidence is the two corebooks (each is itself a *worked example* of building a YZE game for a genre): Forbidden Lands 2E (FL) = dark-fantasy survival; Tales of the Old West 2E (West) = historical Western. The two games are the calibrated reference answers at nearly every step.

## Abstraction target

Two **cookbooks** that make the skill operational, not just descriptive:

- **Recipe A — Build a new YZE game.** A 15-step procedure for going from "I want a YZE game in genre X" to a *playable skeleton*. Each step names the decision to make, gives the calibrated FL/West reference answer, points to the reference file + dial that owns the deep detail, and ends with a one-line "what you have when this step is done."
- **Recipe B — Design + validate a new rule.** The end-to-end maker's pipeline (intent → math → exploit → synergy → table → layer → verdict), restated as a numbered checklist with worked stubs and the ship/revise/reject decision logic. Full detail in `13-balance-and-synergy.md` §8; this file restates it as the *go do it* list.

Apply the Abstraction Ladder to: each step's decision, the two games' choices as reference answers, and the trade-offs. The recipes exist so a designer can start at Recipe A step 1 and reach a playable skeleton, or Recipe B step 1 and reach a validated rule, **using only this skill.**

---

## 3. Recipe A — Build a new YZE game for any genre

> **How to use this recipe:** Run the steps in order. Each step is one design decision plus a pointer to where the deep work happens. Do not try to perfect a step before moving on — the recipe produces a *skeleton*; you validate the whole skeleton in step 15 and iterate. Steps 1–2 set the tone everything else inherits; steps 3–11 are parallel dial-settings (you can draft them in one pass); steps 12–14 are authoring; step 15 is the gate.

### Step 1 — State the thesis (ambition-to-exposure tension)

**Decision:** Name the genre's *ambition* and its *exposure* in two physical, credible nouns. The two answers name the game's **currency** (what players spend/risk) and its **adversary** (what the world taxes them with).

**Reference answer:**
- **FL:** ambition = loot and legend; exposure = the land (cold, hunger, the hex, the monster). Currency = *the body and the supply.*
- **West:** ambition = pay, a name, a stake, survival past winter; exposure = the country's indifference (the gun, the distance, the fever, the debt). Currency = *grit and belief (Faith).*

**Where FL and West land:** FL is *ecological* (the land is the adversary); West is *documentary* (indifference is the adversary). Both answers must be felt as pressure, not read as flavor.

**If you cannot fill both blanks with physical nouns, the genre is not ready for the engine.** This single sentence governs every later step — any rule that doesn't serve the thesis doesn't belong in the game.

**Detail lives in:** `10-design-philosophy.md` §3 (core identity), §12 instantiation recipe dial 1. **What you have when done:** a one-sentence thesis that will anchor every flavor and balance choice. → `10`

### Step 2 — Name four attributes expressing the genre's tension + damage types

**Decision:** Name four attributes, each one an *axis of the genre's pressure* (not generic STR/DEX/INT/CHA unless that's genuinely the genre). Then name each attribute's **damage type** with a genre noun.

**Reference answer:**
- **FL:** Strength / Agility / Wits / Empathy — survival axes. Damage typed *silently* by what kind of harm (sword→Strength, fear→Wits).
- **West:** Grit (Hurts) / Quick (Shakes) / Cunning (Vexes) / Docity (Doubts) — frontier-competence axes, each with a *named* damage type.

**The naming is free genre-loading.** West's "you suffer 2 Hurts and a Vex" reads in-genre; "−2 to two stats" does not. **Always name the damage types** even if the mechanic is silent (West-style is the maximal version, FL-style the minimal).

**Detail lives in:** `01-character-model.md` §3 (the 4×4 grid), §4 (per-attribute damage types), §10 instantiation recipe steps 1–2. **What you have when done:** a 4-row attribute table with a damage-type name per row. → `01`

### Step 3 — Write 16 skills (4 per attribute), in-genre names

**Decision:** Write four skills under each attribute — the genre's four ways of *expressing* that attribute's tension. Name them in-genre. **Skill names do ~60% of the work of re-skinning YZE for a new genre.**

**Reference answer:**
- **FL:** Strength → Might, Endurance, Melee, Crafting; Agility → Stealth, Sleight of Hand, Move, Marksmanship; Wits → Scouting, Lore, Survival, Insight; Empathy → Manipulation, Performance, Healing, Animal Handling.
- **West:** Grit → Fightin', Labor, Presence, Resilience; Quick → Light-Fingered, Move, Operate, Shootin'; Cunning → Animal Handlin', Hawkeye, Insight, Nature; Docity → Booklearnin', Doctorin', Makin', Performin'.

**Validate:** does each attribute have four *distinct, non-overlapping* skills? Does every skill route to exactly one attribute? The 4×4 grid is load-bearing symmetry — keep it exactly 16.

**Detail lives in:** `01-character-model.md` §3, §10 step 3. **What you have when done:** a filled 4×4 grid (attribute → 4 skills). → `01`

### Step 4 — Pick the metacurrency model

**Decision:** Choose the push-cost model + the metacurrency refuel + the protected-dial model. This is the **single choice that sets tone more than any other.**

**Reference answer:**
- **FL:** **Bane-self-harm** push cost (body/gear pay, no currency spent to push) + **harm-refueled** metacurrency (Willpower Points, cap 10, +1 WP per 💀 on Base Dice when pushing) + **Pride** (a die, narrow scope, once/session).
- **West:** **Currency-spend** push cost (1 Faith per push) + **action/success-refueled** metacurrency (Faith, cap 10, 4/scenario) + **Faith-as-currency** (broad scope, fuels the whole push/trouble loop).

**Recommended for new games:** **hybrid** — a currency cost *plus* a lighter bane/Trouble trigger, so pushing always costs something visible but isn't always injurious; a small currency pool *plus* an escalating once-session die. Keep the **virtuous loop** intact (risk must refuel agency) — never sever refuel from the risk that earns it.

**Detail lives in:** `00-engine-core.md` §6 (the two cost models), §7 (metacurrency abstraction), §11 dials 1–5; `01-character-model.md` §5 (Pride/Faith); `11-design-dials-and-variants.md` (metacurrency + failure dials). **What you have when done:** a one-paragraph metacurrency rule (cap, refuel trigger, what it buys) consistent with the push-cost model. → `00`, `11`

### Step 5 — Pick the failure-pressure model

**Decision:** Choose how failure taxes the roll — and make it *consistent* with step 4.

**Reference answer:**
- **FL:** **Banes** (💀 baked into Base/Gear dice faces, always active on push) — mechanical, endogenous, feels inevitable.
- **West:** **Trouble tables** (Safe/Risky/Desperate exposure frames, narrative outcomes) — frame-gated, feels *chosen*.

**Pairing rule:** bane-self-harm (step 4) pairs naturally with banes; currency-spend pairs with Trouble. Don't cross the streams without intent. A lighter option: Trouble + a bane-free pool (the lightest failure tax that still bites).

**Detail lives in:** `00-engine-core.md` §10 dial 10 (failure-pressure layer), the divergence rows; `11` failure-pressure dial. **What you have when done:** a stated failure-pressure layer consistent with the push-cost model. → `00`, `11`

### Step 6 — Set the conflict model

**Decision:** Set the action-economy engine: time units (Round/Turn/Shift), initiative method, positioning model, the slow/fast action budget, reactive-defense layer, conflict modes, and whether to include a *ceremonial* mode.

**Reference answer:**
- **FL:** Round (~15s)/Turn (~15 min)/Quarter Day; **rolled-sticky** initiative (AGILITY+WITS → segment, with delay); **zones + range bands + reach-band subsystem** (Short/Normal/Long reach); slow/fast = (1 slow + 1 fast) ∨ (2 fast); dodge (MOVE)/parry (MELEE); melee is *verb-rich* (Slash/Stab/Punch); ceremonial mode = **ambush/sneak-attack**.
- **West:** Round (5–10s)/Turn (5–10 min)/Shift (6h, 4/day); **card-draw** initiative (Aces high, redrawn each Round); **cover ratings + to-hit grades + 6 range bands**; same slow/fast budget; block/dodge with *counterattack*; melee is *modifier-rich* (single verb + All-Out/Called); ceremonial mode = **the Duel** (Face Off → Go for Your Guns → Shoot-off).

**The load-bearing rule:** the **two-actions-per-Round budget** (1 slow + 1 fast, or 2 fast) — both games use it verbatim; keep it. Reactions draw from the same budget (no free infinite defense). **Include at least one ceremonial mode** for the genre's signature beat — it's optional but every genre benefits from one.

**Detail lives in:** `03-conflict-and-combat.md` (entire file — time units §3, initiative §4, positioning §5, reach §6, action budget §7, reactions §8, melee §9, ranged §10, social §11, ceremonial §12); `11` action-economy dial. **What you have when done:** a conflict chapter skeleton — time units, initiative, range/zone model, action menu, defense verbs, ceremonial mode. → `03`

### Step 7 — Set the harm model

**Decision:** Set the layered cascade: attribute-as-HP mapping, critical-injury architecture (typed families vs single master table), lethality climax (`65`/`66`), death model, stabilization, conditions set, environmental hazards, healing cadence, retirement path.

**Reference answer:**
- **FL:** single-attribute-per-source damage; **family of 8 typed D66 critical-injury tables** (Slash/Blunt/Stab/Burn/Acid/Cold/Swallow/Horror) — *the table family is a genre-commitment device*; hard-time-limit death; 5 conditions (Hungry/Thirsty/Sleepy/Cold/Addicted); slow recovery; explicit retirement-as-retainer-NPC path.
- **West:** paired-attribute split (Hurts/Shakes, Doubts/Vexes); **single master D66 table** indexed by body location × severity; periodic un-pushable Death roll; 5 conditions (Starving/Dehydrated/Exhausted/Freezing/Heatstroke, the last imposes Trouble on all rolls); rated environmental hazards (Intensity/Blast Power/Potency/Virulence); faster recovery (1/Turn).

**The signature choice:** which harm types get their own D66 family? That list *is* a portrait of the genre's threats. Port the D66 architecture + `65`=maim / `66`=die climax as-is; write genre-specific rows.

**Detail lives in:** `04-harm-and-consequences.md` (entire file — esp. §5 the Critical-Injury table engine, §5.4 the typed-family recipe, §12 instantiation recipe). **What you have when done:** a harm chapter skeleton — damage mapping, crit table family set, death/stabilization, conditions, recovery tempo, retirement path. → `04`

### Step 8 — Decide the power layer (none/low/medium/high)

**Decision:** First, does the genre need powers at all? If no → **None** (you're done with this step; the engine is complete without it — West is your proof). If yes, pick a density and select taxonomy tiers, casting model, fuel, mishap layer, rank ladder, epic tier.

**Reference answer:**
- **FL:** **High** — all three taxonomy tiers (Spells/Power Words/Rituals), all three casting models (safe/chance/overcharge), metacurrency+Burn fuel, 17 per-discipline mishap families, rank 1–6, full epic-ingredient economy.
- **West:** **None** — no power layer exists. The nearest analogue (Faith) is a *metacurrency*, not a power source.

**The decision procedure:** None → specialist/universal → taxonomy tiers → casting models → fuel+cost → mishap layer → rank ladder → epic tier (in that order). Low = reskins (gadgets/psi/miracles); Medium = sword & sorcery / urban fantasy; High = mythic high fantasy. Fuel is *always* the core metacurrency — that's what binds the layer to the engine.

**Detail lives in:** `05-power-layer.md` §10 (the density decision table — *this file's central deliverable*), §11 divergence; `11` power-density dial. **What you have when done:** either a clear "no power layer," or a power-layer spec (density, tiers, casting, fuel, mishap, ranks, epic y/n). → `05`, `11`

### Step 9 — Pick the travel model

**Decision:** Choose the spatial model (hex/pointcrawl/hybrid), the time block, activity-menu breadth, and weather/environmental depth. Then weight the **Expedition loop** as primary or secondary.

**Reference answer:**
- **FL:** **hex-crawl** (10 km tiles, terrain types, tile-by-tile procedures); Quarter Day (4/day) with daily-roll checklist; **14-activity formal menu** (HIKE/LEAD THE WAY/KEEP WATCH/FORAGE/HUNT/FISH/SURVEY/MAKE CAMP/REST/SLEEP/TRAIN/CRAFT/REPAIR/EXPLORE); deep weather (Wind/Rainfall/Temperature). Expedition loop = *primary.*
- **West:** **pointcrawl** (mileage-between-points, lighter); Shift (6h); ~6–8 implicit activities; regional weather killers (blue norther/chinook/drought/haboob); deep mounted/animal labor. Expedition loop = secondary.

**The most transferable artifact:** the **activity-menu architecture** — distribute the party's labor across a fixed menu so every PC has a travel job, and *movement/navigation/security/supply are mutually exclusive demands*. Port the carry model (primary physical attribute × 2 + heavy/light/tiny) and adopt **Resource Dice** for consumables.

**Detail lives in:** `06-travel-and-downtime.md` (spatial model §3, time block §4, activity menu §5, weather §7); `11` travel-spatial dial. **What you have when done:** a travel chapter skeleton — spatial model, time block, activity menu, weather depth, carry/resource-die rules. → `06`, `11`

### Step 10 — Pick the org model

**Decision:** Decide which scale rungs to enable (solo → party → band → company → faction → army → polity), whether to turn on the faction turn, and whether to include mass combat. Weight the **Base loop** accordingly.

**Reference answer:**
- **FL:** full ladder — Stronghold (base org) + Mercenary Company (band org) + Factions/Legacies (high-scale org, with **Faction Turn**) + mass combat/sieges. Base loop = *primary.*
- **West:** personal/small-org scale — Business/Property + Your Town (settlement-as-character) + Outlaw Band (band org). No faction turn, no mass combat. Base loop = secondary.

**Every org runs the same five-beat lifecycle:** founding → functions → upkeep → events → scale escalation. Enable only the rungs the genre/campaign-length needs; a one-shot needs none, a hex-crawl campaign wants the base rung, a domain game wants them all.

**Detail lives in:** `07-base-faction-mass-scale.md` (the lifecycle pattern §3, scale ladder §9, instantiation recipe §11); `11` faction/mass-combat dial. **What you have when done:** a stated set of enabled org rungs + (if any) a base-org spec. → `07`, `11`

### Step 11 — Pick the economy model

**Decision:** Choose the economy form (barter/cash/cash+capital), the **feature grammar** tag set for weapons/armor, the crafting gating (talent/workshop/time/material), and the quality/condition/artifact tiers.

**Reference answer:**
- **FL:** **barter + silver** (gold ceremonial); weapon/armor defined by **composable feature tags** (Edged, Pointed, Polearm, Parrying, Pierce Armor…); crafting is talent-gated + workshop-gated + time-gated + material-gated; quality tiers (Crude/Standard/Fine) + artifact die (D8/D10/D12).
- **West:** **cash + Capital** ($250 = 1 Capital) with loans/salaries/credit; weapon features as action-type tags (SINGLE/DOUBLE/LEVER/BREECH) + qualities (CALIBRED/RELIABLE…) + conditions (Worn→broken via Trouble); optional Resource Dice for consumables.

**The central reusable artifact:** the **Feature Grammar** — weapons/armor are defined by a small set of composable tags, not bespoke stat lines. The grammar is what lets two swords feel different without inflating numbers. Both games ship near-identical **Availability/Scarcity** tables — port as-is.

**Detail lives in:** `08-gear-and-economy.md` (economy dial §4, feature grammar §6–7, crafting §5, quality/artifact §8–9); `11` economy dial. **What you have when done:** an economy + gear skeleton — money form, availability ladder, feature tag set, crafting gates, quality tiers. → `08`, `11`

### Step 12 — Write the GM layer

**Decision:** Author 5–7 GM principles (de-flavored from the FL seven), an encounter table (D66 terrain-keyed matrix + reoccurring rule), a settlement model (settlement-as-character), the NPC statblock grammar, and the consequence/faction tracks.

**Reference answer:**
- **FL:** the 7 Principles (World Lies Before You / Land Full of Legends / Adventurers Make Their Own Fate / Nothing Is for Free / Them That's Got Shall Lose / Death Is Part of the Story / End Is Never Set); D66 terrain-keyed encounter matrix (44 situational entries); Village generator (history/size/problem/locations/NPCs/vicissitudes/household ledger); minimal NPC statblock; stronghold-event table + faction feuds.
- **West:** same doctrine inherited; generic NPC statblocks (8-column); **Your Town** six-Aspect model (Farming/Mercantile/Natural Riches/Law/Civic/Welfare/Prosperity); **Turn of the Season** fortune rolls; four-track Faction Standing ledger; faction clocks.

**The signature trait:** encounters are *situations, not statblocks* — most can be resolved without combat. The reoccurring rule gives the table memory (continue / change / re-roll).

**Detail lives in:** `09-gm-procedures.md` (principles §3, encounter engine §4, settlement model §5, statblock grammar §6, solo engine §7, consequence tracks §8); `10-design-philosophy.md` §3 (the principles are the philosophy in operation). **What you have when done:** a GM chapter skeleton — principles, encounter table, settlement generator, statblock template, campaign-state tracker. → `09`

### Step 13 — Set advancement

**Decision:** Set the XP-source mix, the talent-ladder depth (the central choice), the cost curves, narrative-access gating, Legacy XP, and (optional) metacurrency→XP.

**Reference answer:**
- **FL:** 1–3 XP/session + lethal +1 / minor +2 / major +4 / downtime 1/season; **deep 5-rank talent trees** (rank × 3 XP with teacher, ×3 without, mentor required); magic paths 1–6; implicit teacher gating; WP→XP conversion (10 WP → 1 XP, optional); Legacy XP; Named Men (NPC parallel).
- **West:** near-identical XP-source mix; **flat 2-rank (Basic/Advanced)** talents; **explicit narrative-access gating** (forge/society/institution); no metacurrency→XP; Legacy XP.

**The converged engine default:** skill cost `(new rank × 3)` XP with teacher, ~×1.33 without, + scaling time cost + self-taught WITS/learning roll. **Make narrative-access gating explicit** (group talents by function; tag self-taught-OK vs needs-teacher) — it's free in-fiction texture.

**Detail lives in:** `02-progression-and-xp.md` (XP models §3, training costs §4, ladder depth §5, instantiation recipe §11). **What you have when done:** an advancement skeleton — XP sources, ladder depth, cost curves, gating, Legacy. → `02`

### Step 14 — Pick optional rules (declare the optional surface)

**Decision:** Explicitly declare which Optional rules are *in* the manuscript and which are out. The optional surface is itself a dial (FL = larger; West = leaner).

**Reference answer:**
- **FL optional surface:** heroic campaigns, artifact/Pride dice, Surge of Willpower (1 XP → 1 WP), stronghold, lifepath book, Morale & Rout.
- **West optional surface:** Fast Initiative, Consumables as Resource Dice, Group Concepts, Resource Die module.

**The discipline:** a rule that *could* be Situational/Optional but is written as General is a **Warning Sign** (subsystem inflation). Tag every rule General/Situational/Optional explicitly. Keep the General layer small enough to hold in working memory.

**Detail lives in:** `10-design-philosophy.md` §9 (the three-tier layering principle), §10a (subsystem inflation warning), §11 divergence (optional-rule surface); `11` optional-surface dial. **What you have when done:** an explicit in/out list of optional rules, each tagged. → `10`, `11`

### Step 15 — Run the validation pipeline on the whole skeleton

**Decision:** Run the skeleton through Recipe B (below) as if it were one large rule. Confirm the **five loops all function** (Expedition/Conflict/Recovery/Metacurrency/Base — weight 2 as dominant), confirm every pressure source has a four-beat loop, confirm the thesis survives, and confirm the whole hits the **balance targets**.

**The balance targets to set first** (these become the dials every later rule validates against):
1. **Default pool size** (competent-character baseline ≈ 4–6 dice).
2. **Competence thresholds** — `T = 0.50` (competent usually succeeds), `T = 0.80` (expert reliably succeeds).
3. **Push-cost model** (step 4) — sets the pushed-column per-die rate.
4. **Metacurrency refuel model** (step 4).
5. **Failure-pressure layer** (step 5).
6. **Lethality & recoverability posture** (step 7).
7. **Power-layer on/off & ceiling** (step 8).
8. **Action-economy granularity** (step 6).

**Check:** does a starting character (≈4-die pool) sit on the 50% competence line? (It should.) Does the metacurrency loop stay symmetric (refuel earned from the same risk that spends it)? Does any rule cross the 50% or 80% breakpoint ungated? If a loop is decorative (no four-beat pressure), cut it or wire it.

**Detail lives in:** `13-balance-and-synergy.md` §10 (set the dials), §4 (breakpoints), §8 (the full pipeline = Recipe B); `10-design-philosophy.md` §5 (the five loops), §4 (resource-at-risk model), §13 (the gate questions). **What you have when done:** a validated, playable skeleton — ready to author into a manuscript. → `13`

---

## 4. Recipe B — Design and validate a new rule/subsystem

> **How to use this recipe:** Start at Stage 0. Run the stages in order. A fail at any stage loops back to *redesign at that stage* — don't push a failing rule forward hoping a later stage fixes it. End at Stage 6 with a verdict. This is the maker's-pipeline restatement of `13-balance-and-synergy.md` §8; the full executable detail (heuristics, fix templates, pattern catalog) lives there.

### Stage 0 — Intent & source check (the gate)

**Do this first. If the rule fails here, stop — don't design it.**

- **[ ] What pressure / decision / loop does this rule serve?** Name the engine loop it touches (Expedition/Conflict/Recovery/Metacurrency/Base) and the pressure source it puts at risk. **If none → REJECT** (subsystem inflation, Warning Sign §10a). A rule with no pressure to relieve and no decision to sharpen is decorative.
- **[ ] Does an existing rule already do this?** Search the sibling that owns the problem. **If yes → REJECT as duplication** or fold into the existing rule. Identify the *chapter that owns the problem* and the *rule type* — a Chapter-8 problem solved in Chapter-6 language, or a talent problem patched with a general rule, is a warning sign.
- **[ ] Write the one-sentence mechanism summary** (strip all flavor): *"Grants 1 WP when the character takes Strength damage."* **If you can't summarize it in one sentence, it does too much — split it.**

**Detail:** `13` §8 Stage 0; `10-design-philosophy.md` §10a–b (subsystem inflation, silent invalidation). → `13`

### Stage 1 — Math

- **[ ] Compute the rule's effect on expected successes.** Does it change `p` (per-die rate), grant successes, or add dice? Recompute the chance-of-success table (`13` §3.3) and the threshold table (`13` §3.4) against the new values. **Never eyeball it** — the engine is mathematically sharp (1/6 → 2/6 per-die jumps a 6-die pool's P(≥1) from 67% to 91%).
- **[ ] Compute the breakpoint shift.** Does it move a typical pool across the **50% competence line** (≈4 dice) or the **80% line** (≈9 dice)? Is the shift gated? (`13` §4: an auto-success *deletes* the breakpoint; a +3-die passive talent *crosses* it for a starting character.)
- **[ ] Check the sensitivity cases** (`13` §3.7): per-die-rate shift, auto-success (premium category — auto-success dominates on medium pools), action-cost change (slow→fast→free often stronger than a numeric buff), recovery compression (one of the strongest tempo effects).

**Detail:** `13` §3 (the probability core), §4 (breakpoints), §8 Stage 1. → `13`

### Stage 2 — Exploit

- **[ ] Tag the rule's mechanism** and cross-reference the eight exploit categories (`13` §5): infinite-loop combos / cap-bypass / silent-stacking / free-resource generation / action-economy abuse / push-cost avoidance / mishap-avoidance / talent-invalidation.
- **[ ] Run the detection heuristic** for each fired tag. The master first question for all of them: *does activating this require one easy decision or many hard ones?* (0–1 decisions + per-round activation = danger zone; 3+ decisions + per-use cost = sweet spot.)
- **[ ] Run the §5.9 pattern match** — name the root pattern (A Free Refund / B Unscoped Amplifier / C Risk Bypass / D Self-Maintaining Zone / E One-Decision Build / F Invisible Attacker / G Stacking Gate). The pattern dictates the fix template.
- **[ ] Run the red-flag keyword scan** (`13` §6 Step 8): "free action," "without rolling," "no mishap," "gain WP," "ignore armor," "per Power Level," "lasts until," "automatically succeed," "stack with," "in addition to," "all allies/enemies." **Two or more in one rule → run the full Five Tests (Stage 3).**

**Detail:** `13` §5 (the exploit taxonomy), §5.9 (the seven patterns), §6 Step 8 (red-flag scan). → `13`

### Stage 3 — Synergy

- **[ ] Map the touch surface.** List every subsystem the rule touches (resolution, push, action-economy, damage-state, recovery, resource, travel-pressure, exception, advancement, economy/access). A rule touching **two or more** of {metacurrency, recovery, spell/power, travel pressure} is **system-level** — review it as such, never let it ship as "local."
- **[ ] Enumerate the interactions** — the specific existing rules each touch-point connects to. Describe the chain: *which rule feeds which, what triggers what.*
- **[ ] Apply the "more than the sum of parts?" test** — the three overlap questions: (A) does it make an existing danger *cheaper*? (B) does it *increase* an existing danger's output? (C) does it *remove* an existing brake? 0 yes → proceed; 1 yes on a light zone → Cap; 1 yes on a heavy zone → Restructure; 2+ yes → Reject or Separate.
- **[ ] If "more than the sum," run the Five Tests**, scored Healthy/Borderline/Unhealthy: **Decision Cost / Risk Exposure / Opportunity Cost / Repeatability / Campaign Erosion.** **"More than the sum" AND failing the gating tests (cost/time/risk absent or cosmetic) = exploit.**
- **[ ] Pressure-channel audit.** Name every channel the rule relieves (resource attrition, injury fear, action scarcity, metacurrency scarcity, time pressure, mishap risk, social resistance, environmental hostility). **A rule that *deletes* a channel (not temporarily relieves) breaks the campaign spine.**
- **[ ] Baseline comparison.** What does a character *without* this rule look like in the same situation? Enormous gap with no cost = dominant.

**Detail:** `13` §6 (the full protocol), §8 Stage 3. → `13`

### Stage 4 — Table

Run the nine lenses (`13` §7). Score each **OK / Caution / Fail.**

- **[ ] Mathematical balance** — odds, EV, frequency (Stages 1–2).
- **[ ] Perceived balance** — does it *feel* fair? Is the choice legible *before* commitment?
- **[ ] Table balance** — player-facing complexity, GM burden (another timer/condition?), speed in live play ("don't roll too often" — a rule that adds rolls floods the economy).
- **[ ] Ambiguity risk** — does it *say* replace-or-stack, per-round-or-per-QD, resisted-or-not? Unstated → table dispute.
- **[ ] Recoverability & permanence** — is the worst case playable? Are permanent/always-on effects the highest-risk surface (pattern D)?
- **[ ] Player agency** — does it create choice or remove a character from play? Does it require GM mercy to stay humane?
- **[ ] Catastrophic-outcome playability** — when the worst case fires, is the resulting state still playable? Survival-with-cost = good; hidden non-playability = bad (Warning Sign §10e).
- **[ ] Campaign balance** — run the attrition curve over a multi-session horizon. Does the party end sessions *higher* on resources than it started?
- **[ ] Verdict-lens overlay** — map to Accept now / Accept w/ simplification / Hold / Reject (structurally).

**Detail:** `13` §7 (the lenses), §8 Stage 4. → `13`

### Stage 5 — Layer & voice

- **[ ] Classify the rule General / Situational / Optional** and tag it. A rule that *could* be Situational/Optional but is written as General is subsystem inflation (Warning Sign §10a).
- **[ ] Place the voice.** Design rationale stays in design docs; only native rulebook prose crosses into the corebook. Strip setting nouns from engine-agnostic text (Warning Sign §10f).

**Detail:** `13` §8 Stage 5; `10-design-philosophy.md` §9 (layering principle). → `13`

### Stage 6 — Verdict (ship / revise / reject)

Choose exactly one. **Reject *structurally*, not impressionistically** ("I dislike it" is not a verdict).

| Verdict | When | What to do next |
| --- | --- | --- |
| **Ship (Accept now)** | Passes math, exploit, synergy, table. | Add to manuscript. |
| **Ship w/ simplification** | Passes but heavier than it needs to be. | Trim before adding. |
| **Revise — Cap** | Fails one test moderately. | Apply a fix template (`13` §6 Step 7: per-round limit, per-QD limit, metacurrency-capped activation, non-refundable cost, re-roll-after-trigger, exclude-from-stacking, lock-to-scope, escalating cost, require-resistance). **Loop back to Stage 1.** |
| **Revise — Restructure** | Fails the mechanism itself. | Redesign. **Loop back to Stage 0.** |
| **Hold** | Depends on a broader rewrite not yet done. | Queue it. |
| **Reject** | Wrong problem / wrong chapter / wrong rule type / too much system impact for too little gain. | Document the structural reason; do not ship. |

**Pipeline output format** (`13` §8): Summary (one sentence) · Tags · Danger Zones Hit · Overlap answers (cheaper/stronger/brake-removed) · Red Flags · Five-Test results · Pattern Match · **Verdict** · Recommended Fix · (if Cap+) a catalog entry for the game-specific exploit catalog (goes to the sibling skill, **not** this file).

**Detail:** `13` §8 Stage 6, the verdict ladder; §9 (division of labor — method here, instantiated findings in siblings). → `13`

---

## 5. Worked examples

> Three concrete walkthroughs showing the recipes in action on real subsystems. Each demonstrates a different combination: Recipe A (whole-game build), Recipe A + Recipe B (build then validate), and Recipe B alone (rule addition to an existing game).

### Worked Example 1 — "NEON/RAIN": a cyberpunk YZE reskin (Recipe A, abridged) + hacking-rule validation (Recipe B)

**Genre thesis (Step 1):** ambition = *cred and a name in the sprawl*; exposure = *the system and the street* (ICE, debt, the corporation, the gear you're wired into). Currency = *your body (chrome) and your nerve.* Adversary = the network's indifference. Thesis sentence: *"You are hungry, driven operators moving through a hard city where debt, wounds, scarcity, heat, and code all exact a price."*

**Attributes + damage (Step 2):** **Chrome** (installed body — damage: *Glitches*), **Reflex** (wired nervous system — *Strains*), **Cortex** (augmented mind — *Crashes*), **Edge** (street presence — *Burns*). Named damage types = free genre-loading.

**16 skills (Step 3):** Chrome → *Brawl, Endure, Implant, Wrench*; Reflex → *Sneak, Drive, Move, Shoot*; Cortex → *Hack, Data-Splice, Deduce, Decrypt*; Edge → *Con, Lease, Fix, Medicine.* (Note *Hack* and *Data-Splice* — the genre's signature verbs — are now first-class skills, not a reskinned Lore.)

**Metacurrency (Step 4):** **hybrid** — *Edge* pool (cap 10, action/success-refueled like West's Faith) pays for pushing (1/push) and buying off Trouble; plus a *Overclock* escalating die (once/session, D8→D12, at-risk like Pride) for peak moments. Push cost = currency + light Trouble (baneanemic, since chrome attrition is modeled as condition tracks, not banes).

**Failure pressure (Step 5):** **Trouble** (Safe/Risky/Desperate exposure frames), West-style — the city taxes the *frame*, not the dice. Consistent with the currency-spend push model.

**Conflict (Step 6):** Round/Turn/Shift; **card-draw initiative** (chaotic gunfights); **cover ratings + 6 range bands** (firearms are the genre's icon); slow/fast budget verbatim; block/dodge+counterattack; ceremonial mode = **the Standoff** (Face Off → Go for Iron → Shoot-off, reskinned Duel). Add a *Netrunner* conflict mode operating on a different positioning layer (ICE constructs as zones).

**Harm (Step 7):** paired-attribute split (Glitches/Strains; Crashes/Burns); **typed D66 families**: Ballistic, Energy, Cyber-psych, Toxic, Fall, *ICE-Burn* (net damage), Overclock-Strain. Port the `65`/`66` climax. Conditions: *Jacked-Out, Crashing, Overheating, Debt-Stressed, Addicted* (chrome withdrawal). Retirement path = "go flatline or go ghost" (become a fixer NPC).

**Power layer (Step 8):** **Low-to-Medium** density. "Powers" = **cyberware** (reskinned as Standard powers, safe-only casting model — a ware either works or you're too low on Edge). Ritual tier = *Long intrusions* (multi-hour deck runs). Fuel = the Edge metacurrency + a *Heat* track (reskinned Burn: chosen quantity, random attribute — "you choose how hard to push, not where the bleed lands"). One generic mishap table per source (ICE-mishap for net; Glitch-table for chrome). Rank 1–3.

**Travel (Step 9):** **pointcrawl** (the sprawl as a graph of districts with mileage/heat-between-points); Shift = 6h; activity menu = *Transit / Navigate Grid / Keep Eyes / Scavenge / Fence / Lay Low / Crash / Repair / Train*; weather = *Smog, Acid Rain, Heat Dome, Surveillance Sweep*. Expedition loop = primary (the *run* is the expedition).

**Org (Step 10):** personal-scale — **Crew** (band org, reskinned Outlaw Band: hideout = safehouse, resources = fence/chopshop/provisions, Scores = runs, Heat = wanted), plus **Turf** (base org, reskinned Business/Property). No faction turn, no mass combat.

**Economy (Step 11):** **cash + Capital** (cred + *Reputation* as a soft capital); feature grammar = cyberware/gun tags (*CONCEALABLE, SILENCED, SMARTLINK, CHROME-HEAVY, FRAGILE*); crafting = *Wrench/Fix* gated by workshop (chopshop) + tier; artifact tier = *prime chrome* (D8/D10/D12 die, immune to Glitch-degradation).

**GM layer (Step 12):** 6 principles (de-flavored FL seven — *The Sprawl Lies Before You / Every Street Has a Legend / Operators Make Their Own Fate / Nothing Is for Free / The Tall Nail Gets Hammered / Flatlining Is Part of the Story / The Run Is Never Set*); D66 district-keyed encounter matrix; *Settlement-as-character* = the Fixer's network / the neighborhood.

**Advancement (Step 13):** **flat 2-rank talents** (Basic/Advanced) — cyberpunk competence is binary-ish; explicit narrative-access gating (a *Ripperdoc* needs a clinic; *ICE-breaker* needs a deck); Legacy XP; downtime 1/season.

**Optional surface (Step 14):** in = Fast Initiative, Resource Dice (for ammo/charge), Group Concept (the Crew); out = full faction turn, epic-tier chrome.

**Validation (Step 15):** Run Recipe B on the whole. The five loops function: Expedition (the run), Conflict (combat/net), Recovery (chromedoctor), Metacurrency (Edge loop), Base (Turf). Weight Expedition + Conflict as dominant. Breakpoint check: a starting decker with Hack 2 + Cortex 3 = 5 dice sits at P(≥1) ≈ 60% unpushed — a touch above the 50% line, which suits a competent-operator genre; an expert (8 dice) at 77%. ✓

---

**Now validate one rule from the above through Recipe B: the "Overclock" hacking die.**

*Proposed rule (one sentence):* "When hacking, spend 1 Edge to add your Overclock die (D8, escalating to D12) to the pool; if the roll still fails, lose Overclock for the session."

- **Stage 0 (Intent):** Serves the Metacurrency + Conflict loops; puts Edge at risk for a peak moment. No existing rule does this (Pride is for protective rolls only). ✓ One-sentence summary clean. → proceed.
- **Stage 1 (Math):** A D8 added to a pool is ≈ +1.33 expected successes on a 6+ read; on a typical 5-die pool it bumps P(≥2) from ~20% to ~38% — a real but gated bump (costs 1 Edge, once/session, at-risk). Does not cross the 80% breakpoint ungated. Auto-success? No. ✓
- **Stage 2 (Exploit):** Tags = *exception/metacurrency-spend*. Red-flag scan: "gain" (Edge *spent*, not gained — clean), "per session" (frequency-limited — good). No infinite-loop (Edge spent ≠ Edge refunded). Pattern match: closest is **E One-Decision Build** — but it's per-session + at-risk, not always-on. ✓
- **Stage 3 (Synergy):** Touch surface = resolution + metacurrency + power-layer (if hacking is a power). Two subsystems → system-level review. Overlap questions: (A) cheaper? — no, costs 1 Edge; (B) stronger? — yes, +a die, but gated; (C) brake removed? — no. 1 yes on a light zone → *Cap* candidate. Five Tests: Decision Cost = 2 (declare + spend) ✓; Risk Exposure = lose-the-die-for-session ✓; Opportunity Cost = 1 Edge not spent on a push ✓; Repeatability = once/session ✓; Campaign Erosion = doesn't delete a channel ✓. All Healthy/Borderline. ✓
- **Stage 4 (Table):** Math OK; perceived = legible (you see the die, you know the risk); GM burden = one more thing to track per session (Caution); ambiguity = none ("add to pool," "if fail, lose"); recoverability = lose-for-session is playable; agency = adds a real choice; campaign = doesn't distort attrition. **One Caution (GM tracking).**
- **Stage 5 (Layer):** Situational (only on hacking rolls). Voice: native rulebook prose.
- **Stage 6 (Verdict):** **Ship with simplification** — it passes; trim by stating explicitly "does not stack with Edge-spent-to-push on the same roll" to close the only ambiguity. Catalog entry: this is a Pride-analog gated to hacking → goes in the game-specific exploit catalog noting the stacking boundary.

### Worked Example 2 — A post-apoc scavenging economy (Recipe A, single subsystem focus, drawing on Steps 11 + 15)

**Goal:** Add a *scavenging* economy to a post-apoc YZE game whose thesis is *ambition = a working vehicle and a full canteen; exposure = the wasted land* (currency = *scrap and water*).

**Economy model (Step 11):** **barter + commodity currency** — water, fuel, ammo, and *salvage* are the media of exchange (FL-style, not cash). Feature grammar for gear = tags like *BROKEN, RUSTED, JURY-RIGGED, PRISTINE* (pre-war). Crafting gated by the *Tinker* talent + a workshop (the garage) + *Scrap* as the universal material. Quality tiers: *Junk / Worn / Working / Pristine* (the last is effectively artifact-tier — a D8 "Pre-War" die immune to rust-degradation). Adopt **Resource Dice** for fuel/ammo/water (D12 abundant → D4 desperate).

**Scavenging as a travel activity (Step 9 menu addition):** Add **SCAVENGE** to the activity menu (like FL's FORAGE/HUNT — cannot stack with HIKE; must stop). Roll *Scavenge* (a Cortex skill); successes yield a *Scrap Die* (D6→D12 by zone richness) that steps down on use like any resource die. A failed push on a Scavenge roll in a *Hot Zone* triggers the *Rad* critical-injury family (a typed D66 family added in Step 7).

**Validation (Step 15 → Recipe B) on the Scrap Die:**

- **Stage 0:** Serves Expedition loop (scavenging *is* the expedition's payoff); puts time + Rad-risk on the line. Not duplicative (no existing "free material" rule). ✓
- **Stage 1:** A D6–D12 step-down die has expected hard uses ≈ 18 before loss (`13` §4.4) — the engine's calibrated "meaningful but not annoying" depletion. ✓
- **Stage 2:** Tags = *resource/economy*. Red-flag: "per use" stepdown is *not* a refund loop (the die depletes, doesn't refill from the same action). Pattern: **A Free Refund**? — trace the flow: Scavenge *produces* Scrap; Scrap is *spent* on crafting; spending Scrap doesn't trigger Scavenge. No loop. ✓
- **Stage 3:** Touch surface = economy + travel-pressure + harm (Rad). Three subsystems → system-level. Overlap: does cheap Scrap remove the *scarcity* channel? **No** — Scrap is finite (stepdown) and gated behind time + Rad-risk. Campaign Erosion: a party that scavenges every ruin still faces Hot Zones and depletion. ✓
- **Stage 4:** Math OK; perceived = "I found a working alternator!" feels great; GM burden = one resource die per PC per trip (manageable); ambiguity = none; recoverability = Scrap is replaceable by more scavenging. ✓
- **Stage 6:** **Ship.** Optional catalog note: watch for a talent that refunds Scrap on a craft roll — that *would* be a Free Refund (pattern A); flag it now.

**Key insight from the example:** the *Scrap Die* is a direct port of the engine's Resource-Die + typed-crit-family patterns — almost no new machinery, maximum genre fit. This is the engine's strength: the *mechanics barely change; the fiction transforms completely.*

### Worked Example 3 — Adding a naval-combat ceremonial mode (Recipe B alone)

**Goal:** Add a *Naval Duel* ceremonial conflict mode to an existing YZE game (e.g., an age-of-sail reskin), modeled on West's Duel pattern.

*Proposed rule (one sentence):* "When two ships make ready to broadside and neither has the weather gage, resolve a Naval Duel in three phased opposed rolls — *Weather Gage* (Cunning/Nature) → *Maneuver* (the pilot's Seamanship) → *Broadside* (Gunnery) — with each phase's margin adding dice to the next; if unresolved, draw initiative and resume normal ship combat."

- **Stage 0:** Serves the Conflict loop; puts the ship (a Base/org asset) and crew at risk. Is it duplicative? No — normal ship combat lacks the phased structure the genre's signature beat deserves. ✓ One-sentence summary clean.
- **Stage 1:** Phased opposed rolls carry margins forward as *dice* (not auto-successes) — at each phase, +1 die per margin-success. Math: a 2-margin on Weather Gage = +2 dice on Maneuver = bumps a 5-die pool to P(≥1) 60%→67%. Gated, additive, no breakpoint deletion. ✓
- **Stage 2:** Tags = *conflict/ceremonial*. Red-flag scan: "automatically" (no — rolled), "stack with" (the carry-forward dice stack *within the duel*, by design — this is the Duel pattern's core mechanism, not silent-stacking across separate sources). Pattern match: **D Self-Maintaining Zone**? — no, the effect ends when the duel ends (returns to normal combat). ✓
- **Stage 3:** Touch surface = conflict + (if ship damage routes to the org layer) base. Two subsystems. Overlap: (A) cheaper broadside? — no, costs the phased setup; (B) stronger? — the winner gets a decisive opening, but *both* sides roll every phase; (C) brake removed? — no (still costs the ship's guns/crew on a loss). Five Tests: Decision Cost = 3+ (three phased rolls) ✓; Risk Exposure = the ship ✓; Opportunity Cost = a duel foregoes fleeing/ramming ✓; Repeatability = once per engagement ✓; Campaign Erosion = doesn't delete a channel. ✓
- **Stage 4:** Math OK; perceived = three escalating rolls is dramatic and legible; GM burden = three opposed rolls then resume (manageable); ambiguity = *state the reaction-denial*: "on the Broadside, the loser cannot Brace/evade the opening salvo" (port this explicitly from the ambush/Duel pattern — it's what makes the opening decisive); recoverability = a lost duel damages the ship, which is recoverable via the org's upkeep/repair loop. ✓
- **Stage 5:** Situational (only triggers on the weather-gage standoff fiction). Voice: native prose.
- **Stage 6:** **Ship with simplification** — passes; the only required addition is the explicit reaction-denial clause on the Broadside (else the loser turtles and the duel stalls). Pattern provenance: this is a straight port of `03-conflict-and-combat.md` §12's ceremonial-scripted-conflict template (West's 3-phase carry-forward), so it inherits that pattern's validated shape. Catalog entry: note that a talent granting *auto-weather-gage* would be a Cap-bypass (pattern B) on this mode → flag.

**Key insight:** the ceremonial-mode *template* (phase-1 social/mental → phase-2 speed/technique → phase-3 resolution, margins carry forward) is engine-level and reusable for *any* genre's signature standoff — the horse-race, the courtroom cross-exam, the dragon's riddle-contest, the ship duel. Recipe B confirmed the port is balanced *because it reuses a calibrated pattern* rather than inventing new machinery.

---

## 6. Design intent

The recipes exist so that the skill's knowledge is **operational, not just descriptive.** A designer should be able to start at Recipe A step 1 and reach a *playable skeleton*, or start at Recipe B Stage 0 and reach a *validated rule*, using only this skill — loading the sibling reference files for the deep detail each step points to, but never needing to re-derive the procedure.

The two recipes are the two halves of the engine's design loop:

- **Recipe A is the *build* half.** It walks from thesis → attribute grid → 16 skills → metacurrency → failure pressure → conflict → harm → power → travel → org → economy → GM layer → advancement → optional rules → validation. The order is not arbitrary: steps 1–2 set the tone everything else inherits (the thesis names the currency and the adversary; the attribute names express the tension); steps 3–11 are the parallel dial-settings that instantiate the five loops; steps 12–14 are authoring; step 15 is the gate that confirms the whole is *a YZE game* and not just a pile of dials. The recipe's discipline is that **every step cites the file that owns the detail** — so a designer never has to guess where to look, and the skill never duplicates what a sibling already holds.

- **Recipe B is the *validate* half.** It is the executable form of `13-balance-and-synergy.md` §8 and `10-design-philosophy.md` §13. Its discipline is that **no rule ships on vibes.** Intent gates out subsystem inflation and duplication before any math is done; math catches breakpoint crossings and per-die-rate shifts the eye can't see; exploit + synergy catch the *couplings* where the engine is fragile (metacurrency, recovery, power, travel-pressure); table catches the rules that are mathematically clean but unplayable, ambiguous, or GM-punishing; layer keeps the General core lean. The verdict ladder — Ship / Ship-w-simplification / Revise-Cap / Revise-Restructure / Hold / Reject — forces a *structural* judgment, not an impressionistic one, and every "revise" loops back to the specific stage that failed rather than restarting from scratch.

The two recipes meet at **Recipe A step 15**: the whole-game skeleton is itself run through Recipe B, because a new game is just a large new rule whose every subsystem must cohere. And the test both recipes ultimately serve is the engine's own founding question (`13` §11, `10` §13): **does ambition still cost something after this lands?** If a step in Recipe A produces a loop where risk no longer refuels agency, or a stage in Recipe B finds a rule that lets a character get more for less, for free, forever, from one decision — the answer is no, and the recipe says exactly where to loop back to fix it.

That is what makes the skill actionable end-to-end: a designer can enter at either recipe, follow the citations to the deep detail, and exit with either a playable skeleton or a validated rule — and in both cases the output is *defensible against the engine's own philosophy and math*, not merely authored.
