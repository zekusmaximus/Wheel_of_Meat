#!/usr/bin/env python3
"""
Punctuation and rhythm auditor for scene files.
Flags mechanical issues and stylistic overuse patterns.

Usage: python punctuation_audit.py scenes/chapter-01/scene-01.md
"""

import sys
import re
from pathlib import Path
from collections import defaultdict


def audit_punctuation(filepath):
    """Analyze a scene file for punctuation and rhythm issues."""

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = []
    stats = defaultdict(int)

    # Track consecutive short sentences across lines
    consecutive_short = 0
    short_streak_start = None

    for i, line in enumerate(lines, 1):
        line_text = line.strip()

        # Skip empty lines and headers
        if not line_text or line_text.startswith('#'):
            consecutive_short = 0
            continue

        # Em-dash density check
        em_dash_count = line_text.count('—')
        if em_dash_count > 1:
            issues.append(f"Line {i}: Multiple em-dashes ({em_dash_count}) - consider splitting or reducing")
            stats['em_dash_overuse'] += 1

        # Semicolon in dialogue
        if '"' in line_text and ';' in line_text:
            # Check if semicolon is actually inside quotes
            in_quotes = False
            for char in line_text:
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ';' and in_quotes:
                    issues.append(f"Line {i}: Semicolon inside dialogue (likely error)")
                    stats['semicolon_in_dialogue'] += 1
                    break

        # Comma splice detection
        conjunctive_adverbs = r'\b(however|therefore|thus|nevertheless|moreover|furthermore|consequently|meanwhile)\s*,'
        if re.search(conjunctive_adverbs, line_text, re.IGNORECASE):
            # Check if there's a complete sentence before it
            parts = re.split(conjunctive_adverbs, line_text, flags=re.IGNORECASE)
            if len(parts) > 1 and '.' not in parts[0] and parts[0].strip():
                issues.append(f"Line {i}: Possible comma splice with conjunctive adverb")
                stats['comma_splice'] += 1

        # Ellipsis overuse (per paragraph - using double newline as paragraph marker)
        if line_text.count('...') > 1 or line_text.count('…') > 1:
            issues.append(f"Line {i}: Multiple ellipses in single paragraph")
            stats['ellipsis_overuse'] += 1

        # Count sentences and check length
        sentences = re.split(r'[.!?]+\s+', line_text)
        sentences = [s.strip() for s in sentences if s.strip()]

        short_in_line = sum(1 for s in sentences if len(s.split()) < 8)

        if short_in_line >= 2:
            consecutive_short += short_in_line
            if short_streak_start is None:
                short_streak_start = i
        else:
            if consecutive_short >= 3:
                issues.append(
                    f"Lines {short_streak_start}-{i-1}: {consecutive_short} consecutive short sentences (rhythm issue)"
                )
                stats['rhythm_issues'] += 1
            consecutive_short = 0
            short_streak_start = None

        # Coordinating conjunction sentence starters in same paragraph
        coord_conj_starts = len(re.findall(r'^\s*(And|But|Or|So)\s+', line_text))
        if coord_conj_starts > 0:
            stats['conjunction_starts'] += coord_conj_starts

    # Final check for short sentence streak
    if consecutive_short >= 3:
        issues.append(
            f"Lines {short_streak_start}-{len(lines)}: {consecutive_short} consecutive short sentences (rhythm issue)"
        )
        stats['rhythm_issues'] += 1

    return issues, stats


def main():
    if len(sys.argv) != 2:
        print("Usage: python punctuation_audit.py <scene-file.md>")
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    print(f"\n=== Punctuation Audit: {filepath.name} ===\n")

    issues, stats = audit_punctuation(filepath)

    if not issues:
        print("✓ No punctuation issues detected.\n")
    else:
        for issue in issues:
            print(f"• {issue}")
        print(f"\n--- Summary ---")
        print(f"Total issues: {len(issues)}")
        for category, count in sorted(stats.items()):
            print(f"  {category.replace('_', ' ').title()}: {count}")

    print()


if __name__ == '__main__':
    main()
