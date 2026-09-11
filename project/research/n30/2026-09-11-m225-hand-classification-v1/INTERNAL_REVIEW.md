# Internal review of the hand classification

**Result: no blocking flaw identified in this continuation's written classification and checked arithmetic. This is same-assistant internal review, not independent specialist validation.**

The reviewed scope comprises the whole new hand argument, its cap-four classification table, all 361 printed preimage intervals, the clipping payments, the independent arithmetic methods, the generated profile list, its connection to the existing endpoint checker, and the current reviewer-facing navigation changes.

## Main completeness risks examined

- **Clipping beyond the earlier m226 assumptions.** The older endpoint first proved all demands at least two. Here zeros and ones are allowed. The only exceptional payment involving a low entry is twelve fives with one entry below four: level three sees that entry only if it equals three. The written proof and checker explicitly include all four low values `0,1,2,3`.
- **Threshold-inadmissible vectors.** Some original large demands have no threshold at most sixteen. They are excluded before the finite score argument; they are not silently assigned a finite value or omitted from a valid graph case.
- **Sparse active demand counts.** The cap-four reductions handle `N2=0` separately and prove the padding comparison for every nonempty >=2 part. The bounds `N2<=10 => D<=4` and `N2<=11 => D<=5` justify reducing to the four displayed `(p,N2)` pairs.
- **Omitted cap-four cells.** Every feasible `(y,z)` in those four cases is checked directly, with 365 arithmetic entries. The checker reconstructs the demand vector and its tail sums independently of the compact score formula. A separate text checker confirms that the table printed in the proof equals the verified classification constants.
- **A clipped survivor hiding a larger original demand.** The cap-five lift check includes every Table 1 row with a four, not only those eventually surviving. All 366 positive lifts are partitioned into constant-threshold intervals. All 225 positive six-lifts of the thirty surviving profiles then have score at most sixteen. This establishes the reverse step for six through twelve using the already-proved forward clipping chain.
- **Threshold jumps and endpoints.** Direct first-fit thresholds are cross-checked with a separate inverse-capacity construction. Every point within every printed interval satisfies its displayed affine score, not merely the chosen maximizer. The `g_h(0)=0` discontinuity is explicit in the cap-four argument; all lift parameters start at one.
- **A hidden historical-list premise.** Derivation starts from the written table constants, which are checked over complete reduced domains. The historical file is read only for the optional final comparison. The end-to-end replay uses the newly generated file, whose SHA-256 differs from the historical file because its provenance header is different.

## Observed results

- Exactly 100 distinct profiles: 70 cap-four and 30 cap-five; no profile containing six or more survives.
- Score distribution `64,29,6,1` at scores `18,19,20,21`.
- All 50 printed capacity entries and every printed classification table agree with the audited arithmetic.
- The generated profiles reproduce the 272-row tail reconstruction, all 61 positive-slack ledger exclusions, and the 211 tight rows inside the existing endpoint checker.
- The unchanged four-envelope checker covers all 211 tight rows with the same assignment `195+13+2+1` and minimum exact gap one.
- Publication checks cover the current README, both main reviewer entry points, three predecessor READMEs, and every Markdown file in this checkpoint. Current reviewer versions remain N25/27/28/30 v2 and N29 v4.

The mathematical formulas and arithmetic are reproducible with the standard library; no new full multiset sweep, solver, or floating point is involved. The optional structural probes are separately retained and labelled reconstructed exploration.

## Limits of this review

The universal graph-to-model bridge was treated as an existing dependency, not re-proved from scratch in this turn. The full four-envelope proof and all other N30 degree branches were not re-audited mathematically here; the downstream arithmetic was replayed. The present argument is a hand classification with explicit bounded tables, not a table-free theorem. A complete supplementary assembly review and the separate Delta=17 finite work remain necessary before any replacement N30 reviewer edition. External review remains OPEN, and no theorem-ledger status is promoted.
