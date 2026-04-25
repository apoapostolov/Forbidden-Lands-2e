---
name: forbidden-lands-writing-voice
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

# Forbidden Lands Writing Voice

This skill is the literary technique layer for the Forbidden Lands 2E
manuscript. It names the authors, maps their techniques, and gives
the operational rules for applying those techniques to new prose.

For the complete combined skill — sentence rules, manuscript register,
rewrite calibration, worldbuilding voice patterns, and these author
techniques together — load `skills/forbidden-lands-writing/` instead.
This skill is the author-technique layer only.

## The Target Voice

The target register is:

> **Pre-feudal medieval survival fantasy with a Swedish tone, the
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
The Abercrombie-Cook line covers the mercenary company fiction voice
specifically — contracted violence, company hierarchy, band-of-brothers
register. See `skills/forbidden-lands-writing/references/fiction-voice-abercrombie-cook.md`
when writing mercenary band fiction.

The six authors analyzed in this skill define the general manuscript
registers the project requires:

| Author | Primary Contribution |
|---|---|
| Andrzej Sapkowski | Monster-as-contract, village ecology, fable structure, Eastern European pre-Christian daily religion |
| Guy Gavriel Kay | Elegiac register, sacred geography, long memory, soft Tolkienesque poetic inheritance |
| K.J. Parker | Pre-industrial craft authenticity, economic realism, unreliable pragmatist narrator, dark comedy |
| Ursula K. Le Guin | Anthropological village authenticity, absence as presence, ecological specificity, the unhurried sentence |
| Bernard Cornwell | Dark Ages physical survival, food and weather as constant pressure, first-person pragmatist, no clean heroes |
| John Gwynne | Norse/Dark Ages oath culture, body-first narration, shield-wall perspective, physical grief |
| Joe Abercrombie | Close-third confessional, physicality as psychology, bathetic pivot, dark humor as character property, violence as claustrophobic aftermath |
| Glen Cook | Military annals voice, radical understatement, logistical baseline, character through repeated habit, structural absence as emotional content |

## When To Load Which Reference

Load by scene type, not by preference:

- **Village scenes, NPC texture, daily life** → Le Guin + Cornwell +
  Sapkowski
- **Monster encounter, ecological horror** → Sapkowski + Cook
  (`references/author-glen-cook.md` for understatement and logistics)
- **Moral dilemma, faction conflict** → Abercrombie + Sapkowski +
  Parker (`references/author-abercrombie.md` for moral weight through
  consequence)
- **Artifact or relic with history** → Kay + Parker
- **Battle or combat** → Cornwell + Gwynne + Cook + Abercrombie
  (`references/author-glen-cook.md` for military logistics;
  `references/author-abercrombie.md` for violence in claustrophobic
  detail and aftermath)
- **Grief, long memory, sacred place** → Kay + Gwynne
- **Economic pressure, craft, survival mechanics** → Parker + Cornwell
  - Le Guin
- **Mercenary company, contracted violence, hired sword** →
  `references/author-abercrombie.md` + `references/author-glen-cook.md`
  For the vignette synthesis of how both authors combine into one
  operational fiction voice, load
  `skills/forbidden-lands-writing/references/fiction-voice-abercrombie-cook.md`
- **Vignette or epigraph** → Kay + Sapkowski
- **Rules prose, game example scenes, chapter structure** →
  `references/rules-voice.md`
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

- `references/author-abercrombie.md`
  Joe Abercrombie: close-third confessional tied to character
  psychology, physicality as psychology, the bathetic pivot,
  dark humor sourced in character not narrator, violence as
  claustrophobic and undignified, aftermath worse than event,
  moral weight through consequence.

- `references/author-glen-cook.md`
  Glen Cook: the annalist voice, radical understatement, logistical
  baseline as default mode, character through repeated habit,
  structural absence as emotional content, dark humor as survival
  mechanism, the material catalogue as world-building.

- `references/rules-voice.md`
  The game designer register. Two manuscript temperatures (Härenstam
  cool precision vs. Granström warm-dark). The five manuscript
  registers (rules, mixed bridge, item, example, flavor). Chapter
  temperature map. Paragraph shapes. Multi-rule sequence writing.
  Progressive disclosure architecture. Recurring characters in
  examples. What AI gets wrong in rules prose. **Load when writing
  or auditing any rules text, talent, spell description, item entry,
  or example scene.**

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

- `references/worked-examples.md`
  13 wrong/correct pairs targeting the 13 highest-frequency AI
  patterns. Quick Diagnostic checklist. Use when an abstract
  rule is not landing — read the correct example, not the rule.

- `references/rewrite-calibration-examples.md`
  10 before-and-after pairs across all six manuscript registers:
  item description, injury naming, proposal tone, fiction opening,
  spell description, cultural flavor, mixed bridge, talent, journey,
  and item distinction. Each pair includes change notes explaining
  what was cut, what was added, and why. **Load when calibrating
  voice for a specific register — these are register-focused where
  worked-examples.md is pattern-focused.**

- `references/register-contrastive.md`
  Same scene (arrive at dark village, gate barred, no dogs, no fire)
  rendered in all six author registers with cross-register notes.
  Use when checking whether a passage sounds like the named register
  or has drifted.

- `references/world-vocabulary.md`
  Setting-specific vocabulary rules. How the three human peoples
  name themselves in speech, thought, and writing. Non-human kin
  speech patterns. Divine names in use by tradition. The Older Gods
  naming practice. Currency and economic vocabulary. Social rank terms.
  Place names. Register rules by culture. Forbidden vocabulary.

- `references/voice-test-protocol.md`
  Three tests: Quick Scan (13 highest-frequency patterns, binary,
  under 2 minutes), Full Pass (all 43 patterns with scoring
  thresholds), Author Lens Check (per-register positive and negative
  signals). Use as the final gate before integrating prose.

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

5. **For manuscript drafting, load `skills/forbidden-lands-writing/`**
   which combines this author-technique layer with sentence rules,
   register system, rewrite calibration, and worldbuilding voice
   patterns.

6. **Abercrombie and Cook are the mercenary company voice.**
   For individual author technique: `references/author-abercrombie.md`
   and `references/author-glen-cook.md`. For the vignette synthesis
   (how the 25 Band Life vignettes combine both authors into one
   operational voice), load
   `skills/forbidden-lands-writing/references/fiction-voice-abercrombie-cook.md`.
   Neither is the general manuscript voice.

## Companion Skills

- `skills/forbidden-lands-writing/SKILL.md` — complete combined skill:
  author techniques (this skill), sentence rules, register system,
  anti-AI patterns, worldbuilding voice, rewrite calibration
- `skills/forbidden-lands-lore/SKILL.md` — setting authenticity,
  tonal classification, encounter anti-tropes
- `skills/forbidden-lands-bestiary/SKILL.md` — encounter design
  mandate, the seven encounter shapes
