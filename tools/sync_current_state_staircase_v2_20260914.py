#!/usr/bin/env python3
"""Robust wrapper for the staircase CURRENT_STATE rewrite.

Uses the content/rewrite logic from sync_current_state_staircase_20260914.py,
then preserves navigation phrases required by the older canonical status guard.
"""
import sync_current_state_staircase_20260914 as base


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
    "205,919",
    "8:        9",
    "### P1. Attack the aggregate consecutive-band Hall inequalities",
    "34820187136",
    "separate gated promotion only after agreement",
]
missing = [x for x in required if x not in new]
if missing:
    raise SystemExit(f"staircase handoff missing required status: {missing}")

print("CURRENT_STATE_STAIRCASE_V2_20260914_OK")
