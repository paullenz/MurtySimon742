#!/usr/bin/env python3
"""Robust wrapper for the staircase CURRENT_STATE rewrite.

Uses the content/rewrite logic from sync_current_state_staircase_20260914.py
but avoids brittle punctuation-sensitive status checks.
"""
import sync_current_state_staircase_20260914 as base

old = base.PATH.read_text()
new = base.rewrite(old)
base.PATH.write_text(new)
if base.rewrite(new) != new:
    raise SystemExit("staircase CURRENT_STATE rewrite is not idempotent")

required = [
    "977 quantified closures, 1,971 exclusions / 3,607 survivors",
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
