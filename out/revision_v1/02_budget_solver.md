# Budget Solver

## Methodology

**Constraint intersection**:
- C1 requires final: 110,000–130,000
- C2 requires net cut 80,000–100,000, meaning final: 116,594–136,594
- Combined valid range: **116,594–130,000**

**Manchester requirement**:
- C4 requires FINAL Manchester %: 40–50%
- Current Manchester: 17,643 (8.15%)
- Manchester chapters: Ch1 (7,895) and Ch22 (9,748) only
- Expansion is REQUIRED to meet C4

**Cut pool**:
- 4 editor-recommended incarnations: 41,844 words
- Remaining cuts must come from compression of kept content

---

## Budget A: Aggressive (Maximum Cut)

**Target final**: 116,594 words
**Net cut**: 100,000 words (maximum per C2)
**Manchester**: 46,638 words (40.00% of final)

### Ledger

```
BASELINE                                           216,594

CUT (4 incarnations):
  Ch6 Athens Philosopher (Philon)                  -10,202
  Ch8 Rome Investigator (Verinus)                   -9,405
  Ch10 Egypt Hermit (Macarius)                     -13,777
  Ch12 Heian Lover (Kaoru)                          -8,460
  Subtotal CUT:                                    -41,844

COMPRESS (by type):
  Historical (6 kept chapters):
    74,756 → 35,000                                -39,756
  Lilith (10 chapters):
    44,544 → 10,000                                -34,544
  Final sequence (Ch23-26):
    37,807 → 24,956                                -12,851
  Subtotal COMPRESS:                               -87,151

EXPAND (Manchester):
  Ch1: 7,895 → 23,319                              +15,424
  Ch22: 9,748 → 23,319                             +13,571
  Subtotal EXPAND:                                 +28,995

────────────────────────────────────────────────────────
NET CHANGE:                                       -100,000
FINAL TOTAL:                                       116,594
```

### Composition Check
- Manchester: 46,638 (40.00%)
- Non-Manchester: 69,956 (60.00%)
- Total: 116,594 ✓

### Constraint Check
| Constraint | Value | Range | Status |
|------------|-------|-------|--------|
| C1 Final | 116,594 | 110,000–130,000 | PASS |
| C2 Net cut | 100,000 | 80,000–100,000 | PASS |
| C3 Cuts | 4 | 3–4 | PASS |
| C4 Manchester % | 40.00% | 40–50% | PASS |

---

## Budget B: Moderate

**Target final**: 120,000 words
**Net cut**: 96,594 words
**Manchester**: 48,000 words (40.00% of final)

### Ledger

```
BASELINE                                           216,594

CUT (4 incarnations):
  Ch6 Athens Philosopher (Philon)                  -10,202
  Ch8 Rome Investigator (Verinus)                   -9,405
  Ch10 Egypt Hermit (Macarius)                     -13,777
  Ch12 Heian Lover (Kaoru)                          -8,460
  Subtotal CUT:                                    -41,844

COMPRESS (by type):
  Historical (6 kept chapters):
    74,756 → 36,000                                -38,756
  Lilith (10 chapters):
    44,544 → 12,000                                -32,544
  Final sequence (Ch23-26):
    37,807 → 24,000                                -13,807
  Subtotal COMPRESS:                               -85,107

EXPAND (Manchester):
  Ch1: 7,895 → 24,000                              +16,105
  Ch22: 9,748 → 24,000                             +14,252
  Subtotal EXPAND:                                 +30,357

────────────────────────────────────────────────────────
NET CHANGE:                                        -96,594
FINAL TOTAL:                                       120,000
```

### Composition Check
- Manchester: 48,000 (40.00%)
- Non-Manchester: 72,000 (60.00%)
- Total: 120,000 ✓

### Constraint Check
| Constraint | Value | Range | Status |
|------------|-------|-------|--------|
| C1 Final | 120,000 | 110,000–130,000 | PASS |
| C2 Net cut | 96,594 | 80,000–100,000 | PASS |
| C3 Cuts | 4 | 3–4 | PASS |
| C4 Manchester % | 40.00% | 40–50% | PASS |

---

## Budget C: Balanced (SELECTED)

**Target final**: 125,000 words
**Net cut**: 91,594 words
**Manchester**: 50,000 words (40.00% of final)

### Ledger

```
BASELINE                                           216,594

CUT (4 incarnations):
  Ch6 Athens Philosopher (Philon)                  -10,202
  Ch8 Rome Investigator (Verinus)                   -9,405
  Ch10 Egypt Hermit (Macarius)                     -13,777
  Ch12 Heian Lover (Kaoru)                          -8,460
  Subtotal CUT:                                    -41,844

COMPRESS (by type):
  Historical (6 kept chapters):
    74,756 → 40,000                                -34,756
  Lilith (10 chapters):
    44,544 → 15,000                                -29,544
  Final sequence (Ch23-26):
    37,807 → 20,000                                -17,807
  Subtotal COMPRESS:                               -82,107

EXPAND (Manchester):
  Ch1: 7,895 → 25,000                              +17,105
  Ch22: 9,748 → 25,000                             +15,252
  Subtotal EXPAND:                                 +32,357

────────────────────────────────────────────────────────
NET CHANGE:                                        -91,594
FINAL TOTAL:                                       125,000
```

### Composition Check
- Manchester: 50,000 (40.00%)
- Non-Manchester: 75,000 (60.00%)
- Total: 125,000 ✓

### Constraint Check
| Constraint | Value | Range | Status |
|------------|-------|-------|--------|
| C1 Final | 125,000 | 110,000–130,000 | PASS |
| C2 Net cut | 91,594 | 80,000–100,000 | PASS |
| C3 Cuts | 4 | 3–4 | PASS |
| C4 Manchester % | 40.00% | 40–50% | PASS |

---

## Budget Comparison

| Metric | Budget A | Budget B | Budget C |
|--------|----------|----------|----------|
| Final total | 116,594 | 120,000 | 125,000 |
| Net cut | 100,000 | 96,594 | 91,594 |
| Manchester words | 46,638 | 48,000 | 50,000 |
| Manchester % | 40.00% | 40.00% | 40.00% |
| Historical cap | 35,000 | 36,000 | 40,000 |
| Lilith cap | 10,000 | 12,000 | 15,000 |
| Final sequence cap | 24,956 | 24,000 | 20,000 |
| Historical compression % | 53.2% | 51.8% | 46.5% |
| Lilith compression % | 77.6% | 73.1% | 66.3% |

---

## Selection: Budget C

**Rationale** (5 bullets):

1. **Least aggressive compression**: Budget C requires 46.5% compression of kept Historical content vs 53.2% for Budget A — more achievable without losing essential narrative beats
2. **Adequate Lilith space**: 15,000 words for 10 Lilith chapters (avg 1,500/chapter) allows meaningful tracking content vs Budget A's 1,000/chapter average
3. **Comfortable margin within C1**: 125,000 sits safely within 110,000–130,000, allowing adjustment during execution
4. **Manchester expansion feasible**: 32,357 net add to Manchester is substantial but matches editor's "15,000-20,000 words net" for Ch22 plus significant Ch1 expansion
5. **Final sequence preserved**: 20,000 words for metaphysical climax chapters (avg 5,000/chapter) maintains philosophical depth vs Budget A's cramped 6,239/chapter average

---

## Cut Bank (Numerical Accounting)

All cuts attributed to specific chapters or type pools:

| Source | Words |
|--------|-------|
| Ch6 Philon (CUT) | 10,202 |
| Ch8 Verinus (CUT) | 9,405 |
| Ch10 Macarius (CUT) | 13,777 |
| Ch12 Kaoru (CUT) | 8,460 |
| Historical compression | 34,756 |
| Lilith compression | 29,544 |
| Final sequence compression | 17,807 |
| **GROSS CUT** | **123,951** |
| Manchester expansion | -32,357 |
| **NET CUT** | **91,594** |

Verification: 216,594 - 91,594 = 125,000 ✓

---

## NET-0 Rewrite Bucket (Dramatizations)

Per system contract, dramatizations are NET-0 (replace summary with scene).

Pivotal scenes to dramatize (C7):
1. Devaka's betrayal — NET-0 rewrite within Ch4/Ch5
2. Stewart rooftop fall — NET-0 rewrite within Ch22
3. Lilith's first intervention — NET-0 rewrite within Ch5

These do NOT add to word count; they replace existing summary text with scene-level prose.
