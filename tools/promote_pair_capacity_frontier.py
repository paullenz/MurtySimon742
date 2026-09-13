#!/usr/bin/env python3
"""Promote the independently audited pair-capacity frontier closures.

This is an idempotent metadata operation. It reads the exact state-id
certificate committed at
  project/research/general_n/2026-09-13-alternative-attacks-v1/
      PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv
and ensures every listed state appears in WHOLE_STATE_LEDGER.tsv with the
canonical family method/record.

No mathematical search is performed here. The mathematical audit is preserved
in PAIR_CAPACITY_FRONTIER_AUDIT.md; this script only makes the canonical ledger
accounting match that audited result.
"""
from pathlib import Path
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1"
IDS = BASE / "PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv"
LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"
AUDIT = BASE / "PAIR_CAPACITY_FRONTIER_AUDIT.md"

EXPECTED_COUNT = 943
EXPECTED_IDS_SHA256 = "f2f3d581a7bb69749d66fd07d7bfd51e5303cf8d5b4445b9b08c16cb2944e1a1"
METHOD = "potential-pair capacity frontier closure"
RECORD = "PAIR_CAPACITY_FRONTIER_AUDIT.md"


def read_ids():
    raw = IDS.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_IDS_SHA256:
        raise SystemExit(f"closure-id certificate hash mismatch: {digest}")
    with IDS.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = [int(r["state_id"]) for r in rows]
    if len(ids) != EXPECTED_COUNT or len(set(ids)) != EXPECTED_COUNT:
        raise SystemExit(f"expected {EXPECTED_COUNT} unique ids, got {len(ids)}/{len(set(ids))}")
    if ids != sorted(ids):
        raise SystemExit("closure-id certificate must be sorted")
    return ids


def main():
    if not AUDIT.is_file():
        raise SystemExit("missing PAIR_CAPACITY_FRONTIER_AUDIT.md")
    ids = read_ids()

    with LEDGER.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows:
        raise SystemExit("empty whole-state ledger")

    by_state = {int(r["state"]): r for r in rows}
    if len(by_state) != len(rows):
        raise SystemExit("duplicate state in existing whole-state ledger")

    added = 0
    for state in ids:
        if state in by_state:
            row = by_state[state]
            if row["method"] != METHOD or row["record"] != RECORD:
                raise SystemExit(
                    f"state {state} already ledgered with different provenance: {row}"
                )
            continue
        row = {"state": str(state), "method": METHOD, "record": RECORD}
        rows.append(row)
        by_state[state] = row
        added += 1

    # Keep the original historical rows first, then the family rows in numeric
    # order. This avoids rewriting the pre-existing closure chronology while
    # making the promoted block deterministic.
    historical = [r for r in rows if r["record"] != RECORD]
    family = sorted((r for r in rows if r["record"] == RECORD), key=lambda r: int(r["state"]))
    rows = historical + family

    out = io.StringIO()
    w = csv.DictWriter(out, fieldnames=["state", "method", "record"], delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    LEDGER.write_text(out.getvalue())

    print("PAIR_CAPACITY_FRONTIER_PROMOTION_OK")
    print("certificate_ids", len(ids))
    print("added", added)
    print("ledger_states", len(rows))
    print("catalogue_exclusions", 994 + len(rows))
    print("catalogue_survivors", 4584 - len(rows))


if __name__ == "__main__":
    main()
