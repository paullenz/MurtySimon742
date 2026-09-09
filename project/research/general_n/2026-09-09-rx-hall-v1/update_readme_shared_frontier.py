#!/usr/bin/env python3
"""One-shot README frontier update for the exact shared-nine / n29 transfer checkpoint.

Fails closed unless the expected predecessor paragraph occurs exactly once.
"""
from pathlib import Path

p=Path('README.md')
s=p.read_text()
old="""The present symbolic target is therefore to replace the finite `6+3` staircase prototype by parameterised pairwise-majorization potentials and derive universal label-side lower / source-side upper envelopes strong enough to push below the new `7/12` candidate frontier. No universal staircase theorem is claimed yet.
"""
new="""The finite n=30 obstruction has now been compressed further to a **single common exact 9-shape potential (6 BC + 3 SH) across all seven hard profiles**. A mixed-integer support search over the full generated dictionary of 262 BC + 4 SH shapes proved support cardinality 9 optimal for the stated shared-envelope model with zero MIP gap, and the selected support was then rebuilt and checked in exact integer arithmetic across all 2,775 envelope rows. See the [shared nine-shape note](project/research/general_n/2026-09-09-rx-hall-v1/SHARED_NINE_SHAPE_POTENTIAL.md) and [exact global checkpoint](project/research/general_n/2026-09-09-rx-hall-v1/checkpoints/N30_GLOBAL_NINE_EXACT_RUN_34362935743.json). A different six-BC basis also exactifies, so the compact mechanism is not tied to one brittle BC basis; the same three SH corrections persist.

The first cross-order falsification test is also encouraging. Keeping the **same nine staircase generator shapes** and allowing only continuous coefficients/envelopes to refit profile-by-profile on the independently regenerated n=29 `Delta=16` RX-Hall frontiers separates 94/94 `t=3` profiles and 838/902 `t=2` profiles: 932/996 overall (93.5743%). See the [n=29 transfer note](project/research/general_n/2026-09-09-rx-hall-v1/N29_NINE_SHAPE_TRANSFER.md). This is floating-point shape-transfer reconnaissance, not proof evidence; the remaining research frontier is the 64 n=29 `t=2` profiles not covered by the unchanged n=30 dictionary.

The present symbolic target is therefore to explain those 64 transfer survivors with the smallest parameter-dependent correction and then replace the finite `6+3` staircase architecture by parameterised pairwise-majorization potentials with universal label-side lower / source-side upper envelopes strong enough to push below the new `7/12` candidate frontier. No universal staircase theorem is claimed yet.
"""
if s.count(old)!=1:
    raise SystemExit(f'expected predecessor paragraph exactly once, found {s.count(old)}')
p.write_text(s.replace(old,new))
print('README frontier updated')
