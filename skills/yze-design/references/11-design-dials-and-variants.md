<!-- markdownlint-disable MD013 MD024 MD041 MD060 -->

# Design Dials and Variants — The Master Calibrated Options Catalog

> **STATUS: FILLED (roll-up of `00`–`10`).** This is the **configuration catalog** a designer consults when *setting* a new YZE game. It consolidates every calibrated choice identified across the engine-system files into one master list, with FL and West shown as the two named points on each dial, the trade-off stated, and *when-to-choose* guidance. It culminates in **combined preset archetypes** — named dial-sets that produce recognizable genre feels. It is a catalog, not a re-derivation: the *why* behind each dial lives in its owning system file (cited per dial); this file is the *what* and *which*.

## Contents

1. Source provenance
2. Abstraction target
3. How to read a dial
4. The master dial catalog (organized by system layer)
   - 4.A Engine Core (`00`) — the resolution spine
   - 4.B Character Model (`01`)
   - 4.C Progression & XP (`02`)
   - 4.D Conflict & Combat (`03`)
   - 4.E Harm & Consequences (`04`)
   - 4.F Power Layer (`05`)
   - 4.G Travel & Downtime (`06`)
   - 4.H Base / Faction / Mass-Scale (`07`)
   - 4.I Gear & Economy (`08`)
   - 4.J Design Philosophy (`10`)
5. Dial-dependency map (which choices constrain which)
6. Combined preset archetypes (genre dial-sets)
7. How to use this file (the configuration procedure)

## 1. Source provenance

This file rolls up the dials identified in the sibling reference files. Each dial entry cites both (a) the owning system file (e.g. `00 §6`) for the full derivation, and (b) the primary FL/West rulebook evidence (e.g. `FL 03-skills.md:59`). The two canonical calibrated instances:

- **Forbidden Lands 2E (FL)** — the *maximal/survival* instance: magic high, lethality high, metacurrency = WP (harm-refueled), failure = banes, travel = hex-crawl, economy = barter + commodity silver, faction ladder = full (through Polity), talent ladder = 5-rank, authenticity = inventive-within-tone.
- **Tales of the Old West 2E (West)** — the *zero/personal* instance: magic none, lethality high (attritional), metacurrency = Faith (action-refueled), failure = Trouble, travel = pointcrawl, economy = cash + capital + loans + salaries, faction ladder = capped (Company/Town), talent ladder = 2-rank, authenticity = documentary-verify.

The FL/West pair is the engine's proof-by-construction that **the same spine produces opposite tones by swapping the dials.** A new genre sets each dial; the presets in §6 bundle coherent settings.

## 2. Abstraction target

Produce the **master dial catalog** — every place the engine offers a calibrated choice — and the **preset archetypes** that bundle those choices into genre feels. A "dial" here means a design parameter with at least two calibrated instances (FL and West), a stated trade-off, and genre guidance. Dials are tagged by **Layer** (General / Situational / Optional) following `10 §9`.

This file does not re-argue the dials — it indexes them. When a choice needs justification, follow the citation to the owning file.

## 3. How to read a dial

Every dial is written in a fixed six-field compact form:

> **D# — Dial name** *(the parameter being tuned — one short phrase)*
> - **FL** — the FL calibrated point, with citation.
> - **West** — the West calibrated point, with citation.
> - **Trade-off** — what you gain and lose at each pole.
> - **Choose** — when to pick FL-pole, West-pole, or a middle/hybrid setting.
> - **Layer** — General / Situational / Optional.

Conventions:
- **Pole vs middle.** Most dials are continuous; FL and West are two named points. "Hybrid" or "middle" settings are noted in *Choose* where the sibling files recommend one.
- **Citations.** The system-file citation (e.g. `00 §6`) points to the full derivation; the rulebook citation (e.g. `FL 03-skills.md:59`) is primary evidence.
- **Consistency rule.** Dials marked **⟷ must-align** must be set consistently with each other (see §5). Setting one independently breaks the engine's coherence.

## 4. The master dial catalog

Dials are numbered **D1–D113** continuously, grouped by owning system. Within a group they follow the order of the owning file's own "Dials" section.

### 4.A Engine Core — the resolution spine (`00`)

**D1 — Push-cost model** *(what a push costs)* ⟷ D2, D10
- **FL** — bane-self-harm: each 💀 on a Base Die = 1 damage to the rolled attribute; 💀 on Gear Dice degrades the gear. Free in currency. (`FL 03-skills.md:59-101`; `00 §6`)
- **West** — currency-spend: 1 Faith Point per push; no automatic harm to body or gear. (`West 03-rolling-the-bones.md:74-83`; `00 §6`)
- **Trade-off** — gritty attrition (the body/gear *is* the currency) vs dramatic resource-management (belief is the currency).
- **Choose** — FL-pole for survival/horror/attritional; West-pole for dramatic/character-driven; **hybrid** (small currency cost + light bane/Trouble) recommended for new games.
- **Layer** — General (the push itself); the model is the core dial.

**D2 — Cost-face trigger** *(when the latent cost face fires)* ⟷ D1, D10
- **FL** — always-on-push: 💀 is baked into Base/Gear dice and activates every push. (`FL 03-skills.md:71-73`; `00 §3, §6`)
- **West** — exposure-gated: 1s are latent Trouble fuel, counted only on Risky/Desperate fails, after the roll resolves. (`West 03-rolling-the-bones.md:90-101`; `00 §3`)
- **Trade-off** — harm feels *inevitable* (endogenous) vs harm feels *chosen* (frame-gated).
- **Choose** — banes-when-harm-should-be-inevitable; Trouble-when-harm-should-be-a-choice.

**D3 — Metacurrency refuel trigger** *(what earns the pool)* ⟷ D4, D5
- **FL** — harm-earned: 1 WP per 💀 on a Base Die when you push — taking harm generates agency. (`FL 03-skills.md:124`; `00 §7`)
- **West** — action/success-earned: 1 Faith on a 3-⚔ un-pushed roll, or by performing rituals/actions (pray, avenge, save a life, rest). (`West 03-rolling-the-bones.md:273-296`; `00 §7`)
- **Trade-off** — virtuous damage loop (aggression rewarded, if you survive) vs behavior-reward loop (agency decoupled from harm).
- **Choose** — harm-refuel for attritional/survival; action/success-refuel for dramatic/character-driven; success-refuel for pulp.

**D4 — Metacurrency cap + refresh** *(pool size and pacing)*
- **FL** — cap 10; earned in play; refreshed by stronghold rest. (`FL 03-skills.md:120`; `00 §7`)
- **West** — cap 10; 4 per scenario; resets to 4 at Turn of the Season; may carry within a season. (`West 03-rolling-the-bones.md:84-88, 258`; `00 §7`)
- **Trade-off** — slow-burn sandbox grit vs predictable per-arc budget.
- **Choose** — refresh-per-arc for paced drama; earned-only for sandbox grit.

**D5 — Metacurrency depletion** *(what hitting zero means)*
- **FL** — no lockout (zero is just empty). (`00 §7`)
- **West** — Shaken Faith at 0: cannot push, cannot gain Faith; restored by a 4-⚔ roll or end-of-adventure. (`West 03-rolling-the-bones.md:298-307`; `00 §7`)
- **Trade-off** — no floor vs a despair story-beat.
- **Choose** — add the lockout only if you want a "hitting zero" narrative beat (horror, crisis arcs).

**D6 — Modification target** *(which dice mods touch)*
- **FL** — colored: Skill Dice only (never Base/Gear); below-zero skill dice roll as negative dice (⚔ on a negative die cancels a real ⚔). (`FL 03-skills.md:152-162`; `00 §5`)
- **West** — unified pool: mods add/subtract generic dice; no negative-dice subsystem. (`West 03-rolling-the-bones.md:176-182`; `00 §5`)
- **Trade-off** — colored precision (gear/attribute/skill separable, with pressure amplifier) vs speed and simplicity.
- **Choose** — FL-style for tactical depth and clean gear/attribute separation; West-style for pace; negative dice Optional.

**D7 — Help gating** *(what "helping" requires)*
- **FL** — social-stat cap: total help bonus capped by the lowest Empathy in the group. (`FL 03-skills.md:182-190`; `00 §5`)
- **West** — rank floor: each helper needs ≥1 rank in the ability. (`West 03-rolling-the-bones.md:192-196`; `00 §5`)
- **Trade-off** — social-trust limit vs competence floor.
- **Choose** — Empathy-gate for relationship-heavy games; rank-gate for competence-focused; both/none are also valid.

**D8 — Success ladder** *(how outcomes scale)*
- **FL** — threshold-raise (GM-side): default 1⚔; raise to Challenging (2) / Difficult (3); surplus ⚔ = richer detail. (`FL 03-skills.md:19-27`; `00 §4`)
- **West** — grade-read (0 fail / 1 limited / 2 complete / 3+ critical) + player-side Declared Effort; surplus ⚔ = Stunts. (`West 03-rolling-the-bones.md:41-68`; `00 §4`)
- **Trade-off** — GM-sets-the-bar vs roll-reads-its-grade.
- **Choose** — **hybrid (recommended):** read the grade, allow optional threshold-raising / Declared Effort.

**D9 — Legendary-die subsystem** *(the power ceiling for single rolls)* ⟷ D85
- **FL** — on: artifact dice (D8/D10/D12, 6+ = ⚔, scaled, immune to wear) + Pride (once/session escalating heroic-moment die). (`FL 03-skills.md:232-258`; `00 §9`)
- **West** — off: no equivalent (Faith is a currency, not a die). (`00 §9`)
- **Trade-off** — high-tier escalation + heroic peaks vs flat power ceiling.
- **Choose** — on for fantasy/pulp/epic; off for grounded/historical/low-power.

**D10 — Failure-pressure layer** *(how failure taxes)* ⟷ D1, D2
- **FL** — banes: mechanical tax on the dice (💀), always on push; failed push + ≥3💀 = severe setback. (`FL 03-skills.md:97-101`; `00 §6, §10`)
- **West** — Trouble: narrative tables (Safe/Risky/Desperate exposure), frame-gated; failed push = +1 Trouble. (`West 03-rolling-the-bones.md:90-101`; `00 §6, §10`)
- **Trade-off** — mechanical tax (precise, attritional) vs narrative tax (fictional, chosen).
- **Choose** — must be consistent with D1 (banes pair with bane-self-harm; Trouble pairs with currency-spend). Hybrid valid.

### 4.B Character Model (`01`)

**D11 — Attribute naming** *(what the four attributes are called)*
- **FL** — survival axes: Strength / Agility / Wits / Empathy. (`FL 02-your-adventurer.md:378-400`; `01 §3`)
- **West** — frontier-grit: Grit / Quick / Cunning / Docity. (`West 02-your-player-character.md:16-59`; `01 §3`)
- **Trade-off** — generic-resolver (portable) vs genre-flavored (immersive).
- **Choose** — **always name after the genre's core tension** (West-style); skill names do ~60% of re-skinning work.

**D12 — Damage typing** *(how each attribute's harm is named)* ⟷ D56
- **FL** — by position (silent): damage type is functional, not named. (`FL 05-combat-and-damage.md`; `01 §4`)
- **West** — by name (fictional): Grit→Hurts, Quick→Shakes, Cunning→Vexes, Docity→Doubts. (`West 02-your-player-character.md:20-34`; `01 §4`)
- **Trade-off** — functional brevity vs fictional richness (free genre-loading).
- **Choose** — **always name them** (West-style); it costs nothing and makes attrition feel in-genre.

**D13 — Attribute ceiling (creation)** *(max single attribute at start)*
- **FL** — 2–4 range (5/6 in a kin/profession key attribute). (`FL 02-your-adventurer.md:353-377`; `01 §3`)
- **West** — 1–5 range. (`West 02-your-player-character.md:356-364`; `01 §3`)
- **Trade-off** — narrow competent range vs wider curve.
- **Choose** — match the desired power spread; 2–4 for gritty competence, 1–5 for wider differentiation.

**D14 — Protected-dial model** *(the player's personal pressure-relief resource)* ⟷ D1, D3
- **FL** — Pride: a die (D8/D10/D12), narrow scope (protective rolls only), once/session, at-risk. (`FL 02-your-adventurer.md:456-462`; `01 §5`)
- **West** — Faith: a currency, broad scope (whole push/trouble loop), per-scenario, depleted = Shaken. (`West 03-rolling-the-bones.md:84-88, 258-311`; `01 §5`)
- **Trade-off** — peak moments (die) vs sustained agency (currency).
- **Choose** — **hybrid (recommended):** small currency pool + escalating once/session die. Pride-style for lethal one-shots; Faith-style for dramatic arcs.

**D15 — Protected-dial identity load** *(how heavy the resource's meaning is)*
- **FL** — light: Pride is "stubborn will" (a note). (`01 §5`)
- **West** — heavy: Faith is a one-sentence belief system ("the Lord is my shepherd"). (`West 03-rolling-the-bones.md:258`; `01 §5`)
- **Trade-off** — minimal texture vs character-defining beat.
- **Choose** — heavy when the genre is about belief (West, horror, faith-magic); light when it's about grit.

**D16 — Social anchor depth** *(the PC's relational scaffolding)*
- **FL** — minimum: relationships + Dark Secret + home settlement. (`FL 02-your-adventurer.md:467-483`; `01 §6`)
- **West** — maximum: + Pardner + Compadres + Big Dream + town-as-system. (`West 02-your-player-character.md:36-151`; `01 §6`)
- **Trade-off** — lean party-bond vs rich NPC-ally + player-drive layer.
- **Choose** — **always add Big Dream** (free XP engine); add Compadres if you want player-controlled NPC allies.

**D17 — Encumbrance detail** *(carry-limit granularity)*
- **FL** — detailed: backpacks/sacks tables, heavy/light/tiny tiers, over-encumbrance Endurance tax. (`FL 02-your-adventurer.md:499-550`; `01 §7`)
- **West** — lighter: same core (primary physical attribute × 2) with less table detail. (`West 02-your-player-character.md:89-103`; `01 §7`)
- **Trade-off** — precision vs speed.
- **Choose** — port the core (×2 + tiers + tax); match table taste for table detail.

**D18 — Consumables tracking** *(how food/water/ammo/torches are counted)* ⟷ D103
- **FL** — Resource Dice as default (D6–D12, roll on use, 1–2 steps down). (`FL 02-your-adventurer.md:552-574`; `01 §7`)
- **West** — counted units default; Resource Dice as Optional Module. (`West 06-life-in-the-old-west.md:689`; `01 §7`)
- **Trade-off** — die-roll drama ("running out" moments) vs bookkeeping precision.
- **Choose** — **Resource Dice always** — less bookkeeping, better scarcity drama. Default-on for survival; default-off for cinematic.

**D19 — Fast-gen identity selector** *(the quick-generation first choice)*
- **FL** — Kin (8 biological/cultural species), each granting a kin talent + key attribute. (`FL 02-your-adventurer.md:40-351`; `01 §8`)
- **West** — Archetype (10 social professions), each a pre-built stat block. (`West 02-your-player-character.md:337-754`; `01 §8`)
- **Trade-off** — fantasy races vs social roles.
- **Choose** — pick the genre's primary sorter (species / caste / role / lineage / occupation).

**D20 — Lifepath default** *(how deep character generation goes)*
- **FL** — optional add-on (Life Generator + dedicated Lifepaths book). (`FL 13-lifepaths-of-the-forbidden-lands.md`; `01 §8`)
- **West** — standard deep method ("Your Tale Begins" lifepath in corebook). (`West 02-your-player-character.md:755-827`; `01 §8`)
- **Trade-off** — deep lifepath = specialist text vs available-in-core.
- **Choose** — **ship both fast and deep**; make the lifepath optional but available.

**D21 — Party-identity layer** *(a shared starting identity at session zero)*
- **FL** — none formalized. (`01 §8`)
- **West** — Group Concepts (7: Law Men, Outlaws, Ranchers, etc.) granting shared starting gear/resources. (`West 02-your-player-character.md:232-326`; `01 §8`)
- **Trade-off** — none vs strong party-binding.
- **Choose** — add a Group Concept layer when you want the party bound at creation.

### 4.C Progression & XP (`02`)

**D22 — Talent ladder depth** *(how tall talent trees are)* ⟷ D23
- **FL** — 5-rank (kin / profession / general). (`FL 04-talents.md`; `02 §5`)
- **West** — 2-rank (Basic / Advanced). (`West 04-talents.md`; `02 §5`)
- **Trade-off** — build identity + specialization (long campaigns) vs accessibility + low cognitive load (short arcs).
- **Choose** — 5-rank for long campaigns; 2-rank for short arcs / new players; **hybrid** (flat utility + deep signature) internally shown by FL.

**D23 — Talent cost curve** *(XP per rank)*
- **FL** — `rank × 3` XP with teacher; ×3 without; mentor required for rank 1. (`FL 02-your-adventurer.md:656-679`; `02 §4`)
- **West** — flat: Basic 6 XP (teacher) / 18 (no teacher); Advanced 9 / 27. (`West 02-your-player-character.md:199-208`; `02 §5`)
- **Trade-off** — linear scaling vs two flat steps.
- **Choose** — match to D22 (deep ladder → scaling curve; flat ladder → two steps). The skill curve `(new rank × 3)` is the engine default for both.

**D24 — Magic-path ladder** *(power-class growth arc)* ⟷ D77
- **FL** — 1–6 (taller than the talent cap). (`FL 07-magic.md`; `02 §5`)
- **West** — none (no magic). (`02 §5`)
- **Trade-off** — long power-growth arc vs absent.
- **Choose** — only if the power layer is on (D74); scale ladder to campaign length.

**D25 — Narrative access gating** *(what blocks learning, beyond XP/time)*
- **FL** — implicit (via the teacher requirement). (`02 §5`)
- **West** — explicit: talents grouped by function; many need a forge / society / institution / teacher. (`West 02-your-player-character.md:210`; `02 §5`)
- **Trade-off** — implicit vs fiction-gated.
- **Choose** — **always make it explicit (West-style)** — free in-fiction texture.

**D26 — XP pace dial** *(arc-length control)*
- **FL** — two paces: Tale (fast, short stories) vs Campaign (slow, multi-year). (`FL 02-your-adventurer.md:602-606`; `02 §3`)
- **West** — single default pace. (`02 §3`)
- **Trade-off** — adjustable arc length vs simplicity.
- **Choose** — add a pace dial for flexible groups; both books converge on 1–3 XP/session + 2/4 milestones + 1/season downtime as the default budget.

**D27 — Attribute training cap** *(max attribute via training)* ⟷ D13
- **FL** — 4 (key attribute up to 6 at creation). (`FL 02-your-adventurer.md:637-645`; `02 §4`)
- **West** — 5. (`West 02-your-player-character.md:179-188`; `02 §4`)
- **Trade-off** — narrow ceiling vs wider.
- **Choose** — match D13's creation ceiling.

**D28 — Metacurrency → XP conversion** *(linking short-term pool to long-term growth)*
- **FL** — yes (Optional): 10 WP surrendered across sessions = 1 XP. (`FL 02-your-adventurer.md:404-408`; `02 §9`)
- **West** — no. (`02 §9`)
- **Trade-off** — pools-mean-something vs cleaner separation.
- **Choose** — Optional; use if short-term pools cap out and you want reserve to convert.

**D29 — NPC advancement parallel** *(do long-term NPC allies grow?)*
- **FL** — Named Men (mercenaries advance alongside PCs). (`FL 12-mercenaries-of-forbidden-lands.md`; `02 §10`)
- **West** — none formalized. (`02 §10`)
- **Trade-off** — NPCs grow vs static statblocks.
- **Choose** — add if you have long-term NPC allies (roster orgs, D94).

### 4.D Conflict & Combat (`03`)

**D30 — Time-unit ladder** *(Round / Turn / Shift durations)*
- **FL** — Round ~10s–1min / Turn ~15min / Shift implied (Quarter Days). (`FL 05-combat-and-damage.md:29-34`; `03 §3`)
- **West** — fixed table: Round 5–10s / Turn 5–10min / Shift 6h (4/day: Morning/Afternoon/Evening/Night). (`West 05-conflict-and-damage.md:18-31`; `03 §3`)
- **Trade-off** — loose prose vs calendrical precision.
- **Choose** — West's explicit table when downtime beats matter; keep the three-scale nesting regardless.

**D31 — Initiative archetype** *(who acts first)* ⟷ D32
- **FL** — rolled-and-sticky: AGILITY+WITS ⚔ + AGILITY = numeric segment; holds within Round; simultaneous ties; delay allowed. (`FL 05-combat-and-damage.md:7-23`; `03 §4`)
- **West** — random-and-redrawn: card draw each Round; Aces high; suit seniority breaks ties. (`West 05-conflict-and-damage.md:44-50`; `03 §4`)
- **Trade-off** — stat-coupled & predictable vs volatile & dramatic.
- **Choose** — rolled-sticky for tactical/character-build; random-redrawn for chaotic/genre-iconic; **side-based (Optional, both)** for fast skirmishes.

**D32 — Initiative stat coupling** *(is agility a combat stat?)*
- **FL** — coupled to AGILITY+WITS. (`03 §4`)
- **West** — decoupled (cards). (`03 §4`)
- **Trade-off** — rewards character build vs rewards tactical adaptability.
- **Choose** — match D31.

**D33 — In-Round order malleability** *(can you trade turn order?)*
- **FL** — delay to any lower segment; FEINT swaps segments with an opponent. (`FL 05-combat-and-damage.md:339`; `03 §4`)
- **West** — once-per-scene ally card-swap. (`West 05-conflict-and-damage.md:60-62`; `03 §4`)
- **Trade-off** — solo-tactical vs cooperative-tactical.
- **Choose** — FL-style for duel play; West-style for party-coordination.

**D34 — Range band count** *(named, non-measured distance tiers)*
- **FL** — 5 (Arm's Length / Near / Short / Long / Distant). (`FL 05-combat-and-damage.md:155-161`; `03 §5`)
- **West** — 6 (adds Medium). (`West 05-conflict-and-damage.md:34-42`; `03 §5`)
- **Trade-off** — coarser vs finer ranged granularity.
- **Choose** — 6 for firearm genres; 5 for melee/bow genres.

**D35 — Terrain layer** *(what the ground does)* ⟷ D36
- **FL** — zone features (Cramped/Rough/Open/Dark-Foggy) + borders (Blocked/Obscured): movement & line-of-sight pressure. (`FL 05-combat-and-damage.md:115-145`; `03 §5`)
- **West** — cover ratings (bush 1 → adobe 8) + to-hit penalty grades (Partial/Good/Heavy): concealment & defense pressure. (`West 05-conflict-and-damage.md:263, 375-379`; `03 §5`)
- **Trade-off** — movement/LOS scarcity (dungeons) vs concealment scarcity (gunfights).
- **Choose** — zones for dungeon/ruin genres; cover for firearm genres; hybrid valid.

**D36 — Cover model** *(ranged-defense depth)* ⟷ D35
- **FL** — soak-only (Cover Rating rolls against damage; no to-hit penalty). (`FL 05-combat-and-damage.md:688-699`; `03 §5`)
- **West** — soak + to-hit penalty grades. (`West 05-conflict-and-damage.md:375-379`; `03 §5`)
- **Trade-off** — simpler vs the gold standard for firearms.
- **Choose** — West's dual model for firearm genres; FL's soak-only for lower-tech.

**D37 — Reach subsystem** *(weapon-length as positioning pressure)*
- **FL** — deep: Short/Normal/Long bands + CUT IN/BRACE/INTERCEPT/LOCK SHIELDS/FEINT/HALF-HAND. (`FL 05-combat-and-damage.md:249-339`; `03 §6`)
- **West** — light: Brace for ranged only; melee reach implicit. (`West 05-conflict-and-damage.md:209-211`; `03 §6`)
- **Trade-off** — melee tactical depth vs simplicity.
- **Choose** — FL-reach for melee/historical; omit for ranged-centric genres.

**D38 — Action budget** *(actions per Round)* — **load-bearing constant**
- **FL / West** — **2 per Round** = (1 slow + 1 fast) ∨ (2 fast); refresh each Round; cannot bank. (`FL 05-combat-and-damage.md:41`; `West 05-conflict-and-damage.md:66`; `03 §7`)
- **Trade-off** — scarcity (the engine's balance assumption) vs flexibility.
- **Choose** — **keep at 2.** Raise to 3 only for high-action pulp (requires rebalancing damage).

**D39 — Reaction economy** *(what out-of-turn defense costs)*
- **FL / West** — reactions draw from the shared action budget (declared before the attack resolves). (`FL 05-combat-and-damage.md:271-273`; `West 05-conflict-and-damage.md:162-170`; `03 §8`)
- **Trade-off** — prevents defense-bloat vs free infinite defense.
- **Choose** — **never make reactions free** without rebalancing damage. This coupling is non-negotiable.

**D40 — Defense verbs & economy** *(how you avoid a hit)*
- **FL** — Dodge (MOVE) + Parry (MELEE+gear); pure success-cancellation (your ⚔ erase attacker ⚔) with a slash/stab/shield matrix. (`FL 05-combat-and-damage.md:271-313`; `03 §8`)
- **West** — Dodge (MOVE) + Block (FIGHTIN') + Protect Another; success-menu — each ⚔ cancels damage *or* buys a counterattack. (`West 05-conflict-and-damage.md:162-176`; `03 §8`)
- **Trade-off** — fast/resolved vs aggressive/choice-laden (defense can hurt).
- **Choose** — FL for speed; West for "defense can hurt"; add Protect Another for bodyguard play.

**D41 — Melee verb model** *(how melee attacks are expressed)*
- **FL** — verb-rich: Slash / Stab / Punch, each with a weapon-feature prerequisite and a distinct defense profile. (`FL 05-combat-and-damage.md:289-325`; `03 §9`)
- **West** — verb-single + modifiers: one Melee attack + All-Out/Called modifiers + Stunt menu. (`West 05-conflict-and-damage.md:148-160`; `03 §9`)
- **Trade-off** — weapon-as-puzzle vs success-as-authorship.
- **Choose** — FL for weapon-dueling genres; West for cinematic narrative combat.

**D42 — Ranged weapon-behavior encoding** *(where the weapon's behavior lives)*
- **FL** — gear-feature tags (PIERCE ARMOR, HIGH-VELOCITY, MISFIRE, LOAD, READY, WINDLASS). (`FL 05-combat-and-damage.md:498-536`; `03 §10`)
- **West** — action-type economy (single/double/lever/breech) + named tricks. (`West 05-conflict-and-damage.md:239-251`; `03 §10`)
- **Trade-off** — composable tags vs legible action types.
- **Choose** — FL-features for fantasy; West-actions for firearm genres.

**D43 — Reload/prepare depth** *(the prepare-shoot-reload loop)*
- **FL** — READY-per-shot (bows) / LOAD-per-shot (crossbows). (`FL 05-combat-and-damage.md:373-375`; `03 §10`)
- **West** — cartridge-count + reload-actions (revolver 3 actions; magazine 4 Rounds) + cock/chamber prepare. (`West 05-conflict-and-damage.md:381-385`; `03 §10`)
- **Trade-off** — feature-tag depth vs action-economy depth.
- **Choose** — depth scales with weapon technology; cartridge-count for firearm genres.

**D44 — Signature ranged tricks** *(the cinematic verbs)*
- **FL** — Aim, High-Velocity, Pierce Armor (via tags). (`03 §10`)
- **West** — Fanning, Overwatch, Quick Shot, Called Shots. (`West 05-conflict-and-damage.md:255-366`; `03 §10`)
- **Trade-off** — tag-composable vs named-cinematic.
- **Choose** — add the genre's iconographic tricks (West's named tricks for genre flavor).

**D45 — Social-conflict currency** *(how social conflict resolves)*
- **FL** — binary: comply *or* escalate to violence (failed persuasion becomes a fight). (`FL 05-combat-and-damage.md:405-431`; `03 §11`)
- **West** — damage-attrition: surplus ⚔ = Vexes/Doubts; can Break a character without a punch. (`West 05-conflict-and-damage.md:418-438`; `03 §11`)
- **Trade-off** — short/punchy escalation vs attritional scene-ending.
- **Choose** — binary-escalate for escalation-prone games; damage-attrition for reputation-as-combat games.

**D46 — Social attribute mapping + medium** *(which abilities social conflict uses)*
- **FL** — Manipulation vs Insight. (`03 §11`)
- **West** — Presence/Performin' vs Insight + Booklearnin' for Social Conflict by Mail. (`West 05-conflict-and-damage.md:414-416`; `03 §11`)
- **Trade-off** — single ability vs circumstance-chosen + medium expansion.
- **Choose** — map to your attribute array; add mail/telegram/radio variants for any genre with written comms.

**D47 — Reputation integration** *(is social standing a tracked subsystem?)*
- **FL** — explicit local-Reputation table (+1/+2, symmetric). (`FL 05-combat-and-damage.md:429-431`; `03 §11`)
- **West** — folded into genre core, not a separate table. (`03 §11`)
- **Trade-off** — explicit-table vs implicit.
- **Choose** — FL-table when reputation is a tracked subsystem (D110).

**D48 — Ceremonial conflict mode** *(the genre's signature scripted beat)*
- **FL** — Ambush/sneak-attack: free pre-initiative action, target cannot react. (`FL 05-combat-and-damage.md:218-233`; `03 §12`)
- **West** — Duel: Face Off → Go for Your Guns → Shoot-off (phased bonus chain, all in one Round). (`West 05-conflict-and-damage.md:276-326`; `03 §12`)
- **Trade-off** — opening-advantage vs escalating-script.
- **Choose** — **include at least one** for the genre's signature beat (standoff, ambush, dogfight, chase).

**D49 — Morale & rout** *(do NPC fights end without annihilation?)*
- **FL** — on (Optional): per-side dice rating with add/subtract factors (veterans +, rabble −). (`FL 05-combat-and-damage.md:191-212`; `03 §13`)
- **West** — on (Optional): flat 3-tier (2/4/6 dice by troop quality). (`West 05-conflict-and-damage.md:213-229`; `03 §13`)
- **Trade-off** — tunable-per-enemy vs fast-at-table.
- **Choose** — default on for frequent NPC combat; both share the trigger list (leader down / half-down / terrifying display / outmatch).

**D50 — Mount depth** *(how central mounts are)*
- **FL** — condition: −1 vs mounted; polearm synergy. (`FL 05-combat-and-damage.md:135, 167`; `03 §14`)
- **West** — participant: statted horse, ANIMAL HANDLIN', Spooked state, lasso, 8-dice fall risk. (`West 05-conflict-and-damage.md:110, 231-237`; `03 §14`)
- **Trade-off** — tactical edge vs full subsystem.
- **Choose** — condition-depth for low-mount genres; participant-depth for mounted genres.

### 4.E Harm & Consequences (`04`)

**D51 — Attribute-as-HP mapping** *(how damage is recorded)* ⟷ D56, D12
- **FL** — single-attribute-per-source: each source names its target (sword→Strength, fear→Wits). (`FL 06-critical-injuries.md:5`; `04 §3`)
- **West** — paired split: physical alternates Hurts→Grit then Shakes→Quick; mental alternates Doubts→Docity then Vexes→Cunning. (`West 05-conflict-and-damage.md:443`; `04 §3`)
- **Trade-off** — clean routing to consequence tables vs two-axis attritional spread.
- **Choose** — single when damage type must route to a typed crit family (D52); split when physical/mental harm should spread.

**D52 — Critical-injury architecture** *(the shape of the consequence table)* — **signature choice**
- **FL** — family of typed tables (8: Slash, Blunt Force, Stab, Burn, Acid, Cold, Swallow, Horror) — the set *is* a portrait of the genre's threats. (`FL 06-critical-injuries.md:188-523`; `04 §5`)
- **West** — single master table indexed by body location (Tens) × severity (Units). (`West 05-conflict-and-damage.md:521-560`; `04 §5`)
- **Trade-off** — damage-type specificity vs anatomical parsimony.
- **Choose** — typed families when the genre has meaningfully different harm types; master table when all hits are "a wound somewhere." Both use the same D66 architecture + `65`=maim / `66`=die climax.

**D53 — Permanent-injury layer** *(do survivors carry scars?)*
- **FL** — dedicated Permanent tables per family (on `65`), survivable via timely rescue. (`FL 06-critical-injuries.md:22-27`; `04 §5, §10`)
- **West** — inline Long-term Effect column, preventable by a heal during the window. (`West 05-conflict-and-damage.md:521-560`; `04 §10`)
- **Trade-off** — rich maiming sub-system vs parsimony.
- **Choose** — dedicated tables for survival/horror; inline for action; omit for pulp.

**D54 — Death model** *(the rhythm of dying)*
- **FL** — hard time limit: die when the countdown expires unless healed in time. (`FL 06-critical-injuries.md:7-13`; `04 §8`)
- **West** — periodic un-pushable Death roll (full Grit) each interval until stabilized. (`West 05-conflict-and-damage.md:499-503`; `04 §8`)
- **Trade-off** — urgency/GM-paced vs player engagement (the dying player keeps rolling).
- **Choose** — hard limit for GM-paced grit; death rolls for dramatic lingering.

**D55 — Stabilization** *(the medic's role complexity)*
- **FL** — single healing roll (one attempt each; self at −2). (`FL 06-critical-injuries.md:7-13`; `04 §8`)
- **West** — layered DOCTORIN' jobs: stabilize / revive / prevent long-term. (`West 05-conflict-and-damage.md:489`; `04 §8`)
- **Trade-off** — simple vs distinct healer roles.
- **Choose** — layered when the medic should have distinct jobs; simple for speed.

**D56 — Broken fiction** *(what reaching zero feels like)* ⟷ D12
- **FL** — generic helplessness. (`04 §3`)
- **West** — per-attribute flavor (Grit-Broken = collapse; Cunning-Broken = rage/withdrawal; Docity-Broken = panic/despair). (`West 05-conflict-and-damage.md:445-451`; `04 §3`)
- **Trade-off** — one state vs four story-beats.
- **Choose** — per-attribute when Broken should be a narrative event (recommended).

**D57 — Conditions set** *(the slow attrition clock)*
- **FL** — Hungry, Thirsty, Sleepy, Cold, Addicted (single-attr recovery block). (`FL 06-critical-injuries.md:59-103`; `04 §6`)
- **West** — Starving, Dehydrated, Exhausted, Freezing, Heatstroke (paired-attr; Heatstroke imposes Trouble on all rolls). (`West 05-conflict-and-damage.md:509-597`; `04 §6`)
- **Trade-off** — trait-flavored vs attritional-spread + dice-pressure.
- **Choose** — pick the 4–6 deprivations your setting's *travel* threatens. Borrow West's Trouble-on-all-rolls to make a condition *feel* debilitating.

**D58 — Environmental hazards** *(rated-pressure model)*
- **FL / West** — both: fire (Intensity), explosions (Blast Power, West), fall (height÷2), drown (3-stage), poison (Potency, 4-type taxonomy), disease (Virulence), darkness. (`FL 06-critical-injuries.md:113-170`; `West 05-conflict-and-damage.md:599-688`; `04 §7`)
- **Trade-off** — narrative table (FL routes fire to Burn crits) vs rated-pressure engine (West's escalating Intensity).
- **Choose** — rated pressures when hazards should scale and combine; tables when outcomes should be specific. Port the 4-type poison taxonomy (lethal/paralyzing/sleeping/hallucinogenic).

**D59 — Healing cadence** *(bounce-back tempo)* ⟷ D30
- **FL** — slow: per Quarter-Day (in travel); healing roll halves remaining injury time. (`FL 06-critical-injuries.md:13-21`; `04 §9`)
- **West** — fast: 1 attribute point per Turn (5–10min); DOCTORIN' restores N = successes. (`West 05-conflict-and-damage.md:457-491`; `04 §9`)
- **Trade-off** — survival attrition vs action-game tempo.
- **Choose** — fast for action; slow for survival attrition; tie to the travel time block (D64).

**D60 — Retirement path** *(what happens when a PC is too broken to play)*
- **FL** — explicit: "become a retainer NPC, keep XP," dignified prose. (`FL 06-critical-injuries.md:33-39`; `04 §10`)
- **West** — implicit (a maimed PC is simply played with lasting effects or replaced). (`04 §10`)
- **Trade-off** — story-beat exit vs table-decides.
- **Choose** — **always consider FL's explicit path** — high-value, low-cost; preserves player investment + seeds supporting cast.

**D61 — Coup de grâce** *(finishing a helpless foe)*
- **FL** — character trait (Cold-blooded talent allows; Honorable injury forbids). (`FL 06-critical-injuries.md:500`; `04 §4`)
- **West** — per-act conscience test: fail a no-ability, no-push Docity roll to go through; 1 Doubts cost regardless. (`West 05-conflict-and-damage.md:453-455`; `04 §4`)
- **Trade-off** — capacity trait vs moral test.
- **Choose** — the per-act test for any genre where killing should *cost the killer something* (recommended).

### 4.F Power Layer (`05`)

**D62 — Power layer on/off** *(the master switch)* — **single most important genre decision**
- **FL** — ON: full apparatus (17 disciplines). (`FL 07-magic.md`; `05 §10`)
- **West** — OFF: zero instance (proof the engine runs at full strength without it). (`West 03-rolling-the-bones.md:258-311`; `05 §10`)
- **Trade-off** — maximal subsystem vs engine alone.
- **Choose** — OFF for any genre where powers break the fiction (historical, western, war, mystery); ON when powers *are* the fiction.

**D63 — Power density** *(how much of the FL apparatus to instantiate)* ⟷ D62
- **FL** — High. (`05 §10`)
- **West** — None. (`05 §10`)
- **Trade-off** — specialist-class depth vs universal-light vs absent.
- **Choose** — None (West) / Low (gadgets, psi, knacks — drop Power Words) / Medium (sword & sorcery, urban fantasy — add Rituals + Burn) / High (FL — all three tiers). **If everyone has a power, lean Low.**

**D64 — Taxonomy tiers** *(effect-speed coverage)* ⟷ D63
- **FL** — all three: Spells (slow) + Power Words (fast/reactive) + Rituals (long/ceremonial). (`FL 07-magic.md:67-71`; `05 §3`)
- **West** — none. (`05 §3`)
- **Trade-off** — tactical + reactive + ceremonial vs absent.
- **Choose** — always Standard if on; add Rituals for ceremonial/downtime; add Power Words only if power-users need to defend like fighters (else glass cannons).

**D65 — Casting-risk model** *(variance and backlash)*
- **FL** — all three: Safe (guaranteed-but-costly) + Chance (reach beyond rank, certain mishap) + Overcharge (gamble for scale, 💀 = mishap). (`FL 07-magic.md:61-100`; `05 §4`)
- **West** — none (no casting). (`05 §4`)
- **Trade-off** — guaranteed-costly / rolled-cheap / pushed-scale vs absent.
- **Choose** — Safe-only for Low; Safe+Overcharge for Medium; all three for High. You can never *fail* to cast — the roll is a risk-and-scale test.

**D66 — Fuel** *(what powers cost)* ⟷ D3
- **FL** — core WP (the same pool as talents) + Burn (self-harm override: chosen quantity, random attribute) + refunds at high rank. (`FL 07-magic.md:73-131`; `05 §5`)
- **West** — core Faith (fuels pushing/Trouble only, never new capabilities). (`05 §5`)
- **Trade-off** — extended purchase scope vs core-scope only.
- **Choose** — **always reuse the core metacurrency** (never invent a parallel one); add Burn for Medium+ if you want desperate casting; refunds only at High.

**D67 — Mishap layer** *(failure pressure for powers)* ⟷ D10, D52
- **FL** — 17 typed D66 mishap families (one per discipline), count-modified (−10/+0/+10 by 💀 count). (`FL 07-magic.md:158-176`; `05 §7`)
- **West** — core Trouble (narrative, frame-gated). (`05 §7`)
- **Trade-off** — specific-and-memorable vs narrative-and-light.
- **Choose** — none/Trouble-reskin for Low; a few typed families (per source) for Medium; per-discipline families for High. Same pattern as the typed crit family (D52).

**D68 — Material gating** *(do powers need stuff?)*
- **FL** — ingredients (+1 Power Level, consumed; required for some; ritual ingredients for epic). (`FL 07-magic.md:100, 116-118`; `05 §6`)
- **West** — none. (`05 §6`)
- **Trade-off** — scarcity matters vs free casting.
- **Choose** — add when scarcity matters to the genre (gadgets → ingredients; alchemy → reagents).

**D69 — Knowledge gating** *(do powers need books/teachers?)* ⟷ D25
- **FL** — grimoires (−1 rank), teachers, secrecy tables (Rarity/Secrecy). (`FL 07-magic.md:13-41, 108-114`; `05 §6`)
- **West** — none. (`05 §6`)
- **Trade-off** — scholarly/tradition flavor vs open access.
- **Choose** — add for scholarly/tradition-flavored magic; rituals *always* require a teacher or grimoire.

**D70 — Rank ladder height** *(power-growth arc)* ⟷ D24
- **FL** — 1–6 (taller than the 1–3 talent cap). (`FL 07-magic.md:57-59`; `05 §8`)
- **West** — none. (`05 §8`)
- **Trade-off** — long power-growth arc vs absent.
- **Choose** — Low: 1–3 / Medium: 1–5 / High: 1–6; scale to campaign length.

**D71 — Epic tier** *(world-changing effects)*
- **FL** — on: epic ingredients (permanent attributes loss, monster hearts, sacrifices, world-shaping places); corruption spiral. (`FL 07-magic.md:137-156`; `05 §9`)
- **West** — none. (`05 §9`)
- **Trade-off** — mythic ceiling gated by irreplaceable fiction costs vs absent.
- **Choose** — on only at High density, for genres whose ceiling includes world-changing acts. The ceiling is gated by *cost*, not fuel.

**D72 — Player authoring** *(can players invent powers?)*
- **FL** — on: full forging appendix (rank/scope benchmarks + spell-form template + 10-check balance test + Keeper Veto). (`FL 07-magic.md:5254-5452`; `05 §8`)
- **West** — none. (`05 §8`)
- **Trade-off** — extensibility with safety rails vs closed list.
- **Choose** — include if the table wants to invent powers; the Keeper Veto ("if the GM cannot imagine fair counterplay, the spell is not ready") is essential.

### 4.G Travel & Downtime (`06`)

**D73 — Spatial model** *(the central travel dial — what travel is about)*
- **FL** — hex-crawl: 10km tiles, per-tile navigation + mishaps, fog-of-war, terrain types. (`FL 08-journeys.md:7-42`; `06 §3`)
- **West** — pointcrawl: miles/Shift between named points, rush roll, the "between" is attrition. (`West 06-life-in-the-old-west.md:1261-1345`; `06 §3`)
- **Trade-off** — exploration depth (the map *is* play) vs prep/speed (the points are the story).
- **Choose** — hex for sandbox exploration & fog-of-war; pointcrawl for trail/pursuit drama & fast pacing; hybrid (named points on a hex map) valid.

**D74 — Time block** *(the travel resolution unit)* ⟷ D30
- **FL** — 4 Quarter Days (Morning/Day/Evening/Night) + daily checklist (resource dice, weather, calendar). (`FL 08-journeys.md:44-49, 149-157`; `06 §4`)
- **West** — Shift (count loose), no formal checklist. (`West 06-life-in-the-old-west.md:1283-1290`; `06 §4`)
- **Trade-off** — structured attritional day vs flexible block.
- **Choose** — Quarter Day when the *day* should feel like a series of costs; Shift for lighter pacing.

**D75 — Activity-menu breadth** *(how many travel jobs exist)*
- **FL** — full 14-row formal menu (HIKE/LEAD THE WAY/KEEP WATCH/FORAGE/HUNT/FISH/SURVEY/MAKE CAMP/REST/SLEEP/TRAIN/CRAFT/REPAIR/EXPLORE), solo/shared tagged. (`FL 08-journeys.md:158-173`; `06 §5`)
- **West** — ~6–8 implicit jobs + mounted/animal labor. (`West 06-life-in-the-old-west.md:1263-1281`; `06 §5`)
- **Trade-off** — tight labor puzzle vs genre-textured jobs.
- **Choose** — formal menu when travel is the game; implicit when travel is connective tissue. The architecture (movement/navigation/security/supply mutually exclusive) is the transferable core.

**D76 — Navigation cost** *(how getting there taxes)*
- **FL** — per-tile: Survival roll per hex entered; fail = mishap table (Lost, Blocked, Sprained Ankle…). (`FL 08-journeys.md:229-258`; `06 §6`)
- **West** — per-edge: one rush roll/block (+50% or Trouble halt). (`West 06-life-in-the-old-west.md:1263-1267`; `06 §6`)
- **Trade-off** — mechanical per-tile tax vs narrative per-block tax.
- **Choose** — per-tile for exploration; per-block for drama. Must align with D73.

**D77 — Over-exertion valve** *(the "push on or camp" decision)* ⟷ D1
- **FL** — forced march: Endurance roll, Agility damage + SLEEPY on fail. (`FL 08-journeys.md:200-217`; `06 §6`)
- **West** — rush: MOVE/Animal Handlin' roll, +50% or Trouble halt. (`West 06-life-in-the-old-west.md:1263-1267`; `06 §6`)
- **Trade-off** — body-tax vs progress-tax.
- **Choose** — match the harm model (FL body → bane-self-harm; West progress → currency-spend). The valve itself is General.

**D78 — Weather generation** *(how weather appears)*
- **FL** — morning D6 table (Wind/Rainfall/Temperature) + HEAT/TEMP expanded (felt vs actual, seasonal, clothes/sleeping gear). (`FL 08-journeys.md:51-147`; `06 §7`)
- **West** — regional-killer reference (blue norther, chinook, haboob) + Trouble/condition triggers. (`West 11-frontier-survival-and-hunt.md:39-82`; `06 §7`)
- **Trade-off** — mechanical grind (every day taxes) vs dramatic scenes (storms are scenes).
- **Choose** — table for attritional survival; reference for dramatic, GM-discretion weather.

**D79 — Food tracking** *(how supply is counted)* ⟷ D18
- **FL** — Resource Dice (daily roll-down) + spoilage-by-HEAT + food-as-healing-currency (short break restores attributes via food/water). (`FL 08-journeys.md:307-430, 555-573`; `06 §8`)
- **West** — scene-level scarcity + profession/trap subsystem. (`West 11-frontier-survival-and-hunt.md:191-470`; `06 §8`)
- **Trade-off** — mechanical attrition vs color + mechanics.
- **Choose** — Resource Die when supply is load-bearing; profession when the hunt is the story; **wire food to healing (FL) for hard-survival games.**

**D80 — Camp failure model** *(what a bad camp costs)*
- **FL** — hidden Failed-Camp-Liability table (flaws: Exposed, Smoky, Wet…) + Trouble at Camp on 66. (`FL 08-journeys.md:531-553`; `06 §9`)
- **West** — condition-on-fail (Exhausted/Freezing). (`West 06-life-in-the-old-west.md:1277-1281`; `06 §9`)
- **Trade-off** — mechanical flaws vs condition tax.
- **Choose** — liability table for rich camp play; condition for speed. Both encode the fire-vs-concealment trade-off (General for stealth games).

**D81 — Downtime architecture** *(a second activity-menu for "not on the road")*
- **FL** — formal settlement menu (Ask Around / Seek Work / Petition / Trade / Carouse / Heal / Rest / Train) + notice board + Reputation. (`FL 08-journeys.md:686-1234`; `06 §10`)
- **West** — profession-scale economics + procedural reference. (`West 11-frontier-survival-and-hunt.md`; `06 §10`)
- **Trade-off** — Quarter-Day downtime economy vs job-as-campaign.
- **Choose** — formal menu when settlement play matters (highly transferable); profession when the job is the campaign.

**D82 — Mishap model (travel)** *(how travel failure taxes)* ⟷ D10
- **FL** — extensive D6/D66 mishap tables per activity. (`FL 08-journeys.md`; `06 §11`)
- **West** — Trouble system (narrative). (`06 §11`)
- **Trade-off** — mechanical tax vs narrative tax.
- **Choose** — keep consistent with the core loop's push-cost model (D1).

### 4.H Base / Faction / Mass-Scale (`07`)

**D83 — Ladder ceiling** *(the single most consequential campaign-design decision)*
- **FL** — full ladder through Polity (Solo → Party → Band → Company → Faction → Army → Polity). (`07 §9`)
- **West** — capped at Company/Town (Solo → Party → Band → Company). (`07 §9`)
- **Trade-off** — saga-scale interlocking vs focused personal scale.
- **Choose** — by intended session count: <8 = Party; 10–20 = Band; 20–60 = Company; 60+ = Polity. **Do not enable a rung the campaign cannot sustain.**

**D84 — Org-founding currency** *(what bases are bought with)*
- **FL** — materials + labor + crafting roll. (`FL 09-the-stronghold.md:17-22`; `07 §3`)
- **West** — Capital (illiquid, $250 = 1). (`West 06-life-in-the-old-west.md:11-49`; `07 §3`)
- **Trade-off** — crafting-driven vs investment-driven.
- **Choose** — materials for survival/crafting games; Capital for economic games; hybrid valid.

**D85 — Base → metacurrency link** *(does the base fuel adventure?)*
- **FL** — on: Stronghold grants +1 WP/PC/session + undisturbed rest. (`FL 09-the-stronghold.md:55-58`; `07 §4`)
- **West** — off (business grants coin/profit, not metacurrency). (`07 §5`)
- **Trade-off** — base fuels adventure directly vs base fuels economy.
- **Choose** — **FL link recommended** — it's the economic reason to want a base.

**D86 — Upkeep vectors** *(how the org is threatened)*
- **FL** — three independent: resourcing, payroll, security (each with a degeneration table). (`FL 09-the-stronghold.md:146-272`; `07 §3`)
- **West** — one: season Business/Town roll. (`West 08-campaigns-in-the-old-west.md:522-643`; `07 §3`)
- **Trade-off** — granular threat vs single roll.
- **Choose** — three-vector for survival grit; single-roll for pacing.

**D87 — Roster-org morale model** *(how the band's people are tracked)*
- **FL** — single stat (Morale 1–5) + Grievance Difficulty + Feud Track. (`FL 12-mercenaries-of-forbidden-lands.md:106-194`; `07 §6`)
- **West** — single stat (Cohesion 1–5) + per-member Loyalty 1–3 + Wanted. (`West 11-outlaws-of-the-old-west.md:62-122`; `07 §5`)
- **Trade-off** — gritty military friction vs outlaw-crew drama.
- **Choose** — both work; FL's is richer, West's is lighter.

**D88 — Abstraction-collapse threshold** *(scaling past ~50 members)*
- **FL** — on: Host Play (Ledger −6 to +6 abstracts the Host as one entity). (`FL 12-mercenaries-of-forbidden-lands.md:88-104`; `07 §6`)
- **West** — off: capped at Outfit (16–30). (`West 11-outlaws-of-the-old-west.md:36-45`; `07 §5`)
- **Trade-off** — scales indefinitely vs never needs to.
- **Choose** — include a Host-Play-equivalent if the roster org can grow past ~30–50.

**D89 — Faction turn** *(does the world move procedurally while PCs act?)* — **largest FL/West divergence**
- **FL** — on: full procedural turn (Mode, pillars, practices, acts, fallout D66). (`FL 11-politics-of-the-forbidden-lands.md:982-1091`; `07 §7`)
- **West** — absent. (`07 §5`)
- **Trade-off** — world-moves-while-PCs-do vs world-is-the-PCs'-work.
- **Choose** — enable for political/strategic campaigns; omit for character/community games (saves enormous bookkeeping).

**D90 — Faction-turn Mode dial** *(does turn length parameterize by war/peace?)*
- **FL** — on: Peace/Pressure = Season Turn; Muster/Campaign = Campaign Week. (`FL 11-politics-of-the-forbidden-lands.md:988-997`; `07 §7`)
- **West** — N/A. (`07 §7`)
- **Trade-off** — peaceful/warring factions run at different speeds vs fixed.
- **Choose** — on only if D89 is on.

**D91 — Faction stat block** *(the polity-scale skeleton)*
- **FL** — four-pillar: Mandate / Force / Reach / Hearth + 16 Practices + 9 Legacies + Basis of Rule. (`FL 11-politics-of-the-forbidden-lands.md:206-552`; `07 §7`)
- **West** — N/A. (`07 §7`)
- **Trade-off** — character-sheet-at-polity-scale vs absent.
- **Choose** — the four-pillar block is the recommended polity skeleton; Basis of Rule (why the org is obeyed) is high-value Optional.

**D92 — Town model** *(is the community a PC or an object?)*
- **FL** — settlement-as-faction-asset (Ruled/Protected/Tributary status ladder). (`FL 11-politics-of-the-forbidden-lands.md:907-977`; `07 §7`)
- **West** — settlement-as-character (six Aspects 1–6, Prosperity, failure at Aspect 0). (`West 08-campaigns-in-the-old-west.md:69-126`; `07 §5`)
- **Trade-off** — town-as-prize (conquest/politics) vs town-as-PC (community/dynasty).
- **Choose** — West model for community/dynasty; FL model for political/conquest.

**D93 — Mass combat** *(how org-scale violence resolves)*
- **FL** — on: troop-dice engine (reuses core dice grammar at unit scale: Base↔numbers, Advantage↔quality, Protection↔armor) + battle sequence + sieges. (`FL 12-battles-and-sieges.md:54-450`; `07 §8`)
- **West** — absent. (`07 §8`)
- **Trade-off** — resolves org-scale violence vs handwaves it.
- **Choose** — enable only if the campaign sustains field operations. **Reuse the core dice grammar; do not invent a new system.**

**D94 — Logistics layer** *(supply/disease/march — more decisive than the battle)*
- **FL** — on: supply units, forage depletion, disease doubling in sieges, stacking demoralization. (`FL 12-battles-and-sieges.md:906-1046`; `07 §8`)
- **West** — absent. (`07 §8`)
- **Trade-off** — wars feel like wars (arithmetic decides) vs board-game pieces.
- **Choose** — **if mass combat is on, logistics is more important than the battle sequence** — omit it and wars become board games.

**D95 — Generational play** *(family-saga / multi-decade campaigns)*
- **FL** — via Faction + Dynasty-of-house legacies. (`07 §7`)
- **West** — Dynasty: Legacy XP, play a family member after a PC's death. (`West 08-campaigns-in-the-old-west.md:57-60`; `07 §5`)
- **Trade-off** — polity-scale dynasties vs family-scale dynasty.
- **Choose** — West Dynasty is the cleaner model for family sagas; enable for generational campaigns.

### 4.I Gear & Economy (`08`)

**D96 — Economy model** *(what characters struggle for)* — **most tone-defining gear dial**
- **FL** — barter + commodity silver; gold ceremonial (prestige, +lead time). (`FL 10-gear.md:21-28`; `08 §4`)
- **West** — cash (dollars) + Capital ($250 = 1) + loans (5–10% interest) + salaries. (`West 06-life-in-the-old-west.md:11-125`; `08 §4`)
- **Trade-off** — scarcity-as-story (starved of money) vs money-as-story (managed by money).
- **Choose** — FL-pole for survival/post-collapse; West-pole for any genre where property, debt, or business is a pillar.

**D97 — Large-denomination store** *(the prestige/investment currency)*
- **FL** — ceremonial gold (static prestige). (`FL 10-gear.md:25`; `08 §4`)
- **West** — investment Capital (liquidates D6 × $50 — easy in, risky out). (`West 06-life-in-the-old-west.md:21, 49`; `08 §4`)
- **Trade-off** — static prestige vs liquidatable-but-risky assets.
- **Choose** — Capital only if you want an asset/business subsystem (D84); ceremonial-gold is lighter.

**D98 — Credit / debt** *(is debt a lever?)*
- **FL** — none. (`08 §4`)
- **West** — seasonal-interest loans with collateral, foreclosure on default. (`West 06-life-in-the-old-west.md:55-63`; `08 §4`)
- **Trade-off** — no debt drama vs default-as-story-beat.
- **Choose** — include loans when debt should be a lever NPCs and PCs pull on each other.

**D99 — Income stream** *(how characters get money)*
- **FL** — ad hoc (loot, favors, stronghold). (`08 §4`)
- **West** — salaries table ($65–300/season) + business rolls + hired-hands day-wages. (`West 06-life-in-the-old-west.md:84-125`; `08 §4`)
- **Trade-off** — found money vs predictable budget.
- **Choose** — salaries for settled/working characters; ad hoc for drifters/raiders.

**D100 — Property model** *(is owning things a pillar?)*
- **FL** — stronghold = craft project (materials + labor + time). (`FL 10-gear.md:700-714`; `08 §4`)
- **West** — Property Status 0–8 (Capital-priced) + Location + Features + haggle. (`West 06-life-in-the-old-west.md:230-351`; `08 §4`)
- **Trade-off** — build-it-yourself vs buy/haggle/auction.
- **Choose** — West model when *owning* is the game; FL model when *building* is the game.

**D101 — Availability resolution** *(how "can I buy it here?" is answered)*
- **FL** — per-item die roll (D6/D66), weekly restock. (`FL 10-gear.md:13-19`; `08 §3`)
- **West** — settlement-tag judgment (Mercantile/Law/amenities shift steps) + Strong Market threshold. (`West 06-life-in-the-old-west.md:500-541`; `08 §3`)
- **Trade-off** — randomized stock vs deterministic town-quality.
- **Choose** — FL's roll for sandbox unpredictability; West's tags for settlement-as-character. **Port West's two-sided scarcity→price table (−25% surplus … +100%+ panic).**

**D102 — Weapon stat model** *(what a weapon's bonus is)* ⟷ D1, D107
- **FL** — degrading Gear Dice (BONUS = a pool that drops by 1 per 💀 on push; breaks at 0). (`FL 05-combat-and-damage.md:456`; `08 §6`)
- **West** — flat ATTACK/DRAW mods (no push-degradation). (`West 06-life-in-the-old-west.md:715-735`; `08 §6`)
- **Trade-off** — weapon-as-resource-pool vs weapon-as-modifier.
- **Choose** — FL model when gear should *be* the cost face (survival); West model for faster, lighter combat. **Must align with D1.**

**D103 — Feature grammar shape** *(how loadout drives play)* — **central gear decision**
- **FL** — action-prerequisite tags (Parrying→PARRY, Hook→SHOVE, Edged→SLASH+Slash crits). (`FL 05-combat-and-damage.md:472-536`; `08 §6`)
- **West** — three layers: Features (stats) / Qualities (positive, max 4, stack) / Conditions (negative, Trouble-driven). (`West 06-life-in-the-old-west.md:842-905`; `08 §6`)
- **Trade-off** — unified action-gating tags vs separated good/bad stacks.
- **Choose** — FL when loadout should unlock tactical options; West when you want clean positive/negative optimization. Port the architecture (schema + small composable tags) either way.

**D104 — Quality ladder** *(what "Fine" means)*
- **FL** — 3-tier (Crude −1 breaks at 0 / Standard / Fine +1 Gear Die, ×2 cost); high-end = combat bonus + status. (`FL 05-combat-and-damage.md:462-470`; `08 §8`)
- **West** — 4-tier (Poor / Worn / Standard / Fine +50%); high-end = one gear bonus *or* ignore first Worn + resale/social. (`West 06-life-in-the-old-west.md:561-566`; `08 §8`)
- **Trade-off** — mechanical power vs social/economic load.
- **Choose** — FL for lethal games where Fine must *hit harder*; West for games where Fine is about *standing*. West's Poor/Worn split is more expressive.

**D105 — Degradation mechanism** *(how gear gets worse)* ⟷ D1, D102
- **FL** — continuous counter (Bonus ticks down on push 💀 / penetration). (`FL 05-combat-and-damage.md:456, 654-656`; `08 §8`)
- **West** — discrete Conditions (named tags from D6 table, Trouble-driven; "broken beyond repair" on a second Trouble/scene). (`West 06-life-in-the-old-west.md:885-905`; `08 §8`)
- **Trade-off** — granular attrition vs narrative breakage.
- **Choose** — must match D1/D102: continuous-counter pairs with bane-self-harm; discrete-Conditions pair with currency-spend + Trouble.

**D106 — Legendary tier** *(escalating-success-die gear)* ⟷ D9
- **FL** — on: artifact die (D8/D10/D12, 6+ = ⚔, scaled, immune to wear) + named + oddity table. (`FL 10-gear.md:922-1106`; `08 §9`)
- **West** — off (nearest analogue: Faith metacurrency). (`08 §9`)
- **Trade-off** — story-loaded top-tier items vs flat power ceiling.
- **Choose** — on for fantasy/pulp; off for grounded/historical.

**D107 — Crafting depth** *(is making things a pillar?)*
- **FL** — full unit-economy (fractional raw materials, material ladder Iron→Dwarven steel, masterwork, 4 gates: talent/workshop/materials/time). (`FL 10-gear.md:30-54, 802-921`; `08 §5`)
- **West** — folded into Availability/Quality + business prerequisites. (`08 §5`)
- **Trade-off** — deep simulation vs light resolution.
- **Choose** — FL depth when crafting is a pillar (alchemy, cybernetics, starship components); West lightness otherwise. Port the material ladder where crafting mastery should scale output.

### 4.J Design Philosophy (`10`)

**D108 — Thesis costume** *(ambition vs exposure — the game's currency and adversary)*
- **FL** — frontier survival: ambition = loot/legend; exposure = cold/hunger/the wild; currency = body + supply. (`FL system-design-map.md:18-20`; `10 §3`)
- **West** — Old West grit: ambition = pay/a name/a stake; exposure = distance/fever/debt/the law; currency = grit + belief. "The land does not care." (`West 02-the-1870s/00-introduction.md:13`; `10 §3`)
- **Trade-off** — ecological exposure vs documentary indifference.
- **Choose** — **state the thesis first** with physical, credible nouns (ambition = ___, exposure = ___). The two answers name the currency and the adversary.

**D109 — Primary loop weighting** *(which 2 of 5 loops carry the campaign)*
- **FL** — Expedition + Base (journey-and-investment). (`FL system-design-map.md:32-109`; `10 §5`)
- **West** — Conflict + Recovery (violence-and-aftermath). (`10 §5`)
- **Trade-off** — what play is *about*.
- **Choose** — weight the loop the genre's stories are about. All 5 loops must still function; 2 carry the campaign.

**D110 — Lethality calibration** *(the threat the Pressure Economy leans on)* ⟷ D54
- **FL** — Broken-easy / death-hard; never kill the defenseless (use the situation). (`FL 02-the-gamemaster.md:61`; `10 §7`)
- **West** — attrition-and-circumstance: a gutshot is survivable but the fever is not; medical technology will not save you. (`West 02-the-1870s/12-availability.md:37`; `10 §7`)
- **Trade-off** — mechanical breakpoint (clear "Broken" state) vs slow inevitability.
- **Choose** — together with D111 (they must agree): documentary genre → attrition-and-circumstance; inventive genre → cleaner breakpoint.

**D111 — Authenticity strictness** *(can you invent, or must you verify?)*
- **FL** — inventive-within-tone (material/ecological realism: cold, hunger, steel). (`FL realism-audit...md:34-52`; `10 §8`)
- **West** — documentary-verify (evidentiary realism: the 1870s ledger; "the bias should always be toward *not yet*"). (`West 02-the-1870s/12-availability.md:5`; `10 §8`)
- **Trade-off** — invention-permitted vs invention-forbidden.
- **Choose** — West's strictness for any historical genre; FL's for any invented-but-grounded genre. Both must pass the realism sniff-test (what decision does this make sharper?).

**D112 — Optional-rule surface** *(how many variant levers the table gets)*
- **FL** — large (heroic campaigns, artifact/Pride dice, Surge of Willpower, stronghold, expanded weather). (`10 §9, §11`)
- **West** — lean (Fast Initiative, Consumables as Resource Dice). (`10 §9, §11`)
- **Trade-off** — more dials vs leaner core.
- **Choose** — larger surface for high-fantasy/pulp; leaner for grounded/low-power. Governed by the General/Situational/Optional layering principle (`10 §9`).

**D113 — Failure-pressure idiom** *(mechanical vs narrative tax)* ⟷ D1, D10
- **FL** — mechanical (banes on dice, always on push). (`10 §11`)
- **West** — narrative (Trouble tables, exposure-gated). (`10 §11`)
- **Trade-off** — tax on the roll vs tax on the frame.
- **Choose** — see D10; must be consistent with the push-cost model.

---

## 5. Dial-dependency map (which choices constrain which)

Many dials are **not independent** — setting one constrains others. Setting them inconsistently is the most common cause of a game that "feels wrong." The engine's coherence rests on these alignment chains:

**The push-cost alignment chain (the engine's spine):**
> **D1 (push-cost)** ⟷ **D2 (cost-face trigger)** ⟷ **D10/D113 (failure-pressure idiom)** ⟷ **D102 (weapon stat)** ⟷ **D105 (degradation)** ⟷ **D77 (over-exertion valve)** ⟷ **D82 (travel mishap)**.

Two coherent configurations:
- **Bane configuration (FL-pole):** bane-self-harm + always-on-push banes + degrading Gear Dice + continuous-counter degradation + forced-march body-tax + D6/D66 mishap tables. *Body and gear are the currency.*
- **Trouble configuration (West-pole):** currency-spend + exposure-gated 1s + flat weapon mods + discrete Conditions + rush progress-tax + Trouble travel mishap. *Belief is the currency.*
- **Hybrid:** mix deliberately, not accidentally.

**The lethality/authenticity pair:** **D110 ⟷ D111** must agree — a documentary genre wants attrition-and-circumstance; an inventive genre can afford a cleaner breakpoint.

**The harm-routing chain:** **D51 (attribute mapping) ⟷ D52 (crit architecture) ⟷ D12 (damage typing) ⟷ D56 (Broken fiction).** Single-attribute mapping pairs with typed crit families; paired-split pairs with a master table.

**The power-density bundle:** **D62 (on/off) → D63 (density) → {D64-power tiers, D65 casting-risk, D66 fuel, D67 mishap, D68–69 gating, D70 ladder, D71 epic}.** Density sets all sub-dials by default.

**The ladder-ceiling cascade:** **D83 (ceiling) → {D88 abstraction-collapse, D89 faction turn, D93 mass combat, D94 logistics}.** Only enable a rung the campaign's session count can sustain.

**The economy-feel pair:** **D96 (economy model) → {D97 store, D98 credit, D99 income, D100 property}.** Strip the whole asset layer unless owning/business/debt is a pillar.

## 6. Combined preset archetypes

Each preset is a **coherent dial-set for a genre** — a starting configuration, not a finished game. Pick the closest preset, then tune. Each lists: the thesis, the key dial settings (referenced by D#), the resulting feel, and the FL/West affinity.

### Preset A — Grim Survival *(FL-like)*

> **Thesis:** Ambition = loot and legend; exposure = cold, hunger, the wild. The body and the supply are the currency.

| Dial | Setting |
| --- | --- |
| D1 Push-cost | Bane-self-harm |
| D2 / D10 / D113 Failure pressure | Banes, always-on-push |
| D3 / D4 / D5 Metacurrency | WP, harm-refueled, cap 10, no lockout |
| D108 / D110 / D111 Tone | Frontier survival; Broken-easy/death-hard; inventive-within-tone |
| D62 / D63 Power | ON, High |
| D73 / D74 / D75 Travel | Hex-crawl; Quarter-day + checklist; full 14-row menu |
| D78 / D79 Weather/Food | Morning table + HEAT/TEMP; Resource Die + food-as-healing-currency |
| D96 / D100 Economy/Property | Barter + commodity silver; stronghold-as-craft-project |
| D83 / D89 Faction | Full ladder through Polity; faction turn on |
| D102 / D103 / D106 Gear | Degrading Gear Dice; action-prerequisite tags; artifact die on |
| D22 / D70 Advancement | 5-rank talents; magic ladder 1–6 |
| D51 / D52 / D54 Harm | Single-attr; typed crit families (8); hard time limit |

**Feel:** attritional, exploratory, lethal-but-survivable; the wilderness is the dungeon. **Affinity:** FL.

### Preset B — Historical Realism *(West-like)*

> **Thesis:** Ambition = pay, a name, a stake; exposure = distance, fever, debt, the law. Grit and belief are the currency. "The land does not care."

| Dial | Setting |
| --- | --- |
| D1 Push-cost | Currency-spend (Faith) |
| D2 / D10 / D113 Failure pressure | Trouble tables, exposure-gated |
| D3 / D4 / D5 Metacurrency | Faith, action/success-refueled, 4/scenario, Shaken at 0 |
| D108 / D110 / D111 Tone | Old West grit; attrition-and-circumstance; documentary-verify |
| D62 Power | OFF (None) |
| D73 / D74 / D75 Travel | Pointcrawl; Shift (loose); implicit menu + mounted labor |
| D78 / D79 Weather/Food | Regional-killer reference + Trouble; profession/scavenging |
| D96 / D100 Economy/Property | Cash + capital + loans + salaries; Property Status ladder |
| D83 / D89 Faction | Capped at Company/Town; no faction turn |
| D92 Town model | Settlement-as-character (Aspects) |
| D102 / D103 / D106 Gear | Flat mods; three-layer grammar; legendary tier off |
| D22 / D25 Advancement | 2-rank talents; explicit narrative access gating |
| D51 / D52 / D54 Harm | Paired split; single master crit table (location); periodic death roll |
| D48 Ceremonial conflict | Duel (phased bonus chain) |

**Feel:** grounded, volatile, community-and-debt-driven; the country's indifference is the antagonist. **Affinity:** West.

### Preset C — Heroic Pulp *(magic high / lethality low / Faith-style)*

> **Thesis:** Ambition = glory and justice; exposure = villainy and overwhelming odds (environmental pressure low). Belief and daring are the currency.

| Dial | Setting |
| --- | --- |
| D1 Push-cost | Currency-spend or light hybrid |
| D2 / D10 / D113 Failure pressure | Trouble (light narrative) or none |
| D3 / D4 / D5 Metacurrency | Action/success-refueled; **larger cap (12–15)**; **no lockout** (forgiving) |
| D108 / D110 / D111 Tone | Heroic; **death very hard, fast recovery**; inventive-within-tone (loose) |
| D62 / D63 Power | ON, Medium–High (magic/powers central) |
| D9 / D106 Legendary | ON (artifact die + heroic-moment die) |
| D73 / D75 Travel | Pointcrawl, light; weather as color |
| D96 Economy | Cash, simple |
| D83 Faction | Off or Party only |
| D102 / D104 Gear | Flat mods; Fine = combat bonus; abundant |
| D22 / D26 Advancement | 2-rank or hybrid; **fast pace** |
| D52 / D53 / D54 Harm | Single master table; **low lethality climax**; no permanent scars (or easily healed) |
| D112 Optional surface | Large |
| D48 Ceremonial conflict | The signature showdown / stunt |

**Feel:** cinematic, forgiving, power-fantasy; characters are protected heroes with narrative momentum. **Affinity:** neither FL nor West — a deliberate third pole (raise the cap, lower the lethality, keep the action budget).

### Preset D — Post-Apocalypse *(magic none/low / hex / barter+scavenging / attrition-heavy)*

> **Thesis:** Ambition = survival and a patch of safety; exposure = fallout, raiders, decay. Salvage and the failing body are the currency.

| Dial | Setting |
| --- | --- |
| D1 Push-cost | Bane-self-harm (attritional) |
| D2 / D10 / D113 Failure pressure | Banes + Trouble (hybrid — rad-storms as Trouble, combat as banes) |
| D3 / D4 / D5 Metacurrency | WP harm-refueled *or* action-refueled; cap 10; **Shaken-style lockout optional** (despair spiral) |
| D108 / D110 / D111 Tone | Ruin survival; **high attrition**; inventive-within-tone |
| D62 / D63 Power | None or Low (salvage "gadgets" / mutations as Standard-tier reskins) |
| D73 / D74 / D75 Travel | Hex-crawl (exploration of ruin); Quarter-day + checklist; full menu |
| D78 / D79 Weather/Food | Weather table (rad-storms, toxic rain); Resource Die + **scavenging** + food-as-healing-currency |
| D96 / D100 Economy/Property | **Barter + scavenging** (commodity: caps, bullets, water); stronghold-as-craft-project |
| D83 / D89 Faction | Band/Company (raider gangs, settlements); faction turn optional |
| D102 / D103 / D107 Gear | Degrading; feature-grammar; **crafting from scrap** (material ladder = salvage tiers); consumables default-on |
| D22 Advancement | 5-rank or hybrid |
| D51 / D52 / D57 Harm | Typed families (**Ballistic / Radiation / Toxic / Cyber**); conditions heavy (Rad-sick, Dehydrated, Infected) |

**Feel:** desperate, scavenging, attritional; every bullet and every dose of Rad-Away is a gamble. **Affinity:** FL-pole on the body-as-currency chain, with scavenging layered on the economy.

### Preset E — Sci-Fi

> **Thesis:** Ambition = mission, credits, survival; exposure = vacuum, hostile tech, the enemy, the corporation. Oxygen and power are the currency.

| Dial | Setting |
| --- | --- |
| D1 Push-cost | Currency-spend or hybrid |
| D2 / D10 Failure pressure | Trouble + banes (hybrid) |
| D3 / D4 Metacurrency | Action/success-refueled or harm-refueled; cap 10 |
| D108 / D110 / D111 Tone | Mission/survival; medium lethality; inventive-but-grounded (tech must be coherent) |
| D62 / D63 Power | Medium (psi / gadgets / cyber) — often universal, so lean Low if everyone has it |
| D73 / D83 Travel/Base | Pointcrawl (star systems) **or** hex; ship-as-base (D85 base→metacurrency link on); life-support as attrition |
| D96 Economy | Credits + capital (corp shares, ship mortgages → D98 debt) |
| D89 Faction | Company/Faction (corps, fleets) |
| D102 / D103 / D105 Gear | Three-layer grammar; **Energy/Ballistic tags, smart-link, recoil, overheating Conditions** |
| D22 Advancement | 2-rank or hybrid |
| D51 / D52 / D58 Harm | Typed families (**Ballistic / Energy / Vacuum / Radiation / Toxic / Grav-Fall**); rated environmental hazards (hull breach, decompression) |
| D48 Ceremonial conflict | The dogfight / the chase / the hack-and-counter-hack |

**Feel:** technical, tactical, corporate-or-survival; gear and ship are load-bearing characters. **Affinity:** West-pole on grammar (three-layer tags fit tech), FL-pole on typed harm families.

### Preset F — Horror

> **Thesis:** Ambition = truth and survival; exposure = the unknown, the thing, madness. Sanity and the failing body are the currency.

| Dial | Setting |
| --- | --- |
| D1 Push-cost | Bane-self-harm (body **and mind** attrition — pushes hurt) |
| D2 / D10 Failure pressure | Banes + Trouble (**madness/mishap tables** for the unknown) |
| D3 / D4 / D5 Metacurrency | Small pool, harm-refueled; **Shaken-style lockout ON** (despair spiral when empty) |
| D108 / D110 / D111 Tone | Dread; **high lethality**; inventive but **tonally strict** (the unknown is never explained) |
| D62 / D63 Power | None or Low — **the unknown is the power, not the PCs** (if magic, it corrupts: D71 corruption spiral) |
| D73 Travel | Pointcrawl (investigation) **or confined** (the haunted house — no travel layer) |
| D96 Economy | Minimal/none |
| D83 Faction | Off (Solo/Party only) |
| D102 / D103 Gear | Light, mundane, degrading (weapons break, flashlights die — D18 Resource Dice for light/ammo) |
| D22 / D26 Advancement | 2-rank, slow |
| D51 / D52 / D56 / D57 Harm | **Horror crit family** + mental harm track (Empathy/Wits-Broken = madness); per-attribute Broken fiction (panic, despair); conditions: **Fear / Insanity / Exhaustion** |
| D61 Coup de grâce | Per-act conscience test (killing costs the killer) |
| D60 Retirement | Explicit (the survivor who can no longer face the dark becomes an NPC anchor) |

**Feel:** escalating dread, attritional, the-stakes-are-your-mind; survival is pyrrhic. **Affinity:** FL-pole on bane-self-harm and harm families (Horror table is FL's 8th family), West-pole on the Shaken lockout and the confined scope.

---

### Preset quick-reference (one-line feel)

| Preset | One-line feel | Push-cost | Power | Travel | Economy | Lethality |
| --- | --- | --- | --- | --- | --- | --- |
| **A Grim survival** | The wilderness is the dungeon | Bane-self-harm | High | Hex-crawl | Barter | High (Broken-easy) |
| **B Historical realism** | The country does not care | Currency-spend | None | Pointcrawl | Cash+capital | High (attrition) |
| **C Heroic pulp** | Protected heroes, big stunts | Currency/hybrid | Med–High | Light pointcrawl | Cash | Low |
| **D Post-apoc** | Every bullet is a gamble | Bane-self-harm | None/Low | Hex-crawl | Barter+scavenge | High attrition |
| **E Sci-fi** | Ship, gear, and corp debt | Currency/hybrid | Low–Med | Pointcrawl/hex | Credits+capital | Medium |
| **F Horror** | Survival is pyrrhic | Bane-self-harm (mind) | None/Low | Confined/pointcrawl | Minimal | High (madness) |

## 7. How to use this file (the configuration procedure)

When configuring a new YZE game:

1. **Pick a preset (§6)** closest to your genre — it bundles the hardest choices coherently. Note its affinity (FL-pole, West-pole, or hybrid) to know which sibling file is your deeper reference.
2. **State the thesis (D108)** — fill "ambition = ___, exposure = ___" with physical, credible nouns. If you cannot, the genre is not ready.
3. **Set the push-cost alignment chain (§5) first** — D1, D2, D10/D113, D102, D105, D77, D82. This single chain does more to set the *feel* than any other group of choices. Decide: bane-configuration, Trouble-configuration, or deliberate hybrid.
4. **Set the lethality/authenticity pair (D110 ⟷ D111)** together — they must agree.
5. **Walk the catalog (D1–D113)** in layer order (Engine → Character → Conflict → Harm → Power → Travel → Faction → Gear), setting each dial. For each, the *Choose* field tells you when to take FL-pole, West-pole, or a hybrid.
6. **Validate the dependency chains (§5)** — confirm every ⟷-marked dial is consistent with its partners.
7. **Validate against the math** (`13-balance-and-synergy.md`): default pool size, push rate, expected success, time-to-Broken, resource-die exhaustion, WP throughput, milestone rate vs arc length.
8. **Run the Warning Signs** (`10 §10`): subsystem inflation, silent invalidation, false realism, vague enforcement, misleading survivability, setting-laden generic language, sibling-skill duplication. A dial setting that trips a warning sign is flagged for deeper review, not auto-rejected.

**The governing rule:** a new genre's job is to *find its currency and wire the cost model to it* (D1), *find its signature spatial pressure and ceremonial beat* (D35/D48), *find its relationship to money* (D96), *set its power ceiling* (D62/D63), and *set its campaign ceiling* (D83). Everything else is calibration. The same spine produces any genre by swapping the dials — that is the engine's proof, and this catalog is its controls.
