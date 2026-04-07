<!-- markdownlint-disable MD013 MD024 -->

# Changelog

All notable changes to the Forbidden Lands Corebook will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2026-04-07

### Added

- **Chapter 12: Mercenaries of the Forbidden Lands** — a full mercenary band system for any fellowship captain, warchief, or hard-eyed pragmatist who needs twenty swords pointed at the right problem and enough coin to keep them there. Built on existing Quarter Day structure, Settlement Reputation, and resource mechanics, with no independent subsystems bolted on the side.
  - **Raise a band from nothing.** The hireling-vs-mercenary distinction, advance payment, the verbal non-ceremony of signing a new man, and what it means when he takes the coin.
  - **Pay it or don't.** Weekly retainer, loot-share split by tier and time served, and the complete mechanics of field non-payment — what the men's faces look like by the second morning, and what they start calculating.
  - **Contracts and the board.** Posting boards, binding contract terms, mid-job bad surprises, hoard-clearing jobs with proof-of-elimination clauses, and the specific line in every employer's paperwork a careful captain scratches out.
  - **Bounty work.** Taking a bounty contract, delivering a man alive and standing, the rate for discretion, and the colder question of what the employer does with him after delivery.
  - **Extortion and tribute.** Take what the band needs by negotiation, by quartering, or by being the only swords within three days' ride. Rules for tribute demands, hostile quartering, and the Reputation cost of burning what is not yours and not covered by the contract.
  - **Named Men.** Individual veteran fighters with stat blocks, Loyalty scores (what keeps them), Triggers (what breaks them), and Agendas (what they are actually in this for). They hold the line because the coin is right. They also remember every order you gave at the farmstead.
  - **Promotion from hireling.** A GUARD who has survived two engagements can be assessed, promoted to Named Man, and put on the roster at Named Man rates. Rules for the downtime process and what they bring to the role.
  - **Second Triggers.** A Named Man with a full year of active contracts behind him can carry a second Trigger. Both fire independently. A man with that many breaking points is expensive and unreliable. Some captains keep them anyway.
  - **Morale.** A MORALE die that falls with missed payments, routs, atrocities, and things the men saw that you told them not to talk about. Grievances that spread through a column like fever. The mechanics of a band that has decided it is done.
  - **Hired casters.** Three tiers — Initiate, Adept, Master — each with Willpower pools, discipline lists, restrictions on camp use, and the Caster Loyalty system: what it takes to hold a sorcerer on contract, what it looks like when their second Trigger fires in the same season, and how a Master leaves when they decide to go.
  - **Special rules.** Pillage and the Reputation wreckage that outlasts the fires. Kidnapping contracts (_retrieval_, the middleman calls it). Mercenary hoards buried at split-boulder boulders in forests with no names. Blood oaths, because sometimes words are not enough. What the band does when the captain orders something nobody can live with afterward.
  - **Host play.** Multi-band Hosts under a Warmaster: the Ledger system that tracks authority and trust, treasury allocation rules, band budget management, the Warmaster's share (which defers before band pay or costs Ledger), inter-band bonus favoritism with its MANIPULATION mechanics and GRIEVANCE consequences, and the Host Council — how captains vote on whether the Warmaster keeps the chair.
  - **Serving under another captain.** Rules for a PC riding as a Named Man inside an existing band: rank progression from FRESH to FIRST BLADE, Call Names earned through play (the crew shortens a deed to one word and it sticks), disagreeing with orders, and where the line between insubordination and mutiny actually runs.
  - **The band, charted.** Size tiers from Skirmisher (3–6) to Legion (200+), MORALE thresholds by tier, Named Men guidelines, and cost-of-upkeep math that scales with the contract income your band can realistically generate.
  - **Meet the Band.** Ten fully statted pregenerated characters — the Gristle's company — built on standard creation rules from Chapter 2. Every one of them has a Pride, a dark secret, and a reason they are still doing this that they will not say aloud. All ten are available as player characters, hireable Named Men, or vignette reference.
  - **Premade bands.** Three ready-to-use bands with full rosters, Reputations, Agendas, and field histories. Install them in any campaign as employers, rivals, or the warband three contracts ahead of you on the same job.
  - **Band Life vignettes.** Thirty three short prose pieces — in the chapter voice, named for mechanics — that walk one company from recruiting through contract, pay day, short pay, punishment, a blood oath, a kidnapping job, a bounty take, and the arithmetic of burying a man's kit. Reference material for what the rules actually feel like when the fiction is running.

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
