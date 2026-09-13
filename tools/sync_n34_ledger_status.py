#!/usr/bin/env python3
"""Synchronize durable N34 whole-state status from WHOLE_STATE_LEDGER.tsv.

This script deliberately touches only bounded status surfaces. Reviewer-material
links are protected by their separate guard and are not rewritten here.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1"
LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"
ROOT_README = ROOT / "README.md"
ALT_README = BASE / "README.md"
CURRENT = ROOT / "CURRENT_STATE.md"

BASE_EXCLUSIONS = 994
BASE_SURVIVORS = 4584
N35_SURVIVORS = 78


def rows():
    with LEDGER.open(newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def replace_one(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f"{label}: expected one replacement, got {n}")
    return out


def replace_or_insert_block(text, start, end, block, anchor_pattern, label):
    if start in text:
        pat = re.escape(start) + r".*?" + re.escape(end)
        return replace_one(text, pat, block, label, flags=re.S)
    return replace_one(text, anchor_pattern, block, label, flags=re.S)


def ledger_table(rs, prefix):
    lines = [
        "| State | Method | Record |",
        "|---:|---|---|",
    ]
    for r in rs:
        lines.append(f"| {r['state']} | {r['method']} | [`{r['record']}`]({prefix}{r['record']}) |")
    return "\n".join(lines)


def sync_root(rs, count, exclusions, survivors, n34_survivors):
    p = ROOT_README
    t = p.read_text()
    t = replace_one(
        t,
        r"\*\*Updated 13 September 2026 through[^\n]*remain OPEN\.\*\*",
        f"**Updated 13 September 2026 through the canonical N34 whole-state ledger: {count} quantified whole-state closures, frontier {exclusions:,}/{survivors:,}. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.**",
        "root headline",
    )
    t = replace_one(
        t,
        r"\| Generalisation frontier \|[^\n]*",
        f"| Generalisation frontier | **{exclusions:,} exclusions / {survivors:,} survivors** from the canonical N34 whole-state ledger; these are scalar states in a frozen experiment, not surviving graphs |",
        "root frontier row",
    )
    t = replace_one(
        t,
        r"## Quantifier pivot: [^\n]*whole-state exclusions",
        f"## Quantifier pivot: {count} whole-state exclusions",
        "root quantifier heading",
    )
    t = replace_one(
        t,
        r"## What the [^\n]* closures suggest",
        f"## What the {count} closures suggest",
        "root lesson heading",
    )

    start = "<!-- N34-WHOLE-STATE-LEDGER:START -->"
    end = "<!-- N34-WHOLE-STATE-LEDGER:END -->"
    block = (
        f"{start}\n"
        f"### Canonical N34 whole-state ledger\n\n"
        f"The canonical ledger records **{count} distinct quantified whole-state exclusions**. "
        f"This table is generated from [`WHOLE_STATE_LEDGER.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/WHOLE_STATE_LEDGER.tsv) so parallel lines of work cannot silently disappear from the headline count.\n\n"
        + ledger_table(rs, "project/research/general_n/2026-09-13-alternative-attacks-v1/")
        + f"\n\nThe current frozen frontier is therefore\n\n```text\n{exclusions:,} exclusions / {survivors:,} survivors,\n{n34_survivors:,} N34 equality-derived survivors,\n{N35_SURVIVORS} N35 m=306-derived survivors.\n```\n\n"
        "Survival in this catalogue is not graph feasibility.\n"
        f"{end}"
    )
    old_frontier = (
        r"The current frozen frontier is therefore\s*```text\n.*?```\s*"
        r"Survival in this catalogue is not graph feasibility\."
    )
    t = replace_or_insert_block(t, start, end, block, old_frontier, "root ledger block")
    p.write_text(t)


def sync_alt(rs, count, exclusions, survivors, n34_survivors):
    p = ALT_README
    t = p.read_text()
    state_list = ", ".join(r["state"] for r in rs)
    t = replace_one(
        t,
        r"The quantified line now has \*\*[^\n]*whole-state N34 exclusions\*\*:\s*```text\n.*?```",
        f"The quantified line now has **{count} whole-state N34 exclusions**:\n\n```text\n{state_list}.\n```",
        "alt closure count/list",
        flags=re.S,
    )
    t = replace_one(
        t,
        r"The latest three closures,[^\n]*",
        "The canonical union of all closure lines is recorded in [`WHOLE_STATE_LEDGER.tsv`](WHOLE_STATE_LEDGER.tsv); that ledger, rather than local ordinal wording in individual notes, controls the headline count.",
        "alt old latest-three sentence",
    )
    t = replace_one(
        t,
        r"The frozen frontier is now\s*```text\n.*?```\s*split as\s*```text\n.*?```",
        f"The frozen frontier is now\n\n```text\n{exclusions:,} exclusions / {survivors:,} survivors,\n```\n\nsplit as\n\n```text\n{n34_survivors:,} N34 equality-derived survivors,\n{N35_SURVIVORS} N35 m=306-derived survivors.\n```",
        "alt frontier",
        flags=re.S,
    )
    t = re.sub(r"## General lesson from the [^\n]* closures", f"## General lesson from the {count} closures", t)
    t = re.sub(r"None of the [^\n]* whole-state closures", f"None of the {count} whole-state closures", t)
    t = re.sub(r"explain the [^\n]* closures symbolically", f"explain the {count} closures symbolically", t)

    replacements = {
        122: "| 122 | `+1` | none — **whole state closed** ([`STATE_122_WHOLE_STATE.md`](STATE_122_WHOLE_STATE.md)) |",
        283: "| 283 | `+1` | none — **whole state closed** ([`STATE_283_WHOLE_STATE.md`](STATE_283_WHOLE_STATE.md)) |",
        154: "| 154 | `+1` | none — **whole state closed** ([`STATE_154_WHOLE_STATE.md`](STATE_154_WHOLE_STATE.md)) |",
        231: "| 231 | `+1` | none — **whole state closed** ([`STATE_231_WHOLE_STATE.md`](STATE_231_WHOLE_STATE.md)) |",
    }
    for sid, line in replacements.items():
        t = replace_one(t, rf"\| {sid} \|[^\n]*", line, f"alt matrix state {sid}")

    t = replace_one(
        t,
        r"This is a useful compression\.[^\n]*\n\nAfter state 153,[^\n]*\n",
        "This matrix has compressed further: states **122, 283, 154 and 231 are now whole-state closed** by endpoint class packing and its mixed-class Hall refinement. The remaining states from this seven-state ring are **77 and 60**; their preserved original weak layers are the next finite targets. These are necessary-condition scan survivors, not graphs.\n",
        "alt matrix interpretation",
    )

    t = replace_one(
        t,
        r"At scan time five were closed and four were active: states `230,282,385,519`\. State 519 is now closed\. The remaining active companions are\s*```text\n230, 282, 385\.\n```",
        "At scan time five were closed and four were active: states `230,282,385,519`. **All four are now closed**: state 519 by endpoint-order/source-availability rigidity and states 230, 282 and 385 by the incidence-capacity family closure.",
        "alt adjacent-family status",
        flags=re.S,
    )

    t = replace_one(
        t,
        r"\*\*Current priority:\*\*[^\n]*",
        "**Current priority:** apply the joint endpoint-class Hall refinement to states 77 and 60, then extract the strongest reusable mixed-class Hall/flow theorem and rescan the remaining frozen N34 catalogue.",
        "alt priority",
    )

    start = "<!-- CANONICAL-WHOLE-STATE-LEDGER:START -->"
    end = "<!-- CANONICAL-WHOLE-STATE-LEDGER:END -->"
    block = (
        f"{start}\n"
        "### Canonical closure ledger\n\n"
        + ledger_table(rs, "")
        + f"\n\nCanonical frontier: **{exclusions:,} exclusions / {survivors:,} survivors**.\n"
        f"{end}"
    )
    anchor = r"## Core selected-excess mechanism"
    if start in t:
        t = replace_or_insert_block(t, start, end, block, anchor, "alt ledger block")
    else:
        t = replace_one(t, anchor, block + "\n\n## Core selected-excess mechanism", "alt ledger insertion")
    p.write_text(t)


def sync_current(rs, count, exclusions, survivors, n34_survivors):
    p = CURRENT
    t = p.read_text()
    state_list = ", ".join(r["state"] for r in rs)
    t = replace_one(
        t,
        r"\*\*Research state reconciled:\*\*[^\n]*",
        f"**Research state reconciled:** 13 September 2026 through the canonical N34 whole-state ledger: **{count} quantified closures** (`{state_list}`), frontier **{exclusions:,}/{survivors:,}**. External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.",
        "current headline",
    )
    t = replace_one(
        t,
        r"The frozen frontier is now\s*```text\n.*?```\s*Breakdown:\s*```text\n.*?```",
        f"The frozen frontier is now\n\n```text\n{exclusions:,} exclusions / {survivors:,} survivors.\n```\n\nBreakdown:\n\n```text\n{n34_survivors:,} N34 equality-derived survivors,\n{N35_SURVIVORS} N35 m=306-derived survivors.\n```",
        "current frontier",
        flags=re.S,
    )
    t = re.sub(r"## General-theory lesson from the [^\n]* closures", f"## General-theory lesson from the {count} closures", t)
    replacements = {
        122: "| 122 | `+1` | none — **whole state closed** |",
        283: "| 283 | `+1` | none — **whole state closed** |",
        154: "| 154 | `+1` | none — **whole state closed** |",
        231: "| 231 | `+1` | none — **whole state closed** |",
    }
    for sid, line in replacements.items():
        t = replace_one(t, rf"\| {sid} \|[^\n]*", line, f"current matrix state {sid}")

    t = replace_one(
        t,
        r"This is a useful compression\.[^\n]*\n\nAfter state 153,[^\n]*\n",
        "This matrix has compressed further: states **122, 283, 154 and 231 are now whole-state closed**. The remaining states from this ring are **77 and 60**, which are the next finite class-packing targets.\n",
        "current matrix interpretation",
    )
    t = replace_one(
        t,
        r"At scan time five were closed and four were active: states `230,282,385,519`\. State 519 is now closed\. The remaining active companions are\s*```text\n230, 282, 385\.\n```",
        "At scan time five were closed and four were active: states `230,282,385,519`. **All four are now closed**; the canonical ledger records their whole-state status.",
        "current adjacent family",
        flags=re.S,
    )
    t = re.sub(
        r"Independent reproduction of the exact computations for states 227, 279, 588, 526, 382, 519 and 153\.",
        "Independent reproduction of the exact computations and hand steps linked from the canonical whole-state ledger.",
        t,
    )

    priority = f"""## Current research priorities

### P1. Attack state 77 with joint class packing

Replay the strengthened mixed demand-two/demand-three Hall projection on its preserved weak layers

```text
E=0,1,3,4,5,6,7.
```

If every layer becomes strict, package state 77 immediately as closure number {count + 1}.

### P2. Attack state 60 next

Its preserved weak layers are

```text
E=0,1,2,3,4,5,6,7.
```

Use the same scanner first; only derive a new inequality if a residual equality or negative gap survives.

### P3. Extract a symbolic mixed-class Hall/flow theorem

Generalise [`ENDPOINT_CLASS_PACKING.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ENDPOINT_CLASS_PACKING.md), especially the joint demand-two/demand-three threshold system that closed state 231. Seek a parameterised theorem rather than accumulating state-specific patches.

### P4. Widen quantified pruning

Apply the strengthened scanner to the remaining {survivors:,} frozen scalar survivors wherever its hypotheses apply, preserving inputs, outputs, hashes and failures.

### P5. Continue independent routes and audit

Maintain external review of the canonical bridge and fixed-order candidates; continue selection-free and maximum-cut routes where they offer genuinely different information. Preserve failed approaches and do not infer proof from timeout or numerical infeasibility alone.

"""
    t = replace_one(
        t,
        r"## Current research priorities\n.*?(?=## Research/preservation rules)",
        priority,
        "current priorities",
        flags=re.S,
    )

    t = replace_one(
        t,
        r"3\. read the alternative-attacks README and the seven whole-state notes \([^\n]*\) plus verification summaries;",
        "3. read the alternative-attacks README, [`WHOLE_STATE_LEDGER.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/WHOLE_STATE_LEDGER.tsv), and the closure records linked from that ledger;",
        "current restart ledger",
    )
    t = replace_one(
        t,
        r"4\. inspect `REFINED_BASELINE3_LEMMA\.md`, `ZERO_EXCESS_ENDPOINT_ORDER\.md`, `REFINED_H2_FAMILY_SCAN\.md`, `make_low_demand_extension_scanner\.py` and the preserved state-153 extension table;",
        "4. inspect `REFINED_BASELINE3_LEMMA.md`, `ZERO_EXCESS_ENDPOINT_ORDER.md`, `ENDPOINT_CLASS_PACKING.md`, `make_class_packing_scanner.py` and the current residual result tables;",
        "current restart tools",
    )
    p.write_text(t)


def main():
    rs = rows()
    states = [int(r["state"]) for r in rs]
    if len(states) != len(set(states)):
        raise SystemExit("duplicate state in ledger")
    count = len(rs)
    exclusions = BASE_EXCLUSIONS + count
    survivors = BASE_SURVIVORS - count
    n34_survivors = survivors - N35_SURVIVORS
    sync_root(rs, count, exclusions, survivors, n34_survivors)
    sync_alt(rs, count, exclusions, survivors, n34_survivors)
    sync_current(rs, count, exclusions, survivors, n34_survivors)
    print("N34_LEDGER_STATUS_SYNC_OK")
    print("closures", count)
    print("frontier", exclusions, survivors)


if __name__ == "__main__":
    main()
