#!/usr/bin/env python3
"""Synchronize public README frontier to the exact analytic-hinge state."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
TOP=ROOT/'README.md'
SUB=Path(__file__).resolve().parent/'README.md'

old_top="""The first cross-order falsification test is also encouraging. Keeping the **same nine staircase generator shapes** and allowing only continuous coefficients/envelopes to refit profile-by-profile on the independently regenerated n=29 `Delta=16` RX-Hall frontiers separates 94/94 `t=3` profiles and 838/902 `t=2` profiles: 932/996 overall (93.5743%). See the [n=29 transfer note](project/research/general_n/2026-09-09-rx-hall-v1/N29_NINE_SHAPE_TRANSFER.md). This is floating-point shape-transfer reconnaissance, not proof evidence; the remaining research frontier is the 64 n=29 `t=2` profiles not covered by the unchanged n=30 dictionary.

The present symbolic target is therefore to explain those 64 transfer survivors with the smallest parameter-dependent correction and then replace the finite `6+3` staircase architecture by parameterised pairwise-majorization potentials with universal label-side lower / source-side upper envelopes strong enough to push below the new `7/12` candidate frontier. No universal staircase theorem is claimed yet.
"""
new_top="""The cross-order work has now moved well beyond the first 932/996 shape-transfer scan. Boundary specialization reduces the unchanged n=30 nine-shape dictionary's `t=2` misses to 38 profiles, and an exact common n=29 potential has been verified across all 996 regenerated `t=2`/`t=3` profiles. More importantly, the `t=3` side has undergone a second analytic compression: with the full BC family available, **SH is unnecessary for all 94 `t=3` profiles**, and the BC potential can be replaced by a nine-feature analytic min-hinge potential

```text
H_{D,V}(d,v) = min((d-D)_+, (v-V)_+).
```

The nine breakpoints are `(0,0),(0,2),(1,7),(1,8),(1,9),(1,10),(1,11),(2,0),(4,0)`. The [analytic min-hinge note](project/research/general_n/2026-09-09-rx-hall-v1/MIN_HINGE_ANALYTIC_REDUCTION.md) records the exact identity expressing each hinge as a chain of nested Hall rectangles. The [exact checkpoint](project/research/general_n/2026-09-09-rx-hall-v1/checkpoints/N29_T3_MIN_HINGE_EXACT_RUN_34384549422.json) checks 30,646 inequalities in integer arithmetic with zero row/bound violations and a worst profile margin nearly twice the required margin. This is exact **finite** evidence conditional on the RX-Hall bridge/frontier preparation, not an unrestricted theorem.

The difficult `t=2` geometry is now sharply localized. Solving the 38 post-specialization profiles individually with all 75 canonical BC staircases and no SH correction succeeds on **37/38**; demand 45 is the unique BC-only obstruction in that experiment. With all 75 BC shapes available, a common potential for the 38-profile core needs only three SH shapes in the zero-gap support-minimization scan, although that support-minimality statement remains MILP evidence rather than an exact impossibility theorem. The active symbolic target is therefore a parameterized BC min-hinge family plus the smallest principled `t=2` correction, with demand 45 used as the primary falsification case.

The exact nine `t=3` breakpoints have the parameter-only specialization
`(0,0),(0,t-1),(t-2,V)` for `V=a-t-2,...,a-1`, `(t-1,0),(t+1,0)` at `(a,t)=(12,3)`. This proposed template is being tested directly on `t=2` before any general claim is made. The aim is to turn the finite Hall/staircase mechanism into a parameterized analytic inequality capable of pushing below the `7/12` maximum-degree frontier.
"""

t=TOP.read_text()
if old_top not in t:
    raise SystemExit('top README stale-frontier block not found; refuse blind patch')
TOP.write_text(t.replace(old_top,new_top,1))

s=SUB.read_text()
anchor='## 7. Highest-priority next steps\n'
if anchor not in s:
    raise SystemExit('RX-Hall README next-steps anchor not found')
prefix=s.split(anchor,1)[0]
new_sub="""## 7. Current analytic frontier

Subsequent work has compressed the finite potential mechanism substantially beyond the original two-rectangle Hall-core experiment.

For the complete regenerated n=29 `t=3` frontier (94 hard profiles), the full canonical BC family needs **no SH correction**. The resulting BC potential was first exactified as a pure staircase surface and then replaced by the analytic min-hinge family

```text
H_{D,V}(d,v)=min((d-D)_+,(v-V)_+).
```

A single exact rational potential using only nine hinges works across all 94 profiles. The exact support is

```text
(0,0), (0,2),
(1,7),(1,8),(1,9),(1,10),(1,11),
(2,0),(4,0).
```

See [`MIN_HINGE_ANALYTIC_REDUCTION.md`](MIN_HINGE_ANALYTIC_REDUCTION.md) and
[`checkpoints/N29_T3_MIN_HINGE_EXACT_RUN_34384549422.json`](checkpoints/N29_T3_MIN_HINGE_EXACT_RUN_34384549422.json).
The latter checks 30,646 inequalities by integer arithmetic, with no row or bound violations.

The hinge has the exact discrete Hall-chain identity

```text
H_{D,V}(d,v)=sum_{k>=1} 1[d>=D+k and v>=V+k],
```

so this analytic form is a weighted chain of nested Hall rectangles rather than an unrelated fitted nonlinearity.

On the difficult n=29 `t=2` post-specialization core, all 75 canonical BC staircases solve 37 of the 38 profiles individually without SH; demand 45 is the unique BC-only obstruction. With all BC shapes available, a common hard38 potential needs only three SH shapes in the current zero-gap support-minimization experiment. Those minimum-support statements are computational/MILP evidence; positive common potentials are exactified separately before being used as proof evidence.

The nine exact `t=3` hinge locations admit the parameter-only description

```text
(0,0),
(0,t-1),
(t-2,V) for V=a-t-2,...,a-1,
(t-1,0),
(t+1,0),
```

specialized at `(a,t)=(12,3)` (with duplicates/nonnegative boundary handling for small `t`). This is now the principal falsification target, not a theorem.

## 8. Highest-priority next steps

1. test the parameterized min-hinge template on the n=29 `t=2` hard38 core with and without the full SH correction dictionary;
2. if it survives, test the same template on all 902 `t=2` profiles and exactify any positive result;
3. isolate and symbolically explain the demand-45 correction rather than increasing the feature dictionary indiscriminately;
4. test the resulting parameter rule on the n=30 `t=1` laboratory and then on new synthetic/fixed-order falsification domains;
5. derive closed source/label envelopes for the min-hinges, exploiting the cancellation in `min(u,v) <= (u+v)/2`;
6. combine the analytic potential with charging/demand bounds to seek a maximum-degree theorem below `7/12`;
7. continue external review of the universal graph-to-demand/RX-Hall bridge, which remains the main mathematical trust boundary.

No complete order above 30, unrestricted solution, novelty determination, full formal verification or external endorsement is claimed here.
"""
SUB.write_text(prefix+new_sub)
print('README_SYNC_OK')
