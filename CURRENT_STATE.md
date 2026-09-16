# Murty–Simon / Erdős #742 — live current state

> Read this file first on resumption. README may lag routine internal WIP. The complete preceding handoff is archived unchanged.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. The saturated d=5 two-hole minimum has no valid destinations; conditional hand bound strengthened.

WORK MODE: `MATH`. One bounded continuation of the live two-hole routing task. No catalogue transfer, audit promotion, README editing, workflow launch or polling. The previous interface-only control is preserved as such, not treated as a full graph.

**INSPECTED PREDECESSOR:** `002713dc090035ec4f01d8eaaf9d27023082bc4d` on main. CURRENT_STATE was read first, then AGENTS and the exact individual-pool/full-profile proofs and supplied evidence. Main is re-read before non-forced publication.

**LAST VERIFIED RESULT:** internal conditional HAND PROOF under the FULL canonical bridge, tau>0, |T|=|H|=5, and extra selections E>0 (so full pools p_t>=2). Set p_t=2+u_t, L=sum u_t, h=kappa-9 and Omega=5h+3L+eta. The new algebraic bound Omega>=36-h+(11-h)L proves Omega>=30 without relying on a minimizer table; Omega=30 forces h=6,L=0,eta=0. Then all 15 K-labels have exactly two holes, q_t=6, complete F[T], beta_t=0 and demand four. Each is selected at all four vertices in the two pools indexed by its holes. Each pool source selects six K-labels. Two of these have the same hole pair, hence identical presence at all profile destinations. A destination for either twin cannot be high (label present), a profile vertex (the other twin must be present while this one is absent), or outside the profiles (five required K-labels exceed four residual slots). Thus Omega=30 is impossible, and integrality gives Omega>=31.

**NUMERICAL CONSEQUENCE / LIMIT:** 4a+5>=b+2tau+101, hence a>=ceil((98+2tau)/3) using b>=a+2. For integer tau>=1, d=5 extras require a>=34, compared with 33 previously: E=0 through a=33. This is rigidity, NOT automatic whole-state exclusion. C(5,2)=30 remains correct for the old row relaxation; the new result uses additional routing conditions. Other d bounds are unchanged. No sharpness or realizability claim.

**CHECKS / LIMITS:** executed Python remaining-degree and C++ six-free-multiplicity enumerators agree on the complete reduced destination decisions for all 654 degree-six two-hole interfaces on five distinguished tight labels. At least 56 of 60 mandatory selected incidences fail in each interface (90 have 56 failures, 564 have 60). Total 38,880/39,240 failures; zero interfaces pass all mandatory destinations. The displayed predecessor interface fails all 60. A separate Python greedy / C++ dynamic-programming replay agrees on 29,424 ordered pool/type tuples, all h-slice minima and the sole old minimizing outer key. Additional 990 local profile masks and 83,740 twin-predicate cases passed; four negative controls are preserved. Exact sources, full decision lists and outputs accompany the proof. Both implementations are by the same assistant. NOT original-graph enumeration, NOT catalogue replay, NOT inherited-bridge validation or independent expert acceptance. The main bound and equality contradiction are hand proofs, not finite-check extrapolations.

**DEPENDENCIES / LIMITS:** full representatives, exact demand level T, eligibility, A-side domination, inherited K-residual/disjoint-destination facts, full profile pools, and positive-surplus residual activity for the global b-dependent budget. Only destination absence and forward containment are needed by the NEW routing contradiction; no new reverse-containment step. beta=0 and demand four are proved in the equality case, not exported to near-equality cases. Do not extend automatically to tau=0 or other d. Independent expert review and novelty assessment remain OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration remains unresolved. Original equality replay was not rerun. No new state ID, promotion or unrestricted theorem is claimed.

**UNPRESERVED WORK:** `None` after publication and one remote confirmation. Full proof, both checkers, exact results/decisions and the unchanged predecessor archive accompany this handoff.

**DEFERRED ADMIN:** catalogue application and separate audit promotion; Markdown status-parser repair; reviewer/README integration after review; large-input transfer; automatic completion reporting; unrelated CI. Do not retry the failed direct-download route. No remote CI success is asserted.

**NEXT ACTION:** one bounded mathematical unit on Omega=31. The new hand inequality restricts it to (h,L,eta)=(5,0,6) or (6,0,1). Quantify the deviations that could break the twin-label destination obstruction. Do not assume beta=0, complete F[T], or all four selecting sources without deriving them for each branch. Preserve the first contradiction or surviving routing control immediately before another unit; no further affirmation is needed.

**PROCESS RULE:** STATUS_SYNC_POLICY_V2 / RESEARCH_EXECUTION_POLICY_V3. One bounded unit, coherent preservation, one remote confirmation. No work is claimed to continue after the response ends. Pause/stop overrides continuation.
<!-- CURRENT-STATUS:END -->

## Evidence and predecessor

- [Full conditional hand proof](project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/PROOF.md).
- [Python checker and replay driver](project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/check_routing.py).
- [Differently structured C++ checker](project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/verify_routing.cpp).
- [Exact test results](project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/CHECK_RESULTS.json).
- [Lossless full reduced decision lists](project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/EXACT_DECISIONS.indexed.json); [safe decoder](project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/unpack_decisions.py).
- [Complete unchanged predecessor](archive/status-snapshots/2026-09-16/CURRENT_STATE_before_two_hole_routing_002713dc.md), copied from blob c26d7d19b07da0493f48ca72e697eeabba27f48d.
- [Individual-pool row dependency](project/research/general_n/2026-09-16-individual-pool-rows-v1/PROOF.md).
- [Full-profile dependency](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/PROOF.md).

Read AGENTS.md and only the exact mathematical dependencies needed. Older proofs, failures and reviewer material remain preserved.
