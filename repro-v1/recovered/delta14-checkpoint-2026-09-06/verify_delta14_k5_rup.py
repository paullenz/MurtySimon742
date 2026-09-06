#!/usr/bin/env python3
"""Independently replay RUP traces for k=5 or k=6.

For every added proof clause C, the checker asks a separate CaDiCaL instance
whether unit propagation on the current clause database with assumptions -C
finds a conflict.  Deletion records are safely ignored: retained clauses have
already passed RUP and are therefore consequences of the original CNF.
With --checker, use the independent C++ watched-literal implementation instead.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import gzip
import hashlib
import json
import subprocess
import tempfile
import time
from pathlib import Path

from pysat.solvers import Solver

from delta14_k5_core_sat import build, decode_graph6


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify(task):
    proof_root, row, checker_path = task
    started = time.time()
    cnf, _ = build(
        decode_graph6(row["graph6"]), row["r"],
        rho_pattern=tuple(row["rho"]),
        expected_delta_f=row.get("max_degree_f", 4),
    )
    dimacs = cnf.to_dimacs().encode("ascii")
    if sha256_bytes(dimacs) != row["formula_sha256"]:
        raise RuntimeError("rebuilt CNF hash mismatch")

    path = Path(proof_root) / row["proof_path"]
    compressed = path.read_bytes()
    if sha256_bytes(compressed) != row["proof_gzip_sha256"]:
        raise RuntimeError("compressed proof hash mismatch")
    proof = gzip.decompress(compressed)
    if sha256_bytes(proof) != row["proof_sha256"]:
        raise RuntimeError("proof hash mismatch")

    if checker_path:
        with tempfile.TemporaryDirectory(prefix="delta14-rup-") as temp:
            cnf_path = Path(temp) / "formula.cnf"
            cnf_path.write_bytes(dimacs)
            result = subprocess.run(
                [checker_path, str(cnf_path), str(path.resolve())],
                capture_output=True, text=True, check=False,
            )
        if result.returncode != 0 or not result.stdout.startswith("VERIFIED UNSAT"):
            raise RuntimeError(f"C++ checker failed: {result.stdout} {result.stderr}")
        return {
            "r": row["r"], "core_index": row["core_index"],
            "rho": row["rho"], "status": "RUP-VERIFIED",
            "checker": "independent C++ watched-literal RUP checker",
            "checker_output": result.stdout.strip(),
            "formula_sha256": row["formula_sha256"],
            "proof_sha256": row["proof_sha256"],
            "seconds": time.time() - started,
        }

    additions = 0
    deletions = 0
    saw_empty = False
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as checker:
        for line_number, raw in enumerate(proof.splitlines(), start=1):
            fields = raw.split()
            if not fields:
                continue
            deleting = fields[0] == b"d"
            if deleting:
                fields = fields[1:]
            if not fields or fields[-1] != b"0":
                raise RuntimeError(f"malformed proof line {line_number}")
            clause = [int(item) for item in fields[:-1]]
            if deleting:
                deletions += 1
                continue
            status, _ = checker.propagate(
                assumptions=[-literal for literal in clause]
            )
            if status:
                raise RuntimeError(f"non-RUP clause at proof line {line_number}")
            additions += 1
            if not clause:
                saw_empty = True
                break
            checker.add_clause(clause)

    if not saw_empty:
        raise RuntimeError("proof does not derive the empty clause")
    return {
        "r": row["r"],
        "core_index": row["core_index"],
        "rho": row["rho"],
        "status": "RUP-VERIFIED",
        "formula_sha256": row["formula_sha256"],
        "proof_sha256": row["proof_sha256"],
        "additions_checked": additions,
        "deletions_ignored": deletions,
        "seconds": time.time() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    parser.add_argument("--proof-root", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--checker", help="Optional compiled check_drup_fast path")
    args = parser.parse_args()

    manifest = Path(args.manifest).resolve()
    rows = [json.loads(line) for line in manifest.read_text().splitlines()
            if line.strip()]
    rows.sort(key=lambda row: (
        row["r"], row["core_index"], row["pattern_ordinal"]
    ))
    if args.limit is not None:
        rows = rows[:args.limit]
    started = time.time()
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    checkpoint = output.with_suffix(".jsonl")
    completed = {}
    if checkpoint.exists():
        for line in checkpoint.read_text().splitlines():
            entry = json.loads(line)
            completed[(entry["r"], entry["core_index"], tuple(entry["rho"]))] = entry
    results = []
    pending = []
    for row in rows:
        key = (row["r"], row["core_index"], tuple(row["rho"]))
        cached = completed.get(key)
        if cached and (
            cached.get("status") != "RUP-VERIFIED"
            or cached.get("formula_sha256") != row["formula_sha256"]
            or cached.get("proof_sha256") != row["proof_sha256"]
        ):
            raise RuntimeError("stale replay checkpoint; use a fresh output path")
        if cached:
            results.append(completed[key])
        else:
            pending.append(row)
    checker_path = str(Path(args.checker).resolve()) if args.checker else None
    print(json.dumps({"already_verified": len(results), "pending": len(pending)}), flush=True)
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.jobs
    ) as executor:
        futures = [executor.submit(verify, (args.proof_root, row, checker_path))
                   for row in pending]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            with checkpoint.open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(result, sort_keys=True) + "\n")
            if len(results) % 10 == 0 or len(results) == len(rows):
                print(json.dumps({
                    "verified": len(results),
                    "remaining": len(rows) - len(results),
                    "elapsed_seconds": time.time() - started,
                }, sort_keys=True), flush=True)

    # Rewrite the canonical complete checkpoint once all workers finish.
    checkpoint.write_text("".join(json.dumps(row, sort_keys=True)+"\n"
                                  for row in results), encoding="utf-8")
    output.write_text(json.dumps({
        "status": "ALL-RUP-VERIFIED",
        "manifest": str(manifest),
        "proof_root": str(Path(args.proof_root).resolve()),
        "records": len(results),
        "results": results,
        "seconds": time.time() - started,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
