#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / "current_state.md"

STATE_RE = re.compile(r"^v(\d+)\|(redac|gouv)\|(lock|free)$")


def read_state() -> tuple[int, str, str, str]:
    raw = STATE_FILE.read_text(encoding="utf-8").strip()
    m = STATE_RE.fullmatch(raw)
    if not m:
        raise ValueError(f"Etat invalide dans current_state.md: {raw!r}")
    version = int(m.group(1))
    holder = m.group(2)
    status = m.group(3)
    return version, holder, status, raw


def decide_role(holder: str, status: str) -> str:
    if holder == "redac" and status == "lock":
        return "redac"
    if holder == "redac" and status == "free":
        return "gouv"
    if holder == "gouv" and status == "lock":
        return "gouv"
    if holder == "gouv" and status == "free":
        return "redac"
    raise ValueError(f"Transition non supportee: {holder}|{status}")


def main() -> int:
    version, holder, status, raw_state = read_state()
    role = decide_role(holder, status)

    print(f"[continuity] state={raw_state}")
    print(f"[continuity] dispatch={role}")

    cmd = [sys.executable, str(ROOT / "run_role.py"), role, raw_state]
    completed = subprocess.run(cmd, cwd=str(ROOT))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())