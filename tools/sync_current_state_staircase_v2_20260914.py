#!/usr/bin/env python3
"""Robust wrapper for the staircase CURRENT_STATE rewrite.

Uses the content/rewrite logic from sync_current_state_staircase_20260914.py,
then preserves canonical navigation phrases and appends the latest band-reach
and state-226 diagnostic reconnaissance without touching ledger-derived
headline counts.
"""
import sync_current_state_staircase_20260914 as base

OLD_BAND_REACH = r'''
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

BAND_REACH = r'''
### Near-exact band reach and resolved state-226 diagnostic

[`STAIRCASE_BAND_REACH_PILOT.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STAIRCASE_BAND_REACH_PILOT.md) measures how much exact target-Hall power survives the verified band relaxation on the same deterministic 15-state Murty pilot. GitHub Actions run `34832806900` completed green.

Across `205,919` exact target-Hall-failing profiles, the coarse band relaxation was also infeasible on **205,918** and passed only **one** profile:

```text
band retention of exact target-Hall failures:
205,918 / 205,919 = 99.999514%.
```

The sole false-negative is a two-generator profile in N34 state `226`. The dedicated diagnostic run `34838612503` completed green and its exact block is frozen in [`STATE_226_BAND_EXCEPTION_DIAGNOSTIC.txt`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STATE_226_BAND_EXCEPTION_DIAGNOSTIC.txt), with provenance in [`STATE_226_BAND_EXCEPTION_DIAGNOSTIC_PROVENANCE.json`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STATE_226_BAND_EXCEPTION_DIAGNOSTIC_PROVENANCE.json) and interpretation in [`STATE_226_BAND_EXCEPTION.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STATE_226_BAND_EXCEPTION.md).

The exception occurs at `E=6`, `Q=47`: exact quotient flow is `46` (deficit `1`), while the coarse band flow is exactly saturated at `39/39`. The entire capacity error occurs at target type `(q,c,P,n)=(2,4,4,1)`: exact selected-source incoming capacity is `2`, but the coarse band model supplies `7`, an overestimate of `5`. Those five spurious incidences are exactly the five copies of selected non-generator type `(q,c,rho,P,n)=(6,9,3,3,5)`, grouped under easier band generator `(5,9,4,4,1)`. The generator reaches the target because `5<=4+1`; the five non-generator copies do not because `6>4+1`.

This identifies a stronger theorem-safe **compatible-copy band refinement**: for each band/target edge count only selected source copies in that band which are individually compatible with that target, rather than all copies whenever the generator is compatible. On state `226`, this reduces total effective target receiving capacity to `38` against band demand `39`, so it rejects the unique coarse-band exception. Since refinement only removes capacity, all earlier `205,918` coarse-band failures remain failures. Therefore, as a **derived frozen-pilot conclusion**, the compatible-copy refinement detects `205,919/205,919` exact target-Hall failures in the same 15-state pilot. This refinement still needs its own formal theorem note and independent CI verifier before being elevated beyond derived reconnaissance.

The interval-neighborhood structure does **not** imply that it is enough to check contiguous source-band cuts. [`BAND_INTERVAL_CUT_COUNTEREXAMPLE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/BAND_INTERVAL_CUT_COUNTEREXAMPLE.md) preserves a three-band example where every contiguous band interval has nonnegative Hall margin but the disconnected cut `{1,3}` has margin `-1`. Therefore the promising object is the complete compatible-copy band flow or a stronger Murty-specific reduction, not an unsupported interval-cut shortcut.
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
    if OLD_BAND_REACH.strip() in text:
        text = text.replace(OLD_BAND_REACH.strip(), BAND_REACH.strip(), 1)
    elif BAND_REACH.strip() not in text:
        if text.count(anchor) != 1:
            raise SystemExit("band-reach insertion anchor missing or duplicated")
        text = text.replace(anchor, "\n" + BAND_REACH.strip() + "\n" + anchor, 1)
    text = text.replace(
        "Seek aggregate interval/band inequalities or a restricted parametric family of violating band cuts. Use the unique state-226 band false-negative to identify which within-band statistic must be restored before attempting any stronger exact reduction.",
        "Formalize the compatible-copy staircase-band lemma identified by the completed state-226 diagnostic, give it an independent verifier, and replay it on the frozen pilot. Then seek aggregate inequalities for the resulting exact-compatible band capacities rather than returning to generator-only or contiguous-cut shortcuts.",
        1,
    )
    text = text.replace(
        "The Murty-specific antichain pilot shows that high generator counts are real inside the scanned relaxation, while the band-reach pilot retains 205,918/205,919 exact target-Hall failures. The active theory target is therefore **aggregate staircase-band demand/capacity plus the single missing within-band distinction**, not a small-generator or contiguous-cut shortcut.",
        "The Murty-specific antichain pilot shows that high generator counts are real inside the scanned relaxation. The completed state-226 diagnostic identifies the single coarse-band loss as invented within-band compatibility, and the compatible-copy refinement therefore detects 205,919/205,919 exact target-Hall failures on the frozen pilot by monotonicity plus the exact exception calculation. The active theory target is now **compatible-copy staircase-band demand/capacity**, pending its own independent theorem/CI replay, not a small-generator or contiguous-cut shortcut.",
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
    "34838612503",
    "205,918",
    "205,919/205,919",
    "99.999514%",
    "STATE_226_BAND_EXCEPTION.md",
    "STATE_226_BAND_EXCEPTION_DIAGNOSTIC.txt",
    "BAND_INTERVAL_CUT_COUNTEREXAMPLE.md",
    "state `226`",
    "compatible-copy",
    "### P1. Attack the aggregate consecutive-band Hall inequalities",
    "34820187136",
    "separate gated promotion only after agreement",
]
missing = [x for x in required if x not in new]
if missing:
    raise SystemExit(f"staircase handoff missing required status: {missing}")

print("CURRENT_STATE_STAIRCASE_V2_20260914_OK")
