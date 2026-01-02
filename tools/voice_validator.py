#!/usr/bin/env python3
"""
Voice pattern validator for scene files.
Checks adherence to the five core voice patterns of The Wheel of Meat.

Usage: python voice_validator.py scenes/chapter-01/scene-01.md [--thresholds undermining:0.6,sensory:0.8]
"""

import sys
import re
from pathlib import Path
from collections import defaultdict
import argparse


DEFAULT_THRESHOLDS = {
    'undermining_clause': 0.60,  # 60% of sentences should have complication
    'sensory_anchor': 0.75,      # 75% of paragraphs should open with physical detail
    'loaded_gesture': 0.40,      # 40% of paragraphs should contain gesture
    'environmental_presence': 0.50,  # 50% of paragraphs should reference setting
    'parallel_construction': 0.20,   # 20% of paragraphs should use mirrored phrases
}


def analyze_voice_patterns(filepath, thresholds=None):
    """Analyze scene file for voice pattern density."""

    if thresholds is None:
        thresholds = DEFAULT_THRESHOLDS

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into paragraphs (double newline separated)
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.strip().startswith('#')]

    # Split into sentences
    sentences = []
    for para in paragraphs:
        sents = re.split(r'[.!?]+\s+', para)
        sentences.extend([s.strip() for s in sents if s.strip()])

    results = {
        'undermining_clause': analyze_undermining(sentences),
        'sensory_anchor': analyze_sensory_anchors(paragraphs),
        'loaded_gesture': analyze_gestures(paragraphs),
        'environmental_presence': analyze_environment(paragraphs),
        'parallel_construction': analyze_parallelism(paragraphs),
    }

    issues = []

    for pattern, data in results.items():
        expected = thresholds.get(pattern, 0.5)
        if data['ratio'] < expected:
            issues.append({
                'pattern': pattern,
                'expected': expected,
                'actual': data['ratio'],
                'severity': 'HIGH' if data['ratio'] < expected * 0.7 else 'MEDIUM',
                'examples': data.get('missing_examples', []),
            })

    return results, issues, len(sentences), len(paragraphs)


def analyze_undermining(sentences):
    """Check for undermining clauses (complicating assertions)."""

    undermining_words = [
        r'\bbut\b', r'\bthough\b', r'\byet\b', r'\balmost\b', r'\bseemed?\b',
        r'\bperhaps\b', r'\bmight\b', r'\bcould\b', r'\bnearly\b', r'\balways\b',
        r'\bnever quite\b', r'\bnot exactly\b', r'\bbarely\b', r'\bonly\b',
        r'\beven as\b', r'\bwhile\b', r'\balthough\b', r'\bhowever\b'
    ]

    pattern = '|'.join(undermining_words)
    count = sum(1 for s in sentences if re.search(pattern, s, re.IGNORECASE))

    # Find examples of sentences without undermining
    missing_examples = [s[:80] + '...' for s in sentences[:20]
                       if not re.search(pattern, s, re.IGNORECASE) and len(s.split()) > 8][:3]

    return {
        'count': count,
        'total': len(sentences),
        'ratio': count / len(sentences) if sentences else 0,
        'missing_examples': missing_examples,
    }


def analyze_sensory_anchors(paragraphs):
    """Check if paragraphs open with concrete physical details."""

    # Patterns that indicate sensory/physical opening
    sensory_openers = [
        r'^(The|A|An)\s+\w+\s+(light|dark|cold|warm|heat|sound|smell|taste|texture)',
        r'^(The|A|An)\s+(room|space|air|wind|ground|floor|wall|ceiling|sky)',
        r'^(Light|Dark|Cold|Warm|Heat|Sound|Silence|Pain|Pressure)',
        r'^(His|Her|Their)\s+(hand|hands|fingers|eyes|face|body|skin|breath|heart)',
        r'^\w+\'s\s+(hand|fingers|eyes|face|body|skin|breath|voice)',
        r'^(Blood|Sweat|Tears|Dust|Smoke|Rain|Snow|Stone|Metal|Wood|Glass)',
    ]

    pattern = '|'.join(sensory_openers)
    count = sum(1 for p in paragraphs if re.match(pattern, p, re.IGNORECASE))

    # Examples of paragraphs with non-sensory openings
    missing_examples = [p[:80] + '...' for p in paragraphs[:20]
                       if not re.match(pattern, p, re.IGNORECASE)][:3]

    return {
        'count': count,
        'total': len(paragraphs),
        'ratio': count / len(paragraphs) if paragraphs else 0,
        'missing_examples': missing_examples,
    }


def analyze_gestures(paragraphs):
    """Check for physical actions/loaded gestures."""

    gesture_words = [
        r'\b(reached|grabbed|touched|held|lifted|turned|stepped|walked|moved|shifted)\b',
        r'\b(hand|hands|finger|fingers|arm|arms)\s+\w+',
        r'\b(nodded|shook|raised|lowered|tilted|clenched|unclenched)\b',
        r'\b(eyes|gaze)\s+(met|found|followed|tracked|settled)\b',
    ]

    pattern = '|'.join(gesture_words)
    count = sum(1 for p in paragraphs if re.search(pattern, p, re.IGNORECASE))

    return {
        'count': count,
        'total': len(paragraphs),
        'ratio': count / len(paragraphs) if paragraphs else 0,
    }


def analyze_environment(paragraphs):
    """Check for environmental/setting details."""

    env_words = [
        r'\b(room|hallway|street|building|house|office|space|place)\b',
        r'\b(window|door|wall|ceiling|floor|table|chair|desk)\b',
        r'\b(outside|inside|above|below|beyond|between)\b',
        r'\b(light|shadow|darkness|brightness|dim|glow)\b',
        r'\b(sound|noise|silence|quiet|echo)\b',
    ]

    pattern = '|'.join(env_words)
    count = sum(1 for p in paragraphs if re.search(pattern, p, re.IGNORECASE))

    return {
        'count': count,
        'total': len(paragraphs),
        'ratio': count / len(paragraphs) if paragraphs else 0,
    }


def analyze_parallelism(paragraphs):
    """Detect parallel construction (repeated sentence structures)."""

    # Look for paragraphs with repeated sentence starters or structures
    count = 0

    for para in paragraphs:
        sentences = re.split(r'[.!?]+', para)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) >= 2:
            # Check for repeated opening words
            openers = [s.split()[0] if s.split() else '' for s in sentences]
            if len(openers) != len(set(openers)):  # Repeated openers
                count += 1
                continue

            # Check for repeated syntactic patterns (crude heuristic)
            patterns = [' '.join(s.split()[:3]) if len(s.split()) >= 3 else s for s in sentences]
            if len(patterns) != len(set(patterns)):
                count += 1

    return {
        'count': count,
        'total': len(paragraphs),
        'ratio': count / len(paragraphs) if paragraphs else 0,
    }


def main():
    parser = argparse.ArgumentParser(description='Validate voice patterns in scene files')
    parser.add_argument('filepath', help='Path to scene markdown file')
    parser.add_argument('--thresholds', help='Custom thresholds (e.g., undermining:0.7,sensory:0.8)', default='')

    args = parser.parse_args()
    filepath = Path(args.filepath)

    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    # Parse custom thresholds if provided
    thresholds = DEFAULT_THRESHOLDS.copy()
    if args.thresholds:
        for pair in args.thresholds.split(','):
            key, val = pair.split(':')
            if key in thresholds:
                thresholds[key] = float(val)

    print(f"\n=== Voice Pattern Validation: {filepath.name} ===\n")

    results, issues, sentence_count, para_count = analyze_voice_patterns(filepath, thresholds)

    print(f"Total sentences: {sentence_count}")
    print(f"Total paragraphs: {para_count}\n")

    print("--- Pattern Density ---")
    for pattern, data in results.items():
        status = "✓" if data['ratio'] >= thresholds[pattern] else "✗"
        print(f"{status} {pattern.replace('_', ' ').title()}: "
              f"{data['ratio']:.1%} ({data['count']}/{data['total']}) "
              f"[expected: {thresholds[pattern]:.0%}+]")

    if not issues:
        print("\n✓ All voice patterns within expected range.\n")
    else:
        print("\n--- Issues Detected ---\n")
        for issue in sorted(issues, key=lambda x: x['severity'], reverse=True):
            print(f"[{issue['severity']}] {issue['pattern'].replace('_', ' ').title()}")
            print(f"  Expected: {issue['expected']:.0%}  |  Actual: {issue['actual']:.1%}")
            if issue['examples']:
                print("  Missing from:")
                for ex in issue['examples'][:2]:
                    print(f"    • {ex}")
            print()

    print()


if __name__ == '__main__':
    main()
