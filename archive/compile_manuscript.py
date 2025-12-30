#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Define chapter information
chapters_dir = Path("/home/user/Wheel_of_Meat/incarnations")
output_file = Path("/home/user/Wheel_of_Meat/manuscript_v2_partial.md")

# Map chapter numbers to their directory names
chapter_dirs = {
    1: "ch01-contemporary-manchester",
    2: "ch02-prehistoric-ka",
    3: "ch03-lilith-cp01",
    4: "ch04-mauryan-chandra",
    5: "ch05-lilith-cp02",
    6: "ch06-athens-philosopher",
    7: "ch07-lilith-cp03",
    8: "ch08-rome-investigator",
    9: "ch09-lilith-cp04",
    10: "ch10-egypt-hermit",
    11: "ch11-lilith-cp05",
    12: "ch12-heian-lover",
    13: "ch13-lilith-cp06",
    14: "ch14-inquisition-accused",
    15: "ch15-lilith-cp07",
    16: "ch16-renaissance-skeptic",
    17: "ch17-lilith-cp08",
    18: "ch18-taiping-rebel",
    19: "ch19-lilith-cp09",
    20: "ch20-noir-detective",
    21: "ch21-lilith-cp10",
}

def find_draft_file(chapter_num, chapter_dir):
    """Find the draft markdown file for a chapter."""
    dir_path = chapters_dir / chapter_dir

    # Look for CH0X_draft.md or CH0X_draft_v2.md
    padded_num = str(chapter_num).zfill(2)

    # Try different naming patterns
    patterns = [
        f"CH{padded_num}_draft.md",
        f"CH{padded_num}_draft_v2.md",
        f"CH{padded_num}-draft.md",
    ]

    for pattern in patterns:
        file_path = dir_path / pattern
        if file_path.exists():
            return file_path

    raise FileNotFoundError(f"Could not find draft file for chapter {chapter_num} in {dir_path}")

def extract_narrative(file_path):
    """Extract narrative text from chapter file, removing titles and metadata."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    narrative_lines = []
    skip_title = True

    for line in lines:
        # Skip title lines (lines starting with # or ## followed by "Chapter")
        if skip_title and (re.match(r'^#+\s+Chapter\s+', line, re.IGNORECASE) or
                          re.match(r'^#+\s+Complete Chapter', line, re.IGNORECASE)):
            continue

        # First non-title line marks end of title section
        if skip_title and line.strip() and not re.match(r'^#+', line):
            skip_title = False

        # Add non-title content
        if not (skip_title and (re.match(r'^#+', line) or line.strip() == "")):
            narrative_lines.append(line)
        elif not skip_title:
            narrative_lines.append(line)

    # Convert lines back to string and clean up
    text = '\n'.join(narrative_lines).strip()

    # Remove any leading horizontal rules
    text = re.sub(r'^\n*---\n*', '', text)

    # Remove trailing metadata sections (Word Count, etc.)
    # Find the last occurrence of content that looks like narrative
    # and remove everything after a metadata separator
    text = re.sub(r'\n*---\s*\n\*\*Word Count.*$', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\n*---\s*\n+$', '', text)

    return text.strip()

# Compile the manuscript
manuscript_parts = []

# Add title
manuscript_parts.append("The Wheel of Meat")
manuscript_parts.append("")
manuscript_parts.append("")

# Add all chapters
for chapter_num in range(1, 22):
    chapter_dir = chapter_dirs[chapter_num]

    try:
        draft_file = find_draft_file(chapter_num, chapter_dir)
        narrative = extract_narrative(draft_file)

        # Add chapter header
        manuscript_parts.append(f"Chapter {['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'Twenty-One'][chapter_num - 1]}")

        # Add narrative
        manuscript_parts.append(narrative)

        # Add blank line and divider
        manuscript_parts.append("")
        manuscript_parts.append("---")

        print(f"✓ Chapter {chapter_num}")
    except FileNotFoundError as e:
        print(f"✗ Chapter {chapter_num}: {e}")

# Write output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(manuscript_parts))

print(f"\n✓ Manuscript compiled to {output_file}")
print(f"  Total size: {output_file.stat().st_size / 1024:.1f} KB")
