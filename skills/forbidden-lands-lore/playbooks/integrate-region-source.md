# Playbook: Integrating a Region or Campaign Source into the Lore Skill

Use this playbook whenever a new sourcebook, regional supplement,
or campaign module is being absorbed into the lore skill's
reference files. The Raven's Purge integration (pass 1–3 across
two sessions) is the canonical example for Ravenlands campaigns.
The Bloodmarch integration is the canonical example for expansion
regions.

---

## Before You Start

**Confirm the scope of the source material:**

1. Does this source cover a new region not yet in `places.md`, or
   does it extend the existing core Ravenlands?
2. **Is this an expansion region** — a neighboring country distinct
   from the Ravenlands with its own kin, geography, gods, and magic?
   Or is it a campaign set **within** the core Ravenlands?
3. Does it introduce a campaign with spoilable plot content, or
   is it purely setting expansion?
4. Is the text clean for reading, or is it an OCR scan / rough
   draft that requires interpretation?

**This answer to question 2 determines the entire workflow.**
If the source is an expansion region, follow the Expansion Region
workflow below. If it is a Ravenlands campaign, follow the Core
Ravenlands Campaign workflow.

If the source contains a campaign (spoilable plot content),
a campaign file is required regardless of type. If it is purely
setting expansion with no plot secrets, reference files only.

---

## WORKFLOW A: Core Ravenlands Campaign

Use when the source covers territory **within** the existing
Ravenlands. Examples: Raven's Purge, any adventure site in
Harga or Weatherstone.

### A1 — Create the Campaign File (if applicable)

Create `campaigns/<source_slug>.md` before reading the source.

The campaign file is the **spoiler container**. Everything that
would ruin discovery for a player goes here, never into
`references/`.

**Campaign file structure:**

```markdown
# [Campaign Title]

**Source:** [Author, publisher, year]
**Scope:** [region(s) covered; whether it overlaps core Ravenlands
          or introduces new territory]
**Central conflict:** [one sentence, non-spoiler]

## Public Overview (non-spoiler)

[Factions, major locations, publicly known tensions.
Safe for GM and player-facing use.]

## Key Locations

[Adventure site descriptions at the level a traveler would know:
what it looks like from outside, what the locals say about it,
who controls it, what the legends say.]

## Key NPCs

[Public identity, faction, appearance, role.
No secret agendas, no true natures here.]

## ⚠️ SPOILER SECTION

[Everything below requires explicit user confirmation before
the skill reads or cites it. See the Spoiler Handling Protocol
in SKILL.md.]

### NPC True Agendas

### Artifact True Powers and Histories

### Plot Twists and Reveals

### Adventure Site Secrets

### Campaign Outcome Paths
```

Wire the campaign file into `SKILL.md` under **Campaign Files**
using the same format as `ravens_purge.md`.

### A2 — Three Passes: Ravenlands Triage Destinations

| Fact type | Destination |
|---|---|
| Public location description, geography | `references/places.md` |
| Kin culture, clan names, customs, named individuals | `references/kin.md` |
| Historical events, named figures, dates | `references/history.md` |
| Gods, religious orders, rituals | `references/gods.md` |
| Named artifacts (legend + location only) | `references/artifacts.md` |
| Monster origin, ecology, cultural integration | `references/bestiary.md` |
| Setting facts (currency, factions, world state) | `references/setting.md` |
| Artifact true powers, NPC secret agendas, plot twists | Campaign file SPOILER SECTION |
| Campaign-specific mechanics or statblocks | Campaign file SPOILER SECTION |

### A3 — Wiring Audit

1. Confirm campaign file is listed in `SKILL.md`
2. Confirm `references/places.md` has entries for every named
   location from the source
3. Confirm `references/history.md` has entries for all new
   historical events and named figures
4. Confirm all cross-references inside reference files that
   mention campaign content say *"See `campaigns/<slug>.md`"*
   for spoilable facts

---

## WORKFLOW B: Expansion Region

Use when the source covers a **neighboring country distinct from
the Ravenlands** with its own kin, geography, gods, and magic
system. Examples: The Bloodmarch (Aslene), The Bitter Reach
(northern tundra).

**Core rule:** Nothing from an expansion region enters
`references/`. The `/references/` files describe the Ravenlands
only. All expansion region content lives under
`regions/<slug>/`.

### B1 — Create the File Structure

Before reading the source, create two things:

**1. The regions directory:**

```
regions/
  <slug>/
    setting.md    — world state, terrain, magic, drugs, potions
    kin.md        — all kin native and immigrant to the region
    history.md    — full chronology from prehistory to present
    gods.md       — all gods, orders, and religious practices
    bestiary.md   — creature lore, ecology, cultural integration
    artifacts.md  — named artifacts (legend + public knowledge only)
    places.md     — sub-regions, named locations, adventure sites
```

Canonical example: `regions/bloodmarch/`

**2. The campaign file (if the source includes a campaign):**

`campaigns/<slug>.md` — the **spoiler container only**.
It should not repeat non-spoiler lore from `regions/<slug>/`.
Its structure:

```markdown
# [Region Name] — Campaign File

**Lead Writer:** [Author]
**Campaign:** [Campaign name]
**Type:** Expansion Region

---

## Region References

Non-spoiler lore for [Region Name] is organized in
`regions/<slug>/`. Load the appropriate file when the user
asks about the region, its kin, its history, etc.

- `regions/<slug>/setting.md` — [brief scope description]
- `regions/<slug>/kin.md` — [brief scope description]
- `regions/<slug>/history.md` — [brief scope description]
- `regions/<slug>/gods.md` — [brief scope description]
- `regions/<slug>/bestiary.md` — [brief scope description]
- `regions/<slug>/artifacts.md` — [brief scope description]
- `regions/<slug>/places.md` — [brief scope description]

This file contains only spoiler content.

---

## Spoiler Handling Protocol

[Standard gate — see SKILL.md]

## ⚠️ SPOILER SECTION

### True Powers and Mechanics of Campaign MacGuffins
### Key Players — True Agendas and Secret Goals
### Ancient History / World Revelation
### Campaign Phases
### Adventure Site Secrets
### Campaign Outcomes
```

Wire the campaign file into `SKILL.md` under **Expansion Regions**
(not under Campaign Files). Wire each `regions/<slug>/` file
into the appropriate listing in SKILL.md.

### B2 — Three Passes: Expansion Region Triage Destinations

| Fact type | Destination |
|---|---|
| World state, climate, access routes, terrain mechanics | `regions/<slug>/setting.md` |
| New terrain types and their journey rules | `regions/<slug>/setting.md` |
| New magic traditions (full spell lists) | `regions/<slug>/setting.md` |
| Drugs, potions, unique substances with mechanics | `regions/<slug>/setting.md` |
| Kin culture, clan names, customs, named individuals | `regions/<slug>/kin.md` |
| New kin or sub-kin native to the region | `regions/<slug>/kin.md` |
| Historical events, named figures, dates | `regions/<slug>/history.md` |
| Gods, religious orders, rituals | `regions/<slug>/gods.md` |
| Named artifacts (public legend and location only) | `regions/<slug>/artifacts.md` |
| Monster origin, ecology, cultural integration | `regions/<slug>/bestiary.md` |
| Sub-regions, named locations, adventure site overviews | `regions/<slug>/places.md` |
| Artifact true powers, NPC secret agendas, plot twists | `campaigns/<slug>.md` SPOILER SECTION |
| Campaign mechanics, phase structure, outcome paths | `campaigns/<slug>.md` SPOILER SECTION |

**Spoiler triage test:** Ask — *"Would knowing this fact before
play ruin a discovery, a twist, or a reveal?"* If yes, it is a
spoiler. If it reads like something a knowledgeable NPC might
tell the players over beer, it is not a spoiler.

### B3 — Three-Pass Execution

Each pass applies to all seven `regions/<slug>/` files. Do not
batch all reading before writing — context overflows. Write to
the appropriate file after each read chunk.

**Pass 1 — Structural Extraction:** Get all major world-building
content into the appropriate region files. Work through the source
in chunks of 200–400 lines. After each chunk, write before moving
on. After the pass: grep-audit five to ten key proper nouns from
each major section to verify coverage.

**Pass 2 — Lore Depth Audit:** Re-read at higher speed looking
for named individuals not yet in `kin.md`, faction tensions not
yet in `places.md`, ecological detail not yet in `bestiary.md`,
and artifact provenance gaps. Write immediately when found.
After the pass: a GM using only the skill files should be able
to run a session in any named location without obvious gaps.

**Pass 3 — Texture Pass:** Capture cultural flavor, sensory
anchors, domestic customs, eccentric NPC behaviors, ecological
behaviors, and architectural peculiarities. Append to existing
entries; do not create new top-level sections. After the pass:
the files should be capable of producing first-draft prose without
consulting the source.

### B4 — Wiring and Cross-Contamination Audit

1. Confirm all seven `regions/<slug>/` files are referenced in
   `SKILL.md` under the correct expansion region entry
2. Confirm `campaigns/<slug>.md` is listed under **Expansion
   Regions** in `SKILL.md` (not under Campaign Files)
3. Verify that no expansion-region content has leaked into any
   `references/` file — run a grep for the region's key proper
   nouns against all `/references/*.md` files
4. Confirm all cross-references inside `regions/<slug>/` files
   that touch spoilable facts say *"See `campaigns/<slug>.md`"*
5. Run markdownlint on all new and changed files

---

---

## Session Handoff Note (for multi-session integrations)

If the integration spans multiple sessions, create a session note
before the context ends:

- Record which workflow applies (A or B)
- Record which source lines have been read and which remain
- Record which files have been updated and which still need work
- List cataloged additions not yet written (the in-memory queue)
- Record whether pass 1, 2, or 3 is complete or in progress

This note lives in session memory only (`/memories/session/`),
not committed to the repo.

---

## Decision Reference

| Situation | Action |
|---|---|
| Source covers only new geography within Ravenlands, no campaign | No campaign file; reference files only |
| Source is a Ravenlands campaign | Workflow A; content → `references/`; spoilers → `campaigns/<slug>.md` |
| Source is an expansion region (neighboring country) | Workflow B; content → `regions/<slug>/`; spoilers → `campaigns/<slug>.md` |
| Source introduces kin native to the Ravenlands | `references/kin.md` |
| Source introduces kin native to an expansion region | `regions/<slug>/kin.md` |
| Source retcons or contradicts an existing file entry | Flag conflict; record both versions with source attribution; do not silently overwrite |
| Source covers history that predates the existing chronology | Insert in date order into the appropriate history file |
| Source contains region that intersects both Ravenlands and an expansion region | Write the Ravenlands-side content to `references/`; write the expansion-region-side content to `regions/<slug>/`; note the cross-border connection in both |

---

## File and Folder Naming Conventions

**Ravenlands campaign file:**
`campaigns/<title-slug>.md`

**Expansion region directory:**
`regions/<slug>/`
— with files: `setting.md`, `kin.md`, `history.md`, `gods.md`,
`bestiary.md`, `artifacts.md`, `places.md`

**Expansion region campaign file:**
`campaigns/<slug>.md`

**Slug format:** lowercase, words separated by underscores,
matching the source material's title closely enough to be
unambiguous.

Examples:

- `campaigns/ravens_purge.md` — Raven's Purge (Ravenlands)
- `campaigns/bloodmarch.md` — The Bloodmarch spoilers
- `campaigns/bitter_reach.md` — The Bitter Reach spoilers
- `regions/bloodmarch/` — The Bloodmarch non-spoiler reference
- `regions/bitter_reach/` — The Bitter Reach non-spoiler reference
