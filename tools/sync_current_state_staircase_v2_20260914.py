#!/usr/bin/env python3
"""Robust wrapper for the staircase CURRENT_STATE rewrite.

Uses the content/rewrite logic from sync_current_state_staircase_20260914.py,
then preserves canonical navigation phrases and appends the latest band-reach
reconnaissance without touching ledger-derived headline counts.
"""
import sync_current_state_staircase_20260914 as base

BAND_REACH = r'''
### Near-exact band reach and the remaining exception

[`STAIRCASE_BAND_REACH_PILOT.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STAIRCASE_BAND_REACH_PILOT.md) measures how much exact target-Hall power survives the verified band relaxation on the same deterministic 15-state Murty pilot. GitHub Actions run `34832806900` completed green.

Across `205,919` exact target-Hall-failing profiles, the band relaxation was also infeasible on **205,918** and passed only **one** profile:

```text
band retention of exact target-Hall failures:
205,918 / 205,919 = 99.999514%.
```

The sole false-negative is a two-generator profile in N34 state `226`. A dedicated diagnostic workflow is isolating its exact `(E,rho,q)` profile, canonical type-level minimum cut and feasible band flow so that the missing within-band statistic can be identified. This is reconnaissance only and changes no canonical closure count.

The interval-neighborhood structure does **not** imply that it is enough to check contiguous source-band cuts. [`BAND_INTERVAL_CUT_COUNTEREXAMPLE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/BAND_INTERVAL_CUT_COUNTEREXAMPLE.md) preserves a three-band example where every contiguous band interval has nonnegative Hall margin but the disconnected cut `{1,3}` has margin `-1`. Therefore the promising object is the complete band flow or a stronger Murty-specific reduction, not an unsupported interval-cut shortcut.
'''


def postprocess(text):
    text = text.replace(
        "**Exact type-level max-flow and submodularity:**",
        "**Exact type-level max-flow theorem and submodularity:**",
        1,
    )
    text = text.replace(
        "- **Sharp dominance:**\n",
        "- **Sharp dominance:** [`SHARP_DOMINANCE_UPSET_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SHARP_DOMINANCE_UPSET_HALL.md)\n",
        1,
    )
    anchor = "\n### Full frontier relational scan\n"
    if BAND_REACH.strip() not in text:
        if text.count(anchor) != 1:
            raise SystemExit("band-reach insertion anchor missing or duplicated")
        text = text.replace(anchor, "\n" + BAND_REACH.strip() + "\n" + anchor, 1)
    text = text.replace(
        "Seek aggregate interval/band inequalities or a restricted parametric family of violating band intervals.",
        "Seek aggregate interval/band inequalities or a restricted parametric family of violating band cuts. Use the unique state-226 band false-negative to identify which within-band statistic must be restored before attempting any stronger exact reduction.",
        1,
    )
    text = text.replace(
        "The Murty-specific antichain pilot shows that high generator counts are real inside the scanned relaxation, so the active theory target is **aggregate staircase-band demand/capacity**, not a small-generator shortcut.",
        "The Murty-specific antichain pilot shows that high generator counts are real inside the scanned relaxation, while the band-reach pilot retains 205,918/205,919 exact target-Hall failures. The active theory target is therefore **aggregate staircase-band demand/capacity plus the single missing within-band distinction**, not a small-generator or contiguous-cut shortcut.",
        1,
    )
    return text


old = base.PATH.read_text()
new = postprocess(base.rewrite(old))
base.PATH.write_text(new)
if postprocess(base.rewrite(new)) != new:
    raise SystemExit("staircase CURRENT_STATE rewrite is not idempotent")

required = [
    "977 quantified closures, 1,971 exclusions / 3,607 survivors",
    "Exact type-level max-flow theorem",
    "SHARP_DOMINANCE_UPSET_HALL.md",
    "34831605792",
    "34832155910",
    "34831697002",
    "34832806900",
    "205,918",
    "99.999514%",
    "BAND_INTERVAL_CUT_COUNTEREXAMPLE.md",
    "state `226`",
    "### P1. Attack the aggregate consecutive-band Hall inequalities",
    "34820187136",
    "separate gated promotion only after agreement",
]
missing = [x for x in required if x not in new]
if missing:
    raise SystemExit(f"staircase handoff missing required status: {missing}")

print("CURRENT_STATE_STAIRCASE_V2_20260914_OK")
