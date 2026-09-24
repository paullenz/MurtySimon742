# Independent helper-LP replay: former-timeout row 362

Observed research interval: 2026-09-24T03:05:49+01:00--2026-09-24T03:06:46+01:00 (57 seconds).

A standalone replay script was committed with this result. It reconstructs the continuous helper LP directly as equality and upper-bound matrices and calls `scipy.optimize.linprog(method="highs-ipm")`, rather than importing the historical integer-MILP solver or relying on the uncommitted implementation behind `HELPER_LP_ALL32_COMPLETE.md`.

Command:

`python3 helper_lp_replay_13.py --indices 362 --method highs-ipm --time-limit 120`

Result for strict-row index 362 / identity `[5179456,0,11,81]`:

- patterns: 3,589
- residual-free types: 1
- residual-free helper discharges: 0
- helper constraints: 4,624
- solver status: 2, infeasible
- unknown: 0

The structural counts agree with the earlier report. Continuous-LP infeasibility excludes the corresponding integer helper model. This closes row 362 at the preserved-code internal-replay level, but it is still the same HiGHS backend and is not an exact rational certificate or external mathematical acceptance. The other 12 former-timeout rows remain to be replayed; `S<=14` remains frozen.
