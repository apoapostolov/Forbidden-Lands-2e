<!-- markdownlint-disable MD013 MD024 -->

# Changelog

All notable changes to the Forbidden Lands Corebook will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Added the missing political layer between settlement play and mass combat. Introduces faction creation and play with the native pillars `Mandate`, `Force`, `Reach`, and `Hearth`; sixteen practices covering legitimacy, coercion, logistics, intrigue, and extraction; legacies; settlement bonds (ruled, protected, tributary, vassal, occupied, allied); feud escalation; seasonal faction turns and campaign weeks; tribute, burden, levy, retainer, mercenary, and supply-line rules; guidance for converting faction contingents into Chapter 12 troops; and six premade factions for campaign use.

### Changed

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Added a persistent army layer between faction turns and `BATTLES & SIEGES`: the faction sheet now records `Armies at Disposal`; Chapter 11 now includes a separate army roster, army-scale guidance that keeps most Ravenlands wars at small-host or field-host size, `Reach` limits for how many separate armies a faction can keep moving cleanly, rough `Provision Load / Pay Load` bands, weekly `Provisions` and `Maintenance` procedures, and army-travel rules derived from the existing quarter-day movement engine rather than a new one. The `Call Levy`, `Hire Mercenaries`, and war handoff guidance now point into that roster layer, and every premade faction now includes ongoing named army rosters rather than only a loose force list.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Added explicit `Agents` and `Advisors` rules for named faction hands below army scale. Traveling agents now use ordinary adventurer attribute-and-skill rolls when the GM resolves a dangerous offstage undertaking, and only faction-changing achievements on the scale of a short campaign or greater can generate CP for the faction. Resident advisors now use ordinary adventurer rolls for seat intrigue, muster reckoning, envoy handling, counter-espionage, hostage management, and other hall-bound work; their successes grant stored bonus dice to later seat-based faction checks, and a truly exceptional difficulty-4 success can convert one of those into a `D8` Ascendancy Die instead.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Repositioned `Armies at Disposal` so the army roster layer now sits later in the chapter, after the political-act, burden, revenue, fallout, and levy material it depends on. The roster table now uses `BATTLE FORM` instead of `CHAPTER 12 FORM`, the surrounding prose now points to `BATTLES & SIEGES` by title rather than chapter number, and army travel is recalculated around a **10-hex** weekly pace for a foot host on good ground, with the rest of the movement table adjusted from that anchor.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Added faction **Campaign Points (CP)** advancement for practices, pillars, and legacies without any teacher requirement, with milestone awards keyed to minor gains, major successes, significant victories, and full conquest or absorption, plus pillar recovery tied to the kind of victory that earned the CP. Also revised Chapter 11 prose cadence across its framing, turn structure, and political procedures to reduce the chopped micro-paragraph feel and bring the rules exposition closer to the denser paragraph rhythm used elsewhere in the Gamemaster's Guide. The chapter now expands `Key Terms` into a fuller glossary, uses a table-based faction sheet with `RECORD` fields, renames the pillar set to `Mandate / Force / Reach / Hearth`, grounds Treasury by ready-silver benchmarks from the corebook economy, splits Labor / Levy / Retainers into separate working tables, gives Treasury, Stores, Labor, Levy, and Retainers direct procedural weight, and rewrites every legacy path in a Chapter 04-style rank presentation with stronger high-rank faction effects.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Refined the faction engine further: CP awards may now be spent immediately to heal damaged pillars instead of being banked; pillar healing uses a stepped CP cost table; assets now use rated **1–5 asset dice** with only the single highest relevant asset applying to a roll; overwhelming advantages may replace one base die with a once-per-season **Ascendancy Die**; passive faction recovery is reduced to **1 pillar point per Season Turn**; `Political Instruments` is expanded into more practical medieval guidance on oaths, hostages, charter rights, sanction, and outlawry; and the faction turn is rebuilt as four explicit **Modes of Rule** (`Peace`, `Pressure`, `Muster`, `Campaign`) with separate GM procedures for community control, development, prosperity, logistics, production, and campaign upkeep.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Clarified that asset banes reduce an asset only when the final roll fails or when the roll is pushed, never on a successful unpushed roll; moved campaign-defining named examples like the **Crown of Five Elven Rubies** and a **captured monster kept as a weapon** into the `Ascendancy Dice` guidance; added an explicit optional **Decree** step to every Mode of Rule; and defined the political action system more cleanly by separating **minor acts**, **major acts**, and **campaign acts**, with `Issue Decree` formalized as a minor act that can also generate limited carryover bonus dice for the next faction turn of the same length.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Renamed `Political Acts` to `Faction Acts`, alphabetized the act entries, added an explicit `**TYPE:**` line under every act heading, moved the old revenue/tribute/burden material to follow the acts, split it into separate `Fallout`, `Burden`, `Revenue`, and `Tribute` sections, and added `D66` tables for failed faction-act fallout and failed burden-linked outcomes.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Reworked the `Act Scale` presentation so default act scope now lives inside the table instead of a technical lead-in, added a new `Handoff` procedure with `D66` failed-transition outcomes for crossing from faction play into `BATTLES & SIEGES`, normalized stronghold function naming to fullcaps and troop-source bullets to the chapter's preferred bold-capitalized style, renamed the war-transition heading away from technical language, and greatly expanded `After the War` to cover hunger, veteran return, scarcity, broken infrastructure, and supernatural fallout in ravaged lands.

- **Writing standards.** Updated both `WRITING_GUIDE.md` and the `forbidden-lands-writing` skill rules to state explicitly that rule voice must never slip into technical-document language, even when the prose is procedural and exact.

- **Gamemaster's Guide Chapter 11 — Politics of the Forbidden Lands.** Expanded `After the War` again so each major aftermath track now produces concrete `D66` results: failed hunger recovery, failed veteran resettling, market scarcity scenes, broken-works encounter fallout, and tainted-ground manifestations. Also completely replaced the old generic premade faction roster with setting-rooted powers drawn from `History`, `Gods`, and `Kin`, including Alderstone's Rust Brothers, Zertorme at Amber's Peak, the Raven Sisters, the Golden Bough, the Redrunners, the Iron Hounds of Stonegarden, Emperor Hroka's Urhurs, and the Gristle's company as the surviving mercenary hook.

- **Gamemaster's Guide Chapter 12 — Battles & Sieges second-pass war procedures.** Added an explicit morale-roll procedure for all existing morale checks; expanded siege play with leaky blockade, supply-run, surrender, parley, and bad-faith rules; added ransom negotiation procedure; sharpened unpaid-soldier consequences with weekly commander checks, desertion, and mutiny outcomes; added wartime coercion procedures for hostages, quartering, and exemplary violence when villages refuse contribution; and added post-assault mercy, ordered sack, open sack, and occupation-holding procedures so siege aftermath now models plunder, disease, discipline loss, reprisals, and the long cost of treachery.

- **Gamemaster's Guide Chapter 12 — Battles & Sieges core battle clarity pass.** Added a short quickstart for running a battle from the chapter's core path; defined section adjacency; added explicit reserve-commitment and battle-turn-order procedures; corrected demoralization so unresolved base-die banes remove fleeing groups at troop scale instead of mixing exact soldier counts with base-die losses; clarified friendly-fire resolution for skirmishers shooting into allied melees; added a `Winning a Section` procedure for hold / pivot / pursue decisions; added a `Breach and Gate Fighting` transition for wall sections that stop functioning as walls; and added a `Relief of a Siege` procedure for the moment a field army reaches an invested fortress.
- **Gamemaster's Guide Chapter 12 — Battles & Sieges troop-strength clarification.** Clarified that troops may still be recorded with exact musters, but battle tracks fighting groups by threshold rather than counting single bodies in the middle of the clash: one base die normally stands for twenty infantry or skirmishers, five cavalry, or one monster, with siege defenders using ten per die, and each point of unresolved damage removes one such full group.
- **Gamemaster's Guide Chapter 12 — Battles & Sieges battle-pace refinement.** Slowed section collapse slightly so more battlefield decisions can matter before a line disappears: only one edge-spend option that inflicts direct damage may now be chosen per section per turn, protection that still catches part of the blow now preserves 1 morale point from that exchange, and a reserve already waiting behind a section may be thrown in immediately if the frontline troop is destroyed before it can answer.

- **Gamemaster's Guide Chapter 12 — Battles & Sieges tactical completeness pass.** Added battlefield screening and picket rules before deployment; made siege-engine progress explicitly visible to defenders; clarified when blockade-running can bring reinforcements into a fortress; added counter-siege measures for burning towers and rams, countermine work, and deliberate withdrawal from an outer wall; added rear-area pressure rules for baggage raids, camp raids, and baggage guards; and added ferry, boat, landing, and waterside assault rules so crossings and water access matter more sharply in campaign war and siege play.

- **Gamemaster's Guide Chapter 12 — Battles & Sieges advantage-edge expansion.** Expanded uncancelled advantage successes so they can now be spent on battlefield gains instead of only damage, including pressing a section back, pinning it in place, cutting down signalers, covering a withdrawal, opening gaps for adjacent troops, spoiling reserve relief, silencing standards, disordering shields, triggering panic, seizing key ground at gates and breaches, and riding through to baggage or engines when cavalry breaks the rear. The battle-roll flow now also states when weapon attack properties are applied, turns direct extra damage into explicit edge-spend choices, adds a costly 3-success option to inflict 2 damage at the price of being more exposed on the next turn, and places the local damage-resolution procedure next to the battle roll.

- **Corebook — Prose quality improvements across eleven chapters.** Opening and framing prose revised in Chapters 1, 2, 3, 5, 7, 8, 9, 11, 12, and 13 (Front Matter, Your Adventurer, Skills, Combat & Damage, Magic, Journeys, The Stronghold, Appendix, Mercenaries of the Forbidden Lands, Lifepaths of the Forbidden Lands). Filler phrasing, rhetorical ornamentation, and over-articulated observations replaced with direct, physically-grounded prose. Key revisions: kin entry descriptions (Half-Elf, Orc, Rider) rewritten to open on behavior and physical circumstance; the Civilized/Uncivilized framing section tightened and the embedded narrator-apology sentence removed; LORE skill description revised to a single clear statement; Magic chapter opening replaced with concrete grounded language; Stronghold chapter intro's closing rhetorical question removed; Heroic Campaign section in the Appendix reframed to state its register directly; the Mercenaries chapter scope paragraph condensed; the Lifepaths intro and one descriptive bullet reworked to open on specific consequence. No rules content changed.

### Changed

- **Bestiaries — Lore Roll spoiler scaling.** Restructured Lore Roll tables across the Gamemaster's Guide bestiary (Abyss Worm, Bloodling, Ent, Ghost, Giant, Giant Squid, Gryphon, Hydra, Manticore, Sea Serpent, Troll, Wyvern) and the Book of Beasts (Amoeba, Basilisk, Bog Man, Greater Golem, Imp, Iron Dragon, Mara, Mummy, Possessor, Rat King, Rock Troll, Swarming Death, Twisted Ent, Will-o'-the-Wisp, Wolfshadow). Two successes now give a solid in-world hint via songs, warnings, and observations that still requires the players to think; three successes give a more directional hint with narrative effect, no bare mechanic words or spell names.
- **Gamemaster's Guide Chapter 06 — Bestiary encounters and resources.**
  - **Scope:** Complete rewrite of the random encounters and RESOURCES block for all 23 monster entries (Abyss Worm, Bloodling, Death Knight, Demon, Dragon, Drakewyrm, Ent, Ghost, Giant, Giant Squid, Gray Bear, Gryphon, Harpies, Hydra, Insectoids, Manticore, Minotaur, Nightwargs, Sea Serpent, Strangling Vine, Troll, Undead, Wyvern).
  - **Encounters:** Moved away from village-attack tropes toward unexpected moral or physical dilemmas where the victim is not innocent, the pay is generous and the price worse, or the monster is the symptom and not the threat.
  - **Resources:** RESOURCES blocks de-templated: every monster now yields salvage tied to its own specific ability — potency-scaled poisons, canonical potion ingredients (troll, dragon, hydra, gryphon, manticore, drakewyrm, insectoid, sea serpent, ghoul), Artifact Dice on narrow acts, condition cures, attribute restoration, and narrative tools (worm saliva that dissolves iron, squid eye-lens darksight, drakewyrm pollen beacon, giant tooth weapon-core, minotaur horn, gravefrost that lets lanterns hold the speech of the dead, night-shadow that frosts every wound, sea serpent crown-horn whistle, strangling vine-rope, wyvern pinion-bone oil).
  - **Pattern removed:** The +1-to-X for one Quarter Day pattern has been removed from every entry.
- **Book of Beasts Chapter 02 — Bestiary encounters and resources.**
  - **Scope:** Complete overhaul of the random encounters and RESOURCES block for all 28 monster entries (Amphibian, Amoeba, Basilisk, Bog Man, Dread Raptor, Gatekeeper, Giant Specter, Giant Spider, Greater Golem, Imp, Iron Dragon, Mara, Mire Drake, Mummy, Nature Spirit, Possessor, Rat King, Rock Troll, Shapeshifter, Skolopendra, Swarming Death, Tupilaq, Twisted Ent, Undead Dragon, Vampyr, Water Troll, Will-o'-the-Wisp, Wolfshadow).
  - **Encounters:** Two encounters per monster, each built around a moral dilemma, a physical choice, or a person already decided — bound bridegrooms paying troll-tithes, dwarven husbandries fattening rock trolls on stolen cattle, a Druid keeping a plague village alive while the rat king waits in the bell-tower, a Raven Sister bound to play her brother's wakening song, a vampyr cleansing a village it has hypnotised, an undead dragon holding court at a mass grave with a chained reader.
  - **Structure:** Tropes of "the village is attacked" replaced throughout with named NPCs, factional pressures (Iron Guard, Rust Brothers, Raven Sisters, Wyrm cult, Order of the Silent, Howling Path, Meromannian dwarves, Aslene riders), and time-pressure scenarios where every choice has a price.
  - **Resources:** Book 03 resource-gathering notes were expanded into a large section that makes monster parts play a more important role for alchemists and spellcasters.
  - **Harvest:** RESOURCES blocks de-templated and tied to canonical Alchemical Potions where the monster's ingredient is bound (dragon's blood/scale/tooth, troll's blood/tooth/gastric juice, giant spider venom for Porridge of Prophecy, insect-ichor, blackened ent ruby, manticore-line components), with named materials, harvest mechanic per ⚔️ rolled, factional buyers and hunters, and narrative tools (cold-light crystals, bone flutes that command vermin, queen-husks that turn aside swarms, blood-stones that hypnotise weak humanoids, mimic-skins that imitate one voice, binding-tokens that send curses back to the sorcerer who set them).

## [1.0.8] - 2026-04-24

### Added

- **Gamemastery Guide.** Added as a 2nd Edition template. It is fully processed to compliant standard Markdown format and will be expanded into a second edition in the coming weeks.
  - - **Chapter 06 — Bestiary.** Expanded Gamemaster's Guide monster entries toward the Book of Beasts format. Added flavor vignettes, Lore Roll tables, two random encounters per main monster group, and resources blocks for alchemical or magical salvage.
  - **Chapter 10 — Villages and Towns.** Expanded settlement chapter added to the Gamemaster's Guide. Covers settlement history, current state, resources, inhabitants, situations, and long-term change through vicissitudes.
  - **Chapter 10 — Villages and Towns.** Added settlement turn, household ledger, stores and shortages, optional route links for pointcrawl play, first-arrival guidance, and justice/retaliation procedures.
- **Book of Beasts.** Added as a 2nd Edition template. It is fully processed to compliant standard Markdown format and will be expanded into a second edition in the coming weeks.

## [1.0.7] - 2026-04-13

### Added

- **Chapter 07 — Demonic Magic.** Seventeenth discipline for Sorcerers. Built around mog — a corrosive substance from the demon dimension Churmog; practitioners hunted on sight in settlements. 20 spells across R1–R6, mog handling rules, D66 mishap table.
- **Chapter 07 — New spells across existing disciplines.** 21 new spells added to 10 existing disciplines: General (3), Healing (2), Awareness (2), Symbolism (2), Elemental Magic (5), Ice Affinity (3), Blood Magic (1), Mentalism (2), Shapeshifting (1).
- **Chapter 07 — Rarity and Secrecy table.** Reference table for all 17 disciplines with public reaction (Known to Prohibited) and teacher access (Initiation to Journey).
- **Chapter 07 — Burn rules.** Casters may burn attribute points to fuel a spell: 1D8 random attribute damage per point, 1 WP per point (current spell only).
- **Chapter 04 — PATH OF THE UNCLEAN.** Five-rank Sorcerer path talent for Demonic Magic. Progressive mog-symbiosis abilities and permanent appearance changes at each rank.
- **Chapter 08 — VILLAGES AND TOWNS.** Seven player-facing settlement activities added after REPUTATION: ASK AROUND, THE NOTICE BOARD (posted jobs by settlement size), SEEK WORK (two-roll employment, six work types by D6, tiered pay 1D6cp–3s, in-kind pay at poor settlements, board option), PETITIONING AUTHORITY (nine types, patron track 0–3), CAROUSE, REPUTATION AS LEVERAGE, and SETTLEMENT VISIT FLOW.
- **Chapter 08 — CRIME AND PUNISHMENT.** Full crime and justice system for settlements. Eight offense categories (petty through capital), detection via hue and cry or investigation, judgment procedure with defense rolls by skill, compurgation (oath-helping), four trials by ordeal, sentencing table (stocks through execution), weregild blood-price schedule, imprisonment and escape rules, outlawry mechanics, defending others in court, bringing charges against NPCs, temple sanctuary, corruption and bribery.
- **Chapter 14 — Appendix D: Traderoads of the Forbidden Lands.** Self-contained caravan economics module. Seven transport options, 60+ individually priced goods across seven cargo categories, supply tiers defined inline, settlement trade profiles, market MANIPULATION roll, D66 hazard table, Caravan Circle reputation, seasonal pricing, PATH OF THE CARAVAN integration, WAREHOUSE stronghold function (200 wood + 100 stone), and a one-roll simple shortcut.
- **Chapter 14 — Caravan Mishaps (failed rolls).** Added a D66 mishap table for failed caravan procedure rolls that show ☠️, with severity bands for 1, 2, and 3+ ☠️.

### Changed

- **Chapter 10 — Villages and Towns.** Town history and oddity tables grounded further in post-apocalypse settlement life. Replaced whimsical or literary entries with feud, levy, hunger, road loss, plague, Rust Brother pressure, refugee flow, and trade recovery.
- **Chapter 10 — Villages and Towns.** Unified the inherited settlement-generation prose, paragraph rhythm, headings, and table terminology with the Gamemaster's Guide voice through the characters, situations, vicissitudes, and settlement play sections.
- **Chapter 10 — Settlement Play.** Rewritten in the Gamemaster's Guide voice and structure, with clearer compatibility notes for Book 01 journey village rules and optional pointcrawl route-link use.
- **Chapter 07 — Discipline count.** Updated to 17; sorcery paths rise to 8 with Demonic Magic.
- **Chapter 07 — Learning Magic.** Four named rules added: MAGICAL TALENT RANKS, FREE SPELLS, LEARNING ADDITIONAL SPELLS, EXPANDED TALENT ACCESS.
- **Chapter 07 — Elemental Magic: Elemental Environment.** Two-tier PL bonus for casting near strong (+1) or overwhelming (+2) natural sources of the relevant element.
- **Chapter 07 — Blood Magic: Blood Rot.** Blood ingredients must be drawn from a living source within the last two quarter days.
- **Chapter 07 — Mentalism: Influence.** Word and gesture replace physical ingredients; same +1 PL bonus.
- **Chapter 07 — Symbolism: Inscribed Symbols.** Symbols can be inscribed on surfaces and triggered by a set condition rather than cast immediately.
- **Chapter 07 — Stone Song: Instruments.** Instruments are not consumed on use.
- **Lifepaths — Muster-out draws.** Count equals turns completed in final path; choose best result.
- **Lifepaths — Advancement benefits draws.** Tiered: 1 success = 1 draw; 2 = 2 draws; 3+ = 2 draws plus free pick from remaining four.
- **Lifepaths — Mishap result 7.** Universal catastrophic result on all 12 mishap tables. Forces path change; two consequences; no permanent stat damage.
- **Lifepaths — "The fiction" language.** Replaced throughout Lifepaths with "the story."
- **Mercenaries — Finding Men.** Recruit pool table by location, quality distribution table (Common/Veteran/Elite) with TRAINING GROUNDS modifiers. Hard building requirements removed.
- **Chapter 14 — Traderoad cadence and standing orders.** Clarified that seasons are the market clock while caravan runs resolve in days/weeks; added route-length guidance for expected runs per season; standing orders now remain valid through the end of the following season.

## [1.0.5] - 2026-04-10

### Added

- Added Appendix C: Lifepaths of the Forbidden Lands (`13-lifepaths-of-the-forbidden-lands.md`) — a full cycle-based life path generator that replaces the simple backstory tables with a detailed character history system. Produces characters of the same mechanical power as the standard method, with deeper fiction, scars, contacts, and old debts.
  - **Life generator framework.** Cycle-and-turn structure where each cycle represents years in a single way of life. Young characters resolve 2 cycles (6 turns), Adults 3 (10 turns), Old 4 (14 turns). Each turn produces exactly one skill mark via a pass/fail turn test.
  - **Three play modes.** Full Random (roll everything), Guided Random (choose paths, roll events), and Full Guided (choose paths, roll two events per turn, pick one).
  - **Childhood foundations.** Ten kin-specific tables (Alderlander, Ailander, Aslene, Half-Elf, Halfling, Dwarf, Elf, Goblin, Orc, Wolfkin) each with six backgrounds granting 2 starting skills, favored attributes, a narrative hook, and a profession affinity.
  - **Eight profession paths.** Druid, Fighter, Hunter, Minstrel, Peddler, Rider, Rogue, and Sorcerer — each with a turn test skill, normal and hard-lesson skill lists, four turn-event tables (one per turn), a mishap table, a mustering-out table, and advancement benefits.
  - **Four crisis paths.** Captive, Drifter, Laborer, and Outcast — entered through the forced-departure table when a character fails advancement and has no voluntary options. Same full table structure as profession paths but representing years of hardship rather than chosen work.
  - **Skill ranks and marks.** Marks-to-ranks progression table (1→R1, 2→R2, 3→R3, 5→R4, 7→R5) shared with talent advancement. Prevents runaway specialization while rewarding sustained focus.
  - **Thresholds.** Entry gates for certain profession paths requiring minimum skill ranks (e.g., Sorcerer requires Lore 2, Fighter requires Melee 1). Crisis paths have no thresholds.
  - **Advancement and departure.** End-of-cycle roll determining whether the character stays on the current path, departs voluntarily, or is forced out. Forced departure triggers the crisis path system.
  - **Narrowing tax.** Repeating a path applies -1 to turn tests and +1 to mishaps. Mechanically discourages grinding a single path while allowing dedicated careers.
  - **Wear system.** Tracks consecutive failures within the same cycle. Wear tiers (0–1, 2–3, 4+) weight the character's unfinished business — higher Wear means heavier fictional debts.
  - **Pride and Dark Secret tags.** Certain events carry "This may be your Pride" or "This may be your Dark Secret" tags, giving players the option to claim them during generation rather than choosing from a list.
  - **Unfinished business.** Post-generation narrative hook framed as an unanswered question. Short Errands (10 XP) resolve in one to three sessions; Life Quests (25 XP) may span a campaign. Wear determines available weight.
  - **Starting gear floor.** Ensures no character enters play unarmed and broke. Fills gaps in weapon, armor (Fighter: studded leather), mount (Rider), instrument (Minstrel), silver, waterskin, and backpack based on chosen profession's standard starting gear.
  - **Profession integration.** Qualification rules route the character's final path into a Chapter 2 profession. Profession talent seed grants 1 mark in the chosen profession talent. Spell access for Sorcerers and Druids follows Chapter 7 rules at the granted rank.
  - **Reputation and Standing.** Characters start with Reputation 6 and Standing +1 in their home settlement, modified by any Standing changes gained during the life generator.
  - **Worked examples.** Two complete walkthroughs — Jorrh (Adult human Fighter via Drifter crisis) and Torvin (Old Dwarf Peddler via Captive crisis) — demonstrating full generation from childhood through profession selection.
  - **How Did You Meet? table.** Shared table for linking characters at the end of generation.

### Changed

- Replaced the old coup de grâce rule in Chapter 5 with a four-tier killing system based on situation rather than kin.
  - **Broken by a pushed attack:** The target dies. No choice. Applies only to PCs pushing attacks against NPCs — NPCs who push attacks that break PCs break them normally, not kill them.
  - **Killing blow in active combat:** A slow action against a broken enemy while the fight continues. No roll required; the cost is action economy.
  - **Coup de grâce after combat:** Killing a defenseless intelligent being once combat ends costs 1 WP. No Empathy roll required.
  - **Killing the helpless:** Slaying a non-combatant (elder, child, surrendered prisoner) requires failing an Empathy roll, spending 1 WP, and suffering 1 Empathy damage. If the roll succeeds, the character cannot bring themselves to do it.
  - Creatures without Wits (animals, monsters, undead) are exempt from all tiers.
- Updated the Cold-Blooded talent in Chapter 4 to map onto the new tiers. Rank 1 removes the WP cost for post-combat coup de grâce. Rank 2 bypasses the Empathy roll, WP, and Empathy damage for killing helpless non-combatants. Ranks 3–5 updated to reference both killing blows and coup de grâce.
- Converted Horrifying Monsters attack lists in Chapter 11 from numbered prose to `D6 / Attack / Effect` tables for each of the four monsters (Giant Serpent, Feral Ape, Enormous Spider, Forgotten God). Fixed typo OTHERWORDLY → OTHERWORLDLY on the Forgotten God.

## [1.0.4] - 2026-04-07

### Added

- Added seasonal HUNT modifiers to the Seasons table in Chapter 8: Spring -2, Summer -1, Autumn +1, Winter 0.
- Added weather modifiers for HUNT in Chapter 8 when using expanded weather rules: Strong Wind -1, Drizzle -1, Downpour -2, Storm (impossible), active snowfall +1 to finding prey, clear winter skies +1. All stack with season and terrain.
- Replaced the animal table in Chapter 8: Squirrel, Game birds, Hare, Fox, Boar, Deer. Corrected difficulties, yields, and requirements. Game birds become waterfowl in Marshlands or near water.
- Added temperature-sensitive meat spoilage rule in Chapter 8 tied to the HEAT system. Summer heat spoils MEAT the same Quarter Day; winter cold preserves it for D3 days. CHEF roll extends by one day.
- Changed Marshlands HUNT modifier from -1 to +1 in the terrain table, the in-text modifier list, and the terrain description. Marshlands are productive hunting ground, not poor.

### Changed

- Revised `MASTER OF THE HUNT` ranks 1, 2, and 4 in Chapter 4. Rank 1 adds animal-sign reading while hiking at no Quarter Day cost. Rank 2 adds absent trap monitoring on top of REST equivalence. Rank 4 replaced extra-animals mechanic with wounded-game tracking (additional Quarter Day, SURVIVAL at -1).
- Removed duplicate extortion vignette from Chapter 12 Part 3. Kept Yellowdew; removed Redrun as a redundant variation of the same scene.

## [1.0.3] - 2026-04-07

### Added

- Added Chapter 12: Mercenaries of the Forbidden Lands — a full mercenary band system built on the existing Quarter Day structure, Settlement Reputation, and resource mechanics. Covers band formation, pay, provisioning, contracts, Named Men, hired casters, and multi-band Host play.
  - **Band structure.** Size tiers (Skirmisher through Legion), band archetypes (Rural Mob, Tyrant Band, Military Squad, Kin Clan) with per-archetype recruitment modifiers and MORALE consequences.
  - **Recruitment.** Settlement-based recruitment rolls with kin modifiers, Advance Payment rules, and fighter quality tiers (Common, Veteran, Elite) with stats and salary rates.
  - **Pay model.** Retainer and mission pay rates by fighter type, field non-payment rules and consequences, loot share division by band archetype, and WINDFALL event table.
  - **Provisioning.** Daily forager output table by terrain and party size. Ransom rules for captives of value by tier.
  - **MORALE system.** A 1–5 band score with automatic Trigger events, GRIEVANCE difficulty table, voluntary check procedure, stacking and escalation rules, and worked examples.
  - **Contracts.** Posting board mechanics, public and private contract access, MANIPULATION-based negotiation, binding contract terms, mid-contract breach rules, in-kind payment table with goods values and guarantor requirements.
  - **Bounty work.** Bounty posting rules, collector mechanics, goods-denominated bounties, and cold-clock reset conditions.
  - **Extortion and tribute.** Tribute demand rules, hostile quartering, and Standing and REPUTATION consequences for atrocities.
  - **Campaign life.** Punishment procedures, Fear-Held and Trust-Held band distinctions, Argument and Escalation mechanics (Stages 1–4), occupation and territory holding, and Captain Succession rules.
  - **Named Men.** Individual veteran fighters with Role-based stat blocks, Loyalty (1–3), Triggers, and Agendas. Sergeant rules, Promotion from Hireling procedure, and Second Triggers for Named Men with a full year of service.
  - **Hired casters.** Three tiers — Initiate, Adept, Master — with Willpower pools, discipline restrictions, camp-use limits, and Caster Loyalty mechanics including coin-vs-Agenda commitment and tier-specific departure behavior.
  - **Special rules.** Pillage and REPUTATION consequences, kidnapping contracts, mercenary hoards, blood oath mechanics, atrocity handling, and War Room stronghold rules.
  - **Host play.** Multi-band Hosts under a Warmaster: per-band MORALE and Named Men tracking, Ledger authority score (−6 to +6), treasury and band budget rules, Warmaster's Share and Bonus Allocation mechanics, rival dynamics, inter-band communication, Host Council voting, and dissolution procedures.
  - **Serving under another captain.** Rank progression from FRESH to FIRST BLADE, Call Name mechanics, order disagreement and mutiny thresholds.
  - **Appendix A: Meet the Band.** Ten pregenerated characters built on standard creation rules from Chapter 2, with full stat blocks, Prides, Dark Secrets, and relationships.
  - **Appendix B: Premade bands.** Three ready-to-use bands with full rosters, Reputations, Agendas, and field histories.
  - **Band Life vignettes.** Thirty-three short prose pieces illustrating mechanics in play, one per named rule area, following the Gristle's company.

## [1.0.2] - 2026-04-06

### Added

- Introduced the new local Reputation system and writing skill guidance, including hometown starting Reputation, first-impression trigger rules, Reputation growth scaling, and a new onboarding reference for complex rule chapters.
- Added `Makeshift Tools` as a common adventuring resource item in Chapter 10, tracked with a `D8` Resource Die for hard field use such as digging, prying, and rough repairs, with penalties when it replaces proper hand tools. Clarified in Chapter 2 that some expedition gear may also be tracked with a Resource Die when hard use wears it down.
- Added clear close-combat range bands with `CUT IN / BACK`, plus the new combat options `BRACE`, `HOLD FAST`, `LOCK SHIELDS`, and a one-immediate-attack limit outside your turn.
- Added the general talents `INSIDE THE GUARD` and `KEEP THEM OUT` in Chapter 4 for fighters who either slip inside longer weapons or hold enemies at reach.
- Added the new weapon features `HALF-HAND`, `FLEXIBLE`, and `SMASHING`, with weapon-specific limits and reach handling.
- Added optional NPC morale and rout rules with morale dice, fear breaks, trapped-fighter fear penalties, and a delay before the next check.
- Added monster reach handling, including passive `LONG-REACH` for large monsters and reach listed on monster attacks.
- Added Chapter 6 guidance for retiring a crippled but surviving adventurer with dignity, including the option to remain with the company as a follower or retainer NPC under the existing `1 XP` per session retainer rule.
- Added the new acid/corrosion, cold/freeze, and swallow injury tables in Chapter 6, with permanent injury subtables placed directly after their matching critical injury tables.
- Added a separate General Spells mishap table in Chapter 7 with path-based mishap routing for each magical discipline.

### Changed

- Updated `INTERCEPT` to fit the new ready-action model.
- Clarified polearm and spear handling so haft weapons, spears, and inside-range fallback attacks each have a distinct role.
- Revised many Chapter 6 critical injury labels to better match their actual recovery times while keeping the same mechanics, and rewrote several horror trauma names to fit the harsher low-tech tone of the setting.
- Reworked Chapter 6 physical critical injuries so `65` now represents a survivable catastrophe rather than automatic death, and clarified how `LUCKY`, `PHYSICIAN`, `MEND WOUNDS`, and `REGENERATION` interact with lasting bodily ruin.
- Restructured Chapter 7 mishaps so each magical path has its own integrated mishap table, and rebalanced severity bands.
- Rebalanced ranged weapon table in Chapter 5: `Throwing Axe`, all three bows, `Blowgun`, and all three crossbows each lose one Gear Die of bonus; `Light Crossbow` range extended from Short to Long. `Composite Bow` entry in Chapter 10 corrected to reflect the new Short Bow baseline.

### Removed

## [1.0.1] - 2026-02-18

### Added

- Initial release of the complete homebrewed corebook
- Optional rule `Surge of Willpower`: allow conversion of unspent XP into Willpower (1 XP → 1 WP), once per session at GM discretion — added to Chapter 3 (`WILLPOWER`)

### Changed

### Removed
