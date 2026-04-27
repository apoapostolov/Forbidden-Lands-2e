# Triage Worksheet

Use this before deciding how aggressively to clean a PDF.

## Questions

1. What part of the document is broken?
2. Is the damage structural or cosmetic?
3. Does the fix depend on reading order or meaning?
4. Is the same error repeated across many pages?
5. Can a script fix it safely?
6. Do I need a visual PDF check first?

## Decision path

- if the issue is repeated page furniture, use the structural passes first
- if the issue is a flattened table, try the shared table repair first
- if the issue is hard-wrapped prose, use the wrap/unwrap helper
- if the issue is ambiguous ownership or interleaving, compare visually first

## Output

Write a short note to yourself before editing:

- what class this belongs to
- which pass or tool you will use
- what you will not touch yet
