# Scripts Directory — Forbidden Lands 2E

Simulation, testing, and analysis tools for the core manuscript and proposals.

## Economic Systems Analysis

### Traderoads Subsystem (Chapters 8 & 10)

**Status:** ✓ VIABLE, BALANCED, READY FOR INTEGRATION

See [TRADEROADS_VIABILITY_REPORT.md](TRADEROADS_VIABILITY_REPORT.md) for:

- 1-year simulation results on 30×30 hex map with 20 settlements
- Sensitivity analysis across different starting capitals (250–2000 silver)
- Seasonal profitability breakdown (Spring +370, Summer +109, Autumn +178, Winter -35)
- Game balance assessment and integration recommendations

**Scripts:**

- `traderoads_simulation.py` — Core 1-year trading simulation (124% ROI achieved)
- `traderoads_sensitivity.py` — Tests 4 different starting capital amounts
- `traderoads_analysis.py` — Detailed contextual analysis

**Key finding:** Caravan trading is economically competitive with adventure work, produces 37–342% annual ROI depending on capital, and provides meaningful seasonal gameplay.

---

### Mercenary Economy (Chapter 12)

**Status:** ✓ INTEGRATED & BALANCED

See `proposals_applied/` for band economy models and mercenary balancing work.

**Scripts:**

- `band_economy_sim.py` — Band pay/retainer/share economics

---

## Manuscript & Content Tools

### PDF/Markdown Processing

- `pdf_to_markdown.py` — Extract text from PDF source
- `ocr_markdown_audit.py` — Quality check on OCR'd markdown
- `repair_flattened_tables.py` — Fix table formatting issues

### Content Generation

- `build_mercenaries.py` — Generate mercenary chapter content
- `split_mercenaries.py` — Split mercenary content into sections
- `split_markdown_sections.py` — Refactor markdown structure

### Analysis

- `analyze_corebook.py` — Scan manuscript for consistency issues
- `lifepath_simulation.py` — Test life path generator mechanics

---

## Quick Start

### To test Traderoads economics:

```bash
python traderoads_simulation.py
python traderoads_sensitivity.py
```

### To analyze manuscript:

```bash
python analyze_corebook.py
python ocr_markdown_audit.py
```

---

## Notes for Contributors

1. **Simulation conventions:**
   - All monetary values in silver (per Chapter 10 economy)
   - Hex distance measured in travel days
   - Seasonal modifiers: Spring +0%, Summer -10%, Autumn +5%, Winter +50%

2. **Economic benchmarks** (from Chapter 12 mercenary contracts):
   - Soldier pay: 10–50 silver/month
   - Escort contracts: 10–50 silver per job
   - Clearing contracts: 50–100 silver per job
   - Caravan profit target: 40+ silver per route to be competitive

3. **File encoding:**
   - All scripts UTF-8
   - Markdown files UTF-8 with CRLF line endings (Windows convention)

---

Last updated: April 11, 2026
