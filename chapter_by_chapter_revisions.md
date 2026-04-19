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

**4. "Emperor" — period-rules violation (23 instances)**
- **Problem:** Period-rules mandate avoiding "emperor"; draft uses it 23 times.
- **Source requirement:** period-rules.md lines 64–65: "avoid 'king' (use 'raja' or describe), avoid 'emperor' (describe Ashoka's position)."
- **Current text:** Lines 1, 3, 11, 15, 19, 21, 31, 61, 119, 121, 147, 149, 157, 193, 207, 277, 317, 323, 417, 433, 491, 791, 957, 1019 all contain "emperor." Example line 1: "the emperor's edict."
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
- **Problem:** L31 has Alexios say "You hesitated with the tanner" — but the three morning patients shown at L23 are a boy with a gash, an old woman with aching joints, and a young man with a cough. A tanner appears only at L105, where Philon is organizing "the herbs and linen strips he had used on a tanner's infected foot" — a post-treatment recap that places the tanner later in the morning than Alexios's line. The patient list Alexios references at L31 does not include him.
- **Source requirement:** Internal continuity.
- **Current text:** L23: "By mid-morning, three patients had already come and gone. A boy with a deep gash on his forearm… An old woman whose joints ached… A young man with a cough…" L31: "'You hesitated with the tanner,' Alexios said quietly, during a lull between patients." L105: "Philon was repacking his satchel, organizing the herbs and linen strips he had used on a tanner's infected foot…"
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
| Philon's tragic flaw articulated (hunger to understand virtue) | 599–603 | ✓ present |
| "It was not virtue. It was fear wearing virtue's face" | 573 | ✓ present (appears at L573, not the closing line; chapter closes on "The hunger remained") |
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
| Bronze stylus compulsively cleaned / ritually handled | 11, 85, 135, 245, 325, 519, 745, 801 | ✓ present (L79 — "reached for his stylus" — is reach, not cleaning; actual cleaning motion begins at L85 "began cleaning the stylus, the motion automatic") |
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
- **Problem:** period-rules.md:155–160 forbids non-universally-recognizable Greek terms. Draft uses "kenosis" at three narration lines (with multiple instances packed into L785 — "had read about kenosis, had taught about kenosis, had written elegant explanations of kenosis") and "theosis" three times in narration (plus one acceptable use in Theophanes's dialogue at L337).
- **Source requirement:** period-rules.md lines 155–160; CH10_draft.md lines 785, 787, 813, 837, 899, 987 (narration).
- **Current text:** L785: "The fathers spoke of kenosis." L787: "He had never experienced kenosis." L813: "the holy emptiness of kenosis." L837: "more like dying than theosis." L899: "He did not know if this was theosis." L987: "more raw than theosis."
- **Revision instruction:** Replace every narration instance with period-appropriate English paraphrase. Suggested substitutions:

  | Current | Replace with |
  |---|---|
  | kenosis (narration) | "the emptying the fathers spoke of" / "the self-emptying" / "hollowing" / simply "emptiness" |
  | theosis (narration) | "the union the fathers named" / "the becoming-one-with-God" / "the union" |

  Preserve L337 "theosis — union with God" in Theophanes's spoken dialogue (character speech is acceptable; the character unpacks the term in the same breath).
- **Verification:** Grep CH10_draft.md for "kenosis" — only contexts that are clearly dialogue, if any. Grep for "theosis" — zero outside L337.

**3. Modern psychological vocabulary in narration — multiple instances**
- **Problem:** period-rules.md:159 proscribes modern psychological vocabulary. Draft uses "self-image," "structure," "self-filling" as if they were neutral terms.
- **Source requirement:** period-rules.md line 159 ("Avoid modern psychological vocabulary (e.g., 'trauma response,' 'ego dissolution'). Convey these through behavior and sensation").
- **Current text:**

  | Term | Lines | Current usage |
  |---|---|---|
  | self-image | 813, 855, 895 | "falling away of false self-image," "the ruins of his self-image" |
  | structure (psychological sense) | 27, 279, 281, 287, 465, 487, 691, 745, 767, 881, 891, 895, 945 | "structure of his pride," "structure never changed" |
  | self-filling | 789 | "a very sophisticated form of self-filling" |

  (Earlier revision notes listed "framework" at lines 484, 551, 807 — `grep -n framework CH10_draft.md` returns zero hits in the current draft; the term is not present.)
- **Revision instruction:** Convert each to concrete imagery in desert-appropriate register:

  | Current term | Replace with concrete image |
  |---|---|
  | false self-image | "the face he had shown himself in the dark" / "the reed-basket portrait" |
  | structure of his pride | "the ladder of his pride" / "the scaffolding he had built" |
  | the structure never changed | "the shape of the thing was unchanged" / "the vessel's wall, hidden, was the same" |
  | self-filling | "a filling with other things — reverence in place of respect, holiness in place of learning — but a filling all the same" |

  One use of "structure" in the chapter is arresting; thirteen uses is essayistic. Aim for no more than one instance total.
- **Verification:** Grep CH10_draft.md for "self-image" → zero narration hits; "structure" → at most one hit (ideally zero) in narration; "self-filling" → zero.

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

## Chapter 16: Renaissance Skeptic — Jean de Langon (Guyenne / Bordeaux, 1588)

> Setting correction: `avatar-profile.json` gives **death_year: 1588**, and the draft itself dates the action "On the roads of Guyenne in 1588" (line 51). The previous revision-guide entry wrongly placed Jean in Paris, 1598; all references below use the correct 1588 Guyenne setting.

### Critical Fixes (must resolve before locking)

**1. Missing Isabeau de Carcassonne at the ball (continuity setup for CH17's retrospect)**
- **Problem:** `avatar-profile.json` → `lilith_in_this_chapter.recognition_moment`, `period-rules.md` → "Isabeau de Carcassonne (Lilith's Past Incarnation — Peripheral)," and the outline's Scene 6 require Isabeau to appear peripherally at the ball with specific markers: pronounced widow's peak, single darker strand falling left, left-eye brown-with-pale-green crescent (11-to-1 o'clock), watchful stillness. Jean should glimpse her and feel a flicker of unnamed familiarity. No interaction. This is the first time Lilith's line and Silas's line co-locate historically; CH17 is supposed to retrospectively identify "one of my past lives was there but wisely did not engage." Without Isabeau on the ballroom floor, CH17's beat loses its referent.
- **Source requirement:** avatar-profile.json `recognition_moment`; period-rules.md Isabeau section; CH16 outline Scene 6.
- **Current text (CH16 draft):** Full-file grep for "Isabeau," "Carcassonne," "widow's peak," "pale-green," "darker strand" returns **zero matches**. The only "other woman" beat in Scene 6 is the yellow-silk noblewoman at line 521 — and that is functioning as the Diego (CH14) smoke/fire bleed-through, not as Isabeau. Marie de Gramont at lines 527–545 is a Catholic faction voice, not Isabeau. The canonical face is absent from the ball.
- **Revision instruction:** Insert a 20–40-word glimpse during Scene 6, ideally before the Marie de Gramont beat at line 527 — a natural slot is immediately after line 519 ("Jean moved toward the refreshment tables, seeking space to breathe and think.") Suggested insertion:

  > "Near a pillar at the far end of the hall stood a woman Jean did not know. Black hair parted over a pronounced widow's peak, a single darker strand falling across her left temple. She was watching him — not with the sidelong measurement of the Catholic matrons, nor the calculation of the Protestant wives. Simply watching. When his glance found hers, he caught a flicker of pale green at the edge of her left iris, like the ghost of a crescent moon. Something in him tugged toward recognition and found nothing. She did not approach. Jean looked away first."

  No interaction. No dialogue. No name. Three physical markers (widow's peak, darker strand left, pale-green crescent 11-to-1 o'clock) and watchful stillness.
- **Verification:** Grep CH16_draft.md for "widow's peak" — one hit, in Scene 6. The glimpse lasts ≤ 40 words. Isabeau is not named, does not speak, and does not reappear in the chapter. CH17's retrospective reference ("one of my past lives was there") now has a referent.

**2. Three-day / same-evening timeline contradiction in the coda**
- **Problem:** The draft's internal chronology cannot support the epilogue's "three days after submitting his report." Line 802: "Jean had perhaps a day before both factions moved against him." Line 820: "Jean left Bordeaux at dusk" — same day as the submission. Ambush follows that same evening (lines 828–905). Line 946 (epilogue): "Jean de Langon died on the road west of Bordeaux three days after submitting his report." Three days contradicts the narrative; the ambush happens hours after submission, not three days later.
- **Source requirement:** Internal consistency between Scenes 8, 9, and the coda.
- **Current text (line 946):** "Jean de Langon died on the road west of Bordeaux three days after submitting his report."
- **Revision instruction:** Either delete the clause (preferred — see item 3, which argues for cutting the coda entirely) or replace "three days after submitting his report" with "the evening of the day he submitted his report." Do not attempt to stretch the narrative to accommodate three days; the urgency ("perhaps a day" at line 802) is earning the ambush's immediacy.
- **Verification:** Grep CH16_draft.md for "three days after" — zero hits. The coda, if retained, matches the narrative's same-evening compression.

**3. Redundant third-person epilogue (lines 944–956)**
- **Problem:** The soul-transition sequence at lines 926–942 ("The wheel turned. / Consciousness pulled loose like thread from fabric…") already completes the chapter's karmic bridge and hands off to the next incarnation. The epilogue that follows ("His report was filed and forgotten. Henri de Ségur's murder remained unresolved. Guyenne tumbled into another year of uneasy peace…") re-states what is already thematically closed, introduces the "three days" contradiction (item 2), and dilutes the close the wheel-turn passage has earned.
- **Source requirement:** Voice guidance — death scenes should close on the karmic-bridge thought, not on narrator-voice recap.
- **Current text (lines 944–956):** The full epilogue paragraph, from "Jean de Langon died on the road west of Bordeaux three days after submitting his report" through "And the wheel would turn again."
- **Revision instruction:** Delete lines 944–956 entirely; let the chapter end at line 942 ("The wheel turned."). Alternative if the author wants the magistrate's banditry-finding preserved: reduce to a single line placed BEFORE "The wheel turned" at line 928 — e.g., "The magistrate's report would call it banditry. No alternative served order." Then resume the wheel-turn sequence. Do not trail after the wheel-turn with narrator commentary.
- **Verification:** Final line of CH16 is "The wheel turned," OR a single compressed banditry line precedes the wheel-turn. The factional-vindication commentary is gone.

### Should-Fix (significant but not structural)

**4. Word count overrun — 14,471 words vs. 8,000–9,000 target**
- **Problem:** Outline target is ~8,000–9,000 words across nine scenes. Current draft is **14,471 words** (verified by `wc -w`). The review flagged ~11,000–12,000 as already long; the current draft is further over. Bloat concentrates in Scenes 4, 7, 8, and in the finger-touch gesture's repetition.
- **Source requirement:** Outline target word count; voice-rule against intellectualized reiteration of resolved beats.
- **Current text (representative bloat sites):**
  - **Scene 4 (lines 249–341):** Marguerite's philosophical position is delivered fully.
  - **Scene 7 (lines 581–697):** Marguerite's argument is re-staged in almost the same structure before the breakthrough at 659.
  - **Scene 8 (lines 699–818):** the formal report is quoted as block text (visible at line 725 with "The testimony is irreconcilable…"), running close to a full page.
- **Revision instruction:** Target a 2,500–3,500-word cut to reach ~11,000 words (still over, but survivable). Approach:
  - Scene 4 — keep Marguerite's core Pyrrhonist move; cut ≥ 500 words of peripheral shop-texture and restated propositions.
  - Scene 7 — compress so the argument restatement lands in one tight exchange; the emotional hinge is the breakthrough at 659 ("You offer me a fortress"), not the philosophical ground preceding it. Target ≥ 800-word cut.
  - Scene 8 — condense the quoted report to two or three excerpted paragraphs surrounded by summary ("He drafted the section on the merchant's testimony. He drafted the section on the farmer's testimony…"). Target ≥ 600-word cut.
- **Verification:** `wc -w CH16_draft.md` ≤ 11,000. Scenes 4 and 7 no longer mirror each other's argument structure. Scene 8's report appears as excerpts, not full text.

**5. Finger-touch gesture — over 20 occurrences; thin to 6–8 inflection points**
- **Problem:** The finger-counting ritual is Jean's recognition marker and the chapter's central loaded gesture. Current draft deploys it ~20+ times. By mid-chapter it is mechanical; the reader registers repetition rather than weight. Thinning restores its load.
- **Source requirement:** Voice rules — loaded gestures carry meaning through restraint.
- **Current text (sampled occurrences):** Lines 5, 21, 67, 75, 103, 125, 157, 233, 247, 263, 305, 363, 379, 409, 443, 485, 565, 577, 635, 693, 746, 794, 808, 904 — twenty-four instances in the drafted file.
- **Revision instruction:** Retain the gesture at 6–8 inflection points. Suggested keepers: line 5 (first establishment), line 157 (the first sign of doubt), line 247 (fortress-shift), line 565 (recognition of gesture as performance), line 659 / 693 (breakthrough), line 794 (the steady testimony under ambush-threat), line 904 (death-beat). Delete or collapse the rest — especially the interview-tic instances at 75, 103, 125, 263, 305, 379, 409, 443, 485, 635.
- **Verification:** Grep CH16_draft.md for "touched his" — 6–8 hits, each tied to a structural beat, none in routine witness-interview rhythm.

**6. "Epistemological crisis" / "epistemological" — 19th-century coinage, anachronistic**
- **Problem:** "Epistemological" is a 19th-century coinage (borrowed into English c. 1856). A 1588 character cannot use it, and in the draft Marguerite (educated Pyrrhonist) deploys it at line 599, and Sorbin gestures at "epistemological complications" at line 491.
- **Source requirement:** Period-rules — no anachronistic vocabulary.
- **Current text:**
  - Line 599: `"I have read Montaigne. One recognizes the symptoms of epistemological crisis."`
  - Line 491: `"Though I suppose a man educated at the Collège de Guyenne would find epistemological complications where simpler minds see merely facts."`
- **Revision instruction:**
  - Line 599: Replace with period-appropriate phrasing such as "One recognizes the symptoms of a man who has stopped trusting his own instruments of knowing," or lean explicitly on Pyrrhonist diction: "One recognizes the Pyrrhonist's vertigo — the sickness of a mind that has doubted itself into stillness."
  - Line 491: Replace "epistemological complications" with "scholastic subtleties," "sophist's difficulties," or "philosophical complications."
- **Verification:** Grep CH16_draft.md for "epistemolog" — zero hits.

**7. "Narrative" used in modern media sense**
- **Problem:** "Narrative" in the modern rhetorical/media sense ("serving their faction's narrative") postdates the period. The word itself exists in 1588 Latin/French, but the rhetorical-strategy sense is 20th-century.
- **Source requirement:** Period-rules — avoid modern rhetorical vocabulary.
- **Current text (sampled):**
  - Line 133: "testimony that served neither faction's simple narrative"
  - Line 151: "his memory had helpfully filled in details that served his faction's narrative"
  - Line 541: "I do not discard findings because they complicate my narrative"
  - Line 559: "a case for Catholic conspiracy but needed more evidence… vindicate their narrative"
  - Line 750: "no attempt to protect either faction's narrative or his own reputation"
  - Line 840: "refused to serve either faction's narrative"
- **Revision instruction:** Replace "narrative" in every such instance with "account," "story," "version," or "report" as context allows. Rotate among them to avoid a single-word monoculture. Keep "narrative" only if used in its older sense of a chronological recital (rare in this draft).
- **Verification:** Grep CH16_draft.md for "narrative" — zero hits in rhetorical-strategy sense (incidental literal uses acceptable).

**8. "Performance of certainty" at line 567 — modern rhetorical sense**
- **Problem:** "Performance" in the sense of "putting on a display / act" is a 20th-century rhetorical usage (cf. Austin, performativity). In 1588, "performance" meant completion of a task or office.
- **Current text:** Actually at line 565 — "the gesture itself had become performance. The careful investigator weighing evidence. The neutral arbiter considering all sides." (Minor_revisions cites line 567 — the passage spans 565–567.)
- **Revision instruction:** Replace "had become performance" with "had become a display," "had become pretense," or "had become a show." Keep the three-part apposition that follows.
- **Verification:** Grep CH16_draft.md for "performance" — zero hits in rhetorical sense.

**9. "Professional armor" at line 297 — modern compound**
- **Problem:** "Armor" as metaphor is period-acceptable; the compound "professional armor" reads modern (the adjective "professional" in this modifier sense is largely post-1700).
- **Current text (line 297):** "The argument was seductive. Jean felt it slide beneath his professional armor like a blade testing for gaps."
- **Revision instruction:** Replace with "the guard of his profession," "his investigator's guard," or simply "his guard." Preferred: "Jean felt it slide beneath the guard of his profession like a blade testing for gaps."
- **Verification:** Grep CH16_draft.md for "professional armor" — zero hits.

**10. Marguerite's argument delivered twice (Scenes 4 and 7) — compress or differentiate**
- **Problem:** Scene 4 delivers Marguerite's Pyrrhonist position fully; Scene 7 restates the same argument structure before Jean's breakthrough at line 659 ("You offer me a fortress. The same fortress I have inhabited my entire career."). This is both item-4 bloat and structural redundancy — the breakthrough is blunted by the re-argued ground.
- **Source requirement:** Outline — Scene 7 is the temptation/breakthrough beat, not a re-argument.
- **Revision instruction:** Compress the Scene 7 argument to a single exchange in which Marguerite invokes the position already established in Scene 4 by reference ("You remember what I said in this same room"), then press immediately to the temptation. The breakthrough at 659 should land 400–600 words sooner. Alternative: differentiate — Scene 4's argument is abstract (Pyrrhonist epistemology); Scene 7's should be situational (what Jean specifically should DO with the letter). This re-casts Scene 7's content without re-arguing Scene 4's.
- **Verification:** Scene 7 no longer mirrors Scene 4's argument beats. Breakthrough at 659 lands with the weight of first recognition, not twelfth.

### Polish (minor, opportunistic)

**11. Scene 8's fully-quoted report — condense with excerpts at half the length**
- **Problem:** Scene 8 (lines 699–818) presents Jean's formal report in close to full text, starting at the block quotation around line 725 ("The testimony is irreconcilable. If the Catholic merchant's account is accurate…"). The quoted document works as character action — but at current length it is the single largest bloat site.
- **Source requirement:** Outline — the report functions, narratively, to show Jean committing truthful uncertainty to paper. A condensed version with two or three excerpted paragraphs achieves the same function.
- **Revision instruction:** Reduce the block quotation to 2–3 paragraphs interleaved with brief narrator passages describing what Jean wrote in the sections he does not quote. Preserve the signature moment where he names the four "Ifs" (see item 13) verbatim — that dialogue echo is load-bearing for CH17.
- **Verification:** Scene 8 word count at most half the current length. The four "Ifs" survive intact for CH17's retrospective.

**12. Past-life bleed-through cues — confirmed present, catalog for continuity**
- **Problem:** Review flagged two past-life bleed-through cues as present and restrained. Verification confirms both.
- **Current text:**
  - Line 53: "De Lacaze's hand briefly touched Jean's arm as he spoke — a gesture of personal concern born from eight years of shared work. Jean should have felt comfort in that familiar touch. Instead, a chill passed through him, quick and inexplicable. Old friends who shared confidences. Trusted bonds between men who knew each other's secrets. Something in his body flinched from the pattern, though his mind supplied no reason for the revulsion." — Judas-patterned touch (bleed-through from an earlier betrayal-life).
  - Line 521: "A noblewoman passed in a gown of deep yellow silk… For a moment he tasted smoke that was not present, felt heat against his face that the October evening did not explain… His body had recoiled as if from fire itself." — Smoke/fire bleed-through from Diego's burning (CH14).
- **Revision instruction:** [RESOLVED — verified: both bleed-through cues present and restrained]. No change required; catalog these two lines in a continuity note so later revision passes do not accidentally trim them.
- **Verification:** Lines 53 and 521 remain intact in the locked draft.

**13. CH17 dialogue echoes — verify each verbatim match**
- **Problem:** CH17's Lilith-POV references specific CH16 beats almost verbatim: "Nearly missed it," the four "Ifs," "You offer me a fortress," "I told the truth about what I didn't know." Continuity depends on each surviving the revision pass.
- **Current text (confirmed locations in CH16):**
  - "Nearly missed it" — line 377: "'Yesterday, while preparing the archives for your examination. It was misfiled among other correspondence.' Her voice was steady, her face composed. 'I nearly missed it.'" Jean's echo line 379: "*Nearly.* Jean touched his middle finger to his thumb."
  - Four "Ifs" — clustered at lines 433–439 ("If he included it…/ If he excluded it…/ If the letter was genuine…/ If the letter was forged…") and restated at lines 465, 669, 725. The canonical four appear at 433–439.
  - "You offer me a fortress" — line 659: "'No.' Jean shook his head. 'You offer me a fortress. The same fortress I have inhabited my entire career. The belief that uncertainty absolves me of responsibility for action.'"
  - "I told the truth about what I didn't know" — line 878: "'Tell him,' Jean said, and his voice was steady despite the blood soaking through his doublet, 'that I told the truth about what I didn't know. That was mine to give.'"
- **Revision instruction:** [RESOLVED — verified: all four dialogue anchors present at lines 377, 433–439, 659, 878]. Do not touch these lines in any subsequent revision pass; they are CH17's structural hooks.
- **Verification:** Grep CH16_draft.md for each phrase — one hit each at the documented line.

### Positive checks (confirm still present)

| Beat | Line | Status |
|---|---|---|
| Opening chamber scene establishes Jean, political trap, declined-purse beat | 1–67 | ✓ present |
| Lisette interview "you have carried this burden alone" | 114–145 | ✓ present |
| Six-rider ambush — ugly, survival-mode combat | 175–247 | ✓ present |
| Marguerite's Pyrrhonist position, not a straw man | Scene 4, Scene 7 | ✓ present (see items 4, 10) |
| Jean's breakthrough: truthfulness ≠ certainty | 651–671 | ✓ present |
| Ball scene present with rhetoric as fencing | Scene 6 | ✓ present (Isabeau missing — see item 1) |
| Formal report as character action | Scene 8 | ✓ present (bloated — see item 11) |
| Judas-patterned touch bleed-through | 53 | ✓ present |
| Yellow-silk / smoke / Diego bleed-through | 521 | ✓ present |
| Death-thought progression ending in karmic bridge | 876–942 | ✓ present |
| "What is worth dying for with conviction?" | 926 | ✓ present (CH18 seed) |

### Continuity Checklist (CH16 ↔ CH15, CH17)

| Beat | CH16 line | Partner line | Status |
|---|---|---|---|
| CH15 forward-thread names next avatar | — | CH15 closing | ✓ matches (verify name "Jean," Guyenne 1588) |
| "Nearly missed it" | 377, 379 | CH17 retrospect | ✓ matches |
| Four "Ifs" (letter genuine/forged × include/exclude) | 433–439 | CH17 retrospect | ✓ matches |
| "You offer me a fortress" | 659 | CH17 retrospect | ✓ matches |
| "I told the truth about what I didn't know" | 878 | CH17 retrospect | ✓ matches |
| Six-rider ambush, shoulder betrayal, horse going down | 828–905 | CH17 retrospect | ✓ matches |
| Isabeau glimpse at ball (peripheral, no interaction) | **missing** | CH17 retrospective reference to co-located past life | **BROKEN — see item 1** |
| Jean's final thought seeds CH18 Wei's conviction-hunger | 920–940 | CH18 opening state | ✓ matches |

---

## Chapter 18: Taiping Rebel — Wei Shufen (Nanjing / Tianjing, 1864)

### Critical Fixes (must resolve before locking)

**1. Opening lacks date, "1862 / Siege of Tianjing," physical portrait of Wei, and the outline's dawn-kneeling image**
- **Problem:** The draft opens in medias res with "Wei Shufen counted his supplies at dawn" (line 1) and lists yarrow, honey-garlic paste, and cloth bandages. It does not deliver the outline's required opening image ("Wei kneels beside a wounded soldier at dawn. Dust motes in slanted temple light. Herb-stained hands moving with practiced precision as he applies a poultice."), there is no dated anchor ("1862" / "1864" / "Siege of Tianjing" / "the third year of the siege" arrives only at line 69), and Wei's physical markers — long hair, red-faded-to-rust tunic with yellow trim torn off for bandages, herb-stained hands with surgical scars — are not established in prose. A reader arriving from CH17's Manchester/France oscillation has no sensory anchor.
- **Source requirement:** `ch18-outline.md` line 39 ("Wei kneels beside a wounded soldier at dawn. Dust motes in slanted temple light. His hands are herb-stained, moving with practiced precision as he applies a poultice."); `avatar-profile.json` physical-marker fields; `period-rules.md` dating requirements.
- **Current text (lines 1–7):** "Wei Shufen counted his supplies at dawn. / Three pouches of yarrow, nearly exhausted. One jar of honey-garlic paste, the last of the batch. Clean cloth enough for perhaps fifteen bandages, assuming he cut them thin. The arithmetic was always the same: not enough. Never enough. / Old Huang arrived as the light crept through the temple windows…"
- **Revision instruction:** Replace the opening paragraph with a version that delivers the outline's required image and folds in the physical portrait and the dating anchor. Suggested replacement (to become lines 1–4 of the revised draft):

  > "Wei Shufen knelt beside the wounded soldier at dawn. Dust motes turned in the slanted temple light where a Buddha had once sat before the Heavenly Kingdom's iconoclasts had hauled it down. His hands — herb-stained, the knuckles ridged with old surgical scars — moved across the poultice with the practiced economy of a medic who had changed this dressing four hundred times in two years. His tunic, red once and now the color of dried rust, hung loose at his shoulders; the yellow trim that had marked him as *lüshuai* of the West Ward was long since torn away for bandages. His hair, uncut by Taiping law, hung in a single plait down his back.
  >
  > Two years into the siege. Tianjing in the summer of the third year since the Xiang Army had closed its ring. The Heavenly King was dead — had died a month ago, on the first of June — though Wei still counted time from the ascension announcement, not from the body.
  >
  > He finished the dressing, sat back on his heels, and counted his supplies."

  Then resume the existing line 3's "Three pouches of yarrow…" Word count gain: ~140 words, easily absorbed given the draft's modest 8,734-word length. This single insertion resolves the opening-anchor, physical-portrait, and dated-anchor gaps at once.
- **Verification:** First four paragraphs of CH18 contain: (a) "knelt" / "dawn" / "dust motes" / "slanted temple light"; (b) physical markers (long hair, faded red tunic, yellow trim torn, herb-stained hands, surgical scars); (c) dating — Tianjing, third year of siege, Heavenly King's June death.

**2. Opening ledger number mismatch (48/23 vs. profile's 47/23)**
- **Problem:** `avatar-profile.json` specifies the ledger opens at 47 saved / 23 lost. The draft opens the ledger at line 47 with "Forty-eight saved. Twenty-three lost." Trivial but easy.
- **Source requirement:** avatar-profile.json `opening_state` field.
- **Current text (line 47):** "Wei added him to the count: *Forty-eight saved. Twenty-three lost.*"
- **Revision instruction:** The beat at line 45 shows Liu's fever breaking and being added to the count. If the profile's 47/23 is meant to be the state BEFORE Liu is added, change line 47 to "Forty-seven saved. Twenty-three lost." and adjust the surrounding sentences so Liu's count has not yet been added. Alternatively, change the profile to 47 + Liu = 48 and keep the draft. Author decision; trivial edit.
- **Verification:** Draft and profile agree on the opening ledger state.

**3. Narrator POV slips on Lilith at lines 163–164 and 219–221**
- **Problem:** Period-rules call for Lilith's hand to be visible to the reader only in CH19 — the pattern of her interference should register to the CH18 reader as ordinary war-misfortune, with recognition deferred. The draft breaks POV twice with omniscient narrator cues that name Lilith's intervention as intervention.
- **Source requirement:** `period-rules.md` → "Lilith never manifests or speaks to Wei; pattern visible to reader only in Ch19."
- **Current text:**
  - Lines 163–164: "And the pattern Wei had not yet noticed was beginning to take shape — the patients he saved dying in subsequent weeks, the coincidences that were not coincidences, the invisible hand tilting the ledger toward loss."
  - Lines 219–221: "Wei did not know that the intelligence leak had been no accident, that the raid's timing and route had been exposed by manipulation so subtle it looked like ordinary treachery. Did not know that eighteen deaths were being tallied in a ledger not his own, counted as successes in a war he could not see."
- **Revision instruction:** Two options.
  - **Option A (purist — preferred):** Delete both passages. The reader learns the pattern in CH19; CH18 should stay inside Wei's understanding. After cuts, line 163 flows from Huang's silence into "The night deepened." at 161; lines 219–221 are removable between 217 and 223 without continuity damage.
  - **Option B (lenient):** Shade to ambiguity. "the coincidences that refused to feel like coincidences" (no "invisible hand"); "the intelligence leak that the captains blamed on their own" (no "manipulation so subtle"). Preserves the rhythm while keeping agency off-page.
  - Author decision. The purist read is safer for the CH19 reveal; the lenient read preserves dramatic-irony texture.
- **Verification:** Grep CH18_draft.md for "invisible hand," "no accident," "manipulation so subtle" — zero hits (Option A) or softened phrasings (Option B). Wei's POV remains uncontaminated by the larger pattern.

### Should-Fix (significant but not structural)

**4. Underdeveloped hierarchy-as-corrosion: Wei's complicity in orders that send healed men to die**
- **Problem:** Profile and period-rules call for at least one scene in which Wei FOLLOWS a correct order with catastrophic results — his complicity in the moral corrosion of hierarchy, not just its aftermath. The raid scene at lines 181–203 delivers aftermath only ("They returned at dawn. Two of them."), and line 209's retrospection on "the twenty men he had released to die" points at the beat without rendering it.
- **Source requirement:** `period-rules.md` §2.1 "hierarchy as moral corrosion"; outline scene calling for Wei to certify healed soldiers for redeployment.
- **Current text (lines 181–203 + 209):** Aftermath-only rendering; the decision-point ("You are fit for duty. Report to the wall.") is off-page.
- **Revision instruction:** Add a short scene (~250–400 words) before line 181, in which Wei signs the fitness certifications that return twenty healed men to the West Wall. Render the bureaucratic act physically: the chop on the red-ink pad, the lüshuai seal pressed to the roster, a young soldier thanking him on the way out. Wei knows the wall cannot hold. He signs anyway because the rule is to sign. The raid's aftermath at 181 then lands with the weight of Wei's visible signature on each dead man. This is the chapter's cleanest hierarchy-corrosion beat and the outline's explicit ask.
- **Verification:** A scene exists, prior to line 181, in which Wei physically certifies the twenty soldiers and knowingly sends them to the wall.

**5. Mother's 1854 cholera death — never referenced in-text**
- **Problem:** Profile specifies Wei's mother died of cholera in 1854. The draft quotes her voice ("We can't save them all, Shufen. Only try." at line 429) but never establishes how or when she died. The Hakka / medical lineage is under-rendered.
- **Source requirement:** avatar-profile.json `backstory.mother` field.
- **Current text (line 429):** Mother's voice quoted without context.
- **Revision instruction:** Add a one-line memory adjacent to the mother's voice at line 429. Suggested: "She had said it the week before the cholera took her in 1854, the last summer before Wei carried her body to the pyre with the other ten from their Hakka village." One sentence; no backstory dump.
- **Verification:** The 1854 cholera death is named in-text within 50 words of the mother's voice.

**6. "Fifty hours" (line 509) vs. "third day" (lines 507, 513) arithmetic bobble**
- **Problem:** Line 507: "The child came on the third day." Line 509: "Wei had been sitting for fifty hours." Line 513: "The child entered at dawn." Fifty hours ≈ two days and two hours, not three days. In a chapter whose motif is arithmetic, this is a self-inflicted wound.
- **Source requirement:** Internal consistency; the ledger motif.
- **Current text:** As above.
- **Revision instruction:** Either change line 509 to "seventy-two hours" (truly the third day) or change lines 507, 513 to "the second day" / "The child came on the second day." Preferred: "seventy-two hours" — preserves the three-day / dawn image and sharpens the arithmetic.
- **Verification:** Fifty hours and "third day" no longer co-occur. The numbers match Wei's motif.

**7. Young Ping disappears at line 465 and is never accounted for**
- **Problem:** Young Ping is established as a working member of the West Ward station (lines 91, 361). At line 465 during the manna riot: "Young Ping had disappeared — fled, perhaps, or caught in the riot. It did not matter. The wounded kept coming." The character is then never referenced again. In a war-attrition chapter this is defensible, but it reads as dropped rather than chosen.
- **Source requirement:** Consequence-free loss violates the voice-rule that every dropped thread should feel chosen.
- **Revision instruction:** Two options. (a) Accept as intentional attrition; add a single later sentence confirming the fact to the reader — e.g., in Scene 8 Wei sees Young Ping's abandoned sandals in a corner and does not pick them up. (b) Complete the thread: in the death scene Wei sees Ping's body or receives word. The author should choose; current draft reads as dropped.
- **Verification:** Young Ping's fate is either explicitly confirmed once (option a) or closed in the death scene (option b).

**8. CH19 numerical handoff: recalculation after village-deaths news is implicit, not dramatized**
- **Problem:** CH19 line 79 implies Wei recalculates his ledger after the village-deaths news arrives. The daughter delivers that news in CH18 lines 267–283 ("Everyone died. The whole village."), but Wei's arithmetic correction is never made explicit in CH18's prose. CH19's "91 saved / 171 lost" recalculation (cited in the review) therefore lands without the triggering moment on the CH18 side.
- **Source requirement:** CH19 lines 79, 109 — numerical handoff.
- **Current text:** CH18 ends the daughter scene at line 315 without Wei re-counting; the ledger beat at line 417 rejects the ledger entirely rather than updating it.
- **Revision instruction:** Two options. (a) Add two or three sentences immediately after line 283 in which Wei subtracts the village from his running count — "The family of six. The two he had treated for dysentery the month before. All of them gone. He did not update the ledger. He did not need to. He knew the number had inverted." (b) Note the gap for CH19: if CH18 does not dramatize the recalculation, CH19's "recalculated" language should be softened to "understood." Author decision.
- **Verification:** Either CH18 contains a beat where Wei subtracts the village dead from his running count, or CH19's handoff language is adjusted. The two chapters agree numerically.

### Polish (minor, opportunistic)

**9. Jean's name surfaces as karmic thread at line 657**
- **Current text (line 657):** "Wei looked at him. Thought about Jean, about honesty. Thought about compassion. Chose both."
- **Revision instruction:** [RESOLVED — verified: karmic thread to CH16 explicit at line 657]. Do not trim in copy-edit.

**10. Old Huang as quiet mirror functions correctly**
- **Current text:** Huang appears at lines 5, 35–37, 153, 465, etc., as a quiet mirror who humanizes Wei without becoming co-protagonist.
- **Revision instruction:** [RESOLVED — verified: functional and restrained]. No change.

**11. Manna / Elder Zhou scene (lines 369–395) — theology-vs-body articulation**
- **Current text (line 373):** "'Lüshuai,' Zhou whispered. 'Why does the Heavenly Father allow this?'"
- **Revision instruction:** [RESOLVED — verified: cleanest theology-collapse beat in the chapter]. Preserve.

**12. Wounded-child breakthrough (lines 507–589) — matches CH19:245**
- **Current text (line 559):** "*It doesn't matter if I'm cursed,* Wei thought. *He needs help.*"
- **Revision instruction:** [RESOLVED — verified: breakthrough present; near-verbatim match to CH19:245 ("You're bleeding now. And I can stop that") per review]. Preserve; do not rephrase.

**13. Enemy sergeant's "I'm sorry" at line 715 — flag for author decision**
- **Problem:** Period-rules §10.1 specify "enemy soldiers not personalized." The sergeant's "I'm sorry" at line 715 humanizes him. The review notes this is defensible as honesty-under-violence but edges the rule.
- **Current text (line 715):** "'I'm sorry,' the sergeant said."
- **Revision instruction:** **AUTHOR DECISION.**
  - **Option A (purist):** Cut the line. The sergeant kills Wei in professional silence; the anonymity preserved by the rule.
  - **Option B (retain):** Keep. The line is a single beat and functions as the moment where Wei's doubt-without-bitterness extends to his killer — the last karmic action of the life. Document the exception in `period-rules.md` so the rule stays bright for future chapters.
  - **Option C (compromise):** Replace with silence or a gesture — the sergeant pauses, does not meet Wei's eyes, then strikes. Preserves the humanization without the dialogue.
- **Verification:** Author records the decision in `period-rules.md` if the line is retained.

### Positive checks (confirm still present)

| Beat | Line | Status |
|---|---|---|
| Wei's clinical honesty ("I don't know") | 15–23, 53–65, 377 | ✓ present |
| Ledger motif as through-line | throughout | ✓ present |
| Medical network / cooperation across ward stations | 5–7 | ✓ present |
| Manna as weeds / dysentery outbreak | 349–395 | ✓ present |
| Empty Buddha alcove habit (no prayer) | 315 | ✓ present |
| Sister Mei separation by Taiping segregation | 605–613 | ✓ present |
| Jean's name as karmic thread | 657 | ✓ present |
| Mother's voice ("We can't save them all, Shufen. Only try.") | 429 | ✓ present |
| Wounded-child adhiṭṭhāna breakthrough | 507–589 | ✓ present |
| "*I will try again*" — karmic bridge to CH20 | 753–763 | ✓ present |
| Tianjing named | 775 | ✓ present |
| No clean ending / no heroic last stand | final scenes | ✓ present |

### Continuity Checklist (CH18 ↔ CH17, CH19)

| Beat | CH18 line | Partner line | Status |
|---|---|---|---|
| CH17 forward-thread names Wei Shufen, Taiping | — | CH17 closing | ✓ matches |
| Jean's inherited question ("what can I die for with conviction?") lands in Wei's clinical-honesty opening | 15–23, 53–65 | CH17 closing | ✓ matches |
| "It doesn't matter if I'm cursed. He needs help" ↔ CH19:245 "You're bleeding now. And I can stop that" | 559 | CH19:245 | ✓ matches |
| 12-of-15 list Wei burns | 297–307 | CH19:107 | ✓ matches |
| Ledger numbers (133 saved / 128 lost) | — | CH19:109 | ✓ matches (per review) |
| Evacuation intercepted by "too-perfectly-timed" cavalry | 619–633 | CH19:283–289 | ✓ matches |
| Death scene + "I will try again" | 753–763 | CH19:311–319 | ✓ matches |
| Village-deaths arithmetic handoff | **implicit** (see item 8) | CH19:79 | **PARTIAL — see item 8** |
| Lilith never recognized by Wei | throughout | CH19 retrospect | ✓ (narrator POV slips — see item 3) |

---

## Chapter 20: Noir Detective — Jack Malone (Los Angeles, 1938)

> Setting correction: `avatar-profile.json` and `period-rules.md` place Malone in Los Angeles, **1938** — the Harry Raymond bombing (January 1938), the Kynette corruption recall, and the March 1938 LA Flood are all dramatized in the draft. The previous revision-guide entry wrongly placed Malone in 1947; all references below use the correct 1938 setting.

### Critical Fixes (must resolve before locking)

**1. Lilith's canonical face is too conspicuous — Malone sees too much**
- **Problem:** Period-rules specifically require: "He barely notices her — just a face that feels strangely familiar but he can't place." And: "No attraction, no relationship, no femme fatale dynamic." The draft inventories her signature markers three separate times, across distances and weather that make the green-crescent detail physically implausible (the crescent is specified "visible in good light" up close).
- **Source requirement:** `period-rules.md` Lilith carve-out; `avatar-profile.json` — Malone is "a face he cannot place, not one he tracks."
- **Current text:**
  - **Bar (lines 187–189):** "Her face was angled toward the window, but I could see the sharp line of her widow's peak, the single darker strand that fell across her forehead."
  - **Corner (lines 395–399):** "Dark hair caught in the wind, a coat that looked too expensive for this neighborhood, face turned slightly away from me. But there was something about the line of her profile — the sharp widow's peak, the single darker strand falling across her forehead — that made me stop." (Line 415 follow-up: "that widow's peak, that strange flicker in her left eye — lodged in my chest like a splinter.")
  - **Alley (line 831):** "This time, I could see her face clearly. The sharp widow's peak. The single darker strand that fell across her forehead despite the rain. Her eyes, fixed on mine across fifty feet of wet pavement — and in one of them, the left one, something strange. A flicker of color that didn't belong. Green, maybe, a pale crescent of green in an iris that should have been brown."
- **Revision instruction:**
  - **Bar (187–189):** Retain the widow's-peak + darker-strand detail; this is Malone's first sighting and may land as noticed-face. Cut any recognition-loaded interiority around it.
  - **Corner (395–399) and alley (831):** Strip the widow's peak and darker strand from Malone's perception at these distances. Keep his perception generic: "a dark-haired woman I'd seen somewhere before," "a woman on the corner, her coat too good for the neighborhood." Move the green-crescent detail entirely off-page from Malone — the reader carries it from the bar sighting; Malone does not re-inventory it in the rain.
  - Line 415 "that strange flicker in her left eye" — cut or soften to "that sense of having seen her before." The specific ocular detail is not Malone's to register at distance.
  - Line 831 alley: Remove the crescent-of-green line entirely. Replace the full-face close-up with a silhouette ("dark hair, a figure turning away"). The reader already knows who this is; Malone does not.
- **Verification:** Grep CH20_draft.md for "widow's peak" — one hit (bar only). "Darker strand" — one hit (bar only). "Crescent," "pale-green," "pale green" — zero hits in Malone-POV passages.

**2. "I'd never been to France" — hard contradiction with WWI backstory (lines 427–429)**
- **Problem:** Profile establishes Malone fought in France in WWI (Belleau Wood, Meuse-Argonne). At lines 427–429 he thinks "*In France—*" then blinks: "In France? I'd never been to France." This is a flat contradiction. Most likely a draft error in which the bleed-through moment was written without reference to Malone's WWI service.
- **Source requirement:** avatar-profile.json WWI backstory.
- **Current text (lines 427–429):** "*In France—* / I blinked. In France? I'd never been to France."
- **Revision instruction:** Recast the bleed-through so the confusion is about the WRONG France — a France Malone has never been to, even though he served in France in 1918. Suggested replacement:

  > "*In France—* / I blinked. The France I'd seen had been mud and shelling and a town whose name I couldn't remember — Belleau something. This was a different France. A stone cell. A rope. A voice I did not know speaking words I did not know. The image was gone before I could look at it."

  This honors the WWI service while routing the bleed-through into a prior life (Jean, Diego, or an unnamed earlier avatar). The contradiction is cut and the cue is sharpened.
- **Verification:** Grep CH20_draft.md for "never been to France" — zero hits. Belleau Wood or Meuse-Argonne referenced at least once in the chapter to ground the WWI backstory.

**3. Gloria Dane functions as a femme-fatale ghost-echo — reframe**
- **Problem:** Gloria Dane (lines 471–514) is a sequined-dress nightclub singer at The Velvet Room, rendered with sexual framing ("dark hair, full lips, a figure that the sequined dress she wore did nothing to hide"). She is aesthetically a femme-fatale ghost-echo in a chapter whose period-rules carve-out forbids the femme-fatale register attaching to the Lilith-adjacent material.
- **Source requirement:** `period-rules.md` — "No femme fatale subplot should exist."
- **Current text (line 471, 473, 497):** The Velvet Room, sequined dress, full lips, the calibration of a woman "women in her position had to play to survive."
- **Revision instruction:** Reframe Gloria to a less-coded role. Options:
  - A **bookkeeper's mistress** seen in a drab rooming-house parlor, not a nightclub. Preserves the blackmail-photograph dynamic; removes the sequined-dress aesthetic.
  - A **secretary** at the firm where Brennan launders the land-buys. Conversation happens in her apartment over tea, not over a stage band.
  - A **widowed sister** of one of Brennan's associates. Same information, no romantic framing.

  Cut the physical inventory ("full lips," "figure that the sequined dress did nothing to hide"). Preserve the plot function (her testimony about Brennan, the photographs). Target ≥ 200-word cut on the scene as a whole.
- **Verification:** No sequined dress, no full-lips / figure inventory, no nightclub stage. Gloria's function remains but the femme-fatale register is gone.

**4. Brennan / Brennan name collision**
- **Problem:** The chapter contains **two Brennans** with no acknowledgment. David Brennan at line 32 is the reformer from the Civic Reform Committee. Howard Brennan at line 487 is the blackmail-subplot businessman. A reader cannot be expected to track two Brennans without either a shared-family explanation or a rename. This is copyediting residue, not design.
- **Source requirement:** Clean character-name discipline.
- **Current text:**
  - Line 32: "'Mr. Malone?' The tall one extended his hand. 'Vernon Shaw. This is David Brennan.'"
  - Line 487: "'I know exactly what kind of girl you are, Miss Dane.' I kept my voice low, neutral. 'I know about Howard Brennan. I know about the photographs.'"
- **Revision instruction:** Rename one of them. Preferred: Howard Brennan → **Howard Brannigan** or **Howard Brenner**. The reformer David Brennan is named only once at line 32 and was going to appear again in notes Malone reviews; leaving him as Brennan preserves the Civic Reform roster without further editing. Sweep for every instance of "Howard Brennan" and "Brennan" (where context is the blackmail case) and replace.
- **Verification:** Grep CH20_draft.md for "Brennan" — all surviving hits refer to the reformer David Brennan. Grep for the new blackmail name returns only the blackmail-subplot hits.

### Should-Fix (significant but not structural)

**5. Lines 391, 601 — Malone's theorizing edges toward supernatural / distant operator**
- **Problem:** Profile insists the Combination plants the bomb and Malone dies believing the Combination did it. The draft has Malone theorize, twice, a non-Combination agent with impossible reach — which nudges the reader toward Lilith unwarrantedly and makes Malone look obtuse for not following through.
- **Source requirement:** avatar-profile.json — Malone stays inside Combination-paranoia.
- **Current text:**
  - Line 391: "The Combination was the obvious answer. They had the resources, the reach, the motivation. But the precision of it nagged at me. This wasn't the Combination's usual style — they preferred blunt force, intimidation, bullets and bombs. This was surgical. This was personal."
  - Line 601: "Someone was playing a game I didn't understand. Someone who had more power than the Combination, more reach than the police, more patience than any enemy I'd ever faced."
- **Revision instruction:**
  - Line 391: Soften from "This was surgical. This was personal" to "This was the Combination showing it had learned. This was the Combination adapting." Retain the "precision nagged at me" beat without converting it into a separate-operator theory.
  - Line 601: Replace with something that stays inside the Combination frame — "Someone who had bought more reach than I'd realized the Combination possessed. Someone inside it I hadn't mapped." Malone's paranoia intensifies about the Combination's extent, not about a non-Combination operator.
- **Verification:** Grep CH20_draft.md for "more power than the Combination," "more reach than the police," "more patience than any enemy" — zero hits. "Surgical" / "personal" applied to a non-Combination operator — zero hits.

**6. Missing CH21 handoff — no narrator-coda sentence locating Lilith's realization**
- **Problem:** CH21 opens with Lilith's horror at the completed perfections — her timeline compressing from "a week" to "NOW." The draft's omniscient coda at lines 951–971 supplies the wheel-turn and the karmic seed ("Someone has to give a damn. / I will try again") but does not plant Lilith's realization. The "woman was still there. Still watching" beat at 933 and the "receding" beat at 933 end Malone's perception of her; the coda never returns to her side. CH21's "I have to find him NOW" therefore lands as coincidence rather than cause.
- **Source requirement:** CH21 opening beat demands a visible trigger in CH20.
- **Current text (lines 957–961):** "And somewhere else — somewhere that had no name, no location, no existence in any geography the living could map — something stirred. / A momentum that had been building for millennia. A pattern that had been waiting for completion. Lifetimes of failure that were also preparation. Fires that had refined instead of destroyed. / And now, finally: the urge that would carry forward into the next life."
- **Revision instruction:** Insert one sentence in the coda that names Lilith's perception of what she has just witnessed. Suggested insertion between lines 955 and 957:

  > "On the far side of the rain, a woman stood on the sidewalk and understood, too late, what she had just watched complete. Ten lives. All ten. The pattern she had been chasing across the centuries had closed itself in front of her on a wet alley in a city she did not love."

  One sentence. No dialogue from her. Coda remains omniscient. CH21's compression now has a cause.
- **Verification:** The coda contains a named beat of Lilith's realization that all ten perfections are complete. CH21 opens with causal momentum, not coincidence.

### Polish (minor, opportunistic)

**7. Buick Roadmaster age (line 311) — pre-1936 impossibility**
- **Problem:** Line 311: "a three-year-old Roadmaster I'd bought cheap from a widow." The Roadmaster nameplate launched in 1936. A three-year-old Roadmaster in March 1938 would be a 1935 car — which predates the nameplate.
- **Source requirement:** `period-rules.md` — "Buick Roadmaster (1936+ model)."
- **Current text (line 311):** "I parked my Buick — a three-year-old Roadmaster I'd bought cheap from a widow who didn't need it anymore —"
- **Revision instruction:** Two options. (a) Change "three-year-old" to "two-year-old" (a 1936 Roadmaster in March 1938). (b) Change "three-year-old" to "couple of years old" — vague but safe. Preferred: **"two-year-old Roadmaster"** — matches the 1936 launch and preserves the "bought cheap from a widow" beat.
- **Verification:** Grep CH20_draft.md for "three-year-old" — zero hits on the Buick.

**8. Flood section (lines 615–645) is thin vs. period-rules' rich Great Flood detail**
- **Problem:** Period-rules give the March 1938 LA Flood rich sensory detail (Lankershim Bridge collapse, Pacific Electric Red Car washouts, 100+ dead, city dissolving, NG troops, mud and debris). The draft delivers this in three-plus paragraphs of mostly telling: "Hundred confirmed dead and rising. Thousands homeless. The movie studios had shut down." Lankershim is named (line 617), but the overall sensory expansion the period-rules call for is absent. Profile specifically calls this "perfect backdrop for climax."
- **Source requirement:** `period-rules.md` Great Flood section.
- **Current text (lines 615–645):** Three-plus paragraphs of news-summary register; one paragraph (lines 631–633) delivers walking-through-mud sensory detail.
- **Revision instruction:** Add one sensory paragraph (~150–250 words) between lines 629 and 631. Ground-level: mud on shoe-tops; a streetcar on its side at Pacific Electric's washout; a mattress caught in a tree; National Guard cordons; the smell the review names but the draft euphemizes ("something sweet and wrong I didn't want to identify" — name it: bodies). Keep the news-summary at 621–623 shorter; lean the weight of the section onto ground-level sensory.
- **Verification:** Flood section contains at least one Red Car / Pacific Electric detail, at least one ground-level body / mattress / tree-caught-debris image, and the NG troops physically on the street, not only on the radio.

**9. No Clifton's Cafeteria visit despite profile's named habit**
- **Problem:** Profile names Clifton's specifically ("Eats at Clifton's"). Clifton's Brookdale at 648 S. Broadway was one of the defining 1930s LA locations — fantasy-forest decor, pay-what-you-can policy, redwood-grove atmosphere. Not a single visit in the draft.
- **Source requirement:** avatar-profile.json habits.
- **Revision instruction:** Add a short scene or paragraph in which Malone eats at Clifton's between cases — the pay-what-you-can tray, the redwood-grove dining room, the painted waterfall. A single paragraph (~100 words) in the middle of the chapter (near lines 207 or 517) suffices.
- **Verification:** Grep CH20_draft.md for "Clifton" — one hit, anchored in the fantasy-forest decor.

**10. "Someone has to give a damn" — repeated seven times, thin to four or five**
- **Problem:** The phrase is the chapter's spine and is meant to recur. Seven occurrences starts to read as stamp rather than refrain.
- **Current text:** Grep confirms exactly seven hits — lines 433, 689, 731, 763, 793, 803, 963.
- **Revision instruction:** Keep the opening use (L433, woman-on-the-corner aftermath), one flood-aftermath use (L689 or L731), one pre-death use (L793 or L803), and the karmic-bridge use (L963). Replace two of the tighter repetitions (L731 or L689; L803 or L793) with closely-adjacent variants: "Someone had to bother," "Someone had to look," "Someone had to name it." Preserve the spine; lose the stamp.
- **Verification:** Grep CH20_draft.md for "Someone has to give a damn" — 4–5 hits, each at an inflection point. No two consecutive uses within 300 words of each other.

**11. Word count ~13,833 vs. 8,000–11,000 target — cut from blackmail-case middle**
- **Problem:** `wc -w CH20_draft.md` returns 13,833 words. Profile target is 8,000–11,000. The blackmail-case middle (Jerry Novak / blackmail-subplot arc, lines 471–611) is the largest cut-able block without touching the corruption spine or the death sequence.
- **Source requirement:** avatar-profile.json target word count.
- **Revision instruction:** Compress lines 471–611 by ≥ 1,500 words. Keep Gloria's scene (reframed per item 3), Brennan's insider-land-purchase discovery, and the blackmailer's death (Jerry Novak). Cut redundant Malone-interior passages about "why so much trouble for a ten-thousand-dollar blackmail," the double-backtrack to the Hall of Records, and the callbacks to Helen Marsh that merely re-establish her weight.
- **Verification:** `wc -w CH20_draft.md` ≤ 11,000. The blackmail-case middle no longer sprawls into the corruption-case spine.

**12. No Shadow on the radio, no pulp magazines, no recurring Angels Flight — habits underused**
- **Problem:** Profile names these habits explicitly. Angels Flight appears at lines 19 and 759 (good — twice). The Shadow on the radio and pulp magazines do not appear at all.
- **Revision instruction:** Two small additions. (a) A single line in a solo scene (Malone at home, lines 621–625 during the flood): "The radio gave me the news, then The Shadow at eight, then more news. I stayed up for the serial and slept through the rest." (b) A pulp magazine on his desk or nightstand — "a month-old *Black Mask* I'd been reading since Tuesday." Each is one line. Neither disrupts scene pacing.
- **Verification:** The Shadow and a pulp title each named at least once.

**13. Past-life bleed-through cues — catalog and assess**
- **Current text:**
  - Line 4: "I tasted something that wasn't whiskey: dust, blood, the smell of bodies too close together." — rally crowd flashback, bleed-through from an earlier crowd-life (Wei's Nanjing? Verinus's Rome? Ambiguous by design).
  - Line 51: "For a moment the office smelled wrong: dust and incense and too many bodies packed into a space meant for prayer, voices raised in unison promising heaven while the ground turned to mud and blood." — Taiping / Wei bleed-through, strongly marked ("heaven," "prayer," "mud and blood").
  - Line 417: "*I've seen those eyes before.* I couldn't say where. But I knew not to trust them." — recognition-adjacent; too overt for pre-death placement.
  - Line 427–429: "*In France—* / I blinked. In France? I'd never been to France." — addressed under item 2.
- **Revision instruction:**
  - Lines 4 and 51: [RESOLVED — verified: appropriate bleed-through register, restrained].
  - Line 417 ("I've seen those eyes before"): soften or relocate. At line 417 Malone is pre-death by several scenes; this overt recognition should be pushed into the death sequence (near line 925 or 933 where the woman is "still there. Still watching"). Replace the line 417 beat with something vaguer: "Something about her pulled at me in a way I didn't know how to name. Not attraction. Not memory. Something older." The explicit eye-recognition lands in the death sequence where it belongs.
  - Line 427–429: fix per item 2.
- **Verification:** Line 4, line 51, line 427–429 all survive (427 reshaped). Line 417 no longer contains "I've seen those eyes before"; the eye-recognition beat appears instead inside the death sequence.

**14. CH01 flashback match — "A passerby, rushing to avoid" [RESOLVED — verified in current draft]**
- **Problem:** CH01's opening flashback references Malone's death scene. Review cited CH01:9 as the verbatim anchor; CH20:839 delivers "A passerby, rushing to avoid." and CH20:935 delivers "A passerby. A witness. Nothing more."
- **Source requirement:** CH01 Manchester-opening flashback.
- **Current text (verified):**
  - CH20:839 — "A passerby, rushing to avoid."
  - CH20:935 — "A passerby. A witness. Nothing more."
  - CH01_draft.md:161 — "He shuddered as he recognized those eyes, in another place. Another rainy night, a different city, a passerby. Lilith, but not Lilith, rushing to avoid an antique car. The car was a brand new Buick Roadmaster." The verbal match holds; Silas's flashback references the passerby/rushing-to-avoid beat directly. The review's line reference (CH01:9) was approximate — the actual anchor is at CH01:161, deeper in the chapter after Silas's present-day orientation.
- **Revision instruction:** [RESOLVED] No change required. Three-way alignment verified: CH20:839 "rushing to avoid" → CH01:161 "a passerby. Lilith, but not Lilith, rushing to avoid an antique car"; CH20:935 "A passerby. A witness. Nothing more." supports the same cross-chapter reference. The Buick Roadmaster detail at CH01:161 also confirms CH20's death-scene vehicle (see item 7).
- **Verification:** Catalog CH01:161 in the continuity-tracking doc so future revision passes do not accidentally alter either anchor.

**15. SRO geography on Bunker Hill — check internal consistency**
- **Problem:** Profile establishes Malone's residence as an SRO on Bunker Hill with a Murphy bed, shared bathroom down the hall, alley parking, and stair access. Draft delivers Murphy bed (line 2), thin walls / neighbor coughing (line 2), alley parking (line 311), stair access (line 311). Shared bath not mentioned.
- **Revision instruction:** Add a single concrete reference to the shared bath — a scene in which Malone brushes his teeth at a hall basin, or waits for the door, or hears Mrs. Kowalski cough through the bathroom wall. One sentence in an existing scene suffices.
- **Verification:** Shared bathroom named at least once.

**16. CH19 "tracking" language vs. CH20's observational presence**
- **Problem:** CH19 states Lilith needs "the data from Jack Malone's tracking" before approaching Silas. CH20 shows three observational sightings (bar, corner, alley) but no tracking signal on Malone's side.
- **Source requirement:** CH19 line indicating tracking (per review).
- **Revision instruction:** **AUTHOR DECISION.**
  - **Option A:** Add a tracking signal on CH20's side — e.g., a single beat where Malone finds a cigarette butt outside his office that he doesn't smoke, or a shadow across the alley wall at 3 AM. One small cue; ambiguous to Malone, legible to the reader after CH19 retrospect.
  - **Option B:** Retune CH19's language — drop "tracking" and substitute "watching" or "observing." CH20's observational presence then matches.
  - Preferred: Option B, since CH20's three sightings are already the maximum Lilith-presence the period-rules allow; adding more cuts into item 1's restraint budget.
- **Verification:** Either CH20 contains a single observational cue Malone registers without understanding, or CH19's language is softened to match.

### Positive checks (confirm still present)

| Beat | Line | Status |
|---|---|---|
| Opening hangover / failed Helen Marsh case / Peterson client / twelve dollars / rent due | 2–12 | ✓ present |
| First-person Malone voice, economical, metaphor-driven | throughout | ✓ present |
| Three-act descent (hook with rot → layers of complicity → truth without justice) | throughout | ✓ present |
| Viriya lesson: "The trying was not nothing" | 939, 943 | ✓ present |
| Death-scene mechanics: Buick Roadmaster, alley, rain, starter-triggered bomb, extended bleed-out | 813–947 | ✓ present (Roadmaster age — see item 7) |
| Lilith as minimal presence (bar, corner, passerby) | 187, 395, 831 | ✓ present (over-specified — see item 1) |
| Harry Raymond car bomb / Captain Kynette corruption | 47 | ✓ present |
| March 1938 LA Flood | 615–645 | ✓ present (thin — see item 8) |
| "I will try again" karmic bridge to CH21 | 965 | ✓ present |

### Continuity Checklist (CH20 ↔ CH19, CH21, CH01)

| Beat | CH20 line | Partner line | Status |
|---|---|---|---|
| CH19 forward-thread names "Jack Malone, Los Angeles, 1938" | — | CH19 closing | ✓ matches (verify year 1938) |
| CH19 "tracking" language vs. CH20's observational presence | throughout | CH19 | **PARTIAL — see item 16** |
| CH21 opening "I have to find him NOW" causally triggered by CH20 coda | 957–961 | CH21 opening | **BROKEN — see item 6** |
| CH21 / frame-close reference to the Malone death | 947 | CH21 | ✓ (pending coda fix) |
| CH01 flashback match: "A passerby, rushing to avoid" | 839, 935 | CH01 antique-car flashback | **NEEDS VERIFICATION — see item 14** |
| Wei's "I will try again" karmic bridge lands in Malone's opening hunger to matter | opening | CH18:753–763 | ✓ matches |
| WWI / France backstory consistent | 427–429 | — | **BROKEN — see item 2** |
| Two-Brennan name collision | 32, 487 | — | **BROKEN — see item 4** |
| Lilith's canonical face visible to reader through repetition, not Malone's forensic inventory | 187, 395, 831 | — | **BROKEN — see item 1** |

---

## Completion Summary

This guide covers chapters **4, 6, 8, 10, 12, 14, 16, 18, and 20** of *The Wheel of Meat / Incarnations*. Every actionable finding in `minor_revisions.md` has been translated into a chapter-specific instruction and marked with one of:

- **[RESOLVED — verified in current draft]** when verification against the current draft confirmed the issue is already fixed;
- **[AUTHOR DECISION]** when `minor_revisions.md` raises a substantive authorial choice the guide should not pre-empt;
- **[NEEDS VERIFICATION]** when the flag requires the author to check against source material;
- An executable revision instruction (Problem / Source requirement / Current text / Revision instruction / Verification) otherwise.

Each chapter carries a **Continuity Checklist** against its flanking Lilith chapters, and cross-chapter issues (notably the CH13 ↔ CH14 avatar-name break) are flagged under both touched chapters with an explicit cross-reference note where one of the touched chapters lies outside the nine covered here.
