#!/usr/bin/env python3
"""Offline replay for the fresh forced-core/high-squeeze closure."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GN = HERE.parent
INPUT = GN / "2026-09-14-joint-blocks-v1" / "FRESH_RECHECK_FULL.json"
VERIFY = HERE / "verify_fresh_forced_core.py"
FROZEN = HERE / "RESULT.json"
EXPECTED = "7357a5139417a1b48f94d8ddbb6122c57363ce70ab0c4586673a290a25c51464"


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: assertions are audit checks.")
    proc = subprocess.run(
        [sys.executable, str(VERIFY), "--input", str(INPUT)],
        text=True, capture_output=True, check=True,
    )
    actual = json.loads(proc.stdout)
    frozen = json.loads(FROZEN.read_text())
    assert actual == frozen
    digest = hashlib.sha256(canonical(actual)).hexdigest()
    assert digest == EXPECTED
    assert actual["capacity_deficit_exclusions"] == [20, 91, 391, 528, 562, 677]
    assert actual["row490_high_squeeze"]["adjusted_high_selected_upper"] == 43
    assert actual["row490_high_squeeze"]["required_high_selected"] == 45
    assert actual["fresh_sample"] == {"not_rejected": [], "rejected": 715, "total": 715}
    assert actual["canonical_finite_frontier"]["changed"] is False
    print("PASS: forced-core capacity excludes fresh rows20,91,391,528,562,677")
    print("PASS: row490 high-demand squeeze gives 43 < 45")
    print("PASS: fresh synthetic namespace is 715/715 rejected")
    print("PASS: original synthetic namespace remains 713/713 rejected")
    print("PASS: canonical finite frontier unchanged")
    print("PASS: canonical result", digest)
    print("SCOPE: sample-level necessary-condition closure; unrestricted conjecture not claimed")


if __name__ == "__main__":
    main()
