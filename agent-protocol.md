# Agent Protocol: The Wheel of Meat (Revision Phase)

## How to Use This File

This document describes **how to revise prose** in this project.

For **what the novel is** (voice, character, theme, constraints), see `claude.md`.

Read `claude.md` first to understand the creative parameters. Read this file to understand revision workflow and procedures.

---

## Revision Focus

**Status:** REVISION PHASE (January 2026)

The novel structure is complete. All Lilith chapters have been revised with integrated prose technique. This protocol now focuses on:

1. **Line-level prose revision** (tic removal, style enforcement, voice consistency)
2. **Revision tracking** (per-scene pass completion via `revision-manifest.json`)
3. **Prompt-based workflow** (generate revision prompts for author review)

---

## Revision Passes

Run these passes on each scene. Track completion in `revision-manifest.json`.

### Pass 1: Prose Tic Scan

**Purpose:** Identify and propose fixes for recurring prose weaknesses.

**Check for:**

1. **"The particular [noun]"** — Remove unnecessary intensifier or replace with specific descriptor
2. **Vague "something" constructions** — Name the referent specifically
3. **Em-dash excess** — More than 2 pairs per paragraph; vary punctuation
4. **Abstract nouns performing physical actions** — Rephrase with concrete subject
5. **"Not X—Y" repetition** — Vary sentence structure

**Tool support:** `tools/prose_tic_analyzer.py` generates reports; `tools/revision_prompt_generator.py` outputs formatted prompts.

**Output format:**

```
REVISION PROMPT: Prose Tic Scan
Chapter: [X] | Scene: [scene-name.md]
Line: [N]

ORIGINAL:
> [quoted text]

ISSUE:
[tic type and description]

PROPOSED REVISION:
> [suggested replacement]

RATIONALE:
[why this change improves the prose]
```

---

### Pass 2: Forbidden Pattern Audit

**Purpose:** Eliminate violations of INVIOLABLE constraints from `claude.md`.

**Check for:**

1. **Abstract emotion words:**
   afraid, angry, sad, happy, anxious, nervous, excited, worried, relieved, frustrated, confused, surprised, lonely, guilty, ashamed, proud, jealous, hopeful, desperate

2. **Buddhist terminology:**
   dharma, karma, samsara, nirvana, enlightenment, attachment, suffering, awakening, meditation, mindfulness, consciousness (spiritual sense), ego, self (Buddhist sense), rebirth, reincarnation

3. **Filter verbs without purpose:**
   saw, felt, noticed, realized, thought, knew, wondered, decided, remembered

4. **Unearned interiority:**
   Extended internal monologue, pages of thought without action

**Procedure:**

1. Scan for each forbidden pattern
2. For each violation, generate revision prompt
3. Propose concrete physical/sensory alternative
4. Document in output

---

### Pass 3: Voice Consistency Check

**Purpose:** Verify core prose patterns are present and correctly adapted by period.

**Core patterns to verify:**

1. **Undermining clause** — Every significant assertion has complicating element
   - Prehistoric: Paratactic contradiction
   - Ancient/Classical: Aphoristic reversal
   - Contemporary: Grammatical complexity
   - Cosmic: Paradox/koan structure

2. **Sensory anchoring** — Scene opens with environment/body before interiority
   - Check first paragraph of each scene
   - No floating heads or ungrounded dialogue

3. **Loaded gestures** — Physical actions carry psychological meaning
   - Small movements encode what characters cannot say

4. **Environmental metaphor** — Setting reflects emotional/spiritual state
   - Weather, light, space mirror interior conditions

5. **Parallel construction** — Mirrored phrases for thematic content
   - Used for philosophical content and character contrast

**Procedure:**

1. Identify declarative statements lacking undermining element
2. Check scene openings for sensory anchor
3. Flag dialogue without physical grounding
4. Verify method matches period (per genre table in `claude.md`)

---

### Pass 4: Sensory Audit

**Purpose:** Ensure full sensory immersion in every scene.

**Requirements:**

- All five senses present: sight, sound, smell, taste, touch
- No segment >400 words missing two or more senses
- Sensory details match period-specific palette (per `period-rules.md`)

**Procedure:**

1. List each sense and identify where it appears
2. Flag gaps
3. Propose additions that match period vocabulary
4. Verify physical actions have tactile grounding

**Output format:**

```
SENSORY AUDIT: [scene-name.md]
- Sight: [locations]
- Sound: [locations]
- Smell: [locations or MISSING]
- Taste: [locations or MISSING]
- Touch: [locations]
- Gaps identified: [list]
- Proposed additions: [specific suggestions]
```

---

### Pass 5: Continuity Verification

**Purpose:** Ensure consistency across scenes and chapters.

**Check for:**

1. **Character names** — Match documentation exactly
2. **Setting details** — Align with `period-rules.md`
3. **Lilith appearance** — Consistent markers:
   - Widow's peak with darker strand falling left
   - Left eye: deep brown with pale-green crescent at 11-1 o'clock
4. **Prior scene alignment** — No contradictions within chapter
5. **Karmic bridge** (death scenes) — Matches next chapter's lesson

**Cross-reference files:**
- `incarnations/[ch]/avatar-profile.json`
- `incarnations/[ch]/period-rules.md`
- `meta/lilith-arc.json`
- `meta/soul-constants.json`

---

## Revision Workflow

### Starting a Revision Session

1. Check `revision-manifest.json` for scenes with `status: "needs_revision"`
2. Select a scene to revise (prefer sequential within chapter)
3. Read the scene file completely
4. Read `period-rules.md` for that chapter
5. Note which passes remain (`passes_remaining` array)

### Running Revision Passes

**Option A: Tool-Assisted (Recommended)**

1. Run `python tools/revision_prompt_generator.py [scene_path]`
2. Review generated prompts in `/out/revision_prompts/`
3. Apply approved revisions manually
4. Update `revision-manifest.json`

**Option B: Manual Passes**

1. Run each pass in sequence
2. Generate revision prompts (do not auto-apply)
3. Present prompts to author for review
4. Author approves or modifies revisions
5. Update `revision-manifest.json`

### Updating Revision Manifest

After completing a pass:

```bash
python tools/revision_tracker.py pass-complete [chapter] [scene] [pass_name]
```

After completing all passes for a scene:

```bash
python tools/revision_tracker.py complete [chapter] [scene]
```

### Logging Sessions

After each revision session, append to `novel-progress.txt`:

```
---
## [Date] - Revision Session

**Scenes revised:** [list]
**Passes completed:** [list]
**Issues flagged for author:** [list or "none"]
**Notes:** [observations]
```

---

## Revision Prompt Format

All revision suggestions use this standard format:

```
REVISION PROMPT: [Pass Name]
Chapter: [X] | Scene: [scene-name.md]
Line: [N]

ORIGINAL:
> [quoted text - include surrounding context]

ISSUE:
[Clear description of the problem]

PROPOSED REVISION:
> [Suggested replacement text]
> [Alternative option if applicable]

RATIONALE:
[Why this change improves the prose; reference style rules if relevant]
```

**Important:** Generate prompts only. Do not auto-apply changes. Author reviews and decides.

---

## Quality Gates

### Before Marking Scene "revision_complete"

- [ ] Pass 1: Prose Tic Scan — complete
- [ ] Pass 2: Forbidden Pattern Audit — complete
- [ ] Pass 3: Voice Consistency Check — complete
- [ ] Pass 4: Sensory Audit — complete
- [ ] Pass 5: Continuity Verification — complete
- [ ] All prompts reviewed by author
- [ ] `revision-manifest.json` updated

### Before Marking Chapter "revision_complete"

- [ ] All scenes in chapter marked complete
- [ ] Chapter-level continuity verified
- [ ] No outstanding issues flagged

---

## File Reference

| Need | File |
|------|------|
| Revision status tracking | `reference/revision-manifest.json` |
| Scene/chapter structure | `reference/scene-manifest.json` |
| Session log | `reference/novel-progress.txt` |
| Voice patterns & constraints | `claude.md` |
| Prose style rules | `reference/style-rules.md` |
| Lilith integrated prose | `reference/lilith-style-rules.md` |
| Chapter-specific rules | `incarnations/[ch]/period-rules.md` |
| Character details | `incarnations/[ch]/avatar-profile.json` |

---

## Tools Reference

| Tool | Purpose |
|------|---------|
| `prose_tic_analyzer.py` | Scan manuscript for prose tics |
| `prose_tic_analyzer_scenes.py` | Scene-level tic analysis |
| `revision_prompt_generator.py` | Generate formatted revision prompts |
| `revision_tracker.py` | CLI for updating revision-manifest.json |
| `continuity_checker.py` | Cross-reference scenes for consistency |
| `revision_diff.py` | Compare before/after versions |
| `manuscript_analyzer.py` | Comprehensive manuscript analysis |
| `compile_chapters.py` | Reassemble scenes into chapter drafts |

---

## Quick Reference: Revision Priorities

**High Priority (INVIOLABLE violations):**
- Abstract emotion words
- Buddhist terminology
- Missing karmic bridges in death scenes

**Medium Priority (Voice consistency):**
- Missing undermining clauses
- Scene not opening with sensory anchor
- Dialogue without physical grounding

**Lower Priority (Polish):**
- Prose tics (particular, something, em-dash)
- Sensory gaps
- Minor continuity details

---

## Remember

1. **Generate prompts, don't auto-apply** — Author reviews all changes
2. **Voice is paramount** — Every revision should maintain the novel's distinctive style
3. **Function persists, method adapts** — Core patterns transform by period
4. **Track everything** — Update `revision-manifest.json` after each pass
5. **Show through body** — Revisions should replace abstraction with physical sensation
6. **Lilith chapters are revised** — Focus on historical and contemporary chapters
