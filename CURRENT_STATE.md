# Murty–Simon / Erdős #742 — live current state

> Read this file first on resumption. README may lag routine internal WIP. The complete preceding handoff is archived unchanged.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. Individual pool prices: d=4 bound improved; d=5 one-hole minimizer removed but two-hole minimum survives.

WORK MODE: `MATH`. One bounded continuation of the individual-pool task. No catalogue transfer, audit promotion, README edit, workflow launch or polling. The failure of this refinement to improve the d=5 global threshold is preserved, not hidden.

**INSPECTED PREDECESSOR:** `afeb6ac3f573f8525bde05083689c4efabf1a4f5` on main. CURRENT_STATE was read first, then AGENTS and the exact weak-label proof and supplied evidence. Main is re-read before non-forced publication.

**LAST VERIFIED RESULT:** conditional row-priced bound C(d,z) under the FULL canonical bridge, tau>0, |T|=|H|=d>=3. Full residual-profile pools have p_t=z+u_t, sum u_t=L. Exact row equations imply n_t<=h-L+u_t for one-hole labels missing t. Retaining each price (d-1-z-u_t)_+ gives the finite relaxation in the new proof and a(d-1)+d>=b+2tau+zd(2d-3)+C(d,z). The d=5,z=2 target (h,L,n0,n1,n2)=(4,2,1,12,0) costs at least 46, not 30: the missing demand deficit is 16 or 18 over the two pool-distribution types.

**PRESERVED OBSTRUCTION / NEGATIVE RESULT:** C(5,2) is still 30. The other predecessor minimizer (6,0,0,0,15) survives, with p_t=2 and fifteen two-hole labels. An explicit T-K incidence interface (all ten hole pairs plus one five-cycle of repeated pair types) has q_t=6, complete F[T], R_t=8 and beta_t=0. It satisfies the tight row equations but is NOT a full selected/residual system or original graph. Eliminating the first minimizer therefore does NOT justify a stronger d=5 threshold. Extras still require a>=33 in that case.

**ACTUAL IMPROVEMENT:** C(4,2)=19 instead of B(4,2)=17. Under b>=a+2 and tau>=1, extras require a>=30 instead of 29: E=0 through a=29. For d=3..10,z=2 the C values are 8,19,30,35,39,40,45,50. Thresholds for extras are 27,30,33,36,38,41,45,48 respectively. Necessary bounds only; no realizability, sharpness or catalogue claim.

**CHECKS / LIMITS:** executed Python sorted-pool/greedy-price and C++ ordered-pool/dynamic-programming methods agree exactly on minima, every h-slice minimum, feasible counts and all symmetry-reduced minimizing outer keys for 16 (d,z) pairs and 638,396 ordered pool/type tuples. This tuple count is NOT a count of all n_t allocations. Additional checks: all 15 targeted distributions, explicit surviving interface, fresh replay of 1,457 predecessor d=5 scalar tuples, and 533 small binary interface cases. Exact source, results, minima and initial exploration are preserved. Both implementations are by the same assistant; no remote CI success, original-graph enumeration, catalogue replay or independent review is asserted.

**DEPENDENCIES / LIMITS:** inherited full representatives, exact demand level, A-side domination, K-residual and disjoint-destination facts, full profile pools, positive-surplus activity, and maximum-degree identity where used. The new model retains necessary row capacities, NOT the full realization constraints for multi-hole columns. Do not extend one-hole confinement to two-hole labels or extend automatically to tau=0 or d<3. External review and novelty assessment remain OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration remains unresolved. Original equality replay was not rerun. No new state ID, promotion or unrestricted theorem is claimed.

**UNPRESERVED WORK:** `None` after publication and one remote confirmation. Proof, both checkers, exact evidence bundle, exploration, and predecessor archive accompany this handoff.

**DEFERRED ADMIN:** catalogue application and separate audit promotion; Markdown status-parser repair; reviewer/README integration after review; large-input transfer; automatic completion reporting; unrelated CI. Do not retry the failed direct-download route.

**NEXT ACTION:** one bounded mathematical unit on the surviving d=5,z=2 two-hole equality pattern. Its row equations force p_t=2, q_t=6, complete F[T] and beta_t=0. Determine the selecting sources forced by zero remaining demand deficit for each two-hole label, then test destination absence and forward containment against their other selected labels. Do not assume the interface extends to a canonical graph. Preserve the first contradiction or full-routing control before another unit; no further affirmation is needed.

**PROCESS RULE:** STATUS_SYNC_POLICY_V2 / RESEARCH_EXECUTION_POLICY_V3. One bounded unit, coherent preservation, one remote confirmation. No work is claimed to continue after the response ends. Pause/stop overrides continuation.
<!-- CURRENT-STATUS:END -->

## Evidence and predecessor

- [Individual-pool proof and preserved obstruction](project/research/general_n/2026-09-16-individual-pool-rows-v1/PROOF.md).
- [Python replay driver](project/research/general_n/2026-09-16-individual-pool-rows-v1/check_rows.py).
- [C++ allocation checker](project/research/general_n/2026-09-16-individual-pool-rows-v1/verify_rows.cpp).
- [Lossless exact results, minimizers and exploration bundle](project/research/general_n/2026-09-16-individual-pool-rows-v1/EVIDENCE.json.gz.b64); [safe extractor](project/research/general_n/2026-09-16-individual-pool-rows-v1/unpack_evidence.py).
- [Complete unchanged predecessor](archive/status-snapshots/2026-09-16/CURRENT_STATE_before_pool_rows_afeb6ac3.md), copied from blob 01e649ea1bb4a7c659a8090b995dfce510735033.
- [Weak-label profile dependency](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/PROOF.md).

Read AGENTS.md and only the exact mathematical dependencies needed. Older proofs, negative controls and review material remain preserved.
