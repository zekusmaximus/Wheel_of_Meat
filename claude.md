# CLAUDE.md - The Wheel of Meat

## Project Overview

This is a literary novel following one soul's journey toward enlightenment across sixteen lifetimes, spanning 300,000 years. The novel uses an agent-assisted drafting workflow based on Anthropic's research into long-running agents.

**Core Premise:** Silas Pahlavan approaches stream-entry while Lilith Azami, a rival bodhisattva, attempts to derail his progress through his past lives. They ultimately merge to become Maitreya, the future Buddha.

**Structure:** 16 chapters, each in a different historical period and genre, unified by persistent voice patterns and thematic throughlines.

---

## Before You Do Anything

**READ THE RELEVANT FILES FIRST.** This project has extensive documentation. Before drafting or editing:

1. `novel-progress.txt` — Current state, recent sessions, outstanding issues
2. `scene-manifest.json` — Master chapter/scene list with status
3. `reference/style-rules.md` — Core voice patterns (CRITICAL)
4. `reference/voice-analysis.md` — Detailed prose analysis
5. For specific chapters: `incarnations/[chapter-id]/period-rules.md`

---

## Repository Structure

```
/Wheel_of_Meat
├── CLAUDE.md                    # This file
├── scene-manifest.json          # Master scene/chapter tracking
├── novel-progress.txt           # Session log
│
├── /meta
│   ├── soul-constants.json      # What persists across incarnations
│   ├── lilith-arc.json          # Antagonist progression & objectives
│   ├── thematic-echoes.md       # Recurring symbols and situations
│   └── decisions.md             # Log of structural/creative decisions
│
├── /reference
│   ├── style-rules.md           # Core voice patterns
│   └── voice-analysis.md        # Detailed prose analysis from Ch 1-2
│
├── /incarnations
│   └── /[chapter-id]
│       ├── period-rules.md      # Historical/genre constraints
│       ├── avatar-profile.json  # Character details
│       ├── voice-analysis.md    # (if exists) Chapter-specific voice notes
│       └── /scenes
│           └── scene-XX.md      # Draft files
│
└── /prompts
    ├── initializer-prompt.md    # Environment setup instructions
    └── drafting-prompt.md       # Scene drafting instructions
```

---

## The Voice (CRITICAL)

This novel has a distinctive prose style that must persist across all genres and periods. The FUNCTION of each pattern persists; the METHOD adapts.

### Core Patterns (Always Present)

1. **The Undermining Clause** — Every assertion gets complicated
   - Contemporary: "A gesture that seemed both innocent and calculated."
   - Prehistoric: "Ka strong. Ka good hunter. But hunters, different."

2. **Sensory Anchoring** — Physical reality before interiority
   - Always open scenes with environment or body sensation
   - No floating heads, no ungrounded dialogue

3. **Loaded Gestures** — Physical actions carry meaning
   - Small movements encode psychology
   - Scale increases in action-heavy chapters

4. **Environmental Metaphor** — Setting reflects state
   - Weather, light, space mirror emotional/spiritual conditions
   - In prehistoric chapters, self and world are unified

5. **Parallel Construction** — Mirrored phrases for thematic content
   - Contemporary: balanced clauses
   - Prehistoric: ritual repetition

### Forbidden Patterns (Never Do These)

- Filter verbs without purpose ("he saw," "she felt," "he noticed")
- Unearned interiority (pages of internal monologue)
- Dialogue without action (speech must be embodied)
- Setting without meaning (every detail carries weight)
- Single-register dialogue (characters shift speech by context)
- Simple statements (complicate with second clause)

### Genre Adaptation

The voice transforms by period. See `reference/voice-analysis.md` for the transformation table. Key principle:

| Constraint Level | Undermining Method | Anchoring Method |
|-----------------|-------------------|------------------|
| No abstractions (Ch 2) | Paratactic contradiction | Body sensation |
| Formal ancient (Ch 3-6) | Aphoristic reversal | Ritual/material culture |
| Genre-heavy (Ch 7-11) | Genre-appropriate twist | Genre atmosphere |
| Cosmic (Ch 13-16) | Paradox/koan structure | Synesthetic flooding |

---

## The Two Protagonists

### Silas / The Soul

One consciousness across sixteen lives, working toward enlightenment.

**Core Flaw:** Compulsive helping — attachment to being the one who fixes, saves, guides others. This manifests differently in each life but is always present.

**Recognition Markers:** Subtle signs that persist across incarnations (see `meta/soul-constants.json`):
- Patience and observation ("Ka watches. Learns." → Silas's academic temperament)
- [Physical marker TBD]
- [Behavioral marker TBD]

**Spiritual Progression:**
- Chapters 2-11: Developing perfections, maintaining identity-view
- Chapter 12: Stream-entry (breaks first three fetters)
- Chapters 13-14: Once-returner progress
- Chapter 15: Non-returner status
- Chapter 16: Full enlightenment / Merger with Lilith

### Lilith

A rival bodhisattva, very close to Buddhahood, who believes only one Buddha can exist per world-system. See `meta/lilith-arc.json` for full details.

**Key Facts:**
- Same face across all incarnations (dark-haired woman)
- Her interventions ALWAYS backfire — they become the friction that forges his progress
- Power level escalates chapter by chapter
- Each chapter has a specific objective (documented in lilith-arc.json)
- Present-day relationship with Silas: lovers

**The Resolution:** They merge to become Maitreya. The competition was illusory — they were always two aspects of the same future Buddha.

---

## Chapter-by-Chapter Quick Reference

| Ch | Title | Period | Genre | Avatar | Lesson/Fetter | Status |
|----|-------|--------|-------|--------|---------------|--------|
| 1 | The Meeting | Contemporary | Literary/Supernatural | Silas Pahlavan | Introduction | DRAFTED |
| 2 | Blood | 300,000 BCE | Survival Horror | Ka | Cooperation | DRAFTED |
| 3 | The Ledger | 268-232 BCE | Political Thriller | Chandra | Generosity | outlined |
| 4 | The Philosopher | 461-429 BCE | Historical Tragedy | [TBD] | Altruism | needs_dev |
| 5 | The Investigator | 1st-2nd c. CE | Mystery/Drama | [TBD] | Virtue | needs_dev |
| 6 | The Hermit | 3rd-4th c. CE | Spiritual Drama | [TBD] | Renunciation | needs_dev |
| 7 | The Lover | 794-1185 CE | Gothic Romance | [TBD] | Sensual desire | needs_dev |
| 8 | The Accused | 1480-1492 | Psych Horror | [TBD] | Ill will | needs_dev |
| 9 | The Skeptic | 1580-1592 | Phil Adventure | [TBD] | Doubt | needs_dev |
| 10 | The Rebel | 1850-1864 | War Epic | [TBD] | Self-sacrifice | needs_dev |
| 11 | The Detective | 1930s | Noir | [TBD] | Perseverance | needs_dev |
| 12 | The Choice | Contemporary | Supernatural Thriller | Silas | Stream-entry | outlined |
| 13 | The Celestial | Non-temporal | Cosmic Fantasy | Silas (elevated) | Higher fetters | needs_dev |
| 14 | The Prophet | Future | Science Fiction | Silas (elevated) | Once-returner | needs_dev |
| 15 | The Explorer | Far Future | Space Opera/Cosmic Horror | Silas (elevated) | Non-returner | needs_dev |
| 16 | The Awakened | Beyond time | Transcendent | Merged | Arahantship | needs_dev |

---

## Thematic Throughlines

### The Meat/Body Theme

The title refers to the flesh that traps and enables spiritual development. Track manifestations per chapter in `meta/thematic-echoes.md`.

### The Intervention Paradox

Every attempt by Lilith to derail Silas becomes the catalyst for his growth. She is not his enemy — she is his necessary other half.

### The One-Buddha Question

Buddhist texts say one Buddha per world-system. This creates the apparent conflict. Resolution: they were always one Buddha-to-be, appearing as two.

### Foreshadowing Maitreya

Plant references throughout:
- Maitreya statues, texts, passing mentions
- "Loving-kindness" (the name's meaning) in significant contexts
- Moments where duality collapses
- Times when harming him causes her inexplicable pain

---

## Workflow Instructions

### Starting a Session

1. Read `novel-progress.txt`
2. Read `scene-manifest.json` to identify current task
3. Read relevant `period-rules.md` for the chapter
4. Read previous scene's ending if continuing a chapter
5. Check `meta/thematic-echoes.md` for required elements

### Drafting a Scene

1. Draft ONE scene completely
2. Match voice patterns from `reference/style-rules.md`
3. Honor period constraints from chapter's `period-rules.md`
4. Include: soul recognition markers, meat/body theme, Lilith presence (per her power level)
5. Verify against scene requirements before finishing

### Ending a Session

1. Update `scene-manifest.json` with status and word count
2. Update `novel-progress.txt` with:
   - What was drafted
   - Decisions made
   - Continuity concerns
   - Next steps
3. Git commit with descriptive message

### Scene Verification Checklist

- [ ] Opens with sensory anchor
- [ ] Contains undermining clause(s)
- [ ] Physical gestures carry meaning
- [ ] Dialogue shifts register by power dynamics
- [ ] Environment reflects emotional/spiritual state
- [ ] No filter verbs without purpose
- [ ] No unearned interiority
- [ ] POV consistent
- [ ] Recognition markers present (subtle)
- [ ] Genre conventions honored
- [ ] No anachronisms
- [ ] Meat/body theme present
- [ ] Lilith presence appropriate to power level
- [ ] Scene goal achieved
- [ ] Emotional arc complete

---

## Development Priorities

Current phase: **DEVELOPMENT** — completing scaffolding before full drafting.

### Immediate Needs

1. **Unnamed avatars (Ch 4-11)** — Names, occupations, circumstances
2. **Recognition markers** — Physical/behavioral signs of soul continuity
3. **Period-rules.md completion** — Each chapter needs full documentation
4. **Scene breakdowns** — Individual scenes within each chapter

### Before Drafting Any Chapter

Ensure the chapter folder contains:
- [ ] Completed `period-rules.md` with voice adaptation notes
- [ ] Completed `avatar-profile.json` with full arc
- [ ] Scene list in `scene-manifest.json`
- [ ] Lilith's objective documented in `meta/lilith-arc.json`

---

## Key Files to Reference

| Need | File |
|------|------|
| Current project state | `novel-progress.txt` |
| What to work on next | `scene-manifest.json` |
| How to write prose | `reference/style-rules.md` |
| Deep voice analysis | `reference/voice-analysis.md` |
| Soul/spiritual framework | `meta/soul-constants.json` |
| Lilith's role per chapter | `meta/lilith-arc.json` |
| Recurring symbols | `meta/thematic-echoes.md` |
| Why decisions were made | `meta/decisions.md` |
| Chapter-specific rules | `incarnations/[ch]/period-rules.md` |
| Character details | `incarnations/[ch]/avatar-profile.json` |

---

## Commit Message Format

```
[Type]: [chapter-id]/[scene] - [summary]

[Details if needed]
```

Types:
- `Draft` — New scene content
- `Revise` — Changes to existing draft
- `Dev` — Development work (profiles, rules, structure)
- `Doc` — Documentation updates
- `Fix` — Corrections to errors

Examples:
- `Draft: ch02/full - Complete Ka chapter draft`
- `Dev: ch04 - Avatar profile for Athenian philosopher`
- `Doc: Update voice-analysis with Ch3 patterns`

---

## Contact with Author

This project is being developed collaboratively with the author (Jeffrey). Key decisions should be logged in `meta/decisions.md` with reasoning. If uncertain about:

- Character motivation
- Plot logic
- Thematic interpretation
- Voice/style questions

Document the uncertainty and flag for author review rather than making assumptions.

---

## Remember

1. **Read before writing** — The documentation exists for a reason
2. **Voice is paramount** — Every sentence should feel like this novel
3. **Function persists, method adapts** — Core patterns transform by period
4. **Lilith always backfires** — Her opposition enables his growth
5. **They become Maitreya** — The ending recontextualizes everything
6. **One scene at a time** — Incremental progress, clean state after each session
