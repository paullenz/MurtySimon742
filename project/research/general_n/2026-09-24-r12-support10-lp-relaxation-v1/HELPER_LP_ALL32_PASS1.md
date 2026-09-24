# r=12 support-ten helper stage: independent continuous-LP pass

Observed solver interval: 2026-09-24T01:21:32+01:00 to 2026-09-24T01:24:54+01:00.

I independently rebuilt the helper-aware source/supplement system on the independently regenerated 32 source survivors, but relaxed both the source multiplicities and activation variables to continuous variables. This is a strict relaxation of the integer helper MILP: LP infeasibility therefore certifies integer infeasibility for a row.

A first pass using SciPy/HiGHS with a 30-second per-row limit gave:

- **19 LP-infeasible**
- **0 LP-feasible**
- **13 time-limit/unknown**

The unknown row indices are:

`362, 363, 437, 438, 451, 455, 1494, 3755, 3758, 4663, 4664, 4665, 4682`

The first row, index 355 / identity `[5179456,0,11,19]`, was independently LP-infeasible, agreeing with the earlier single-row checkpoint. The pass used the same helper semantics as the committed model but a fresh implementation and continuous relaxation; it did not reuse the saved helper result table.

This materially narrows the 24-September red-team failure: the fresh integer rerun had 32/32 unknown/timeouts, whereas an independently encoded **LP relaxation** already excludes 19/32 without branch-and-bound. The remaining 13 are unresolved, not survivors. A `highs-ipm` pass with a longer limit is now being run on exactly those 13.

This is internal computer-assisted evidence only. It does not establish graph realizability, external acceptance, or `S<=14`; that row remains frozen until all load-bearing helper rows are decisively reproduced/certified under the repository trust rules.
