#!/usr/bin/env python3
"""Synchronize and audit canonical generalisation headline counts.

The layer-specific whole-state ledgers are the source of truth. Historical
frontier steps inside research notes are intentionally left untouched; only
canonical/headline surfaces are synchronized. Rewriting is deliberately
idempotent: already-normalized wording is accepted on subsequent runs.
"""
from pathlib import Path
import argparse
import csv
import re

from sync_current_state_hall_20260914 import rewrite as rewrite_hall_current_state

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1"
N34_LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"
N35_LEDGER = BASE / "WHOLE_STATE_LEDGER_N35.tsv"
ROOT_README = ROOT / "README.md"
CURRENT = ROOT / "CURRENT_STATE.md"
PACKAGE = BASE / "README.md"

BASE_EXCLUSIONS = 994
BASE_N34_SURVIVORS = 4506
BASE_N35_SURVIVORS = 78
CATALOGUE_TOTAL = BASE_EXCLUSIONS + BASE_N34_SURVIVORS + BASE_N35_SURVIVORS


def ledger_count(path):
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    states = [int(r["state"]) for r in rows]
    if len(states) != len(set(states)):
        raise SystemExit(f"duplicate state in {path.name}")
    return len(states)


def counts():
    c34 = ledger_count(N34_LEDGER)
    c35 = ledger_count(N35_LEDGER)
    n34 = BASE_N34_SURVIVORS - c34
    n35 = BASE_N35_SURVIVORS - c35
    if n34 < 0 or n35 < 0:
        raise SystemExit("negative layer survivor count")
    closures = c34 + c35
    survivors = n34 + n35
    exclusions = BASE_EXCLUSIONS + closures
    if exclusions + survivors != CATALOGUE_TOTAL:
        raise SystemExit("layer-aware catalogue accounting mismatch")
    return closures, exclusions, survivors, n34, n35, c34, c35


def commas(x):
    return f"{x:,}"


def sub_required(text, pattern, repl, label):
    new, n = re.subn(pattern, repl, text, count=1, flags=re.MULTILINE)
    if n != 1:
        raise SystemExit(f"canonical status pattern not found exactly once: {label}")
    return new


def rewrite_root(text, c, e, s, n34, n35, c34, c35):
    text = sub_required(
        text,
        r"(Candidate proofs and reproducible research\. \*\*Updated .*?: )[\d,]+ quantified whole-state closures, frontier [\d,]+/[\d,]+(\. Independent mathematical review,)",
        rf"\g<1>{commas(c)} quantified whole-state closures, frontier {commas(e)}/{commas(s)}\g<2>",
        "root headline",
    )
    text = sub_required(
        text,
        r"^\| Generalisation frontier \| .*?\|$",
        f"| Generalisation frontier | **{commas(e)} exclusions / {commas(s)} survivors** from the canonical quantified whole-state ledgers; `{commas(n34)}` are N34 equality-derived and `{commas(n35)}` are N35 `m=306`-derived; these are scalar states in a frozen experiment, not surviving graphs |",
        "root frontier table",
    )
    return text


def rewrite_current(text, c, e, s, n34, n35, c34, c35):
    lines = text.splitlines()
    found_head = found_guard = False
    for i, line in enumerate(lines):
        if line.startswith("**Research state reconciled:**"):
            line = re.sub(r"[\d,]+ quantified whole-state closures", f"{commas(c)} quantified whole-state closures", line, count=1)
            line = re.sub(r"frontier \*\*[\d,]+/[\d,]+\*\*", f"frontier **{commas(e)}/{commas(s)}**", line, count=1)
            line = re.sub(
                r"\(`?[\d,]+`? N34-derived survivors plus `?[\d,]+`? N35-derived survivors\)",
                f"(`{commas(n34)}` N34-derived survivors plus `{commas(n35)}` N35-derived survivors)",
                line,
                count=1,
            )
            lines[i] = line
            found_head = True
        if line.startswith("**Durability guard:**"):
            line = re.sub(r"currently verifies `?[\d,]+`? ledger states", f"currently verifies `{commas(c34)}` ledger states", line, count=1)
            lines[i] = line
            found_guard = True
    if not found_head or not found_guard:
        raise SystemExit("CURRENT_STATE canonical headline/guard not found")
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    return rewrite_hall_current_state(text)


def rewrite_package(text, c, e, s, n34, n35, c34, c35):
    text = sub_required(
        text,
        r"The canonical ledger now has \*\*[\d,]+ quantified N34-derived whole-state exclusions\*\*:",
        f"The canonical ledger now has **{commas(c34)} quantified N34-derived whole-state exclusions**:",
        "package current N34 ledger count",
    )
    text = sub_required(
        text,
        r"The canonical \[`WHOLE_STATE_LEDGER\.tsv`\]\(WHOLE_STATE_LEDGER\.tsv\) contains \*\*[\d,]+ quantified (?:N34 )?whole-state exclusions\*\*\.",
        f"The canonical [`WHOLE_STATE_LEDGER.tsv`](WHOLE_STATE_LEDGER.tsv) contains **{commas(c34)} quantified N34 whole-state exclusions**.",
        "package canonical N34 ledger block",
    )
    text = sub_required(
        text,
        r"Canonical frontier: \*\*[\d,]+ exclusions / [\d,]+ survivors\*\* \(`?[\d,]+`? N34-derived plus `?[\d,]+`? N35-derived\)\.",
        f"Canonical frontier: **{commas(e)} exclusions / {commas(s)} survivors** (`{commas(n34)}` N34-derived plus `{commas(n35)}` N35-derived).",
        "package canonical frontier block",
    )
    return text


def expected_snippets(c, e, s, n34, n35, c34, c35):
    return {
        ROOT_README: [
            f"{commas(c)} quantified whole-state closures, frontier {commas(e)}/{commas(s)}",
            f"**{commas(e)} exclusions / {commas(s)} survivors** from the canonical quantified whole-state ledgers; `{commas(n34)}` are N34 equality-derived and `{commas(n35)}` are N35",
        ],
        CURRENT: [
            f"**{commas(c)} quantified whole-state closures**, frontier **{commas(e)}/{commas(s)}** (`{commas(n34)}` N34-derived survivors plus `{commas(n35)}` N35-derived survivors)",
            f"currently verifies `{commas(c34)}` ledger states",
            "<!-- HALL-STRUCTURE-2026-09-14:START -->",
            "Exact type-level max-flow theorem",
            "SHARP_DOMINANCE_UPSET_HALL.md",
            "PRINCIPAL_UPSET_COUNTEREXAMPLE.md",
            "34820187136",
            "separate gated promotion only after agreement",
        ],
        PACKAGE: [
            f"**{commas(c34)} quantified N34-derived whole-state exclusions**",
            f"contains **{commas(c34)} quantified N34 whole-state exclusions**",
            f"Canonical frontier: **{commas(e)} exclusions / {commas(s)} survivors** (`{commas(n34)}` N34-derived plus `{commas(n35)}` N35-derived).",
        ],
    }


def check(c, e, s, n34, n35, c34, c35):
    for path, snippets in expected_snippets(c, e, s, n34, n35, c34, c35).items():
        text = path.read_text()
        missing = [x for x in snippets if x not in text]
        if missing:
            raise SystemExit(f"canonical status drift in {path}: missing {missing}")
    print("GENERALISATION_STATUS_OK")
    print("total_closures", c)
    print("n34_closures", c34)
    print("n35_closures", c35)
    print("exclusions", e)
    print("survivors", s)
    print("n34_survivors", n34)
    print("n35_survivors", n35)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    vals = counts()
    if args.write:
        ROOT_README.write_text(rewrite_root(ROOT_README.read_text(), *vals))
        CURRENT.write_text(rewrite_current(CURRENT.read_text(), *vals))
        PACKAGE.write_text(rewrite_package(PACKAGE.read_text(), *vals))
    check(*vals)


if __name__ == "__main__":
    main()
