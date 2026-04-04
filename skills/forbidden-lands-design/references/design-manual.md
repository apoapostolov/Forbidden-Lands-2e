<!-- markdownlint-disable MD013 -->

# Forbidden Lands 2E Design Manual

## Contents

1. Purpose
2. Design Identity
3. Core Loops
4. Rule Taxonomy
5. Mathematical Spine
6. Pressure Economy
7. Willpower Economy
8. Subsystem Design Notes
9. Critical Consequence Design
10. Travel And Logistics Design
11. Gear And Material Design
12. Talent And Spell Risk Categories
13. Realism Boundary
14. Proposal Audit Workflow
15. Synergy Framework
16. Expansion Framework
17. Mathematical Calibration Rules
18. Practical Use

## Purpose

This is the unified manual for the `forbidden-lands-design` skill.

It consolidates the analytical work from the supporting references into one research-grade source document that can be loaded when the AI needs a complete picture of how this game works, why it works, where it is fragile, and how to extend it without flattening its identity.

Use this document when:

- auditing a major proposal
- planning a new subsystem
- evaluating rule balance or interaction depth
- deciding whether a realism-driven change belongs in the manuscript
- identifying whether a change is local or system-level

Use the smaller reference documents when only one slice is needed.

## Design Identity

Forbidden Lands 2E works because it ties ambition to exposure.

The player characters are not protected protagonists.
They are capable, desperate, fallible people who push into danger because reward exists only beyond hardship.

The system's identity rests on these tensions:

- risk versus reward
- speed versus safety
- power versus mishap
- preparation versus scarcity
- survival versus lasting cost

This means the game is not designed around equal comfort across all systems.
It is designed around layered pressure that forces judgment.

The game should remain:

- harsh
- practical
- materially grounded
- unforgiving but legible
- survivable at a price

## Core Loops

The game is best understood as a stack of interacting loops rather than as isolated chapters.

### Expedition loop

- prepare
- travel
- spend resources
- absorb friction and attrition
- reach a site
- risk injury for gain
- withdraw, recover, rearm

Purpose:

- make exploration meaningful through cost

### Conflict loop

- roll initiative
- choose action
- resolve
- decide whether to push
- absorb consequences
- alter tempo, position, or injury state

Purpose:

- make violence tactically sharp and strategically dangerous

### Recovery loop

- become damaged or Broken
- stabilize
- rest, heal, or use exceptional tools
- recover partially or fully
- carry lasting consequences where required

Purpose:

- ensure survival is not a clean reset

### Willpower loop

- attempt difficult action
- push
- suffer risk
- gain Willpower
- spend Willpower on talents and spells

Purpose:

- convert desperation into leverage

### Settlement loop

- gather wealth and materials
- construct or improve stronghold
- gain functions and safety
- assume new obligations

Purpose:

- let long-term success reshape campaign structure

## Rule Taxonomy

The manuscript uses recurring rule families.
Most new design should extend one of these rather than inventing a new category.

### Resolution rules

- skill rolls
- opposed rolls
- threshold tiers
- modifiers

### Push rules

- reroll non-locked dice
- activate banes
- gain Willpower from pushed base banes
- damage gear on pushed gear banes

### Action-economy rules

- slow and fast actions
- initiative
- reactive actions
- action compression exceptions

### Damage-state rules

- attribute damage
- Broken states
- armor mitigation
- critical injury entry

### Recovery rules

- healing
- care
- rest
- sleep
- condition removal

### Resource rules

- Willpower
- resource dice
- supply access
- raw materials

### Travel-pressure rules

- Quarter Day allocation
- movement by terrain
- forage and hunt
- camp quality
- darkness and weather

### Exception rules

- talents
- spells
- artifacts

### Advancement rules

- XP spend
- rank gates
- teacher requirements

### Access and economy rules

- item rarity
- village supply
- stronghold functions
- specialist tools

## Mathematical Spine

The engine's mathematics are simple at entry and sharp in consequence.

### Base success grammar

Each die succeeds on `6`.

Difficulty thresholds:

- Normal: `1` success
- Challenging: `2` successes
- Difficult: `3` successes

Initial roll model for `n` dice:

- `P(1+) = 1 - (5/6)^n`

The 2+ and 3+ tiers rise steeply.
That is one of the engine's central balancing features.

### Push asymmetry

Not all dice are equal on a push.

After one legal push:

- skill die success rate = `11/36 = 30.56%`
- base die success rate = `2/9 = 22.22%`
- gear die success rate = `2/9 = 22.22%`

Additional push consequences:

- base bane rate = `1/6` and grants `1 WP`
- gear bane rate = `1/6` and causes wear
- skill dice do not trigger bane effects

This means:

- skill dice are premium dice in pushed pools
- base dice are power-risk dice
- gear dice are reliability-with-wear dice

### Threshold sensitivity

The game is mathematically sensitive to any change that:

- increases per-die success odds
- grants automatic successes
- changes action costs
- compresses recovery times

These are premium change categories and should never be treated as small edits.

## Pressure Economy

The game is built on stacked pressure rather than flat fairness.

Primary pressure sources:

- reduced attributes
- critical injuries
- conditions
- gear wear
- resource-die decay
- travel time
- weather exposure
- scarcity of tools and functions
- magical mishaps

Design rule:

Do not ask only whether a rule is strong.
Ask which pressure it relieves, which pressure it adds, and whether it quietly cancels a pressure source another chapter depends on.

## Willpower Economy

Willpower is the master coupling in the game.

It sits at the center of:

- pushing
- talents
- magic
- emergency survivability
- burst offense

### Generation

Willpower is primarily gained from pushed Base Dice.

For `m` pushed Base Dice:

- expected `WP = m / 6`
- `P(1+ WP) = 1 - (5/6)^m`

This is a deliberate throttle.
Power comes from danger, not passive recharge.

### Spend profile

The talent chapter strongly centers on `1 WP` effects.

That means even a single extra reliable point of WP matters a great deal.

One point of WP often buys:

- one success-equivalent edge
- one point of damage or mitigation
- one tempo shift
- one spell power increment
- one activation of a decisive exception

### Design rule

Any rule that changes:

- WP generation
- WP discounting
- WP refunding
- emergency WP substitution

should be treated as system-critical.

## Subsystem Design Notes

### Skills

Function:

- universal action grammar

Good design:

- reuses the dice grammar cleanly
- preserves pushing as a meaningful choice
- avoids nested edge-case logic

### Talents

Function:

- exception layer and character specialization

Good design:

- grants a distinct edge
- preserves adjacent niches
- keeps exception handling legible

### Combat

Function:

- convert action choice into immediate danger

Good design:

- keeps action economy tight
- lets offense feel tempting but costly

### Critical injuries

Function:

- convert defeat into durable consequence

Good design:

- tells the truth about survivability and playability
- maps penalties to existing procedures
- preserves fear without collapsing the campaign by default

### Magic

Function:

- give characters unstable leverage

Good design:

- ensures effect reliability comes with volatility
- prevents safe universal bypass of mundane hardship

### Journeys

Function:

- make the landscape an active adversary

Good design:

- turns time into meaningful cost
- makes logistics playable
- avoids empty bookkeeping

### Gear

Function:

- materialize preparedness and specialist access

Good design:

- solves a concrete problem
- has believable scarcity
- does not erase the value of talents, functions, or proper tools

### Stronghold

Function:

- convert wealth into infrastructure

Good design:

- lowers friction in exchange for rootedness, cost, and vulnerability

## Critical Consequence Design

Critical injuries are one of the manuscript's defining strengths.

They create a layered consequence structure:

- scene loss
- survival at cost
- long-term impairment
- retirement-default states
- death

Best practice for injury design:

- separate survivable catastrophe from annihilation
- be explicit about retirement-default outcomes
- preserve compatibility with healing and regeneration systems
- avoid modern clinical language that breaks manuscript voice

Design warning:

- if healing exceptions compress injury time too easily, Chapter 6 becomes cosmetic

## Travel And Logistics Design

Journeys are the primary sustained attrition engine.

Their strength lies in converting time into choices.

Quarter Days force tradeoffs between:

- movement
- scouting
- foraging
- hunting
- surveying
- camp preparation
- rest and sleep

Best practice:

- deepen decisions, not maintenance
- expand camp posture, field medicine, load discipline, and weather adaptation
- preserve the cost of staying alive while traveling

## Gear And Material Design

Gear should not be read as a store list.
It is a rules layer for:

- reliability
- readiness
- specialization
- scarcity

Best existing patterns:

- tool gating
- resource-die gear
- material substitution with tradeoffs
- profession-specific gear depth

Most promising expansion directions:

- field medicine tools
- haul and shelter tools
- weatherproofing supplies
- clearer expedition-grade versus workshop-grade equipment

## Talent And Spell Risk Categories

The most dangerous exception categories are:

- automatic success or success substitution
- action compression
- armor bypass
- direct critical-injury access
- recovery bypass
- WP refund and discount loops

Magic must remain volatile by design.

At moderate WP spend, mishap odds already become significant.
That volatility is not a flaw.
It is the balancing structure that allows spells to be reliable in effect.

Design warning:

- any new stabilizer added to magic must be weighed against grimoires, safe casting, rank advantage, and existing cost reducers

## Realism Boundary

Realism belongs in the game when it improves play.

Good realism:

- sharpens choices
- improves consequence credibility
- connects rule to material reality

Bad realism:

- adds procedure without judgment
- stalls the campaign
- produces hidden non-playability
- forces GM mercy to remain tolerable

Practical realism test:

1. What decision becomes sharper?
2. What abstraction is being clarified?
3. What table burden is added?
4. Does campaign movement survive?
5. Is any resulting non-playability described honestly?

## Proposal Audit Workflow

Use this sequence:

1. define the actual problem
2. identify chapter ownership
3. classify rule type
4. trace subsystem integration
5. evaluate table speed
6. evaluate player agency
7. separate proposal rationale from manuscript prose

Verdicts:

- `Accept now`
- `Accept with simplification`
- `Hold for broader rewrite`
- `Reject for now`
- `Reject as wrong chapter / wrong rule type`

## Synergy Framework

Synergy matters most where one rule changes the assumptions of another pressure channel.

High-risk synergy categories:

- WP multiplier loops
- action-compression loops
- defense-bypass stacking
- recovery-collapse stacking
- travel-pressure nullification

When evaluating synergy, ask:

1. what cost does this reduce
2. what pressure does it bypass
3. what refund, auto-success, or tempo effect can it stack with
4. does it become a repeatable dominant line

## Expansion Framework

Expand by:

- adding decisions
- preserving existing niches
- reusing current grammar
- deepening the middle of play rather than only the extremes

Promising expansion areas:

- mundane field medicine
- camp discipline and posture
- logistics under duress
- non-magical weather adaptation
- expedition labor and delegation
- social leverage through equipment and preparation

Avoid:

- new tracking layers with weak decisions
- broad bypasses of attrition
- subsystem inflation where existing structures already suffice

## Mathematical Calibration Rules

Treat these as high-sensitivity levers:

- per-die success odds
- automatic successes
- slow-to-fast or fast-to-free action changes
- repeated push permission
- recovery-time halving
- easy WP refunds

Examples already established in the skill's supporting analysis:

- raising die success from `1/6` to `2/6` radically inflates all difficulty tiers
- care halving healing time is already a very strong tempo effect
- a stepdown resource chain like `D12 -> D10 -> D8 -> D6 -> lost` yields meaningful durability without permanence

## Practical Use

When answering a design question with this manual, use this order:

1. current mechanics
2. relevant loop or subsystem
3. pressure channels affected
4. mathematical implications
5. synergy or integration risks
6. recommendation

When auditing a proposal:

1. identify the real problem
2. identify the owning chapter
3. test whether the proposal preserves the pressure stack
4. test whether realism improves decisions
5. decide whether it belongs in proposal space or manuscript space

This is the governing principle of the manual:

The manuscript stays strong when it preserves a harsh but legible stack of pressures, lets risk buy power without making that power free, and tells the truth about the cost of survival.
