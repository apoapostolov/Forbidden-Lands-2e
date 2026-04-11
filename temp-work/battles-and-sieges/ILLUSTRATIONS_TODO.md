# Battles & Sieges Illustration Targets

These are rules-significant illustrations to preserve during the OCR cleanup and later image extraction pass.

Default handling:

- retain transparency: `yes`
- insert position: `original`
- asset folder: `/illustrations`
- sharing scope: may be reused across chapters when the same illustration supports multiple sections

## User-Priority Illustrations

| Priority | Source Page | Subject | Purpose | Extraction Notes |
| --- | --- | --- | --- | --- |
| 1 | 4 | Troops Replacement / Troop Regrouping | Explains frontage replacement, rear-line movement, and section advantage after collapse or flight. | Preserve as a rules diagram, not decorative art. Keep labels readable. |
| 2 | 9 | Battle Preparations | Shows battle-line section layout used during deployment. | Preserve relative positioning and labels for left, center, and right sections. |
| 3 | 14 | Order of Battle | Important structural diagram for army arrangement. | User-specified page reference retained as given; likely needs visual confirmation during extraction because current PDF physical page 14 does not match this description. |

## Extraction Workflow Notes

- Do not discard these during cleanup even if OCR has already converted nearby labels into text.
- When extracted, save the files into `temp-work/battles-and-sieges/illustrations/` unless the user requests a different shared location.
- Insert image references in the manuscript at the original rule position by default.
- If a later cleanup replaces the diagram with a temporary text description, keep a nearby note so the image can be restored at the same spot.
- If a diagram contains transparent background elements, keep transparency unless the user requests a flattened export.
