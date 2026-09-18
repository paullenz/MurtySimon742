# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_NEAR_FULL_SOURCE_SWITCHING_ENVELOPE_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime. The strongest current compact route is the source-tuple beta-load envelope combined with switching/Hall structure. The repaired cylinder inequality remains valid but is not the generic scale route: the source-tuple theorem itself keeps its total left side only `O(p)` when `u,a=O(p)`.

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

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x` beta deficit. The source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`    `(FDPr)`

for every `r>=3`.

The directional Hamming/product budget and enhanced alpha-beta coercivity remain preserved. In particular:

> if `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` satisfies `rho<27/14`. `(SLRG)`

Thus any sequence with `limsup u/p>=27/14` must enter a genuinely linear root-imbalance regime.

Core preserved files include:

- `FINITE_DEFICIT_SOURCE_TUPLE_CAPACITY_AND_RATIO_GAP.md`;
- `ENHANCED_COERCIVITY_CONTINUUM_SOURCE_PROFILE_AND_CLIQUE_SLACK.md`;
- `DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md`.

## 4. Cylinder route: preserved but not generic

The repaired beta-cylinder theorem and all critical-witness channels remain valid, including matched-B collision control, A/U complementary witnesses, same-code crowding, complementary-pair localization, and the distribution-free complete-cylinder inequality `(DCF)`.

However `(FDPr)` implies, for `u,a=O(p)`,

> `sum_x 2^{-k_x}=O(1)`,

hence the entire repaired-cylinder expression

> `Gamma=sum_x ceil((p-epsilon_x)_+/2^{k_x})=O(p)`.       `(CSO)`

Therefore the old plan “force the `(DCF)` left side to quadratic scale” is retired. Use the cylinder machinery only for finite/equality/stability subcases unless a new theorem reduces its witness-capacity side to `O(p)`.

Core files:

- `project/research/post_ms/2026-09-18-large-code-pair-v1/SAME_CODE_CROWDING_COMPLEMENT_PAIR_LOCALIZATION.md`;
- `project/research/post_ms/2026-09-18-source-tuple-envelope-v1/SOURCE_TUPLE_BETA_LOAD_ENVELOPE_AND_CYLINDER_SCALE_OBSTRUCTION.md`.

## 5. Exact total beta-load envelope

Put

`B_beta=sum_x ell_x=pu-h_alpha`.

For `r>=3` and `0<=K<=p-r`, define

> `U_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

Then

> `B_beta<=a(p-K-1)+(K+1)U_r(K)`.                        `(STB)`

Above threshold put `R_hat=min(p,R_*)`. Since `h_alpha<=mu_alpha a<=R_hat a`,

> `B_beta >= [pu-R_hat a]_+`.                             `(STL)`

Hence every above-`M(n)` partial-Boolean candidate satisfies

> `[pu-R_hat a]_+`
> `<=a(p-K-1)+(K+1)U_r(K)`                               `(STS)`

for every `r>=3` and `0<=K<=p-r`.

### Continuum form

If

`u/p->rho`, `lambda/p->theta`, `A=2+rho-theta>0`,

and `K/p->kappa in (0,1)`, then for every fixed `r>=3`,

> `beta:=limsup B_beta/p^2`
> `<= A(1-kappa)+(kappa^2/r)(rho/(1-kappa))^r`.           `(CBE)`

If `C_0/p^2->c>=0`, then `(STL)` gives

> `beta >= [rho-A min(1,sqrt(c))]_+`.                    `(CBL)`

For the live above-threshold linear scaling,

> `c=theta(1+rho)-theta^2/2`.

The root-imbalance floor, valid already before switching, is

> `beta>=(theta-2)_+`.                                    `(RBF)`

## 6. Source-root envelope: quantitative replacement for the old strict wedge

Combining `(CBE)` with `(RBF)` eliminates beta load. For every `theta>2`, fixed `r>=3` and `0<kappa<1`,

> `theta <= Theta_r(kappa;rho)`                           `(SRE)`

with

> `Theta_r(kappa;rho)`
> `=[4+rho-(2+rho)kappa`
> ` +(kappa^2/r)(rho/(1-kappa))^r]/(2-kappa)`.

Thus

> `theta<=inf_{0<kappa<1}Theta_r(kappa;rho)`.

For `r=3`, the derivative at `kappa=0` is `-rho/4`, so this is strictly stronger for every fixed `rho>0` than the old endpoint line

> `theta<2+rho/2`.                                        `(SBW)`

At `rho=2` the exact optimizing `kappa` is the root in `(0,1)` of

`3kappa^4-4kappa^3+14kappa^2-28kappa+3=0`,

and gives `theta<=2.965973...`; the tiny decimal improvement is not the main point and the cleaner rational cap `3227/1088` remains useful exposition.

## 7. New switching-source exclusion in the small-rho high-imbalance branch

When `c<1`, `(CBL)` and `(CBE)` give the parameter-only switching-source sandwich

> `rho-A sqrt(c)`
> `<=A(1-kappa)+(kappa^2/r)(rho/(1-kappa))^r`.            `(SSS)`

Two clean consequences are now proved.

### Small-unmatched exclusion

Every above-threshold linear-scale survivor with `theta>2` satisfies

> `rho>4/25`.                                             `(RHO16)`

Proof uses `r=3`, `kappa=13/20`; at the hostile endpoint `rho=4/25, theta=2`, the required strict margin is certified exactly by

> `(291161/514500)^2-8/25`
> `=67447921/264710250000>0`.

Monotonicity makes the contradiction stronger as `theta` increases.

### Two-fifths wedge

For every above-threshold sequence with `0<rho<=1/2` and `theta>2`,

> `theta<2+(2/5)rho`.                                     `(2/5W)`

Thus the surviving slice is

> `4/25<rho<=1/2`,
> `2<theta<2+(2/5)rho`.

The proof uses `r=3`, `kappa=2/5`; the lower-minus-upper margin is decreasing in `rho` and remains positive at `rho=1/2`, where

> `(1171/2025)^2-198/625=72163/4100625>0`.

Core file:

`project/research/post_ms/2026-09-18-source-root-switching-v1/SOURCE_ROOT_SWITCHING_ENVELOPE_AND_WEIGHTED_U_EDGE_CAPACITY.md`.

## 8. New weighted criticality theorem for all U--U edges

For a code `c`, put

`n_c=|A_c|`, `t_c=|U_c|`,

`L_c=sum_{x in A_c}epsilon_x`, `E_c=sum_{y in U_c}epsilon_y`.

Every edge of `G[U]` lies in a root triangle. Choosing one triangle-edge criticality orientation for each such edge gives an A-side complementary-code witness and the unique-common-neighbour slack payment. The resulting exact inequality is

> `(lambda+1)q`
> `<=sum_c [n_bar(c) E_c+t_c L_bar(c)]`.                 `(WU)`

Hence, with `mu_UA=max_c max(n_c,t_c)`,

> `(lambda+1)q<=mu_UA(E_U+L_A)`.                         `(WU2)`

Above threshold,

> `q<=mu_UA C_0/(lambda+1)`.                              `(WU3)`

In a linear-scale above-threshold sequence with `theta>0`, the complementary-pair mass bound gives `mu_UA/p<=A`, hence

> `xi:=q/p^2<=A c/theta=A(rho+A)/2`.                     `(WU4)`

Together with `(SU)`,

> `xi<=A min(RA,(rho+A)/2)`,                              `(QMIN)`

where `R=min(1,sqrt(c))`.

Strategic scope is important:

- for `theta<2`, `A>rho`, so `(WU4)` can improve the old `A^2` sparse-U bound;
- for `theta>2`, `A<rho`, so `(WU4)` is weaker than the old sparse-U bound and does **not** remove the high-imbalance `q` bottleneck.

This is an exact structural theorem, not a numerical heuristic.

## 9. Continuum enhanced IPM and current obstruction

The continuum enhanced IPM `(CEIPM)` remains a valid global necessary condition. It combines directional Hamming energy, beta-deficit/U-degree product, alpha-beta fibre coercivity, alpha overflow, the continuum source-deficit profile, sparse-U control and the scorecard.

The advertised `CBE/CBL -> CEIPM` coupling was reassessed this run. The beta variable can now be bounded from both sides, but in the high-`theta` branch the present distribution-free `q` allowance remains too large for the enhanced IPM to exploit those bounds sharply. The new `(WU)` theorem confirms rather than removes that obstruction: it improves `q` mainly for `theta<2`, while `(SU)` remains better for `theta>2`.

Therefore do **not** spend the next run merely decimal-optimizing `(CEIPM)` in the high-`theta` region. The higher-value target is a beta-sensitive/source-tuple-sensitive bound on `q`, or directly on the combined degree supply `2q+s`.

For `0<theta<2`, however, `(QMIN)` is genuinely stronger and should be inserted into `(CEIPM)`.

## 10. Verification at this checkpoint

Preserved audits include the exact published 12/32 `X_3` reconstruction and the earlier signed-2-lift, matched-foot, A/U-overlap, same-code and source-tuple regression suites.

New audit package:

`project/research/post_ms/2026-09-18-source-root-switching-v1/check_source_root_switching.py`

with frozen summary

`SOURCE_ROOT_SWITCHING_CHECK_SUMMARY.json`:

- small-rho switching-source grid: 100,000 checks;
- two-fifths wedge grid: 100,500 checks;
- source-root strict-envelope grid: 1,000 checks;
- all 21 D2C graph-atlas classes through order seven; 14 rooted triangle-edge kernel checks at maximum-degree roots;
- **201,514 total checks, zero failures**.

The two proof endpoints are also certified by exact rational positive margins. These checks are audit support only; promoted statements rest on the hand proofs.

## 11. Active next move

Priorities, in order:

1. **High `theta>2`: derive a beta/source-tuple-sensitive upper bound for `q` or `2q+s`.** The source-root/switching envelope now controls beta traffic sharply, but the independent sparse-U cap is the main information bottleneck.
2. **Moderate `0<theta<2`: feed `(QMIN)` into `(CEIPM)`** and seek a hand-certifiable excluded region, not merely a numerical envelope.
3. Preserve `(SRE)/(SSS)` as the compact externally reviewable bridge: they eliminate beta and all Hamming/code-distribution variables before any variational optimization.
4. Keep the `u=0` full-tight finite exception protected. No argument in Sections 5--9 applies to the published 12/32 graph.
5. Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

<!-- CURRENT-STATUS:END -->
