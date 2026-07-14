---
name: forbidden-lands-writing-voice
description: Draft, revise, or audit Forbidden Lands 2E manuscript prose. Use for rules, examples, tables, vignettes, epigraphs, legends, NPCs, locations, encounters, and GM guidance that must be clear, concrete, setting-native, playable, and free of generic AI style. Covers concise rules voice, physical dark-fantasy fiction, dialogue, sensory detail, register control, and sandbox-facing situation writing.
---

<!-- markdownlint-disable MD013 MD060 -->

# Forbidden Lands Writing Voice

This skill covers the complete literary and mechanical voice standard
for the Forbidden Lands 2E manuscript. It defines two voice modes that
must coexist in the book, names the authors whose techniques define the
fiction mode, and gives the operational rules for the rules mode.

Use this skill as the complete prose router. Load only the references required
for the passage and pair it with `forbidden-lands-lore` whenever the prose
makes setting claims.

## The Two Voices

The Forbidden Lands manuscript operates in two distinct voice modes.
Both are mandatory. A chapter that gets the rules voice right but
writes weak fiction is half a manuscript. A chapter with vivid fiction
and mechanical mush is the other half.

### The Writing Voice

**Scope:** Fiction vignettes, epigraphs, flavor exposition, novella-style
worldbuilding passages, NPC introductions, atmospheric scene-setters, the
in-world fiction that opens chapters or sections, and backtick-offset
prose blocks meant to be read as fiction first.

**What it must do:**

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

The literary tradition below defines its technical lineage. The eight
author deep-dives are the primary operational references for this voice.

### The Rules Voice

**Scope:** Talent descriptions, skill definitions, attribute rules,
combat procedures, journey phases, item and spell entries, example
scenes demonstrating a mechanic, GM guidance, tables, and all rules
text in the corebook or any supplement.

**What it must do:**

The rules voice belongs to a game designer who has playtested the
system until its failure modes are known. It writes:

- **Declaratively** — not "players may wish to consider," but "roll"
- **From consequence** — trigger first, decision second, consequence third;
  not in the order the designer thinks about the rule
- **Without design commentary** — no "this elegant mechanic," no design
  philosophy intrusions
- **In second person for player-facing instructions** — "you roll," not
  "the character rolls"
- **With radical compression** — one paragraph, one rule; one sentence
  if the rule allows it

The rules voice has five manuscript registers: pure rules, mixed bridge
(world truth and game operation in the same sentence), item description,
example scene, and flavor exposition. See `references/rules-voice.md`
for the complete game-designer persona, paragraph shapes, multi-rule
sequence writing, progressive disclosure architecture, and the
submission checklist.

## The Literary Tradition

This voice draws technique from eight modern literary lineages. Use the
techniques to solve sentence and scene problems; do not mimic a living author's
distinctive voice or reproduce recognizable passages.

The authors analyzed in this skill define the general manuscript
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
- **Economic pressure, craft, survival mechanics** → Parker + Cornwell +
  Le Guin
- **Mercenary company, contracted violence, hired sword** →
  `references/author-abercrombie.md` + `references/author-glen-cook.md`
- **Vignette or epigraph** → Kay + Sapkowski
- **Rules prose, game example scenes, chapter structure** →
  `references/rules-voice.md`
- **Humanizing or auditing a draft** → anti-AI humanizer first

## Bundled References

- `references/anti-ai-humanizer.md`
  55 named AI writing patterns, each with AI example, human fix,
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
  Three tests: Quick Scan (14 highest-frequency patterns, binary,
  under 2 minutes), Full Pass (all 55 patterns with scoring
  thresholds), Author Lens Check (per-register positive and negative
  signals). Use as the final gate before integrating prose.

## Write for Play

Manuscript prose must help someone decide, imagine, or act. Give each passage a
job:

- teach a procedure
- reveal a usable fact
- establish a concrete situation
- distinguish a person, place, object, or threat
- present a cost, opportunity, or uncertainty
- show the consequence of a rule

Cut lore summary, atmosphere, or design commentary that performs none of these
jobs.

### Sandbox-facing prose

Write situations with unresolved pressure. Present:

- what is visibly happening
- what each actor wants
- what constrains them
- what can be learned or changed
- what worsens with time

Do not predict player choices, name the correct moral answer, protect a planned
scene, or state that the adventurers “must” act unless a rule literally compels
them.

Write GM-facing secrets as causes and response logic, not as plot beats. Prefer:

> If the miller is exposed, Yawim closes the east road and offers the grain to
> the Rust Brothers.

Avoid:

> After the adventurers expose the miller, they will confront Yawim in the
> climactic scene.

### Information prose

Separate:

- observable fact
- common belief
- speaker's claim
- GM truth
- mechanical effect

Do not let omniscient narration erase uncertainty intended for play. Rumors
should identify a source and a concrete claim. Clues should suggest a preparation
or question without announcing the hidden mechanic.

### Rules examples

An example should settle a real ambiguity. Include:

1. fictional position
2. player intent
3. rule invoked
4. dice or cost
5. outcome
6. changed situation

Do not make the example merely repeat the preceding rule with names attached.

### GM guidance

Give criteria and an operation:

> When another Myth could clarify the text's language, symbols, author, or
> subject, the GM may let it help; add only the highest directly relevant Myth
> Die.

Avoid vague permission such as “the GM may adjust this as needed” unless the text
also names the relevant factors and limits.

## Hard Rules

1. **Load the anti-AI humanizer before submitting any draft.** Run
   the 55-pattern diagnostic. Not a suggestion.

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
   `skills/forbidden-lands-lore/references/tone.md`.

5. **Abercrombie and Cook techniques suit the mercenary company voice.**
   For individual author technique: `references/author-abercrombie.md`
   and `references/author-glen-cook.md`.
   Neither is the general manuscript voice.

## Companion Skills

- `skills/forbidden-lands-lore/SKILL.md` — setting authenticity,
  tonal classification, encounter anti-tropes
- `skills/forbidden-lands-bestiary/SKILL.md` — encounter design
  and monster construction
- `skills/forbidden-lands-design/SKILL.md` — mechanics, player
  experience, sandbox procedures, and supplement architecture
