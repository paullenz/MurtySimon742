# N32, Delta=17, m=257 (t=2): exact candidate closure

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate exact finite closure inside the established graph-to-RX/Hall bridge. Independent mathematical review and novelty assessment remain OPEN.** This is not an unrestricted Murty-Simon theorem.

## Result

For

```text
n=32, Delta=17, a=14, b=17, m=257, t=2,
```

the fourteen-label hand theorem gives `Q<=23` while the bridge gives `Q>=21`.

The committed exhaustive score checker independently verifies all `20,058,300` nondecreasing fourteen-demand multisets and finds exactly

```text
Q=21 : 50
Q=22 : 18
Q=23 :  3
-------------
         71
```

frontier profiles. Every surviving demand is at most five. There is exactly one zero-demand row, `0,3^13`.

The 70 positive-demand rows expand, after every allowed zero/one/two-unit residual-tail slack distribution is included, to exactly **154** `(s,rho)` states.

## Exact nine-rectangle potential

All 154 positive-demand states are excluded by one common graph-level BC potential using only two adjacent threshold layers:

```text
F = 4 B_(2,0)
  + 2 B_(2,6)
  +   B_(2,8)
  +   B_(2,10)
  +   B_(2,13)
  +   B_(2,14)
  +   B_(3,9)
  +   B_(3,11)
  +   B_(3,12).
```

No diagonal/slack correction is required.

With these nine weights pinned exactly at the displayed integers, the common finite envelope exactifies at denominator `100000` with

```text
positive-demand states:        154
contradiction margins:         154
nonnegative margins:             0
zero-RHS row violations:         0
bound violations:                0
repair count:                  269
repair total numerator:        582
worst contradiction numerator: -99891
```

Acceptance is integer arithmetic. Floating point is used only to propose profile-specific envelope coefficients.

The mathematical implication of the potential is the elementary `POTENTIAL_CERTIFICATE_LEMMA.md`: monotone selected-incidence transport, source/supplement threshold transport, exact incidence balances, and summation. The nine rectangles themselves are direct graph-level counting inequalities.

## Zero-demand row

The unique zero-demand frontier `s=(0,3^13)` is excluded by hand. Equality in the tail ledger forces residual degrees `3^9,1^8` and exact `h=2` threshold capacity. The N31 endpoint equality analysis then gives at least 33 supplement indegrees into the nine high sources, while endpoint-load forcing gives at most `9*2=18`, a contradiction. Full details are in `N32_T2_RECTANGLE_POTENTIAL.md`.

## Consequence

Together with the already hand-closed `m>=258` branch, the current candidate framework now gives

```text
n=32 => e(G) <= 256.
```

So the **N32 Turan upper bound is candidate closed**.

The equality classification is not yet finished. The next target is the `m=256` layer, especially `Delta=17,t=1`; the balanced `Delta=16` branch is expected to force `K_{16,16}` by degree/witness rigidity.

## Files

- `N32_T2_RECTANGLE_POTENTIAL.md` — full derivation, exact status and zero-demand hand proof.
- `N32_T2_FRONTIER.csv` — exact 71-profile score frontier.
- `check_n32_t2_frontier.cpp` — independent exhaustive score checker.
- `n32_t2_nine_rectangle_exact.py` — regenerates the 154 states and exactifies/verifies the fixed nine-term potential.
- `../2026-09-11-hand-route-v1/` — hand closure of the `m=258` equality profiles.

## Trust boundary

- Internal exact replay is not independent external validation.
- Correctness remains conditional on the canonical graph-to-selected/residual bridge used throughout the fixed-order programme.
- The positive-demand finite envelope is computer-checked; the global potential has only nine explicit graph-level rectangle terms.
- Independent specialist review remains OPEN.
