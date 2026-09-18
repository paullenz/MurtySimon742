# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_A_EDGE_FAN_RIGIDITY_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime.

The conceptual spine is now

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete A-edge witness channels -> macroscopic fan geometry -> stability/classification`.

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

Its rooted-triangle transfer is endpoint-saturated: `Q-f=12`. The current A-edge floor gives `F_min=0=f`, so every new unmatched/A-edge theorem remains compatible with the mandatory negative control.

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

With `T_Q:=Q-f`,

> `L_A=delta+T_Q`,
>
> `E_U=delta+lambda(p+u)-p-T_Q`.                          `(TR)`

Every above-`M(n)` candidate therefore satisfies the direct A-edge floor

> `f>=F_min`,                                             `(FTR)`

where

> `F_min:=Q-lambda(p+u)+p-D_M+1`
> `      =(p-lambda)(p+u)+q-D_M+1`.                       `(FMIN)`

This is the live bridge from rooted triangles to internal A-edge structure.

Core file:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md`.

## 4. Preserved switching / Hall / source-tuple stack

A switchable zero-signed matched subcore of order `sigma_0>=3` forces

> `L_A>=sigma_0(sigma_0-1)`.                              `(ZS)`

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x`. The exact source-tuple hierarchy is

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`     `(FDPr)`

for every `r>=3`.

For every subset `L subseteq A` of size `N`,

> `sum_{x in L}(p-ell_x)>=Phi_r(N)`.                      `(IST)`

The preserved beta lower bounds include

> `B_beta:=sum_x ell_x >= [pu-R_hat a]_+`,                `(STL)`
>
> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF)`

Applying `(IST)` to all of `A` and to `A_+={x:ell_x>0}` gives the integrated total-load and support restrictions used in `(ISRE)/(STDS)`.

If `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` still satisfies

> `rho<27/14`.

The repaired cylinder theorem remains valid, but its generic total lower-bound mass is only `O(p)` for `u,a=O(p)`, so it is not the main quadratic closure mechanism.

## 5. Complete global A-edge witness-channel theorem

For a Boolean code `c`, write

- `A_c={x in A:c(x)=c}`, `n_c=|A_c|`;
- `V_c=(A union U)_c`, `N_c=|V_c|`;
- `L_c=sum_{x in A_c}epsilon_x`;
- `S_c=sum_{z in V_c}epsilon_z`.

Every internal A-edge belongs to one of three criticality channels:

1. **direct:** `N(x) intersect N(y)=empty`;
2. **matched-B witness:** an external tight-core endpoint certifies the edge;
3. **A/U witness:** after orienting the edge from an A-source `z`, a witness `w in A union U` satisfies `N(z) intersect N(w)={head}`.

The exact complete upper bound is

> `f <= sigma_0 a`
> `   + min{ 1/2 sum_c n_c n_bar(c),`
> `          (1/(lambda+1)) sum_c n_bar(c)L_c }`
> `   + sum_c min{ n_c N_bar(c),`
> `                [N_bar(c)L_c+n_cS_bar(c)]/(lambda+1) }`. `(AFE)`

A coarse consequence is

> `f<=sigma_0 a+3mu_V(E_U+L_A)/(lambda+1)`,              `(AFE3)`

where `mu_V=max_c N_c`.

Combining `(FTR)` and `(AFE3)` forces a macroscopic Boolean class in every surviving sublinear-root-imbalance, linearly-unmatched sequence. That conclusion is now refined further by the fan theorems below.

Core file:

`project/research/post_ms/2026-09-18-global-a-edge-transfer-v1/GLOBAL_A_EDGE_TRANSFER_AND_WITNESS_CHANNELS.md`.

## 6. New direct-fan rigidity

Fix `x in A` and let `D_x` be its direct A-neighbours, `d_x=|D_x|`.

All vertices of `D_x` have code `bar(c(x))`, and:

> `D_x` is independent.                                  `(DFI)`

Put

`W_x=(V(G)\{v})\N(x)`.

For `y in D_x`, let `H_x(y)=W_x\N(y)`. Then

> `N(y)=W_x\H_x(y)`,
>
> `|H_x(y)|=epsilon_x+epsilon_y-(lambda+1)`.              `(DFH)`

Hence

> `|N(y) triangle N(y')|`
> ` <= |H_x(y)|+|H_x(y')|`.                              `(DFT)`

In the zero-surplus equality case all leaves of the fan are exact false twins. Thus the direct equality model is explicitly complete-bipartite-like rather than an anonymous code concentration.

The fan also pays slack once it exceeds the outside-capacity threshold

`T=a-p=p+u-lambda-1`:

> `L_A>=d_x(d_x-T)_+`.                                   `(DFS)`

With

`R_D(T,L)=floor((T+sqrt(T^2+4L))/2)`,

the total number `D` of direct A-edges satisfies

> `D<=a R_D(T,L_A)/2`.                                   `(DFC)`

## 7. New A/U induced-matching fan theorem

Fix an A-source `x` and all chosen A/U certificates oriented out of `x`. Let `H_x` be the distinct A-heads and `W_x` the distinct A/U witnesses, with common order `d_x`.

There is a canonical bijection `h_i <-> w_i`, and

> `G[H_x,W_x]` is exactly a matching.                     `(IMC)`

Thus `x` is adjacent to every head and no witness, while all off-diagonal head-witness pairs are nonedges.

For the witness side,

> `2e(overline{G[W_x]})`
> ` <= d_x epsilon_x + sum_{w in W_x}epsilon_w`
> `    -d_x(lambda+1)`.                                   `(WFD)`

So low-hole A/U fans force the witnesses, all of one complementary Boolean code, towards a clique.

The induced-matching cut also gives the direct scorecard payment

> `S=E_U+L_A>=2d_x(d_x-T)_+`.                             `(AUFS)`

With

`R_C(T,S)=floor((T+sqrt(T^2+2S))/2)`,

every A/U certificate fan has `d_x<=R_C(T,S)` and the total A/U certificate traffic `C` satisfies

> `C<=aR_C(T,S)`.                                        `(AUFC)`

## 8. New quadratic A/U traffic capacity

The witness-fan near-clique information can be summed without assuming disjoint fans.

For one code `c`, let `C_c` be total chosen A/U traffic sourced in `A_c`. Then for `n_c>0`,

> `C_c^2/n_c + lambda C_c`
> ` <= [2n_c/(lambda+1)]`
> `      [N_cS_bar(c)+N_bar(c)S_c]`
> `    +N_bar(c)L_c+n_cS_bar(c)`.                         `(FS-c)`

For one unordered complementary pair `P={c,bar c}`, put

`C_P=C_c+C_bar(c)`, `A_P=n_c+n_bar(c)`,

`L_P=max(N_c,N_bar(c))`,

`W_P=max(N_c+n_c,N_bar(c)+n_bar(c))`,

`S_P=S_c+S_bar(c)`.

Then

> `C_P^2/A_P + lambda C_P`
> ` <= [2A_PL_P/(lambda+1)+W_P]S_P`.                     `(FS-P)`

Globally, with `V_0=a+u` and

`K_0=2aV_0/(lambda+1)+a+V_0`,

> `C^2/a + lambda C <= K_0 S`.                           `(GFS)`

Thus

> `C<=C_fan`
>
> `=(-a lambda+sqrt(a^2lambda^2+4aK_0S))/2`.             `(GFC)`

This is a new parameter-only quadratic cap for the A/U channel; it is independent of `mu_A`, `mu_V`, or a cylinder choice.

## 9. Rooted-transfer fan-feasibility theorem

Let `P` be chosen matched-B certificate traffic. The channel identity is

`f=D+P+C`,

with `P<=sigma_0a`.

Combining the new fan caps gives

> `f <= sigma_0a`
> `   + aR_D(T,L_A)/2`
> `   + min{aR_C(T,S),C_fan}`.                            `(HFFC)`

Therefore every above-threshold candidate satisfies

> `F_min <= sigma_0a`
> `       + aR_D(T,L_A)/2`
> `       + min{aR_C(T,S),C_fan}`.                        `(RTF)`

More structurally, if

`H=(F_min-sigma_0a)_+`,

then `D+C>=H`. Hence either:

- **direct-fan branch:** some A-vertex has at least `H/a` direct leaves, forming an independent complementary-code near-false-twin block governed by `(DFH)`; or
- **A/U-fan branch:** some A-source has at least `H/(2a)` distinct complementary-code witnesses and distinct A-heads, with the exact induced-matching cut `(IMC)` and near-clique witness control `(WFD)`.

The previous generic “macroscopic code class” escape has therefore sharpened to two explicit macroscopic fan geometries.

Core package:

`project/research/post_ms/2026-09-18-a-edge-fan-rigidity-v1/`.

## 10. Verification at this checkpoint

The new package contains:

1. `A_EDGE_FAN_RIGIDITY_AND_QUADRATIC_TRAFFIC_CAPACITY.md` — hand theorem package;
2. `check_a_edge_fan_geometry.py` — independent graph-atlas audit of the generic fan kernels;
3. `A_EDGE_FAN_GEOMETRY_AUDIT_SUMMARY.json` — frozen audit summary.

The audit covered all 21 graph-atlas D2C isomorphism classes through order seven and every maximum-degree root:

- 43 nonempty direct fans;
- 48 direct fan incidences;
- 5 direct fan leaf pairs;
- 48 exact direct-hole identities;
- 101 external unique-common-neighbour pairs;
- 36 two-certificate fan-pair tests with distinct heads;
- 19 nonadjacent witness-pair hole tests;
- failures: 0.

This is audit support only. The promoted statements rest on the hand arguments.

## 11. Live next move

Do not return to the closed mixed `{4,5}` selected-excess ladder, and do not optimize for first-proof priority on Erdős #742.

The highest-value next step is a **stability/classification theorem for the two fan equality models**.

1. **Direct branch.** Many low-hole direct leaves around one centre are near false twins; zero hole gives an exact complete-bipartite-type block. Show that a triangle-containing near-full graph cannot sustain a linear direct fan with sublinear total hole mass unless it collapses into the separately understood false-twin/bipartite regime.
2. **A/U branch.** A linear source fan gives an induced matching `H_x--W_x`, while low hole surplus makes `W_x` a same-code near-clique. Combine that matching cut with same-code edge payment and the rooted triangle count `Q`.
3. Keep `(RTF)` as the finite scorecard gate: if neither fan can be structurally sustained, the rooted-transfer demand forces `delta>=D_M`.

The separate `Q=0` false-twin-core branch remains distinct.

<!-- CURRENT-STATUS:END -->
