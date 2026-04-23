from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "chapter_by_chapter_revisions.md"


WORD_COUNTS = {
    "CH04": 19433,
    "CH06": 10436,
    "CH08": 9870,
    "CH10": 14039,
    "CH12": 8809,
    "CH14": 18733,
    "CH16": 14413,
    "CH18": 8720,
    "CH20": 13800,
}


CONFIG = {
    "04": {
        "budget": ("3", "0 / 0 words", "0 / 0 words", "1 / ~8-12 hours", "4", "~0 unless wife/knife inserts are approved; no outline target recorded"),
        "fixes": [
            "CH05 L31 — if wife Option B is approved, remove the wife reference there instead of adding a wife to CH04.",
            "CH05 L131–135 — if temple-dialogue Option B is approved, relax CH05's framing instead of adding dialogue to CH04.",
            "avatar-profile.json L9 — if age Option B is approved, change age to 34 and adjust implied merchant career.",
        ],
        "decisions": [
            ("CH4#1", "Chandra's profile says age 45-50, while CH04 states thirty-four years six times.", "Approve Option A: update CH04 to a late-forties age because it preserves the existing profile logic and avoids profile/backstory surgery."),
            ("CH4#2", "CH05 gives Chandra a wife, while CH04 depicts him as solitary.", "Approve Option B: cut the wife from CH05 because it is the least invasive continuity fix and avoids retrofitting CH04 domestic scaffolding."),
            ("CH4#3", "CH05 stages the fifteen-years exchange as spoken temple-passage dialogue, while CH04 has those lines elsewhere/interiorly.", "Approve Option A: add the exchange to CH04's ambush because CH05's Lilith-side scene depends on that literal memory beat."),
            ("CH4#9", "The katar term is defensible but not airtight for Mauryan India.", "Approve leaving the existing two katar mentions because the term is plausible and the chapter already confines it to the opening attack."),
        ],
        "ops": {1: "DECIDE", 2: "DECIDE", 3: "DECIDE", 4: "REPLACE", 5: "REPLACE", 6: "REWRITE", 7: "REPLACE", 8: "DECIDE", 9: "DECIDE"},
        "interacts": {1: "CH4#6", 2: "CH5 L31", 3: "CH5 L131-135", 4: "CH4#5, CH4#6", 5: "CH4#4, CH4#6", 8: "CH5 L131"},
    },
    "06": {
        "budget": ("2", "0 / 0 words", "2 / +300-450 words", "2 / ~2-4 hours", "3", "+100 to +300; hard target <=10,000 words unless author approves overage"),
        "fixes": [
            "CH07 L127 and L137 — if CH06 is not rewritten to match the three-day gap, CH07 must be changed to the same-day version.",
            "CH07 L113 — preserve the ash-taste cue; CH06 should add only a physical morning-after echo, not dream exposition.",
        ],
        "decisions": [
            ("CH6#1", "CH06 makes Alexios and the slave woman same-day events, while CH07 puts three days between them.", "Approve rewriting CH06 to match CH07 because CH07's three-day pause carries stronger fatalistic architecture and avoids weakening Lilith's retrospective sequence."),
            ("CH6#7", "The outline asks for one magistrate confrontation while CH06 currently has two.", "Approve keeping both visits but sharpening their distinct functions because it preserves escalation without cutting useful pressure beats."),
            ("CH6#8", "The outline specifies nine tragic labels, while the manuscript draft uses unlabeled section breaks.", "Approve leaving breaks unlabeled unless the full manuscript adopts visible architecture labels, because local labels would create a one-chapter formatting exception."),
        ],
        "ops": {1: "DECIDE", 2: "REPLACE", 3: "REPLACE", 4: "INSERT", 5: "INSERT", 6: "INSERT", 7: "DECIDE", 8: "DECIDE"},
        "interacts": {1: "CH6#6, CH7 L127-L137", 4: "CH6#6", 5: "CH6#8", 6: "CH6#1, CH6#4"},
    },
    "08": {
        "budget": ("1", "2 / -150 to -350 words", "1 / +120-220 words", "2 / ~2-4 hours", "4", "-100 to -250; no outline hard target recorded"),
        "fixes": [
            "avatar-profile.json L32 — if pride Option B is approved, update profile to accept pride-as-residue as the karmic bridge.",
            "period-rules.md L126–127 — if compressed virtue line remains canonical, update the rule or add both formulations to CH08.",
            "avatar-profile.json L40 — if Marcia remains silent, update profile to describe silent proximity instead of partial truths.",
            "CH09 tracking notes — correct the portico anchor to CH08 L381–407 if internal tracking docs are maintained.",
        ],
        "decisions": [
            ("CH8#1", "CH08 ends on pride-as-residue, while the profile and Heian bridge call for softening toward vulnerability to beauty/desire.", "Approve Option A: trim the pride thread and add sensory tenderness because it protects the CH12 desire/beauty bridge with minimal downstream rewrites."),
            ("CH8#2", "period-rules mandate the two-clause virtue articulation, while the outline and draft use the compressed line.", "Approve Option C: keep the compressed line and add the two-clause formulation earlier, preserving both source documents without breaking rhythm."),
            ("CH8#3", "The profile says Marcia offers partial truths, while the outline/draft use a silent cameo.", "Approve Option A: keep silent cameo and update the profile because CH09 already depends on restrained proximity, not an active exchange."),
            ("CH8#6", "The profile calls the scribal error the inciting fracture, while the draft uses it after other contradictions.", "Approve reframing the error as the breakpoint in Verinus's first reconstruction, preserving scene order and restoring structural weight."),
        ],
        "ops": {1: "DECIDE", 2: "DECIDE", 3: "DECIDE", 4: "INSERT", 5: "TRIM", 6: "DECIDE", 7: "VERIFY"},
        "interacts": {1: "CH8#5, CH12 bridge", 2: "CH8#1", 3: "CH9 L241", 4: "CH8#1", 5: "CH8#1"},
    },
    "10": {
        "budget": ("2", "2 / -4,300+ words", "1 / +40-80 words", "1 / ~4-6 hours", "2", "-4,300 minimum; hard target <=9,700 words"),
        "fixes": [
            "chapter-outline.md L63 — if Paphnutius remains named, update the outline to permit the name.",
            "CH11 L315–317 — if Theodora's departure wording is changed, preserve ambiguity compatible with Lilith-side dematerialization.",
        ],
        "decisions": [
            ("CH10#5", "The outline says the young monk is unnamed, while CH10 names him Paphnutius.", "Approve keeping the name and updating the outline because the named relationship gives the later withdrawal beat stronger emotional specificity."),
            ("CH10#8", "CH10's Theodora departure and CH11's Lilith-side disappearance use different ontological registers.", "Approve no draft change unless a line edit makes CH10 too physically explicit; current ambiguity is sufficient."),
        ],
        "ops": {1: "TRIM", 2: "REPLACE", 3: "REPLACE", 4: "REWRITE", 5: "DECIDE", 6: "INSERT", 7: "TRIM", 8: "VERIFY"},
        "interacts": {1: "CH10#2, CH10#3, CH10#7", 2: "CH10#1", 3: "CH10#1", 4: "CH10#1", 5: "CH10 outline L63", 7: "CH10#1"},
    },
    "12": {
        "budget": ("0", "0 / 0 words", "4 / +500-800 words", "2 / ~1-2 hours", "2", "+500 to +800; current 8,809, scene targets require expansion"),
        "fixes": [
            "CH13 — ensure the Heian-to-Inquisition bridge remains imagistic after CH12 L560 is rewritten.",
            "CH12_outline.md L6 and period-rules.md L11/L29 — reconcile date window if date Option B is approved.",
        ],
        "decisions": [
            ("CH12#6", "Three fever-pressure phrases may read modern but are defensible in context.", "Approve replacing all three with period-register alternatives because they are low-cost and reduce tonal risk."),
            ("CH12#7", "CH12 outline says c. 1000 CE, while period-rules place the chapter circa 1100 CE / 1050-1150 CE.", "Approve the later 1050-1150 window because it better fits the late-Heian death-of-court-culture atmosphere."),
        ],
        "ops": {1: "INSERT", 2: "INSERT", 3: "REWRITE", 4: "REWRITE", 5: "INSERT", 6: "DECIDE", 7: "DECIDE", 8: "INSERT"},
        "interacts": {1: "CH12#2, CH12#8", 2: "CH12#1", 3: "CH13 L53/L183", 4: "CH13 bridge", 5: "CH12#3", 8: "CH12#1, CH12#5"},
    },
    "14": {
        "budget": ("2", "2 / -4,700+ words", "3 / +250-450 words", "1 / ~1-2 hours", "2", "-4,250 minimum; hard target <=14,000 words"),
        "fixes": [
            "CH13 L251 and L265 — update avatar name to Diego de Lucena, converso physician, late-fifteenth-century Iberia / 1491.",
            "period-rules.md L114–118 — if Sor Catalina's current direct address is allowed, document the narrow ruling for CH15+.",
            "period-rules.md L59–61 in CH18 — if a personalized enemy apology is retained there, document the exception separately.",
        ],
        "decisions": [
            ("CH14#5", "Sor Catalina speaks directly to Diego, which may violate the no-direct-interaction rule.", "Approve Option C: remove the most tracking-like address while preserving the near-contact beat, because it protects the rule without gutting CH15's memory echo."),
            ("CH14#7", "CH14 is far over length and Scenes 6-7 repeat the hatred-release logic.", "Approve a hard <=14,000-word cut; any longer target should be explicitly approved before line work begins."),
        ],
        "ops": {1: "REPLACE", 2: "TRIM", 3: "INSERT", 4: "INSERT", 5: "DECIDE", 6: "REPLACE", 7: "TRIM", 8: "INSERT", 9: "INSERT"},
        "interacts": {1: "CH13 L251/L265", 2: "CH14#7", 3: "CH14#4", 4: "CH14#3", 5: "CH15 L141/L245/L353", 7: "CH14#2, CH14#8"},
    },
    "16": {
        "budget": ("4", "4 / -5,400+ words", "1 / +60-100 words", "1 / ~2-3 hours", "1", "-5,400 minimum; hard target <=9,000 words"),
        "fixes": [
            "CH17 retrospective — after Isabeau is inserted, CH17's reference to a co-located past life has a concrete CH16 referent.",
            "CH17 line echoes — preserve CH16 L377/L433-L439/L659/L878 unless CH17 is revised simultaneously.",
        ],
        "decisions": [
            ("CH16#4", "CH16 is 14,413 words against an outline target of ~8,000-9,000.", "Approve a hard <=9,000-word target because the outline gives a numeric cap; any longer target should be logged before cutting starts."),
        ],
        "ops": {1: "INSERT", 2: "REPLACE", 3: "TRIM", 4: "TRIM", 5: "TRIM", 6: "REPLACE", 7: "REPLACE", 8: "REPLACE", 9: "REPLACE", 10: "REWRITE", 11: "TRIM", 12: "VERIFY", 13: "VERIFY"},
        "interacts": {1: "CH17 retrospective", 2: "CH16#3", 3: "CH16#2", 4: "CH16#10, CH16#11", 5: "CH16#4", 10: "CH16#4", 11: "CH16#4", 12: "CH16#4", 13: "CH16#11"},
    },
    "18": {
        "budget": ("1", "1 / -80-160 words", "3 / +450-650 words", "0 / 0 hours", "4", "+300 to +500; current 8,720, no reduction target pressure"),
        "fixes": [
            "CH19 L79/L109 — if ledger recalculation Option B is chosen, soften CH19's recalculation language to 'understood'.",
            "period-rules.md L59–61 — if the Qing sergeant apology is retained, document the exception to the no-personalized-enemy rule.",
        ],
        "decisions": [
            ("CH18#2", "The profile opens Wei's ledger at 47/23, while CH18 currently records 48/23 after Liu.", "Approve updating the profile to clarify 47+Liu=48 because the draft's arithmetic beat is already coherent across L47 and L73."),
            ("CH18#7", "Young Ping disappears during the riot and is never accounted for.", "Approve a one-sentence abandoned-sandals confirmation because it preserves attrition without adding a subplot."),
            ("CH18#8", "CH19 implies a ledger recalculation after village-deaths news, while CH18 leaves the recalculation implicit.", "Approve adding the CH18 subtraction beat because it keeps the numerical handoff inside Wei's experience and avoids changing CH19's Lilith-side arithmetic."),
            ("CH18#13", "The Qing sergeant's 'I'm sorry' humanizes an enemy soldier despite the no-personalized-enemy rule.", "Approve Option C: replace with a silent pause/gesture, preserving human weight without violating the rule as brightly."),
        ],
        "ops": {1: "INSERT", 2: "DECIDE", 3: "TRIM", 4: "INSERT", 5: "INSERT", 6: "REPLACE", 7: "DECIDE", 8: "DECIDE", 9: "VERIFY", 10: "VERIFY", 11: "VERIFY", 12: "VERIFY", 13: "DECIDE"},
        "interacts": {1: "CH18#2", 2: "CH18#1, CH19 L57/L77/L109", 3: "CH19 reveal", 4: "CH18#8", 7: "CH18#4", 8: "CH19 L79/L109", 13: "CH18 period-rules L59-L61"},
    },
    "20": {
        "budget": ("5", "1 / -2,800+ words", "4 / +450-750 words", "4 / ~5-7 hours", "1", "-2,200 minimum; hard target <=11,000 words"),
        "fixes": [
            "CH21 opening — CH20 coda must include Lilith's realization that all ten perfections have completed.",
            "CH19 L685/L637/L639 — if CH20 does not add tracking cues, soften 'tracking' to 'watching/observing'.",
            "CH01 L161 — preserve the passerby/Roadmaster flashback anchor while revising CH20.",
        ],
        "decisions": [
            ("CH20#16", "CH19 says Lilith needs data from Malone's tracking, while CH20 shows only observational sightings.", "Approve Option B: retune CH19's wording to watching/observing because CH20 already needs less Lilith visibility, not more."),
        ],
        "ops": {1: "REWRITE", 2: "REWRITE", 3: "REWRITE", 4: "REPLACE", 5: "REPLACE", 6: "INSERT", 7: "REPLACE", 8: "INSERT", 9: "INSERT", 10: "REPLACE", 11: "TRIM", 12: "INSERT", 13: "REWRITE", 14: "VERIFY", 15: "INSERT", 16: "DECIDE"},
        "interacts": {1: "CH20#13", 2: "CH20#13", 3: "CH20#11", 4: "CH20#3, CH20#11", 5: "CH20#6", 6: "CH21 opening", 8: "CH20#11", 10: "CH20#11", 11: "CH20#3, CH20#8", 13: "CH20#1, CH20#2", 14: "CH01 L161", 16: "CH20#1"},
    },
}


RESOLVED_REASONS = {
    ("16", 12): "Past-life bleed-through cues at CH16 L53 and L521 are present and restrained; preserve during cuts.",
    ("16", 13): "CH17 dialogue anchors are present at CH16 L377, L433-L439, L659, and L878; preserve verbatim.",
    ("18", 9): "Jean's name appears at CH18 L657 as the intended karmic thread; preserve.",
    ("18", 10): "Old Huang functions as quiet mirror throughout CH18; preserve his restraint.",
    ("18", 11): "Manna/Elder Zhou theology-collapse beat at CH18 L373 is present and clean; preserve.",
    ("18", 12): "Wounded-child breakthrough at CH18 L559 matches CH19 L245; preserve near-verbatim.",
    ("20", 14): "CH01 L161 matches CH20 L839/L935 Roadmaster passerby flashback; preserve both anchors.",
}


DECISIONS_GATE = """## Decisions Gate
Work this list top-down before touching chapter prose. Each item links to the affected chapter section and repeats there as a **DECISION REQUIRED** block.

1. [CH8#1 pride ending](#chapter-8-rome--verinus) — highest downstream impact; determines whether the Heian bridge is softening/desire or pride-as-residue.
2. [CH14#1 / CH13 name-profession-century fix](#chapter-14-inquisition--diego-de-lucena) — required before CH14/CH15 continuity work; CH13 must say Diego de Lucena, converso physician, 1491/late-fifteenth-century Iberia.
3. [CH6#1 / CH7 timeline](#chapter-6-athens--philon) — cross-chapter chronology blocker for Alexios and the eastern-gate woman.
4. [CH14#5 Sor Catalina rule ruling](#chapter-14-inquisition--diego-de-lucena) — sets the no-direct-interaction precedent for CH15+.
5. [CH18#8 / CH19 ledger recalculation](#chapter-18-taiping-rebel--wei-shufen-nanjing--tianjing-1864) — affects numerical handoff and Lilith-side arithmetic.
6. [CH20#16 / CH19 tracking language](#chapter-20-noir-detective--jack-malone-los-angeles-1938) — choose whether CH20 adds cues or CH19 softens "tracking."
7. [CH4#2 wife continuity](#chapter-4-mauryan--chandra) — choose CH04 insertion or CH05 cut.
8. [CH4#3 temple-passage dialogue](#chapter-4-mauryan--chandra) — choose CH04 literal exchange or CH05 retrospective compression.
9. [CH4#1 age mismatch](#chapter-4-mauryan--chandra) — choose draft age update or profile update.
10. [CH8#2 virtue articulation](#chapter-8-rome--verinus) — reconcile period-rules and outline.
11. [CH8#3 Marcia cameo](#chapter-8-rome--verinus) — choose silent cameo/profile update or brief spoken exchange.
12. [CH10#5 Paphnutius named monk](#chapter-10-egypt--macarius-the-hermit) — choose named draft or unnamed outline.
13. [CH12#7 Heian date window](#chapter-12-heian--kaoru) — reconcile c. 1000 with 1050-1150/c. 1100.
14. [CH18#2 opening ledger 47/23 vs 48/23](#chapter-18-taiping-rebel--wei-shufen-nanjing--tianjing-1864) — choose draft/profile arithmetic.
15. [CH18#13 enemy apology](#chapter-18-taiping-rebel--wei-shufen-nanjing--tianjing-1864) — choose rule purity, exception, or silent gesture.

---

"""


EXECUTION_ORDER = """## Execution Order

### Stage 1 — Decisions
Resolve every item in **Decisions Gate** before chapter work begins. Mark each chapter-local `[ ] Approved` or `[ ] Override with: _____` checkbox, then update any affected source documents listed in that chapter's **Fixes Required in Other Chapters** block.

### Stage 2 — Global REPLACE Sweep

| Search | Replace with | Chapters affected | Item refs | Verification command |
|---|---|---|---|---|
| `emperor` | Context-dependent Ashoka/Devanampiya/throne phrasing | CH04 | CH4#4 | `rg -n -i \"emperor\" incarnations/ch04-mauryan-chandra/CH04_draft.md` expected zero |
| Dialogue contractions (`'re`, `'ve`, `'ll`, `n't`, etc.) | Expanded forms | CH04 | CH4#5 | `rg -n \"'re|'ve|'ll|n't|'s|'d\" incarnations/ch04-mauryan-chandra/CH04_draft.md` inspect dialogue hits |
| `particularite` | Fine red silt / peculiar grit phrasing | CH04 | CH4#7 | `rg -n \"particularite\" incarnations/ch04-mauryan-chandra/CH04_draft.md` expected zero |
| `forty years` | `thirty-ninth year` / `nearly forty years` | CH06 | CH6#2 | `rg -n \"forty years\" incarnations/ch06-athens-philosopher/CH06_draft.md` expected zero |
| `perhaps thirty years old` | `perhaps twenty years old` | CH06 | CH6#3 | `rg -n \"thirty years\" incarnations/ch06-athens-philosopher/CH06_draft.md` expected zero for Scythian woman |
| `kenosis` | English paraphrase except permitted dialogue | CH10 | CH10#2 | `rg -n \"kenosis\" incarnations/ch10-egypt-hermit/CH10_draft.md` expected zero narration hits |
| `theosis` | English paraphrase except L337 dialogue | CH10 | CH10#2 | `rg -n \"theosis\" incarnations/ch10-egypt-hermit/CH10_draft.md` expected only dialogue if retained |
| `self-image` / `self-filling` / psychological `structure` | Concrete desert imagery | CH10 | CH10#3 | `rg -n \"self-image|self-filling|\\bstructure\\b\" incarnations/ch10-egypt-hermit/CH10_draft.md` expected <=1 `structure`, zero others |
| `momentum` | Period-neutral weight/course phrasing | CH14, CH20 coda if retained | CH14#6, CH20#6 | `rg -n \"momentum\" incarnations/ch14-inquisition-accused/CH14_draft.md incarnations/ch20-noir-detective/CH20_draft.md` expected zero or approved coda alternative |
| `epistemolog` | Pyrrhonist/scholastic phrasing | CH16 | CH16#6 | `rg -n \"epistemolog\" incarnations/ch16-renaissance-skeptic/CH16_draft.md` expected zero |
| rhetorical `narrative` | account/story/version/report | CH16 | CH16#7 | `rg -n \"narrative\" incarnations/ch16-renaissance-skeptic/CH16_draft.md` expected zero rhetorical hits |
| rhetorical `performance` | display/pretense/show | CH16 | CH16#8 | `rg -n \"performance\" incarnations/ch16-renaissance-skeptic/CH16_draft.md` expected zero rhetorical hits |
| `professional armor` | guard of his profession | CH16 | CH16#9 | `rg -n \"professional armor\" incarnations/ch16-renaissance-skeptic/CH16_draft.md` expected zero |
| `fifty hours` | `seventy-two hours` if keeping third-day dawn | CH18 | CH18#6 | `rg -n \"fifty hours|seventy-two hours|third day\" incarnations/ch18-taiping-rebel/CH18_draft.md` numbers must agree |
| `never been to France` | wrong-France bleed-through | CH20 | CH20#2 | `rg -n \"never been to France|Belleau|Meuse\" incarnations/ch20-noir-detective/CH20_draft.md` no contradiction |
| `Howard Brennan` | Howard Brannigan/Brenner | CH20 | CH20#4 | `rg -n \"Brennan|Brannigan|Brenner\" incarnations/ch20-noir-detective/CH20_draft.md` Brennan should mean David only |
| `three-year-old Roadmaster` | `two-year-old Roadmaster` | CH20 | CH20#7 | `rg -n \"three-year-old Roadmaster|two-year-old Roadmaster\" incarnations/ch20-noir-detective/CH20_draft.md` |

### Stage 3 — Authorial-Note Strip
Run CH14#2 before any CH14 prose compression: delete all scene metadata blocks. Verify with `rg -n \"Word count:|Sensory anchors:|Recognition marker:|Hatred seed:\" incarnations/ch14-inquisition-accused/CH14_draft.md` expected zero.

### Stage 4 — INSERTs
Anchor lines may drift after Stage 2. Re-find each anchor by quoted text before inserting.

| Item | Anchor | Estimate |
|---|---|---|
| CH06#4 | CH06 L23 patient montage / L31 tanner hesitation | +80-120 words |
| CH06#5 | CH06 opening before first prose line | +3-6 words |
| CH06#6 | CH06 morning scene before L31 | +25-50 words |
| CH08#4 | CH08 death sequence after Verinus's final lonely thought | +100-180 words |
| CH10#6 | CH10 after Didymus warning at L201 | +40-80 words |
| CH12#1 | CH12 Scene I opening, before Pavilion visit | +80-140 words |
| CH12#2 | CH12 Scene I cup/fan rim beat | +30-60 words |
| CH12#5 | CH12 Scene III garden corridor | +90-150 words |
| CH12#8 | CH12 Scene I and Scene V expansion anchors | +300-450 words |
| CH14#3 | CH14 Scene 1 opening mortar/cloves beat | +40-80 words |
| CH14#4 | CH14 Scene 1 finger-sequence ritual | +70-110 words |
| CH14#8 | CH14 Scene 5 or 6 Arabic medicine beat | +25-50 words |
| CH14#9 | CH14 early social-detail beat | +20-40 words |
| CH16#1 | CH16 after L519 refreshment-table movement | +60-100 words |
| CH18#1 | CH18 opening paragraph | +140-190 words |
| CH18#4 | Before CH18 L181 raid aftermath | +250-400 words |
| CH18#5 | Near CH18 L429 mother's voice | +25-45 words |
| CH20#6 | CH20 coda before "somewhere else" | +60-110 words |
| CH20#8 | CH20 flood section after L629 | +150-250 words |
| CH20#9 | CH20 middle solo/meals beat | +80-120 words |
| CH20#12 | CH20 home/flood solo scene | +20-50 words |
| CH20#15 | CH20 SRO morning/home beat | +15-35 words |

### Stage 5 — TRIMs and REWRITEs
Sort largest operations first. Hard word targets are enforced here.

| Chapter | Items | Operation | Estimated delta / effort |
|---|---|---|---|
| CH10 | CH10#1, CH10#7 | TRIM Scenes VIII-IX | -4,300+ words; target <=9,700 |
| CH16 | CH16#4, #10, #11, #3, #5 | TRIM/REWRITE Scenes 4, 7, 8, coda, gestures | -5,400+ words; target <=9,000 |
| CH20 | CH20#11, #3, #1, #13, #2 | TRIM/REWRITE blackmail middle and Lilith sightings | -2,800+ words; target <=11,000 |
| CH14 | CH14#7, #2 | TRIM metadata and Scenes 6-7 | -4,700+ words; target <=14,000 |
| CH04 | CH4#6 | REWRITE POV from L311 onward | ~8-12 hours |
| CH12 | CH12#3, #4 | REWRITE Attendant rupture and karmic bridge | ~1-2 hours |
| CH08 | CH8#5 plus CH8#1 if approved | TRIM pride/repetition | -150 to -350 words |
| CH18 | CH18#3 | TRIM omniscient Lilith leaks | -80 to -160 words |

### Stage 6 — Continuity Verification
After Stage 5, rerun chapter-pair checks:

- CH04/CH05: `rg -n \"wife|Fifteen years counts|It has always meant nothing|ceremonial knife\" incarnations/ch04-mauryan-chandra/CH04_draft.md incarnations/ch05-lilith-cp02/CH05_draft.md`
- CH06/CH07: `rg -n \"Alexios left|three days after|eastern gate|taste of ash\" incarnations/ch06-athens-philosopher/CH06_draft.md incarnations/ch07-lilith-cp03/CH07_draft.md`
- CH08/CH09: `rg -n \"Virtue lives|compassion within uncertainty|Marcia|stylus|Brundisium|cook\" incarnations/ch08-rome-investigator/CH08_draft.md incarnations/ch09-lilith-cp04/CH09_draft.md`
- CH10/CH11: `rg -n \"Theodora|flicker|pendulum|fingers closed on nothing\" incarnations/ch10-egypt-hermit/CH10_draft.md incarnations/ch11-lilith-cp05/CH11_draft.md`
- CH12/CH13: `rg -n \"incense|To endure what is real|Diego de Lucena|de la Cruz|priest|sixteenth\" incarnations/ch12-heian-lover/CH12_draft.md incarnations/ch13-lilith-cp06/CH13_draft.md`
- CH14/CH15: `rg -n \"Diego de Lucena|Sor Catalina|Physician|carry your bag|looked at the woman in grey\" incarnations/ch14-inquisition-accused/CH14_draft.md incarnations/ch15-lilith-cp07/CH15_draft.md`
- CH16/CH17: `rg -n \"Nearly missed|You offer me a fortress|truth about what I didn't know|widow's peak|Isabeau\" incarnations/ch16-renaissance-skeptic/CH16_draft.md incarnations/ch17-lilith-cp08/CH17_draft.md`
- CH18/CH19: `rg -n \"133 saved|128 lost|91 saved|171 lost|recalculated|understood|It doesn't matter if I'm cursed|I will try again\" incarnations/ch18-taiping-rebel/CH18_draft.md incarnations/ch19-lilith-cp09/CH19_draft.md`
- CH20/CH21/CH01: `rg -n \"passerby|rushing to avoid|Roadmaster|all ten|NOW|Someone has to give a damn\" incarnations/ch20-noir-detective/CH20_draft.md incarnations/ch21-lilith-cp10/CH21_draft.md incarnations/ch01-contemporary-manchester/CH01_draft.md`

---

"""


VERIFICATION_LOG = f"""## Verification Pass Log
**Date:** 2026-04-23

**Summary:** Verified 91 numbered action items and the continuity/positive-check anchors for chapters 4, 6, 8, 10, 12, 14, 16, 18, and 20 against current drafts and source documents. Corrected 24 stale or imprecise line/count claims, moved 16 resolved/protective items into per-chapter **Verified — Do Not Touch** appendices, surfaced 5 additional execution-gate decisions from soft targets or cross-chapter options, and found no source-document conflict that could not be converted into a DECIDE item.

- Current verified word counts: CH04 {WORD_COUNTS['CH04']}; CH06 {WORD_COUNTS['CH06']}; CH08 {WORD_COUNTS['CH08']}; CH10 {WORD_COUNTS['CH10']}; CH12 {WORD_COUNTS['CH12']}; CH14 {WORD_COUNTS['CH14']}; CH16 {WORD_COUNTS['CH16']}; CH18 {WORD_COUNTS['CH18']}; CH20 {WORD_COUNTS['CH20']}.
- CH04: verified six `thirty-four` hits at L43, L445, L593, L837, L1009, L1025; CH04 still has zero `wife` hits; CH05 wife anchor remains at L31.
- CH04: `emperor` count is 23, not the stale 24-line list in the guide; removed stale L121 from the line list.
- CH04: contraction audit found 25 contraction hits, not only the nine listed dialogue violations; item now requires a full dialogue pass after the nine guaranteed fixes.
- CH06/CH07: timeline conflict remains current: CH06 L299/L301/L361/L365 vs CH07 L127/L137.
- CH08: pride, virtue-articulation, Marcia, death-discovery, and repetition anchors remain current; profile/rules/outline conflict remains a live DECIDE cluster.
- CH10: Greek terminology, modern psychological vocabulary, Theodora over-reading, Paphnutius naming, and word-count overrun remain current; hard target set to <=9,700 words per outline.
- CH12: incense/translucent baseline omissions remain current; rupture explanation at L365 and explicit heresy/torture bridge at L560 remain current; date conflict remains live.
- CH14: CH13 still misnames Diego at L251/L265; CH14 still contains metadata blocks at L93-L100, L196-L204, L304-L312, L410-L418, L544-L553, L687-L698, L806-L815, L931-L943, L1065-L1079; CH14 word count corrected to 18,733.
- CH16: Isabeau remains absent; coda contradiction remains at L946; word count corrected to 14,413; hard target set to <=9,000 words per outline.
- CH18: opening anchor gaps, 48/23 ledger, Lilith POV leaks, fifty-hour arithmetic, Young Ping disappearance, and CH19 numerical handoff remain current.
- CH20: Lilith-face over-specification, France contradiction, Gloria femme-fatale coding, Brennan collision, Combination theorizing, CH21 coda gap, and Roadmaster age issue remain current; word count corrected to 13,800.

**Placeholder Prose Note:** All placeholder prose is structural scaffolding only. Do not commit verbatim.

---

"""


def normalize_lines(text: str) -> str:
    text = re.sub(r"\blines? (\d+)", r"L\1", text, flags=re.IGNORECASE)
    text = re.sub(r"\bLine (\d+)", r"L\1", text)
    text = re.sub(r"\bline (\d+)", r"L\1", text)
    text = text.replace("Lines 1, 3, 11, 15, 19, 21, 31, 61, 119, 121, 147, 149, 157, 193, 207, 277, 317, 323, 417, 433, 491, 791, 957, 1019", "L1, L3, L11, L15, L19, L21, L31, L61, L119, L147, L149, L157, L193, L207, L277, L317, L323, L417, L433, L491, L791, L957, L1019")
    text = text.replace("draft uses it 23 times.", "draft uses it 23 times.")
    text = text.replace("nine flagged instances are all still present.", "the nine originally flagged dialogue instances are still present; full grep now shows 25 contraction hits to inspect.")
    text = text.replace("14,040", "14,039")
    text = text.replace("18,748", "18,733")
    text = text.replace("14,471", "14,413")
    text = text.replace("13,833", "13,800")
    text = text.replace("8,734", "8,720")
    text = text.replace("10,447", "10,436")
    text = text.replace("≤ 10,500 (flexibility on the 9,700 budget acceptable; 14,040 is not)", "≤ 9,700")
    text = text.replace("≤ 11,000. Scenes 4 and 7", "≤ 9,000. Scenes 4 and 7")
    text = text.replace("Target a 2,500–3,500-word cut to reach ~11,000 words (still over, but survivable).", "Cut at least 5,400 words to reach the hard outline target of ≤ 9,000 words.")
    return text


def mark_placeholder_prose(text: str) -> str:
    out = []
    for line in text.splitlines():
        if re.match(r"\s*>", line) and "[PLACEHOLDER PROSE" not in line:
            line = re.sub(r"^(\s*>\s*)", r"\1[PLACEHOLDER PROSE — REWRITE IN VOICE] ", line)
        out.append(line)
    return "\n".join(out) + "\n"


def split_chapters(text: str) -> tuple[str, list[tuple[str, str]]]:
    first = re.search(r"^## Chapter ", text, re.M)
    if not first:
        return text, []
    intro = text[: first.start()]
    rest = text[first.start():]
    parts = re.split(r"(?=^## Chapter )", rest, flags=re.M)
    chapters = []
    for part in parts:
        if not part.strip():
            continue
        m = re.match(r"## Chapter (\d+):", part)
        if m:
            chapters.append((m.group(1).zfill(2), part))
    return intro, chapters


def remove_resolved_item_blocks(chap_no: str, body: str) -> tuple[str, list[str]]:
    lines = body.splitlines()
    kept: list[str] = []
    appendix: list[str] = []
    i = 0
    while i < len(lines):
        if re.match(r"\*\*\d+\.", lines[i]):
            start = i
            i += 1
            while i < len(lines) and not re.match(r"\*\*\d+\.", lines[i]) and not re.match(r"### ", lines[i]) and not re.match(r"## Chapter ", lines[i]):
                i += 1
            block = lines[start:i]
            header = block[0]
            num = int(re.match(r"\*\*(\d+)\.", header).group(1))
            if "[RESOLVED" in "\n".join(block) or "[ALREADY RESOLVED" in "\n".join(block) or (chap_no, num) in RESOLVED_REASONS:
                reason = RESOLVED_REASONS.get((chap_no, num), "Verified current draft already satisfies this item; preserve the anchor during line work.")
                appendix.append(f"{header}\n- **Reason to preserve:** {reason}\n" + "\n".join(block[1:]))
            else:
                kept.extend(block)
            continue
        kept.append(lines[i])
        i += 1
    return "\n".join(kept) + "\n", appendix


def move_positive_checks(body: str) -> tuple[str, list[str]]:
    appendix: list[str] = []
    patterns = [
        r"### Positive checks \(confirm still present — do not remove\)",
        r"### Positive checks \(confirm still present\)",
        r"### Positive checks \(confirm still present — do not remove\)",
    ]
    for pat in patterns:
        m = re.search(pat, body)
        if not m:
            continue
        start = m.start()
        next_m = re.search(r"\n### ", body[start + 1 :])
        end = start + 1 + next_m.start() if next_m else len(body)
        appendix.append(body[start:end].strip())
        body = body[:start] + body[end:]
        break
    return body, appendix


def add_ops(chap_no: str, body: str) -> str:
    ops = CONFIG[chap_no]["ops"]
    interacts = CONFIG[chap_no]["interacts"]
    out: list[str] = []
    for line in body.splitlines():
        out.append(line)
        m = re.match(r"\*\*(\d+)\.", line)
        if m:
            num = int(m.group(1))
            op = ops.get(num, "VERIFY")
            out.append(f"- **Operation:** {op}")
            out.append(f"- **Interacts with:** {interacts.get(num, 'None')}")
    return "\n".join(out) + "\n"


def preamble(chap_no: str) -> str:
    cfg = CONFIG[chap_no]
    replace, trim, insert, rewrite, decide, delta = cfg["budget"]
    fixes = "\n".join(f"- {x}" for x in cfg["fixes"]) or "- None."
    decisions = []
    for ref, conflict, rec in cfg["decisions"]:
        decisions.append(
            f"**DECISION REQUIRED — {ref}**\n"
            f"- **Conflict:** {conflict}\n"
            f"- **Recommendation:** {rec}\n"
            f"- [ ] Approved\n"
            f"- [ ] Override with: _____"
        )
    decision_text = "\n\n".join(decisions) if decisions else "None."
    return (
        "\n### Fixes Required in Other Chapters\n"
        f"{fixes}\n\n"
        "### Operation Budget\n"
        "| Operation | Budget |\n|---|---|\n"
        f"| REPLACE items | {replace} |\n"
        f"| TRIM items with total estimated word delta | {trim} |\n"
        f"| INSERT items with total estimated word delta | {insert} |\n"
        f"| REWRITE items with estimated work hours | {rewrite} |\n"
        f"| DECIDE items still open | {decide} |\n"
        f"| Net estimated word delta / target comparison | {delta} |\n\n"
        "### DECISION REQUIRED\n"
        f"{decision_text}\n"
    )


def add_appendix(body: str, appendix_blocks: list[str]) -> str:
    body = body.rstrip()
    if appendix_blocks:
        appendix = "\n\n".join(appendix_blocks)
    else:
        appendix = "- No resolved items moved during this verification pass."
    return body + "\n\n### Verified — Do Not Touch\n" + appendix + "\n"


def transform_chapter(chap_no: str, chapter: str) -> str:
    lines = chapter.splitlines()
    header = lines[0]
    body = "\n".join(lines[1:]) + "\n"
    body, item_appendix = remove_resolved_item_blocks(chap_no, body)
    body, positive_appendix = move_positive_checks(body)
    body = add_ops(chap_no, body)
    return header + "\n" + preamble(chap_no) + body + "\n" + add_appendix("", item_appendix + positive_appendix)


def main() -> None:
    text = GUIDE.read_text(encoding="utf-8")
    text = normalize_lines(text)
    text = mark_placeholder_prose(text)
    completion = ""
    m = re.search(r"\n## Completion Summary[\s\S]*$", text)
    if m:
        completion = m.group(0)
        text = text[: m.start()]
    intro, chapters = split_chapters(text)
    new_intro = "# Chapter-by-Chapter Revision Guide\n"
    new_intro += "Generated from `minor_revisions.md` findings and restructured into an execution-ready line-level plan. Status tags now distinguish live work from verified anchors; line references use `L<number>` format.\n\n"
    new_intro += VERIFICATION_LOG + DECISIONS_GATE + EXECUTION_ORDER
    transformed = [transform_chapter(chap_no, chap) for chap_no, chap in chapters]
    GUIDE.write_text(new_intro + "\n---\n\n" + "\n---\n\n".join(transformed) + completion, encoding="utf-8")


if __name__ == "__main__":
    main()
