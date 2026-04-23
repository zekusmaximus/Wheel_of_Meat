from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


FILES = {
    "CH01": "incarnations/ch01-contemporary-manchester/CH01_draft.md",
    "CH03": "incarnations/ch03-lilith-cp01/CH03_draft.md",
    "CH04": "incarnations/ch04-mauryan-chandra/CH04_draft.md",
    "CH04_PROFILE": "incarnations/ch04-mauryan-chandra/avatar-profile.json",
    "CH04_RULES": "incarnations/ch04-mauryan-chandra/period-rules.md",
    "CH05": "incarnations/ch05-lilith-cp02/CH05_draft.md",
    "CH06": "incarnations/ch06-athens-philosopher/CH06_draft.md",
    "CH06_PROFILE": "incarnations/ch06-athens-philosopher/avatar-profile.json",
    "CH06_OUTLINE": "incarnations/ch06-athens-philosopher/outline_v1.md",
    "CH06_RULES": "incarnations/ch06-athens-philosopher/period-rules.md",
    "CH07": "incarnations/ch07-lilith-cp03/CH07_draft.md",
    "CH08": "incarnations/ch08-rome-investigator/CH08_draft.md",
    "CH08_PROFILE": "incarnations/ch08-rome-investigator/avatar-profile.json",
    "CH08_OUTLINE": "incarnations/ch08-rome-investigator/ch08_outline.md",
    "CH08_RULES": "incarnations/ch08-rome-investigator/period-rules.md",
    "CH09": "incarnations/ch09-lilith-cp04/CH09_draft.md",
    "CH10": "incarnations/ch10-egypt-hermit/CH10_draft.md",
    "CH10_PROFILE": "incarnations/ch10-egypt-hermit/avatar-profile.json",
    "CH10_OUTLINE": "incarnations/ch10-egypt-hermit/chapter-outline.md",
    "CH10_RULES": "incarnations/ch10-egypt-hermit/period-rules.md",
    "CH11": "incarnations/ch11-lilith-cp05/CH11_draft.md",
    "CH12": "incarnations/ch12-heian-lover/CH12_draft.md",
    "CH12_PROFILE": "incarnations/ch12-heian-lover/avatar-profile.json",
    "CH12_OUTLINE": "incarnations/ch12-heian-lover/CH12_outline.md",
    "CH12_RULES": "incarnations/ch12-heian-lover/period-rules.md",
    "CH13": "incarnations/ch13-lilith-cp06/CH13_draft.md",
    "CH14": "incarnations/ch14-inquisition-accused/CH14_draft.md",
    "CH14_PROFILE": "incarnations/ch14-inquisition-accused/avatar-profile.json",
    "CH14_OUTLINE": "incarnations/ch14-inquisition-accused/CH14_outline.md",
    "CH14_RULES": "incarnations/ch14-inquisition-accused/period-rules.md",
    "CH15": "incarnations/ch15-lilith-cp07/CH15_draft.md",
    "CH16": "incarnations/ch16-renaissance-skeptic/CH16_draft.md",
    "CH16_PROFILE": "incarnations/ch16-renaissance-skeptic/avatar-profile.json",
    "CH16_OUTLINE": "incarnations/ch16-renaissance-skeptic/ch16-outline.md",
    "CH16_RULES": "incarnations/ch16-renaissance-skeptic/period-rules.md",
    "CH17": "incarnations/ch17-lilith-cp08/CH17_draft.md",
    "CH18": "incarnations/ch18-taiping-rebel/CH18_draft.md",
    "CH18_PROFILE": "incarnations/ch18-taiping-rebel/avatar-profile.json",
    "CH18_OUTLINE": "incarnations/ch18-taiping-rebel/ch18-outline.md",
    "CH18_RULES": "incarnations/ch18-taiping-rebel/period-rules.md",
    "CH19": "incarnations/ch19-lilith-cp09/CH19_draft.md",
    "CH20": "incarnations/ch20-noir-detective/CH20_draft.md",
    "CH20_PROFILE": "incarnations/ch20-noir-detective/avatar-profile.json",
    "CH20_OUTLINE": "incarnations/ch20-noir-detective/chapter-outline.md",
    "CH20_RULES": "incarnations/ch20-noir-detective/period-rules.md",
    "CH21": "incarnations/ch21-lilith-cp10/CH21_draft.md",
}


def lines(key: str) -> list[str]:
    return (ROOT / FILES[key]).read_text(encoding="utf-8").splitlines()


def find(key: str, pattern: str, flags: int = 0) -> list[tuple[int, str]]:
    rx = re.compile(pattern, flags)
    return [(i, line) for i, line in enumerate(lines(key), 1) if rx.search(line)]


def wc(key: str) -> int:
    text = (ROOT / FILES[key]).read_text(encoding="utf-8")
    return len(re.findall(r"\b\S+\b", text))


SEARCHES: list[tuple[str, str, str]] = [
    ("CH04", r"thirty-four", "age"),
    ("CH04", r"\bwife\b", "wife"),
    ("CH05", r"wife|Fifteen years counts|always meant nothing|temple|passage", "ch05-continuity"),
    ("CH04", r"fifteen years counts|The words meant nothing|They had always meant nothing", "temple-dialogue"),
    ("CH04", r"emperor", "emperor"),
    ("CH04", r"You(?:'re|'ll|'ve)|We(?:'re)|I(?:'ll|'ve)|He(?:'s)|wasn't|n't", "contractions"),
    ("CH04", r"particularite|katar|ceremonial knife|polished surface", "misc"),
    ("CH06", r"Alexios found|eastern gate|three days|forty years|thirty years old|tanner|title|Virtue|Fear wearing", "ch06"),
    ("CH07", r"Alexios left|three days after|taste of ash|eastern gate", "ch07"),
    ("CH08", r"pride|Virtue lives|Virtue is not|Marcia|No witnesses|No discovery|could not see it|did not see it|temperate|intemperate", "ch08"),
    ("CH08_PROFILE", r"dissolves|Marcia|partial truths|pride", "ch08-profile"),
    ("CH08_OUTLINE", r"bittersweet|Virtue lives|Freedman|cook|No witnesses|Marcia", "ch08-outline"),
    ("CH08_RULES", r"Virtue is not|compassion within uncertainty|Virtue lives", "ch08-rules"),
    ("CH10", r"kenosis|theosis|self-image|self-filling|\bstructure\b|spider|predator|She was speaking|She seemed|satisfied|waiting for something|Paphnutius|snake that flatters|fingers closed on nothing", "ch10"),
    ("CH10_PROFILE", r"does not recognize|Theodora|Paphnutius", "ch10-profile"),
    ("CH10_OUTLINE", r"unnamed|9700|9,700|recognition is physical|No inner", "ch10-outline"),
    ("CH10_RULES", r"kenosis|Greek|modern psychological|recognition is physical|No declaration", "ch10-rules"),
    ("CH12", r"incense|translucent|presence lived|intelligence|knew he had seen|heresy|tortured|victim|slumped|country he had not known|chains|suffocating", "ch12"),
    ("CH12_PROFILE", r"incense|translucent", "ch12-profile"),
    ("CH12_OUTLINE", r"1000|slumped|victim|Scene I|Scene V", "ch12-outline"),
    ("CH12_RULES", r"1100|1050|wakes|interpret|Inquisition", "ch12-rules"),
    ("CH13", r"Diego de la Cruz|Diego de Lucena|converso priest|converso physician|sixteenth-century|fifteenth-century|1491", "ch13"),
    ("CH14", r"Word count:|Sensory anchors:|Recognition marker:|Hatred seed:|1491|Granada|Alhambra|silver|temples|deep-set|steady hands|Momentum|momentum|Sor Catalina|Physician\. You walk late|carry your bag|I'm sorry|I hate you|I know|Release without forgiveness", "ch14"),
    ("CH14_PROFILE", r"silvering|deep-set|steady hands|Arabic|Catalina|Diego de Lucena|physician", "ch14-profile"),
    ("CH14_RULES", r"1491|Granada|Lilith cannot speak|touch|directly|momentum", "ch14-rules"),
    ("CH15", r"Diego de Lucena|Catalina|tracked|tracking|Sor Catalina", "ch15"),
    ("CH16", r"Isabeau|Carcassonne|widow's peak|pale-green|darker strand|three days after|Jean de Langon died|The wheel turned|epistemolog|narrative|performance|professional armor|touched his|Nearly missed it|You offer me a fortress|truth about what I didn't know|If he included|If he excluded|If the letter", "ch16"),
    ("CH16_PROFILE", r"death_year|1588|Isabeau|recognition", "ch16-profile"),
    ("CH16_RULES", r"Isabeau|Carcassonne|Paris|1598|1588", "ch16-rules"),
    ("CH16_OUTLINE", r"8,000|9000|9,000|Scene 6|Isabeau", "ch16-outline"),
    ("CH17", r"Nearly missed|fortress|truth about what|one of my past lives|Isabeau", "ch17"),
    ("CH18", r"knelt|dawn|dust motes|Tianjing|Heavenly King|Forty-eight saved|Forty-seven saved|invisible hand|no accident|manipulation so subtle|twenty men|1854|cholera|fifty hours|seventy-two|third day|Young Ping|Everyone died|whole village|Jean|It doesn't matter if I'm cursed|I'm sorry|I will try again", "ch18"),
    ("CH18_PROFILE", r"47|saved|23|mother|cholera|1854|hair|tunic|scars", "ch18-profile"),
    ("CH18_RULES", r"hierarchy|moral corrosion|Lilith never|pattern visible|enemy soldiers|personalized", "ch18-rules"),
    ("CH19", r"recalculated|understood|91 saved|171 lost|tracking|watching|Jack Malone|Wei Shufen|It doesn't matter|bleeding now|133 saved|128 lost", "ch19"),
    ("CH20", r"widow's peak|darker strand|pale crescent|pale-green|never been to France|Belleau|Meuse|Gloria Dane|sequined|full lips|figure that|David Brennan|Howard Brennan|more power than the Combination|surgical|personal|three-year-old Roadmaster|Lankershim|Pacific Electric|Clifton|The Shadow|Black Mask|Someone has to give a damn|I've seen those eyes before|A passerby, rushing to avoid|shared bathroom|Murphy|Momentum|momentum", "ch20"),
    ("CH20_PROFILE", r"France|Belleau|Meuse|Clifton|Shadow|pulp|tracking|1938|Roadmaster", "ch20-profile"),
    ("CH20_RULES", r"barely notices|femme fatale|Roadmaster|1938|Flood|Lankershim|Pacific Electric", "ch20-rules"),
    ("CH21", r"NOW|ten|completed|Malone|Jack|find him", "ch21"),
    ("CH01", r"passerby|rushing to avoid|Roadmaster|Buick", "ch01"),
]


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    out_lines: list[str] = []
    def emit(value: str = "") -> None:
        out_lines.append(value)
        print(value)

    emit("# WORD COUNTS")
    for key in ["CH04", "CH06", "CH08", "CH10", "CH12", "CH14", "CH16", "CH18", "CH20"]:
        emit(f"{key}: {wc(key)}")

    emit("\n# SEARCHES")
    for key, pattern, label in SEARCHES:
        hits = find(key, pattern, re.IGNORECASE)
        emit(f"\n## {label} :: {key} :: {len(hits)}")
        for ln, text in hits[:80]:
            emit(f"{ln}: {text}")
        if len(hits) > 80:
            emit(f"... {len(hits) - 80} more")
    (ROOT / "tools" / "guide_audit_output.txt").write_text("\n".join(out_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
