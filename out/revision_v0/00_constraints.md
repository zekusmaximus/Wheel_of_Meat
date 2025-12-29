# Revision Constraints — Acceptance Tests

## Source: Editor Letter (December 2025)

---

## Hard Constraints (Must Pass)

### C1: Final Word Count
- **Requirement**: 110,000–130,000 words (target: 120,000)
- **Formula**: `final_total_words >= 110000 AND final_total_words <= 130000`
- **Pass threshold**: 110,000 ≤ total ≤ 130,000
- **Fail**: Any value outside range

### C2: Manchester Frame Percentage
- **Requirement**: Manchester content must be 40–50% of final manuscript
- **Formula**: `manchester_words / final_total_words >= 0.40 AND <= 0.50`
- **Pass threshold**: 40% ≤ Manchester% ≤ 50%
- **Fail**: Manchester% < 40% OR Manchester% > 50%

### C3: Net Word Cut
- **Requirement**: Net cut of 80,000–100,000 words from current manuscript
- **Formula**: `current_words - final_words >= 80000 AND <= 100000`
- **Current baseline**: 216,594 words
- **Pass threshold**: 116,594 ≤ final ≤ 136,594 (but must also satisfy C1)
- **Effective range (intersection with C1)**: 110,000–130,000
- **Fail**: Cut < 80,000 (final > 136,594) OR cut > 106,594 (final < 110,000)

### C4: Incarnation Reduction
- **Requirement**: Cut/convert 3–4 incarnation sequences OR equivalent structural removal
- **Formula**: `incarnations_removed >= 3 AND <= 4`
- **Pass threshold**: 3–4 historical incarnations cut or compressed to flashback
- **Alternative pass**: Equivalent word savings (~40,000–55,000) via other structural means

### C5: Pivotal Moment Dramatization
- **Requirement**: Dramatize ≥3 currently summarized pivotal moments
- **Formula**: `dramatized_scenes >= 3`
- **Pass threshold**: ≥3 of the following expanded to full scenes:
  1. Devaka's betrayal
  2. Lilith's first intervention
  3. Lilith's car confession
  4. Lilith's final resistance before merge
  5. Stewart's rooftop fall
- **Fail**: < 3 dramatized

### C6: Reflective Elaboration Reduction
- **Requirement**: Cut 30–40% of reflective elaboration via line-edit pass
- **Formula**: `(1 - final_elaboration_words / baseline_elaboration_words) >= 0.30 AND <= 0.40`
- **Proxy metric**: Abstraction density reduction in high-density chapters
- **Pass threshold**: Density reduced by 30–40% in top-10 abstraction chapters

### C7: Line Tic Reduction
- **Requirement**: Reduce key tics by ~50% relative density (per 10,000 words)
- **Baseline densities** (per 10k words, manuscript-wide):
  - `particular`: 110 / 216,594 × 10,000 = 5.08 per 10k
  - `something`: 1,135 / 216,594 × 10,000 = 52.41 per 10k
  - `not_x_y_pattern`: 124 / 216,594 × 10,000 = 5.72 per 10k
  - `em_dashes`: 2,883 / 216,594 × 10,000 = 133.13 per 10k
- **Target densities** (50% reduction):
  - `particular`: ≤2.54 per 10k
  - `something`: ≤26.20 per 10k
  - `not_x_y_pattern`: ≤2.86 per 10k
  - `em_dashes`: ≤66.56 per 10k
- **Pass threshold**: Each tic density at ≤50% of baseline
- **Fail**: Any tic density > 50% of baseline

---

## Computed Constraint Intersections

### Valid Final Word Count Range
Combining C1 and C3:
- C1 requires: 110,000–130,000
- C3 requires: 216,594 − 100,000 = 116,594 minimum; 216,594 − 80,000 = 136,594 maximum
- **Intersection**: 116,594–130,000 (but we use 110,000–130,000 since editor explicitly states this)

### Required Manchester Words
For final of 120,000 (target):
- 40% = 48,000 words Manchester
- 50% = 60,000 words Manchester
- **Target range**: 48,000–60,000 Manchester words

Current Manchester: 17,643 words (8.1%)
**Required Manchester expansion**: +30,357 to +42,357 words (net)

### Available Cut Budget from Incarnations
If cutting 3 incarnations at ~10,000 avg: ~30,000 words
If cutting 4 incarnations at ~10,000 avg: ~40,000 words
Plus line-edit pass: ~20,000–30,000 words (from 30–40% reflective cut)

---

## Constraint Dependency Map

```
C1 (Total) ←── affects ──→ C2 (Manchester %)
    │                          │
    ├── depends on ──→ C3 (Net Cut)
    │                          │
    └── depends on ──→ C4 (Incarnation Cuts)
                               │
                        C6 (Line Edit)
                               │
                        C7 (Tic Reduction)

C5 (Dramatization) ── independent ── affects word count minimally (+3,000–5,000)
```

---

## Verification Commands

```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Check total words
jq '.total_words' out/revision_audit/analysis_data.json

# Check Manchester words
jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json

# Compute Manchester %
# manchester_words / total_words * 100

# Check tic densities
jq '.chapters[] | {chapter, tics}' out/revision_audit/analysis_data.json
```

---

## Summary Table

| ID | Constraint | Current | Target | Status |
|----|-----------|---------|--------|--------|
| C1 | Final words | 216,594 | 110,000–130,000 | PENDING |
| C2 | Manchester % | 8.1% | 40–50% | PENDING |
| C3 | Net cut | 0 | 80,000–100,000 | PENDING |
| C4 | Incarnations cut | 0 | 3–4 | PENDING |
| C5 | Pivotal scenes | 0 | ≥3 | PENDING |
| C6 | Reflective cut | 0% | 30–40% | PENDING |
| C7 | Tic density | 100% | ≤50% | PENDING |
