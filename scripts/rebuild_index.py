from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
manifest = root / "manifest.yaml"
main = root / "main.md"

chapter_dirs = sorted([p for p in root.iterdir() if p.is_dir() and re.match(r"^\d{2}-", p.name)])
lines = [
    "# Cours — Architecture, découpage et pilotage d'équipes hybrides humain+IA",
    "",
    "## Table des matières régénérée",
    "",
]
for idx, chap in enumerate(chapter_dirs, start=1):
    title = chap.name.split('-', 1)[1].replace('-', ' ').capitalize()
    chapter_file = chap / 'chapitre.md'
    lines.append(f"{idx}. [{title}]({chap.name}/chapitre.md)")
    if chapter_file.exists():
        section_files = sorted([p for p in chap.glob("*.md") if p.name != 'chapitre.md'])
        for sec in section_files:
            lines.append(f"   - [{sec.stem}]({chap.name}/{sec.name})")
main.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Index régénéré: {main}")
