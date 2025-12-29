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

**Acceptance test**:
```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify word count
jq '.total_words' out/revision_audit/analysis_data.json
# Expected: 130,000-145,000 (still needs Manchester expansion)

# Verify incarnations removed
jq '.chapters | length' out/revision_audit/analysis_data.json
# Expected: 22

# Verify no Philon, Verinus, Macarius, Kaoru chapters
jq '.chapters[] | select(.name | test("Philon|Verinus|Macarius|Kaoru"; "i"))' out/revision_audit/analysis_data.json
# Expected: no output
```

**Pass criteria**:
- Total words: 130,000–145,000
- Chapter count: 22
- No cut chapters present
- Lilith fragments integrated

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

**Acceptance test**:
```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify total
jq '.total_words' out/revision_audit/analysis_data.json
# Expected: 120,000-128,000

# Verify Manchester words
jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json
# Expected: 48,000-52,000

# Calculate Manchester %
# Expected: 40-43%
```

**Pass criteria**:
- Total words: 120,000–128,000
- Manchester words: 48,000–52,000
- Manchester %: 40–43%
- Stewart thread resolved
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

**Acceptance test**:
```bash
# Verify total
jq '.total_words' out/revision_audit/analysis_data.json
# Expected: 122,000-126,000

# Verify Lilith compression
jq '[.chapters[] | select(.type == "Lilith") | .word_count] | add' out/revision_audit/analysis_data.json
# Expected: 14,000-18,000

# Verify no continuity breaks (manual review)
```

**Pass criteria**:
- Total words: 122,000–126,000
- Lilith words: 14,000–18,000
- Continuity log cleared
- 3+ pivotal scenes verified

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

**Acceptance test**:
```bash
# Run analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify all constraints
jq '.total_words' out/revision_audit/analysis_data.json
# Expected: 123,000-125,000

jq '[.chapters[] | select(.type == "Manchester") | .word_count] | add' out/revision_audit/analysis_data.json
# Expected: 48,000-52,000

# Calculate Manchester %
# Expected: 40-42%

# Verify net cut
# 216,594 - current = 91,594-93,594
```

**Pass criteria**:
- C1: 123,000–125,000 words ✓
- C2: 40–42% Manchester ✓
- C3: 91,594–93,594 net cut ✓
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

**Acceptance test**:
```bash
# Run full analyzer
python3 /home/user/Wheel_of_Meat/tools/revision_audit/manuscript_analyzer.py

# Verify final totals
jq '.total_words' out/revision_audit/analysis_data.json
# Expected: 120,000-124,000

# Calculate tic densities (per 10k words)
# Baseline: particular=5.26, something=48.52, not_x_y=5.45, em_dashes=133.15
# Target: ≤50% of baseline for each

# Verify abstraction density improvement
jq '[.chapters[] | .abstraction_density] | add/length' out/revision_audit/analysis_data.json
# Expected: lower average than baseline
```

**Pass criteria**:
- C1: 120,000–124,000 ✓
- C2: 40–50% Manchester ✓
- C3: 92,594–96,594 net cut ✓
- C4: 4 incarnations ✓
- C5: 3+ dramatized ✓
- C6: 30–40% reflective reduction ✓
- C7: ≤50% tic density ✓

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
