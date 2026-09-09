# RX-Hall numerical status-4 diagnosis

9 September 2026. Internal diagnosis by ChatGPT/Geeps at Paul Lenz's direction.

**Scope:** GitHub Actions run `34295699108`, commit `3fb0a25ba7bb9fe1532d3127982f4d3de370e4d9`.

**Disposition:** the red workflow did not reveal a numerically feasible RX-Hall state. It revealed six conservative `status=4` solver outcomes. The first-pass default HiGHS route classified 990 of the 996 hard positive-demand zero-slack rows as infeasible and 6 as `model_status=Unknown; primal_status=Infeasible`; it classified **zero** rows as feasible. Re-solving exactly those six unchanged LPs with the distinct HiGHS interior-point route (`method='highs-ipm'`) returns SciPy status 2, infeasible, in all six cases.

This is still floating-point reconnaissance. None of these numerical infeasibility verdicts is accepted as proof evidence; exact certificates remain required.

## 1. Why the workflow was red

The original scanner deliberately treats any result other than public SciPy status 2 (infeasible) or `success=True` as unresolved. This is correct conservative behaviour. SciPy 1.17.0 / HiGHS returned public status 4 for six states with the message

```text
The HiGHS status code was not recognized.
(HiGHS Status 15: model_status is Unknown; primal_status is Infeasible)
```

The workflow assertion `numerical_other == 0` therefore failed. Because the upload step was success-gated, the JSON reports from the red shards were not retained as artifacts; the job logs nevertheless contain the complete unresolved state records.

## 2. Complete red-state list

All six were independently reconstructed with the same SciPy 1.17.0 package and unchanged RX-Hall LP builder.

| t | shard | demand id | hard position | s | rho | default HiGHS | HiGHS-IPM retry |
|---:|---:|---:|---:|---|---|---|---|
| 3 | 0/1 | 31 | 14 | `[2,4,4,4,5,5,5,5,5,5,5,5]` | `[1,1,1,1,1,1,1,2,4,5,5,5,5,5,5,5]` | status 4 | status 2, infeasible |
| 2 | 1/12 | 343 | 649 | `[3,3,4,4,4,5,5,5,5,5,5,5]` | `[1,1,1,1,1,1,1,2,4,5,5,5,5,5,5,6]` | status 4 | status 2, infeasible |
| 2 | 6/12 | 319 | 498 | `[3,3,3,3,4,4,4,4,4,4,4,4]` | `[1,1,1,1,1,1,1,3,3,3,3,4,4,4,4,5]` | status 4 | status 2, infeasible |
| 2 | 7/12 | 350 | 691 | `[3,4,4,4,4,4,4,4,5,5,5,5]` | `[1,1,1,1,1,1,1,1,4,4,5,5,5,5,5,6]` | status 4 | status 2, infeasible |
| 2 | 8/12 | 234 | 164 | `[2,2,4,4,4,5,5,5,5,5,5,5]` | `[1,1,1,1,1,1,1,1,4,4,5,5,5,5,5,6]` | status 4 | status 2, infeasible |
| 2 | 11/12 | 178 | 107 | `[2,2,2,3,3,3,3,4,4,4,4,4]` | `[1,1,1,1,1,1,1,1,2,2,3,3,4,4,4,4]` | status 4 | status 2, infeasible |

For each of these states `highs-ds` reproduces the status-4/unknown outcome while `highs-ipm` returns the normal infeasible status. This pattern is consistent with a numerical/algorithm-status issue in the simplex/default route, not with an exhibited feasible point.

## 3. Hardened replay policy

`rx_hall_scan_hardened.py` now implements the following policy:

1. run the unchanged original scanner model through its original `method='highs'` solve;
2. if and only if that returns status 4, rebuild the same sparse matrices from the same model object;
3. retry with `method='highs-ipm'`;
4. classify from the retry's public SciPy status;
5. leave every other original result unchanged.

The CI workflow is also changed so each shard report is uploaded with `if: always()`, and the aggregate job runs with `if: always()`. Future unresolved solver states therefore remain inspectable instead of disappearing when an assertion deliberately fails.

## 4. Trust boundary

This repair does **not** strengthen the RX-Hall mathematical relaxation and does not affect the n=29 or n=30 complete-candidate proofs, which do not depend on this later reconnaissance. The RX-Hall route remains a general-N research direction only.

The next proof-relevant step is unchanged: generate exact integer/rational Farkas certificates for the stripped RX-Hall system and inspect those duals for a symbolic Hall/threshold inequality.
