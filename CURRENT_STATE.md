# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_INTEGRATED_SOURCE_SUPPORT_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime. The conceptual spine is now residual defect `delta`, rooted-triangle transfer `T=Q-f`, integrated source-tuple beta capacity, and beta-support control of the zero-beta cross-edge reservoir.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `p=4,b=8,a=3,u=0,lambda=4,r=0,F=empty`.

See `project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

For this graph `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, and the residual threshold below is `D_M=1`. Its rooted-triangle transfer window collapses exactly to `Q-f=12`. Any eventual theorem must permit this finite endpoint-saturated mechanism.

## 2. Near-full normal form and exact residual target

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

> `E_U=u(p+u-1)-2q-s`,
>
> `L_A=a(p+u)-s-2f`.

Put

`c_lambda=ceil(lambda(lambda+2)/2)`

and

> `D_M=ceil((4p+2u-c_lambda-2)/2)`.

The exact residual-scorecard identity is

> `E_U+L_A=2delta+lambda(p+u)-p`.                         `(RS)`

Moreover

> `D_M=b(n-b)-M(n)`,
>
> `m<=M(n) iff delta>=D_M`,
>
> `m>M(n) iff delta<=D_M-1`.                              `(RT)`

Thus the active second-extremal target is exactly `delta>=D_M`.

The separate `Q=0` / false-twin-core branch remains open and must not be conflated with this triangle-containing partial-Boolean branch.

## 3. Rooted triangles are an exact transfer variable

The new transfer identities are

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

Hence every above-`M(n)` candidate must place its rooted-triangle surplus in the exact window

> `L_A-D_M+1 <= T`
> `              <= D_M-1+lambda(p+u)-p-E_U`.            `(TW)`

Core file:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md`.

## 4. Preserved switching / Hall / source-tuple stack

A switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

Above threshold the largest switchable zero-signed subcore and largest projective alpha class are at most

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`,

where `C_0` is the preserved scorecard cap. Put `R_hat=min(p,R_*)`.

For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x`, and `Y_x` the pairwise-distinct designated unmatched beta sources. The exact source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`    `(FDPr)`

for every `r>=3`.

The exact integrated form says that for every subset `L subseteq A` of size `N`,

> `sum_{x in L}(p-ell_x)>=Phi_r(N)`,                      `(IST)`

where

> `Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`,
>
> `C_hat_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

The preserved beta lower bounds are

> `B_beta:=sum_x ell_x >= [pu-R_hat a]_+`,                `(STL)`
>
> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

If `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` still satisfies `rho<27/14`.

## 5. New integrated total beta envelope

Applying `(IST)` to the entire A-layer gives the exact finite theorem

> `B_beta<=ap-Phi_r(a)`                                   `(ITB)`

for every `r>=3`.

Hence every above-threshold candidate satisfies the parameter-only condition

> `max(0,p(lambda+1-2p),pu-R_hat a)`
> `<=ap-Phi_r(a)`.                                        `(ITB*)`

In linear scaling

`u/p->rho>0`, `lambda/p->theta`, `A=2+rho-theta>0`,

`c=theta(1+rho)-theta^2/2`, `R=min(1,sqrt(c))`,

put

> `beta_*=max(0,theta-2,rho-A R)`.

With the continuum source profile

> `phi_r(nu;rho)=int_0^1 [nu-(kappa/r)(rho/(1-kappa))^r]_+ d kappa`,

one gets the compact integrated source-root condition

> `beta_*+phi_r(A;rho)<=A`.                               `(ISRE)`

For `r=3`, if `kappa_A` is determined by

> `A=rho^3 kappa_A/[3(1-kappa_A)^3]`,

then `(ISRE)` becomes

> `beta_*<=rho^3 kappa_A(2+kappa_A)`
> `             /[6(1-kappa_A)^2]`.                      `(ISRE3)`

This uses the whole source-deficit staircase rather than one cutoff. Preserve the older one-cutoff source-root envelope `(SRE)` as a valid comparison tool, but test `(ISRE)/(ISRE3)` before invoking more elaborate variational machinery.

Core file:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/INTEGRATED_SOURCE_ROOT_ENVELOPE.md`.

## 6. Beta-sensitive joint degree supply

For each `x in A`, let `d_x=d_U(x)` and let `w_x` be the number of chosen oriented `U--U` criticality certificates using `x` as A-side witness.

The complement-code non-neighbour lemma gives:

- if `ell_x>=2`, no U-neighbour of `x` has code `bar(c(x))`, so `w_x<=u-d_x`;
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

Thus beta traffic prices the combined `2q+s` degree supply directly; the remaining escape is localized in the zero-beta A--U reservoir `s_0`.

## 7. New source-tuple support theorem closes the distribution-free zero-beta escape

Let

> `A_+={x:ell_x>0}`, `N_+=|A_+|`.

Apply `(IST)` to `A_+`. Since

`N_+p-B_beta=sum_{x in A_+}(p-ell_x)`,

one gets the exact finite capacity

> `B_beta<=N_+p-Phi_r(N_+)`.                              `(BSP)`

Define

> `N_r(B)=min{N:Np-Phi_r(N)>=B}`.

Then

> `N_+>=N_r(B_beta)`.                                     `(NS)`

Combine this with the elementary distinct-source support floor

> `N_+>=ceil(B_beta/min(p,u))`.

Let `N_sup(B)` be the maximum of these valid lower bounds. Then

> `N_0<=a-N_sup(B_beta)`,
>
> `s_0<=u[a-N_sup(B_beta)]`.                              `(S0ST)`

Substituting into the degree-supply inequalities yields

> `E_U>=u(p+u-1)-3au+B_beta`
> `       +u N_sup(B_beta)-2a`,                           `(ST-E)`

and

> `r>=p(p-lambda)-u[a-N_sup(B_beta)]-a`.                 `(ST-R)`

Thus the zero-beta reservoir is no longer distribution-free: required beta traffic forces a minimum number of positive-beta A-witnesses, which shrinks `s_0`.

Core file:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/SOURCE_TUPLE_SUPPORT_AND_ZERO_BETA_CAPACITY.md`.

## 8. Explicit continuum beta-support floor

If

`B_beta/p^2->beta>0`, `N_+/p->nu`,

then `(BSP)` gives

> `nu-beta>=phi_r(nu;rho)`.                               `(CSPsup)`

For fixed `r`, `F_r(nu)=nu-phi_r(nu;rho)` is strictly increasing, so there is a unique support threshold `nu_r(beta;rho)>beta` satisfying

> `F_r(nu_r)=beta`.

For `r=3`, write

> `t=6beta/rho^3`,
>
> `kappa=t/(t+1+sqrt(3t+1))`,
>
> `nu_3(beta;rho)=rho^3 kappa/[3(1-kappa)^3]`.            `(NU3)`

Every limiting configuration has

> `nu>=nu_3(beta;rho)`,                                   `(CSfloor)`

and of course also `nu>=beta/min(1,rho)`.

The integrated envelope `(ISRE3)` is equivalent to the support feasibility condition

> `nu_3(beta_*;rho)<=A`.                                  `(STSUP)`

The unmatched-slack floor strengthens to

> `liminf E_U/p^2`
> `>=rho(1+rho-3A)+beta+rho nu_3(beta;rho)`.              `(CST3)`

Hence every limiting above-threshold candidate satisfies the parameter-only condition

> `rho(1+rho-3A)+beta_*+rho nu_3(beta_*;rho)<=c`.         `(STDS)`

This is a direct source-tuple-support / degree-supply constraint, independent of Hamming energy and alpha-overflow optimization.

## 9. Preserved small-unmatched consequences

Because designated beta sources are pairwise distinct,

> `ell_x<=min(p,u)`,
>
> `B_beta<=a min(p,u)`.                                   `(DSB)`

For `u<=p` this gives

> `lambda<=2p-1+floor(u^2/(p+u))`,                        `(FDRW)`

and, in the high-root-imbalance continuum branch `0<rho<1`,

> `theta<2+rho^2/(1+rho)`.                                `(SDRW)`

Above threshold the switching/distinct-source sandwich gives

> `rho>2-sqrt(3)`                                         `(RHO27)`

for `theta>2`.

The beta-sensitive U-edge theorem remains

> `q<=a u-B_beta+N_1`,                                    `(BQ)`

with continuum form `xi<=A rho-beta`; for `theta>2,rho<1` the switching form

> `xi<=A(rho+R)-rho`                                      `(SQ)`

strictly improves the older sparse-U cap.

## 10. Cylinder and enhanced-IPM machinery: preserved, supporting role

The repaired beta-cylinder theorem and all critical-witness channels remain valid. However source-tuple scarcity keeps the total distribution-free cylinder mass only `O(p)` when `u,a=O(p)`, so the old plan of forcing the complete-cylinder inequality to quadratic scale remains retired.

The continuum enhanced IPM `(CEIPM)` also remains valid. Use it only as a supporting global constraint after the parameter pair has survived `(ISRE)/(STSUP)/(STDS)`, rather than optimizing CEIPM first.

## 11. Verification at this checkpoint

Preserved audits include the exact published 12/32 `X_3` reconstruction and the earlier signed-2-lift, matched-foot, A/U-overlap, same-code, source-tuple, source-root-switching and distinct-source suites.

New audit packages in

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/`:

1. `check_rooted_residual_supply.py` / `ROOTED_RESIDUAL_SUPPLY_CHECK_SUMMARY.json`:
   - exact residual-threshold checks: 19,425;
   - transfer-identity checks: 200,000;
   - local degree-supply checks: 250,000;
   - zero-load compression checks: 250,000;
   - **719,425 checks, zero failures**.
2. `check_source_tuple_support.py` / `SOURCE_TUPLE_SUPPORT_CHECK_SUMMARY.json`:
   - 100,000 admissible finite source-support profiles;
   - 1,176 exact rational triple-source continuum identities;
   - **101,176 checks, zero failures**.

Total new promoted-audit checks this session: **820,601**, zero failures. These are audit support only; promoted statements rest on the hand proofs.

## 12. Active next move

Priorities, in order:

1. **Exploit `(ST-R)` together with the rooted-triangle transfer window `(TW)`.** The distribution-free zero-beta escape has now been replaced by the source-tuple support floor. The next target is a compact theorem showing that the resulting residual floor and the required value of `T=Q-f` cannot coexist for large cores unless a tightly classified endpoint structure occurs.
2. **Price `f=e(A)` / the transfer variable directly.** Since `Q=p(p+u-1)+q` is explicit, the remaining freedom in `T=Q-f` is internal A-edge mass. Use A-edge criticality, same-code clique payment, or complementary-code witness congestion to constrain `f` relative to the source-support partition `A_+ union A_0`.
3. **High `theta>2`, `rho>=1`.** Test `(ISRE3)`, then `(STSUP)/(STDS)`, before `(SRE)/(CEIPM)`. Do not return to a q-only attack unless a genuinely new local theorem appears.
4. **High `theta>2`, `rho<1`.** Preserve `(SDRW)/(RHO27)/(SQ)`; again test integrated source support before variational optimization.
5. **Moderate `0<theta<2`.** Preserve weighted `(QMIN)` and the residual-transfer formulation; the same integrated source-support machinery remains available whenever beta traffic is forced.
6. Keep the `u=0` full-tight finite exception protected. No unmatched-layer argument suppresses the published 12/32 graph.
7. Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

<!-- CURRENT-STATUS:END -->