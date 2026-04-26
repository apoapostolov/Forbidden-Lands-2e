---
name: forbidden-lands-lore
description: |
  Use when checking, auditing, or enforcing Forbidden Lands setting
  authenticity, and when classifying tone or designing encounters
  for the Forbidden Lands 2E manuscript. Covers geography, the three
  human peoples, non-human kin, magic paths, the full pantheon and
  religious orders, the canonical chronology and named historical
  figures, the bestiary lore (origin myths, ecology, encounter
  shapes), the canonical artifacts, and the village-as-system model
  (The Hollows reference, Heat and Need, named geography). Also the
  authority for genre register: re-feudal medieval survival fantasy
  with Swedish tone, realistic village authenticity, soft
  Tolkienesque worldbuilding, and the encounter anti-trope catalog.
  Load this skill whenever writing or reviewing prose that involves
  place names, character nationality, kin identity, cultural detail,
  monster lore, religious factions, artifacts, named NPCs, village
  texture, or any fact claim about the Ravenlands setting. Also use
  when auditing existing text for setting errors, anachronisms,
  basic-fantasy tropes, or wrong-register tone.
---

# Forbidden Lands Lore

This skill is the setting-authenticity authority for the Forbidden
Lands 2E repo. It ensures that every proper noun, cultural detail,
geographic reference, kin trait, and world-state claim in the
manuscript is consistent with established canon and approved
author decisions.

## When To Load This Skill

- Writing or revising fiction that names places, peoples, or kin
- Auditing existing prose for setting errors
- Creating new characters with nationality or kin identity
- Checking whether a place name is canonical or invented
- Verifying magic path details or religious faction references
- Any task where the `forbidden-lands-writing` skill says
  "load the setting reference"

## Bundled References

- `references/setting.md`
  The master setting document. Contains:
  - World state (post-Blood Mist, broken infrastructure)
  - Religion (Raven Church, Congregation, Rust Brothers) — quick form
  - Currency (silver, no mines, old Alder War coins)
  - Geography table (canonical and manuscript-canon locations)
  - The three human peoples with approved physical types
  - Non-human kin table (8 kin with physical and cultural tells)
  - Dwarf and half-elf cultural details
  - Magic system notes (15 paths)
  - Writing rules for human nationality in prose
  - Proper noun appendix

- `references/tone.md`
  The genre-register and encounter-authenticity authority. Contains:
  - Genre Classification: re-feudal medieval survival fantasy with
    Swedish tone, realistic village authenticity, soft Tolkienesque
    poetic worldbuilding (each clause defined as a constraint)
  - What Forbidden Lands Is Not (failure modes)
  - Encounter Anti-Trope Catalog (7 anti-tropes with in-world
    reasons, paired to the 7 encounter shapes in the bestiary skill)
  - Vignette and Novella Register (sensory anchors, voice anchors,
    plot anchors)

- `references/history.md`
  Calendar (8 phases and named festivals), full chronology from the
  Mythic Past to 1165 AS, named historical figures index (~32
  entries), guidance on referencing dates in prose.

- `references/gods.md`
  The full pantheon: the Protector under three faces (Wyrm/Raven/
  Rust), Reapenters, Sisters of Heme, Vampyr heresy, the Older
  Gods (Huge, Clay, Wail, Flow, Nightwalker, Horn, Eor, Red
  Wanderer), other powers (Shardmaiden, Golden Bough, Order of
  the Silent, Stone Singers, Maha language). Reference NPC
  statblocks for each major religious order. Faction distribution
  by region.

- `references/kin.md`
  Cultural depth on every kin: clan names, governance, customs,
  named individuals, statblock anchors. Humans (Alderlanders,
  Ailanders, Frailers, The Silent, Aslenes, Quards, Galdanes),
  Elvenspring, Misgrown, Elves (Stillelves, Unruly, Ents, Melders,
  Watchers, Redrunners), Dwarves (Belderranian, Meromannian,
  Canide, Crombe, Dwelvers), Ogres, Orcs (Urhur, Roka, Isir,
  Viraga, Drifters), Wolfkin, Saurians, Whiners, Halflings,
  Goblins.

- `references/bestiary.md`
  Lore for every named creature: origin myth, ecology, cultural
  integration, named individuals (Erinya, Menkaura, Krasjika),
  folk warnings, encounter-shape anchors. Includes the lore-rule:
  _A monster is a contract the village has been keeping, and the
  contract is now breaking._ Pair with the bestiary skill for
  encounter mechanics.

- `references/artifacts.md`
  Every named artifact: myth-as-told, truth-behind-myth,
  mechanical hint, current location/holder. Asina, Barkhyde,
  Carskenfoot's Boots, Clay's Rosary, Feroxa's Claws, Ivelde,
  Menkaura's Tooth, Phantom Daggers, Queen Agatha's Twin Tablets,
  Scarnesbane, Scarnesclaw, Nightwalker's Hourglass, Tezaur,
  Tvedra's Twin Rings, Voller's Helmet, Wail's Horn, Well of
  Tears, Wyrm's Key, Arrow of the Fire Wyrm. Campaign artifacts
  (public legend only, true powers in campaign file):
  Stanengist, Maligarn, Nekhaka, Blood Star (Hemella).

- `references/places.md`
  The village-as-system model (seven components), The Hollows
  full reference (template for village authenticity), Heat and
  Need lore-side, settlement archetypes, named geography master
  index covering all manuscript regions. Includes Raven's Purge
  adventure site locations (Vond, Eye of the Rose, Pelagia,
  Stoneloom Mines, Haggler's House, Ravenhole, Grindbone).

## Campaign Files

Bundled campaign references live in `campaigns/`. Each campaign
file contains both **non-spoiler** public lore and a
**SPOILER SECTION** with plot secrets, NPC true agendas,
artifact powers, and outcome paths.

- `campaigns/ravens_purge.md`
  Full reference for the **Raven's Purge** campaign by Erik
  Granström. Scope: entirely within the core Ravenlands.
  Central conflict: Stanengist (the elven crown) and who controls
  the Forbidden Lands after the Blood Mist. Covers all key
  players (Zytera, Merigall, Krasylla, Zertorme, Arvia, Soria,
  Kalman Rodenfell, Kartorda), all adventure sites (Grindbone,
  Ravenhole, Amber's Peak, Eye of the Rose, Pelagia, Stonegarden,
  Stoneloom Mines, Haggler's House, Vond), all four campaign
  artifacts, and the full range of campaign outcomes.

### Spoiler Handling Protocol

**Before reading any section marked ⚠️ SPOILER or SPOILER SECTION
in a campaign file, stop and ask the user:**

> *"This content contains major campaign spoilers for [Campaign
> Name]. Do you want me to proceed with spoiler content?"*

Wait for explicit confirmation before continuing. This applies
to:
- True natures and secret agendas of named NPCs
- Artifact full powers and true histories
- Adventure site secrets and dungeon contents
- Plot twist reveals and campaign outcome paths

Non-spoiler content (public legends, location descriptions,
faction structures, geography) can be shared freely without
asking.

## Expansion Regions

An expansion region is a neighboring country with its own kin,
geography, religions, magic traditions, terrain rules, and
creatures. Its content is **entirely self-contained** in its
own campaign file — nothing from an expansion region merges
into the `/references/` files. This is because most Forbidden
Lands stories do not involve these regions; loading expansion
content by default would pollute the core world reference.

**Loading rule:** Load an expansion region file only when the
user explicitly asks about that region, its creatures, its kin,
or its campaign. Do not load it for general Forbidden Lands
queries, Ravenlands lore checks, or Raven's Purge questions.

**Spoiler rule:** Expansion region spoilers follow the same
protocol as campaign spoilers above. Ask before reading any
section marked ⚠️ SPOILER.

- `campaigns/bloodmarch.md`
  Full reference for **The Bloodmarch** (Aslene) by Erik
  Granström. Scope: entirely new region west of Ravenland.
  New kin (horse clans, Vasnians, Caprids, red elves, moon elves,
  grargs), new terrain types (Ashlands, Firelands, Crimson
  Forest), new magic traditions (Magma Song, Mentalism,
  Oneiromancy, Magnetism), new creatures, new gods. Campaign:
  **Legacy of Horn** — competing factions race to collect five
  sacred Astra and determine who controls the Bloodmarch. Key
  players: Selligar Horne, Poansa Moulter, Colonel Grudenstaal,
  Fiena Fromelei, The Seventh, Vinhelm Kaal, Konana, Vaerefor
  Van Reiben, the Dreamstress, Octomadria. Access via Shadowgate
  Pass (opened after events of Raven's Purge).

- `skills/forbidden-lands-bestiary/SKILL.md` — encounter design
  mandate, the seven encounter shapes, the Resources mandate,
  statblock format. **Load alongside this skill** when writing
  any monster encounter or bestiary entry.
- `skills/forbidden-lands-writing/SKILL.md` — sentence-level prose
  technique and the Worldbuilding Voice section. **Load alongside
  this skill** when drafting manuscript or proposal prose.
- `skills/forbidden-lands-design/SKILL.md` — mechanics and rules
  integration.

## Playbooks

Operational workflows for expanding the skill live in `playbooks/`.

- `playbooks/integrate-region-source.md`
  Step-by-step protocol for absorbing a new sourcebook, regional
  supplement, or campaign module into the reference files. Covers
  the three-pass integration workflow (structural extraction, lore
  depth audit, small-detail texture pass), spoiler triage, campaign
  file creation, wiring, cross-reference audit, and multi-session
  handoff. Use this whenever a new source is being added.

## Hard Rules

1. **Canonical locations are not movable.** Weatherstone, Harga,
   Ravenford, Stillmire, Amber Peaks — these are fixed on the hex
   map. Do not relocate them or change their character.

2. **Manuscript-canon locations are flexible but consistent.**
   Hollowford, Ashfall, Blackwood, Greymark, Redrun, Yellowdew,
   Fen River — invented for the manuscript. Once placed, keep them
   consistent across all references.

3. **Human peoples have approved physical types.** Do not improvise
   new racial features. Use the approved anchors:
   - Alderlander = Icelandic/Swedish
   - Aslene = Arabic/Mongol mix (light-skinned, Mongol features)
   - Ailander = Slavic

4. **Kin traits are mechanical.** Dwarf True Grit, half-elf Psychic
   Power — these are game talents with specific effects. Do not
   embellish them into something they are not.

5. **Magic paths have rules.** Blood Magic works through blood and
   Willpower cost. Mentalism is political and invasive. Do not mix
   path effects or invent new ones without checking the reference.

6. **Show, never label.** One physical detail per character, at most.
   Do not name the culture directly in fiction prose. Let the reader
   assemble it.

7. **The Blood Mist is recent history.** Ten generations of isolation.
   The Mist lifted in 1160 AS; the manuscript "now" is 1165 AS.
   Infrastructure is broken. Settlements are suspicious. This is
   the baseline.

8. **The tonal register is fixed.** Re-feudal medieval survival
   fantasy with Swedish tone, realistic village authenticity, and
   soft Tolkienesque poetic worldbuilding. Each clause is a
   constraint — see `references/tone.md` for
   the definitions. Reject any draft that drifts toward generic
   high-fantasy, heroic-quest, or modern-comic register.

9. **Encounters refuse the seven anti-tropes.** Kill-the-monster,
   purge-the-undead, defeat-the-cultists, kill-the-bandits,
   mindless-orcs, good-faction-vs-bad-faction, find-the-artifact-win.
   Every monster encounter is a contract that the village has been
   keeping. Every undead is a confused dead or a wrong unanswered.
   Every faction is partly right. Every artifact carries a curse,
   a contested provenance, or a binding that was load-bearing
   somewhere. Pair with the seven approved encounter shapes in the
   bestiary skill.

10. **Named historical figures are mostly still alive.** Elves
    millennia, dwarves centuries, Death Knights and undead artifacts
    longer. Hroka, Archa, Karonax, Sulma, Tademir, Turik, Tormund,
    Zytera, Zygofer, Therania, Merigall, Krasylla, Zertorme,
    Badalar, Geno, Kartorda, Blaudewedd, Veliman, Teramalda — alive
    in 1165 AS. See `references/history.md`.

11. **Every village described in prose names at least three of its
    seven components in the first 200 words** — food source, water
    source, defense, shrine(s), burial place, authority, grudge
    structure. The Hollows is the template. See
    `references/places.md`.

## Audit Checklist

When auditing prose for setting authenticity, check:

- [ ] Place names match canonical or manuscript-canon list
- [ ] Human character descriptions match approved physical types
- [ ] Kin descriptions match the kin table and the deep-dive file
- [ ] Magic references match the correct path and mechanics
- [ ] Religious references use correct faction names; faction
      distribution is plausible for the region
- [ ] Currency references use silver (not gold, not "coins"
      generically); old Alder War coin is the prestige form
- [ ] World state reflects post-Blood Mist conditions (1165 AS,
      five years since the Mist lifted)
- [ ] No anachronisms (no banks, no courts, no postal service, no
      printed broadsheets, no hospitals)
- [ ] Proper nouns spelled consistently
- [ ] Cultural behaviors match the people
- [ ] **Tonal register** matches the genre classification
      (re-feudal / survival / Swedish / village-real / soft
      Tolkienesque). No high-fantasy drift, no comic-fantasy
      drift, no modern-genre drift.
- [ ] **Encounters refuse the anti-trope catalog.** No
      kill-the-monster as the right answer; no undead-purge as
      the right answer; no mindless-orcs; no good-faction-vs-bad;
      no find-artifact-win.
- [ ] **Monsters carry a contract** that some village or person
      has been keeping. The contract is the scene, not the fight.
- [ ] **Named historical figures** referenced consistently with
      the chronology (alive vs dead, current location, current
      pressure).
- [ ] **Villages** are named via at least three of the seven
      components (food, water, defense, shrine, burial, authority,
      grudge) in the first 200 words.
- [ ] **Time** is anchored by the eight phases (Springrise →
      Winterwane) or named festivals (Awakening Day, Lushday,
      Harvest Day, Rotday, Midwinter, Midsummer), not "spring,"
      "autumn," "next year."
- [ ] **Calendar dates** are in AS (After the Shift) only when an
      old object, person, or grievance forces them into the scene.
