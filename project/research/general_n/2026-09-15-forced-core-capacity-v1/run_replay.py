#!/usr/bin/env python3
"""Offline replay for the forced-core receiver-capacity exclusions."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GN = HERE.parent
INPUT = GN / "2026-09-14-block-pressure-v1" / "REMAINDER_12.json"
VERIFY = HERE / "verify_forced_core_capacity.py"
FROZEN = HERE / "RESULT.json"
EXPECTED = "8784209ee05bb1ec6cd6da559e8845dbfeee3e041a96dcce9f41360c6d12920e"


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: assertions are audit checks.")
    proc = subprocess.run(
        [sys.executable, str(VERIFY), "--remainder", str(INPUT)],
        text=True, capture_output=True, check=True
    )
    actual = json.loads(proc.stdout)
    frozen = json.loads(FROZEN.read_text())
    assert actual == frozen
    digest = hashlib.sha256(canonical(actual)).hexdigest()
    assert digest == EXPECTED
    assert actual["newly_excluded"] == [160, 338]
    assert actual["original_sample"] == {"not_rejected": [], "rejected": 713, "total": 713}
    assert actual["canonical_finite_frontier"]["changed"] is False
    print("PASS: forced-core receiver-capacity partition excludes rows160 and338")
    print("PASS: original synthetic namespace is 713/713 rejected")
    print("PASS: canonical finite frontier unchanged")
    print("PASS: canonical result", digest)
    print("SCOPE: sample-level necessary-condition closure; unrestricted conjecture not claimed")


if __name__ == "__main__":
    main()
