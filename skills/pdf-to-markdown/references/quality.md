# Quality Gates

Run these checks before calling the cleanup done.

## Minimum gates

- raw source preserved
- clean output written separately
- headings read in a sensible hierarchy
- page furniture removed
- tables remain structured
- no accidental prose invention
- markdown lint passes when the file stays in the repo

## Spot-check order

1. opening pages
2. one middle spread
3. one late section
4. any dense table section
5. any interleaved two-column section

## Escalate when

- a table is still logically unclear
- a block seems owned by the wrong heading
- the page layout contradicts the extracted order
- a repair would require guessing content

## Done standard

A cleanup run is done only when the file is readable, the structure is stable, and the remaining ambiguity is explicitly named.
