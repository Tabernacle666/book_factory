from __future__ import annotations
from pathlib import Path
import argparse, tempfile, zipfile, html
import yaml, mistune
from weasyprint import HTML
from merge_course import merge_course


def find_project_root(path: Path) -> Path:
    if path.is_dir():
        if (path / 'manifest.yaml').exists() and (path / 'README.md').exists():
            return path
        for child in path.iterdir():
            if child.is_dir() and (child / 'manifest.yaml').exists() and (child / 'README.md').exists():
                return child
    raise FileNotFoundError('Impossible de trouver la racine du projet (README.md + manifest.yaml).')


def extract_if_zip(input_path: Path) -> tuple[Path, tempfile.TemporaryDirectory | None]:
    if input_path.suffix.lower() == '.zip':
        tempdir = tempfile.TemporaryDirectory()
        with zipfile.ZipFile(input_path, 'r') as zf:
            zf.extractall(tempdir.name)
        return find_project_root(Path(tempdir.name)), tempdir
    return find_project_root(input_path), None


def load_config(project_root: Path) -> dict:
    cfg = project_root / 'build' / 'config.yaml'
    if cfg.exists():
        return yaml.safe_load(cfg.read_text(encoding='utf-8')) or {}
    return {}


def render_toc(chapters: list[dict], included_files: list[str], mode: str) -> str:
    if mode == 'public':
        allowed = set(p.rsplit('/', 1)[0] + '/chapitre.md' for p in included_files if '/' in p)
    items = []
    for ch in chapters:
        if mode == 'public' and ch['path'] not in allowed:
            continue
        items.append(f"<li><span class='toc-id'>{html.escape(str(ch['id']))}.</span> {html.escape(ch['title'])}</li>")
    return '<ol>' + ''.join(items) + '</ol>'


def split_content_sections(merged_markdown: str) -> list[str]:
    lines = merged_markdown.splitlines()
    blocks = []
    current = []
    for line in lines:
        if line.startswith('# ') and current:
            blocks.append('\n'.join(current).strip())
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append('\n'.join(current).strip())
    return [b for b in blocks if b]


def build_cover_meta(project: dict, release: dict, config: dict, mode: str) -> str:
    if mode == 'public':
        lines = [html.escape(config.get('public_author', config.get('author', 'Auteur')))]
        subtitle = config.get('public_tagline')
        if subtitle:
            lines.append(html.escape(subtitle))
    else:
        lines = [html.escape(config.get('author', 'Auteur')),
                 html.escape(release.get('current_release', 'v?')),
                 html.escape(config.get('date_label', 'Release générée automatiquement'))]
    return ''.join(f"<div class='meta'>{line}</div>" for line in lines if line)




def compute_render_stats(merged: dict) -> dict:
    text = merged['merged_markdown']
    return {
        'chars': len(text),
        'words': len(text.split()),
        'headings': len([line for line in text.splitlines() if line.startswith('#')]),
        'files': len(merged['included_files']),
    }


def build_equivalence_report(project_root: Path) -> Path:
    work = merge_course(project_root, mode='work')
    public = merge_course(project_root, mode='public')
    work_stats = compute_render_stats(work)
    public_stats = compute_render_stats(public)
    missing = [p for p in work['included_files'] if p not in public['included_files']]
    public_text = public['merged_markdown']
    suspicious = {
        'editorial_markers': public_text.count('[['),
        'local_md_links': public_text.count('.md)'),
        'placeholder_mentions': public_text.lower().count('placeholder structuré'),
        'signal_de_redaction': public_text.lower().count('signal de rédaction'),
    }
    ratio_chars = (public_stats['chars'] / work_stats['chars']) if work_stats['chars'] else 0
    ratio_words = (public_stats['words'] / work_stats['words']) if work_stats['words'] else 0
    lines = [
        "# Rapport d'équivalence travail / publication",
        "",
        "## Volumes",
        f"- travail : {work_stats['chars']} caractères / {work_stats['words']} mots / {work_stats['headings']} intertitres / {work_stats['files']} fichiers inclus",
        f"- publication : {public_stats['chars']} caractères / {public_stats['words']} mots / {public_stats['headings']} intertitres / {public_stats['files']} fichiers inclus",
        f"- ratio publication / travail (caractères) : {ratio_chars:.3f}",
        f"- ratio publication / travail (mots) : {ratio_words:.3f}",
        "",
        "## Fichiers présents en travail mais absents en publication",
    ]
    if missing:
        lines.extend([f"- {item}" for item in missing])
    else:
        lines.append("- aucun")
    lines.extend([
        "",
        "## Vérifications rapides sur le rendu publication",
        f"- marqueurs éditoriaux bruts restants : {suspicious['editorial_markers']}",
        f"- liens markdown locaux vers des fichiers .md : {suspicious['local_md_links']}",
        f"- mentions de placeholder structuré : {suspicious['placeholder_mentions']}",
        f"- mentions de signal de rédaction : {suspicious['signal_de_redaction']}",
    ])
    report_path = project_root / 'output' / 'render-equivalence-report.md'
    report_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return report_path


def build_html(project_root: Path, mode: str = 'work') -> tuple[str, Path, Path]:
    merged = merge_course(project_root, mode=mode)
    manifest = merged['manifest']
    config = load_config(project_root)
    project = manifest.get('project', {})
    release = manifest.get('release_metadata', {})
    md = mistune.create_markdown(plugins=['table', 'strikethrough'])
    content_blocks = split_content_sections(merged['merged_markdown'])
    content_html = []
    for idx, block in enumerate(content_blocks):
        cls = 'chapter-block' if idx > 0 else 'front-block'
        content_html.append(f"<section class='{cls}'>" + md(block) + "</section>")
    template = (project_root / 'build' / 'template.html').read_text(encoding='utf-8')
    title = config.get('public_title' if mode == 'public' else 'title', project.get('title', 'Cours'))
    subtitle = config.get('public_subtitle' if mode == 'public' else 'subtitle', '')
    toc_title = config.get('public_toc_title' if mode == 'public' else 'toc_title', 'Table des matières')
    html_doc = template.format(
        lang=html.escape(project.get('language', 'fr')),
        title=html.escape(title),
        subtitle=html.escape(subtitle),
        toc_title=html.escape(toc_title),
        cover_meta=build_cover_meta(project, release, config, mode),
        toc=render_toc(manifest.get('chapters', []), merged['included_files'], mode),
        body_class=f"mode-{mode}",
        content='\n'.join(content_html),
    )
    out_dir = project_root / 'output'
    out_dir.mkdir(exist_ok=True)
    html_name = config.get(f'{mode}_html_output', f'{mode}.html')
    md_name = config.get(f'{mode}_merged_markdown_output', f'{mode}-merge.md')
    html_path = out_dir / html_name
    md_path = out_dir / md_name
    html_path.write_text(html_doc, encoding='utf-8')
    md_path.write_text(merged['merged_markdown'], encoding='utf-8')
    return html_doc, html_path, md_path


def build_mode(project_root: Path, mode: str) -> tuple[Path, Path, Path]:
    html_doc, html_path, md_path = build_html(project_root, mode=mode)
    config = load_config(project_root)
    pdf_name = config.get(f'{mode}_pdf_output', f'{mode}.pdf')
    pdf_path = project_root / 'output' / pdf_name
    HTML(string=html_doc, base_url=str(project_root)).write_pdf(str(pdf_path))
    return pdf_path, html_path, md_path


def main() -> int:
    parser = argparse.ArgumentParser(description='Génère des PDF à partir du dossier de release ou d’un zip.')
    parser.add_argument('input', nargs='?', default='.', help='Chemin vers le dossier de release ou le zip.')
    parser.add_argument('--mode', choices=['work', 'public', 'both'], default='both', help='Mode de rendu à générer.')
    args = parser.parse_args()
    input_path = Path(args.input).resolve()
    project_root, tempdir = extract_if_zip(input_path)
    try:
        modes = ['work', 'public'] if args.mode == 'both' else [args.mode]
        for mode in modes:
            pdf_path, html_path, md_path = build_mode(project_root, mode=mode)
            print(f'[{mode}] PDF généré: {pdf_path}')
            print(f'[{mode}] HTML généré: {html_path}')
            print(f'[{mode}] Markdown fusionné: {md_path}')
        if args.mode == 'both':
            report_path = build_equivalence_report(project_root)
            print(f"[audit] Rapport d’équivalence: {report_path}")
        return 0
    finally:
        if tempdir is not None:
            tempdir.cleanup()


if __name__ == '__main__':
    raise SystemExit(main())
