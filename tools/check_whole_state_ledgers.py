#!/usr/bin/env python3
"""Layer-aware accounting guard for the frozen N34/N35 generalisation experiment."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1"
N34_LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"
N35_LEDGER = BASE / "WHOLE_STATE_LEDGER_N35.tsv"

BASE_EXCLUSIONS = 994
BASE_N34_SURVIVORS = 4506
BASE_N35_SURVIVORS = 78
CATALOGUE_TOTAL = BASE_EXCLUSIONS + BASE_N34_SURVIVORS + BASE_N35_SURVIVORS


def read_ledger(path):
    if not path.is_file():
        raise SystemExit(f"missing ledger: {path}")
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    expected = ["state", "method", "record"]
    if rows:
        if list(rows[0]) != expected:
            raise SystemExit(f"wrong ledger schema for {path}: {list(rows[0])}")
    else:
        header = path.read_text().splitlines()[0].split("\t") if path.read_text().splitlines() else []
        if header != expected:
            raise SystemExit(f"wrong empty-ledger schema for {path}: {header}")
    ids = [int(r["state"]) for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"duplicate state within {path.name}")
    for r in rows:
        if not r["method"].strip() or not r["record"].strip():
            raise SystemExit(f"blank provenance in {path.name}: {r}")
        record = BASE / r["record"]
        if not record.is_file():
            raise SystemExit(f"missing closure record in {path.name}: {r['record']}")
    return rows


def main():
    n34 = read_ledger(N34_LEDGER)
    n35 = read_ledger(N35_LEDGER)
    n34_survivors = BASE_N34_SURVIVORS - len(n34)
    n35_survivors = BASE_N35_SURVIVORS - len(n35)
    if n34_survivors < 0 or n35_survivors < 0:
        raise SystemExit("negative layer survivor count")
    closures = len(n34) + len(n35)
    survivors = n34_survivors + n35_survivors
    exclusions = BASE_EXCLUSIONS + closures
    if exclusions + survivors != CATALOGUE_TOTAL:
        raise SystemExit("layer-aware catalogue accounting mismatch")

    print("WHOLE_STATE_LEDGERS_OK")
    print("n34_closures", len(n34))
    print("n35_closures", len(n35))
    print("total_closures", closures)
    print("n34_survivors", n34_survivors)
    print("n35_survivors", n35_survivors)
    print("survivors", survivors)
    print("exclusions", exclusions)


if __name__ == "__main__":
    main()
