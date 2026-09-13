#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1"
LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"

# Frozen catalogue accounting before the whole-state closures listed here.
BASE_EXCLUSIONS = 994
BASE_SURVIVORS = 4584
CATALOGUE_TOTAL = 5578

# These closures were independently committed on parallel intraday branches.
# Keeping the minimum set explicit prevents a later README/ledger rewrite from
# silently dropping one branch of work.  New closures may be added freely.
KNOWN_MINIMUM = {
    122, 153, 154, 227, 230, 279, 282, 283, 382, 385, 519, 526, 588
}


def main():
    with LEDGER.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if not rows:
        raise SystemExit("empty whole-state ledger")
    states = [int(r["state"]) for r in rows]
    if len(states) != len(set(states)):
        raise SystemExit("duplicate state in whole-state ledger")
    missing = sorted(KNOWN_MINIMUM - set(states))
    if missing:
        raise SystemExit(f"known whole-state closures missing from ledger: {missing}")
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
    print("exclusions", exclusions)
    print("survivors", survivors)
    print("state_ids", ",".join(map(str, sorted(states))))


if __name__ == "__main__":
    main()
