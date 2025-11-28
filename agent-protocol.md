# Agent Protocol: The Wheel of Meat

## How to Use This File

This document describes **how to work on this project** correctly.

For **what the novel is** (voice, character, theme, constraints), see `CLAUDE.md`.

Read `CLAUDE.md` first to understand the creative parameters. Read this file to understand workflow and procedures.

---

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
- Note any decisions requiring author review in `meta/decisions.md`

---

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
- [ ] `period-rules.md` exists and is complete for this chapter
- [ ] `avatar-profile.json` exists and is complete for this chapter
- [ ] Scene is listed in `scene-manifest.json`
- [ ] Lilith's objective for this chapter is documented in `lilith-arc.json`
- [ ] Previous scene's ending has been read (if not first scene)
- [ ] `thematic-echoes.md` checked for required elements

**If any entry requirement is NOT satisfied:**
1. HALT — Do not draft
2. Switch to Mode 1: SCAFFOLDING
3. Create the missing documentation
4. Return to Mode 2 only when all requirements are met

**Exit requirements:**
- Run all verification passes (see below)
- Update `scene-manifest.json` with status and word count
- Update `novel-progress.txt` with:
  - Scene completed
  - Decisions made
  - Continuity concerns
  - Issues for author review

---

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
- Do not "improve" passages that weren't flagged

**Exit requirements:**
- Document all changes in `novel-progress.txt`
- Note if revision revealed larger issues requiring author input
- Update `scene-manifest.json` status if applicable

---

## Session Workflow

### Starting a Session

Execute in order:

1. **Read `novel-progress.txt`**
   - Understand current state
   - Note outstanding issues
   - Identify what was planned for this session

2. **Read `scene-manifest.json`**
   - Identify current task
   - Confirm chapter/scene status
   - Verify prerequisites

3. **Determine Agent Mode**
   - What is the task? (scaffolding / drafting / revision)
   - Are entry requirements met?
   - If not, what must be done first?

4. **Load context files based on mode:**

   *For SCAFFOLDING:*
   - Relevant existing documentation
   - `CLAUDE.md` for creative constraints
   - Source material if researching

   *For DRAFTING:*
   - `CLAUDE.md` (full read)
   - `reference/style-rules.md`
   - Chapter's `period-rules.md`
   - Chapter's `avatar-profile.json`
   - `meta/lilith-arc.json` (this chapter's entry)
   - `meta/thematic-echoes.md`
   - `meta/rebirth-mechanics.md` (if death scene or Lilith intervention)
   - Previous scene ending (if continuing chapter)

   *For REVISION:*
   - The draft being revised
   - `CLAUDE.md` constraint hierarchy
   - `reference/style-rules.md`
   - Revision notes/objectives

5. **Confirm readiness**
   - All required files present?
   - Task clearly defined?
   - Constraints understood?
   - If any uncertainty, document and request clarification before proceeding

---

### During a Session

**DRAFTING sessions:**
- Write the complete scene before stopping
- Do not pause mid-scene for feedback
- Maintain voice patterns throughout
- Track sensory inclusion mentally as you write
- Note concerns for later rather than stopping to resolve

**SCAFFOLDING sessions:**
- Complete one documentation unit before moving to next
- Cross-reference existing files for consistency
- Flag contradictions rather than resolving unilaterally
- Check `CLAUDE.md` "Never Improvise" list before creating new canonical content

**REVISION sessions:**
- Make targeted changes only
- Read surrounding context before each edit
- Verify voice consistency after each change
- Stop if revision scope is expanding beyond original objective

**All sessions:**
- If you encounter a blocking issue, document it and stop
- Do not invent solutions to problems outside your mode's scope
- When uncertain between two valid approaches, document both and request author decision

---

### Ending a Session

Execute in order:

1. **Run applicable verification passes** (drafting mode only—see below)

2. **Update `scene-manifest.json`**
   - Scene status (outlined / drafted / revised / complete)
   - Word count (for drafted scenes)
   - Any blocking issues

3. **Update `novel-progress.txt`**
   ```
   ### Session [DATE]
   
   **Mode:** [Scaffolding / Drafting / Revision]
   
   **Work Completed:**
   - [Specific deliverables]
   
   **Decisions Made:**
   - [Any choices that affect continuity or canon]
   
   **Issues for Author Review:**
   - [Questions, concerns, contradictions discovered]
   
   **Next Session Should:**
   - [Clear next steps]
   ```

4. **Update `meta/decisions.md`** (if any significant creative decisions were made)

5. **Final check:**
   - All files saved?
   - All updates logged?
   - Session state clean for next agent?

---

## Post-Draft Verification Passes

After completing a scene draft, run these audits before finalizing. Do not skip passes.

### Pass 1: Sensory Audit

**Check:** All five senses present (sight, sound, smell, taste, touch)

**Procedure:**
1. List each sense and identify where it appears in the scene
2. Flag any segment >400 words missing two or more senses
3. Add sensory details where gaps exist
4. Verify sensory details match period-specific palette

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

---

### Pass 2: Undermining Clause Audit

**Check:** Every significant assertion/observation has a complicating element

**Procedure:**
1. Identify declarative statements about character, setting, or situation
2. Verify each has undermining clause, adversative element, or complication
3. Add undermining clauses where simple statements exist
4. Verify method matches period (paratactic for prehistoric, aphoristic for ancient, etc.)

**Output format:**
```
UNDERMINING AUDIT
- Statements checked: [count]
- Already undermined: [count]
- Additions made: [count]
- Method verification: [pass / adjustments made]
```

---

### Pass 3: Forbidden Pattern Scan

**Check:** No violations of INVIOLABLE or forbidden pattern rules

**Procedure:**
1. Scan for abstract emotion words:
   afraid, angry, sad, happy, anxious, nervous, excited, worried, relieved, frustrated, confused, surprised, lonely, guilty, ashamed, proud, jealous, hopeful, desperate
2. Scan for filter verbs:
   saw, felt, noticed, realized, thought, knew, wondered, decided, remembered
3. Scan for Buddhist terminology:
   dharma, karma, samsara, nirvana, enlightenment, attachment, suffering, awakening, meditation, mindfulness, consciousness (spiritual sense), ego, self (Buddhist sense)
4. Revise all violations before finalizing

**Output format:**
```
FORBIDDEN PATTERN SCAN
- Abstract emotions found: [count] → [revised / none]
- Filter verbs found: [count] → [revised / none]  
- Buddhist terms found: [count] → [revised / none]
- Other violations: [list / none]
```

---

### Pass 4: Structural Verification

**Check:** Scene meets structural requirements

**Procedure:**
1. Verify scene opens with sensory anchor (environment before interiority)
2. Verify POV consistency (no head-hopping)
3. Verify dialogue has physical grounding (no floating talking heads)
4. If death scene: verify extended treatment, visceral detail, karmic bridge to next life
5. Verify Lilith presence matches chapter power level (per `lilith-arc.json`)
6. Verify recognition markers present (if defined)
7. Verify meat/body theme present
8. Verify genre conventions honored

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

---

### Pass 5: Continuity Check

**Check:** Scene aligns with established canon and prior scenes

**Procedure:**
1. Verify character names match documentation
2. Verify setting details match `period-rules.md`
3. Verify Lilith's appearance matches cross-life consistency
4. Verify no contradictions with prior scenes in chapter
5. If chapter-ending death scene: verify karmic bridge matches next chapter's lesson
6. Flag any potential continuity issues for author review

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

---

## Error-Handling Protocol

### Missing Files

**If required file does not exist:**
1. HALT current task
2. Document in `novel-progress.txt`:
   - What file is missing
   - What task cannot proceed without it
   - Suggested content for the file (if scaffolding is appropriate)
3. Either:
   - Switch to Mode 1 and create the file, OR
   - Wait for author to provide the file
4. Do not proceed with drafting until file exists

### Contradictory Information

**If two sources contradict each other:**
1. HALT if contradiction affects current task
2. Document in `novel-progress.txt`:
   - The specific contradiction
   - Which files contain conflicting information
   - Which interpretation you believe is correct (with reasoning)
3. Apply hierarchy: `CLAUDE.md` > `style-rules.md` > chapter-specific `period-rules.md` > older documentation
4. Document which interpretation was used
5. Flag for author review

### Unclear Instructions

**If instructions are ambiguous:**
1. Document the ambiguity in `novel-progress.txt`
2. If a reasonable default exists, state it and proceed
3. If no reasonable default, HALT and request clarification
4. Do not invent major creative content to fill gaps

### Scope Creep

**If task is expanding beyond original objective:**
1. Stop at natural boundary
2. Document what was completed
3. Document what additional work emerged
4. Let author decide whether to continue in next session

### Canon Violation Discovered

**If you realize prior work violates established rules:**
1. Complete current task if possible without compounding the violation
2. Document the violation in `novel-progress.txt`:
   - What rule was violated
   - Where the violation occurs
   - Suggested fix
3. Do not unilaterally rewrite prior work
4. Flag for author decision

---

## File Dependency Map

Understanding which files depend on which prevents working with stale or incomplete information.

### Core Dependencies

```
CLAUDE.md (creative authority)
    ↓
├── style-rules.md (voice implementation)
│   └── voice-analysis.md (detailed patterns)
│
├── soul-constants.json (spiritual framework)
│   └── rebirth-mechanics.md (karma/transfer rules)
│
├── lilith-arc.json (antagonist per chapter)
│
└── thematic-echoes.md (symbols/patterns)
```

### Chapter-Level Dependencies

```
scene-manifest.json (what exists)
    ↓
incarnations/[chapter]/
    ├── period-rules.md
    │   depends on: style-rules.md, voice-analysis.md
    │
    ├── avatar-profile.json
    │   depends on: soul-constants.json, lilith-arc.json
    │
    └── scenes/
        depend on: ALL of the above
```

### Drafting Prerequisites (Complete Chain)

To draft a scene, the following chain must be complete:

```
CLAUDE.md ✓
    └── style-rules.md ✓
        └── period-rules.md for chapter ✓
            └── avatar-profile.json for chapter ✓
                └── scene listed in scene-manifest.json ✓
                    └── Lilith objective in lilith-arc.json ✓
                        └── READY TO DRAFT
```

If any link is missing or incomplete, drop to scaffolding mode.

---

## Quality Gates

### Before Marking Scene "Drafted"

All verification passes completed:
- [ ] Pass 1: Sensory Audit
- [ ] Pass 2: Undermining Clause Audit
- [ ] Pass 3: Forbidden Pattern Scan
- [ ] Pass 4: Structural Verification
- [ ] Pass 5: Continuity Check

### Before Marking Scene "Complete"

- [ ] Author has reviewed draft
- [ ] All author notes addressed
- [ ] Re-run verification passes after revisions
- [ ] No outstanding issues flagged

### Before Marking Chapter "Complete"

- [ ] All scenes marked "complete"
- [ ] Chapter-level continuity verified
- [ ] Death scene karmic bridge verified against next chapter
- [ ] Lilith's objective for chapter achieved (even if backfiring)
- [ ] Recognition markers present throughout
- [ ] Genre conventions satisfied

---

## Commit Message Format

When saving work to repository:

```
[Type]: [chapter-id]/[scene] - [summary]

[Details if needed]
```

**Types:**
- `Draft` — New scene content
- `Revise` — Changes to existing draft
- `Scaffold` — Documentation, profiles, rules
- `Doc` — Project documentation updates
- `Fix` — Corrections to errors

**Examples:**
```
Draft: ch02/scene-03 - Ka joins the dog pack
Scaffold: ch04 - Avatar profile for Athenian philosopher
Revise: ch03/scene-05 - Address author notes on Devaka's betrayal
Doc: Update thematic-echoes with Ch2 death bridge
Fix: ch03/period-rules - Correct Mauryan dating error
```

---

## Communication with Author

### When to Document and Continue

- Minor stylistic choices within established parameters
- Selection between equally valid sensory details
- Paragraph-level structural decisions
- Word choice within period-appropriate vocabulary

### When to Document and Flag for Review

- Any creative decision affecting continuity
- Potential contradictions discovered
- Scope questions (is X part of this scene?)
- Interpretation of ambiguous prior content
- Anything touching "Never Improvise" territory

### When to HALT and Wait

- Missing required files with no clear scaffolding path
- Contradictions that significantly affect the scene
- Instructions that seem to conflict with INVIOLABLE constraints
- Tasks requiring creation of new canonical content (characters, metaphysics, plot)
- Uncertainty about whether current approach is correct

### How to Flag Issues

In `novel-progress.txt`, use clear markers:

```
**AUTHOR DECISION NEEDED:**
[Clear statement of the question]
[Options if applicable]
[Your recommendation if you have one]

**POTENTIAL ISSUE:**
[Description of concern]
[Why it might matter]
[Suggested investigation/resolution]

**CONTRADICTION FOUND:**
[Source A says X]
[Source B says Y]
[Which was used and why]
[Request for authoritative resolution]
```

---

## Session State Checklist

Use this to verify clean handoff between sessions:

### End of Session

- [ ] Current work saved
- [ ] `scene-manifest.json` updated
- [ ] `novel-progress.txt` updated with session summary
- [ ] All decisions documented
- [ ] All issues flagged
- [ ] Next steps clearly stated
- [ ] No work in ambiguous/incomplete state

### Start of Session

- [ ] `novel-progress.txt` read completely
- [ ] Previous session's next steps understood
- [ ] Outstanding issues noted
- [ ] Agent mode determined
- [ ] Entry requirements verified
- [ ] Context files loaded
- [ ] Ready to proceed

---

## Quick Reference: What Goes Where

| Information Type | File |
|-----------------|------|
| What happened this session | `novel-progress.txt` |
| Scene/chapter status | `scene-manifest.json` |
| Creative decisions with reasoning | `meta/decisions.md` |
| Voice/style questions | `reference/style-rules.md` or author |
| Canon/continuity questions | Relevant `/meta` file or author |
| "Can I do X?" | Check `CLAUDE.md` "Never Improvise" first |
| "How do I do X?" | This file (`agent-protocol.md`) |