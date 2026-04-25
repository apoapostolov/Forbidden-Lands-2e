---
name: writing-voice
description: |
  Use when drafting, revising, or auditing fiction prose that must match
  the pre-feudal medieval survival fantasy register of this project. This
  skill identifies and teaches the literary techniques of six modern authors
  whose combined practice defines the target voice — Andrzej Sapkowski,
  Guy Gavriel Kay, K.J. Parker, Ursula K. Le Guin, Bernard Cornwell, and
  John Gwynne — alongside the Abercrombie-Cook line already analyzed in
  the forbidden-lands-writing skill. Includes the master anti-AI humanizer
  catalog (43 patterns, each with AI example, human fix, and Forbidden
  Lands application), a composite voice synthesis for blending authors
  by scene type, sentence architecture targets, dialogue mechanics, and a
  sensory vocabulary catalog. Load when writing village scenes, vignettes,
  encounter fiction, monster encounters, NPC introductions, epigraphs, or
  any prose where generic AI output would be detected immediately. Also
  load for humanizing or auditing a draft that reads generated.
---

# Writing Voice

This skill is the literary ancestor layer for the Forbidden Lands 2E
manuscript. It names the authors, maps their techniques, and gives
the operational rules for applying those techniques to new prose.

It is not a substitute for `skills/forbidden-lands-writing/`. That
skill owns the sentence-level rules, register system, anti-AI patterns,
and rewrite calibration for the manuscript specifically. This skill owns
the deeper question: who writes in this tradition, how do they do it,
and what does a human writer in this style actually produce?

## The Target Voice

The target register is:

> **Re-feudal medieval survival fantasy with a Swedish tone, the
> realistic authenticity of village life, and a soft Tolkienesque
> poetic worldbuilding.**

Each clause is a constraint, not a mood. The prose must be:

- **Physical before atmospheric** — body, weather, food, iron, wood
- **Small-scale before epic** — village before kingdom, family before
  faction, one bad winter before the war
- **Morally weighted without moral resolution** — every faction has
  a price, every choice has a cost, no one is simply right
- **Melancholy as baseline** — joy is earned and small; loss is older
  than the speaker
- **Oral-culture patterned** — people speak in memory and repetition,
  not analysis

## The Literary Tradition

This voice sits at the intersection of six modern literary lineages.
The Abercrombie-Cook line is the primary existing analysis:
see `skills/forbidden-lands-writing/references/fiction-voice-abercrombie-cook.md`.

The six authors analyzed in this skill extend that foundation into the
specific registers the manuscript also requires:

| Author | Primary Contribution |
|---|---|
| Andrzej Sapkowski | Monster-as-contract, village ecology, fable structure, Eastern European pre-Christian daily religion |
| Guy Gavriel Kay | Elegiac register, sacred geography, long memory, soft Tolkienesque poetic inheritance |
| K.J. Parker | Pre-industrial craft authenticity, economic realism, unreliable pragmatist narrator, dark comedy |
| Ursula K. Le Guin | Anthropological village authenticity, absence as presence, ecological specificity, the unhurried sentence |
| Bernard Cornwell | Dark Ages physical survival, food and weather as constant pressure, first-person pragmatist, no clean heroes |
| John Gwynne | Norse/Dark Ages oath culture, body-first narration, shield-wall perspective, physical grief |

The Abercrombie-Cook line provides: grimdark moral neutrality, military
logistics as baseline, character through habit, humor as survival
mechanism.

## When To Load Which Reference

Load by scene type, not by preference:

- **Village scenes, NPC texture, daily life** → Le Guin + Cornwell +
  Sapkowski
- **Monster encounter, ecological horror** → Sapkowski + Cook
- **Moral dilemma, faction conflict** → Abercrombie + Sapkowski +
  Parker
- **Artifact or relic with history** → Kay + Parker
- **Battle or combat** → Cornwell + Gwynne + Cook
- **Grief, long memory, sacred place** → Kay + Gwynne
- **Economic pressure, craft, survival mechanics** → Parker + Cornwell
  - Le Guin
- **Vignette or epigraph** → Kay + Sapkowski
- **Humanizing or auditing a draft** → anti-AI humanizer first

## Bundled References

- `references/anti-ai-humanizer.md`
  43 named AI writing patterns, each with AI example, human fix,
  and Forbidden Lands application. Also contains the 7-layer
  failure taxonomy, author-specific evasion techniques, the
  full diagnostic checklist, and the revision protocol. **Load
  this first when auditing or humanizing a draft.**

- `references/composite-voice.md`
  How the six authors combine into one working voice. Priority
  hierarchy when techniques conflict. Register map by scene type.
  Worked examples of the composite voice applied to FL2E scenes.
  Anti-patterns of misapplication.

- `references/author-sapkowski.md`
  Andrzej Sapkowski: techniques, sentence architecture, the false
  threshold structure, fable frame, monster-as-contract, dialogue
  as duel, the price mechanism, pre-Christian ecology.

- `references/author-kay.md`
  Guy Gavriel Kay: techniques, elegiac omniscience, sacred geography,
  long memory, the "last time" marker, death in subordinate clauses,
  song as structure, parallel construction as emotional intensifier.

- `references/author-parker.md`
  K.J. Parker: techniques, the unreliable pragmatist narrator,
  technical procedure as character, economics as plot, institutional
  characters, dark comedy through incongruity.

- `references/author-leguin.md`
  Ursula K. Le Guin: techniques, thick description, custom over drama,
  gift economies as worldbuilding, absence as presence, the unhurried
  sentence, ecological specificity.

- `references/author-cornwell.md`
  Bernard Cornwell: techniques, food and weather as constant pressure,
  first-person survivor narration, the loyalty test, tactical
  geography, death without ceremony.

- `references/author-gwynne.md`
  John Gwynne: techniques, body-first narration, oath as narrative
  spine, shield-wall perspective, grief as physical, oral-culture
  tells, the named object.

- `references/sentence-architecture.md`
  Per-author sentence profiles, the Forbidden Lands target sentence,
  rhythm techniques, variation strategies, and diagnostic questions.

- `references/dialogue-mechanics.md`
  Per-author dialogue profiles, oral-culture sentence patterns, dialect
  without parody, silence between lines, implied conversation, tags,
  attribution, and when to skip dialogue entirely.

- `references/sensory-vocabulary.md`
  Priority sense hierarchy, weather as character, food as worldbuilding,
  body as consciousness, sound before sight, specific vs. generic
  decision tree, master vocabulary lists by environment type.

## Hard Rules

1. **Load the anti-AI humanizer before submitting any draft.** Run
   the 43-pattern diagnostic. Not a suggestion.

2. **Choose an author register for each scene.** Name it before
   writing: "This scene is Cornwell-primary with Le Guin texture."
   Mixed registers without a named primary always produce generic
   output.

3. **Physical before atmospheric.** Every scene opens on a body doing
   a physical thing in a specific place. Weather, mood, and theme
   enter through that body, not before it.

4. **The monster is a contract. The relic has a price. The faction
   is partly right.** These are structural constraints inherited from
   the literary tradition and built into the lore. See
   `skills/forbidden-lands-lore/references/tone-and-encounter-design.md`.

5. **Cross-load `skills/forbidden-lands-writing/` for manuscript
   prose.** This skill is the author-technique layer. The
   forbidden-lands-writing skill is the manuscript-application
   layer. Both must be active for manuscript drafting.

6. **The Abercrombie-Cook analysis is the primary existing reference.**
   Read it first at
   `skills/forbidden-lands-writing/references/fiction-voice-abercrombie-cook.md`.
   The authors in this skill extend, not replace, that analysis.

## Companion Skills

- `skills/forbidden-lands-writing/SKILL.md` — sentence rules,
  register system, anti-AI patterns, rewrite examples for this
  manuscript
- `skills/forbidden-lands-lore/SKILL.md` — setting authenticity,
  tonal classification, encounter anti-tropes
- `skills/forbidden-lands-bestiary/SKILL.md` — encounter design
  mandate, the seven encounter shapes
