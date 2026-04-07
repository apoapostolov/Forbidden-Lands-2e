---
name: forbidden-lands-writing
description: |
  Use when drafting, revising, or reviewing manuscript-facing prose for the
  Forbidden Lands 2E repo. Applies the voice, structure, diction, and
  anti-AI rules so prose reads like native fiction and practical rulebook
  text — harsh, clear, physical, atmospheric, and free of generated-text
  tells. Covers corebook chapters, proposal prose intended for promotion,
  item and spell descriptions, flavor exposition, examples, and mixed
  fiction-and-rule bridges.
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

- `references/fiction-voice-abercrombie-cook.md`
  The fiction voice authority. Deep literary analysis of
  Glen Cook and Joe Abercrombie techniques, how the 25
  Band Life vignettes synthesize them, and operational
  rules for replicating the style: POV, sentence targets,
  dialogue mechanics, emotion budget, violence rendering,
  anti-patterns, and a diagnostic checklist. **Load first
  for any fiction drafting — vignettes, epigraphs,
  character scenes, or proposal fiction previews.**

- `references/setting-ravenland-and-human-peoples.md`
  **Moved to the `forbidden-lands-lore` skill.** Load that
  skill when writing or revising fiction that involves place
  names, character nationality, or kin identity. The lore
  skill owns all setting-authenticity concerns.

- `references/writing-manual.md`
  The unified writing authority. Voice identity, register
  system, paragraph and sentence rules, diction, fiction
  craft, anti-AI pattern library, emotional intelligence,
  revision method. Load this for any non-trivial drafting.

- `references/manuscript-style-analysis.md`
  Forensic analysis of original author techniques. Passage-
  level breakdowns of why specific manuscript prose works.
  Load when studying the originals or calibrating voice.

- `references/diction-voice-and-anti-style.md`
  The anti-AI bible for this manuscript. 30+ concrete AI
  writing patterns mapped to Forbidden Lands-specific fixes.
  Word-field inventories, verb preferences, and contrastive
  revision rules. Load when cleaning or auditing prose.

- `references/corpus-map-and-registers.md`
  Chapter voice map and retrieval guide. Where to find
  exemplars by task, what each chapter teaches about voice,
  and what to watch for when imitating each register.
  Load when choosing what to read before drafting.

- `references/paragraph-sentence-and-structure-metrics.md`
  Measured chapter averages for paragraph and sentence length.
  Per-register targets and structural signals to watch.
  Load when checking whether a draft fits its chapter.

- `references/rewrite-calibration-examples.md`
  Ten before-and-after pairs across all six registers.
  Gear, injury, proposal, fiction, spell, culture, bridge,
  talent, journey, and item rewrites with change notes.
  Load when calibrating revision choices.

- `references/multi-rule-sequence-calibration.md`
  Combat, journey, and recovery sequence examples. How to
  write playable multi-rule scenes that teach through
  consequence, not through annotation. Load when writing
  example scenes that chain multiple rules.

## Hard Rules

These are non-negotiable. Violating any one disqualifies
a draft from the manuscript.

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
