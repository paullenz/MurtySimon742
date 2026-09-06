# Project reconciliation: complete N=25 candidate route

Date: 6 September 2026. Baseline main commit before this work: `3f84b2471f70fb5a552669ff312c2eba634e8dca`.

**Current finding:** a complete candidate proof now covers the upper bound at 156 edges and the equality characterization K_{12,13}. Every finite domain in this route has been executed and cross-checked. Internal reading found no blocking defect in the deductions. External mathematical scrutiny and formal verification have not occurred; the governed theorem ledger is not promoted by this candidate package.

| Earlier issue | Disposition in this route |
|---|---|
| Reduction from an arbitrary counterexample to exactly 157 edges | Resolved using Fan's published strict bound, which is 157.1125 at order 25. No deletion-preserves-criticality assumption. |
| Δ≤12 | Degree sum gives at most 150 edges. |
| Δ=13 hand proof absent from the early canonical review | Replaced by a fully written witness-count proof. It handles both 157-edge exclusion and 156-edge equality. |
| Δ=14 at 157 edges | The supplied complete dossier was reviewed and both unchanged verifiers reproduced; its full reconstructed evidence is bundled. |
| Parked historical Δ=15 proof chain | Preserved and arithmetic-replayed, but not retroactively certified. A new, shorter proof uses the generalized all-active and low-k lemmas, then only 108 and 211 pair-threshold states for e=157 and e=156. Both implementations agree. |
| Old Δ=16 residual-component dependency | Replaced by direct ledger/all-active contradictions, with a k=0 injection at 156 edges. |
| Δ≥17, including the rounding boundary | Published complement minimum-degree theorem applies at δ(H)≤7; stars and complete bipartite exceptions are handled explicitly. |
| 156-edge equality previously out of scope | Now covered: the Δ=14 equality scan includes the otherwise omitted k=1 boundary, and all 1,959 final labelled columns have independently checked subset-capacity rejection certificates. |
| SAT/DRAT/LRAT and old graph-catalogue completeness | Not dependencies of this route. Historical certification tasks remain historical tasks, not unproved premises smuggled into the new proof. |
| Independent external mathematical review | Still outstanding. Software independence means separate implementations, both by the same assistant; no independent researcher has signed off. |

## Historical Delta=15 archive

The recovered checkpoint is `N25_Delta15_Parked_Checkpoint_2026-09-06_v1.zip`, SHA256 `99b1c5ec7eed0d0bab98c9ea89bea4105ceef0e02d0539020947f61aa035bfd0`. Its verifier confirms 39 manifested files against manifest SHA256 `d34043f0eeeef1e1e7e728ce98e8dc2f5d1869efb27c533117cb1b76a831b13c`. Both preserved v3/v4 arithmetic scripts reproduce their historical stdout hashes exactly. The replay correctly reports `mathematical_proof_verified=false`.

This recovers preserved bytes and arithmetic. It does not establish every old exceptional-state hand argument, resolve an overwritten original-v4-final document's historical provenance, or convert inherited v5 text into that missing original. Those questions remain parked in their existing checkpoint. The new proof's Delta=15 branch does not cite those unresolved arguments.

## Focused external-review request

The reviewable question is whether the deductions in PROOF.md, together with the exact finite verifiers, establish the stated theorem. Reviewers should particularly examine:

1. The partitioned critical-edge witness count and equality deductions in Section 3.
2. The distinctness and residual status of every edge charged in Sections 5 and 6.
3. Applicability of the dimension-independent ledger and inequalities to a=8,9,10, including both edge counts.
4. Sorting, positivity, maximum-degree attainment and the labelled-column coverage in Section 8.
5. The necessary direction of source matching, the simultaneous supplement refinement, and the subset inequality (9.1).
6. Exact assembly of all degree cases and the external theorems' hypotheses, including the odd-order complement-diameter-three point.

The proof text and evidence are prepared for review. They have not been sent to an external reviewer. No novelty, priority, journal acceptance or formal-kernel verification is asserted.
