# Lilith Chapter Manifest Revision Brainstorm

**Purpose:** Plan the creation of `lilith-chapter-manifest.json` as specified in the lilith-refactor.md implementation plan.

**Status:** Phase 1 Core Architecture (after CLAUDE.md, lilith-arc.json)

---

## Current State

The `lilith-chapter-manifest.json` file **does not currently exist**. References to Lilith chapters exist in:

1. **scene-manifest.json** - Already updated with new architecture (integrated prose, fetter intensification, parallel structure, etc.)
2. **meta/lilith-arc.json** - Contains OLD power progression model + some updated content
3. **meta/lilith-arc-bible.md** - Contains correct emotional arc and competition-through-intimacy framework
4. **lilith-refactor.md** - Authoritative source for all new decisions

The manifest needs to be **created from scratch** to serve as the dedicated reference for Lilith chapter requirements.

---

## Purpose of lilith-chapter-manifest.json

Per lilith-refactor.md, this file should be the **single source of truth** for:

1. Per-chapter requirements for all 10 Lilith chapters (3, 5, 7, 9, 11, 13, 15, 17, 19, 21)
2. Integrated prose technique specifications per historical period
3. Fetter intensification beats
4. Parallel structure requirements (Lilith mistake mirrors avatar mistake)
5. Pivotal moment specifications
6. Maitreya foreshadowing distribution
7. Word targets and structural templates

---

## Proposed Structure

```json
{
  "manifest_version": "2.0",
  "architecture": {
    // High-level description of integrated prose, timeline, etc.
  },
  "technique": {
    // Integrated prose mechanics, sensory bridges, etc.
  },
  "timeline": {
    // Compressed tracking period, time jump, etc.
  },
  "chapters": [
    // Per-chapter detailed requirements
  ]
}
```

---

## Content to Include

### 1. Architecture Section

- Confirmation that all chapters use integrated prose (no alternating)
- Full cosmic power from Ch 3 (constrained by karmic law, not capability)
- Fetter intensification arc (not power progression)
- Timeline compression (8-10 weeks, not 10 years)
- Time jump between Ch 21 and Ch 1 (6-12 months)
- Word targets: 2,500-3,500 per chapter

### 2. Technique Section

- Sensory bridge mechanics
- Pronoun flow (She for Lilith; avatar sensations register in her body)
- Parallel structure requirement (her mistake mirrors avatar's mistake)
- Dominant timeline moments (1-2 per chapter where one timeline foregrounds)
- No transition markers, no scene breaks between timelines

### 3. Integration Flavor by Period

From lilith-refactor.md:

| Period | Integration Flavor |
|--------|-------------------|
| Prehistoric (Ka) | Primal, sensory, non-verbal, body-knowledge |
| Mauryan (Chandra) | Bureaucratic, ledgers and rain, political weight |
| Athens (Philon) | Philosophical, dialogue bleeding through, ideas as sensation |
| Rome (Verinus) | Procedural, investigation layered on investigation |
| Egypt (Macarius) | Ascetic, emptiness against emptiness, silence doubled |
| Heian (Kaoru) | Aesthetic, beauty saturating both frames, longing amplified |
| Inquisition | Claustrophobic, persecution in two keys |
| Renaissance | Intellectual, wit and doubt, skepticism layered |
| Taiping | Chaotic, violence bleeding through, conviction fractured |
| Noir | Atmospheric, cigarette smoke and rain, failure repeated |

### 4. Per-Chapter Requirements

Each chapter entry should include:

```json
{
  "chapter": 3,
  "title": "The Discovery",
  "tracking_timeline": "Days 1-3",
  "weeks_since_discovery": "0",

  "corresponds_to": {
    "historical_chapter": 2,
    "avatar": "Ka",
    "lesson": "Loving-kindness (mettā) / Cooperation"
  },

  "integration": {
    "flavor": "Primal, sensory, non-verbal, body-knowledge",
    "sensory_bridges": [
      "Kettle scream / wind scream",
      "Tea warmth / fire warmth",
      "Flat silence / cave silence"
    ],
    "parallel_structure": {
      "avatar_mistake": "Hoarding meat, isolation, calling alone-way 'strength'",
      "lilith_mistake": "Hoarding capability, solitary tracking, calling isolation 'strategic'"
    }
  },

  "fetter_beat": {
    "manifestation": "I've found a problem to solve",
    "emotional_state": "Analytical curiosity, first unnamed stirring",
    "shown_through": "Action - stays in tracking corner, drinks cold tea"
  },

  "pivotal_moments": [
    {
      "dominant_timeline": "Historical",
      "moment": "Ka's death",
      "technique": "Historical foregrounds, Manchester recedes to body-echo"
    }
  ],

  "maitreya_foreshadowing": [
    "'We are the same' - horror indistinguishable from fascination"
  ],

  "intervention": null, // None in Ch 3 - observation only

  "word_target": 3000,
  "status": "needs_full_rewrite"
}
```

---

## Fetter Intensification Schedule

From lilith-refactor.md (authoritative):

| Ch | Weeks | Fetter Manifestation |
|----|-------|---------------------|
| 3 | Days 1-3 | "I've found a problem to solve" — analytical curiosity |
| 5 | Week 1-2 | "This intervention will work" — confident strategy |
| 7 | Week 2-3 | "I see what went wrong; I'll correct" — adjustment |
| 9 | Week 3-4 | "More precision required" — intensifying focus |
| 11 | Week 4-5 | "Why do I hesitate?" — first doubts, suppressed |
| 13 | Week 5-6 | "The pull toward him is tactical" — denial of unnamed feeling |
| 15 | Week 6-7 | "I don't feel what I'm feeling" — the pull growing |
| 17 | Week 7-8 | "One more. One more. One more." — manic persistence |
| 19 | Week 8-9 | "I will manifest fully" — total commitment, power at peak |
| 21 | Week 9-10 | "If I can't stop him, I'll bind him" — the pivot |

Key insight: "She's not falling apart—she's *crystallizing*. The attachment becomes harder, brighter, more absolute."

---

## Maitreya Foreshadowing Distribution

Need to map 0-2 subtle moments per chapter:

| Ch | Potential Foreshadowing |
|----|------------------------|
| 3 | "We are the same" - ambivalent affect |
| 5 | Brief hesitation before influencing Devaka |
| 7 | Kinship whisper extending from Ka to Philon |
| 9 | "Together doesn't hold" - mutual interference memory |
| 11 | Inexplicable hesitation, unnamed pull emerging |
| 13 | TBD - denial phase, so foreshadowing more suppressed |
| 15 | Face constancy observation (first time she notices?) |
| 17 | Dreams where she sees through his eyes |
| 19 | Moments where she loses track of which consciousness is which |
| 21 | Deciding to bind him = deciding to merge? |

---

## What's REMOVED from Old Model

Per lilith-refactor.md, these are explicitly eliminated:

1. **Patient sessions** (Gerald, David, etc.)
2. **Professional subplot** (career erosion, colleague concerns)
3. **Notebook/documentation motif**
4. **Power level progression markers**
5. **Extended Manchester-only scenes**
6. **Clinical demonstration of fetter mastery through counseling**
7. **Power tiers** (Grainy Awareness → Scene-Level → Near-Continuous)
8. **Professional decline tracking** (CP-01 through CP-10)
9. **Decade timeline** (now compressed to 8-10 weeks)

---

## What's ADDED in New Model

1. **Integrated prose technique throughout** (100% integration)
2. **Fetter intensification beats** (attachment sharpening, not power growing)
3. **Parallel structure** (her mistake mirrors avatar's mistake at different scale)
4. **Enhanced Maitreya foreshadowing**
5. **The pull toward him that exceeds strategy**
6. **Sensory bridges** connecting timelines
7. **Dominant timeline moments** (1-2 per chapter)

---

## Relationship to Other Files

### scene-manifest.json
- Already contains per-chapter requirements in new format
- lilith-chapter-manifest.json should be **extracted from scene-manifest.json** or complement it
- Scene-manifest has full chapter entries; lilith-chapter-manifest focuses on Lilith-specific requirements

### meta/lilith-arc.json
- Contains OLD power progression (needs complete overhaul per Phase 1)
- New lilith-chapter-manifest.json can supersede or complement
- May want to keep lilith-arc.json for character profile, resolution, etc.

### lilith-arc-bible.md
- Narrative/thematic guidance (competition-through-intimacy)
- Complements the manifest; manifest is structural, bible is thematic

---

## Questions to Resolve

1. **Separate file vs. embedded in scene-manifest.json?**
   - Refactor plan says "lilith-chapter-manifest.json" as separate file
   - scene-manifest.json already has detailed Lilith entries
   - Recommendation: Create lilith-chapter-manifest.json as the **Lilith-specific reference** that extracts and consolidates from scene-manifest.json

2. **Overlap with lilith-arc.json?**
   - lilith-arc.json has power_progression (obsolete) and emotional states
   - Could merge/replace or keep separate
   - Recommendation: lilith-chapter-manifest.json for structural requirements; lilith-arc.json for character profile/identity/resolution (after updating to remove power progression)

3. **Manchester settings in integrated chapters?**
   - Per lilith-refactor.md Open Questions: "Does she stay primarily in her flat? Move through the city?"
   - Current assumption: Primarily flat (tracking corner) with possible variation
   - This should be specified in manifest

4. **Intervention details?**
   - scene-manifest.json has intervention details per chapter
   - lilith-chapter-manifest.json should reference these or duplicate for completeness

---

## Implementation Notes

When creating the manifest:

1. Extract Lilith chapter data from scene-manifest.json (chapters 3, 5, 7, 9, 11, 13, 15, 17, 19, 21)
2. Add architecture/technique sections from lilith-refactor.md
3. Ensure fetter intensification matches lilith-refactor.md table
4. Ensure integration flavors match lilith-refactor.md table
5. Add Maitreya foreshadowing distribution
6. Mark status per chapter (needs_full_rewrite for all currently)
7. Cross-reference with lilith-arc-bible.md for emotional arc correctness

---

## Next Steps

1. Review this brainstorm with author
2. Decide on file structure (standalone vs. scene-manifest reference)
3. Create lilith-chapter-manifest.json with full content
4. Update CLAUDE.md reference to point to new file
5. Mark as complete in lilith-refactor.md Phase 1
