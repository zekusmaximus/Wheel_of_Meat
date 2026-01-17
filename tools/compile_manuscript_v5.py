import os
import re

def compile_chapters(base_dir):
    incarnations_dir = os.path.join(base_dir, 'incarnations')
    chapter_folders = sorted([f for f in os.listdir(incarnations_dir) if f.startswith('ch') and os.path.isdir(os.path.join(incarnations_dir, f))])
    
    for folder in chapter_folders:
        ch_num = folder.split('-')[0].replace('ch', '')
        scenes_dir = os.path.join(incarnations_dir, folder, 'scenes')
        if not os.path.exists(scenes_dir):
            print(f"Skipping {folder}: scenes dir not found.")
            continue
        
        scene_files = sorted([f for f in os.listdir(scenes_dir) if f.endswith('.md') and 'scene' in f.lower()])
        chapter_content = []
        
        for scene_file in scene_files:
            file_path = os.path.join(scenes_dir, scene_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    chapter_content.append(content)
        
        output_filename = f"CH{ch_num}_draft.md"
        output_path = os.path.join(incarnations_dir, folder, output_filename)
        
        # Join with double newlines for clear separation
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(chapter_content))
        print(f"Updated {output_path}")

def assemble_manuscript(base_dir, output_file):
    incarnations_dir = os.path.join(base_dir, 'incarnations')
    chapter_folders = sorted([f for f in os.listdir(incarnations_dir) if f.startswith('ch') and os.path.isdir(os.path.join(incarnations_dir, f))])
    
    manuscript = []
    manuscript.append("# THE WHEEL OF MEAT")
    
    # Act 1: Chapter 1
    manuscript.append("\n## ACT 1")
    manuscript.append("\n### CHAPTER ONE")
    ch01_path = os.path.join(incarnations_dir, chapter_folders[0], "CH01_draft.md")
    with open(ch01_path, 'r', encoding='utf-8') as f:
        manuscript.append(f.read())
    
    # Act 2: Chapters 2-21
    manuscript.append("\n## ACT 2")
    for i in range(1, 21): # Folders 1 to 20 (ch02 to ch21)
        folder = chapter_folders[i]
        ch_num_str = folder.split('-')[0].replace('ch', '')
        ch_num_int = int(ch_num_str)
        # Convert to word if possible or keep as numbers? User said "CHAPTER TWO" in example but "Consists of 2 through 21". 
        # I'll use cardinal words for headers if easily mappable, or stick to Roman numerals/digits. 
        # User example: "CHAPTER ONE", "ACT 2", "CHAPTER 22". 
        # I'll use digits for 2-21 to be safe, unless I should follow "CHAPTER ONE" style.
        # Let's use words for consistency with "CHAPTER ONE" if I can.
        
        from num2words import num2words
        try:
            ch_word = num2words(ch_num_int).upper()
        except ImportError:
            ch_word = str(ch_num_int)
            
        manuscript.append(f"\n### CHAPTER {ch_word}")
        draft_file = f"CH{ch_num_str}_draft.md"
        draft_path = os.path.join(incarnations_dir, folder, draft_file)
        with open(draft_path, 'r', encoding='utf-8') as f:
            manuscript.append(f.read())

    # Act 3: Chapter 22
    manuscript.append("\n## ACT 3")
    manuscript.append("\n### CHAPTER TWENTY-TWO") 
    ch22_path = os.path.join(incarnations_dir, chapter_folders[21], "CH22_draft.md")
    with open(ch22_path, 'r', encoding='utf-8') as f:
        manuscript.append(f.read())
        
    # Act 4: Chapters 23-26
    manuscript.append("\n## ACT 4")
    for i in range(22, 26): # Folders 22 to 25 (ch23 to ch26)
        folder = chapter_folders[i]
        ch_num_str = folder.split('-')[0].replace('ch', '')
        ch_num_int = int(ch_num_str)
        try:
            ch_word = num2words(ch_num_int).upper()
        except ImportError:
            ch_word = str(ch_num_int)
            
        manuscript.append(f"\n### CHAPTER {ch_word}")
        draft_file = f"CH{ch_num_str}_draft.md"
        draft_path = os.path.join(incarnations_dir, folder, draft_file)
        with open(draft_path, 'r', encoding='utf-8') as f:
            manuscript.append(f.read())

    final_content = '\n\n'.join(manuscript)
    
    # UTF-8 Cleanup: Ensure only valid UTF-8 and address common problematic symbols if needed.
    # The requirement is "ONLY UTF-8 compliant symbols". 
    # Most modern text is UTF-8. Pandoc specifically handles smart quotes etc but user wants "clean compilations".
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Full manuscript compiled to {output_file}")

if __name__ == "__main__":
    import sys
    # Add num2words if possible, otherwise fallback
    try:
        from num2words import num2words
    except ImportError:
        def num2words(n): return str(n)
        
    base = r"c:\Users\zeke\Projects\Wheel_of_Meat"
    output = os.path.join(base, "manuscript_draft1_16_26.md")
    
    compile_chapters(base)
    assemble_manuscript(base, output)
