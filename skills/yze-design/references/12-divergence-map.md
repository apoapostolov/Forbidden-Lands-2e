<!-- markdownlint-disable MD013 MD024 MD041 MD060 -->

# Divergence Map — Every FL-vs-West Decision

> **STATUS: FILLED (Pass-2 roll-up complete).** This is the skill's single highest-value original artifact: a complete table of every design decision where FL and West made different choices, plus the synthesis of *what the pattern of divergences reveals about the engine's true degrees of freedom.* Built incrementally from each system file's "Divergence rows" section (`00`–`10`).

## Contents

1. Source provenance
2. Abstraction target
3. How to read the map
4. The divergence table (master)
5. Cluster: Core resolution
6. Cluster: Character & progression
7. Cluster: Conflict & harm
8. Cluster: Power layer
9. Cluster: Travel & downtime
10. Cluster: Org/faction/economy
11. Cluster: GM procedures & tone
12. Synthesis — what the divergences reveal about the engine

## 1. Source provenance

This file is a **roll-up**, not a primary source. Each row is sourced from the "Divergence rows" section of `00`–`10`. Primary evidence is the two corebooks (see each system file's provenance block for exact paths). Cross-links throughout point to the system file that documents each row *in depth*.

The roll-up contains **52 master decisions** distilled from **128 source rows** (many decisions recur across files — e.g. the push-cost model appears in `00`, `04`, `05`, `08` — and are consolidated here into one canonical row with all cross-links).

- **FL** = *Forbidden Lands 2E* (the maximal/attritional pole).
- **West** = *Tales of the Old West 2E* (the lighter/dramatic pole; often the "zero instance").

## 2. Abstraction target

Produce the **single highest-value original artifact** of the skill: a complete table of every design decision where FL and West made different choices, in the form:

> *decision · option A (FL) · option B (West) · trade-off · when to choose each*

This is what makes the engine *configurable*: by seeing exactly where two professional builds diverged and why, a designer building a third game can make an informed choice rather than a guess. The table is grouped by cluster and ends with a synthesis: *what the pattern of divergences reveals about the engine's true degrees of freedom.*

## 3. How to read the map

**Row format:** `| Decision | FL option | West option | Trade-off | When to choose A | When to choose B |`

- **Decision** names the design choice in engine terms (not genre terms).
- **FL option / West option** are the two calibrated points. Where a cell is `(none)` / `(absent)` / `(implicit)`, that absence is *itself* the data — see the power layer (`05`) and the org-ceiling row (`07`) where West's omission is the proof.
- **Trade-off** states the tension in one phrase.
- **When to choose A / When to choose B** gives genre/campaign-length guidance.
- Each cluster section (§5–§11) holds the same rows expanded with cross-links to the system file documenting that row in depth.

**Cluster grouping (matches the master table in §4):**

1. **Core resolution** — the loop, dice grammar, pushing, Willpower/Faith, failure layer. *(From `00`.)*
2. **Character & progression** — attributes, damage typing, the inner fire, generation, XP, talent ladders. *(From `01`, `02`.)*
3. **Conflict & harm** — action budget, initiative, positioning, melee/ranged/social, crit tables, conditions, death. *(From `03`, `04`.)*
4. **Power layer** — magic on/off, casting models, fuel, mishaps, gating, ceiling. *(From `05`.)*
5. **Travel & downtime** — spatial model, time block, activity menu, weather, food, camp, recovery. *(From `06`.)*
6. **Org/faction/economy** — base lifecycle, ladder ceiling, faction turn, mass combat, economy model, gear grammar. *(From `07`, `08`.)*
7. **GM procedures & tone** — principles, encounter engine, settlement-as-character, statblocks, solo, campaign-state trackers, failure doctrine. *(From `09`.)*

**The two poles in one sentence:** FL is the *body-as-currency, simulate-everything, escalate-to-polity* pole; West is the *belief-as-currency, dramatize-the-fiction, cap-at-community* pole. Every row below is a calibrated point on the choice between them.

## 4. The divergence table (master)

> The deliverable. 52 rows, cluster-grouped, with the system file documenting each row in depth named in the final column (`→ file`). Where a single engine decision recurs across files, it appears once here with all cross-links.

### Cluster 1 — Core resolution (`00-engine-core.md`)

| Decision | FL option | West option | Trade-off | When to choose FL | When to choose West | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| **Push-cost model** | Bane self-harm (body/gear damage) | Faith spend (currency) | Gritty attrition vs resource drama | Survival, horror, attritional | Dramatic, character-driven, pulpy | `00 §6` |
| **Cost-face trigger** | 💀 on dice, always on push | 1s, only on Risky/Desperate fails | Endogenous vs frame-gated | Harm should feel inevitable | Harm should feel *chosen* | `00 §6` |
| **Failure amplifier** | Failed push + ≥3💀 = severe setback | Failed push = +1 Trouble | Mechanical severity vs narrative severity | Match genre's failure relationship | Match genre's failure relationship | `00 §10` |
| **Willpower/Faith refuel** | Harm-earned (1 WP/💀 on Base) | Action/success-earned | Virtuous damage loop vs behavior-reward loop | Attritional games | Dramatic, character-driven | `00 §7` |
| **Willpower/Faith refresh model** | Earned in play + stronghold rest | 4/scenario + reset at season | Slow-burn vs predictable budget | Sandbox grit | Paced drama | `00 §7` |
| **Willpower/Faith depletion** | (no lockout) | Shaken Faith at 0 | No floor vs a despair beat | Omit unless "hitting zero" is a beat | Add a lockout for a despair beat | `00 §7` |
| **Modification target** | Skill Dice only (+ negative dice) | Unified pool | Colored precision vs simplicity | Gear/attr/skill cleanly separable | Speed | `00 §5` |
| **Help gating** | Lowest Empathy caps bonus | Each helper needs ≥1 rank | Social-trust limit vs competence floor | Relationship-heavy games | Competence-focused | `00 §5` |
| **Success ladder default** | Threshold model (1⚔ default, raise to 2/3) | Grade model (0/1/2/3+ read) | GM-sets-bar vs roll-reads-grade | (hybrid recommended) | (hybrid recommended) | `00 §4` |
| **Legendary-die rule set** | Artifact dice (D8/D10/D12) + Pride | None | High-tier escalation vs flat power | Fantasy, pulp | Grounded, historical | `00 §9` |
| **Failure-pressure layer** | Banes (on the dice) | Trouble tables (narrative, by exposure) | Dice tax vs story tax | Both work; Trouble + bane-free pool is lighter | Both work | `00 §10` |

### Cluster 2 — Character & progression (`01-character-model.md`, `02-progression-and-xp.md`)

| Decision | FL option | West option | Trade-off | When to choose FL | When to choose West | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| **Attribute naming** | Survival axes (STR/AGI/WIT/EMP) | Frontier-grit (Grit/Quick/Cunning/Docity) | Generic-resolver vs genre-flavored | Pure portability only | Name after genre's tension (default) | `01 §3` |
| **Damage typing** | By position (silent) | By name (Hurts/Shakes/Vexes/Doubts) | Functional vs fictional-rich | (always name them — West-style) | Always name them | `01 §4` |
| **Attribute ceiling (creation)** | 2–4 (5/6 key) | 1–5 | Narrow competent range vs wider curve | Narrow power spread | Wider curve | `01 §3` |
| **Inner-fire model** | Pride (die, narrow, once/session) | Faith (currency, broad, whole loop) | Peak moments vs sustained agency | Lethal one-shots; hybrid for new games | Dramatic arcs; hybrid for new games | `01 §5` |
| **Inner-fire identity load** | "Stubborn will" (a note) | One-sentence belief system | Light vs heavy identity load | Genre is about grit | Genre is about belief | `01 §5` |
| **Social-anchor depth** | Relationships + Dark Secret + home settlement | + Pardner + Compadres + Big Dream + town | Minimum vs maximum | Minimum suffices | Add Big Dream always; Compadres if NPC allies | `01 §6` |
| **Consumables tracking** | Resource Dice (default) | Counted (Resource Dice optional) | Die-roll vs bookkeeping | (Resource Dice always — less bookkeeping) | Resource Dice opt-in | `01 §7` |
| **Fast-gen identity selector** | Kin (biological/cultural species) | Archetype (social profession) | Fantasy races vs social roles | Pick genre's primary sorter | Pick genre's primary sorter | `01 §8` |
| **Lifepath default** | Optional add-on book | Standard deep method | Deep lifepath = specialist text | Ship one; make optional but available | Ship one | `01 §8` |
| **Party-identity layer** | (none formalized) | Group Concepts (7) | None vs shared starting identity | Add for strong party-binding | Add for strong party-binding | `01 §8` |
| **Talent ladder depth** | 5-rank (kin/profession/general) | 2-rank (Basic/Advanced) | Build identity vs accessibility | Long campaigns | Short arcs / new players | `02 §5` |
| **Narrative access gating** | Implicit (via teacher requirement) | Explicit (forge/society/institution) | Implicit vs fiction-gated | (always make it explicit — West-style) | Always make explicit | `02 §5` |
| **XP pace choice** | Tale (fast) vs Campaign (slow) | Single default pace | Adjustable arc length vs simplicity | Flexible groups | Simplicity | `02 §3` |
| **Willpower/Faith→XP** | Yes (10 WP → 1 XP, optional) | No | Links short-term pool to long-term growth | Optional; use if pools cap out | — | `02 §9` |

### Cluster 3 — Conflict & harm (`03-conflict-and-combat.md`, `04-harm-and-consequences.md`)

| Decision | FL option | West option | Trade-off | When to choose FL | When to choose West | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| **Initiative archetype** | Rolled segment (AGILITY+WITS ⚔), sticky, simultaneous ties | Random card draw, redrawn each Round, suit-breaks-ties | Stat-coupled & predictable vs volatile & dramatic | Tactical / character-build | Chaotic / genre-iconic | `03 §4` |
| **In-Round order malleability** | Delay + FEINT swaps segments | Once-per-scene ally card-swap | Solo-tactical vs cooperative-tactical | Duel-style play | Party-coordination play | `03 §4` |
| **Range band count** | 5 (no Medium) | 6 (adds Medium) | Coarser vs finer ranged granularity | Melee/bow genres | Firearm genres | `03 §5` |
| **Terrain layer** | Zone features + borders (Cramped/Rough/Open/Dark; Blocked/Obscured) | Cover ratings + to-hit penalty grades (Partial/Good/Heavy) | Movement/LOS pressure vs concealment/defense pressure | Dungeons, ruins | Gunfights; hybrid possible | `03 §5` |
| **Cover as armor** | On (Cover Rating, no to-hit penalty) | On (Cover Rating + to-hit penalty grades) | Soak-only vs soak + to-hit | Lower-tech | Firearm genres (dual model) | `03 §5` |
| **Reach rule set** | Deep (Short/Normal/Long + CUT IN/BRACE/INTERCEPT/FEINT) | Light (Brace for ranged only; melee reach implicit) | Melee tactical depth vs simplicity | Melee/historical genres | Ranged-centric genres | `03 §6` |
| **Melee verb model** | Verb-rich (Slash/Stab/Punch, each w/ defense profile) | Verb-single + modifiers (Melee + All-Out/Called/Stunt menu) | Weapon-as-puzzle vs success-as-authorship | Weapon-dueling genres | Cinematic narrative combat | `03 §9` |
| **Defense verbs & economy** | Dodge + Parry; pure success-cancellation + weapon matrix | Dodge + Block + Protect; success-menu (cancel *or* counterattack) | Two-verb vs three-verb; fast vs aggressive | Speed | "Defense can hurt"; bodyguard play | `03 §8` |
| **Ranged weapon model** | Bow/crossbow/throw + READY/LOAD + feature tags | Firearm-action budget (single/double/lever) + Fanning/Overwatch/Quick Shot/reload | Feature-tag depth vs action-budget depth | Fantasy | Firearm genres | `03 §10` |
| **Social conflict currency** | Binary: comply *or* escalate to violence | Damage-attrition: surplus ⚔ as Vexes/Doubts, can Break | Short/punchy vs attritional/scene-ending | Escalation-prone games | Reputation-as-combat games | `03 §11` |
| **Ceremonial conflict** | Ambush/sneak-attack (free pre-init action, no reactions) | Duel: Face Off → Go for Your Guns → Shoot-off (phased bonus chain) | Opening-advantage vs escalating-script | Include genre's signature beat | Include genre's signature beat | `03 §12` |
| **Morale rating model** | Per-side dice with add/subtract factors | Flat 3-tier (2/4/6 dice by troop quality) | Tunable-per-enemy vs fast-at-table | Bespoke foes | Quick resolution | `03 §13` |
| **Mount depth** | Condition (−1 vs mounted; polearm synergy) | Participant (statted horse, ANIMAL HANDLIN', Spooked, lasso, fall-risk) | Tactical-edge vs full-rule set | Low-mount genres | Mounted genres | `03 §14` |
| **Critical-injury architecture** | Family of typed tables (8: Slash/Blunt/Stab/Burn/Acid/Cold/Swallow/Horror) | Single master table indexed by location × severity | Damage-type specificity vs anatomical parsimony | Meaningfully different harm types | All hits are "a wound somewhere" | `04 §5` |
| **Damage→attribute mapping** | Single named attribute per source | Paired split (Hurts/Shakes; Doubts/Vexes), alternating | Clean routing vs two-axis attrition | Damage type must route to a table | Physical/mental harm spreads across two stats | `04 §3` |
| **Broken fiction** | Generic helplessness | Per-attribute helplessness flavor (collapse/drained/outburst/panic) | One state vs four story-beats | (per-attribute — Broken should be an event) | Per-attribute | `04 §3` |
| **Permanent injury** | Dedicated Permanent table per family (on `65`) | Inline Long-term Effect column (preventable by heal) | Rich maiming rule set vs parsimony | Survival/horror | Action | `04 §10` |
| **Death model** | Hard time limit (die when up unless healed) | Periodic un-pushable Death roll (full Grit) each interval | Urgency/pacing vs player engagement | GM-paced grit | Keep the dying player rolling | `04 §8` |
| **Conditions set** | 5 (incl. Addicted); single-attr recovery block | 5 (incl. Heatstroke); paired-attr; Heatstroke imposes Trouble | Trait-flavored vs attritional-spread + dice-pressure | Clean routing | "Feel bad at the dice" | `04 §6` |
| **Retirement path** | Explicit "retainer NPC, keep XP," dignified prose | Implicit | Story-beat exit vs table-decides | (always consider FL's path — high-value, low-cost) | Consider FL's path | `04 §10` |
| **Coup-de-grâce gate** | Character trait (Cold-blooded allows; Honorable forbids) | Per-act conscience test (fail a no-ability roll) + 1 Doubts | Trait-gated vs per-act moral cost | Trait model | Include if killing should cost the killer | `04 §4` |
| **Degradation rule pattern** | Continuous counter (Gear Bonus ticks down on push 💀/penetration) | Discrete Conditions (named tags from D6 table, Trouble-driven) | Granular attrition vs narrative breakage | Gear is a resource pool | Lighter bookkeeping | `04`, `08 §8` |

### Cluster 4 — Power layer (`05-power-layer.md`)

| Decision | FL option | West option | Trade-off | When to choose FL | When to choose West | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| **Power layer on/off** | ON — full apparatus (17 disciplines, 3 spell types, casting models, fuel, mishaps, epic) | OFF — zero instance | Engine + maximal rule set vs engine alone | Powers *are* the fiction | Powers break the fiction | `05 §10` |
| **What Willpower/Faith buys** | Pushing, talents, **and entire new capabilities** (spells) | Pushing and Trouble-buyoff **only** | Extended purchase scope vs core-scope only | If layer is on | If layer is off | `05 §5` |
| **Power families** | Three tiers (Spells slow / Power Words fast-reactive / Rituals long-dramatic) | None | Tactical + reactive + ceremonial | High density; prune for Low/Medium | — | `05 §3` |
| **Casting-risk choice** | Safe + Chance + Overcharge | None | Guaranteed-costly / rolled-cheap / pushed-scale | Pick ≥1 when layer on | — | `05 §4` |
| **Self-harm override (Burn)** | Yes — chosen quantity, random attribute | None | Desperation valve | Adds grit (Medium+ density) | — | `05 §5` |
| **Failure pressure for powers** | 17 typed D66 mishap families, count-modified | Core Trouble (narrative, frame-gated) | Specific-and-memorable vs narrative-and-light | Medium+ density | Trouble-reskin for Low | `05 §7` |
| **Material gating** | Ingredients (+1 PL), consumed | None | Powers need *stuff* | Scarcity matters to genre | — | `05 §6` |
| **Knowledge gating** | Grimoires (−1 rank), teachers, secrecy | None | Powers need *books/teachers* | Scholarly/tradition magic | — | `05 §6` |
| **Rank ladder height** | 1–6 (taller than 1–3 talent cap) | None | Long power-growth arc | Scale to campaign length | — | `05 §8` |
| **High-end ceiling** | Epic ingredients (permanent attributes, sacrifices, places); corruption spiral | None | World-changing gated by irreplaceable fiction costs | High density only | — | `05 §9` |
| **Player-authored powers** | Full forging appendix (benchmarks + 10-check veto) | None | Extensibility with safety rails | Table wants to invent powers | — | `05 §8` |

### Cluster 5 — Travel & downtime (`06-travel-and-downtime.md`)

| Decision | FL option | West option | Trade-off | When to choose FL | When to choose West | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| **Spatial model** | Hex-crawl (10 km tiles, per-tile navigation + mishaps) | Pointcrawl (miles/Shift between points, rush roll) | Exploration depth vs prep/speed | Sandbox exploration & fog-of-war | Trail/pursuit drama & fast pacing | `06 §3` |
| **Time block** | 4 Quarter Days (Morning/Day/Evening/Night) + daily checklist | Shift (count loose) | Structured attritional day vs flexible block | Day should feel like a series of costs | Lighter pacing | `06 §4` |
| **Activity-menu formality** | 14-row formal menu, solo/shared tagged | ~6–8 implicit jobs + mounted/animal labor | Tight labor puzzle vs genre-textured jobs | Travel is the game | Travel is connective tissue | `06 §5` |
| **Navigation cost** | Survival roll **per hex entered**; fail = mishap table | One rush roll/block; Trouble halts progress | Mechanical per-tile tax vs narrative per-block tax | Exploration | Drama | `06 §6` |
| **Over-exertion valve** | Forced march: Endurance, Agility damage + SLEEPY | Rush: MOVE/Animal Handlin', +50% or Trouble halt | Body-tax vs progress-tax | Pairs with bane-self-harm | Pairs with currency-spend | `06 §6` |
| **Weather system** | Morning D6 table (Wind/Rain/Temp) + HEAT/TEMP expanded + clothes/gear | Regional-killer reference + Trouble/condition triggers | Mechanical grind vs dramatic scenes | Attritional survival | Dramatic, GM-discretion | `06 §7` |
| **Food tracking** | Resource Dice, daily roll-down, spoilage-by-HEAT | Scene-level scarcity + profession/trap rule set | Mechanical attrition vs color + rules | Supply is load-bearing | The hunt is the story | `06 §8` |
| **Food-as-healing-currency** | Yes — short break restores attributes via food/water/etc. | No (recovery via camp clearing conditions) | Supply = survival vs supply = flavor | Hard-survival games | — | `06 §10` |
| **Camp failure model** | Hidden Failed-Camp-Liability table (flaws) + Trouble at Camp | Condition on fail (Exhausted/Freezing) | Mechanical flaws vs condition tax | Rich camp play | Speed | `06 §9` |
| **Downtime architecture** | Formal settlement menu + notice board + Reputation | Profession/economics + procedural reference | Quarter-Day downtime economy vs job-as-campaign | Settlement play matters | The job is the campaign | `06 §10` |
| **Mishap model** | Extensive D6/D66 mishap tables per activity | Trouble system (narrative) | Dice tax vs story tax | Granularity | Speed (consistent with `00 §6`) | `06 §11` |

### Cluster 6 — Org/faction/economy (`07-base-faction-mass-scale.md`, `08-gear-and-economy.md`)

| Decision | FL option | West option | Trade-off | When to choose FL | When to choose West | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| **Org ladder ceiling** | Full ladder through Polity (base→band→company→faction→army→polity) | Capped at Company/Town | Saga-scale interlocking vs focused personal scale | Epic/political | Community/frontier | `07 §9` |
| **Faction turn** | Full procedural turn layer (Mode, pillars, practices, acts, fallout) | Absent | World-moves-while-PCs-do vs world-is-the-PCs'-work | Political/strategic campaigns | Character/community games | `07 §7` |
| **Mass combat** | Troop-dice engine + logistics + sieges | Absent | Resolves org-scale violence vs handwaves it | Campaign sustains field operations | Otherwise it's bookkeeping | `07 §8` |
| **Org-founding currency** | Materials + labor + crafting roll | Capital (illiquid, $250=1) | Crafting-driven vs investment-driven | Survival/crafting games | Economic games | `07 §3`, `08 §4` |
| **Town model** | Settlement = faction asset (Ruled/Protected/Tributary) | Settlement = shared character (Aspects, Prosperity, failure at 0) | Town-as-object vs town-as-PC | Political/conquest | Community/dynasty | `07 §5` |
| **Roster-org morale** | Morale 1-5 + Grievance Difficulty + Feud Track | Cohesion 1-5 + Loyalty 1-3 + Wanted | Gritty military friction vs outlaw-crew drama | Both work; FL richer | Both work; West lighter | `07 §6` |
| **Abstraction-collapse at scale** | Host Play (Ledger −6 to +6 past ~50) | None (capped at Outfit 16-30) | Scales past 50 bodies vs never needs to | Roster org grows past ~30-50 | — | `07 §6` |
| **Upkeep vectors** | Three independent (resourcing, payroll, security) | One (season Business/Town roll) | Granular threat vs single roll | Survival grit | Pacing | `07 §3` |
| **Base→Willpower/Faith link** | Stronghold grants +1 WP/PC/session | (Business grants coin/profit, not Willpower/Faith) | Base fuels adventure directly vs base fuels economy | Recommended — economic reason to want a base | — | `07 §4` |
| **Generational play** | (via Faction + Dynasty-of-house legacies) | Dynasty: Legacy XP, play a family member | Polity-scale dynasties vs family-scale dynasty | Polity sagas | Family sagas (cleaner model) | `07 §9` |
| **Economy model** | Barter + commodity silver; gold ceremonial | Cash (dollars) + Capital + loans + salaries | Scarcity-as-story vs money-as-story | Survival/post-collapse | Property/debt/business is a pillar | `08 §4` |
| **Credit / debt** | None | Seasonal-interest loans (5–10%), collateral, foreclosure | No debt drama vs default-as-story-beat | — | Debt should be a lever NPCs/PCs pull | `08 §4` |
| **Income stream** | Ad hoc (loot, favors, stronghold) | Salaries table + business rolls + hired-hands day-wages | Found money vs predictable budget | Drifters/raiders | Settled/working characters | `08 §4` |
| **Property model** | Stronghold = craft project (materials + labor + time) | Property Status 0–8 (Capital-priced) + Location + Features | Build-it-yourself vs buy/haggle/auction | *Building* is the game | *Owning* is the game | `08 §4` |
| **Availability resolution** | Per-item die roll (D6/D66), weekly restock | Settlement-tag judgment (Mercantile/Law/amenities shift steps) | Randomized stock vs deterministic town-quality | Sandbox unpredictability | Settlement-as-character | `08 §3` |
| **Weapon stat model** | Gear Dice (BONUS) that *degrade on push* | Flat ATTACK/DRAW mods, no push-degradation | Weapon-as-resource-pool vs weapon-as-modifier | Gear should *be* the cost face | Faster, lighter combat | `08 §6` |
| **Feature grammar shape** | Tags double as action-prerequisites (Parrying→PARRY, Hook→SHOVE) | Three layers: Features (stats) / Qualities (pos, max 4) / Conditions (neg, Trouble-driven) | Unified action-gating tags vs separated good/bad stacks | Loadout drives *tactical options* | Clean positive/negative optimization | `08 §6` |
| **Quality high-end effect** | +1 Gear Die (combat bonus) + status | +1 gear bonus (one-cap) *or* ignore first Worn + resale/social | Mechanical power vs social/economic load | Lethal games where Fine must *hit harder* | Fine is about *standing* | `08 §8` |
| **Legendary tier** | Artifact die (D8/D10/D12) + named + oddity table | None (nearest analogue: Faith) | Escalating-success-die + story-loaded items vs flat ceiling | Fantasy/pulp | Grounded/historical | `08 §9` |
| **Consumables tracking (scope)** | Resource dice as **default** | Resource dice as **Optional Module**; loose counting default | Always-on logistics vs opt-in survival mode | Wilderness/survival | Urban/cinematic | `08 §10` |
| **Crafting depth** | Full unit-economy (fractional raw materials, material ladder, masterwork) | Folded into Availability/Quality + business prerequisites | Deep simulation vs light resolution | Crafting is a pillar | Otherwise | `08 §5` |

### Cluster 7 — GM procedures & tone (`09-gm-procedures.md`)

| Decision | FL option | West option | Trade-off | When to choose FL | When to choose West | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| **GM principles** | 7 explicit, codified axioms | Diffuse campaign-driver list (Ambitions, Vengeance, Justice…) | Codified judgement vs inspirational themes | GM wants a checklist | Looser, theme-driven table | `09 §3` |
| **Encounter table** | 44-entry D66 matrix, 9 terrain columns, situational entries | Campaign seeds + adventure-embedded encounters; no master terrain matrix | Dense random-but-weighted engine vs authored scenario encounters | Hex-sandbox | Narrative/region campaign | `09 §4` |
| **Settlement model (GM-side)** | Village generator: history→present→locations→characters; vicissitudes 3D6+vars; Need/Heat ledger | Your Town: 6 Aspects + Prosperity; player-chosen amenities | GM-side simulationist vs player-facing advancement tree | GM-authored living places | Party-owned growing towns | `09 §5` |
| **Settlement state roll** | Vicissitudes 3D6 + variables (monthly) / settlement turn 2D6 (short) | Turn of the Season: Business + Personal Fortune + Town Fortune D66 (seasonal) | Gritty attrition sim vs story-hook generator | Survival/decline pressure | Character-driven hooks | `09 §5` |
| **NPC statblock** | Inline prose, procedurally generatable, attr ceiling 8 | 8-column table roster, hand-authored archetypes | Embedded-in-encounter vs quick-reference bestiary | Encounters-as-stories | Glanceable cast | `09 §6` |
| **Solo-play layer** | Full suite: companions, quarter-day procedure, card oracles | Not present in core | GMless-capable vs GM-required | Solo/co-op/zero-prep | Traditional GM-led | `09 §7` |
| **Campaign-state tracker** | Stronghold events (Reputation-weighted D66) + household Need/Heat + vicissitude variables | Faction Standing (4-track ledger) + week-ticked Faction Clocks + Aspect/Prosperity fortune modifiers | Base-under-siege + internal feuds vs faction-relations + region-clock | Base-defense/decline | Multi-faction political sandboxes | `09 §8` |
| **Adventure-site doctrine** | Site-as-dungeon: locations+NPCs+events, no narrative, 15-min turn, legend handouts | Sandbox country: multiple roads through, factions on their own clocks, shortcut-positive | Hexcrawl-site vs region-sandbox | Pointcrawled sites | Open political country | `09 §9` |
| **Failure / forward motion** | Fail-forward (GM judgement) + reoccurring-encounter memory | Sandbox "country answers back" + faction clocks | GM-adjudicated vs clock-driven | GM wants authority over pace | Table wants the world self-driving | `09 §10` |

## 5. Cluster: Core resolution

*Source: `00-engine-core.md` §10.* The engine's spine: how a roll is made, what pushing costs, what failure taxes, and what the Willpower/Faith is *for.* This cluster holds the **most load-bearing** divergence in the whole engine — the push-cost model — which is why it recurs in `04`, `05`, and `08`: every downstream layer inherits the cost model chosen here.

**The spine both share:** D6 pool, sixes = success (⚔), push-once, a graded success ladder, a capped-10 Willpower/Faith that converts risk into future agency, opposed rolls, group rolls (highest/lowest selector), and the "one chance" rule (no free retries). *This spine does not diverge.* Every row below is a choice *on top of* an invariant core.

The two canonical points and why they matter:

- **FL — "the body is the currency."** Pushing is free in WP; you pay in 💀 damage to attributes/gear. Failure is priced in *harm*. Willpower/Faith refuels from harm. Banes are always-on. Result: gritty, attritional, physical pressure.
- **West — "belief is the currency."** Pushing costs 1 Faith. Failure is priced in *Trouble* (narrative, frame-gated). Willpower/Faith refuels from action/success. Result: dramatic, resource-management pressure without mandatory harm.

**The hybrid recommendation (for new games):** a currency cost *plus* a lighter bane or Trouble trigger, so pushing always costs *something* visible but isn't always injurious. See `00 §11` for the full choice set and build recipe.

*(The 11 rows for this cluster are in §4, Cluster 1. Each is documented in depth in `00-engine-core.md` §3–§10.)*

## 6. Cluster: Character & progression

*Sources: `01-character-model.md` §9, `02-progression-and-xp.md` §10.* The model being advanced: a 4×4 attribute-skill grid, attribute-as-HP with named damage types, a per-session inner fire, a social anchor, and dual fast/deep generation — plus how XP is earned, spent, and gated behind in-fiction time.

**What does NOT diverge (the invariant skeleton):** exactly 4 attributes × 4 skills (16 skills); attribute-as-HP with a "Broken at 0" state; dual fast + deep generation; age as a sub-choice trading attributes for skills; the XP-source mix (1–3/session + lethal +1, +2/+4 milestones, 1/season downtime); the skill cost curve `(new rank × 3)` with teacher; Legacy XP on death/retirement. *The convergence here is so strong it reads as the engine's spec.*

**Where the two games diverge is almost entirely *flavor and depth*:** West names attributes and damage types in-genre (free genre-loading); FL keeps them generic-resolver. FL's talent ladder runs to 5 ranks (build identity); West's stops at 2 (accessibility). FL's inner fire is a die (Pride, peak moments); West's is a currency (Faith, sustained agency). West adds Big Dream + Compadres + Group Concepts (social depth); FL adds Dark Secret + the lifepath book (backstory depth).

**The single transferable insight:** *skill and attribute names do ~60% of the work of re-skinning YZE for a new genre.* The rules barely change; the fiction transforms completely. This is the engine's greatest strength and the reason a generic skill like this one is possible.

*(The 14 rows for this cluster are in §4, Cluster 2. Documented in `01` §3–§8 and `02` §3–§9.)*

## 7. Cluster: Conflict & harm

*Sources: `03-conflict-and-combat.md` §15, `04-harm-and-consequences.md` §11.* The action budget and the layered consequence cascade. This is the largest cluster because conflict and harm are where the engine's *genre flavor* is densest.

**The invariant load-bearing rules (do not change):**
- **2 actions/Round = (1 slow + 1 fast) ∨ (2 fast).** This is the single most important combat rule. Everything hangs off it.
- **Reactions draw from the same budget.** This is the defense-bloat prevention. Never make reactions free without rebalancing damage.
- **Named range bands, not measured distances.** A conversation, not a grid. Playable without a battlemat.
- **The D66 critical-injury architecture** with the `65`=maim / `66`=die climax split. Both games use it identically; only the table *shape* differs.
- **Attribute-as-HP → Broken → death threshold → stabilization window.** The harm cascade is invariant; the *flavor* of each layer diverges.

**Where FL and West diverge is *what scarce resource combat is about*:**
- FL's conflict is a **reach-and-zone tactical puzzle** (melee-centric): Slash/Stab/Punch verbs, a deep reach rule set, zone features, weapon-vs-defense matrices. FL's harm is a **family of typed tables** — the *kind* of wound is the story.
- West's conflict is a **firearm-and-cover volatility engine** (ranged-centric): action-type tags (single/double/lever), Fanning/Overwatch/Quick Shot, cover ratings + to-hit grades, card-draw initiative. West's harm is a **single anatomical master table** — *where* you got hit is the story. West's social conflict can *end* a character (Broken by Doubts) without a punch.

**The cross-cutting principle:** *the degradation rule pattern follows the cost model.* FL's continuous-counter degradation (Gear Bonus ticks down on push 💀) is the gear-layer instance of bane-self-harm; West's discrete Conditions (named tags, Trouble-driven) is the gear-layer instance of currency-spend + Trouble. Choose them consistently. (This row recurs in Cluster 6 because it straddles conflict and gear.)

*(The 22 rows for this cluster are in §4, Cluster 3. Documented in `03` §3–§14 and `04` §3–§10.)*

## 8. Cluster: Power layer

*Source: `05-power-layer.md` §11.* The engine's largest *optional* rule set. This cluster's central divergence is the cleanest in the whole engine: **FL has the full power layer; West has none.** That *is* the row.

**The deliverable is the proof-by-construction:** West runs at full strength — core loop, Willpower/Faith, push, Trouble, conflict, harm, travel, orgs — *with the power layer entirely removed.* This is not a deficiency; it is the demonstration that the power layer is **purely additive** — a plug-in, not a load-bearing wall.

**When the layer IS on (FL = the maximal instance), three principles govern it:**
1. **It must add *decisions*, not just power.** FL's three-way casting choice (safe / overcharge / chance) + Burn makes every cast a gamble, never a solved problem.
2. **Fuel binds it to the core loop.** Powers cost the *same* WP that pushing earns. A caster who wants to cast must first engage the engine's risk rules. The layer is *downstream* of the harm-and-push economy.
3. **Mishaps keep it from being solved.** Per-discipline D66 families (the typed-table pattern from `04 §5`, applied to magical failure) make backlash *specific and memorable*, with a count-modified gradient that slides toward character-ending rows.

**The ceiling is gated by *cost*, not *fuel*.** Epic magic can't be bought with banked WP — it requires irreplaceable, fiction-bound payments (permanent attributes, monster hearts, sacrifices, world-shaping places). At the top, the limit is *what you're willing to lose or become*, not *what you have saved*.

**The on/off + density choice** (none / low / medium / high) is the single most important genre-setting decision in this cluster. West = none; FL = high; low/medium map the reskin middle (gadgets, psi, miracles, knacks).

*(The 11 rows for this cluster are in §4, Cluster 4. Documented in `05` §3–§10. Note: every "West option" is the *absence* of the rule set — and the engine works anyway.)*

## 9. Cluster: Travel & downtime

*Source: `06-travel-and-downtime.md` §11.* The journey engine: where YZE turns *logistics* into play.

**The invariant load-bearing artifact — the activity menu:** distribute the party's labor across a fixed menu so *every PC has a travel job*, balanced so that movement, navigation, security, and supply are *mutually exclusive* demands. You cannot move, navigate, watch, and forage with the same character in the same block. This is what makes travel a resource-allocation puzzle rather than narration.

**The central choice — the spatial model — determines *what travel is about*:**
- **FL = hex-crawl:** the world is a grid of unknown tiles; each tile entered is a procedure (navigate → possibly mishap → possibly encounter). Travel is the *discovery of unknown space*; the map is treasure. Favors exploration depth, fog-of-war. Cost: prep and table-time per tile.
- **West = pointcrawl:** the world is a graph of named points with edge weights (miles × terrain). Travel is the *traversal of a known route under attrition*; the points are the story. Favors speed, pursuit/drama. Cost: less discovery.

**The over-exertion valve + the recovery loop are mirror images** — and they follow the cost model: FL's forced march (Endurance, Agility damage, sleep loss) pairs with bane-self-harm; West's rush (MOVE/Animal Handlin', Trouble halts progress) pairs with currency-spend. *Choose them consistently with `00 §6`.*

**Weather and food are where the two games push depth in opposite directions:** FL formalizes both as rules systems (morning D6 weather table, HEAT/TEMP felt-vs-actual split, Resource Dice food economy wired into healing); West renders them as *setting* — regional weather killers as prose, hunting as professions, survival as procedures. Same pressure (the environment taxes you); opposite expressions (deterministic grind vs dramatic scenes).

*(The 11 rows for this cluster are in §4, Cluster 5. Documented in `06` §3–§10.)*

## 10. Cluster: Org/faction/economy

*Sources: `07-base-faction-mass-scale.md` §10, `08-gear-and-economy.md` §11.* The downtime org layer and the gear/money layer. These two files are grouped because the org-founding currency (materials vs Capital) and the economy model (barter vs cash) are the *same choice* seen from two angles.

**The invariant pattern — the five-beat org lifecycle:** founding → functions → upkeep → events → scale. Every org in both games (a Stronghold, a saloon, a mercenary band, a faction, an outlaw crew, the town the players grow) runs on this same pattern. The beats are genre-neutral; the choices on each beat are where genre is set.

**The single most consequential decision — the ladder ceiling:** FL climbs the full ladder (Solo → Party → Band → Company → Faction → Army → Polity, all interlocking); West *caps* at Company/Town. This is not FL being "bigger" — it is a deliberate genre choice. **The ceiling determines what the campaign is *about*:** individuals, communities, or power. West's genres (frontier, dynasty, outlaw) are about people and places, so the cap is a *feature*. FL's genres (epic fantasy, saga) are about power, so the ladder extends.

**The faction turn is the largest single FL/West divergence in the whole org layer** — the only rule set that runs on its own clock *above* the players' adventure play. Its absence in West is the proof that the engine runs without "the world moving procedurally while the PCs act." West's world is the community the PCs build; FL's world is the politics that happens around them. Opposite fantasies (community vs power), same engine.

**The economy choice *is* the genre's statement about value:** FL's barter + ceremonial gold says scarcity and isolation are the story; West's cash + capital + loans says money, debt, and reputation are the story. The same engine produces opposite tones by swapping the currency — exactly as the core loop does by swapping the push-cost model.

**The feature grammar (weapons/armor = composable tags, not stat lines)** is the gear layer's most reusable artifact and is shared in architecture by both games; they diverge only in *shape* (FL's tags double as action-prerequisites; West splits into Features/Qualities/Conditions). The degradation rule pattern again follows the cost model (continuous counter vs discrete Conditions).

*(The 21 rows for this cluster are in §4, Cluster 6. Documented in `07` §3–§9 and `08` §3–§10.)*

## 11. Cluster: GM procedures & tone

*Source: `09-gm-procedures.md` §10.* The GM-facing operating manual: how a GM *runs* the engine with minimal prep.

**The most transferable deliverables (port near-verbatim for any genre):**
- **5–7 GM principles** (de-flavored): open-table/player-driven agenda, lore-as-rumor, say-yes-to-player-agenda, scarcity/cost-of-safety, acquisition-as-target, lethality-as-story, emergent-finale. These are the judgement rules where the dice are silent.
- **The settlement-as-character model:** a settlement is a character sheet for a place — attributes, a state machine, internal-faction pressure gauges, a resource economy, and a growth rule pattern driven by player investment. Both games share this; they diverge on *who drives it* (FL: GM-authored village generator; West: player-facing Your Town with amenities).
- **The minimal NPC statblock:** 4 attributes + 1–4 relevant skills + 0–3 talents + gear + special tags only when the NPC breaks a core rule.

**Where FL and West diverge is *how the world generates pressure*:** FL rolls D66 event tables weighted by the party's Reputation (base-under-siege + internal feuds via Need/Heat); West runs week-ticked Faction Clocks and seasonal Fortune rolls (multi-faction political pressure + character-driven hooks). FL's failure is fail-forward by GM judgement; West's failure is "the country answers back" via self-driving clocks. Both make the campaign *remember*; they differ on whether the GM or the system holds the pace.

**The solo-play layer** (FL only) is worth flagging: the full GMless suite (companions, quarter-day procedure, card oracles with a bias choice) proves the engine runs without a GM at all — another instance of "the engine is complete without this layer."

*(The 9 rows for this cluster are in §4, Cluster 7. Documented in `09` §3–§9.)*

## 12. Synthesis — what the divergences reveal about the engine

> **This is the file's key intellectual output.** The 52 rows above are not 52 independent decisions. They are ~52 *expressions* of a small number of **true degrees of freedom** — the axes along which the engine is actually configurable. Everything else is reskin.

### The hypothesis, verified

The brief hypothesized four true degrees of freedom. The data confirms them — and refines the framing. Reading all 128 source rows distilled into 52 master decisions, the divergences cluster overwhelmingly around **four true degrees of freedom** plus a fifth meta-axis. Here they are, each named, defined, and traced to the rows that express it.

#### Choice axis 1 — How failure is priced: harm vs currency

**This is the engine's master choice.** It is set once, in the core loop (`00 §6`), and *every downstream layer inherits it.* Trace the cascade:

- **Push cost** (bane-self-harm vs Faith-spend) — `00` row 1.
- **Cost-face trigger** (always-on vs frame-gated) — `00` row 2.
- **Failure-pressure layer** (banes on the dice vs Trouble in the story) — `00` row 11.
- **Willpower/Faith refuel** (harm-earned vs action-earned) — `00` row 4.
- **Failure amplifier** (rules severity vs narrative severity) — `00` row 3.
- **Gear degradation** (continuous counter on push 💀 vs discrete Conditions via Trouble) — Cluster 3 + `08`.
- **Over-exertion valve** (forced march = body-tax vs rush = progress/Trouble-tax) — `06`.
- **Food-as-healing-currency** (supply restores attributes vs conditions clear) — `06`.
- **Conditions impose Trouble** (West's Heatstroke taxes *all* rolls) — `04`.
- **Mishap model** (D66 tables per activity vs Trouble system) — `06`, `05`.

**That is ~10 of the 52 rows, all flowing from one choice.** Set the push-cost model and you have implicitly chosen the degradation rule pattern, the over-exertion valve flavor, the failure-pressure layer's character, and whether food/magic/travel failure is a dice tax or a narrative one. The engine's own build recipe (`00 §11`) confirms this: *"Decide the push-cost model (choice 1) — this single choice does more to set tone than any other."* FL's bane-self-harm makes a game where **the body is the currency**; West's Faith-spend makes a game where **belief is the currency**. A new genre's job is to find *its* currency and wire the cost model to it.

#### Choice axis 2 — How dense the optional/power layer is

The power layer (`05`) is the engine's largest *optional* rule set, and West proves it is **purely additive** — remove it and nothing in `00` breaks. But the *density* choice doesn't stop at magic. It governs every layer that can be present at "high density" (FL) or "absent/light" (West):

- **Power layer on/off + density** (none/low/medium/high) — `05` rows.
- **Legendary-die / artifact tier** (D8/D10/D12 + oddities vs none) — `00`, `08`.
- **Feature-grammar depth** (action-prerequisite tags vs three-layer stats/qualities/conditions vs flat) — `08`.
- **Crafting depth** (full unit-economy + material ladder vs folded into availability) — `08`.
- **Reach rule set** (deep verb set vs light/omitted) — `03`.
- **Mass combat + logistics** (troop-dice engine vs absent) — `07`.
- **Solo-play layer** (full oracle suite vs absent) — `09`.
- **HEAT/TEMP weather depth** (felt-vs-actual split vs implicit) — `06`.

The pattern: **FL is the maximal-density pole; West is the zero/light-density pole.** A genre picks, layer by layer, how much apparatus to instantiate. The on/off + density decision for the power layer is the flagship, but the *same choice* recurs for legendary gear, crafting, reach, mass combat, solo play, and weather. **"How much machinery do you want between the player and the fiction?"** — that is the second true choice axis.

#### Choice axis 3 — How literally the setting is simulated

This is the axis the brief named "how literally the setting is simulated," and the data refines it into a sharp opposition: **rules-forward simulation vs narrative dramatism.** Same pressure, opposite expression, across half a dozen layers:

- **Spatial model** (hex-crawl tile-by-tile vs pointcrawl miles-between-points) — `06`.
- **Weather** (morning D6 table + HEAT/TEMP vs regional-killer reference + Trouble) — `06`.
- **Food tracking** (Resource Dice daily roll-down + spoilage vs profession/trap + scene scarcity) — `06`.
- **Camp failure** (hidden liability D66 table vs condition-on-fail) — `06`.
- **Critical-injury architecture** (family of typed tables vs single master table) — `04`.
- **Encounter engine** (44-entry D66 terrain matrix vs authored scenario encounters) — `09`.
- **Settlement state roll** (vicissitudes 3D6 + variables vs seasonal Fortune D66) — `09`.
- **Damage→attribute mapping** (single attribute per source vs paired split) — `04`.
- **Mishap tables vs Trouble** (dice tax vs story tax) — `06`, `05`.

FL asks *"what does the system deterministically produce?"* — a hex you enter triggers a procedure; a morning triggers a weather roll; a Broken state routes to a typed table. West asks *"what does the fiction dramatically demand?"* — the country is an indifferent antagonist whose weather *kills* (as prose); Trouble halts your rush because the fiction says so; the Hunt is a profession with economics, not a per-block roll. **Both produce pressure; they differ in whether the pressure comes from a die roll or a scene.** This is the third choice axis: *does the world simulate itself, or does the GM dramatize it?*

#### Choice axis 4 — How deep the build/advancement system goes

The brief's fourth hypothesis, confirmed cleanly. The two games sit at opposite ends of a *depth* choice that governs how much character/build differentiation the system produces:

- **Talent ladder depth** (5-rank vs 2-rank) — `02`.
- **Talent cost curve** (rank×3 scaling vs two flat steps) — `02`.
- **Attribute ceiling** (2–4 / 5–6 key vs 1–5) — `01`.
- **Inner-fire model** (Pride die, narrow vs Faith currency, broad) — `01`.
- **Social-anchor depth** (minimum vs maximum: +Pardner +Compadres +Big Dream) — `01`.
- **Magic-path ladder** (1–6 vs none) — `02`, `05`.
- **Material-quality ladder** (Iron→Dwarven steel, talent-gated vs buyable grade) — `08`.
- **Party-identity layer** (none vs Group Concepts) — `01`.

FL's deeper ladders produce *build identity* — a rank-5 Champion feels meaningfully different from a rank-2 one, over a long campaign. West's flatter ladders produce *broad, accessible competence* — faster to grok, lower cognitive load, suited to shorter arcs. **The depth choice is calibrated to intended campaign length** (`02`): 5-rank for 20–60 session sagas; 2-rank for 3–20 session arcs. Neither is better; the choice is about how long characters live and how much they specialize.

#### Choice axis 5 (meta) — How high the org ladder climbs

This emerged from the data as a distinct fifth axis the brief did not name but the org layer (`07`) makes inescapable: **the ladder ceiling.** It is *meta* because it governs not a single rule but *which rule sets exist at all*:

- **Org ladder ceiling** (full ladder through Polity vs capped at Company/Town) — `07`.
- **Faction turn** (full procedural turn layer vs absent) — `07`.
- **Mass combat** (troop-dice engine vs absent) — `07`.
- **Town model** (settlement-as-faction-asset vs settlement-as-character) — `07`.
- **Abstraction-collapse at scale** (Host Play/Ledger vs capped roster) — `07`.
- **Generational play** (polity dynasties vs family Dynasty/Legacy XP) — `07`.

**The ceiling determines what the campaign is *about*:** individuals, communities, or power. West caps the ladder to stay focused on people and places; FL extends it to make the campaign a saga. Every rung above the ceiling is bookkeeping the campaign cannot repay — so choosing the ceiling is choosing the campaign's *scope and subject*. This is arguably the single most consequential campaign-design decision in the whole engine, and it sits orthogonally to the other four degrees of freedom (you can have a harm-priced, high-density, simulationist, deep-build game at *any* ceiling).

### What is NOT a choice axis — the reskin surface

Everything else in the 52 rows is **reskin** — flavor that transforms the fiction without changing the engine. The evidence for this is the engine's own convergence:

- **The 4×4 attribute-skill grid** is invariant. Both games use exactly 4 attributes × 4 skills. Renaming them (STR/AGI/WIT/EMP → Grit/Quick/Cunning/Docity) does ~60% of the re-skinning work. *The grid is the load-bearing constraint; the names are paint.*
- **The XP-source mix** converges to near-identical numbers (1–3/session, +1 lethal, +2/+4 milestones, 1/season downtime). *The engine has settled on its advancement budget.*
- **The skill cost curve** is essentially identical (`new rank × 3` with teacher, ~×1.33 without). *This is the engine's default.*
- **The D66 critical-injury architecture** (Tens/Units, `65`/`66` climax) is shared verbatim. *Only the table contents are genre work.*
- **The availability/scarcity table** is near-identical machinery (4-step ladder, ±price curve). *Port it verbatim.*
- **The activity menu, the five-beat org lifecycle, the settlement-as-character model, the minimal NPC statblock, the GM principles** — all invariant in architecture; only the nouns change.

**The single most powerful consequence:** you can take the entire engine and make it feel like cyberpunk, post-apoc, space opera, or Napoleonic naval warfare largely by (a) renaming the 16 skills + 4 attributes + their damage types, (b) swapping the identity selector (kin → lineage/species; archetype → role), and (c) setting the four choices above. *The rules barely change; the fiction transforms completely.* This is the engine's greatest strength — and it is *why a generic design skill is possible at all.*

### The configurability surface, named

The Year Zero Engine's **actual configurability surface** is four choices plus one meta-axis:

| # | Choice axis | Set in | What it decides | Rows it governs |
| --- | --- | --- | --- | --- |
| **1** | **Failure pricing: harm vs currency** | `00 §6` (push-cost model) | Tone: attritional vs dramatic | ~10 (push, cost-face, refuel, failure layer, degradation, over-exertion, food-healing, conditions, mishaps, amplifier) |
| **2** | **Optional-layer density: minimal vs maximal** | `05 §10` (on/off + density) | How much machinery sits between player and fiction | ~8 (power, legendary die, feature grammar, crafting, reach, mass combat, solo, weather depth) |
| **3** | **Simulation register: rules-forward vs dramatic** | `06 §3` (spatial model) | Does the world simulate itself or does the GM dramatize it? | ~9 (spatial, weather, food, camp, crit architecture, encounters, settlement roll, damage mapping, mishap vs Trouble) |
| **4** | **Build/advancement depth: flat vs deep** | `02 §5` (ladder depth) | How much character differentiation; calibrated to campaign length | ~8 (talent ladder, cost curve, attribute ceiling, inner fire, social anchor, magic ladder, material ladder, party-identity) |
| **5 (meta)** | **Org-ladder ceiling: individual vs polity** | `07 §9` (ceiling) | What the campaign is *about*; which rule sets exist | ~6 (ceiling, faction turn, mass combat, town model, large-scale, generational) |

**~41 of the 52 rows are governed by these five axes.** The remaining ~11 are pure reskin (attribute/skill names, damage-type names, identity selector, ceremonial-gold vs Capital, verb names, terrain-column nouns, encounter-entry prose). A designer setting these five choices and then doing the reskin has *chosen the whole engine stance* — resolution, character, conflict, harm, power, travel, orgs, economy, and GM procedures — without touching the invariant spine.

### The engine's thesis, in one sentence

> **The Year Zero Engine is a single invariant spine — D6 pool, sixes-as-success, push-once-pay-a-cost, attribute-as-HP, 2-actions-per-Round, D66 consequences, activity-menu logistics, five-beat org lifecycle — on which five choices are set. FL and West are the same game with the choices turned to opposite ends. A new genre's job is to find its currency (choice 1), decide how much machinery it wants (choice 2), choose whether the world simulates or dramatizes (choice 3), calibrate build depth to campaign length (choice 4), and pick its ceiling (choice 5) — then reskin the nouns. Everything else is already done.**
