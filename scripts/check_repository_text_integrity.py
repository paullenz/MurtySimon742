#!/usr/bin/env python3
"""Repository text-integrity check; not a mathematical verifier."""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path
import subprocess

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    ledger = json.loads((root / "project/maintenance/2026-09-24/INTEGRITY_EXCEPTIONS.json").read_text())
    allowed = {entry["path"]: entry["sha256"] for entry in ledger["intentional_invalid_json"]}
    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    errors = []
    counts = {"python": 0, "json": 0, "preserved_invalid_json": 0}
    for name in filter(None, paths):
        path = root / name
        if path.suffix not in (".py", ".json"):
            continue
        raw = path.read_bytes()
        if name in allowed:
            if hashlib.sha256(raw).hexdigest() != allowed[name]:
                errors.append(f"{name}: preserved corruption digest changed")
            counts["preserved_invalid_json"] += 1
            continue
        try:
            content = raw.decode("utf-8")
            if path.suffix == ".py":
                ast.parse(content, filename=name)
                counts["python"] += 1
            else:
                json.loads(content)
                counts["json"] += 1
        except (SyntaxError, ValueError, RecursionError) as exc:
            errors.append(f"{name}: {exc}")
    for name in allowed:
        if name not in paths:
            errors.append(f"{name}: preserved original missing")
    print(json.dumps({"counts": counts, "errors": errors, "known_incomplete_artifacts": ledger["known_incomplete_artifacts"], "scope": "Syntax and preserved-file integrity only, not mathematical acceptance"}, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
