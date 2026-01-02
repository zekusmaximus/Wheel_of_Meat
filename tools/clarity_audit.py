#!/usr/bin/env python3
"""
Clarity auditor for scene files.
Identifies unclear pronoun references and ambiguous constructions.

Usage: python clarity_audit.py scenes/chapter-01/scene-01.md
"""

import sys
import re
from pathlib import Path
from collections import defaultdict


def check_clarity(filepath):
    """Analyze a scene file for clarity issues."""

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = []
    stats = defaultdict(int)

    # Personal pronouns to track
    pronouns = r'\b(he|she|it|they|him|her|them|his|hers|their|its)\b'
    demonstrative = r'\b(that|this|these|those)\b'

    for i, line in enumerate(lines, 1):
        line_text = line.strip()

        # Skip empty lines and headers
        if not line_text or line_text.startswith('#'):
            continue

        # Sentences starting with pronouns
        if re.match(r'^\s*"?(He|She|It|They)\s+', line_text):
            issues.append({
                'line': i,
                'severity': 'MEDIUM',
                'issue': 'Sentence starts with pronoun',
                'detail': 'Check that antecedent is clear in previous sentence'
            })
            stats['pronoun_start'] += 1

        # Multiple named entities with pronouns (ambiguity risk)
        # Count capitalized words (likely names) and proper nouns
        named_entities = len(re.findall(r'\b[A-Z][a-z]{2,}\b', line_text))
        has_pronouns = bool(re.search(pronouns, line_text, re.IGNORECASE))

        if named_entities >= 2 and has_pronouns:
            issues.append({
                'line': i,
                'severity': 'HIGH',
                'issue': 'Multiple entities with pronoun',
                'detail': f'{named_entities} named entities + pronoun - verify reference is clear'
            })
            stats['ambiguous_pronoun'] += 1

        # Demonstrative pronouns as sentence subjects
        demo_match = re.search(r'\b(That|This|These|Those)\s+(was|is|were|are|would|could|should|made|seemed|felt|meant)\b', line_text)
        if demo_match:
            issues.append({
                'line': i,
                'severity': 'MEDIUM',
                'issue': 'Demonstrative pronoun as subject',
                'detail': f'"{demo_match.group()}" - ensure referent is specific and recent'
            })
            stats['vague_demonstrative'] += 1

        # Vague constructions
        vague_patterns = [
            (r'\bIt seemed\b', '"It seemed" - consider more specific observation'),
            (r'\bThere (?:was|were|is|are)\b', '"There was/were" - consider stronger verb'),
            (r'\bthings?\s+(?:that|which)\b', '"things that/which" - specify what things'),
            (r'\bsomething\s+(?:that|which)\b', '"something that/which" - can you name it?'),
        ]

        for pattern, suggestion in vague_patterns:
            if re.search(pattern, line_text, re.IGNORECASE):
                issues.append({
                    'line': i,
                    'severity': 'LOW',
                    'issue': 'Vague construction',
                    'detail': suggestion
                })
                stats['vague_construction'] += 1

        # "Which" clauses that might be too far from referent
        # Simple heuristic: "which" preceded by more than 5 words
        which_match = re.search(r'(\w+(?:\s+\w+){5,})\s+which\b', line_text)
        if which_match:
            issues.append({
                'line': i,
                'severity': 'MEDIUM',
                'issue': 'Distant "which" clause',
                'detail': '"which" appears far from potential referent - verify clarity'
            })
            stats['distant_which'] += 1

    return issues, stats


def main():
    if len(sys.argv) != 2:
        print("Usage: python clarity_audit.py <scene-file.md>")
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    print(f"\n=== Clarity Audit: {filepath.name} ===\n")

    issues, stats = check_clarity(filepath)

    if not issues:
        print("✓ No clarity issues detected.\n")
    else:
        # Group by severity
        by_severity = defaultdict(list)
        for issue in issues:
            by_severity[issue['severity']].append(issue)

        for severity in ['HIGH', 'MEDIUM', 'LOW']:
            if severity in by_severity:
                print(f"\n--- {severity} Priority ---")
                for issue in by_severity[severity]:
                    print(f"Line {issue['line']}: {issue['issue']}")
                    print(f"  → {issue['detail']}\n")

        print(f"--- Summary ---")
        print(f"Total issues: {len(issues)}")
        for category, count in sorted(stats.items()):
            print(f"  {category.replace('_', ' ').title()}: {count}")

    print()


if __name__ == '__main__':
    main()
