<!-- markdownlint-disable MD013 -->

# Engine Math And Rule Taxonomy

## Contents

1. Scope
2. System Map
3. Rule Taxonomy
4. Core Mathematical Grammar
5. Baseline Success Probabilities
6. Pushed-Roll Mathematics
7. Mixed Pool Findings
8. Design Implications

## Scope

This reference executes steps 1 through 5 of the `forbidden-lands-design` research plan:

1. full system map
2. rule-type catalog
3. core mathematical grammar
4. baseline success probabilities
5. pushed-roll outcome model

It is meant to give the skill a real analytical base instead of a generic design checklist.

## System Map

The corebook is not one rules engine. It is a stack of connected loops.

Each major chapter below is summarized by:

- inputs
- outputs
- costs
- risks
- downstream consequences

### Chapter 3: Skills

Primary function:

- universal action resolution grammar

Inputs:

- attribute dice
- skill dice
- gear dice
- roll modifiers
- player choice to push or not push

Outputs:

- successes
- banes after a push
- partial escalation into Willpower, damage, or gear loss

Costs:

- risk exposure when pushing
- time, action, or narrative commitment

Risks:

- attribute damage from pushed base dice
- gear damage from pushed gear dice
- failed action despite investment

Downstream consequences:

- Willpower generation
- combat efficacy
- travel success
- crafting throughput
- healing and recovery chance

### Chapter 4: Talents

Primary function:

- exception layer and power specialization

Inputs:

- Willpower
- rank investment
- scene state

Outputs:

- rule exceptions
- bonus dice
- altered recovery
- action compression
- improved damage, defense, or utility

Costs:

- Willpower spending
- XP investment

Risks:

- overpowering existing procedures
- collapsing niches if too broad

Downstream consequences:

- changes to action economy
- changes to survivability
- access to stronger magic and recovery tools

### Chapter 5: Combat And Damage

Primary function:

- convert conflict choices into immediate danger

Inputs:

- initiative result
- action choice
- attack and defense rolls
- armor
- weapon data

Outputs:

- damage
- Broken states
- positioning and tempo changes

Costs:

- actions
- ammunition or gear wear
- exposure to counterattack

Risks:

- rapid attribute collapse
- critical injury entry

Downstream consequences:

- Chapter 6 injuries
- healing demand
- gear attrition
- tactical tempo shifts

### Chapter 6: Critical Injuries

Primary function:

- translate defeat into lasting consequence

Inputs:

- Broken result
- damage type
- D66 roll
- healing intervention

Outputs:

- healing time
- lethal countdowns
- permanent or semi-permanent effects

Costs:

- lost time
- care resources
- party tempo

Risks:

- death
- retirement-default states
- long-term impairment

Downstream consequences:

- healing bottlenecks
- campaign pacing
- playability and character continuity

### Chapter 7: Magic

Primary function:

- convert Willpower into unstable leverage

Inputs:

- Willpower spent
- discipline rank
- overcharge roll
- mishap roll

Outputs:

- spell effect
- increased Power Level
- mishap consequences

Costs:

- Willpower
- action time
- teacher and advancement investment

Risks:

- mishaps
- unsafe scaling
- chance-casting collapse

Downstream consequences:

- battlefield swing
- travel bypass
- healing bypass
- subsystem invalidation if costs are too low

### Chapter 8: Journeys

Primary function:

- make the landscape an active source of pressure

Inputs:

- Quarter Day allocation
- terrain
- weather
- forage and hunt rolls
- camp quality

Outputs:

- movement
- resource consumption
- encounters
- conditions

Costs:

- time
- food and water
- shelter effort

Risks:

- conditions
- lost tempo
- attrition before reaching the main site

Downstream consequences:

- weakened party entering adventure scenes
- dependence on gear, strongholds, and talents

### Chapter 9: Stronghold

Primary function:

- convert long-term wealth into infrastructure

Inputs:

- materials
- labor
- time
- crafting

Outputs:

- housing
- functions
- safe recovery and production spaces

Costs:

- materials
- time
- vulnerability to attention

Risks:

- static commitments
- economy imbalance

Downstream consequences:

- stronger downtime loops
- improved access to recovery, crafting, and social leverage

### Chapter 10: Gear

Primary function:

- materialize preparedness, specialization, and scarcity

Inputs:

- money
- supply rolls
- raw materials
- tools
- crafting time

Outputs:

- item access
- bonus dice
- armor
- resource pools

Costs:

- price
- rarity
- encumbrance
- crafting prerequisites

Risks:

- scarcity bottlenecks
- repair difficulty
- overreliance on rare tools

Downstream consequences:

- higher success rates
- stronger survival odds
- economy and logistics pressure

## Rule Taxonomy

The game uses a finite set of recurring rule types.
This matters because new rules should usually plug into an existing type rather than invent a new category.

### 1. Resolution rules

Examples:

- skill rolls
- opposed rolls
- modification dice
- difficulty thresholds

Core question:

- how many successes are rolled

### 2. Push rules

Examples:

- reroll all non-locked dice
- activate banes
- gain Willpower from base banes
- degrade gear from gear banes

Core question:

- how much extra success is worth the added risk

### 3. Action-economy rules

Examples:

- slow actions
- fast actions
- initiative order
- free reactions from talents

Core question:

- who acts, when, and at what opportunity cost

### 4. Damage-state rules

Examples:

- attribute damage
- Broken thresholds
- critical injury entry
- armor mitigation

Core question:

- how quickly failure becomes incapacitation

### 5. Recovery rules

Examples:

- healing rolls
- care halving recovery time
- resting
- talent or spell recovery exceptions

Core question:

- how long pressure persists after a setback

### 6. Resource rules

Examples:

- Willpower
- resource dice
- supply access
- raw materials

Core question:

- what can be spent, depleted, or replenished

### 7. Travel-pressure rules

Examples:

- Quarter Day allocation
- movement by terrain
- camp quality
- forage and hunt
- conditions

Core question:

- what the world extracts from movement

### 8. Exception rules

Examples:

- talents
- spells
- artifacts

Core question:

- what baseline rule is being bent, bypassed, or amplified

### 9. Advancement rules

Examples:

- XP costs
- teacher requirements
- rank unlocks

Core question:

- how power accumulates over time

### 10. Economy and access rules

Examples:

- supply ratings
- item rarity
- building functions

Core question:

- what capabilities are locally available and at what friction

## Core Mathematical Grammar

The engine's mathematics begin with a simple success model and then branch into different risk channels.

### Base action formula

A standard pool is:

- Base Dice from attribute
- Skill Dice from skill
- Gear Dice from useful equipment

Each die succeeds on a `6`.

Difficulty tiers:

- Normal: 1 success
- Challenging: 2 successes
- Difficult: 3 successes

### Initial-roll success model

For an unpushed die:

- success probability per die = `1/6`
- non-success probability per die = `5/6`

For `n` identical dice on the first roll:

- `P(at least 1 success) = 1 - (5/6)^n`
- `P(at least k successes) = sum from i=k to n of C(n,i) * (1/6)^i * (5/6)^(n-i)`

### Push lifecycle by die type

The manuscript's current rules make skill dice mathematically different from base and gear dice.

#### Skill die after one legal push

- `6` on first roll stays
- `1` on first roll rerolls
- `2-5` on first roll reroll
- `1` never counts as a bane

So for one skill die after a full one-push lifecycle:

- success = `11/36 = 0.3056`
- blank = `25/36 = 0.6944`

#### Base die after one legal push

- `6` on first roll stays as success
- `1` on first roll locks and becomes a bane if the roll is pushed
- `2-5` reroll

So for one base die after a full one-push lifecycle:

- success = `2/9 = 0.2222`
- bane = `1/6 = 0.1667`
- blank = `11/18 = 0.6111`

#### Gear die after one legal push

Mathematically identical to a base die for success rate:

- success = `2/9 = 0.2222`
- bane = `1/6 = 0.1667`
- blank = `11/18 = 0.6111`

But the consequence channel differs:

- base bane -> attribute damage and 1 WP
- gear bane -> gear or weapon bonus loss, no WP

### Important asymmetry

Adding one skill die to a pushed pool is stronger than adding one base or gear die:

- higher pushed success rate
- no bane exposure
- no gear wear

This is one of the central hidden mathematical facts of the system.

## Baseline Success Probabilities

### Initial roll by pool size

This table treats the pool as homogeneous for first-roll purposes, which is valid because all dice succeed on `6` before push distinctions matter.

| Dice | 1+ Success | 2+ Success | 3+ Success |
| ---- | ---------- | ---------- | ---------- |
| 1    | 16.67%     | 0.00%      | 0.00%      |
| 2    | 30.56%     | 2.78%      | 0.00%      |
| 3    | 42.13%     | 7.41%      | 0.46%      |
| 4    | 51.77%     | 13.19%     | 1.62%      |
| 5    | 59.81%     | 19.62%     | 3.55%      |
| 6    | 66.51%     | 26.32%     | 6.23%      |
| 7    | 72.09%     | 33.02%     | 9.58%      |
| 8    | 76.74%     | 39.53%     | 13.48%     |
| 10   | 83.85%     | 51.55%     | 22.48%     |
| 12   | 88.78%     | 61.87%     | 32.26%     |

### Why the first-roll table is not enough

Once push enters, pool composition matters.

A 6-die pool built from:

- `4 Base + 2 Skill`
- `3 Base + 3 Skill`
- `4 Base + 1 Skill + 1 Gear`

does not behave the same after a push, even though the initial chance is identical.

## Pushed-Roll Mathematics

### Homogeneous reference table

If a pool is approximated using the base/gear pushed die rate of `2/9` success per die, the pushed chances look like this:

| Dice | 1+ Success | 2+ Success | 3+ Success |
| ---- | ---------- | ---------- | ---------- |
| 1    | 22.22%     | 0.00%      | 0.00%      |
| 2    | 39.51%     | 4.94%      | 0.00%      |
| 3    | 52.95%     | 12.62%     | 1.10%      |
| 4    | 63.40%     | 21.58%     | 3.66%      |
| 5    | 71.54%     | 30.88%     | 7.64%      |
| 6    | 77.86%     | 39.91%     | 12.80%     |
| 7    | 82.78%     | 48.35%     | 18.83%     |
| 8    | 86.61%     | 56.00%     | 25.39%     |
| 10   | 91.90%     | 68.75%     | 38.99%     |
| 12   | 95.10%     | 78.30%     | 51.89%     |

This is useful as a lower-risk baseline for base-heavy pools, but it understates pushed performance for skill-heavy pools.

### Expected bane load on pushed base or gear dice

For `m` pushed base dice:

- expected base banes = `m / 6`
- expected Willpower from those dice = `m / 6`

For `m` pushed gear dice:

- expected gear banes = `m / 6`

Probability of at least one base bane on a pushed set:

| Pushed Base Dice | 1+ Base Bane | 2+ Base Banes |
| ---------------- | ------------ | ------------- |
| 1                | 16.67%       | 0.00%         |
| 2                | 30.56%       | 2.78%         |
| 3                | 42.13%       | 7.41%         |
| 4                | 51.77%       | 13.19%        |
| 5                | 59.81%       | 19.62%        |
| 6                | 66.51%       | 26.32%        |

This means a character who pushes 4 base dice is already more likely than not to take at least one attribute damage and gain at least one WP.

## Mixed Pool Findings

The table below shows common pool shapes.

Notation:

- `B/S/G` = Base / Skill / Gear dice
- pushed values assume one legal push
- `EBaseBanePush` = expected attribute damage from pushed base dice
- `EGearBanePush` = expected weapon or gear bonus loss
- `EWPpush` = expected Willpower gained from pushed base dice

| B/S/G | Init 1+ | Push 1+ | Init 2+ | Push 2+ | Init 3+ | Push 3+ | EBaseBanePush | EGearBanePush | EWPpush |
| ----- | ------- | ------- | ------- | ------- | ------- | ------- | ------------- | ------------- | ------- |
| 2/2/0 | 51.77%  | 70.83%  | 13.19%  | 28.48%  | 1.62%   | 5.78%   | 0.3333        | 0.0000        | 0.3333  |
| 3/2/0 | 59.81%  | 77.31%  | 19.62%  | 37.89%  | 3.55%   | 10.83%  | 0.5000        | 0.0000        | 0.5000  |
| 4/2/0 | 66.51%  | 82.35%  | 26.32%  | 46.65%  | 6.23%   | 16.84%  | 0.6667        | 0.0000        | 0.6667  |
| 3/3/0 | 66.51%  | 84.24%  | 26.32%  | 49.94%  | 6.23%   | 19.10%  | 0.5000        | 0.0000        | 0.5000  |
| 4/3/0 | 72.09%  | 87.74%  | 33.02%  | 57.56%  | 9.58%   | 25.95%  | 0.6667        | 0.0000        | 0.6667  |
| 4/3/1 | 76.74%  | 90.47%  | 39.53%  | 64.27%  | 13.48%  | 32.98%  | 0.6667        | 0.1667        | 0.6667  |
| 3/3/2 | 76.74%  | 90.47%  | 39.53%  | 64.27%  | 13.48%  | 32.98%  | 0.5000        | 0.3333        | 0.5000  |
| 5/3/1 | 80.62%  | 92.59%  | 45.73%  | 70.09%  | 17.83%  | 39.93%  | 0.8333        | 0.1667        | 0.8333  |

### Immediate reading

Two pools with the same total dice can have the same initial success odds but very different pushed behavior.

Example:

- `4/3/1` and `3/3/2` have the same pushed success rates
- but `4/3/1` produces more expected Willpower
- while `3/3/2` produces more expected gear damage

So the composition of a pool matters not only for success, but for the kind of pressure it generates.

## Design Implications

### 1. Skill dice are premium dice

Because skill dice reroll ones on a push and never trigger banes, they are the safest dice in the system once push is on the table.

Implication:

- bonuses that become skill-like dice are mathematically stronger than plain pool-size increases suggest

### 2. Base dice create a risk-power exchange

Base dice are the only push dice that both:

- hurt the character
- feed Willpower

Implication:

- any rule that reduces base-die bane cost without also touching WP gain can distort the Willpower economy

### 3. Gear dice are pressure without payoff

Gear dice improve success odds, but when pushed they add risk without generating Willpower.

Implication:

- gear-heavy builds gain reliability, but pay for ambition in durability rather than in self-generated power

### 4. Challenge and difficult thresholds rise steeply

The jump from 1 success to 2 or 3 successes is large.

Implication:

- any rule that grants automatic successes or converts WP directly into successes can reshape the game faster than raw dice bonuses do

### 5. Pool composition is a design lever

When designing a new talent, item, or spell bonus, the question is not just:

- how many dice does this add

It is also:

- what kind of dice are they
- what risk channel do they activate on a push
- do they produce Willpower, gear loss, or neither

That is a much more precise way to reason about balance in this engine.
