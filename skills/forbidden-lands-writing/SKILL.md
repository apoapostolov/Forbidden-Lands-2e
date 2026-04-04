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
