# Actual-graph regression of the raw selected/profile bridge

22 September 2026. Status: **PASS — FINITE_INTERNAL_REGRESSION**.

This checker was written independently for the reconstructed profile bridge. It uses only the Python standard library. The earlier graph checker supplied the explicit cube-face X_k construction, not the validation algorithms or profile code.

## Inputs and independently checked coverage

- Enumerated all 33,864 labelled simple graphs on 3 through 6 vertices and retained only D2C graphs.
- Added balanced complete bipartite controls of both parities through order 20, stars, X_3/X_4/X_5, and deterministic greedy D2C constructions for orders 7 through 16 with 12 seeds per order.
- The deduplicated suite contains 757 graphs, distributed as {"exhaustive_labelled_small_graphs":608,"bipartite_and_star_controls":28,"cube_face_controls":3,"seeded_greedy_graphs":118}.
- Every retained graph passed a common-neighbour D2C test and a separately implemented BFS check of diameter two and every edge deletion: 8,374 deletion checks.
- All 1,256 maximum-degree roots were tested. All legal quasi-edge selections were exhausted at EVERY root: 2,722 assignments; the largest choice space was 216. No sampling limit was reached in this run.
- Complement total-domination candidates and the equivalent unique-common-neighbour candidates agreed for every B-pair.

## Bridge checks

All exact ledger identities, label-degree lower bounds, source-demand injections, distinct supplements, signature-union inclusions, heavy-source/supplement membership, unordered-pair capacity bounds, maximum-demand source counts and nested residual budgets passed.

The pointwise and summed profile radical inequalities were certified using integer square-root upper bounds at scale 10^40. They do not use floating-point tolerances.

| Coverage | Count |
|---|---:|
| Legal selections | 2722 |
| Positive-demand selections | 153 |
| Zero-demand selections | 2569 |
| Selected injection checks | 8326 |
| Nonempty injection checks | 7030 |
| Signature-union checks | 12298 |
| Threshold checks | 158 |
| Threshold checks with high-load sources | 2 |
| Residual supplement cases | 3 |
| Selected-edge supplement cases | 1 |
| Roots with choice-dependent demand profile | 30 |
| Zero-a star controls | 34 |
| Positive-surplus selections | 0 |

The positive-demand and two supplement-branch counts matter: these checks exercise nonempty parts of the proof rather than validating only vacuous zero-demand examples. Choice-dependent profiles occur, so the universal quantifier over legal selections is also exercised.

## Controls and limitations

X_3 is independently confirmed to be D2C with n=12 and m=32, exceeding floor((n-1)^2/4)+1=31. It remains a mandatory counterexample to the abandoned all-order second-extremal claim, not to Murty–Simon. The balanced bipartite controls attain floor(n^2/4), and stars exercise the repaired a=0 domain.

No positive-surplus graph was found. Positive demand is not positive surplus. Only two high-load threshold instances occur in this suite, so the most delicate branch has concrete but narrow finite coverage. The next step is to extract its complete graph/selection witness and audit that witness directly.

This is not exhaustive over all orders, all unlabelled graphs, or all D2C graphs above order 6. It does not establish external verification or complete the independent #742 strip proof.

## Reproduction

```sh
python check_raw_profile.py --max-exhaustive-n 6 --random-seeds 12 --max-random-n 16 --output RESULTS.json
```

The source SHA-256 is `138ef5194f134e1902685692285af1f816a18792dbd337439634bfdc3dfbf2d4`. Full graph/root/selection-space metadata, concrete positive-demand examples and exact counters are in `RESULTS.json`.
