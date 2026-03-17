from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / "current_state.md"

STATE_RE = re.compile(r"^v(\d+)\|(redac|gouv)\|(lock|free)$")


def read_state() -> str:
    if not STATE_FILE.exists():
        raise FileNotFoundError("current_state.md introuvable")
    return STATE_FILE.read_text(encoding="utf-8").strip()


def parse_state(state: str):
    m = STATE_RE.match(state)
    if not m:
        raise ValueError(f"Etat invalide: {state}")
    version = int(m.group(1))
    holder = m.group(2)
    status = m.group(3)
    return version, holder, status


def decide_next_action(version: int, holder: str, status: str) -> str:
    if holder == "redac" and status == "lock":
        return f"Relancer REDACTION sur v{version}"
    if holder == "redac" and status == "free":
        return f"Lancer GOUVERNANCE sur v{version}"
    if holder == "gouv" and status == "lock":
        return f"Relancer GOUVERNANCE sur v{version}"
    if holder == "gouv" and status == "free":
        return f"Lancer REDACTION sur v{version}"
    raise ValueError("Transition inconnue")


def main() -> int:
    try:
        raw_state = read_state()
        version, holder, status = parse_state(raw_state)
        action = decide_next_action(version, holder, status)
        print(f"Etat courant : {raw_state}")
        print(f"Action : {action}")
        print("Mode actuel : squelette de continuité sans appel OpenAI.")
        return 0
    except Exception as e:
        print(f"ERREUR: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())