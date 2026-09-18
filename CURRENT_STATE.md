# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_DISTINCT_SOURCE_Q_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime. The strongest compact route now combines source-tuple beta-load control, switching/Hall structure, and the new distinct-source beta ceiling / beta-sensitive U-edge theorem.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `k=4,b=8,a=3,r=0,F=empty`.

See `project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`. It has `u=0`, so every unmatched-layer theorem below leaves it untouched.

## 2. Near-full normal form, rooted triangles, residual defect, and scorecard

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
> `delta=b(n-b)-m=(p+u)(a-p)+p-s-q-f`.

For `epsilon_z=b-d(z)`, put

> `E_U=sum_{y in U}epsilon_y=u(p+u-1)-2q-s`,
>
> `L_A=sum_{x in A}epsilon_x=a(p+u)-s-2f`.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`.

Then

> `m<=M(n)` iff `E_U+L_A>=S_req`,

and parity gives

> `m>M(n) ==> E_U+L_A<=C_0:=S_req-2`.                    `(GS-A)`

At `lambda=-1`, `C_0=2p+u-4`.

The separate `Q=0` / false-twin-core branch remains open and must not be conflated with this triangle-containing partial-Boolean branch.

## 3. Preserved switching / Hall / source-tuple stack

A switchable zero-signed matched subcore of order `s_0>=3` forces

> `L_A>=s_0(s_0-1)`.                                     `(ZS)`

If `sigma_0` is the largest zero-signed subcore obtainable after switching, then above threshold

> `sigma_0(sigma_0-1)<=C_0`.                              `(SD)`

With

`R_*=max(2,floor((1+sqrt(1+4C_0))/2))`,

one has `sigma_0<=R_*`, unmatched-row cover lower bounds, and `mu_alpha<=R_*` for the largest projective alpha / switching true-twin class.

Selected/Hall consequences include

> `nu_c t_c<=a`,
>
> `p(t_c+t_bar c)<=(mu_alpha+1)a`,
>
> `min(h,p)a>=pu-mu_alpha a`.

Selected orientation inside `U` gives

> `e(G[S])<=sum_{y in S}n_{bar c(y)}` for every `S subseteq U`,

hence

> `q<=a floor((mu_alpha+1)a/p)<=(mu_alpha+1)a^2/p`.       `(SU)`

For `x in A`, let `ell_x` be beta load, `k_x=p-ell_x`, and `Y_x` the pairwise-distinct designated unmatched beta sources. The exact source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`    `(FDPr)`

for every `r>=3`.

The directional Hamming/product budget and enhanced alpha-beta coercivity remain preserved. In particular:

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`. `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

## 4. Cylinder route: preserved but not generic

The repaired beta-cylinder theorem and all critical-witness channels remain valid, including matched-B collision control, A/U complementary witnesses, same-code crowding, complementary-pair localization, and the distribution-free complete-cylinder inequality `(DCF)`.

However `(FDPr)` implies, for `u,a=O(p)`,

> `sum_x 2^{-k_x}=O(1)`,

hence

> `Gamma=sum_x ceil((p-epsilon_x)_+/2^{k_x})=O(p)`.       `(CSO)`

Therefore the old plan “force the `(DCF)` left side to quadratic scale” remains retired. Use the cylinder machinery for finite/equality/stability subcases unless a new theorem reduces its witness-capacity side to `O(p)`.

## 5. Total beta-load envelope and source-root envelope

Put

`B_beta=sum_x ell_x=pu-h_alpha`.

For `r>=3` and `0<=K<=p-r`, define

> `U_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

Then

> `B_beta<=a(p-K-1)+(K+1)U_r(K)`.                        `(STB)`

Above threshold put `R_hat=min(p,R_*)`. Since `h_alpha<=mu_alpha a<=R_hat a`,

> `B_beta >= [pu-R_hat a]_+`.                             `(STL)`

Hence every above-`M(n)` candidate satisfies the parameter-only sandwich

> `[pu-R_hat a]_+`
> `<=a(p-K-1)+(K+1)U_r(K)`                               `(STS)`

for every `r>=3`, `0<=K<=p-r`.

In linear scaling

`u/p->rho`, `lambda/p->theta`, `A=2+rho-theta>0`,

`c=C_0/p^2 -> theta(1+rho)-theta^2/2`,

and `R=min(1,sqrt(c))`, one has

> `beta:=limsup B_beta/p^2`
> `<= A(1-kappa)+(kappa^2/r)(rho/(1-kappa))^r`            `(CBE)`

and

> `beta >= [rho-A R]_+`.                                  `(CBL)`

The root floor gives independently

> `beta >= (theta-2)_+`.                                  `(RBF)`

Combining `(CBE)` and `(RBF)` yields the preserved source-root envelope `(SRE)`, which remains the main compact high-`rho` tool.

## 6. New exact distinct-source beta ceiling

Because `Y_x subseteq U` and the designated beta sources are pairwise distinct,

> `ell_x<=min(p,u)`.

Therefore

> `B_beta<=a min(p,u)`.                                   `(DSB)`

In particular, for `u<=p`,

> `B_beta<=a u`.                                          `(DSB-u)`

This simple ceiling is structurally much stronger than `B_beta<=ap` in the small-unmatched high-root-imbalance branch.

Combining `(DSB-u)` with the exact root-imbalance beta floor gives the finite theorem

> `lambda<=2p-1+floor(u^2/(p+u))`                         `(FDRW)`

for every selected partial-Boolean configuration with `u<=p`; no above-threshold assumption is needed.

In continuum form, for `0<rho<1`,

> `theta<=2+rho^2/(1+rho)`.                               `(DRW)`

The source-tuple hierarchy shows that the distinct-source ceiling cannot be asymptotically saturated by a linear A-population. Consequently, if `theta>2`,

> `theta<2+rho^2/(1+rho)`.                                `(SDRW)`

For `rho<=1/2`, this implies the clean strict one-third wedge

> `theta<2+rho/3`.                                        `(1/3W)`

This supersedes the previous two-fifths wedge.

Core file:

`project/research/post_ms/2026-09-18-distinct-source-q-v1/DISTINCT_SOURCE_BETA_CEILING_AND_Q_CAPACITY.md`.

## 7. New switching/distinct-source sandwich and small-rho exclusion

Combining `(DSB-u)` with the switching beta lower bound `(STL)` gives the exact finite necessary condition

> `pu<=a(u+R_hat)`                                        `(DSS-f)`

for every above-threshold candidate with `u<=p`.

In continuum form,

> `A(rho+R)>=rho`.                                        `(DSS)`

For `0<rho<1`, `theta>2`, source-tuple non-saturation makes this strict:

> `A(rho+R)>rho`.                                         `(SDSS)`

This yields the new exact small-unmatched exclusion

> `rho>2-sqrt(3)=0.2679491924...`                         `(RHO27)`

for every above-threshold linear-scale survivor with `theta>2`.

The old `rho>4/25` result is therefore superseded. Together with `(1/3W)`, the clean surviving small-rho slice is now

> `2-sqrt(3)<rho<=1/2`,
>
> `2<theta<2+rho/3`,

with the stronger implicit curve `(SDSS)` available when needed.

## 8. New beta-sensitive U-edge theorem

Choose one preserved A-side critical witness for each oriented edge of `G[U]`. If `w_x` is the number of chosen U-edge certificates using `x in A`, then all their sources have code `bar(c(x))`, and a fixed source-witness pair certifies at most one edge.

The beta-target code rule implies that for `ell_x>=2`, the complementary U-code class is disjoint from `Y_x`; for `ell_x=1`, it can meet `Y_x` in at most one vertex. Thus, with

`N_1=|{x:ell_x=1}|`,

> `q<=a u-B_beta+N_1`
> ` <=a u-B_beta+a`.                                     `(BQ)`

This is exact and finite.

In continuum form,

> `xi:=q/p^2<=A rho-beta`.                                `(CBQ)`

Combining with switching gives, in the high-root-imbalance branch,

> `xi<=A(rho+R)-rho`.                                     `(SQ)`

The old sparse-U continuum cap is `xi<=R A^2`. Their difference factors as

> `[A(rho+R)-rho]-R A^2=(1-A)(AR-rho)`.

Hence whenever `theta>2` and `A<1`, `(SQ)` is strictly stronger than the old distribution-free sparse-U cap. In particular this holds throughout `0<rho<1`, because then `A<rho<1`.

This removes the previously recorded high-`theta` q-information bottleneck on the entire small-unmatched branch. Near the strict switching boundary `(SDSS)`, the permitted `q/p^2` is forced to zero.

## 9. Preserved weighted U-edge theorem

The independent weighted criticality theorem remains useful:

> `(lambda+1)q`
> `<=sum_c [n_bar(c) E_c+t_c L_bar(c)]`.                 `(WU)`

Hence

> `(lambda+1)q<=mu_UA(E_U+L_A)`                          `(WU2)`

and, above threshold,

> `q<=mu_UA C_0/(lambda+1)`.                              `(WU3)`

Its continuum form `(WU4)/(QMIN)` remains especially useful for `0<theta<2`. For `theta>2`, `rho<1`, the new beta-sensitive `(SQ)` is the stronger route.

## 10. Continuum enhanced IPM and revised obstruction

The continuum enhanced IPM `(CEIPM)` remains a valid global necessary condition. It combines directional Hamming energy, beta-deficit/U-degree product, alpha-beta fibre coercivity, alpha overflow, source-deficit profiles, U-edge supply and the scorecard.

The previous checkpoint identified the high-`theta` distribution-free `q` cap as the main obstruction. That obstruction is now removed for `theta>2`, `rho<1`: use

> `xi<=A(rho+R)-rho`

instead of `xi<=R A^2` there.

For `rho>=1`, the distinct-source ceiling degenerates to `B_beta<=ap`; `(SRE)/(CBE)` remain the stronger compact beta tools, and a beta-sensitive `q` theorem beyond the `u<p` ceiling remains desirable.

For `0<theta<2`, preserve `(QMIN)` as the preferred q cap and feed it into `(CEIPM)`.

## 11. Verification at this checkpoint

Preserved audits include the exact published 12/32 `X_3` reconstruction and the earlier signed-2-lift, matched-foot, A/U-overlap, same-code, source-tuple and source-root switching suites.

New audit package:

`project/research/post_ms/2026-09-18-distinct-source-q-v1/check_distinct_source_q.py`

with frozen summary

`DISTINCT_SOURCE_Q_CHECK_SUMMARY.json`:

- local beta/complement code checks through `p=8`: 24,604;
- finite root-wedge checks: 32,939;
- finite switching-compatible parameter checks: 376,817;
- finite switching-rejected parameter cases recorded: 56,252;
- small-rho boundary grid checks: 50,000;
- beta-sensitive q versus sparse-U comparisons: 40,000;
- **580,612 total checks, zero failures**.

These checks are audit support only; promoted statements rest on the hand proofs.

## 12. Active next move

Priorities, in order:

1. **High `theta>2`, `rho<1`: feed `(SQ)` into `(CEIPM)`** and seek a short hand-certifiable exclusion region or scorecard contradiction. Do not revert to the obsolete distribution-free `q` cap on this slice.
2. **High `theta>2`, `rho>=1`: seek a source-tuple-sensitive analogue of `(BQ)` that remains nontrivial once `u>=p`, or a direct bound on `2q+s` using beta-deficit/source geometry.
3. **Moderate `0<theta<2`: feed `(QMIN)` into `(CEIPM)`** and seek a hand-certifiable excluded region rather than decimal optimization.
4. Preserve `(DSS-f)/(SDSS)` and `(BQ)/(SQ)` as compact externally reviewable bridges: they eliminate most code-distribution variables before variational optimization.
5. Keep the `u=0` full-tight finite exception protected. No argument in Sections 6--10 suppresses the published 12/32 graph.
6. Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

<!-- CURRENT-STATUS:END -->