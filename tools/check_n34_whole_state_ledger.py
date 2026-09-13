#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1"
LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"
PAIR_FAMILY = BASE / "PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv"
PAIR_AUDIT = BASE / "PAIR_CAPACITY_FRONTIER_AUDIT.md"

# Frozen catalogue accounting before the whole-state closures listed here.
BASE_EXCLUSIONS = 994
BASE_SURVIVORS = 4584
CATALOGUE_TOTAL = 5578

# Individually established closures that predate the large pair-capacity family.
KNOWN_INDIVIDUAL = {
    60, 77, 122, 153, 154, 227, 230, 231, 279, 282, 283, 382, 385, 519, 526, 588,
    13518, 13519,
}

PAIR_EXPECTED_COUNT = 943
PAIR_EXPECTED_SHA256 = "f2f3d581a7bb69749d66fd07d7bfd51e5303cf8d5b4445b9b08c16cb2944e1a1"
PAIR_METHOD = "potential-pair capacity frontier closure"
PAIR_RECORD = "PAIR_CAPACITY_FRONTIER_AUDIT.md"


def pair_family_ids():
    raw = PAIR_FAMILY.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != PAIR_EXPECTED_SHA256:
        raise SystemExit(f"pair-capacity closure certificate hash mismatch: {digest}")
    with PAIR_FAMILY.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = [int(r["state_id"]) for r in rows]
    if len(ids) != PAIR_EXPECTED_COUNT or len(set(ids)) != PAIR_EXPECTED_COUNT:
        raise SystemExit(
            f"pair-capacity certificate expected {PAIR_EXPECTED_COUNT} unique ids; "
            f"got {len(ids)}/{len(set(ids))}"
        )
    if ids != sorted(ids):
        raise SystemExit("pair-capacity closure certificate is not sorted")
    return set(ids)


def main():
    if not PAIR_AUDIT.is_file():
        raise SystemExit("missing PAIR_CAPACITY_FRONTIER_AUDIT.md")
    family = pair_family_ids()
    known_minimum = KNOWN_INDIVIDUAL | family
    if len(known_minimum) != len(KNOWN_INDIVIDUAL) + PAIR_EXPECTED_COUNT:
        raise SystemExit("pair-capacity family overlaps an individually ledgered closure")

    with LEDGER.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows:
        raise SystemExit("empty whole-state ledger")

    states = [int(r["state"]) for r in rows]
    if len(states) != len(set(states)):
        raise SystemExit("duplicate state in whole-state ledger")
    state_set = set(states)

    missing = sorted(known_minimum - state_set)
    if missing:
        raise SystemExit(f"known whole-state closures missing from ledger: {missing}")

    by_state = {int(r["state"]): r for r in rows}
    for state in family:
        r = by_state[state]
        if r["method"] != PAIR_METHOD or r["record"] != PAIR_RECORD:
            raise SystemExit(
                f"pair-capacity closure {state} has wrong ledger provenance: {r}"
            )

    for r in rows:
        record = BASE / r["record"]
        if not record.is_file():
            raise SystemExit(f"missing closure record for state {r['state']}: {r['record']}")

    exclusions = BASE_EXCLUSIONS + len(states)
    survivors = BASE_SURVIVORS - len(states)
    if exclusions + survivors != CATALOGUE_TOTAL:
        raise SystemExit("catalogue accounting mismatch")

    print("N34_WHOLE_STATE_LEDGER_OK")
    print("states", len(states))
    print("protected_individual", len(KNOWN_INDIVIDUAL))
    print("protected_pair_family", len(family))
    print("exclusions", exclusions)
    print("survivors", survivors)
    print("state_ids", ",".join(map(str, sorted(states))))


if __name__ == "__main__":
    main()
