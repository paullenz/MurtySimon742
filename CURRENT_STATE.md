# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_R1_K2_COMPRESSED_GLOBAL_HALF_2026_09_20`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `baffe19b28a402133b19d4b1139231eee449e2e4`; this invocation began by reconciling the stale handoff with live head `ba87a2d...`, rereading CURRENT_STATE.md, README.md, the 20 September red-team audit, the newest D1/private-spoke/cross-code/capacity/Y-cap files, and then preserving the intermediate compressed `7/16` theorem atomically at `baffe19...` before immediately reassessing and continuing.

LAST VERIFIED RESULT: `Same-session conditional strengthening. The W_s--U_bar(d) anticompleteness plus general complement-witness capacity implies that, in the compressed normal form, the dominant proper-support q_j-nonneighbour W_s-free set P is not only independent but has only O(p) total edges to the entire escape reservoir outside P: compressed nonhub K-heavy vertices cannot have code bar(d), while every F1/W-heavy/mixed vertex touches W_s and therefore cannot have code bar(d). Thus M_U(P,E) >= (delta-delta^2/2-o(1))p^2. K-heavy Y-capacity adds the disjoint block Z_Y(R)>=(alpha(1-delta)-o(1))p^2, giving L2=delta-delta^2/2+alpha(1-delta). The predecessor additive class theorem gives L1=1-alpha-delta/2. These simultaneous bounds imply max(L1,L2)>=1/2 for every admissible alpha,delta, so the earlier same-session 7/16 bound is superseded by a compressed global half barrier. Equality before further feedback requires alpha=mu=(1-delta)/2, theta=0 and D asymptotically all F0. A mixed vertex, however, has at most two neighbours in P, and those missing P-neighbours are disjoint from the p+1 mandatory mixing holes, so epsilon_mixed>=p+|P|-1 and the mixed coefficient is 1+delta. This destroys every interior equality point 0<delta<1. The only relaxed coefficient-1/2 endpoints left are: (A) pure compressed F0; or (B) no D/T mass and R:M=1:1.`

UNPRESERVED WORK: `None after the atomic preservation commit. ONE_CODE_R1_K2_COMPRESSED_GLOBAL_7_16.md, ONE_CODE_R1_K2_COMPRESSED_GLOBAL_HALF_BARRIER.md, and this handoff are preserved. No finite scan was used.`

DEFERRED ADMIN: `README remains deliberately at the independently audited public checkpoint. Do not promote the same-session compressed half barrier, F0 extensions, or endpoint classification before the next daily hostile audit. Historical invalidated/superseded claims and failed CI evidence remain preserved.`

NEXT ACTION: `First hostile-replay the new half-barrier proof, especially: (i) the claim that every T/M vertex has code != bar(d) from W_s--U_bar(d) anticompleteness; (ii) the use of nonhub R to exclude code bar(d); (iii) complement-capacity conversion to O(p) P--outside edges; (iv) disjointness of the p+1 mixed slack holes from P. If all survive, attack the two coefficient-1/2 endpoints directly. Endpoint A (pure F0): use exact F0 sector equality, A--U edge criticality and maximum-degree saturation. Endpoint B (R:M=1:1): classify the two aligned mixed types forced by beta cross exclusions and apply raw R--M U--U criticality with no F0 repair capacity. Keep exact weighted currencies E_U,Z_X,Z_Y,M_U separate.`

AUDIT GATE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; raw same-code criticality and ordered (source,witness) injection independently passed in later repair work; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing whenever invoked; finite scans are diagnostics only; superseded evidence stays superseded; bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3.`

SECOND STRICT: `Provisional exact unloaded second-strict chain remains finite-order: mixed y=1 x=3 gives n<=16; x=4 n<=19; x>=5 n<=33; two-X-hole arm n<=816; (0,2) empty; mixed y>=2 internally closed. Conditional on the rigid one-code interface and predecessor closures, no exact unloaded second-strict survivor remains for n>=817. Pending hostile replay.`

R1 K2 LIVE CHAIN: `Residual-one common hub/beta fan -> exact low-k k=2 ray -> one-sided escape partition -> heavy/F0/D1 budgets -> D1 and K-heavy hub/private-spoke compression -> raw cross-code complement localization -> proper-support nonhub global independence -> complement-witness degree capacity -> Y-cap global coefficient -> F0 hub/private-spoke compression -> compressed proper-support P normal form -> global compressed half barrier -> two remaining equality endpoints: pure F0 or R:M=1:1.`

R1 K2 COMPRESSED HALF: `Let alpha=|R|/p and delta=|D|/p under the compressed normal form. P, the proper-support nonhub part of D, has density delta, is independent, and every escape outside P except o(p) exceptions has at most two neighbours in P. Thus M_U(P,E)/p^2 >= delta-delta^2/2-o(1). Since F0 density phi<=delta, K-heavy Y-capacity gives Z_Y(R)/p^2>=alpha(1-delta)-o(1), so L2=delta-delta^2/2+alpha(1-delta). The additive partition gives L1>=1-alpha-delta/2. Therefore max(L1,L2)>=1/2. Mixed-to-P complement capacity further gives epsilon_mixed/p >=1+delta-o(1), eliminating all interior equality points; only pure F0 and R:M=1:1 remain at coefficient 1/2 in the relaxed model.`
<!-- CURRENT-STATUS:END -->

---

## Binding audit gate

Latest daily audit: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Binding constraints:
- repaired P1/P2 semantics;
- raw same-code criticality / ordered `(source,witness)` injection independently passed in later repair;
- `X_3` mandatory negative control;
- zero positive actual D2C rigid complete Hall cuts with `x>=3` in bounded regression;
- exact pair-local `Ccap_P`, `(ONE-P)`, `(CROWD)` whenever invoked;
- finite scans are diagnostics only;
- superseded evidence stays superseded;
- same-session closures stay provisional until hostile replay.

## Live structural chain

`audited rooted/Hall setup`
`-> rigid singleton-head implication`
`-> provisional unloaded second-strict finite-order closure`
`-> one-code residual-one common hub / beta fan`
`-> k=2 low-k/high-y escape`
`-> heavy/F0/D1 class partition`
`-> hub/private-spoke compression`
`-> cross-code complement localization`
`-> proper-support P independence`
`-> complement-witness capacity into P`
`-> F0 compression`
`-> compressed global half barrier`
`-> pure-F0 or R:M=1:1 endpoints`
`-> live endpoint raw-criticality attack`.

## Session ledger — current invocation

**Invocation start:** 18:29:56 BST.  
**Planned preservation cutoff:** 18:55:38 BST.

Substantive units completed:
1. reconciled CURRENT_STATE.md, README.md, live commits through `ba87a2d...`, and the 20 September daily red-team audit before forward mathematics;
2. hostile-replayed the general cross-code complement-localization/capacity theorem from raw rooted B-edge criticality;
3. extended the private-spoke forward/Y-killing versus reverse/H-consuming theorem to F0;
4. classified F0 residual-hub edges into forward Y/R-anticomplete or reverse injective-H rectangle branches;
5. transferred private-support sparsification to F0 and obtained the compressed W_s-free proper-support endpoint;
6. derived and optimized the intermediate compressed `7/16` barrier, preserved atomically at `baffe19...`, and immediately reassessed rather than stopping;
7. observed that W_s--U_bar(d) anticompleteness forces every T/M source away from code bar(d), so complement capacity applies to P from the entire outside reservoir;
8. upgraded the missing-U bill to `delta-delta^2/2`, combined it with K-heavy Y-capacity and the additive class floor, and proved the compressed global coefficient is at least `1/2`;
9. retained the P-missing pairs inside mixed U-slack and proved `epsilon_mixed>=p+|P|-1`, which eliminates all interior coefficient-1/2 equality mixtures;
10. isolated the only two relaxed half-barrier endpoints: pure compressed F0, or a half K-heavy / half mixed reservoir with no D/T mass.

**Live unfinished line:** independently replay the half-barrier accounting, then attack pure-F0 and R:M=1:1 endpoints directly by raw edge criticality. Endpoint B is especially concrete because every mixed vertex has exactly one K-neighbour and one selected-witness neighbour with the same head index, while no F0 repair witnesses exist.

**Stop reason:** preservation checkpoint after ten tightly connected mathematical/audit units within the shortened research window. No mathematical blocker; the next endpoint attack is preserved for immediate continuation.
