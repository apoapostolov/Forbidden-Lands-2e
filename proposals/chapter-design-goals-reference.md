<!-- markdownlint-disable MD013 -->

# Chapter Design Goals Reference

## Purpose

This document stores stabilized design goals and cleaned design notes for chapter-scale work after each proposal pass reaches editorial polish.

Its job is simple:

- preserve the intended shape of a polished chapter or subchapter
- keep design goals out of final manuscript prose
- give later passes a clean reference point
- prevent important chapter intentions from being buried in drafting history

Use this file when:

- a proposal pass has been polished enough to count as a stable checkpoint
- a chapter's goals, pressures, and non-goals need to be preserved
- later rewrites need to know what must not be lost

Do **not** treat this file as manuscript prose.
It is a design reference.

## Entry Format

Every chapter entry should use this structure:

### Chapter Or Section Name

**Status:** Draft / Stabilized / Integration-ready

**Purpose**

- what this chapter or section must do in play

**Core Design Goals**

- the few outcomes the chapter must reliably create

**Pressure Channels Preserved**

- what hardships, tradeoffs, or limits the design must keep intact

**What It Must Not Become**

- nearby failure modes, false identities, or tempting but wrong directions

**Voice And Texture Notes**

- what the prose and examples should feel like

**Integration Notes**

- what adjacent chapters, rules, or subsystems it must remain compatible with

## Chapter 2: Life Generator Replacement

**Status:** Final stabilized replacement draft after Pass 10

**Purpose**

- replace the current simple life generator with a deeper life-path system
- create characters who feel lived-in before play begins
- preserve Chapter 2 starting power while greatly increasing history, scars, hooks, and second-career texture

**Core Design Goals**

- life should unfold through cycles divided into turns rather than one childhood result plus a few formative events
- childhood should point a character toward a life, not finish the build
- age should still anchor starting power through Chapter 2's attribute and talent baselines
- every completed turn after childhood should matter and leave a mark
- failure should redirect a life rather than merely punish it
- the system should support random play, guided-random play, and constrained guided authorship
- prison, exile, disgrace, debt, and patron collapse should redirect a character into a new life instead of stopping character creation
- fallback lives should remain viable roads back toward the chapter's professions

**Pressure Channels Preserved**

- no extra Willpower engine at character creation
- no front-loaded talent bloom beyond existing Chapter 2 tolerances
- no clean removal of scarcity, danger, or social consequence
- no old-character invulnerability disguised as experience
- no universal best path that informed players would always choose
- no failure state that leaves a character underbuilt or mechanically stranded
- no hidden increase to Chapter 2 attribute, skill, silver, mount, armor, or talent baselines

**What It Must Not Become**

- not a soft narrative minigame detached from the rest of the system
- not Traveller pasted into Ravenland with names swapped
- not a modern career ladder with clean advancement logic
- not a second talent economy layered on top of Chapter 2
- not a lore-generic fantasy backstory builder
- not an optimizer's ladder where one path chain solves combat, silver, mobility, and safety at once

**Voice And Texture Notes**

- turns should feel harsh, practical, and materially grounded
- a turn should read as one reach of the wheel of life, not as a neat calendar unit
- the prose can allow a little hard poetry here: the gruel of life, hardship ground thin, and the rare spark of happiness caught between one burden and the next
- events should smell of roads, weather, beasts, silver, shrines, blood, labor, and poor shelter
- Alderlander color should carry levy, walls, tolls, ledgers, ferries, and worn feudal command
- Aslene color should carry herds, horse-flesh, clan duty, feud, fire, and the long plain
- Ailander color should carry Raven Sisters, hidden shrines, kin sorrow, old songs, and practical mysticism
- the prose should read like the book, not like design commentary
- tables should feel local to Ravenland, never abstract or institutionally clean
- procedure should read like Chapter 2 instructions, not like a design memo defending itself
- worked examples should sound like hard lives remembered, not like optimization demos

**Integration Notes**

- must remain compatible with Chapter 2 age, profession, talent, language, gear, Pride, Dark Secret, and relationship structures
- must preserve profession identity instead of dissolving it into broad life-path mush
- must feed naturally into `How Did You Meet?`
- must be written so proposal rationale can stay here while final rules text moves cleanly into `corebook/`
- fallback paths must bridge failed careers, prison, exile, and hunger without needing separate subgames
- must keep starting gear and silver near profession baselines, with richer history replacing raw inflation
- must ban result types that create extra attacks, free Willpower engines, armor bypass, stacked premium mounts, or other obvious dominant starts
- `How Did You Meet?` should remain as the closing company-bond table with only a stronger bridge above it
- the old simple generator should be removed rather than preserved as a sidebar once this replacement is adopted
- childhood should count as the first two turns of the first cycle so the skill math still lands on `8 / 12 / 16`
- profession Resource Dice should remain, but profession starting gear and silver should not stack on top of life-path gear and silver
