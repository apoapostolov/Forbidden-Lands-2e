# Repair Playbook

Repair artifact classes, not random lines.

## Phase order

### 1. Stabilize the container

Fix:

- document title
- front matter
- repeated page furniture
- obvious extraction noise

### 2. Rebuild navigation

Fix:

- chapter headings
- section headings
- heading levels
- duplicated heading fragments

### 3. Rebuild data

Fix:

- tables
- statblocks
- roll tables
- matrix sections

### 4. Rebuild prose

Fix:

- paragraph joins
- mid-sentence wraps
- obvious OCR word breaks
- drop-cap damage

### 5. Normalize and verify

Fix:

- whitespace
- `<br>` leftovers
- list spacing
- blockquote consistency

## High-confidence repairs

Usually safe:

- removing repeated page numbers
- removing repeated running headers
- converting obvious picture placeholders to nothing
- replacing `<br>` in table cells with spaces
- joining a line that clearly continues the same sentence

## Medium-confidence repairs

Need nearby context:

- reconstructing spaced headings
- rebuilding flattened tables
- moving a line under a different heading
- deciding whether a short italic block is a sidebar or flavor quote

## Low-confidence repairs

Escalate or preserve cautiously:

- restoring corrupted names from memory
- reconstructing missing table cells with no nearby support
- rewriting ambiguous rules language
- inventing headings not supported by repeated patterns

## Rule of restraint

If the source is ambiguous, keep the best recovered version and note the ambiguity.
