# Quality Gates and Escalation Rules

This document tells an agent when a cleanup pass is good enough to keep moving
and when it must stop and escalate.

## Quality Gate 1: Source Safety

Pass if:

- raw file preserved
- clean file written separately
- no destructive overwrite happened

Fail if:

- raw extraction replaced by cleaned text

## Quality Gate 2: Structural Recovery

Pass if:

- book title is clear
- section hierarchy is navigable
- repeated page furniture mostly removed
- chapter openings do not look like random scans

Fail if:

- headings are flatter after cleanup than before
- prose got cleaner but structure got worse

## Quality Gate 3: Data Integrity

Pass if:

- obvious rules tables are still structured
- roll ranges remain attached to outcomes
- statblocks are not merged into prose

Fail if:

- table rows were lost
- numeric ranges drifted
- spell metadata got detached from spell names

## Quality Gate 4: Prose Legibility

Pass if:

- most paragraphs read continuously
- obvious line-wrap damage is gone
- blockquotes and epigraphs look intentional

Fail if:

- fragments remain everywhere
- sentences from different columns are merged together

## Quality Gate 5: Verification

Pass if:

- lint passes, or file-local exceptions are narrow and justified
- agent can explain what was fixed and what remains risky

Fail if:

- broad lint suppression hides unresolved structural damage

## Escalate When

Escalate to manual review or a stronger pass when:

- a table requires invented cells
- many lore terms are corrupted and there is no local corroboration
- multiple headings could plausibly own the same paragraph
- the source uses complex visual layout that markdown cannot safely encode automatically

## Reporting Standard

At the end of a major cleanup pass, report:

1. what file was produced
2. what classes of damage were fixed
3. what classes were only partially fixed
4. what remains ambiguous
5. whether lint passed

That report is part of the recovery workflow, not optional polish.
