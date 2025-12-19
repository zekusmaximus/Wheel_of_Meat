# Scene Manifest Revision Brainstorm: Resetting Lilith Chapters

**Date:** December 19, 2025
**Purpose:** Detailed plan for revising all Lilith chapter entries in `scene-manifest.json` to align with `lilith-refactor.md`
**Scope:** Chapters 3, 5, 7, 9, 11, 13, 15, 17, 19, 21
**Approach:** **Return to beginning state** — complete architectural reset

---

## Core Concept: Return to Beginning State

We're **resetting** all Lilith chapters to a beginning state that reflects the new architectural decisions:

- **FROM:** 10-year timeline with power progression, patient scenes, professional decline
- **TO:** 8-10 week fever with full power from start, integrated prose, fetter intensification

This is a **complete architectural overhaul**, not incremental revisions. Every Lilith chapter entry needs to be rebuilt from scratch.

---

## Universal Changes Across All Lilith Chapters (3-21)

### 1. Timeline Compression

**OLD PATTERN:**
```json
"year": "10 years before Chapter 1"  // Ch 3
"year": "9 years before Chapter 1"   // Ch 5
"year": "8 years before Chapter 1"   // Ch 7
// ... declining by 1 year each chapter
"year": "1 year before Chapter 1"    // Ch 21
```

**NEW PATTERN:**
```json
"year": "Approximately 6-12 months before Chapter 1",
"tracking_timeline": {
  "time_since_discovery": "Days 1-3",
  "tracking_week": "Discovery period"
}
```

All chapters 3-21 happen within **8-10 weeks** (compressed tracking period), then there's a **6-12 month gap** before Chapter 1.

**Specific timeline by chapter (from refactor doc):**

| Chapter | Time Since Discovery | Emotional State                           |
|---------|---------------------|-------------------------------------------|
| 3       | Days 1-3            | Curiosity, recognition                    |
| 5       | Week 1-2            | First intervention, first backfire, still confident |
| 7       | Week 2-3            | Adjusting strategy, certainty intact      |
| 9       | Week 3-4            | Intensifying focus, first suppressed doubts |
| 11      | Week 4-5            | Driven, the unnamed pull emerging         |
| 13      | Week 5-6            | Committed, cracks appearing               |
| 15      | Week 6-7            | Relentless, manic clarity                 |
| 17      | Week 7-8            | Exhaustion of strategies, not body        |
| 19      | Week 8-9            | Full manifestation attempts               |
| 21      | Week 9-10           | Final failure, the pivot to present-day gambit |

### 2. Age Consistency

**OLD:** Lilith ages from 25 to 35 across chapters
**NEW:** Lilith stays approximately the same age (28-29) since all chapters happen within weeks

```json
"age": 28  // consistent across all Lilith chapters 3-21
```

### 3. Remove "years_tracking" Field

**OLD:**
```json
"years_tracking": 0,  // Ch 3
"years_tracking": 1,  // Ch 5
```

**NEW:**
```json
"weeks_into_tracking": "Days 1-3",     // Ch 3
"weeks_into_tracking": "Week 1-2",     // Ch 5
```

### 4. Replace Power Progression with Fetter Intensification

**REMOVE these fields:**
- `"power_level": "Observation only"`
- `"power_level": "Remote influence"`
- `"capabilities": [...]` (with progressive lists)
- `"limitations": [...]` (that suggest growing power)

**REPLACE with:**
```json
"lilith": {
  "age": 28,
  "occupation": "Psychiatrist",
  "cosmic_capability": "Full power from start—temporal perception, physical manifestation, circumstance manipulation",
  "constraints": [
    "Cannot override karmic law",
    "Cannot force choices or negate accumulated merit",
    "Interventions backfire structurally, not due to power limits"
  ],
  "fetter_state": {
    "attachment_manifestation": "I've found a problem to solve",
    "emotional_state": "Curiosity, recognition",
    "blind_spot": "Cannot see her own grasping"
  }
}
```

**Fetter progression by chapter (from refactor doc):**

| Chapter | Fetter Manifestation                                      | Emotional State                           |
|---------|----------------------------------------------------------|-------------------------------------------|
| 3       | "I've found a problem to solve"                          | Curiosity, recognition                    |
| 5       | "This intervention will work"                            | Confident strategy, first backfire        |
| 7       | "I see what went wrong; I'll correct"                    | Adjustment, certainty intact              |
| 9       | "More precision required"                                | Intensifying focus                        |
| 11      | "Why do I hesitate?"                                     | First doubts, suppressed                  |
| 13      | "The pull toward him is tactical"                        | Denial of unnamed feeling                 |
| 15      | "I don't feel what I'm feeling"                          | The pull growing                          |
| 17      | "One more. One more. One more."                          | Manic persistence                         |
| 19      | "I will manifest fully"                                  | Total commitment, power at peak           |
| 21      | "If I can't stop him, I'll bind him"                     | The pivot to present-day gambit           |

### 5. Setting Field: Include BOTH Timelines

**OLD:**
```json
"setting": {
  "period": "Contemporary",
  "location": "Manchester, UK",
  "year": "X years before Chapter 1"
}
```

**NEW:**
```json
"setting": {
  "integrated_timelines": true,
  "manchester": {
    "period": "Contemporary",
    "location": "Manchester, UK (primarily her Fallowfield flat)",
    "year": "6-12 months before Chapter 1",
    "tracking_timeline": "Days 1-3 of compressed tracking period"
  },
  "historical": {
    "period": "Prehistoric",
    "location": "Jebel Irhoud, Morocco",
    "year": "300,000 BCE",
    "avatar": "Ka"
  },
  "integration_technique": "Primal, sensory, non-verbal—kettle scream/wind scream, tea warmth/fire warmth"
}
```

### 6. Remove Patient Demonstration Scenes

**DELETE entire sections like:**
```json
"demonstration": {
  "fetter": "Generosity (dāna)",
  "scene": "Gives up chair to anxious first-year student",
  "patient": {...}
}
```

**REPLACE with:**
```json
"spiritual_advancement_shown_through": [
  "Capability to hold two timelines simultaneously",
  "Ironic parallels between her mistakes and avatar's mistakes",
  "Fetter intensification beat"
]
```

### 7. Remove Professional/Family Subplots

**DELETE references to:**
- Career progression/erosion
- Colleagues' concerns
- Professional relationships
- Family dynamics (mother's wedding, sister Nadia, etc.)
- Clinical work details

### 8. Update Scene Structure

**OLD:**
```json
"scenes": [
  {"section": "I", "title": "Manchester Morning", ...},
  {"section": "II", "title": "Patient Session", ...},
  {"section": "III", "title": "Tracking Corner", ...},
  // 5-6 separate scenes
]
```

**NEW:**
```json
"structure": {
  "technique": "Integrated prose throughout",
  "components": [
    "Manchester and historical timelines held simultaneously via sensory bridges",
    "1-2 pivotal moments where one timeline dominates",
    "One clear fetter intensification beat",
    "0-2 Maitreya foreshadowing moments"
  ]
},
"scenes": [],
"status": "needs_full_rewrite"
```

### 9. Update Word Targets

**OLD:** 3,500-4,500 words
**NEW:** 2,500-3,500 words

```json
"word_target": 3000
```

### 10. Update Chapter Functions

**REMOVE references to:**
- "First intervention" (she has full power from start)
- "Realizes she can DO things"
- Professional subplot advancement
- Patient parallels

**ADD references to:**
- Fetter intensification
- Intervention backfire
- Parallel structure (her mistake mirrors avatar's)
- Integrated experience

---

## Chapter-Specific Updates

### Chapter 3: "The Discovery"

**Current state:** Graduate student, observation only, first discovery of Ka

**New state:**
- Days 1-3 of tracking
- Full cosmic power, just discovered Silas's thread
- Integrated with Ka's prehistoric Morocco
- Fetter: "I've found a problem to solve"

**Proposed new entry:**
```json
{
  "chapter": 3,
  "id": "ch03-lilith-cp01",
  "title": "The Discovery",
  "type": "lilith_contemporary",
  "genre": "Literary Fiction / Psychological / Integrated Prose",
  "setting": {
    "integrated_timelines": true,
    "manchester": {
      "period": "Contemporary",
      "location": "Fallowfield flat, Manchester, UK",
      "year": "6-12 months before Chapter 1",
      "tracking_timeline": "Days 1-3, Discovery period"
    },
    "historical": {
      "period": "Prehistoric",
      "location": "Jebel Irhoud, Morocco",
      "year": "300,000 BCE",
      "avatar": "Ka"
    },
    "integration_technique": "Primal, sensory, non-verbal—kettle scream/wind scream, tea warmth/fire warmth, silence/silence"
  },
  "pov": "Lilith (integrated with Ka's experience)",
  "lilith": {
    "age": 28,
    "occupation": "Psychiatrist",
    "weeks_into_tracking": "Days 1-3",
    "cosmic_capability": "Full temporal perception, physical manifestation, circumstance manipulation—constrained by karmic law, not power",
    "constraints": [
      "Cannot override karmic law—interventions backfire structurally",
      "Cannot force choices or negate accumulated merit",
      "Cannot change past events, only manifest within them and influence"
    ],
    "fetter_state": {
      "attachment_manifestation": "I've found a problem to solve",
      "emotional_state": "Analytical curiosity, first unnamed stirring",
      "blind_spot": "Cannot see her own grasping"
    }
  },
  "corresponds_to": {
    "historical_chapter": 2,
    "avatar": "Ka",
    "lesson": "Loving-kindness (mettā) / Cooperation"
  },
  "parallel_structure": {
    "ka_mistake": "Hoarding meat, choosing isolation over tribe, calling alone-way 'strength'",
    "lilith_mistake": "Hoarding capability, choosing solitary tracking over connection, calling isolation 'strategic'",
    "recognition_moment": "'We are the same'—horrifying and fascinating"
  },
  "integrated_prose_features": {
    "sensory_bridges": ["Kettle scream / wind scream", "Tea warmth / fire warmth", "Flat silence / cave silence"],
    "pronoun_flow": "She for Lilith throughout; Ka's sensations register in her body",
    "temporal_markers": "Three hundred thousand years before, embedded naturally",
    "no_transitions": "Scene doesn't cut between Manchester and Morocco—holds both"
  },
  "pivotal_moments": [
    {
      "dominant_timeline": "Historical",
      "moment": "Ka's death—hoarding meat in isolation, desperate hunger to understand giving",
      "technique": "Historical foreground, Manchester recedes to body-echo"
    }
  ],
  "fetter_beat": {
    "moment": "Decision to continue tracking despite recognition of shared isolation",
    "shown_through": "Action/choice, not stated—she drinks cold tea and stays in her tracking corner"
  },
  "maitreya_foreshadowing": [
    "The thought 'We are the same' and its ambivalent affect—horror indistinguishable from fascination"
  ],
  "spiritual_advancement_shown_through": [
    "Capability to access karmic thread and perceive Ka's entire life",
    "Ability to hold Manchester present and prehistoric past simultaneously",
    "Perfect understanding of Ka's attachment while blind to her own identical pattern"
  ],
  "function": "Discovery of Silas's thread; first integrated experience; recognition of kinship; decision to track",
  "word_target": 3000,
  "scenes": [],
  "status": "needs_full_rewrite"
}
```

**Delete from current entry:**
- All separate scene entries (scene-01-manchester-morning.md, scene-02-patient-session.md, etc.)
- Patient demonstration scene (anxious first-year student)
- Graduate student context
- "years_tracking": 0
- "power_level": "Observation only"
- "tracks_forward_to": "Chandra" (this is implicit)

---

### Chapter 5: "The Ledger's Shadow" → Title TBD

**Current state:** Year 1 tracking, remote influence power, first intervention

**New state:**
- Week 1-2 of tracking
- Full power (always could intervene)
- Integrated with Chandra's Mauryan India
- Fetter: "This intervention will work"

**Key changes:**
```json
{
  "chapter": 5,
  "id": "ch05-lilith-cp02",
  "title": "TBD",
  "setting": {
    "integrated_timelines": true,
    "manchester": {
      "tracking_timeline": "Week 1-2"
    },
    "historical": {
      "period": "Ancient",
      "location": "Mauryan Empire, India",
      "year": "268-232 BCE",
      "avatar": "Chandra"
    },
    "integration_technique": "Bureaucratic, ledgers and rain, political weight—record-keeping bleeding across timelines"
  },
  "lilith": {
    "age": 28,
    "weeks_into_tracking": "Week 1-2",
    "fetter_state": {
      "attachment_manifestation": "This intervention will work",
      "emotional_state": "Confident strategy, first backfire witnessed",
      "escalation": "From observation to deliberate interference"
    }
  },
  "parallel_structure": {
    "chandra_mistake": "Incomplete generosity—saving ledgers while people burn, transactional giving",
    "lilith_mistake": "Strategic withholding, calculated interventions, treating tracking as ledger to balance"
  },
  "intervention": {
    "method": "Influences Devaka's betrayal to harden Chandra against trust",
    "objective": "Sabotage development of true generosity by corrupting trusted relationships",
    "backfire": "Betrayal teaches Chandra that generosity cannot depend on reciprocity—crystallizes the lesson rather than corrupting it"
  },
  "status": "needs_full_rewrite"
}
```

**Delete:**
- All patient demonstration content
- Power progression language
- Separate scene files
- "First deliberate interference" language (implies she couldn't before)

---

### Chapter 7: "The Dream-Walker" → Title TBD

**Current state:** Years 2-3, dream influence power, David patient, family wedding subplot

**New state:**
- Week 2-3 of tracking
- Full power (always could influence dreams)
- Integrated with Philon's Athens
- Fetter: "I see what went wrong; I'll correct"

**MAJOR DELETIONS:**
- **Entire family dynamics section** (mother's wedding to Jeff, sister Nadia subplot)
- **David patient** (caregiver guilt, mother Marsha)
- **Clinical demonstration scene**
- **Progressive dream power capabilities**

**Key changes:**
```json
{
  "chapter": 7,
  "id": "ch07-lilith-cp03",
  "title": "TBD",
  "setting": {
    "integrated_timelines": true,
    "historical": {
      "period": "Classical Athens",
      "year": "430 BCE",
      "avatar": "Philon"
    },
    "integration_technique": "Philosophical, dialogue bleeding through, ideas as sensation—Socratic questions in two keys"
  },
  "lilith": {
    "age": 28,
    "weeks_into_tracking": "Week 2-3",
    "fetter_state": {
      "attachment_manifestation": "I see what went wrong; I'll correct",
      "emotional_state": "Adjustment, certainty intact, refining strategy"
    }
  },
  "parallel_structure": {
    "philon_mistake": "Conflates selflessness with self-destruction, martyrdom compulsion, cannot distinguish service from suicide",
    "lilith_mistake": "Compulsive tracking, cannot stop even when recognizing kinship, sacrifice of everything to this pursuit"
  },
  "intervention": {
    "method_1": "Accelerates xenophobic rumor—plague from Persian ships",
    "method_2": "Sends dream to Alexios—abandons Philon to face final choice alone",
    "backfire_witnessed": "Isolation crystallized Philon's insight rather than corrupting it; concentrated karma; question 'Was the one for them or for me?' became pure seed"
  },
  "recognition": {
    "moment": "Watching Philon die, recognizes something of herself—same driven quality",
    "emotional_register": "Curious, not alarmed—a near-enlightened being doesn't rattle",
    "the_whisper": "Could they be on the same journey? Not rivals but fellow travelers?",
    "response": "Files it with interest; doesn't dismiss but doesn't dwell"
  },
  "status": "needs_full_rewrite"
}
```

---

### Chapter 9: Ch09-lilith-cp04

**New state:**
- Week 3-4 of tracking
- Integrated with Verinus's Rome
- Fetter: "More precision required"
- Integration: Procedural, investigation layered on investigation

---

### Chapter 11: Ch11-lilith-cp05

**New state:**
- Week 4-5 of tracking
- Integrated with Macarius's desert
- Fetter: "Why do I hesitate?"
- Integration: Ascetic, emptiness against emptiness, silence doubled
- First inexplicable hesitations before interventions

---

### Chapter 13: Ch13-lilith-cp06

**Current state:** Marked "needs_development", Heian courtier, brief manifestation, 5 years tracking

**New state:**
- Week 5-6 of tracking
- Integrated with Kaoru's Heian Japan
- Fetter: "The pull toward him is tactical"
- Integration: Aesthetic, beauty saturating both frames, longing amplified

**Key changes:**
```json
{
  "chapter": 13,
  "id": "ch13-lilith-cp06",
  "title": "TBD",
  "setting": {
    "integrated_timelines": true,
    "historical": {
      "period": "Heian Japan",
      "year": "~1000 CE",
      "avatar": "Kaoru"
    },
    "integration_technique": "Aesthetic, beauty saturating both frames, longing amplified—mono no aware in dual register"
  },
  "lilith": {
    "age": 28,
    "weeks_into_tracking": "Week 5-6",
    "fetter_state": {
      "attachment_manifestation": "The pull toward him is tactical",
      "emotional_state": "Denial of unnamed feeling, justifying escalation",
      "complication": "First appearance to him as object of desire"
    }
  },
  "intervention": {
    "method": "Physical manifestation as object of desire",
    "appearance": "Dark hair with widow's peak, single darker strand escaping over left side; pale-green crescent in left eye",
    "readers_recognize": "Same face readers have seen before; Kaoru doesn't"
  },
  "parallel_structure": {
    "kaoru_mistake": "Aesthetic longing becomes attachment, confuses beauty with transcendence",
    "lilith_mistake": "Unnamed pull toward him exceeding tactical necessity, denying what she feels"
  },
  "status": "needs_full_rewrite"
}
```

**Delete:**
- "years_tracking": 5
- "power_level": "Brief manifestation"
- "First physical manifestation" language (she could always manifest)
- "Colleagues notice she's distracted" (no professional subplot)
- "Manifestation drains her for days" (physical exhaustion is mortal response, not near-Buddha)

---

### Chapter 15: Ch15-lilith-cp07

**New state:**
- Week 6-7 of tracking
- Integrated with Diego's Inquisition Toledo
- Fetter: "I don't feel what I'm feeling"
- Integration: Claustrophobic, persecution in two keys
- The pull exceeding tactical necessity

---

### Chapter 17: Ch17-lilith-cp08

**New state:**
- Week 7-8 of tracking
- Integrated with Renaissance avatar
- Fetter: "One more. One more. One more."
- Integration: Intellectual, wit and doubt, skepticism layered
- Manic persistence, exhaustion of strategies (spiritual, not physical)

---

### Chapter 19: Ch19-lilith-cp09

**New state:**
- Week 8-9 of tracking
- Integrated with Taiping rebellion avatar
- Fetter: "I will manifest fully"
- Integration: Chaotic, violence bleeding through, conviction fractured
- Total commitment, power at peak

---

### Chapter 21: "The Commitment" → "The Pivot"

**CRITICAL REVISION:** This chapter's current content is COMPLETELY WRONG for the new structure.

**Current state (INCORRECT):**
- 1 year before Chapter 1
- Shows established relationship with Silas
- Intimacy strategy in Phase 4
- Domestic scenes, merger dreams, lovers' paradox
- Multiple scenes showing established intimacy

**Correct new state:**
- Week 9-10 of tracking (NOT 1 year before)
- Final historical intervention (noir detective) FAILS
- Ends with THE PIVOT to present-day gambit
- NO relationship with present-day Silas yet (hasn't met him)
- Fetter: "If I can't stop him, I'll bind him"

**Proposed new entry:**
```json
{
  "chapter": 21,
  "id": "ch21-lilith-cp10",
  "title": "The Pivot",
  "type": "lilith_contemporary",
  "genre": "Literary Fiction / Noir / Integrated Prose",
  "setting": {
    "integrated_timelines": true,
    "manchester": {
      "tracking_timeline": "Week 9-10, final historical intervention"
    },
    "historical": {
      "period": "1930s noir",
      "location": "American city",
      "year": "~1935",
      "avatar": "Detective"
    },
    "integration_technique": "Atmospheric, cigarette smoke and rain, failure repeated—noir atmosphere bleeding across timelines"
  },
  "pov": "Lilith (integrated with noir detective experience)",
  "lilith": {
    "age": 28,
    "weeks_into_tracking": "Week 9-10",
    "fetter_state": {
      "attachment_manifestation": "If I can't stop him, I'll bind him",
      "emotional_state": "Final failure witnessed, pivot to new strategy",
      "the_decision": "Cannot stop him from outside—must meet him in the present, make him love her, become indispensable"
    }
  },
  "corresponds_to": {
    "historical_chapter": 20,
    "avatar": "1930s Detective",
    "lesson": "Perseverance (viriya)"
  },
  "intervention": {
    "method": "Full manifestation as femme fatale—face to face in noir detective story",
    "objective": "Final attempt to corrupt his perseverance",
    "backfire": "Femme fatale becomes the case he must solve; her opposition sharpens his determination",
    "the_failure": "Face to face manifestation, all power deployed, still backfires"
  },
  "parallel_structure": {
    "detective_mistake": "Obsessive pursuit of case consuming everything else",
    "lilith_mistake": "Obsessive pursuit of him consuming everything else, manic 'one more, one more'"
  },
  "chapter_ending": {
    "realization": "Cannot stop him from historical interventions—pattern is clear, all backfire",
    "traces_thread_forward": "Follows karmic thread to present-day Manchester",
    "discovery": "Finds Silas Pahlavan, philosophy professor, approaching stream-entry",
    "decision": "Will meet him in the flesh, make him love her, become the thing he cannot transcend",
    "final_beat": "On the threshold of the final gambit",
    "final_image": "TBD—her tracking corner, the thread glowing forward to now, the pivot from past to present"
  },
  "time_jump_note": "6-12 months pass between end of this chapter and Chapter 1. During this gap: she locates Silas, engineers their meeting, develops intimate relationship, rebuilds composure over tracking fever. The relationship becomes both tactic and (complicating) genuine feeling.",
  "maitreya_foreshadowing": [
    "Inexplicable pain when causing detective suffering",
    "Moment of losing track of which consciousness is which during confrontation",
    "The pull toward him that has grown beyond strategy"
  ],
  "function": "Final historical intervention fails; realization she must meet him in present; the pivot that sets up Chapter 1; end of compressed tracking period",
  "word_target": 3500,
  "structure": {
    "technique": "Integrated prose—noir rain, cigarette smoke, shadowed alleys bleeding across Manchester present",
    "pivotal_moment": "The confrontation with detective where full manifestation still backfires",
    "fetter_beat": "The decision to pivot—attachment crystallizing into final gambit",
    "transition": "From historical interventions to present-day intimacy strategy"
  },
  "scenes": [],
  "status": "needs_complete_reconception"
}
```

**DELETE ENTIRELY from current entry:**
- All established relationship content
- Intimacy strategy Phase 4 descriptions
- All current scene files (scene-01-established-orbit.md, scene-02-conversation.md, etc.)
- Merger dream content
- Domestic intimacy scenes
- Maitreya foreshadowing about completing sentences (too advanced for this timeline)
- References to "one year later" and university position
- All content showing them as lovers

**This chapter hasn't happened yet in the new timeline!**

---

## Act 2 Description Update

**Current:**
```json
{
  "act": 2,
  "title": "The Wheel Turns",
  "description": "Ten historical past lives alternating with ten contemporary Lilith chapters. Silas develops perfections while Lilith's powers grow and her pursuit intensifies over a decade.",
  "structure": "Historical → Lilith → Historical → Lilith (alternating)"
}
```

**New:**
```json
{
  "act": 2,
  "title": "The Wheel Turns",
  "description": "Ten historical past lives alternating with ten Lilith chapters using integrated prose technique. Silas develops perfections across 300,000 years while Lilith's final fetter intensifies over 8-10 weeks of feverish tracking. Each Lilith chapter holds Manchester present and historical period simultaneously.",
  "structure": "Historical → Lilith (integrated) → Historical → Lilith (integrated) — alternating",
  "timeline_note": "Historical chapters span 300,000 years; Lilith chapters span 8-10 weeks; time jump of 6-12 months between Ch 21 and Ch 1"
}
```

---

## Fields to Remove Entirely

Across ALL Lilith chapters, delete these fields:

1. ✅ `"years_tracking"` → Replace with `"weeks_into_tracking"`
2. ✅ `"power_level"` → Replace with constant `"cosmic_capability"`
3. ✅ `"capabilities": [...]` when it shows progression
4. ✅ `"limitations": [...]` when they're about power rather than karmic law
5. ✅ `"demonstration": {...}` (patient scenes)
6. ✅ `"patient": {...}` (any patient character details)
7. ✅ `"family_dynamics": {...}` (mother/sister subplots—Ch 7)
8. ✅ `"professional_cost"` or `"physical_cost"` (unless reframed as spiritual)
9. ✅ Individual `"scenes": [...]` arrays with separate scene files
10. ✅ `"backfire_awareness"` as progression (she witnesses backfires throughout)
11. ✅ `"timespan"` in setting (irrelevant for week-long tracking)
12. ✅ References to specific ages changing (25, 26, 27, 28, 30, 34, 35)
13. ✅ `"occupation"` changing (graduate student → established psychiatrist)
14. ✅ `"physical_deterioration"` or fatigue mentions

---

## Fields to Add

Across ALL Lilith chapters, add these fields:

1. ✅ `"integrated_timelines": true` in setting
2. ✅ `"historical": {...}` nested in setting (location, avatar, period details)
3. ✅ `"integration_technique": "..."` describing specific flavor for this period
4. ✅ `"fetter_state": {...}` with manifestation, emotional state, blind spot
5. ✅ `"parallel_structure": {...}` showing avatar's mistake // Lilith's mistake
6. ✅ `"maitreya_foreshadowing": [...]` (0-2 moments per chapter, increasing)
7. ✅ `"weeks_into_tracking"` or similar timeline marker
8. ✅ `"cosmic_capability"` (constant across all chapters)
9. ✅ `"constraints"` (karmic law, not power limits)
10. ✅ `"spiritual_advancement_shown_through": [...]`
11. ✅ `"intervention": {...}` with method, objective, backfire
12. ✅ `"pivotal_moments": [...]` where timeline dominates
13. ✅ `"fetter_beat": {...}` showing the intensification moment
14. ✅ `"integrated_prose_features": {...}` (sensory bridges, pronoun flow, etc.)

---

## Summary of the Reset

We're **throwing out** the entire current Lilith chapter structure and **starting fresh** with:

1. **Compressed timeline:** 8-10 weeks total (not 10 years)
2. **Integrated prose:** Both timelines in every paragraph
3. **Full power from start:** No progression, just fetter intensification
4. **No patient scenes:** No demonstrations, no clinical parallels
5. **No professional subplot:** No career, minimal Manchester setting
6. **No family subplot:** No mother/Jeff wedding, no sister Nadia
7. **Shorter chapters:** 2,500-3,500 words (down from 3,500-4,500)
8. **Parallel structure:** Her cosmic-scale mistakes mirror avatar's human-scale mistakes
9. **Chapter 21 pivot:** Ends BEFORE meeting present-day Silas, not after relationship established
10. **Age consistency:** Same age (28) throughout all Lilith chapters
11. **No physical deterioration:** Spiritual intensification, not somatic collapse

---

## Special Note: Chapter 21

Chapter 21 requires the most dramatic reconception. Its current content shows:
- Established romantic relationship with Silas
- University colleagues
- Domestic intimacy scenes
- Merger dreams
- "One year before Chapter 1" timeline

**ALL OF THIS IS WRONG for the new structure.**

Chapter 21 should show:
- Week 9-10 of tracking
- Final historical intervention (noir detective)
- The intervention FAILING despite full manifestation
- The PIVOT decision: "I must meet him in the present"
- Ends on threshold of new gambit
- NO present-day Silas contact yet

The current Chapter 21 content belongs to the **6-12 month gap** between Ch 21 and Ch 1, which happens OFF-PAGE.

---

## Next Steps

**Recommendation:**

1. Create a **template JSON structure** for new Lilith chapters
2. Apply systematically to chapters 3, 5, 7, 9, 11, 13, 15, 17, 19, 21
3. Update Act 2 description
4. Add timeline note about gap between Ch 21 and Ch 1
5. Update `"status"` for all Lilith chapters to `"needs_full_rewrite"` or `"needs_complete_reconception"`

**Question for user:**

Ready to proceed with creating the template and systematically updating all ten Lilith chapter entries? Should we tackle them all at once or one at a time?

---

**This is a complete architectural reset, not incremental revision.**
