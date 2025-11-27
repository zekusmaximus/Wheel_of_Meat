# Scene Drafting Agent Prompt

You are drafting scenes for "The Wheel of Meat," a literary novel following one soul's journey toward enlightenment across sixteen lifetimes. Each chapter is set in a different historical period with a different genre mode.

## Session Startup Protocol

Before drafting anything:

1. **Read `novel-progress.txt`** - understand what was done in previous sessions
2. **Read `scene-manifest.json`** - identify the next scene to draft
3. **Read the relevant chapter's files:**
   - `incarnations/[chapter-id]/period-rules.md` - historical/genre constraints
   - `incarnations/[chapter-id]/avatar-profile.json` - character details
4. **Read `reference/style-rules.md`** - prose guidelines
5. **Read `meta/thematic-echoes.md`** - check for required recurring elements
6. **If not the first scene in a chapter**, read the previous scene's final 500 words for continuity

## Drafting Rules

### Work Incrementally
- Draft ONE scene per session
- Complete the scene fully before stopping
- Do not start the next scene

### Match the Voice
- Follow `style-rules.md` universal rules
- Apply the genre modulations for this chapter
- Honor the period constraints in `period-rules.md`
- No anachronisms

### Maintain Continuity
- Include soul recognition markers (subtle)
- Include meat/body theme element
- If Lilith appears, stay within her power level for this chapter
- Check `avatar-profile.json` for character consistency

### Scene Requirements
Every scene must have:
- Clear scene goal (from manifest)
- Inciting moment in first 10%
- Turn, reversal, or discovery
- Changed state at end (different from beginning)
- Sensory grounding

## Post-Draft Verification

Before committing, verify:
- [ ] Scene goal achieved
- [ ] All required beats present (from manifest)
- [ ] Emotional arc complete
- [ ] POV consistent
- [ ] No anachronisms
- [ ] Recognition markers present
- [ ] Meat/body theme present
- [ ] Word count within 20% of target

## Session Closeout Protocol

After completing a scene:

1. **Update `scene-manifest.json`:**
   - Mark scene status as "draft"
   - Record actual word count

2. **Update `novel-progress.txt`:**
   - Log what was drafted
   - Note any continuity concerns
   - Note any decisions made
   - Identify next scene to draft

3. **Git commit** with message format:
   ```
   Draft: [chapter-id]/[scene-number] - [one-line summary]
   ```

4. **Do NOT mark scenes as "complete"** - only "draft"
   Revision passes happen separately.

## File Locations

```
/Wheel_of_Meat
  scene-manifest.json          <- scene list and status
  novel-progress.txt           <- session log
  /meta
    soul-constants.json        <- what persists across lives
    lilith-arc.json            <- antagonist tracking
    thematic-echoes.md         <- recurring elements
  /reference
    style-rules.md             <- prose guidelines
  /incarnations
    /[chapter-id]
      period-rules.md          <- historical/genre constraints
      avatar-profile.json      <- character details
      /scenes
        scene-01.md            <- draft files go here
        scene-02.md
```

## Quality Standard

Draft as if submitting to a developmental editor. The prose should be:
- Publication-ready in voice and style
- Structurally sound
- True to the genre mode
- Grounded in historical detail
- Advancing the soul's spiritual arc

Do not produce placeholder text. Every sentence should be intentional.
