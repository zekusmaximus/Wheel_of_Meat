#!/usr/bin/env python3
"""
The Wheel of Meat - Manuscript Compiler v4.1
============================================
Compiles all 26 chapters into a unified manuscript with comprehensive
statistics, validation, and professional formatting.

Features:
- Cross-platform path handling
- Detailed word/character/paragraph statistics per chapter
- Manuscript validation and integrity checks
- Table of contents generation
- Professional formatting with scene breaks preserved
- Comprehensive compilation report
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
from collections import namedtuple
from typing import Dict, List, Tuple, Optional

# ============================================================================
# CONFIGURATION
# ============================================================================

# Detect base directory (cross-platform)
BASE_DIR = Path(__file__).parent.resolve()
CHAPTERS_DIR = BASE_DIR / "incarnations"
OUTPUT_DIR = BASE_DIR
OUTPUT_FILE = OUTPUT_DIR / "WOM_Manuscript_full.md"
STATS_FILE = OUTPUT_DIR / "manuscript_statistics.txt"

# Chapter configuration with metadata
ChapterInfo = namedtuple('ChapterInfo', ['num', 'dir_name', 'title', 'era', 'protagonist'])

CHAPTERS = [
    ChapterInfo(1, "ch01-contemporary-manchester", "The Awakening", "Contemporary", "Silas Phalavan"),
    ChapterInfo(2, "ch02-prehistoric-ka", "The First Flame", "Prehistoric", "Ka"),
    ChapterInfo(3, "ch03-lilith-cp01", "Lilith's Watch I", "Celestial", "Lilith"),
    ChapterInfo(4, "ch04-mauryan-chandra", "The Mauryan Empire", "Ancient India", "Chandra"),
    ChapterInfo(5, "ch05-lilith-cp02", "Lilith's Watch II", "Celestial", "Lilith"),
    ChapterInfo(6, "ch06-athens-philosopher", "The Philosopher", "Classical Athens", "Philosopher"),
    ChapterInfo(7, "ch07-lilith-cp03", "Lilith's Watch III", "Celestial", "Lilith"),
    ChapterInfo(8, "ch08-rome-investigator", "The Investigator", "Roman Empire", "Investigator"),
    ChapterInfo(9, "ch09-lilith-cp04", "Lilith's Watch IV", "Celestial", "Lilith"),
    ChapterInfo(10, "ch10-egypt-hermit", "The Desert Hermit", "Byzantine Egypt", "Hermit"),
    ChapterInfo(11, "ch11-lilith-cp05", "Lilith's Watch V", "Celestial", "Lilith"),
    ChapterInfo(12, "ch12-heian-lover", "The Lover", "Heian Japan", "Lover"),
    ChapterInfo(13, "ch13-lilith-cp06", "Lilith's Watch VI", "Celestial", "Lilith"),
    ChapterInfo(14, "ch14-inquisition-accused", "The Accused", "Spanish Inquisition", "Accused"),
    ChapterInfo(15, "ch15-lilith-cp07", "Lilith's Watch VII", "Celestial", "Lilith"),
    ChapterInfo(16, "ch16-renaissance-skeptic", "The Skeptic", "Renaissance", "Skeptic"),
    ChapterInfo(17, "ch17-lilith-cp08", "Lilith's Watch VIII", "Celestial", "Lilith"),
    ChapterInfo(18, "ch18-taiping-rebel", "The Rebel", "Taiping Rebellion", "Rebel"),
    ChapterInfo(19, "ch19-lilith-cp09", "Lilith's Watch IX", "Celestial", "Lilith"),
    ChapterInfo(20, "ch20-noir-detective", "The Detective", "1940s Noir", "Detective"),
    ChapterInfo(21, "ch21-lilith-cp10", "Lilith's Watch X", "Celestial", "Lilith"),
    ChapterInfo(22, "ch22-contemporary-breakthrough", "The Breakthrough", "Contemporary", "Silas Phalavan"),
    ChapterInfo(23, "ch23-deva-celestial", "The Celestial Realm", "Deva Realm", "Celestial Being"),
    ChapterInfo(24, "ch24-future-prophet", "The Prophet", "Near Future", "Prophet"),
    ChapterInfo(25, "ch25-space-explorer", "The Explorer", "Far Future", "Explorer"),
    ChapterInfo(26, "ch26-pure-abodes-awakened", "The Awakened", "Pure Abodes", "Awakened One"),
]

# Chapter names for headers
CHAPTER_NAMES = [
    'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
    'Eighteen', 'Nineteen', 'Twenty', 'Twenty-One', 'Twenty-Two', 'Twenty-Three',
    'Twenty-Four', 'Twenty-Five', 'Twenty-Six'
]

# ============================================================================
# STATISTICS TRACKING
# ============================================================================

class ChapterStats:
    """Track statistics for a single chapter."""
    def __init__(self, chapter_num: int, title: str):
        self.chapter_num = chapter_num
        self.title = title
        self.word_count = 0
        self.char_count = 0
        self.char_count_no_spaces = 0
        self.paragraph_count = 0
        self.scene_count = 0
        self.sentence_count = 0
        self.avg_sentence_length = 0.0
        self.file_path: Optional[Path] = None
        self.status = "pending"
        self.error_message = ""

    def calculate(self, text: str):
        """Calculate all statistics from the chapter text."""
        self.char_count = len(text)
        self.char_count_no_spaces = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))

        # Word count (split on whitespace)
        words = text.split()
        self.word_count = len(words)

        # Paragraph count (separated by double newlines)
        paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
        self.paragraph_count = len(paragraphs)

        # Scene count (marked by *** or --- or scene breaks)
        scene_markers = re.findall(r'^\s*[*\-]{3,}\s*$', text, re.MULTILINE)
        self.scene_count = len(scene_markers) + 1  # +1 for the initial scene

        # Sentence count (approximate)
        sentences = re.split(r'[.!?]+(?:\s|$)', text)
        self.sentence_count = len([s for s in sentences if s.strip()])

        # Average sentence length
        if self.sentence_count > 0:
            self.avg_sentence_length = self.word_count / self.sentence_count

    def to_dict(self) -> dict:
        return {
            'chapter': self.chapter_num,
            'title': self.title,
            'words': self.word_count,
            'characters': self.char_count,
            'paragraphs': self.paragraph_count,
            'scenes': self.scene_count,
            'sentences': self.sentence_count,
            'avg_sentence_length': round(self.avg_sentence_length, 1),
            'status': self.status
        }


class ManuscriptStats:
    """Track statistics for the entire manuscript."""
    def __init__(self):
        self.chapters: List[ChapterStats] = []
        self.compilation_time: Optional[datetime] = None
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def add_chapter(self, stats: ChapterStats):
        self.chapters.append(stats)

    @property
    def total_words(self) -> int:
        return sum(c.word_count for c in self.chapters if c.status == "success")

    @property
    def total_chars(self) -> int:
        return sum(c.char_count for c in self.chapters if c.status == "success")

    @property
    def total_paragraphs(self) -> int:
        return sum(c.paragraph_count for c in self.chapters if c.status == "success")

    @property
    def total_scenes(self) -> int:
        return sum(c.scene_count for c in self.chapters if c.status == "success")

    @property
    def successful_chapters(self) -> int:
        return len([c for c in self.chapters if c.status == "success"])

    @property
    def failed_chapters(self) -> int:
        return len([c for c in self.chapters if c.status == "error"])

    def estimated_pages(self, words_per_page: int = 250) -> int:
        """Estimate page count based on standard manuscript format."""
        return self.total_words // words_per_page


# ============================================================================
# FILE OPERATIONS
# ============================================================================

def find_draft_file(chapter: ChapterInfo) -> Path:
    """Find the standardized draft markdown file for a chapter."""
    dir_path = CHAPTERS_DIR / chapter.dir_name
    padded_num = str(chapter.num).zfill(2)

    # Try standard naming convention
    file_path = dir_path / f"CH{padded_num}_draft.md"
    if file_path.exists():
        return file_path

    # Try alternative naming patterns
    alternatives = [
        f"ch{padded_num}_draft.md",
        f"Chapter{padded_num}_draft.md",
        f"chapter_{padded_num}_draft.md",
    ]

    for alt in alternatives:
        alt_path = dir_path / alt
        if alt_path.exists():
            return alt_path

    raise FileNotFoundError(
        f"Could not find draft file for chapter {chapter.num} in {dir_path}\n"
        f"Expected: CH{padded_num}_draft.md"
    )


def extract_narrative(file_path: Path) -> str:
    """Extract and clean narrative text from the chapter file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any YAML frontmatter if present
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Remove any metadata comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Clean up excessive whitespace while preserving paragraph breaks
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


def validate_chapter(text: str, chapter: ChapterInfo) -> List[str]:
    """Validate chapter content and return any warnings."""
    warnings = []

    word_count = len(text.split())

    # Check for minimum content
    if word_count < 1000:
        warnings.append(f"Chapter {chapter.num}: Very short ({word_count} words)")

    # Check for unusually long chapter
    if word_count > 15000:
        warnings.append(f"Chapter {chapter.num}: Very long ({word_count} words)")

    # Check for potential formatting issues
    if '# ' in text and not text.startswith('#'):
        warnings.append(f"Chapter {chapter.num}: Contains embedded headers")

    # Check for unresolved placeholders
    placeholders = re.findall(r'\[(?:TODO|TBD|PLACEHOLDER|XXX)[^\]]*\]', text, re.IGNORECASE)
    if placeholders:
        warnings.append(f"Chapter {chapter.num}: Contains {len(placeholders)} unresolved placeholders")

    return warnings


# ============================================================================
# COMPILATION
# ============================================================================

def compile_manuscript(verbose: bool = True) -> Tuple[str, ManuscriptStats]:
    """Compile the complete manuscript from all chapters."""
    stats = ManuscriptStats()
    stats.compilation_time = datetime.now()

    manuscript_parts = []

    # Add title page
    manuscript_parts.append("# The Wheel of Meat")
    manuscript_parts.append("")
    manuscript_parts.append("*A Novel*")
    manuscript_parts.append("")
    manuscript_parts.append(f"*Compiled: {stats.compilation_time.strftime('%B %d, %Y')}*")
    manuscript_parts.append("")
    manuscript_parts.append("---")
    manuscript_parts.append("")

    # Process all chapters
    for chapter in CHAPTERS:
        chapter_stats = ChapterStats(chapter.num, chapter.title)

        try:
            # Find and read the chapter file
            draft_file = find_draft_file(chapter)
            chapter_stats.file_path = draft_file

            if verbose:
                print(f"  [{chapter.num:02d}/26] Processing: {chapter.dir_name}")

            # Extract narrative content
            narrative = extract_narrative(draft_file)

            # Calculate statistics
            chapter_stats.calculate(narrative)

            # Validate content
            warnings = validate_chapter(narrative, chapter)
            stats.warnings.extend(warnings)

            # Add chapter header
            manuscript_parts.append(f"# Chapter {CHAPTER_NAMES[chapter.num - 1]}")
            manuscript_parts.append("")

            # Add narrative content
            manuscript_parts.append(narrative)

            # Add chapter divider (except for last chapter)
            if chapter.num < 26:
                manuscript_parts.append("")
                manuscript_parts.append("---")
                manuscript_parts.append("")

            chapter_stats.status = "success"

        except FileNotFoundError as e:
            chapter_stats.status = "error"
            chapter_stats.error_message = str(e)
            stats.errors.append(f"Chapter {chapter.num}: {e}")
            if verbose:
                print(f"  [ERROR] Chapter {chapter.num}: File not found")

        except Exception as e:
            chapter_stats.status = "error"
            chapter_stats.error_message = str(e)
            stats.errors.append(f"Chapter {chapter.num}: Unexpected error - {e}")
            if verbose:
                print(f"  [ERROR] Chapter {chapter.num}: {e}")

        stats.add_chapter(chapter_stats)

    # Combine all parts
    manuscript = '\n'.join(manuscript_parts)

    return manuscript, stats


def generate_statistics_report(stats: ManuscriptStats) -> str:
    """Generate a detailed statistics report."""
    lines = []
    lines.append("=" * 70)
    lines.append("THE WHEEL OF MEAT - MANUSCRIPT STATISTICS")
    lines.append("=" * 70)
    lines.append(f"Compiled: {stats.compilation_time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Summary
    lines.append("-" * 70)
    lines.append("MANUSCRIPT SUMMARY")
    lines.append("-" * 70)
    lines.append(f"  Chapters Compiled:     {stats.successful_chapters}/26")
    lines.append(f"  Total Word Count:      {stats.total_words:,}")
    lines.append(f"  Total Characters:      {stats.total_chars:,}")
    lines.append(f"  Total Paragraphs:      {stats.total_paragraphs:,}")
    lines.append(f"  Total Scenes:          {stats.total_scenes:,}")
    lines.append(f"  Estimated Pages:       ~{stats.estimated_pages():,} (at 250 words/page)")
    lines.append("")

    # Chapter breakdown
    lines.append("-" * 70)
    lines.append("CHAPTER BREAKDOWN")
    lines.append("-" * 70)
    lines.append(f"{'Ch#':<4} {'Title':<30} {'Words':>8} {'Pars':>6} {'Scenes':>6} {'Status':<8}")
    lines.append("-" * 70)

    for ch in stats.chapters:
        status_icon = "✓" if ch.status == "success" else "✗"
        lines.append(
            f"{ch.chapter_num:>3}  {ch.title:<30} {ch.word_count:>8,} {ch.paragraph_count:>6} "
            f"{ch.scene_count:>6} {status_icon}"
        )

    lines.append("-" * 70)
    lines.append(f"{'TOTAL':<35} {stats.total_words:>8,} {stats.total_paragraphs:>6} {stats.total_scenes:>6}")
    lines.append("")

    # Word count distribution
    lines.append("-" * 70)
    lines.append("WORD COUNT ANALYSIS")
    lines.append("-" * 70)
    successful = [c for c in stats.chapters if c.status == "success"]
    if successful:
        word_counts = [c.word_count for c in successful]
        avg_words = sum(word_counts) / len(word_counts)
        min_ch = min(successful, key=lambda c: c.word_count)
        max_ch = max(successful, key=lambda c: c.word_count)

        lines.append(f"  Average per chapter:   {avg_words:,.0f} words")
        lines.append(f"  Shortest chapter:      Ch.{min_ch.chapter_num} - {min_ch.word_count:,} words")
        lines.append(f"  Longest chapter:       Ch.{max_ch.chapter_num} - {max_ch.word_count:,} words")
    lines.append("")

    # Warnings
    if stats.warnings:
        lines.append("-" * 70)
        lines.append("WARNINGS")
        lines.append("-" * 70)
        for warning in stats.warnings:
            lines.append(f"  ⚠ {warning}")
        lines.append("")

    # Errors
    if stats.errors:
        lines.append("-" * 70)
        lines.append("ERRORS")
        lines.append("-" * 70)
        for error in stats.errors:
            lines.append(f"  ✗ {error}")
        lines.append("")

    lines.append("=" * 70)

    return '\n'.join(lines)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main entry point for manuscript compilation."""
    print("=" * 60)
    print("THE WHEEL OF MEAT - Manuscript Compiler v4.1")
    print("=" * 60)
    print(f"Base directory: {BASE_DIR}")
    print(f"Chapters directory: {CHAPTERS_DIR}")
    print("")

    # Validate directories exist
    if not CHAPTERS_DIR.exists():
        print(f"ERROR: Chapters directory not found: {CHAPTERS_DIR}")
        sys.exit(1)

    print("Compiling manuscript...")
    print("-" * 60)

    # Compile the manuscript
    manuscript, stats = compile_manuscript(verbose=True)

    print("-" * 60)

    # Write the manuscript
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(manuscript)
        print(f"\n✓ Manuscript saved to: {OUTPUT_FILE}")
        print(f"  File size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    except Exception as e:
        print(f"\n✗ Failed to write manuscript: {e}")
        sys.exit(1)

    # Generate and display statistics
    report = generate_statistics_report(stats)
    print("")
    print(report)

    # Save statistics report
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n✓ Statistics saved to: {STATS_FILE}")
    except Exception as e:
        print(f"\n⚠ Failed to write statistics file: {e}")

    # Final status
    print("")
    if stats.failed_chapters == 0:
        print("=" * 60)
        print("COMPILATION SUCCESSFUL")
        print(f"All 26 chapters compiled | {stats.total_words:,} words total")
        print("=" * 60)
        return 0
    else:
        print("=" * 60)
        print("COMPILATION COMPLETED WITH ERRORS")
        print(f"{stats.failed_chapters} chapter(s) failed to compile")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
