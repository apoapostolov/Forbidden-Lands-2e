# Playbook: Integrating a Region or Campaign Source into the Lore Skill

Use this playbook whenever a new sourcebook, regional supplement,
or campaign module is being absorbed into the lore skill's
reference files. The Raven's Purge integration (pass 1–3 across
two sessions) is the canonical example of this workflow.

---

## Before You Start

**Confirm the scope of the source material:**

1. Does this source cover a new region not yet in `places.md`, or
   does it extend the existing core Ravenlands?
2. Does it introduce a campaign with spoilable plot content, or
   is it purely setting expansion?
3. Is the text clean for reading, or is it an OCR scan / rough
   draft that requires interpretation?

If the source contains a campaign (spoilable plot content),
a campaign file is required. If it is purely setting expansion
(new region, new kin detail, new historical period), reference
files only.

---

## Step 1 — Create the Campaign File (if applicable)

Create `campaigns/<source_slug>.md` before reading the source.

The campaign file is the spoiler container. Everything that would
ruin discovery for a player goes here, never into `references/`.

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

Wire the campaign file into `SKILL.md` under the **Campaign Files**
section using the same format as `ravens_purge.md`.

---

## Step 2 — First Pass: Systematic Structural Extraction

**Goal:** Get all major world-building content into the reference
files. Work through the source in order, section by section.

**Read method:** Read the source in chunks of 200–400 lines.
After each chunk, write additions before moving to the next.
Do not batch all reading before writing — context overflows.

**Triage rule for every fact:**

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
| Campaign-specific mechanics or statblocks | Campaign file |

**Spoiler triage test:** Ask — *"Would knowing this fact before
play ruin a discovery, a twist, or a reveal?"* If yes, it is a
spoiler. If it reads like something a knowledgeable NPC might
tell the players over beer, it is not a spoiler.

**After the first pass:** Run a grep-audit to verify key proper
nouns from the source now appear in the reference files. Spot-check
five to ten names from each major section.

---

## Step 3 — Second Pass: Lore Depth Audit

**Goal:** Catch interesting world-building details missed in the
structural pass — things that inspire new scenarios, deepen
faction complexity, or add regional character.

**What to look for:**

- Named individuals with interesting roles not yet in `kin.md` or
  `history.md`
- Faction tensions, grudge structures, political angles not yet
  in `places.md`
- Ecological or environmental detail that makes a region feel
  distinct
- Creature behaviors and cultural relationships not yet in
  `bestiary.md`
- Artifact provenance gaps — physical description, current holder,
  contested history
- Historical events that reframe known facts

**Method:** Re-read the source at higher speed with these
categories in mind. When a missed detail is found, write it
immediately into the appropriate reference file before continuing.
Do not queue a list for later; write as you find.

**After the second pass:** The reference files should now be dense
enough to support scenario creation from scratch. A GM using only
the skill (without the source) should be able to run a session in
any named location without obvious gaps.

---

## Step 4 — Third Pass: Small-Detail Texture Pass

**Goal:** Capture small curiosities, cultural flavor, sensory
material, village life texture, and atmospheric location detail
that does not rise to the level of major lore but makes prose
and worldbuilding feel lived-in.

**What to look for:**

- Morning routines, domestic customs, food habits
- Specific insults, slang terms, named games or pastimes
- Eccentric NPC behaviors that reveal character
- Sensory anchors: what a location smells like, sounds like,
  what is on the floor
- Small rituals — what people do before a battle, at a shrine,
  at a market
- Ecological behaviors: how creatures hunt, court, feed, or rest
- Workshop and craft details: what specific tools or materials
  look like, how processes work
- Architectural or environmental peculiarities that distinguish
  one site from another

**These details go into:**
- `references/kin.md` — cultural texture under the relevant kin
  or clan subsection
- `references/places.md` — appended to the named location entry
- `references/bestiary.md` — appended to the creature entry
- `references/artifacts.md` — expanded into the mechanical hint
  block for physical appearance

**Anti-pattern:** Do not write third-pass texture into new
top-level sections. Append to existing entries. The texture
should be invisible — readers should feel the file got richer,
not longer.

**After the third pass:** The reference files should be capable
of producing first-draft prose without consulting the source.

---

## Step 5 — Wiring and Cross-Reference Audit

1. Confirm the campaign file is listed in `SKILL.md`
2. Confirm `references/places.md` has entries for every named
   location from the source
3. Confirm `references/history.md` has entries for all new
   historical events and named figures
4. Confirm all cross-references inside reference files that
   mention campaign content say *"See `campaigns/<slug>.md`"*
   for spoilable facts
5. Run markdownlint on changed files:
   ```
   npx markdownlint-cli2 "skills/forbidden-lands-lore/**/*.md"
   ```

---

## Step 6 — Session Handoff Note (for multi-session integrations)

If the integration spans multiple sessions, create a session note
before the context ends:

- Record which source lines have been read and which remain
- Record which reference files have been updated and which still
  need additions
- List the specific cataloged additions not yet written (the
  in-memory queue that would otherwise be lost on compaction)
- Record whether the three passes are complete or in progress

This note lives in session memory only (`/memories/session/`),
not committed to the repo.

---

## New Region vs. Campaign Overlap: Decision Points

| Situation | Action |
|---|---|
| Source covers only new geography with no ongoing campaign plot | No campaign file needed; reference files only |
| Source covers an area with intersecting campaign plot (e.g. Bitter Reach events affect Ravenlands) | Create campaign file; add geography to `references/places.md` under the appropriate region section |
| Source introduces new kin or sub-kin | Add to `references/kin.md`; add statblock anchor |
| Source retcons or contradicts an existing reference file entry | Flag the conflict, note both versions with source attribution, do not silently overwrite |
| Source covers history that predates the existing chronology | Insert into `references/history.md` in the correct date-ordered position |

---

## File Naming Convention for Campaigns

`campaigns/<region-or-title-slug>.md`

Examples:
- `campaigns/ravens_purge.md` — Raven's Purge (Ravenlands)
- `campaigns/bitter_reach.md` — The Bitter Reach expansion
- `campaigns/bloodmarch.md` — The Bloodmarch supplement

The slug should be lowercase, words separated by underscores,
matching the source material's title closely enough to be
unambiguous.
