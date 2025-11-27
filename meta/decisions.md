# Decisions Log

This document records key structural and creative decisions made during development, with reasoning. Reference this when revising or troubleshooting.

---

## Structural Decisions

### Decision: Agent-based drafting workflow
**Date:** [Current date]
**Decision:** Use long-running agent pattern (initializer + drafting agents) for scene generation
**Reasoning:** Novel's complexity (16 genres, 16 time periods, dual protagonists with interlocking arcs) requires systematic tracking that exceeds what ad-hoc drafting can maintain. Agent pattern enforces consistency across context windows.
**Source:** Anthropic's "Effective harnesses for long-running agents" research

### Decision: One folder per incarnation
**Date:** [Current date]
**Decision:** Each chapter gets its own folder with period-rules.md and avatar-profile.json
**Reasoning:** Genre/period constraints vary dramatically; centralizing would create unwieldy documents. Folder structure mirrors the novel's episodic nature.

### Decision: Scene-level granularity for manifest
**Date:** [Current date]
**Decision:** Track individual scenes, not just chapters
**Reasoning:** Agent needs atomic units of work. Chapter-level is too coarse for incremental progress.

---

## Character Decisions

### Decision: [TBD]
**Date:**
**Decision:**
**Reasoning:**

---

## Thematic Decisions

### Decision: [TBD]
**Date:**
**Decision:**
**Reasoning:**

---

## Plot Decisions

### Decision: [TBD]
**Date:**
**Decision:**
**Reasoning:**

---

## Voice/Style Decisions

### Decision: [TBD]
**Date:**
**Decision:**
**Reasoning:**

---

## Revision Notes

[Add notes here when revisiting decisions or discovering problems]
