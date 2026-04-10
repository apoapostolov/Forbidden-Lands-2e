# OCR Markdown Audit

- Raw: `temp-work/spells-and-sorcerers/Forbidden Lands-spells_and_sorcerers_eng_1_01.clean.md`

## Raw Artifact Counts

- `all_caps_lines`: 0
- `double_blank_runs`: 0
- `dropcap_damage_candidates`: 543
- `html_breaks`: 0
- `markdown_headings`: 351
- `page_number_lines`: 0
- `picture_placeholders`: 0
- `picture_text_markers`: 0
- `pipe_table_lines`: 572
- `spaced_heading_candidates`: 0

## Raw Repeated Short-Line Candidates

- None detected

## Interpretation

- High `picture_placeholders`, `picture_text_markers`, or `html_breaks` means image-text cleanup is still needed.
- High `all_caps_lines` often indicates surviving running headers or flattened labels.
- High `spaced_heading_candidates` suggests decorative heading reconstruction remains incomplete.
- High `double_blank_runs` usually indicates layout noise rather than real manuscript spacing.
- `pipe_table_lines` rising after cleanup is often good if flattened tables were reconstructed.
- Repeated short-line candidates often catch leftover running headers or footer titles that generic counts miss.
