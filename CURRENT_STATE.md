# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_R1_LOW_K_ESCAPE_2026_09_20`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `5cfeaf5ad002bf6434ed936d91f98885936db7b9`; before forward mathematics this invocation reread CURRENT_STATE.md, README.md, the latest commits, the 20 September daily red-team audit, the complete residual-one orientation-covering note, the physical-reprice/private-orientation note, and the exact pair-local scalar-gate definitions.

LAST VERIFIED RESULT: `Same-session hostile replay found no overlap/location defect in OC-RECT through OC-RES. Full residual-one optimization then exposed a new exact unbounded low-k/high-y parameter family: c=p=lambda=t, y=t-1, g0=1, k=2, u=x=t+1, m=t-1, s_f=2, n=5t+2 for t>=4. It survives the strengthened OC score gate, exact predecessor rooted-Q gate, and the audit-mandated aggregate exact Ccap_P/(ONE-P)/(CROWD) gates. In the k=2 endpoint the beta map is the transposition on K={a,b}; the two beta singleton equations force cross holes. Combining those holes with orientation covering proves that any escape vertex adjacent both K and W_s pays epsilon_w>=p+1. Hence every escape of slack <p+1 is one-sided: it is anticomplete to K or anticomplete to W_s.`

UNPRESERVED WORK: `None: ONE_CODE_R1_LOW_K_ESCAPE_AND_MIXING_DICHOTOMY.md, check_r1_low_k_escape.py, and this exact handoff are committed. The checker replays the closed-form family arithmetic through t=10000; it is diagnostic only.`

DEFERRED ADMIN: `README remains deliberately at the independently audited public checkpoint. Do not promote the same-session low-k residual-one family or mixing dichotomy before the next daily hostile audit. Historical failed/superseded claims and CI failures remain preserved.`

NEXT ACTION: `Hostile-replay LK-CROSS through LK-ONESIDE first. If they survive, keep the cheap escape reservoir partitioned into K-serving and W_s-serving vertices and derive a joint degree/rooted-residual conservation law; the target is to show that avoiding p+1 mixed-escape slack forces enough located K--E or W_s--E holes to close the k=2 ray, or else to characterize the exact one-sided scaling geometry. Do not return to a scalar min(k,p-1) aggregation. Keep exact Ccap_P/(ONE-P)/(CROWD) pair-local whenever invoked and keep the zero-positive actual-D2C rigid-fixture caveat active.`

AUDIT GATE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; raw same-code criticality and ordered (source,witness) injection independently passed in later repair work; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing whenever invoked; finite scans are diagnostics only; and bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3.`

SECOND STRICT: `Provisional exact unloaded second-strict chain remains finite-order: mixed y=1 x=3 gives n<=16; x=4 n<=19; x>=5 n<=33; two-X-hole arm n<=816; (0,2) empty; mixed y>=2 internally closed. Conditional on the rigid one-code interface and predecessor closures, no exact unloaded second-strict survivor remains for n>=817. Pending hostile replay.`

R1 PREDECESSOR: `At r=p-m=c-d_U=1, K has code C=d xor e_j, matched heads h_i have support {i} or {i,j}, A_bar(C)=empty for p>=3, |U_bar(C)|<=c-1, e(K)<=k(c-1), and the old exact high-k stress family c=p=2t,y=1,g0=2t-1,lambda=4t-2,u=x=3t,k=t+1,d_U=2t-1,m=p-1,n=10t+2 is now rejected by orientation covering for t>=5.`

R1 HOSTILE REPLAY: `The q_j hub beta orientation was re-derived: reverse orientation is impossible; the forward A-witness has code C and lies in K\{h}; this forces h--a_h absent and N_Y(z_h)=empty. The two same-code U--U orientations then give E(W_s,U_bar(d))=empty. Replaying private-coordinate spokes gives E(K,H)=empty. No missing witness location or orientation was found, but all claims remain conditional on rigid-interface reachability.`

R1 PHYSICAL REPRICE: `Write f:K->K, r_a=|f^{-1}(a)|, s_f=|im f|, E=U\W_s and P for beta-forced W_s--E nonedges. Each z_h has exactly one X-neighbour, no Y-neighbour, no W_s-neighbour, so epsilon_z_h>=p+k-2+P_h and E_Ws>=k(p+k-2)+P. The active beta witnesses give L_X+P>=lambda s_f+k. Every inactive b in K\im f has epsilon_b>=g0+1, hence L_X+P>=T(s_f)=lambda s_f+k+(k-s_f)(g0+1)=k(g0+2)+s_f(c-2). For p>=4 an actual survivor must admit 2<=s_f<=k satisfying the exact predecessor score/rooted gates.`

R1 ORIENTATION MATRIX: `For every h in K and private coordinate i, criticality of z_h q_i has only F: witness h_i with N(z_h) cap N(h_i)={q_i}, or R: witness h with N(q_i) cap N(h)={z_h}. If h_i has radius-two code d xor e_i xor e_j, F is impossible because q_j is a second common neighbour; therefore R is forced for every h. If E_bad consists of escape U vertices adjacent some such q_i, then E(K,E_bad)=empty.`

R1 ORIENTATION COVER: `Independent same-session replay confirms: for w in E, A_w x S_w cells are forced F and B_w x T_w cells are forced R, so (A_w cap B_w) x (S_w cap T_w)=empty. The J1 and J2 missing-pair sets lie in the exact U-slack degree universe and are disjoint where added. Thus epsilon_w>=min(k,p-1) and E_E>=(c-1)min(k,p-1) survive hostile replay at their stated conditional scope.`

R1 LOW-K ESCAPE: `For every t>=4, the exact family c=p=lambda=t, y=t-1, g0=1, k=2, u=x=t+1, m=t-1, s_f=2 has n=5t+2. Here L0=floor(5t/2)+2, T=2t+2, OC score floor=floor(13t/2), C0=floor((3t^2+10t-4)/2), and the rooted margin is t^2-5t-2+C0>0. With g_P=t-1, k_P=2, S_P=2t and D0=7t+3, exact Ccap_P and purified ONE-P have large positive margin while scalar CROWD is zero. Therefore this is a genuine aggregate-method escape family, not a graph construction.`

R1 K2 MIXING: `Write K={a,b}; f swaps a,b. The beta equations N(z_a) cap N(b)={q_j} and N(z_b) cap N(a)={q_j} force two cross holes for every escape w. If w sees both K and W_s, those cross exclusions force A_w cap B_w nonempty; orientation covering then forces S_w cap T_w empty. Such a mixed w cannot be J2-bad, so it misses all J2 q_i as well. The two beta cross holes, J1 fibre holes and J2 q_i holes are disjoint, giving epsilon_w>=2+|J1|+|J2|=p+1. Hence epsilon_w<p+1 implies w is one-sided between K and W_s.`
<!-- CURRENT-STATUS:END -->

---

## Binding audit gate

Latest daily audit: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Binding constraints:

- repaired P1/P2 semantics;
- raw same-code criticality / ordered `(source,witness)` injection independently passed in the subsequent upstream repair;
- `X_3` mandatory negative control;
- zero positive actual-D2C rigid complete Hall cuts with `x>=3` in bounded regression;
- exact pair-local `Ccap_P`, `(ONE-P)`, `(CROWD)` whenever invoked;
- finite scans are diagnostics only;
- superseded evidence stays superseded;
- same-session closures stay provisional until independent adversarial replay.

## Live structural chain

`audited rooted/Hall setup`
`-> rigid singleton-head implication`
`-> provisional unloaded second-strict finite-order closure`
`-> one-code private-coordinate exhaustion r=c-d_U`
`-> hostile-replayed W independence / quadratic U price`
`-> exact Psi_phys ellipse and rooted-Q feedback`
`-> residual-one normal form`
`-> common residual hub q_j`
`-> forced beta witness map f:K->K`
`-> W_s--Y=empty and W_s--U_bar(d)=empty`
`-> K--H=empty`
`-> beta multiplicity tradeoff`
`-> physical P repricing on both U-slack and X-slack`
`-> private-coordinate F/R orientation matrix`
`-> radius-two coordinates force reverse orientation`
`-> radius-one forced-rectangle covering theorem`
`-> hostile-replayed universal escape floor epsilon_w>=min(k,p-1)`
`-> old high-k t-ray finite`
`-> new exact k=2 high-y escape ray`
`-> k=2 beta cross-hole normal form`
`-> mixed escape penalty epsilon_w>=p+1`
`-> live one-sided escape-partition attack`.

## Session ledger — current invocation

**Invocation start:** 16:30:32 BST.  
**Planned preservation cutoff:** 16:55:38 BST.

Substantive units completed:

1. reconciled CURRENT_STATE, README, latest commits and the 20 September daily red-team audit before forward mathematics;
2. independently hostile-replayed `OC-RECT` through `OC-RES`, including the exact degree-universe and disjointness checks, and found no defect at the stated conditional scope;
3. optimized the strengthened residual-one score/rooted gates over the full parameter domain diagnostically and extracted the exact unbounded low-k family `c=p=lambda=t, y=t-1, k=2, u=x=t+1, n=5t+2`;
4. verified that family analytically against exact `OC-SCORE` and `PR-ROOT`, showing quadratic positive margins rather than a bounded-box artefact;
5. replayed the audit-mandated exact pair-local `Ccap_P`, purified `(ONE-P)` and scalar `(CROWD)` gates on the new family and proved all three aggregate gates remain open;
6. exploited the forced two-cycle beta map at `k=2` to derive the two physical cross-hole constraints for every escape vertex;
7. combined those cross holes with orientation covering and the J2 theorem to prove the new mixing dichotomy: every escape touching both K and W_s pays `epsilon_w>=p+1`, so every cheaper escape is one-sided;
8. added a closed-form diagnostic checker through `t=10000` and preserved the theorem/checker/handoff in the repository.

**Live unfinished line:** keep the cheap escape reservoir partitioned into K-serving and W_s-serving vertices and derive a joint maximum-degree/rooted-residual conservation law. The key question is whether avoiding mixed vertices forces enough located K--E and W_s--E holes to eliminate the exact k=2 ray. If not, characterize the one-sided physical scaling geometry exactly before any further scalar aggregation.

**Stop reason:** preservation checkpoint after eight tightly connected mathematical/audit units. No mathematical blocker and no clean-checkpoint early stop; the next coherent structural line is preserved for immediate continuation.
