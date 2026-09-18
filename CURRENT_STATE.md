# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_WHOLE_CODE_FAN_SCORECARD_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime.

The current spine is

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete witness channels -> fan geometry -> whole-code witness capacity -> complementary-pair slack concentration / direct false-twin branch`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is only the eventual comparison threshold.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 D2C graph has been reconstructed exactly and is isomorphic to the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`.

Its rooted-triangle transfer is endpoint-saturated: `Q-f=12`. At the canonical root `u=0` and `F_min=0=f`, so no positive unmatched/fan theorem below suppresses it.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

## 2. Residual defect and rooted triangles

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

There are `p` tight antipode pairs in `B` and an unmatched set `U`, `u=|U|`, so

`b=2p+u`,

`a=2p+u-lambda-1`.

Every vertex of `A union U` has a Boolean code in `{0,1}^p`.

Put

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`.

Then

> `Q=e(G[B])=p(p+u-1)+q`,
>
> `r=(p+u)(a-p)+p-s-q`,
>
> `delta=b(n-b)-m=r-f`.                                  `(DEF)`

With `epsilon_z=b-d(z)`, put

> `E_U=u(p+u-1)-2q-s`,
>
> `L_A=a(p+u)-s-2f`,
>
> `S=E_U+L_A`.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`D_M=ceil((4p+2u-c_lambda-2)/2)`.

Then the exact residual scorecard is

> `S=2delta+lambda(p+u)-p`,                               `(RS)`
>
> `D_M=b(n-b)-M(n)`,
>
> `m<=M(n) iff delta>=D_M`.                               `(RT)`

Rooted triangles are an exact transfer variable:

> `r+Q=L_A+2f`,                                           `(RQ1)`
>
> `delta+Q=L_A+f`,                                        `(RQ2)`
>
> `delta=E_U+Q-f-lambda(p+u)+p`.                          `(RQ3)`

Therefore every above-`M(n)` candidate satisfies

> `f>=F_min`,                                             `(FTR)`

where

> `F_min=(p-lambda)(p+u)+q-D_M+1`.                        `(FMIN)`

This residual/rooted-triangle formulation is the live target: prove `delta>=D_M` for all sufficiently large graphs in the triangle-containing branch.

## 3. Preserved switching / Hall / source-tuple stack

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x`. The exact source-tuple hierarchy remains

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`     `(FDPr)`

for every `r>=3`, with integrated deficit profile

> `sum_{x in L}(p-ell_x)>=Phi_r(|L|)`.                    `(IST)`

The main beta lower bounds are

> `B_beta:=sum_x ell_x >= [pu-R_hat a]_+`,                `(STL)`
>
> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

The beta-sensitive U-edge cap is

> `q<=Q_beta:=au-B_beta+N_1`,                             `(BQ)`

where `N_1=|{x in A:ell_x=1}|`.

A switchable zero-signed matched subcore of order `sigma_0>=3` forces

> `L_A>=sigma_0(sigma_0-1)`.                              `(ZS)`

For `u=O(p)` and `lambda=o(p)`, every finite limiting unmatched ratio still satisfies `u/p<27/14` asymptotically.

The repaired cylinder theorem remains a finite/equality tool rather than the generic quadratic closure mechanism.

## 4. Complete A-edge witness channels and rooted fan gate

Every internal A-edge belongs to one of three critical-witness channels:

1. direct;
2. matched-B witness;
3. A/U unique-common-neighbour witness.

Matched-B traffic satisfies the preserved `P<=sigma_0a` capacity with additional self-pricing when reuse is heavy.

For an A/U source `x`, distinct heads `h_i` and witnesses `w_i` satisfy

> `N(x) intersect N(w_i)={h_i}`,                          `(UCN)`
>
> `G[H_x,W_x]` is exactly the matching `h_iw_i`,          `(IMC)`
>
> all witnesses have the one Boolean code `bar(c(x))`.   `(WCODE)`

With

`H=(F_min-sigma_0a)_+`,

the rooted transfer dichotomy says:

> either some source has a direct fan of order at least `H/a`,
>
> or some source has an A/U fan of order at least `ceil(H/(2a))`. `(FG)`

Core A-edge package:

`project/research/post_ms/2026-09-18-a-edge-fan-rigidity-v1/`.

## 5. Exact A/U fan-hole normal form

For one A/U fan define

`Y_x=V(G)\({x} union N(x))`,

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|=epsilon_x+epsilon_{w_i}-(lambda+1)`,

`G_x=sum_i g_i`, `d=|W_x|`.

Then

> `N(w_i)={h_i} union (Y_x\({w_i} union Z_i))`.          `(EFN)`

Consequently

> `2e(overline{G[W_x]})<=G_x`.                           `(EWM)`

Every A-witness has the root as one of its holes. Zero-hole witnesses therefore lie in `U`; in the exact zero-hole model the witness side is a U-clique.

The preceding stability work also gives Hamming localization: low-hole / low-head-defect indices have heads close to `c(x)`, while every witness is exactly at the antipodal code `bar(c(x))`.

The one-hole model is completely classified: the witness side is a clique minus a matching, A-witnesses use the root as their unique hole, and the corresponding clean heads have code `c(x)`.

Preserved files:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/ONE_HOLE_FAN_CLASSIFICATION_AND_CAPACITY.md`

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/BOUNDED_HOLE_FAN_CAPACITY.md`

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/INTEGRATED_FAN_HOLE_PROFILE_AND_SCORECARD.md`.

## 6. New whole-code witness capacity

The key reassessment is that splitting A- and U-witnesses is not the correct primary capacity model: by `(WCODE)` the *entire* witness graph lies in one Boolean code class.

For code `gamma`, write

`V_gamma={z in A union U:c(z)=gamma}`,

`N_gamma=|V_gamma|`,

`S_gamma=sum_{z in V_gamma}epsilon_z`.

The preserved same-code weighted edge capacity is

> `(lambda+1)e(G[V_gamma])`
> ` <= N_bar(gamma)S_gamma+N_gamma S_bar(gamma)`.         `(SCE)`

For a fan source `x` of code `c`, define

> `E_x=floor((N_cS_bar(c)+N_bar(c)S_c)/(lambda+1))`.     `(EX)`

Then

> `e(G[W_x])<=E_x`,                                      `(EW)`
>
> `E_x<=E_0:=floor((a+u)S/(lambda+1))`.                  `(E0)`

Combining `(EW)` with `(EWM)` gives the new aggregate hole floor

> `G_x >= [d(d-1)-2E_x]_+`.                              `(WCHF)`

This prices all A-A, A-U and U-U witness edges in one shot.

## 7. New whole-fan low-hole / beta hybrid theorem

For `K>=0`, let

`I_K={i:g_i<=K}`, `N_K=|I_K|`,

and let `A_K` count A-witnesses in `I_K`.

A low-hole U-witness is adjacent to at least `d-1-K` vertices of the *whole* witness set; an A-witness is adjacent to at least `d-K`, because the root consumes one hole outside the witness set. Hence

> `N_K(d-1-K)+A_K<=2E_x`.                                `(WFHI)`

Let

> `R_U(K)=max{r:r(r-K-1)<=2Q_beta}`.                     `(RUK)`

For `K>=1`, `A_K>=(N_K-R_U(K))_+`, so

> `N_K(d-1-K)+(N_K-R_U(K))_+<=2E_x`.                    `(HBH)`

If `0<=K<=d-2`, with `t=d-1-K`, this yields the explicit cap

> `N_K<=min{`
> ` d,`
> ` floor(2E_x/t),`
> ` floor((2E_x+R_U(K))/(t+1))`
> `}`.                                                     `(CX)`

For `K=0`, A-witnesses are impossible and

> `N_0<=min{d,R_U(0),floor(2E_x/(d-1))}`.                `(CX0)`

These caps strengthen the preceding bounded-hole/integrated profile because low-hole witnesses must fit simultaneously into one same-code edge budget and the beta-sensitive U-edge budget.

Define the hybrid staircase `Psi_sharp` by taking, at every threshold, the minimum of the preceding cap and `(CX)/(CX0)`. Then

> `G_x>=Psi_sharp(d)`.                                    `(IFHP+)`

The strongest recorded local hole floor is therefore

> `Gamma_x(d)=max{0,d(d-1)-2E_x,Psi_sharp(d)}`,          `(GAM)`
>
> `G_x>=Gamma_x(d)`.                                      `(GF)`

## 8. Strengthened whole-code fan scorecard

Put

`P=p+u`, `T=P-lambda-1=a-p`.

The source-degree bound is

> `epsilon_x<=P-d`.                                       `(SRC)`

The exact hole identity then gives

`sum_i epsilon_{w_i}>=G_x+d(d-T)`.

The heads independently contribute at least `d(d-T)_+`. Since heads and witnesses are disjoint,

> `S`
> ` >= d(d-T)_+`
> `   +[Gamma_x(d)+d(d-T)]_+`.                            `(WCSC)`

There is also a compact finite consequence:

> `2d^2-(T+2)d+P <= S+2E_x`.                             `(CFC)`

The complementary-pair local version is sharper when slack is unevenly distributed:

> `d(d+lambda-epsilon_x)<=S_bar(c(x))+2E_x`,             `(PFC)`
>
> `2d^2-(T+1)d<=S_bar(c(x))+2E_x`.                       `(PFC2)`

The distribution-free substitution `E_x<=E_0` is often too generous. A conservative scan through `p<=60` found no new parameter-only closure when the *maximum* above-threshold global scorecard was substituted everywhere. This is a useful obstruction: the next gain should come from showing that a forced fan cannot concentrate enough slack in its one complementary code pair.

Core theorem and audit:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/WHOLE_CODE_FAN_CAPACITY_AND_COMPACT_SCORECARD.md`

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/WHOLE_CODE_FAN_CAPACITY_AUDIT.md`.

## 9. Direct false-twin branch

For a zero-hole direct fan, the leaves are exact false twins. For any false-twin class `D` with common open neighbourhood `W`, `d=|D|`, `w=|W|`,

> `2e(overline{G[W]})`
> ` >= min(d,w-1)(2w+d-n)_+`.                            `(FTF)`

Applied to the direct fan around `x`, this turns a large fan into common-side sparsity and a rooted local-triangle deficit.

The direct branch should now be treated as the second equality model, not mixed into the A/U capacity optimization.

## 10. Verification

Earlier graph-atlas checks over all 21 D2C classes through order seven found zero failures for the fan normal form, threshold stability, zero-hole equality, one-hole classification and false-twin floor.

The new whole-code arithmetic audit adds:

- 1,494,045 low-hole / beta hybrid profile cases;
- 2,010 uniformly bounded-hole whole-code cases;
- 10,949,820 compact quadratic implication cases;
- total: **12,445,875** exact arithmetic checks;
- failures: **0**.

These scans are audit support only. The promoted statements rest on the hand inequalities above.

## 11. Live next move

Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

The highest-value next move is now **complementary-pair slack concentration**.

1. Use `(PFC)/(PFC2)` together with the source-tuple / Hall code-distribution constraints to show that a rooted-transfer-forced A/U fan cannot place enough of the total slack into its source/witness complementary pair.
2. Aggregate `(PFC)` over distinct complementary code pairs if rooted A-edge traffic is dispersed; the pair slacks are disjoint and their total is `S`.
3. Feed the resulting fan cap back into `(FG)/(FMIN)` to force the direct-fan branch on a nontrivial parameter region.
4. On the direct branch, combine `(FTF)` with the exact rooted triangle count `Q=p(p+u-1)+q` to turn common-side sparsity into a residual-defect lower bound.
5. Keep `X_3` explicit throughout: it has `u=0`, `F_min=0` and remains a required finite exception.

The separate `Q=0` / false-twin-core branch remains distinct.

<!-- CURRENT-STATUS:END -->