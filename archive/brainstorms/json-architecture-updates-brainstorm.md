# JSON Architecture Updates Brainstorm

**Created:** December 19, 2025
**Purpose:** Plan necessary changes to `lilith-arc.json`, `soul-constants.json`, and `scene-manifest.json` to align with the new Lilith refactor architecture
**Source:** Based on `lilith-refactor.md` and `lilith-chapter-manifest.json`

---

## Executive Summary

The Lilith refactor fundamentally changes her arc from **power progression** to **fetter intensification**, compresses the timeline from **10 years to 8-10 weeks**, and eliminates the professional decline subplot. Three JSON files need updating:

1. **`meta/lilith-arc.json`** — **COMPLETE OVERHAUL REQUIRED**
2. **`meta/soul-constants.json`** — **MODERATE UPDATES REQUIRED**
3. **`scene-manifest.json`** — **VERIFICATION PASS REQUIRED** (appears largely updated)

---

## 1. Changes Required: `meta/lilith-arc.json`

### Current State Analysis

**Structure:**
- `identity` object ✓ (mostly fine)
- `motivation` object ✓ (mostly fine)
- `power_progression` array ❌ **REMOVE ENTIRELY**
- `arc_summary` object ❌ **NEEDS MAJOR REVISION**
- `physical_description` object ✓ (fine)
- `appearance_across_lives` object ✓ (fine)
- `intervention_paradox` object ✓ (fine)
- `resolution` object ✓ (fine)
- `key_questions_resolved` array ✓ (fine)
- `questions_still_open` array ⚠ (needs minor update)
- `awareness_access_progression` array ❌ **REMOVE ENTIRELY**
- `professional_decline` array ❌ **REMOVE ENTIRELY**
- `maitreya_foreshadowing` array ⚠ (simplify/update)

### Proposed New Structure

```json
{
  "identity": { ... },  // Keep mostly as-is
  "motivation": { ... },  // Keep mostly as-is

  "spiritual_status": {
    "description": "Non-Returner (has broken 5 of 10 fetters)",
    "current_fetter": "Attachment to being 'the one who achieves Buddhahood'",
    "fetters_broken": [
      "self_illusion (sakkāya-diṭṭhi)",
      "doubt (vicikicchā)",
      "rites_rituals (sīlabbata-parāmāsa)",
      "sensual_desire (kāma-rāga)",
      "ill_will (vyāpāda)"
    ],
    "final_fetter": {
      "name": "Conceit (māna) — specifically attachment to being 'the one'",
      "manifestation": "She must be the one who achieves Buddhahood in this world-system; desperate to prevent Silas from achieving it first"
    },
    "note": "She has broken 9 of 10 fetters in various formulations; the exact count matters less than the fact that she has ONE remaining obstacle"
  },

  "cosmic_capability": {
    "description": "Full power from Chapter 3 onwards. She is a near-Buddha.",
    "constant_from": "Chapter 3",
    "capabilities": [
      "Full temporal perception (can access any point on Silas's karmic thread)",
      "Physical manifestation in historical periods (can inhabit vessels, take form)",
      "Circumstance manipulation (can influence events, people, environments)",
      "Dream influence, environmental manipulation, direct intervention"
    ],
    "constraints": [
      "Cannot override karmic law—interventions backfire structurally",
      "Cannot force Silas's choices or negate his accumulated merit",
      "Cannot change past events—can only manifest within them and influence",
      "Interventions have karmic consequences for herself (attachment intensifies)"
    ],
    "what_drives_arc": "Not power acquisition, but intensification of her final fetter—attachment to being 'the one who achieves Buddhahood'"
  },

  "timeline": {
    "tracking_period": {
      "duration": "8-10 weeks",
      "description": "Compressed fever of discovery, intervention, failure, escalation. Not a decade—a manic pursuit.",
      "chapters": [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
      "age": 28,
      "occupation": "Psychiatrist",
      "note": "No professional decline subplot; tracking is private pursuit"
    },
    "time_jump": {
      "placement": "Between Chapter 21 and Chapter 1",
      "duration": "6-12 months",
      "what_happens_offpage": [
        "Lilith locates Silas in present-day Manchester",
        "Engineers their first meeting at the university",
        "Develops intimate relationship",
        "Rebuilds composure over tracking fever",
        "Relationship becomes both tactic and (complicating) genuine feeling"
      ]
    },
    "chapter_1": {
      "age": 35,
      "description": "Established relationship with Silas; composure is performance over desperation",
      "recontextualization": "First read: established lovers. After Act II: her composure masks obsession that burned through her weeks ago."
    }
  },

  "fetter_intensification_arc": {
    "description": "Her attachment sharpens chapter by chapter. She's not falling apart—she's crystallizing. The attachment becomes harder, brighter, more absolute.",
    "arc_type": "Spiritual intensification, not power progression",

    "emotional_progression": [
      {
        "chapter": 3,
        "historical_chapter": 2,
        "avatar": "Ka",
        "tracking_timeline": "Days 1-3",
        "manifestation": "I've found a problem to solve",
        "emotional_state": "Analytical curiosity, first unnamed stirring",
        "intervention": null,
        "intervention_note": "None—this is when she first becomes aware of his pattern. Observation only.",
        "backfire": "N/A",
        "blind_spot": "Cannot see her own grasping",
        "maitreya_hints": ["'We are the same'—horror indistinguishable from fascination"]
      },
      {
        "chapter": 5,
        "historical_chapter": 4,
        "avatar": "Chandra",
        "tracking_timeline": "Week 1-2",
        "manifestation": "This intervention will work",
        "emotional_state": "Confident strategy, first backfire witnessed",
        "intervention": "Influences Devaka's betrayal to harden Chandra against trust",
        "backfire": "Betrayal teaches Chandra that generosity cannot depend on reciprocity—crystallizes lesson rather than corrupting it",
        "blind_spot": "Satisfaction at manipulation blind to the backfire pattern",
        "maitreya_hints": ["Brief hesitation before influencing Devaka—suppressed immediately"]
      },
      {
        "chapter": 7,
        "historical_chapter": 6,
        "avatar": "Philon",
        "tracking_timeline": "Week 2-3",
        "manifestation": "I see what went wrong; I'll correct",
        "emotional_state": "Adjustment, certainty intact, refining strategy",
        "intervention": "Accelerates xenophobic rumor; sends dream to Alexios to isolate Philon",
        "backfire": "Isolation crystallized rather than corrupted; concentrated karma; question became pure seed of insight",
        "blind_spot": "Recognition of kinship filed with interest, not alarm",
        "maitreya_hints": ["Kinship whisper extending from Ka to Philon", "Curiosity about kinship, not rivalry"]
      },
      {
        "chapter": 9,
        "historical_chapter": 8,
        "avatar": "Verinus",
        "tracking_timeline": "Week 3-4",
        "manifestation": "More precision required",
        "emotional_state": "Intensifying focus, first suppressed doubts",
        "intervention": "Creates competing testimonial versions, traffic delay, amplifies senator's rage",
        "backfire": "Contradictions made him humble, not cynical; exile gave permission to not know",
        "blind_spot": "Attachment to precision mirrors avatar's attachment to certainty",
        "maitreya_hints": ["Kinship deepens—parallel between his attachment to insight and her attachment to being first", "Mutual interference memory plants seed of merger necessity"]
      },
      {
        "chapter": 11,
        "historical_chapter": 10,
        "avatar": "Macarius",
        "tracking_timeline": "Week 4-5",
        "manifestation": "Why do I hesitate?",
        "emotional_state": "Driven, the unnamed pull emerging",
        "intervention": "Feeds spiritual pride through Theodora vessel",
        "backfire": "Pride becomes so obvious he finally sees it; the seeing is the breakthrough",
        "blind_spot": "Inexplicable hesitations suppressed immediately",
        "maitreya_hints": ["Inexplicable hesitation—first hint of something beyond strategy", "The unnamed pull toward him emerging"]
      },
      {
        "chapter": 13,
        "historical_chapter": 12,
        "avatar": "Kaoru",
        "tracking_timeline": "Week 5-6",
        "manifestation": "The pull toward him is tactical",
        "emotional_state": "Denial of unnamed feeling, justifying escalation, cracks appearing",
        "intervention": "Physical manifestation as The Attendant—creates 'perfect romance' to trap in realm of desire",
        "backfire": "Static perfection repels rather than binds; beauty requires impermanence",
        "blind_spot": "First physical appearance to him as object of desire",
        "maitreya_hints": ["The pull toward him exceeding strategic necessity", "Her appearance to him—first face-to-face across time"]
      },
      {
        "chapter": 15,
        "historical_chapter": 14,
        "avatar": "Diego",
        "tracking_timeline": "Week 6-7",
        "manifestation": "I don't feel what I'm feeling",
        "emotional_state": "The pull growing, manic clarity, relentless",
        "intervention": "Sustained presence as Sor Catalina—engineers Tomás's betrayal",
        "backfire": "Personal betrayal teaches about attachment to safety; releases rather than hardens",
        "blind_spot": "Sustained presence revealing depth of investment",
        "maitreya_hints": ["The pull growing beyond denial", "Sustained presence—deeper investment than strategy requires", "Face constancy observation"],
        "note": "FULCRUM CHAPTER—equidistant from Ch 3 (discovery) and Ch 1 (confession); perceives wheel is real; commits fully"
      },
      {
        "chapter": 17,
        "historical_chapter": 16,
        "avatar": "Jean",
        "tracking_timeline": "Week 7-8",
        "manifestation": "One more. One more. One more.",
        "emotional_state": "Manic persistence, exhaustion of strategies (spiritual, not physical)",
        "intervention": "Appears as Marguerite Viret—philosophical companion pushing doubt toward nihilism",
        "backfire": "Jean discovers truthfulness under uncertainty; trap becomes crucible",
        "blind_spot": "Cycling through approaches, certainty fracturing",
        "maitreya_hints": ["Exhaustion revealing the pull beneath strategy", "Persistence exceeding rational calculation"]
      },
      {
        "chapter": 19,
        "historical_chapter": 18,
        "avatar": "Wei",
        "tracking_timeline": "Week 8-9",
        "manifestation": "I will manifest fully",
        "emotional_state": "Total commitment, power at peak, final attempts",
        "intervention": "Circumstantial manipulation—adjusts artillery timing, spreads disease vectors; ensures everyone Wei saves dies anyway",
        "backfire": "By making futility visible, forces Wei to purify determination from outcome-attachment. True adhiṭṭhāna achieved.",
        "blind_spot": "Full deployment revealing obsession, not mastery",
        "maitreya_hints": ["Face to face manifestation—intimacy of opposition", "Total commitment revealing depth of attachment"]
      },
      {
        "chapter": 21,
        "historical_chapter": 20,
        "avatar": "Jack Malone",
        "tracking_timeline": "Week 9-10",
        "manifestation": "If I can't stop him, I'll bind him",
        "emotional_state": "Final failure witnessed, pivot to new strategy—the decision",
        "intervention": "MINIMAL PRESENCE. 3 brief appearances as distant observer; accelerates failures from distance; Combination plants car bomb",
        "backfire": "CATASTROPHIC: He dies with ALL TEN PERFECTIONS COMPLETE. Next life is stream-entry.",
        "blind_spot": "Intimacy strategy is the final fetter made flesh",
        "maitreya_hints": ["Inexplicable pain when causing detective suffering", "Losing track of which consciousness is which", "The pull driving the pivot to intimacy"],
        "note": "THE PIVOT—decision to meet him in present, become thing he cannot transcend"
      }
    ]
  },

  "arc_summary": {
    "act_2_structure": "Chapters 2-21 alternate historical (Silas's past lives) and Lilith (integrated prose)",
    "act_2_historical": "Chapters 2, 4, 6, 8, 10, 12, 14, 16, 18, 20—Silas develops ten perfections across 300,000 years",
    "act_2_lilith": "Chapters 3, 5, 7, 9, 11, 13, 15, 17, 19, 21—Lilith's 8-10 week tracking fever using integrated prose technique; fetter intensifies",
    "timeline_compression": "8-10 weeks of feverish tracking (Chapters 3-21), then 6-12 month gap, then Chapter 1 (established relationship)",
    "integrated_prose": "Lilith chapters hold Manchester present and historical period simultaneously—no alternating scenes, sensory bridges throughout",
    "no_professional_decline": "Tracking is private pursuit; no patient sessions, no colleague concerns, no career erosion",
    "chapter_1": "Lilith at age 35 in established relationship with Silas; composure as performance over desperation",
    "chapter_22": "All-or-nothing gambit in present day; intimate relationship as final weapon; complete failure",
    "chapters_23_25": "Post-failure recalibration; the race to Buddhahood rather than prevention",
    "chapter_26": "Resolution: souls merge to become Maitreya, the future Buddha"
  },

  "physical_description": { ... },  // Keep as-is
  "appearance_across_lives": { ... },  // Keep as-is
  "intervention_paradox": { ... },  // Keep as-is
  "resolution": { ... },  // Keep as-is

  "key_questions_resolved": [
    "What is Lilith's true nature? A rival bodhisattva, very close to enlightenment, who sees Silas as an existential threat.",
    "Why does she oppose Silas's enlightenment specifically? The one-Buddha-per-world-system rule means his success nullifies her eons of work.",
    "Does she have her own spiritual progression? Yes—she's a Non-Returner (or has broken 9 of 10 fetters), which is why she can manipulate reality. But her attachment to achieving Buddhahood is itself the obstacle.",
    "What drives her arc? Not power growth, but intensification of her final fetter—attachment to being 'the one'.",
    "What is the timeline? 8-10 weeks of tracking (Chapters 3-21), 6-12 month gap, then Chapter 1.",
    "What is the resolution? Their souls merge to become Maitreya, the future Buddha. The competition was illusory.",
    "Same face across lives? Yes—readers will recognize her before Silas does.",
    "Do her interventions work? Never. They always backfire, becoming the catalyst for his growth."
  ],

  "questions_still_open": [
    "Exact backfire mechanisms for chapters not yet developed",
    "The exact mechanism of the merger in Chapter 26",
    "Chapter 21 ending specifics: How exactly does she locate Silas in the present? What does she see? How does the chapter end on the threshold of the gambit?"
  ],

  "maitreya_foreshadowing": [
    "Moments of hesitation before interventions (she doesn't understand why)",
    "Inexplicable pain when she causes him suffering",
    "Dreams where she sees through his eyes or they appear merged",
    "The pull toward him that exceeds tactical necessity",
    "Moments where she loses track of which consciousness is which",
    "Face constancy observation (her face same across incarnations; his changes)",
    "References to loving-kindness (mettā/maitri—Maitreya's name meaning)"
  ]
}
```

### Items to REMOVE from Current File

1. **`power_progression` array** — Entire section (lines 15-141 in current file)
   - Replace with `fetter_intensification_arc` object

2. **`awareness_access_progression` array** — Entire section (lines 237-253)
   - Power tiers no longer exist; she has full access from Ch 3

3. **`professional_decline` array** — Entire section (lines 254-260)
   - No professional decline subplot in new architecture

### Items to UPDATE

1. **`identity.spiritual_status`** (line 7)
   - Current: "Non-Returner (has broken 5 of 10 fetters; final obstacle is attachment to being 'the one who achieves Buddhahood')"
   - Update: Expand into full `spiritual_status` object as shown above

2. **`arc_summary`** (lines 187-193)
   - Current mentions "decade of tracking" and "professional life declines"
   - Replace with new arc_summary as shown above

3. **Chapter 21 entry in emotional progression** (lines 124-140)
   - Current describes "femme fatale" role and "Observer with circumstantial manipulation"
   - Update to MINIMAL PRESENCE as specified in lilith-chapter-manifest.json

---

## 2. Changes Required: `meta/soul-constants.json`

### Current State Analysis

This file is simpler and mostly focused on Silas, with Lilith references scattered throughout. Main issues:

1. Line 91: `"powers": "Full presence in present timeline; decade of tracking complete"`
   - Should be: `"powers": "Full presence in present timeline; 8-10 weeks of tracking complete"`

2. The file references Lilith in historical chapter entries with OLD power progression language (e.g., "Observation only", "Remote influence", "Dream influence")
   - These need updating to reflect CONSTANT FULL POWER with constraints

### Proposed Changes

#### Update Chapter 1 Lilith entry (around line 87-93):

```json
"lilith": {
  "name": "Lilith Azami",
  "occupation": "Psychiatrist",
  "age": 35,
  "powers": "Full cosmic capability in present timeline; 8-10 weeks of tracking complete (6-12 months ago)",
  "relationship": "His lover, positioned for final intervention",
  "note": "Composure is performance over tracking fever; intimacy strategy is final fetter made flesh"
}
```

#### Update Historical Chapter Lilith entries:

For each historical chapter (2, 4, 6, 8, 10, 12, 14, 16, 18, 20), update the `lilith` object pattern:

**OLD pattern (e.g., Ch 2 - lines 180-184):**
```json
"lilith": {
  "powers": "Observation only (from future); accidental influence possible",
  "intervention": "None—this is when she first becomes aware of his pattern",
  "objective": null
}
```

**NEW pattern:**
```json
"lilith": {
  "cosmic_capability": "Full temporal perception, physical manifestation, circumstance manipulation—constrained by karmic law",
  "intervention": "None—this is when she first becomes aware of his pattern (Chapter 3 Lilith POV)",
  "objective": null,
  "backfire": null,
  "note": "Lilith has full power from the start; what escalates is her attachment, not her capability"
}
```

**For chapters WITH intervention (e.g., Ch 4):**
```json
"lilith": {
  "cosmic_capability": "Full temporal perception, physical manifestation, circumstance manipulation—constrained by karmic law",
  "intervention": "Influences Devaka's betrayal to harden Chandra against trust",
  "objective": "Sabotage development of true generosity by corrupting trusted relationships",
  "backfire": "Betrayal teaches him generosity cannot depend on reciprocity",
  "corresponding_lilith_chapter": 5
}
```

#### Update References Throughout

Search and replace:
- "decade of tracking" → "8-10 weeks of tracking"
- "age 25-35" → "age 28 during tracking"
- "Observation only" / "Remote influence" / "Dream influence" language → "Full cosmic capability constrained by karmic law"

---

## 3. Changes Required: `scene-manifest.json`

### Current State Analysis

From my read, this file appears **largely updated already**:

✅ Act 2 description (line 45) mentions:
- "integrated prose technique"
- "8-10 weeks of feverish tracking"
- "time jump of 6-12 months between Ch 21 and Ch 1"

✅ Individual Lilith chapter entries (3, 5, 7, 9, 11, 13, 15, 17, 19, 21) include:
- `"integrated_timelines": true`
- `"tracking_timeline": "Week X-Y"`
- Integration technique descriptions
- Parallel structure
- Fetter beats
- Maitreya foreshadowing

### Verification Pass Required

**Check these items:**

1. **Chapter 1 Lilith entry** (around lines 87-93)
   - Verify `"age": 35` ✓
   - Verify `"powers"` mentions tracking is complete ✓
   - Check if it needs note about 6-12 months post-tracking

2. **All Lilith chapter entries (3, 5, 7, 9, 11, 13, 15, 17, 19, 21)**
   - Verify all have `"integrated_timelines": true`
   - Verify tracking_timeline follows the schedule
   - Verify no references to "power progression" language
   - Verify all have `"cosmic_capability": "Full temporal perception..."`

3. **Historical chapter Lilith entries** (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
   - Check if Lilith's interventions are described
   - Verify language doesn't suggest power limitation
   - Ensure consistency with corresponding Lilith chapters

### Specific Updates Needed

Based on grep results, I found these that need checking:

**Chapter 3** (lines 256-329):
- ✓ Already has integrated prose structure
- ✓ Has `"cosmic_capability": "Full temporal perception, physical manifestation, circumstance manipulation—constrained by karmic law, not power"`
- ✓ Tracking timeline: "Days 1-3"

**Chapter 5** (lines 429-503):
- ✓ Already updated with integrated prose
- ✓ Has full cosmic_capability
- ✓ Tracking timeline: "Week 1-2"

**Chapter 7** (lines 794-863):
- ✓ Already updated

**Chapter 9** (lines 1201-1270):
- ✓ Already updated
- Check intervention description matches lilith-chapter-manifest

**Chapter 11** (lines 1412-1481):
- ✓ Already updated

**Chapter 13** (lines 1637-1706):
- ✓ Already updated
- Has `"title": "TBD"` — this is fine, matches lilith-chapter-manifest

**Chapters 15, 17, 19** — Similar pattern, appear updated

**Chapter 21** (lines 2544-2560+):
- Verify it includes THE PIVOT language
- Verify "Week 9-10, final historical intervention"
- Verify note about 6-12 month gap before Ch 1

### Minor Consistency Checks

1. Verify all Lilith chapters have consistent `word_target` (2500-3500)
2. Verify all have `"type": "lilith_contemporary"`
3. Verify `"genre": "Literary Fiction / Psychological / Integrated Prose"`
4. Check that Manchester location is consistently "Fallowfield flat"

---

## 4. Implementation Priority

### Phase 1: Critical Architecture (Do First)

1. **`meta/lilith-arc.json`** — Complete overhaul
   - Remove power_progression, awareness_access_progression, professional_decline
   - Add spiritual_status, cosmic_capability, timeline, fetter_intensification_arc
   - Update arc_summary
   - Update Chapter 21 entry

2. **`meta/soul-constants.json`** — Moderate updates
   - Update Chapter 1 Lilith entry (age, timeline)
   - Update all historical chapter Lilith entries (replace power language with cosmic_capability)
   - Search/replace "decade" → "8-10 weeks"

### Phase 2: Verification

3. **`scene-manifest.json`** — Verification pass
   - Verify all Lilith chapters have integrated prose structure ✓ (appears done)
   - Spot-check consistency across chapters
   - Verify Chapter 21 has THE PIVOT language
   - Verify no lingering power progression references

---

## 5. Key Terminology Changes

### OLD → NEW

| Old Term | New Term | Context |
|----------|----------|---------|
| "Power progression" | "Fetter intensification" | Arc structure |
| "Decade of tracking" | "8-10 weeks of tracking" | Timeline |
| "Age 25-35" | "Age 28 during tracking" | Lilith's age |
| "Professional decline" | [removed] | No subplot |
| "Patient sessions" | [removed] | No Gerald, David, etc. |
| "Observation only" | "Full cosmic capability constrained by karmic law" | Chapter 3 |
| "Remote influence" | "Full cosmic capability constrained by karmic law" | Chapter 5 |
| "Dream influence" | "Full cosmic capability constrained by karmic law" | Chapter 7 |
| "Circumstance manipulation" | "Full cosmic capability constrained by karmic law" | Chapter 9+ |
| "Power at peak" | "Attachment at peak" | Chapter 19-21 |
| "Grainy Awareness" | [removed] | Old power tier |
| "Scene-Level Access" | [removed] | Old power tier |
| "Near-Continuous Access" | [removed] | Old power tier |

---

## 6. Validation Checklist

After making changes, verify:

- [ ] No references to "decade" in Lilith context
- [ ] No references to "power progression" or "power levels"
- [ ] No references to "professional decline" or "patient sessions"
- [ ] All Lilith chapters show age 28
- [ ] Chapter 1 shows age 35
- [ ] All references to tracking period say "8-10 weeks"
- [ ] Time jump between Ch 21 and Ch 1 is "6-12 months"
- [ ] All interventions show "cosmic_capability" with karmic constraints
- [ ] Fetter intensification schedule matches across all files
- [ ] Chapter 21 described as THE PIVOT, not femme fatale role
- [ ] Integration technique consistently described across all Lilith chapters

---

## 7. Questions for Consideration

### Resolved by lilith-chapter-manifest.json:

✅ What is Lilith's age during tracking? **Age 28**
✅ What is her age in Chapter 1? **Age 35 (7 years older due to 6-12 month gap + some additional time)**
✅ How many perfections has she completed? **She's a Non-Returner / has broken 9 of 10 fetters**
✅ What is her capability in each chapter? **Full cosmic capability from Ch 3, constrained by karmic law**
✅ Timeline structure? **8-10 weeks (Ch 3-21), 6-12 month gap, then Ch 1**

### Still Open:

- Should `soul-constants.json` include a `lilith_constants` section mirroring Silas's structure?
  - Probably not—file is focused on Silas's soul progression
  - Lilith details live in `lilith-arc.json` and `lilith-chapter-manifest.json`

- Should historical chapters in `scene-manifest.json` have expanded `lilith` objects?
  - Currently they're minimal or absent
  - Could add brief notes about her intervention from that chapter's Lilith POV
  - Low priority—historical chapters focus on avatar

- Age arithmetic: If tracking is at age 28, and Ch 1 is 6-12 months later, why is she 35?
  - **ANSWER:** Need to clarify timeline. Options:
    1. Tracking happens at age 28, Ch 1 is age 29 (12 months later)
    2. Tracking happens at age 34, Ch 1 is age 35 (12 months later)
    3. There's a longer gap than 6-12 months
  - **CHECK:** lilith-chapter-manifest.json says age 28 during tracking
  - **CHECK:** scene-manifest.json Ch 1 says age 35
  - **POSSIBLE ISSUE:** Inconsistency between the two files OR longer time gap than stated
  - **RECOMMENDATION:** Flag this for resolution—probably tracking should be age 34, not 28

---

## 8. Open Issues & Recommendations

### Issue 1: Age Inconsistency

**Problem:**
- `lilith-chapter-manifest.json` says age 28 during tracking (Ch 3-21)
- `scene-manifest.json` Ch 1 says age 35
- Gap between Ch 21 and Ch 1 is stated as "6-12 months"
- Math doesn't work: 28 + 1 year ≠ 35

**Possible Solutions:**
1. Change tracking age to 34 in lilith-chapter-manifest.json
2. Change Ch 1 age to 29 in scene-manifest.json
3. Change gap to "6-7 years" (but this contradicts refactor intent)

**Recommendation:** Ask user for clarification before updating files.

### Issue 2: Spiritual Status Terminology

**Problem:** Different sources use different fetter counts:
- soul-constants.json line 7: "Non-Returner (has broken 5 of 10 fetters)"
- lilith-chapter-manifest.json: "broken nine of ten fetters"

**Buddhist Context:**
- Non-Returner = broken first 5 fetters (traditional)
- "9 of 10 broken" would be Arahant-adjacent (only ignorance remains)

**Recommendation:**
- Standardize on "Non-Returner" status (5 fetters broken)
- Her final fetter is attachment/conceit (māna), specifically attachment to being "the one"
- Update all references for consistency

### Issue 3: Chapter 21 Minimal Presence

**Status:** Already resolved in lilith-chapter-manifest.json
- NOT femme fatale
- 3 brief appearances as distant observer
- Combination plants car bomb, not Lilith

**Action:** Verify soul-constants.json Ch 20 entry doesn't describe her as femme fatale

---

## 9. File-by-File Summary

### `meta/lilith-arc.json`
**Status:** ❌ **COMPLETE OVERHAUL REQUIRED**
**Work Required:** Heavy
**Estimated Changes:** ~70% of file content
**Priority:** 🔴 **CRITICAL** — Do first

**Major Changes:**
- Remove 3 entire sections (power_progression, awareness_access_progression, professional_decline)
- Add 4 new sections (spiritual_status, cosmic_capability, timeline, fetter_intensification_arc)
- Rewrite arc_summary
- Update motivation/identity slightly

### `meta/soul-constants.json`
**Status:** ⚠ **MODERATE UPDATES REQUIRED**
**Work Required:** Medium
**Estimated Changes:** ~20-30% of Lilith-related content
**Priority:** 🟡 **HIGH** — Do second

**Major Changes:**
- Update Ch 1 Lilith entry (age, timeline reference)
- Update all 10 historical chapter Lilith entries (capability language)
- Search/replace timeline references
- Verify no power progression language

### `scene-manifest.json`
**Status:** ✅ **MOSTLY COMPLETE — VERIFICATION NEEDED**
**Work Required:** Light
**Estimated Changes:** <5% — spot fixes only
**Priority:** 🟢 **MEDIUM** — Verify third

**Major Changes:**
- Verify consistency across all Lilith chapters (appears already done)
- Check Chapter 21 for THE PIVOT language
- Verify no lingering old terminology
- Resolve age inconsistency if present

---

## Next Steps

1. **Resolve open questions:**
   - Age arithmetic (28 vs 35)
   - Spiritual status terminology (5 fetters vs 9 fetters)

2. **Implement changes in order:**
   - Phase 1: `meta/lilith-arc.json` (complete overhaul)
   - Phase 2: `meta/soul-constants.json` (moderate updates)
   - Phase 3: `scene-manifest.json` (verification pass)

3. **Validation:**
   - Run checklist in Section 6
   - Cross-reference all three files for consistency
   - Ensure alignment with `lilith-refactor.md` and `lilith-chapter-manifest.json`

4. **Document:**
   - Update novel-progress.txt with architectural changes
   - Note any remaining open questions
   - Flag for review before implementing chapter rewrites

---

**END OF BRAINSTORM**
