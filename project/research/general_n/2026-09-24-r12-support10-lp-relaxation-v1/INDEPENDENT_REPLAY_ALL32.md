# Independent replay of all 32 source-feasible r=12 support-ten rows

Observed interval: 2026-09-24T03:22:27+01:00--2026-09-24T03:28:58+01:00.

## Result

The standalone `scipy.optimize.linprog` reconstruction was extended to use explicit stable-index-to-identity mapping and replayed on the complete 32-row source-feasible universe with `method=highs-ipm`, six workers, and a 120-second per-row limit.

- rows attempted: 32
- LP-infeasible (HiGHS status 2): 32
- feasible: 0
- timeout/UNKNOWN: 0
- pattern counts: 3,478--4,017
- helper constraints: 4,296--5,803
- residual-free types: exactly one per row
- residual-free helper discharges: zero for every row

The four rows whose solver message reported `primal_status is None` still had solver status 2 and model status `Infeasible`; they are not recorded as UNKNOWN.

## Interpretation and trust limit

This independently preserved matrix reconstruction reproduces the previously reported classification for all 32 source-feasible rows, including the 13 that had timed out in the fresh integer replay. Thus the latest audit's requested reproducibility gate is met at internal-computation scope and the finite edge bound may again be carried through `S<=14`.

This is not a rational infeasibility certificate, does not provide external mathematical acceptance, and does not upgrade an abstract/profile exclusion into a graph-realizability theorem. The implementation still uses the HiGHS backend through SciPy, although it is a separate continuous-LP encoding from the historical integer-MILP driver. Equality remains controlled only through `S<=8`.

Command:

```text
python3 helper_lp_replay_13.py --indices all --workers 6 --method highs-ipm --time-limit 120
```

Terminal summary: `infeasible=32, unknown=0`.
