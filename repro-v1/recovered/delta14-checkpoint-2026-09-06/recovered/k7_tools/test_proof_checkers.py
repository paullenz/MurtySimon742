#!/usr/bin/env python3
"""Positive and negative regression tests for the DRUP replay checkers."""

from __future__ import annotations

import gzip
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path


def write(path, text, compressed=False):
    if compressed:
        with gzip.open(path, "wt", encoding="ascii") as stream:
            stream.write(text)
    else:
        path.write_text(text, encoding="ascii")


def run(checker, cnf_text, proof_text, expected):
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        cnf = root / "case.cnf"
        proof = root / "case.drup.gz"
        write(cnf, cnf_text)
        write(proof, proof_text, compressed=True)
        result = subprocess.run(checker + [str(cnf), str(proof)], capture_output=True, text=True)
        if (result.returncode == 0) != expected:
            raise RuntimeError(
                f"unexpected checker result: expected={expected}, exit={result.returncode}, "
                f"stdout={result.stdout!r}, stderr={result.stderr!r}"
            )


def main():
    checker = (
        shlex.split(sys.argv[1])
        if len(sys.argv) > 1
        else [str(Path("check_drup_fast").resolve())]
    )
    cases = [
        (
            "contradictory units",
            "p cnf 1 2\n1 0\n-1 0\n",
            "0\n",
            True,
        ),
        (
            "two-step RUP proof",
            "p cnf 2 4\n1 2 0\n-1 2 0\n1 -2 0\n-1 -2 0\n",
            "2 0\n0\n",
            True,
        ),
        (
            "false UNSAT claim",
            "p cnf 1 1\n1 0\n",
            "0\n",
            False,
        ),
        (
            "invalid derived unit",
            "p cnf 2 1\n1 2 0\n",
            "1 0\n0\n",
            False,
        ),
    ]
    for name, cnf, proof, expected in cases:
        run(checker, cnf, proof, expected)
        print(f"PASS: {name} ({'accepted' if expected else 'rejected'})")
    print("CHECKER REGRESSION SUITE PASSED: 4/4")


if __name__ == "__main__":
    main()
