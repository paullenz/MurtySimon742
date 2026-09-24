# Preserved second-encoding replay of all 13 former timeout rows

Observed research intervals:

- 2026-09-24T03:07:41+01:00--03:18:16+01:00 (635 seconds): replayed the remaining 12 identities.
- 2026-09-24T03:18:49+01:00--03:21:04+01:00 (135 seconds): corrected positional identity mapping and reran the affected pair.

The committed script independently rebuilds the continuous helper LP as explicit equality and upper-bound matrices and calls `scipy.optimize.linprog(method="highs-ipm")`. It does not import the historical helper solver or the uncommitted implementation behind `HELPER_LP_ALL32_COMPLETE.md`.

All 13 former timeout identities return solver status 2 (LP infeasible), with zero feasible and zero unknown rows:

`362, 363, 437, 438, 451, 455, 1494, 3755, 3758, 4663, 4664, 4665, 4682`.

Every row has one residual-free type and zero residual-free helper discharges. Pattern and helper-constraint counts agree with the durable COMPLETE table.

## Provenance correction

The saved chunk files do not order their last two identities by strict-row index. A first positional mapping therefore labelled the two underlying rows in reverse order. Both identities were already solved, so the mathematical identity set was complete, but the labels were wrong. The committed script now maps strict indices to explicit four-coordinate identities and asserts a bijection. Corrected replays give:

- 4663 = `[48373761,0,7,11]`: 4,017 patterns, 5,803 helper constraints, LP infeasible.
- 4664 = `[48373761,0,7,19]`: 3,999 patterns, 5,774 helper constraints, LP infeasible.

## Trust scope

Continuous-LP infeasibility excludes each corresponding integer helper model. Preserving the second encoding closes the audit's reproducibility gap at the internal-computation level and restores the finite edge bound through `S<=14`. It remains the same HiGHS backend, not a rational Farkas certificate, external verification, graph realizability evidence, or a proof of the full conjecture. Equality remains established only through `S<=8`.
