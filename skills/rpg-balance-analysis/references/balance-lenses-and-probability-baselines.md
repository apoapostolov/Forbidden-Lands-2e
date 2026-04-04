<!-- markdownlint-disable MD013 -->

# Balance Lenses And Probability Baselines

## Contents

1. Scope
2. Balance Lenses
3. Probability Baseline
4. Apparent Value Versus Actual Value
5. Balance Reading Rules

## Scope

This reference executes steps 1 through 3 of the `rpg-balance-analysis` research plan:

- define the full analytical framework
- build a probability baseline
- compare apparent value versus actual value

It is the foundation document for the balance skill.

## Balance Lenses

RPG balance should be read through five separate lenses.

### 1. Mathematical balance

Questions:

- how often does the rule succeed
- what does it produce on success
- what does it cost
- what is the expected return over time

Use this lens for:

- dice odds
- damage
- mitigation
- resource conversion
- recovery rate
- frequency of activation

### 2. Perceived balance

Questions:

- does it feel fair
- does it feel worth it
- does it match what the text promises

Use this lens for:

- resentment
- disappointment
- envy
- bait-and-switch effects

### 3. Table balance

Questions:

- who gets the spotlight
- who waits
- who carries the memory load
- who must adjudicate the fallout

Use this lens for:

- spotlight concentration
- GM burden
- arguments
- scene pacing

### 4. Campaign balance

Questions:

- what happens after repeated use
- what old constraints does the rule quietly erase
- what niches collapse over time

Use this lens for:

- attrition
- progression
- repeatable loops
- power scaling

### 5. Social-psychological balance

Questions:

- what emotions does the rule create
- does it teach caution, aggression, resentment, distrust, or creativity
- does it support group cohesion or reward anti-party play

Use this lens for:

- trust in the text
- feeling of agency
- fear of trying things
- pressure on the GM to rescue the experience

## Probability Baseline

Mathematics do not solve RPG balance, but they set the floor for honest analysis.

### Core rule

Whenever a rule changes one of these, it is balance-relevant:

- probability of success
- probability of partial success
- probability of disaster
- size of reward
- frequency of use
- action cost

### Practical probability baseline for this repo

Forbidden Lands uses a d6 pool where each die succeeds on `6`.

Useful benchmark probabilities:

| Dice | 1+ Success | 2+ Success | 3+ Success |
| ---- | ---------- | ---------- | ---------- |
| 2 | 30.56% | 2.78% | 0.00% |
| 4 | 51.77% | 13.19% | 1.62% |
| 6 | 66.51% | 26.32% | 6.23% |
| 8 | 76.74% | 39.53% | 13.48% |
| 10 | 83.85% | 51.55% | 22.48% |

Immediate implication:

- one-success tasks stabilize fast
- two-success tasks remain meaningfully uncertain on medium pools
- three-success tasks are premium outcomes

That makes any rule that grants automatic successes much more valuable than a plain die bonus.

### Action-cost baseline

RPGs often hide balance in action cost rather than raw numbers.

In systems with turn structure, compare:

- free effect
- fast effect
- standard effect
- slow effect
- once-per-round effect
- once-per-scene effect

The practical strength of an ability often follows action compression more than raw numeric buff.

### Attrition baseline

A rule is not only about scene output.
Ask:

- what does it consume
- how often can it be replenished
- how painful is the replenishment

This matters in RPGs more than in many board games because replenishment often lives in fiction and campaign time, not only in tactical rounds.

## Apparent Value Versus Actual Value

Players do not choose from true expected value.
They choose from presented value.

### Apparent value

What the player thinks a rule gives them based on:

- fantasy
- wording
- examples
- emotional promise
- obvious upside

### Actual value

What the rule really gives once you include:

- success odds
- action cost
- opportunity cost
- counterplay
- downstream burden
- repeat-use implications

### Four common gaps

#### 1. Inflated fantasy, ordinary output

The text promises a huge identity payoff, but the rule is only a mild modifier.

Consequence:

- disappointment even if numerically fair

#### 2. Ordinary wording, extreme output

The rule sounds modest but actually bends the whole system.

Consequence:

- dominant lines discovered late

#### 3. Visible reward, hidden burden

The player sees the benefit but not:

- action loss
- future risk
- table burden
- social cost

Consequence:

- trap or bully options

#### 4. High reliability, low drama

The rule is mathematically efficient but emotionally flat.

Consequence:

- it may still be “balanced” yet damage the feel of play

### Method for evaluating the gap

For any rule, write two statements:

1. “What a player thinks this buys.”
2. “What this actually buys once play starts.”

Then compare:

- output
- risk
- frequency
- emotional payoff
- load on the GM or group

If the gap is too wide, the rule is unstable even if it is not numerically broken.

## Balance Reading Rules

### Rule 1

Never evaluate a bonus without asking what kind of bonus it is:

- raw chance
- auto-success
- extra action
- extra resource
- risk cancellation

### Rule 2

Never evaluate a cost without asking whether it is real in campaign play.

### Rule 3

Never evaluate a scene win without checking whether it becomes routine over ten sessions.

### Rule 4

Never trust intuitive fairness if the text misleads the player about what the rule actually does.
