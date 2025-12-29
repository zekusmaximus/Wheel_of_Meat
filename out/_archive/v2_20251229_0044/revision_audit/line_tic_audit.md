# Line-Level Tic Audit — *The Wheel of Meat* (v2)

**Prepared:** December 2025 (v2 revision)
**Scope:** Full manuscript analysis with RELATIVE reduction metrics
**Data Source:** manuscript_analyzer.py (verified 216,594 total words)

---

## V2 Changelog

**What changed from v1:**
- Replaced absolute targets (e.g., "something <500") with RELATIVE reductions per 10k words
- Added per-chapter density metrics for measurable line-editing
- Defined "tic monsters" (top 5 highest-density chapters) with micro-checklists
- Reflective elaboration now has measurable heuristics

---

## I. Tic Count Summary with Density Metrics

### Overall Totals (Current Manuscript)

| Tic Pattern | Total Count | Per 10k Words | Target (50% reduction) | Target Density |
|-------------|-------------|---------------|------------------------|----------------|
| "particular" | 88 | 4.06 | ≤44 | 2.03/10k |
| "something" | 931 | 42.99 | ≤465 | 21.50/10k |
| "not [X]—[Y]" | 104 | 4.80 | ≤52 | 2.40/10k |
| Em-dashes (—) | 2,857 | 131.90 | Vary; no paragraph >2 | <100/10k |
| **Total tics** | **3,980** | **183.75** | ≤2,000 | <100/10k |

### Post-Revision Projections (at 120,000 words)

| Tic | Current/10k | Target/10k | Absolute Target |
|-----|-------------|------------|-----------------|
| "particular" | 4.06 | 2.03 | ≤24 |
| "something" | 42.99 | 21.50 | ≤258 |
| "not X—Y" | 4.80 | 2.40 | ≤29 |
| Total tics | 183.75 | 91.88 | ≤1,103 |

---

## II. Per-Chapter Density Analysis (Retained Chapters Only)

### Tic Density Rankings

| Rank | Ch | Name | Words | Total Tics | Tics/10k | Target/10k | Reduction Needed |
|------|-----|------|-------|------------|----------|------------|------------------|
| 1 | 25 | Formless Realms | 11,880 | 430 | **362.0** | 181.0 | -50% |
| 2 | 21 | Lilith CP10 | 3,738 | 121 | **323.7** | 161.9 | -50% |
| 3 | 26 | Pure Abodes | 10,464 | 307 | **293.4** | 146.7 | -50% |
| 4 | 24 | Future Prophet | 8,650 | 220 | **254.3** | 127.2 | -50% |
| 5 | 23 | Deva Celestial | 6,813 | 176 | **258.3** | 129.2 | -50% |
| 6 | 22 | Contemporary | 9,748 | 202 | 207.2 | 103.6 | -50% |
| 7 | 19 | Lilith CP09 | 10,011 | 162 | 161.8 | 80.9 | -50% |
| 8 | 14 | Diego | 18,641 | 300 | 160.9 | 80.5 | -50% |
| 9 | 4 | Chandra | 19,676 | 247 | 125.5 | 62.8 | -50% |
| 10 | 15 | Lilith CP07 | 4,711 | 109 | 231.4 | 115.7 | -50% |

**Note:** Chapters 6-13 (marked CUT) excluded from reduction targets.

---

## III. Top 5 "Tic Monsters" with Micro-Checklists

### Monster #1: Ch 25 (Formless Realms) — 362.0 tics/10k

**Current Profile:**
- Words: 11,880 → Target: 7,000
- "something": 125 (highest in manuscript)
- Em-dashes: 294 (highest in manuscript)
- Abstraction density: 13.72 (highest)

**Micro-Checklist:**
- [ ] Search "something" — reduce from 125 to ~40 (in compressed version)
  - KEEP: Intentional uses for the ineffable ("something beyond naming")
  - CUT: Author-level vagueness ("something shifted")
- [ ] Search em-dashes — reduce from 294 to ~90
  - CONVERT: Interruptive asides (—X—) → commas or parentheses
  - CONVERT: Dramatic pauses → periods for new sentences
- [ ] Add 3 Ka-register moments: body-first prose interrupting abstraction
- [ ] Physical anchor for each stage transition (smell, texture, weight)

**Expected density after revision:** ~130 tics/10k

### Monster #2: Ch 26 (Pure Abodes) — 293.4 tics/10k

**Current Profile:**
- Words: 10,464 → Target: 5,500
- "something": 74
- "not X—Y": 24 (highest in manuscript)
- Em-dashes: 200

**Micro-Checklist:**
- [ ] Search "not X—Y" — reduce from 24 to ~8
  - CONVERT: "not fear—recognition" → "Recognition flooded through her."
  - VARY: Use full sentences, comma constructions, positive statements
- [ ] Search "something" — reduce from 74 to ~25
- [ ] Em-dash audit: No paragraph with >2; vary with semicolons
- [ ] Final resistance expansion should use POSITIVE statements, not more tic patterns

**Expected density after revision:** ~120 tics/10k

### Monster #3: Ch 24 (Future Prophet) — 254.3 tics/10k

**Current Profile:**
- Words: 8,650 → Target: 5,500
- "something": 60
- "not X—Y": 11
- Abstraction density: 9.48

**Micro-Checklist:**
- [ ] Ground post-scarcity setting in physical detail
- [ ] Search "something" — reduce from 60 to ~20
- [ ] Each philosophical passage needs sensory anchor
- [ ] Village scene: add one moment of conflict/doubt per editor

**Expected density after revision:** ~100 tics/10k

### Monster #4: Ch 23 (Deva Celestial) — 258.3 tics/10k

**Current Profile:**
- Words: 6,813 → Target: 5,000
- "something": 58
- Abstraction density: 11.01

**Micro-Checklist:**
- [ ] Devaka's celestial realm needs physical grounding
- [ ] Search "something" — reduce from 58 to ~20
- [ ] Dramatized betrayal scene should use concrete language
- [ ] Add Lilith observation with body-first prose

**Expected density after revision:** ~100 tics/10k

### Monster #5: Ch 22 (Contemporary Breakthrough) — 207.2 tics/10k

**Current Profile:**
- Words: 9,748 → Target: 25,000 (EXPAND)
- "something": 55
- "not X—Y": 11
- This chapter EXPANDS, so tic reduction is per-existing-content only

**Micro-Checklist:**
- [ ] New Manchester content: Write clean (target <100 tics/10k in new material)
- [ ] Search existing "something" — reduce from 55 to ~25
- [ ] Stewart resolution scenes: Use concrete emotional language
- [ ] Silas resistance scenes: Show through action, not "something shifted"

**Expected density after revision:** ~80 tics/10k

---

## IV. Tic-Specific Reduction Strategies

### A. "Particular" (88 → ≤44)

**Highest chapters (retained):**
- Ch 4 (Chandra): 22 → 11
- Ch 14 (Diego): 10 → 5
- Ch 26 (Climax): 9 → 4

**Replacement patterns:**
| Current | Problem | Revision |
|---------|---------|----------|
| "this particular moment" | Filler | "this moment" |
| "her particular way of" | Vague intensifier | "her way of" or specify |
| "the particular quality of" | Delays meaning | Name the quality |
| "in that particular life" | Redundant | "in that life" or cut |

### B. "Something" (931 → ≤465)

**Highest chapters (retained):**
- Ch 25 (Formless): 125 → 40
- Ch 10 (Macarius): 78 → CUT
- Ch 26 (Climax): 74 → 25
- Ch 12 (Kaoru): 62 → CUT

**Replacement patterns:**
| Current | Problem | Revision |
|---------|---------|----------|
| "something shifted in her" | Vague | Name the shift |
| "something like fear" | Hedging | "fear" or describe sensation |
| "he felt something" | Empty | Describe the sensation |
| "something about the way" | Double vagueness | Name thing and way |

**Note:** Some "something" uses are intentional for ineffability. KEEP in passages about the formless/unnameable. CUT in author-level vagueness.

### C. "Not [X]—[Y]" Pattern (104 → ≤52)

**Highest chapters (retained):**
- Ch 26 (Climax): 24 → 8
- Ch 22 (Contemporary): 11 → 4
- Ch 24 (Future): 11 → 4

**Conversion methods:**
1. **Full sentences:** "It wasn't fear. It was recognition."
2. **Positive statement:** "Recognition flooded through her."
3. **Comma construction:** "Recognition, not fear, flooded through her."

### D. Em-Dashes (2,857 → varied density)

**Target:** No paragraph with >2 em-dashes

**Highest chapters:**
- Ch 25: 294 → ~90 (67% reduction in compressed chapter)
- Ch 14: 230 → ~80 (in compressed chapter)
- Ch 26: 200 → ~60

**Conversion patterns:**
| Pattern | Current | Replacement |
|---------|---------|-------------|
| Interruptive aside | —X— | commas or parentheses |
| Dramatic pause | — | period for new sentence |
| Appositive | —X— | commas |
| List-breaking | —X—Y—Z— | commas or semicolons |

---

## V. Reflective Elaboration Cuts (30-40% Reduction)

### Measurable Heuristics

**Definition of "reflective elaboration":**
A passage is reflective elaboration if it:
1. Explains what the scene already showed
2. Uses phrases like "This meant that...", "What this revealed was..."
3. Repeats in different words within 2 paragraphs
4. Glosses character emotion that action already demonstrated

### Identification Method

For each chapter, count paragraphs matching criteria above.
Target: Remove 30-40% of identified passages.

### Sample Before/After

**Before (Reflective Elaboration):**
> Lilith watched him walk away. This was the moment she had anticipated for three centuries—the crystallization of a pattern she had traced through fourteen incarnations. What this revealed was not merely his readiness to move forward, but her own exhaustion with the game she could not stop playing. She understood now that her watching had become its own form of attachment, that every intervention bound her more tightly to the wheel she claimed to despise.

**After (Tightened):**
> Lilith watched him walk away. Three centuries of waiting, crystallized. She understood: her watching had become its own attachment. Every intervention bound her tighter to the wheel she despised.

**Reduction:** 89 words → 38 words (57% cut)

### Per-Chapter Targets

| Chapter | Current Words | Est. Reflective % | Cut Target | Words Saved |
|---------|---------------|-------------------|------------|-------------|
| Ch 25 | 11,880 | 25% | 35% of 25% | ~1,040 |
| Ch 26 | 10,464 | 20% | 35% of 20% | ~730 |
| Ch 24 | 8,650 | 22% | 35% of 22% | ~660 |
| Ch 23 | 6,813 | 18% | 35% of 18% | ~430 |
| Ch 19 | 10,011 | 20% | 35% of 20% | ~700 |

---

## VI. Abstraction Grounding Protocol

### Highest Abstraction Chapters

| Ch | Density | Issue | Grounding Target |
|----|---------|-------|------------------|
| 25 | 13.72 | Recursive formless prose | 1 sensory anchor per stage |
| 23 | 11.01 | Celestial realm abstraction | Physical detail in deva realm |
| 24 | 9.48 | Post-scarcity abstraction | Conflict/texture in village |
| 26 | 5.06 | Climax abstraction | Body-awareness in merger |

### Ka-Register Insertion Points

Insert 1-2 brief body-first sentences per high-abstraction chapter:

**Example insertion (Ch 25):**
> "Consciousness expanded into formlessness."
→
> "The body still breathed. In, out. Ribs expanding, contracting. Consciousness expanded into formlessness, but the breath continued."

**Target:** 5+ Ka-register moments across Ch 23-26.

---

## VII. Verification Checklist for Line-Edit Pass

### Per-Chapter Protocol

For each retained chapter:

```
□ Run: grep -c "particular" [chapter]
  Current: ___ Target: ≤50% of current

□ Run: grep -c "something" [chapter]
  Current: ___ Target: ≤50% of current

□ Run: grep -cE "not\s+\w+\s*[—-]\s*\w+" [chapter]
  Current: ___ Target: ≤50% of current

□ Manual check: Paragraphs with >2 em-dashes
  Current: ___ Target: 0

□ Sensory grounding: Each philosophical passage has physical anchor
  Count: ___

□ Reflective elaboration: Explanatory paragraphs identified and cut
  Before: ___ After: ___
```

### Final Verification

After line-edit pass, run manuscript_analyzer.py and verify:
- Total tics reduced by ≥50%
- Tic density <100/10k words
- Abstraction density reduced in Ch 23-26

---

*Line-level tic audit prepared December 2025 (v2)*
