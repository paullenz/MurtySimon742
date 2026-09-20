# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_R1_BETA_WITNESS_MULTIPLICITY_2026_09_20`

WORK MODE: `MATH_AFTER_AUDIT_GATE`

LATEST_RECONCILED_PREDECESSOR_HEAD: `aa9f246c2df30d3765b361c6ff19163fa9b1252d`.

LATEST_THIS_RUN_COMMITS: `04f5e2bd234407babb522c5a72679c1a906f7cec` (residual-one hub criticality), `bb0ceb44ba2af1e416f9570d8e7178126da88e51` (escape-ray arithmetic replay), `5604d67169a6d733c91c1f2883d4470e336f1c0a` (beta-witness multiplicity tradeoff), plus this state synchronization commit.

LAST VERIFIED/AUDITED BASE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; raw same-code criticality and ordered (source,witness) injection independently passed in later repair work; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing whenever invoked; finite scans are diagnostics only; and bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3. The zero-positive-fixture interface remains the dominant global risk.`

SECOND_STRICT_STATUS: `Same-session candidate chain closes the exact unloaded second-strict layer to finite order: mixed y=1 x=3 gives n<=16; x=4 n<=19; x>=5 n<=33; two-X-hole arm n<=816; (0,2) empty; mixed y>=2 internally closed. Conditional on the rigid one-code interface and predecessor closures, no exact unloaded second-strict survivor remains for n>=817. These remain provisional pending hostile replay.`

RIGID_INTERFACE_AUDIT: `The raw-criticality reconstruction supports M_X=E_X=0 => complete A-cut, selected crossing sources in Y, x distinct physical singleton-head witnesses per source, witnesses only in tight matched endpoints or U, x<=p+u, and complementary U-code concentration. Reachability is still unresolved; graph regression has zero positive fixtures.`

USED_WITNESS_INDEPENDENCE_REPLAY: `07f6ae6... hostile-replayed G[W]=empty and E_W>=k_P(p+k_P-2), with the orientation correction that the valid same-code U--U source must be chosen before renaming. It deliberately did not claim W anticomplete to unused U_bar(d).`

PSI_PHYS_AND_Q: `6bb6531... gives the exact Psi_phys ellipse 3R^2+4RS+4S^2<=10c^2+40c+44 in u>=c, hence n<=6c+18+sqrt(55c^2+220c+242), but c remains unbounded. 4d07e27... gives q<=d_U u-d_U(d_U+1)/2 and the exact residual-r rooted-Q inequality.`

PRIVATE_COORDINATE_EXHAUSTION: `d532bca... gives r=p-m=c-d_U. If k>0 then r>=1, d_U<=c-1 and k>=u-c+1. At r=1 all U-certified heads have the single code C=d xor e_j.`

R1_PREDECESSOR_PROFILE: `ccd5794... gives r=1: K has code C=d xor e_j; matched heads h_i have support {i} or {i,j}; A_bar(C)=empty for p>=3; |U_bar(C)|<=c-1; e(K)<=k(c-1). aa9f246... records the exact unbounded parameter stress family c=p=2t,y=1,g0=2t-1,lambda=4t-2,u=x=3t,k=t+1,d_U=2t-1,m=p-1,n=10t+2, which survives the predecessor aggregate gates.`

R1_HUB_CRITICALITY: `Direct criticality of h z_h recycles the original crossing certificate and is a dead end. The residual endpoint q_j is a common hub for all K-heads and selected W_s witnesses. Raw rooted B-edge criticality forces every z_h q_j spoke into beta orientation; its A-witness a_h has code exactly C and lies in K\{h}, h a_h is a nonedge, and N_Y(z_h)=empty. Hence N_A(z_h)={h} and k>=2.`

R1_SAME_CODE_AND_X_SPLIT: `The new Y-anticompleteness closes the orientation gap left by the general W replay: E(W_s,U_bar(d))=empty. Applying rooted criticality to every private-coordinate edge z_h q_i gives E(K,H)=empty, so G[A_X]=G[K] dotcup G[H] with no cross edges.`

R1_BETA_MAP_BASIC: `Choosing one hub beta witness per h gives a fixed-point-free map f:K->K, f(h)=a_h, on missing K-edges. Consequently bar G[K] has minimum degree at least one and e(K)<=binom(k,2)-ceil(k/2). Together with e(K)<=k(c-1), this yields the s-free strengthened L_X floor in ONE_CODE_R1_RESIDUAL_HUB_CRITICALITY.md. P1/P2 do not by themselves bound k: the beta obligations have distinct physical sources z_h at the same coordinate j.`

R1_BETA_MULTIPLICITY: `Retain r_a=|f^{-1}(a)| and s=|im f|. The k beta arcs occupy at least k-floor(s/2) distinct missing K-edges, so e(K)<=binom(k,2)-k+floor(s/2). If t_a=d_U(a) and epsilon_a is A-slack, K--H=empty and the r_a preimages give t_a>=lambda+1+r_a-epsilon_a. The singleton equation N(z_h) cap N(a_h)={q_j} forces at least P>=sum r_a(t_a-1)>=sum r_a[lambda+r_a-epsilon_a]_+ additional W_s--(U\W_s) nonedges. Exact minimization gives the conservation law L_A+2P>=lambda s+k. Consequently q<=k(c-1)+binom(c-1,2)-P and every survivor satisfies k(x+y-1)+lambda s+k<=u(p-lambda)+2(c-1)u-c(c-1)+C0. The same s sharpens X-slack to L_X>x g0-p/2+max{k(p+1)-2floor(s/2),k(p+k-2c)} for p>=4.`

R1_STRESS_TEST: `On aa9f246...'s exact family, the s-free hub theorem gives L_X>=8t^2-3t+2ceil((t+1)/2), E_W>=3t^2+2t-1, leaving positive score margin t^2+7t-3-2ceil((t+1)/2) and rooted-Q margin 3t^2+8t-4-2ceil((t+1)/2) for all t>=2. The new s-dependent multiplicity package has not yet been jointly optimized with these floors. No closure is claimed.`

PROCESS_NOTE: `README remains deliberately at the independently audited public checkpoint. Same-session r=1 results stay provisional until the next adversarial replay. The branch is still conditional on reaching a rigid complete Hall cut, and zero positive actual-D2C rigid fixtures with x>=3 remain the dominant interface risk.`

NEXT_ACTION: `First hostile-replay both new r=1 notes, especially forced beta orientation/code localization, W_s--Y and W_s--U_bar(d) anticompleteness, K--H anticompleteness, and the multiplicity degree identity t_a>=lambda+1+r_a-epsilon_a. If they survive, jointly optimize over s, the beta indegrees r_a, A-slack, forced W--escape holes P, exact Ccap_P/(ONE-P)/(CROWD), and the rooted residual identity. The target is to determine whether near-permutation maps (large s) or concentrated maps (small s) can support an unbounded family. Keep the zero-positive actual-D2C rigid-fixture caveat active throughout.`
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
`-> singleton matched budget`
`-> one-code private-coordinate exhaustion r=c-d_U`
`-> hostile-replayed W independence / quadratic U price`
`-> exact Psi_phys ellipse and rooted-Q feedback`
`-> residual-one normal form`
`-> exact residual-one scalar escape family`
`-> common residual hub q_j`
`-> forced beta spoke orientation with witness map f:K->K`
`-> W_s--Y=empty and W_s--U_bar(d)=empty`
`-> K--H=empty`
`-> image-size/multiplicity tradeoff between missing K-edges and forced W--escape holes`
`-> exact stress family still not closed by the presently separated scalar inequalities`.

The public README remains deliberately at the independently audited checkpoint. Do not promote these same-session rigid-interface refinements before daily red-team replay.

## Session ledger — current invocation

**Invocation start:** 14:28:17 BST.  
**Planned preservation cutoff:** 14:55:38 BST.

Substantive units completed:

1. reread `CURRENT_STATE.md`, README, the 20 September daily red-team audit and all commits newer than the stale handoff through `aa9f246...`, reconciling the live frontier before forward mathematics;
2. identified the direct head-witness recycling obstruction for `h z_h` and pivoted to rooted matched-hub edges;
3. exposed the literal residual-coordinate hub `q_j` common to all K-heads and selected W_s witnesses;
4. proved the reverse orientation of every `z_h q_j` spoke impossible and localized every forward beta witness to `a_h in K\{h}`, forcing `h a_h` nonedges and W_s--Y anticompleteness;
5. used W_s--Y anticompleteness to strengthen same-code U geometry to `E(W_s,U_bar(d))=empty` at r=1;
6. applied rooted criticality to private-coordinate edges `z_h q_i` and proved `E(K,H)=empty`;
7. converted hub beta certificates into a missing-edge budget on K and combined it with complement-code capacity;
8. combined the exact X-degree identity, `e(H)<p/4`, `Z_X>=k(x-1)` and the X decomposition to obtain the stronger r=1 L_X floor;
9. fed that floor into the rooted-Q ledger and stress-tested the exact `aa9f246...` family, proving it remains unbounded at the separated scalar level rather than hiding the failure behind a bounded scan;
10. audited P1/P2 against the one-coordinate geometry and proved they do not themselves imply constant k because sources vary while the coordinate is fixed;
11. retained the beta-witness image size `s` and indegrees `r_a`, proving `k-floor(s/2)` distinct missing K-edges;
12. derived the repeated-witness degree/forced-hole inequality `P>=sum r_a[lambda+r_a-epsilon_a]_+` and the exact conservation law `L_A+2P>=lambda s+k`;
13. fed P into the U-edge ceiling and obtained the s-sensitive rooted-Q condition together with the s-sensitive X-slack floor, exposing a concrete joint optimization problem rather than another one-dimensional relaxation.

**Live unfinished line:** independent hostile replay of the two new r=1 notes, then joint optimization of `(s,r_a,epsilon_a,P)` with exact pair-local gates and rooted residual bookkeeping. The key dichotomy is now explicit: small s forces many K-holes; large s raises the `lambda s` rooted-Q price.

**Stop reason:** preservation phase reached after thirteen tightly connected substantive units. No mathematical blocker and no clean-checkpoint early stop; the remaining work is the next coherent structural optimization, not a missing-tool problem.
