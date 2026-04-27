# Bundled tests for `pdf-to-markdown`

These tests travel with the skill bundle.

## Run the bundled suite

```bash
python -m unittest discover -s skills/pdf-to-markdown/scripts/tests
```

## What belongs here

- parser and CLI smoke checks for the bundled scripts
- regression tests for table repair, pass selection, and reflow behavior
- skill-doc checks that keep the bundled instructions honest
- narrow tests that lock down a bug fix or a reusable transformation

## What does not belong here

- module-system experiments that are not bundled with the skill
- repository-wide tests that rely on shared repo-only helpers
- book-specific OCR notes or ad hoc investigation logs

If a test needs a helper that is not part of the bundled skill scripts, it does not belong here.
