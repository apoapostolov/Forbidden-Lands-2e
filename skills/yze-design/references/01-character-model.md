<!-- markdownlint-disable MD013 -->

# Character Model — Attributes, Skills, Damage, Generation

> **STATUS: FILLED (Pass-1 + Pass-2).** Read alongside `00-engine-core.md` (resolution) and `02-progression-and-xp.md` (advancement).

## Contents

1. Source provenance
2. Abstraction target
3. The 4×4 attribute-skill grid
4. Per-attribute damage types
5. Pride, Faith, and Inner Fire
6. Relationships, companions, and the social anchor
7. Encumbrance and carrying
8. Character generation: Race/archetype vs life events
9. Life Events
10. What Skills Do
11. Divergence rows (FL vs West)
12. Rule choices and instantiation recipe
13. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/02-your-adventurer.md:1-744` — 8 Races, 9 professions, age, attributes (STR/AGI/WIT/EMP, 2–6 range), 16 skills, Pride, Dark Secret, relationships, encumbrance (Strength×2 + backpacks/sacks), consumables (Resource Dice), experience, training, reputation, **Life Generator**.
- `01-corebook/13-lifepaths-of-the-forbidden-lands.md` — full advanced Life Events system.
- `02-gamemasters-guide/05-kin.md` — expanded kin write-ups.

**Tales of the Old West 2E (West):**
- `01-corebook/02-your-player-character.md:1-827` — 4 attributes (Grit/Quick/Cunning/Docity, 1–5 range) each with a **named damage type** (Hurts/Shakes/Vexes/Doubts), 16 abilities, **Big Dream**, **Faith**, talents, relationships + **Pardner**, encumbrance (Grit×2), Compadres, Session Zero, **Group Concepts** (7), **10 Archetypes**, the **"Your Tale Begins" lifepath**, XP/advancement.
- `01-corebook/04-talents.md` — talent access gating.

## Abstraction target

Abstract the **character model** as a genre-neutral skeleton: a small grid of attributes (each owning a *damage type* and a *cluster of skills*), a personal reserve such as Pride or Faith, a social/relationship anchor, an encumbrance rule, and a choice between archetype-based vs life-events generation. FL and West both use a 4×4 grid but flavor it completely differently — capture that as the canonical "attribute identity" recipe: **the *name* and *damage-type name* of each attribute should express the genre's core tension.** The two games also demonstrate two ends of the generation-depth choice (FL: Race + profession + optional deep Life Events book; West: archetype-quick + standard life-events flow, with a richer Session Zero / Group Concept social layer).

## 3. The 4×4 attribute-skill grid

**Both games use exactly 4 attributes × 4 skills (= 16 skills), no more.** Each skill is permanently tied to one attribute. The grid is the engine's load-bearing symmetry: it keeps the character sheet small, makes balance tractable (every attribute has the same number of skills), and distributes character competence across four "domains."

**FL — survival/physical-mental axis:**
- **Strength** (raw power, stamina) → Might, Endurance, Melee, Crafting
- **Agility** (body control, speed) → Stealth, Sleight of Hand, Move, Marksmanship
- **Wits** (perception, intelligence, sanity) → Scouting, Lore, Survival, Insight
- **Empathy** (charisma, manipulation) → Manipulation, Performance, Healing, Animal Handling
FL `02-your-adventurer.md:378-400, 264-283`.

**West — frontier-grit axis (same structure, re-skinned and re-named):**
- **Grit** (resilience, strength, presence) → Fightin', Labor, Presence, Resilience
- **Quick** (dexterity, hand-eye) → Light-Fingered, Move, Operate, Shootin'
- **Cunning** (instinct, common sense, nature-sense) → Animal Handlin', Hawkeye, Insight, Nature
- **Docity** (learning, book-smarts) → Booklearnin', Doctorin', Makin', Performin'
West `02-your-player-character.md:16-59`.

**Generic abstraction — the "attribute identity" recipe:**
The four attributes are not generic "STR/DEX/INT/CHA." Each one should be **named after the genre's core tension**, and its four skills should be the genre's four ways of *expressing* that tension. FL's grid is about *survival in a hostile world* (each attribute is a survival axis). West's grid is about *frontier competence* (each attribute is a way of being competent in the West). The skill *names* are the single most powerful genre-flavoring lever in the engine — renaming the 16 skills does ~60% of the work of re-skinning YZE for a new genre.

**Point-buy at creation (both):** FL distributes attribute points by age (Young 15 / Adult 14 / Old 13) with a 2–4 range (up to 5/6 in a kin/profession "key attribute"); West distributes by age (Greenhorn 6 / Tested 5 / Old-timer 4, added to a base) with a 1–5 range. FL `02-your-adventurer.md:353-377`; West `02-your-player-character.md:356-364`. Both gate the *ceiling* of a single attribute at creation. **Layer:** General.

## 4. Per-attribute damage types

**The shared mechanic:** Each attribute is also a *health track* — damage reduces it; at 0 the character is **Broken** (helpless). This is "attribute-as-HP": there is no separate HP pool. Harm is *typed* by which attribute it strikes.

**FL — type-by-position (mechanical):** Damage is dealt to an attribute by *what kind of harm* it is — weapon damage typically hits Strength or Agility; fear/horror hits Wits; social conflict hits Empathy. The type is functional, not named. FL `05-combat-and-damage.md`.

**West — type-by-name (fictional):** Each attribute has a *named damage type* — Grit takes **Hurts**, Quick takes **Shakes**, Cunning takes **Vexes**, Docity takes **Doubts**. West `02-your-player-character.md:20-34`. This is the *same mechanic* as FL but with richer fiction: "you suffer 2 Hurts" reads more in-genre than "you take 2 Grit damage," and it gives players a vocabulary for their character's state.

**Generic abstraction — "damage typing as genre flavor":** Type every attribute's damage with a genre-appropriate noun. FL's silent typing is the minimal version; West's named typing is the maximal version. **The named damage types are free genre-loading** — they cost nothing mechanically and make attrition *feel* like the genre. **Layer:** General (the typing); the *naming* is a design choice (always name them).

## 5. Pride, Faith, and Inner Fire

Both games give each PC a **personal pressure-relief resource** tied to character identity — but they wire it to the core loop very differently (this is one of the engine's most important divergences; see `00-engine-core.md` §7 for the full Willpower/Faith treatment).

**FL — Pride (a die, narrow scope):** Once per session, after failing a roll made *to protect yourself or another person*, you may add your **Pride die** (D8/D10/D12). It starts at D12. If the roll still fails, you *lose* Pride for next session; it returns at D8 thereafter. If you use it and succeed, or don't use it, it grows one step (D8→D10→D12) next session. FL `02-your-adventurer.md:456-462`, `03-skills.md:254-258`. **Scope:** narrow — only protective rolls. **Identity load:** Pride is "the stubborn will that keeps you standing."

**West — Faith (a pool, broad scope):** Faith is a personal reserve (4/scenario, cap 10) that pays for **all pushes** (1/push) *and* **buys off Trouble** (1:1). It's not a die added to a roll — it's the fuel for the entire push/trouble rule set. Faith is earned by 3-⚔ un-pushed rolls or by performing in-fiction rituals/actions. At 0, you're **Shaken** (can't push, can't gain Faith). West `03-rolling-the-bones.md:84-88, 258-311`. **Scope:** broad — the whole core loop. **Identity load:** Faith is described in one sentence ("the Lord is my shepherd," "my place is in the saddle") and is *what keeps you going.*

**Generic abstraction:** every character needs an **inner fire** rule: a named reserve, die, vow, faith, pride, nerve, spark, or hope that lets the player stand up when the world presses down. Two calibrated points:
- **Die-added, narrow (FL Pride):** a single, escalating, at-risk D8–D12 added to one protective roll/session. Produces *peak moments*. Loss is a story beat.
- **Currency-spend, broad (West Faith):** a pool that fuels the whole push/trouble economy. Produces *sustained agency*. Depletion (Shaken) is a story beat.
- **Hybrid (recommended for new games):** a small currency pool *plus* an escalating once-session die, so players have both a steady fuel and a peak moment.

**Layer:** General (the resource exists); the wiring (die vs pool, narrow vs broad) is a **core rule choice** — see `00-engine-core.md` §11.

## 6. Relationships, companions, and the social anchor

**FL — relationships + Dark Secret:** At creation, describe your relationship to each other PC in one sentence (the profession offers 3 prompts each). Plus a **Dark Secret** (a pre-game mark/threat the GM can use) and a **home settlement + Reputation/Standing**. FL `02-your-adventurer.md:467-483, 705-715`. Social anchor = the party + a home village.

**West — relationships + Pardner + Compadres + Big Dream + home town:** Describe relationships to other PCs, then mark one as your **Pardner** (the one you'd take a bullet for). **Compadres** are player-controlled friendly NPCs with their own statblocks (family/friends/crew) — a dedicated ally rule set. The **Big Dream** is a player-authored long-term goal that drives XP awards. The **home town** is a full rule set (Settlement Points, see `09-gm-procedures.md`). West `02-your-player-character.md:36-83, 119-151`.

**Generic abstraction — "the social tether":** Every PC needs (a) intra-party bonds (relationships + one *primary* bond), (b) an NPC anchor (home settlement/town), and (c) optionally a player-controlled ally layer (Compadres) and a player-authored drive (Big Dream). FL provides the minimum (relationships + dark secret + home); West provides the maximum (+ Pardner + Compadres + Big Dream + town-as-system). The **Big Dream** is especially transferable: a player-authored goal that the GM rewards XP for pursuing *is* the character's through-line. **Layer:** General (relationships + anchor); Compadres and Big Dream are **Optional** add-ons.

## 7. Encumbrance and carrying

**Near-identical in both games:**
- Carry regular items = **primary physical attribute × 2** (FL: Strength; West: Grit), using the *base* score, not the damage-reduced one.
- **Heavy** items count as 2 (or 3–4); **Light** items count as ½ (or ¼); **Tiny** items don't count (rule of thumb: "if it can be hidden in a closed fist, it's tiny"). 100 coins = light, 200 = normal, 400 = heavy.
- **Over-encumbered:** you can exceed the limit temporarily, but must roll **Endurance** (FL) / **Resilience** (West) to run/hike, or suffer 1 damage (FL: Agility; West: Shakes) and keep going.
- **Mounts** carry Strength/Grit × 2 (×2 again if led, not ridden).
- **Backpacks/sacks** extend the limit (FL details travel backpacks, large backpacks, sacks; West keeps it lighter).
FL `02-your-adventurer.md:499-550`; West `02-your-player-character.md:89-103`.

**FL-specific — consumables as Resource Dice:** Food/water/arrows/torches aren't counted in units; each has a **Resource Die (D6–D12)** rolled on use — on a 1–2 it steps down; at D6 1–2 it's depleted. West's corebook does *not* use Resource Dice but offers them as an **Optional Module** (`06-life-in-the-old-west.md:689`). FL `02-your-adventurer.md:552-574`.

**Generic abstraction:** the "primary physical attribute × 2" carry limit, heavy/light/tiny tiers, the over-encumbrance Endurance tax, and mount-carrying are the transferable core. **Resource Dice for consumables** is a strongly-recommended optional module — it turns bookkeeping into a single die roll and naturally produces "running out" moments. **Layer:** General (the carry model); Resource Dice Optional.

**Deep inventory handoff:** this file only owns the character-sheet part of encumbrance. When designing containers, pack animals, wagons, boats, stockpiles, storage functions, group Provisions, access costs, or the personal-inventory-to-enterprise-stores boundary, load `08-gear-and-economy.md`.

## 8. Character generation: Race/archetype vs life events

**Both games offer TWO generation methods — one fast, one deep — and both tune the fast method to a genre-specific identity selector:**

**FL:**
- **Fast:** choose **Race** (8: human, elf, half-elf, dwarf, halfling, wolfkin, orc, goblin — each grants a unique **race talent** and key attribute) + **Profession** (9: Champion, Druid, Fighter, Hunter, Minstrel, Peddler, Rider, Rogue, Sorcerer — each grants key attribute, skill list, gear, Pride/Dark Secret/Relationship prompts, Resource Dice). FL `02-your-adventurer.md:40-351`.
- **Deep:** the **Life Generator** (`02-your-adventurer.md:717+`) and the full **Lifepaths of the Forbidden Lands** book (`13-lifepaths-of-the-forbidden-lands.md`) — roll/choose Race, homeland, childhood, profession, life events, age progression (Young→Adult→Old, each age reduces an attribute), mustering-out gear.
- **Age** is a choice within generation: Young = more attribute points, fewer skill/talent points; Old = the inverse.

**West:**
- **Fast:** choose one of **10 Archetypes** (Gentlefolk, Grifter, Homesteader, Laborer, Lawman, Outlaw, Prospector, Ranch Hand, Tracker, Trader) — each is a pre-built stat block with suggested talents, Big Dreams, Faiths, and gear. **Age** adds points (Greenhorn 6/2/1 → Old-timer 4/6/3 attributes/abilities/talents). West `02-your-player-character.md:337-754`.
- **Deep:** the **"Your Tale Begins" lifepath** — 2D6 birth region → upbringing (sets attributes + first 6 ability points) → family → 1–3 "Livings" (each grants 2 ability points + 1 talent, but each Living after the first costs an attribute point as you age) → Faith, Big Dream, Pardner. West `02-your-player-character.md:755-827`.
- **Group Concepts** (7: Law Men, Outlaws, Ranchers, Farmers, Business Owners, Vaqueros, Mountain Folk) are an optional **party-identity layer** that grants shared starting gear/resources. West `02-your-player-character.md:232-326`.

**Generic abstraction — "the generation-depth choice" + "the identity selector":**
1. **The identity selector** (the fast method's first choice) should be the genre's *primary social/biological category*. FL = **Race** (fantasy peoples); West = **Archetype** (a profession/life-path in frontier society). Pick whichever axis the genre uses to sort people.
2. **The generation-depth choice:** offer *fast* (pick archetype + age → done in 15 min) and *deep* (Life Events → emergent backstory). Both games ship both; both make them produce *equivalent power* characters.
3. **Age as a sub-choice:** Young = more raw potential (attributes), fewer skills/talents; Old = the inverse. This is a transferable trade-off curve that adds in-fiction texture for free.
4. **Group Concept (Optional party layer):** a shared starting identity + pooled resources — excellent for binding a party together at session zero.

**Layer:** General (both methods); Group Concept Optional.

## 9. Life Events

Life Events are the deep character method: a playable past generated through choices, rolls, gains, losses, scars, debts, and unfinished business. This is not backstory prose. It is a rules procedure that creates a character who arrives at session one with skills, talents, friends, enemies, obligations, reputation, and reasons to adventure.

**Source calibration:** FL `13-lifepaths-of-the-forbidden-lands.md` provides the richest form: Full Random, Guided Random, and Full Guided modes; Race, homeland, childhood, age, four life turns, turn tests, success/failure event tracks, wear, skill marks, talent marks, Pride/Dark Secret tags, threshold gates, crisis paths, mustering out, starting gear floors, and unfinished business. West `02-your-player-character.md:755-827` provides the compact version: birth region, upbringing, family, livings, age cost, Faith, Big Dream, Pardner.

### 9.1 The three modes

| Mode | Table method | Best for | Guardrail |
| --- | --- | --- | --- |
| Full Random | roll every step and accept the strange result | discovery, old-school play, solo generation | always apply the gear floor and profession fit pass |
| Guided Random | roll 2-3 options per step, choose one | default for most tables | never choose only the strongest reward; choose the best story |
| Full Guided | choose every step | concept-first play, licensed settings, ensemble casts | require at least one scar, debt, rival, or unfinished business |

### 9.2 Life Events procedure

1. **Choose Race.** Race is the broad people-category of the game: species, ancestry, lineage, caste, model, strain, folk, synthetic make, uplift stock, or other genre equivalent. Record its race talent, key attribute, and one social pressure it brings.
2. **Choose homeland.** Homeland is where the character learned what the world costs. It grants a local reputation, a common tongue/culture, a starting contact, and one trouble type the GM may call on.
3. **Choose childhood.** Childhood gives the first skill marks, one early relationship, and the character's first image of safety: family, clan, school, street, temple, farm, regiment, lab, ship, orphanage, gang, corporation.
4. **Choose age.** Young gives more raw attributes and fewer marks; old gives fewer raw attributes and more marks/talents. Age is the first visible trade-off between potential and history.
5. **Resolve life turns.** Each age band grants a number of turns. Four turns is the FL-rich default: Entry, Pressure, Rise, Reckoning. Shorter games may use two; generational games may use six.
6. **Make a turn test.** Pick the life path for the turn, name the risk, and roll the relevant skill. On success, take an event and ordinary marks. On 2+ successes, choose an edge. On failure, take a mishap and a hard-lesson mark.
7. **Mark wear.** Consecutive failed turns, harsh mishaps, imprisonment, disgrace, war, hunger, or exile add Wear. Wear is the past leaving a bruise.
8. **Convert marks.** Skill and talent marks convert into ranks at set thresholds. Leftover marks become XP or a small starting resource.
9. **Check thresholds.** Some paths require minimum Race, homeland, skill, talent, status, money, or contact conditions. If the character fails the threshold, offer a crisis path rather than dead-ending generation.
10. **Muster out.** The last completed path grants gear, coin, contacts, reputation, enemies, wounds, favors, or a post. Apply a gear floor so no character starts unable to play.
11. **Write unfinished business.** Every deep-generated PC leaves something open: a debt, oath, heirloom, enemy, missing kin, hidden crime, lost love, promised return, court case, bounty, diagnosis, or forbidden discovery.
12. **Choose profession.** The final profession should grow from the life turns unless the player explicitly wants a dramatic break. Seed its path talent and starting gear.
13. **Bind the party.** Answer "how did you meet?" using one shared event: survived the same disaster, served under one patron, escaped one prison, owe the same creditor, crossed the same desert, hid the same secret.

### 9.3 Life turn result table

| Turn result | Mechanical gain | Story gain | Cost or trouble |
| --- | --- | --- | --- |
| Clean success | 2 skill marks or 1 skill + 1 talent mark | ally, reputation, route, useful secret | small obligation |
| Strong success | as above + edge | patron, rare gear, status, safe house | jealous rival or public notice |
| Hard lesson | 1 hard-lesson skill mark | scar, bitter wisdom, survival trick | Wear + mishap |
| Narrow escape | 1 skill mark + gear/contact | escaped captivity, ruin, scandal, monster, lawsuit | enemy, debt, lost gear |
| Dark bargain | 1 talent mark or rare access | teacher, cult, patron, gang, spirit, officer, doctor | forbidden act, oath, blackmail |
| Lost season | 1 XP or minor mark | wandering, sickness, grief, recovery | no wealth, Wear, missed chance |

### 9.4 Wear table

| Wear | Past has done this | Choose or roll |
| --- | --- | --- |
| 0-1 | marked but not bent | distinctive scar, rumor, keepsake, enemy's name |
| 2-3 | left a lasting hook | debt, rival, fear, addiction, lost status, family trouble |
| 4-5 | changed the character's life | chronic pain, feud, outlawry, exile, broken oath, dependent |
| 6+ | almost consumed them | hunted, cursed, disgraced, terminal duty, inherited war, doomed love |

**Wear rule:** Wear is not a penalty by default. It becomes a rule only when the game wants the past to bite: a GM intrusion, a relationship edge, a starting condition, a debt die, a reputation modifier, or a blocked door. Do not punish deep generation by making the character weaker than a fast-generated peer.

### 9.5 Mark thresholds

Use marks when Life Events need to create skills without granting full ranks too fast.

| Marks in one skill/talent | Starting rank |
| --- | --- |
| 1 | rank 1 |
| 2 | rank 2 |
| 3 | rank 3 |
| 5 | rank 4 |
| 7 | rank 5 |

**Leftover marks:** convert every unused mark into 3 XP, one small contact, or one narrow piece of gear. Pick one conversion for the whole game; do not let players shop each leftover mark differently.

### 9.6 Unfinished business menu

| Business | Rule hook | Works in |
| --- | --- | --- |
| Debt | creditor can demand money, labor, silence, or risk | crime, western, space opera, court |
| Oath | breaking it costs reputation, faith, WP, or a relationship | fantasy, military, mythic, political |
| Rival | named NPC appears with leverage | any genre |
| Lost family | rescue, inheritance, feud, dependence | family saga, survival, horror |
| Hidden crime | exposure creates Trouble, Menace, or legal heat | noir, cyberpunk, court, outlaw |
| Unpaid mentor | teacher grants access but calls in service | magic, martial arts, trade, academia |
| Forbidden discovery | knowledge grants power and pursuit | occult, science, conspiracy |
| Home in danger | homeland's need becomes a campaign hook | community, war, fantasy, post-apoc |

### 9.7 Genre skins

| Genre | Race means | Homeland means | Life events look like |
| --- | --- | --- | --- |
| Fantasy | peoples of the world | village, clanhold, citadel, wandering camp | apprenticeship, war, pilgrimage, monster mark |
| Space opera | species, uplift, clone line, station-born | planet, ship, station, corporation | academy, tour, smuggling run, alien contact |
| Crime | neighborhood, family, subculture | borough, prison, crew turf | first score, betrayal, heat, prison stretch |
| Medical drama | background, class, training route | hospital, city, school, military unit | residency, outbreak, lawsuit, mentor death |
| Mecha | nation, colony, pilot strain, academy class | base, colony, carrier, city-state | training, battle, trauma, prototype test |

### 9.8 Life Events validation

- A fast-generated and deep-generated character must have equivalent total power.
- Life Events must create at least one skill rank, one relationship, one trouble, and one reason to adventure.
- No result may make a starting PC unplayable; use the gear floor and crisis paths.
- Every table must include gains, costs, and story hooks, not only bonuses.
- The last page of generation must answer: Who are you? What can you do? Who cares? Who wants something from you? Why do you leave now?

## 10. What Skills Do

Skills are not a list of verbs. Each skill is a promise about what kind of problem the game thinks is worth rolling for. A complete YZE skill entry must say when to roll, what success wins, what failure costs, what trouble follows, and what other rules it hands off to.

### 10.1 Skill families

| Family | Common names | Roll when | Success wins | Failure costs |
| --- | --- | --- | --- | --- |
| Might | Might, Labor, Fight, Endurance | force, carry, resist, smash, endure | movement through resistance, damage avoided, object moved | harm, fatigue, broken gear, delay |
| Dexterity | Move, Sleight, Operate, Shoot | speed, balance, fine handling, aim | position, shot, escape, delicate work | exposure, fall, lost item, misfire |
| Stealth | Stealth, Sneak, Hide, Shadow | unseen movement matters | position without notice | alarm, split party, lost time |
| Survival | Survival, Nature, Scouting, Hawkeye | read land, find route, find resources | route, food, camp, omen, track | mishap, depletion, weather exposure |
| Lore | Lore, Booklearning, Science, Occult | knowledge changes action | answer, clue, safe method | false certainty, time, dangerous attention |
| Craft | Crafting, Making, Repair, Doctoring | making or fixing matters | item, repair, treatment, progress | flaw, delay, material loss, harm |
| Command | Command, Presence, Leadership | groups need courage or direction | morale, order, obedience, rally | panic, mutiny, resentment |
| Insight | Insight, Empathy, Read Person | motives or lies matter | truth, leverage, danger read | misread, offense, false ally |
| Persuasion | Manipulation, Persuasion, Bargain | someone can be moved | concession, deal, delay, access | refusal, price, escalation |
| Performance | Performance, Performin', Oratory | public feeling is at stake | crowd, cover, fame, distraction | ridicule, rumor, unwanted notice |
| Beast Handling | Animal Handling, Ride, Beast Handling | animal/companion will matters | control, calm, command, bond | spooked beast, injury, lost mount |

### 10.2 Skill entry template

Use this for every new game.

| Field | Required answer |
| --- | --- |
| Name | flavorful skill name in the game's voice |
| Attribute | one of the four attributes; never floating |
| Roll trigger | the precise fictional moment that calls for a roll |
| Success | what one success definitely gives |
| Extra successes | what surplus successes can buy |
| Failure | what changes if no success appears |
| Trouble | what banes/Trouble can add even if the roll succeeds |
| Hand-off | combat, harm, travel, gear, power, holdings, social, or GM procedure |
| No-roll zone | what this skill does automatically for competent characters |

### 10.3 Resolution checks by skill type

**FORCE A WAY.** Roll a Might-family skill when brute pressure must overcome resistance now. Success opens the way, holds the door, breaks the grip, carries the load, or keeps the body going. Failure means the obstacle remains and the character takes harm, fatigue, lost time, or broken gear. Extra successes may move faster, protect an ally, reduce damage, or avoid noise.

**MOVE UNDER DANGER.** Roll a Dexterity-family skill when position, balance, precision, or speed is the risk. Success changes position or completes the delicate act. Failure exposes the character, costs gear, causes a fall, triggers a trap, or worsens range/cover. Extra successes may improve position, keep silent, help an ally, or bank a carry-forward bonus.

**PASS UNSEEN.** Roll Stealth when unseen action matters and discovery would change the scene. Success reaches the stated position unnoticed. Failure does not always mean instant capture; it may mean a guard changes route, a clock advances, the party splits, or the character must choose between speed and silence.

**READ THE WORLD.** Roll Survival or Lore when the table needs a trustworthy answer that changes action. Success gives a route, clue, weakness, safe method, or warning. Failure gives incomplete truth, delay, a wrong-but-plausible answer, or a dangerous price for certainty.

**MAKE OR MEND.** Roll Craft when work can fail meaningfully. Success produces the repair, treatment, item, or project progress. Failure creates delay, flaw, material loss, patient harm, tool breakage, or the need for a better workshop.

**MOVE HEARTS.** Roll Persuasion, Performance, Command, or Insight when another will is truly at stake. Success wins a concession, read, morale shift, cover, audience, or delay. Failure changes the relationship: suspicion, demand, insult, fear, rumor, counteroffer, or escalation.

**MASTER A BEAST.** Roll Beast Handling when an animal or companion has fear, hunger, pain, instinct, training, or loyalty in the way. Success gets obedience, calm, speed, tracking, or trust. Failure makes the beast balk, bolt, bite, draw notice, lose supplies, or demand recovery.

### 10.4 Extra-success menu

| Spend | Effect |
| --- | --- |
| Faster | halve time or act before danger catches up |
| Cleaner | avoid noise, trace, witness, flaw, or insult |
| Safer | reduce harm, preserve gear, avoid a condition |
| Wider | include an ally, more cargo, more audience, more ground |
| Deeper | learn one extra truth, motive, weakness, or route |
| Better | improve quality, price, reputation, or future modifier |

### 10.5 Skill validation

- Every skill must have at least three recurring scene uses.
- No skill should own both too much action and too much information.
- A skill that only adds color should be folded into another skill.
- A skill that replaces a wider rule set must name that handoff.
- If two skills could roll for the same moment, decide by risk: body, position, knowledge, making, will, or beast.
- A 16-skill grid is full. Add a new skill only by removing or merging another.

## 11. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Attribute naming** | Survival axes (STR/AGI/WIT/EMP) | Frontier-grit (Grit/Quick/Cunning/Docity) | Generic-resolver vs genre-flavored | Name attributes after the genre's tension (West-style) unless you need pure portability |
| **Damage typing** | By position (silent) | By name (Hurts/Shakes/Vexes/Doubts) | Functional vs fictional-rich | Always name them (West-style) — free genre-loading |
| **Attribute ceiling (creation)** | 2–4 (5/6 key) | 1–5 | Narrow competent range vs wider curve | Match to desired power spread |
| **Inner fire model** | Pride (die, narrow, once/session) | Faith (pool, broad, whole loop) | Peak moments vs sustained agency | Hybrid for new games; Pride-style for lethal one-shots; Faith-style for dramatic arcs |
| **Inner fire identity** | "Stubborn will" (a note) | One-sentence belief system | Light vs heavy identity load | Faith-style if the genre is about belief (West, horror); Pride-style if it's about grit |
| **Social anchor depth** | Relationships + Dark Secret + home settlement | + Pardner + Compadres + Big Dream + town | Minimum vs maximum | Add Big Dream always (free XP engine); Compadres if you want NPC allies |
| **Encumbrance detail** | Backpacks/sacks tables | Lighter | Precision vs speed | Match table taste |
| **Consumables tracking** | Resource Dice (default) | Counted (Resource Dice optional) | Die-roll vs bookkeeping | Resource Dice always — less bookkeeping, better "running out" drama |
| **Fast-gen identity selector** | Race (biological/cultural species) | Archetype (social profession) | Fantasy races vs social roles | Pick the genre's primary sorter |
| **Life Events default** | Optional add-on book | Standard deep method | Deep Life Events = specialist text | Ship Life Events; make them optional but available |
| **Party-identity layer** | (none formalized) | Group Concepts (7) | None vs shared starting identity | Add a Group Concept layer for strong party-binding |

## 12. Rule choices and instantiation recipe

To build the character model for a new YZE game:

1. **Name four attributes** after the genre's core tension (not STR/DEX/INT/CHA unless that's genuinely the genre). Each attribute = one axis of genre pressure.
2. **Name each attribute's damage type** with a genre noun (Hurts/Shakes/etc.). This is free genre-loading.
3. **Write 16 skills** (4 per attribute), named in-genre. Skill names do most of the re-skinning work.
4. **Set the attribute range + ceiling** (e.g. 2–4 or 1–5) and the creation point budget by "age" or equivalent.
5. **Pick the inner fire model** (die-narrow / pool-broad / hybrid) and its identity load (a note vs a belief sentence). Wire it to the push-cost model chosen in `00-engine-core.md` §11.
6. **Set the social anchor:** relationships + primary bond + home settlement minimum; add Big Dream + Compadres if desired.
7. **Port the encumbrance model** (primary physical attribute × 2 + heavy/light/tiny + over-encumbrance tax). Adopt **Resource Dice** for consumables, then load `08` if inventory pressure matters beyond personal rows.
8. **Choose the identity selector** for fast gen (the genre's primary social/biological sorter).
9. **Ship both fast and deep generation.** Make age (or equivalent) a visible choice trading attributes for skills/talents. Use Life Events when the past must matter in play.
10. **Write What Skills Do.** Each skill needs roll trigger, success, extra-success spends, failure, Trouble, handoff, and no-roll zone.
11. **(Optional) Add a Group Concept layer** for party-binding at session zero.
12. **Check:** does each attribute have 4 distinct, non-overlapping skills? Does each damage type feel like the genre? Does inner fire produce the right rhythm of peak/sustained agency? Can a Life Events character enter play with hooks but not lower power?

## 13. Design intent

The character model is engineered to be **small enough to hold in the head, symmetrical enough to balance, and flavorable enough to feel like any genre:**

- **The 4×4 grid** is the load-bearing constraint. Four attributes is the magic number — few enough to grasp, enough to differentiate characters. Four skills each makes every attribute matter equally.
- **Attribute-as-HP + named damage types** means attrition is *specific* and *felt* — "2 Hurts and a Vex" is a story state; "−2 to two stats" is not. This is the engine's signature feel.
- **Inner fire** is what keeps the engine from being pure attrition — it's the player's *personal* resource for turning a loss into a win, and its identity load (Pride/Faith) makes the rule a character beat, not just a number.
- **Dual generation methods** (fast + Life Events) serve two player populations without splitting the rules — and both produce equivalent power, so the choice is about *story*, not optimization.
- **The identity selector + skill names** do the bulk of genre re-skinning. You can take the entire engine and make it feel like cyberpunk, post-apoc, or space opera largely by choosing what Race means, renaming profession→role, and rewriting the 16 skill names. The *mechanics* barely change; the *fiction* transforms completely. This is the engine's greatest strength and the reason a generic skill like this one is possible.
