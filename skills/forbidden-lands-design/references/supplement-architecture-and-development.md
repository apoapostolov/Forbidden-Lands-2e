# Supplement Architecture and Development

Use this reference to turn a strong idea into a coherent, usable Forbidden Lands
supplement. A supplement succeeds when its promise appears repeatedly in play,
its parts reinforce one another, and the GM can deploy it without repairing the
design.

## Product Thesis

Write one sentence:

> This supplement helps [users] create [specific play experience] by giving
> them [repeatable tools and content] while preserving [core constraints].

Then define:

- target campaign phase
- player-facing fantasy
- GM-facing workload reduced
- core loop affected
- expected frequency of use
- compatibility promise
- material explicitly out of scope

If the thesis cannot identify repeated table use, the project is lore or
inspiration rather than a game supplement. That can be valid, but label it
honestly.

## The Three-Layer Deliverable

Every major feature should provide:

1. **Procedure:** how play resolves.
2. **Content:** options, actors, places, events, or outcomes used by it.
3. **Support:** examples, generators, summaries, and guidance for uncertain
   cases.

Procedure without content creates prep. Content without procedure creates
adjudication burden. Advice without either is not a playable feature.

## Architecture Map

Before drafting chapters, map:

| Layer | Question |
| --- | --- |
| Promise | What changes at the table? |
| Entry | How do characters and campaigns access it? |
| Loop | What repeats? |
| Decisions | Where do players choose? |
| Resources | What is gained, spent, damaged, or transformed? |
| Opposition | What resists or exploits it? |
| Growth | How does mastery or campaign scale change it? |
| Consequence | How does it alter the world? |
| Exit | How does a scene, project, career, or campaign phase conclude? |
| Integration | Which existing chapters must acknowledge it? |

Missing entry and exit rules are common sources of unusable supplements.

## Scope by Play Frequency

Allocate rules weight by expected use:

- **Every roll or round:** extremely short; use core grammar.
- **Once per scene:** one decision and one resolution, with rare exceptions.
- **Once per Quarter Day:** may include posture, allocation, or a small table.
- **Once per session:** can support a distinctive procedure.
- **Once per campaign arc:** may carry more ceremony and consequence.

Do not give a rare event more lookup machinery than a central loop unless the
event is the supplement's main promise.

## Character Option Coverage

Build a coverage matrix for:

- kin
- professions
- attributes and skills
- combat and non-combat roles
- early, middle, and late advancement
- solitary and cooperative use
- resource-rich and resource-poor campaigns

Coverage does not mean identical access. It means intentional inclusion and
exclusion.

### Common and rare identities

Common professions are broad entry points. A rare or prestigious profession
should enter through a gate such as:

- a narrow lifepath result
- a formative event
- an in-world mentor or institution
- a costly choice after demonstrated aptitude
- a campaign achievement

The gate must be:

- visible enough to pursue
- rare enough to preserve identity
- based on a meaningful acceptance or sacrifice
- compatible with characters who never enter it

Do not replace generic profession entries across many tables to advertise a
specialist class. Add a limited conversion opportunity at an appropriate stage.

### Avoid orphan content

Every player-facing option needs:

- a legal acquisition route
- rules for starting and advanced characters
- clear prerequisites
- interaction with lifepaths or advancement
- at least one ordinary use case
- a reason it is not mandatory

## Chapter Design

Teach from use:

1. What the feature does.
2. When it enters play.
3. The default procedure.
4. Player choices and costs.
5. Outcomes and state changes.
6. Exceptions and advanced cases.
7. Worked example.
8. GM tools and content.
9. Summary or reference table.

Keep concepts near the procedure that consumes them. Avoid definitions that
become meaningful only several chapters later.

### Rules text completeness

State:

- trigger
- eligible actor
- target
- range or access
- timing
- action cost
- roll and modifiers
- resource cost
- success
- failure
- duration
- stacking
- recovery or removal
- exceptions
- GM authority

Not every rule needs every field, but every relevant field must be answerable.

## Content Density

Prefer entries that do more than one job. A settlement can provide a market,
faction pressure, a rumor source, recovery, and a legal complication. A monster
can create combat danger, ecological evidence, valuable resources, and a moral
dilemma.

Multi-use content must remain coherent. Do not attach unrelated functions merely
to increase utility.

### Generators

A generator should combine meaningful dimensions, not produce ornamental noise.
Good columns answer:

- what is wanted
- what obstructs it
- who benefits
- what is visible
- what changes with time
- what price or compromise is possible

Test combinations at extremes. Remove results that require the GM to invent the
actual situation from scratch.

## Compatibility Discipline

Classify additions as:

- **Native extension:** uses current rules and terms.
- **Optional module:** changes a contained procedure and declares interfaces.
- **Replacement:** supersedes a current rule and lists all downstream changes.
- **Campaign frame:** changes assumptions about access, scarcity, or authority.

Never present a replacement as a harmless extension. State what becomes
obsolete, what must be converted, and how existing characters are treated.

## GM Value

Each chapter should reduce at least one burden:

- invention
- adjudication
- bookkeeping
- pacing
- consequence tracking
- portraying distinct actors
- answering unexpected choices

Supply operational tools:

- one-page procedures
- reaction and consequence tables
- faction or site sheets
- examples of strict and permissive rulings
- state trackers only when state matters
- guidance for scaling pressure

“Use your judgment” is acceptable only after criteria are supplied.

## Safety and Mature Material

Dark fantasy gains force from specificity and consequence, not escalation for
its own sake. For coercion, trauma, prejudice, torture, sexuality, or harm to
children:

- establish why the subject matters to play
- give the GM alternatives with equivalent functional pressure
- avoid surprise detail beyond the campaign's agreed boundaries
- never use suffering as mere atmosphere or proof of seriousness
- preserve player authority over their character's internal response

Safety tools support trust and therefore permit braver play; they are not a
substitute for responsible content design.

## Development Stages

### 1. Thesis prototype

Write the smallest complete loop and enough content to test it. Avoid polished
prose.

### 2. Structural test

Test entry, repeated use, escalation, failure, and exit. Delete features that do
not support the thesis.

### 3. Interaction test

Audit every interface with core rules, existing options, economy, recovery, and
campaign scale.

### 4. Content test

Test generators, sites, NPCs, and examples for variety, usability, and coverage.

### 5. Manuscript pass

Apply canonical terminology, voice, navigation, cross-references, and summaries.

### 6. Release candidate

Run regression tests, blind usability review, linting, link validation, version
updates, and changelog review.

## Blind Usability Test

Give the chapter to a GM who did not design it. Ask them to:

1. create one legal character or campaign entry
2. run the central procedure
3. adjudicate an edge case
4. recover or exit the state
5. find the relevant rule again

Record where they infer missing rules, search for terms, or contradict intended
behavior. Explanations from the designer do not count as manuscript success.

## Quality Gate

- [ ] The product thesis describes repeated table use.
- [ ] Every major feature has procedure, content, and support.
- [ ] Entry, escalation, failure, recovery, and exit are complete.
- [ ] Common and rare character options have proportional access.
- [ ] Coverage gaps are intentional and documented.
- [ ] Rules weight matches frequency and importance.
- [ ] The GM receives concrete operational tools.
- [ ] Optional, replacement, and campaign-frame rules are labeled correctly.
- [ ] Mature content is purposeful, bounded, and adaptable.
- [ ] A new GM can use the feature without designer intervention.
- [ ] All affected manuscript locations are updated.
