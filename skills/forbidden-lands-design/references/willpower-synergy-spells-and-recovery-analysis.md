<!-- markdownlint-disable MD013 -->

# Willpower, Synergy, Spells, And Recovery Analysis

## Contents

1. Scope
2. Willpower Economy
3. Subsystem Interaction Matrix
4. Talent Path Analysis
5. Spell-System Volatility
6. Damage And Recovery Pressure
7. Design Conclusions

## Scope

This reference executes steps 6 through 10 of the `forbidden-lands-design` research plan:

- Willpower economy
- subsystem interaction matrix
- talent path analysis
- spell-system analysis
- damage and recovery analysis

It extends `engine-math-and-rule-taxonomy.md`.

## Willpower Economy

Willpower is the central conversion currency of the game.

The engine creates it through risk and spends it through exceptions.
That makes it the main bridge between:

- the core dice system
- talents
- magic
- recovery bypasses
- burst damage

### Generation model

In the current manuscript, Willpower is generated from pushed Base Dice only.

For `m` pushed Base Dice:

- expected WP gain = `m / 6`
- probability of at least 1 WP = `1 - (5/6)^m`

Examples:

| Pushed Base Dice | Expected WP | Chance Of 1+ WP |
| ---------------- | ----------- | --------------- |
| 2                | 0.3333      | 30.56%          |
| 3                | 0.5000      | 42.13%          |
| 4                | 0.6667      | 51.77%          |
| 5                | 0.8333      | 59.81%          |
| 6                | 1.0000      | 66.51%          |

Immediate implication:

- low-Strength or low-Agility characters do not only push smaller pools
- they also feed the Willpower engine more slowly

### Generation bottlenecks

The economy is intentionally throttled by:

- Base Dice only
- push only once
- damage risk attached to gain
- maximum WP cap of 10
- no WP gain for NPCs

This is a robust design choice.
It keeps burst power tied to danger rather than to passive recharge.

### Secondary generation and bypass channels

The manuscript also includes rule exceptions that bypass the normal push loop:

- talents that amplify how much a point of WP counts for
- talents that refund WP
- talents that allow extra pushes
- stronghold or rest-side WP restoration modules
- narcotics in short-break rules

These are not all equal.
Some create more power.
Some create more frequency.
Some create lower-risk access.

### Spend profile in talents

`corebook/04-talents.md` is heavily WP-driven.

Observed manuscript facts:

- `197` lines mention `WP` or `Willpower`
- `173` talent rank lines explicitly mention `WP`
- explicit spend mentions cluster hard around `1 WP`

Observed explicit cost mentions:

- `1 WP`: 89 mentions
- `2 WP`: 12 mentions
- `3 WP`: 4 mentions
- `4 WP`: 1 mention
- `6 WP`: 1 mention
- variable spend patterns: 25 mentions

### What that means

The talent chapter is built around a strong default price point:

- `1 WP` is the standard action-costing burst

This has several design effects:

1. Talents feel usable often enough to matter.
2. Small amounts of generated WP are meaningful immediately.
3. The system encourages many small activations rather than only rare ultimates.

But it also creates a balancing hazard:

- anything that generates or discounts even 1 extra WP reliably can distort many different talents at once

### Relative value of one point of WP

In the current manuscript, `1 WP` often buys one of these:

- one extra success
- one action edge
- one point of prevented or added damage
- one guaranteed activation
- one burst of movement or initiative manipulation
- one spell power increment

That makes `1 WP` a high-value tactical unit.
The game is not using WP as a mild nudge resource.
It is using it as immediate leverage.

### High-risk and low-risk WP loops

#### Healthy loop

- push in danger
- take real risk
- gain some WP
- spend it on a meaningful edge

This is the core intended loop.

#### Unhealthy loop

- gain WP through low-stakes repetition
- spend it on high-leverage combat or spell effects
- avoid matching exposure

This is what future design work should guard against.

## Subsystem Interaction Matrix

The most important interactions are not pairwise flavor links.
They are pressure links.

### Core matrix

| System | Directly Feeds | Directly Drains | Hidden Coupling |
| ------ | -------------- | --------------- | --------------- |
| Skills | Combat, travel, crafting, healing, scouting | Attributes, gear durability | Willpower generation |
| Pushing | Willpower, extra successes | Attributes, gear | Talent and spell tempo |
| Talents | Combat, recovery, travel, stealth, social leverage | Willpower | Niche invalidation risk |
| Magic | Damage, recovery, travel bypass, utility | Willpower, mishap risk | Strongest bypass layer |
| Journeys | Conditions, attrition, tempo pressure | Food, water, shelter, time | Weakens party before conflict |
| Critical injuries | Campaign consequence, recovery burden | Time, care bandwidth | Retirement pressure |
| Gear | Success odds, protection, specialist access | Money, supply, repair load | Gear dice create non-WP risk |
| Stronghold | Recovery, crafting, economy, status | Materials, time, rootedness | Converts campaign success into lower friction |

### Most important two-way relationships

#### Skills <-> Willpower

- skills create the risk context
- pushing converts risk into fuel
- talents and spells cash that fuel out

#### Talents <-> Magic

- many talents directly alter spell cost, rank access, or power expression
- magic disciplines themselves live inside the talent structure

#### Journeys <-> Recovery

- travel drains resources and adds conditions
- camp quality determines how efficiently damage is shed

#### Combat <-> Critical injuries

- combat damage is the main gateway into catastrophic consequences
- any combat buff therefore has downstream campaign impact, not just scene impact

#### Gear <-> Crafting <-> Stronghold

- gear quality shapes success rates
- repair and replacement depend on tools and functions
- strongholds soften the logistics pressure that keeps gear meaningful

### Design rule from the matrix

If a proposal touches:

- Willpower
- recovery
- spell power
- or travel pressure

it is almost certainly not local.
It should be reviewed as a system-level change.

## Talent Path Analysis

### Structural findings

The talent chapter contains a very large exception surface.

Observed manuscript facts:

- `39` `PATH OF ...` headings
- `128` level-3 headings overall

This means the talent chapter is one of the primary sources of both:

- character expression
- balance instability

### Functional categories

Most talent paths fall into one or more of these roles:

1. Dice enhancement
2. Action compression
3. Damage amplification
4. Damage prevention
5. Recovery bypass
6. Mobility or initiative control
7. Information or sensing
8. Terrain and travel override
9. Social or narrative leverage

### High-risk talent categories

#### Automatic success or success substitution

Examples:

- treating a zero-success roll as one success
- buying success directly with WP
- auto-succeeding at Dodge or similar gates

Why risky:

- these interact strongly with challenging and difficult thresholds
- they reduce variance in the most tactically important moments

#### Action compression

Examples:

- extra fast actions
- extra attacks
- immediate slow actions
- free reactive actions

Why risky:

- action economy advantages often outscale raw dice bonuses
- they change not just output but opportunity structure

#### Recovery bypass

Examples:

- healing all damage
- healing critical injuries
- restoring attributes above starting values

Why risky:

- these can erase long-term pressure, not just scene pressure

#### Armor bypass and direct damage scaling

Examples:

- ignore armor
- spend WP for direct damage
- force critical injuries

Why risky:

- these attack the main defensive layers of the game directly

### Strong niche designs

The strongest talent design in this manuscript usually does one thing well while preserving the rest of the engine.

Examples of healthy specialization:

- terrain-specific bonuses
- prey-marking and hunt focus
- rescue and interception roles
- shield control and defensive projection

These produce identity without universally solving problems.

### Red-flag patterns for future additions

- any talent that turns variable outcomes into fixed success too often
- any talent that grants extra actions repeatedly with low WP cost
- any talent that refunds WP on the same loop that spends it
- any talent that removes both recovery friction and critical-injury weight

## Spell-System Volatility

Magic is not balanced around failure chance.
It is balanced around:

- unavoidable effect
- variable overcharge
- mishap exposure

### Base spell model

If you spend `n` WP, you roll `n` Base Dice, modified by:

- spell rank relative to talent rank
- grimoires
- safe casting

Outcomes:

- expected extra Power Level from swords = `n / 6`
- chance of at least one mishap trigger = `1 - (5/6)^n`

### Mishap and overcharge table

| WP Dice | Mishap Chance | Expected Extra Power | Chance Of 2+ Extra Power |
| ------- | ------------- | -------------------- | ------------------------ |
| 1       | 16.67%        | 0.1667               | 0.00%                    |
| 2       | 30.56%        | 0.3333               | 2.78%                    |
| 3       | 42.13%        | 0.5000               | 7.41%                    |
| 4       | 51.77%        | 0.6667               | 13.19%                   |
| 5       | 59.81%        | 0.8333               | 19.62%                   |
| 6       | 66.51%        | 1.0000               | 26.32%                   |
| 7       | 72.09%        | 1.1667               | 33.02%                   |
| 8       | 76.74%        | 1.3333               | 39.53%                   |
| 9       | 80.62%        | 1.5000               | 45.73%                   |
| 10      | 83.85%        | 1.6667               | 51.55%                   |

### Immediate reading

The system is aggressive about mishap risk.

At:

- `3 WP`, mishaps are already at `42.13%`
- `5 WP`, mishaps are at `59.81%`
- `6 WP`, mishaps are at `66.51%`

So high-power casting is meant to feel unstable, not merely expensive.

### Safe-casting significance

Safe casting is one of the most important stabilizers in the system.

It allows:

- lower-rank spell use with reduced dice
- up to zero dice, which makes the spell resolve as intended

This means rank advantage in magic is not only stronger spells.
It is also:

- lower volatility
- lower mishap frequency
- more deterministic access to utility

### Grimoires as stability technology

Grimoires effectively reduce spell rank by one.

Implication:

- grimoires are not just convenience items
- they are risk-management tools

That makes grimoire access a major balancing lever in the campaign economy.

### Chance casting

Chance casting forces an automatic mishap.

This is a sound design stopgap because it prevents:

- casual overreach at rank boundaries
- easy access to higher-rank utility without consequence

### Hidden high-risk interactions

The following talent patterns are especially explosive when paired with magic:

- effective extra WP value
- reduced Power Level cost
- WP refunds
- emergency WP substitution from attributes

These do not only make spells stronger.
They also change the risk curve the spell system assumes.

## Damage And Recovery Pressure

### Damage-state logic

The game's danger is not just HP loss.
It is a layered state model:

1. attribute damage reduces effective pools
2. Broken states remove agency
3. critical injuries convert scene loss into campaign cost
4. conditions block recovery and can become death spirals

### Speed of pressure

Some damage channels are fast:

- combat hits
- poison
- fear
- fire

Some are slow:

- hunger
- thirst
- disease
- sleep loss
- cold exposure over time

This is good design because it lets the game threaten both:

- immediate survival
- expedition continuity

### Recovery bottlenecks

Recovery is intentionally fragmented.

Attributes are not all restored from the same sources:

- Strength: food or alcohol on short break
- Agility: water
- Empathy: liquor or high-grade food
- Wits: tobacco
- Willpower: narcotics

This means recovery is not a single “rest to full” button.
It is a logistics puzzle.

### Camp as recovery multiplier

Successful `MAKE CAMP` does more than avoid discomfort.
Extra successes:

- improve hiddenness
- increase attribute recovery

That means camp quality is mathematically tied to long-run attrition.
It is not flavor-only.

### Conditions as anti-recovery rules

Conditions matter because they selectively shut doors:

- `HUNGRY` blocks Strength recovery
- `THIRSTY` blocks all attribute recovery
- `SLEEPY` blocks Wits recovery
- `COLD` blocks Strength and Wits recovery
- `ADDICTED` blocks Empathy recovery

Design implication:

- resource scarcity does not only deal damage
- it also disables the systems that would normally remove damage

This is efficient pressure design.

### Critical injury pressure

Being Broken is already costly.
Critical injuries escalate that into:

- lethal timers
- long healing times
- action restrictions
- retirement-default outcomes in some cases

Care halves healing time.
That is a very strong compression effect.

If a future rule grants repeated or easy “care” equivalents, it will flatten one of the main campaign brakes in the system.

### Fast versus slow recovery

Fast recovery channels:

- healing skill to get someone back on their feet
- short breaks with the right resources
- some talent or spell effects

Slow recovery channels:

- natural camp and sleep loops
- critical injury healing time
- disease progression

Healthy pressure comes from preserving the tension between these two.

If too many rules move slow recovery into fast recovery, campaign danger collapses.

### Broken-state pressure formula

Because attributes also determine dice pools, damage has a non-linear effect:

- each lost point reduces future success rates
- lower success rates invite more pushing
- more pushing increases more damage and WP volatility

This is one of the engine's most elegant loops:

- damage does not only move you toward death
- it makes every future decision sharper

## Design Conclusions

### 1. Willpower is the master coupling

Most of the game's swingiest systems meet at WP.

Any proposal that touches WP generation, discounts, refunds, or emergency substitutes should be treated as system-critical.

### 2. Talent balance is mostly about exception shape, not raw count

The danger is not “too many talents.”
The danger is:

- auto-success
- action compression
- armor bypass
- recovery bypass
- refund loops

Those are the destabilizing categories.

### 3. Magic is volatile by design

The spell system assumes:

- high effect reliability
- meaningful mishap frequency

If a proposal reduces mishap exposure too far, it turns magic from unstable leverage into dominant utility.

### 4. Recovery is a logistical subsystem, not only a healing subsystem

Food, water, shelter, sleep, camp quality, healing, and condition removal all participate in one pressure network.

Future rules should respect that network instead of solving only one local inconvenience.

### 5. The engine works because pressure layers stack

The game remains sharp when:

- pushing hurts
- WP matters
- spells stay risky
- recovery stays fragmented
- critical injuries stay consequential

That stack is the design spine.
