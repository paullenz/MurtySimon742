# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_ONE_HOLE_FAN_CAPACITY_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime.

The conceptual spine is now

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete witness channels -> macroscopic fans -> equality stability -> one-hole type split -> global budget closure`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `p=4,b=8,a=3,u=0,lambda=4,r=0,F=empty`;
- `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`, `f=0`.

Its rooted-triangle transfer is endpoint-saturated: `Q-f=12`. At the canonical root `u=0` and `F_min=0=f`, so the live unmatched/fan machinery does not suppress it.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

## 2. Residual target and rooted-triangle transfer

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

There are `p` tight antipode pairs in `B` and an unmatched set `U`, `u=|U|`, with `b=2p+u`. Every vertex of `A union U` has a Boolean code in `{0,1}^p`.

Put `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Then

> `a=2p+u-lambda-1`,
>
> `Q=e(G[B])=p(p+u-1)+q`,
>
> `r=(p+u)(a-p)+p-s-q`,
>
> `delta=b(n-b)-m=r-f`.

With `epsilon_z=b-d(z)`, put

> `E_U=u(p+u-1)-2q-s`,
>
> `L_A=a(p+u)-s-2f`.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`D_M=ceil((4p+2u-c_lambda-2)/2)`.

Then

> `E_U+L_A=2delta+lambda(p+u)-p`,                         `(RS)`
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

Every above-`M(n)` candidate therefore satisfies

> `f>=F_min`,                                             `(FTR)`

where

> `F_min=(p-lambda)(p+u)+q-D_M+1`.                        `(FMIN)`

The separate `Q=0` / false-twin-core branch remains distinct.

## 3. Preserved switching / Hall / source-tuple stack

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x`. The exact source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`     `(FDPr)`

for every `r>=3`, with integrated deficit profile

> `sum_{x in L}(p-ell_x)>=Phi_r(|L|)`.                    `(IST)`

The beta lower bounds include

> `B_beta:=sum_x ell_x >= [pu-R_hat a]_+`,                `(STL)`
>
> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

A switchable zero-signed matched subcore of order `sigma_0>=3` forces

> `L_A>=sigma_0(sigma_0-1)`.                              `(ZS)`

If `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` still satisfies `rho<27/14`.

The repaired cylinder theorem remains a finite/equality tool rather than the generic quadratic closure mechanism.

## 4. Complete A-edge witness channels and fan gate

Every internal A-edge belongs to one of three channels: direct, matched-B witness, or A/U unique-common-neighbour witness.

For a direct A-edge fan around `x`, leaves are independent complementary-code vertices. With

`W_x=(V(G)\{v})\N(x)`

and `H_x(y)=W_x\N(y)`,

> `N(y)=W_x\H_x(y)`,
>
> `|H_x(y)|=epsilon_x+epsilon_y-(lambda+1)`.              `(DFH)`

For an A/U fan with source `x`, distinct heads `h_i` and witnesses `w_i`,

> `G[H_x,W_x]` is exactly the matching `h_iw_i`.          `(IMC)`

The global A/U fan-square capacity is

> `C^2/a + lambda C <= K_0(E_U+L_A)`,                    `(GFS)`

with `K_0=2a(a+u)/(lambda+1)+2a+u`.

With matched-B traffic `P<=sigma_0a` and `f=D+P+C`, every above-threshold candidate satisfies

> `F_min <= sigma_0a`
> `       + aR_D(T,L_A)/2`
> `       + min{aR_C(T,E_U+L_A),C_fan}`,                  `(RTF)`

where `T=a-p`.

If `H=(F_min-sigma_0a)_+`, then either some source has a direct fan of order at least `H/a`, or some source has an A/U fan of order at least `H/(2a)`.

Core package:

`project/research/post_ms/2026-09-18-a-edge-fan-rigidity-v1/`.

## 5. Fan-hole normal form and exact equality classification

For one A/U fan define

`Y_x=V(G)\({x} union N(x))`,

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|=epsilon_x+epsilon_{w_i}-(lambda+1)`,

`G_x=sum_i g_i`.

Then

> `N(w_i)={h_i} union (Y_x\({w_i} union Z_i))`.          `(EFN)`

Hence

> `2e(overline{G[W_x]})<=G_x`.                           `(EWM)`

Every A-witness has the root as a hole, so

> `|W_x intersect A|<=G_x`,
>
> `|W_x intersect U|>=(d-G_x)_+`.                        `(AWU)`

Therefore

> `q >= max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`.         `(FQLB)`

If `G_x=0` and `p>=1`, every witness lies in `U`, the witness set is a clique, and all but at most one matched head-witness edge is direct; for those clean indices `c(h_i)=c(x)`. In particular

> `q>=binom(d,2)`.                                        `(ZHQ)`

## 6. Quantitative fan stability and Hamming localization

Put

`t_i=|N(h_i) intersect (Y_x\{w_i})|`.

For a witness edge oriented from `w_i` to `w_j`, the critical certificate is either the matching head `h_j`, forcing `t_j<=g_i`, or a hole in `Z_i`; each hole certifies at most one target from a fixed source.

For integer `tau>=0`, with

`B_tau={i:g_i<=tau<t_i}`,

> `|B_tau|(|B_tau|-1)<=3G_x`.                            `(BST)`

Hence all but at most

> `floor(G_x/(tau+1))`
> ` +floor((1+sqrt(1+12G_x))/2)`                         `(EXC)`

indices satisfy `g_i,t_i<=tau`. For every such index,

> `|N(h_i) intersect N(w_i)|<=tau`,
>
> `dist_H(c(h_i),c(x))<=tau`.                            `(HLOC)`

Thus a linear fan with `G_x=o(p^2)` is an asymptotic two-cluster antipodal Hamming configuration.

## 7. Beta-sensitive fan-hole feedback

The preserved beta-sensitive U-edge theorem is

> `q<=Q_beta:=au-B_beta+N_1`,                             `(BQ)`

where `N_1=|{z in A:ell_z=1}|`; coarsely `Q_beta<=au-B_beta+a`.

Combining `(BQ)` with `(FQLB)` gives

> `G_x >= [d-floor(sqrt(2Q_beta+d))]_+`.                 `(BFH)`

If `z_0=|{i:g_i=0}|`, then

> `binom(z_0,2)<=q<=Q_beta`,                              `(ZHC1)`
>
> `z_0<=floor((1+sqrt(1+8Q_beta))/2)`.                   `(ZHC2)`

Thus if `Q_beta=o(p^2)`, a linear fan has only `o(p)` zero-hole witnesses and `G_x>=d-o(p)`.

Writing `F_0=(p-lambda)(p+u)-D_M+1`, the fan also feeds back into rooted transfer:

> `F_min >= F_0`
> ` +max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`.            `(RFF)`

On the A/U side of the fan dichotomy,

> `d >= (1/(2a))`
> ` [F_0`
> `  +max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`
> `  -sigma_0a]_+`.                                      `(AFG)`

Core follow-on:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/BETA_SENSITIVE_FAN_HOLE_AND_ROOTED_FEEDBACK.md`.

## 8. New one-hole fan classification

The cheapest surviving sparse-U perturbation is `g_i=1`.

Assume an A/U fan has

> `g_i=1` for every witness.                               `(OH)`

Write `Z_i={z_i}`.

Then the missing witness graph has maximum degree one:

> `Delta(overline{G[W_x]})<=1`;                           `(OHM)`

if `w_iw_j` is missing, then `z_i=w_j` and `z_j=w_i`. Thus the witness side is exactly a clique minus a matching.

Split witnesses by type:

`W_A=W_x intersect A`, `d_A=|W_A|`,

`W_U=W_x intersect U`, `d_U=|W_U|`.

### A-witness mechanism

If `w_i in A`, its unique hole is the root:

> `z_i=v`.                                                `(RHI)`

Hence `W_A` is a same-code clique. Among the heads matched to A-witnesses, at most one is dirty; all the others satisfy

> `N(h_i) intersect Y_x={w_i}`,                           `(ACLEAN)`
>
> `N(h_i) intersect N(w_i)=empty`,                        `(ADIR)`
>
> `c(h_i)=c(x)`.                                          `(ACODE)`

The preserved same-code weighted edge capacity gives

> `(lambda+1)binom(d_A,2)<=V_0(E_U+L_A)`,                `(AWP)`

where `V_0=a+u`. Therefore

> `d_A`
> ` <= floor((1+sqrt(1+8V_0(E_U+L_A)/(lambda+1)))/2)`.   `(DAC)`

### U-witness mechanism

The U-witness graph is clique minus a matching, so

> `q>=binom(d_U,2)-floor(d_U/2)`.                         `(OHQ)`

Combining with `(BQ)` gives

> `d_U<=floor(1+sqrt(2Q_beta+1))`.                       `(DUC)`

### One-hole capacity

Therefore every all-one-hole fan satisfies

> `d<=R_A^(1)+R_U^(1)`,                                  `(OHFC)`

with the two terms given by `(DAC)` and `(DUC)`.

Also

> `e(G[A_bar(c(x))])+q >= d^2/4-d`.                      `(OHED)`

So a linear one-hole fan necessarily creates quadratic internal edge mass either in a same-code A-clique or in U.

Finally the general stability theorem at `tau=1`, together with the exact A-witness result, gives:

- all but at most one A-witness head has exactly code `c(x)`;
- all but `O(sqrt(d))` remaining heads lie in the radius-one Hamming ball about `c(x)`;
- every witness has exactly code `bar(c(x))`.

The one-hole model is therefore a finite-radius Hamming object, not a generic large code class.

Core file:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/ONE_HOLE_FAN_CLASSIFICATION_AND_CAPACITY.md`.

## 9. Direct false-twin equality theorem

For any false-twin class `D` in a D2C graph with common open neighbourhood `W`, `d=|D|`, `w=|W|`, `d,w>=2`,

> `2e(overline{G[W]})`
> ` >= min(d,w-1)(2w+d-n)_+`.                            `(FTF)`

Applied to a zero-hole direct fan around `x`, where

`w=|W_x|=b-lambda-1+epsilon_x`,

this gives

> `e(overline{G[W_x]})`
> ` >= (1/2)min(d,w-1)`
> `      (d+2epsilon_x-lambda-2)_+`.                     `(DFQ)`

A leaf has local triangle count `e(G[W_x])`, hence

> `e(G[N(y)])`
> ` <= binom(w,2)`
> `    -(1/2)min(d,w-1)`
> `      (d+2epsilon_x-lambda-2)_+`.                     `(DTS)`

Thus a large exact direct fan forces a sparse/bipartite-like common side unless absorbed by root imbalance.

## 10. Verification at this checkpoint

Main equality/stability audit over all 21 D2C graph-atlas classes through order seven:

- 31 admissible UCN fans;
- 63 exact witness-neighbourhood checks;
- 140 threshold-stability checks;
- 4 zero-hole fan checks;
- 20 false-twin classes;
- 53 false-twin vertex-level checks;
- 20 global false-twin floor checks;
- failures: 0.

Separate one-hole audit:

- 7 generic one-hole fans;
- 14 complement-degree checks;
- 7 `tau=1` stability checks;
- 3 rooted one-hole fans;
- failures: 0.

The atlas contains no rooted A-witness one-hole instance, so the A-witness root-hole/clique theorem is supported by the hand proof rather than an empirical example. All scans are audit support only.

Package:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/`.

## 11. Live next move

Do not return to the closed mixed `{4,5}` selected-excess ladder, and do not optimize for first-proof priority on Erdős #742.

The highest-value next move is now **bounded-hole reduction / budget closure**, not further generic fan counting.

1. Insert `(OHFC)` into `(RTF)` and the rooted floor `(FMIN)` to test whether one-hole-dominant fans are already impossible in a nontrivial parameter region.
2. Extend the one-hole type split to bounded `g_i<=K`: A-witnesses always contain the root hole; U-witnesses do not. After deleting `O(Kd)` witness defects, seek a bounded union of same-code A-cliques and U near-cliques, each paid by `E_U+L_A` or `Q_beta`.
3. Use the radius-one head localization with selected/Hall/source-tuple capacity. This is now a much smaller code-capacity problem than the previous `o(p)` Hamming ball.
4. On the direct branch, combine `(DFQ)/(DTS)` with `W_x intersect B` and the rooted count `Q=e(G[B])` to turn common-side sparsity into residual defect.
5. Keep `X_3` explicit as the mandatory negative control.

The separate `Q=0` false-twin-core branch remains distinct.

<!-- CURRENT-STATUS:END -->
