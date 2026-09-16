# Murty–Simon / Erdős #742 — live current state

> Read this file first on resumption. This checkpoint follows the strategic pivot; it does not restart the equality-by-equality programme. The full predecessor handoff is preserved unchanged.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_PROOF_NOT_PROMOTED`. Shared residual-receiver budget for selected-label bundles, including certified destination-leakage allowances.

WORK MODE: `MATH`. One bounded unit: formulate a parameterized shared-cost inequality before specializing, prove its residual-incidence reuse accounting, test it on the Omega=34 control, and preserve all evidence. No README edit, catalogue replay, promotion, workflow launch or polling.

**INSPECTED PREDECESSOR:** `888e24fe285db0363a2670370e933963f937a02b` on main, tree `4b7910a7bdeaf8ae94a32aa8edb1344a5bc0ab36`. CURRENT_STATE was read first, then AGENTS and the exact endpoint-cap and fixed-neighbourhood-flow dependencies. Main is re-read before non-forced publication.

**LAST VERIFIED RESULT:** conditional HAND PROOF under the full canonical representative facts and explicit bundle hypotheses. Disjoint label bundles L_t have g_t>=2 labels, m_t monitored full-bundle sources with residual ceiling C_t, positive label demands at least s_t, common residual support H of size h0, and an outside set O at which no monitored-family label is selected. At most D_t monitored obligations from bundle t may escape O. Put eps_t=min(g_t-1,floor(D_t/m_t)) and theta_t=(h0+s_t-C_t-eps_t)_+. Each label has R_i>=h0+g_t-1-eps_t. A receiver serving bundle-index set Z needs at least sum_Z(g_t-1)+max_Z theta_t residual incidences and receives at most min(rho_v+b-a-1,sum_Z m_t) monitored arcs. Hence Q-sum D_t<=sum_(v in O) F_D(rho_v), with F_D defined by a finite bundle-subset capacity maximization. Any rational envelope F_D(r)<=A0(r-1)+B0 gives a lower bound on the ONE shared budget sigma_O, not a sum of separately reusable receiver budgets.

**REUSE / DEFECT ACCOUNTING:** different mates within a bundle require distinct destinations; multiple sources sending the same label may share one receiver; residual labels from disjoint bundles are distinct; external residual labels may overlap and are counted by MAXIMUM, not sum. Escaping an entire label type costs m_t escaped arcs, explaining floor(D_t/m_t). Closed internal all-or-none bundle presence proves D_t=0. Measured partially present internal destinations give explicit upper allowances using min(m_t,receiver capacity). A general conversion from arbitrary selection omissions to small D_t has NOT been proved.

**CONTROL-PATTERN CONSEQUENCE:** in the predecessor's Omega=34 pattern, use the ten one-hole labels as five paired bundles, h0=5,m_t=2,g_t=2,s_t=2,C_t=4,c=4,D_t=0. The hypotheses follow from its proved saturation and beta=0, not from an assumed graph realization. theta_t=3, Q=20; F_D(r)=0 for r=1,2,3 and F_D(4)=2. At least ten distinct degree-four O-receivers are required, so sigma_O>=30. This is a branch-specific shared cost. At Omega=34, 4a+5>=b+2tau+134 and tau>=1 implies a>=45 for THAT branch only. It is NOT a universal a>=45 claim, nor an unconditional contradiction of that branch.

**GLOBAL CONSEQUENCE / LIMIT:** Omega>=34 was already proved. The new branch cost plus integrality gives Omega+alpha+sigma_H+sigma_O>=35, so 4a+5>=b+2tau+105 and a>=ceil((102+2tau)/3) for d=5 extras. At tau=1 the necessary minimum remains a>=35; the simplified threshold has NOT improved. Do not infer Omega>=35: the new bound is on the joint expression. With otherwise unchanged bundle hypotheses, a certified allowance of just one escaped arc still requires sigma_O>=30 by integer receiver counting; that does not equate one selection omission to one escaped arc.

**CHECKS / LIMITS:** executed Python bundle-subset and C++ integer-allocation enumerators agree on the FULL sequence of 78,624 receiver-capacity costs. SHA256 63f57d1ed7b8cadd3d83b97888efc45a790ab8553059a51f1608b0fe329bb58f. Additional tests: 78,076 small monitored-destination assignments (2,306 type-compatible), 75,894 finite residual-union configurations, 14,256 endpoint scalar cases, exact Omega-control resource cover, one-leakage control, six assumption/reuse controls. Compressed exact costs and a decoder preserve evidence without recomputing it. Both implementations are by the same assistant. NOT original-graph enumeration, NOT catalogue replay, NOT inherited-bridge validation or independent acceptance. A displayed resource-only cost-30 witness is not a full canonical routing or graph.

**COVERAGE / SCOPE:** theorem has variable bundle sizes, demands, source ceilings and certified leakage; no exact d=5 block is assumed in its general statement. It still requires full monitored source bundles, positive demands, forced residual support and no selected monitored-family labels at O. No forcing theorem makes every counterexample satisfy these conditions. No universal tight-or-diffuse alternative or selection-defect robustness theorem is claimed. Standard capacity pricing is not claimed new. External mathematical review and novelty assessment remain OPEN. Retain the true counterexample margin tau>=1+floor((b-a-1)^2/4) in applications.

**CANONICAL / PROMOTED STATUS:** unchanged — **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration is unresolved; original equality replay is not rerun. No new state ID, promotion or unrestricted theorem.

**UNPRESERVED WORK:** `None` after non-forced publication and one remote confirmation. Full proof, both checkers, exact costs/results, decoder and unchanged predecessor archive accompany this handoff. Publication is not claimed until remote confirmation.

**DEFERRED ADMIN:** catalogue coverage census and separate promotion work; Markdown status-parser repair; reviewer/README integration after review; large-input transfer; automatic completion reporting; unrelated CI. No remote CI success asserted. Publication protocol unchanged.

**NEXT ACTION:** one bounded defect-to-leakage unit. Starting with intact monitored source subsets and partial internal bundle presence, bound the total escaping obligations using the SHARED capacities of bad internal destinations; either derive a quantitative bound from an explicit incidence/profile defect or preserve a small countermodel showing amplification. Do not presume D(I) selection omissions directly bound D_t. Keep the joint residual objective rather than attacking the next isolated Omega integer. A later whole-catalogue hypothesis-coverage diagnostic remains unperformed. Preserve the first substantive result or obstruction before moving on; no further affirmation needed.

**PROCESS RULE:** STATUS_SYNC_POLICY_V2 / RESEARCH_EXECUTION_POLICY_V3 unchanged. One bounded unit, coherent preservation, one remote confirmation. No background continuation or automatic promotion; pause/stop overrides continuation.
<!-- CURRENT-STATUS:END -->

## Proof and exact evidence

- [Shared-bundle budget and leakage proof](project/research/general_n/2026-09-16-shared-bundle-budget-v1/PROOF.md).
- [Python checker and replay driver](project/research/general_n/2026-09-16-shared-bundle-budget-v1/check_budget.py).
- [C++ incoming-allocation checker](project/research/general_n/2026-09-16-shared-bundle-budget-v1/verify_budget.cpp).
- [Exact check results](project/research/general_n/2026-09-16-shared-bundle-budget-v1/CHECK_RESULTS.json).
- [Lossless cost sequence](project/research/general_n/2026-09-16-shared-bundle-budget-v1/EXACT_COSTS.bin.gz.b64); [decoder](project/research/general_n/2026-09-16-shared-bundle-budget-v1/unpack_costs.py).
- [Manifest](project/research/general_n/2026-09-16-shared-bundle-budget-v1/MANIFEST.json).
- [Complete strategic predecessor](archive/status-snapshots/2026-09-16/CURRENT_STATE_before_shared_bundles_888e24fe.md), preserved from blob b97a218245fe77e6dcc6461fda394cebd0c2d7a8.
- [Endpoint-cap dependency](project/research/general_n/2026-09-16-residual-endpoint-cap-v1/PROOF.md).
- [Fixed-neighbourhood routing dependency and limits](project/research/general_n/2026-09-12-arc-realisation-pilot-v1/FIXED_NEIGHBOURHOOD_FLOW.md).

Read AGENTS.md and only the exact mathematical dependencies needed. Earlier mathematics, failed models, strategy and publication records remain preserved.
