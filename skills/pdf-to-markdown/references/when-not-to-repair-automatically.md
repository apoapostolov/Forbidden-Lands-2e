# When Not to Repair Automatically

This reference exists to stop agents from becoming overconfident.

OCR cleanup fails most dangerously when an agent keeps "improving" text after
its evidence runs out.

## Do Not Auto-Repair When

### 1. A Lore Term Has Multiple Plausible Expansions

Example:

- `ore`

Possible meanings:

- `Lore`
- `More`
- `Core`
- literal `ore`

If the local context does not decide it, do not pick one.

### 2. A Table Cell Would Need To Be Invented

If you know a matrix is missing a value but cannot recover that value from the
line, nearby rows, or a repeated source pattern, stop.

Do not fabricate a mechanically important cell.

### 3. A Heading Could Belong To More Than One Block

If a paragraph sits between two plausible headings due to OCR drift, do not
silently assign it unless the structure is obvious from repetition.

### 4. The Repair Would Change Mechanical Meaning

Examples:

- changing a dice range
- changing a spell rank
- changing a cost
- changing a rule condition

If the repair changes play, require stronger evidence.

### 5. The Source Is Already Better Than The Guess

If the extracted term is ugly but still usable and the correction is uncertain,
prefer the ugly truth over a polished invention.

## Preferred Alternatives

When you cannot repair automatically:

- preserve the best recovered form
- keep structure around it intact
- note the ambiguity in your report
- leave it for a later review pass

## Principle

OCR cleanup is not a contest to produce the prettiest file.

It is a discipline for producing the most trustworthy working manuscript.
