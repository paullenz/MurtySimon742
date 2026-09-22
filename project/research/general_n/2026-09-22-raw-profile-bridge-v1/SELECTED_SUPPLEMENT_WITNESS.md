# A physical witness for the selected-supplement branch

22 September 2026. **EXACT_FINITE_WITNESS / INTERNAL_CHECKED**.

The regression found an actual D2C graph where the tempting shortcut "all other heavy-label edges at a supplement are residual" is false. The repaired residual-or-selected proof remains valid.

The graph has vertices 0,...,13, n=14, m=31 and unique maximum-degree root v=4 of degree b=7. Its full edge list is:

```json
[[0,1],[0,2],[0,5],[0,7],[1,4],[1,7],[1,9],[2,3],[2,6],[2,10],[2,12],[2,13],[3,4],[3,5],[3,11],[4,8],[4,9],[4,10],[4,11],[4,13],[5,6],[5,9],[5,12],[6,7],[6,8],[7,8],[7,11],[7,12],[8,10],[9,10],[12,13]]
```

Direct breadth-first searches verify diameter exactly two and verify that deleting any one of its 31 edges destroys diameter at most two.

The root partition is A={0,2,5,6,7,12}, B={1,3,8,9,10,11,13}. The graph F=G[A] is K_{3,3}, with parts {0,6,12} and {2,5,7}. Select the four quasi-edges (source,label,supplement):

```text
(9,7,1), (11,2,3), (10,7,8), (9,2,10).
```

The full selection space at this root has six assignments, all checked by the regression. They produce three different demand profiles, so choice dependence is real.

For the displayed assignment:

| label i | 0 | 2 | 5 | 6 | 7 | 12 |
|---|---:|---:|---:|---:|---:|---:|
| d_i | 3 | 3 | 3 | 3 | 3 | 3 |
| R_i | 6 | 2 | 5 | 6 | 2 | 6 |
| s_i | 0 | 1 | 0 | 0 | 1 | 0 |

Thus at h=1 the heavy labels are I_1={2,7}. Source 9 selects both, so it is a high-load source with ell_9=2>1.

Consider selection (9,2,10). Its supplement is 10, and the other heavy label is 7. The H-edge (10,7) exists, but it is SELECTED, namely (10,7,8). It is not residual. There are therefore zero residual edges among this one "other heavy-label" edge, despite h=1.

The correct argument invokes the already proved source-demand injection at selected edge (10,7): rho_10>=s_7=1. In the actual graph rho_10=4, so 10 belongs to Z_1. The other selection from source 9, (9,7,1), exercises the residual case: (1,2) is residual.

All seven sources belong to Z_1, W_1=2, r=27, e(F)=9 and t=-18. The exact capacity inequality has substantial slack:

2W_1=4 <= z_1^2-z_1+1(1+1)=44.

This example validates the need for the proof's two-case mechanism. It is not a positive-surplus graph, a near-extremal construction, or a counterexample to the corrected bridge. No claim of smallest possible order is made.

The complete selected and residual edges, degrees and all four high-load events from the regression are in `SUPPLEMENT_WITNESSES.json`. Reproduce the extraction using:

```sh
python extract_supplement_witness.py
```
