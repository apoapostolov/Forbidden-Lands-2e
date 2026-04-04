<!-- markdownlint-disable MD013 -->

# System Design Map

## Contents

1. Core Design Identity
2. Primary Gameplay Loops
3. Pressure Economy
4. Chapter Map
5. Interaction Surfaces
6. Design Logic By System
7. Proposal Integration Method
8. Warning Signs

## Core Design Identity

Forbidden Lands works because it ties ambition to exposure.

The characters are not protected heroes. They are hungry, driven opportunists moving through a hard landscape where travel, wounds, scarcity, weather, and magic all exact a price.

The system's design identity rests on these tensions:

- risk versus reward
- speed versus safety
- power versus mishap
- scarcity versus preparation
- survivability versus long-term cost

Any new rule that ignores those tensions may function locally while still breaking the larger game.

## Primary Gameplay Loops

### 1. Expedition loop

Sequence:

- prepare
- travel
- spend resources
- face encounters and environmental pressure
- reach site
- risk injury or gain treasure
- retreat, recover, rearm

Design purpose:

- survival pressure makes exploration meaningful
- logistics and risk assessment are part of play, not prep outside play

### 2. Conflict loop

Sequence:

- initiative
- action choice
- roll
- push or accept
- immediate consequence
- injury, positioning, or loss of tempo

Design purpose:

- combat is dangerous enough that choosing it matters
- tactical decisions are simple but costly

### 3. Recovery loop

Sequence:

- become damaged, Broken, or conditioned
- survive the immediate crisis
- rest, heal, use talents, use magic
- recover partially or completely
- carry lasting consequences where rules specify

Design purpose:

- the game does not only ask whether you survive the fight
- it asks what surviving costs

### 4. Willpower loop

Sequence:

- attempt difficult action
- push
- accept risk from banes
- gain Willpower
- spend Willpower on talents or spells

Design purpose:

- desperation feeds power
- players are rewarded for risk-taking, but never for free

### 5. Base-building loop

Sequence:

- gather wealth and materials
- establish or improve stronghold
- gain functions, safety, and status
- attract new obligations and vulnerabilities

Design purpose:

- long-term success alters campaign shape
- security becomes another asset to defend

## Pressure Economy

The game is built on layered pressure rather than single-axis balance.

### Main pressure sources

- low attribute scores after damage
- critical injuries
- conditions
- gear wear
- resource dice shrinking
- travel time
- weather and shelter exposure
- scarcity of expert tools and functions
- mishaps from overreach

### Design implication

Do not evaluate a rule in isolation.
Ask which pressure it relieves, which pressure it adds, and whether it accidentally cancels a core source of tension elsewhere.

## Chapter Map

### Chapter 2: Adventurer creation

Design role:

- sets the initial ceiling and identity of a character
- shapes long-term differentiation through kin, profession, and age

Common integration questions:

- does a new rule privilege one kin or profession too strongly
- does it invalidate a character creation choice

### Chapter 3: Skills

Design role:

- establishes the core resolution grammar
- success thresholds, pushing, and banes all cascade outward from here

Common integration questions:

- does the rule create new roll logic that should instead reuse the base grammar
- does it overload success symbols or bane symbols inconsistently

### Chapter 4: Talents

Design role:

- introduces exceptions, specializations, and power expression
- many local balance problems are actually talent interaction problems

Common integration questions:

- does the new rule become trivial or broken with an existing talent
- does it invalidate a talent's niche

### Chapter 5: Combat and damage

Design role:

- translates action choice into danger quickly
- makes violence costly, not routine

Common integration questions:

- does the rule alter action economy
- does it change how often characters become Broken
- does it create new initiative edge cases

### Chapter 6: Critical injuries

Design role:

- converts defeat into consequence
- differentiates short-term loss from permanent cost

Common integration questions:

- is the injury survivable, playable, retirement-default, or fatal
- how does healing or regeneration interact with it
- does the rule still feel honest about the cost of survival

### Chapter 7: Magic

Design role:

- gives characters explosive leverage with built-in instability

Common integration questions:

- does the new rule stack with Willpower economies too efficiently
- does it erase attrition that other systems rely on
- does it introduce safe casting by accident

### Chapter 8: Journeys

Design role:

- makes the landscape an active adversary
- sustains the expedition loop

Common integration questions:

- does the new rule shortcut time, weather, supply, or shelter too cheaply
- does it add table burden without real tension

### Chapter 9: Stronghold

Design role:

- converts campaign success into infrastructure
- trades mobility for rooted value

Common integration questions:

- does the rule belong here or in gear, hirelings, or journeys
- does it create an economy exploit

### Chapter 10: Gear

Design role:

- gives material expression to preparedness, scarcity, and specialization

Common integration questions:

- is the item solving a real gap
- does it displace proper tools, talents, or stronghold functions
- should it use a resource die

## Interaction Surfaces

Every new rule should be checked against these recurring interaction surfaces:

- push mechanics
- Willpower generation and spending
- healing and recovery reduction
- travel pace and Quarter Day use
- specialist tools versus makeshift tools
- condition removal
- armor and damage reduction
- talent-based exceptions
- spell power scaling
- resource die attrition

If a proposal touches two or more of these, it needs a deeper integration pass.

## Design Logic By System

### Skills

Good design:

- preserves the simple dice grammar
- makes extra successes matter only when the action supports it
- avoids nested exceptions

### Talents

Good design:

- grants a distinct edge
- does not rewrite the whole engine casually
- stays legible in live play

### Injuries

Good design:

- matches severity to actual play consequence
- uses names that fit the manuscript
- tells the truth about long-term cost

### Gear

Good design:

- solves a concrete need
- has a believable place in the economy
- does not make specialist equipment irrelevant

### Journeys

Good design:

- adds pressure or meaningful choice
- does not reduce travel to bookkeeping without drama

### Magic

Good design:

- offers dramatic payoff
- leaves room for catastrophe
- does not become the universal answer to ordinary hardship

## Proposal Integration Method

When reviewing a proposal:

1. State the exact problem it tries to solve.
2. Identify which chapter actually owns that problem.
3. Trace all affected adjacent systems.
4. Check whether the proposal uses existing terms and procedures.
5. Check whether the outcome is playable at the table.
6. Decide whether the content belongs in proposal voice or manuscript voice.

### Special check: realism proposals

Realism is not enough.
Ask:

- does it produce better decisions
- does it deepen atmosphere without freezing play
- does it preserve campaign function
- does it force retirement, and if so, is that stated honestly

## Warning Signs

### Subsystem inflation

The proposal adds a new category, die, or track where an existing rule could carry the load.

### Silent talent invalidation

A new general rule makes a talent, spell, or item special ability feel redundant.

### False realism

The rule sounds harsher or more authentic, but only produces stalled play, bookkeeping, or GM mercy.

### Vague enforcement

The effect relies on loose phrases like "harder to act" or "reduced travel ability" without direct game hooks.

### Misleading survivability

The text presents an outcome as playable when it is functionally retirement or dependence without agency.
