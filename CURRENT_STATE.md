# Murty–Simon / Erdős #742 — live current state

> Read this file first on resumption. README may lag routine internal WIP. The complete preceding handoff is archived unchanged.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. Weak-label full-profile caps and a stronger tight-block demand/residual budget.

WORK MODE: `MATH`. One bounded continuation of the live next action: distinguish all sources of a residual profile from the used receiver pool, derive the one-hole-label source cap, and quantify its global cost. No README edit, catalogue transfer, audit promotion, workflow launch or polling.

**INSPECTED PREDECESSOR:** `31f6c8aca964de0bcaed0cdfe03f14d7abbd7e18` on main. CURRENT_STATE was read first, then AGENTS and the exact preceding proof. Main is re-read before non-forced publication.

**LAST VERIFIED RESULT:** internal conditional derivation under the FULL canonical bridge, tau>0 and |T|=|H|=d>=3. For V_t={low u:R_u=T minus {t}}, p_t=|V_t|, a K-label missing exactly t among its tight F-neighbours can be selected only at V_t. Thus x_k<=p_t and s_k<=min(d-1,p_t). Used receiver pools U_t may be strict subsets of V_t. Put m=sum p_t, beta_t=R_t-(m-p_t)>=0. Choosing any common lower bound z<=min p_t, set h=kappa-1-z(d-1), L=m-zd. Exact interface identity: 2mu+Q+sum beta_t=dh-(d-1)L. Common labels contribute demand deficit d-1; each one-hole label missing t contributes at least (d-1-p_t)_+. The finite scalar relaxation B(d,z) in the new proof therefore gives a(d-1)+d>=b+2tau+zd(2d-3)+B(d,z). Here z is a chosen pool lower bound, not necessarily chi(Gamma); z=1 is always valid and E>0 permits z=2.

**NUMERICAL CONSEQUENCES:** exact B(d,2) values for d=3..10 are 8,17,30,35,39,40,45,50. With b>=a+2 and tau>=1, extras require a at least 27,29,33,36,38,41,45,48 respectively. In particular d=5 now forces E=0 through a=32, versus a=27 previously. These are necessary bounds, not realizability or sharpness claims. z=1 also supplies whole-block necessary conditions, but no catalogue ID is newly excluded. E=0 is rigidity, NOT automatic whole-state exclusion.

**CHECKS / LIMITS:** executed Python eliminated-variable minimization and separately structured C++ full-composition enumeration agree on exact minima, feasible counts and every minimizing tuple for 131 (d,z) pairs / 1,774,146 feasible scalar tuples. Additional Python checks passed on 88,139 residual-profile multisets and 244,683 relaxed tight-interface/profile-count configurations. Four negative controls are preserved. Exact sources, losslessly encoded MINIMIZERS.json.gz.b64 and CHECK_RESULTS.json accompany the proof. These are necessary-condition tests, NOT original-graph enumeration, NOT catalogue replay, NOT inherited-bridge validation or external acceptance. Both implementations are by the same assistant.

**DEPENDENCIES / LIMITS:** exact demand level T, full selected representatives, A-side domination, inherited K-residual and disjoint-tight-destination facts, positive-surplus residual activity and maximum-degree identity where used. Do not extend to tau=0 or d<3 automatically. One-hole source confinement does not extend to labels missing two or more tight neighbours. Scalar relaxation deliberately replaces each pool price by the cheapest allowed price, so minimizers need not satisfy the individual row/profile conditions. Expert review and novelty assessment remain OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration remains unresolved; original equality replay was not rerun. No new state ID, promotion or unrestricted theorem is claimed.

**UNPRESERVED WORK:** `None` after publication. Proof, both checkers, exact results/minimizers, exploratory code and unchanged predecessor archive are included. One remote publication confirmation is required before reporting the checkpoint saved.

**DEFERRED ADMIN:** catalogue application and separate audit-promotion work; Markdown status-parser repair; reviewer/README integration after review; large-input transfer; completion reporting; unrelated CI. Do not retry the failed direct-download route. No remote CI success is asserted.

**NEXT ACTION:** one bounded mathematical unit retaining individual prices (d-1-p_t)_+ and the exact row constraints q_t+nu_t+beta_t=h-L+u_t. Start at the d=5,z=2 scalar minimum h=4,L=2,n0=1,n1=12,n2=0: distribute the two extra sources across five pools and determine whether twelve one-hole labels can have the zero deficit granted by the coarse relaxation. Preserve the first stronger bound, infeasibility proof or counterexample; do not infer original-graph realizability or catalogue promotion. No further affirmation is needed.

**PROCESS RULE:** STATUS_SYNC_POLICY_V2 / RESEARCH_EXECUTION_POLICY_V3. One bounded mathematical unit, immediate coherent preservation, one remote confirmation. No work is claimed to continue after the response ends. Pause/stop overrides continuation.
<!-- CURRENT-STATUS:END -->

## Exact evidence and predecessor

- [Weak-label profile proof and budget](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/PROOF.md).
- [Python checker and replay driver](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/check_profiles.py).
- [C++ full scalar enumerator](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/verify_minima.cpp).
- [Exact results](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/CHECK_RESULTS.json).
- [All checked scalar minima and minimizing tuples](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/MINIMIZERS.json.gz.b64).
- [Initial exploratory minimizer, not the certification driver](project/research/general_n/2026-09-16-weak-label-profile-budget-v1/explore.py).
- [Unchanged predecessor handoff](archive/status-snapshots/2026-09-16/CURRENT_STATE_before_weak_profiles_31f6c8ac.md), preserved from blob b1cc7624fe4d1840bcb341beba815cac3315023b.
- [Predecessor tight-interface proof](project/research/general_n/2026-09-16-tight-interface-slack-v1/PROOF.md).
- [Canonical bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).

Read AGENTS.md and only the mathematical dependencies needed for the next unit. Older evidence and reviewer navigation remain preserved.
