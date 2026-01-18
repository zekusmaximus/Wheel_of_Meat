import argparse
import re
from pathlib import Path

SENSORY_WORDS = [
    # touch/weight/space
    "weight",
    "edge","edges",
    "surface","surfaces",
    "tremor","tremors",
    "shiver","shivers",
    "vibration","vibrations",
    "oscillation","oscillations",
    "pulse","pulses",
    "pressure",
    "gravity","floor","wall","stone","cave","glass","wood","earth",
    # body
    "body","bodies","skin","muscle","lungs","breath","mouth","tongue","hand","hands","feet","foot",
    "finger","fingers","heart","heartbeat","limb",
    # temperature/light/dark
    "warm","heat","cold","light","dark","shadow",
    # sound/voice
    "sound","voice","voices","echo","echoes",
    # fluids
    "water","pool","drain",
    # motion/objects
    "fist","spear","ring",
]


def split_sentences(text: str) -> list[str]:
    # Heuristic split: keep em-dash and punctuation as boundaries, also split on blanklines.
    parts = re.split(r"(?<=[.!?])\s+|\n{2,}", text)
    sentences: list[str] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # further split long lines on single newlines
        for sub in re.split(r"\n+", part):
            sub = sub.strip()
            if sub:
                sentences.append(sub)
    return sentences


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="manuscript_draft1_17_26.md")
    ap.add_argument("--start", type=int, required=True, help="1-based start line (inclusive)")
    ap.add_argument("--end", type=int, required=True, help="1-based end line (inclusive)")
    ap.add_argument("--show", type=int, default=0, help="show N example sensory + abstract sentences")
    args = ap.parse_args()

    path = Path(args.file)
    lines = path.read_text(encoding="utf-8").splitlines()
    start = max(1, args.start)
    end = min(len(lines), args.end)

    chunk = "\n".join(lines[start - 1 : end])

    lex = sorted(set(SENSORY_WORDS), key=len, reverse=True)
    pattern = re.compile(r"\b(" + "|".join(re.escape(w) for w in lex) + r")\b", re.IGNORECASE)

    sentences = split_sentences(chunk)
    sensory = []
    abstract = []
    hit_counts: dict[str, int] = {}
    for s in sentences:
        hits = pattern.findall(s)
        if hits:
            sensory.append(s)
            for h in hits:
                key = h.lower()
                hit_counts[key] = hit_counts.get(key, 0) + 1
        else:
            abstract.append(s)

    print(f"Range: lines {start}-{end} ({path})")
    print("Sentence counts:")
    print(f"  total: {len(sentences)}")
    print(f"  sensory/concrete: {len(sensory)}")
    print(f"  abstract/non-sensory: {len(abstract)}")
    if abstract:
        print(f"  ratio sensory:abstract = {len(sensory)/len(abstract):.2f}:1")

    words = re.findall(r"[A-Za-z']+", chunk)
    word_total = len(words)
    word_sensory_hits = sum(1 for w in words if pattern.search(w))
    print("\nWord counts (rough):")
    print(f"  total words: {word_total}")
    print(f"  sensory token hits: {word_sensory_hits}")

    if args.show:
        print("\nExamples (sensory/concrete):")
        for s in sensory[: args.show]:
            print("-", s)
        print("\nExamples (abstract/non-sensory):")
        for s in abstract[: args.show]:
            print("-", s)

    if hit_counts:
        print("\nTop sensory anchors (sentence-level hits):")
        for token, count in sorted(hit_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:25]:
            print(f"  {token}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
