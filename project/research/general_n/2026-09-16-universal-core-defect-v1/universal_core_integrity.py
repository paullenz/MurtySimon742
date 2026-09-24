#!/usr/bin/env python3
"""Fail-closed transport/replay wrapper; the preserved mathematics is unchanged.

A successful replay is bound to the reviewed 11,357-record fixture, not just
agreement between two possibly truncated streams. Generation and replay take
place in a temporary directory; only validated complete files are published.
This is stream integrity and same-project replay, not external proof review.
"""
from __future__ import annotations
import argparse
import contextlib
import gzip
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import sys
import subprocess
import tempfile

RECORDS = 11357
INPUT_SHA = "ab9ed63d9caa99b5fbd237fc6b238f77b69a8dc893ff17a764f96ff5cc9ab4bb"
DECISION_SHA = "c4859538b56444860b26fdc46e40f68bf21b4c65b68dce2e394b531c621ba82a"
GRAPH_SHA = "07e00b0794491679dfb5bf7b98da1757806296db7b56ea2bad6c9f69d8d903b9"
SOURCE_SHA = {"universal_core_impl.py": "0ea9ac79ff7d965a14bd45b45b1cd411dcee4fafd3b4bb36fd277b7e073afec9", "check_universal_core.cpp": "620b5354f12f242fa3db14fef6c015dbbcb539bf18c067726a17285ae7374d59"}

class IntegrityError(RuntimeError):
    """Incomplete, changed or unreviewed source/fixture: do not certify."""

def require(condition: bool, message: str) -> None:
    if not condition:
        raise IntegrityError(message)

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def validate(root: Path, *, cpp: bool = False) -> dict:
    summary = json.loads((root / "CHECK_SUMMARY.json").read_text())
    require(summary.get("records") == RECORDS, "summary record count differs from reviewed fixture")
    require(summary.get("seed") == 202609162, "summary seed differs from reviewed fixture")
    require(summary.get("input_sha256") == INPUT_SHA, "summary input digest differs from reviewed fixture")
    require(summary.get("decision_sha256") == DECISION_SHA, "summary decision digest differs from reviewed fixture")
    streams = [("INPUT.txt", INPUT_SHA), ("PYTHON_DECISIONS.tsv", DECISION_SHA)]
    if cpp:
        streams.append(("CPP_DECISIONS.tsv", DECISION_SHA))
    for name, expected in streams:
        data = (root / name).read_bytes()
        require(len(data.splitlines()) == RECORDS, f"{name}: expected {RECORDS} records")
        require(hashlib.sha256(data).hexdigest() == expected, f"{name}: digest mismatch")
    graph = root / "GRAPH_RECORDS.json"
    require(digest(graph) == GRAPH_SHA, "graph sidecar digest mismatch")
    require(len(json.loads(graph.read_text())) == 1399, "graph sidecar record count mismatch")
    return summary

def unpack_or_copy(root: Path, stage: Path, name: str) -> None:
    if (root / name).is_file():
        shutil.copyfile(root / name, stage / name)
    else:
        with gzip.open(root / (name + ".gz"), "rb") as src, (stage / name).open("wb") as dst:
            shutil.copyfileobj(src, dst)

def main(argv: list[str] | None = None, *, root: Path | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    modes = ap.add_mutually_exclusive_group()
    modes.add_argument("--generate-only", action="store_true")
    modes.add_argument("--replay-only", action="store_true")
    args = ap.parse_args(argv)
    root = Path(root) if root is not None else Path(__file__).resolve().parent
    lock = root / ".universal-core-integrity.lock"
    acquired = False
    try:
        require(__debug__, "optimized Python disables inherited mathematical assertions; run without -O")
        for name, sha in SOURCE_SHA.items():
            require(digest(root / name) == sha, f"{name}: source differs from reviewed implementation")
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        acquired = True
        with os.fdopen(fd, "w") as f:
            f.write(str(os.getpid()) + "\n")
        spec = importlib.util.spec_from_file_location("preserved_universal_core", root / "universal_core_impl.py")
        require(spec is not None and spec.loader is not None, "cannot load preserved implementation")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory(prefix=".universal-core-stage-", dir=root) as temp:
            stage = Path(temp)
            module.ROOT = stage
            shutil.copyfile(root / "check_universal_core.cpp", stage / "check_universal_core.cpp")
            # Do not print the legacy PASS output until independent integrity checks pass.
            with contextlib.redirect_stdout(io.StringIO()):
                if args.replay_only:
                    shutil.copyfile(root / "CHECK_SUMMARY.json", stage / "CHECK_SUMMARY.json")
                    for name in ("INPUT.txt", "PYTHON_DECISIONS.tsv", "GRAPH_RECORDS.json"):
                        unpack_or_copy(root, stage, name)
                else:
                    module.generate()
                validate(stage)
                if not args.generate_only:
                    module.replay()
                summary = validate(stage, cpp=not args.generate_only)
            allowed = ["INPUT.txt", "PYTHON_DECISIONS.tsv", "GRAPH_RECORDS.json", "CONTROLS.json", "ENVELOPES.json"]
            if not args.generate_only:
                allowed += ["CPP_DECISIONS.tsv"] + [n + ".gz" for n in ("INPUT.txt", "PYTHON_DECISIONS.tsv", "CPP_DECISIONS.tsv", "GRAPH_RECORDS.json")]
            # Multi-file publication is not a database transaction. The summary is
            # the last commit marker; each subsequent invocation revalidates all bytes.
            for name in allowed:
                if (stage / name).is_file():
                    os.replace(stage / name, root / name)
            os.replace(stage / "CHECK_SUMMARY.json", root / "CHECK_SUMMARY.json")
            summary["integrity_gate"] = "PASS_PINNED_COUNT_HASH_AND_SIDECAR"
            summary["implementation_change"] = "transport wrapper only; original Python and C++ unchanged"
            print(json.dumps(summary, indent=2))
        return 0
    except (OSError, ValueError, IntegrityError, AssertionError, subprocess.CalledProcessError) as exc:
        print("INTEGRITY_ERROR: " + str(exc), file=sys.stderr)
        return 2
    finally:
        if acquired:
            lock.unlink(missing_ok=True)

if __name__ == "__main__":
    raise SystemExit(main())
