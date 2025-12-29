# Execution Schedule — *The Wheel of Meat* Revision (v2)

**Prepared:** December 2025 (v2 revision)
**Target Submission:** April 2026
**Timeline:** 16-20 weeks

---

## Why v1 Failed

The v1 schedule was based on flawed math: claiming "Manchester expansion of 15-20k" would achieve 40-50% Manchester. It would not. At a target of 120,000 words, 40% Manchester requires 48,000 words—not the ~33,000 that v1's expansion would produce. Additionally, v1 lacked explicit verification gates to catch this error before execution began.

## What Changed in v2

- **Gate system:** Three explicit verification gates with pass/fail criteria
- **Manchester target corrected:** 50,000 words (41.7% of 120k), requiring +32,357 new content
- **Each week specifies:** chapters touched, word targets (add/cut), verification step
- **Recompute totals:** After every structural move, totals are verified via manuscript_analyzer.py

---

## GATED EXECUTION MODEL

### GATE 1: TOC + Word Budget Verified

**Trigger:** End of Week 2
**Pass Criteria:**
- [ ] Final TOC locked (14-20 chapters per chosen option)
- [ ] Per-chapter word budgets sum to 120,000 (or 115,000 for Option B)
- [ ] Manchester chapters sum to 50,000+ (41.7%+)
- [ ] All cut decisions documented

**Fail Action:** Do not proceed to Phase 2 until math verified.

### GATE 2: Post-Cut Continuity Pass Complete

**Trigger:** End of Week 6
**Pass Criteria:**
- [ ] All cut chapters removed from manuscript
- [ ] No broken references (character names, events, objects from cut chapters)
- [ ] Lilith chapters revised to reference cut incarnations as brief mentions
- [ ] manuscript_analyzer.py run confirms word count: ~158,000 → ~110,000 after compressions

**Fail Action:** Continuity issues must be resolved before new content written.

### GATE 3: Manchester Share Verified at 40-50%

**Trigger:** End of Week 10
**Pass Criteria:**
- [ ] Run manuscript_analyzer.py on current draft
- [ ] Manchester section total: ≥48,000 words
- [ ] Manchester %: 40-50% of current total
- [ ] All new scenes integrated and smoothed

**Fail Action:** Additional Manchester content required; do not proceed to line-edit.

---

## Phase Overview

| Phase | Weeks | Focus | Verification |
|-------|-------|-------|--------------|
| 1: Planning & Gates | 1-2 | Finalize structure, verify math | GATE 1 |
| 2: Structural Cuts | 3-6 | Remove chapters, compress retained | GATE 2 |
| 3: Manchester Expansion | 7-10 | Write new scenes, integrate | GATE 3 |
| 4: Scene-Level Polish | 11-13 | Dramatizations, character arcs | Quality check |
| 5: Line-Edit Pass | 14-16 | Tic reduction, prose tightening | Tic counts |
| 6: Final Polish | 17-20 | Beta read, submission prep | Final verification |

---

## PHASE 1: Planning & Gates (Weeks 1-2)

### Week 1: Structure Decision

**Chapters Touched:** None (planning only)
**Word Targets:** N/A

**Tasks:**
- [ ] Confirm Option A or B
- [ ] Document cut decisions with rationale
- [ ] Map thematic threads from cut chapters to preserved references
- [ ] Create per-chapter word budget spreadsheet

**Verification:** Draft TOC with budgets; sum equals target

### Week 2: Scene Planning

**Chapters Touched:** None (planning only)
**Word Targets:** N/A

**Tasks:**
- [ ] Finalize Manchester scene outlines (all FL, SR, RC, BT scenes)
- [ ] Complete character voice notes
- [ ] Research Manchester locations for authenticity
- [ ] Mark integration points in manuscript

**Verification:** Scene inventory complete; GATE 1 checklist passed

**GATE 1 CHECK:** ☐ TOC verified ☐ Budgets sum correctly ☐ Manchester 41.7%+

---

## PHASE 2: Structural Cuts (Weeks 3-6)

### Week 3: Cut Four Incarnations

**Chapters Touched:** 6, 7, 8, 9, 10, 11, 12, 13 (removed)
**Word Targets:**
- Cut: 58,660 words
- Running total: 216,594 → 157,934

**Tasks:**
- [ ] Remove Ch 6 (Philon) + Ch 7 (CP03)
- [ ] Remove Ch 8 (Verinus) + Ch 9 (CP04)
- [ ] Remove Ch 10 (Macarius) + Ch 11 (CP05)
- [ ] Remove Ch 12 (Kaoru) + Ch 13 (CP06)
- [ ] Update chapter numbering

**Verification:** Run manuscript_analyzer.py → confirm ~158,000 words

### Week 4: Compress Retained Incarnations (Part 1)

**Chapters Touched:** 4 (Chandra), 14 (Diego)
**Word Targets:**
- Ch 4: 19,676 → 7,500 (cut 12,176)
- Ch 14: 18,641 → 7,500 (cut 11,141)
- Running total: 157,934 → 134,617

**Tasks:**
- [ ] Focus Chandra on betrayal arc only
- [ ] Add dramatized Devaka betrayal scene (+1,500)
- [ ] Focus Diego on essential horror arc
- [ ] Remove pre-arrest elaboration

**Verification:** Chapter word counts verified

### Week 5: Compress Retained Incarnations (Part 2)

**Chapters Touched:** 16 (Renaissance), 18 (Taiping), 20 (Malone)
**Word Targets:**
- Ch 16: 13,725 → 5,000 (cut 8,725)
- Ch 18: 6,512 → 4,000 (cut 2,512)
- Ch 20: 11,144 → 6,000 (cut 5,144)
- Running total: 134,617 → 118,236

**Tasks:**
- [ ] Compress Renaissance skeptic passages
- [ ] Tighten Taiping collective scenes
- [ ] Cut Malone funeral scene
- [ ] Remove Doyle witness (3 → 2)

**Verification:** Chapter word counts verified

### Week 6: Compress Lilith + Meta/Climax

**Chapters Touched:** 3, 5, 15, 17, 19, 21, 23, 24, 25, 26
**Word Targets:**
- Lilith: 27,728 → 12,000 (cut 15,728)
- Meta/Climax: 37,807 → 23,000 (cut 14,807)
- Running total: 118,236 → 87,701

**Tasks:**
- [ ] Merge Lilith chapters: 10 → 4
- [ ] Add brief shards for cut incarnations
- [ ] Compress Deva, Future, Formless, Climax
- [ ] Combine Formless stages 2-3
- [ ] Full continuity pass

**Verification:** Run manuscript_analyzer.py → confirm ~87,000-88,000 words

**GATE 2 CHECK:** ☐ All cuts complete ☐ No broken references ☐ Word count verified

---

## PHASE 3: Manchester Expansion (Weeks 7-10)

### Week 7: Write Falling-in-Love Scenes

**Chapters Touched:** 1 (expanding)
**Word Targets:**
- FL-1 (Walnut): +2,500
- FL-2 (Flat): +3,000
- FL-3 (Campus): +2,000
- Running total: 87,701 → 95,201

**Tasks:**
- [ ] Draft FL-1: first date at The Walnut
- [ ] Draft FL-2: intimacy at Lilith's flat
- [ ] Draft FL-3: campus morning routine
- [ ] First revision pass on all three

**Verification:** Scene word counts; voice consistency check

### Week 8: Write Stewart + Silas Scenes

**Chapters Touched:** 1 (expanding), 22 (expanding)
**Word Targets:**
- SR-1 (Hospital): +2,500
- SR-2 (Departure): +2,000
- RC-1 (Ellen): +2,500
- RC-2 (Flashback): +2,000
- Running total: 95,201 → 104,201

**Tasks:**
- [ ] Draft SR-1: hospital visit
- [ ] Draft SR-2: Stewart's departure
- [ ] Draft RC-1: Ellen therapy session
- [ ] Draft RC-2: night flashback
- [ ] First revision pass

**Verification:** Scene word counts; character arc check

### Week 9: Write Bridging + Pivots

**Chapters Touched:** Distributed (5, 8, 12, 15 in new TOC)
**Word Targets:**
- BT-1 through BT-4: +4,000
- Car confession expansion: +300
- Stewart suspended time: +100
- Running total: 104,201 → 108,601

**Tasks:**
- [ ] Draft BT-1: after Chandra anchor
- [ ] Draft BT-2: after Diego anchor
- [ ] Draft BT-3: after Renaissance anchor
- [ ] Draft BT-4: after Malone anchor
- [ ] Revise car confession (add pressure)
- [ ] Expand Stewart fall moment

**Verification:** Bridging scenes distributed; pivots integrated

### Week 10: Integration + Lilith Resistance

**Chapters Touched:** 1, 22, 24
**Word Targets:**
- Remaining Manchester content: +8,000
- Lilith final resistance expansion: +500
- Existing content enhancement: +3,000
- Running total: 108,601 → 120,101

**Tasks:**
- [ ] Integrate all new scenes into manuscript
- [ ] Smooth transitions between old and new
- [ ] Expand Lilith final resistance (Ch 24)
- [ ] First full read-through of Manchester chapters
- [ ] Trim 100 words to hit 120,000 target

**Verification:** Run manuscript_analyzer.py → confirm ~120,000 words

**GATE 3 CHECK:** ☐ Manchester ≥48,000 ☐ Manchester % ≥40% ☐ All scenes integrated

---

## PHASE 4: Scene-Level Polish (Weeks 11-13)

### Week 11: Silas Arc Strengthening

**Chapters Touched:** 1, 22, 24, 26
**Word Targets:** Net neutral (revisions only)

**Tasks:**
- [ ] Verify Silas visible wants in Ch 1
- [ ] Check resistance arc through middle
- [ ] Ensure pain visible before release
- [ ] Silas character arc document complete

**Verification:** Beta reader test: "What does Silas want?"

### Week 12: Lilith Arc Strengthening

**Chapters Touched:** L1-L4, 24, 26
**Word Targets:** Net neutral (revisions only)

**Tasks:**
- [ ] Manipulation visible but sympathetic
- [ ] Genuine feeling apparent
- [ ] First intervention (shard) shows cost
- [ ] Final resistance feels earned

**Verification:** Lilith arc feels tragic

### Week 13: Transition Polish

**Chapters Touched:** All chapter endings/beginnings
**Word Targets:** Net neutral

**Tasks:**
- [ ] Smooth all transitions
- [ ] Manchester returns feel grounded
- [ ] Historical-to-Lilith flow natural
- [ ] Pacing assessment complete

**Verification:** Full read-through; no jarring transitions

---

## PHASE 5: Line-Edit Pass (Weeks 14-16)

### Week 14: High-Priority Tic Chapters

**Chapters Touched:** 25, 26, 24, 23, 22
**Word Targets:** Net reduction ~2,000 (reflective cuts)

**Tasks:**
- [ ] Ch 25: "something" 125 → 40; em-dashes 294 → 90
- [ ] Ch 26: "not X—Y" 24 → 8; "something" 74 → 25
- [ ] Ch 24: Ground post-scarcity abstraction
- [ ] Ch 23: Ground celestial abstraction
- [ ] Ch 22: Clean new Manchester content

**Verification:** Tic counts per chapter

### Week 15: Remaining Chapters

**Chapters Touched:** 4, 14, 1, remaining
**Word Targets:** Net reduction ~1,500 (reflective cuts)

**Tasks:**
- [ ] Ch 4: "particular" 22 → 11; em-dashes reduced
- [ ] Ch 14: Em-dashes 230 → 80
- [ ] Ch 1: Clean new content
- [ ] All other chapters: general tic pass

**Verification:** Manuscript-wide tic report

### Week 16: Reflective Elaboration

**Chapters Touched:** All
**Word Targets:** Final trim to 118,000-120,000

**Tasks:**
- [ ] Full pass for explanatory paragraphs
- [ ] Cut 30-40% of identified reflective elaboration
- [ ] Add Ka-register moments (5+)
- [ ] Final word count verification

**Verification:** Run manuscript_analyzer.py → confirm final count

---

## PHASE 6: Final Polish (Weeks 17-20)

### Week 17: Full Read-Through

**Tasks:**
- [ ] Read manuscript in 2-3 sessions
- [ ] Flag remaining issues
- [ ] Pacing assessment
- [ ] Create fix list

### Week 18: Fix Pass

**Tasks:**
- [ ] Address flagged issues
- [ ] Final continuity check
- [ ] Last tic cleanup

### Week 19: Beta Feedback

**Tasks:**
- [ ] Send to 2-3 beta readers
- [ ] Collect feedback
- [ ] Prioritize fixes

### Week 20: Submission

**Tasks:**
- [ ] Address priority beta feedback
- [ ] Final proofread
- [ ] Format manuscript
- [ ] Prepare cover letter
- [ ] **SUBMIT**

---

## Final Verification Checklist

**Before Submission:**

| Constraint | Target | Actual | ✓ |
|------------|--------|--------|---|
| Final word count | 110,000-130,000 | _____ | ☐ |
| Manchester % | 40-50% | ___% | ☐ |
| Net cut | 80,000-100,000 | _____ | ☐ |
| Incarnations cut | 3-4 | 4 | ☐ |
| Pivotal dramatizations | ≥3 | 5 | ☐ |
| "particular" | ≤44 | _____ | ☐ |
| "something" | ≤465 | _____ | ☐ |
| "not X—Y" | ≤52 | _____ | ☐ |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Manchester content underdelivers | Gate 3 catches before line-edit |
| Cuts create continuity gaps | Gate 2 requires full pass |
| Word count drift | Weekly verification steps |
| Beta feedback requires major changes | Week 19-20 buffer |
| Schedule slippage | Gates force no proceeding without verification |

---

*Execution schedule prepared December 2025 (v2)*
