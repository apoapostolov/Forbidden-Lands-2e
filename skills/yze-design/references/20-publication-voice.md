<!-- markdownlint-disable MD013 MD024 -->

# Publication Voice — From Designer Jargon to Player Prose

> **STATUS: FILLED.** This is the skill's **voice layer** — the translation bridge between the designer/AI vocabulary used inside `yze-design` (pressure loops, friction levers, deltas, propagation formulas, abstraction ladders) and the publication-ready prose a player or Gamemaster actually reads. Load this file whenever you are writing text that will be read by the audience below — rulebook chapters, talent descriptions, adventure text, GM guidance, examples of play. Do not load it for internal design notes, skill files, or private outlines.

## Contents

1. Why this file exists
2. The audience
3. The core principle — two registers, never mixed
4. The dictionary — designer/AI jargon → player prose
5. The blacklist — words to never use in published text
6. The OK-list — technical terms players already know
7. The six register rules
8. Worked transformations
9. The read-aloud test
10. When to defer to the sibling writing skills

## 1. Why this file exists

`yze-design` thinks in a dense internal vocabulary — *pressure loops, friction levers, deltas, propagation rules, abstraction ladders, dual-use matrices, felt-experience failure modes, the org lifecycle.* This vocabulary is necessary for precision when *designing*. It is poison when *publishing*. A player or GM reading a rulebook does not want to learn a design theory; they want to learn the rule and get back to the table.

This file is the translation layer. It does three things:

1. **Defines the audience** and their reading level.
2. **Gives a dictionary** mapping the skill's internal jargon to plain player-facing prose.
3. **Gives rules and worked examples** for writing publication text that a player can run without a design degree.

This file does **not** teach literary prose style. For fiction voice, period diction, anti-AI humanizing, and genre tone, use the sibling writing skills (`forbidden-lands-writing-voice`, `western-writing`). This file teaches *register* — the difference between talking to a designer and talking to a player.

## 2. The audience

**Who they are:**
- **Ages 18–33.** Mostly millennials and older Gen Z.
- **Gamemasters and players**, not game designers. They may have design opinions, but they do not design for a living and they do not read design theory for fun.
- **Familiar with modern TTRPG culture.** They have read *D&D 5e*, maybe *Pathfinder 2e*, probably one PbtA game, maybe *Blades in the Dark*, possibly a Free League game. They know what a "roll" is, what a "check" is, what "advantage" means.
- **Comfortable with some jargon** that has crossed into mainstream play culture (see §6, the OK-list). They are not comfortable with design-theory jargon or academic/AI vocabulary.
- **Reading to play, not to study.** They want to understand the rule, make a decision, and move on. They will not re-read a paragraph to unpack it.

**Who they are NOT:**
- Not game designers. Do not assume they know what a "pressure economy" or a "design dial" is.
- Not AI. Do not write in the bullet-heavy, abstracted, framework-driven register this skill uses internally. That register is for design precision; it is not how humans talk to each other about games.
- Not academics. Avoid mathematical notation (Δ, formulas), scientific phrasing ("calibrates," "instantiates," "parameters"), and structuralist vocabulary ("taxonomy," "instantiation," "matrix" outside its common RPG sense).

**The test:** would a 24-year-old who has run a year of *D&D* and just bought this book understand this sentence on the first read, without a dictionary? If yes, ship it. If no, rewrite it.

## 3. The core principle — two registers, never mixed

This skill operates in two registers. They must never appear in the same document.

| | **Design register** (internal) | **Publication register** (player-facing) |
| --- | --- | --- |
| **Where** | Skill files, design notes, outlines, private analysis | Rulebook chapters, talent descriptions, adventure text, GM guidance, examples of play |
| **Vocabulary** | Pressure loops, deltas, propagation, friction levers, abstraction ladders, dials, primitives | Roll, check, bonus, penalty, consequence, stake, risk, cost, effect |
| **Tone** | Analytical, precise, framework-driven | Plain, direct, confident, instructive |
| **Sentence shape** | Long, nested, qualified ("the propagation rule shifts the party's standing with B by a fraction of Δ") | Short, active, concrete ("help the Guild and the Cartel notices") |

**The rule:** when you cross from designing to writing-for-publication, switch register entirely. Do not "dumb down" the design register — *replace* it with the publication register. A player is not a designer who knows less; they are a different reader with different needs.

## 4. The dictionary — designer/AI jargon → player prose

The left column is the vocabulary this skill (and AI design reasoning generally) uses internally. The right column is what to write in published text.

### Core engine

| Designer/AI jargon | Publication prose |
| --- | --- |
| pressure loop / pressure economy | (don't name it — just describe the consequence: "every roll you push costs you something") |
| friction lever / friction | cost, risk, drawback, trade-off, price |
| delta (Δ) | change, shift, gain, loss ("your standing with the Guild drops by 1") |
| propagation / propagation rule | "helping one side makes its enemies notice you" |
| calibration / calibrate | set, choose, adjust |
| instantiate / instantiation | set up, version, example |
| parameter / dial | choice, option, setting |
| primitive (P1–P15) | (never mention — these are internal labels) |
| abstraction ladder | (never mention) |
| reinvention operator | (never mention) |
| domain transfer / inversion / fusion | (never mention — just present the result) |
| dual-use matrix | (never mention) |
| generic mechanism | the rule, the system, how it works |
| composable tags / feature grammar | tags, qualities, features ("weapons have tags like Edged or Hooked") |
| typed D66 family | table (or "roll on the Slash table," "roll on the Burn table") |
| resource die | supply die, the die you roll when you use it |
| activity menu | jobs, tasks, what you do that day |
| org lifecycle | (don't name it — describe founding, upkeep, events) |

### Character & progression

| Designer/AI jargon | Publication prose |
| --- | --- |
| attribute-as-HP | "damage reduces your attributes; at zero you're Broken" |
| named damage types | Hurts, Shakes, Vexes, Doubts (or your genre's names) — use them directly |
| protected dial | your edge, your conviction, your faith (or your genre's name) |
| metacurrency | Willpower, Faith, Momentum, Heat — use the game's name |
| refuel trigger | "you gain Willpower when you push a roll and roll a bane" |
| decay valve | "your Influence drops by 1 each session unless you've done something public" |
| depletion state | "at zero Faith you're Shaken — you can't push until you recover" |
| talent ladder depth | "talents have five ranks" or "talents have two ranks: Basic and Advanced" |
| narrative access gating | "you need a forge and a teacher to learn this" |
| generation-depth dial | "quick start" vs "lifepath" |

### Conflict & harm

| Designer/AI jargon | Publication prose |
| --- | --- |
| action economy | "you get one slow action and one fast action each Round" |
| slow/fast action | slow action, fast action (these terms are fine — players use them) |
| reactive actions / reactions | reactions, parry, dodge |
| range bands | range bands (fine — common RPG term) or just name them: Arm's Length, Near, Short, Long, Distant |
| zone features | terrain (cramped, rough, dark) |
| ceremonial conflict | a duel, a showdown, a formal debate |
| critical-injury table engine | critical injury table |
| typed families | "Slash injuries," "Burn injuries" — roll on the matching table |
| conditions | conditions (fine — players know this word) |
| Broken | Broken (capitalized — it's a game state) |
| breakpoint | (don't use — describe the consequence: "at two points of Hurts you're struggling") |
| attrition curve | (don't name it — show it: "the longer you go without rest, the worse this gets") |

### The power layer

| Designer/AI jargon | Publication prose |
| --- | --- |
| power layer | magic, powers, spells (or your genre's name) |
| casting-risk dial | "you can cast safely, or push for more power and risk a mishap" |
| safe / chance / overcharge | safe casting, reckless casting, overcharging |
| mishap table | mishap table |
| fuel / Burn | "spells cost Willpower; you can also Burn — take damage to cast when you're empty" |
| rank ladder | spell ranks, power ranks |
| material gating | "some spells need ingredients" |
| knowledge gating | "you need a grimoire to cast this" |
| epic tier | ritual magic, epic spells |
| ceiling | (don't use — describe the limit: "the most powerful spells require a sacrifice you can't take back") |

### Travel & downtime

| Designer/AI jargon | Publication prose |
| --- | --- |
| spatial model | (don't name it — just use hex or pointcrawl) |
| hex-crawl / pointcrawl | hex crawl, point crawl (or just "travel by hex" / "travel between points") |
| time block | Quarter Day, Shift (or your game's name) |
| activity menu | "each of you picks one job for the Quarter Day" |
| weather as attrition | (don't name it — "roll on the weather table each morning; bad weather costs you" ) |
| food layer | food, water, supplies |
| making camp | making camp |
| recovery shifts | rest, recovery |

### Orgs, factions, economy

| Designer/AI jargon | Publication prose |
| --- | --- |
| org lifecycle | (don't name it — describe founding, building, upkeep, events) |
| five-beat lifecycle | (never mention) |
| scale ladder | (don't name it — "your company can grow into a faction, and a faction can raise an army") |
| scale-escalation | (don't name it — "as your band grows, the stakes grow") |
| faction turn | faction turn, season turn |
| ladder ceiling | (don't name it — describe the scope: "this game is about your town, not about ruling a kingdom") |
| settlement-as-character | "your town has stats, like a character" |
| economy model | coins, barter, credit (or your game's currency) |
| availability/scarcity table | availability table, supply table |
| feature grammar | weapon tags, armor tags, gear qualities |
| quality tiers | Crude, Standard, Fine (or your game's names) |
| consumables-as-resource-dice | supply dice ("roll your Food die when you eat; on a 1–2 it drops a step") |

### Design philosophy & validation

| Designer/AI jargon | Publication prose |
| --- | --- |
| pressure economy | (never in publication — just make the rules create pressure) |
| "Nothing Is for Free" | (you can quote this as a GM principle if you frame it as advice, not theory) |
| lethality-as-feature | (don't name it — "death is on the table; survival is earned") |
| general/situational/optional layering | core rules, situational rules, optional rules |
| warning signs / anti-patterns | (never in publication — these are internal review tools) |
| felt-experience failure modes | (never in publication) |
| flow channel | (never in publication) |
| loss aversion | (never in publication) |
| agency ledger | (never in publication) |
| abstraction-vs-authenticity dial | (never in publication — just write concrete, grounded rules) |
| validation pipeline | (never in publication) |

### Workshop modules — their internal terms

| Designer/AI jargon | Publication prose |
| --- | --- |
| Influence pool (decay valve) | Influence ("your Influence drops by 1 each session unless you've made a public show") |
| constituency | "who you have standing with — the Court, the Church, the Street" |
| scandal roll | scandal roll |
| Bond / Debt (faction web) | Bond, Debt ("the Guild and the Cartel have a Bond of −2 — they distrust each other") |
| propagation | "helping the Guild makes the Cartel cool on you" |
| social distance (Intimate/Personal/Professional/Public) | "a whisper, a direct word, a formal address, a public declaration" |
| Composure | Composure (or your game's name — "social stamina you lose in a tense scene") |
| leverage | leverage ("a secret, a favor owed, a witness — spend it for an edge in a social scene") |
| track-position ladder (chase) | "the gap between you and the hunters: Caught, Closing, Matched, Pulling Away, Out of Sight" |
| clue pool / hard & soft clues | clues ("soft clues are anything; hard clues are the specific evidence you need to nail a conclusion") |
| Threat Clock | clock, countdown ("the cult's ritual advances every phase you spend investigating") |
| Debt (inverted) | Debt ("every favor you accept adds to your Debt; creditors can call it in") |
| Corruption die | Corruption die ("it grows as you use forbidden power — D6 to D8 to D10 to D12 to Lost") |
| milestone table | corruption table, what-happens-to-you table |
| atonement | atonement, redemption ("a pilgrimage steps your Corruption die down one rank") |

## 5. The blacklist — words to never use in published text

These are the AI/design-theory tells. If you find any of these in publication text, rewrite.

- **pressure loop, pressure economy, pressure source** — describe the consequence, not the loop
- **friction, friction lever** — cost, risk, drawback
- **delta, Δ** — change, shift, gain, loss
- **calibrate, calibration** — set, choose, adjust
- **instantiate, instantiation** — set up, example, version
- **parameter** — choice, option, setting (or just name the thing)
- **taxonomy, taxonomy of** — list, breakdown, kinds of
- **matrix** (in the design sense — a 2D table of options) — table, grid (note: "matrix" is fine if the game itself calls something a matrix)
- **primitive** (as a noun) — never; these are internal labels
- **abstraction ladder, reinvention operator, domain transfer, inversion, fusion, abstraction-climb** — never; internal only
- **dual-use** — never
- **generic mechanism** — the rule, how it works
- **org lifecycle, five-beat lifecycle** — never; describe the steps
- **propagation** (as a noun) — "helping them makes their enemies notice you"
- **attrition curve, breakpoint** — describe the consequence at the threshold
- **felt experience, flow channel, loss aversion, agency ledger** — never; these are psychology-theory terms
- **validation pipeline, warning signs, anti-patterns** — never; internal review only
- **dialectic, heuristic, ontology, epistemic** — never; academic
- **paradigm, synergy, leverage** (as a verb) — corporate-speak
- **moreover, furthermore, additionally, it should be noted that** — AI transition padding; use plain "and," "but," or just start the sentence
- **it is important to note that, it is worth considering** — AI throat-clearing; delete and say the thing
- **in order to** — just "to"
- **utilize** — use
- **facilitate** — help, allow, make possible
- **demonstrate** — show
- **subsequently** — then, next
- **consequently** — so
- **leverage** (as a noun, outside the Social Combat module where it's a game term) — use, advantage, edge

## 6. The OK-list — technical terms players already know

These are fine in publication text because modern TTRPG players know them. Don't over-explain.

- **roll, check, dice pool, D6, D66** — universal
- **success, failure, critical** — universal
- **bonus, penalty, modifier** — universal
- **advantage, disadvantage** — common (5e)
- **tag** — common (PbtA, FitD)
- **clock, countdown** — common (FitD, PbtA) — *the user confirmed this one is OK as flavor*
- **track, progress track** — common (PbtA, FitD)
- **arc** — common (narrative games)
- **scene, session** — universal
- **NPC, PC, GM** — universal
- **tick, step** (as in "tick a clock," "step a die down") — common
- **trigger, move** — common (PbtA)
- **consequence, cost, stake, risk** — universal
- **broken, shaken, exhausted** (as condition names) — common
- **rank, tier, level** — universal
- **hex, pointcrawl** — common (OSR, Free League)
- **Quarter Day, Shift** (as time-block names) — fine if the game defines them
- **Willpower, Faith** (as metacurrency names) — fine if the game uses them
- **lever** (as in "leverage," the Social Combat game term) — fine *only* inside that module's text

## 7. The six register rules

1. **Write to the player, not about the system.** "When you push a roll, you take damage" — not "the push-cost model extracts a bane-self-harm cost from the acting character." The player is the subject; the rule is what happens to them.

2. **Use the game's nouns, not the engine's nouns.** If the game calls it "Willpower," call it Willpower. If it calls it "Faith," call it Faith. Do not call it "the metacurrency" in publication. The game's nouns are the player's nouns.

3. **Show the consequence, not the mechanism.** "Your Influence drops by 1 each session unless you've done something public" — not "the decay valve fires at each downtime boundary, stepping the pool down unless the cultivation test passes." The player needs to know *what happens*, not *why it happens in the design*.

4. **Name the thing, don't theorize it.** "Roll on the Slash table" — not "roll on the typed D66 critical-injury family corresponding to the slash damage type." The table has a name; use it.

5. **Short sentences. Active voice. Concrete nouns.** "You take 1 damage" — not "the character suffers a reduction of one point to the relevant attribute." The publication register is plain English, not academic prose.

6. **Address the reader directly.** "You" is the player or GM. "You roll the dice. You decide whether to push. You take the damage." This is how rulebooks talk. It is not how design documents talk. Switch.

## 8. Worked transformations

Each pair: the design-register sentence (how this skill thinks internally) → the publication-register sentence (what the player reads).

### Engine core

**Design:** "The push-cost model extracts a bane-self-harm cost from the latent cost-face when the player opts to reroll non-success dice."
**Publication:** "When you push a roll, look at the banes (💀) you rolled. Each bane on your attribute dice deals 1 damage to that attribute. Each bane on your gear dice reduces the gear's bonus by 1."

**Design:** "The metacurrency is refueled by the harm-earned loop: 1 WP per bane on Base dice when pushing."
**Publication:** "Every time you push a roll, you gain 1 Willpower for each bane on your attribute dice. Pain fuels your will."

### Character

**Design:** "The attribute-as-HP model routes typed damage to named attributes, with a Broken state at zero."
**Publication:** "Damage reduces your attributes. Take enough Hurts and your Grit hits zero — you're Broken, out of the fight and in danger."

**Design:** "The protected dial is a once-per-session escalating die (D8→D10→D12) wired to character identity, producing peak-moment agency."
**Publication:** "Once per session, after you fail a roll to protect yourself or someone else, you can roll your Pride die and add it to the roll. Pride starts at D12. If you use it and still fail, you lose it next session — it comes back as D8, then grows back to D12 over time if you don't lose it again."

### Conflict

**Design:** "The action economy grants (1 slow + 1 fast) ∨ (2 fast) per Round, with reactions drawn from the same budget."
**Publication:** "On your turn, you can take one slow action and one fast action, or two fast actions. Parrying or dodging is a reaction — it costs a fast action."

**Design:** "A typed D66 critical-injury family is rolled, with the 65/66 climax split producing maim-or-die outcomes."
**Publication:** "Roll D66 on the Slash table. A 65 means you lose a hand. A 66 means you're dead."

### Travel

**Design:** "The activity menu distributes the party's labor across mutually-exclusive demands per time block, producing a coordination-as-tactic pressure."
**Publication:** "Each Quarter Day, everyone picks one job: Hike, Lead the Way, Keep Watch, Forage, Hunt, Make Camp, or Rest. You can only do one. You can't move, navigate, keep watch, and forage at the same time — so split the work."

### Faction web (workshop)

**Design:** "The propagation rule shifts the party's Standing with B by floor(Δ × Bond[A,B] / 5)."
**Publication:** "When you help or anger one faction, the others notice. Help the Guild and the factions that hate the Guild cool on you. Hurt the Guild and its allies warm to you. The stronger the bond between two factions, the bigger the shift."

### Corruption (workshop)

**Design:** "The inverted-step die (P5) grows on benefit-only triggers, with a 3+ result stepping up one tier; at D12 the next 3+ triggers a milestone roll on the tier-gated P4 family."
**Publication:** "Every time you use forbidden power and gain from it, roll your Corruption die. On a 1–2, you got away with it — this time. On a 3 or higher, the die steps up: D6 to D8, D8 to D10, D10 to D12. At D12, the next 3+ means you cross a line — roll on the corruption table to see what you've become."

## 9. The read-aloud test

Before shipping publication text, read it aloud. If:

- **You sound like a textbook** → rewrite in plain English.
- **You sound like a design document** → rewrite addressing "you," the player.
- **A word would need a glossary** → replace it with a plain word or define it inline the first time it appears.
- **A sentence is longer than one breath** → cut it in two.
- **You used a word from the blacklist (§5)** → replace it.
- **The player would ask "what does that mean?"** → rewrite.

The test is simple: **would a 24-year-old who has played D&D understand this on the first read?** If not, rewrite. The goal is not to impress; it is to be understood and get out of the way of play.

## 10. When to defer to the sibling writing skills

This file teaches **register** — the designer-to-player translation. It does not teach:

- **Fiction voice** (prose style, tone, genre diction) → use `forbidden-lands-writing-voice` (FL) or `western-writing` (West).
- **Adventure structure & published-adventure register** → use `adventure-writing` (system-agnostic; its "Published register" section is the companion to this file for adventure text specifically).
- **Engine-level manuscript formatting** (ALL-CAPS names, paragraph format for maneuvers, SLOW/FAST inline, symbols, rule-voice) → use `21-manuscript-format.md` in this skill. These conventions are engine-level (true for any YZE game) and owned by `yze-design`.
- **Game-specific manuscript chrome** (FL's statblock table layout, West's 8-column NPC table, chapter structure, example-of-play format) → use `forbidden-lands-design` or `western-rpg-design`. These are game-specific layout choices, not engine conventions.

**The workflow when writing publication text for a YZE game:**
1. Use `yze-design` to design the rule or subsystem.
2. Load **this file** (`20-publication-voice`) to translate the design into publication register — strip designer jargon, write to the audience.
3. Load `21-manuscript-format.md` to format the text correctly — ALL-CAPS names, paragraph format for maneuvers, tables only for roll results.
4. Load the relevant game-specific writing skill (`forbidden-lands-writing-voice` or `western-writing`) for fiction voice and genre tone.
5. Load `adventure-writing` if the text is an adventure (its "Published register" section complements this file).
6. Write. Read aloud (§9). Ship.
