# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_GLOBAL_A_EDGE_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime. The conceptual spine is now

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete A-edge witness-channel accounting -> scorecard payment or macroscopic Boolean code class`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `p=4,b=8,a=3,u=0,lambda=4,r=0,F=empty`.

For this graph

`Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`, `f=0`.

Its rooted-triangle transfer is endpoint-saturated: `Q-f=12`. The new A-edge floor below gives `F_min=0=f`, so the negative control remains explicitly permitted.

Certification file:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

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

Let

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

The exact identities are

> `r+Q=L_A+2f`,                                           `(RQ1)`
>
> `delta+Q=L_A+f`,                                        `(RQ2)`
>
> `delta=E_U+Q-f-lambda(p+u)+p`.                          `(RQ3)`

With `T:=Q-f`,

> `L_A=delta+T`,
>
> `E_U=delta+lambda(p+u)-p-T`.                            `(TR)`

Hence every above-`M(n)` candidate must satisfy

> `L_A-D_M+1 <= T`
> `              <= D_M-1+lambda(p+u)-p-E_U`.            `(TW)`

The transfer identity now has a direct consequence for `f`. Since `E_U>=0`, every above-threshold candidate satisfies

> `f>=F_min`,                                             `(FTR)`

where

> `F_min:=Q-lambda(p+u)+p-D_M+1`
> `      =(p-lambda)(p+u)+q-D_M+1`.                       `(FMIN)`

Thus too-small residual defect forces internal A-edge mass directly.

Core files:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md`

and

`project/research/post_ms/2026-09-18-global-a-edge-transfer-v1/GLOBAL_A_EDGE_TRANSFER_AND_WITNESS_CHANNELS.md`.

## 4. Preserved switching / Hall / source-tuple stack

A switchable zero-signed matched subcore of order `sigma_0>=3` forces

> `L_A>=sigma_0(sigma_0-1)`.                              `(ZS)`

Above threshold the largest switchable zero-signed subcore and largest projective alpha class are controlled by the scorecard radius

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`,

with `R_hat=min(p,R_*)`.

For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x`, and `Y_x` the pairwise-distinct designated unmatched beta sources. The exact source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`    `(FDPr)`

for every `r>=3`.

For every subset `L subseteq A` of size `N`,

> `sum_{x in L}(p-ell_x)>=Phi_r(N)`,                      `(IST)`

where

> `Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`,
>
> `C_hat_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

Preserved beta lower bounds are

> `B_beta:=sum_x ell_x >= [pu-R_hat a]_+`,                `(STL)`
>
> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

Applying `(IST)` to all of `A` gives

> `B_beta<=ap-Phi_r(a)`.                                  `(ITB)`

Applying it only to `A_+={x:ell_x>0}`, `N_+=|A_+|`, gives

> `B_beta<=N_+p-Phi_r(N_+)`.                              `(BSP)`

Thus beta traffic forces a minimum support population `N_sup(B_beta)` and shrinks the zero-beta cross-edge reservoir.

If `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` still satisfies `rho<27/14`.

## 5. Integrated source support and beta-sensitive degree supply

For each `x in A`, let `d_x=d_U(x)` and let `w_x` count chosen oriented `U--U` certificates using `x` as A-side witness.

The complement-code non-neighbour lemma gives:

- if `ell_x>=2`, `w_x<=u-d_x`;
- if `ell_x=1`, `w_x<=u-d_x+1`;
- if `ell_x=0`, use `w_x<=u`.

Let

`A_0={x:ell_x=0}`, `N_0=|A_0|`, `N_1=|{x:ell_x=1}|`,

`s_0=sum_{x in A_0}d_U(x)`.

Then

> `q+s<=a u+s_0+N_1`,                                    `(QS)`
>
> `2q+s<=2a u-B_beta+s_0+2N_1`.                          `(2QS)`

Consequently

> `r>=p(p-lambda)-s_0-N_1`,                              `(RLOW)`
>
> `E_U>=u(p+u-1)-2a u+B_beta-s_0-2N_1`.                 `(ELOW)`

The integrated source support gives

> `s_0<=u[a-N_sup(B_beta)]`,                              `(S0ST)`

hence

> `E_U>=u(p+u-1)-3au+B_beta`
> `       +u N_sup(B_beta)-2a`,                           `(ST-E)`

and

> `r>=p(p-lambda)-u[a-N_sup(B_beta)]-a`.                 `(ST-R)`

In continuum notation `B_beta/p^2->beta`, `N_+/p->nu`, `u/p->rho`,

> `nu-beta>=phi_r(nu;rho)`.                               `(CSPsup)`

For `r=3`, the explicit support floor `nu_3(beta;rho)` remains available, and the parameter-only degree-supply condition is

> `rho(1+rho-3A)+beta_*+rho nu_3(beta_*;rho)<=c`.         `(STDS)`

The integrated whole-A source-root envelope `(ISRE)/(ISRE3)` remains the first global filter before CEIPM.

## 6. New direct A-edge theorem

For a Boolean code `c`, write

- `A_c={x in A:c(x)=c}`, `n_c=|A_c|`;
- `V_c=(A union U)_c`, `N_c=|V_c|`;
- `L_c=sum_{x in A_c}epsilon_x`;
- `S_c=sum_{z in V_c}epsilon_z`.

Call `xy in E(G[A])` **direct** when `N(x) intersect N(y)=empty`.

A direct A-edge must join complementary Boolean codes, and its endpoint slacks satisfy

> `epsilon_x+epsilon_y>=lambda+1`                         `(DES)`

for `lambda>=0`.

If `D` is the number of direct A-edges, then

> `D<=min{ 1/2 sum_c n_c n_bar(c),`
> `        (1/(lambda+1)) sum_c n_bar(c)L_c }`.           `(DAE)`

Thus the zero-common-neighbour criticality channel is simultaneously complementary-code limited and slack limited.

## 7. Complete global A-edge witness-channel theorem

Every non-direct A-edge admits an oriented criticality certificate

> `N(z) intersect N(w)={h}`

with `z` an A-endpoint source, `h` the other endpoint, and external witness `w` either a matched tight-core endpoint or a vertex of `A union U`.

The matched-B channel is bounded by the preserved `gamma(w)` collision theorem:

> `M_P<=sigma_0 a`.                                       `(ABC-P)`

For the A/U channel, if `C_c` is the number of chosen certificates with A-source code `c`, then fixed source-witness pairs cannot be reused for different heads and the unique-common-neighbour hole identity gives

> `C_c<=min{n_c N_bar(c),`
> `          [N_bar(c)L_c+n_cS_bar(c)]/(lambda+1)}`.       `(ABC)`

Therefore, in the near-full partial-Boolean branch with `lambda>=0`,

> `f <= sigma_0 a`
> `   + min{ 1/2 sum_c n_c n_bar(c),`
> `          (1/(lambda+1)) sum_c n_bar(c)L_c }`
> `   + sum_c min{ n_c N_bar(c),`
> `                [N_bar(c)L_c+n_cS_bar(c)]/(lambda+1) }`. `(AFE)`

This accounts for all internal A-edge criticality channels:

1. direct / no common neighbour;
2. matched-B witness;
3. A/U witness.

No cylinder assumption is used.

With

`mu_A=max_c n_c`, `mu_V=max_c N_c`, `S=E_U+L_A`,

a coarse form is

> `f<=sigma_0 a`
> `  +[mu_A E_U+(mu_V+2mu_A)L_A]/(lambda+1)`,             `(AFEc)`

and hence

> `f<=sigma_0 a+3mu_V S/(lambda+1)`.                     `(AFE3)`

The constant `3` is deliberately crude; use `(AFE)` when code-resolved data are available.

## 8. Rooted-transfer / macroscopic-code dichotomy

Combining `(FTR)` with `(AFE3)` gives

> `F_min<=sigma_0 a+3mu_V S/(lambda+1)`.                 `(RTC)`

Whenever `F_min>sigma_0a`,

> `mu_V >= (lambda+1)(F_min-sigma_0a)/(3S)`.             `(MC)`

Thus a large rooted-transfer demand must be absorbed either by a large switchable zero-signed core, which already pays through `(ZS)`, or by a large Boolean code class in `A union U`.

A useful asymptotic corollary is now available.

If

`u/p->rho>0`, `u=O(p)`, `lambda=o(p)`, `lambda>=0`,

and the sequence remains above `M(n)`, then

- `F_min=Theta(p^2)`;
- `S=o(p^2)`;
- `(ZS)` gives `sigma_0=o(p)`, hence `sigma_0a=o(p^2)`;
- the exact scorecard cap gives `S/(lambda+1)=O(p)`.

Therefore

> `mu_V=Omega(p)`.                                        `(MACRO)`

So every surviving sublinear-root-imbalance, linearly-unmatched sequence contains a macroscopic Boolean code class in `A union U`. This is now the principal structural object to attack.

Core file:

`project/research/post_ms/2026-09-18-global-a-edge-transfer-v1/GLOBAL_A_EDGE_TRANSFER_AND_WITNESS_CHANNELS.md`.

## 9. Preserved small-unmatched and variational consequences

Because designated beta sources are pairwise distinct,

> `ell_x<=min(p,u)`,
>
> `B_beta<=a min(p,u)`.                                   `(DSB)`

For `u<=p`,

> `lambda<=2p-1+floor(u^2/(p+u))`.                       `(FDRW)`

For `0<rho<1`, high root imbalance satisfies

> `theta<2+rho^2/(1+rho)`,                               `(SDRW)`

and above threshold the switching/distinct-source sandwich gives

> `rho>2-sqrt(3)`                                         `(RHO27)`

when `theta>2`.

The beta-sensitive U-edge theorem

> `q<=a u-B_beta+N_1`                                     `(BQ)`

and the enhanced-IPM / alpha-overflow machinery remain valid supporting constraints. Test `(ISRE)/(STSUP)/(STDS)` and now `(FTR)/(AFE)/(RTC)` before returning to CEIPM optimization.

The repaired beta-cylinder theorem also remains valid, but its distribution-free total mass is only `O(p)` when `u,a=O(p)`, so it is not the generic quadratic closure mechanism.

## 10. Verification at this checkpoint

Preserved audits include the exact published 12/32 `X_3` reconstruction and the earlier signed-2-lift, matched-foot, A/U-overlap, same-code, source-tuple, source-root-switching, residual-transfer and source-support suites.

New package:

`project/research/post_ms/2026-09-18-global-a-edge-transfer-v1/`

contains

1. `GLOBAL_A_EDGE_TRANSFER_AND_WITNESS_CHANNELS.md` — hand theorem package;
2. `check_a_edge_criticality_channels.py` — independent graph-atlas trichotomy audit;
3. `A_EDGE_CRITICALITY_AUDIT_SUMMARY.json` — results.

Graph-atlas audit through order seven:

- 21 D2C isomorphism classes;
- 156 edges checked;
- 127 direct edges;
- 29 non-direct externally certified edges;
- 47 total witness orientations;
- failures: 0.

This audit supports only the generic critical-edge trichotomy. It does not prove the Boolean-code injections or `(AFE)`; promoted statements rest on the hand proofs.

## 11. Active next move

Priorities, in order:

1. **Attack the macroscopic Boolean code class forced by `(MACRO)/(MC)`.** Split into a dense same-code A-subgraph and a sparse one. In the dense case, combine same-code criticality/clique payment with `(AFE)` to force scorecard. In the sparse case, use the required A-edge mass `(FTR)` to force complementary-code congestion elsewhere.
2. **Exploit the exact code-resolved `(AFE)`, not only `(AFE3)`.** The coarse factor `3mu_VS/(lambda+1)` deliberately throws away complement-pair structure. A weighted complement-pair inequality may turn a macroscopic class directly into `L_A` or `E_U` payment.
3. **Combine `(ST-R)` with `(FTR)/(AFE)`.** Source-tuple support already controls the zero-beta reservoir and gives a residual floor; the new A-edge theorem independently controls the transfer variable. Their overlap is the most promising compact route to contradiction.
4. **High `theta>2`, rho>=1.** Test `(ISRE3)`, `(STSUP)/(STDS)`, then the new rooted-transfer/A-edge constraints before CEIPM.
5. **High `theta>2`, rho<1.** Preserve `(SDRW)/(RHO27)/(BQ)` and again test source support plus A-edge transfer before variational optimization.
6. Keep the `u=0` full-tight finite exception protected. No unmatched-layer argument suppresses the published 12/32 graph, and `(FTR)` is exactly tight there with `f=0`.
7. Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

<!-- CURRENT-STATUS:END -->
