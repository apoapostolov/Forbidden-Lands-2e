<!-- markdownlint-disable MD013 MD024 -->

# Changelog

All notable changes to the Forbidden Lands Corebook will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.5] - 2026-04-09

### Changed

- Replaced the old coup de grâce rule in Chapter 5 with a four-tier killing system based on situation rather than kin.
  - **Broken by a pushed attack:** The target dies. No choice. Applies only to PCs pushing attacks against NPCs — NPCs who push attacks that break PCs break them normally, not kill them.
  - **Killing blow in active combat:** A slow action against a broken enemy while the fight continues. No roll required; the cost is action economy.
  - **Coup de grâce after combat:** Killing a defenseless intelligent being once combat ends costs 1 WP. No Empathy roll required.
  - **Killing the helpless:** Slaying a non-combatant (elder, child, surrendered prisoner) requires failing an Empathy roll, spending 1 WP, and suffering 1 Empathy damage. If the roll succeeds, the character cannot bring themselves to do it.
  - Creatures without Wits (animals, monsters, undead) are exempt from all tiers.
- Updated the Cold-Blooded talent in Chapter 4 to map onto the new tiers. Rank 1 removes the WP cost for post-combat coup de grâce. Rank 2 bypasses the Empathy roll, WP, and Empathy damage for killing helpless non-combatants. Ranks 3–5 updated to reference both killing blows and coup de grâce.

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
