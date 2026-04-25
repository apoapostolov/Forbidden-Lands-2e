---
name: forbidden-lands-writing
description: |
  Use when drafting, revising, or auditing any prose for the Forbidden
  Lands 2E manuscript — fiction vignettes, rules text, worldbuilding
  passages, item and spell descriptions, flavor exposition, example
  scenes, proposals, and mixed fiction-and-rule bridges. Covers the
  literary techniques of six authors whose combined practice defines the
  target voice, the complete manuscript register and paragraph system,
  the 43-pattern anti-AI humanizer, composite voice synthesis, sentence
  architecture, dialogue mechanics, sensory vocabulary, worldbuilding
  voice patterns for history, gods, kin, and oral register, and all
  revision calibration tools. Load when writing village scenes,
  vignettes, encounter fiction, NPC introductions, epigraphs, or any
  prose where generic AI output would be detected immediately. Also load
  when humanizing or auditing a draft that reads generated.
---

# Forbidden Lands Writing

This skill exists because AI cannot write good roleplaying-book
prose by default. It produces something that looks like prose —
grammatical, organized, superficially tonal — but reads like
a summarization of a book rather than a page from one.

The Forbidden Lands manuscript was written by experienced
authors who thought in body, weather, iron, danger, and use.
Their prose is not decorated. It is built. Every sentence does
a job: it teaches a rule, grounds the world, or moves the reader
closer to the table.

This skill teaches you to match that standard, not approximate it.

## The Problem This Skill Solves

AI writing fails in roleplaying books in three stacked ways:

1. **Surface voice.** The AI produces "dark fantasy flavor" — shadow,
   whisper, ancient power, grim destiny — without physical grounding.
   The result is mood fog that teaches nothing and feels generic.

2. **Structural flattening.** The AI writes every paragraph the same
   way: topic sentence, elaboration, softened conclusion. Real
   manuscript paragraphs have shape — statement then consequence,
   definition then procedure then exception, condition then pressure
   then player response. The AI's paragraphs are interchangeable.
   The manuscript's paragraphs are not.

3. **Invisible AI tells.** Even when the AI avoids obvious slop,
   it leaks: em-dash overuse, rule-of-three padding, copula
   avoidance ("serves as" instead of "is"), elegant variation
   (cycling synonyms to avoid repetition), negative parallelisms
   ("not just X, but Y"), hedging stacks, and generic positive
   conclusions. These are detectable and they break trust.

This skill attacks all three layers.

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

| Author | Primary Contribution |
|---|---|
| Andrzej Sapkowski | Monster-as-contract, village ecology, fable structure, Eastern European pre-Christian daily religion |
| Guy Gavriel Kay | Elegiac register, sacred geography, long memory, soft Tolkienesque poetic inheritance |
| K.J. Parker | Pre-industrial craft authenticity, economic realism, unreliable pragmatist narrator, dark comedy |
| Ursula K. Le Guin | Anthropological village authenticity, absence as presence, ecological specificity, the unhurried sentence |
| Bernard Cornwell | Dark Ages physical survival, food and weather as constant pressure, first-person pragmatist, no clean heroes |
| John Gwynne | Norse/Dark Ages oath culture, body-first narration, shield-wall perspective, physical grief |
| Joe Abercrombie & Glen Cook | Band of brothers, mercenary company voice, contracted violence, grimdark moral neutrality, character through habit |

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
- **Economic pressure, craft, survival mechanics** → Parker + Cornwell + Le Guin
- **Vignette or epigraph** → Kay + Sapkowski
- **Mercenary company, band-of-brothers, hired-sword** →
  `fiction-voice-abercrombie-cook.md`
- **History, gods, kin, or oral register prose** →
  Worldbuilding Voice section below + `manuscript-style-analysis.md`
- **Calibrating a draft against the manuscript** →
  `rewrite-calibration-examples.md` + `manuscript-style-analysis.md`
- **Rules text, mixed bridge scenes, example scenes** →
  `writing-manual.md` + `corpus-map-and-registers.md`
- **Humanizing or auditing a draft** → anti-AI humanizer first

## Source Of Truth

Read before drafting:

- `WRITING_GUIDE.md` — the short operational style authority
- `AGENTS.md` — repo handling rules and voice rules

When working in a chapter or proposal folder, also read the
local `AGENTS.md` if present.

For substantial drafting or revision, load the bundled references.

## Bundled References

Load on demand. Do not load all at once unless the task
requires deep multi-register work.

### Anti-AI and Diagnostic Tools

- `../forbidden-lands-writing-voice/references/anti-ai-humanizer.md`
  **The canonical 43-pattern anti-AI library.** Each pattern has an
  AI example, human fix, Forbidden Lands application, and the author
  model that never does it. Also contains the 7-layer failure
  taxonomy, author-specific evasion techniques, the full diagnostic
  checklist, and the revision protocol. **Load this first when
  auditing or humanizing a draft. When any pattern description here
  conflicts with `writing-manual.md` or `diction-voice-and-anti-style.md`,
  this file takes precedence.**

- `references/diction-voice-and-anti-style.md`
  **Manuscript lexical identity and FL-specific anti-patterns.**
  Load for: word fields by domain (body, material, travel, survival,
  culture), verb preferences, modifier discipline, punctuation
  restraint, and Forbidden Lands-specific anti-patterns not in the
  general humanizer. The pattern detection list here overlaps with
  `anti-ai-humanizer.md` — the humanizer is the authoritative count
  and format; this file is supplementary for the manuscript-specific
  lexical rules.

- `../forbidden-lands-writing-voice/references/voice-test-protocol.md`
  Three tests: Quick Scan (13 highest-frequency patterns, binary,
  under 2 minutes), Full Pass (all 43 patterns with scoring
  thresholds), Author Lens Check (per-register positive and negative
  signals). Use as the final gate before integrating prose.

### Author Technique References

- `../forbidden-lands-writing-voice/references/composite-voice.md`
  How the six authors combine into one working voice. Priority
  hierarchy when techniques conflict. Register map by scene type.
  Worked examples of the composite voice applied to FL2E scenes.
  Anti-patterns of misapplication.

- `../forbidden-lands-writing-voice/references/author-sapkowski.md`
  Andrzej Sapkowski: techniques, sentence architecture, the false
  threshold structure, fable frame, monster-as-contract, dialogue
  as duel, the price mechanism, pre-Christian ecology.

- `../forbidden-lands-writing-voice/references/author-kay.md`
  Guy Gavriel Kay: techniques, elegiac omniscience, sacred geography,
  long memory, the "last time" marker, death in subordinate clauses,
  song as structure, parallel construction as emotional intensifier.

- `../forbidden-lands-writing-voice/references/author-parker.md`
  K.J. Parker: techniques, the unreliable pragmatist narrator,
  technical procedure as character, economics as plot, institutional
  characters, dark comedy through incongruity.

- `../forbidden-lands-writing-voice/references/author-leguin.md`
  Ursula K. Le Guin: techniques, thick description, custom over drama,
  gift economies as worldbuilding, absence as presence, the unhurried
  sentence, ecological specificity.

- `../forbidden-lands-writing-voice/references/author-cornwell.md`
  Bernard Cornwell: techniques, food and weather as constant pressure,
  first-person survivor narration, the loyalty test, tactical
  geography, death without ceremony.

- `../forbidden-lands-writing-voice/references/author-gwynne.md`
  John Gwynne: techniques, body-first narration, oath as narrative
  spine, shield-wall perspective, grief as physical, oral-culture
  tells, the named object.

- `references/fiction-voice-abercrombie-cook.md`
  **The mercenary company fiction voice.** Deep literary analysis of
  Glen Cook and Joe Abercrombie techniques, how the 25 Band Life
  vignettes synthesize them, and operational rules for replicating
  the style: POV, sentence targets, dialogue mechanics, emotion
  budget, violence rendering, anti-patterns, and a diagnostic
  checklist. **Load when writing mercenary band characters,
  contracted violence, company hierarchy scenes, or any prose
  operating in the hired-sword register.**

### Sentence, Dialogue, and Sensory Craft

- `../forbidden-lands-writing-voice/references/sentence-architecture.md`
  Per-author sentence profiles, the Forbidden Lands target sentence,
  rhythm techniques, variation strategies, and diagnostic questions.

- `../forbidden-lands-writing-voice/references/dialogue-mechanics.md`
  Per-author dialogue profiles, oral-culture sentence patterns,
  dialect without parody, silence between lines, implied conversation,
  tags, attribution, and when to skip dialogue entirely.

- `../forbidden-lands-writing-voice/references/sensory-vocabulary.md`
  Priority sense hierarchy, weather as character, food as
  worldbuilding, body as consciousness, sound before sight, specific
  vs. generic decision tree, master vocabulary lists by environment
  type.

### Manuscript Calibration

- `references/writing-manual.md`
  **The unified manuscript-specific synthesis.** Voice identity, the
  six registers, fiction craft, emotional intelligence, paragraph
  architecture, sentence craft, diction, rules prose, item/equipment
  prose, mixed bridges, example scenes, and revision method — all
  applied to this manuscript specifically. Contains its own anti-AI
  pattern list (a shorter derivative set). When those patterns
  conflict with `anti-ai-humanizer.md`, the humanizer takes
  precedence. Load for any non-trivial drafting.

- `references/manuscript-style-analysis.md`
  Forensic analysis of original author techniques. Passage-level
  breakdowns of why specific manuscript prose works. Load when
  studying the originals or calibrating voice.

- `references/corpus-map-and-registers.md`
  Chapter voice map and retrieval guide. Where to find exemplars
  by task, what each chapter teaches about voice, and what to watch
  for when imitating each register. Load when choosing what to read
  before drafting.

- `references/paragraph-sentence-and-structure-metrics.md`
  Measured chapter averages for paragraph and sentence length.
  Per-register targets and structural signals to watch. Load when
  checking whether a draft fits its chapter.

- `../forbidden-lands-writing-voice/references/register-contrastive.md`
  Same scene (arrive at dark village, gate barred, no dogs, no fire)
  rendered in all six author registers with cross-register notes.
  Use when checking whether a passage sounds like the named register
  or has drifted.

### Worked Examples

- `references/rewrite-calibration-examples.md`
  Ten before-and-after pairs across all six registers.
  Gear, injury, proposal, fiction, spell, culture, bridge,
  talent, journey, and item rewrites with change notes.
  Load when calibrating revision choices.

- `../forbidden-lands-writing-voice/references/worked-examples.md`
  13 wrong/correct pairs targeting the 13 highest-frequency AI
  patterns. Quick Diagnostic checklist. Use when an abstract
  rule is not landing — read the correct example, not the rule.

- `references/multi-rule-sequence-calibration.md`
  Combat, journey, and recovery sequence examples. How to write
  playable multi-rule scenes that teach through consequence, not
  through annotation. Load when writing example scenes that chain
  multiple rules.

- `references/rules-onboarding-and-progressive-examples.md`
  Progressive rule examples. How to teach a rule through graduated
  scenario examples that assume increasing table familiarity.

### World Vocabulary

- `../forbidden-lands-writing-voice/references/world-vocabulary.md`
  Setting-specific vocabulary rules. How the three human peoples
  name themselves in speech, thought, and writing. Non-human kin
  speech patterns. Divine names in use by tradition. Currency and
  economic vocabulary. Social rank terms. Place names. Register
  rules by culture. Forbidden vocabulary.

### Setting (Redirect)

- `references/setting-ravenland-and-human-peoples.md`
  **Moved to the `forbidden-lands-lore` skill.** Load that skill
  when writing or revising fiction that involves place names,
  character nationality, or kin identity. The lore skill owns all
  setting-authenticity concerns.

## Hard Rules

These are non-negotiable. Violating any one disqualifies
a draft from the manuscript.

### Framework Rules

1. **Load the anti-AI humanizer before submitting any draft.** Run
   the 43-pattern diagnostic in
   `../forbidden-lands-writing-voice/references/anti-ai-humanizer.md`.
   Not a suggestion.

2. **Choose an author register for each scene.** Name it before
   writing: "This scene is Cornwell-primary with Le Guin texture."
   Mixed registers without a named primary always produce generic
   output.

3. **Physical before atmospheric.** Every scene opens on a body doing
   a physical thing in a specific place. Weather, mood, and theme
   enter through that body, not before it.

4. **The monster is a contract. The relic has a price. The faction
   is partly right.** These are structural constraints built into the
   lore. See `skills/forbidden-lands-lore/references/tone-and-encounter-design.md`.

### Manuscript Rules

1. **No mood without object.** Every atmospheric sentence must
   contain a physical noun — a body part, a material, a tool,
   a terrain feature, a weather condition. "Darkness gathered"
   is banned. "The cold crept through the seams of his mail"
   is allowed.

2. **No paragraph without a job.** Before writing a paragraph,
   name its job in one word: define, describe, distinguish,
   warn, demonstrate, bridge. If you cannot name the job,
   do not write the paragraph.

3. **No AI tells.** Run a final pass for: em-dash clusters,
   rule-of-three, copula avoidance, elegant variation,
   negative parallelisms, hedging stacks, sycophantic
   qualifiers, filler phrases, and generic positive endings.
   If any survive, cut them.

   **Split-sentence negative:** The pattern "It is not X. It
   is Y." is a hard AI tell. Two short sentences, first a
   negation, second the correction. Humans do not write this
   way. It reads like a generated clarification — mechanical,
   bloodless, obvious. Collapse it every time:
   - "It is not X. It is Y." → "It is not X, but Y."
   - "It is not a bank. It has no ledger." → "It is not a
     bank — no lock, no ledger, no one to answer to."
   - "This is not a rule. It is a consequence." → "This is
     not a rule, it is a consequence that follows from the
     world's logic."
   Any two-sentence pair where the first sentence negates
   and the second corrects must be collapsed into one sentence
   or rewritten in a form that does not lean on the negation
   as a structural device.

4. **No synonym cycling.** If the game calls it Willpower,
   call it Willpower. Do not write "mental reserves" in one
   sentence and "inner fortitude" in the next. Repetition is
   cleaner than variation when the repeated word is a game term.

5. **No therapy, no corporate, no blog.** The manuscript does
   not say "meaningful," "impactful," "engage with," "it's
   worth noting," "basically," "in other words," "this means
   that," or "the key takeaway." These phrases are invisible
   to the AI that writes them and loud to every human who
   reads them.

6. **End on weight.** Sentences should land on concrete nouns,
    bodily consequences, hard verbs, or material facts. Trailing
    qualifiers, abstract summaries, and "voicey" filler at
    the end of a sentence are the most reliable sign of
    generated text.

7. **Earn every adjective.** One strong noun beats two
    modified ones. "The blade" beats "the sharp, gleaming
    blade." If an adjective does not change what the reader
    pictures, it is decoration and should be cut.

8. **No game designer jargon.** Terms like "critical riders,"
    "proc," "tuned," "feature effects," and similar design-layer
    vocabulary are internal shorthand. They do not belong in
    manuscript prose. Replace them with plain description of what
    happens at the table: not "critical riders" but "what the
    talent does when the attack connects." "Trigger" is
    acceptable plain English and may stay. "On-hit effects" is
    borderline — it reads technical; prefer "what happens when
    the attack connects" or "what the talent does on a hit."
    If a reader would need to know design theory to understand
    a sentence, the sentence is wrong.

9. **No AI guardrail sections.** Do not introduce a section
    labeled "GUARDRAILS," "Safety Note," "Content Warning," or
    any equivalent. These are AI safety framing conventions and
    read as generated text. If the rule has genuine edge cases
    the GM needs to handle, write them as GM advice embedded
    inside the rule itself — a short sentence beginning with
    "The GM" or "The GM decides," placed where the concern
    actually arises. Not a separate block before or after the
    rule. Not a titled section. A sentence.

## Writing Workflow

1. Identify the register: fiction opener, flavor exposition,
   rules explanation, mixed bridge, item description,
   example scene.
2. Pull 2-5 exemplars from the relevant chapter.
3. Draft with one paragraph job at a time.
4. Check diction: concrete subjects, physical verbs,
   material nouns, no abstract filler.
5. Check structure: paragraph shape matches its job,
   sentence length varies with purpose.
6. Run anti-AI pass: scan for the tells listed in Hard
   Rule 3 and in the anti-style reference.
7. Read the draft aloud. If a sentence sounds like
   a summary of a book rather than a page from one, rewrite.

## Review Checklist

Before finalizing any draft:

- [ ] Could this paragraph sit beside the manuscript
      without sounding imported?
- [ ] Does every atmospheric line contain a physical noun?
- [ ] Does every paragraph do one job?
- [ ] Do sentences end on weight, not filler?
- [ ] Are game terms used consistently, not varied?
- [ ] Is every adjective earned?
- [ ] Has the anti-AI pass been run?
- [ ] If this is rules text, can it be run at the table
      without interpretation drift?
- [ ] If this is flavor text, does it still point toward
      use, danger, or consequence?
- [ ] Does the draft contain any designer jargon (riders,
      triggers, on-hit effects, procs, tuned)? Replace
      each with plain table-language.
- [ ] Does the draft contain a GUARDRAILS, Safety Note,
      or Content Warning block? Break it up and embed
      any genuine GM guidance as short in-rule sentences.

## Worldbuilding Voice: History, Kin, and Gods

This section is for writing and evaluating world-facing content — history
passages, god descriptions, kin profiles, cultural detail, in-world quotes,
folk sayings, and founding myths. It derives from forensic analysis of
`02-gamemasters-guide/03-history.md`, `04-gods.md`, and `05-kin.md`.

These chapters are not lore documents. They are operational world tools that
a GM needs to run a campaign starting tonight. Every stylistic choice serves
that function.

---

### History as Survival Chronicle

The Forbidden Lands history chapter does not narrate a heroic story. It
records a chain of practical failures: food shortages, religious wars, a
drunken dwarf's victory banquet, a demon that got homesick. The prose
treats these causes without irony *markers* — there is no "ironically"
or "sadly" — because the irony is carried entirely by the juxtaposition of
stated cause and actual consequence.

**Pattern: mundane cause, epic consequence, no comment.**

The Blood Mist lifted because a demon was seduced by homesickness from a
bard's songs and turned to cannibalism. This is stated in one paragraph
without exclamation. The sentence reads: "Such was their killer instinct
that they could not refrain from cannibalism." The paragraph ends. This
is the technique. Do not explain why this is remarkable.

**Pattern: named character, role first, then name.**

Write "the dwarven lord Garmar Four-Beard" not "Garmar Four-Beard, a
dwarven lord." Role before name. This applies to all historical figures:
"the priestess Jamharda," "the sorcerer Zygofer," "the bard Merigall."
Role first, always.

**Pattern: dates and durations compress rather than summarize.**

"820-821 AS" carries more weight than "after a year of bitter fighting."
Dates do not explain; they bound. The reader can calculate that the first
Alder War lasted one year. They do not need to be told it was brief.

**Pattern: dark acts in procedural tone.**

"When he turned her down, she had him killed, brought him back to life
with her necrokinetics, and took his dead body for a lover." Three
comma-separated events. No horror adjectives. No moral framing. The horror
is the list; the grammar is doing the work. If your sentence about a
terrible act contains the word "horrifying," "terrifying," "unspeakable,"
or "chilling," you have failed this pattern.

**Pattern: historic quotes carry attribution, role, and date.**

> ETARIK HAMMERHAND, ambassador from the Merromannians to Alderstone, 833 AS

Three pieces of information: who said it, what their specific role was at
the moment they said it, when they said it. The date is 332 years before the
game's present. This temporal distance is not decorative; it says that this
insult has been true for over three centuries.

---

### Gods as Faction Definitions

A god in this world is not a theology. A god is defined by three facts:
what the followers believe the god *is*, what material things they hold
sacred, and what they do to people who believe otherwise.

**Never describe a god abstractly first.**

Describe the physical rite, then the belief, then the faction behavior.
The gods chapter opens with the Rust Lord Kartorda nude among iron chains,
being stained rust-brown for a coming human sacrifice. This is the first
sentence about gods. Not "the god Rust is worshipped by the Iron Guard."
A body, chains, staining, the preparation. Then the belief follows.

**Material holiness is specific and grounded.**

- The Rust Brothers swing chains with balls of burning coals. Rusty iron
  is more effective against demons than clean iron. The figurines cannot
  be too detailed or it insults the gods' perfection.
- The Congregation of the Serpent keeps a library. Their symbol is an
  ouroboros snake biting its own tail.
- Raven Sisters move constantly, always on guard, because there are
  informants everywhere and the Rust Brothers pay for captured sisters.
- The god Clay's followers create clay objects for ritual. Clay and soil
  are divine substances.

The material objects are not symbolic. They are operational — they tell
the GM what the NPCs carry, what they build, what they fear. Write gods
so that every paragraph could arm an encounter.

**Multiple contradictory interpretations of the same deity are not
resolved.**

The Protector god is Wyrm (the Congregation), Raven (the Raven Sisters),
and Rust (the Rust Brothers). The text does not propose a reconciliation
or suggest which is correct. It describes the three camps and notes they
are "deeply hostile towards one another." This is the model. Do not tidy
theological contradictions. The contradiction *is* the world fact.

---

### Kin as Survival Ecologies

People in the Forbidden Lands are defined by what they do to survive, not
by who they claim to be. The first fact about human villagers is that they
kill their elderly when they can no longer contribute. This is stated plainly:
"It is viewed as unavoidable but sad and is usually accepted by the victims."
This is the baseline register for all human cultural writing in this book.

**Cultural identity lives in behavior, not self-description.**

Do not write "the Galdanes are a proud, nomadic people." Write what they
do: they drink too much, go back and forth between wanting to fight and
weeping and singing sad songs, hate fences and walls as an expression of
contempt for farmers who divide land that should belong to everyone. The
culture is in the behavior.

Concrete behavioral details from the text:

- Alderlanders wear alder branches during festivals and keep them as
  sacred heraldry
- Quards braid hair (both men and women), wear earth-tone clothes with
  field patterns, prefer gold and bronze over silver
- Redrunners carry dried starfish, flowers, and star-shaped jewelry in
  red — because their name comes from the red wandering star that bore
  the first elves
- Dwarves cultivate troll excrement to extract rare minerals
- Elves can rearrange the darker sap in their bodies to create skin
  patterns — neither cut nor painted — as an art form

Each of these is a physical act or material object. None are character
traits described abstractly.

**Social structure is clan, priestly, and martial — not feudal.**

The present-day Forbidden Lands has no lords, no kings, no feudal titles
in active use. There are clan warlords (Tormund Halfhand, King Karonax),
priesthoods (the Raven Sisters, the Rust Brothers, the Congregation of
Serpents), druidic orders (the Golden Bough, the Order of Maidens), and
knightly orders (the Iron Guard, the Redrunners). When writing settlement
NPCs and social friction, do not default to lord/peasant feudal vocabulary.
Default to the factional web: which priestly presence, which clan pressure,
which order's eyes are on this village.

**Undeath is a social phenomenon, not a horror event.**

"The living dead are a natural phenomenon in the villages since the deceased
often tend to keep walking about in a state of confusion before finding their
final rest. They are treated with respectful courtesy." Villages soothe the
restless dead with music and conversation, treating them like confused children.
The Rust Brothers remove them to turn into soldiers. This is the register: dead
are a village problem with social management protocols, not a jump-scare threat.
Write undead encounters from this angle: who manages the dead here, and what
has gone wrong with that management.

---

### The Oral and Poetic Register

Forbidden Lands world content circulates in-world as song, saying, folk
warning, and traveler's tale. When writing in this register, follow these
patterns.

**A folk song sounds like a real person singing it, not an author composing
atmosphere.**

The beggar from Varassa's song in the history chapter uses a refrain and
simple imagery: "walks and whispers," "walks and lures you in and whimpers."
It does not try to be beautiful. It tries to remember something true and
terrifying about the mountains, through the voice of someone who is cold
and scared. When writing a folk song, write what the specific person
singing it is afraid of, not what the author wants to evoke.

**An elvish saying uses three physical objects and a consequence.**

"Three things mortal hands cannot mend: broken birds' eggs, the heart ruby
and ravaged oaths between kin."

The pattern: a number, a list of physical or material objects in escalating
gravity, no verb in the conclusion. The saying does not explain. It lists.
The reader constructs the meaning. The punchline — dwarves mend eggs to
spite the elves — is delivered in the next sentence, in flat prose. The
joke lands because the saying was not set up to be funny.

**A historical quote from a named NPC requires role and date.**

Not: *"Your kind does not belong here," said the dwarven ambassador.*

Yes: *"Your place is not here, everyone hates you and you do not even like
each other." — Etarik Hammerhand, ambassador from the Merromannians to
Alderstone, 833 AS*

The attribution earns the quote. The date carries the weight.

---

### The Soft Tolkienesque Technique

The founding myths of this world are poetic but not decorative. Each myth
has three components:

1. A physical cosmic object that explains origin
2. A consequence the believer can act on
3. A mechanical reality at the table

**Dwarves:** The sun is the fire in Huge's forge. Their goal is to reach
it by expanding the earth until they do. All clans want to reach it first
to secure the best seats at his table. — The myth explains the meritocracy,
the inter-clan rivalry, and the daily work of world-expansion. The believer
acts on it every morning at the forge.

**Elves:** Rubies fell like seeds from the wandering red star to guide
confused life toward higher purpose. Elves renew themselves from their
rubies. If the ruby is destroyed, the elf is gone forever. — The myth is
also the game mechanic. The ruby grows like a pearl in an oyster. This is
poetry that the GM can act on: the ruby is a target, a commodity, a person.

**Horses of Aslene:** Ancient horses galloped from the volcano Horn with
manes aflame at the dawn of time. Fire comes from Horn. — The myth explains
why Quards light huge fires at festivals and why a prophet identifying a
sorcerer as Horn's chosen savior draws pilgrims. The physical image (manes
aflame) is the covenant between myth and behavior.

The technique: **state the myth in the believer's voice, not the narrator's.
Ground it in a physical object. Show the behavior it produces.**

Do not write: "According to elven mythology, their souls originate from
a celestial source." Write: "The elves say the rubies fell like seeds from
the wandering red star, to guide the confused life of the world towards
a higher purpose."

The first is a summary. The second is someone speaking.

---

### The Swedish/Nordic Tonal Signature

This is the hardest to teach and the easiest to violate. The following
passages are exemplars of the tone. Read them and then read your draft.
If your draft sounds warmer or more moralized, revise.

**The deadpan atrocity list:**
"Therania had grown tired of the cold embrace of the dead king Algarod and
suggested that the reanimated corpse should be sent to command the fortress
at Weatherstone, and so he was."
One sentence. Past tense. "And so he was." No dramatic weight. The sentence
does not feel the horror it describes because the text is not trying to make
you feel the horror. The horror is in the information.

**The procedural cruelty:**
"Garmar Four-Beard, drunk on power and alcohol, had the priestess thrown on
a bed of hot coals during the victory banquet at Lumra, to bake her like a
shellfish. He swore to eat her heart himself after it had been tenderized
into submission."
There is dark comedy here. "Tenderized into submission" is almost a recipe.
The text does not apologize for the comedy. The comedy comes from the
precision, not from mockery.

**The flat disproof:**
"The entire legend is false."
After a full paragraph founding myth for the Crombe dwarves (complete with
divine hammer, slain dragon-mother, fortress built from dragon ribs), this
is the entire next paragraph. Three words. No explanation follows
immediately. The text continues with what actually happened. This is a
writing choice, not a fact-delivery choice. It signals that the world
contains people who believe things that are wrong, and that the text is
comfortable being right without performing being right.

**The practical relationship to death:**
"Killing people who can no longer contribute due to age or frailty is not
uncommon. It is viewed as unavoidable but sad and is usually accepted by the
victims as a better alternative than being forced to venture out from the
village on their own."
No moral judgment. No authorial distance marker ("it must be noted" or "this
disturbing practice"). The sentence treats this as a management fact of
pre-feudal survival life. The observation that "victims" usually accept it
is delivered as a practical note, not as horror.

**The operating rule:** In this world, cruelty, death, dark humor, and
practical atrocity are reported in the same register as weather and harvest.
The reader's emotional response is not managed by the text. The text provides
the fact; the reader provides the reaction. Write everything at the same
temperature.
