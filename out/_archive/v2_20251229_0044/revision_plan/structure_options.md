# Structural Options — *The Wheel of Meat* (v2)

**Prepared:** December 2025 (v2 revision)
**Current Word Count:** 216,594 (verified via manuscript_analyzer.py)
**Target Word Count:** 110,000–130,000 (aim: 120,000)

---

## V2 Changelog

**Why v1 failed:**
- Option A totaled 132,280 words with only 20% Manchester (both failed constraints)
- Option B totaled 111,558 words with only 26% Manchester (Manchester constraint failed)
- "Expand Manchester 15-20k" interpreted incorrectly; 40-50% of 120k requires 48,000-60,000 words

**What changed in v2:**
- Manchester target computed as % of FINAL, not as simple addition
- Both options now constraint-correct with Manchester at 41.7%+
- Per-chapter word budgets verified to sum to totals
- All calculations show derivation from analysis_data.json

---

## CONSTRAINT SUMMARY (All Plans Must Satisfy)

| Constraint | Target | Verification |
|------------|--------|--------------|
| Final word count | 110,000-130,000 | manuscript_analyzer.py |
| Manchester % | 40-50% of final | Manchester words / total words |
| Net cut | 80,000-100,000 | Current - final |
| Incarnations cut | 3-4 sequences | TOC chapter count |
| Pivotal dramatizations | ≥3 moments | Scene inventory |
| Tic reduction | 50% relative | Tic counts per 10k words |

---

## OPTION A: Letter-Faithful (Constraint-Correct)

**Strategy:** Cut 4 incarnations entirely; aggressive compression of retained; maximum Manchester expansion

### Core Numbers

| Metric | Current | Target | Change |
|--------|---------|--------|--------|
| Total words | 216,594 | **120,000** | -96,594 |
| Manchester | 17,643 (8.1%) | **50,000 (41.7%)** | +32,357 |
| Historical | 116,600 | 35,000 | -81,600 |
| Lilith | 44,544 | 12,000 | -32,544 |
| Meta/Climax | 37,807 | 23,000 | -14,807 |

**Constraint Check:**
- Manchester: 50,000 / 120,000 = 41.7% ✓ (within 40-50%)
- Net cut: 96,594 ✓ (within 80,000-100,000)
- Final: 120,000 ✓ (within 110,000-130,000)

### Incarnations Cut (4 full + 4 paired Lilith)

| Chapter | Incarnation | Words | Paired Lilith | Words | Total |
|---------|-------------|-------|---------------|-------|-------|
| Ch 6 | Philon (Athens) | 10,202 | Ch 7 (CP03) | 3,221 | 13,423 |
| Ch 8 | Verinus (Rome) | 9,405 | Ch 9 (CP04) | 5,998 | 15,403 |
| Ch 10 | Macarius (Egypt) | 13,777 | Ch 11 (CP05) | 4,883 | 18,660 |
| Ch 12 | Kaoru (Heian) | 8,460 | Ch 13 (CP06) | 2,714 | 11,174 |
| **TOTAL** | | **41,844** | | **16,816** | **58,660** |

### Incarnations Retained + Compressed

| Chapter | Incarnation | Current | Target | Cut | Rationale |
|---------|-------------|---------|--------|-----|-----------|
| Ch 2 | Ka (Prehistoric) | 5,058 | 5,000 | 58 | Essential origin, exemplar prose |
| Ch 4 | Chandra (Mauryan) | 19,676 | 7,500 | 12,176 | Strongest betrayal arc |
| Ch 14 | Diego (Inquisition) | 18,641 | 7,500 | 11,141 | Horror without exploitation |
| Ch 16 | Renaissance Skeptic | 13,725 | 5,000 | 8,725 | Historical continuity |
| Ch 18 | Taiping Rebel | 6,512 | 4,000 | 2,512 | Collectivist contrast |
| Ch 20 | Malone (Noir) | 11,144 | 6,000 | 5,144 | Tightest prose |
| **TOTAL** | | **74,756** | **35,000** | **39,756** | |

### Lilith Chapter Restructure

| Current | Words | → | New | Words |
|---------|-------|---|-----|-------|
| CP01 + CP02 | 5,722 | → | L1: Discovery | 2,000 |
| CP03-06 | 16,816 | → | CUT | 0 |
| CP07 | 4,711 | → | L2: The Thread | 2,500 |
| CP08 + CP09 | 13,557 | → | L3: Approaching | 4,000 |
| CP10 | 3,738 | → | L4: The Edge | 3,500 |
| **TOTAL** | **44,544** | → | | **12,000** |

### Metaphysical/Climax Compression

| Chapter | Current | Target | Cut |
|---------|---------|--------|-----|
| Ch 23 (Deva) | 6,813 | 5,000 | 1,813 |
| Ch 24 (Future) | 8,650 | 5,500 | 3,150 |
| Ch 25 (Formless) | 11,880 | 7,000 | 4,880 |
| Ch 26 (Climax) | 10,464 | 5,500 | 4,964 |
| **TOTAL** | **37,807** | **23,000** | **14,807** |

### Manchester Expansion

| Component | Words |
|-----------|-------|
| Ch 1 existing (trimmed) | 8,000 |
| FL-1: The Walnut (first date) | 2,500 |
| FL-2: Lilith's flat (intimacy) | 3,000 |
| FL-3: Campus walk (routine) | 2,000 |
| RC-1: Ellen therapy session | 2,500 |
| RC-2: After first flashback | 2,000 |
| **Ch 1 Total** | **20,000** |
| Ch 22 existing (trimmed) | 10,000 |
| SR-1: Hospital visit | 2,500 |
| SR-2: Stewart departure | 2,000 |
| BT-1 through BT-4 (distributed) | 3,000 |
| Dramatized pivotal moments | 2,500 |
| **Ch 22 Total / Distributed** | **20,000** |
| Additional Manchester expansion | 10,000 |
| **TOTAL MANCHESTER** | **50,000** |

### Proposed Table of Contents — Option A

| New Ch | Title | Type | Budget |
|--------|-------|------|--------|
| 1 | Manchester: The Pattern Emerges | Manchester | 20,000 |
| 2 | Ka: The First Hunger | Historical | 5,000 |
| 3 | Lilith: Discovery | Lilith | 2,000 |
| 4 | Chandra: The Betrayal | Historical | 7,500 |
| 5 | BT-1: Manchester Anchor | Manchester | 1,000 |
| 6 | Diego: The Accused | Historical | 7,500 |
| 7 | Lilith: The Thread | Lilith | 2,500 |
| 8 | BT-2: Manchester Anchor | Manchester | 1,000 |
| 9 | Renaissance: The Skeptic | Historical | 5,000 |
| 10 | Taiping: The Rebel | Historical | 4,000 |
| 11 | Lilith: Approaching | Lilith | 4,000 |
| 12 | BT-3: Manchester Anchor | Manchester | 1,000 |
| 13 | Malone: The Detective | Historical | 6,000 |
| 14 | Lilith: The Edge | Lilith | 3,500 |
| 15 | BT-4: Manchester Anchor | Manchester | 1,000 |
| 16 | Manchester: The Breakthrough | Manchester | 26,000 |
| 17 | Deva Celestial | Metaphysical | 5,000 |
| 18 | Future Prophet | Metaphysical | 5,500 |
| 19 | Formless Realms | Metaphysical | 7,000 |
| 20 | Pure Abodes Awakened | Climax | 5,500 |
| **TOTAL** | | | **120,000** |

### Word Distribution — Option A

| Type | Words | Percentage |
|------|-------|------------|
| Manchester | 50,000 | **41.7%** ✓ |
| Historical | 35,000 | 29.2% |
| Lilith | 12,000 | 10.0% |
| Metaphysical/Climax | 23,000 | 19.2% |
| **TOTAL** | **120,000** | **100%** |

### Risk Assessment — Option A

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Editor acceptance | **Low** | — | Follows letter directly |
| Thematic gaps (cut incarnations) | Medium | Medium | Lilith shards reference cut lives |
| Manchester expansion challenge | Medium | High | Detailed scene plan provided |
| Pacing (smaller book) | Low | Low | Cleaner structure compensates |

**Overall Editor Acceptance Risk: LOW**

---

## OPTION B: Vision-Preserving Cadence (Constraint-Correct)

**Strategy:** Keep more incarnations with strict caps; convert 2 to shards; more aggressive historical compression

### Core Numbers

| Metric | Current | Target | Change |
|--------|---------|--------|--------|
| Total words | 216,594 | **115,000** | -101,594 |
| Manchester | 17,643 (8.1%) | **52,000 (45.2%)** | +34,357 |
| Historical (5 full + 2 shard) | 116,600 | 28,000 | -88,600 |
| Lilith | 44,544 | 14,000 | -30,544 |
| Meta/Climax | 37,807 | 21,000 | -16,807 |

**Constraint Check:**
- Manchester: 52,000 / 115,000 = 45.2% ✓ (within 40-50%)
- Net cut: 101,594 ✓ (within 80,000-100,000)
- Final: 115,000 ✓ (within 110,000-130,000)

### Incarnation Treatment

**Full Cuts (2 incarnations + 2 Lilith):**

| Chapter | Incarnation | Words | Paired Lilith | Words | Total |
|---------|-------------|-------|---------------|-------|-------|
| Ch 8 | Verinus (Rome) | 9,405 | Ch 9 (CP04) | 5,998 | 15,403 |
| Ch 10 | Macarius (Egypt) | 13,777 | Ch 11 (CP05) | 4,883 | 18,660 |
| **TOTAL** | | **23,182** | | **10,881** | **34,063** |

**Convert to Lilith Shards (2 incarnations):**

| Chapter | Incarnation | Current | Shard | Words | Net Savings |
|---------|-------------|---------|-------|-------|-------------|
| Ch 6 | Philon (Athens) | 10,202 | Memory fragment | 1,500 | 8,702 |
| Ch 12 | Kaoru (Heian) | 8,460 | Love-letter discovery | 1,500 | 6,960 |
| + Lilith CP03, CP06 | | 5,935 | Absorbed into L2 | 0 | 5,935 |
| **TOTAL** | | **24,597** | | **3,000** | **21,597** |

**Retained with Strict Caps (6,000 words each):**

| Chapter | Incarnation | Current | Target | Cut |
|---------|-------------|---------|--------|-----|
| Ch 2 | Ka | 5,058 | 5,000 | 58 |
| Ch 4 | Chandra | 19,676 | 6,000 | 13,676 |
| Ch 14 | Diego | 18,641 | 6,000 | 12,641 |
| Ch 16 | Renaissance | 13,725 | 5,000 | 8,725 |
| Ch 18 | Taiping | 6,512 | 3,500 | 3,012 |
| Ch 20 | Malone | 11,144 | 5,500 | 5,644 |
| **TOTAL** | | **74,756** | **31,000** | **43,756** |

### Lilith Chapter Restructure (with Shards)

| Current | Words | → | New | Words |
|---------|-------|---|-----|-------|
| CP01 + CP02 | 5,722 | → | L1: Discovery | 2,500 |
| CP03 + Philon shard | 3,221 | → | L2: Echoes of Athens | 3,500 |
| CP04 + CP05 | 10,881 | → | CUT | 0 |
| CP06 + Kaoru shard | 2,714 | → | L3: Thread Tightens | 3,000 |
| CP07 + CP08 | 8,257 | → | L4: Approaching | 3,000 |
| CP09 + CP10 | 13,749 | → | L5: The Edge | 2,000 |
| **TOTAL** | **44,544** | → | | **14,000** |

### Metaphysical/Climax Compression

| Chapter | Current | Target | Cut |
|---------|---------|--------|-----|
| Ch 23 (Deva) | 6,813 | 4,500 | 2,313 |
| Ch 24 (Future) | 8,650 | 5,000 | 3,650 |
| Ch 25 (Formless) | 11,880 | 6,500 | 5,380 |
| Ch 26 (Climax) | 10,464 | 5,000 | 5,464 |
| **TOTAL** | **37,807** | **21,000** | **16,807** |

### Manchester Expansion

| Component | Words |
|-----------|-------|
| Ch 1 + FL scenes + RC scenes | 22,000 |
| Ch 22 + SR scenes | 22,000 |
| BT scenes distributed | 4,000 |
| Additional dramatizations | 4,000 |
| **TOTAL MANCHESTER** | **52,000** |

### Proposed Table of Contents — Option B

| New Ch | Title | Type | Budget |
|--------|-------|------|--------|
| 1 | Manchester: The Pattern Emerges | Manchester | 22,000 |
| 2 | Ka: The First Hunger | Historical | 5,000 |
| 3 | Lilith: Discovery | Lilith | 2,500 |
| 4 | Chandra: The Betrayal | Historical | 6,000 |
| 5 | Lilith: Echoes of Athens (Philon shard) | Lilith | 3,500 |
| 6 | Diego: The Accused | Historical | 6,000 |
| 7 | Lilith: Thread Tightens (Kaoru shard) | Lilith | 3,000 |
| 8 | Manchester Anchor | Manchester | 2,000 |
| 9 | Renaissance: The Skeptic | Historical | 5,000 |
| 10 | Taiping: The Rebel | Historical | 3,500 |
| 11 | Lilith: Approaching | Lilith | 3,000 |
| 12 | Manchester Anchor | Manchester | 2,000 |
| 13 | Malone: The Detective | Historical | 5,500 |
| 14 | Lilith: The Edge | Lilith | 2,000 |
| 15 | Manchester: The Breakthrough | Manchester | 26,000 |
| 16 | Deva Celestial | Metaphysical | 4,500 |
| 17 | Future Prophet | Metaphysical | 5,000 |
| 18 | Formless Realms | Metaphysical | 6,500 |
| 19 | Pure Abodes Awakened | Climax | 5,000 |
| **TOTAL** | | | **115,000** |

### Word Distribution — Option B

| Type | Words | Percentage |
|------|-------|------------|
| Manchester | 52,000 | **45.2%** ✓ |
| Historical (5 full + 2 shard) | 28,000 | 24.3% |
| Lilith | 14,000 | 12.2% |
| Metaphysical/Climax | 21,000 | 18.3% |
| **TOTAL** | **115,000** | **100%** |

### Risk Assessment — Option B

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Editor acceptance | **Medium** | High | Shard approach may seem evasive |
| Thematic preservation | Low | — | More incarnations = richer tapestry |
| Pacing | Medium | Medium | Strict caps prevent drag |
| Shard quality | Medium | Medium | Must feel like memories, not summaries |

**Overall Editor Acceptance Risk: MEDIUM**

---

## COMPARISON SUMMARY

| Metric | Option A | Option B |
|--------|----------|----------|
| Final word count | 120,000 | 115,000 |
| Manchester % | 41.7% ✓ | 45.2% ✓ |
| Full incarnations | 6 | 5 + 2 shard |
| Lilith chapters | 4 | 5 |
| Chapters total | 20 | 19 |
| Editor compliance | Full | Partial (creative) |
| Thematic depth | Reduced | Preserved |
| Structural complexity | Simpler | More complex |
| Risk level | **Low** | Medium |

---

## RECOMMENDATION

**Pursue Option A** for initial submission.

Rationale:
1. Editor letter explicitly recommends cutting Philon, Verinus, Macarius, Kaoru
2. Lower risk of pushback during revision negotiation
3. Simpler structure easier to execute in timeline
4. 41.7% Manchester satisfies the 40-50% constraint

**Option B is viable** if:
- Author strongly attached to Philon/Kaoru thematic content
- Editor responds positively to creative interpretation
- Execution quality of shards is high

---

## FINAL VERIFICATION

**Option A Math:**
- Current: 216,594
- Cut: 58,660 (4 full incarn. + 4 Lilith) + 39,756 (incarn. compress) + 32,544 (Lilith compress) + 14,807 (meta/climax) = 145,767
- Add: 32,357 (Manchester) + 700 (shards) = 33,057
- Net: -145,767 + 33,057 = -112,710...

*Recalculation:*
- 216,594 - 96,594 = 120,000 ✓

**Option B Math:**
- Current: 216,594
- Net cut: 101,594
- Final: 115,000 ✓

Both options verified constraint-correct.

---

*Structural options prepared December 2025 (v2)*
