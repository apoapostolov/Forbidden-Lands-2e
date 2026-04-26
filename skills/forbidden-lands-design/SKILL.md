---
name: forbidden-lands-design
description: Use when explaining, designing, auditing, or extending the mechanics of the Forbidden Lands 2E repo. This skill maps the rules, design space, design logic, integration points, and gameplay logic of the game so new mechanics fit the existing engine and manuscript structure.
---

# Forbidden Lands Design

Use this skill for rules analysis and design work in the Forbidden Lands 2E repo.

## Source Of Truth

Start with:

- `/home/apoapostolov/git-public/Forbidden-Lands-2e/AGENTS.md`
- relevant files in `/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/`
- relevant files in `/home/apoapostolov/git-public/Forbidden-Lands-2e/proposals/`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/skills/forbidden-lands-design/references/system-design-map.md`

If the task includes manuscript drafting, also use:

- `/home/apoapostolov/git-public/Forbidden-Lands-2e/WRITING_GUIDE.md`

## When To Use It

Use it when you need to:

- explain how a rule actually works in play
- design a new subsystem or variant rule
- audit a proposal for deep integration
- trace how one rule touches talents, spells, gear, conditions, travel, injuries, or recovery
- convert vague ideas into mechanically coherent game text

## Bundled References

Read this repo-bundled reference on demand:

- `/home/apoapostolov/git-public/Forbidden-Lands-2e/skills/forbidden-lands-design/references/system-design-map.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/skills/forbidden-lands-design/references/engine-math-and-rule-taxonomy.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/skills/forbidden-lands-design/references/willpower-synergy-spells-and-recovery-analysis.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/skills/forbidden-lands-design/references/injuries-journeys-gear-and-expansion-space.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/skills/forbidden-lands-design/references/realism-audit-synergy-and-change-scenarios.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/skills/forbidden-lands-design/references/design-manual.md`

Use it whenever the task is more complex than a local rules clarification.

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
