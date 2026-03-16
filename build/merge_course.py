from __future__ import annotations
from pathlib import Path
import re, yaml

FRONT_MATTER_RE = re.compile(r'^---\n.*?\n---\n+', re.DOTALL)
EDITORIAL_MARKER_RE = re.compile(r'^\s*\[\[(EDITORIAL|INSERT|FIGURE|CITATION|BLAGUE):.*?\]\]\s*$', re.MULTILINE)
LOCAL_MARKDOWN_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)\)')

INTERNAL_SECTION_HEADINGS = {
    "Signal de rédaction",
    "Rôle attendu du chapitre",
    "Sections du chapitre",
    "Sections",
    "Critères de complétion avant use-case",
    "Ce que ce nœud devra apporter",
    "Ce qui manque encore avant rédaction",
}

PUBLICATION_REMOVED_SECTION_PREFIXES = (
    "Passage explicite",
    "Renvois utiles",
    "Ce que cette étape a réellement stabilisé",
    "Ce nœud doit",
    "Statut du nœud",
)

PEDAGOGICAL_HEADINGS = {
    "Idée centrale": "Idée centrale.",
    "Pourquoi c'est important": "Pourquoi c'est important.",
    "Pourquoi ce chapitre existe": "Pourquoi ce chapitre existe.",
    "Ce que le lecteur doit comprendre en sortant": "Ce que le lecteur doit comprendre en sortant.",
    "Place dans la progression du livre": "Place dans la progression du livre.",
    "Erreur classique": "Erreur classique.",
    "Erreur de lecture à éviter": "Erreur de lecture à éviter.",
    "Méthode concrète": "Méthode concrète.",
    "Mini exemple": "Mini exemple.",
    "Règle pratique": "Règle pratique.",
    "Transition vers les cas pratiques": "Transition vers les cas pratiques.",
    "Thèse du chapitre": "Thèse du chapitre.",
    "Ce que valide vraiment chaque étage": "Ce que valide vraiment chaque étage.",
    "Ce que le cas montre sans prétendre automatiser": "Ce que le cas montre sans prétendre automatiser.",
    "Passage explicite à la section suivante": "Passage vers la section suivante.",
    "Passage explicite à la suite": "Passage vers la suite.",
}


def strip_front_matter(text: str) -> str:
    return FRONT_MATTER_RE.sub('', text, count=1)


def parse_front_matter(text: str) -> tuple[dict, str]:
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            raw = text[4:end]
            body = text[end + 5:]
            try:
                data = yaml.safe_load(raw) or {}
            except Exception:
                data = {}
            return data, body
    return {}, text


def load_manifest(project_root: Path) -> dict:
    return yaml.safe_load((project_root / 'manifest.yaml').read_text(encoding='utf-8'))


def ordered_section_files(chapter_dir: Path) -> list[Path]:
    files = [p for p in chapter_dir.glob('*.md') if p.name != 'chapitre.md']
    return sorted(files, key=lambda p: p.name)


def is_placeholder(body: str, meta: dict) -> bool:
    body_l = body.lower()
    return (
        'placeholder structuré' in body_l
        or 'signal de rédaction' in body_l
        or "ce fichier n'est pas encore rédigé" in body_l
        or 'quand ce nœud sera rédigé' in body_l
    )


def strip_local_markdown_links(text: str) -> str:
    return LOCAL_MARKDOWN_LINK_RE.sub(lambda m: m.group(1), text)


def strip_editorial_markers(text: str) -> str:
    return EDITORIAL_MARKER_RE.sub('', text)


def strip_internal_lines(text: str) -> str:
    text = re.sub(r'^>\s*État du nœud\s*:.*?(?:\n|$)', '', text, flags=re.MULTILINE)
    text = re.sub(r'^>\s*Statut\s*:.*?(?:\n|$)', '', text, flags=re.MULTILINE)
    text = re.sub(r'^>\s*Owner concept\s*:.*?(?:\n|$)', '', text, flags=re.MULTILINE)
    text = re.sub(r'^>\s*Résumé de fabrication\s*:.*?(?:\n|$)', '', text, flags=re.MULTILINE)
    return text


def should_remove_publication_section(heading: str) -> bool:
    if heading in INTERNAL_SECTION_HEADINGS:
        return True
    return any(heading.startswith(prefix) for prefix in PUBLICATION_REMOVED_SECTION_PREFIXES)


def strip_internal_scaffolding(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    skip_level: int | None = None
    for line in lines:
        stripped = line.strip()
        m = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if m:
            level = len(m.group(1))
            heading = m.group(2).strip()
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if should_remove_publication_section(heading):
                skip_level = level
                continue
        if skip_level is not None:
            continue
        out.append(line)
    text = '\n'.join(out)
    text = strip_editorial_markers(text)
    text = strip_internal_lines(text)
    text = strip_local_markdown_links(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def rewrite_pedagogical_headings_for_publication(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    for line in lines:
        m = re.match(r'^(#{2,6})\s+(.*)$', line.strip())
        if not m:
            out.append(line)
            continue
        heading = m.group(2).strip()
        label = PEDAGOGICAL_HEADINGS.get(heading)
        if label is None:
            out.append(line)
            continue
        if out and out[-1].strip() != "":
            out.append("")
        out.append(f"**{label}**")
        out.append("")
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def publication_title(body: str, meta: dict) -> str:
    title = meta.get('title')
    if title:
        return f"# {title}\n\n" + strip_front_matter(body).strip()
    return strip_front_matter(body).strip()


def prepare_file_text(path: Path, mode: str) -> tuple[dict, str] | None:
    raw = path.read_text(encoding='utf-8')
    meta, body = parse_front_matter(raw)
    clean_body = body.strip()
    if mode == 'public' and is_placeholder(clean_body, meta):
        return None
    text = strip_front_matter(raw).strip()
    if mode == 'public':
        text = strip_internal_scaffolding(text)
        text = rewrite_pedagogical_headings_for_publication(text)
    return meta, text.strip()


def merge_course(project_root: Path, mode: str = 'work') -> dict:
    manifest = load_manifest(project_root)
    project = manifest.get('project', {})
    chapters = manifest.get('chapters', [])
    parts: list[str] = []
    included_files: list[str] = []

    preface = project_root / project.get('front_matter_entry', 'preface.md')
    if preface.exists():
        prepared = prepare_file_text(preface, mode)
        if prepared is not None:
            _, text = prepared
            parts.append(text)
            included_files.append(preface.relative_to(project_root).as_posix())

    for chapter in chapters:
        ch_path = project_root / chapter['path']
        if ch_path.exists():
            prepared = prepare_file_text(ch_path, mode)
            if prepared is not None:
                _, text = prepared
                parts.append(text)
                included_files.append(ch_path.relative_to(project_root).as_posix())
                ch_dir = ch_path.parent
                for sec in ordered_section_files(ch_dir):
                    sec_prepared = prepare_file_text(sec, mode)
                    if sec_prepared is None:
                        continue
                    _, sec_text = sec_prepared
                    parts.append(sec_text)
                    included_files.append(sec.relative_to(project_root).as_posix())

    merged_markdown = '\n\n'.join(p for p in parts if p)
    return {
        'manifest': manifest,
        'merged_markdown': merged_markdown,
        'included_files': included_files,
        'mode': mode,
    }
