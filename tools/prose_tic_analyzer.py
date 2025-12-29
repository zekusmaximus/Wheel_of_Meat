#!/usr/bin/env python3
"""
Prose Tic Analyzer for The Wheel of Meat
=========================================
Identifies and proposes revisions for common prose tics:
1. "The particular [noun]" - overuse of "particular" as intensifier
2. Vague "something" constructions
3. Em-dash interruptions (>2 per paragraph)
4. Abstract nouns performing physical actions
5. "Not X" repetition structures

Generates detailed revision proposals with line numbers and context.
"""

import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

# ============================================================================
# CONFIGURATION
# ============================================================================

BASE_DIR = Path(__file__).parent.parent.resolve()
CHAPTERS_DIR = BASE_DIR / "incarnations"
OUTPUT_DIR = BASE_DIR / "out" / "prose_tic_analysis"

# Chapter metadata
CHAPTERS = [
    (1, "ch01-contemporary-manchester", "The Awakening"),
    (2, "ch02-prehistoric-ka", "The First Flame"),
    (3, "ch03-lilith-cp01", "Lilith's Watch I"),
    (4, "ch04-mauryan-chandra", "The Mauryan Empire"),
    (5, "ch05-lilith-cp02", "Lilith's Watch II"),
    (6, "ch06-athens-philosopher", "The Philosopher"),
    (7, "ch07-lilith-cp03", "Lilith's Watch III"),
    (8, "ch08-rome-investigator", "The Investigator"),
    (9, "ch09-lilith-cp04", "Lilith's Watch IV"),
    (10, "ch10-egypt-hermit", "The Desert Hermit"),
    (11, "ch11-lilith-cp05", "Lilith's Watch V"),
    (12, "ch12-heian-lover", "The Lover"),
    (13, "ch13-lilith-cp06", "Lilith's Watch VI"),
    (14, "ch14-inquisition-accused", "The Accused"),
    (15, "ch15-lilith-cp07", "Lilith's Watch VII"),
    (16, "ch16-renaissance-skeptic", "The Skeptic"),
    (17, "ch17-lilith-cp08", "Lilith's Watch VIII"),
    (18, "ch18-taiping-rebel", "The Rebel"),
    (19, "ch19-lilith-cp09", "Lilith's Watch IX"),
    (20, "ch20-noir-detective", "The Detective"),
    (21, "ch21-lilith-cp10", "Lilith's Watch X"),
    (22, "ch22-contemporary-breakthrough", "The Breakthrough"),
    (23, "ch23-deva-celestial", "The Celestial Realm"),
    (24, "ch24-future-prophet", "The Prophet"),
    (25, "ch25-space-explorer", "The Explorer"),
    (26, "ch26-pure-abodes-awakened", "The Awakened"),
]

# ============================================================================
# PATTERN DEFINITIONS
# ============================================================================

# Abstract nouns that often perform physical actions (problematically)
ABSTRACT_NOUNS = {
    'certainty', 'fear', 'recognition', 'awareness', 'understanding',
    'realization', 'knowledge', 'thought', 'feeling', 'emotion',
    'memory', 'doubt', 'confusion', 'clarity', 'truth', 'insight',
    'consciousness', 'comprehension', 'perception', 'sensation',
    'anxiety', 'dread', 'hope', 'despair', 'grief', 'joy',
    'terror', 'panic', 'relief', 'shame', 'guilt', 'pride',
    'anger', 'rage', 'calm', 'peace', 'tension', 'pressure'
}

# Physical verbs that abstract nouns shouldn't typically perform
PHYSICAL_VERBS = {
    'dissolved', 'dissolve', 'dissolves', 'dissolving',
    'moved', 'move', 'moves', 'moving',
    'settled', 'settle', 'settles', 'settling',
    'grew', 'grow', 'grows', 'growing',
    'spread', 'spreads', 'spreading',
    'crystallized', 'crystallize', 'crystallizes', 'crystallizing',
    'shattered', 'shatter', 'shatters', 'shattering',
    'broke', 'break', 'breaks', 'breaking',
    'crumbled', 'crumble', 'crumbles', 'crumbling',
    'swept', 'sweep', 'sweeps', 'sweeping',
    'washed', 'wash', 'washes', 'washing',
    'crashed', 'crash', 'crashes', 'crashing',
    'rushed', 'rush', 'rushes', 'rushing',
    'flooded', 'flood', 'floods', 'flooding',
    'spilled', 'spill', 'spills', 'spilling',
    'poured', 'pour', 'pours', 'pouring'
}

# ============================================================================
# TIC DETECTION CLASSES
# ============================================================================

class TicInstance:
    """Represents a single instance of a prose tic."""
    def __init__(self, tic_type: str, line_num: int, line_text: str,
                 matched_text: str, context_before: str = "", context_after: str = ""):
        self.tic_type = tic_type
        self.line_num = line_num
        self.line_text = line_text
        self.matched_text = matched_text
        self.context_before = context_before
        self.context_after = context_after
        self.proposals = []

    def add_proposal(self, original: str, revision: str, explanation: str = ""):
        """Add a revision proposal for this tic."""
        self.proposals.append({
            'original': original,
            'revision': revision,
            'explanation': explanation
        })

    def to_dict(self) -> dict:
        return {
            'tic_type': self.tic_type,
            'line_num': self.line_num,
            'line_text': self.line_text,
            'matched_text': self.matched_text,
            'context_before': self.context_before,
            'context_after': self.context_after,
            'proposals': self.proposals
        }


class ChapterAnalysis:
    """Analysis results for a single chapter."""
    def __init__(self, chapter_num: int, title: str, file_path: Path):
        self.chapter_num = chapter_num
        self.title = title
        self.file_path = file_path
        self.word_count = 0
        self.tics = []
        self.tic_counts = defaultdict(int)

    def add_tic(self, tic: TicInstance):
        self.tics.append(tic)
        self.tic_counts[tic.tic_type] += 1

    def total_tics(self) -> int:
        return len(self.tics)

    def tic_density(self) -> float:
        """Tics per 1000 words."""
        if self.word_count == 0:
            return 0.0
        return (self.total_tics() / self.word_count) * 1000

    def to_dict(self) -> dict:
        return {
            'chapter_num': self.chapter_num,
            'title': self.title,
            'file_path': str(self.file_path),
            'word_count': self.word_count,
            'total_tics': self.total_tics(),
            'tic_density': round(self.tic_density(), 2),
            'tic_counts': dict(self.tic_counts),
            'tics': [tic.to_dict() for tic in self.tics]
        }


# ============================================================================
# TIC DETECTION FUNCTIONS
# ============================================================================

def detect_particular_tic(lines: List[str]) -> List[TicInstance]:
    """Detect 'the particular [noun]' pattern."""
    tics = []
    pattern = re.compile(r'\bthe particular (\w+)', re.IGNORECASE)

    for i, line in enumerate(lines, 1):
        for match in pattern.finditer(line):
            tic = TicInstance(
                tic_type="particular",
                line_num=i,
                line_text=line.strip(),
                matched_text=match.group(0)
            )

            # Generate proposals
            noun = match.group(1)

            # Option 1: Remove "particular"
            simple = match.group(0).replace(" particular", "")
            tic.add_proposal(
                original=match.group(0),
                revision=simple,
                explanation="Remove unnecessary intensifier"
            )

            # Option 2: Suggest specific descriptor (context-dependent)
            # We'll provide a placeholder that needs author judgment
            tic.add_proposal(
                original=match.group(0),
                revision=f"the [specific descriptor] {noun}",
                explanation="Replace with concrete descriptor"
            )

            tics.append(tic)

    return tics


def detect_something_constructions(lines: List[str]) -> List[TicInstance]:
    """Detect vague 'something' constructions."""
    tics = []

    # Pattern 1: something [verbed]
    pattern1 = re.compile(r'\bsomething (\w+ed|moved|shifted|changed|broke|clicked|snapped)\b', re.IGNORECASE)

    # Pattern 2: something in/about/within [noun]
    pattern2 = re.compile(r'\bsomething (in|about|within|of) (?:the |his |her |their |my |your )?(\w+)', re.IGNORECASE)

    # Pattern 3: something like
    pattern3 = re.compile(r'\bsomething like ([^,.;]+)', re.IGNORECASE)

    for i, line in enumerate(lines, 1):
        # Check pattern 1
        for match in pattern1.finditer(line):
            tic = TicInstance(
                tic_type="something_construction",
                line_num=i,
                line_text=line.strip(),
                matched_text=match.group(0)
            )

            verb = match.group(1)
            tic.add_proposal(
                original=match.group(0),
                revision=f"[name the thing] {verb}",
                explanation="Name the specific referent instead of using 'something'"
            )

            tics.append(tic)

        # Check pattern 2
        for match in pattern2.finditer(line):
            tic = TicInstance(
                tic_type="something_construction",
                line_num=i,
                line_text=line.strip(),
                matched_text=match.group(0)
            )

            preposition = match.group(1)
            noun = match.group(2)
            tic.add_proposal(
                original=match.group(0),
                revision=f"[specific quality] {preposition} the {noun}",
                explanation="Replace 'something' with specific descriptor"
            )

            tics.append(tic)

        # Check pattern 3
        for match in pattern3.finditer(line):
            tic = TicInstance(
                tic_type="something_construction",
                line_num=i,
                line_text=line.strip(),
                matched_text=match.group(0)
            )

            description = match.group(1).strip()
            tic.add_proposal(
                original=match.group(0),
                revision=f"{description}",
                explanation="Consider naming it directly instead of 'something like'"
            )

            tics.append(tic)

    return tics


def detect_em_dash_excess(text: str, lines: List[str]) -> List[TicInstance]:
    """Detect paragraphs with >2 em-dash pairs."""
    tics = []

    # Split into paragraphs
    paragraphs = text.split('\n\n')
    current_line = 1

    for para in paragraphs:
        if not para.strip():
            current_line += 1
            continue

        # Count em-dashes in this paragraph
        em_dash_count = para.count('—')

        # If more than 4 em-dashes (2 pairs), flag it
        if em_dash_count > 4:
            # Find the line number of the paragraph start
            para_lines = para.split('\n')
            first_line = para_lines[0].strip() if para_lines else ""

            # Find which line this paragraph starts on
            for i, line in enumerate(lines, 1):
                if line.strip() == first_line:
                    tic = TicInstance(
                        tic_type="em_dash_excess",
                        line_num=i,
                        line_text=f"[Paragraph with {em_dash_count} em-dashes]",
                        matched_text=para[:100] + "..."
                    )

                    tic.add_proposal(
                        original="[Multiple em-dash pairs in paragraph]",
                        revision="Convert some to periods or semicolons",
                        explanation=f"Paragraph has {em_dash_count} em-dashes ({em_dash_count//2} pairs). Consider varying punctuation."
                    )

                    tics.append(tic)
                    break

        current_line += len(para.split('\n'))

    return tics


def detect_abstract_noun_actions(lines: List[str]) -> List[TicInstance]:
    """Detect abstract nouns performing physical actions."""
    tics = []

    for i, line in enumerate(lines, 1):
        # Look for pattern: [abstract noun] [physical verb]
        words = line.lower().split()

        for j in range(len(words) - 1):
            # Check if word is an abstract noun
            word = re.sub(r'[^\w]', '', words[j])
            next_word = re.sub(r'[^\w]', '', words[j + 1])

            if word in ABSTRACT_NOUNS and next_word in PHYSICAL_VERBS:
                # Found a match
                # Get the actual text (with capitalization)
                match_start = line.lower().find(word)
                if match_start != -1:
                    # Extract the phrase
                    match_text = line[match_start:match_start + len(word) + len(next_word) + 10]
                    match_text = match_text.split('.')[0]  # Stop at sentence end

                    tic = TicInstance(
                        tic_type="abstract_noun_action",
                        line_num=i,
                        line_text=line.strip(),
                        matched_text=f"{word} {next_word}"
                    )

                    tic.add_proposal(
                        original=f"{word} {next_word}",
                        revision="[Rephrase with human subject or concrete imagery]",
                        explanation=f"Abstract noun '{word}' performing physical action '{next_word}'"
                    )

                    tics.append(tic)

    return tics


def detect_not_x_patterns(lines: List[str]) -> List[TicInstance]:
    """Detect 'Not X—Y' and 'Not X. Not Y. Z.' repetition patterns."""
    tics = []

    # Pattern 1: Not X—Y (with em-dash)
    pattern1 = re.compile(r'\bNot \w+[^.!?]*?—[^.!?]+', re.IGNORECASE)

    # Pattern 2: Not X. Y. (two sentences starting with variations)
    # We'll check for multiple "Not" sentences in proximity

    for i, line in enumerate(lines, 1):
        # Check pattern 1
        for match in pattern1.finditer(line):
            tic = TicInstance(
                tic_type="not_x_pattern",
                line_num=i,
                line_text=line.strip(),
                matched_text=match.group(0)
            )

            tic.add_proposal(
                original=match.group(0),
                revision="[Rephrase without 'Not X—Y' structure]",
                explanation="Consider varying sentence structure"
            )

            tics.append(tic)

        # Check for repeated "Not" at sentence starts
        sentences = re.split(r'[.!?]+', line)
        not_count = sum(1 for s in sentences if s.strip().lower().startswith('not '))

        if not_count >= 2:
            tic = TicInstance(
                tic_type="not_x_pattern",
                line_num=i,
                line_text=line.strip(),
                matched_text=f"[{not_count} sentences starting with 'Not']"
            )

            tic.add_proposal(
                original="Multiple 'Not X' sentences",
                revision="Vary sentence openings",
                explanation=f"Line has {not_count} sentences starting with 'Not'"
            )

            tics.append(tic)

    return tics


# ============================================================================
# CHAPTER PROCESSING
# ============================================================================

def analyze_chapter(chapter_num: int, dir_name: str, title: str) -> Optional[ChapterAnalysis]:
    """Analyze a single chapter for prose tics."""
    # Find the draft file
    dir_path = CHAPTERS_DIR / dir_name
    padded_num = str(chapter_num).zfill(2)
    file_path = dir_path / f"CH{padded_num}_draft.md"

    if not file_path.exists():
        print(f"  [SKIP] Chapter {chapter_num}: Draft file not found")
        return None

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove metadata/word counts
    content = re.sub(r'\*\*Word count:.*?\*\*', '', content)

    lines = content.split('\n')

    # Create analysis object
    analysis = ChapterAnalysis(chapter_num, title, file_path)
    analysis.word_count = len(content.split())

    # Run all tic detections
    print(f"  [{chapter_num:02d}/26] Analyzing: {title}")

    # 1. Particular tic
    particular_tics = detect_particular_tic(lines)
    for tic in particular_tics:
        analysis.add_tic(tic)

    # 2. Something constructions
    something_tics = detect_something_constructions(lines)
    for tic in something_tics:
        analysis.add_tic(tic)

    # 3. Em-dash excess
    em_dash_tics = detect_em_dash_excess(content, lines)
    for tic in em_dash_tics:
        analysis.add_tic(tic)

    # 4. Abstract noun actions
    abstract_tics = detect_abstract_noun_actions(lines)
    for tic in abstract_tics:
        analysis.add_tic(tic)

    # 5. Not X patterns
    not_x_tics = detect_not_x_patterns(lines)
    for tic in not_x_tics:
        analysis.add_tic(tic)

    return analysis


# ============================================================================
# REPORT GENERATION
# ============================================================================

def generate_markdown_report(analyses: List[ChapterAnalysis]) -> str:
    """Generate human-readable markdown report."""
    lines = []

    lines.append("# Prose Tic Analysis Report")
    lines.append("# The Wheel of Meat - Complete Manuscript")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Overall summary
    total_tics = sum(a.total_tics() for a in analyses)
    total_words = sum(a.word_count for a in analyses)
    avg_density = (total_tics / total_words * 1000) if total_words > 0 else 0

    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"- **Total chapters analyzed:** {len(analyses)}")
    lines.append(f"- **Total word count:** {total_words:,}")
    lines.append(f"- **Total tics identified:** {total_tics}")
    lines.append(f"- **Average tic density:** {avg_density:.2f} per 1,000 words")
    lines.append("")

    # Tic type breakdown
    all_tic_counts = defaultdict(int)
    for analysis in analyses:
        for tic_type, count in analysis.tic_counts.items():
            all_tic_counts[tic_type] += count

    lines.append("### Tic Distribution")
    lines.append("")
    for tic_type, count in sorted(all_tic_counts.items(), key=lambda x: -x[1]):
        pct = (count / total_tics * 100) if total_tics > 0 else 0
        lines.append(f"- **{tic_type}:** {count} instances ({pct:.1f}%)")
    lines.append("")

    # Top 10 chapters by density
    lines.append("### Chapters Requiring Most Attention (by tic density)")
    lines.append("")
    sorted_analyses = sorted(analyses, key=lambda a: a.tic_density(), reverse=True)
    for i, analysis in enumerate(sorted_analyses[:10], 1):
        lines.append(f"{i}. **Ch.{analysis.chapter_num}: {analysis.title}** - "
                    f"{analysis.total_tics()} tics ({analysis.tic_density():.1f} per 1K words)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed chapter-by-chapter analysis
    lines.append("## Detailed Chapter Analysis")
    lines.append("")

    for analysis in analyses:
        lines.append(f"### Chapter {analysis.chapter_num}: {analysis.title}")
        lines.append("")
        lines.append(f"**Word count:** {analysis.word_count:,} | "
                    f"**Total tics:** {analysis.total_tics()} | "
                    f"**Density:** {analysis.tic_density():.2f} per 1K words")
        lines.append("")

        if analysis.total_tics() == 0:
            lines.append("✓ No tics detected in this chapter.")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue

        # Group tics by type
        tics_by_type = defaultdict(list)
        for tic in analysis.tics:
            tics_by_type[tic.tic_type].append(tic)

        # Report each tic type
        for tic_type in sorted(tics_by_type.keys()):
            tic_list = tics_by_type[tic_type]

            # Tic type header
            type_names = {
                'particular': '"The particular [noun]" usage',
                'something_construction': 'Vague "something" constructions',
                'em_dash_excess': 'Em-dash excess (>2 pairs per paragraph)',
                'abstract_noun_action': 'Abstract nouns performing physical actions',
                'not_x_pattern': '"Not X" repetition patterns'
            }

            lines.append(f"#### {type_names.get(tic_type, tic_type)} ({len(tic_list)} instances)")
            lines.append("")

            # List each instance
            for tic in tic_list[:20]:  # Limit to first 20 per type
                lines.append(f"**Line {tic.line_num}:**")
                lines.append(f"> {tic.line_text[:150]}")
                lines.append("")

                if tic.proposals:
                    lines.append("**Revision proposals:**")
                    for proposal in tic.proposals:
                        lines.append(f"- `{proposal['original']}` → `{proposal['revision']}`")
                        if proposal['explanation']:
                            lines.append(f"  - *{proposal['explanation']}*")
                    lines.append("")

            if len(tic_list) > 20:
                lines.append(f"*...and {len(tic_list) - 20} more instances*")
                lines.append("")

        lines.append("---")
        lines.append("")

    return '\n'.join(lines)


def generate_summary_report(analyses: List[ChapterAnalysis]) -> str:
    """Generate quick summary statistics."""
    lines = []

    lines.append("=" * 80)
    lines.append("PROSE TIC ANALYSIS - SUMMARY")
    lines.append("=" * 80)
    lines.append("")

    # Table header
    lines.append(f"{'Ch':<4} {'Title':<30} {'Words':>8} {'Tics':>6} {'Density':>8}")
    lines.append("-" * 80)

    for analysis in analyses:
        lines.append(
            f"{analysis.chapter_num:<4} "
            f"{analysis.title[:28]:<30} "
            f"{analysis.word_count:>8,} "
            f"{analysis.total_tics():>6} "
            f"{analysis.tic_density():>8.2f}"
        )

    lines.append("-" * 80)

    total_words = sum(a.word_count for a in analyses)
    total_tics = sum(a.total_tics() for a in analyses)
    avg_density = (total_tics / total_words * 1000) if total_words > 0 else 0

    lines.append(
        f"{'TOTAL':<35} "
        f"{total_words:>8,} "
        f"{total_tics:>6} "
        f"{avg_density:>8.2f}"
    )

    lines.append("")
    lines.append("=" * 80)

    return '\n'.join(lines)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main entry point."""
    print("=" * 60)
    print("PROSE TIC ANALYZER - The Wheel of Meat")
    print("=" * 60)
    print("")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Analyzing all chapters...")
    print("-" * 60)

    analyses = []

    for chapter_num, dir_name, title in CHAPTERS:
        analysis = analyze_chapter(chapter_num, dir_name, title)
        if analysis:
            analyses.append(analysis)

    print("-" * 60)
    print(f"\n✓ Analysis complete: {len(analyses)} chapters processed")
    print("")

    # Save JSON data
    json_output = OUTPUT_DIR / "tic_analysis_full.json"
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(
            {
                'total_chapters': len(analyses),
                'total_tics': sum(a.total_tics() for a in analyses),
                'chapters': [a.to_dict() for a in analyses]
            },
            f,
            indent=2
        )
    print(f"✓ JSON data saved: {json_output}")

    # Generate markdown report
    markdown_report = generate_markdown_report(analyses)
    markdown_output = OUTPUT_DIR / "tic_revision_report.md"
    with open(markdown_output, 'w', encoding='utf-8') as f:
        f.write(markdown_report)
    print(f"✓ Markdown report saved: {markdown_output}")

    # Generate summary
    summary = generate_summary_report(analyses)
    summary_output = OUTPUT_DIR / "tic_summary.txt"
    with open(summary_output, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"✓ Summary saved: {summary_output}")

    # Print summary to console
    print("")
    print(summary)

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
