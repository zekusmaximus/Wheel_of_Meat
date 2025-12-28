#!/usr/bin/env python3
"""
Manuscript Analyzer for The Wheel of Meat
Generates revision audit data including:
- Chapter word counts
- Chapter classification (Manchester/Historical/Lilith)
- Line-level tic analysis
- Summary-narrated moment extraction
"""

import re
import json
from pathlib import Path
from collections import defaultdict

MANUSCRIPT_PATH = Path("/home/user/Wheel_of_Meat/WOM_Manuscript_full.md")
OUTPUT_DIR = Path("/home/user/Wheel_of_Meat/out")

# Chapter metadata based on directory structure analysis
CHAPTER_METADATA = {
    1: {"name": "Contemporary Manchester", "type": "Manchester", "pov": "Silas/Lilith"},
    2: {"name": "Prehistoric Ka", "type": "Historical", "pov": "Ka"},
    3: {"name": "Lilith CP01", "type": "Lilith", "pov": "Lilith"},
    4: {"name": "Mauryan Chandra", "type": "Historical", "pov": "Chandra"},
    5: {"name": "Lilith CP02", "type": "Lilith", "pov": "Lilith"},
    6: {"name": "Athens Philosopher (Philon)", "type": "Historical", "pov": "Philon"},
    7: {"name": "Lilith CP03", "type": "Lilith", "pov": "Lilith"},
    8: {"name": "Rome Investigator (Verinus)", "type": "Historical", "pov": "Verinus"},
    9: {"name": "Lilith CP04", "type": "Lilith", "pov": "Lilith"},
    10: {"name": "Egypt Hermit (Macarius)", "type": "Historical", "pov": "Macarius"},
    11: {"name": "Lilith CP05", "type": "Lilith", "pov": "Lilith"},
    12: {"name": "Heian Lover (Kaoru)", "type": "Historical", "pov": "Kaoru"},
    13: {"name": "Lilith CP06", "type": "Lilith", "pov": "Lilith"},
    14: {"name": "Inquisition Accused (Diego)", "type": "Historical", "pov": "Diego de Lucena"},
    15: {"name": "Lilith CP07", "type": "Lilith", "pov": "Lilith"},
    16: {"name": "Renaissance Skeptic", "type": "Historical", "pov": "Unknown"},
    17: {"name": "Lilith CP08", "type": "Lilith", "pov": "Lilith"},
    18: {"name": "Taiping Rebel", "type": "Historical", "pov": "Unknown"},
    19: {"name": "Lilith CP09", "type": "Lilith", "pov": "Lilith"},
    20: {"name": "Noir Detective (Malone)", "type": "Historical", "pov": "Jack Malone"},
    21: {"name": "Lilith CP10", "type": "Lilith", "pov": "Lilith"},
    22: {"name": "Contemporary Breakthrough", "type": "Manchester", "pov": "Silas"},
    23: {"name": "Deva Celestial", "type": "Historical/Metaphysical", "pov": "Devaka"},
    24: {"name": "Future Prophet", "type": "Historical/Future", "pov": "Unknown"},
    25: {"name": "Space Explorer / Formless Realms", "type": "Metaphysical", "pov": "Merged"},
    26: {"name": "Pure Abodes Awakened", "type": "Climax", "pov": "Silas/Merged"},
}

WORD_TO_NUM = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
    'nineteen': 19, 'twenty': 20, 'twenty-one': 21, 'twenty-two': 22,
    'twenty-three': 23, 'twenty-four': 24, 'twenty-five': 25,
    'twenty-six': 26
}


def extract_chapters(content):
    """Extract chapters from manuscript content."""
    # Pattern to match chapter headings - more flexible
    chapter_pattern = r'^#\s+Chapter\s+(\S+(?:-\S+)?)'

    chapters = {}
    current_chapter = None
    current_content = []
    lines = content.split('\n')

    for i, line in enumerate(lines):
        match = re.match(chapter_pattern, line, re.IGNORECASE)
        if match:
            # Save previous chapter
            if current_chapter is not None:
                chapters[current_chapter] = '\n'.join(current_content)

            # Convert chapter number (handle "One", "Two", "Twenty-One", etc.)
            chapter_id = match.group(1).strip(':')
            try:
                current_chapter = int(chapter_id)
            except ValueError:
                # Convert word to number
                chapter_id_lower = chapter_id.lower()
                current_chapter = WORD_TO_NUM.get(chapter_id_lower, 0)
                if current_chapter == 0:
                    print(f"Warning: Could not parse chapter: {chapter_id}")
                    continue
            current_content = []
        elif current_chapter is not None:
            current_content.append(line)

    # Don't forget the last chapter
    if current_chapter is not None:
        chapters[current_chapter] = '\n'.join(current_content)

    return chapters


def count_words(text):
    """Count words in text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def analyze_tics(text):
    """Analyze line-level tics in text."""
    tics = {
        'particular': len(re.findall(r'\bparticular\b', text, re.IGNORECASE)),
        'something': len(re.findall(r'\bsomething\b', text, re.IGNORECASE)),
        'not_x_y_pattern': len(re.findall(r'\bnot\s+\w+\s*[-—]\s*\w+', text, re.IGNORECASE)),
        'em_dashes': len(re.findall(r'—', text)),
    }
    return tics


def calculate_abstraction_density(text):
    """Calculate abstraction density heuristics."""
    # Abstract nouns (common philosophical/abstract terms)
    abstract_nouns = [
        'consciousness', 'awareness', 'identity', 'existence', 'essence',
        'being', 'reality', 'illusion', 'truth', 'meaning', 'purpose',
        'soul', 'spirit', 'mind', 'thought', 'feeling', 'emotion',
        'understanding', 'wisdom', 'knowledge', 'insight', 'realization',
        'transformation', 'enlightenment', 'awakening', 'liberation',
        'attachment', 'desire', 'suffering', 'karma', 'dharma',
        'emptiness', 'nothingness', 'void', 'self', 'ego', 'nature',
        'recognition', 'fetter', 'fetters', 'pattern', 'framework'
    ]

    # Sensory verbs
    sensory_verbs = [
        'see', 'saw', 'seeing', 'sees', 'hear', 'heard', 'hearing', 'hears',
        'touch', 'touched', 'touching', 'touches', 'smell', 'smelled', 'smelling', 'smells',
        'taste', 'tasted', 'tasting', 'tastes', 'feel', 'felt', 'feeling', 'feels',
        'grip', 'gripped', 'gripping', 'grips', 'press', 'pressed', 'pressing', 'presses',
        'watch', 'watched', 'watching', 'watches', 'look', 'looked', 'looking', 'looks',
        'bite', 'bitten', 'biting', 'bites', 'grab', 'grabbed', 'grabbing', 'grabs'
    ]

    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)

    if word_count == 0:
        return 0

    abstract_count = sum(1 for w in words if w in abstract_nouns)
    sensory_count = sum(1 for w in words if w in sensory_verbs)

    # Abstraction density = (abstract - sensory) / total * 1000
    density = (abstract_count - sensory_count) / word_count * 1000
    return round(density, 2)


def find_pivotal_moments(content):
    """Find summary-narrated pivotal moments referenced in editor letter."""
    moments = {
        'devaka_betrayal': [],
        'lilith_first_intervention': [],
        'lilith_car_confession': [],
        'lilith_final_resistance': [],
        'stewart_rooftop_fall': []
    }

    # Search patterns for each moment
    patterns = {
        'devaka_betrayal': [
            r'.{0,200}devaka.{0,200}betray.{0,200}',
            r'.{0,200}betray.{0,200}devaka.{0,200}',
            r'.{0,200}conspirator.{0,100}inform.{0,200}'
        ],
        'lilith_first_intervention': [
            r'.{0,200}first.{0,50}interven.{0,200}',
            r'.{0,200}observation.{0,50}manipulat.{0,200}',
            r'.{0,200}began.{0,50}influenc.{0,200}'
        ],
        'lilith_car_confession': [
            r'.{0,200}car.{0,100}confess.{0,200}',
            r'.{0,200}didn\'t find you by accident.{0,200}',
            r'.{0,200}watching you.{0,100}long time.{0,200}'
        ],
        'lilith_final_resistance': [
            r'.{0,200}final.{0,50}resist.{0,200}',
            r'.{0,200}merge.{0,100}resist.{0,200}',
            r'.{0,200}before.{0,50}merge.{0,200}'
        ],
        'stewart_rooftop_fall': [
            r'.{0,200}stewart.{0,100}fall.{0,200}',
            r'.{0,200}rooftop.{0,100}stew.{0,200}',
            r'.{0,200}barrier.{0,100}gravity.{0,200}'
        ]
    }

    for moment, pats in patterns.items():
        for pat in pats:
            matches = re.findall(pat, content, re.IGNORECASE | re.DOTALL)
            for m in matches[:3]:  # Limit to 3 per pattern
                cleaned = re.sub(r'\s+', ' ', m.strip())[:300]
                if cleaned and cleaned not in moments[moment]:
                    moments[moment].append(cleaned)

    return moments


def main():
    print("Reading manuscript...")
    content = MANUSCRIPT_PATH.read_text(encoding='utf-8')

    print("Extracting chapters...")
    chapters = extract_chapters(content)

    print(f"Found {len(chapters)} chapters: {sorted(chapters.keys())}")

    # Analyze each chapter
    chapter_data = []
    total_words = 0

    for ch_num in sorted(chapters.keys()):
        ch_content = chapters[ch_num]
        words = count_words(ch_content)
        total_words += words
        tics = analyze_tics(ch_content)
        abstraction = calculate_abstraction_density(ch_content)

        meta = CHAPTER_METADATA.get(ch_num, {"name": f"Chapter {ch_num}", "type": "Unknown", "pov": "Unknown"})

        chapter_data.append({
            'chapter': ch_num,
            'name': meta['name'],
            'type': meta['type'],
            'pov': meta['pov'],
            'word_count': words,
            'tics': tics,
            'abstraction_density': abstraction
        })

    print(f"Total words: {total_words}")

    # Find pivotal moments
    print("Finding pivotal moments...")
    pivotal_moments = find_pivotal_moments(content)

    # Save results
    results = {
        'total_words': total_words,
        'chapters': chapter_data,
        'pivotal_moments': pivotal_moments
    }

    output_file = OUTPUT_DIR / "revision_audit" / "analysis_data.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Analysis saved to {output_file}")

    # Print summary
    print("\n=== CHAPTER SUMMARY ===")
    print(f"{'Ch':<4} {'Name':<35} {'Type':<20} {'Words':>8} {'Abstraction':>12}")
    print("-" * 85)

    for ch in chapter_data:
        print(f"{ch['chapter']:<4} {ch['name'][:33]:<35} {ch['type'][:18]:<20} {ch['word_count']:>8} {ch['abstraction_density']:>12}")

    print("-" * 85)
    print(f"{'TOTAL':<60} {total_words:>8}")

    # Word count by type
    print("\n=== WORD COUNT BY TYPE ===")
    by_type = defaultdict(int)
    for ch in chapter_data:
        by_type[ch['type']] += ch['word_count']

    for t, wc in sorted(by_type.items(), key=lambda x: -x[1]):
        pct = wc / total_words * 100
        print(f"{t:<25} {wc:>8} words ({pct:.1f}%)")

    # Tic summary
    print("\n=== TIC SUMMARY (Top 10 by total tics) ===")
    tic_totals = []
    for ch in chapter_data:
        total_tics = sum(ch['tics'].values())
        tic_totals.append((ch['chapter'], ch['name'], total_tics, ch['tics']))

    tic_totals.sort(key=lambda x: -x[2])
    for ch_num, name, total, tics in tic_totals[:10]:
        print(f"Ch{ch_num}: {name[:25]:<25} - {total} total (particular:{tics['particular']}, something:{tics['something']}, not-x-y:{tics['not_x_y_pattern']}, em-dash:{tics['em_dashes']})")

    # Abstraction density ranking
    print("\n=== TOP 10 CHAPTERS BY ABSTRACTION DENSITY ===")
    abstraction_ranked = sorted(chapter_data, key=lambda x: -x['abstraction_density'])
    for ch in abstraction_ranked[:10]:
        print(f"Ch{ch['chapter']}: {ch['name'][:30]:<30} - density: {ch['abstraction_density']}")

    return results


if __name__ == "__main__":
    main()
