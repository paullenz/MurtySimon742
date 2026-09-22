# Low-residual hostile graph replay
22 September 2026. Exact finite internal regression; no external review.

The same 1,396 fixtures and 68,741 assignments as EQUALITY_REGRESSION.md passed:
- 1,288,964 F-edge checks of R_i+R_j>=2.
- 88 non-vacuous zero-residual-endpoint checks.
- 30 one-residual-label occurrences, six with nonempty F.
- 82 r<=2 checks.
- 68,556 demand-at-most-two bound checks and 863 equality checks.
- 39,846 independent breadth-first edge-deletion checks.

All-assignment coverage holds at 2,727 maximum roots; 56 roots are sampled. These are fixture and assignment counts, not isomorphism counts.

The complete machine output preserves an actual zero-residual endpoint witness, a nonempty single-column residual witness, and a sharp r=2,f=1 witness (C5). Thus the local assertions are not checked only on empty graphs. No non-bipartite graph at the target density was present; the counterexample-exclusion corollary is not directly exercised at that impossible-or-open boundary.

Command: `python check_low_residual.py`.
Source SHA256: c24485fbdea05482e1b8348e31fb067ede561664f40c90265d9f4b63b4dd3b26.
Dependency checker SHA256: 565b392d707d87c1effd0e0db066caeb8ca8721156fb31f2683e4ff1d2af18f4.
Measured execution: 52.69677127999603 seconds.

The host proof audit separately enumerated all possible new distance-three pairs after deleting a centre-leaf F-edge. Both endpoints and all leaf pairs retain a common neighbour outside the residual source set, forcing the private witnesses used in the proof. Repeated codes are never identified as vertices. No counterexample or missing hypothesis was found in this replay; universal conclusions still depend on the written proof, not the finite test.
