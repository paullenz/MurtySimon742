# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_R1_K2_COMPRESSED_HALF_ADDITIVE_REFINEMENT_2026_09_20`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `4706f09f4da49bf387088579c0c42b85309296f3`; this invocation began by reconciling the stale handoff with live head `ba87a2d...`, rereading CURRENT_STATE.md, README.md, the 20 September red-team audit, and the newest D1/private-spoke/cross-code/capacity/Y-cap files. It then preserved the intermediate 7/16 theorem at `baffe19...` and the first compressed half-barrier theorem at `4706f09...`, reassessing after each rather than stopping.

LAST VERIFIED RESULT: `Same-session conditional correction/strengthening. The compressed global half barrier is retained, but the provisional R:M=1:1 equality endpoint in the predecessor half-barrier note is superseded. In the compressed normal form, the proper-support W_s-free set P is independent and has only O(p) edges to the whole outside escape reservoir; hence M_U(P,E)/p^2 >= delta-delta^2/2-o(1). K-heavy Y-capacity adds alpha(1-delta). Crucially, the predecessor T bill Z_Y(T)+M_U(R,T) and the mixed slack bill E_U(M) are disjoint currencies from those P/Y blocks and may be added. Mixed-to-P complement capacity further strengthens epsilon_mixed to p+|P|-1, since the missing P neighbours are disjoint from the p+1 mandatory mixing holes. Therefore D_phys/p^2 is bounded below by F=delta-delta^2/2+alpha(1-delta)+vartheta(1+alpha)+mu(1+delta). Exact two-case minimization over alpha,delta,vartheta,mu gives F>=1/2, with equality only at alpha=0, delta=1, vartheta=mu=0. Thus the only coefficient-1/2 compressed endpoint is asymptotically pure F0. In that endpoint P=E is independent and already contributes the full half-quadratic leading term; coefficient equality therefore forces E_U,Z_X,Z_Y=o(p^2). The exact F0 sector identity then gives alpha_H(t)+beta_Y(t)=epsilon_t-2+o(p), so average F0 slack is 2+o(p) and the reservoir is simultaneously almost H-complete and Y-complete while K-free, W_s-free, q_j-nonhub and sparse-support.`

UNPRESERVED WORK: `None after atomic preservation. ONE_CODE_R1_K2_COMPRESSED_GLOBAL_7_16.md, ONE_CODE_R1_K2_COMPRESSED_GLOBAL_HALF_BARRIER.md, ONE_CODE_R1_K2_COMPRESSED_HALF_ADDITIVE_REFINEMENT.md, and this handoff are preserved. No finite scan was used.`

DEFERRED ADMIN: `README remains deliberately at the independently audited public checkpoint. Do not promote the same-session compressed half barrier, its additive refinement, or the pure-F0 equality normal form before the next daily hostile audit. Historical invalidated/superseded claims remain preserved, including the now-superseded R:M=1:1 equality statement in the predecessor same-session note.`

NEXT ACTION: `First independently hostile-replay the additive refinement: P-to-outside complement capacity; disjointness of P/U, R/Y, T and mixed-slack currencies; and the p+|P|-1 mixed slack refinement. If it survives, stop broad coefficient algebra and attack the pure-F0 equality normal form directly. Classify criticality of F0--Y and F0--H edges under simultaneous near-completeness to H,Y, independence in E, q_j-nonneighbour status and sparse private support. Any forced positive-density H/Y holes or additional slack feeds directly into the exact weighted rooted ledger and would raise the coefficient above 1/2.`

AUDIT GATE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; raw same-code criticality and ordered (source,witness) injection independently passed in later repair work; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing whenever invoked; finite scans are diagnostics only; superseded evidence stays superseded; bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3.`

SECOND STRICT: `Provisional exact unloaded second-strict chain remains finite-order: mixed y=1 x=3 gives n<=16; x=4 n<=19; x>=5 n<=33; two-X-hole arm n<=816; (0,2) empty; mixed y>=2 internally closed. Conditional on the rigid one-code interface and predecessor closures, no exact unloaded second-strict survivor remains for n>=817. Pending hostile replay.`

R1 K2 LIVE CHAIN: `Residual-one common hub/beta fan -> exact low-k k=2 ray -> one-sided escape partition -> D1/K-heavy hub-private compression -> raw cross-code complement localization -> proper-support nonhub independence -> complement-witness capacity -> F0 hub/private compression -> compressed P normal form -> global half barrier -> additive refinement -> pure-F0 equality normal form.`

R1 K2 PURE F0: `At coefficient 1/2 under compression, alpha=0, delta=1, vartheta=mu=0. Almost every escape is F0, misses q_j, has proper sparse support and lies in independent P. Since M_U(E) already supplies (1/2-o(1))p^2, equality forces all other D_phys currencies subquadratic. With gamma_E(t)=p-2+o(p), the exact F0 sector identity yields alpha_H(t)+beta_Y(t)=epsilon_t-2+o(p), so average epsilon_t=2+o(p) and almost every F0 vertex is almost complete to both H and Y.`
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
`-> escape-class physical budgets`
`-> hub/private-spoke compression`
`-> cross-code complement localization/capacity`
`-> compressed proper-support P normal form`
`-> compressed global half barrier`
`-> additive disjoint-currency refinement`
`-> pure-F0 equality endpoint`
`-> live F0--Y / F0--H raw-criticality attack`.

## Session ledger — current invocation

**Invocation start:** 18:29:56 BST.  
**Planned preservation cutoff:** 18:55:38 BST.

Substantive units completed:
1. reconciled CURRENT_STATE.md, README.md, live commits through `ba87a2d...`, and the 20 September daily red-team audit before forward mathematics;
2. hostile-replayed the general cross-code complement-localization/capacity theorem from raw rooted B-edge criticality;
3. extended the private-spoke forward/Y-killing versus reverse/H-consuming theorem to F0;
4. classified F0 residual-hub edges into forward Y/R-anticomplete or reverse injective-H rectangle branches;
5. transferred private-support sparsification to F0;
6. derived the intermediate compressed 7/16 barrier and preserved it atomically at `baffe19...`;
7. extended complement capacity from P to the whole outside escape reservoir using W_s--U_bar(d) anticompleteness and compressed nonhub R;
8. strengthened the compressed global coefficient to 1/2 and preserved the first half-barrier theorem at `4706f09...`;
9. reassessed instead of stopping and found that T and M costs are additive to the P/Y blocks in disjoint currencies;
10. strengthened mixed slack to epsilon_mixed>=p+|P|-1;
11. minimized the resulting direct additive functional exactly and corrected the equality classification: only pure compressed F0 remains at coefficient 1/2;
12. extracted the pure-F0 equality normal form: independent escape reservoir, subquadratic non-M_U defect, average slack 2+o(p), and simultaneous near-completeness to H and Y.

**Live unfinished line:** independently replay the additive half-barrier correction, then attack F0--Y and F0--H edge criticality in the pure-F0 equality normal form.

**Stop reason:** final preservation phase after twelve tightly connected mathematical/audit units in a shortened window. No mathematical blocker; the next raw-criticality endpoint attack is preserved precisely.
