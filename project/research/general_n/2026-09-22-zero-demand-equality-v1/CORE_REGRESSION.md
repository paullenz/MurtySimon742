# Positive residual-core replay and remaining diamond kernels

22 September 2026. Internal bounded computation; no external verification.

PASS on the unchanged 1,396-fixture / 2,783-root / 68,741-selection suite: 68,741 positive-core ledger identities; 1,982 cases with one to three residual labels; 186 cases with r=5, none saturating f=r; and all 68,741 assignments satisfying the S<=7 bound. The suite's largest observed demand is S=5, so S=6,7 are NOT directly exercised. Sampling and isomorphism caveats remain those in EQUALITY_REGRESSION.md. Source SHA256: 84c6cf91fe751f88ca6aa56374197b83b6490db47f3740a561bc0d53c6b6dfd7. Exact output: CORE_RESULTS.json.

## Necessary source-pattern kernel

core_source_kernel.py enumerates physical-source column states on the two diamond cores at r=5, R=(2,1,1,1). State 0 means adjacent/unselected at that column, 1 selected missing crosspair, 2 residual missing crosspair. Selected i forces every F-neighbor into missing state; the number of selected F-neighbors is at most R_i. Residual column sums are exact and selected column sums meet d_i-R_i. It enumerates unordered source-state multisets; active sources each consume residual mass. Residual-free sources cannot meet any selected incidence in either connected diamond: such a source's selected labels would be a neighborhood-closed set, hence all four labels, violating a unit label's selected-neighbor limit. All-zero sources are irrelevant and omitted.

For the diamond whose heavy residual vertex has degree two: 27 allowed single-source patterns, zero surviving multisets.
For heavy degree three: 28 patterns and exactly one surviving multiset:
(1,2,1,1), (2,1,1,2), (2,1,2,1).

The survivor is NOT an actual graph: supplement endpoints, B-edges, unique common-neighbor conditions and edge criticality have not been imposed. It is a concrete next target, not evidence of realizability. The other r=5 equality shapes (triangle plus heavy vertex with zero/one triangle neighbors and remaining T-neighbors) are not enumerated by this four-label diamond script.

No equality theorem beyond the proved scope is asserted. Next: test whether the surviving diamond source multiset can admit legal distinct supplements, and separately treat the T-neighbor shapes.
