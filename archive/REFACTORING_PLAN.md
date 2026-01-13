# Repository Refactoring Plan: Novel Writing → Novel Revision

**Created:** January 2026
**Branch:** `claude/refactor-novel-revision-plan-hefMH`
**Status:** Implementation Ready

---

## Overview

This plan refocuses the Wheel of Meat repository from novel drafting to line-level prose revision. Structural revision and Lilith chapter overhaul are complete. The repository now needs to optimize for:

1. **Prose quality passes** (tic removal, style enforcement, voice consistency)
2. **Revision tracking** (per-scene status, pass completion, before/after comparison)
3. **Prompt-based workflow** (tools generate revision prompts for author review)

---

## Phase 1: Folder & File Reorganization

### 1.1 Archive Brainstorms

**Action:** Move `/brainstorms/` → `/archive/brainstorms/`

Files to archive:
- `scene-manifest-revision-brainstorm.md`
- `LILITH-CONTINUITY-AUDIT.md`
- `ACTIVideas.md`
- `claude-revision-brainstorm.md`
- `ch22-brainstorm.md`
- `lilith-chapter-manifest-revision.md`
- `CH20_BRAINSTORMING.md`
- `ch21-brainstorm.md`
- `ch22-flow-critique.md`
- `json-architecture-updates-brainstorm.md`
- `ch22-revision-plan.md`

**Rationale:** These planning documents served their purpose during the Lilith arc overhaul. Archive preserves history without cluttering active workspace.

### 1.2 Update Chapter Statuses

**Action:** Mark all 10 Lilith chapters as "revised" in:
- `scene-manifest.json`
- `claude.md` chapter reference table

Chapters to update: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21

---

## Phase 2: Agent Configuration Overhaul

### 2.1 Sunset SCAFFOLDING and DRAFTING Modes

**File:** `agent-protocol.md`

**Remove/Archive:**
- Mode 1: SCAFFOLDING (entire section)
- Mode 2: DRAFTING (entire section)
- Lilith Chapter Workflow (3-phase process)
- Entry requirements for drafting
- "Before Marking Scene 'Drafted'" checklist

**Rationale:** Novel drafting is complete. These modes add cognitive overhead for a revision-focused workflow.

### 2.2 Expand REVISION Mode

**New Structure for `agent-protocol.md`:**

```markdown
# Agent Protocol: The Wheel of Meat (Revision Phase)

## Purpose
This document defines procedures for line-level prose revision.
For novel content and voice patterns, see `claude.md`.

## Revision Passes

### Pass 1: Prose Tic Scan
Identify and propose fixes for:
- "The particular [noun]" constructions
- Vague "something" language
- Em-dash excess (>2 per paragraph)
- Abstract nouns performing physical actions
- "Not X—Y" repetition patterns

### Pass 2: Forbidden Pattern Audit
Scan for violations of INVIOLABLE constraints:
- Abstract emotion words
- Buddhist terminology
- Filter verbs without purpose
- Unearned interiority

### Pass 3: Voice Consistency Check
Verify core patterns present:
- Undermining clauses
- Sensory anchoring
- Loaded gestures
- Environmental metaphor
- Parallel construction

### Pass 4: Sensory Audit
- All five senses present per scene
- Sensory details match period-specific palette
- No segments >400 words missing 2+ senses

### Pass 5: Continuity Verification
- Character names match documentation
- Setting details match period-rules.md
- Lilith appearance consistent
- No cross-chapter contradictions

## Revision Workflow

1. Select scene from `revision-manifest.json` (status: "needs_revision")
2. Run applicable passes (or use tool output)
3. Generate revision prompts (do not auto-apply)
4. Author reviews and approves changes
5. Update `revision-manifest.json` with completed passes
6. Log session in `novel-progress.txt`

## Output Format

All revision suggestions follow this format:

​```
REVISION PROMPT: [Pass Name]
Chapter: [X] | Scene: [scene-name.md]
Line: [N]

ORIGINAL:
> [quoted text]

ISSUE:
[description of problem]

PROPOSED REVISION:
> [suggested replacement]

RATIONALE:
[why this change improves the prose]
​```

## Quality Gates

Before marking a scene "revision_complete":
- [ ] All 5 passes completed
- [ ] No INVIOLABLE violations remain
- [ ] Voice patterns verified
- [ ] Author has reviewed all prompts
```

### 2.3 Update claude.md

**Changes needed:**

1. **Project Overview** - Update status from "DRAFTING PHASE" to "REVISION PHASE"
2. **Chapter Quick Reference** - Mark Lilith chapters as "REVISED" not "needs_revision"
3. **Remove/Archive:**
   - References to "Mode 2: DRAFTING"
   - "Entry requirements for drafting"
   - Instructions about generating new scenes
4. **Add:**
   - Reference to `revision-manifest.json`
   - Link to revision pass procedures

---

## Phase 3: New Reference Files

### 3.1 Create `revision-manifest.json`

**Location:** `/reference/revision-manifest.json`

**Structure:**

```json
{
  "metadata": {
    "created": "2026-01-02",
    "total_scenes": 265,
    "revision_complete": 0,
    "revision_in_progress": 0,
    "needs_revision": 265
  },
  "chapters": {
    "1": {
      "title": "Contemporary Manchester",
      "type": "contemporary",
      "status": "needs_revision",
      "scenes": {
        "scene-01-seminar-room.md": {
          "word_count": 1250,
          "status": "needs_revision",
          "passes_complete": [],
          "passes_remaining": ["tic_scan", "forbidden_pattern", "voice_check", "sensory_audit", "continuity"],
          "last_revised": null,
          "notes": ""
        }
      }
    }
  },
  "pass_definitions": {
    "tic_scan": "Prose Tic Scan (particular, something, em-dash, abstract actions, not-x)",
    "forbidden_pattern": "Forbidden Pattern Audit (emotion words, Buddhist terms, filter verbs)",
    "voice_check": "Voice Consistency Check (undermining, sensory anchor, loaded gesture)",
    "sensory_audit": "Sensory Audit (5 senses per scene)",
    "continuity": "Continuity Verification (names, settings, Lilith appearance)"
  }
}
```

**Population:** Generate from existing `scene-manifest.json` data.

---

## Phase 4: Tool Additions

### 4.1 Revision Prompt Generator

**File:** `tools/revision_prompt_generator.py`

**Purpose:** Runs prose tic analysis and outputs formatted revision prompts for author review.

**Features:**
- Takes scene file as input
- Runs all tic detection patterns
- Outputs formatted prompts (not auto-fixes)
- Saves prompts to `/out/revision_prompts/[chapter]/[scene].md`

**Sample Output:**

```markdown
# Revision Prompts: CH02 Scene 01

## Prose Tic Scan

### Issue 1 (Line 47)
ORIGINAL:
> The particular silence of the cave pressed against his ears.

ISSUE: "The particular [noun]" construction

PROPOSED REVISION:
> The deep silence of the cave pressed against his ears.
> OR: The cave's silence pressed against his ears.

RATIONALE: "Particular" adds no specificity. Replace with concrete descriptor or simplify.

---

### Issue 2 (Line 112)
ORIGINAL:
> Something shifted in his understanding.

ISSUE: Vague "something" construction

PROPOSED REVISION:
> A new clarity settled in his understanding.
> OR: His understanding shifted—the pattern suddenly visible.

RATIONALE: Name what shifted. Abstract nouns are allowed if grounded.
```

### 4.2 Continuity Checker

**File:** `tools/continuity_checker.py`

**Purpose:** Cross-reference scenes for consistency violations.

**Checks:**
- Lilith appearance markers (widow's peak, eye crescent)
- Character name spelling across chapters
- Setting details vs period-rules.md
- Timeline consistency
- Recurring motif presence (meat/body theme)

**Output:** JSON report + formatted prompts for violations.

### 4.3 Before/After Comparison Tool

**File:** `tools/revision_diff.py`

**Purpose:** Generate readable diffs between revision versions.

**Features:**
- Compare scene files before/after revision
- Highlight changes with context
- Calculate revision statistics (% changed, words added/removed)
- Archive previous versions automatically

### 4.4 Revision Tracker

**File:** `tools/revision_tracker.py`

**Purpose:** CLI for updating `revision-manifest.json`.

**Commands:**
```bash
# Mark scene as in-progress
python revision_tracker.py start ch02 scene-01-blood-wake.md

# Mark pass complete
python revision_tracker.py pass-complete ch02 scene-01-blood-wake.md tic_scan

# Mark scene fully revised
python revision_tracker.py complete ch02 scene-01-blood-wake.md

# Generate progress report
python revision_tracker.py report
```

---

## Phase 5: Folder Structure Updates

### 5.1 New Structure

```
Wheel_of_Meat/
├── README.md                     # Update for revision focus
├── claude.md                     # Update status, remove drafting refs
├── agent-protocol.md             # Revision-only protocol
│
├── reference/
│   ├── scene-manifest.json       # Keep (source of truth for structure)
│   ├── revision-manifest.json    # NEW: revision status tracking
│   ├── style-rules.md            # Keep
│   ├── lilith-style-rules.md     # Keep (reference for integrated prose)
│   └── novel-progress.txt        # Keep (session log)
│
├── meta/                          # Keep as-is (narrative architecture)
│
├── incarnations/                  # Keep as-is (chapter content)
│
├── tools/
│   ├── compile_chapters.py       # Keep (still useful for recompilation)
│   ├── compile_manuscript_v4.py  # Keep
│   ├── prose_tic_analyzer.py     # Keep (core revision tool)
│   ├── prose_tic_analyzer_scenes.py  # Keep
│   ├── revision_prompt_generator.py  # NEW
│   ├── continuity_checker.py     # NEW
│   ├── revision_diff.py          # NEW
│   ├── revision_tracker.py       # NEW
│   └── revision_audit/
│       └── manuscript_analyzer.py # Keep
│
├── out/
│   ├── prose_tic_analysis/       # Keep
│   ├── prose_tic_analysis_scenes/ # Keep
│   └── revision_prompts/         # NEW: generated prompts
│
├── archive/
│   ├── brainstorms/              # Moved from /brainstorms/
│   ├── lilith-v1-drafts/
│   └── revision_v1/
│
└── docs/
    └── manuscript_statistics.txt
```

### 5.2 Files to Remove

None—archive rather than delete for history.

---

## Implementation Order

### Immediate (This Session)
1. ✅ Create this plan document
2. Archive `/brainstorms/` → `/archive/brainstorms/`
3. Update Lilith chapter statuses in `scene-manifest.json`
4. Update `claude.md` chapter reference table

### Short-term (Next Session)
5. Create `revision-manifest.json` from scene-manifest data
6. Rewrite `agent-protocol.md` for revision focus
7. Update README.md

### Medium-term (Tool Development)
8. Build `revision_prompt_generator.py`
9. Build `revision_tracker.py`
10. Build `continuity_checker.py`
11. Build `revision_diff.py`

---

## Success Criteria

The refactoring is complete when:

1. **No drafting references** remain in agent-protocol.md
2. **revision-manifest.json** tracks all 265 scenes with pass status
3. **Tools generate prompts** (not auto-fixes) for author review
4. **Brainstorms archived** and working directory is clean
5. **Lilith chapters marked revised** in all manifests
6. **README.md** reflects revision-phase status

---

## Notes

- This refactoring preserves all historical data in `/archive/`
- Compilation tools remain useful for generating chapter drafts from scenes
- Prose tic analyzer is already revision-focused and serves as template for new tools
- The revision-manifest.json pattern mirrors scene-manifest.json for consistency
