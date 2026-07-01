import os
import sys
from pathlib import Path

CHAPTER_WORDS = [
    'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN',
    'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN',
    'EIGHTEEN', 'NINETEEN', 'TWENTY', 'TWENTY-ONE', 'TWENTY-TWO', 'TWENTY-THREE',
    'TWENTY-FOUR', 'TWENTY-FIVE', 'TWENTY-SIX',
]


def chapter_word(n):
    return CHAPTER_WORDS[n - 1]


def assemble_manuscript(base_dir, output_file):
    incarnations_dir = os.path.join(base_dir, 'incarnations')
    chapter_folders = sorted(
        f for f in os.listdir(incarnations_dir)
        if f.startswith('ch') and os.path.isdir(os.path.join(incarnations_dir, f))
    )

    manuscript = ["# THE WHEEL OF MEAT"]

    def add_chapter(folder, ch_word):
        ch_num_str = folder.split('-')[0].replace('ch', '')
        manuscript.append(f"\n### CHAPTER {ch_word}")
        draft_path = os.path.join(incarnations_dir, folder, f"CH{ch_num_str}_draft.md")
        with open(draft_path, 'r', encoding='utf-8') as f:
            manuscript.append(f.read())

    # Act I: Chapter 1
    manuscript.append("\n## ACT 1")
    add_chapter(chapter_folders[0], chapter_word(1))

    # Act II: Chapters 2-21
    manuscript.append("\n## ACT 2")
    for i in range(1, 21):
        ch_num_int = int(chapter_folders[i].split('-')[0].replace('ch', ''))
        add_chapter(chapter_folders[i], chapter_word(ch_num_int))

    # Act III: Chapter 22
    manuscript.append("\n## ACT 3")
    add_chapter(chapter_folders[21], chapter_word(22))

    # Act IV: Chapters 23-26
    manuscript.append("\n## ACT 4")
    for i in range(22, 26):
        ch_num_int = int(chapter_folders[i].split('-')[0].replace('ch', ''))
        add_chapter(chapter_folders[i], chapter_word(ch_num_int))

    final_content = '\n\n'.join(manuscript)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Full manuscript compiled to {output_file}")


if __name__ == "__main__":
    base = Path(__file__).parent.parent
    output_name = sys.argv[1] if len(sys.argv) > 1 else "manuscript_draft_7_26.md"
    output = base / output_name

    assemble_manuscript(str(base), str(output))
