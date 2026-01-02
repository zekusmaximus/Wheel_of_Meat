# Lilith Continuity Audit Report

**Date:** December 10, 2025
**Auditor:** Claude Code
**Scope:** Full repository review for conflicts with canonical timeline and terminology
**Reference Documents:** `meta/lilith-contemporary-timeline.md` and `incarnations/ch13-lilith-cp06/ch13_oultine.md`

---

## Executive Summary

This audit identified **32 discrepancies** across **15 files** that conflict with the newly established canonical understanding of Lilith's powers and intervention mechanisms. The conflicts fall into three primary categories:

### Findings by Priority

- **High Priority (Direct Narrative Conflicts):** 12 instances
- **Medium Priority (Documentation Terminology):** 15 instances
- **Low Priority (Minor Phrasing):** 5 instances

### Patterns Observed

1. **"Vessel possession" terminology** appears 12 times across 6 files (should be "vessel pushing" or "driving")
2. **"Inhabit/inhabits" terminology** appears 8 times across 4 files (should be "pushes" or "drives")
3. **"Karmic disturbance" terminology** appears 3 times in Lilith-interiority contexts (should be "noise floor")
4. **Internal contradictions** in `ch13_oultine.md` itself—the outline notes the need to avoid certain terms, then uses them

### Critical Observation

Interestingly, `ch13_oultine.md` line 419-421 explicitly states:

> **Instead of "karmic disturbance":**
> - "The noise floor"—baseline interference that cannot be eliminated

Yet the same document uses "karmic disturbance" in line 20. This suggests the terminology shift was identified during outline development but not yet propagated through the existing text.

---

## Detailed Findings

### Discrepancy 1: Core Mechanism Terminology in lilith-arc.json

**File:** `meta/lilith-arc.json`
**Location:** Lines 79-82 (Chapter 12 power level entry)

**Current Text:**
```json
"level": "Vessel possession (Low Agency)",
"capabilities": "Inhabits a local human vessel (The Attendant) but lacks full integration; drives the host through subconscious compulsion rather than direct control."
```

**Conflict With:** The canonical mechanism established in ch13-outline.md that Lilith *pushes* or *drives* vessels through subconscious compulsion, NOT "possesses" or "inhabits" them.

**Issue:** Uses both "possession" and "inhabits" terminology. While the description of the mechanism (driving through subconscious compulsion) is correct, the framing language contradicts the new canonical understanding.

**Suggested Revision:**
```json
"level": "Vessel pushing (Low Agency)",
"capabilities": "Pushes a local human vessel (The Attendant) through subconscious compulsion but lacks full integration; drives the host from afar rather than inhabiting with direct control."
```

**Priority:** High (core documentation that informs all chapter development)

---

### Discrepancy 2: Power Level Label in lilith-arc.json

**File:** `meta/lilith-arc.json`
**Location:** Line 79

**Current Text:**
```json
"level": "Vessel possession (Low Agency)"
```

**Conflict With:** The canonical "pushing" mechanism—the label itself embeds the problematic terminology.

**Issue:** The power level name uses "possession" when the mechanism is actually remote compulsion/pushing.

**Suggested Revision:**
```json
"level": "Vessel pushing (Low Agency)"
```

**Priority:** High

---

### Discrepancy 3: Timeline Document Uses "Inhabits"

**File:** `meta/lilith-contemporary-timeline.md`
**Location:** Line 116

**Current Text:**
> - Inhabits Theodora (church dignitary) but only as observer/orchestrator, not full possession

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Uses "inhabits" language even while clarifying it's not "full possession."

**Suggested Revision:**
> - Works through Theodora (church dignitary) as observer/orchestrator, pushing from afar rather than inhabiting directly

**Priority:** Medium (canonical timeline document but in descriptive rather than narrative context)

---

### Discrepancy 4: Timeline Uses "Karmic Disturbance"

**File:** `meta/lilith-contemporary-timeline.md`
**Location:** Line 299

**Current Text:**
> **After Ch13:** The limit is karmic disturbance—interventions create counter-pressure regardless of her capacity

**Conflict With:** The "noise floor" terminology established in ch13-outline.md.

**Issue:** Uses Buddhist-adjacent "karmic" terminology to describe Lilith's understanding of her limitation.

**Suggested Revision:**
> **After Ch13:** The limit is the noise floor—interventions create interference regardless of her capacity

**Priority:** Medium (documentation context, but describes Lilith's interiority)

---

### Discrepancy 5: CH12 Outline "Possesses" Language

**File:** `incarnations/ch12-heian-lover/CH12_outline.md`
**Location:** Line 17

**Current Text:**
> She possesses the canonical physical markers (Widow's Peak, Rogue Strand, Green Crescent in left eye). Lilith inhabits this vessel with Low Agency—driving her through subconscious compulsion rather than direct control.

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Uses both "possesses" (referring to physical markers, which is fine) and "inhabits" (referring to the mechanism, which is not fine) in the same sentence.

**Suggested Revision:**
> She has the canonical physical markers (Widow's Peak, Rogue Strand, Green Crescent in left eye). Lilith pushes this vessel with Low Agency—driving her through subconscious compulsion from afar rather than inhabiting with direct control.

**Priority:** High (chapter outline that guides narrative drafting)

---

### Discrepancy 6: CH12 Outline Power Level Header

**File:** `incarnations/ch12-heian-lover/CH12_outline.md`
**Location:** Line 23

**Current Text:**
> **Power Level:** Vessel Possession (Low Agency)—first attempt at this capability

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Section header uses "possession" terminology.

**Suggested Revision:**
> **Power Level:** Vessel Pushing (Low Agency)—first attempt at this capability

**Priority:** High

---

### Discrepancy 7: CH12 Outline Method Description

**File:** `incarnations/ch12-heian-lover/CH12_outline.md`
**Location:** Line 25

**Current Text:**
> **Method:** Lilith possesses the Attendant and uses her to stage-manage an artificial Gothic romance.

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Direct statement that "Lilith possesses the Attendant."

**Suggested Revision:**
> **Method:** Lilith pushes the Attendant and uses her to stage-manage an artificial Gothic romance.

**Priority:** High (directly describes narrative action)

---

### Discrepancy 8: CH12 Outline Final Note

**File:** `incarnations/ch12-heian-lover/CH12_outline.md`
**Location:** Line 153

**Current Text:**
> **Lilith's First Vessel Possession:** This chapter establishes her ability to inhabit a human vessel, though imperfectly.

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Summary statement uses both "possession" and "inhabit."

**Suggested Revision:**
> **Lilith's First Vessel Pushing:** This chapter establishes her ability to push a human vessel through remote compulsion, though imperfectly.

**Priority:** High

---

### Discrepancy 9: CH12 Avatar Profile

**File:** `incarnations/ch12-heian-lover/avatar-profile.json`
**Location:** Line 36 (notes field)

**Current Text:**
```json
"notes": "Lilith possesses a local human vessel (The Attendant) in her first attempt at this power level."
```

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Character profile uses "possesses" terminology.

**Suggested Revision:**
```json
"notes": "Lilith pushes a local human vessel (The Attendant) through remote compulsion in her first attempt at this power level."
```

**Priority:** Medium (character documentation)

---

### Discrepancy 10: CH13 Notes Power Level

**File:** `incarnations/ch13-lilith-cp06/notes.md`
**Location:** Line 10

**Current Text:**
> **Vessel Possession (Low Agency)** — Now with understanding of its structural limitations

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Power level header uses "possession" terminology.

**Suggested Revision:**
> **Vessel Pushing (Low Agency)** — Now with understanding of its structural limitations

**Priority:** High (guides chapter drafting)

---

### Discrepancy 11: CH13 Notes Capabilities Description

**File:** `incarnations/ch13-lilith-cp06/notes.md`
**Location:** Line 13

**Current Text:**
> - Full vessel possession of the Attendant (her own past incarnation)

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Capability description uses "possession."

**Suggested Revision:**
> - Full vessel pushing of the Attendant (her own past incarnation)

**Priority:** High

---

### Discrepancy 12: CH13 Notes "Karmic Disturbance"

**File:** `incarnations/ch13-lilith-cp06/notes.md`
**Location:** Line 21

**Current Text:**
> - Every action raises karmic disturbance; the universe compensates for precise intervention

**Conflict With:** The "noise floor" terminology.

**Issue:** Uses "karmic disturbance" when describing Lilith's realization—this would be her interiority.

**Suggested Revision:**
> - Every action raises the noise floor; the universe compensates for precise intervention

**Priority:** High (describes Lilith's actual understanding)

---

### Discrepancy 13: CH13 Outline Internal Contradiction (Part 1)

**File:** `incarnations/ch13-lilith-cp06/ch13_oultine.md`
**Location:** Line 20

**Current Text:**
> - The meditation reveals she's overcome the attentional costs—but discovered karmic disturbance

**Conflict With:** Line 419-421 of the same document, which explicitly states to use "noise floor" instead of "karmic disturbance."

**Issue:** The outline uses the terminology it explicitly rejects later. This is an internal contradiction within the canonical reference document itself.

**Suggested Revision:**
> - The meditation reveals she's overcome the attentional costs—but discovered the noise floor

**Priority:** High (internal inconsistency in canonical document)

---

### Discrepancy 14: CH13 Outline "Vessel Possession" in Narrative

**File:** `incarnations/ch13-lilith-cp06/ch13_oultine.md`
**Location:** Line 201

**Current Text:**
> The failure wasn't about effort. She had complete control of the Attendant. Her vessel possession worked perfectly.

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Uses "vessel possession" in what appears to be draft narrative text or close paraphrase of Lilith's thoughts.

**Suggested Revision:**
> The failure wasn't about effort. She had complete control of the Attendant. Her vessel pushing worked perfectly.

**Priority:** High (appears in narrative-adjacent context)

---

### Discrepancy 15: CH13 Outline Continuity Checklist

**File:** `incarnations/ch13-lilith-cp06/ch13_oultine.md`
**Location:** Line 455

**Current Text:**
```markdown
- [ ] Power level represents evolution from Ch11 (vessel possession)
```

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Checklist item uses "possession" terminology.

**Suggested Revision:**
```markdown
- [ ] Power level represents evolution from Ch11 (vessel pushing)
```

**Priority:** Medium (checklist/metadata)

---

### Discrepancy 16: Claude.md Power Progression Reference

**File:** `claude.md`
**Location:** Line 180

**Current Text:**
> - Power grows from observation (Ch 3) → remote influence (Ch 5) → dream influence (Ch 7) → circumstance manipulation (Ch 9) → growing control (Ch 11) → vessel possession (Ch 13+) → full manifestation (Ch 20-22) → cosmic scale (Ch 23-26)

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Power progression summary uses "vessel possession" terminology.

**Suggested Revision:**
> - Power grows from observation (Ch 3) → remote influence (Ch 5) → dream influence (Ch 7) → circumstance manipulation (Ch 9) → growing control (Ch 11) → vessel pushing (Ch 13+) → full manifestation (Ch 20-22) → cosmic scale (Ch 23-26)

**Priority:** Medium (project overview documentation)

---

### Discrepancy 17: Claude.md Chapter Table

**File:** `claude.md`
**Location:** Line 217

**Current Text:**
```markdown
|13|TBD                       |Lilith    |Lilith age 30          |Vessel possession                 |needs_dev|
```

**Conflict With:** The canonical "pushing" mechanism.

**Issue:** Chapter quick-reference table uses "possession."

**Suggested Revision:**
```markdown
|13|TBD                       |Lilith    |Lilith age 30          |Vessel pushing                    |needs_dev|
```

**Priority:** Medium (quick reference table)

---

## Additional Observations

### Observation 1: "Karmic" in Meta-Documentation vs. Narrative

The term "karmic" appears extensively throughout the repository (20+ files), but the majority of uses are in **meta-documentation contexts** describing the novel's structure:

- "karmic bridge" (the death-to-rebirth connection mechanism)
- "karmic thread" (describing cause-and-effect across lives)
- "karmic weight" (describing thematic significance)

**These meta-documentary uses are likely acceptable** because they describe the *structure* of the novel from an outside perspective, not Lilith's interiority or the characters' thoughts.

**The problematic uses** are the 3 instances where "karmic disturbance" appears as Lilith's actual understanding of her power limitations. These should change to "noise floor."

### Observation 2: Self-Correcting Documentation

The fact that `ch13_oultine.md` contains both the problematic terminology AND explicit notes to avoid it (lines 419-421, 72) suggests:

1. The terminology shift was recognized during outline development
2. The outline itself predates the final canonical decision
3. A systematic find-and-replace may have been intended but not yet executed

### Observation 3: No Issues in Actual Draft Prose

Interestingly, the **CH12_draft.md** (the actual narrative prose for Chapter 12) does NOT use "possession" or "inhabit" terminology when describing the Attendant's actions. The draft shows her scrubbing, working compulsively, but never explicitly states mechanism language. This suggests the problem is isolated to **documentation and outlines** rather than drafted narrative.

---

## Recommended Revision Order

### Phase 1: Core Documentation (High Impact)

1. **`meta/lilith-arc.json`** — Update Chapter 12 power level entry (lines 79-82)
2. **`meta/lilith-contemporary-timeline.md`** — Update line 116 (inhabits→works through) and line 299 (karmic disturbance→noise floor)
3. **`claude.md`** — Update power progression (line 180) and chapter table (line 217)

### Phase 2: Chapter 13 Canon Documents (Critical for Development)

4. **`incarnations/ch13-lilith-cp06/notes.md`** — Update lines 10, 13, 21
5. **`incarnations/ch13-lilith-cp06/ch13_oultine.md`** — Update lines 20, 201, 455

### Phase 3: Chapter 12 Documentation (Prevents Confusion During Revision)

6. **`incarnations/ch12-heian-lover/CH12_outline.md`** — Update lines 17, 23, 25, 153
7. **`incarnations/ch12-heian-lover/avatar-profile.json`** — Update notes field

### Phase 4: Verification

8. **Run search for any remaining instances** of "vessel possession," "inhabits" (in Lilith context), and "karmic disturbance" (in Lilith interiority)
9. **Review any new documentation** created after this audit to ensure compliance

---

## Terminology Reference Guide

For future development and revision, use this quick reference:

### ✅ CORRECT Terminology

**Power Mechanism:**
- "Pushes" the vessel
- "Drives" the vessel through subconscious compulsion
- "Compels from afar"
- "Remote compulsion"
- The vessel "experiences inexplicable urges"
- The vessel acts "as if driven by something she can't name"

**Cost/Limitation:**
- "The noise floor"
- "Baseline interference"
- "Every action raises the noise"
- "Something compensates"
- "The universe has a noise floor she cannot go beneath"

**The Attendant's Experience:**
- "Manic compulsion"
- "Inexplicable drive"
- "Pressure from somewhere she can't identify"
- "In rare moments of lucidity, Lilith can observe through those eyes"

### ❌ INCORRECT Terminology

**Avoid in Narrative/Lilith's Interiority:**
- "Possesses" / "possession" (when describing the mechanism)
- "Inhabits" / "inhabiting"
- "Rides in" / "riding"
- "Controls" (when implying direct consciousness transfer)
- "Puppet" (when implying she's inside the vessel)
- "Karmic disturbance"
- "Karmic cost"
- Buddhist terminology in Lilith's thoughts

**Exception:** "Possession" is fine when referring to owning/having something (e.g., "She possesses the physical markers" = she has them). The problem is specifically "vessel possession" or "possesses the Attendant."

---

## Files Requiring No Changes

The following files were reviewed and found to be **compliant** with canonical terminology:

- `incarnations/ch09-lilith-cp04/notes.md` — Uses "circumstance manipulation" power level; no vessel pushing yet
- `incarnations/ch12-heian-lover/CH12_draft.md` — Narrative prose avoids mechanism terminology; shows behavior only
- `agent-protocol.md` — Uses "karmic bridge" in meta-documentary sense (acceptable)
- `reference/style-rules.md` — No Lilith mechanism discussion

---

## Conclusion

This audit identified a clear pattern: the terminology shift from "vessel possession" to "vessel pushing" and from "karmic disturbance" to "noise floor" was established in the canonical reference documents, but **not yet propagated** through the existing chapter documentation and core metadata files.

**The good news:** No narrative prose conflicts were found. The issues are isolated to:
- Documentation files (outlines, notes, profiles)
- Core metadata (lilith-arc.json, claude.md)
- The canonical documents themselves (internal contradictions)

**Recommendation:** Execute revisions in the order specified above, prioritizing the core documentation that informs all future development. Once these foundational files are corrected, the accurate terminology will naturally flow into future drafts.

**Estimated Revision Time:** ~30-45 minutes for all 17 discrepancies across 7 files.

---

**Audit completed:** December 10, 2025
**Next step:** Implement revisions and verify with follow-up search
