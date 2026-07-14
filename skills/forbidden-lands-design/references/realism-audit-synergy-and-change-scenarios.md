<!-- markdownlint-disable MD013 -->

# Realism, Audit Method, Synergy, And Change Scenarios

## Contents

1. Scope
2. Realism Versus Playability
3. Proposal-Audit Method
4. Synergy Analysis
5. Mathematical Change Scenarios
6. Design Conclusions

## Scope

This reference executes steps 16 through 19 of the `forbidden-lands-design` research plan:

- realism versus playability
- proposal-audit method
- synergy analysis
- mathematical change scenarios

It is the last analytical block before the final unified design manual.

## Realism Versus Playability

The game already contains a clear design stance:

- danger should feel physical and credible
- consequence should matter after the scene
- realism is welcome when it sharpens decisions
- realism is bad when it creates drag without new judgment

This is not a realism simulator.
It is a harsh adventure game that uses realism selectively to intensify pressure.

### Good realism

Realism is helping when it does at least one of these:

1. creates a meaningful choice
2. reinforces the material reality of the world
3. gives existing pressure a cleaner rule hook
4. makes outcomes feel more believable without slowing play

Examples from the current manuscript:

- cold blocking recovery instead of only dealing damage
- gear and materials shaping what can be built or repaired
- critical injuries carrying distinct lasting effects
- travel actions consuming Quarter Days rather than handwaving logistics

### Bad realism

Realism is hurting when it does one or more of these:

1. adds procedure without adding decisions
2. creates “you are technically alive but functionally unusable” states without saying so
3. duplicates an existing pressure channel with new bookkeeping
4. relies on GM mercy to remain playable

### Practical realism test

Ask these in order:

1. What decision does this make sharper?
2. What existing abstraction is it replacing or clarifying?
3. What is the new table burden?
4. Does it preserve campaign movement, or stall it?
5. If it cripples a character, is that honestly labeled as playable, retirement-default, or fatal?

If a proposal cannot answer question 1, it probably does not deserve rules weight.

### Repo-specific realism lessons

The critical injury proposals in this repo show the correct direction.

Observed proposal stance:

- catastrophic injury is more interesting as survivable consequence than as flat instant death
- but “survivable” must not be used dishonestly for states that effectively end active adventuring

This is exactly the right realism boundary for this manuscript:

- survival with cost is good
- hidden non-playability is bad

## Proposal-Audit Method

This method should be used whenever evaluating a new proposal for inclusion in the manuscript.

### Stage 1: Problem definition

State clearly:

- what problem the proposal claims to solve
- whether that problem is actually present in the current manuscript

If the problem is vague, the solution will drift.

### Stage 2: Chapter ownership

Determine which chapter truly owns the problem:

- skills
- talents
- combat
- injuries
- magic
- journeys
- stronghold
- gear

Many weak proposals fail because they solve a Chapter 8 problem in Chapter 6 language, or a talent problem with a general-rule patch.

### Stage 3: Rule-type match

Identify what rule category the proposal is using:

- resolution
- push
- action economy
- damage
- recovery
- resource
- travel pressure
- exception
- economy/access

If the proposal invents a new type where an existing one would work, that is a warning sign.

### Stage 4: Integration check

Trace direct interactions with:

- push and Willpower
- healing and recovery
- talents and spell exceptions
- Quarter Days and travel pace
- gear access and tool requirements
- critical injuries and retirement pressure

If two or more of these are touched, the proposal is system-level, not local.

### Stage 5: Table-speed check

Ask:

- what must be remembered during live play
- whether the GM must track another timer, condition, or exception
- whether the rule resolves in one sentence or requires repeated interpretation

### Stage 6: Agency check

Ask:

- does the proposal create meaningful choice
- does it remove a character from useful play
- if so, is that stated honestly

### Stage 7: Voice placement

Separate:

- design rationale
- proposal explanation
- final manuscript rule text

Proposal logic belongs in proposals.
Only native rulebook prose should cross into `01-corebook/`.

### Audit verdict classes

Use these verdicts:

- `Accept now`
- `Accept with simplification`
- `Hold for broader rewrite`
- `Reject for now`
- `Reject as wrong chapter / wrong rule type`

### Current repo example

The critical injury acceptance summary in this repo already demonstrates good audit behavior:

- accepts the core `65` survivable-catastrophe logic
- rejects broad non-typical-damage rewrites for now
- isolates compatibility clarifications as necessary integration work

That is the model to reuse.

## Synergy Analysis

Synergy is not just “two strong things work well together.”
In this manuscript, synergy matters when one rule changes the pressure assumptions of another.

### Main synergy classes

#### 1. WP multiplier synergies

These are the most dangerous.

Pattern:

- easier WP generation
- more effective WP spending
- refunds or discounts

Examples already visible:

- talents that make the first WP count as more than one
- talents that permit extra pushes
- talents that refund WP after high-impact actions
- spells that generate WP directly

Why dangerous:

- they attack the central coupling resource of the game

#### 2. Action-compression synergies

Pattern:

- free fast actions
- extra slow actions
- extra attacks
- additional reactions

Why dangerous:

- they bypass the ordinary opportunity-cost structure

### 3. Defense-bypass synergies

Pattern:

- ignore armor
- force critical injuries
- auto-success on attacks or control effects

Why dangerous:

- they skip the main defensive layers and accelerate death or disablement

### 4. Recovery-collapse synergies

Pattern:

- heal all damage
- halve or erase injury time
- bypass conditions
- stable non-magical or magical replenishment loops

Why dangerous:

- they flatten the campaign-pressure spine

### 5. Travel-pressure nullification synergies

Pattern:

- easy shelter
- easy food and water
- easy weather immunity
- lossless movement

Why dangerous:

- they hollow out Chapter 8

### Existing manuscript synergy risks

#### Risk cluster: extra pushes plus WP economy

When a rule permits repeated pushing, any rule that:

- softens bane consequences
- increases conversion to success
- refunds WP

becomes much more dangerous than it looks in isolation.

#### Risk cluster: spell stabilization

Grimoires, safe casting, rank advantage, and any cost reducers already form a spell-risk control package.

Any additional stabilizer risks turning magic from:

- volatile leverage

into:

- repeatable optimal utility

#### Risk cluster: automatic injury conversion

Effects that jump straight from a successful hit to an automatic critical injury are extremely sharp because they bypass:

- armor's full protective role
- ordinary damage pacing
- the distinction between attritional defeat and catastrophic result

### Proposal synergy review method

When reading a new proposal, ask:

1. What existing costs does it reduce?
2. What pressure channel does it bypass?
3. Does it stack with any refund, auto-success, or action-compression effect?
4. Does it turn a once-interesting edge case into a repeatable dominant line?

## Mathematical Change Scenarios

These scenarios are not recommendations by themselves.
They are calibration tools showing how sensitive the engine is.

### Scenario 1: Raise per-die success from `1/6` to `2/6`

For initial pools:

| Pool | Model | 1+ | 2+ | 3+ |
| ---- | ----- | --- | --- | --- |
| 4 | `1/6` | 51.77% | 13.19% | 1.62% |
| 4 | `2/6` | 80.25% | 40.74% | 11.11% |
| 6 | `1/6` | 66.51% | 26.32% | 6.23% |
| 6 | `2/6` | 91.22% | 64.88% | 31.96% |
| 8 | `1/6` | 76.74% | 39.53% | 13.48% |
| 8 | `2/6` | 96.10% | 80.49% | 53.18% |

Conclusion:

- even what looks like a modest per-die increase detonates the tier system
- challenging and difficult tasks become routine very fast

### Scenario 2: Resource-die longevity for depletion on `1-2`

For a descending die chain like `D12 -> D10 -> D8 -> D6 -> lost`, the expected number of hard uses before loss is approximately:

- `18` uses

Conclusion:

- stepdown resource dice are a strong way to model meaningful but not annoying depletion
- they are durable enough for expedition tools, but still finite

### Scenario 3: Care halves recovery time

Care compression examples:

| Base Recovery | After Care |
| ------------- | ---------- |
| 2 days | 1 day |
| 4 days | 2 days |
| 7 days | 3.5 days |
| 14 days | 7 days |
| 28 days | 14 days |

Conclusion:

- care is one of the strongest tempo effects in the recovery system
- anything that grants repeatable “care-equivalent” compression is a high-impact rule even if it looks small

### Scenario 4: Automatic success versus dice bonus

Because 2+ and 3+ thresholds are steep, a rule that says:

- “treat as one success”

is much stronger than:

- “add one die”

especially on medium pools.

Conclusion:

- success substitution should be treated as a premium effect category

### Scenario 5: Action-cost reduction

Changing a repeated action from:

- `slow` to `fast`

or:

- `fast` to `free`

is often stronger than adding damage or dice.

Conclusion:

- action-cost changes should be analyzed before numeric buffs

## Design Conclusions

### 1. Realism should justify itself through better play

If realism does not sharpen choice or improve consequence clarity, it is probably decorative weight.

### 2. Proposal audit should be structural, not impressionistic

The best way to reject bad design is not “I dislike it.”
It is:

- wrong problem
- wrong chapter
- wrong rule type
- too much system impact for too little gain

### 3. Synergy risk lives mostly in couplings

The manuscript is most fragile where systems meet:

- WP
- action economy
- injury conversion
- recovery compression
- travel-pressure removal

### 4. The engine is mathematically sharp

Small numeric changes can create large downstream differences.
This is especially true for:

- per-die success rate
- auto-success rules
- action-cost changes
- recovery-time compression

### 5. The final manual should preserve these distinctions

The unified design manual should treat:

- local power
- pressure bypass
- and system coupling

as separate analytical categories.
