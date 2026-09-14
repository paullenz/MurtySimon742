#!/usr/bin/env python3
"""Freshly audit discovered relational exclusions with two implementations.

Each candidate state is reconstructed as a one-state input and rerun through
both the primary vector-enumeration scanner and the independent type-count
scanner. Exact agreement of proof-relevant counters is required. Timeouts,
errors, non-exclusion, malformed output and disagreement are unresolved audit
outcomes and are never promoted.
"""
from pathlib import Path
import argparse
import csv
import json
import subprocess
import time

RESULT_FIELDS = [
    "layer", "state_id", "S", "Emax", "profiles_tested",
    "paircap_fail", "paircap_pass", "incidence_fail", "incidence_pass",
    "pairhall_fail", "pairhall_pass", "targethall_fail", "targethall_pass",
    "cost_fail", "status", "witness_E", "witness_cost", "witness_envelope",
    "seconds", "witness_rho", "witness_q",
]
COMPARE_FIELDS = [
    "layer", "state_id", "S", "Emax", "profiles_tested",
    "paircap_fail", "paircap_pass", "incidence_fail", "incidence_pass",
    "pairhall_fail", "pairhall_pass", "targethall_fail", "targethall_pass",
    "cost_fail", "status", "witness_E", "witness_cost", "witness_envelope",
]


def atomic_write(path, text):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def read_input(path):
    lines = [x.strip() for x in Path(path).read_text().splitlines() if x.strip()]
    if not lines:
        raise SystemExit("empty audit input")
    n = int(lines[0])
    body = lines[1:]
    if n != len(body):
        raise SystemExit(f"audit input count mismatch: {n} != {len(body)}")
    keys = [(int(x.split()[0]), int(x.split()[1])) for x in body]
    if len(keys) != len(set(keys)):
        raise SystemExit("duplicate layer/state in audit input")
    return body


def parse_one(path, expected_layer, expected_state):
    with Path(path).open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if len(rows) != 1:
        raise ValueError(f"expected one row, got {len(rows)}")
    row = rows[0]
    if list(row) != RESULT_FIELDS:
        raise ValueError(f"unexpected output schema: {list(row)}")
    if int(row["layer"]) != expected_layer or int(row["state_id"]) != expected_state:
        raise ValueError("layer/state mismatch")
    return row


def write_results(path, rows):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=RESULT_FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    tmp.replace(path)


def run_scanner(binary, one_input, output, replay, timeout):
    try:
        proc = subprocess.run(
            [binary, str(one_input), str(output)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        Path(replay).write_text(proc.stdout or "")
        if proc.returncode != 0:
            return False, {"reason": "PROCESS_ERROR", "returncode": proc.returncode}
        return True, None
    except subprocess.TimeoutExpired as exc:
        text = exc.stdout or ""
        if isinstance(text, bytes):
            text = text.decode(errors="replace")
        Path(replay).write_text(text)
        return False, {"reason": "STATE_TIMEOUT", "timeout_seconds": timeout}
    except Exception as exc:
        Path(replay).write_text(f"runner exception: {exc!r}\n")
        return False, {"reason": "RUNNER_EXCEPTION", "detail": repr(exc)}


def payload(shard, expected, audited, unresolved, started):
    return {
        "schema": "post-pair-relational-crosscheck-shard-v1",
        "shard": shard,
        "states_expected": expected,
        "states_audited": len(audited),
        "audited_keys": [[int(r["layer"]), int(r["state_id"])] for r in audited],
        "unresolved": unresolved,
        "elapsed_seconds": time.monotonic() - started,
        "promotion_status": "NOT_PROMOTED",
        "external_review": "OPEN",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--primary", default="./scan_post_pair_relational")
    ap.add_argument("--independent", default="./scan_post_pair_relational_types")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--shard", type=int, required=True)
    ap.add_argument("--state-timeout", type=int, default=300)
    args = ap.parse_args()

    lines = read_input(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    audited = []
    unresolved = []
    started = time.monotonic()
    results_path = outdir / "AUDITED_RESULTS.tsv"
    status_path = outdir / "AUDIT_STATUS.json"

    for index, line in enumerate(lines):
        tok = line.split()
        layer, state = int(tok[0]), int(tok[1])
        state_dir = outdir / f"layer-{layer}-state-{state}"
        state_dir.mkdir(exist_ok=True)
        one_input = state_dir / "INPUT.txt"
        primary_out = state_dir / "PRIMARY.tsv"
        independent_out = state_dir / "INDEPENDENT.tsv"
        atomic_write(one_input, "1\n" + line + "\n")
        t0 = time.monotonic()

        ok, err = run_scanner(args.primary, one_input, primary_out, state_dir / "PRIMARY_REPLAY.txt", args.state_timeout)
        if not ok:
            err.update({"layer": layer, "state_id": state, "implementation": "primary", "seconds": time.monotonic() - t0})
            unresolved.append(err)
        else:
            try:
                primary = parse_one(primary_out, layer, state)
            except Exception as exc:
                unresolved.append({"layer": layer, "state_id": state, "implementation": "primary", "reason": "MALFORMED_OUTPUT", "detail": str(exc), "seconds": time.monotonic() - t0})
            else:
                ok2, err2 = run_scanner(args.independent, one_input, independent_out, state_dir / "INDEPENDENT_REPLAY.txt", args.state_timeout)
                if not ok2:
                    err2.update({"layer": layer, "state_id": state, "implementation": "independent", "seconds": time.monotonic() - t0})
                    unresolved.append(err2)
                else:
                    try:
                        independent = parse_one(independent_out, layer, state)
                    except Exception as exc:
                        unresolved.append({"layer": layer, "state_id": state, "implementation": "independent", "reason": "MALFORMED_OUTPUT", "detail": str(exc), "seconds": time.monotonic() - t0})
                    else:
                        differences = [
                            {"field": field, "primary": primary[field], "independent": independent[field]}
                            for field in COMPARE_FIELDS
                            if primary[field] != independent[field]
                        ]
                        comparison = {
                            "schema": "post-pair-relational-state-crosscheck-v1",
                            "layer": layer,
                            "state_id": state,
                            "fields": COMPARE_FIELDS,
                            "differences": differences,
                            "primary_status": primary["status"],
                            "independent_status": independent["status"],
                            "result": "PASS" if not differences and primary["status"] == "RELATIONAL_EXCLUDED" else "FAIL",
                        }
                        atomic_write(state_dir / "COMPARE.json", json.dumps(comparison, indent=2, sort_keys=True) + "\n")
                        if comparison["result"] == "PASS":
                            audited.append(primary)
                        else:
                            unresolved.append({
                                "layer": layer,
                                "state_id": state,
                                "reason": "CROSSCHECK_MISMATCH_OR_NONEXCLUSION",
                                "differences": differences,
                                "primary_status": primary["status"],
                                "independent_status": independent["status"],
                                "seconds": time.monotonic() - t0,
                            })

        write_results(results_path, audited)
        atomic_write(status_path, json.dumps(payload(args.shard, len(lines), audited, unresolved, started), indent=2, sort_keys=True) + "\n")
        print(f"audit checkpoint shard={args.shard} index={index+1}/{len(lines)} layer={layer} state={state} audited={len(audited)} unresolved={len(unresolved)}", flush=True)

    final = payload(args.shard, len(lines), audited, unresolved, started)
    final["finished"] = True
    atomic_write(status_path, json.dumps(final, indent=2, sort_keys=True) + "\n")
    print(json.dumps(final, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
