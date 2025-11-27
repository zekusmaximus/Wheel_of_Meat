# The Wheel of Meat

A literary novel following one soul's journey toward enlightenment across sixteen lifetimes, spanning 300,000 years from prehistoric Morocco to transcendent realms beyond time.

## Premise

Silas Pahlavan, a philosophy professor in contemporary Manchester, is approaching stream-entry—the first stage of Buddhist enlightenment. Lilith Azami, a psychiatrist with growing supernatural abilities, can see his past lives and is determined to stop his progress. As Silas's accumulated incarnations unfold, Lilith's power grows, building toward a confrontation that will determine whether enlightenment—or something else—awaits.

## Structure

- **Act 1:** Contemporary Manchester - Introduction
- **Act 2:** Ten past lives spanning prehistory to 1930s America
- **Act 3:** The breakthrough - Stream-entry achieved
- **Act 4:** Post-enlightenment progression through higher realms

Each chapter operates in a distinct genre mode while maintaining thematic and narrative unity.

## Repository Structure

```
/Wheel_of_Meat
  scene-manifest.json          # Master scene/chapter tracking
  novel-progress.txt           # Session log for drafting
  
  /meta
    soul-constants.json        # What persists across incarnations
    lilith-arc.json            # Antagonist progression
    thematic-echoes.md         # Recurring symbols and situations
    decisions.md               # Log of structural/creative decisions
  
  /reference
    style-rules.md             # Prose guidelines by genre
  
  /incarnations
    /ch01-contemporary-manchester
    /ch02-prehistoric-jebel-irhoud
    /ch03-mauryan-india
    ... (one folder per chapter)
      period-rules.md          # Historical/genre constraints
      avatar-profile.json      # Character details
      /scenes
        scene-01.md
        scene-02.md
  
  /prompts
    initializer-prompt.md      # Agent setup instructions
    drafting-prompt.md         # Scene drafting instructions
```

## Development Workflow

This project uses an agent-assisted drafting workflow based on Anthropic's research into long-running agents.

1. **Brainstorming/Structure:** Collaborative development in Claude chat
2. **Environment Setup:** Initializer agent ensures scaffolding is complete
3. **Drafting:** Scene-by-scene drafting with systematic verification
4. **Revision:** Separate passes for continuity, style, and polish

## Status

**Phase:** Development - completing chapter scaffolding and avatar profiles before drafting begins.
