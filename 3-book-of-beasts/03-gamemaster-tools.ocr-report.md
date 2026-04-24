# OCR Markdown Audit

- Raw: `3-book-of-beasts/03-gamemaster-tools.md`
- Clean: `3-book-of-beasts/04-solo-rules.md`

## Raw Artifact Counts

- `all_caps_lines`: 0
- `double_blank_runs`: 63
- `dropcap_damage_candidates`: 17
- `html_breaks`: 0
- `markdown_headings`: 29
- `page_number_lines`: 0
- `picture_placeholders`: 0
- `picture_text_markers`: 0
- `pipe_table_lines`: 113
- `spaced_heading_candidates`: 0

## Raw Repeated Short-Line Candidates

- None detected

## Clean Artifact Counts

- `all_caps_lines`: 0
- `double_blank_runs`: 60
- `dropcap_damage_candidates`: 30
- `html_breaks`: 0
- `markdown_headings`: 68
- `page_number_lines`: 0
- `picture_placeholders`: 0
- `picture_text_markers`: 0
- `pipe_table_lines`: 15
- `spaced_heading_candidates`: 0

## Clean Repeated Short-Line Candidates

- None detected

## Delta

- `all_caps_lines`: 0 -> 0 (+0)
- `double_blank_runs`: 63 -> 60 (-3)
- `dropcap_damage_candidates`: 17 -> 30 (+13)
- `html_breaks`: 0 -> 0 (+0)
- `markdown_headings`: 29 -> 68 (+39)
- `page_number_lines`: 0 -> 0 (+0)
- `picture_placeholders`: 0 -> 0 (+0)
- `picture_text_markers`: 0 -> 0 (+0)
- `pipe_table_lines`: 113 -> 15 (-98)
- `spaced_heading_candidates`: 0 -> 0 (+0)

## Interpretation

- High `picture_placeholders`, `picture_text_markers`, or `html_breaks` means image-text cleanup is still needed.
- High `all_caps_lines` often indicates surviving running headers or flattened labels.
- High `spaced_heading_candidates` suggests decorative heading reconstruction remains incomplete.
- High `double_blank_runs` usually indicates layout noise rather than real manuscript spacing.
- `pipe_table_lines` rising after cleanup is often good if flattened tables were reconstructed.
- Repeated short-line candidates often catch leftover running headers or footer titles that generic counts miss.
