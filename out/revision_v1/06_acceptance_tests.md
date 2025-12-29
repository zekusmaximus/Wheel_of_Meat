# Acceptance Tests

## Prerequisites

Run the analyzer to generate fresh data:
```bash
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py
```

Verify output exists:
```bash
test -f /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json && echo "OK" || echo "FAIL"
```

---

## C1: Final Total Words

**Constraint**: 110,000 ≤ total ≤ 130,000
**Target**: 125,000

```bash
TOTAL=$(jq '.total_words' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
echo "Total words: $TOTAL"
if [ "$TOTAL" -ge 110000 ] && [ "$TOTAL" -le 130000 ]; then
  echo "C1: PASS"
else
  echo "C1: FAIL (expected 110,000-130,000)"
fi
```

---

## C2: Net Word Cut

**Constraint**: 80,000 ≤ cut ≤ 100,000
**Target**: 91,594

```bash
BASELINE=216594
TOTAL=$(jq '.total_words' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
CUT=$((BASELINE - TOTAL))
echo "Net cut: $CUT"
if [ "$CUT" -ge 80000 ] && [ "$CUT" -le 100000 ]; then
  echo "C2: PASS"
else
  echo "C2: FAIL (expected 80,000-100,000)"
fi
```

---

## C3: Incarnations Cut

**Constraint**: 3 ≤ cuts ≤ 4
**Target**: 4 (Philon, Verinus, Macarius, Kaoru)

```bash
CHAPTERS=$(jq '.chapters | length' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
CUTS=$((26 - CHAPTERS))
echo "Chapters removed: $CUTS"
if [ "$CUTS" -ge 3 ] && [ "$CUTS" -le 4 ]; then
  echo "C3: PASS"
else
  echo "C3: FAIL (expected 3-4 chapters removed)"
fi

# Verify specific cuts
echo "Checking for cut chapters..."
jq -r '.chapters[].name' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json | grep -i "philon" && echo "WARNING: Philon still present" || echo "Philon: removed"
jq -r '.chapters[].name' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json | grep -i "verinus" && echo "WARNING: Verinus still present" || echo "Verinus: removed"
jq -r '.chapters[].name' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json | grep -i "macarius" && echo "WARNING: Macarius still present" || echo "Macarius: removed"
jq -r '.chapters[].name' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json | grep -i "kaoru" && echo "WARNING: Kaoru still present" || echo "Kaoru: removed"
```

---

## C4: Final Manchester Percentage

**Constraint**: 40% ≤ Manchester% ≤ 50%
**Target**: 40.00%

```bash
TOTAL=$(jq '.total_words' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
PCT=$(echo "scale=4; $MANCH * 100 / $TOTAL" | bc)
echo "Manchester words: $MANCH"
echo "Manchester %: $PCT"
if (( $(echo "$PCT >= 40" | bc -l) )) && (( $(echo "$PCT <= 50" | bc -l) )); then
  echo "C4: PASS"
else
  echo "C4: FAIL (expected 40-50%)"
fi
```

---

## C5: Pivotal Scenes Dramatized

**Constraint**: ≥3 scenes dramatized
**Verification**: MANUAL

This constraint cannot be verified via analyzer. Manual review required.

**Checklist**:
- [ ] Devaka's betrayal scene has decision/cost/consequence structure
- [ ] Stewart rooftop fall has expanded suspended-time prose
- [ ] Lilith's first intervention shows moment of choice

---

## C6: Reflective Elaboration Reduction

**Constraint**: 30-40% reduction
**Verification**: MANUAL (proxy: abstraction density)

Abstraction density is available in analysis_data.json but reduction percentage requires baseline comparison.

```bash
echo "Top 5 abstraction densities (current):"
jq -r '.chapters | sort_by(.abstraction_density) | reverse | .[0:5] | .[] | "\(.name): \(.abstraction_density)"' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json
```

**Baseline top 5** (for comparison):
- Ch25 Space Explorer: 13.72
- Ch23 Deva Celestial: 11.01
- Ch24 Future Prophet: 9.48
- Ch13 Lilith CP06: 5.53
- Ch26 Pure Abodes Awakened: 5.06

Manual verification: Compare post-edit densities to baseline.

---

## C7: Tic Density Reduction

**Constraint**: ≤50% of baseline density per 10k words
**Baseline densities**:
- particular: 5.26 per 10k
- something: 48.52 per 10k
- not_x_y_pattern: 5.45 per 10k
- em_dashes: 133.13 per 10k

**Target densities** (50%):
- particular: ≤2.63 per 10k
- something: ≤24.26 per 10k
- not_x_y_pattern: ≤2.73 per 10k
- em_dashes: ≤66.57 per 10k

```bash
python3 << 'EOF'
import json

with open('/home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json') as f:
    data = json.load(f)

total = data['total_words']
tics = {'particular': 0, 'something': 0, 'not_x_y_pattern': 0, 'em_dashes': 0}

for ch in data['chapters']:
    for tic in tics:
        tics[tic] += ch['tics'].get(tic, 0)

baselines = {
    'particular': 5.26,
    'something': 48.52,
    'not_x_y_pattern': 5.45,
    'em_dashes': 133.13
}

print(f"Total words: {total}")
print()
print("Tic Densities (per 10k words):")
all_pass = True
for tic in tics:
    density = tics[tic] / total * 10000
    target = baselines[tic] * 0.5
    status = 'PASS' if density <= target else 'FAIL'
    if status == 'FAIL':
        all_pass = False
    print(f"  {tic}: {density:.2f} (target ≤{target:.2f}) {status}")

print()
if all_pass:
    print("C7: PASS")
else:
    print("C7: FAIL")
EOF
```

---

## Words by Type

Verify composition matches target:

```bash
echo "Words by type:"
jq -r '
  .chapters | group_by(.type) |
  map({type: .[0].type, words: (map(.word_count) | add)}) |
  sort_by(.words) | reverse |
  .[] | "\(.type): \(.words)"
' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json
```

**Target composition**:
- Manchester: 50,000 (40.00%)
- Historical: 40,000 (32.00%)
- Lilith: 15,000 (12.00%)
- Final sequence (Metaphysical + Climax + Historical/Future + Historical/Metaphysical): 20,000 (16.00%)

---

## Chapter Count

Verify 22 chapters remain:

```bash
COUNT=$(jq '.chapters | length' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
echo "Chapter count: $COUNT"
if [ "$COUNT" -eq 22 ]; then
  echo "Chapter count: PASS"
else
  echo "Chapter count: FAIL (expected 22)"
fi
```

---

## Full Constraint Summary

Run all tests:

```bash
#!/bin/bash
echo "=== REVISION ACCEPTANCE TESTS ==="
echo

# Re-run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py > /dev/null 2>&1

BASELINE=216594
TOTAL=$(jq '.total_words' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
CHAPTERS=$(jq '.chapters | length' /home/user/Wheel_of_Meat/out/revision_audit/analysis_data.json)
CUT=$((BASELINE - TOTAL))
CUTS=$((26 - CHAPTERS))
PCT=$(echo "scale=2; $MANCH * 100 / $TOTAL" | bc)

echo "C1 Total words: $TOTAL (target: 110,000-130,000)"
echo "C2 Net cut: $CUT (target: 80,000-100,000)"
echo "C3 Incarnations cut: $CUTS (target: 3-4)"
echo "C4 Manchester %: $PCT% (target: 40-50%)"
echo "C5 Pivotal scenes: MANUAL"
echo "C6 Reflective reduction: MANUAL"
echo "C7 Tic density: (run Python script above)"
echo

# Pass/fail
PASS=0
FAIL=0

[ "$TOTAL" -ge 110000 ] && [ "$TOTAL" -le 130000 ] && { echo "C1: PASS"; ((PASS++)); } || { echo "C1: FAIL"; ((FAIL++)); }
[ "$CUT" -ge 80000 ] && [ "$CUT" -le 100000 ] && { echo "C2: PASS"; ((PASS++)); } || { echo "C2: FAIL"; ((FAIL++)); }
[ "$CUTS" -ge 3 ] && [ "$CUTS" -le 4 ] && { echo "C3: PASS"; ((PASS++)); } || { echo "C3: FAIL"; ((FAIL++)); }
(( $(echo "$PCT >= 40" | bc -l) )) && (( $(echo "$PCT <= 50" | bc -l) )) && { echo "C4: PASS"; ((PASS++)); } || { echo "C4: FAIL"; ((FAIL++)); }

echo
echo "Automated tests: $PASS PASS, $FAIL FAIL"
echo "Manual tests remaining: C5, C6, C7"
```
