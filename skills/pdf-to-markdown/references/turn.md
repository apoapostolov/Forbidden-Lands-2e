# Agent Turn Template

Use this structure for a cleanup turn.

## Input

- source PDF or markdown
- target output file
- relevant profile or local corrections

## Process

1. audit the artifact
2. identify the damage class
3. choose the narrowest safe pass
4. run the pass
5. inspect the result
6. only then move to the next class

## Output

- cleaned markdown or updated script
- short note on what changed
- short note on what remains ambiguous

## Rule

Keep the turn small enough that the next run can start from the notes alone.
