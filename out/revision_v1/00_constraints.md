# Revision Constraints

## Source
All constraints extracted from: `/docs/editor_letter.md` (December 2025)

---

## C1: Final Total Word Count
- **Requirement**: "Standard literary fiction runs 70,000–90,000 words; even ambitious literary work rarely exceeds 120,000."
- **Editor Target**: 110,000–130,000 words
- **Condition**: `final_total_words >= 110000 AND final_total_words <= 130000`
- **Verification**: `jq '.total_words' out/revision_audit/analysis_data.json`

## C2: Net Word Cut
- **Requirement**: "Cut 80,000–100,000 Words" (Issue #1 title)
- **Baseline**: 216,594 words (from analysis_data.json)
- **Condition**: `(216594 - final_total_words) >= 80000 AND (216594 - final_total_words) <= 100000`
- **Implied final range**: 116,594–136,594 (intersection with C1 = 116,594–130,000)
- **Verification**: Compute `216594 - final_total_words`

## C3: Incarnation Reduction
- **Requirement**: "Cut 3-4 incarnation sequences entirely"
- **Condition**: `incarnations_cut >= 3 AND incarnations_cut <= 4`
- **Note**: Editor explicitly names Philon, Verinus, Macarius, Kaoru as cut candidates
- **Verification**: Count chapters with type="Historical" removed from final TOC

## C4: Final Manchester Percentage
- **Requirement**: "The Manchester frame is ~20% of the narrative; it should be 40-50%"
- **Scope**: FINAL manuscript only (not intermediate states)
- **Condition**: `(manchester_words / final_total_words) >= 0.40 AND <= 0.50`
- **Verification**: Sum word_count where type="Manchester", divide by total_words

## C5: Tic Reduction
- **Requirement**: "Reduce 'particular,' 'something,' and the 'not X—Y' construction by 50%"
- **Baseline densities** (per 10k words, from analysis_data.json):
  - `particular`: 114 total / 216594 * 10000 = 5.26 per 10k
  - `something`: 1051 total / 216594 * 10000 = 48.52 per 10k
  - `not_x_y_pattern`: 118 total / 216594 * 10000 = 5.45 per 10k
  - `em_dashes`: 2883 total / 216594 * 10000 = 133.13 per 10k
- **Target densities** (50% of baseline):
  - `particular`: <= 2.63 per 10k
  - `something`: <= 24.26 per 10k
  - `not_x_y_pattern`: <= 2.73 per 10k
  - `em_dashes`: <= 66.57 per 10k
- **Verification**: Re-run analyzer on final manuscript, compute densities

## C6: Reflective Elaboration Reduction
- **Requirement**: "Cut 30-40% of reflective elaboration"
- **Proxy metric**: Abstraction density (available in analysis_data.json)
- **Note**: Abstraction density is computed per chapter; reduction target is qualitative
- **Verification**: MANUAL — compare pre/post abstraction density averages in high-density chapters

## C7: Pivotal Scenes Dramatized
- **Requirement**: "Dramatize at least three of the following"
- **Candidates listed by editor**:
  1. Devaka's betrayal
  2. Lilith's first intervention
  3. Lilith's final resistance before merge
  4. Stewart rooftop fall
- **Condition**: `pivotal_scenes_dramatized >= 3`
- **Note**: Dramatizations are NET-0 word changes (replace summary with scene, not net-add)
- **Verification**: MANUAL — confirm scene structure (decision/cost/consequence) present

---

## Constraint Summary Table

| ID | Constraint | Threshold | Measurable | Verification |
|----|-----------|-----------|------------|--------------|
| C1 | Final words | 110,000–130,000 | YES | analyzer |
| C2 | Net cut | 80,000–100,000 | YES | arithmetic |
| C3 | Incarnations cut | 3–4 | YES | chapter count |
| C4 | Final Manchester % | 40–50% | YES | analyzer |
| C5 | Tic density | ≤50% baseline | YES | analyzer |
| C6 | Reflective reduction | 30–40% | PROXY | manual |
| C7 | Pivotal scenes | ≥3 | NO | manual |

---

## Notes

- Constraints C1-C4 are hard numerical requirements that MUST pass
- Constraint C5 is measurable via analyzer but requires line-edit execution
- Constraints C6-C7 require manual verification after execution
- No intermediate-state constraints are defined (editor only constrains FINAL state)
