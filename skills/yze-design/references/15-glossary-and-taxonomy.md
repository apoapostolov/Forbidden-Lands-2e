<!-- markdownlint-disable MD013 MD024 MD041 MD060 -->

# Glossary and Taxonomy — Generic ↔ FL ↔ West

> **STATUS: FILLED (Pass-1 extraction + Pass-2 abstraction complete).** This is the roll-up reference — two artifacts in one file: (1) the **translation table** that maps every game-specific noun in either source book to a canonical generic term (three columns: *Generic · FL · West*), and (2) the **master taxonomy** of every engine system/subsystem, one-line definitions grouped by cluster, cross-linked to the reference file that owns it. Together these enforce the skill's "no setting nouns in the generic layer" rule and give the skill a map of itself.

## Contents

1. Source provenance
2. Abstraction target
3. The translation table (generic ↔ FL ↔ West)
4. The master system taxonomy (clustered, with ref links)
5. Cross-reference index (term → file §)
6. Design intent

## 1. Source provenance

Synthesis file — built from the terminology of both corebooks, harvested through the sibling reference files (00–10, 13):

- **FL terms:** `01-corebook/01-front-matter.md` (dice/symbols ⚔💀🩸), `02-your-adventurer.md` (kin/profession/Pride/Dark Secret/Resource Dice/encumbrance), `03-skills.md` (16 skills/WP/levels of effort), `05-combat-and-damage.md` (Round/Turn/Shift, range bands, weapon features), `06-critical-injuries.md` (typed D66 families), `07-magic.md` (Spells/Power Words/Rituals/Burn/disciplines), `08-journeys.md` (Quarter Day/hex/activities), `09-the-stronghold.md` (Stronghold/functions), `10-gear.md` (Supply/Artifact Die/Resource Die), `12-mercenaries-of-forbidden-lands.md` (Mercenary Company/Morale), `11-politics-of-the-forbidden-lands.md` (Faction/Pillars/Legacies).
- **West terms:** `01-corebook/02-your-player-character.md` (4 attributes+damage types/Archetype/Pardner/Compadres/Big Dream/Your Tale Begins), `03-rolling-the-bones.md` (Faith/Trouble/Declared Effort/Stunts), `05-conflict-and-damage.md` (card initiative/Duel/cover ratings), `06-life-in-the-old-west.md` (dollar/Capital/Business/Property/Outlaw Band/Resource Die Optional Module), `08-campaigns-in-the-old-west.md` (Your Town/Aspects/Turn of the Season/Dynasty), `11-outlaws-of-the-old-west.md` (Cohesion/Wanted).

## 2. Abstraction target

Two artifacts:

1. **The translation table** — every game-specific noun in either book mapped to a canonical generic term, so the rest of the skill stays engine-agnostic. Three columns: *Generic · FL · West*. **This is what enforces the "no setting nouns in the generic layer" rule.** When a sibling file (00–14) speaks generically, every term it uses must appear in the left column here; when it instantiates, it cites the FL/West column.
2. **The master taxonomy** — a one-line definition of every engine system/subsystem, grouped by cluster (Core, Character, Conflict, Harm, Power, Travel, Org, Gear, GM, Meta), each cross-linked to the reference file that owns it. **This is the skill's map of itself.**

The two artifacts are mutually validating: the translation table's generic terms are the *nouns* the taxonomy names; the taxonomy's clusters are the *homes* the translation table's terms live in.

## 3. The translation table (generic ↔ FL ↔ West)

Read each row as: *"the generic term (left) is what FL calls X (middle) and West calls Y (right)."* A blank cell or `(none)` means that game does not instantiate the concept. Rows marked **(abstraction)** name a generic concept that neither book names literally but that both implement.

### 3.1 Character model

| Generic | FL | West |
| --- | --- | --- |
| **attribute** | Strength / Agility / Wits / Empathy (STR/AGI/WIT/EMP) | Grit / Quick / Cunning / Docity |
| **attribute (damage track)** | each attribute is a health track; reduced by 🩸 | each attribute is a health track; reduced by Hurts/Shakes/Vexes/Doubts |
| **named damage type** (per attribute) | (silent — damage typed by position) | **Hurts** (Grit) / **Shakes** (Quick) / **Vexes** (Cunning) / **Doubts** (Docity) |
| **skill / ability** (the 16) | Skill (16, 4 per attribute) | Ability (16, 4 per attribute) |
| **talent** (general advancement unit) | Talent (kin / profession-"Path" / general; ranks 1–5) | Talent (Background/Combat/Frontier/Social/Trade/Outlaw; Basic + Advanced, 2 ranks) |
| **kin / ancestry** (fantasy identity selector) | Kin (8: human/elf/half-elf/dwarf/halfling/wolfkin/orc/goblin) | (none — uses Archetype) |
| **profession / archetype** (social identity selector) | Profession (9: Champion/Druid/Fighter/Hunter/Minstrel/Peddler/Rider/Rogue/Sorcerer) | Archetype (10: Gentlefolk/Grifter/Homesteader/Laborer/Lawman/Outlaw/Prospector/Ranch Hand/Tracker/Trader) |
| **fast generation method** | Kin + Profession + age | Archetype + age |
| **deep generation method** (lifepath) | Life Generator / Lifepaths of the Forbidden Lands | "Your Tale Begins" lifepath |
| **party-identity layer** (optional shared start) | (none formalized) | Group Concepts (7) |
| **Broken** (attribute-at-zero helpless state) | Broken | Broken (flavored per attribute: collapse / drained / outburst / panic) |
| **age dial** (young=raw/old=skilled) | Young (15) / Adult (14) / Old (13) attr points | Greenhorn (6) / Tested (5) / Old-timer (4) attr points |
| **encumbrance base** | primary physical attribute × 2 (Strength) | primary physical attribute × 2 (Grit) |
| **over-encumbrance tax** | Endurance roll or 1 Agility damage | Resilience roll or 1 Shakes |

### 3.2 Protected dial / personal resource

| Generic | FL | West |
| --- | --- | --- |
| **metacurrency** (capped pool, risk→agency) | Willpower Points (WP), cap 10 | Faith (Points), cap 10 |
| **protected dial** (personal pressure-relief resource) | **Pride** (a die, D8/D10/D12, once/session, protective rolls only) | **Faith** (the same pool as metacurrency — broad-scope currency spend) |
| **protected-dial identity** (the belief sentence) | "stubborn will" (a note) | one-sentence belief ("the Lord is my shepherd…") |
| **depletion state** (metacurrency at zero) | (no explicit lockout) | **Shaken** Faith (cannot push, cannot gain) |
| **metacurrency refuel** | harm-earned (1 WP per 💀 on Base Dice when pushing) | action/success-earned (1 Faith on 3-⚔ un-pushed; rituals/actions) |
| **metacurrency→XP conversion** (optional) | 10 WP → 1 XP (optional) | (none) |

### 3.3 Resolution core

| Generic | FL | West |
| --- | --- | --- |
| **base die** (attribute dice, damageable) | Base Dice (white) | (rolled as part of unified pool; attribute dice) |
| **skill die** (skill dice, inert 1s) | Skill Dice (maroon) | (rolled as part of unified pool; ability dice) |
| **gear die** (gear dice, degradable) | Gear Dice / Weapon Dice (black) | (no gear-die type; gear enters as flat modification) |
| **success face** | ⚔ (sword) | ⚔ (sword) |
| **cost face / latent bane** | 💀 (skull) on Base & Gear dice | 1s (latent Trouble fuel, counted only on Risky/Desperate fails) |
| **damage symbol** | 🩸 (blood) | (uses named damage nouns: Hurts/Shakes/Vexes/Doubts) |
| **success ladder (threshold model)** | Levels of Effort (Normal 1⚔ / Challenging 2⚔ Great / Difficult 3⚔ Critical) | Declared Effort (Standard/Bold/Desperate — 1/2/3 ⚔ thresholds) |
| **success ladder (grade model)** | (surplus ⚔ = richer detail) | 0 Fail / 1 Limited / 2 Complete / 3+ Critical |
| **surplus-success spend** | (extra ⚔ = detail/clues/positioning) | Stunts (+1 dmg / knockdown / grapple / crit) |
| **escalating-success die** (legendary) | Artifact Die (D8 Mighty / D10 Epic / D12 Legendary) | (none) |
| **heroic-moment die** (character's peak) | Pride (D8/D10/D12, once/session) | (none — Faith is currency, not a die) |
| **opposed roll** | opposed (attacker ⚔ minus defender ⚔; only attacker pushes) | opposed (same spine) |
| **group roll** | lowest-level (sneak) / highest-level (track) / all-must-succeed (climb) | same three variants |
| **one-chance rule** (no free retry) | same approach cannot be retried for same goal | same rule |
| **help** (cooperation bonus) | +1 each (max +3), gated by lowest Empathy | +1 each (max +3), each helper needs ≥1 rank |

### 3.4 Failure pressure / push cost

| Generic | FL | West |
| --- | --- | --- |
| **push** (reroll non-6 once) | Push (reroll non-6, non-💀 dice) | Push (reroll non-6 dice) |
| **push-cost model: bane-self-harm** | 💀 on Base = 1🩸 attribute damage; 💀 on Gear = −1 bonus | (not used) |
| **push-cost model: currency-spend** | (not used) | 1 Faith per push |
| **failure pressure: banes-on-dice** | Bane (💀, always on push) | (none — uses Trouble) |
| **failure pressure: table** | (none — uses banes + crit tables) | **Trouble** (Safe / Risky / Desperate + outcome tables) |
| **failure amplifier** (failed push) | ≥3 💀 = severe setback | failed push = +1 Trouble |
| **modification target** | Skill Dice only (negative dice below zero) | unified pool (generic dice) |
| **difficulty ladder** (±3 cap, stack) | Trivial +3 … Formidable −3 (7 steps) | identical table |

### 3.5 Conflict / combat

| Generic | FL | West |
| --- | --- | --- |
| **combat time unit** (tactical) | Round (~10s–1min) | Round (5–10s) |
| **exploration time unit** | Turn (~15min) | Turn (5–10min) |
| **recovery/downtime time unit** | Quarter Day (implied) | Shift (6h) |
| **travel time block** | Quarter Day (Morning/Day/Evening/Night) | Shift (4/day: Morning/Afternoon/Evening/Night) |
| **initiative: rolled-sticky** | AGILITY+WITS ⚔ → segment (sticky in-Round) | (not used) |
| **initiative: random-redrawn** | (not used) | card draw (Aces high; spades>hearts>diamonds>clubs) |
| **initiative: side-based (fast)** | Fast Skill Roll Initiative (optional) | Fast Initiative (Quick roll, optional) |
| **action budget** | 2/Round = (1 slow + 1 fast) ∨ (2 fast) | identical |
| **slow action** | Slash/Stab/Cast Spell/Flee/Treat… | Melee attack/Shoot/First Aid/Persuade… |
| **fast action** | Dodge/Parry/Draw/Aim/Run… | Run/Draw/Block/Dodge/Aim/Reload… |
| **reactive defense** | Dodge (MOVE) / Parry (MELEE+gear) | Dodge (MOVE) / Block (FIGHTIN') + Protect Another |
| **defense economy** | success-cancellation (+ slash/stab/shield matrix) | success-menu (cancel damage *or* counterattack) |
| **range bands** (named, non-measured) | Arm's Length/Near/Short/Long/Distant (5) | + Medium (6) |
| **terrain layer: zone features** | Cramped/Rough/Open/Dark-Foggy + Blocked/Obscured borders | (not used) |
| **terrain layer: cover ratings** | Cover Rating (soak only) | Cover Rating (Partial/Good/Heavy) + to-hit penalty grades |
| **reach subsystem** | Short/Normal/Long-Reach + CUT IN/BRACE/INTERCEPT/LOCK SHIELDS/FEINT | (light — Brace for ranged only) |
| **melee verb model** | verb-rich (Slash/Stab/Punch, each defense profile) | verb-single + modifiers (All-Out/Called/Stunt menu) |
| **ranged weapon model** | feature tags (PIERCE ARMOR/HIGH-VELOCITY/MISFIRE) + READY/LOAD | action-type economy (single/double/lever/breech) + reload count |
| **signature ranged trick** | Aim, High-Velocity | Fanning, Overwatch, Quick Shot, Called Shots |
| **social conflict currency** | binary (comply *or* escalate to violence) | damage-attrition (surplus ⚔ = Vexes/Doubts, can Break) |
| **social attribute mapping** | Manipulation vs Insight | Presence/Performin' vs Insight (+ Booklearnin' by mail) |
| **ceremonial conflict mode** | Ambush / Sneak-Attack (free pre-initiative action, no reactions) | **Duel** (Face Off → Go for Your Guns → Shoot-off; phased bonus chain) |
| **morale & rout** (optional) | Morale rating in dice (per-side, add/subtract factors) | flat 3-tier (2/4/6 dice by troop quality) |
| **mount depth** | condition (−1 vs mounted; polearm synergy) | participant (statted horse, Animal Handlin', Spooked, lasso, fall-risk) |
| **reputation / standing** (local) | Reputation / Standing (modifier in social + stronghold events) | (folded into genre core; Standing in settlement) |

### 3.6 Harm / consequences

| Generic | FL | West |
| --- | --- | --- |
| **attribute-as-HP mapping** | single-attribute-per-source (source names target) | paired split (Hurts/Shakes physical; Doubts/Vexes mental, alternating) |
| **critical-injury engine** | typed D66 families (8: Slash/Blunt Force/Stab/Burn/Acid-Corrosion/Cold-Freeze/Swallow/Horror) | single D66 master table (Tens=location × Units=severity) |
| **crit trigger: surplus-success** | Stunts (surplus ⚔ buy crit) | Crit Rating (stunts needed) |
| **crit trigger: Broken-takes-damage** | Broken + more damage to that attribute → crit | same |
| **lethality climax** (65/66) | `65` = maim (Permanent table); `66` = final death | `65` = survivable grim; `66` = instant death |
| **permanent injury** | dedicated Permanent table per family (on `65`) | inline Long-term Effect column (preventable by heal) |
| **death model** | hard time limit (die when up unless healed) | periodic un-pushable Death roll (full Grit) each interval |
| **stabilization** | healing roll (one each, self at −2) | Doctorin' roll + severity mod (separate stabilize/revive/prevent) |
| **conditions** (deprivation) | Hungry/Thirsty/Sleepy/Cold/Addicted (single-attr block) | Starving/Dehydrated/Exhausted/Freezing/Heatstroke (paired; Heatstroke→Trouble) |
| **environmental hazard rating** | (routes through crit tables; Burn/Cold families) | Intensity (fire) / Blast Power (explosions) / Potency (poison) / Virulence (disease) |
| **coup de grâce** (merciful-killing test) | (character trait — Cold-blooded talent / Honorable injury) | per-act Docity test (must *fail* = zero successes); 1 Doubts cost |
| **retirement / graceful exit** | "When the Road Ends" (retainer NPC, keep XP) | (implicit — Dynasty/Legacy XP) |
| **self-Broken safety** | pushing yourself Broken never crits | (no carve-out) |

### 3.7 Power layer

| Generic | FL | West |
| --- | --- | --- |
| **power layer** (on/off) | **ON** — full apparatus (17 disciplines) | **OFF** — zero instance |
| **power taxonomy: standard (slow)** | Spell (slow action, default) | (none) |
| **power taxonomy: reactive (fast)** | Power Word (fast, out-of-turn, parry/dodge slot) | (none) |
| **power taxonomy: dramatic (long)** | Ritual (one Turn / Quarter Day / longer) | (none) |
| **power source axis** (arcane/divine split) | (folded — disciplines flavor-differentiated) | (none) |
| **casting-risk model: safe** | Safe casting (below rank, fewer dice, no roll) | (none) |
| **casting-risk model: chance** | Chance casting (one rank above, auto mishap) | (none) |
| **casting-risk model: overcharge** | Overcharge (roll WP dice; ⚔=+PL, 💀=mishap; no push) | (none) |
| **power fuel** | core WP (capped 10, harm-refueled) | (none — Faith is metacurrency only) |
| **self-harm override (Burn)** | Burn (chosen quantity, random attribute, temporary WP) | (none) |
| **material gating (ingredient)** | Ingredient (+1 PL, consumed; required for some) | (none) |
| **knowledge gating (grimoire)** | Grimoire (−1 rank); teacher; secrecy tables | (none) |
| **power failure pressure** | typed D66 mishap families (17, count-modified) | (none — uses core Trouble) |
| **power rank ladder** | 1–6 (taller than 1–3 talent cap) | (none) |
| **high-tier / epic magic** | epic ingredients (permanent attributes, sacrifice, place); corruption spiral | (none) |
| **player-authored powers** | Forging New Spells appendix (benchmarks + 10-check veto) | (none) |

### 3.8 Travel / downtime

| Generic | FL | West |
| --- | --- | --- |
| **spatial model: tile-crawl** | hex-crawl (10 km hex, per-tile navigation + mishaps) | (not used) |
| **spatial model: point-hop** | (not used) | pointcrawl (miles/Shift between points) |
| **travel unit** | hex (10 km) | pointcrawl leg (miles/Shift) |
| **activity menu** (travel jobs) | 14-row formal menu (HIKE/LEAD THE WAY/KEEP WATCH/FORAGE/HUNT/FISH/SURVEY/MAKE CAMP/REST/SLEEP/TRAIN/CRAFT/REPAIR/EXPLORE) | ~6–8 implicit jobs + mounted/animal labor |
| **navigation cost** | Survival roll per hex entered; fail = mishap table | single rush roll/block (+50% or Trouble halt) |
| **over-exertion valve** | forced march (Endurance, Agility damage + SLEEPY) | rush (MOVE/Animal Handlin', Trouble halts progress) |
| **weather generation** | morning D6 table (Wind/Rain/Temp) + HEAT/TEMP expanded | regional-killer reference + Trouble/condition triggers |
| **food tracking** | Resource Dice (daily roll-down, spoilage-by-HEAT) | scene-level scarcity + profession/trap subsystem (Resource Dice optional) |
| **food-as-healing currency** | yes (short break restores attributes via food/water/etc.) | no (recovery via camp clearing conditions) |
| **camp procedure** | MAKE CAMP (Survival; success ladder + Failed-Camp-Liability table) | Making Camp (Nature roll; pursuit-evasion use; fail = Exhausted/Freezing) |
| **fire-vs-concealment trade-off** | enemy Scouting must beat camp ⚔ | fire = +3 to pursuers' Hawkeye |
| **downtime architecture** (settlement) | formal settlement menu (Ask/Work/Petition/Trade/Carouse/Heal/Train) + notice board | profession/economics + procedural reference |
| **daily checklist** (optional pacing) | yes (resource dice, weather, calendar) | (no formal checklist) |

### 3.9 Org / downtime layer

| Generic | FL | West |
| --- | --- | --- |
| **org lifecycle** (founding→functions→upkeep→events→scale) | (the invariant pattern) | (the invariant pattern) |
| **base / home org** (rung-1, place-bound) | **Stronghold** | Property + Business |
| **settlement-as-character** (org = stat block) | Village (GM-side generator: vicissitudes, Need/Heat) | **Your Town** (6 Aspects, Prosperity, Amenities, player-owned) |
| **band org** (roster-and-cohesion) | **Mercenary Band** (Skirmishers/Warband/Company/Host) | **Outlaw Band** (Crew/Gang/Outfit) |
| **roster morale stat** | Morale 1–5 (Broken→Keen) + Grievance Difficulty + Feud Track | Cohesion 1–5 + Loyalty 1–3 + Wanted |
| **abstraction-collapse threshold** | Host Play (Ledger −6 to +6) | (none — capped at Outfit 16–30) |
| **high-scale org** (faction turn) | **Faction** (4 Pillars: Mandate/Force/Reach/Hearth; 16 Practices; 9 Legacies) | (absent) |
| **faction turn** (procedural world-moves) | Faction Turn (Mode of Rule sets scale; pillars+practice+asset roll; acts) | (absent) |
| **mass combat** | troop dice (Base/Advantage/Protection) + battle sequence + logistics | (absent) |
| **siege engine** | Battering Ram/Siege Tower/Catapult/Trebuchet/Tunnel | (absent) |
| **scale-escalation ladder** (solo→polity) | full ladder through Polity | capped at Company/Town |
| **org-founding currency** | materials + labor + crafting roll | **Capital** (illiquid, $250 = 1) |
| **base → metacurrency link** | Stronghold grants +1 WP/PC/session | (Business grants coin/profit, not metacurrency) |
| **generational play** | (via Faction + Dynasty-of-house legacies) | Dynasty (Legacy XP, play a family member) |
| **campaign framework** (territory-scale) | Raven's Purge (Elven gemstones) | King of Santa Fe (New Mexico campaign) |

### 3.10 Gear / economy

| Generic | FL | West |
| --- | --- | --- |
| **economy model** | barter + commodity silver (gold ceremonial) | cash (dollars) + Capital + loans + salaries |
| **economy unit** (daily) | silver + barter | dollar |
| **large-denomination store** | gold (ceremonial, prestige, +lead time) | Capital ($250 = 1, liquidates D6×$50) |
| **credit / debt** | (none) | Loans (5–10% interest/season, collateral, foreclosure) |
| **income stream** | ad hoc (loot, favors, stronghold) | Salaries table + business rolls + hired-hands day-wages |
| **availability ladder** | Common/Uncommon/Rare/Extremely Rare (D6/D66 roll) | Common/Uncommon/Rare/Very Rare (settlement-tag judgment) |
| **scarcity → price curve** | upward only (+50–200%) | two-sided (−25% surplus … +100%+ panic) |
| **strong-market concept** | implicit (specialist access) | explicit Strong Market threshold + rate limits |
| **weapon feature grammar** | tags double as action-prerequisites (Edged/Pointed/Parrying/Hook/Polearm…) | three layers: Features (stats) / Qualities (pos, max 4) / Conditions (neg, Trouble-driven) |
| **weapon stat model** | Gear Dice (BONUS) that degrade on push | flat Attack/Draw mods, no push-degradation |
| **quality ladder** | Crude / Standard / Fine (Masterwork) | Poor / Worn / Standard / Fine |
| **gear-degradation trigger** | Gear Die 💀 (continuous counter, broken at 0) | Condition (Worn/broken — discrete tag from D6 table, Trouble-driven) |
| **material-quality ladder** | Iron→Wrought→Steel→Crucible→Dwarven (+1 to +3, talent-gated) | (not present — quality is buyable grade) |
| **legendary tier (artifact)** | Artifact Die (D8/D10/D12) + named + oddity table | (none) |
| **consumables tracking** | Resource Dice (default; Arrows/Torches/Food/Tools) | Resource Dice (Optional Module; loose counting default) |
| **resource die ladder** | D12→D10→D8→D6 (deplete on 1–2) | D12→D10→D8→D6→D4 (deplete on 1–2) |
| **crafting gates** | Talent + Workshop/Tools + Raw Materials + Time (4 gates) | folded into Availability/Quality + business prerequisites |

### 3.11 GM procedures / meta

| Generic | FL | West |
| --- | --- | --- |
| **GM principles** (axioms) | 7 Principles (de-flavored: open-table, lore-as-rumor, say-yes, nothing-for-free, tall-flower, death-as-story, emergent-finale) | diffuse campaign-driver list (Ambitions/Vengeance/Justice) |
| **encounter engine** | D66 matrix × 9 terrain columns + reoccurring rule | campaign seeds + adventure-embedded encounters |
| **NPC statblock** | inline prose (4 attr + skills + talents + gear), procedural | 8-column table roster, hand-authored archetypes |
| **campaign-state tracker** | stronghold events (Reputation-weighted D66) + household Need/Heat | Faction Standing (4-track ledger) + week-ticked Faction Clocks |
| **seasonal fortune roll** | (stronghold events + vicissitudes) | Turn of the Season (Business + Personal Fortune + Town Fortune) |
| **adventure-site doctrine** | site-as-dungeon (locations+NPCs+events, no narrative, 15-min turn, legend) | sandbox country (multiple roads, faction clocks, shortcut-positive) |
| **solo-play layer** | full suite (companions, quarter-day procedure, card oracles) | (not present in core) |
| **Dark Secret / player-authored threat** | Dark Secret (pre-game mark) | Big Dream (player-authored long-term goal → XP) |
| **relationships (intra-party)** | one-sentence relationship per PC | relationships + **Pardner** (primary bond) |
| **NPC ally subsystem** | (hirelings/residents at stronghold) | **Compadres** (player-controlled friendly NPCs with statblocks) |
| **legend / lore handout** | Legend (rumor/handout, LORE-gated) | (folded into campaign seeds/procedural reference) |

## 4. The master system taxonomy (clustered, with ref links)

One-line definition of every engine system/subsystem, grouped by cluster. Each entry names the **generic term**, defines it in one line, and links to the reference file + section that owns it. Cluster headers name the subsystem family.

### 4.1 Core cluster — resolution, dice, push, metacurrency

| Term | Definition | Ref |
| --- | --- | --- |
| **Dice grammar** | A D6 pool where 6 = success (⚔); colored pools (base/skill/gear in FL) or unified (West); a latent cost face (💀 / 1) realized on push or exposure. | `00` §3 |
| **Success ladder** | Two complementary readings of the ⚔ count: a graded ladder (0/1/2/3+) and a threshold-raise mechanic (Normal/Challenging/Difficult). | `00` §4 |
| **Modification ladder** | A flat ±3-per-source, stack-without-cap model with a 7-step difficulty ladder (Trivial +3 … Formidable −3). | `00` §5 |
| **Push** | A single optional reroll of non-success dice that converts a latent cost face into an active cost; one push per roll, ever. | `00` §6 |
| **Push-cost model** | The dial deciding what pushing costs: bane-self-harm (FL, body/gear) / currency-spend (West, metacurrency) / hybrid. | `00` §6, §11 |
| **Metacurrency** | A capped pool (10) that converts risk/failure into future agency; refueled by harm (FL) or action/success (West). | `00` §7 |
| **Opposed roll** | A symmetric contest where each adversary ⚔ cancels one of yours; only the attacker may push. | `00` §8 |
| **Group roll** | A labor-distribution roll using a highest/lowest selector that encodes the task type (sneak=weakest-link; track=strongest; climb=individual-with-cover). | `00` §8 |
| **One-chance rule** | The same approach cannot be retried for the same goal; makes the push decision load-bearing. | `00` §8 |
| **Escalating-success die** | An optional D8/D10/D12 (6+ = ⚔, scaled multi-successes) for high-tier outcomes, immune to degradation. | `00` §9 |
| **Failure-pressure layer** | The dial for how failure taxes: banes-on-dice (FL) / Trouble tables (West) / hybrid / none. | `00` §10 |

### 4.2 Character cluster — model, generation, protected dial

| Term | Definition | Ref |
| --- | --- | --- |
| **Attribute** | One of four genre-named stats, each a damage track (attribute-as-HP) and the parent of 4 skills. | `01` §3 |
| **Named damage type** | A genre noun typed to each attribute (Hurts/Shakes/Vexes/Doubts) making attrition feel in-genre. | `01` §4 |
| **Skill / Ability** | One of 16 competences, permanently tied to one attribute (4×4 grid). | `01` §3 |
| **Talent** | The advancement unit beyond skills; a ranked ability with a cost curve and access gating. | `01` §5; `02` §5 |
| **Protected dial** | The player's personal pressure-relief resource: a die (Pride, narrow) or currency (Faith, broad) tied to identity. | `01` §5; `00` §7 |
| **Broken** | The helpless state when an attribute reaches 0; no separate HP exists. | `01` §4; `04` §3 |
| **Identity selector** | The fast-generation first choice: kin (fantasy species) or archetype (social profession). | `01` §8 |
| **Lifepath** | The deep-generation method producing emergent backstory; equivalent power to fast gen. | `01` §8 |
| **Age dial** | A sub-dial trading raw attributes (young) for skills/talents (old). | `01` §8 |
| **Social tether** | The PC's anchor: intra-party bonds + primary bond + NPC home + (optional) ally layer + authored drive. | `01` §6 |
| **Big Dream** | A player-authored long-term goal that drives XP awards (the character's through-line). | `01` §6 |
| **Encumbrance** | The carry limit (primary physical attribute × 2) with heavy/light/tiny tiers and an over-encumbrance tax. | `01` §7 |
| **Resource Die (consumables)** | A degrading die (D12→D6) replacing unit-counts for ammo/food/torches; depletes on 1–2. | `01` §7; `08` §10 |

### 4.3 Conflict cluster — action economy, positioning, modes

| Term | Definition | Ref |
| --- | --- | --- |
| **Three-scale time ladder** | Round (combat, seconds) / Turn (exploration, minutes) / Shift (recovery, hours). | `03` §3 |
| **Action budget** | The load-bearing 2-actions-per-Round rule: (1 slow + 1 fast) ∨ (2 fast); the scarcity that makes combat a trade-off. | `03` §7 |
| **Slow / fast action** | The two action pools: slow = the decisive roll; fast = the shaping moves (move/draw/defend). | `03` §7 |
| **Initiative archetype** | The dial for combat order: rolled-sticky / random-redrawn / side-based / fixed. | `03` §4 |
| **Range bands** | Named, non-measured distance tiers (Arm's Length → Distant) gating legal actions and modifiers. | `03` §5 |
| **Terrain layer** | The spatial-pressure dial: zone-features-and-borders (FL) / cover-ratings-and-to-hit-grades (West). | `03` §5 |
| **Cover model** | Ranged-defense layer: soak-only (FL) / soak + to-hit penalty (West) / none. | `03` §5 |
| **Reach subsystem** | An optional melee-depth system making weapon length a distance-control contest (CUT IN/BRACE/INTERCEPT). | `03` §6 |
| **Reactive defense** | Out-of-turn actions (dodge/parry/block) declared before the attack, costing from the shared budget. | `03` §8 |
| **Melee verb model** | The dial for melee texture: verb-rich with defense matrix (FL) / verb-single + stunt menu (West). | `03` §9 |
| **Ranged weapon model** | The dial for where weapon behavior lives: feature tags (FL) / action-type economy (West). | `03` §10 |
| **Reload/prepare economy** | The scarcity that makes ammunition and weapon choice matter (READY/LOAD, cock/chamber/reload). | `03` §10 |
| **Social conflict** | A parallel mode to physical combat using opposed rolls + a leverage modifier table; currency is binary-escalate (FL) or damage-attrition (West). | `03` §11 |
| **Ceremonial conflict mode** | A scripted mini-scene for the genre's signature beat: Duel (phased bonus chain) / Ambush (opening advantage). | `03` §12 |
| **Morale & rout** | An optional disengagement layer letting NPC groups break and run when the fight turns. | `03` §13 |
| **Mount depth** | The dial for mount modeling: condition (FL) / participant (West). | `03` §14 |

### 4.4 Harm cluster — damage, injury, conditions, recovery

| Term | Definition | Ref |
| --- | --- | --- |
| **Attribute-as-HP mapping** | The dial for how harm is recorded: single-attribute-per-source (FL) / paired split (West). | `04` §3 |
| **Critical-injury engine** | A D66 lookup converting "a really bad hit" into a named, narratively-loaded consequence; the engine's memory of harm. | `04` §5 |
| **Typed crit family** | FL's innovation: one D66 family per damage *type* the genre cares about (Slash/Stab/Burn…); the set of families is a genre-commitment device. | `04` §5.2 |
| **Lethality climax (65/66)** | The reusable top-of-table split: `65` = maiming threshold (survivable via rescue → Permanent table); `66` = final death. | `04` §5.1 |
| **Death model** | The dial for dying rhythm: hard time limit (FL) / periodic un-pushable Death roll (West). | `04` §8 |
| **Stabilization** | The healer's life-saving roll within the countdown window; gates the rescue opportunity. | `04` §8 |
| **Conditions** | The deprivation layer (starve/thirst/exhaust/freeze/heat/addicted) — the engine's slow clock making time a threat. | `04` §6 |
| **Environmental hazard rating** | A single numeric rating (Intensity/Potency/Virulence/Blast Power) driving an opposed/threshold roll; scalable and combinable. | `04` §7 |
| **Healing cadence** | The bounce-back tempo: fast 1/Turn (West) / slow per Quarter-Day in travel (FL); two-tracked (attributes fast, injuries slow). | `04` §9 |
| **Permanent injury / retirement** | The graceful-exit layer: permanent-injury resolution + a retirement path converting a broken PC into an NPC asset. | `04` §10 |

### 4.5 Power cluster — magic, miracles, powers

| Term | Definition | Ref |
| --- | --- | --- |
| **Power layer** | The engine's largest optional subsystem; a plug-in that West proves is purely additive (remove it, nothing breaks). | `05` §10 |
| **Power taxonomy** | A three-tier effect-speed frame: Standard (slow) / Reactive (fast, out-of-turn) / Dramatic (long, ceremonial). | `05` §3 |
| **Casting-risk model** | The dial for casting variance: safe (guaranteed-costly) / chance (rolled, failure-locked) / overcharge (pushed-for-scale). | `05` §4 |
| **Power fuel** | The core metacurrency spent to cast; binds the power layer downstream of the risk loop (never a parallel currency). | `05` §5 |
| **Self-harm override (Burn)** | An optional desperation valve letting a caster cast without currency by paying attribute damage instead. | `05` §5 |
| **Material gating** | Powers need *stuff* — ingredients (+PL, consumed, required for some). | `05` §6 |
| **Knowledge gating** | Powers need *books/teachers* — grimoires (−rank), secrecy tables, required teachers for rituals. | `05` §6 |
| **Mishap table** | The failure-pressure layer for powers; structurally identical to the typed-crit-family pattern, one D66 family per discipline. | `05` §7 |
| **Power rank ladder** | A tall ladder (1–6) taller than the talent cap, scaling power across a long campaign. | `05` §8 |
| **Epic / high-tier magic** | The ceiling gated not by fuel but by irreplaceable fiction costs (permanent attributes, sacrifice, place); corruption spiral. | `05` §9 |
| **Density dial** | The four-point on/off+depth dial: none (West) / low / medium / high (FL). | `05` §10 |

### 4.6 Travel cluster — journey, survival, downtime

| Term | Definition | Ref |
| --- | --- | --- |
| **Spatial model** | The central travel dial: tile-crawl/hex (FL, exploration) / point-hop/pointcrawl (West, traversal). | `06` §3 |
| **Travel time block** | The discrete block (Quarter Day / Shift) that is the resolution unit for all travel procedures. | `06` §4 |
| **Activity menu** | The load-bearing structure: a fixed list of travel jobs, one per PC per block, balanced so movement/navigation/watch/supply are mutually exclusive. | `06` §5 |
| **Navigation cost** | The dial for the travel tax: per-tile roll+mishap (FL) / per-edge rush+Trouble (West). | `06` §6 |
| **Over-exertion valve** | The roll taken to exceed safe daily travel; makes "push on or camp" a real decision. | `06` §6 |
| **Weather layer** | The environment-as-attrition dial: mechanical morning table (FL) / reference + Trouble (West). | `06` §7 |
| **Food layer** | The supply subsystem: daily consumption replenished by Survival/Nature rolls, modified by terrain/season, with spoilage. | `06` §8 |
| **Camp procedure** | The recovery point of the day, gated by a Survival/Nature roll with a success ladder and a failure cost. | `06` §9 |
| **Recovery loop** | REST/SLEEP as the healing gate; the currency of recovery (supply-dice FL / condition-clear West). | `06` §10 |
| **Downtime menu** | A second activity-menu architecture for "not on the road" (info/work/trade/craft/carouse/train/petition). | `06` §10 |

### 4.7 Org cluster — base, faction, mass-combat

| Term | Definition | Ref |
| --- | --- | --- |
| **Org lifecycle** | The invariant five-beat pattern every org runs: founding → functions → upkeep → events → scale. | `07` §3 |
| **Base / home org** | Rung-1: a place-bound, player-owned capability hub that banks downtime labor and generates metacurrency. | `07` §4 |
| **Settlement-as-character** | A settlement modeled as a stat block with attributes, a state machine, internal-faction gauges, and a growth mechanism. | `07` §5; `09` §5 |
| **Band org** | Rung-2/3: a roster-and-cohesion org with tracked headcount, a single morale stat, and a pay/feed cycle. | `07` §5, §6 |
| **Abstraction-collapse threshold** | The mechanism (Host Play/Ledger) that collapses a roster past ~50 bodies into a single trackable number. | `07` §6 |
| **High-scale org / faction** | Rung-5: a polity-scale org with a four-stat block, practices, legacies, and a procedural turn layer. | `07` §7 |
| **Faction turn** | A procedural turn layer running on its own clock that resolves org-vs-org pressure through a stat+skill+asset roll. | `07` §7 |
| **Mass combat** | Rung-top: the resolution engine for org-scale violence, reusing the core dice grammar at unit scale. | `07` §8 |
| **Logistics layer** | The supply/disease/march rules that decide most campaigns by arithmetic, not tactics. | `07` §8 |
| **Scale-escalation ladder** | The rung ladder (solo→party→band→company→faction→army→polity) whose ceiling is the campaign-design dial. | `07` §9 |
| **Org-founding currency** | The dial for what founds orgs: materials+labor (FL) / Capital illiquid investment (West). | `07` §11 |
| **Base → metacurrency link** | The economic keystone binding the downtime layer to adventure (base grants WP/Faith). | `07` §4, §12 |

### 4.8 Gear cluster — equipment, economy, crafting

| Term | Definition | Ref |
| --- | --- | --- |
| **Availability ladder** | A 4-step rating (Common→Very Rare) controlling whether an item can be found in a given settlement. | `08` §3 |
| **Scarcity → price curve** | A price-adjustment table keyed to how hard an item was to find (surplus → panic). | `08` §3 |
| **Economy model** | The central divergence dial: barter+commodity (FL) / cash+capital+credit+wages (West). | `08` §4 |
| **Asset layer** | An optional subsystem where a large-denomination currency converts in fixed/out random, and assets pay on seasonal rolls. | `08` §4.2 |
| **Crafting / making gate** | The four-gate structure gating making: talent + workshop + materials + time. | `08` §5 |
| **Material-quality ladder** | A ladder where each material tier trades crafting difficulty and scarcity for a +1 bonus (talent-gated). | `08` §5.2 |
| **Feature grammar** | The central reusable artifact: weapons/armor defined by composable tags (not bespoke stat lines); tags double as action-prerequisites. | `08` §6, §7 |
| **Quality ladder** | A 3- or 4-tier ladder (Crude/Poor/Worn/Standard/Fine) where low breaks first and high adds a bonus + is rarer. | `08` §8 |
| **Degradation mechanism** | The dial for how gear worsens: continuous counter (FL, Gear Die 💀) / discrete Conditions (West, Trouble-driven). | `08` §8 |
| **Legendary tier (artifact)** | An optional top tier using the escalating-success-die, named/typed, carrying an oddity table. | `08` §9 |
| **Consumables-as-resource-dice** | A single degrading die replacing unit-counts; the consumables analogue of the push. | `08` §10 |

### 4.9 GM cluster — procedures, encounters, settlements, solo

| Term | Definition | Ref |
| --- | --- | --- |
| **GM principles** | 5–7 de-flavored axioms (scarcity, cost-of-safety, death-as-story, emergent-finale) governing judgement where dice are silent. | `09` §3 |
| **Encounter engine** | A random-but-weighted D66 selector remapped by context column, plus a reoccurring rule giving the table memory. | `09` §4 |
| **Living settlement** | A settlement modeled as a character sheet for a place: attributes, state machine, internal-faction gauges, growth mechanism. | `09` §5 |
| **Minimal statblock** | The NPC format: 4 attributes + relevant skills + 0–3 talents + gear + special tags. | `09` §6 |
| **Solo-play layer** | An optional GMless replacement: draw-and-interpret oracles with a bias dial + a turn procedure + a companion rule. | `09` §7 |
| **Campaign-state tracker** | Named scores that move on player choices and throw consequences forward at thresholds (faction standing, aspects, clocks). | `09` §8 |
| **Seasonal fortune roll** | A resolution roll at the season turn that resolves off-screen time and generates hooks. | `09` §8 |
| **Adventure-site doctrine** | The structure of a playable place: site-as-dungeon (locations+NPCs+events, no narrative) / region-sandbox (multiple roads, clocks). | `09` §9 |

### 4.10 Meta cluster — philosophy, balance, layering

| Term | Definition | Ref |
| --- | --- | --- |
| **Pressure economy** | The engine's analytical spine: layered pressure sources (time/body/gear/metacurrency/safety/overreach), never single-axis balance. | `10` §4 |
| **Resource-at-risk model** | The four-beat interaction shape: pressure → decision → consequence → state change; missing a beat = decorative. | `10` §4 |
| **Five primary loops** | Expedition / Conflict / Recovery / Metacurrency / Base — the genre-neutral gameplay loops; 2 weighted as primary. | `10` §5 |
| **Cost-of-safety axiom** | "Nothing Is for Free" — safety is the most expensive thing; every gain must cost something. | `10` §6 |
| **Lethality-as-feature** | Broken-easy / death-hard, but death real; attrition is the operating mechanism, death the boundary. | `10` §7 |
| **Authenticity lens** | The realism sniff-test: realism earns its place only when it sharpens a decision without sacrificing playability. | `10` §8 |
| **Layering principle** | The three-tier complexity strategy: General (always-on core) / Situational (context-gated) / Optional (mode-switched). | `10` §9 |
| **Warning-sign catalog** | The seven anti-patterns: subsystem inflation, silent invalidation, false realism, vague enforcement, misleading survivability, setting-laden generic language, sibling-skill duplication. | `10` §10 |
| **Expected-success math** | The binomial probability core (n D6, count sixes); the engine's published backbone. | `13` §3 |
| **Breakpoint** | The pool size n* at which expected success drops below a chosen threshold T; the competence floor / exploitation ceiling. | `13` §4 |
| **Exploit-surface taxonomy** | The eight categories of unhealthy synergy (infinite-loop, cap-bypass, silent-stacking, free-resource, action-economy, push-cost-avoidance, mishap-avoidance, invalidation) + seven root patterns. | `13` §5 |
| **Synergy stress-test protocol** | The step-by-step interaction-analysis method: map touch surface → enumerate → "more than sum?" → gated? → Five Tests → verdict. | `13` §6 |
| **Table-behavior lenses** | The nine playability checks (math/perceived/table-complexity/ambiguity/recoverability/agency/catastrophe/campaign/verdict). | `13` §7 |
| **Validation pipeline** | The end-to-end checklist: intent → math → exploit → synergy → table → layer → verdict. | `13` §8 |

## 5. Cross-reference index (term → file §)

For each generic term, the file + section where it is defined in depth. This is the skill's internal routing table — when a term appears in any sibling file, this index says where to read its full treatment.

### Core terms (`00-engine-core.md`)

| Term | File § |
| --- | --- |
| Dice grammar, base/skill/gear die, ⚔/💀/🩸 | `00` §3 |
| Success ladder (threshold + grade), surplus-success spend | `00` §4 |
| Modification ladder, difficulty, help gating | `00` §5 |
| Push, push-cost model (bane-self-harm / currency-spend / hybrid) | `00` §6, §11 |
| Metacurrency (WP/Faith), refuel trigger, depletion state | `00` §7 |
| Opposed roll, group roll, one-chance rule | `00` §8 |
| Escalating-success die (artifact die), heroic-moment die (Pride) | `00` §9 |
| Failure-pressure layer (banes / Trouble) | `00` §10 |
| All core dials (push-cost, cost-face, refuel, cap, depletion, mod-target, help, ladder, legendary, failure-pressure) | `00` §11 |

### Character terms (`01-character-model.md`, `02-progression-and-xp.md`)

| Term | File § |
| --- | --- |
| Attribute (4×4 grid), attribute-as-HP | `01` §3 |
| Named damage type | `01` §4 |
| Protected dial (Pride/Faith), protected-dial identity | `01` §5; `00` §7 |
| Social tether, Big Dream, Pardner, Compadres | `01` §6 |
| Encumbrance, resource die (consumables) | `01` §7 |
| Identity selector (kin/archetype), lifepath, age dial, group concept | `01` §8 |
| Skill/ability, talent (ranks) | `01` §3; `02` §5 |
| Broken | `01` §4; `04` §3 |
| XP award models, training costs, talent rank ladder, milestones, downtime training, Legacy XP, metacurrency→XP | `02` §3–9 |

### Conflict terms (`03-conflict-and-combat.md`)

| Term | File § |
| --- | --- |
| Three-scale time ladder (Round/Turn/Shift) | `03` §3 |
| Initiative archetype, surprise | `03` §4 |
| Range bands, terrain layer, cover model | `03` §5 |
| Reach subsystem (CUT IN/BRACE/INTERCEPT/LOCK SHIELDS/FEINT) | `03` §6 |
| Action budget (2/Round), slow/fast action | `03` §7 |
| Reactive defense (dodge/parry/block), defense economy | `03` §8 |
| Melee verb model (Slash/Stab/Punch vs single+stunts) | `03` §9 |
| Ranged weapon model, reload economy, signature tricks | `03` §10 |
| Social conflict (currency, attribute mapping, leverage table) | `03` §11 |
| Ceremonial conflict (Duel / Ambush) | `03` §12 |
| Morale & rout | `03` §13 |
| Mount depth | `03` §14 |

### Harm terms (`04-harm-and-consequences.md`)

| Term | File § |
| --- | --- |
| Attribute damage, Broken, Broken fiction | `04` §3 |
| Coup de grâce / merciful-killing test | `04` §4 |
| Critical-injury engine (D66 architecture), typed crit family, lethality climax (65/66) | `04` §5 |
| Conditions (starve/thirst/exhaust/freeze/heat/addicted) | `04` §6 |
| Environmental hazard (fire/blast/fall/drown/poison/disease/darkness), ratings (Intensity/Potency/Virulence/Blast Power) | `04` §7 |
| Stabilization, death model, death roll | `04` §8 |
| Healing cadence, healer acceleration, long-term-effect prevention | `04` §9 |
| Permanent injury, retirement ("When the Road Ends") | `04` §10 |

### Power terms (`05-power-layer.md`)

| Term | File § |
| --- | --- |
| Power taxonomy (Spell/Power Word/Ritual) | `05` §3 |
| Casting-risk model (safe/chance/overcharge) | `05` §4 |
| Power fuel (WP), self-harm override (Burn) | `05` §5 |
| Material gating (ingredient), knowledge gating (grimoire/teacher/secrecy) | `05` §6 |
| Mishap table (per-discipline D66 family) | `05` §7 |
| Power rank ladder, learning economy, forging appendix | `05` §8 |
| Epic/high-tier magic, epic ingredients, corruption | `05` §9 |
| Density dial (none/low/medium/high), on/off switch | `05` §10 |

### Travel terms (`06-travel-and-downtime.md`)

| Term | File § |
| --- | --- |
| Spatial model (hex-crawl / pointcrawl) | `06` §3 |
| Travel time block (Quarter Day / Shift) | `06` §4 |
| Activity menu (travel jobs) | `06` §5 |
| Navigation cost, over-exertion valve (forced march / rush) | `06` §6 |
| Weather layer, HEAT/TEMP | `06` §7 |
| Food layer, forage/hunt/fish, spoilage, food-as-healing | `06` §8 |
| Camp procedure, failed-camp liability, fire-vs-concealment | `06` §9 |
| Recovery loop, downtime menu | `06` §10 |

### Org terms (`07-base-faction-mass-scale.md`)

| Term | File § |
| --- | --- |
| Org lifecycle (5-beat pattern) | `07` §3 |
| Base/home org (Stronghold, Property+Business) | `07` §4, §5 |
| Settlement-as-character (Village, Your Town) | `07` §5 |
| Band org (Mercenary Band, Outlaw Band), roster morale | `07` §5, §6 |
| Abstraction-collapse threshold (Host Play) | `07` §6 |
| High-scale org/faction (Pillars/Practices/Legacies) | `07` §7 |
| Faction turn (Mode of Rule, acts, fallout) | `07` §7 |
| Mass combat (troop dice, battle sequence) | `07` §8 |
| Logistics layer (supply/disease/march) | `07` §8 |
| Scale-escalation ladder (solo→polity), ceiling dial | `07` §9 |
| Org-founding currency (materials / Capital) | `07` §11 |
| Base → metacurrency link | `07` §4, §12 |

### Gear terms (`08-gear-and-economy.md`)

| Term | File § |
| --- | --- |
| Availability ladder, settlement modifiers, strong market | `08` §3 |
| Scarcity → price curve | `08` §3 |
| Economy model (barter/cash/capital), asset layer, credit, income | `08` §4 |
| Crafting/making gate (4 gates) | `08` §5 |
| Material-quality ladder | `08` §5.2 |
| Feature grammar (weapon tags), armor feature grammar | `08` §6, §7 |
| Quality ladder (Crude/Poor/Worn/Standard/Fine) | `08` §8 |
| Degradation mechanism (Gear Die 💀 / Conditions) | `08` §8 |
| Legendary tier (artifact die, oddity) | `08` §9 |
| Consumables-as-resource-dice | `08` §10 |

### GM terms (`09-gm-procedures.md`)

| Term | File § |
| --- | --- |
| GM principles (7, de-flavored) | `09` §3 |
| Encounter engine (D66 matrix, reoccurring rule) | `09` §4 |
| Living settlement (attributes, state machine, gauges, growth) | `09` §5 |
| Minimal statblock | `09` §6 |
| Solo-play layer (oracles, companion, turn procedure) | `09` §7 |
| Campaign-state tracker (faction standing, clocks, fortune rolls) | `09` §8 |
| Adventure-site doctrine (site-as-dungeon / region-sandbox) | `09` §9 |

### Meta terms (`10-design-philosophy.md`, `13-balance-and-synergy.md`)

| Term | File § |
| --- | --- |
| Core design identity (thesis: ambition ↔ exposure) | `10` §3 |
| Pressure economy, resource-at-risk model | `10` §4 |
| Five primary loops | `10` §5 |
| Cost-of-safety axiom, tall-flower principle | `10` §6 |
| Lethality-as-feature | `10` §7 |
| Authenticity lens, realism sniff-test | `10` §8 |
| Layering principle (General/Situational/Optional) | `10` §9 |
| Warning-sign catalog (7 anti-patterns) | `10` §10 |
| Expected-success math, binomial core, FL Chance-of-Success table | `13` §3 |
| Breakpoint (competence floor / exploitation ceiling) | `13` §4 |
| Exploit-surface taxonomy (8 categories + 7 patterns) | `13` §5 |
| Synergy stress-test protocol (Five Tests) | `13` §6 |
| Table-behavior lenses (9) | `13` §7 |
| Validation pipeline (intent → math → exploit → synergy → table → verdict) | `13` §8 |

## 6. Design intent

This file is the **enforcer** and the **map** of the engine-agnostic skill.

- **The translation table enforces engine-agnosticism.** As long as every generic term is defined here in the left column, the rest of the skill (00–14) can speak cleanly without leaking either game's flavor. The rule is simple: *if a noun appears in a sibling file's generic prose, it must be in this table's left column; if it appears only in an instantiation, it must be cited from the middle or right column.* This is the procedural defense against Warning Sign (f) — setting-laden generic language (`10` §10f). A reader of either source book, or neither, should recognize every generic term as the same concept.
- **The master taxonomy is the skill's map of itself.** Every system/subsystem the engine contains is named once, defined in one line, and cross-linked to its owning reference file. This lets a user navigate from "what is the metacurrency?" to `00` §7, or from "what is the org lifecycle?" to `07` §3, without reading every file. The clusters (Core/Character/Conflict/Harm/Power/Travel/Org/Gear/GM/Meta) mirror the reference-file ownership: each file owns one cluster's terms.
- **The cross-reference index is the routing table.** It resolves the unavoidable ambiguity that a term like "metacurrency" is *defined* in `00` §7 but *instantiated* (as WP/Faith) in `01` §5 and `05` §5. The index sends the reader to the definition; the translation table sends them to the instantiation.
- **The two artifacts are mutually validating.** The translation table's generic terms are the *nouns* the taxonomy names; the taxonomy's clusters are the *homes* the translation table's terms live in. If a term appears in one but not the other, the skill is incomplete — either a noun lacks a definition, or a definition lacks a name. This file's completion is the check that the skill is closed: every named concept is defined, every defined concept is named.

The glossary's deepest purpose is to make the engine **portable**. YZE's greatest strength (`01` §11) is that the *mechanics barely change; the fiction transforms completely* by re-skinning the nouns. This file is the ledger of that re-skinning: it records, once and for all, which nouns are generic (port verbatim) and which are costumed (swap per genre). A new game's job is to fill a fourth column — its own instantiation of every generic term — and the rest of the engine carries.
