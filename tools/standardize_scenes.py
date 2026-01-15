import os
import re
import sys
from pathlib import Path

def standardize_file(file_path, dry_run=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    clean_lines = []
    in_header = True
    for line in lines:
        if in_header:
            # Skip metadata and scene headers
            if re.match(r'^# Scene|^---+$|\*\*Chapter:|\*\*Section:|\*\*Word|\*\*Status:|Ready for review', line, re.IGNORECASE):
                continue
            # If we hit an empty line while in header, stay in header but skip the empty line
            if line.strip() == "":
                continue
            # First line that isn't a header/metadata means we are in the prose
            in_header = False
        clean_lines.append(line)
    prose = "\n".join(clean_lines)

    # Normalize whitespace
    prose = prose.strip()
    
    if not prose:
        return False, "Empty prose"

    # Split into paragraphs and rebuild with single blank line
    # We want to keep blocks of text together but ensure a blank line between them.
    # Simple strategy: split by multiple newlines, then rejoin with \n\n
    paragraphs = re.split(r'\n\s*\n', prose)
    cleaned_paragraphs = []
    for p in paragraphs:
        p_strip = p.strip()
        if p_strip:
            # Within a paragraph, we should keep the lines together but maybe normalize them?
            # User wants "Markdown paragraph formatting (blank line between every paragraph)"
            # Usually this means a block of text.
            cleaned_paragraphs.append(p_strip)
            
    final_output = "\n\n".join(cleaned_paragraphs) + "\n"

    if dry_run:
        print(f"--- DRY RUN: {file_path} ---")
        print(final_output[:200] + "...")
        print("--- END DRY RUN ---")
        return True, "Dry run successful"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    return True, "File standardized"

def main():
    base_dir = Path(__file__).parent.parent / 'incarnations'
    count = 0
    dry_run = "--dry-run" in sys.argv
    
    if dry_run:
        print("Running in DRY RUN mode. No files will be changed.")

    for root, dirs, files in os.walk(base_dir):
        if "scenes" in root.lower():
            for file in files:
                if file.endswith(".md") and not file.startswith("."):
                    file_path = os.path.join(root, file)
                    success, msg = standardize_file(file_path, dry_run=dry_run)
                    if success:
                        print(f"Processed: {file_path}")
                        count += 1
                    else:
                        print(f"Skipped: {file_path} ({msg})")

    print(f"\nTotal files processed: {count}")

if __name__ == "__main__":
    main()
