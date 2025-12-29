# Acceptance Tests — Revision Validation Checklist

## Quick Reference

This document provides executable verification commands for all revision constraints. Run at any gate to verify progress.

---

## Test Suite

### Pre-requisite: Run Analyzer

```bash
cd /home/user/Wheel_of_Meat

# Run the manuscript analyzer to update analysis_data.json
python3 tools/revision_audit/manuscript_analyzer.py

# Verify output file exists
ls -la out/revision_audit/analysis_data.json
```

---

## Constraint C1: Final Word Count

**Requirement**: 110,000–130,000 words (target: 120,000)

### Test Command

```bash
# Get total word count
jq '.total_words' out/revision_audit/analysis_data.json
```

### Expected Output

| Phase | Expected Range | Notes |
|-------|---------------|-------|
| Baseline | 216,594 | Starting point |
| After G2 | 130,000–145,000 | Post structural cuts |
| After G3 | 120,000–128,000 | Post Manchester build |
| After G5 | 123,000–125,000 | Post meta compression |
| After G6 | 120,000–124,000 | Final |

### PASS/FAIL Criteria

```bash
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
if [ $TOTAL -ge 110000 ] && [ $TOTAL -le 130000 ]; then
  echo "C1: PASS ($TOTAL words)"
else
  echo "C1: FAIL ($TOTAL words - outside 110,000-130,000)"
fi
```

---

## Constraint C2: Manchester Percentage

**Requirement**: 40–50% of final manuscript

### Test Command

```bash
# Get Manchester word count
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)

# Get total word count
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)

# Calculate percentage
echo "Manchester: $MANCH words"
echo "Total: $TOTAL words"
echo "Percentage: $(echo "scale=2; $MANCH * 100 / $TOTAL" | bc)%"
```

### Expected Output

| Phase | Manchester Words | Manchester % |
|-------|-----------------|--------------|
| Baseline | 17,643 | 8.15% |
| After G3 | 48,000–52,000 | 40–43% |
| Final | 48,000–52,000 | 40–42% |

### PASS/FAIL Criteria

```bash
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
PCT=$(echo "scale=4; $MANCH / $TOTAL" | bc)

if (( $(echo "$PCT >= 0.40" | bc -l) )) && (( $(echo "$PCT <= 0.50" | bc -l) )); then
  echo "C2: PASS (Manchester $(echo "scale=2; $PCT * 100" | bc)%)"
else
  echo "C2: FAIL (Manchester $(echo "scale=2; $PCT * 100" | bc)% - outside 40-50%)"
fi
```

---

## Constraint C3: Net Word Cut

**Requirement**: 80,000–100,000 words cut from baseline

### Test Command

```bash
BASELINE=216594
CURRENT=$(jq '.total_words' out/revision_audit/analysis_data.json)
CUT=$((BASELINE - CURRENT))

echo "Baseline: $BASELINE"
echo "Current: $CURRENT"
echo "Net cut: $CUT"
```

### Expected Output

| Phase | Current | Net Cut |
|-------|---------|---------|
| After G2 | 130,000–145,000 | 71,594–86,594 |
| After G5 | 123,000–125,000 | 91,594–93,594 |
| Final | 120,000–124,000 | 92,594–96,594 |

### PASS/FAIL Criteria

```bash
BASELINE=216594
CURRENT=$(jq '.total_words' out/revision_audit/analysis_data.json)
CUT=$((BASELINE - CURRENT))

if [ $CUT -ge 80000 ] && [ $CUT -le 100000 ]; then
  echo "C3: PASS (net cut $CUT words)"
else
  echo "C3: FAIL (net cut $CUT - outside 80,000-100,000)"
fi
```

---

## Constraint C4: Incarnation Cuts

**Requirement**: 3–4 incarnations cut

### Test Command

```bash
# Count chapters
CHAPTERS=$(jq '.chapters | length' out/revision_audit/analysis_data.json)
echo "Chapter count: $CHAPTERS"

# Verify cut chapters are absent
echo "Checking for cut chapters (should return nothing):"
jq '.chapters[] | select(.name | test("Philon|Verinus|Macarius|Kaoru"; "i")) | .name' out/revision_audit/analysis_data.json
```

### Expected Output

| Phase | Chapter Count | Cut Chapters Present |
|-------|---------------|---------------------|
| Baseline | 26 | Yes (4) |
| After G2 | 22 | No |
| Final | 22 | No |

### PASS/FAIL Criteria

```bash
CHAPTERS=$(jq '.chapters | length' out/revision_audit/analysis_data.json)
CUT_PRESENT=$(jq '.chapters[] | select(.name | test("Philon|Verinus|Macarius|Kaoru"; "i")) | .name' out/revision_audit/analysis_data.json | wc -l)
INCARNATIONS_CUT=$((26 - CHAPTERS))

if [ $INCARNATIONS_CUT -ge 3 ] && [ $INCARNATIONS_CUT -le 4 ] && [ $CUT_PRESENT -eq 0 ]; then
  echo "C4: PASS ($INCARNATIONS_CUT incarnations cut)"
else
  echo "C4: FAIL (incarnations cut: $INCARNATIONS_CUT, cut chapters still present: $CUT_PRESENT)"
fi
```

---

## Constraint C5: Pivotal Scene Dramatization

**Requirement**: ≥3 pivotal moments dramatized

### Test Command

```bash
# Search for dramatization markers (manual verification)
echo "Checking for Devaka betrayal scene:"
grep -c "Devaka.*spoke\|Devaka.*handed\|Devaka.*delivered" WOM_Manuscript_full.md || echo "0"

echo "Checking for Stewart rooftop expansion:"
grep -c "suspended.*time\|gravity.*taking\|time.*dilating" WOM_Manuscript_full.md || echo "0"

echo "Checking for Lilith first intervention:"
grep -c "first.*intervention\|observation.*manipulation\|participant.*witness" WOM_Manuscript_full.md || echo "0"
```

### Verification Checklist

- [ ] Devaka betrayal scene present (show him speaking to conspirators)
- [ ] Stewart rooftop fall expanded (suspended time prose)
- [ ] Lilith first intervention dramatized (moment of choice visible)
- [ ] Optional: Lilith car confession expanded
- [ ] Optional: Lilith final resistance dialogue added

### PASS/FAIL Criteria

```
Manual review required.
PASS: ≥3 scenes verified with decision/cost/consequence structure
FAIL: <3 scenes verified
```

---

## Constraint C6: Reflective Elaboration Reduction

**Requirement**: 30–40% cut from reflective content

### Test Command

```bash
# Calculate average abstraction density
BASELINE_AVG=0.76  # calculated from initial analysis

CURRENT_AVG=$(jq '[.chapters[] | .abstraction_density] | add / length' out/revision_audit/analysis_data.json)

echo "Baseline average abstraction: $BASELINE_AVG"
echo "Current average abstraction: $CURRENT_AVG"
```

### Proxy Verification

Since direct measurement of "reflective elaboration" is complex, use abstraction density as proxy:

```bash
# Check top abstraction chapters show reduction
echo "Top 5 abstraction chapters:"
jq -r '.chapters | sort_by(-.abstraction_density) | .[0:5] | .[] | "\(.chapter) \(.name): \(.abstraction_density)"' out/revision_audit/analysis_data.json
```

### Expected Output

| Chapter | Baseline Density | Target Density |
|---------|-----------------|----------------|
| Ch 25 (Formless) | 13.72 | ≤9.60 |
| Ch 23 (Deva) | 11.01 | ≤7.71 |
| Ch 24 (Future) | 9.48 | ≤6.64 |
| Ch 26 (Climax) | 5.06 | ≤3.54 |

### PASS/FAIL Criteria

```
Manual review of abstraction density reductions.
PASS: Average density reduced by 30-40% in top-10 chapters
FAIL: Reduction <30% or >40%
```

---

## Constraint C7: Line Tic Reduction

**Requirement**: ≤50% density for key tics (per 10,000 words)

### Test Command

```bash
# Calculate tic totals and densities
python3 -c "
import json
with open('out/revision_audit/analysis_data.json') as f:
    data = json.load(f)

total = data['total_words']
tics = {'particular': 0, 'something': 0, 'not_x_y_pattern': 0, 'em_dashes': 0}

for ch in data['chapters']:
    for tic, count in ch['tics'].items():
        tics[tic] += count

baselines = {'particular': 5.26, 'something': 48.52, 'not_x_y_pattern': 5.45, 'em_dashes': 133.15}
targets = {k: v * 0.5 for k, v in baselines.items()}

print('Tic Density Report (per 10k words):')
print(f\"{'Tic':<20} {'Baseline':>10} {'Target':>10} {'Current':>10} {'Status':>10}\")
print('-' * 60)

for tic in tics:
    density = tics[tic] / total * 10000
    status = 'PASS' if density <= targets[tic] else 'FAIL'
    print(f\"{tic:<20} {baselines[tic]:>10.2f} {targets[tic]:>10.2f} {density:>10.2f} {status:>10}\")
"
```

### Expected Output

| Tic | Baseline | Target (50%) | Status |
|-----|----------|--------------|--------|
| particular | 5.26 | ≤2.63 | — |
| something | 48.52 | ≤24.26 | — |
| not_x_y_pattern | 5.45 | ≤2.73 | — |
| em_dashes | 133.15 | ≤66.58 | — |

### PASS/FAIL Criteria

```bash
# All tics must be at ≤50% of baseline density
# PASS: All 4 tics at or below target
# FAIL: Any tic above target
```

---

## Full Constraint Summary Test

### Run All Tests

```bash
#!/bin/bash
cd /home/user/Wheel_of_Meat

echo "=== REVISION ACCEPTANCE TEST SUITE ==="
echo ""

# Run analyzer first
python3 tools/revision_audit/manuscript_analyzer.py > /dev/null 2>&1

# C1: Total Words
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
if [ $TOTAL -ge 110000 ] && [ $TOTAL -le 130000 ]; then
  echo "C1 Total Words: PASS ($TOTAL)"
else
  echo "C1 Total Words: FAIL ($TOTAL)"
fi

# C2: Manchester %
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)
PCT=$(echo "scale=4; $MANCH * 100 / $TOTAL" | bc)
if (( $(echo "$PCT >= 40" | bc -l) )) && (( $(echo "$PCT <= 50" | bc -l) )); then
  echo "C2 Manchester %: PASS ($PCT%)"
else
  echo "C2 Manchester %: FAIL ($PCT%)"
fi

# C3: Net Cut
BASELINE=216594
CUT=$((BASELINE - TOTAL))
if [ $CUT -ge 80000 ] && [ $CUT -le 100000 ]; then
  echo "C3 Net Cut: PASS ($CUT)"
else
  echo "C3 Net Cut: FAIL ($CUT)"
fi

# C4: Incarnations
CHAPTERS=$(jq '.chapters | length' out/revision_audit/analysis_data.json)
INCARNATIONS_CUT=$((26 - CHAPTERS))
if [ $INCARNATIONS_CUT -ge 3 ] && [ $INCARNATIONS_CUT -le 4 ]; then
  echo "C4 Incarnations Cut: PASS ($INCARNATIONS_CUT)"
else
  echo "C4 Incarnations Cut: FAIL ($INCARNATIONS_CUT)"
fi

# C5-C7: Manual verification required
echo "C5 Pivotal Scenes: PENDING (manual review)"
echo "C6 Reflective Reduction: PENDING (manual review)"
echo "C7 Tic Reduction: PENDING (run tic density check)"

echo ""
echo "=== END TEST SUITE ==="
```

---

## Gate-Specific Tests

### G1 (End Week 2)

```bash
# Structure approval
test -f out/revision_v0/03_structure_candidates.md && echo "G1-1: PASS" || echo "G1-1: FAIL"
```

### G2 (End Week 6)

```bash
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
CHAPTERS=$(jq '.chapters | length' out/revision_audit/analysis_data.json)

if [ $TOTAL -ge 130000 ] && [ $TOTAL -le 145000 ] && [ $CHAPTERS -eq 22 ]; then
  echo "G2: PASS"
else
  echo "G2: FAIL (total: $TOTAL, chapters: $CHAPTERS)"
fi
```

### G3 (End Week 10)

```bash
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)
PCT=$(echo "scale=2; $MANCH * 100 / $TOTAL" | bc)

if [ $TOTAL -ge 120000 ] && [ $TOTAL -le 128000 ] && [ $MANCH -ge 48000 ]; then
  echo "G3: PASS (total: $TOTAL, Manchester: $MANCH = $PCT%)"
else
  echo "G3: FAIL"
fi
```

### G4 (End Week 14)

```bash
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
LILITH=$(jq '[.chapters[] | select(.type == "Lilith") | .word_count] | add' out/revision_audit/analysis_data.json)

if [ $TOTAL -ge 122000 ] && [ $TOTAL -le 126000 ] && [ $LILITH -ge 14000 ] && [ $LILITH -le 18000 ]; then
  echo "G4: PASS (total: $TOTAL, Lilith: $LILITH)"
else
  echo "G4: FAIL"
fi
```

### G5 (End Week 16)

```bash
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)
PCT=$(echo "scale=4; $MANCH / $TOTAL" | bc)

if [ $TOTAL -ge 123000 ] && [ $TOTAL -le 125000 ] && (( $(echo "$PCT >= 0.40" | bc -l) )); then
  echo "G5: PASS (total: $TOTAL, Manchester%: $(echo "scale=2; $PCT * 100" | bc)%)"
else
  echo "G5: FAIL"
fi
```

### G6 (End Week 18) — FINAL

Run full constraint summary test above.

---

## Usage Notes

1. **Run tests after each major edit session**
2. **Commit analysis_data.json** alongside manuscript changes
3. **Track trends** — word counts should move toward targets monotonically
4. **Manual verification** required for C5 (scenes), C6 (reflective), C7 (tics before final pass)
5. **Gate failures** require remediation before proceeding to next phase
