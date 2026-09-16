# Murty–Simon / Erdős #742 — live current state

> Read this file first on resumption. The completed publication-recovery checkpoint and all preceding mathematics remain preserved.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. Residual-endpoint demand cap; both near-equality branches closed and d=5 budget strengthened by hand.

WORK MODE: `MATH`. The user requested resuming mathematics after publication repair. One bounded unit: apply the canonical supplement-residual inequality to K-labels, close the two recorded Omega=31 branches, and derive/check the resulting global d=5 bound. No README editing, catalogue transfer, audit promotion, workflow launch or polling.

**INSPECTED PREDECESSOR:** `9e0c4559d45df0bd033a422bdf18fe0b81078e0b` on main, tree `04b673aa5e7fcc437f0de57937782e1ab09342b3`. CURRENT_STATE was read first, then AGENTS, the published two-hole hand proof, and canonical bridge Section 6.2. Publication uses the working connector tree/commit/non-forced-ref route. Main is re-read before publication.

**LAST VERIFIED RESULT:** internal conditional HAND PROOF. In the full tight-block setup |T|=|H|=d>=2, every k in K=N_F(T) minus T has s_k<=d-2. K is residual at all d high sources, so R_k>=d. Any selected K-incidence has BOTH source and destination low (high vertices all contain the label), hence the inherited/rederived supplement bound delta_k<=rho_source+rho_destination gives delta_k<=2d-2. If x_k=0 then s_k=0. The degree bound is conditional on x_k>0; it is not asserted for all unselected K-labels. This combines existing bridge ingredients, not a claim that the endpoint inequality itself is new. The cap does not require positive surplus once the tight-block hypotheses hold.

**D5 HAND CONSEQUENCE:** for tau>0, |T|=|H|=5 and E>0, eta>=kappa=9+h closes (h,L,eta)=(5,0,6) and (6,0,1) immediately. Retaining common/one-hole deficits yields Omega>=27+3h+(7-h)L; also Omega>=9+6h+3L and the predecessor Omega>=36-h+(11-h)L. A three-range hand argument proves Omega>=34 for every h,L, excluding 32 and 33 as well as 31. Thus 4a+5>=b+2tau+104; b>=a+2 gives a>=ceil((101+2tau)/3), so integer tau>=1 requires a>=35 for extras. E=0 through a=34 is rigidity, NOT automatic whole-state exclusion.

**NEW RELAXED EQUALITY PATTERN:** Omega=34 requires h=2,L=0,eta=24,kappa=11: one common K-label, ten one-hole labels (two for each omitted tight label), p_t=2,q_t=2,complete F[T],beta=0. The one-hole labels have demand two and are selected at both sources in their own pool. This parameter pattern attains the new row-relaxation minimum, NOT an original-graph realization. Full destinations and remaining alpha/sigma costs are unresolved. The old C(5,2)=30 model remains correct as a weaker relaxation and is not overwritten.

**CHECKS / LIMITS:** executed Python sorted-pool/greedy-slot and C++ ordered-pool/dynamic-programming methods agree on the complete cost table: 2,940 symmetry-reduced rows representing 29,424 ordered pool/type tuples, including multiplicities. This is not a count of all internal n_t allocations. H-slice minima for h=0..6 are 36,35,34,36,39,42,45; sole minimizing outer key h=2,L=0,n0=1,N=10,n2=0. Other Python checks passed: 299,332 selected-label scalar arrays, 137,256 local incidence masks, 1,626 hand-envelope pairs, 5,832 generalized-cap arrays, six controls. Exact costs are stored in domain-indexed form; the decoder reconstructs inputs without recomputing costs and verifies the full table SHA256. Both implementations are by the same assistant. NOT original-graph enumeration, NOT catalogue replay, NOT inherited-bridge validation or independent acceptance. The main conclusions are hand proofs, not extrapolations from finite tests.

**DEPENDENCIES / LIMITS:** full representatives and unique destinations, A-side domination, demand eligibility, K-residual property, canonical supplement-residual forcing, and the exact full-profile budget. The d=5 E>0 application additionally uses disjoint tight destinations, positive-surplus residual activity and maximum-degree identity. No automatic extension of that global budget to tau=0, other d numerical tables, or catalogue IDs. The new all-d local cap has not yet been applied to those tables. External expert review and novelty assessment remain OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration is unresolved. Original equality replay was not rerun. No new state ID, promotion or unrestricted theorem is claimed.

**UNPRESERVED WORK:** `None` after non-forced publication and one remote confirmation. Full proof, both checkers, exact costs/results and unchanged predecessor archive accompany this handoff. Do not report publication complete before reading back the remote head and handoff.

**DEFERRED ADMIN:** catalogue application and separate audit promotion; Markdown status-parser repair; reviewer/README integration after review; large-input transfer; automatic completion reporting; unrelated CI. PUBLICATION_PROTOCOL.md remains unchanged. Do not retry the failed direct-download route. No remote CI success is asserted.

**NEXT ACTION:** one bounded mathematical unit on the new Omega=34 pattern. Quantify the destination/residual cost of the two saturated one-hole labels in each full pool, retaining alpha, sigma_H and especially sigma_O in the global identity. Derive any forced off-profile receiver costs rather than assuming them. Do not infer realizability of the row equality, or that eliminating it settles all larger-Omega branches. Apply the all-d cap to other d only as a separate subsequent unit. Preserve the first result or counterexample before moving further; no further affirmation is needed.

**PROCESS RULE:** STATUS_SYNC_POLICY_V2 / RESEARCH_EXECUTION_POLICY_V3 unchanged. One bounded mathematical unit, coherent preservation, one remote confirmation. No work continues after the response ends. Pause/stop overrides continuation.
<!-- CURRENT-STATUS:END -->

## Evidence and predecessor

- [Full endpoint-cap and d=5 hand proof](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/PROOF.md).
- [Python checker and replay driver](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/check_cap.py).
- [Differently structured C++ checker](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/verify_cap.cpp).
- [Exact results](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/CHECK_RESULTS.json).
- [Lossless indexed row costs](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/EXACT_ROWS.indexed.json); [decoder](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/unpack_rows.py).
- [Manifest](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/MANIFEST.json).
- [Unchanged publication-recovery predecessor](archive/status-snapshots/2026-09-16/CURRENT_STATE_before_endpoint_cap_9e0c4559.md), copied from blob 8a0ea5ff7220253f27a88d3b7d61a3cb05eab0ca.
- [Preceding two-hole hand proof](project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/PROOF.md).
- [Canonical endpoint dependency](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).

Read AGENTS.md and only the exact mathematical dependencies needed. All prior proofs, weaker models, controls, reviewer materials and publication records remain preserved.
