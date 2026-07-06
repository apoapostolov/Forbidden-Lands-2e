<!-- markdownlint-disable MD013 -->

# Character Model — Attributes, Skills, Damage, Generation

> **STATUS: FILLED (Pass-1 + Pass-2).** Read alongside `00-engine-core.md` (resolution) and `02-progression-and-xp.md` (advancement).

## Contents

1. Source provenance
2. Abstraction target
3. The 4×4 attribute-skill grid
4. Per-attribute damage types
5. Pride / Faith — the once-per-session protected die / metacurrency
6. Relationships, companions, and the social anchor
7. Encumbrance and carrying
8. Character generation: kin/archetype vs lifepath
9. Divergence rows (FL vs West)
10. Dials and instantiation recipe
11. Design intent

## Source provenance

**Forbidden Lands 2E (FL):**
- `01-corebook/02-your-adventurer.md:1-744` — 8 kin, 9 professions, age, attributes (STR/AGI/WIT/EMP, 2–6 range), 16 skills, Pride, Dark Secret, relationships, encumbrance (Strength×2 + backpacks/sacks), consumables (Resource Dice), experience, training, reputation, **Life Generator**.
- `01-corebook/13-lifepaths-of-the-forbidden-lands.md` — full advanced lifepath system.
- `02-gamemasters-guide/05-kin.md` — expanded kin write-ups.

**Tales of the Old West 2E (West):**
- `01-corebook/02-your-player-character.md:1-827` — 4 attributes (Grit/Quick/Cunning/Docity, 1–5 range) each with a **named damage type** (Hurts/Shakes/Vexes/Doubts), 16 abilities, **Big Dream**, **Faith**, talents, relationships + **Pardner**, encumbrance (Grit×2), Compadres, Session Zero, **Group Concepts** (7), **10 Archetypes**, the **"Your Tale Begins" lifepath**, XP/advancement.
- `01-corebook/04-talents.md` — talent access gating.

## Abstraction target

Abstract the **character model** as a genre-neutral skeleton: a small grid of attributes (each owning a *damage type* and a *cluster of skills*), a per-session protected die / metacurrency, a social/relationship anchor, an encumbrance rule, and a choice between archetype-based vs lifepath-based generation. FL and West both use a 4×4 grid but flavor it completely differently — capture that as the canonical "attribute identity" recipe: **the *name* and *damage-type name* of each attribute should express the genre's core tension.** The two games also demonstrate two ends of the *generation-depth* dial (FL: kin + profession + optional deep lifepath book; West: archetype-quick + standard lifepath, with a richer Session Zero / Group Concept social layer).

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

## 5. Pride / Faith — the once-per-session protected die / metacurrency

Both games give each PC a **personal pressure-relief resource** tied to character identity — but they wire it to the core loop very differently (this is one of the engine's most important divergences; see `00-engine-core.md` §7 for the full metacurrency treatment).

**FL — Pride (a die, narrow scope):** Once per session, after failing a roll made *to protect yourself or another person*, you may add your **Pride die** (D8/D10/D12). It starts at D12. If the roll still fails, you *lose* Pride for next session; it returns at D8 thereafter. If you use it and succeed, or don't use it, it grows one step (D8→D10→D12) next session. FL `02-your-adventurer.md:456-462`, `03-skills.md:254-258`. **Scope:** narrow — only protective rolls. **Identity load:** Pride is "the stubborn will that keeps you standing."

**West — Faith (a currency, broad scope):** Faith is a *metacurrency pool* (4/scenario, cap 10) that pays for **all pushes** (1/push) *and* **buys off Trouble** (1:1). It's not a die added to a roll — it's the fuel for the entire push/trouble subsystem. Faith is earned by 3-⚔ un-pushed rolls or by performing in-fiction rituals/actions. At 0, you're **Shaken** (can't push, can't gain Faith). West `03-rolling-the-bones.md:84-88, 258-311`. **Scope:** broad — the whole core loop. **Identity load:** Faith is described in one sentence ("the Lord is my shepherd," "my place is in the saddle") and is *what keeps you going.*

**Generic abstraction:** the "protected dial" is the player's personal safety/fuel resource. Two calibrated points:
- **Die-added, narrow (FL Pride):** a single, escalating, at-risk D8–D12 added to one protective roll/session. Produces *peak moments*. Loss is a story beat.
- **Currency-spend, broad (West Faith):** a pool that fuels the whole push/trouble economy. Produces *sustained agency*. Depletion (Shaken) is a story beat.
- **Hybrid (recommended for new games):** a small currency pool *plus* an escalating once-session die, so players have both a steady fuel and a peak moment.

**Layer:** General (the resource exists); the wiring (die vs currency, narrow vs broad) is a **core design dial** — see `00-engine-core.md` §11.

## 6. Relationships, companions, and the social anchor

**FL — relationships + Dark Secret:** At creation, describe your relationship to each other PC in one sentence (the profession offers 3 prompts each). Plus a **Dark Secret** (a pre-game mark/threat the GM can use) and a **home settlement + Reputation/Standing**. FL `02-your-adventurer.md:467-483, 705-715`. Social anchor = the party + a home village.

**West — relationships + Pardner + Compadres + Big Dream + home town:** Describe relationships to other PCs, then mark one as your **Pardner** (the one you'd take a bullet for). **Compadres** are player-controlled friendly NPCs with their own statblocks (family/friends/crew) — a dedicated ally subsystem. The **Big Dream** is a player-authored long-term goal that drives XP awards. The **home town** is a full sub-system (Settlement Points, see `09-gm-procedures.md`). West `02-your-player-character.md:36-83, 119-151`.

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

## 8. Character generation: kin/archetype vs lifepath

**Both games offer TWO generation methods — one fast, one deep — and both tune the fast method to a genre-specific identity selector:**

**FL:**
- **Fast:** choose **Kin** (8: human, elf, half-elf, dwarf, halfling, wolfkin, orc, goblin — each grants a unique **kin talent** and key attribute) + **Profession** (9: Champion, Druid, Fighter, Hunter, Minstrel, Peddler, Rider, Rogue, Sorcerer — each grants key attribute, skill list, gear, Pride/Dark Secret/Relationship prompts, Resource Dice). FL `02-your-adventurer.md:40-351`.
- **Deep:** the **Life Generator** (`02-your-adventurer.md:717+`) and the full **Lifepaths of the Forbidden Lands** book (`13-lifepaths-of-the-forbidden-lands.md`) — roll/choose kin, home region, childhood, profession, formative events, age progression (Young→Adult→Old, each age reduces an attribute), mustering-out gear.
- **Age** is a dial within generation: Young = more attribute points, fewer skill/talent points; Old = the inverse.

**West:**
- **Fast:** choose one of **10 Archetypes** (Gentlefolk, Grifter, Homesteader, Laborer, Lawman, Outlaw, Prospector, Ranch Hand, Tracker, Trader) — each is a pre-built stat block with suggested talents, Big Dreams, Faiths, and gear. **Age** adds points (Greenhorn 6/2/1 → Old-timer 4/6/3 attributes/abilities/talents). West `02-your-player-character.md:337-754`.
- **Deep:** the **"Your Tale Begins" lifepath** — 2D6 birth region → upbringing (sets attributes + first 6 ability points) → family → 1–3 "Livings" (each grants 2 ability points + 1 talent, but each Living after the first costs an attribute point as you age) → Faith, Big Dream, Pardner. West `02-your-player-character.md:755-827`.
- **Group Concepts** (7: Law Men, Outlaws, Ranchers, Farmers, Business Owners, Vaqueros, Mountain Folk) are an optional **party-identity layer** that grants shared starting gear/resources. West `02-your-player-character.md:232-326`.

**Generic abstraction — "the generation-depth dial" + "the identity selector":**
1. **The identity selector** (the fast method's first choice) should be the genre's *primary social/biological category*. FL = **Kin** (a fantasy game's races); West = **Archetype** (a profession/life-path in frontier society). Pick whichever axis the genre uses to sort people.
2. **The generation-depth dial:** offer *fast* (pick archetype + age → done in 15 min) and *deep* (lifepath → emergent backstory). Both games ship both; both make them produce *equivalent power* characters.
3. **Age as a sub-dial:** Young = more raw potential (attributes), fewer skills/talents; Old = the inverse. This is a transferable trade-off curve that adds in-fiction texture for free.
4. **Group Concept (Optional party layer):** a shared starting identity + pooled resources — excellent for binding a party together at session zero.

**Layer:** General (both methods); Group Concept Optional.

## 9. Divergence rows (FL vs West)

| Decision | FL option | West option | Trade-off | When to choose |
| --- | --- | --- | --- | --- |
| **Attribute naming** | Survival axes (STR/AGI/WIT/EMP) | Frontier-grit (Grit/Quick/Cunning/Docity) | Generic-resolver vs genre-flavored | Name attributes after the genre's tension (West-style) unless you need pure portability |
| **Damage typing** | By position (silent) | By name (Hurts/Shakes/Vexes/Doubts) | Functional vs fictional-rich | Always name them (West-style) — free genre-loading |
| **Attribute ceiling (creation)** | 2–4 (5/6 key) | 1–5 | Narrow competent range vs wider curve | Match to desired power spread |
| **Protected dial model** | Pride (die, narrow, once/session) | Faith (currency, broad, whole loop) | Peak moments vs sustained agency | Hybrid for new games; Pride-style for lethal one-shots; Faith-style for dramatic arcs |
| **Protected dial identity** | "Stubborn will" (a note) | One-sentence belief system | Light vs heavy identity load | Faith-style if the genre is about belief (West, horror); Pride-style if it's about grit |
| **Social anchor depth** | Relationships + Dark Secret + home settlement | + Pardner + Compadres + Big Dream + town | Minimum vs maximum | Add Big Dream always (free XP engine); Compadres if you want NPC allies |
| **Encumbrance detail** | Backpacks/sacks tables | Lighter | Precision vs speed | Match table taste |
| **Consumables tracking** | Resource Dice (default) | Counted (Resource Dice optional) | Die-roll vs bookkeeping | Resource Dice always — less bookkeeping, better "running out" drama |
| **Fast-gen identity selector** | Kin (biological/cultural species) | Archetype (social profession) | Fantasy races vs social roles | Pick the genre's primary sorter |
| **Lifepath default** | Optional add-on book | Standard deep method | Deep lifepath = specialist text | Ship a lifepath; make it optional but available |
| **Party-identity layer** | (none formalized) | Group Concepts (7) | None vs shared starting identity | Add a Group Concept layer for strong party-binding |

## 10. Dials and instantiation recipe

To build the character model for a new YZE game:

1. **Name four attributes** after the genre's core tension (not STR/DEX/INT/CHA unless that's genuinely the genre). Each attribute = one axis of genre pressure.
2. **Name each attribute's damage type** with a genre noun (Hurts/Shakes/etc.). This is free genre-loading.
3. **Write 16 skills** (4 per attribute), named in-genre. Skill names do most of the re-skinning work.
4. **Set the attribute range + ceiling** (e.g. 2–4 or 1–5) and the creation point budget by "age" or equivalent.
5. **Pick the protected-dial model** (die-narrow / currency-broad / hybrid) and its identity load (a note vs a belief sentence). Wire it to the push-cost model chosen in `00-engine-core.md` §11.
6. **Set the social anchor:** relationships + primary bond + home settlement minimum; add Big Dream + Compadres if desired.
7. **Port the encumbrance model** (primary physical attribute × 2 + heavy/light/tiny + over-encumbrance tax). Adopt **Resource Dice** for consumables.
8. **Choose the identity selector** for fast gen (the genre's primary social/biological sorter).
9. **Ship both fast and deep generation.** Make age (or equivalent) a sub-dial trading attributes for skills/talents.
10. **(Optional) Add a Group Concept layer** for party-binding at session zero.
11. **Validate:** does each attribute have 4 distinct, non-overlapping skills? Does each damage type feel like the genre? Does the protected dial produce the right rhythm of peak/sustained agency?

## 11. Design intent

The character model is engineered to be **small enough to hold in the head, symmetrical enough to balance, and flavorable enough to feel like any genre:**

- **The 4×4 grid** is the load-bearing constraint. Four attributes is the magic number — few enough to grasp, enough to differentiate characters. Four skills each makes every attribute matter equally.
- **Attribute-as-HP + named damage types** means attrition is *specific* and *felt* — "2 Hurts and a Vex" is a story state; "−2 to two stats" is not. This is the engine's signature feel.
- **The protected dial** is what keeps the engine from being pure attrition — it's the player's *personal* resource for turning a loss into a win, and its identity load (Pride/Faith) makes the mechanic a character beat, not just a number.
- **Dual generation methods** (fast + lifepath) serve two player populations without splitting the rules — and both produce equivalent power, so the choice is about *story*, not optimization.
- **The identity selector + skill names** do the bulk of genre re-skinning. You can take the entire engine and make it feel like cyberpunk, post-apoc, or space opera largely by renaming kin→lineage/species, profession→role, and the 16 skills. The *mechanics* barely change; the *fiction* transforms completely. This is the engine's greatest strength and the reason a generic skill like this one is possible.
