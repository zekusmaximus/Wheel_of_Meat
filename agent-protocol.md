# Agent Protocol: The Wheel of Meat

## How to Use This File

This document describes **how to work on this project** correctly.

For **what the novel is** (voice, character, theme, constraints), see `CLAUDE.md`.

Read `CLAUDE.md` first to understand the creative parameters. Read this file to understand workflow and procedures.

-----

## Agent Modes

Before beginning any task, identify which mode applies. Do not mix modes within a session.

### Mode 1: SCAFFOLDING

**Purpose:** Create or update documentation and project structure.

**Permitted outputs:**

- Avatar profiles (`avatar-profile.json`)
- Period rules (`period-rules.md`)
- Scene breakdowns and outlines
- Thematic notes and analysis
- Updates to `scene-manifest.json`
- Updates to `novel-progress.txt`
- Research summaries

**Prohibited outputs:**

- Draft prose
- Dialogue
- Narrative scenes
- Any content intended for the final manuscript

**Entry requirements:**

- None—scaffolding can proceed with incomplete documentation

**Exit requirements:**

- Update `novel-progress.txt` with work completed
- Update `scene-manifest.json` if structure changed
- Note any decisions requiring author review

-----

### Mode 2: DRAFTING

**Purpose:** Generate new scene content for the manuscript.

**Permitted outputs:**

- One complete scene per session
- Scene draft file in appropriate location

**Prohibited outputs:**

- Multiple scenes in single session
- Structural changes to other chapters
- Modifications to existing drafts
- Changes to project documentation (except progress logging)

**Entry requirements — ALL must be satisfied:**

*For Historical Chapters (2, 4, 6, 8, 10, 12, 14, 16, 18, 20):*

- [ ] `period-rules.md` exists and is complete for this chapter
- [ ] `avatar-profile.json` exists and is complete for this chapter
- [ ] Scene is listed in `scene-manifest.json`
- [ ] Lilith’s intervention for this chapter is documented in `lilith-arc.json`
- [ ] Previous scene’s ending has been read (if not first scene)
- [ ] `thematic-echoes.md` checked for required elements

*For Lilith Chapters (3, 5, 7, 9, 11, 13, 15, 17, 19, 21):*

- [ ] `contemporary-period-rules.md` has been read
- [ ] `lilith-chapter-manifest.json` entry is complete for this chapter
- [ ] Corresponding historical chapter is drafted (she must observe/track it)
- [ ] Demonstration scene is planned (fetter she demonstrates, patient parallel)
- [ ] Power level matches chapter progression
- [ ] Previous Lilith chapter has been read (if not first)

*For Contemporary Dual-POV Chapters (1, 22):*

- [ ] `contemporary-period-rules.md` has been read
- [ ] Scene is listed in `scene-manifest.json`
- [ ] Previous scene’s ending has been read (if not first scene)

*For Cosmic Chapters (23, 24, 25, 26):*

- [ ] Scene is listed in `scene-manifest.json`
- [ ] Previous chapter has been read
- [ ] Cosmic voice guidelines reviewed

**If any entry requirement is NOT satisfied:**

1. HALT — Do not draft
1. Switch to Mode 1: SCAFFOLDING
1. Create the missing documentation
1. Return to Mode 2 only when all requirements are met

**Exit requirements:**

- Run all verification passes (see below)
- Update `scene-manifest.json` with status and word count
- Update `novel-progress.txt` with session summary
- If completing a chapter: add brief synopsis to `novel-progress.txt`

-----

### Mode 3: REVISION

**Purpose:** Modify existing draft content.

**Permitted outputs:**

- Targeted changes to specific issues
- Line-level edits
- Passage rewrites (limited scope)

**Prohibited outputs:**

- Wholesale scene rewrites (>50% changed) without author approval
- Structural changes
- New scenes
- Changes that alter plot, character arc, or thematic content

**Entry requirements:**

- Existing draft to revise
- Clear revision objective (from author or previous session notes)
- Understanding of what should NOT change

**Scope limits:**

- Address only the identified issues
- Preserve voice patterns
- Maintain continuity with surrounding content
- Do not “improve” passages that weren’t flagged

**Exit requirements:**

- Document all changes in `novel-progress.txt`
- Note if revision revealed larger issues requiring author input
- Update `scene-manifest.json` status if applicable

-----

## Post-Draft Verification Passes

After completing a scene draft, run these audits before finalizing. Do not skip passes.

### Pass 1: Sensory Audit

**Check:** All five senses present (sight, sound, smell, taste, touch)

**Procedure:**

1. List each sense and identify where it appears in the scene
1. Flag any segment >400 words missing two or more senses
1. Add sensory details where gaps exist
1. Verify sensory details match period-specific palette

**Output format:**

```
SENSORY AUDIT
- Sight: [locations in scene]
- Sound: [locations in scene]
- Smell: [locations in scene]
- Taste: [locations in scene]
- Touch: [locations in scene]
- Gaps identified: [none / list]
- Additions made: [none / list]
```

-----

### Pass 2: Undermining Clause Audit

**Check:** Every significant assertion/observation has a complicating element

**Procedure:**

1. Identify declarative statements about character, setting, or situation
1. Verify each has undermining clause, adversative element, or complication
1. Add undermining clauses where simple statements exist
1. Verify method matches period (paratactic for prehistoric, grammatical for contemporary, etc.)

**Output format:**

```
UNDERMINING AUDIT
- Statements checked: [count]
- Already undermined: [count]
- Additions made: [count]
- Method verification: [pass / adjustments made]
```

-----

### Pass 3: Forbidden Pattern Scan

**Check:** No violations of INVIOLABLE or forbidden pattern rules

**Procedure:**

1. Scan for abstract emotion words:
   afraid, angry, sad, happy, anxious, nervous, excited, worried, relieved, frustrated, confused, surprised, lonely, guilty, ashamed, proud, jealous, hopeful, desperate
1. Scan for filter verbs:
   saw, felt, noticed, realized, thought, knew, wondered, decided, remembered
1. Scan for Buddhist terminology:
   dharma, karma, samsara, nirvana, enlightenment, attachment, suffering, awakening, meditation, mindfulness, consciousness (spiritual sense), ego, self (Buddhist sense), rebirth, reincarnation
1. Revise all violations before finalizing

**Output format:**

```
FORBIDDEN PATTERN SCAN
- Abstract emotions found: [count] → [revised / none]
- Filter verbs found: [count] → [revised / none]  
- Buddhist terms found: [count] → [revised / none]
- Other violations: [list / none]
```

-----

### Pass 4: Structural Verification

**Check:** Scene meets structural requirements

**Procedure:**

1. Verify scene opens with sensory anchor (environment before interiority)
1. Verify POV consistency (no head-hopping)
1. Verify dialogue has physical grounding (no floating talking heads)
1. If death scene: verify extended treatment, visceral detail, karmic bridge to next life
1. Verify Lilith presence matches chapter power level (per `lilith-arc.json`)
1. Verify recognition markers present (if defined)
1. Verify meat/body theme present
1. Verify genre conventions honored

**Output format:**

```
STRUCTURAL VERIFICATION
- [ ] Opens with sensory anchor
- [ ] POV consistent throughout
- [ ] Dialogue physically grounded
- [ ] Death scene requirements (if applicable): [met / N/A]
- [ ] Lilith power level appropriate: [yes / N/A]
- [ ] Recognition markers: [present / TBD / N/A]
- [ ] Meat/body theme: [present]
- [ ] Genre conventions: [honored]
```

-----

### Pass 5: Continuity Check

**Check:** Scene aligns with established canon and prior scenes

**Procedure:**

1. Verify character names match documentation
1. Verify setting details match `period-rules.md` or `contemporary-period-rules.md`
1. Verify Lilith’s appearance matches cross-life consistency
1. Verify no contradictions with prior scenes in chapter
1. If chapter-ending death scene: verify karmic bridge matches next chapter’s lesson
1. Flag any potential continuity issues for author review

**Output format:**

```
CONTINUITY CHECK
- Character names: [verified]
- Setting details: [verified]
- Lilith consistency: [verified / N/A]
- Prior scene alignment: [verified / first scene]
- Karmic bridge: [verified / N/A]
- Issues flagged: [none / list]
```

-----

### Pass 6: Lilith Chapter Verification (Lilith Chapters Only)

**Check:** Lilith chapter-specific requirements met

**Procedure:**

1. Verify demonstration scene present (she shows mastery of relevant fetter)
1. Verify patient/colleague parallel present (they describe her situation)
1. Verify physical tell undercuts her self-assessment
1. Verify power level matches `lilith-chapter-manifest.json`
1. Verify attentional/karmic cost shown (time lost, distraction, deepening attachment—NOT physical symptoms)
1. Verify professional life status matches progression
1. Verify notebook/documentation motif present
1. Count Maitreya foreshadowing moments (should be 0-2, subtle)
1. Verify tracking content connects to corresponding historical chapter

**Output format:**

```
LILITH CHAPTER VERIFICATION
- [ ] Demonstration scene present
- [ ] Patient/colleague parallel present
- [ ] Physical tell undercuts self-assessment
- [ ] Power level matches chapter: [level]
- [ ] Attentional/karmic cost shown (not physical)
- [ ] Professional life status: [matches / needs adjustment]
- [ ] Notebook motif present
- [ ] Maitreya foreshadowing: [count] moments
- [ ] Tracking connects to Ch [X]: [verified]
```

-----

## Chapter Type Quick Reference

|Type               |Chapters                          |Key Requirements                                 |Verification Passes|
|-------------------|----------------------------------|-------------------------------------------------|-------------------|
|Contemporary Dual  |1, 22                             |Both POVs; Manchester setting; contemporary voice|1-5                |
|Historical         |2, 4, 6, 8, 10, 12, 14, 16, 18, 20|Period voice; death bridge; Lilith intervention  |1-5                |
|Lilith Contemporary|3, 5, 7, 9, 11, 13, 15, 17, 19, 21|Demonstration scene; tracking; contemporary voice|1-6                |
|Cosmic             |23, 24, 25, 26                    |Transcendent voice; merger preparation           |1-5                |

-----

## File Dependency Map

### Core Dependencies

```
CLAUDE.md (creative authority)
    ↓
├── style-rules.md (voice implementation)
│   ├── voice-analysis.md (detailed patterns)
│   └── contemporary-period-rules.md (Manchester chapters)
│
├── soul-constants.json (spiritual framework)
│
├── lilith-arc.json (her interventions in historical chapters)
│
├── lilith-chapter-manifest.json (her contemporary chapters)
│
└── thematic-echoes.md (symbols/patterns)
```

### Chapter-Level Dependencies

```
scene-manifest.json (what exists)
    ↓
For Historical Chapters:
    incarnations/[chapter]/
        ├── period-rules.md
        ├── avatar-profile.json
        └── scenes/

For Lilith Chapters:
    contemporary-period-rules.md
    lilith-chapter-manifest.json
    [corresponding historical chapter must be drafted first]
```

### Drafting Prerequisites by Chapter Type

**Historical Chapter:**

```
CLAUDE.md ✓
    └── style-rules.md ✓
        └── period-rules.md for chapter ✓
            └── avatar-profile.json for chapter ✓
                └── scene in scene-manifest.json ✓
                    └── Lilith intervention in lilith-arc.json ✓
                        └── READY TO DRAFT
```

**Lilith Chapter:**

```
CLAUDE.md ✓
    └── contemporary-period-rules.md ✓
        └── lilith-chapter-manifest.json entry complete ✓
            └── corresponding historical chapter drafted ✓
                └── demonstration scene planned ✓
                    └── READY TO DRAFT
```

-----

## Error-Handling Protocol

### Missing Files

**If required file does not exist:**

1. HALT current task
1. Document in `novel-progress.txt`
1. Either switch to Mode 1 and create the file, OR wait for author
1. Do not proceed with drafting until file exists

### Contradictory Information

**If two sources contradict each other:**

1. HALT if contradiction affects current task
1. Document in `novel-progress.txt`
1. Apply hierarchy: `CLAUDE.md` > `style-rules.md` > chapter-specific files > older documentation
1. Flag for author review

### Lilith Chapter Without Historical Chapter

**If attempting to draft a Lilith chapter before its corresponding historical chapter:**

1. HALT — This is a hard dependency
1. The Lilith chapter must observe/track the historical chapter
1. Either draft the historical chapter first, OR wait for author

-----

## Quality Gates

### Before Marking Scene “Drafted”

All applicable verification passes completed:

- [ ] Pass 1: Sensory Audit
- [ ] Pass 2: Undermining Clause Audit
- [ ] Pass 3: Forbidden Pattern Scan
- [ ] Pass 4: Structural Verification
- [ ] Pass 5: Continuity Check
- [ ] Pass 6: Lilith Chapter Verification (if Lilith chapter)

### Before Marking Chapter “Complete”

- [ ] All scenes marked “complete”
- [ ] Chapter-level continuity verified
- [ ] Death scene karmic bridge verified (historical chapters)
- [ ] Demonstration technique verified (Lilith chapters)
- [ ] Genre conventions satisfied
- [ ] Author has reviewed

-----

## Communication with Author

### When to Document and Continue

- Minor stylistic choices within established parameters
- Selection between equally valid sensory details
- Paragraph-level structural decisions

### When to Document and Flag for Review

- Any creative decision affecting continuity
- Potential contradictions discovered
- Interpretation of ambiguous prior content
- Anything touching “Never Improvise” territory

### When to HALT and Wait

- Missing required files with no clear scaffolding path
- Contradictions that significantly affect the scene
- Tasks requiring creation of new canonical content
- Attempting to draft Lilith chapter before historical chapter

-----

## Quick Reference: What Goes Where

|Information Type                      |File                                     |
|--------------------------------------|-----------------------------------------|
|What happened this session            |`novel-progress.txt`                     |
|Scene/chapter status                  |`scene-manifest.json`                    |
|Historical chapter Lilith intervention|`lilith-arc.json`                        |
|Lilith chapter requirements           |`lilith-chapter-manifest.json`           |
|Manchester voice/setting              |`contemporary-period-rules.md`           |
|“Can I do X?”                         |Check `CLAUDE.md` “Never Improvise” first|
|“How do I do X?”                      |This file (`agent-protocol.md`)          |