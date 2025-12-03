# CLAUDE.md - The Wheel of Meat

## How to Use This File

This document describes **what the novel is** and **how it should read**.

For **how to work on this project** (session workflow, error handling, verification procedures), see `agent-protocol.md`.

Read this file to understand voice, character, and theme. Read `agent-protocol.md` to understand procedure and workflow.

-----

## Project Overview

A literary novel following one soul’s journey toward enlightenment across sixteen lifetimes, spanning 300,000 years. Each chapter operates in a distinct historical period and genre (survival horror, political thriller, noir, cosmic fantasy, etc.) while maintaining unified voice patterns and thematic throughlines.

**Core Premise:** Philosophy professor Silas Pahlavan approaches stream-entry while psychiatrist Lilith Azami—a rival bodhisattva who appears with the same face across all his past lives—attempts to derail his progress. Her interventions always backfire, becoming the friction that forges his growth. They ultimately merge to become Maitreya, the future Buddha. The competition was illusory; they were always two aspects of the same being.

**Structure:** 26 chapters in 4 acts:

|Act    |Chapters|Content                                                  |
|-------|--------|---------------------------------------------------------|
|Act I  |1       |Contemporary Manchester—introduction                     |
|Act II |2-21    |Ten historical lives alternating with ten Lilith chapters|
|Act III|22      |Contemporary Manchester—stream-entry and Lilith’s turn   |
|Act IV |23-26   |Post-stream-entry realms—full enlightenment and merger   |

**Act II Alternating Structure:**

- Historical chapter (Silas’s past life) → Lilith chapter (her contemporary pursuit)
- Both timelines move forward: his past lives progress chronologically; her present-day life ages from 25 to 35 over a decade
- This creates parallel momentum toward their convergence in Chapter 22

-----

## Constraint Hierarchy

### INVIOLABLE (Breaking these ruins the novel)

1. **No Buddhist terminology in prose** — Never use dharma, karma, samsara, nirvana, enlightenment, attachment, suffering, awakening, meditation, mindfulness. Show through experience; reader infers meaning. *Exception: historical accuracy (Ashoka’s edicts may reference “Dhamma”).*
1. **No abstract emotion words** — Never write afraid, angry, sad, happy, anxious, nervous, excited, worried, relieved, frustrated, confused, surprised, lonely, guilty, ashamed, proud, jealous, hopeful, desperate. Render all internal states through physical sensation, action, or environment.
1. **Lilith’s interventions always backfire** — Every attempt to derail Silas becomes the catalyst for his growth. No exceptions. She is not his enemy; she is his necessary other half.
1. **Death scenes must include karmic bridge** — The final clinging-thought shapes the next life. Extended, visceral, with clear connection to next chapter’s lesson.
1. **Voice patterns persist across all genres** — The undermining clause, sensory anchoring, loaded gestures, environmental metaphor, and parallel construction adapt their METHOD by period but their FUNCTION never disappears.
1. **They become Maitreya** — The ending recontextualizes everything. Foreshadow throughout: moments where duality collapses, times when harming him causes her inexplicable pain.
1. **Same face across all incarnations** — Lilith appears as the same dark-haired woman in every life. Readers recognize her before avatars do.

### HIGH-PRIORITY (Confirm with author if uncertain)

- All five senses present in every scene
- Recognition markers (once defined) in every chapter
- Genre conventions honored while maintaining voice
- Lilith’s power level matches chapter (see `lilith-arc.json` and `lilith-chapter-manifest.json`)
- Sensory anchor opens every scene (environment before interiority)
- Meat/body theme present in every chapter
- Lilith chapters include demonstration scene (she shows mastery of relevant fetter)

### PREFERENCES (Apply when consistent with scene)

- Specific sensory palette per setting (develop before drafting)
- Dialogue tags omitted when action makes speaker clear
- Deliberate fragments in pairs/triads for emphasis
- Environmental metaphor mirrors or contrasts emotional state
- Parallel construction for philosophical content

-----

## The Voice

This novel has a distinctive prose style. The FUNCTION of each pattern persists; the METHOD adapts by period.

### Core Patterns

**1. The Undermining Clause**
Every assertion gets complicated by a second element. Surface acknowledged, then contradicted or darkened.

- Contemporary: “A gesture that seemed both innocent and calculated.”
- Prehistoric: “Ka strong. Ka good hunter. But hunters, different.”
- Formal ancient: Aphoristic reversal
- Cosmic: Paradox/koan structure

**2. Sensory Anchoring**
Physical reality before interiority. Open scenes with environment or body sensation. No floating heads, no ungrounded dialogue.

- Contemporary: Observed environment
- Prehistoric: Felt body
- Formal ancient: Ritual/material culture
- Cosmic: Synesthetic flooding

**3. Loaded Gestures**
Physical actions carry psychological/spiritual meaning. Small movements encode what characters cannot say.

**4. Environmental Metaphor**
Setting reflects emotional/spiritual state. Weather, light, space mirror interior conditions. In prehistoric chapters, self and world are unified.

**5. Parallel Construction**
Mirrored phrases for thematic content. Used to contrast states, embed philosophy, create incantatory rhythm in spiritual moments.

**6. Emotional Through Physical**
All internal states rendered through body sensation, action, or environment. The forbidden emotion words list exists because this rule is non-negotiable.

### Forbidden Patterns

1. **Filter verbs without purpose** — “he saw,” “she felt,” “he noticed,” “she realized” distance reader from experience
1. **Unearned interiority** — Thoughts are brief, observed; no pages of internal monologue
1. **Dialogue without action** — Speech is embodied; every exchange needs physical grounding
1. **Setting without meaning** — Every environmental detail carries weight
1. **Single-register dialogue** — Characters shift speech by context and power dynamics
1. **Simple statements** — Complicate with second clause or observation
1. **Abstract emotion words** — See INVIOLABLE constraints
1. **Buddhist terminology** — See INVIOLABLE constraints
1. **Exposition dumps** — Information emerges through action and sensory detail
1. **On-the-nose dialogue** — Subtext over text; what’s unsaid matters
1. **Explaining the theme** — Trust the reader
1. **Modern anachronisms** — Research each period thoroughly (objects, concepts, attitudes, vocabulary)
1. **Head-hopping within scenes** — One POV per scene; switch only at clear breaks
1. **Generic descriptions** — “Beautiful,” “strange,” “interesting” are empty; specify
1. **Consequence-free violence** — Injuries and deaths matter; show the cost

See `style-rules.md` for the complete list with examples and physical manifestation reference tables.
See `contemporary-period-rules.md` for Manchester-specific voice and setting guidance.

### Genre Adaptation

|Period                                                     |Vocabulary                                      |Undermining Method      |Anchoring Method       |
|-----------------------------------------------------------|------------------------------------------------|------------------------|-----------------------|
|Prehistoric (Ch 2)                                         |Concrete nouns, sensory verbs, no abstractions  |Paratactic contradiction|Body sensation         |
|Ancient/Classical (Ch 4, 6, 8, 10)                         |Period-appropriate, not archaic pastiche        |Aphoristic reversal     |Ritual/material culture|
|Medieval/Early Modern (Ch 12, 14, 16)                      |Genre-colored formality                         |Genre-appropriate twist |Genre atmosphere       |
|Modern (Ch 18, 20)                                         |Genre-specific (War = expansive; Noir = clipped)|Genre-appropriate twist |Genre atmosphere       |
|Contemporary (Ch 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22)|Academic, clinical, restrained                  |Grammatical complexity  |Observed environment   |
|Cosmic (Ch 23-26)                                          |Abstract, synesthetic, neologism-possible       |Paradox/koan structure  |Synesthetic flooding   |

-----

## The Two Protagonists

### Silas / The Soul

One consciousness across sixteen lives, working toward enlightenment. No memory crosses between lives; continuity is causal, not substantial.

**Core Flaw:** Compulsive helping—attachment to being the one who fixes, saves, guides others. This manifests differently in each life but is always present. The helper identity reinforces the sense of separate self, which is the actual obstacle.

**Recognition Markers** (for reader continuity; characters don’t recognize themselves):

- Patience and observation (“Ka watches. Learns.” → Silas’s academic temperament)
- [Physical marker TBD]
- [Behavioral marker TBD]

**Spiritual Progression:**

- Chapters 2-20 (historical): Developing perfections, maintaining identity-view
- Chapter 22: Stream-entry (breaks first three fetters: self-illusion, doubt, attachment to rites)
- Chapters 23-24: Once-returner progress
- Chapter 25: Non-returner status
- Chapter 26: Full enlightenment / Merger with Lilith

### Lilith

A rival bodhisattva, very close to Buddhahood, who believes only one Buddha can exist per world-system. Her grasping at Buddhahood is itself the attachment that prevents her enlightenment—she cannot see that releasing her claim would free her.

**Key Facts:**

- Same face across all incarnations (dark-haired woman)
- Her interventions ALWAYS backfire—they become the friction that forges his progress
- Power level escalates chapter by chapter (see `lilith-arc.json`)
- Each chapter has a specific objective (documented in `lilith-arc.json`)
- Present-day relationship with Silas: lovers
- Spiritual status: Non-Returner (has broken 5 of 10 fetters; her final obstacle is attachment to being “the one”)

**Power Constraints:**

- Can observe past lives but cannot change past events
- Can influence circumstances and people, not Silas directly
- Cannot force his choices or negate his accumulated merit
- Her interventions have karmic consequences for herself
- Power grows from observation (Ch 2-3) → influence (Ch 4-11) → manifestation (Ch 12-19) → full presence (Ch 20-22) → cosmic scale (Ch 23-26)

**Her Arc Across Act II:**
The 10 Lilith chapters (3, 5, 7, 9, 11, 13, 15, 17, 19, 21) show her contemporary pursuit:

- Age 25-35 over a decade
- Powers escalating from observation to full incarnation
- Professional life declining as obsession grows
- Each chapter demonstrates mastery of the fetter Silas struggles with—while remaining blind to her own final attachment

**The Resolution:** They merge to become Maitreya, the future Buddha. The “one Buddha per world-system” rule was true but misunderstood—there was only ever one Buddha-to-be, appearing as two until ready to unite.

-----

## Chapter Quick Reference

### Act I: The Meeting

|Ch|Title      |Type        |Avatar/Focus  |Status |
|--|-----------|------------|--------------|-------|
|1 |The Meeting|Contemporary|Silas + Lilith|DRAFTED|

### Act II: The Wheel Turns (Alternating Structure)

|Ch|Title              |Type      |Avatar/Focus        |Lesson/Focus                      |Status   |
|--|-------------------|----------|--------------------|----------------------------------|---------|
|2 |Blood              |Historical|Ka (300,000 BCE)    |Cooperation/Mettā                 |DRAFTED  |
|3 |The Discovery      |Lilith    |Lilith age 25       |Tracks Ka; first discovery        |DRAFTED  |
|4 |The Ledger         |Historical|Chandra (268 BCE)   |Generosity/Dāna                   |outlined |
|5 |The Ledger’s Shadow|Lilith    |Lilith age 26       |Tracks Chandra; first intervention|needs_dev|
|6 |The Philosopher    |Historical|TBD (Athens 450 BCE)|Wisdom/Paññā                      |needs_dev|
|7 |TBD                |Lilith    |Lilith age 27       |Dream influence                   |needs_dev|
|8 |The Investigator   |Historical|TBD (Rome 100 CE)   |Virtue/Sīla                       |needs_dev|
|9 |TBD                |Lilith    |Lilith age 28       |Circumstance manipulation         |needs_dev|
|10|The Hermit         |Historical|TBD (Egypt 350 CE)  |Renunciation/Nekkhamma            |needs_dev|
|11|TBD                |Lilith    |Lilith age 29       |Growing control                   |needs_dev|
|12|The Lover          |Historical|TBD (Heian 1000 CE) |Equanimity/Upekkhā                |needs_dev|
|13|TBD                |Lilith    |Lilith age 30       |First manifestation               |needs_dev|
|14|The Accused        |Historical|TBD (Spain 1485)    |Patience/Khanti                   |needs_dev|
|15|TBD                |Lilith    |Lilith age 31       |Sustained presence                |needs_dev|
|16|The Skeptic        |Historical|TBD (France 1585)   |Truthfulness/Sacca                |needs_dev|
|17|TBD                |Lilith    |Lilith age 32       |Extended interaction              |needs_dev|
|18|The Rebel          |Historical|TBD (China 1855)    |Determination/Adhiṭṭhāna          |needs_dev|
|19|TBD                |Lilith    |Lilith age 33       |Near-full manifestation           |needs_dev|
|20|The Detective      |Historical|TBD (USA 1930s)     |Perseverance/Viriya               |needs_dev|
|21|The Decision       |Lilith    |Lilith age 34       |Full manifestation; incarnates    |needs_dev|

### Act III: The Breakthrough

|Ch|Title     |Type        |Avatar/Focus  |Status  |
|--|----------|------------|--------------|--------|
|22|The Choice|Contemporary|Silas + Lilith|outlined|

### Act IV: The Ascension

|Ch|Title        |Type  |Setting               |Status   |
|--|-------------|------|----------------------|---------|
|23|The Celestial|Cosmic|Deva Realm            |needs_dev|
|24|The Prophet  |Cosmic|Future Earth          |needs_dev|
|25|The Explorer |Cosmic|Deep Space            |needs_dev|
|26|The Awakened |Cosmic|Pure Abodes / Maitreya|needs_dev|

-----

## Thematic Throughlines

### The Meat/Body Theme

The title refers to the flesh that traps and enables spiritual development. Each chapter manifests this differently—track in `thematic-echoes.md`.

### The Intervention Paradox

Every attempt by Lilith to derail Silas becomes the catalyst for his growth. Opposition is necessary for enlightenment. She is not the enemy of his awakening—she is its unwitting catalyst.

### The One-Buddha Question

Buddhist texts say one Buddha per world-system. This creates the apparent conflict. Resolution: they were always one Buddha-to-be, appearing as two.

### Karmic Bridges

Each death plants the seed for the next life’s lesson. The flame metaphor: consciousness transfers like fire between candles—not the same flame, yet not entirely different.

### The Demonstration Technique (Lilith Chapters)

In each Lilith chapter, she demonstrates mastery of the fetter Silas struggles with in the corresponding historical chapter—while remaining blind to her own final attachment. This creates devastating irony: she sees truth perfectly, articulates it beautifully, cannot apply it to herself.

### Foreshadowing Maitreya

Plant throughout:

- Maitreya statues, texts, passing mentions
- “Loving-kindness” (the name’s meaning) in significant contexts
- Moments where duality collapses
- Times when harming him causes her inexplicable pain
- Dreams or visions where they appear as one being
- Her unexplained attraction to him that exceeds tactical necessity

-----

## Lilith Chapter Requirements

Each of the 10 Lilith chapters (Ch 3, 5, 7, 9, 11, 13, 15, 17, 19, 21) must include:

### 1. Demonstration Scene

She shows mastery of the fetter Silas struggles with in the corresponding historical chapter:

- Patient or colleague describes situation paralleling her pursuit
- She offers genuinely wise counsel
- Physical tell undercuts her equanimity (shaking hands, etc.)
- Returns to tracking/intervention without applying her own advice

### 2. Tracking Content

- What she observes of the corresponding historical life
- What intervention she attempts (matching her power level)
- What she tracks forward to (next avatar)

### 3. Physical Cost

Tracking and intervention have bodily consequences:

- Early chapters: Headaches, exhaustion
- Middle chapters: Days of recovery after manifestation
- Late chapters: Full incarnation “like dying and being born”

### 4. Professional Life Marker

Her career declines as obsession grows:

- Ch 3-7: Thriving → distracted
- Ch 9-15: Considering leave → partial leave
- Ch 17-21: Full leave; decade consumed

### 5. Maitreya Foreshadowing (Subtle)

0-2 moments per chapter maximum:

- Hesitation before interventions
- Inexplicable pain when she causes him suffering
- Pull toward him that exceeds tactical calculation

See `lilith-chapter-manifest.json` for detailed per-chapter requirements.
See `contemporary-period-rules.md` for voice and setting guidance.

-----

## Never Improvise (Require Author Approval)

The agent must NOT independently create or modify:

- Reincarnation/rebirth mechanics
- Lilith’s powers or constraints beyond what’s documented
- Fetter progression or breaking sequence
- New chapters or structural changes
- Recognition markers (until defined by author)
- The Maitreya resolution or how the merger occurs
- Any Buddhist cosmology or metaphysics
- Plot twists not documented in scene-manifest.json
- New characters with cross-chapter significance
- How Silas and Lilith meet in present day (documented in Ch 21)
- The mechanism of stream-entry in Chapter 22

If any of these seem necessary for a scene to work, document the need in `novel-progress.txt` and wait for author input.

-----

## Key Files Reference

|Need                          |File                                   |
|------------------------------|---------------------------------------|
|Current project state         |`novel-progress.txt`                   |
|What to work on next          |`scene-manifest.json`                  |
|How to write prose            |`style-rules.md`                       |
|Deep voice analysis           |`voice-analysis.md`                    |
|Contemporary chapters voice   |`contemporary-period-rules.md`         |
|Soul/spiritual framework      |`soul-constants.json`                  |
|Lilith’s historical role      |`lilith-arc.json`                      |
|Lilith’s contemporary chapters|`lilith-chapter-manifest.json`         |
|Recurring symbols             |`thematic-echoes.md`                   |
|Chapter-specific rules        |`incarnations/[ch]/period-rules.md`    |
|Character details             |`incarnations/[ch]/avatar-profile.json`|
|Workflow & procedures         |`agent-protocol.md`                    |

-----

## Remember

1. **Voice is paramount** — Every sentence should feel like this novel
1. **Function persists, method adapts** — Core patterns transform by period
1. **Lilith always backfires** — Her opposition enables his growth
1. **They become Maitreya** — The ending recontextualizes everything
1. **Show through body** — No abstract emotions, no Buddhist jargon, no exposition
1. **Death scenes matter** — Extended, visceral, with clear karmic bridge
1. **Same face** — Readers recognize Lilith before Silas does
1. **Lilith chapters demonstrate** — She shows mastery of what he struggles with
1. **Parallel momentum** — Both timelines move forward in Act II
1. **The irony is unspoken** — Trust readers to see her blind spot