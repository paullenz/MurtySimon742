#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1"
CERT = BASE / "POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv"
AUDIT = BASE / "POST_PAIR_RELATIONAL_RECOVERY_AUDIT.json"
LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"
RECORD = "POST_PAIR_RELATIONAL_RECOVERY.md"
METHOD = "post-pair relational cross-implementation closure"

EXPECTED_IDS = [
    961, 1025, 2620, 2706, 2897, 3007, 3139, 3202,
    3302, 3359, 3480, 3599, 4145, 4559, 4654, 4994,
]
EXPECTED_TRIGGER_RUN = 34817529642
EXPECTED_TRIGGER_HEAD = "c2b426da46284617681081797d1c571d23cd531d"
# Filled after the aggregate certificate is frozen and committed.
EXPECTED_CERT_SHA256 = "c1ce4e645edf9dcc3e2f39ef42bd85030449b161549978877eb2e15ab2abe832"


def main():
    if not CERT.is_file() or not AUDIT.is_file():
        raise SystemExit("missing post-pair relational recovery certificate/audit")

    cert_raw = CERT.read_bytes()
    cert_sha = hashlib.sha256(cert_raw).hexdigest()
    if EXPECTED_CERT_SHA256 is not None and cert_sha != EXPECTED_CERT_SHA256:
        raise SystemExit(f"relational certificate hash mismatch: {cert_sha}")

    with CERT.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = [int(r["state_id"]) for r in rows]
    if ids != EXPECTED_IDS:
        raise SystemExit(f"relational certificate ids mismatch: {ids}")
    for row in rows:
        if row["layer"] != "0":
            raise SystemExit(f"non-N34 state in relational certificate: {row}")
        if row["status"] != "RELATIONAL_EXCLUDED":
            raise SystemExit(f"non-excluded state in relational certificate: {row}")
        if row["witness_E"] != "-1":
            raise SystemExit(f"unexpected witness in excluded state: {row}")

    audit = json.loads(AUDIT.read_text())
    if audit.get("trigger_run_id") != EXPECTED_TRIGGER_RUN:
        raise SystemExit("unexpected relational audit run id")
    if audit.get("trigger_head_sha") != EXPECTED_TRIGGER_HEAD:
        raise SystemExit("unexpected relational audit head sha")
    if audit.get("state_ids") != EXPECTED_IDS:
        raise SystemExit("relational audit state list mismatch")
    if audit.get("state_count") != len(EXPECTED_IDS):
        raise SystemExit("relational audit state count mismatch")
    if audit.get("all_comparisons") != "PASS":
        raise SystemExit("relational implementation comparison did not pass")
    if audit.get("combined_tsv_sha256") != cert_sha:
        raise SystemExit("relational audit does not hash-bind the certificate")

    with LEDGER.open(newline="") as f:
        ledger = list(csv.DictReader(f, delimiter="\t"))
    by_state = {int(r["state"]): r for r in ledger}
    for state in EXPECTED_IDS:
        if state not in by_state:
            raise SystemExit(f"relational closure missing from ledger: {state}")
        row = by_state[state]
        if row["method"] != METHOD or row["record"] != RECORD:
            raise SystemExit(f"wrong relational ledger provenance for {state}: {row}")

    if not (BASE / RECORD).is_file():
        raise SystemExit("missing relational recovery record")

    print("POST_PAIR_RELATIONAL_RECOVERY_OK")
    print("states", len(EXPECTED_IDS))
    print("certificate_sha256", cert_sha)
    print("trigger_run", EXPECTED_TRIGGER_RUN)
    print("trigger_head", EXPECTED_TRIGGER_HEAD)


if __name__ == "__main__":
    main()
