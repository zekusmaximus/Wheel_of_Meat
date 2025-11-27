# Initializer Agent Prompt

You are setting up the drafting environment for "The Wheel of Meat," a literary novel following one soul's journey toward enlightenment across sixteen lifetimes.

## Your Task

Review the existing project structure and complete any missing scaffolding:

1. **Read existing files:**
   - `scene-manifest.json` - master chapter/scene list
   - `meta/soul-constants.json` - what persists across incarnations
   - `meta/lilith-arc.json` - antagonist progression
   - `meta/thematic-echoes.md` - recurring symbols/situations
   - `novel-progress.txt` - development log
   - `reference/style-rules.md` - prose guidelines

2. **For each chapter folder in `/incarnations/`:**
   - Verify `period-rules.md` exists (historical/genre constraints)
   - Verify `avatar-profile.json` exists (character details)
   - If missing, create from templates

3. **Update `novel-progress.txt`** with:
   - What you found missing
   - What you created
   - Outstanding development needs

4. **Do NOT draft any scenes.** This agent only sets up the environment.

## File Locations

```
/Wheel_of_Meat
  scene-manifest.json
  novel-progress.txt
  /meta
    soul-constants.json
    lilith-arc.json
    thematic-echoes.md
  /reference
    style-rules.md
  /incarnations
    /ch01-contemporary-manchester
    /ch02-prehistoric-jebel-irhoud
    ... (one folder per chapter)
  /prompts
    initializer-prompt.md (this file)
    drafting-prompt.md
```

## Completion Criteria

Environment is ready when:
- [ ] All 16 chapter folders have `period-rules.md`
- [ ] All 16 chapter folders have `avatar-profile.json`
- [ ] `scene-manifest.json` has scene breakdowns for at least one chapter
- [ ] `novel-progress.txt` reflects current state
- [ ] Git commit made with descriptive message
