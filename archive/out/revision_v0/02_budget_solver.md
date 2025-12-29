# Budget Solver

## Baseline Data (Source: analysis_data.json verified 2025-12-29)

**Formula basis for all calculations below:**
```
Baseline total = 216,594 words (verified by manuscript analyzer)
Manchester baseline = Ch1 (7,895) + Ch22 (9,748) = 17,643 words
Cut candidates = Ch6 Philon (10,202) + Ch8 Verinus (9,405) + Ch10 Macarius (13,777) + Ch12 Kaoru (8,460) = 41,844 words
```

| Metric | Value | Derivation |
|--------|-------|------------|
| Current total words | 216,594 | From analyzer |
| Current Manchester words | 17,643 | 7,895 + 9,748 |
| Current Manchester % | 8.15% | 17,643 / 216,594 |
| Target final | 120,000 (range: 110,000–130,000) | C1 constraint |
| Required net cut | 96,594 (range: 86,594–106,594) | 216,594 - 120,000 |
| Required Manchester % | 40–50% | C2 constraint |

---

## Budget A: Letter-Faithful (4 Incarnation Cuts)

### Strategy
Cut exactly 4 incarnations per editor recommendation: Philon, Verinus, Macarius, Kaoru.
Compress associated Lilith tracking chapters.
Expand Manchester aggressively.
Keep Renaissance Skeptic and Taiping (compressed).

### Per-Chapter Budget

| Ch | Name | Type | Current | Target | Change |
|----|------|------|---------|--------|--------|
| 1 | Contemporary Manchester | Manchester | 7,895 | 24,000 | +16,105 |
| 2 | Prehistoric Ka | Historical | 5,058 | 4,500 | -558 |
| 3 | Lilith CP01 | Lilith | 3,049 | 2,200 | -849 |
| 4 | Mauryan Chandra | Historical | 19,676 | 12,000 | -7,676 |
| 5 | Lilith CP02 | Lilith | 2,673 | 2,000 | -673 |
| 6 | Athens Philosopher (Philon) | Historical | 10,202 | 0 | -10,202 |
| 7 | Lilith CP03 | Lilith | 3,221 | 500 | -2,721 |
| 8 | Rome Investigator (Verinus) | Historical | 9,405 | 0 | -9,405 |
| 9 | Lilith CP04 | Lilith | 5,998 | 800 | -5,198 |
| 10 | Egypt Hermit (Macarius) | Historical | 13,777 | 0 | -13,777 |
| 11 | Lilith CP05 | Lilith | 4,883 | 800 | -4,083 |
| 12 | Heian Lover (Kaoru) | Historical | 8,460 | 0 | -8,460 |
| 13 | Lilith CP06 | Lilith | 2,714 | 500 | -2,214 |
| 14 | Inquisition Accused (Diego) | Historical | 18,641 | 11,000 | -7,641 |
| 15 | Lilith CP07 | Lilith | 4,711 | 3,200 | -1,511 |
| 16 | Renaissance Skeptic | Historical | 13,725 | 6,000 | -7,725 |
| 17 | Lilith CP08 | Lilith | 3,546 | 2,500 | -1,046 |
| 18 | Taiping Rebel | Historical | 6,512 | 4,000 | -2,512 |
| 19 | Lilith CP09 | Lilith | 10,011 | 5,500 | -4,511 |
| 20 | Noir Detective (Malone) | Historical | 11,144 | 7,500 | -3,644 |
| 21 | Lilith CP10 | Lilith | 3,738 | 2,500 | -1,238 |
| 22 | Contemporary Breakthrough | Manchester | 9,748 | 24,000 | +14,252 |
| 23 | Deva Celestial | Historical/Metaphysical | 6,813 | 5,000 | -1,813 |
| 24 | Future Prophet | Historical/Future | 8,650 | 5,500 | -3,150 |
| 25 | Space Explorer / Formless Realms | Metaphysical | 11,880 | 7,000 | -4,880 |
| 26 | Pure Abodes Awakened | Climax | 10,464 | 7,000 | -3,464 |
| **TOTAL** | | | **216,594** | **118,000** | **-98,594** |

### Budget A Validation

| Type | Current | Target | Target % |
|------|---------|--------|----------|
| Manchester | 17,643 | 48,000 | 40.68% |
| Historical (kept) | 64,840 | 45,000 | 38.14% |
| Lilith | 44,544 | 20,500 | 17.37% |
| Metaphysical | 11,880 | 7,000 | 5.93% |
| Climax | 10,464 | 7,000 | 5.93% |
| Historical/Metaphysical | 6,813 | 5,000 | 4.24% |
| Historical/Future | 8,650 | 5,500 | 4.66% |
| CUT (Philon, Verinus, Macarius, Kaoru) | 41,844 | 0 | 0% |

**Note**: Target sums to 138,000 - too high. Need revision.

### Budget A Revised

Let me recalculate to hit exactly 120,000:

| Type | Target Words | Target % |
|------|-------------|----------|
| Manchester | 48,000 | 40.00% |
| Historical (kept: Ka, Chandra, Diego, Renaissance, Taiping, Malone) | 38,500 | 32.08% |
| Lilith (6 active + 4 compressed) | 16,000 | 13.33% |
| Final Sequence (Ch 23-26) | 17,500 | 14.58% |
| CUT (4 incarnations) | 0 | 0% |
| **TOTAL** | **120,000** | **100%** |

**Manchester calculation**: 48,000 / 120,000 = 40.00% ✓

### Budget A Final Per-Chapter

| Ch | Name | Type | Current | Target | Change |
|----|------|------|---------|--------|--------|
| 1 | Contemporary Manchester | Manchester | 7,895 | 24,000 | +16,105 |
| 2 | Prehistoric Ka | Historical | 5,058 | 4,000 | -1,058 |
| 3 | Lilith CP01 | Lilith | 3,049 | 2,000 | -1,049 |
| 4 | Mauryan Chandra | Historical | 19,676 | 11,000 | -8,676 |
| 5 | Lilith CP02 | Lilith | 2,673 | 1,800 | -873 |
| 6 | Philon (CUT) | — | 10,202 | 0 | -10,202 |
| 7 | Lilith CP03 (compress) | Lilith | 3,221 | 400 | -2,821 |
| 8 | Verinus (CUT) | — | 9,405 | 0 | -9,405 |
| 9 | Lilith CP04 (compress) | Lilith | 5,998 | 600 | -5,398 |
| 10 | Macarius (CUT) | — | 13,777 | 0 | -13,777 |
| 11 | Lilith CP05 (compress) | Lilith | 4,883 | 600 | -4,283 |
| 12 | Kaoru (CUT) | — | 8,460 | 0 | -8,460 |
| 13 | Lilith CP06 (compress) | Lilith | 2,714 | 400 | -2,314 |
| 14 | Inquisition Accused (Diego) | Historical | 18,641 | 10,000 | -8,641 |
| 15 | Lilith CP07 | Lilith | 4,711 | 3,000 | -1,711 |
| 16 | Renaissance Skeptic | Historical | 13,725 | 5,500 | -8,225 |
| 17 | Lilith CP08 | Lilith | 3,546 | 2,200 | -1,346 |
| 18 | Taiping Rebel | Historical | 6,512 | 4,000 | -2,512 |
| 19 | Lilith CP09 | Lilith | 10,011 | 4,000 | -6,011 |
| 20 | Noir Detective (Malone) | Historical | 11,144 | 4,000 | -7,144 |
| 21 | Lilith CP10 | Lilith | 3,738 | 1,000 | -2,738 |
| 22 | Contemporary Breakthrough | Manchester | 9,748 | 24,000 | +14,252 |
| 23 | Deva Celestial | Historical/Metaphysical | 6,813 | 4,500 | -2,313 |
| 24 | Future Prophet | Historical/Future | 8,650 | 4,500 | -4,150 |
| 25 | Space Explorer / Formless Realms | Metaphysical | 11,880 | 4,500 | -7,380 |
| 26 | Pure Abodes Awakened | Climax | 10,464 | 4,000 | -6,464 |
| **TOTAL** | | | **216,594** | **120,000** | **-96,594** |

### Budget A Constraint Check

| Constraint | Formula | Value | Range | Status |
|------------|---------|-------|-------|--------|
| C1: Final words | total | 120,000 | 110,000–130,000 | **PASS** |
| C2: Manchester % | 48,000 / 120,000 | 40.00% | 40–50% | **PASS** |
| C3: Net cut | 216,594 - 120,000 | 96,594 | 80,000–100,000 | **PASS** |
| C4: Incarnations cut | count | 4 | 3–4 | **PASS** |
| C5: Pivotal scenes | TBD | ≥3 | ≥3 | PENDING |
| C6: Reflective reduction | TBD | 30–40% | 30–40% | PENDING |
| C7: Tic reduction | TBD | ~50% | ~50% | PENDING |

---

## Budget B: Shard-Preserving (3 Incarnation Cuts)

### Strategy
Cut only 3 incarnations (minimum): Philon, Verinus, Macarius.
Keep Kaoru compressed as "Heian flashback" (~2,000 words).
Preserve more historical texture at cost of tighter line edits.

### Per-Chapter Budget

| Ch | Name | Type | Current | Target | Change |
|----|------|------|---------|--------|--------|
| 1 | Contemporary Manchester | Manchester | 7,895 | 26,000 | +18,105 |
| 2 | Prehistoric Ka | Historical | 5,058 | 4,500 | -558 |
| 3 | Lilith CP01 | Lilith | 3,049 | 2,000 | -1,049 |
| 4 | Mauryan Chandra | Historical | 19,676 | 10,000 | -9,676 |
| 5 | Lilith CP02 | Lilith | 2,673 | 1,700 | -973 |
| 6 | Philon (CUT) | — | 10,202 | 0 | -10,202 |
| 7 | Lilith CP03 (compress) | Lilith | 3,221 | 400 | -2,821 |
| 8 | Verinus (CUT) | — | 9,405 | 0 | -9,405 |
| 9 | Lilith CP04 (compress) | Lilith | 5,998 | 500 | -5,498 |
| 10 | Macarius (CUT) | — | 13,777 | 0 | -13,777 |
| 11 | Lilith CP05 (compress) | Lilith | 4,883 | 500 | -4,383 |
| 12 | Heian Lover (Kaoru) — flashback | Historical | 8,460 | 2,000 | -6,460 |
| 13 | Lilith CP06 | Lilith | 2,714 | 1,200 | -1,514 |
| 14 | Inquisition Accused (Diego) | Historical | 18,641 | 9,000 | -9,641 |
| 15 | Lilith CP07 | Lilith | 4,711 | 2,800 | -1,911 |
| 16 | Renaissance Skeptic | Historical | 13,725 | 5,000 | -8,725 |
| 17 | Lilith CP08 | Lilith | 3,546 | 2,100 | -1,446 |
| 18 | Taiping Rebel | Historical | 6,512 | 3,500 | -3,012 |
| 19 | Lilith CP09 | Lilith | 10,011 | 3,800 | -6,211 |
| 20 | Noir Detective (Malone) | Historical | 11,144 | 3,500 | -7,644 |
| 21 | Lilith CP10 | Lilith | 3,738 | 1,000 | -2,738 |
| 22 | Contemporary Breakthrough | Manchester | 9,748 | 26,000 | +16,252 |
| 23 | Deva Celestial | Historical/Metaphysical | 6,813 | 4,000 | -2,813 |
| 24 | Future Prophet | Historical/Future | 8,650 | 4,000 | -4,650 |
| 25 | Space Explorer / Formless Realms | Metaphysical | 11,880 | 4,000 | -7,880 |
| 26 | Pure Abodes Awakened | Climax | 10,464 | 3,500 | -6,964 |
| **TOTAL** | | | **216,594** | **121,000** | **-95,594** |

### Budget B Type Totals

| Type | Target Words | Target % |
|------|-------------|----------|
| Manchester | 52,000 | 42.98% |
| Historical (kept) | 41,500 | 34.30% |
| Lilith | 16,000 | 13.22% |
| Final Sequence (Ch 23-26) | 15,500 | 12.81% |
| CUT | 0 | 0% |
| **TOTAL** | **121,000** | **103.31%** |

**Adjustment needed**: Totals to 125,000 — recalculating...

### Budget B Revised

| Ch | Name | Current | Target |
|----|------|---------|--------|
| 1 | Manchester | 7,895 | 25,000 |
| 2 | Ka | 5,058 | 4,000 |
| 3 | Lilith CP01 | 3,049 | 1,800 |
| 4 | Chandra | 19,676 | 9,500 |
| 5 | Lilith CP02 | 2,673 | 1,500 |
| 6 | Philon (CUT) | 10,202 | 0 |
| 7 | Lilith CP03 | 3,221 | 350 |
| 8 | Verinus (CUT) | 9,405 | 0 |
| 9 | Lilith CP04 | 5,998 | 450 |
| 10 | Macarius (CUT) | 13,777 | 0 |
| 11 | Lilith CP05 | 4,883 | 450 |
| 12 | Kaoru (flashback) | 8,460 | 1,800 |
| 13 | Lilith CP06 | 2,714 | 1,000 |
| 14 | Diego | 18,641 | 8,500 |
| 15 | Lilith CP07 | 4,711 | 2,500 |
| 16 | Renaissance | 13,725 | 4,500 |
| 17 | Lilith CP08 | 3,546 | 1,900 |
| 18 | Taiping | 6,512 | 3,200 |
| 19 | Lilith CP09 | 10,011 | 3,500 |
| 20 | Malone | 11,144 | 3,200 |
| 21 | Lilith CP10 | 3,738 | 900 |
| 22 | Manchester | 9,748 | 25,000 |
| 23 | Deva | 6,813 | 3,800 |
| 24 | Future | 8,650 | 3,800 |
| 25 | Formless | 11,880 | 3,800 |
| 26 | Climax | 10,464 | 3,350 |
| **TOTAL** | | **216,594** | **114,000** |

### Budget B Constraint Check

| Constraint | Formula | Value | Range | Status |
|------------|---------|-------|-------|--------|
| C1: Final words | total | 114,000 | 110,000–130,000 | **PASS** |
| C2: Manchester % | 50,000 / 114,000 | 43.86% | 40–50% | **PASS** |
| C3: Net cut | 216,594 - 114,000 | 102,594 | 80,000–100,000 | **FAIL** (exceeds by 2,594) |
| C4: Incarnations cut | count | 3 | 3–4 | **PASS** |
| C5: Pivotal scenes | TBD | ≥3 | ≥3 | PENDING |
| C6: Reflective reduction | TBD | 30–40% | 30–40% | PENDING |
| C7: Tic reduction | TBD | ~50% | ~50% | PENDING |

**Budget B fails C3** — net cut of 102,594 exceeds 100,000 maximum.

---

## Budget C: Balanced (4 Cuts, Higher Total)

### Strategy
Cut 4 incarnations but target higher final word count (125,000) to reduce net cut.

### Per-Chapter Budget

| Ch | Name | Current | Target |
|----|------|---------|--------|
| 1 | Manchester | 7,895 | 25,000 |
| 2 | Ka | 5,058 | 4,500 |
| 3 | Lilith CP01 | 3,049 | 2,200 |
| 4 | Chandra | 19,676 | 12,000 |
| 5 | Lilith CP02 | 2,673 | 2,000 |
| 6 | Philon (CUT) | 10,202 | 0 |
| 7 | Lilith CP03 | 3,221 | 500 |
| 8 | Verinus (CUT) | 9,405 | 0 |
| 9 | Lilith CP04 | 5,998 | 700 |
| 10 | Macarius (CUT) | 13,777 | 0 |
| 11 | Lilith CP05 | 4,883 | 700 |
| 12 | Kaoru (CUT) | 8,460 | 0 |
| 13 | Lilith CP06 | 2,714 | 500 |
| 14 | Diego | 18,641 | 11,000 |
| 15 | Lilith CP07 | 4,711 | 3,300 |
| 16 | Renaissance | 13,725 | 6,000 |
| 17 | Lilith CP08 | 3,546 | 2,400 |
| 18 | Taiping | 6,512 | 4,200 |
| 19 | Lilith CP09 | 10,011 | 4,500 |
| 20 | Malone | 11,144 | 4,500 |
| 21 | Lilith CP10 | 3,738 | 1,200 |
| 22 | Manchester | 9,748 | 25,000 |
| 23 | Deva | 6,813 | 5,000 |
| 24 | Future | 8,650 | 5,000 |
| 25 | Formless | 11,880 | 5,000 |
| 26 | Climax | 10,464 | 4,800 |
| **TOTAL** | | **216,594** | **125,000** |

### Budget C Type Totals

| Type | Target Words | Target % |
|------|-------------|----------|
| Manchester | 50,000 | 40.00% |
| Historical (kept) | 46,200 | 36.96% |
| Lilith | 18,000 | 14.40% |
| Final Sequence | 19,800 | 15.84% |
| CUT | 0 | 0% |

**Note**: Totals exceed 125,000 — recalculating...

### Budget C Final

| Ch | Name | Current | Target |
|----|------|---------|--------|
| 1 | Manchester | 7,895 | 25,000 |
| 2 | Ka | 5,058 | 4,200 |
| 3 | Lilith CP01 | 3,049 | 2,000 |
| 4 | Chandra | 19,676 | 11,000 |
| 5 | Lilith CP02 | 2,673 | 1,800 |
| 6 | Philon (CUT) | 10,202 | 0 |
| 7 | Lilith CP03 | 3,221 | 450 |
| 8 | Verinus (CUT) | 9,405 | 0 |
| 9 | Lilith CP04 | 5,998 | 650 |
| 10 | Macarius (CUT) | 13,777 | 0 |
| 11 | Lilith CP05 | 4,883 | 650 |
| 12 | Kaoru (CUT) | 8,460 | 0 |
| 13 | Lilith CP06 | 2,714 | 450 |
| 14 | Diego | 18,641 | 10,000 |
| 15 | Lilith CP07 | 4,711 | 3,000 |
| 16 | Renaissance | 13,725 | 5,500 |
| 17 | Lilith CP08 | 3,546 | 2,200 |
| 18 | Taiping | 6,512 | 4,000 |
| 19 | Lilith CP09 | 10,011 | 4,200 |
| 20 | Malone | 11,144 | 4,200 |
| 21 | Lilith CP10 | 3,738 | 1,100 |
| 22 | Manchester | 9,748 | 25,000 |
| 23 | Deva | 6,813 | 4,600 |
| 24 | Future | 8,650 | 4,600 |
| 25 | Formless | 11,880 | 4,800 |
| 26 | Climax | 10,464 | 4,600 |
| **TOTAL** | | **216,594** | **124,000** |

### Budget C Constraint Check

| Constraint | Formula | Value | Range | Status |
|------------|---------|-------|-------|--------|
| C1: Final words | total | 124,000 | 110,000–130,000 | **PASS** |
| C2: Manchester % | 50,000 / 124,000 | 40.32% | 40–50% | **PASS** |
| C3: Net cut | 216,594 - 124,000 | 92,594 | 80,000–100,000 | **PASS** |
| C4: Incarnations cut | count | 4 | 3–4 | **PASS** |
| C5: Pivotal scenes | TBD | ≥3 | ≥3 | PENDING |
| C6: Reflective reduction | TBD | 30–40% | 30–40% | PENDING |
| C7: Tic reduction | TBD | ~50% | ~50% | PENDING |

**Budget C passes all hard constraints.**

---

## Comparison Table

| Metric | Budget A | Budget B | Budget C |
|--------|----------|----------|----------|
| Final total | 120,000 | 114,000 | 124,000 |
| Manchester words | 48,000 | 50,000 | 50,000 |
| Manchester % | 40.00% | 43.86% | 40.32% |
| Net cut | 96,594 | 102,594 | 92,594 |
| Incarnations cut | 4 | 3 | 4 |
| C1 (total) | PASS | PASS | PASS |
| C2 (Manchester %) | PASS | PASS | PASS |
| C3 (net cut) | PASS | **FAIL** | PASS |
| C4 (incarnations) | PASS | PASS | PASS |

---

## Recommendation

**Budget C (Balanced)** is the recommended budget because:

1. Passes all hard constraints
2. Provides more breathing room (124,000 vs 120,000) for scene dramatization
3. Maintains 40.32% Manchester (within range)
4. Cuts exactly 4 incarnations as recommended
5. Net cut of 92,594 is safely within 80,000–100,000 range

### Budget C Summary

- **Final total**: 124,000 words
- **Manchester**: 50,000 words (40.32%)
- **Historical (kept)**: 38,900 words (31.37%)
- **Lilith**: 16,500 words (13.31%)
- **Final sequence**: 18,600 words (15.00%)
- **Net cut**: 92,594 words
- **Incarnations cut**: 4 (Philon, Verinus, Macarius, Kaoru)

---

## Detailed Budget C Word Allocation

### Manchester Frame (50,000 words)
| Chapter | Current | Target | Notes |
|---------|---------|--------|-------|
| Ch 1 | 7,895 | 25,000 | +17,105: Add Silas-Lilith relationship scenes, Stewart setup |
| Ch 22 | 9,748 | 25,000 | +15,252: Expand breakthrough, Stewart resolution |
| **Subtotal** | 17,643 | 50,000 | +32,357 net expansion |

### Historical Incarnations (38,900 words)
| Chapter | Current | Target | Compression % |
|---------|---------|--------|---------------|
| Ch 2 Ka | 5,058 | 4,200 | 17% |
| Ch 4 Chandra | 19,676 | 11,000 | 44% |
| Ch 14 Diego | 18,641 | 10,000 | 46% |
| Ch 16 Renaissance | 13,725 | 5,500 | 60% |
| Ch 18 Taiping | 6,512 | 4,000 | 39% |
| Ch 20 Malone | 11,144 | 4,200 | 62% |
| **Subtotal** | 74,756 | 38,900 | 48% average |

### Lilith Chapters (16,500 words)
| Chapter | Current | Target | Notes |
|---------|---------|--------|-------|
| Ch 3 | 3,049 | 2,000 | Active tracking |
| Ch 5 | 2,673 | 1,800 | Active tracking |
| Ch 7 | 3,221 | 450 | Compressed (Philon cut) |
| Ch 9 | 5,998 | 650 | Compressed (Verinus cut) |
| Ch 11 | 4,883 | 650 | Compressed (Macarius cut) |
| Ch 13 | 2,714 | 450 | Compressed (Kaoru cut) |
| Ch 15 | 4,711 | 3,000 | Active tracking |
| Ch 17 | 3,546 | 2,200 | Active tracking |
| Ch 19 | 10,011 | 4,200 | Active tracking |
| Ch 21 | 3,738 | 1,100 | Transition to finale |
| **Subtotal** | 44,544 | 16,500 | 63% reduction |

### Final Sequence (18,600 words)
| Chapter | Current | Target | Compression % |
|---------|---------|--------|---------------|
| Ch 23 Deva | 6,813 | 4,600 | 32% |
| Ch 24 Future | 8,650 | 4,600 | 47% |
| Ch 25 Formless | 11,880 | 4,800 | 60% |
| Ch 26 Climax | 10,464 | 4,600 | 56% |
| **Subtotal** | 37,807 | 18,600 | 51% average |

### CUT Chapters (0 words)
| Chapter | Current | Cut |
|---------|---------|-----|
| Ch 6 Philon | 10,202 | -10,202 |
| Ch 8 Verinus | 9,405 | -9,405 |
| Ch 10 Macarius | 13,777 | -13,777 |
| Ch 12 Kaoru | 8,460 | -8,460 |
| **Subtotal** | 41,844 | -41,844 |

---

## Final Verification (Arithmetic Proof)

**Step-by-step calculation from baseline:**

```
Starting baseline:                              216,594

Operations:
  CUT Ch6 Philon:                               -10,202
  CUT Ch8 Verinus:                               -9,405
  CUT Ch10 Macarius:                            -13,777
  CUT Ch12 Kaoru:                                -8,460
  Subtotal after incarnation cuts:              174,750

  COMPRESS Ch2 (Ka): 5,058 → 4,200               -858
  COMPRESS Ch4 (Chandra): 19,676 → 11,000       -8,676
  COMPRESS Ch14 (Diego): 18,641 → 10,000        -8,641
  COMPRESS Ch16 (Renaissance): 13,725 → 5,500   -8,225
  COMPRESS Ch18 (Taiping): 6,512 → 4,000        -2,512
  COMPRESS Ch20 (Malone): 11,144 → 4,200        -6,944
  COMPRESS Ch23 (Deva): 6,813 → 4,600           -2,213
  COMPRESS Ch24 (Future): 8,650 → 4,600         -4,050
  COMPRESS Ch25 (Formless): 11,880 → 4,800      -7,080
  COMPRESS Ch26 (Climax): 10,464 → 4,600        -5,864
  Subtotal historical/final compression:        -55,063

  COMPRESS Lilith CP01 (Ch3): 3,049 → 2,000     -1,049
  COMPRESS Lilith CP02 (Ch5): 2,673 → 1,800      -873
  CONVERT Lilith CP03 (Ch7): 3,221 → 450        -2,771
  CONVERT Lilith CP04 (Ch9): 5,998 → 650        -5,348
  CONVERT Lilith CP05 (Ch11): 4,883 → 650       -4,233
  CONVERT Lilith CP06 (Ch13): 2,714 → 450       -2,264
  COMPRESS Lilith CP07 (Ch15): 4,711 → 3,000    -1,711
  COMPRESS Lilith CP08 (Ch17): 3,546 → 2,200    -1,346
  COMPRESS Lilith CP09 (Ch19): 10,011 → 4,200   -5,811
  COMPRESS Lilith CP10 (Ch21): 3,738 → 1,100    -2,638
  Subtotal Lilith compression:                  -28,044

  EXPAND Ch1 (Manchester): 7,895 → 25,000      +17,105
  EXPAND Ch22 (Manchester): 9,748 → 25,000     +15,252
  Subtotal Manchester expansion:                +32,357

─────────────────────────────────────────────────────
Total change:                                   -92,594

Baseline:                                       216,594
Total change:                                   -92,594
─────────────────────────────────────────────────────
FINAL TOTAL:                                    124,000 ✓

Manchester verification:
  Ch1 target: 25,000
  Ch22 target: 25,000
  Manchester total: 50,000
  Manchester %: 50,000 / 124,000 = 40.32% ✓

Constraint verification:
  C1 (Final total): 124,000 ∈ [110,000, 130,000] ✓
  C2 (Manchester %): 40.32% ∈ [40%, 50%] ✓
  C3 (Net cut): 92,594 ∈ [80,000, 100,000] ✓
  C4 (Incarnations cut): 4 ∈ [3, 4] ✓
```
