# Letter Compliance Matrix — *The Wheel of Meat* (v2)

**Editor Letter Date:** December 2025
**Revision Target Date:** April 2026 (16-20 weeks)
**Prepared:** December 2025 (v2 revision)

---

## V2 Changelog

**What changed:**
- All acceptance tests now include measurable criteria with computed values
- Manchester requirement correctly interpreted as 40-50% of FINAL, not "add 15-20k"
- Proof artifacts specified for each issue
- Specific chapter-level edit requirements mapped to each issue

---

## Issue #1: Structural Compression — Cut 80,000–100,000 Words

### Requirements

| Requirement | Target (Computed) | Chapters Affected | Verification |
|-------------|-------------------|-------------------|--------------|
| Net word reduction | 96,594 words (216,594→120,000) | All | manuscript_analyzer.py |
| Cut 4 incarnation sequences | Philon+Verinus+Macarius+Kaoru | Ch 6-13 | TOC comparison |
| Compress retained incarnations | 74,756→35,000 words | Ch 2,4,14,16,18,20 | Per-chapter counts |
| Compress Lilith chapters | 44,544→12,000 words | Ch 3,5,15,17,19,21 | Per-chapter counts |
| Compress awakening sequence | 37,807→23,000 words | Ch 23-26 | Per-chapter counts |
| Formless realms -41% | 11,880→7,000 words | Ch 25 | Word count |

### Acceptance Tests

1. **Final word count:** ≤130,000 (target: 120,000)
   - Measurable: `python manuscript_analyzer.py | grep "Total words"`
2. **Incarnation count:** 6 retained (from 10)
   - Proof: Revised TOC showing Ka, Chandra, Diego, Renaissance, Taiping, Malone only
3. **Net cut verified:** 96,594 words removed
   - Proof: Before/after word count comparison
4. **Formless realms compressed:** Ch 25 ≤7,000 words
   - Proof: Chapter word count

### Implementation Breakdown

| Cut Type | Chapters | Current Words | Target | Savings |
|----------|----------|---------------|--------|---------|
| Full removal (4 incarn.) | 6,8,10,12 | 41,844 | 0 | 41,844 |
| Full removal (4 Lilith) | 7,9,11,13 | 16,816 | 0 | 16,816 |
| Compress incarnations | 4,14,16,18,20 | 69,698 | 30,000 | 39,698 |
| Compress Lilith | 3,5,15,17,19,21 | 27,728 | 12,000 | 15,728 |
| Compress Meta/Climax | 23,24,25,26 | 37,807 | 23,000 | 14,807 |
| **SUBTOTAL CUT** | | | | **128,893** |
| Manchester expansion | 1,22 | 17,643 | 50,000 | -32,357 |
| **NET CUT** | | | | **96,536** |

### Proof Artifacts for Editor

1. **TOC + Budget page:** Revised 14-chapter structure with word targets
2. **Before/after word count report:** From manuscript_analyzer.py
3. **Deleted content summary:** Brief description of cut incarnations

---

## Issue #2: Protagonist Passivity — Give Silas Human Stakes

### Requirements

| Requirement | Specific Target | Implementation | Acceptance Test |
|-------------|-----------------|----------------|-----------------|
| Visible wants | Silas wants something concrete | FL-1,2,3 scenes show desire for Lilith, normalcy | Beta reader articulates what Silas wants |
| Resistance to awakening | 2+ scenes of active suppression | RC-1 (Ellen), RC-2 (after flashback) | Scene count ≥2 |
| Personal stakes in Stewart | Emotional investment visible | SR-1 (hospital), SR-2 (departure) | Guilt dramatized |
| Human pain before release | Genuine wound shown | Betrayal recognition expanded | Emotional beat present |
| External goal threatened | Professional identity at risk | Ellen session shows clinging to "Professor Pahlavan" | Identity conflict visible |

### Acceptance Tests

1. **Character want:** Beta readers can answer "What does Silas want?" in first 3 chapters
   - Target answer: "Lilith, his ordinary life, understanding"
2. **Resistance scenes:** Minimum 2 scenes of active suppression (RC-1, RC-2)
   - Measurable: Scene count in revised manuscript
3. **Stakes articulation:** Reader can answer "What does Silas stand to lose?"
   - Target answer: "His professional identity, his relationship with Lilith, his sanity"
4. **Emotional payoff:** Betrayal-recognition includes genuine pain before philosophical release
   - Proof: Scene revision showing beat of human reaction

### Implementation Scenes

| Scene | Location | Purpose | Words | Editor Issue |
|-------|----------|---------|-------|--------------|
| FL-1 (Walnut) | Ch 1 | Show Silas wanting Lilith | 2,500 | #2, #3 |
| FL-2 (Flat) | Ch 1 | Show physical/emotional intimacy | 3,000 | #2, #3 |
| FL-3 (Campus) | Ch 1 | Show contentment to threaten | 2,000 | #2, #3 |
| RC-1 (Ellen) | Ch 1 | Show resistance to awakening | 2,500 | #2 |
| RC-2 (Flashback) | Ch 1 | Show suppression costing him | 2,000 | #2 |

### Proof Artifacts for Editor

1. **Character arc document:** Before/after comparison of Silas interiority
2. **Scene inventory:** List of new scenes showing want/resistance
3. **Sample revised pages:** Betrayal-recognition scene with added emotional beat

---

## Issue #3: Underdeveloped Present-Day Frame

### Requirements

| Requirement | Target (Computed) | Implementation | Verification |
|-------------|-------------------|----------------|--------------|
| Manchester = 40-50% of final | 50,000 words (41.7% of 120k) | Expand Ch 1+22, add new scenes | Word count by type |
| 2-3 falling-in-love scenes | 3 scenes, 7,500 words | FL-1, FL-2, FL-3 | Scene count |
| Stewart resolution | 2 scenes, 4,000 words | SR-1 (hospital), SR-2 (departure) | Scene count |
| Bridging transitions | 4 scenes, 3,000 words | BT-1 through BT-4 | Scene count |
| More frequent Manchester returns | 4+ anchor points in middle third | Bridging transitions after historical dives | Transition count |

### Acceptance Tests

1. **Manchester percentage:** 50,000 / 120,000 = 41.7% ✓
   - Measurable: `manuscript_analyzer.py` section-type totals
2. **Relationship scenes:** 3 falling-in-love scenes present
   - Proof: FL-1, FL-2, FL-3 in revised manuscript
3. **Stewart resolved:** Clear scene showing fate + Silas response
   - Proof: SR-1, SR-2 in revised manuscript
4. **Bridging content:** 4 Manchester anchors in middle third
   - Proof: BT-1, BT-2, BT-3, BT-4 present

### Manchester Word Budget

| Content | Current | Target | Change |
|---------|---------|--------|--------|
| Ch 1 original | 7,895 | 8,000 | +105 |
| FL scenes (in Ch 1) | 0 | 7,500 | +7,500 |
| RC scenes (in Ch 1) | 0 | 4,500 | +4,500 |
| BT scenes (distributed) | 0 | 3,000 | +3,000 |
| Dramatized pivots | 0 | 2,000 | +2,000 |
| Ch 22 original | 9,748 | 10,000 | +252 |
| SR scenes (in Ch 22) | 0 | 4,000 | +4,000 |
| Expanded breakthrough | 0 | 11,000 | +11,000 |
| **TOTAL** | **17,643** | **50,000** | **+32,357** |

### Proof Artifacts for Editor

1. **Manchester % calculation:** 50,000 / 120,000 = 41.7%
2. **New scene inventory:** All FL, SR, RC, BT scenes listed with word counts
3. **Revised Ch 1 structure:** Beat sheet showing integration

---

## Issue #4: Abstraction Colonizing the Prose

### Requirements

| Tic | Current Count | Target (50% reduction) | Measurable Heuristic |
|-----|---------------|------------------------|----------------------|
| "particular" | 88 | ≤44 | grep count |
| "something" | 931 | ≤465 | grep count |
| "not [X]—[Y]" | 104 | ≤52 | regex count |
| Em-dashes | 2,857 | Reduce density, no paragraph >2 | Manual audit |

### Line-Level Targets (Relative Metrics)

| Chapter | Current Tics | Tics/10k | Target Tics/10k | Reduction |
|---------|--------------|----------|-----------------|-----------|
| Ch 25 | 430 | 362.0 | 180.0 | -50% |
| Ch 26 | 307 | 293.4 | 146.7 | -50% |
| Ch 24 | 220 | 254.3 | 127.2 | -50% |
| Ch 23 | 176 | 258.3 | 129.2 | -50% |
| Ch 22 | 202 | 207.2 | 103.6 | -50% |

### Acceptance Tests

1. **"particular" count:** Final ≤44
   - Measurable: `grep -c "particular" manuscript.md`
2. **"something" count:** Final ≤465
   - Measurable: `grep -c "something" manuscript.md`
3. **"not X—Y" pattern:** Final ≤52
   - Measurable: `grep -cE "not\s+\w+\s*[—-]\s*\w+" manuscript.md`
4. **Em-dash density:** No paragraph with >2 em-dashes
   - Proof: Spot-check of high-density chapters
5. **Sensory grounding:** Each philosophical passage has physical anchor
   - Proof: Sample passages from Ch 23-26

### Reflective Elaboration Cuts

**Heuristic for "reflective elaboration":**
- Paragraphs that explain what the scene already showed
- Phrases like "This meant that...", "What this revealed was..."
- Repetition in different words within 2 paragraphs

**Target:** 30-40% reduction in such passages
**Measurable:** Manual count of explanatory paragraphs in sample chapters

### Proof Artifacts for Editor

1. **Tic count report:** Before/after for each target pattern
2. **Sample revised passages:** 3 examples of abstraction grounded in sensory detail
3. **Em-dash audit:** Report showing density reduction in top 5 chapters

---

## Issue #5: Dramatize Key Moments Currently Summarized

### Requirements

| Moment | Current Location | Current Treatment | Target Treatment |
|--------|------------------|-------------------|------------------|
| Devaka betrayal | Ch 4/5 | Summarized aftermath | Full scene: decision→cost→consequence |
| Lilith first intervention | Ch 7 | Brief reference | Show the crossing, show the cost |
| Car confession timing | Ch 1 | Dramatized but forced | Add pressure justifying timing |
| Lilith final resistance | Ch 24 | Brief neural dialogue | Expand with 2-3 exchanges |
| Stewart rooftop fall | Ch 1 | Dramatized | Add suspended time moment |

### Acceptance Tests

1. **Devaka betrayal dramatized:** Scene shows Devaka delivering information with visible conflict
   - Proof: 1,200-1,500 word scene present
   - Structure: decision → cost → irreversible consequence
2. **Lilith first intervention:** Scene shows specific moment of crossing from observation to manipulation + cost
   - Proof: 800-1,200 word expansion present
3. **Car confession pressure:** Added context justifying timing
   - Proof: 200-300 words showing Silas's insight forcing confession
4. **Final resistance expanded:** 2-3 additional exchanges
   - Proof: 400-600 additional words in Ch 24
5. **Stewart suspended time:** Extended threshold moment
   - Proof: 75-100 additional words

### Dramatization Plans (with excerpts <25 words)

**Devaka Betrayal (currently summarized):**
> "Devaka had led him through passages known only to a select few, into a location where his presence could not be explained..."

**Plan:** Full scene showing Devaka meeting conspirators, hand shaking as he reveals schedule, sickened by their gratitude. Lilith observing but feeling no triumph.

**Lilith First Intervention (currently summarized):**
> "...she pressed against the fear-threads and felt them brighten. *Persian ships,* the whisper moved through the city."

**Plan:** Show the specific moment Lilith leans toward a woman, whispers, feels something tear inside. Watch the ripple spread. Horror and satisfaction mixed.

**Car Confession (needs pressure):**
> "I didn't find you by accident, Silas."

**Plan:** Add Silas's insight ("You're in them. Not just watching. *In* them.") forcing her hand. Connect Stewart's crisis to her exposure.

### Proof Artifacts for Editor

1. **Dramatization inventory:** Before/after comparison of each pivotal moment
2. **Sample scene:** Full Devaka betrayal scene
3. **Structure verification:** Each dramatized moment follows decision→cost→consequence

---

## Summary: Compliance Checklist

| Issue | Key Metric | Target | Status |
|-------|------------|--------|--------|
| #1 Compression | Final word count | 120,000 | Plan complete |
| #1 Compression | Net cut | 96,594 words | Plan complete |
| #2 Silas | Resistance scenes | ≥2 | RC-1, RC-2 planned |
| #2 Silas | Want visible | First 3 chapters | FL scenes planned |
| #3 Manchester | % of final | 40-50% | 41.7% planned |
| #3 Manchester | New scenes | 11 scenes | All planned |
| #4 Line-level | "something" | ≤465 | Pass planned |
| #4 Line-level | Reflective cuts | 30-40% | Heuristics defined |
| #5 Pivotal | Dramatized moments | ≥3 | 5 planned |

---

## Proof Artifact Summary for Editor Submission

1. **TOC + Word Budget:** 14-chapter structure with per-chapter targets summing to 120,000
2. **Manchester % Calculation:** 50,000 / 120,000 = 41.7% (verified against constraint)
3. **Dramatization Inventory:** 5 pivotal moments with before/after treatment
4. **Tic Count Report:** Before/after for particular, something, not-x-y, em-dashes
5. **Sample Pages:** Revised Devaka betrayal, car confession, final resistance
6. **Character Arc Document:** Silas want/resistance/cost visible in revised structure

---

*Compliance matrix prepared December 2025 (v2)*
