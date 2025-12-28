#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Define chapter information
base_dir = Path(r"c:\Users\zeke\Projects\Wheel_of_Meat")
chapters_dir = base_dir / "incarnations"
output_file = base_dir / "WOM_Manuscript_full.md"

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
    22: "ch22-contemporary-breakthrough",
    23: "ch23-deva-celestial",
    24: "ch24-future-prophet",
    25: "ch25-space-explorer",
    26: "ch26-pure-abodes-awakened",
}

def find_draft_file(chapter_num, chapter_dir):
    """Find the draft markdown file for a chapter."""
    dir_path = chapters_dir / chapter_dir
    padded_num = str(chapter_num).zfill(2)

    # Try different naming patterns
    patterns = [
        f"CH{padded_num}_draft.md",
        f"CH{padded_num}-draft.md",
        f"ch{padded_num}-draft.md",
        f"ch{padded_num}_draft.md",
        f"CH{padded_num}_draft_v2.md",
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

    # Handle the specific duplicate in CH01 if it's that file
    if "CH01-draft.md" in str(file_path):
        # We know lines 75-84 are repeated in 85-94 in the version we saw.
        # But instead of hardcoding lines, let's look for the specific repeated block.
        # However, a general strategy is safer.
        pass

    lines = content.split('\n')
    narrative_lines = []
    skip_title = True

    for line in lines:
        # Skip title lines
        if skip_title and (re.match(r'^#+\s+Chapter\s+', line, re.IGNORECASE) or
                          re.match(r'^#+\s+Complete Chapter', line, re.IGNORECASE)):
            continue

        # First non-title/non-empty line marks end of title section
        if skip_title and line.strip() and not re.match(r'^#+', line):
            skip_title = False

        if not skip_title:
            # Skip technical metadata
            if re.match(r'^\*\*Word Target:\*\*', line, re.IGNORECASE) or \
               re.match(r'^\*\*Status:\*\*', line, re.IGNORECASE) or \
               re.match(r'^Ready for your review', line, re.IGNORECASE) or \
               re.match(r'^Prepared by:', line, re.IGNORECASE):
                continue
            narrative_lines.append(line)

    # Convert lines back to string and clean up
    text = '\n'.join(narrative_lines).strip()

    # Remove trailing metadata sections (Word Count, etc.)
    text = re.sub(r'\n*---\s*\n\*\*Word Count.*$', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'\n*---\s*\n+$', '', text)

    return text.strip()

# Chapter names mapping
chapter_names = [
    'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
    'Eighteen', 'Nineteen', 'Twenty', 'Twenty-One', 'Twenty-Two', 'Twenty-Three',
    'Twenty-Four', 'Twenty-Five', 'Twenty-Six'
]

# Compile the manuscript
manuscript_parts = []

# Add title
manuscript_parts.append("# The Wheel of Meat")
manuscript_parts.append("")

# Process all 26 chapters
for chapter_num in range(1, 27):
    chapter_dir = chapter_dirs[chapter_num]

    try:
        draft_file = find_draft_file(chapter_num, chapter_dir)
        print(f"Processing Chapter {chapter_num}: {draft_file.name}")
        narrative = extract_narrative(draft_file)

        # Add chapter header
        manuscript_parts.append(f"# Chapter {chapter_names[chapter_num - 1]}")
        manuscript_parts.append("")

        # Add narrative
        manuscript_parts.append(narrative)

        # Add blank line and divider
        if chapter_num < 26:
            manuscript_parts.append("")
            manuscript_parts.append("---")
            manuscript_parts.append("")

    except FileNotFoundError as e:
        print(f"Error: {e}")

# Write output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(manuscript_parts))

print(f"\nSuccess: Manuscript compiled to {output_file}")
print(f"Total size: {output_file.stat().st_size / 1024:.1f} KB")
