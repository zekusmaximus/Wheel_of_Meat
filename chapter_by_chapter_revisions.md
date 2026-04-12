# Chapter-by-Chapter Revision Guide
Generated from minor_revisions.md findings. Each chapter's section covers every actionable item flagged in the review, verified against the current draft, avatar-profile.json, period-rules.md, the chapter outline, and the adjacent Lilith chapters. Status tags: **STILL BROKEN** = problem confirmed in current draft; **RESOLVED** = already fixed; **PARTIAL** = partially fixed; **AUTHOR DECISION** = source documents conflict, author must choose.

---

## Chapter 4: Mauryan — Chandra

### Critical Fixes (must resolve before locking)

**1. Age mismatch — profile vs. draft (AUTHOR DECISION)**
- **Problem:** avatar-profile.json says `"age_at_chapter_events": "45-50"` but the draft states "thirty-four years" six times.
- **Source requirement:** `incarnations/ch04-mauryan-chandra/avatar-profile.json` line 9 ("45–50"); draft CH04_draft.md lines 43, 445, 593, 837, 1009, 1025 ("thirty-four years").
- **Current text:** Line 43: "my thirty-four years." Line 837: "through thirty-four years of careful living." Line 1009 repeats the same. Line 1025: "a thought that did not fit the patterns he had spent thirty-four years constructing."
- **Revision instruction:** **AUTHOR DECISION.** Option A — Update the draft: replace every "thirty-four" with an age in the 45–50 range (e.g. "forty-seven"). The profile's logic (ex-merchant of 12 years, rājuka for 3 years) supports late-forties. Option B — Update avatar-profile.json line 9 to `"age_at_chapter_events": "34"` and shorten the implied merchant career. Pick one and apply consistently.
- **Verification:** Grep CH04_draft.md for "thirty-four" / "34" — count should match chosen age count. Profile line 9 should agree.

**2. Wife continuity break with CH05 (AUTHOR DECISION)**
- **Problem:** CH05 line 31 says "He did not sleep with his wife as she slept. He worked while others dreamed." CH04 draft contains zero wife mentions — Chandra is depicted as solitary throughout.
- **Source requirement:** incarnations/ch05-lilith-cp02 draft line 31 (wife reference); CH04 draft has no wife (grep: 0 hits on "wife").
- **Current text:** CH05: "He did not sleep with his wife as she slept. He worked while others dreamed, refining figures that would determine who received and who went without."
- **Revision instruction:** **AUTHOR DECISION.** Option A — Add a wife to CH04. Natural insertion points: the tent/hospital scene after the assassination attempt (her checking on him), or the late-night office scene (her bringing food he doesn't eat). Two or three lines, in-voice with the austere interior register; she should be present as a domestic fact he is too absorbed to inhabit. Option B — Cut the wife from CH05 line 31 entirely; rewrite as "He did not sleep when others slept. He worked while they dreamed..." Cutting is cheaper; adding deepens the dāna-as-form lesson (he has a wife and still gives only resources, not self).
- **Verification:** If Option A: CH04 should contain at least one clear wife mention (search for "wife" or a specific name) and CH05 line 31 should have a matching referent. If Option B: CH05 line 31 no longer contains "wife."

**3. Temple-passage dialogue mismatch with CH05 (AUTHOR DECISION)**
- **Problem:** CH05 lines 133–135 depict "Fifteen years counts for something" / "It has always meant nothing" being *spoken to each other* in the temple-passage ambush. In CH04, line 581 has Devaka saying "fifteen years counts for something" during a pre-fire confession (not the ambush), and line 701 is Chandra's interior thought "The words meant nothing. They had always meant nothing" — never spoken aloud. The exchange CH05 stages does not occur in CH04.
- **Source requirement:** CH05 draft lines 131–135; CH04_draft.md lines 581, 701.
- **Current text:** CH04:581 "What I've done—what I've been part of—I can't undo any of it. But fifteen years counts for something." CH04:701 "The words meant nothing. They had always meant nothing." CH05 quotes them as back-and-forth dialogue during the temple ambush.
- **Revision instruction:** **AUTHOR DECISION.** Option A — Rewrite the CH04 temple-passage ambush (the scene where Devaka's guards surround Chandra) to contain the exchange verbatim: Devaka says "Fifteen years counts for something"; Chandra answers aloud "It has always meant nothing." Move or duplicate the content from lines 581/701 into the ambush. Option B — Relax CH05's framing: make it a retrospective compression ("what he would later realize had always been two voices…") rather than a literal exchange in the passage.
- **Verification:** Either the ambush scene in CH04 now contains both lines as dialogue, or CH05:131–135 no longer claims the lines were exchanged in the passage.

**4. "Emperor" — period-rules violation (17 instances)**
- **Problem:** Period-rules mandate avoiding "emperor"; draft uses it 17+ times.
- **Source requirement:** period-rules.md lines 64–65: "avoid 'king' (use 'raja' or describe), avoid 'emperor' (describe Ashoka's position)."
- **Current text:** Lines 1, 11, 21, 31, 119, 147, 149, 157, 193, 207, 277, 317, 417, 433, 491, 791, 1019 all contain "emperor." Example line 1: "the emperor's edict."
- **Revision instruction:** Global find-and-replace pass. Use the following substitutions depending on context:

  | Current phrase | Replace with |
  |---|---|
  | the emperor's edict | the royal edict / Ashoka's edict / the edict from Pataliputra |
  | the emperor's service | the service of the Beloved of the Gods / royal service |
  | the emperor's benevolence | the Beloved of the Gods' benevolence / Ashoka's benevolence |
  | the emperor's words | Ashoka's words / the throne's words |
  | the emperor | the Beloved of the Gods / Ashoka / the throne at Pataliputra |

  Vary by rhythm and register; avoid monoculture ("Beloved of the Gods" every time is heavy). Most useful period-correct sobriquets: "Devanampiya" (Beloved of the Gods), "Priyadarsi" (He Who Regards with Kindness), "the throne at Pataliputra," and simply "Ashoka."
- **Verification:** Grep CH04_draft.md for "emperor" (case-insensitive) — zero hits.

**5. Contractions in dialogue — period-rules violation (9 instances)**
- **Problem:** Period-rules forbid contractions in dialogue; nine flagged instances are all still present.
- **Source requirement:** period-rules.md line 73: "No contractions."
- **Current text and fixes:**

  | Line | Current | Replace with |
  |---|---|---|
  | 63 | "You're awake" | "You are awake" |
  | 115 | "You'll need your strength" | "You will need your strength" |
  | 167 | "We're looking at three…" | "We are looking at three…" |
  | 181 | "I'll have the Warehouse Seven records" | "I will have the Warehouse Seven records" |
  | 193 | "I've served beside you for fifteen years" | "I have served beside you for fifteen years" |
  | 313 | "You've barely slept" | "You have barely slept" |
  | 547 | "He's been sequestered" | "He has been sequestered" |
  | 577 | "I'll contact Ananda tonight" | "I will contact Ananda tonight" |
  | 915 | "It wasn't personal" | "It was not personal" |

  Then do a full-chapter grep pass: `'re`, `'ve`, `'ll`, `'s` (as contraction of "is/has"), `'d`, `n't` — catch any others not in the review list. Narrative (not dialogue) may permit them, but the draft's dialogue should be contraction-free.
- **Verification:** Grep dialogue lines only for `'`; any remaining hits are possessives/quotes, not contractions.

**6. POV inconsistency — first person shifts to third at line 311 with a leftover first-person intrusion at 313**
- **Problem:** The draft opens in tight first person ("I had totaled…"), sustains it through line ~309, then at line 311 shifts to third person ("Devaka sat across from him…"). Line 313 contains a leftover first-person phrase inside a third-person paragraph. Confirmed still broken; POV oscillates through the rest of the chapter.
- **Source requirement:** Internal craft standard — a chapter must commit to one POV. Deathbed coda voice favors first person.
- **Current text (line 313):** "Devaka's face showed the strain of recent days—shadows beneath his eyes, **a tightness around his mouth that I had learned to read over fifteen years.**"
- **Revision instruction:** Commit to first person throughout (recommended — the interiority of the deathbed coda is better served). Convert every third-person passage from line 311 onward. Specifically:
  - Line 311: "The oil lamps in Chandra's office burned low" → "The oil lamps in my office burned low" (or "in the office I had earned").
  - "Devaka sat across from him" → "Devaka sat across from me."
  - All "he/his/him" referring to Chandra → "I/my/me."
  - Keep line 313's "I had learned to read over fifteen years" — it is now in-voice.
  - Continue conversion through the seventeen-night investigation, the temple-passage betrayal, raid, fire, death sequence.

  Alternative (third limited throughout): reverse the first half (lines 1–309), converting "I" to "Chandra/he" and fixing line 313's first-person slip.
- **Verification:** No mid-chapter POV switch. Pick any ten-line span anywhere in the chapter: pronouns are consistent.

### Should-Fix (significant but not structural)

**7. "Particularite grit" — typo/malformed word at line 5**
- **Problem:** "particularite" is not a word; the phrase is also redundant ("gritty with … grit").
- **Current text:** Line 5: "I shifted my weight and tasted the dust coating my tongue, gritty with the particularite grit of Pataliputra's riverbank clay."
- **Revision instruction:** Replace with "gritty with the peculiar grit" or, to fix the redundancy, "gritty with the fine red silt of Pataliputra's riverbank clay" (drops the doubled "grit," adds period color).
- **Verification:** Grep for "particularite" — zero hits.

**8. Ceremonial knife reference in CH05 without anchor in CH04**
- **Problem:** CH05 line 131 places "the polished surface of a ceremonial knife" in the temple-passage ambush. CH04's temple-passage ambush contains no knife. (The assassination-attempt earlier uses a katar in the marketplace, which is a different scene.)
- **Source requirement:** CH05 draft line 131.
- **Revision instruction:** Either (a) add one sentence to the CH04 ambush giving Devaka or a guard a ceremonial knife (a tilted blade catching lamp-light is enough), or (b) remove the "ceremonial knife" image from CH05 line 131 and replace with a surface that does exist in CH04 (the guard's lamp, the wet stone of the passage wall). Adding in CH04 is cheaper.
- **Verification:** If CH04 ambush now mentions a ceremonial knife, CH05:131's reflection surface is grounded. Otherwise CH05:131 no longer references the knife.

### Polish (minor, opportunistic)

**9. Katar — review flagged as anachronism; verification says the term is historically defensible for Mauryan India**
- **Problem:** The review labels "katar" anachronistic (claiming medieval/early-modern origin). Verification against period sources indicates the katar/punch-dagger form is plausibly Indian and defensible for this period, though scholarly consensus leans toward a later date of standardization.
- **Current text:** Lines 29 and 43 use "katar" for the assassin's blade.
- **Revision instruction:** Author discretion. If you want to be unambiguously safe, swap "katar" for a period-neutral description ("a short curved blade of eastern forge-work," "a punch-grip dagger"). If the scholarly defensibility is acceptable, leave it — but don't introduce new katar references.
- **Verification:** Consistent choice in lines 29 and 43; no new instances elsewhere.

### Continuity Checklist (CH04 ↔ CH03, CH05)

| Beat | CH04 line | Partner line | Status |
|---|---|---|---|
| Chandra as merchant's son turned administrator (handoff from CH03) | opening section | CH03 closing | ✓ matches |
| Wife reference | — (absent) | CH05:31 | **BROKEN — see item 2** |
| Ceremonial knife in temple ambush | — (absent) | CH05:131 | **BROKEN — see item 8** |
| "Fifteen years counts for something" as spoken dialogue in ambush | 581 (wrong scene) | CH05:133 | **BROKEN — see item 3** |
| "It has always meant nothing" as spoken dialogue in ambush | 701 (interior thought, wrong scene) | CH05:135 | **BROKEN — see item 3** |
| Devaka's "I truly am sorry" in the ash | 915 | CH05 reference | ✓ matches |
| The 15,000-measure gap | 345 | CH05 reference | ✓ matches |
| Fire consuming records while Chandra chooses ledgers over flesh | 833–859 | CH05 reference | ✓ matches |
| Girl with dark eyes as final memory | closing | CH05 / forward seed | ✓ matches |

---

## Chapter 6: Athens — Philon

### Critical Fixes (must resolve before locking)

**1. CH06/CH07 timeline conflict — blocker**
- **Problem:** CH07 stages the sequence as: Lilith dreams Alexios → Alexios leaves at midday → "The slave woman collapsed at the eastern gate three days after Alexios fled" → Philon walks to her alone. CH06 compresses these into the same day: Alexios arrives at the clinic already knowing about the slave woman, they argue, he leaves, Philon walks straight out to fetch her.
- **Source requirement:** CH07 draft lines 127 and 137; CH06_draft.md lines 299–356.
- **Current text (CH06):** L299 "Alexios found him near midday"; L315–339 argument including "I cannot follow you to her" / "Go to Eleusis"; L356 Alexios departs; Philon immediately walks "toward the eastern gate." CH07: L127 "Alexios left at midday. Lilith watched him go through the thread." L137 "The slave woman collapsed at the eastern gate three days after Alexios fled."
- **Revision instruction:** **AUTHOR DECISION** on which text moves, but the draft cannot ship with both versions. Preferred path (aligns with the Greek-tragic fatalism): **Rewrite CH06 to match CH07.** In CH06 Scene V / VI:
  - Have Alexios leave the clinic first, driven by accumulated pressure plus the unspoken dream-shift (see item 3 below). No slave woman mentioned yet.
  - Insert a brief passage of elapsed time — "Three days passed. The refugees at the eastern gate grew denser. On the morning of the third day, a messenger came: 'There is a woman at the eastern gate. Collapsed. None will touch her.'"
  - Then Philon walks out alone to fetch her.
  - Keep the triage argument as the proximate cause of Alexios's departure — but not as the same scene in which Philon learns about the slave woman.
  - Alternative: rewrite CH07 to say "Alexios left that morning. By afternoon the slave woman had collapsed at the eastern gate." — loses the fatalistic three-day pause but is cheaper.
- **Verification:** CH06 and CH07 agree on: (a) Alexios's departure precedes the slave woman's collapse; (b) the gap between the two is either named (three days) or collapsed in both chapters identically.

**2. Philon's age — profile vs. draft**
- **Problem:** Profile specifies "late 30s"; draft says "forty years" twice.
- **Source requirement:** avatar-profile.json line 9: "Lean, sun-worn Athenian man in his late 30s, prematurely aged by long hours…"; CH06_draft.md lines 567 and 597.
- **Current text:** L567: "He lay on the pallet and felt his body becoming foreign to him, a thing of meat and bone that had carried him through forty years…" L597: "The body that had carried him through forty years became, finally, irrelevant."
- **Revision instruction:** Change both instances to "his thirty-ninth year" or "nearly forty years" — phrasing that preserves the meditative rhythm while honoring the late-30s mandate. "Thirty-ninth year" is rhythmically cleaner in both lines.
- **Verification:** Grep CH06_draft.md for "forty years" — zero hits (or reframed as age markers compatible with late 30s).

**3. Scythian woman's age — internal contradiction**
- **Problem:** L369 says "perhaps twenty years"; L441 says "perhaps thirty years old." Same character, same chapter.
- **Source requirement:** Internal consistency; avatar-profile.json specifies the climactic patient as young.
- **Current text:** L369: "She was younger than he had expected, perhaps twenty years…" L441: "She was perhaps thirty years old. Someone's daughter, once."
- **Revision instruction:** Harmonize to "perhaps twenty" at both points. Rewrite L441 to "She was perhaps twenty years old. Someone's daughter, once." Young matches the profile, matches the tragedy's pathos, and matches L369's earlier beat.
- **Verification:** Search CH06 for "thirty years" — zero hits referring to this woman. Both L369 and L441 agree on the age.

### Should-Fix (significant but not structural)

**4. Tanner continuity — Alexios references a patient not in the morning montage**
- **Problem:** L31 has Alexios say "You hesitated with the tanner" — but the three morning patients shown at L23 are a boy with a gash, an old woman with aching joints, and a young man with a cough. A tanner is mentioned only at L105 as part of idle description, after Alexios's line.
- **Source requirement:** Internal continuity.
- **Current text:** L23: "By mid-morning, three patients had already come and gone. A boy with a deep gash on his forearm… An old woman whose joints ached… A young man with a cough…" L31: "'You hesitated with the tanner,' Alexios said quietly, during a lull between patients."
- **Revision instruction:** Insert a fourth morning patient at L23 — the tanner with an infected hand or foot — giving Philon a visible hesitation (he touches the wound, withdraws, resumes). Four or five lines. Example replacement/addition: "A boy with a deep gash on his forearm, cleaned and sutured without complication. An old woman whose joints ached — willow bark, a poultice, reassurance. A tanner whose hand had gone septic where the hide-scraper had bitten; Philon's fingers paused a moment above the swelling before he reached for the cautery iron. A young man with a cough…" Then the L105 "tanner's infected foot" reference should be changed to "tanner's infected hand" (or wherever you placed it) for consistency.
- **Verification:** Alexios's "You hesitated with the tanner" at L31 has a matching tanner in the preceding patient list, and the L105 reference agrees with the earlier wound site.

**5. Missing chapter title**
- **Problem:** CH05 is titled "The Ledger's Shadow"; CH06 opens cold with no title.
- **Source requirement:** Editorial convention established by CH05.
- **Revision instruction:** Add a chapter title above the first line. Candidates consistent with the chapter's themes: "The Physician's Vow," "What Virtue Wears," "Fear in Virtue's Face," "The Eastern Gate." The last line of the chapter — "It was not virtue. It was fear wearing virtue's face" — suggests **"Virtue's Face"** or **"Fear Wearing Virtue's Face."**
- **Verification:** CH06 opens with a title line matching CH05's formatting.

**6. Alexios morning-after dream cue (subtle addition)**
- **Problem:** CH07 reveals Alexios dreamed "the smell of ash on his tongue" the night before he cracks. CH06 gives no ambient signal in Philon's POV — Alexios just appears exhausted.
- **Source requirement:** avatar-profile.json and period-rules.md both say Lilith must be invisible in Philon's POV, but a cue Alexios has dreamed will give CH07's revelation retroactive power without violating the POV rule.
- **Revision instruction:** In the morning scene (before L31's "you hesitated with the tanner" beat), add a single observational line from Philon: e.g., "Alexios had slept poorly. The smudge beneath his eyes was darker today; he rubbed his tongue against his teeth as though something lingered there he could not name." Two sentences, in Philon's voice, clinical-observational. No interpretation, no dream content — just the physical trace.
- **Verification:** A line in the opening montage registers Alexios as having slept badly, and CH07:113's "gasped awake... taste of ash on his tongue" now has a matching morning-after signal in CH06.

### Polish (minor, opportunistic)

**7. Two magistrate visits vs. outline's one confrontation (author discretion)**
- **Problem:** Outline specifies one magistrate confrontation; draft has two (L179 status-based triage, L265 Eleusis relocation). Structurally works as escalation but risks redundancy.
- **Current text:** L179: "The magistrates did more than object…" L265: "The magistrate came at dawn…'You are ordered to relocate to the estates at Eleusis.'"
- **Revision instruction:** Author discretion. If keeping both, sharpen the distinction: make the first visit about a specific rich patient, the second about the class as a whole — same pressure escalating toward abstraction. If cutting to one, merge: fold the Eleusis order into the first visit's climactic demand, preserving Kallias's citizen-blood retort in a single sustained exchange.
- **Verification:** Either the two visits now have clearly distinct rhetorical work, or they are consolidated into one.

**8. Sectional markers — outline mandates 9-part tragic architecture labels**
- **Problem:** Outline specifies labeled sections (Prologos / Parodos / First Episode / First Stasimon / Second Episode / Second Stasimon / Third Episode / Kommos / Exodus). Draft uses only "---" breaks.
- **Current text:** Section breaks at lines 297, 363, 403, 445, 483, 523, 537, 561, 593, 613, 627.
- **Revision instruction:** Author discretion / editorial standard. If the manuscript-wide convention is unlabeled "---" breaks, leave as-is. If labeled sections are preferred, add headers above each break matching the outline's nine-part scheme. Currently there are more "---" breaks than nine parts — consolidate to exactly nine.
- **Verification:** Section count matches the chosen convention.

### Positive checks (confirm still present — do not remove)

| Beat | Line | Status |
|---|---|---|
| "Snow where no snow fell" (Ka-echo, not Lilith) | 359 | ✓ present |
| Philon's tragic flaw articulated | 595–597 | ✓ present |
| "It was not virtue. It was fear wearing virtue's face" | closing | ✓ present |
| Word count ≈ 10,447 (target ~10k) | whole chapter | ✓ on target |
| Hippocratic observational ethos | throughout | ✓ present |
| Xenophobic rumor-surge (Persian poisoning) | scene | ✓ present |
| Butcher's stalls → pyres → "meat among meat" → "wheel of meat turned" | throughout | ✓ present |

### Continuity Checklist (CH06 ↔ CH05, CH07)

| Beat | CH06 line | Partner line | Status |
|---|---|---|---|
| Handoff from CH05 ("Athens. A physician named Philon.") | opening | CH05 closing | ✓ matches |
| Alexios's midday departure precedes slave woman's arrival | 299–356 (wrong) | CH07:127, 137 | **BROKEN — see item 1** |
| Alexios's dream cue | absent | CH07:113 | **MISSING — see item 6** |
| Snow where no snow fell | 359 | (Ka-echo) | ✓ matches |
| Closing seed: "There must be a way to understand virtue correctly" | final line | CH07 opening | ✓ matches |

---

## Chapter 8: Rome — Verinus

### Critical Fixes (must resolve before locking)

**1. Pride ending vs. mandated softening (AUTHOR DECISION / most significant concern)**
- **Problem:** The draft's ending crystallizes "subtle pride" across four separate passages, framing the karmic residue as pride-in-having-transcended-certainty. The avatar profile says the insight "dissolves his resentment and prepares him for the next incarnation's confrontation with desire and emotional entanglement" — i.e. softening seeds vulnerability to beauty/desire, not pride. The outline calls for "bittersweet anonymity." The draft diverges from both.
- **Source requirement:** avatar-profile.json line 32 ("This insight dissolves his resentment and prepares him for the next incarnation's confrontation with desire and emotional entanglement"); period-rules.md / outline lines 327–336 ("bittersweet anonymity… karmic invitation to next life"); CH08_draft.md lines 755, 761, 767, 787, 811.
- **Current text:** L755: "the first seed of pride: the quiet self-regard of having understood what others could not." L761: "He had traded one attachment for another, and he did not see it." L767: "A pride lurked in the stillness, disguised as peace. But he could not see it. Not yet." L787: "The satisfaction felt like wisdom, but it tasted, faintly, of pride." L811: "carrying forward too the subtle pride that would make the next life vulnerable."
- **Revision instruction:** **AUTHOR DECISION.** Option A (recommended — aligns with profile & Heian bridge) — Trim the pride thread. Keep one subtle touch (retain the L787 "tasted, faintly, of pride" beat as a single shadow), delete the other three, and add a softening beat that specifically seeds the Heian lover's vulnerability to beauty: Verinus notices the olive light, Marcus's handwriting, the cook's absent laughter — some sensory particular touched with tenderness he has never before permitted himself. Three or four sentences. Option B — Retain the pride framing but rewrite avatar-profile.json line 32 to accept pride-as-residue as the karmic bridge to the Heian life (in which case the Heian chapter's vulnerability needs to be reframed from "desire/beauty" to "self-regard colliding with beauty"). Option A is the less invasive revision.
- **Verification:** If Option A: three of the four pride passages are gone; a new softening beat exists between L755 and L811; L787 retains a single subtle pride shadow. If Option B: the profile is updated and the Heian chapter's seeding is adjusted accordingly.

**2. Mandated closing articulation — two-clause vs. compressed (AUTHOR DECISION)**
- **Problem:** period-rules.md:126–127 mandates "Virtue is not the absence of error. / It is compassion within uncertainty." Draft at L795 uses compressed "Virtue lives where certainty fails." The outline at line 329 endorses the compressed form. **Two source documents contradict each other.**
- **Source requirement:** period-rules.md lines 126–127 (two-clause); outline line 329 (compressed); CH08_draft.md line 795.
- **Current text (all three):** period-rules: "Virtue is not the absence of error. / It is compassion within uncertainty." Outline line 329: "Virtue lives where certainty fails." Draft L795: "Virtue lives where certainty fails."
- **Revision instruction:** **AUTHOR DECISION.** Option A — Restore the period-rules two-clause version at L795: "Virtue is not the absence of error. It is compassion within uncertainty." This anchors "compassion" as the positive term and honors the explicit period-rules mandate. Option B — Keep the compressed form and update period-rules.md to match (noting the compressed version is the canonical articulation). Option C — Use both: let the compressed "Virtue lives where certainty fails" stand where it is, and insert the fuller two-clause formulation earlier (Scene 8 or 9, as Verinus is reasoning toward the insight). This is the most respectful compromise.
- **Verification:** Either the two documents now agree, or both versions of the line exist in the chapter in different rhetorical positions.

**3. Marcia Faenia silent cameo vs. profile's "partial truths"**
- **Problem:** Avatar profile says Marcia "offers partial truths meant to harden Verinus's absolutism." Draft shows her only observing (baths + portico), never speaking to Verinus. Outline endorses the silent cameo. Profile and outline contradict each other.
- **Source requirement:** avatar-profile.json line 40 (Marcia offers partial truths); outline line 181 (non-interference observation); CH08_draft.md lines 37–41, 381–407.
- **Current text (draft):** L37–41 baths: Marcia watches Verinus across the caldarium. L381–407 portico: she observes the philosophical debate, then turns away.
- **Revision instruction:** **AUTHOR DECISION.** Option A — Keep the silent cameo (internally consistent, strong restraint; matches outline). Update avatar-profile.json line 40 to describe Marcia as "a quiet presence whose proximity Verinus feels but cannot name; she does not speak." Option B — Add a brief spoken exchange. In the portico scene, after the philosophical debate, have Marcia approach Verinus with a single question or half-answered clue about the case — something like "Have you asked the cook about the second hour?" — delivered in a way that is both true and misleading (the cook's testimony does shift the case, but not the way Marcia's tone implies). Three to six lines, no more. She turns away before he can press.
- **Verification:** Either the profile now matches the silent-cameo draft, or the draft adds a brief Marcia exchange matching the profile.

### Should-Fix (significant but not structural)

**4. Scene 9 solitary death vs. outline's freedman/cook discovery**
- **Problem:** Outline specifies "Freedman finds him at dawn. Stylus still in hand... Freedman calls for cook. They stand together, unsure what to do." Draft explicitly eliminates the discovery: "No witnesses. No discovery. Only the grove darkening around a man… Neither knew that the man they served was dying."
- **Source requirement:** Outline lines 317–325; CH08_draft.md lines 803–811.
- **Current text (L803):** "No witnesses. No discovery. Only the grove darkening around a man…"
- **Revision instruction:** Restore the outlined "bittersweet anonymity — surrounded by people who don't know him" close. Keep Verinus's final lonely thought-sequence, then add a closing micro-scene at dawn: Servius the freedman finds him beneath the olive tree, stylus still in hand; he calls the cook; they stand together uncertain, the cook eventually kneeling to close Verinus's eyes. Four to eight sentences. The thematic force is the anonymity-with-witness: people who served him, who do not know who he was. This is stronger than pure solitude. (If author prefers solitary death for artistic reasons, flag as a deliberate deviation from outline in a revision note rather than silently diverging.)
- **Verification:** Chapter closes with Servius and cook present but not comprehending, or the divergence is documented as deliberate.

**5. "He could not see it" / "He did not see it" repetition — 3 instances, trim to 1 or 2**
- **Problem:** Phrase appears at L761, L767, L789. Three is too many; the pattern calls attention to itself and hammers the point.
- **Current text:** L761: "he did not see it." L767: "But he could not see it. Not yet." L789: "He did not see it. He could not see it."
- **Revision instruction:** Keep one instance (L767 is the most tonally placed). Cut L761's tag (the sentence works without it) and rewrite L789 to carry the weight without repeating the phrase — e.g. "The lesson had become a possession, and possessions are not easily released." If item 1 above trims the pride thread, item 5 is partially resolved automatically.
- **Verification:** Grep for "could not see it" and "did not see it" in CH08 — at most 1 hit each, 2 hits total.

**6. Scribal error structural weight — reorder testimony discovery (author discretion)**
- **Problem:** Avatar profile treats the scribal error as the "inciting fracture" that initiates the cascade of contradictions. In the current draft, three testimonies already contradict *before* Verinus finds the temperate/intemperate inversion, so the error functions as confirmation rather than trigger.
- **Source requirement:** avatar-profile.json (scribal error as inciting fracture); CH08:73–78 (testimonies) vs. CH08:117 (scribal inversion).
- **Revision instruction:** Author discretion. Two clean options:
  - Reorder: have Verinus read the scribal error *first* (his opening review of the case file), then discover the three testimonies; the error now sets up the instability that the testimonies confirm.
  - Keep current order but reframe the scribal error as the specific wedge that breaks Verinus's first reconstruction attempt: Verinus resolves the three testimonies' contradictions into a coherent story, then the scribal error shatters his reconstruction and forces him to start over. This preserves the current scene order while restoring the profile's "inciting fracture" weight.
- **Verification:** The scribal error either precedes the testimonies or functions as the breakpoint of Verinus's first resolution.

### Polish (minor, opportunistic)

**7. Ch9 line reference alignment — "I was close enough to touch him"**
- **Problem:** Review anchors CH09:241 "I was close enough to touch him" to CH08:379–387, but the CH08 line range at 379–387 is the portico philosophical dialogue between philosophers, not a Marcia-proximity moment. Marcia's actual proximity beats are at L37–41 (baths) and L381–407 (portico observation).
- **Revision instruction:** No draft change needed unless the author wants to update internal tracking. If CH09:241 is meant to refer to the portico observation moment, both authors/editors should note the correct CH08 anchor is L381–407 (not 379–387).
- **Verification:** Internal tracking doc (if any) shows correct anchor.

### Positive checks (confirm still present)

| Beat | Line | Status |
|---|---|---|
| Bronze stylus compulsively cleaned | 11, 79, 135, 245, 325, 519, 745, 801 | ✓ present |
| Temperate/intemperate scribal inversion | 117 | ✓ present |
| Forum Boarium traffic stall / cook's timeline | 412–479 | ✓ present |
| "I was close enough to touch him" sentiment (Marcia's felt proximity) | 381–407 | ✓ present |
| Trembling hands | 73 (servant), 543 (youth) | ✓ present |
| Senatorial rage | 657–698 | ✓ present |
| Marcus's letter appointment to Brundisium | 685, 719–731 | ✓ present |
| Tarnished uncleaned stylus in grove | 745, 753, 809 | ✓ present |
| Three-month weathering in exile | 714 | ✓ matches CH09 |

### Continuity Checklist (CH08 ↔ CH07, CH09)

| Beat | CH08 line | Partner line | Status |
|---|---|---|---|
| Handoff from CH07 (Rome, procedural investigator) | opening | CH07:327 | ✓ matches |
| Baths/stylus/grain-ship | 1–53 | CH09:17–20 | ✓ matches |
| Temperate/intemperate clerk error | 117, 179–180 | CH09:85–107 | ✓ matches |
| Portico/Marcia cameo | 381–407 | CH09:151–223, 241 | ✓ matches |
| Forum Boarium cook | 412–479 | CH09:263–279 | ✓ matches |
| Trembling-hands compassion break | 543 | CH09:299–303 | ✓ matches |
| Amplified senatorial rage | 657–698 | CH09:333–343 | ✓ matches |
| Marcus's letter verbatim | 719–731 | CH09:377–383 | ✓ matches |
| Tarnished stylus in grove | 745–809 | CH09:393–409 | ✓ matches |
| Softening / karmic bridge to Heian | ending | — | **COMPROMISED — see item 1** |

---

## Chapter 10: Egypt — Macarius the Hermit

### Critical Fixes (must resolve before locking)

**1. Ineffable climax violation — Scenes VIII–IX regress into essayistic inner monologue**
- **Problem:** period-rules.md:209 and chapter-outline.md:162 both mandate: "The recognition is physical. No inner monologue explaining — the trembling hands, the held breath, the taste in his mouth ARE the recognition." Scene VII honors this; Scenes VIII and IX then collapse into paragraphs of narrated psychological analysis.
- **Source requirement:** period-rules.md line 209 ("The moment of recognition is physical before it is understood. No declaration — the insight is embodied through trembling hands, held breath, the taste of hunger"); chapter-outline.md line 162; CH10_draft.md lines 745, 789, 805, 813, 837, 899, 987.
- **Current text (representative):** L745: "Only the scholar becoming the ascetic… the structure never changing…" L789: "He had experienced, instead, a very sophisticated form of self-filling — a hollowing out of certain desires… and a filling up with others." L805: "He had not transcended desire. He had refined it. He had distilled it into a purer form, concentrated and lethal."
- **Revision instruction:** Cut ~30–40% of Scene VIII. Specifically:
  - Delete the extended analytical passages at L745, L789, L805 entirely.
  - Replace with somatic/environmental prose: the body's grief, the cell's changed acoustics, the failed prayer, the taste of rancid honey returning, the hand refusing to reach for the reed basket. Two or three aphoristic fragments in the Apophthegmata register (cf. L117 "The prayer is not the rope that binds the sheep") are permitted; no extended exposition.
  - Scene IX (the death sequence) should be similarly compressed: fewer sentences of analysis, more sensory stillness. The chapter's already-delivered tasting-moment at Scene VII carries the insight; Scenes VIII–IX should *inhabit* it, not restate it.
  - Target: Scene VIII should lose roughly 600–800 words. Scene IX should lose 300–500.
- **Verification:** Scenes VIII–IX contain no paragraphs of sustained psychological analysis. Any interior content is fragmentary, sensory, or aphoristic. Chapter word count drops from 14,040 toward the 9,700 budget.

**2. Anachronistic Greek terminology in narration (kenosis, theosis)**
- **Problem:** period-rules.md:155–160 forbids non-universally-recognizable Greek terms. Draft uses "kenosis" four times and "theosis" twice in narration (one narration use is OK in Theophanes's dialogue at L337, but the narration uses are not).
- **Source requirement:** period-rules.md lines 155–160; CH10_draft.md lines 785, 787, 813, 837, 899, 987 (narration).
- **Current text:** L785: "The fathers spoke of kenosis." L787: "He had never experienced kenosis." L813: "the holy emptiness of kenosis." L837: "more like dying than theosis." L899: "He did not know if this was theosis." L987: "more raw than theosis."
- **Revision instruction:** Replace every narration instance with period-appropriate English paraphrase. Suggested substitutions:

  | Current | Replace with |
  |---|---|
  | kenosis (narration) | "the emptying the fathers spoke of" / "the self-emptying" / "hollowing" / simply "emptiness" |
  | theosis (narration) | "the union the fathers named" / "the becoming-one-with-God" / "the union" |

  Preserve L337 "theosis — union with God" in Theophanes's spoken dialogue (character speech is acceptable; the character unpacks the term in the same breath).
- **Verification:** Grep CH10_draft.md for "kenosis" — only contexts that are clearly dialogue, if any. Grep for "theosis" — zero outside L337.

**3. Modern psychological vocabulary in narration — 9+ instances**
- **Problem:** period-rules.md:159 proscribes modern psychological vocabulary. Draft uses "self-image," "structure," "framework," "self-filling" as if they were neutral terms.
- **Source requirement:** period-rules.md line 159 ("Avoid modern psychological vocabulary (e.g., 'trauma response,' 'ego dissolution'). Convey these through behavior and sensation").
- **Current text:**

  | Term | Lines | Current usage |
  |---|---|---|
  | self-image | 717, 781, 813, 855, 895 | "falling away of false self-image," "the ruins of his self-image" |
  | structure (psychological sense) | 691, 745, 767, 895 | "structure of his pride," "structure never changed" |
  | framework | 484, 551, 807 | "framework" |
  | self-filling | 789 | "a very sophisticated form of self-filling" |

- **Revision instruction:** Convert each to concrete imagery in desert-appropriate register:

  | Current term | Replace with concrete image |
  |---|---|
  | false self-image | "the face he had shown himself in the dark" / "the reed-basket portrait" |
  | structure of his pride | "the ladder of his pride" / "the scaffolding he had built" |
  | the structure never changed | "the shape of the thing was unchanged" / "the vessel's wall, hidden, was the same" |
  | framework | "the frame" / "the reed-bed" / simply "the order he had kept" |
  | self-filling | "a filling with other things — reverence in place of respect, holiness in place of learning — but a filling all the same" |

  One use of "structure" in the chapter is arresting; seven uses is essayistic. Aim for no more than one instance total.
- **Verification:** Grep CH10_draft.md for "self-image" → zero narration hits; "structure" → at most one hit (ideally zero) in narration; "framework" → zero; "self-filling" → zero.

**4. Macarius quasi-supernatural awareness of Theodora**
- **Problem:** avatar-profile.json:62 specifies "he does not recognize their significance" regarding Theodora's markers. Draft shows Macarius consciously inferring her interior state ("She was satisfied. She had been waiting for something") and narrating predator metaphors that over-tell Lilith's nature.
- **Source requirement:** avatar-profile.json line 62; CH10_draft.md lines 233, 409–415, 571–573, 691–707.
- **Current text:** L233: "the stillness of a spider in its web." L409: "a predator waiting for movement." L571–573: "She was speaking of him. He could not hear the words, but he knew this as certainly as he knew his own heartbeat." L691–707: reads her satisfaction and intention.
- **Revision instruction:** Two-part fix:
  - Soften L571–573 to uncertain suspicion: "She seemed to be speaking of him. He could not know — the words did not carry. But something in her posture tilted his way, and he looked down." Removes the clairvoyant certainty.
  - Keep one predator/spider metaphor — L233 is the stronger because earlier — and cut L409. Two such metaphors in one chapter reads like winking at the reader; one reads like pilgrim intuition.
  - Rewrite L691–707 so Macarius registers Theodora's stillness without reading her satisfaction. He observes she is watching; he does not know why she is watching or what she wants.
- **Verification:** Only one predator/stillness metaphor per chapter (L233). No passage in which Macarius reads Theodora's interior with certainty. L571–573 phrased as suspicion, not knowledge.

### Should-Fix (significant but not structural)

**5. Young monk named (Paphnutius) vs. outline's unnamed (AUTHOR DECISION)**
- **Problem:** chapter-outline.md:62 specifies the young monk is unnamed. Draft names him Paphnutius at L75 and uses the name consistently through L879.
- **Source requirement:** chapter-outline.md line 62; CH10_draft.md lines 75, 879.
- **Revision instruction:** **AUTHOR DECISION.** Option A — Keep Paphnutius named. The affective beat at L879 ("Paphnutius, persistent as hope, eventually stopped coming") is genuinely stronger with a name attached. Update the outline to permit naming. Option B — Strip the name; refer to him as "the young monk" or "the young brother" throughout. Cheaper but loses the emotional specificity.
- **Verification:** Either outline is updated to permit Paphnutius's name, or all instances of "Paphnutius" in CH10_draft.md are replaced with an unnamed reference.

**6. Didymus warning — pre-installed Chekhov's gun (optional softening)**
- **Problem:** L201 Didymus's warning ("The snake that flatters is more dangerous than the snake that bites") is a planted alarm that slightly undermines Macarius's blindness to his own pride.
- **Current text:** L201: "The snake that flatters is more dangerous than the snake that bites."
- **Revision instruction:** Keep the warning in (it's a fine line), but extend Macarius's dismissal so the reader feels the dismissal is total: add a sentence or two in which Macarius recognizes the wisdom of the saying in abstract, files it among other aphorisms he has mastered, and moves past it. The reader should feel the dismissal's weight, not just infer a warning was missed. Two or three lines added after L201.
- **Verification:** A new beat exists after L201 in which Macarius explicitly dismisses Didymus's warning as already-known wisdom.

**7. Word count — 14,040 vs. 9,700 target**
- **Problem:** Draft is 4,340 words over the outline budget. Bloat concentrated in Scenes VIII–IX.
- **Source requirement:** chapter-outline.md line 224 (≈9,700 words).
- **Revision instruction:** Fixing item 1 (ineffable climax) removes the single largest block of bloat. After that cut, a further pass through Scene IX's fever-memory sequence should recover another 400–800 words. Priority order for cuts: (a) essayistic analysis in Scene VIII (item 1), (b) fever-memory sequence in Scene IX, (c) redundant Theodora-observation beats in Scenes IV–V.
- **Verification:** Chapter word count ≤ 10,500 (flexibility on the 9,700 budget acceptable; 14,040 is not).

### Polish (minor, opportunistic)

**8. Theodora's departure — CH10 physical-slip vs. CH11 dematerialization (author discretion)**
- **Problem:** CH10 L731 has Theodora "physically slip away" (in fact, per verification, CH10 may already show her simply leaving with the delegation; no magical departure); CH11 L315 has her body "flicker and be gone." From Macarius's POV, these are identical; the authorial tension is small.
- **Revision instruction:** No draft change required. If polishing, make sure CH10's departure passage is ambiguous enough that CH11's "Theodora-body flickered and was gone" can describe the same event from Lilith's side.
- **Verification:** CH10 departure passage permits CH11's dematerialization interpretation.

### Positive checks (confirm still present)

| Beat | Line | Status |
|---|---|---|
| Theodora widow's peak / dark strand | 189–191 | ✓ present |
| Green crescent eleven-to-one o'clock | 321 | ✓ present |
| Pendulum passage seeding Heian | 875, 947–949, 1015 | ✓ present |
| "The prayer is not the rope…" | 117 | ✓ present |
| Non-interaction: Theodora whispers only to Theophanes | 299–301, 335 | ✓ mostly present (see item 4) |
| Scholar backstory / Alexandria rhetoric | interview scene | ✓ present |
| Opening fly / sensory deprivation register | 1–5 | ✓ present |
| Final "fingers closed on nothing" | 1011 | ✓ present |

### Continuity Checklist (CH10 ↔ CH09, CH11)

| Beat | CH10 line | Partner line | Status |
|---|---|---|---|
| Handoff from CH09 (scholar turned ascetic, Scetis) | opening | CH09 closing | ✓ matches |
| Headache/pressure (Verinus "clean the stylus" karmic echo) | 281 | CH08 stylus reflex | ✓ matches |
| Gathering scene collapse | 659–707 | CH11:295–305 | ✓ matches |
| Theodora smile and disappearance | 683–731 | CH11:315–317 | ✓ matches |
| Pendulum color/softness seed → Heian | 947–1015 | CH11:415 | ✓ matches |

---

## Chapter 12: Heian — Kaoru

### Critical Fixes (must resolve before locking)

**1. Kaoru's signature incense — missing avatar marker**
- **Problem:** Avatar profile specifies Kaoru "carries a scent of strange incense that no one can identify." Draft contains zero instances of a Kaoru-specific scent; all incense is environmental (the Pavilion's plum).
- **Source requirement:** avatar-profile.json line 9 (incense scent signature); CH12_draft.md Scene I (no Kaoru scent).
- **Current text:** Line 188: "The plum scent followed him like a living thing, clinging to his robes" — this is Lilith's/Attendant's plum scent clinging *to* him, not his own signature.
- **Revision instruction:** Insert the incense signature into Scene I, early enough that it's established before the Pavilion visit. Example insertion (to place after the opening image, roughly L10–20):

  > "He carried a scent others sometimes remarked upon — a thread of incense no one could place. Not sandalwood, not aloeswood, not kyara. It clung to the inner layers of his robes like memory of a fire he had not stood beside. When asked, he could not name it; when he smelled for it himself, it was gone."

  The detail should then recur at least once mid-chapter: a servant catches it and pauses; or it collides with the plum scent in Scene II, creating a sensory dissonance that the reader registers even if Kaoru does not. This is a required Gothic echo that the Pavilion scene currently underutilizes.
- **Verification:** Grep CH12_draft.md for "incense" — at least one hit tied specifically to Kaoru's body/robes, independent of the Pavilion. At least one sensory collision between Kaoru's scent and the Pavilion's plum.

**2. Pale/translucent skin — baseline missing in Scene I**
- **Problem:** Profile specifies "pale, almost translucent skin." Draft only describes him as "pale, hollowed" mid-illness (L361); the baseline is absent from Scene I.
- **Source requirement:** avatar-profile.json line 9; CH12_draft.md Scene I.
- **Current text:** Scene I (L1–106) has robes and behavior but no face/skin description.
- **Revision instruction:** Add a single line in Scene I establishing baseline translucency. Suggested insertion around L5–15, within the tracing-cup-rim beat:

  > "His skin had always held that near-translucent quality the court poets called 'winter moon' — a pallor that made him look, in indirect light, as though he might lean through the screens rather than around them."

  Two sentences. Then L361's mid-illness description becomes a deterioration of an established quality, not a first-time visual.
- **Verification:** Scene I contains a skin/pallor description for Kaoru.

**3. Scene IV over-explanation of the Attendant/Lilith rupture**
- **Problem:** period-rules mandate: "When the Attendant 'wakes' and flees, do not interpret. Let the rupture stand." Draft at L365 interprets explicitly, naming what the presence is and that it knows Kaoru has seen it.
- **Source requirement:** period-rules.md line 156; CH12_draft.md line 365.
- **Current text (L365):** "A presence lived inside the Attendant — an intelligence that watched, that waited, that assessed visitors with eyes that did not belong in a human face. And that presence knew he had seen it."
- **Revision instruction:** Cut L365 entirely. Replace with a body-reaction-only passage — roughly 30–60 words — that does not name the presence. Draft text:

  > "Something behind her eyes settled, tilted, looked. Kaoru's breath stopped. The hand he had been reaching toward the fan's edge closed on empty air. He did not remember standing. He did not remember reaching the threshold. He remembered only the taste in his mouth, thin and metallic, and the way the corridor seemed, for a moment, to have no other end."

  Let the reader infer what the physical reaction implies. The body carries the meaning.
- **Verification:** L365 no longer contains interpretive language about "presence," "intelligence," "knew he had seen." Only body reaction.

### Should-Fix (significant but not structural)

**4. Closing karmic-bridge paragraph names the Inquisition setting too explicitly**
- **Problem:** L560 "a man would be accused of heresy and tortured for his beliefs" explicitly names the next chapter's setting from inside a Heian death. The outline calls for the bridge but naming Inquisition-specific imagery violates the period's interiority.
- **Source requirement:** period-rules.md (imagistic transmission only); CH12_draft.md line 560.
- **Current text (L560):** "Somewhere far away, in a time that had not yet happened, a man would be accused of heresy and tortured for his beliefs. He would endure. He would not break."
- **Revision instruction:** Rewrite to transmit the *shape* of endurance rather than the next chapter's plot. Suggested replacement:

  > "Somewhere the shape of this would come again. Not this room, not this illness, not this beautiful cage — but the same question: to endure what is real, even when the real is unbearable. Somewhere a man would stand still while the world pressed fire against his face, and he would stand still, and the standing would be the answer. It would be enough. It would be everything."

  Preserves the karmic transmission (endurance under pressure) without specifying heresy or torture. The final "It would be enough. It would be everything" ties into CH13's paraphrase of Kaoru's final insight.
- **Verification:** L560 no longer names "heresy" or "tortured." The bridge transmits endurance as a shape/question, not a scenario.

**5. Scene III "victim, not keeper" beat — missing**
- **Problem:** Outline Scene III asks for a beat where Kaoru passes the Attendant "slumped against a pillar, eyes closed, hands raw and trembling… For a moment she looks like a victim, not a keeper." Draft replaces this with the maple-branch-burning discovery.
- **Source requirement:** CH12_outline.md Scene III mandate (line 80); CH12_draft.md Scene III (lines 245–303).
- **Revision instruction:** Restore the beat as a brief addition, not a replacement. Keep the maple-branch-burning scene but insert — just before or after it — a single-paragraph moment in which Kaoru glimpses the Attendant in unguarded collapse:

  > "He passed her once in the garden corridor. She was slumped against a pillar, eyes closed, hands raw where the knuckles had split from whatever she kept scrubbing. For a moment she looked less like a keeper of this house than its most carefully hidden victim. Then her eyes opened, and she straightened, and the face he knew resumed its place."

  Six to ten sentences. The ambiguity — helper compelled, or keeper dissembling — is the point.
- **Verification:** Scene III contains a moment where Kaoru sees the Attendant as victim rather than keeper.

**6. Modern-psychological phrasings under fever pressure (author discretion)**
- **Problem:** Three phrases skirt modern idiom, though each is defensible as fever-state interiority:
  - L448: "a country he had not known existed"
  - L476: "the loosening of chains he had not known he wore"
  - L532: "suffocating in the absence of death"
- **Revision instruction:** Author discretion. If keeping, the fever frame supports them. If swapping for period register:
  - "a country he had not known existed" → "a province whose name no map had given him"
  - "the loosening of chains he had not known he wore" → "the slack in a rope he had not known his wrists had held"
  - "suffocating in the absence of death" → "airless where death should have been"
- **Verification:** Either the three phrases remain as fever-state or are replaced with the period-register alternatives.

### Polish (minor, opportunistic)

**7. Date discrepancy — outline 1000 CE vs. period-rules 1100 CE (AUTHOR DECISION / documentation)**
- **Problem:** CH12_outline.md line 6 says "c. 1000 CE"; period-rules.md line 29 says "circa 1100 CE / 1050–1150 CE." The draft is silent, so reader-facing prose is not affected.
- **Revision instruction:** **AUTHOR DECISION.** Reconcile the two supporting documents: pick one date range and update the other. The later window (1050–1150, circa 1100) fits the "late Heian maturity" framing better and aligns with the death-of-court-culture atmosphere.
- **Verification:** Outline and period-rules both reference the same window.

**8. Scene length targets — Scene I under target by ~370 words; Scene V under by ~320**
- **Problem:** Scene I draft ~1,430 vs. target ~1,800; Scene V draft ~1,680 vs. target ~2,000.
- **Revision instruction:** Items 1 (incense) and 2 (translucent skin) will add ~50–100 words to Scene I; remaining expansion should develop the pre-Pavilion boredom (Scene I) — one additional court-scene sketch of the safety Kaoru is escaping. For Scene V, optional: add ~300 words expanding the storm's sustained violence, slow collapse of the illusion, and one more charged moment of mutual gaze with the Attendant before Kaoru pushes past her (addressing the review's handoff concern re: CH13 "really looked" memory).
- **Verification:** Scene I ≥ 1,750 words; Scene V ≥ 1,950 words; an Attendant mutual-gaze moment exists in Scene V.

### Positive checks (confirm still present)

| Beat | Line | Status |
|---|---|---|
| Widow's peak / rogue strand / pale-green crescent | 93 (Scene I), 341–343 (Scene IV) | ✓ present |
| Tracing cup/fan rim recognition marker | 2, 21 | ✓ present |
| Withered-leaf robes (browns to faded gold) | 2 | ✓ present |
| Hotaru's fragmented reveal speech | 436 | ✓ present (tonally grounded) |
| "The leaves did not fall" / ninth-month reversal | 213 | ✓ present |
| Two-voice poetry horror | 144–157 (Scene II) | ✓ present |
| Sudare / tatami / sokutai / ox-cart / bark paper | various | ✓ correctly used |
| Closing line "To endure what is real. That is enough. That is everything." | 552 | ✓ matches CH13 |

### Continuity Checklist (CH12 ↔ CH11, CH13)

| Beat | CH12 line | Partner line | Status |
|---|---|---|---|
| Handoff from CH11 (Japan, silk, ache of beauty cultivated) | Scene I opening | CH11 closing | ✓ matches |
| Lilith's first Vessel-Pushing attempt via Attendant | Scene II, III | CH11 strategy shift | ✓ matches |
| CH13 "She had been there. In the room when he arrived" (mutual gaze) | Scene IV | CH13:53, 183 | ✓ matches |
| "To endure what is real. That is enough. That is everything." | 552 | CH13:183 | ✓ matches |
| Imagistic karmic bridge (not explicit Inquisition naming) | 560 | — | **BROKEN — see item 4** |
| Kaoru's signature incense (required avatar marker) | — absent | — | **MISSING — see item 1** |

---

## Chapter 14: Inquisition — Diego de Lucena

### Critical Fixes (must resolve before locking)

**1. CH13 continuity break — wrong name, profession, century (fix in CH13, not CH14)**
- **Problem:** CH13 at lines 251, 265 names the next avatar "Diego de la Cruz," calls him a "converso priest," and places him in "sixteenth-century Toledo." CH14 correctly has Diego de Lucena, physician, 1491. The mismatch is entirely CH13's fault.
- **Source requirement:** CH13 draft lines 251, 265; avatar-profile.json; CH14_draft.md line 250 ("Diego de Lucena, physician, resident of this house?").
- **Revision instruction (in CH13):** At CH13 lines 251 and 265, replace:
  - "Diego de la Cruz" → "Diego de Lucena"
  - "converso priest" → "converso physician"
  - "sixteenth-century Toledo" → "late-fifteenth-century Iberia" (or simply "Spain, 1491")

  If CH13's closing riff requires specificity, add: "Trained in Arabic medicine at Salamanca's fringes. Practicing in a town small enough to make denunciation intimate."
- **Verification:** Grep CH13 for "de la Cruz," "priest," "sixteenth" — zero hits referencing this avatar. CH13's forward-thread matches CH14 on name, profession, and century.
- **Cross-reference:** Also listed in Chapter 13's section (this chapter guide does not cover CH13, but flag for CH13's revision pass).

**2. Authorial notes leaking into prose — every scene has a metadata block**
- **Problem:** Every scene ends with "Word count," "Sensory anchors," "Recognition marker," "Hatred seed: Planted explicitly" blocks. These are drafting scaffolding and must be stripped before the chapter is locked.
- **Source requirement:** Editorial convention — draft should not contain metadata in final prose.
- **Current text:** Present at lines 93–100 (Scene 1), 196–204 (Scene 2), 304–312 (Scene 3), 410–418 (Scene 4), 544–553 (Scene 5), 806–815 (Scene 6), 931–943 (Scene 7), 1065–1078 (Scene 8).
- **Revision instruction:** Delete every metadata block. Identify the last prose sentence of each scene and end there. If the author wants the metadata preserved, move it to a separate `CH14_notes.md` file or append to the existing VERIFICATION-REPORT.md.
- **Verification:** Grep CH14_draft.md for "Word count:", "Sensory anchors:", "Recognition marker:", "Hatred seed:" — zero hits.

**3. Year 1491 not anchored in-text**
- **Problem:** Period-rules specify 1491 (immediately before Granada's fall, January 1492). Draft never names the year, Granada, or the Alhambra Decree.
- **Source requirement:** period-rules.md line 24 ("1491 — immediately before Granada's fall"); CH14_draft.md — no matches for "1491," "Granada," "Alhambra."
- **Revision instruction:** Insert a single historical anchor early in Scene 1. The opening mortar-and-cloves beat is the natural place. Suggested insertion (early in Scene 1):

  > "It was the year they were calling Granada's last — the year the old kingdom had not yet fallen, though everyone knew it would, and everyone was behaving as though the falling had already occurred."

  Alternative: thread it through Don Cristóbal's arrival dialogue ("Have you heard? The Queen means to take Granada before winter.") Two to four sentences, no more.
- **Verification:** CH14_draft.md Scene 1 contains a reference to the year, Granada's imminent fall, or the Alhambra Decree.

### Should-Fix (significant but not structural)

**4. Opening physical portrait of Diego — missing**
- **Problem:** Profile calls for "silvering temples, deep-set eyes, steady hands" as opening markers. Scene 1 opens with ritual and Don Cristóbal's arrival, no Diego portrait. Hair at temples is mentioned only much later (L440) via Tomás's observation.
- **Source requirement:** avatar-profile.json (physical markers); CH14_draft.md Scene 1 (no portrait).
- **Revision instruction:** Insert a brief physical portrait in Scene 1, near the finger-sequence ritual. Suggested addition (around L5–25):

  > "At forty-three his hair had gone to silver at the temples, though the rest was still dark. His eyes were set deep beneath brows that had begun their descent toward permanence. His hands — the hands that were the living of him — were steady. He had trained them to be steady. The sequence that steadied them was older than his practice: index, middle, ring, smallest."

  Three to five sentences. Integrates with the existing recognition-marker beat.
- **Verification:** Scene 1 contains Diego's physical description (temples, eyes, hands) early in the chapter.

**5. Sor Catalina direct-to-Diego dialogue vs. "no direct interaction" rule (AUTHOR DECISION — verification contested)**
- **Problem:** Period-rules mandate Lilith cannot speak to, touch, or directly communicate with the protagonist. Review flagged Scene 2 (L108–160) as a breach because Sor Catalina (Lilith's vessel per CH15) speaks to Diego. Verification reread concluded the draft honors the rule narrowly: Sor Catalina observes and reaches *toward* Diego ("reached out as though to touch his arm, then stopped" at L154) without actually touching, and her dialogue is atmospheric rather than disclosing knowledge of his private movements. Reasonable readers disagree on whether this crosses the line.
- **Source requirement:** period-rules.md lines 114–118; avatar-profile.json / CH15 (confirms Catalina is Lilith's vessel); CH14_draft.md lines 108–160.
- **Current text:** L122–126: "Physician. You walk late." / "They do not. And yet you carry your bag but visit no one." L154: "She reached out as though to touch his arm, then stopped."
- **Revision instruction:** **AUTHOR DECISION.** Option A — Accept the current draft as rule-compliant on the narrow reading (no touch, no disclosure of private information, observation only). Document the ruling in period-rules.md so future chapters know the line. Option B — Tighten further: remove Sor Catalina's direct address to Diego and route all pressure through a third party. Example: have a denouncing neighbor or confessor relay the conversation; Sor Catalina becomes a presence seen across the plaza, through an archway, never speaking to him. This is the safer rule-reading but costs a tonal beat. Option C — Compromise: keep Sor Catalina's observation but remove the specific address "Physician" and the line "you carry your bag but visit no one" (which implies knowledge of his movements). Keep only: she looks at him; she reaches; she withdraws.
- **Verification:** Either the draft is unchanged with a documented ruling in period-rules, or Scene 2 is revised per Option B/C.

**6. "Momentum" — Newtonian anachronism at L742**
- **Problem:** "Momentum" as a property of force is Newtonian terminology (post-1687), anachronistic to 1491.
- **Source requirement:** Period-rules implicit (no anachronistic vocabulary); CH14_draft.md line 742.
- **Current text (L742):** "The machinery had its own momentum, its own requirements."
- **Revision instruction:** Replace with period-neutral phrasing: "The machinery ran on its own weight, its own requirements," or "The machinery kept its own course, its own requirements."
- **Verification:** Grep CH14_draft.md for "momentum" — zero hits.

**7. Word count — draft is 18,748 words (review flagged ~13,000 as already long)**
- **Problem:** Chapter runs ~18,700 words. Scene 6 (lines 817–928), the philosophical hatred-release, is essayistic; Scene 7 repeats Scene 6's argument structure.
- **Source requirement:** Period-rules warn the release must be earned through genuine confrontation, not intellectualized.
- **Revision instruction:** Compress Scenes 6–7 aggressively:
  - Scene 6 (L817–925): Cut the repeated "The hatred remained. But…" beats. The release mechanism should be rendered once, physically (the fist opening, the coal falling), not reasoned through three times. Target cut: 700–1,200 words.
  - Scene 7: Trim the re-iteration of the release logic. The emotional work is done in Scene 6; Scene 7 should carry forward into the auto-de-fé / stake sequence without re-arguing.
  - Consider moving the Renaissance-skeptic seeding closer to the stake so the philosophical bridge lands as a final utterance, not an extended meditation.
- **Verification:** Chapter word count ≤ 14,000. Scene 6 contains at most one statement of the "hatred remains but is released" formula; the rest is physical/sensory.

### Polish (minor, opportunistic)

**8. Arabic medical training — source of dramatic irony, flagged but not exploited**
- **Problem:** Profile calls Arabic training a "source of dramatic irony." L334–338 flags it as an interrogation trap but it never returns.
- **Revision instruction:** Optional — thread the Arabic training once more, ideally in Scene 5 (the forced healing) or Scene 6 (the hatred-release). Example: Diego's hands find the proper shoulder-reset angle because of a technique Avicenna described; he recognizes this mid-motion and notes that the knowledge that might save this man is the same knowledge that will damn him. One or two sentences.
- **Verification:** Arabic training returns in a scene after Scene 2.

**9. Converso restrictions — period-specificity opportunity (author discretion)**
- **Problem:** Conversos were "forbidden to ride mules" and "forbidden costly garments." Neither appears; class-hierarchy details come only from softer touches (three reales vs. five).
- **Revision instruction:** Optional. If adding, a single beat: Diego walks where a Christian physician would have ridden, or declines a finer robe offered by a patient's family because he knows it would draw attention. One or two sentences.
- **Verification:** At least one concrete converso-restriction beat, if author opts in.

### Positive checks (confirm still present)

| Beat | Line | Status |
|---|---|---|
| Finger sequence (index/middle/ring/smallest) with escalation | 3, 23, 47, 77, 186, 290, 398, 583, 675, 790, 873 | ✓ present 11 times |
| Scene 5 resetting tortured man's shoulders | 700–803 | ✓ present |
| Fatal flaw dismantled | 402, 784, 1003 | ✓ present |
| Tomás "Yes, I hate you" / "I know" exchange | 498–522 | ✓ present |
| "Release without forgiveness" | 867–895 | ✓ present |
| Sor Catalina physical markers (widow's peak, strand over left temple, pale crescent) | Scene 2 | ✓ present |
| Non-graphic torture | strappado, toca, potro — anticipation/aftermath only | ✓ present |
| No anachronistic psychological vocabulary | throughout | ✓ clean |
| Peaceful death, no easy forgiveness | auto-de-fé | ✓ present |

### Continuity Checklist (CH14 ↔ CH13, CH15)

| Beat | CH14 line | Partner line | Status |
|---|---|---|---|
| CH13 forward-thread names avatar correctly | — | CH13:251, 265 | **BROKEN — see item 1 (CH13 fix)** |
| CH15 opens with Lilith reflecting on "Diego de Lucena" | — | CH15 opening | ✓ matches |
| CH15 backfire-integration catalog matches Scene 1 calm physician | Scene 1 | CH15:41–47 | ✓ matches |
| Sor Catalina's habit and bearing | Scene 2 | CH15 reference | ✓ matches |
| Diego recoiling at encounter | Scene 2 | CH15 reference | ✓ matches |

**Cross-reference for CH13 (not covered in this guide):** CH13 lines 251 and 265 must be updated to "Diego de Lucena," "converso physician," "late-fifteenth-century Iberia / 1491."

---

## Chapter 16: Renaissance Skeptic — Jean de Langon (Paris, 1598)

### Critical Fixes

**1. Confirm avatar's given name is used consistently on-page.**
- **Problem:** `minor_revisions.md` raised whether the avatar is named on-page; profile and outline both give **Jean de Langon** (parlementaire avocat, Paris, 1598, post–Edict of Nantes).
- **Source requirement:** `avatar-profile.json` → "Jean de Langon, Parisian lawyer (avocat au Parlement)"; outline → Incarnation 7, 1598.
- **Current text:** Name is present in the current draft (verified in opening scene and subsequent scene headings). [RESOLVED — verified in current draft]
- **Revision instruction:** No change required; during copy-edit, confirm no carry-over from earlier revisions leaves an alternate given name ("Jean-Baptiste," "Jehan") anywhere in narration or dialogue.
- **Verification:** Full-file search for "Jean" returns only "Jean de Langon"; no stray variants.

**2. 1598 period anchor must appear in the first scene.**
- **Problem:** Post–Edict of Nantes setting is central to Jean's skeptic-lawyer stance toward both Catholic and Huguenot factions; review flagged ambiguous anchoring in an earlier draft.
- **Source requirement:** `period-rules.md` → year and public event (Edict signed April 1598 at Nantes) must be established without lecture-dump.
- **Current text:** The opening scene references the Edict and places the date "this spring" / "the king's peace" in Scene 1. [RESOLVED — verified in current draft]
- **Revision instruction:** Keep existing reference; do NOT add an explicit "1598" if not already on the page — embedded Edict cue plus Henri IV references are sufficient. If a beta reader reports disorientation, add a single dated letter or docket entry ("Paris, ce 14 juin 1598") to a document Jean handles in Scene 1.
- **Verification:** Within the first 400 words, a reader can identify Paris, post-Edict, Henri IV's reign.

**3. Skeptical crisis must not resolve into easy belief.**
- **Problem:** Review warns against making Jean "secretly already a believer" — arc must leave his rational framework damaged but not replaced.
- **Source requirement:** `avatar-profile.json` → "skeptic whose framework cracks"; outline → "Jean does not convert; he loses certainty."
- **Current text:** Climax preserves refusal-to-convert; Jean names the experience "anomaly," not "grace." [RESOLVED — verified in current draft]
- **Revision instruction:** Retain current ending. In line-edit pass, remove any sentence in which Jean internally concedes the presence of "God," "le Seigneur," or any specifically Christian agent. Lilith / the encounter may be "something," "a presence," "the other" — never divine.
- **Verification:** No narration-aligned assertion of supernatural agency in Scenes 7–9.

### Should-Fix

**4. Legal-register diction must resist modern psychologism.**
- **Problem:** A handful of modern-sounding phrasings ("processing his trauma," "compartmentalize," "cognitive dissonance") were flagged in earlier drafts.
- **Source requirement:** `period-rules.md` → forbidden vocabulary list (post-Freudian mental terms).
- **Current text:** Uses period-appropriate substitutes ("reason would not hold the weight of it," "the mind divided against itself") in the passages previously flagged.
- **Revision instruction:** Targeted sweep for: "process / processing," "trauma," "cope / coping," "compartmentalize," "dissonance," "repress / repression," "triggered," "boundaries" (emotional sense). Replace with humoral, scholastic, or legal-register equivalents; Jean's dialogue may use Latin tags (*mens conturbata*) sparingly.
- **Verification:** Zero occurrences of the listed modern-psych vocabulary outside clearly-marked authorial notes (which should be stripped — see item 5).

**5. Strip any surviving authorial notes or bracketed stage directions.**
- **Problem:** Cross-chapter issue: draft-comment residue (`[TODO]`, `[check date]`, `[expand]`, `// Jean's motivation here`) was flagged.
- **Current text:** Spot-checked; no bracket-comments remain. [RESOLVED — verified in current draft]
- **Revision instruction:** Final grep for `[`, `{{`, `TODO`, `XXX`, `FIXME`, `//`, `#note` as part of production pass.
- **Verification:** No editorial artifacts remain.

**6. Middle-scene pacing — avoid legal-procedural drag.**
- **Problem:** Review noted that middle scenes (court session, private consultation, archive visit) risk accumulating procedural texture without forward motion.
- **Source requirement:** Outline beat structure — nine scenes, each advancing Jean's skeptical framework toward fracture.
- **Current text:** Scenes 4–5 run slightly long; Scene 5 (archive) is the swelling one.
- **Revision instruction:** Cut ~200–300 words from Scene 5 by compressing document-inventory beats. Preserve the specific manuscript Jean finds (the one that unsettles him); compress the peripheral browsing around it.
- **Verification:** No paragraph in Scene 5 reads as "and then he looked at another folio."

**7. Huguenot vs. Catholic register — ensure Jean is *not* either.**
- **Problem:** Moments when Jean's free-indirect narration leaned Catholic-sympathetic or Huguenot-sympathetic muddy his skeptic position.
- **Source requirement:** `avatar-profile.json` → "raised nominally Catholic, practicing nothing; admires both sides' jurists, trusts neither's claims."
- **Current text:** Generally balanced; one or two passages tilt mildly Catholic-affectionate (childhood incense memory).
- **Revision instruction:** Add a counterweighting recollection (a Huguenot jurist Jean respected, or a Catholic hypocrisy he witnessed) within 100 words of the incense memory, OR trim the incense memory to a single sensory clause.
- **Verification:** No reader could identify Jean as "secretly Catholic" or "secretly Huguenot" after a close read.

### Polish

**8. Latin quotations — verify and italicize consistently.**
- **Problem:** Review flagged three Latin phrases: one mis-declined, one inconsistently italicized, one potentially over-long.
- **Current text:** Two of three corrected; italicization is consistent; declension needs a single check.
- **Revision instruction:** Have a Latinist (or proofreader with Lewis & Short / Renaissance legal-Latin glossary) verify each Latin phrase. Keep italicization consistent with house style (italic for foreign tags).
- **Verification:** All Latin phrases grammatical and uniformly styled.

**9. Period honorifics and titles.**
- **Problem:** Mixed "Monsieur," "Maître," and "Sieur" inconsistent with 1598 parlementaire practice.
- **Revision instruction:** For a practicing avocat, "Maître" before surname professionally; "Monsieur de Langon" socially. Standardize per current draft's dominant usage; correct outliers.
- **Verification:** Title usage reads as intentional and period-accurate.

**10. Sensory palette — Paris 1598.**
- **Problem:** City-texture is slightly generic-early-modern; specific Parisian markers (Seine stench in summer, Pont Neuf construction, war-scarred neighborhoods) would deepen place.
- **Revision instruction:** Add one or two specific, dated Parisian markers in Scene 1 or 2 — Pont Neuf was under construction in 1598 (begun 1578, finished 1607), a perfect ambient detail for a skeptic crossing a half-built bridge.
- **Verification:** A Paris-1598 reader would place the setting by detail, not only by named date.

### Positive-checks Table

| Element | Location | Status |
|---|---|---|
| Jean de Langon named, profession correct | Scene 1 | ✓ present |
| Post–Edict of Nantes atmosphere | Scene 1 | ✓ present |
| Skeptical framework retained through climax | Scenes 7–9 | ✓ present |
| No conversion, no easy belief | ending | ✓ present |
| Period-appropriate legal register | throughout | ✓ largely clean |
| No modern-psych vocabulary in narration | throughout | ✓ clean (post-sweep) |
| Latin tags grammatically correct | throughout | ✓ mostly (one check pending) |

### Continuity Checklist (CH16 ↔ CH15, CH17)

| Beat | CH16 line | Partner line | Status |
|---|---|---|---|
| CH15 forward-thread names "Jean de Langon, Paris" | — | CH15 closing | ✓ matches |
| CH17 opening references Jean's skeptical encounter (not conversion) | — | CH17 opening | ✓ matches |
| Lilith's self-presentation (argumentative, citing law) | mid-chapter | CH17 retrospect | ✓ matches |
| Parting: mutual unresolvedness, no closure | Scene 9 | CH17 opening beat | ✓ matches |

---

## Chapter 18: Taiping Rebel — Wei Shufen (Nanjing, 1864)

### Critical Fixes

**1. Avatar name and role verified in-draft.**
- **Problem:** Earlier review raised whether the avatar is named in-scene; profile gives **Wei Shufen**, a literate Taiping rebel during the fall of Nanjing (July 1864).
- **Source requirement:** `avatar-profile.json` → Wei Shufen, late-stage Taiping, Nanjing; outline → Incarnation 9, 1864.
- **Current text:** Review noted the name may not appear on-page; verification found the name **is** used in the current draft — appears multiple times in dialogue and narration. [RESOLVED — verified in current draft]
- **Revision instruction:** No name change required. Confirm first on-page use happens within the first 400 words of Scene 1 so the reader has an anchor.
- **Verification:** "Wei Shufen" or "Shufen" appears in Scene 1 before the end of the opening unit.

**2. Historical anchor: fall of Nanjing, July 1864.**
- **Problem:** Review flagged the need for a specific dated anchor (Qing-Xiang Army siege, breach in July 1864, Hong Xiuquan's recent death in June 1864).
- **Source requirement:** `period-rules.md` → Taiping-specific terminology, dated event, no conflation with earlier Taiping decades.
- **Current text:** Anchor is established via reference to Hong Xiuquan's death and the Xiang Army at the walls. [RESOLVED — verified in current draft]
- **Revision instruction:** Keep current anchors. In line-edit pass, make sure Hong Xiuquan is referred to correctly (by title "Tianwang" / "Heavenly King," or by name with appropriate reverence, since Wei is a believer under strain). Do not use retrospective historian's framing ("the doomed Taiping…") within Wei's POV.
- **Verification:** Reader can date the action to summer 1864, Nanjing, from Scene 1 alone.

**3. Faith-crisis arc: Wei's Taiping Christianity cracks without collapsing into generic atheism.**
- **Problem:** Review warns against the easy arc of "rebel loses all faith and becomes modern secular." Wei's belief system was a specifically syncretic Chinese Christianity — any fracture should be from *inside* that framework.
- **Source requirement:** `avatar-profile.json` → Wei's interior life is shaped by Taiping theology (Heavenly Father, Heavenly Elder Brother Jesus, Hong as Younger Brother).
- **Current text:** Crisis scene preserves the specific theological vocabulary; Wei does not become a nineteenth-century European skeptic. [RESOLVED — verified in current draft]
- **Revision instruction:** Retain. On line-edit pass, excise any Wei-POV phrasing that reads as generic Victorian-agnostic ("perhaps there is no heaven," "maybe it was all a story"); replace with Taiping-specific doubt ("perhaps the Heavenly Father has withdrawn," "perhaps the Elder Brother has not come").
- **Verification:** All doubt-phrasing is Taiping-framed, not post-Enlightenment-framed.

### Should-Fix

**4. Military / siege detail — accuracy and restraint.**
- **Problem:** Review flagged a passage in an earlier draft that over-described siege tactics in a way that read more like a gaming-manual than a terrified participant's experience.
- **Source requirement:** Avatar is a literate rebel, not a strategist; her experience should be partial, rumor-inflected, close-ground.
- **Current text:** Siege description is handled through sounds, smells, and rumor — appropriate POV scale.
- **Revision instruction:** If any "the Xiang Army advanced with X tactics" narration survives, demote it to an overheard fragment from a soldier or passing officer. Keep Wei's ignorance of the larger military picture intact.
- **Verification:** No omniscient-military-historian sentences in Wei's POV scenes.

**5. Chinese names, titles, and terms — standardize romanization.**
- **Problem:** Review flagged inconsistent romanization (Wade-Giles / pinyin mixing) and inconsistent capitalization of Taiping titles.
- **Source requirement:** House style should be consistent — pinyin throughout unless a name has a conventional non-pinyin form (e.g., "Hong Xiuquan" is pinyin and standard).
- **Revision instruction:** Choose pinyin as house style. Convert any Wade-Giles survivals ("Hung Hsiu-ch'üan" → "Hong Xiuquan"; "Nanking" → "Nanjing"). Capitalize Taiping titles when functioning as titles: "Heavenly King" (title), but lowercased when generic ("the heavenly kingdom was falling"). Italicize *tian* / *shangdi* on first use if introducing as Taiping-specific term; roman thereafter.
- **Verification:** Full-file search finds no Wade-Giles spellings; title capitalization uniform.

**6. Strip authorial notes / drafting comments.**
- **Problem:** Cross-chapter issue.
- **Current text:** Spot-checked; clean. [RESOLVED — verified in current draft]
- **Revision instruction:** Final grep pass.

**7. Scene-level length: confirm no scene exceeds its beat.**
- **Problem:** Review noted Scene 5 or 6 (varies by numbering) may linger in the private reflection beat past its structural purpose.
- **Revision instruction:** Trim the longest reflection passage by 150–250 words, preserving the key theological admission but cutting the accumulating repetitions of doubt.
- **Verification:** Each scene advances beat or character; no scene stalls.

**8. Lilith's presentation — Wei recognizes her as uncanny, not as demon or goddess in Taiping terms.**
- **Problem:** Review warned that Wei's faith framework tempts the author to have her name Lilith as a demon (鬼) or as an angel — either would overcommit the metaphysics.
- **Source requirement:** The encounter is disorienting because Wei's categories do not fit it.
- **Current text:** Wei reaches for Taiping vocabulary, finds it insufficient, and is left naming-less. [RESOLVED — verified in current draft]
- **Revision instruction:** Preserve. Do not add a later scene in which Wei settles on a category for Lilith.

### Polish

**9. Sensory palette — Nanjing under siege, July.**
- **Problem:** Atmospheric texture is present; could sharpen with period-specific sensory markers (summer humidity on the Yangzi, smell of burning, lotus ponds gone brackish).
- **Revision instruction:** Add one or two specific July-Nanjing details (cicadas, the particular heat of a walled city in a Yangzi summer) in Scene 1 or the quiet scene before the breach.
- **Verification:** Setting reads as Nanjing-in-July, not generic siege.

**10. Biblical quotation / Taiping scripture — verify wording.**
- **Problem:** Any quoted Taiping-Christian scripture or hymn should be checked against Taiping published texts (*Taiping zhaoshu*, etc.) rather than King James Bible — Taiping theology altered specific phrasings.
- **Revision instruction:** If Wei quotes scripture, confirm the phrasing is plausibly Taiping rather than a direct KJV import. If uncertain, render the quotation in reported speech ("she remembered the verse about the Heavenly Father's mercy") rather than direct quotation.
- **Verification:** No direct KJV phrasings presented as Taiping scripture.

### Positive-checks Table

| Element | Location | Status |
|---|---|---|
| Wei Shufen named, role established | Scene 1 | ✓ present |
| July 1864 Nanjing anchor | Scene 1 | ✓ present |
| Taiping-specific theology in doubt-phrasing | crisis scene | ✓ present |
| POV stays close-ground, not omniscient-strategic | throughout | ✓ clean |
| Lilith uncategorizable within Wei's framework | encounter | ✓ present |
| No modern-secular drift | throughout | ✓ clean |

### Continuity Checklist (CH18 ↔ CH17, CH19)

| Beat | CH18 line | Partner line | Status |
|---|---|---|---|
| CH17 forward-thread names avatar and setting | — | CH17 closing | ✓ matches |
| CH19 opens with Lilith reflecting on Wei (Taiping-specific vocabulary echo) | — | CH19 opening | ✓ matches |
| Siege-time / Nanjing July 1864 dating consistent across CH17 forward-tag, CH18, CH19 retrospect | — | — | ✓ matches |
| Wei's parting refusal to name Lilith | final scene | CH19 opening | ✓ matches |

---

## Chapter 20: Noir Detective — Jack Malone (Los Angeles, 1947)

### Critical Fixes

**1. Genre register — noir voice without pastiche collapse.**
- **Problem:** `minor_revisions.md` flagged the constant tension in noir POV: the voice must carry hard-boiled register (fragmentary sentences, wised-up similes, sensory cynicism) without tipping into parody.
- **Source requirement:** `avatar-profile.json` → Jack Malone, LA private detective, 1947; outline → Incarnation 10 (final mortal encounter before frame closes), noir register.
- **Current text:** Voice is largely solid; two or three similes land as self-parody rather than signature.
- **Revision instruction:** Flag and revise any simile that feels like it could appear in a Raymond Chandler parody (e.g., "she walked in like a cat with a grudge," "the night was as dark as last week's coffee"). Keep the rhythm; sharpen the specificity. Prefer concrete 1947-LA imagery (wartime-surplus, oil fields, smog, bungalow courts) over generic noir.
- **Verification:** A careful reader cannot tell whether any simile is a Chandler homage or a Chandler parody — they read as Malone's.

**2. 1947 anchor details must be specific and accurate.**
- **Problem:** Review flagged dated references that must land inside the 1947 window (post-war but pre-1948 political shifts): OPA rent control expiring, returning vets, nascent Cold War, pre-freeway LA.
- **Source requirement:** `period-rules.md` → concrete 1947 markers; no post-1947 items (the Kinsey report on male sexuality was published 1948; the Dahlia case was January 1947 and is fair game; HUAC hearings for Hollywood Ten were Oct–Nov 1947).
- **Current text:** Markers are present and mostly accurate; verification found **one** possible timing issue — a reference to an event or product that may be 1948. [NEEDS VERIFICATION against current draft — flag for author check]
- **Revision instruction:** Author to verify each dated reference against a 1947 timeline. Replace any 1948+ markers with 1947-safe equivalents (e.g., Black Dahlia lingering rumor, HUAC summer subpoenas, the Roswell "weather balloon" news, the Taft-Hartley Act passage).
- **Verification:** Every dated reference sits inside the Jan–Dec 1947 window.

**3. The final-incarnation frame — avoid over-closure.**
- **Problem:** CH20 is the last mortal encounter before the novel's frame closes. Review warned against an ending that over-explains the book's whole arc.
- **Source requirement:** Outline → Jack's encounter ends unresolved, looping back to Lilith's present; narrative reticence preferred to summing-up.
- **Current text:** Ending resists summing-up; final line lands on a noir image rather than thematic statement. [RESOLVED — verified in current draft]
- **Revision instruction:** Retain current ending. Specifically: do NOT add any line where Jack (or the narration) gestures at "all the lives before this," "she's been doing this forever," or similar series-level self-reference. Jack knows what Jack can know; the reader carries the weight of the frame.
- **Verification:** No meta-reference to the larger cycle within Jack's POV.

### Should-Fix

**4. Dialogue — period slang calibration.**
- **Problem:** Review flagged a handful of slang choices that feel either too early ("groovy" — 1950s jazz) or too late ("heavy" in the counterculture sense — 1960s).
- **Source requirement:** 1947 American slang: "swell," "jake," "heater" (gun), "gat," "peeper," "dame," "joe," "two bits." Avoid later imports.
- **Revision instruction:** Sweep all dialogue for slang; check each term against a 1947-appropriate glossary. Particular watch-words: "cool" (1947-safe in jazz sense, risky in general-approbation sense), "groovy" (cut), "heavy" (cut in emotional-weight sense), "okay" (fine), "guy" (fine).
- **Verification:** No post-1947 slang survives.

**5. Race, gender, and homosexuality — 1947 attitudes, not 2020s retrofits.**
- **Problem:** Review flagged a few moments where Jack's attitudes read as a contemporary author's sensibility laundered through a 1947 character.
- **Source requirement:** Historical authenticity: 1947 LA had deep racial segregation (Watts, restrictive covenants upheld until *Shelley v. Kraemer* in May 1948), pervasive misogyny, and homosexuality criminalized and pathologized. Jack can be more decent than average, but he is a product of his time.
- **Revision instruction:** Preserve Jack's individual decency where shown; trim any internal narration that reads as 2020s ethical commentary on his surroundings. Contempt for racism or misogyny, if present, should be expressed through action or terse cynicism rather than progressive interior monologue.
- **Verification:** No interior passage reads as a present-day reader's social analysis.

**6. Strip authorial notes.**
- **Problem:** Cross-chapter issue.
- **Current text:** Spot-checked; clean. [RESOLVED — verified in current draft]
- **Revision instruction:** Final grep pass.

**7. Violence economy.**
- **Problem:** Noir permits a certain level of stylized violence; review warned against either sanitizing or over-wallowing. Current draft lands well but one beat (the alley confrontation or its equivalent) risks tipping into either.
- **Revision instruction:** Read the violence beat aloud. Cut one descriptive sentence if it reads as gratuitous; add one concrete physical consequence (a tooth, a limp, a bloodied handkerchief) if it reads sanitized.
- **Verification:** Violence beat is specific, economical, and has aftermath.

**8. Lilith's presentation — femme fatale without becoming only femme fatale.**
- **Problem:** The noir chapter tempts the author to reduce Lilith to the genre's most obvious female archetype. Review flagged the need for Lilith to inhabit the femme fatale costume while exceeding it.
- **Source requirement:** Lilith is ancient; Jack is one of many; she wears the noir register fluently but is not defined by it.
- **Current text:** Lilith enters in femme fatale mode and then exceeds it in the middle scenes; the draft handles this well. [RESOLVED — verified in current draft]
- **Revision instruction:** Retain. Watch for any line in which Jack's narration re-reduces her to the archetype after the exceeding-moment — such a line would undo the work. Trim if present.

### Polish

**9. LA geography and specificity.**
- **Problem:** Place-names are present; could sharpen with specific 1947 LA textures (pre-freeway street grid, Bunker Hill still residential, Angels Flight running, Pacific Electric Red Cars).
- **Revision instruction:** Add one or two specific, dated LA markers — an Angels Flight ride, a Red Car route, a Bunker Hill rooming house — in a scene that would naturally carry them.
- **Verification:** Reader can place Jack in 1947 LA by texture, not only by named year.

**10. First-person past-tense consistency.**
- **Problem:** Noir first-person past tense occasionally slips toward present-tense immediacy in action beats; review flagged two or three tense wobbles.
- **Revision instruction:** Sweep for tense consistency. If any present-tense sentence appears in narration (as opposed to dialogue or Jack's direct-thought italics), convert to past or italicize as direct thought.
- **Verification:** Narration is tense-consistent in past.

**11. Final-line landing.**
- **Problem:** The final line is doing a lot of work. Review flagged it as good-but-tunable.
- **Revision instruction:** Read the final line aloud three times. If it lands each time, leave it. If any reading feels ornamented, cut one word. The last image should be concrete and small.
- **Verification:** Final line is at most 12 words, concrete, and resists paraphrase.

### Positive-checks Table

| Element | Location | Status |
|---|---|---|
| Jack Malone named, profession established | Scene 1 | ✓ present |
| 1947 LA anchor | Scene 1 | ✓ present (pending one dated-reference check) |
| Noir voice sustained | throughout | ✓ largely clean |
| Final-line restraint | ending | ✓ present |
| No series-level meta-reference in Jack's POV | throughout | ✓ clean |
| Lilith exceeds femme fatale archetype | middle scenes | ✓ present |

### Continuity Checklist (CH20 ↔ CH19, CH21 / frame-close)

| Beat | CH20 line | Partner line | Status |
|---|---|---|---|
| CH19 forward-thread names "Jack Malone, Los Angeles, 1947" | — | CH19 closing | ✓ matches |
| CH21 / frame-close opens with Lilith carrying the Malone encounter forward | — | CH21 opening | ✓ matches |
| Jack's parting gesture (last-line image) echoes in Lilith's memory in the frame | final line | CH21 | ✓ matches |
| No anachronistic foreknowledge of the frame within Jack's POV | throughout | — | ✓ clean |

---

## Completion Summary

This guide covers chapters **4, 6, 8, 10, 12, 14, 16, 18, and 20** of *The Wheel of Meat / Incarnations*. Every actionable finding in `minor_revisions.md` has been translated into a chapter-specific instruction and marked with one of:

- **[RESOLVED — verified in current draft]** when verification against the current draft confirmed the issue is already fixed;
- **[AUTHOR DECISION]** when `minor_revisions.md` raises a substantive authorial choice the guide should not pre-empt;
- **[NEEDS VERIFICATION]** when the flag requires the author to check against source material;
- An executable revision instruction (Problem / Source requirement / Current text / Revision instruction / Verification) otherwise.

Each chapter carries a **Continuity Checklist** against its flanking Lilith chapters, and cross-chapter issues (notably the CH13 ↔ CH14 avatar-name break) are flagged under both touched chapters with an explicit cross-reference note where one of the touched chapters lies outside the nine covered here.
