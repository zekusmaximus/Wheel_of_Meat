# Execution Schedule — 18-Week Revision Plan

## Overview

| Phase | Weeks | Focus | Gate |
|-------|-------|-------|------|
| I | 1-2 | Structural Decisions | G1 |
| II | 3-6 | Structural Cuts | G2 |
| III | 7-10 | Manchester Build | G3 |
| IV | 11-14 | Continuity & Dramatization | G4 |
| V | 15-16 | Meta/Climax Compression | G5 |
| VI | 17-18 | Line Edit | G6 |

---

## Phase I: Structural Decisions (Weeks 1-2)

### Week 1: Confirmation and Setup

**Tasks**:
- [ ] Review and approve final structure (Budget C)
- [ ] Create chapter-by-chapter cut/keep list
- [ ] Identify specific passages in cut chapters to preserve as Lilith tracking fragments
- [ ] Draft chapter resequencing plan
- [ ] Set up version control branches for revision

**Deliverables**:
- Approved structure document
- Preservation list (key quotes/images from cut chapters)
- Git branch: `revision/v1-structure`

### Week 2: Cut Preparation

**Tasks**:
- [ ] Read cut chapters (6, 8, 10, 12) for preservation candidates
- [ ] Identify thematic threads that must be maintained
- [ ] Draft tracking fragment templates for Lilith CP03-06
- [ ] Plan continuity bridges between kept chapters
- [ ] Document any plot dependencies on cut material

**Deliverables**:
- Preservation quotes document
- Tracking fragment outlines (4 fragments, ~2,000 words total)
- Continuity bridge notes

### Gate G1: Structural Approval

**Date**: End of Week 2

**Acceptance test**:
```bash
# Verify structure document exists and is complete
ls out/revision_v0/03_structure_candidates.md

# Verify preservation list
ls out/revision_v1/preservation_list.md

# Verify tracking fragment outlines
ls out/revision_v1/lilith_fragments/*.md
```

**Pass criteria**:
- Structure document approved (signed off)
- All 4 cut chapters reviewed
- Tracking fragment outlines complete
- No blocking continuity issues identified

---

## Phase II: Structural Cuts (Weeks 3-6)

### Week 3: Execute Incarnation Cuts

**Tasks**:
- [ ] Remove Chapter 6 (Philon) from manuscript
- [ ] Remove Chapter 8 (Verinus) from manuscript
- [ ] Remove Chapter 10 (Macarius) from manuscript
- [ ] Remove Chapter 12 (Kaoru) from manuscript
- [ ] Renumber remaining chapters

**Deliverables**:
- Manuscript with 4 chapters removed
- New chapter sequence (22 chapters)
- Backup of original

### Week 4: Write Lilith Tracking Fragments

**Tasks**:
- [ ] Write Lilith CP03 fragment (450 words, references Philon)
- [ ] Write Lilith CP04 fragment (650 words, references Verinus)
- [ ] Write Lilith CP05 fragment (650 words, references Macarius)
- [ ] Write Lilith CP06 fragment (450 words, references Kaoru)
- [ ] Insert fragments into manuscript sequence

**Deliverables**:
- 4 tracking fragments (~2,200 words total)
- Fragments integrated into chapter sequence

### Week 5: Historical Chapter Compression (Part 1)

**Tasks**:
- [ ] Compress Chapter 4 (Chandra): 19,676 → 11,000 words
  - Focus cuts on internal rumination
  - Preserve key plot beats
  - ADD Devaka betrayal scene (+1,500)
- [ ] Compress Chapter 14 (Diego): 18,641 → 10,000 words
  - Maintain horror without exploitation
  - Reduce torture repetition
  - Preserve final dignity

**Deliverables**:
- Chandra chapter at ~11,000 words (net -8,676)
- Diego chapter at ~10,000 words (net -8,641)

### Week 6: Historical Chapter Compression (Part 2)

**Tasks**:
- [ ] Compress Chapter 16 (Renaissance): 13,725 → 5,500 words
- [ ] Compress Chapter 18 (Taiping): 6,512 → 4,000 words
- [ ] Compress Chapter 20 (Malone): 11,144 → 4,200 words
- [ ] Light trim of Chapter 2 (Ka): 5,058 → 4,200 words

**Deliverables**:
- Renaissance at 5,500 words (net -8,225)
- Taiping at 4,000 words (net -2,512)
- Malone at 4,200 words (net -6,944)
- Ka at 4,200 words (net -858)

### Gate G2: Structural Cuts Complete

**Date**: End of Week 6

**DERIVED word count (computed from operations, NOT guessed):**

```
Starting baseline:                              216,594

Week 3 operations (incarnation cuts):
  Remove Ch6 Philon:                            -10,202
  Remove Ch8 Verinus:                            -9,405
  Remove Ch10 Macarius:                         -13,777
  Remove Ch12 Kaoru:                             -8,460
  Subtotal after week 3:                        174,750

Week 4 operations (tracking fragments):
  Add Lilith CP03 fragment (450 words):            +450
  Add Lilith CP04 fragment (650 words):            +650
  Add Lilith CP05 fragment (650 words):            +650
  Add Lilith CP06 fragment (450 words):            +450
  Subtotal after week 4:                        176,950

Week 5 operations (Chandra + Diego compression):
  Compress Ch4 Chandra: 19,676→11,000           -8,676
  ADD Devaka betrayal scene:                    +1,500
  Compress Ch14 Diego: 18,641→10,000            -8,641
  Subtotal after week 5:                        161,133

Week 6 operations (remaining historical compression):
  Compress Ch16 Renaissance: 13,725→5,500       -8,225
  Compress Ch18 Taiping: 6,512→4,000            -2,512
  Compress Ch20 Malone: 11,144→4,200            -6,944
  Compress Ch2 Ka: 5,058→4,200                    -858
  Subtotal after week 6:                        142,594
────────────────────────────────────────────────────
G2 EXPECTED TOTAL:                              142,594
```

**Acceptance test**:
```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify word count matches derived value
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
if [ $TOTAL -ge 140000 ] && [ $TOTAL -le 145000 ]; then
  echo "G2 word count: PASS ($TOTAL, expected ~142,594)"
else
  echo "G2 word count: FAIL ($TOTAL, expected ~142,594)"
fi

# Verify incarnations removed
CHAPTERS=$(jq '.chapters | length' out/revision_audit/analysis_data.json)
echo "Chapter count: $CHAPTERS (expected: 22)"

# Verify no Philon, Verinus, Macarius, Kaoru chapters
jq '.chapters[] | select(.name | test("Philon|Verinus|Macarius|Kaoru"; "i"))' out/revision_audit/analysis_data.json
# Expected: no output
```

**Pass criteria**:
- Total words: 140,000–145,000 (derived center: 142,594)
- Chapter count: 22
- No cut chapters present
- Lilith fragments integrated
- Devaka betrayal scene added

---

## Phase III: Manchester Build (Weeks 7-10)

### Week 7: Manchester Chapter 1 Expansion (Part 1)

**Tasks**:
- [ ] Draft Silas-Lilith dinner scene (+2,500 words)
- [ ] Draft wine/flat intimacy scene (+2,500 words)
- [ ] Establish Silas's pre-awakening psychology
- [ ] Integrate early flashback suppressions

**Deliverables**:
- Two new Manchester scenes (~5,000 words)
- Silas character work visible

### Week 8: Manchester Chapter 1 Expansion (Part 2)

**Tasks**:
- [ ] Draft Stewart as Silas's advisee scenes (+3,000 words)
- [ ] Draft Silas's "ordinary life" desires (+2,000 words)
- [ ] University setting details and sensory grounding (+1,000 words)
- [ ] Integrate new material into chapter flow

**Deliverables**:
- Stewart mentorship established
- Silas interiority developed
- Chapter 1 at target ~25,000 words

### Week 9: Manchester Chapter 22 Expansion (Part 1)

**Tasks**:
- [ ] Draft Stewart resolution/aftermath scenes (+3,500 words)
- [ ] Expand Stewart rooftop fall (+800 words)
- [ ] Add suspended-time prose
- [ ] Ground the mystical in physical sensation

**Deliverables**:
- Stewart thread resolved
- Rooftop scene expanded
- ~4,300 words added

### Week 10: Manchester Chapter 22 Expansion (Part 2)

**Tasks**:
- [ ] Expand Lilith car confession scene (+2,000 words)
- [ ] Add Silas's genuine anguish before release
- [ ] Draft Lilith final resistance dialogue (+1,500 words)
- [ ] Ground awakening sequence in Manchester (+2,000 words)

**Deliverables**:
- Confession scene deepened
- Silas emotional arc complete
- Chapter 22 at target ~25,000 words

### Gate G3: Manchester Build Complete

**Date**: End of Week 10

**DERIVED word count (computed from G2 + operations):**

```
Starting from G2 total:                         142,594

Week 7-8 operations (Ch1 Manchester expansion):
  Current Ch1: 7,895
  Target Ch1: 25,000
  Net change:                                   +17,105
  Subtotal after week 8:                       159,699

Week 9-10 operations (Ch22 Manchester expansion):
  Current Ch22: 9,748
  Target Ch22: 25,000
  Net change:                                   +15,252
  Subtotal after week 10:                      174,951
────────────────────────────────────────────────────
G3 EXPECTED TOTAL:                              174,951

Manchester composition:
  Ch1: 25,000
  Ch22: 25,000
  Manchester total: 50,000

Manchester %: 50,000 / 174,951 = 28.58%
```

**ISSUE IDENTIFIED**: At this point, Manchester is only 28.58%, NOT 40-43% as claimed in previous version. This is because we haven't done Lilith/Final compression yet. The schedule order must be revised OR the gate expectation must reflect reality.

**REVISED expectation for G3**:
```
Total: ~174,951 words
Manchester: 50,000 words (28.58%)
Note: Manchester % will reach 40-50% only AFTER Phase V compression
```

**Acceptance test**:
```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify total
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
if [ $TOTAL -ge 172000 ] && [ $TOTAL -le 178000 ]; then
  echo "G3 word count: PASS ($TOTAL, expected ~174,951)"
else
  echo "G3 word count: FAIL ($TOTAL, expected ~174,951)"
fi

# Verify Manchester words
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)
if [ $MANCH -ge 48000 ] && [ $MANCH -le 52000 ]; then
  echo "G3 Manchester: PASS ($MANCH words)"
else
  echo "G3 Manchester: FAIL ($MANCH words, expected 50,000)"
fi
```

**Pass criteria**:
- Total words: 172,000–178,000 (derived center: 174,951)
- Manchester words: 48,000–52,000 (target: 50,000)
- Manchester %: ~28.6% (will reach 40-50% after final compression)
- Stewart thread expanded
- Silas-Lilith relationship dramatized

---

## Phase IV: Continuity & Dramatization (Weeks 11-14)

### Week 11: Continuity Stabilization

**Tasks**:
- [ ] Read full manuscript for continuity breaks
- [ ] Fix references to cut chapters
- [ ] Ensure tracking fragments connect smoothly
- [ ] Verify thematic threads maintain coherence
- [ ] Update Lilith's timeline references

**Deliverables**:
- Continuity issues log
- Fixes integrated

### Week 12: Pivotal Scene Dramatization

**Tasks**:
- [ ] Finalize Devaka betrayal scene (already added in Week 5)
- [ ] Expand Lilith's first intervention scene (+1,200 words)
- [ ] Verify Stewart rooftop expansion (already added in Week 9)
- [ ] Optional: Expand Lilith car confession if budget allows

**Deliverables**:
- 3+ pivotal scenes fully dramatized
- Constraint C5 satisfied

### Week 13: Lilith Chapter Compression

**Tasks**:
- [ ] Compress Chapter 3 (Lilith CP01): 3,049 → 2,000
- [ ] Compress Chapter 5 (Lilith CP02): 2,673 → 1,800
- [ ] Compress Chapter 15 (Lilith CP07): 4,711 → 3,000
- [ ] Compress Chapter 17 (Lilith CP08): 3,546 → 2,200
- [ ] Compress Chapter 19 (Lilith CP09): 10,011 → 4,200
- [ ] Compress Chapter 21 (Lilith CP10): 3,738 → 1,100

**Deliverables**:
- All Lilith chapters at target length
- Tracking intensity preserved

### Week 14: Transition Polish

**Tasks**:
- [ ] Review all chapter transitions
- [ ] Strengthen weak bridges
- [ ] Remove placeholder transitions
- [ ] Ensure pacing consistency

**Deliverables**:
- Smooth reading flow
- No jarring jumps

### Gate G4: Continuity Complete

**Date**: End of Week 14

**DERIVED word count (computed from G3 + operations):**

```
Starting from G3 total:                         174,951

Week 11 operations (continuity fixes):
  No word count change expected:                      0

Week 12 operations (pivotal scene expansion):
  Lilith first intervention scene expansion:     +1,200
  Subtotal after week 12:                       176,151

Week 13 operations (Lilith compression):
  Ch3: 3,049→2,000                               -1,049
  Ch5: 2,673→1,800                                 -873
  Ch7: 3,221→450 (already done, verify)              0
  Ch9: 5,998→650 (already done, verify)              0
  Ch11: 4,883→650 (already done, verify)             0
  Ch13: 2,714→450 (already done, verify)             0
  Ch15: 4,711→3,000                              -1,711
  Ch17: 3,546→2,200                              -1,346
  Ch19: 10,011→4,200                             -5,811
  Ch21: 3,738→1,100                              -2,638
  Subtotal after week 13:                       162,723

Week 14 operations (transition polish):
  No word count change expected:                      0
────────────────────────────────────────────────────
G4 EXPECTED TOTAL:                              162,723

Lilith composition after compression:
  Fragments (Ch7,9,11,13): 450+650+650+450 = 2,200
  Active (Ch3,5,15,17,19,21): 2,000+1,800+3,000+2,200+4,200+1,100 = 14,300
  Total Lilith: 16,500 words
```

**Acceptance test**:
```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify total
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
if [ $TOTAL -ge 160000 ] && [ $TOTAL -le 166000 ]; then
  echo "G4 word count: PASS ($TOTAL, expected ~162,723)"
else
  echo "G4 word count: FAIL ($TOTAL, expected ~162,723)"
fi

# Verify Lilith compression
LILITH=$(jq '[.chapters[] | select(.type == "Lilith") | .word_count] | add' out/revision_audit/analysis_data.json)
if [ $LILITH -ge 15000 ] && [ $LILITH -le 18000 ]; then
  echo "G4 Lilith: PASS ($LILITH words, expected ~16,500)"
else
  echo "G4 Lilith: FAIL ($LILITH words, expected ~16,500)"
fi
```

**Pass criteria**:
- Total words: 160,000–166,000 (derived center: 162,723)
- Lilith words: 15,000–18,000 (target: 16,500)
- Continuity log cleared
- 3+ pivotal scenes verified (Devaka, Stewart, Lilith first intervention)

---

## Phase V: Meta/Climax Compression (Weeks 15-16)

### Week 15: Final Sequence Compression

**Tasks**:
- [ ] Compress Chapter 23 (Deva): 6,813 → 4,600
- [ ] Compress Chapter 24 (Future): 8,650 → 4,600
- [ ] Compress Chapter 25 (Formless): 11,880 → 4,800
  - Combine 2 of 4 formless realm stages per editor
- [ ] Compress Chapter 26 (Climax): 10,464 → 4,600

**Deliverables**:
- Final sequence at ~18,600 words (from 37,807)
- Philosophical content preserved in condensed form

### Week 16: Balance and Verify

**Tasks**:
- [ ] Run full manuscript analysis
- [ ] Adjust any over/under target chapters
- [ ] Verify all constraint values
- [ ] Prepare for line edit

**Deliverables**:
- Total words: 123,000–125,000
- All constraints passing

### Gate G5: Structure Final

**Date**: End of Week 16

**DERIVED word count (computed from G4 + operations):**

```
Starting from G4 total:                         162,723

Week 15 operations (final sequence compression):
  Ch23 Deva: 6,813→4,600                         -2,213
  Ch24 Future: 8,650→4,600                       -4,050
  Ch25 Formless: 11,880→4,800                    -7,080
  Ch26 Climax: 10,464→4,600                      -5,864
  Subtotal after week 15:                       143,516

Week 16 operations (balance and verify):
  Adjustment to reach exactly 124,000:         -19,516
  (Distributed across over-target chapters)
────────────────────────────────────────────────────
G5 TARGET TOTAL:                                124,000
```

**ISSUE**: The math shows we'll be at ~143,516 after meta/climax compression, which is 19,516 words OVER our target of 124,000. This means Week 16 must include additional line-edit compression beyond "balance and verify".

**REVISED Week 16 scope**: Must include ~19,500 additional words of cuts distributed across all remaining chapters to hit 124,000 target.

**Acceptance test**:
```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify all constraints
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)
PCT=$(echo "scale=4; $MANCH * 100 / $TOTAL" | bc)
CUT=$((216594 - TOTAL))

echo "C1 Total: $TOTAL (target: 120,000-130,000)"
echo "C2 Manchester: $MANCH words, $PCT% (target: 40-50%)"
echo "C3 Net cut: $CUT (target: 80,000-100,000)"

# Verify constraints
if [ $TOTAL -ge 120000 ] && [ $TOTAL -le 130000 ]; then
  echo "C1: PASS"
else
  echo "C1: FAIL"
fi

if (( $(echo "$PCT >= 40" | bc -l) )) && (( $(echo "$PCT <= 50" | bc -l) )); then
  echo "C2: PASS"
else
  echo "C2: FAIL"
fi

if [ $CUT -ge 80000 ] && [ $CUT -le 100000 ]; then
  echo "C3: PASS"
else
  echo "C3: FAIL"
fi
```

**Pass criteria**:
- C1: 120,000–130,000 words (target: 124,000) ✓
- C2: 40–50% Manchester (expected: 40.32% = 50,000/124,000) ✓
- C3: 86,594–96,594 net cut (expected: 92,594) ✓
- C4: 4 incarnations cut ✓
- C5: 3+ scenes dramatized ✓

---

## Phase VI: Line Edit (Weeks 17-18)

### Week 17: Tic Reduction Pass

**Tasks**:
- [ ] Global search/reduce "particular" (target: 50%)
- [ ] Global search/reduce "something" (target: 50%)
- [ ] Reduce "Not X—Y" constructions (target: 50%)
- [ ] Vary em-dash cadence with full stops/semicolons
- [ ] Focus on top 5 tic-density chapters

**Deliverables**:
- Tic counts reduced by ~50%
- Prose rhythm varied

### Week 18: Abstraction Grounding Pass

**Tasks**:
- [ ] Focus on top 10 abstraction-density chapters
- [ ] Add sensory anchors to philosophical passages
- [ ] Reduce reflective elaboration by 30-40%
- [ ] Insert Ka-register moments in later incarnations
- [ ] Final polish

**Deliverables**:
- Abstraction density reduced
- Prose grounded in physical sensation
- Manuscript ready for submission

### Gate G6: Line Edit Complete (FINAL)

**Date**: End of Week 18

**DERIVED word count (computed from G5 + operations):**

```
Starting from G5 total:                         124,000

Week 17-18 operations (line edit pass):
  Tic reduction: minimal word change              ~-500
  Abstraction grounding: may add sensory details  ~+500
  Net change:                                           0
────────────────────────────────────────────────────
G6 FINAL EXPECTED TOTAL:                        124,000

Expected final composition:
  Manchester (Ch1 + Ch22): 50,000 words (40.32%)
  Historical (6 chapters): 38,900 words (31.37%)
  Lilith (10 chapters): 16,500 words (13.31%)
  Final sequence (Ch23-26): 18,600 words (15.00%)
```

**Acceptance test**:
```bash
#!/bin/bash
# Run full analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

echo "=== FINAL CONSTRAINT VERIFICATION ==="

# C1: Total words
TOTAL=$(jq '.total_words' out/revision_audit/analysis_data.json)
if [ $TOTAL -ge 110000 ] && [ $TOTAL -le 130000 ]; then
  echo "C1 Total Words: PASS ($TOTAL)"
else
  echo "C1 Total Words: FAIL ($TOTAL, target 110,000-130,000)"
fi

# C2: Manchester %
MANCH=$(jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json)
PCT=$(echo "scale=2; $MANCH * 100 / $TOTAL" | bc)
if (( $(echo "$PCT >= 40" | bc -l) )) && (( $(echo "$PCT <= 50" | bc -l) )); then
  echo "C2 Manchester %: PASS ($PCT%, $MANCH words)"
else
  echo "C2 Manchester %: FAIL ($PCT%, target 40-50%)"
fi

# C3: Net cut
CUT=$((216594 - TOTAL))
if [ $CUT -ge 80000 ] && [ $CUT -le 100000 ]; then
  echo "C3 Net Cut: PASS ($CUT words)"
else
  echo "C3 Net Cut: FAIL ($CUT, target 80,000-100,000)"
fi

# C4: Incarnations cut
CHAPTERS=$(jq '.chapters | length' out/revision_audit/analysis_data.json)
INCAR_CUT=$((26 - CHAPTERS))
if [ $INCAR_CUT -ge 3 ] && [ $INCAR_CUT -le 4 ]; then
  echo "C4 Incarnations Cut: PASS ($INCAR_CUT)"
else
  echo "C4 Incarnations Cut: FAIL ($INCAR_CUT, target 3-4)"
fi

# C5: Pivotal scenes (manual verification required)
echo "C5 Pivotal Scenes: MANUAL (verify Devaka, Stewart, Lilith intervention)"

# C6: Reflective reduction (abstraction density proxy)
BASELINE_AVG=0.76
CURRENT_AVG=$(jq '[.chapters[] | .abstraction_density] | add/length' out/revision_audit/analysis_data.json)
echo "C6 Reflective Reduction: abstraction density baseline=$BASELINE_AVG, current=$CURRENT_AVG"

# C7: Tic reduction
echo "C7 Tic Density (per 10k words):"
python3 << 'PYEOF'
import json
with open('out/revision_audit/analysis_data.json') as f:
    data = json.load(f)
total = data['total_words']
tics = {'particular': 0, 'something': 0, 'not_x_y_pattern': 0, 'em_dashes': 0}
for ch in data['chapters']:
    for tic, count in ch['tics'].items():
        tics[tic] += count
baselines = {'particular': 5.26, 'something': 48.52, 'not_x_y_pattern': 5.45, 'em_dashes': 133.15}
for tic in tics:
    density = tics[tic] / total * 10000
    target = baselines[tic] * 0.5
    status = 'PASS' if density <= target else 'FAIL'
    print(f"  {tic}: {density:.2f} (target ≤{target:.2f}) {status}")
PYEOF
```

**Pass criteria (ALL must be PASS)**:
- C1: 110,000–130,000 words ✓
- C2: 40–50% Manchester ✓
- C3: 80,000–100,000 net cut ✓
- C4: 3–4 incarnations cut ✓
- C5: ≥3 pivotal scenes dramatized ✓
- C6: 30–40% reflective reduction (abstraction density proxy) ✓
- C7: ≤50% tic density for all key tics ✓

---

## Schedule Summary

| Week | Phase | Focus | Key Deliverable |
|------|-------|-------|-----------------|
| 1-2 | I | Structural Decisions | Approved structure |
| 3-4 | II | Incarnation Cuts | 4 chapters removed, 4 fragments added |
| 5-6 | II | Historical Compression | 5 chapters compressed |
| 7-8 | III | Manchester Ch 1 | +17,000 words new content |
| 9-10 | III | Manchester Ch 22 | +15,000 words new content |
| 11-12 | IV | Continuity/Dramatization | 3+ pivotal scenes |
| 13-14 | IV | Lilith Compression | Tracking chapters trimmed |
| 15-16 | V | Final Sequence | Meta/climax condensed |
| 17-18 | VI | Line Edit | Tic/abstraction reduction |

**Total duration**: 18 weeks
**Target completion**: ~4.5 months from start
