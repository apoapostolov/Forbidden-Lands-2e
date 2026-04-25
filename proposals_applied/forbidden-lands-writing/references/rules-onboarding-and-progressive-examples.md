<!-- markdownlint-disable MD013 -->

# Rules Onboarding and Progressive Examples

## Purpose

This reference teaches how to introduce complex or comprehensive subsystems to readers who may be encountering them for the first time. It covers the architecture of rules presentation — how to layer mechanics progressively, how to use recurring characters in examples, and how to connect multiple examples into an interconnected narrative that reads like a single session of play.

Use this reference when:

- Writing or revising a chapter that introduces a multi-part subsystem (reputation, stronghold management, magic paths, journey procedures)
- Designing example sections that need to teach several interlocking rules
- Planning the order of rules presentation within a chapter
- Writing for readers who range from first-time players to experienced tabletop veterans

This reference complements `multi-rule-sequence-calibration.md`. That file teaches how to write a single multi-rule example well. This file teaches how to structure the surrounding chapter so the reader arrives at each example already equipped to follow it.

## The Core Problem

Complex subsystems fail readers in three ways:

1. **Front-loading.** All definitions, tables, and exceptions appear before any example of play. The reader memorizes nothing because nothing has context yet.

2. **Scattered examples.** Each rule gets its own isolated example with its own characters and situation. The reader cannot build momentum because every example resets the world.

3. **Expert-only ordering.** Rules are presented in the order the designer thinks about them (taxonomy first, exceptions second, play last) rather than the order a player would encounter them at the table (trigger first, decision second, consequence third).

The solution is progressive disclosure with narrative continuity.

## Progressive Disclosure

### The Principle

Teach the simplest usable version of the rule first. Then add layers. Each layer answers a question the reader is already asking because the previous layer raised it.

### The Pattern

**Layer 1: The core loop.** What does the player do, what does the GM do, what happens? This should be one paragraph, maybe two. No exceptions, no edge cases, no modifiers. Just the spine.

**Layer 2: The first example.** A short scene that walks through the core loop with named characters. The reader sees the rule in motion before encountering any modifiers or exceptions.

**Layer 3: Modifiers and common variations.** Now that the reader knows the base case, introduce the factors that shift it — tables, conditions, situational bonuses. These make sense now because the reader has a mental model to attach them to.

**Layer 4: The richer example.** A second scene, using the same characters or the same situation, that demonstrates the modifiers in practice. This example should feel like a natural continuation — the same session, the same journey, the same fight — not a fresh scenario.

**Layer 5: Edge cases and GM advice.** Corner cases, optional rules, and guidance for unusual situations. These come last because only readers who have absorbed the base system will need them.

### What This Looks Like In Practice

Bad order (front-loaded):

```text
Definition → Full modifier table → Exception list → Edge cases → Example
```

The reader drowns before reaching solid ground.

Good order (progressive):

```text
Core mechanic → Short example → Modifiers → Richer example → Edge cases
```

The reader stands on each layer before the next is added.

### Gauging Depth By Audience

Not every reader needs every layer. Structure the text so that:

- A beginner can read Layer 1 and Layer 2, then start playing. The example carries enough of the rule to get through the first session.
- An intermediate player reads through Layer 4 and understands the full working system with modifiers.
- An experienced GM reads Layer 5 for the edges, the advice, and the design reasoning.

This does not mean labeling sections "beginner" or "advanced." It means ordering the text so that a reader who stops early still has a working version of the rule.

## Recurring Characters In Examples

### Why Recurring Characters Work

The strongest teaching examples in tabletop RPG books use the same characters across a chapter or across the book. This works for three reasons:

1. **Reduced setup cost.** The reader already knows Tyrgar is a fighter, Siga is a druid, Heme is the talker. Each new example starts mid-stride instead of spending a paragraph introducing fresh characters.

2. **Cumulative stakes.** When the same character gets hurt in the combat example, struggles with a healing timer in the recovery example, and limps into a village in the reputation example, the reader feels the continuity that actual play produces.

3. **Character voice as mnemonic.** Readers remember "the time Garmelda talked the guards into opening the gate" better than "the example where the spokesperson rolled MANIPULATION with a +1 modifier." Named characters anchor abstract mechanics in memory.

### How To Use Them

- **Establish the cast early.** The first example in any major subsystem should name 2-4 characters and give each one a sentence of identity: profession, weapon, visible trait, or role in the fellowship. Do not describe them in a character-sheet format. Describe them the way another character would notice them.

- **Keep identities stable.** If Tyrgar fights with a broadsword in the combat chapter, he fights with one in the journey chapter too. If Garmelda is the spokesperson, she speaks in the reputation examples. Consistency teaches role differentiation without stating it.

- **Let characters accumulate consequences.** If Siga took a critical injury in Chapter 6, the Chapter 8 journey example can mention that she is still healing. This teaches the reader that conditions persist across subsystems without requiring a lecture about it.

- **Limit the cast.** Three to five recurring characters is enough. More than that, and the reader starts confusing them. Fewer, and the examples cannot show role differentiation.

### What To Avoid

- Do not write character backstories. A name, a profession, a weapon, and a visible trait is the maximum introduction. "Garmelda, a wolfkin with a raven's voice and a long knife" is enough for a lifetime of examples.
- Do not force every example to use every character. Let characters appear when their role matters.
- Do not kill a recurring character in an example unless the death teaches a rule that requires it.

## Interconnected Narrative Examples

### The Principle

When a subsystem spans several sections — each with its own rules — the examples across those sections should feel like scenes from the same session of play. The reader follows a single narrative thread and encounters each new rule as the characters encounter it.

### The Pattern

1. **Example A** introduces the fellowship arriving at a new place. It teaches the first-impression or arrival mechanic.

2. **Example B**, two sections later, picks up where A left off. The fellowship is now inside the settlement. It teaches recognition, reputation rolls, or social leverage — whatever the next rule in the chapter is.

3. **Example C** follows the consequences. A deal is struck, a favor is asked, a price is paid. It teaches the downstream effects of the scores established in A and B.

The three examples, read together, feel like a single stretch of play: arrival, introduction, negotiation. Read separately, each still teaches its own rule. The interconnection is a bonus, not a dependency.

### How To Build The Thread

- **Plan the thread before writing individual sections.** Decide what the fellowship is doing across the whole chapter, then break the thread into example-sized pieces. Writing examples in isolation and hoping they connect produces disjointed narratives.

- **Use time transitions, not recaps.** Between examples, advance the fiction with a short bridge: "An hour later, the fellowship sits in the headman's hall." Do not summarize previous examples. The reader has already read them.

- **Let each example stand alone.** A reader who skipped Example A should still understand Example B. The interconnection enriches; it must not create a prerequisite chain.

- **Vary the stakes.** If Example A ends well (the gate opens), let Example B introduce friction (the locals are cold). If B goes poorly, let C show partial recovery. A narrative that is all success teaches nothing about failure. A narrative that is all failure teaches nothing about reward.

### Extended Example: A Reputation Thread

This is how a chapter introducing a local reputation system might thread its examples:

> **Section: First Impression** → Example shows the fellowship arriving at a fortified village at dusk. Garmelda speaks at the gate. The presentation modifiers apply. The gate opens under caution. The reader learns the first-impression roll.
>
> **Section: Being Recognized** → The example picks up the next morning. A merchant in the market recognizes Heme from a caravan escort last season. The recognition roll succeeds. The reader learns how prior deeds surface through Reputation scores.
>
> **Section: Leaning On Your Name** → That afternoon, the fellowship needs horses. Heme leans on the caravan folk's good memory. The Reputation roll grants a minor favor. The reader learns how Reputation converts into concrete benefit.
>
> **Section: Rumors** → A week later and three hexes south, the fellowship reaches a hamlet where nobody knows them. But a drover who passed through the fortified village has already mentioned the strangers who brought word of raiders on the north road. The hamlet's gate-guard heard the name. The reader learns how rumors carry Reputation forward.

Each example stands alone. Together, they trace one journey through four rules.

## Tested Approaches From Published RPGs

Several published games handle progressive rules teaching well. These patterns are worth studying — not copying, but understanding what makes them effective.

### Named Cast Across The Book

The strongest examples in tabletop RPGs use a small cast that appears across many chapters. The reader learns the rules by following what happens to people they have already met. The combat example's wounded fighter becomes the healing chapter's patient becomes the journey chapter's limping burden. Each appearance reinforces both the character and the rule chain.

This works because readers remember stories about people, not stories about systems. "Tyrgar broke his arm" sticks. "A sample character suffers a critical injury" does not.

### Conversation-Format Examples

Some games write examples as dialogue between a GM and players, with system commentary interspersed. This format works well for teaching procedures with decision points — the reader sees the moment of choice rather than just the outcome.

The risk is that dialogue examples become long. Keep them to 6-10 lines of dialogue at most. Use them for moments where the player's decision matters more than the mechanical result: "Do you push the roll?" is a better dialogue example than "Roll your Strength."

### One Full Session As Tutorial

Some games devote a chapter or a sidebar to walking through a condensed session — character creation, first scene, first roll, first combat, first downtime — as a continuous narrative. This is a strong onboarding tool for complete beginners. It answers the question "but what does actually playing this game feel like?" before the reader reaches the detailed rules.

This approach works best as a front-of-book section (Chapter 1 or a "How To Play" overview) rather than embedded in the reference chapters themselves.

### The Layered Sidebar

A sidebar next to a dense rules section can carry a running example that applies each paragraph of rules text to a concrete situation. The reader's eye moves between the rule and its application without either format burdening the other.

This works well for tables and modifier lists. The rule text presents the table; the sidebar tells the story of a character walking through it.

## Integration With Multi-Rule Sequence Calibration

This reference and `multi-rule-sequence-calibration.md` work together:

- **This file** teaches how to plan the architecture: which rules come first, where examples go, how to thread characters and narrative through a chapter.
- **Multi-rule sequence calibration** teaches how to write each individual example: action order, consequence proximity, naming, length, and tone.

When writing or revising a chapter with a complex subsystem:

1. Use this file to plan the layering, cast, and narrative thread.
2. Use multi-rule-sequence-calibration to draft each example scene.
3. Use the writing manual and diction references for voice and prose quality.

## Checklist For Complex Subsystem Chapters

Before finalizing a chapter that introduces a major subsystem:

- [ ] The core loop is stated in the first two paragraphs, before any tables or modifiers.
- [ ] The first example appears within the first page of rules text, not at the end.
- [ ] Modifiers and tables appear after the reader has seen the base case in action.
- [ ] At least two examples share characters or situation, creating narrative continuity.
- [ ] A reader who stops after the first example has a playable version of the rule.
- [ ] Edge cases and GM advice appear last, not interspersed with the core rules.
- [ ] No example introduces more than two new rules at once.
- [ ] Each example ends on a concrete game state, not a system observation.
