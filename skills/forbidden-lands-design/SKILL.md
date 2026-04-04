---
name: forbidden-lands-design
description: Use when explaining, designing, auditing, or extending the mechanics of the Forbidden Lands 2E repo. This skill maps the rules, design space, design logic, integration points, and gameplay logic of the game so new mechanics fit the existing engine and manuscript structure.
---

# Forbidden Lands Design

Use this skill for rules analysis and design work in the Forbidden Lands 2E repo.

## Source Of Truth

Start with:

- `AGENTS.md`
- relevant files in `corebook/`
- relevant files in `proposals/`
- `skills/forbidden-lands-design/references/system-design-map.md`

If the task includes manuscript drafting, also use:

- `WRITING_GUIDE.md`

## When To Use It

Use it when you need to:

- explain how a rule actually works in play
- design a new subsystem or variant rule
- audit a proposal for deep integration
- trace how one rule touches talents, spells, gear, conditions, travel, injuries, or recovery
- convert vague ideas into mechanically coherent game text

## Bundled References

Read these on demand:

- `references/system-design-map.md`
  - the game's major loops
  - pressure economy
  - chapter-by-chapter subsystem map
  - integration questions
  - good-design tests for this repo
- `references/engine-math-and-rule-taxonomy.md`
  - system map by inputs, outputs, costs, and risks
  - rule-type catalog
  - base probability model
  - pushed-roll mathematics
  - mixed-pool findings
- `references/willpower-synergy-spells-and-recovery-analysis.md`
  - Willpower generation and spend structure
  - subsystem interaction matrix
  - talent-path pressure categories
  - spell volatility tables
  - recovery and attrition analysis
- `references/injuries-journeys-gear-and-expansion-space.md`
  - injury severity and retirement logic
  - journeys as a pressure engine
  - gear system taxonomy
  - underdeveloped design spaces
  - low-bloat expansion guidance
- `references/realism-audit-synergy-and-change-scenarios.md`
  - realism versus playability tests
  - formal proposal-audit workflow
  - synergy-risk categories
  - mathematical calibration scenarios
- `references/design-manual.md`
  - unified research-grade design manual
  - all major loops, pressure channels, math, audit rules, and expansion principles in one source

Use the reference file whenever the task is more complex than a local rules clarification.

## Design Method

For each mechanic, analyze these layers:

1. Rule loop
   - trigger
   - player decision
   - roll or resolution step
   - consequence
   - downstream state change
2. Design purpose
   - what behavior the rule encourages
   - what pressure it creates
   - what kind of story or table feeling it supports
3. Integration map
   - linked chapters
   - linked subsystems
   - terms that must stay consistent
4. Table behavior
   - player-facing complexity
   - GM burden
   - speed in live play
   - ambiguity risk

## Core Design Space To Check

When evaluating new rules, always look at:

- attributes, skills, and gear dice
- pushing and bane risk
- conditions and recovery
- resource dice and attrition
- quarter day structure and travel pressure
- initiative, action economy, and positioning
- talents and spell interactions
- injury severity, survivability, and campaign consequences
- scarcity, survival, and the cost of safety

## Output Structure

When answering a design question, prefer this order:

1. Current mechanics
2. Design logic
3. Gameplay logic
4. Integration points
5. Risks or edge cases
6. Recommended revision

## Standards For Good Design

- The rule must produce a clear table behavior, not just evocative text.
- It must use existing terms unless there is a strong reason to add a new one.
- It must create a meaningful decision or pressure point.
- It must not silently break adjacent systems.
- It must fit the game's harsh, practical survival logic.
- If it increases realism, it must still preserve playability and campaign function.

## Proposal Review Checklist

When auditing a proposal, explicitly check:

- rules completeness
- cross-chapter integration
- recoverability and permanence logic
- player agency after the rule lands
- whether catastrophic outcomes are playable, retirement-default, or dead ends
- whether the text belongs in proposal space or final manuscript space
