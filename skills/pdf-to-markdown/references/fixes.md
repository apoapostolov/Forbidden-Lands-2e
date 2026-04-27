# High-Confidence Fixes

This list is for corrections that are usually safe in OCR work.

## Generic repairs

- opening letters lost by a drop cap
- obvious paragraph continuations
- repeated page furniture
- simple list compacting
- obvious `<br>` removal inside table cells

## Title repairs

- split or collapsed heading words
- missing apostrophes inside confirmed title text
- repeated uppercase header strings

## Table repairs

- split a flattened one-line table into rows
- rebuild a dirty pipe table
- separate a table from a paragraph when the row structure is still clear

## Use rule

Only apply a fix automatically when:

- the corrupted form is obvious
- the surrounding context matches
- the correction does not change meaning

If any of those fail, preserve the damaged text and flag it.
