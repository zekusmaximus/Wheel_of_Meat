#!/usr/bin/env python3
"""
Revision Prompt Generator for The Wheel of Meat
================================================
Generates formatted revision prompts from prose analysis for author review.
Does NOT auto-apply changes - outputs prompts only.

Usage:
    python revision_prompt_generator.py [scene_path]
    python revision_prompt_generator.py --chapter [chapter_num]
    python revision_prompt_generator.py --all

Output:
    /out/revision_prompts/[chapter]/[scene].md
"""

import re
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple

# ============================================================================
# CONFIGURATION
# ============================================================================

BASE_DIR = Path(__file__).parent.parent.resolve()
INCARNATIONS_DIR = BASE_DIR / "incarnations"
OUTPUT_DIR = BASE_DIR / "out" / "revision_prompts"

# Prose tic patterns (from prose_tic_analyzer.py)
ABSTRACT_NOUNS = {
    'certainty', 'fear', 'recognition', 'awareness', 'understanding',
    'realization', 'knowledge', 'thought', 'feeling', 'emotion',
    'memory', 'doubt', 'confusion', 'clarity', 'truth', 'insight',
    'consciousness', 'comprehension', 'perception', 'sensation',
    'anxiety', 'dread', 'hope', 'despair', 'grief', 'joy',
    'terror', 'panic', 'relief', 'shame', 'guilt', 'pride',
    'anger', 'rage', 'calm', 'peace', 'tension', 'pressure'
}

PHYSICAL_VERBS = {
    'dissolved', 'dissolve', 'dissolves', 'dissolving',
    'moved', 'move', 'moves', 'moving',
    'settled', 'settle', 'settles', 'settling',
    'grew', 'grow', 'grows', 'growing',
    'spread', 'spreads', 'spreading',
    'crystallized', 'crystallize', 'crystallizes', 'crystallizing',
    'swept', 'sweep', 'sweeps', 'sweeping',
    'washed', 'wash', 'washes', 'washing',
    'rushed', 'rush', 'rushes', 'rushing',
    'flooded', 'flood', 'floods', 'flooding'
}

# Forbidden patterns
EMOTION_WORDS = [
    'afraid', 'angry', 'sad', 'happy', 'anxious', 'nervous', 'excited',
    'worried', 'relieved', 'frustrated', 'confused', 'surprised', 'lonely',
    'guilty', 'ashamed', 'proud', 'jealous', 'hopeful', 'desperate'
]

BUDDHIST_TERMS = [
    'dharma', 'karma', 'samsara', 'nirvana', 'enlightenment', 'attachment',
    'suffering', 'awakening', 'meditation', 'mindfulness', 'rebirth',
    'reincarnation'
]

FILTER_VERBS = [
    'saw', 'felt', 'noticed', 'realized', 'thought', 'knew',
    'wondered', 'decided', 'remembered'
]

# ============================================================================
# PROMPT CLASSES
# ============================================================================

class RevisionPrompt:
    """Single revision prompt."""

    def __init__(self, pass_name: str, chapter: int, scene: str, line_num: int,
                 original: str, issue: str, proposed: str, rationale: str):
        self.pass_name = pass_name
        self.chapter = chapter
        self.scene = scene
        self.line_num = line_num
        self.original = original
        self.issue = issue
        self.proposed = proposed
        self.rationale = rationale

    def to_markdown(self) -> str:
        return f"""### REVISION PROMPT: {self.pass_name}
**Chapter:** {self.chapter} | **Scene:** {self.scene}
**Line:** {self.line_num}

**ORIGINAL:**
> {self.original}

**ISSUE:**
{self.issue}

**PROPOSED REVISION:**
> {self.proposed}

**RATIONALE:**
{self.rationale}

---
"""


class SceneAnalysis:
    """Analysis results for a single scene."""

    def __init__(self, chapter: int, scene_file: str, scene_path: Path):
        self.chapter = chapter
        self.scene_file = scene_file
        self.scene_path = scene_path
        self.prompts: List[RevisionPrompt] = []
        self.word_count = 0

    def add_prompt(self, prompt: RevisionPrompt):
        self.prompts.append(prompt)

    def to_markdown(self) -> str:
        lines = [
            f"# Revision Prompts: Chapter {self.chapter} - {self.scene_file}",
            f"",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"**Word Count:** {self.word_count}",
            f"**Total Issues:** {len(self.prompts)}",
            f"",
            f"---",
            f""
        ]

        if not self.prompts:
            lines.append("*No issues found in this scene.*")
        else:
            # Group by pass
            by_pass: Dict[str, List[RevisionPrompt]] = {}
            for prompt in self.prompts:
                if prompt.pass_name not in by_pass:
                    by_pass[prompt.pass_name] = []
                by_pass[prompt.pass_name].append(prompt)

            for pass_name, prompts in by_pass.items():
                lines.append(f"## {pass_name} ({len(prompts)} issues)")
                lines.append("")
                for prompt in prompts:
                    lines.append(prompt.to_markdown())

        return "\n".join(lines)


# ============================================================================
# ANALYSIS FUNCTIONS
# ============================================================================

def get_context(lines: List[str], line_idx: int, context_lines: int = 1) -> str:
    """Get surrounding context for a line."""
    start = max(0, line_idx - context_lines)
    end = min(len(lines), line_idx + context_lines + 1)
    return " ".join(lines[start:end]).strip()


def analyze_prose_tics(lines: List[str], chapter: int, scene: str) -> List[RevisionPrompt]:
    """Analyze for prose tics (Pass 1)."""
    prompts = []

    for i, line in enumerate(lines, 1):
        # Check for "the particular [noun]"
        matches = re.finditer(r'\bthe particular (\w+)', line, re.IGNORECASE)
        for match in matches:
            noun = match.group(1)
            prompts.append(RevisionPrompt(
                pass_name="Prose Tic Scan",
                chapter=chapter,
                scene=scene,
                line_num=i,
                original=line.strip(),
                issue=f'"The particular {noun}" - unnecessary intensifier',
                proposed=f'Option 1: Remove "particular" → "the {noun}"\nOption 2: Use specific descriptor → "the [specific] {noun}"',
                rationale='"Particular" adds no specificity. Replace with concrete descriptor or simplify.'
            ))

        # Check for vague "something"
        something_patterns = [
            (r'\bsomething (\w+ed|moved|shifted|changed)\b', 'something + verb'),
            (r'\bsomething (in|about|within) ', 'something in/about'),
            (r'\bsomething like\b', 'something like')
        ]
        for pattern, desc in something_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                prompts.append(RevisionPrompt(
                    pass_name="Prose Tic Scan",
                    chapter=chapter,
                    scene=scene,
                    line_num=i,
                    original=line.strip(),
                    issue=f'Vague "{desc}" construction',
                    proposed='Name the specific referent instead of using "something"',
                    rationale='Vague constructions distance the reader. Name the thing.'
                ))
                break  # Only one per line

        # Check for abstract nouns with physical verbs
        words = line.lower().split()
        for j in range(len(words) - 1):
            word = re.sub(r'[^\w]', '', words[j])
            next_word = re.sub(r'[^\w]', '', words[j + 1])
            if word in ABSTRACT_NOUNS and next_word in PHYSICAL_VERBS:
                prompts.append(RevisionPrompt(
                    pass_name="Prose Tic Scan",
                    chapter=chapter,
                    scene=scene,
                    line_num=i,
                    original=line.strip(),
                    issue=f'Abstract noun "{word}" performing physical action "{next_word}"',
                    proposed='Rephrase with human subject or concrete imagery',
                    rationale='Abstract nouns should not perform physical actions. Ground in body/character.'
                ))
                break

    # Check em-dash density per paragraph
    text = "\n".join(lines)
    paragraphs = text.split("\n\n")
    current_line = 1
    for para in paragraphs:
        em_dash_count = para.count('—')
        if em_dash_count > 4:
            prompts.append(RevisionPrompt(
                pass_name="Prose Tic Scan",
                chapter=chapter,
                scene=scene,
                line_num=current_line,
                original=f"[Paragraph with {em_dash_count} em-dashes]",
                issue=f'Em-dash excess: {em_dash_count} em-dashes ({em_dash_count//2} pairs) in one paragraph',
                proposed='Convert some em-dash pairs to periods, semicolons, or commas',
                rationale='Excessive em-dashes fragment rhythm. Vary punctuation.'
            ))
        current_line += len(para.split('\n'))

    return prompts


def analyze_forbidden_patterns(lines: List[str], chapter: int, scene: str) -> List[RevisionPrompt]:
    """Analyze for forbidden patterns (Pass 2)."""
    prompts = []

    for i, line in enumerate(lines, 1):
        line_lower = line.lower()

        # Check emotion words
        for word in EMOTION_WORDS:
            if re.search(rf'\b{word}\b', line_lower):
                prompts.append(RevisionPrompt(
                    pass_name="Forbidden Pattern Audit",
                    chapter=chapter,
                    scene=scene,
                    line_num=i,
                    original=line.strip(),
                    issue=f'INVIOLABLE: Abstract emotion word "{word}"',
                    proposed='Replace with physical sensation, action, or environmental description',
                    rationale='Abstract emotion words are forbidden. Show through body, not label.'
                ))

        # Check Buddhist terms
        for term in BUDDHIST_TERMS:
            if re.search(rf'\b{term}\b', line_lower):
                prompts.append(RevisionPrompt(
                    pass_name="Forbidden Pattern Audit",
                    chapter=chapter,
                    scene=scene,
                    line_num=i,
                    original=line.strip(),
                    issue=f'INVIOLABLE: Buddhist terminology "{term}"',
                    proposed='Remove or replace with experiential description',
                    rationale='Buddhist terminology is forbidden. Show through experience; reader infers.'
                ))

        # Check filter verbs (context-dependent - flag for review)
        for verb in FILTER_VERBS:
            if re.search(rf'\b(he|she|they|I)\s+{verb}\b', line_lower):
                prompts.append(RevisionPrompt(
                    pass_name="Forbidden Pattern Audit",
                    chapter=chapter,
                    scene=scene,
                    line_num=i,
                    original=line.strip(),
                    issue=f'Filter verb "{verb}" - distances reader from experience',
                    proposed='Remove filter and show directly, OR keep if perception itself matters',
                    rationale='Filter verbs add distance. Remove unless perception itself is the point.'
                ))

    return prompts


def analyze_sensory_coverage(lines: List[str], chapter: int, scene: str) -> List[RevisionPrompt]:
    """Analyze for sensory gaps (Pass 4)."""
    prompts = []

    text = " ".join(lines)
    word_count = len(text.split())

    # Simple heuristic checks for senses
    senses = {
        'sight': r'\b(saw|see|seeing|looked|look|watch|watched|gaze|gazed|glimpse|glimpsed|visible|bright|dark|light|shadow|color|colours?)\b',
        'sound': r'\b(heard|hear|hearing|sound|sounds|voice|voices|noise|silent|silence|loud|quiet|whisper|whispered|echo|echoed)\b',
        'smell': r'\b(smell|smelled|smelt|scent|odor|aroma|fragrant|stench|nose)\b',
        'taste': r'\b(taste|tasted|tasting|flavor|flavour|bitter|sweet|sour|salty|tongue|mouth)\b',
        'touch': r'\b(felt|feel|feeling|touch|touched|touching|cold|warm|hot|cool|rough|smooth|soft|hard|texture|skin|fingers|hands)\b'
    }

    missing = []
    for sense, pattern in senses.items():
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(sense)

    if len(missing) >= 2:
        prompts.append(RevisionPrompt(
            pass_name="Sensory Audit",
            chapter=chapter,
            scene=scene,
            line_num=1,
            original="[Scene-level audit]",
            issue=f'Missing senses: {", ".join(missing)}',
            proposed=f'Add sensory details for: {", ".join(missing)}',
            rationale='All five senses should be present in every scene. Add period-appropriate details.'
        ))

    return prompts


def analyze_scene(scene_path: Path) -> Optional[SceneAnalysis]:
    """Analyze a single scene file."""
    if not scene_path.exists():
        print(f"  [SKIP] Scene not found: {scene_path}")
        return None

    # Extract chapter number from path
    # Expected: incarnations/ch01-xxx/scenes/scene-01-yyy.md
    chapter_match = re.search(r'ch(\d+)', str(scene_path))
    if not chapter_match:
        print(f"  [SKIP] Cannot determine chapter: {scene_path}")
        return None

    chapter = int(chapter_match.group(1))
    scene_file = scene_path.name

    # Read scene
    with open(scene_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    # Create analysis
    analysis = SceneAnalysis(chapter, scene_file, scene_path)
    analysis.word_count = len(content.split())

    # Run passes
    analysis.prompts.extend(analyze_prose_tics(lines, chapter, scene_file))
    analysis.prompts.extend(analyze_forbidden_patterns(lines, chapter, scene_file))
    analysis.prompts.extend(analyze_sensory_coverage(lines, chapter, scene_file))

    return analysis


# ============================================================================
# OUTPUT FUNCTIONS
# ============================================================================

def save_analysis(analysis: SceneAnalysis):
    """Save analysis to output directory."""
    chapter_dir = OUTPUT_DIR / f"ch{analysis.chapter:02d}"
    chapter_dir.mkdir(parents=True, exist_ok=True)

    output_file = chapter_dir / f"{analysis.scene_file.replace('.md', '_prompts.md')}"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(analysis.to_markdown())

    print(f"  [OK] {analysis.scene_file}: {len(analysis.prompts)} prompts → {output_file}")


def find_scenes_in_chapter(chapter_num: int) -> List[Path]:
    """Find all scene files in a chapter."""
    chapter_dirs = list(INCARNATIONS_DIR.glob(f"ch{chapter_num:02d}-*/scenes"))
    scenes = []
    for scene_dir in chapter_dirs:
        scenes.extend(sorted(scene_dir.glob("scene-*.md")))
    return scenes


def find_all_scenes() -> List[Path]:
    """Find all scene files."""
    scenes = []
    for chapter_dir in sorted(INCARNATIONS_DIR.glob("ch*")):
        scenes_dir = chapter_dir / "scenes"
        if scenes_dir.exists():
            scenes.extend(sorted(scenes_dir.glob("scene-*.md")))
    return scenes


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate revision prompts for scene files"
    )
    parser.add_argument('scene_path', nargs='?', help='Path to specific scene file')
    parser.add_argument('--chapter', '-c', type=int, help='Analyze all scenes in chapter')
    parser.add_argument('--all', '-a', action='store_true', help='Analyze all scenes')

    args = parser.parse_args()

    print("=" * 60)
    print("REVISION PROMPT GENERATOR - The Wheel of Meat")
    print("=" * 60)
    print()

    scenes_to_analyze = []

    if args.scene_path:
        scenes_to_analyze = [Path(args.scene_path)]
    elif args.chapter:
        scenes_to_analyze = find_scenes_in_chapter(args.chapter)
        print(f"Found {len(scenes_to_analyze)} scenes in chapter {args.chapter}")
    elif args.all:
        scenes_to_analyze = find_all_scenes()
        print(f"Found {len(scenes_to_analyze)} scenes total")
    else:
        parser.print_help()
        return 1

    print()

    total_prompts = 0
    for scene_path in scenes_to_analyze:
        analysis = analyze_scene(scene_path)
        if analysis:
            save_analysis(analysis)
            total_prompts += len(analysis.prompts)

    print()
    print("=" * 60)
    print(f"COMPLETE: {len(scenes_to_analyze)} scenes analyzed, {total_prompts} prompts generated")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
