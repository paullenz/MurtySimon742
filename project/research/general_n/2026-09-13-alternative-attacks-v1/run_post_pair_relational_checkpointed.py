#!/usr/bin/env python3
"""Run a relational frontier shard with durable per-state checkpoints.

Discovery only. A timeout, process error, malformed output or missing output is
recorded explicitly and is never treated as an exclusion. Each layer-state is
run in its own subprocess and written to disk before the next one starts, so a
later job cancellation cannot erase already completed mathematical results.
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


def read_input(path: Path):
    lines = [x.strip() for x in path.read_text().splitlines() if x.strip()]
    if not lines:
        raise SystemExit("empty shard input")
    n = int(lines[0])
    states = lines[1:]
    if len(states) != n:
        raise SystemExit(f"shard input count mismatch: header={n} rows={len(states)}")
    keys = [(int(line.split()[0]), int(line.split()[1])) for line in states]
    if len(keys) != len(set(keys)):
        raise SystemExit("duplicate layer-state key in shard input")
    return states


def atomic_write(path: Path, text: str):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def write_results(path: Path, rows):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=RESULT_FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow(row)
    tmp.replace(path)


def parse_single_result(path: Path, expected_layer: int, expected_state: int):
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if len(rows) != 1:
        raise ValueError(f"expected one output row, got {len(rows)}")
    row = rows[0]
    key = (int(row["layer"]), int(row["state_id"]))
    expected = (expected_layer, expected_state)
    if key != expected:
        raise ValueError(f"layer-state mismatch: expected {expected}, got {key}")
    if list(row.keys()) != RESULT_FIELDS:
        raise ValueError(f"unexpected output schema: {list(row.keys())}")
    return row


def status_payload(shard, input_path, total, rows, unresolved, started):
    return {
        "schema": "post-pair-relational-checkpoint-shard-v2-layer-state",
        "shard": shard,
        "input": str(input_path),
        "states_total": total,
        "states_completed": len(rows),
        "relational_excluded": sum(r["status"] == "RELATIONAL_EXCLUDED" for r in rows),
        "survives_relational": sum(r["status"] == "SURVIVES_RELATIONAL" for r in rows),
        "unresolved": unresolved,
        "completed_keys": [
            [int(r["layer"]), int(r["state_id"])] for r in rows
        ],
        "excluded_keys": [
            [int(r["layer"]), int(r["state_id"])]
            for r in rows if r["status"] == "RELATIONAL_EXCLUDED"
        ],
        "elapsed_seconds": time.monotonic() - started,
        "trust_boundary": "Discovery only; exclusions require independent cross-implementation audit before promotion.",
        "external_review": "OPEN",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--scanner", default="./scan_post_pair_relational")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--shard", type=int, required=True)
    ap.add_argument("--state-timeout", type=int, default=300)
    args = ap.parse_args()

    input_path = Path(args.input)
    state_lines = read_input(input_path)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    results_path = outdir / "SHARD_RESULTS.tsv"
    status_path = outdir / "SHARD_STATUS.json"
    rows = []
    unresolved = []
    started = time.monotonic()

    for index, line in enumerate(state_lines):
        tok = line.split()
        layer, state = int(tok[0]), int(tok[1])
        state_dir = outdir / f"layer-{layer}-state-{state}"
        state_dir.mkdir(exist_ok=True)
        one_input = state_dir / "INPUT.txt"
        one_output = state_dir / "RESULT.tsv"
        replay = state_dir / "REPLAY.txt"
        atomic_write(one_input, "1\n" + line + "\n")

        t0 = time.monotonic()
        try:
            proc = subprocess.run(
                [args.scanner, str(one_input), str(one_output)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=args.state_timeout,
                check=False,
            )
            replay.write_text(proc.stdout or "")
            if proc.returncode != 0:
                unresolved.append({
                    "layer": layer,
                    "state_id": state,
                    "reason": "PROCESS_ERROR",
                    "returncode": proc.returncode,
                    "seconds": time.monotonic() - t0,
                })
            else:
                try:
                    row = parse_single_result(one_output, layer, state)
                    rows.append(row)
                except Exception as exc:
                    unresolved.append({
                        "layer": layer,
                        "state_id": state,
                        "reason": "MALFORMED_OUTPUT",
                        "detail": str(exc),
                        "seconds": time.monotonic() - t0,
                    })
        except subprocess.TimeoutExpired as exc:
            text = exc.stdout or ""
            if isinstance(text, bytes):
                text = text.decode(errors="replace")
            replay.write_text(text)
            unresolved.append({
                "layer": layer,
                "state_id": state,
                "reason": "STATE_TIMEOUT",
                "timeout_seconds": args.state_timeout,
                "seconds": time.monotonic() - t0,
            })
        except Exception as exc:
            replay.write_text(f"runner exception: {exc!r}\n")
            unresolved.append({
                "layer": layer,
                "state_id": state,
                "reason": "RUNNER_EXCEPTION",
                "detail": repr(exc),
                "seconds": time.monotonic() - t0,
            })

        write_results(results_path, rows)
        atomic_write(
            status_path,
            json.dumps(
                status_payload(args.shard, input_path, len(state_lines), rows, unresolved, started),
                indent=2,
                sort_keys=True,
            ) + "\n",
        )
        print(
            f"checkpoint shard={args.shard} index={index+1}/{len(state_lines)} "
            f"layer={layer} state={state} completed={len(rows)} unresolved={len(unresolved)}",
            flush=True,
        )

    payload = status_payload(args.shard, input_path, len(state_lines), rows, unresolved, started)
    payload["finished"] = True
    atomic_write(status_path, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
