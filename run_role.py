#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent

STATE_FILE = ROOT / "current_state.md"
README_FILE = ROOT / "README.md"
BOOTSTRAP_REDAC = ROOT / "bootstrap_redac.md"
BOOTSTRAP_GOUV = ROOT / "bootstrap_gouv.md"
FROM_REDAC_TO_GOUV = ROOT / "from_redac_to_gouv.md"
FROM_GOUV_TO_REDAC = ROOT / "from_gouv_to_redac.md"

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.4").strip()
OPENAI_API_URL = os.environ.get("OPENAI_API_URL", "https://api.openai.com/v1/responses").strip()

STATE_RE = re.compile(r"^v(\d+)\|(redac|gouv)\|(lock|free)$")

CONTROL_FILES = {
    "README.md",
    "bootstrap_redac.md",
    "bootstrap_gouv.md",
    "current_state.md",
    "from_redac_to_gouv.md",
    "from_gouv_to_redac.md",
    "continuity_pulse.py",
    "run_role.py",
    "requirements.txt",
}

MAX_FILE_CHARS = 120_000
MAX_TOTAL_CHARS = 900_000


def read_text(path: Path, default: str = "") -> str:
    if not path.exists():
        return default
    return path.read_text(encoding="utf-8", errors="replace").strip()


def write_text(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def parse_state(raw: str) -> tuple[int, str, str]:
    m = STATE_RE.fullmatch(raw.strip())
    if not m:
        raise ValueError(f"Etat invalide: {raw!r}")
    return int(m.group(1)), m.group(2), m.group(3)


def expected_role_from_state(raw_state: str) -> str:
    _, holder, status = parse_state(raw_state)
    if holder == "redac" and status == "lock":
        return "redac"
    if holder == "redac" and status == "free":
        return "gouv"
    if holder == "gouv" and status == "lock":
        return "gouv"
    if holder == "gouv" and status == "free":
        return "redac"
    raise ValueError(f"Transition non supportee: {raw_state}")


def role_files(role: str) -> tuple[Path, Path]:
    if role == "redac":
        return BOOTSTRAP_REDAC, FROM_GOUV_TO_REDAC
    if role == "gouv":
        return BOOTSTRAP_GOUV, FROM_REDAC_TO_GOUV
    raise ValueError(f"Role inconnu: {role}")


def output_file_for_role(role: str) -> Path:
    if role == "redac":
        return FROM_REDAC_TO_GOUV
    if role == "gouv":
        return FROM_GOUV_TO_REDAC
    raise ValueError(f"Role inconnu: {role}")


def iter_project_markdown_files() -> Iterable[Path]:
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".git/") or rel.startswith(".github/"):
            continue
        if path.name in CONTROL_FILES:
            continue
        yield path


def collect_content_blob() -> str:
    total = 0
    parts: list[str] = []

    for path in iter_project_markdown_files():
        rel = path.relative_to(ROOT).as_posix()
        text = read_text(path)
        if not text:
            continue

        if len(text) > MAX_FILE_CHARS:
            text = text[:MAX_FILE_CHARS] + "\n\n[TRONQUE]\n"

        remaining = MAX_TOTAL_CHARS - total
        if remaining <= 0:
            break

        if len(text) > remaining:
            text = text[:remaining] + "\n\n[TRONQUE GLOBAL]\n"

        parts.append(f"===== FILE: {rel} =====\n{text}\n")
        total += len(text)

        if total >= MAX_TOTAL_CHARS:
            break

    if not parts:
        return "[AUCUN FICHIER DE CONTENU .md]"
    return "\n".join(parts).strip()


def build_system_prompt(role: str, current_state: str) -> str:
    return f"""
Tu joues un seul role: {role}.

Tu travailles dans un repo Books Factory.
Le routeur de continuite t'a dispatch a partir de l'etat:
{current_state}

Tu dois suivre uniquement:
- README.md
- ton bootstrap de role
- ton handoff entrant
- les fichiers de contenu du repo

Tu n'as pas a expliquer le workflow.
Tu executes ton role.

Tu dois retourner UNIQUEMENT un JSON valide, sans markdown, sans texte hors JSON.

Schema de sortie obligatoire:
{{
  "output_file_content": "contenu complet a ecrire dans ton fichier de sortie autorise",
  "next_state": "vNN|role|status",
  "summary": "resume tres bref"
}}

Regles:
- redac n'ecrit que from_redac_to_gouv.md
- gouv n'ecrit que from_gouv_to_redac.md
- la mise a jour de current_state.md fait partie de ton travail
- aucun etat intermediaire
- si tu es redac, tu dois sortir vers vN|redac|free
- si tu es gouv, tu dois sortir vers vN+1|gouv|free
- n'invente pas d'autres formats
""".strip()


def build_user_prompt(
    role: str,
    current_state: str,
    readme_text: str,
    bootstrap_text: str,
    incoming_handoff: str,
    content_blob: str,
) -> str:
    return f"""
ROLE
{role}

CURRENT_STATE
{current_state}

README_MD
{readme_text}

BOOTSTRAP_ROLE
{bootstrap_text}

HANDOFF_ENTRANT
{incoming_handoff or "[VIDE]"}

CONTENU_PROJET
{content_blob}

INSTRUCTION FINALE
Fais exactement ton role.
Lis README.md comme point d'entree, puis ton bootstrap et ton handoff.
Retourne strictement le JSON demande.
""".strip()


def call_openai(system_prompt: str, user_prompt: str) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY manquant")

    payload = {
        "model": OPENAI_MODEL,
        "input": [
            {
                "role": "system",
                "content": [{"type": "input_text", "text": system_prompt}],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": user_prompt}],
            },
        ],
        "max_output_tokens": 4000,
    }

    req = urllib.request.Request(
        OPENAI_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {body}") from e

    data = json.loads(raw)

    if isinstance(data.get("output_text"), str) and data["output_text"].strip():
        return data["output_text"].strip()

    texts: list[str] = []
    for item in data.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            ctype = content.get("type")
            if ctype in {"output_text", "text"}:
                text = content.get("text", "")
                if text:
                    texts.append(text)

    merged = "\n".join(texts).strip()
    if not merged:
        raise RuntimeError(f"Reponse OpenAI inexploitable: {raw[:2000]}")
    return merged


def extract_json(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(text[start:end + 1])


def validate_next_state(role: str, current_state: str, next_state: str) -> None:
    current_version, _, _ = parse_state(current_state)
    next_version, next_holder, next_status = parse_state(next_state)

    if role == "redac":
        expected = (current_version, "redac", "free")
        got = (next_version, next_holder, next_status)
        if got != expected:
            raise ValueError(
                f"next_state invalide pour redac. Attendu v{current_version}|redac|free, recu {next_state}"
            )
        return

    if role == "gouv":
        expected = (current_version + 1, "gouv", "free")
        got = (next_version, next_holder, next_status)
        if got != expected:
            raise ValueError(
                f"next_state invalide pour gouv. Attendu v{current_version + 1}|gouv|free, recu {next_state}"
            )
        return

    raise ValueError(f"Role inconnu: {role}")


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python run_role.py <redac|gouv> <current_state>", file=sys.stderr)
        return 2

    role = sys.argv[1].strip()
    dispatched_state = sys.argv[2].strip()

    if role not in {"redac", "gouv"}:
        raise ValueError(f"Role invalide: {role}")

    actual_state = read_text(STATE_FILE)
    if actual_state != dispatched_state:
        print(
            f"State drift detecte. dispatch={dispatched_state} actual={actual_state}. Rien a faire.",
            file=sys.stderr,
        )
        return 0

    expected_role = expected_role_from_state(actual_state)
    if expected_role != role:
        raise ValueError(
            f"Role incoherent. current_state={actual_state}, role attendu={expected_role}, role recu={role}"
        )

    bootstrap_path, incoming_handoff_path = role_files(role)
    output_path = output_file_for_role(role)

    readme_text = read_text(README_FILE)
    bootstrap_text = read_text(bootstrap_path)
    incoming_handoff = read_text(incoming_handoff_path)
    content_blob = collect_content_blob()

    if not readme_text:
        raise RuntimeError("README.md absent ou vide")
    if not bootstrap_text:
        raise RuntimeError(f"{bootstrap_path.name} absent ou vide")

    system_prompt = build_system_prompt(role, actual_state)
    user_prompt = build_user_prompt(
        role=role,
        current_state=actual_state,
        readme_text=readme_text,
        bootstrap_text=bootstrap_text,
        incoming_handoff=incoming_handoff,
        content_blob=content_blob,
    )

    print(f"[run_role] role={role}")
    print(f"[run_role] state={actual_state}")
    print(f"[run_role] input={incoming_handoff_path.name}")
    print(f"[run_role] output={output_path.name}")

    raw_response = call_openai(system_prompt, user_prompt)
    payload = extract_json(raw_response)

    output_file_content = str(payload.get("output_file_content", "")).strip()
    next_state = str(payload.get("next_state", "")).strip()
    summary = str(payload.get("summary", "")).strip()

    if not output_file_content:
        raise RuntimeError("output_file_content manquant")
    if not next_state:
        raise RuntimeError("next_state manquant")

    validate_next_state(role, actual_state, next_state)

    write_text(output_path, output_file_content)
    write_text(STATE_FILE, next_state)

    print(f"[run_role] wrote={output_path.name}")
    print(f"[run_role] next_state={next_state}")
    if summary:
        print(f"[run_role] summary={summary}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())