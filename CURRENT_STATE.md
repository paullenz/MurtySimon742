# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_SUPPLY_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime. The strongest compact route now treats residual defect and rooted triangles as the primary variables, with source-tuple / switching machinery supplying beta traffic and the new beta-sensitive degree-supply theorem controlling `q+s` and `2q+s`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `p=4,b=8,a=3,u=0,lambda=4,r=0,F=empty`.

See `project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

The new rooted-triangle transfer identities below interpret this exception exactly: `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`, and the counterexample transfer window collapses to the single value `Q-f=12`. Any eventual proof must permit this finite endpoint mechanism.

## 2. Near-full normal form

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

Let the complete tight-antipode matching in `B` have `p` pairs and let `U` be the unmatched part, `u=|U|`, so `b=2p+u`. Every vertex of `A union U` chooses exactly one endpoint from every tight pair and has a Boolean code in `{0,1}^p`.

Put `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Then

> `a=2p+u-lambda-1`,
>
> `Q=e(G[B])=p(p+u-1)+q`,
>
> `r=(p+u)(a-p)+p-s-q`,
>
> `delta=b(n-b)-m=r-f`.

For `epsilon_z=b-d(z)`, put

> `E_U=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,
>
> `L_A=sum_{x in A}epsilon_x=a(p+u)-s-2f`.

The separate `Q=0` / false-twin-core branch remains open and must not be conflated with this triangle-containing partial-Boolean branch.

## 3. New exact residual-defect formulation of the threshold

Put

`c_lambda=ceil(lambda(lambda+2)/2)`

and

> `D_M=ceil((4p+2u-c_lambda-2)/2)`.

The new exact residual-scorecard identity is

> `E_U+L_A=2delta+lambda(p+u)-p`.                         `(RS)`

Moreover

> `D_M=b(n-b)-M(n)`,
>
> `m<=M(n) iff delta>=D_M`,
>
> `m>M(n) iff delta<=D_M-1`.                              `(RT)`

Thus the active second-extremal target is exactly the residual-defect inequality `delta>=D_M`.

This supersedes treating `(GS-A)` as the conceptual endpoint; the scorecard remains useful, but it is an affine encoding of residual defect.

Core file:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md`.

## 4. New rooted-triangle transfer identities

The rooted triangle count is an exact transfer variable between the A-side and U-side slack accounts:

> `r+Q=L_A+2f`,                                           `(RQ1)`
>
> `delta+Q=L_A+f`,                                        `(RQ2)`
>
> `delta=E_U+Q-f-lambda(p+u)+p`.                          `(RQ3)`

With

> `T:=Q-f`,

these become

> `L_A=delta+T`,
>
> `E_U=delta+lambda(p+u)-p-T`.                            `(TR)`

Hence every above-`M(n)` candidate must place its rooted-triangle surplus in the exact transfer window

> `L_A-D_M+1 <= T`
> `              <= D_M-1+lambda(p+u)-p-E_U`.            `(TW)`

This is now the preferred way to phrase the triangle-containing residual problem. The order-12 `X_3` negative control saturates both endpoints of `(TW)`.

## 5. Preserved switching / Hall / source-tuple stack

A switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

If `sigma_0` is the largest zero-signed subcore obtainable after switching, then above threshold

> `sigma_0(sigma_0-1)<=C_0`,                              `(SD)`

where `C_0=S_req-2` is the preserved above-threshold scorecard cap.

With

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`,

one has `sigma_0<=R_*`, unmatched-row cover lower bounds, and `mu_alpha<=R_*` for the largest projective alpha / switching true-twin class.

Selected/Hall consequences include

> `nu_c t_c<=a`,
>
> `p(t_c+t_bar c)<=(mu_alpha+1)a`,
>
> `min(h,p)a>=pu-mu_alpha a`.

For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x`, and `Y_x` the pairwise-distinct designated unmatched beta sources. The exact source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`    `(FDPr)`

for every `r>=3`.

If `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`.

## 6. Preserved total beta-load envelopes

Put

`B_beta=sum_x ell_x=pu-h_alpha`.

For `r>=3` and `0<=K<=p-r`, define

> `U_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

Then

> `B_beta<=a(p-K-1)+(K+1)U_r(K)`.                        `(STB)`

Above threshold put `R_hat=min(p,R_*)`. Then

> `B_beta >= [pu-R_hat a]_+`.                             `(STL)`

The root-imbalance floor gives independently

> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

In linear scaling

`u/p->rho`, `lambda/p->theta`, `A=2+rho-theta>0`,

`c=C_0/p^2 -> theta(1+rho)-theta^2/2`,

`R=min(1,sqrt(c))`,

one has the preserved source-tuple upper envelope `(CBE)` and beta lower bounds

> `beta:=lim B_beta/p^2 >= [rho-A R]_+`,
>
> `beta >= (theta-2)_+`.                                  `(CBL/RBF)`

The source-root envelope `(SRE)` remains the main compact high-`rho` beta tool.

## 7. Preserved distinct-source and beta-sensitive `q` theorems

Because the designated beta sources of one A-witness are pairwise distinct,

> `ell_x<=min(p,u)`,
>
> `B_beta<=a min(p,u)`.                                   `(DSB)`

For `u<=p` this gives the finite root wedge

> `lambda<=2p-1+floor(u^2/(p+u))`,                        `(FDRW)`

and in the high-root-imbalance continuum branch `0<rho<1`

> `theta<2+rho^2/(1+rho)`.                                `(SDRW)`

Above threshold the switching/distinct-source sandwich gives

> `pu<=a(u+R_hat)`                                        `(DSS-f)`

and, for `theta>2`,

> `rho>2-sqrt(3)`.                                        `(RHO27)`

The preserved beta-sensitive U-edge theorem is

> `q<=a u-B_beta+N_1`,                                   `(BQ)`

where `N_1=|{x:ell_x=1}|`. In continuum form

> `xi=q/p^2<=A rho-beta`.                                 `(CBQ)`

For `theta>2`, `rho<1`, combining with switching gives

> `xi<=A(rho+R)-rho`,                                     `(SQ)`

which strictly improves the older sparse-U cap throughout that branch.

## 8. New beta-sensitive joint degree-supply theorem

For each `x in A`, let `d_x=d_U(x)` and let `w_x` be the number of chosen oriented U-edge certificates using `x` as A-side witness.

The new complement-code non-neighbour lemma says:

- if `ell_x>=2`, then no U-neighbour of `x` has code `bar(c(x))`, so `w_x<=u-d_x`;
- if `ell_x=1`, at most the one designated beta source can be complementary, so `w_x<=u-d_x+1`;
- if `ell_x=0`, use `w_x<=u`.

Let

`A_0={x:ell_x=0}`,

`N_0=|A_0|`,

`N_1=|{x:ell_x=1}|`,

`s_0=sum_{x in A_0}d_U(x)`.

Then

> `q+s<=a u+s_0+N_1`,                                    `(QS)`
>
> `2q+s<=2a u-B_beta+s_0+2N_1`.                          `(2QS)`

Consequently

> `r>=p(p-lambda)-s_0-N_1`,                              `(RLOW)`
>
> `E_U>=u(p+u-1)-2a u+B_beta-s_0-2N_1`.                 `(ELOW)`

This is the first direct beta-sensitive theorem for the combined `2q+s` degree supply, and it remains meaningful when `u>=p`. The only coarse escape is now sharply localized in the zero-beta A--U supply `s_0`.

## 9. New zero-load compression and parameter-only slack floor

Let `L=min(p,u)` with `u>0`. Since every nonzero beta-loaded A-vertex has load at most `L`,

> `N_0<=a-ceil(B_beta/L)`,
>
> `s_0<=u[a-ceil(B_beta/L)]`.                             `(S0)`

Using also `N_1<=a`,

> `E_U`
> `>=u(p+u-1)-3a u+B_beta`
> `  +u ceil(B_beta/L)-2a`.                               `(PEF)`

For an above-threshold candidate define

> `B_*=max(0,p(lambda+1-2p),pu-R_hat a)`.

The right side of `(PEF)` is monotone in beta load, so

> `E_U>=F_E(p,u,lambda)`                                  `(PEF*)`

with `B_beta` replaced by `B_*`. Since `E_U<=C_0`,

> `F_E(p,u,lambda)<=C_0`                                  `(DSF)`

is a new finite parameter-only necessary condition.

In linear scaling this gives

> `liminf E_U/p^2`
> `>=rho(1+rho-3A)`
> ` +(1+max(1,rho)) beta`.                                `(CDE)`

Hence every limiting above-threshold candidate satisfies

> `rho(1+rho-3A)`
> ` +(1+max(1,rho)) beta_* <= c`,                         `(CDS)`

where

> `beta_*=max(0,theta-2,rho-A R)`.

For `rho>=1`, `theta>2`, the root floor alone gives the clean necessary cap

> `theta<=-3rho+sqrt(13rho^2+14rho+4)`.                  `(CDS+)`

This cap is not promoted as numerically stronger than `(SRE)`; its value is that it prices beta traffic directly into unmatched slack and residual degree supply.

## 10. Cylinder and enhanced-IPM machinery: preserved, supporting role

The repaired beta-cylinder theorem and all critical-witness channels remain valid. However `(FDPr)` implies, for `u,a=O(p)`,

> `sum_x 2^{-k_x}=O(1)`,

hence the total distribution-free cylinder mass is only `O(p)`. The old generic plan of forcing the complete-cylinder inequality to quadratic scale remains retired.

The continuum enhanced IPM `(CEIPM)` also remains valid and should be used as a supporting global constraint, especially with `(CBQ)/(SQ)` for `theta>2,rho<1` and `(QMIN)` for `0<theta<2`.

The new residual/rooted-triangle formulation is now preferred as the conceptual spine because it targets `delta>=D_M` directly rather than optimizing auxiliary densities for their own sake.

## 11. Verification at this checkpoint

Preserved audits include the exact published 12/32 `X_3` reconstruction and the earlier signed-2-lift, matched-foot, A/U-overlap, same-code, source-tuple, source-root switching and distinct-source suites.

New audit package:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/check_rooted_residual_supply.py`

with frozen summary

`ROOTED_RESIDUAL_SUPPLY_CHECK_SUMMARY.json`:

- exact residual threshold checks: 19,425;
- residual/slack/rooted-triangle transfer identity checks: 200,000;
- local degree-supply synthetic checks: 250,000;
- zero-load compression / unmatched-slack checks: 250,000;
- **719,425 total checks, zero failures**.

These checks are audit support only; promoted statements rest on the hand proofs.

## 12. Active next move

Priorities, in order:

1. **Zero-beta cross-edge capacity.** Bound `s_0=sum_{ell_x=0}d_U(x)` structurally using alpha congestion, switching/true-twin capacity, A-edge criticality or rooted-triangle transfer. Any nontrivial improvement over `s_0<=uN_0` feeds simultaneously into `(RLOW)`, `(ELOW)`, `(TW)` and the target `delta>=D_M`.
2. **Exploit the exact transfer window `(TW)`.** Split by the position of `T=Q-f`: near the A-side endpoint force U-slack; near the U-side endpoint force A-slack / internal-A structure. The `X_3` graph is the endpoint-saturated negative control.
3. **High `theta>2`, `rho>=1`.** Combine `(2QS)/(CDE)` with `(SRE)/(CBE)` rather than seeking a q-only theorem. The obstruction is now zero-beta cross degree, not unidentified U-edge supply.
4. **High `theta>2`, `rho<1`.** Preserve `(SDRW)/(SDSS)/(SQ)`; use `(CEIPM)` only if it yields a short hand-certifiable exclusion, not decimal optimization.
5. **Moderate `0<theta<2`.** Preserve weighted `(QMIN)` and the new residual-transfer formulation.
6. Keep the `u=0` full-tight finite exception protected. No unmatched-layer argument suppresses the published 12/32 graph.
7. Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

<!-- CURRENT-STATUS:END -->