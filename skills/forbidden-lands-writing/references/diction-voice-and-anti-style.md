<!-- markdownlint-disable MD013 -->

# Diction, Voice, And Anti-Style

## Contents

1. What This File Is For
2. Lexical Identity
3. Word Fields
4. Verb Preferences
5. Modifier Discipline
6. Punctuation Restraint
7. The Anti-AI Detection Library
8. Forbidden Lands-Specific Anti-Patterns
9. Contrastive Revision Rules

## What This File Is For

This reference covers two jobs. First, it catalogs the diction the Forbidden Lands manuscript actually uses — the word fields, verb choices, modifier habits, and punctuation practices that make the prose feel like this book and not any other. Second, it provides a concrete detection-and-repair library for the AI writing patterns that are invisible to the AI that produces them and obvious to every human who reads games.

The detection library is adapted from the humanizer anti-pattern catalog and from direct observation of AI drafts produced for this repository. Every pattern listed here has been caught in real Forbidden Lands draft text.

## Lexical Identity

The manuscript's lexicon is narrow, physical, and specific. The authors preferred words you could hold, weigh, or bleed from. When they needed abstraction, they used the smallest available word: fear, not trepidation; burden, not encumbrance; cold, not frigid temperatures.

This narrowness is a feature. It creates cohesion. When every chapter uses the same family of concrete words, the book feels like one book. When the AI introduces vocabulary from other registers — clinical, academic, corporate, therapeutic, marketing — the seam is instantly visible.

## Word Fields

### Body

blood, hand, bone, teeth, breath, scar, gut, flesh, lung, wound, skin, sinew, throat, brow, back, spine, skull, knuckle, rib, marrow, nerve, jaw, palm, finger, wrist, shoulder, knee, hip, chest, heart, eye, ear.

Use these for: injury descriptions, physical exertion, mortality passages, exhaustion, kin distinctions.

### Material and craft

iron, stone, grip, haft, cord, wood, nail, hide, tar, edge, wedge, spike, leather, cloth, rope, bone, antler, flint, bronze, steel, copper, tin, glass, clay, wax, oil, pitch, straw, wool, linen, chain, ring, rivet, forge, anvil, bellows, tongs, mould.

Use these for: item descriptions, crafting passages, gear tables, stronghold construction, cultural flavor.

### Travel and weather

cold, rain, frost, trail, mire, ridge, road, ash, mud, pack, ford, dusk, dawn, wind, fog, sleet, hail, snow, sun, cloud, sky, storm, dark, night, fire, smoke, camp, hearth, tent, cloak, boot, saddle, reins, wagon, cart, bridge, gate, ruin, tower, village, well, stream, river, lake, marsh, swamp, forest, hill, cliff, cave, pass, vale.

Use these for: journey narration, terrain descriptions, weather tables, overnight camp, exploration.

### Survival and pressure

burden, hunger, fear, rot, grime, thirst, pain, strain, ruin, ration, supply, coin, debt, scarcity, loss, trap, ambush, flight, siege, plague, curse, poison, starvation, exhaustion, cold, dark, death.

Use these for: encumbrance, supply tracking, deprivation mechanics, camp phase, zone descriptions, threat narration.

### Culture and society

kin, clan, village, elder, lord, priest, smith, trader, wanderer, outcast, thief, hunter, soldier, farmer, slave, beggar, healer, druid, sorcerer, bard, knight, jarl, thrall, beast, mount, hound.

Use these for: kin descriptions, profession intros, NPC templates, settlement flavor.

## Verb Preferences

### Physical verbs: use these

cut, drag, bind, haul, split, twist, break, climb, carry, cling, stalk, brace, wield, bleed, wrench, grind, hack, pull, shove, pin, lift, drop, throw, swing, strike, crush, tear, pierce, slam, kick, grip, hold, press, lean, crouch, duck, roll, crawl, stagger, collapse, fall, rise, reach, seize, grab.

### Rules-prose verbs: use these

roll, spend, gain, lose, take, suffer, push, mark, choose, count, deal, draw, heal, recover, add, subtract, reduce, increase, succeed, fail, attempt, activate, trigger.

### Do not use

Verbs that inflate a simple action into a performance:

- "serves as" → "is"
- "functions as" → "is"
- "stands as" → "is"
- "represents" → "is" (unless genuinely metaphorical)
- "boasts" → "has"
- "features" → "has"
- "offers" → "gives" or "has"
- "enables" → "lets"
- "fosters" → cut the sentence and say what actually happens
- "underscores" → cut or replace with plain statement
- "highlights" → cut or replace with plain statement
- "showcases" → cut
- "leverages" → "uses"
- "utilizes" → "uses"
- "facilitates" → "helps" or restructure
- "encompasses" → "includes"
- "embodies" → "is"
- "navigates" → "crosses" or "enters" or the physical action
- "delves into" → "explores" or cut entirely

## Modifier Discipline

### Adjective rule

One adjective per noun maximum unless stacking physical observations: "a short broad-bladed axe" works because both short and broad-bladed describe what you see. "A powerful ancient devastating weapon" is three adjectives doing one job.

### Earned versus decorative

An adjective earns its place if removing it changes what the reader pictures. "An iron mace" — removing "iron" changes the mental image (could be wood, bone). "A deadly mace" — removing "deadly" changes nothing; maces are deadly by nature.

### Adverb rule

The manuscript uses almost no adverbs. "Slowly" appears in fiction epigraphs occasionally. "Quickly" appears in rules advisories. Outside these cases, adverbs signal that the verb is too weak to carry its sentence. Replace the adverb-verb pair with a stronger verb: "walked slowly" → "crept" or "shuffled."

### The AI modifier problem

AI drafts over-modify because the model has learned that qualified statements are safe. "The relatively dangerous somewhat unpredictable mildly corrosive..." — every hedge word is a failure of confidence. State the fact. If it is dangerous, say dangerous. If it is not, do not mention it.

## Punctuation Restraint

### Commas

Use for lists, for separating clauses that need separation, and for conditional openers. Do not use Oxford commas unless ambiguity demands one. Do not sprinkle commas for rhythm — that is a poetry habit and the manuscript is prose.

### Em dashes

The manuscript uses em dashes sparingly — one per paragraph at most. AI drafts typically produce 2-4 per paragraph, sometimes nested. This is one of the most reliable AI tells in genre fiction. Replace with: full stops, commas, or restructured sentences.

### Semicolons

The manuscript avoids them. Use them only when connecting two independent clauses that share a tight logical link and a period would create a false separation.

### Exclamation marks

Only in dialogue. Never in rules text. Never in flavor text.

### Ellipses

Only in dialogue to indicate trailing speech. Never in rules or flavor prose.

### Colons

Used freely for introducing lists and for definition structures: "Casting a spell: requires WP and a grimoire." The manuscript treats colons as workhorse punctuation, not as dramatic punctuation.

## The Anti-AI Detection Library

Every pattern below has been observed in actual AI drafts for this repository. The library is organized by detection difficulty — the easy patterns first, the subtle ones last.

### Tier 1: Obvious AI tells

These are visible to any attentive reader.

**Inflated significance.** "The mace stands as a testament to enduring dwarven craftsmanship." → "The mace is a dwarven weapon." Detection words: "stands as," "serves as," "is a testament to," "marks a turning point," "represents a shift."

**Promotional language.** "A stunning collection of devastating spells." → "Spells are listed in order of Power Level." Detection words: "stunning," "devastating," "incredible," "remarkable," "must-have," "groundbreaking."

**Sycophantic praise.** "The brilliantly designed push mechanic." → "The push mechanic." The reader does not need to be told the design is brilliant. Detection words: "brilliant," "elegant," "beautifully crafted," "masterfully."

**Blog-tutorial voice.** "Let's take a closer look at how combat works." → "When a conflict begins, the first step is to determine initiative." Detection phrases: "let's," "as you can see," "as we discussed," "in other words," "this means that."

### Tier 2: Structural AI tells

These are invisible in single sentences but visible in paragraphs and sections.

**Structural uniformity.** Every paragraph opens with a topic sentence, develops for 2-3 sentences, and closes with a mild conclusion. The manuscript varies paragraph shape by job. Test: read three consecutive paragraphs and check whether they have the same arc.

**Rule-of-three padding.** "The wilderness is vast, dangerous, and unforgiving." Two of those are doing the same job. Test: can you remove one item from a triple without losing information?

**Balanced sentence pairs.** "While the mace excels at close quarters, the bow dominates at range." The manuscript does not balance its sentences aesthetically. It states facts in order of importance. Test: does the sentence have a while/whereas/on-the-other-hand pivot?

**List-of-three sections.** Every section has exactly three subsections. Every comparison has exactly three points. The AI defaults to three because it has learned that three is a satisfying number. Test: does the content require exactly this number of points?

### Tier 3: Diction-level AI tells

These require word-level attention.

**Copula avoidance.** "Serves as," "functions as," "stands as" instead of "is." AI models avoid "is" and "are" because training data rewards variation. The manuscript uses "is" freely and without embarrassment.

**Elegant variation.** "Willpower" in sentence one, "mental reserves" in sentence two, "inner fortitude" in sentence three. AI models cycle synonyms to avoid repetition. The manuscript repeats game terms.

**Negative parallelism.** "Not just a sword — it's a lifeline." The original authors do not use this construction. It is a TED Talk structure.

**Participial chains.** "...enabling players to craft unique builds while fostering strategic depth." Sentences ending in -ing chains are AI's way of continuing a sentence beyond its natural stopping point.

**Abstract atmosphere.** "A sense of dread permeated the ancient halls." The manuscript does not name emotions. It shows the cliff leaning in, the walls listening, the eyes gone grey as granite.

**AI vocabulary clusters.** Any of: "delve," "enhance," "foster," "pivotal," "tapestry," "testament," "underscore," "vibrant," "robust," "nuanced," "intricate," "comprehensive," "vital." These words appear in AI text at frequencies far above natural writing.

### Tier 4: Invisible tells

These are the hardest to detect and the most damming when found.

**Hedging stacks.** "Could potentially have some utility in certain combat situations." Each hedge individually seems cautious. Stacked, they are AI filler. The manuscript states facts or says "unclear."

**Generic positive endings.** "With these tools at their disposal, adventurers are well-equipped to face whatever challenges await." This could end any section of any game. The manuscript ends on specifics.

**Filler phrases.** "In order to ensure," "due to the fact that," "at this point in time," "it is important to note," "as previously mentioned." Each wastes 3-8 words that carry zero information.

**Excessive conjunctive phrases.** "Furthermore," "moreover," "additionally," "in addition to this," "building on this idea." The manuscript connects sentences through shared subjects and shared logic, not through transition words.

**Sudden style shifts.** The AI writes three sentences of competent dark fantasy, then drops a sentence that sounds like a university essay. This is the model switching between training-data registers. It is invisible to the model and obvious to the reader.

## Forbidden Lands-Specific Anti-Patterns

These are not general AI tells — they are specific failure modes observed in Forbidden Lands draft text.

### Fantasy fog

"Shadow and sorrow haunt the ancient stones of the Forbidden Lands, where destiny intertwines with despair beneath a blood-red sky."

Not one concrete noun in that sentence refers to something a character could touch, use, or fear. It is mood decoration. The manuscript builds atmosphere from physical objects: iron, bone, cold, mire, rain, ruin.

**Fix:** Replace mood nouns with material nouns. A stone is concrete. Shadow is not. Cold rain hitting a mail shirt is atmospheric. "Sorrow haunting stones" teaches nothing.

### Therapeutic framing

"Through their journey, the adventurers will discover deeper truths about themselves and grow as individuals."

The manuscript is not therapy. Characters bleed, starve, and die. Growth happens because you survived, not because you reflected. The word "journey" as metaphor for personal growth does not belong.

**Fix:** Cut the sentence. If growth needs to happen, show it through changed capabilities, not through introspective language.

### Epic inflation

"An awe-inspiring display of raw, unbridled magical power surged through the ancient halls."

The manuscript describes magic through specific sensory images: eyes turned grey as granite, a mouth gaping like a pit, stone rising from a cliff. It does not inflate. It observes.

**Fix:** Replace the inflation with one specific image. What does the magic look like? What does it do to the caster's body? What does the room look like afterward?

### Design-document voice

"This talent is designed to synergize with the combat system's action economy, providing a tactical option that enhances party composition diversity."

The manuscript never acknowledges that it is designed. It presents rules as facts about the world. "You can spend a fast action to parry an incoming attack."

**Fix:** Remove all design-facing language. State the rule as a fact about the character and the world, not about the system.

### Proposal leakage

"As proposed in the balance review, this adjustment addresses the observed power gap between ranged and melee archetypes."

Design rationale belongs in proposals. Once text is promoted to the manuscript, no trace of the proposal process should remain.

**Fix:** Remove the rationale. State the rule.

## Contrastive Revision Rules

Apply these five tests to any draft before finalizing.

### 1. The replacement test

Read each sentence and ask: would the original authors have written this sentence, or would they have written something shorter, harder, and more specific? If the answer is shorter-harder-specific, rewrite.

### 2. The placement test

Imagine this draft placed inside the manuscript between two existing paragraphs. Does it need a different font? Does it need to be introduced? If the reader would feel a voice shift, the draft has imported a foreign register.

### 3. The deletion test

Can you remove this sentence and lose nothing? If the remaining text says the same thing, the sentence was filler. Cut it and do not mourn it.

### 4. The specificity test

Does this sentence contain at least one concrete noun — something with weight, temperature, texture, or edges? If the sentence is purely abstract, it needs an anchor.

### 5. The ending test

Read only the last five words of each sentence. Are they concrete nouns, hard verbs, or material facts? Or are they trailing qualifiers, soft abstractions, or mood-word fog? Sentence endings are where AI writing leaks most visibly. Fix the endings first and the rest of the prose often improves by itself.
