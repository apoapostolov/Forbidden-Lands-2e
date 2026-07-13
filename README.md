# Forbidden Lands 2E

<div style="display: flex; width: 90%; gap: 1%; align-items: flex-start;">
  <img src="01-corebook/00-cover.png" alt="Forbidden Lands 2E corebook cover" style="display: block; width: 31%; max-width: 31%; min-width: 0; height: auto;">
  <img src="02-gamemasters-guide/00-cover.png" alt="Forbidden Lands 2E Gamemaster's Guide cover" style="display: block; width: 31%; max-width: 31%; min-width: 0; height: auto;">
  <img src="03-book-of-beasts/00-cover.png" alt="Forbidden Lands 2E Book of Beasts cover" style="display: block; width: 31%; max-width: 31%; min-width: 0; height: auto;">
</div>

Apostol Apostolov's completed *Forbidden Lands* 2nd Edition magnum opus: an unofficial three-book overhaul built for harsher journeys, stronger campaign play, deeper setting support, and better tools at the table.

This is not an official Free League release. It is a finished fan-made manuscript set and companion toolkit for groups who want to run, expand, and build on *Forbidden Lands* with serious intent.

## What is in this repository

- `01-corebook/` — the complete player-facing core rules
- `02-gamemasters-guide/` — the campaign, settlement, faction, and war-facing referee book
- `03-book-of-beasts/` — the expanded monster, encounter, and legend book
- `skills/forbidden-lands-*` — repo-owned AI and GM copilot skills for building new material in the same game line
- `CHANGELOG.md` — the version-by-version development record
- `LICENSE.md` — the public rights and license notice for this repo

## The three books

### Book 01 — Corebook

The core rules now stand as a complete campaign book rather than a thin adventuring chassis. Character creation, talents, combat, injuries, magic, journeys, strongholds, gear, heroic reference play, mercenaries, traderoads, and lifepaths all live in one integrated volume.

### Book 02 — Gamemaster's Guide

The Gamemaster's Guide turns the setting into a working campaign engine. It covers history, gods, kin, bestiary support, artifacts, encounters, adventure sites, villages, politics, and battles and sieges with enough procedure to run long-form play instead of handwaving the hard parts.

### Book 03 — Book of Beasts

The Book of Beasts is no longer just a creature list. It is a creature, encounter, and legend book built to make the wilderness stranger, meaner, and more usable in play, with monsters that carry story hooks and table consequences instead of filling space.

## What this edition brings

From `1.0.0` through `1.1.0`, this edition adds the best of the best additions that turn the project into a full second-edition line:

- A complete three-book manuscript set: Corebook, Gamemaster's Guide, and Book of Beasts.
- Optional Linked Rolls for carrying exceptional or failed results forward through complex plans and coordinated actions.
- Clear party procedures for stealth, surprise, and chases, with better-defined result quality and modifiers.
- A bundled *Forbidden Lands* skill suite for AI and Game Master coworking.
- A larger bestiary with new monsters, humanoid enemy bands, encounters, legends, and salvage.
- Full faction play and political campaign rules with territory, pressure, recovery, and long-term consequences.
- A mass combat system for wars, field battles, sieges, blockade, breach, and relief.
- A deep settlement game with villages, towns, jobs, petitions, carousing, rumor, and civic pressure.
- A crime and punishment chapter with investigation, ordeals, sentencing, weregild, sanctuary, and outlawry.
- A traderoad and caravan economy with cargo, markets, hazards, and route play.
- A mercenary company system covering bands, Named Men, contracts, loyalty, camp life, and multi-band Hosts.
- A lifepath generator that replaces thin backstory with a full pre-campaign life system.
- A seventeenth magical discipline, Demonic Magic, plus new spells across the wider magic engine.
- Path-based magical mishaps and broader magic integration clean-up.
- Expanded tactical combat with cut-in range play, brace options, shield pressure, morale, and monster reach.
- New general talents and weapon features that give polearms, shields, and spacing clearer jobs.
- Reworked critical injuries, added acid, cold, and swallow injuries, and clearer survival-after-maiming support.
- A local Reputation model that ties adventurers to settlements and first impressions.
- A harsher, more grounded hunting, weather, season, and spoilage pass for wilderness play.
- Stronger human-peoples chapters with clearer cultural, visual, and social differences.
- Better encounter, artifact, and adventure-site support folded into the Gamemaster's Guide where campaign play needs it.
- A cleaner route from crippling injury to retirement, retention, or NPC afterlife in the campaign.

## AI and campaign work

This repository is built so a GM, designer, or AI agent can do more than read it. The `forbidden-lands-*` skills are meant to help you understand the line, create new material in the same register, and keep your own campaign repository consistent.

### Install the Forbidden Lands skills in another repository

If your agent supports repo-local skills, copy or symlink the desired folders from this repository's `skills/` directory into your own local skill path.

Common workspace-local destinations are:

- `.github/skills/` for repo-scoped shared use
- `.agents/skills/` for repo-scoped agent workflows

Keep the folder names and each `SKILL.md` entry point intact.

Only carry over the *Forbidden Lands* skills you actually need:

- `forbidden-lands-bestiary`
- `forbidden-lands-design`
- `forbidden-lands-lore`
- `forbidden-lands-medieval-authenticity`
- `forbidden-lands-synergy-analysis`
- `forbidden-lands-writing-voice`
- `yze-design`

### What each skill is for

| Skill | Use it for |
| --- | --- |
| `yze-design` | Build a new Year Zero Engine game for any genre; invent, transplant, and stress-validate mechanics from proven YZE primitives |
| `forbidden-lands-bestiary` | New monsters, encounter tables, Lore Rolls, Monster Attacks, and salvage design |
| `forbidden-lands-design` | New rules, subsystems, procedures, and campaign mechanics |
| `forbidden-lands-lore` | Setting truth, place names, kin, factions, religion, and regional consistency |
| `forbidden-lands-medieval-authenticity` | Camp life, survival work, barter, bodily strain, and Bitter Reach material reality |
| `forbidden-lands-synergy-analysis` | Balance stress-testing, dominant combos, loopholes, and exploit surfaces |
| `forbidden-lands-writing-voice` | Final prose, rules voice, examples, flavor, and manuscript register |

### Recommended skill stacks

- **New YZE game for any genre:** `yze-design`
- **New region or campaign frame:** `forbidden-lands-lore`, `forbidden-lands-writing-voice`, and `forbidden-lands-medieval-authenticity`
- **New subsystem or house rule:** `forbidden-lands-design` and `forbidden-lands-synergy-analysis`
- **New monster or enemy band:** `forbidden-lands-bestiary`, `forbidden-lands-lore`, and `forbidden-lands-medieval-authenticity`
- **Campaign handouts and local color:** `forbidden-lands-writing-voice` and `forbidden-lands-lore`

### Set up a local campaign repository

If you want a clean local campaign workspace, a simple structure like this is enough:

```text
my-forbidden-lands-campaign/
├── README.md
├── 01-region-overview/
├── 02-settlements/
├── 03-factions/
├── 04-adventure-sites/
├── 05-npcs-and-monsters/
├── 06-session-prep/
├── 07-session-logs/
├── 08-house-rules/
├── 09-rumors-legends-hooks/
└── .github/skills/
    ├── forbidden-lands-bestiary/
    ├── forbidden-lands-design/
    ├── forbidden-lands-lore/
    ├── forbidden-lands-medieval-authenticity/
    ├── forbidden-lands-synergy-analysis/
    ├── forbidden-lands-writing-voice/
    └── yze-design/
```

That gives a GM a practical split between world facts, active prep, session history, and house material.

Useful workflow:

1. Keep regional truth, factions, and place names in the campaign repo.
2. Use `forbidden-lands-lore` to stop continuity drift.
3. Use `forbidden-lands-design` before committing a new rule or subsystem.
4. Use `forbidden-lands-bestiary` when a location needs new creatures, salvage, or wilderness pressure.
5. Use `forbidden-lands-writing-voice` and `forbidden-lands-medieval-authenticity` for letters, rumors, village color, legends, expedition notes, and Bitter Reach material.
6. Track campaign changes in your own changelog so setting drift stays visible.

## Back matter and support files

The repository also includes the root support documents that make the line usable as a working reference:

- `CHANGELOG.md` for the development record from `1.0.0` to `1.1.0`
- `LICENSE.md` for the legal and rights framing of this unofficial repo
- Front matter and cover files for all three books
- Encounter, legend, and reference chapters integrated into the books themselves rather than parked in loose working notes

## License and notice

Free League published the official [Forbidden Lands Third-Party Tabletop Module License v1.0, dated March 31, 2026](https://freeleaguepublishing.com/wp-content/uploads/2026/03/Forbidden-Lands-License-Agreement-version-1.0.pdf).

If you intend to publish, sell, or distribute material derived from this repository, read that license first and then read `LICENSE.md` in this repository.

This project is not affiliated with, sponsored by, or endorsed by Fria Ligan AB / Free League.
