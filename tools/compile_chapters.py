#!/usr/bin/env python3
"""
Script to compile chapter draft files from individual scene files.
Reads all scene files in each chapter's scenes/ folder and combines them
into the CHxx_draft.md file.
"""

import os
import re
from pathlib import Path

def get_scene_number(filename):
    """Extract the scene number from filename like 'CH01-scene-01.md'"""
    match = re.match(r'CH\d+-scene-(\d+)', filename)
    if match:
        return int(match.group(1))
    return 999  # Put non-matching files at the end

def compile_chapter(chapter_dir):
    """Compile all scenes in a chapter directory into the draft file"""
    scenes_dir = chapter_dir / 'scenes'

    if not scenes_dir.exists():
        print(f"  WARNING: No scenes directory found in {chapter_dir.name}")
        return False

    # Get all .md files except .gitkeep
    scene_files = [f for f in scenes_dir.glob('*.md') if f.name != '.gitkeep']

    if not scene_files:
        print(f"  WARNING: No scene files found in {chapter_dir.name}/scenes")
        return False

    # Sort by scene number
    scene_files.sort(key=lambda x: get_scene_number(x.name))

    # Read and concatenate all scenes
    compiled_content = []
    for scene_file in scene_files:
        with open(scene_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                compiled_content.append(content)

    # Join scenes with double newline
    final_content = '\n\n\n'.join(compiled_content) + '\n'

    # Determine chapter number and draft filename
    chapter_match = re.match(r'ch(\d+)', chapter_dir.name)
    if chapter_match:
        chapter_num = chapter_match.group(1)
        draft_filename = f'CH{chapter_num}_draft.md'
    else:
        print(f"  WARNING: Could not determine chapter number from {chapter_dir.name}")
        return False

    draft_path = chapter_dir / draft_filename

    # Write the compiled content
    with open(draft_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"  ✓ Compiled {len(scene_files)} scenes into {draft_filename}")
    return True

def main():
    # Get the incarnations directory
    base_dir = Path(__file__).parent.parent / 'incarnations'

    if not base_dir.exists():
        print(f"ERROR: Directory not found: {base_dir}")
        return

    # Get all chapter directories (ch01, ch02, etc.)
    chapter_dirs = sorted([d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith('ch')])

    print(f"Found {len(chapter_dirs)} chapter directories")
    print("=" * 60)

    success_count = 0
    for chapter_dir in chapter_dirs:
        print(f"\nProcessing {chapter_dir.name}...")
        if compile_chapter(chapter_dir):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"\nCompleted: {success_count}/{len(chapter_dirs)} chapters updated successfully")

if __name__ == '__main__':
    main()
