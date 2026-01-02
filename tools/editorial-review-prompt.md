# Scene Editorial Review Protocol

## Purpose
Provide comprehensive line-level editorial feedback for individual scenes from *The Wheel of Meat*, ensuring technical precision, voice consistency, thematic coherence, and chapter-level structural integrity.

## Context Loading Requirements

Before analyzing the target scene, load and review these files:

1. **Target scene**: `scenes/chapter-XX/scene-YY.md`
2. **Full chapter**: `chapters/chapter-XX/chapter-XX.md` (for context and coherence)
3. **Voice patterns**: `docs/voice-analysis.md` (core prose patterns)
4. **Period constraints**: `chapters/chapter-XX/period-rules.md` (era-specific writing rules)
5. **Character state**: `chapters/chapter-XX/avatar-profile.json` (spiritual development, relationships, vulnerabilities)
6. **Thematic framework**: `docs/thematic-requirements.md` (Buddhist concepts, recurring symbols, lesson chains)
7. **Lilith objectives**: `docs/lilith-motivation.md` (intervention backfire, same-face appearance)

## Analysis Framework

Provide feedback in the following priority order. Be ruthlessly specific—cite line numbers, quote exact text, and provide concrete revisions.

### 1. Technical Issues (Priority: HIGH)

Mechanical problems that undermine readability or professionalism.

**Check for:**
- **Em-dash overuse**: More than one em-dash per sentence dilutes impact
- **Comma splices**: Independent clauses joined with comma instead of semicolon/period
- **Semicolon errors**: In dialogue, after conjunctive adverbs without independent clauses
- **Unclear antecedents**: Pronouns without obvious referents, especially after multiple entities
- **Ambiguous "which/that" clauses**: Referent unclear due to distance or multiple possible nouns
- **Awkward phrasing**: Clunky constructions, unintentional repetition within 3 sentences
- **Rhythm problems**: Three or more consecutive sentences of similar length/structure
- **Paragraph length**: Single-sentence paragraphs without justification; walls of text >200 words

**Output format:**
- Line [X]: [Issue type]
  - Current: "[exact quote]"
  - Problem: [what's wrong]
  - Fix: "[specific revision]"

### 2. Voice Pattern Compliance (Priority: HIGH for thresholds, ADVISORY for stylistic flavor)

Adherence to core voice patterns documented in style guides. Note that these patterns apply differently across POVs:
- **Historical avatar chapters** (2, 4, 6, 8, 10, 12, 14, 16, 18, 20): Period-appropriate transformation of patterns
- **Lilith integrated chapters** (3, 5, 7, 9, 11, 13, 15, 17, 19, 21): Temporal integration technique
- **Contemporary dual-POV chapters** (1, 22): Slight distance, veiled interiority

#### a) Undermining Clause — ADVISORY (Stylistic Flavor)
> **Note:** This is NOT a hard threshold. It's a stylistic flavor that varies by scene needs and POV. Use judgment rather than mechanical percentage.

- **Pattern**: Assertions get complicated or qualified at key moments
- **Spirit**: Epistemological uncertainty—conclusions are partial, perception is limited
- **When it matters most**: Moments of insight, judgment, or conclusion
- **When it's fine to omit**: Emphatic beats, rhythmic punctuation, action sequences

**Review for:**
- Extended passages (5+ sentences) of unqualified certainty where a character draws conclusions
- Moments where a character *should* be uncertain but asserts with false confidence
- Thematic beats where complexity would deepen meaning

#### b) Sensory Anchoring (Target: 75%+ of paragraphs)
- **Pattern**: Physical reality before interiority; concrete before abstract
- **Violations**: Paragraphs opening with thought/emotion; ungrounded dialogue

**Flag:**
- Paragraphs starting with "He thought," "She felt," "He wondered"
- Dialogue without physical beats or environmental context
- Extended internal monologue without sensory grounding

#### c) Loaded Gesture (Target: 40%+ of paragraphs)
- **Pattern**: Physical actions carry psychological/spiritual meaning
- **Violations**: Generic blocking; actions without subtext

**Flag:**
- Generic movements (walked, sat, stood) without emotional charge
- Paragraphs of pure dialogue with no physical business
- Gestures that don't reveal character state

#### d) Environmental Metaphor (Target: 50%+ of paragraphs)
- **Pattern**: Setting reflects emotional/spiritual state
- **Violations**: Neutral or absent setting; description without purpose

**Flag:**
- Scenes without environmental details
- Setting that doesn't echo inner state
- Weather/light/architecture described generically

#### e) Parallel Construction (Target: 20%+ of paragraphs)
- **Pattern**: Mirrored phrases for thematic emphasis
- **Violations**: Opportunities for parallelism missed; list items with inconsistent structure

**Flag:**
- Passages making related points without syntactic mirroring
- List items with different grammatical structures
- Missed opportunities for antithesis or echo

**Output format:**
- [Pattern name] violation in lines [X-Y]
  - Current approach: [describe what's happening]
  - Pattern requirement: [what the voice demands]
  - Suggested revision: [specific rewrite showing pattern in action]

### 3. Period Authenticity (Priority: HIGH for historical chapters)

Check adherence to era-specific constraints in `period-rules.md`.

**Check for:**
- **Anachronistic vocabulary**: Modern words/concepts in historical settings
- **Anachronistic syntax**: Contemporary sentence structures in ancient periods
- **Technology mismatches**: References to tools/objects not yet invented
- **Social convention errors**: Attitudes or behaviors that violate period norms
- **Pattern transformation failures**: Modern voice patterns not adapted to era

**Output format:**
- Line [X]: Anachronism detected
  - Problem: "[quoted text]" - [why it's wrong for this period]
  - Correction: "[period-appropriate revision]"

### 4. Thematic Coherence (Priority: MEDIUM)

Alignment with Buddhist framework and symbolic systems.

**Check for:**

#### a) Spiritual Development Tracking
- Does avatar's state match `avatar-profile.json` spiritual markers?
- Are incomplete realizations seeding next lifetime's challenges?
- Does scene show spiritual progress or regression appropriately?

#### b) Recurring Symbols
- Opportunities to integrate: hands, thresholds, mirrors, circles, water, light/shadow
- Symbol usage that contradicts established meanings
- Heavy-handed symbol deployment (too obvious)

#### c) Buddhist Concepts (embodied, never named)
- Impermanence, attachment, suffering, non-self appropriately rendered?
- Spiritual truths shown through action/sensation, not explained?
- Dharma concepts present but invisible to characters?

#### d) Lilith Intervention Logic
- Does her same-face appearance register correctly?
- Is intervention setup clearly backfiring into catalyst?
- Are moments of duality collapse foreshadowing Maitreya merger?

**Output format:**
- [Thematic element]: [Assessment]
  - Current state: [what's there now]
  - Opportunity: [what could deepen theme]
  - Suggested integration: [specific addition or revision]

### 5. Chapter-Level Structure (Priority: MEDIUM)

Scene's function within larger chapter arc.

**Check for:**
- **Transitions**: Abrupt jumps between scenes; missing connective tissue
- **Pacing**: Scenes that drag relative to importance; rushed revelations
- **Information flow**: Key details disclosed too early or withheld too long
- **Tension curve**: Flat sections where stakes should escalate
- **Scene necessity**: Does this scene earn its space? Could it be cut or combined?

**Output format:**
- Structural issue: [Problem]
  - Impact on chapter: [how it affects pacing/coherence]
  - Recommendation: [cut/expand/move/revise] - [justification]

### 6. Specific Line Revisions (Priority: Variable)

For the 8-10 most critical issues across all categories, provide:

**Format:**
```
LINE [X]: [Issue category - Technical/Voice/Period/Theme/Structure]

Current:
[Exact quote from scene]

Problem:
[Precise diagnosis - what's wrong and why]

Suggested Revision:
[Specific rewrite that fixes the issue]

Rationale:
[Why this revision works - connects to voice/theme/period requirements]
```

## Output Structure

Use this exact heading structure for the report:

```
# Editorial Review: [Scene Name]
## Scene: chapter-XX/scene-YY.md

### 1. Technical Issues
[Findings with line numbers and specific fixes]

### 2. Voice Pattern Compliance
[Pattern-by-pattern assessment with violations and corrections]

### 3. Period Authenticity
[Era-specific issues and corrections - skip if contemporary]

### 4. Thematic Integration
[Spiritual/symbolic assessment with enhancement opportunities]

### 5. Chapter Structure
[Scene's function and pacing within chapter arc]

### 6. Priority Line Revisions
[Top 8-10 most critical fixes with full format above]

### 7. Summary Assessment
- Overall voice consistency: [Strong/Adequate/Weak]
- Technical polish: [Clean/Needs work/Significant issues]
- Thematic depth: [Rich/Present/Underdeveloped]
- Revision priority: [Minor/Moderate/Major]
```

## Execution Standards

- **Be specific**: Line numbers, exact quotes, concrete revisions
- **Be direct**: Say "This is wrong" not "Consider whether"
- **Be complete**: Don't say "similar issues in other lines"—find and fix them all
- **Respect the voice**: Revisions must maintain established patterns
- **Honor the period**: Fixes must work within era constraints
- **Serve the theme**: Even technical corrections should deepen spiritual resonance

## Notes

- This is professional developmental editing—be honest about weaknesses
- Flag patterns across the scene, not just individual instances
- Prioritize issues that compound (voice violations create thematic problems)
- If a scene has fundamental structural problems, say so before line-editing
- Trust your judgment—if something feels off, name it specifically
