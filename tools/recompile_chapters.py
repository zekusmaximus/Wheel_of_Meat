import os
import re
from pathlib import Path

def get_chapter_number(dir_name):
    """Extracts the 2-digit chapter number from directory name like 'ch01-name'."""
    match = re.search(r'ch(\d{2})', dir_name, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def recompile_chapters(base_dir):
    incarnations_dir = os.path.join(base_dir, 'incarnations')
    if not os.path.exists(incarnations_dir):
        print(f"Error: {incarnations_dir} not found.")
        return

    # Iterate through each chapter directory
    for chapter_dir in sorted(os.listdir(incarnations_dir)):
        chapter_path = os.path.join(incarnations_dir, chapter_dir)
        if not os.path.isdir(chapter_path):
            continue

        ch_num = get_chapter_number(chapter_dir)
        if not ch_num:
            continue

        scenes_dir = os.path.join(chapter_path, 'scenes')
        if not os.path.exists(scenes_dir):
            print(f"Skipping {chapter_dir}: No 'scenes' directory found.")
            continue

        # Find and sort scene files
        scene_files = []
        for f in os.listdir(scenes_dir):
            if f.startswith('scene-') and f.endswith('.md'):
                scene_files.append(f)
        
        # Sort numerically by the prefix (e.g., scene-01, scene-02)
        scene_files.sort()

        if not scene_files:
            print(f"Skipping {chapter_dir}: No scene files found in {scenes_dir}.")
            continue

        print(f"Compiling Chapter {ch_num} from {len(scene_files)} scenes...")

        compiled_content = []
        for i, scene_file in enumerate(scene_files):
            scene_path = os.path.join(scenes_dir, scene_file)
            with open(scene_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
                # We can add scene markers if desired, but for now we'll do clean concatenation
                # separated by two newlines as requested for "clean compilations".
                # If we want to add headers like "# Scene 1", we could do:
                # header = f"# Scene {i+1}: {scene_file.replace('scene-', '').replace('.md', '').replace('-', ' ').title()}\n\n"
                # But the user asked for "clean" drafts.
                
                compiled_content.append(content)

        # Join with three newlines (two blank lines) for clear separation
        final_draft = "\n\n\n".join(compiled_content) + "\n"

        # Output filename: CHxx_draft.md
        output_filename = f"CH{ch_num}_draft.md"
        output_path = os.path.join(chapter_path, output_filename)

        # Remove any existing incorrectly named draft files
        # (e.g., CH01-draft.md, ch23-draft.md, etc.)
        # ONLY remove if it has 'draft' in the name and matches the chapter number.
        for existing_file in os.listdir(chapter_path):
            lower_name = existing_file.lower()
            if f"ch{ch_num}" in lower_name and "draft" in lower_name and existing_file.endswith(".md"):
                if existing_file != output_filename:
                    old_path = os.path.join(chapter_path, existing_file)
                    print(f"  Removing old draft: {existing_file}")
                    os.remove(old_path)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_draft)
        
        print(f"  Saved to {output_filename}")

if __name__ == "__main__":
    project_root = r"c:\Users\zeke\Projects\Wheel_of_Meat"
    recompile_chapters(project_root)
