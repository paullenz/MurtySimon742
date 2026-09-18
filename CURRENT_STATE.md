# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_FAN_EQUALITY_BETA_FEEDBACK_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime.

The conceptual spine is now

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete witness channels -> macroscopic fan geometry -> equality/stability classification -> beta-sensitive fan-hole feedback -> residual closure`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is a comparison threshold, not an all-order theorem.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph has been reconstructed and checked exactly:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- isomorphic to the project's `X_3`;
- full-tight data `p=4,b=8,a=3,u=0,lambda=4,r=0,F=empty`;
- `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`, `f=0`.

Its rooted-triangle transfer is endpoint-saturated: `Q-f=12`. The live unmatched/fan arguments do not suppress it: at the canonical root `u=0` and `F_min=0=f`.

Certification:

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

`c_lambda=ceil(lambda(lambda+2)/2)`,

`D_M=ceil((4p+2u-c_lambda-2)/2)`.

Then

> `E_U+L_A=2delta+lambda(p+u)-p`,                         `(RS)`
>
> `D_M=b(n-b)-M(n)`,
>
> `m<=M(n) iff delta>=D_M`.                               `(RT)`

Thus the active target is exactly `delta>=D_M`.

The separate `Q=0` / false-twin-core branch remains distinct.

## 3. Rooted triangles are an exact transfer variable

The exact identities are

> `r+Q=L_A+2f`,                                           `(RQ1)`
>
> `delta+Q=L_A+f`,                                        `(RQ2)`
>
> `delta=E_U+Q-f-lambda(p+u)+p`.                          `(RQ3)`

With `T_Q=Q-f`,

> `L_A=delta+T_Q`,
>
> `E_U=delta+lambda(p+u)-p-T_Q`.                          `(TR)`

Every above-`M(n)` candidate satisfies

> `f>=F_min`,                                             `(FTR)`

where

> `F_min=Q-lambda(p+u)+p-D_M+1`
> `     =(p-lambda)(p+u)+q-D_M+1`.                        `(FMIN)`

Core file:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md`.

## 4. Preserved switching / Hall / source-tuple stack

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

If `u=O(p)` and `lambda=o(p)`, every finite limit `rho=u/p` still satisfies

> `rho<27/14`.

The repaired cylinder theorem remains a finite/equality tool rather than the generic quadratic closure mechanism.

## 5. Complete A-edge witness channels and fan gate

Every internal A-edge belongs to one of three channels: direct, matched-B witness, or A/U unique-common-neighbour witness.

For a direct A-edge fan around `x`, the leaves are independent complementary-code vertices. With

`W_x=(V(G)\{v})\N(x)`

and `H_x(y)=W_x\N(y)`,

> `N(y)=W_x\H_x(y)`,
>
> `|H_x(y)|=epsilon_x+epsilon_y-(lambda+1)`.              `(DFH)`

Also

> `L_A>=d_x(d_x-T)_+`,                                    `(DFS)`

where `T=a-p=p+u-lambda-1`.

For an A/U certificate fan with source `x`, distinct heads `h_i` and witnesses `w_i`,

> `G[H_x,W_x]` is exactly the matching `h_iw_i`.          `(IMC)`

The witness side obeys

> `2e(overline{G[W_x]})`
> ` <= d_x epsilon_x + sum_i epsilon_{w_i}`
> `    -d_x(lambda+1)`.                                   `(WFD)`

The fan-square capacity gives

> `C^2/a + lambda C <= K_0(E_U+L_A)`,                    `(GFS)`

with `K_0=2a(a+u)/(lambda+1)+2a+u`.

With matched-B traffic `P<=sigma_0a` and `f=D+P+C`, every above-threshold candidate satisfies the fan gate

> `F_min <= sigma_0a`
> `       + aR_D(T,L_A)/2`
> `       + min{aR_C(T,E_U+L_A),C_fan}`.                  `(RTF)`

If `H=(F_min-sigma_0a)_+`, then either some source has a direct fan of order at least `H/a`, or some source has an A/U fan of order at least `H/(2a)`.

Core package:

`project/research/post_ms/2026-09-18-a-edge-fan-rigidity-v1/`.

## 6. Exact A/U fan-hole normal form

Fix one A/U fan with source `x`, heads `h_i`, witnesses `w_i`, and order `d`.

Put

`Y_x=V(G)\({x} union N(x))`,

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|=epsilon_x+epsilon_{w_i}-(lambda+1)`,

`G_x=sum_i g_i`.

Then

> `N(w_i)={h_i} union (Y_x\({w_i} union Z_i))`.          `(EFN)`

Hence

> `2e(overline{G[W_x]})<=G_x`.                           `(EWM)`

Every A-witness has the root `v` as a hole, so

> `|W_x intersect A|<=G_x`,
>
> `|W_x intersect U|>=(d-G_x)_+`.                        `(AWU)`

Therefore

> `q >= max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`.         `(FQLB)`

This is the first direct fan-to-rooted-triangle feedback: low-hole A/U geometry itself raises `q`, hence raises both `Q` and `F_min`.

## 7. Zero-hole A/U equality classification

If `G_x=0` and `p>=1`, then:

1. every witness lies in `U`;
2. `W_x` is a clique, so `q>=binom(d,2)`;
3. all but at most one head satisfy `N(h_i) intersect Y_x={w_i}`;
4. for every such head, `N(h_i) intersect N(w_i)=empty`;
5. consequently `c(h_i)=c(x)`.

Thus the exact equality model is a U-clique of antipodal-code witnesses together with, except for at most one index, source-code A-heads joined to the witnesses by direct matching edges.

## 8. Quantitative A/U stability and Hamming localization

For each head define

`t_i=|N(h_i) intersect (Y_x\{w_i})|`.

For a present witness edge `w_iw_j`, any chosen criticality certificate oriented from `w_i` toward `w_j` is either the matching head `h_j`, in which case `t_j<=g_i`, or a vertex of `Z_i`. A fixed hole can certify at most one target from a fixed source.

For integer `tau>=0`, let

`B_tau={i:g_i<=tau<t_i}`.

Then

> `|B_tau|(|B_tau|-1)<=3G_x`.                            `(BST)`

Consequently all but at most

> `floor(G_x/(tau+1))`
> ` + floor((1+sqrt(1+12G_x))/2)`                        `(EXC)`

indices satisfy `g_i,t_i<=tau`. For every such index,

> `|N(h_i) intersect N(w_i)|<=tau`,                      `(NMD)`
>
> `dist_H(c(h_i),c(x))<=tau`.                            `(HLOC)`

Hence if `d=Theta(p)` and `G_x=o(p^2)`, all but `o(p)` heads lie within Hamming distance `o(p)` of the source code while every witness has the exact antipodal code. The low-hole equality model is therefore an asymptotic two-cluster Hamming configuration.

## 9. Beta-sensitive fan-hole capacity and rooted feedback

The preserved beta-sensitive U-edge theorem is

> `q<=Q_beta:=au-B_beta+N_1`,                             `(BQ)`

where `N_1=|{z in A:ell_z=1}|`; coarsely `Q_beta<=au-B_beta+a`.

Combining `(BQ)` with `(FQLB)` gives the exact finite fan-hole floor

> `G_x >= [d-floor(sqrt(2Q_beta+d))]_+`.                 `(BFH)`

If `z_0=|{i:g_i=0}|`, then the zero-hole witnesses form a clique in `U`, so

> `binom(z_0,2)<=q<=Q_beta`,                              `(ZHC1)`
>
> `z_0<=floor((1+sqrt(1+8Q_beta))/2)`.                   `(ZHC2)`

Thus whenever `Q_beta=o(p^2)`, a linear A/U fan has only `o(p)` genuinely zero-hole witnesses and must satisfy

> `G_x>=d-o(p)`.                                         `(ABFH)`

The cheapest surviving sparse-U fan is therefore not the exact equality model but a bounded-/one-hole perturbation of it.

Writing

`F_0=(p-lambda)(p+u)-D_M+1`,

we also have the rooted feedback

> `F_min >= F_0`
> ` +max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`.            `(RFF)`

On the A/U side of the fan dichotomy, a chosen large fan must satisfy the self-consistency gate

> `d >= (1/(2a))`
> ` [F_0`
> `  +max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`
> `  -sigma_0a]_+`.                                      `(AFG)`

So `q` is no longer a free nuisance variable in the equality analysis: the fan pushes it up while beta-source geometry pushes it down.

Follow-on file:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/BETA_SENSITIVE_FAN_HOLE_AND_ROOTED_FEEDBACK.md`.

## 10. False-twin quotient theorem for the direct equality model

Let `D` be any false-twin class in a D2C graph, with common open neighbourhood `W`, and put `d=|D|`, `w=|W|`, with `d,w>=2`.

For each `z in W`, at least one of the following holds:

1. `z` has no neighbour inside `W`;
2. some `q notin W` has `N(q) intersect W={z}`;
3. `z` has at least `d` nonneighbours inside `W`.

It follows that

> `2e(overline{G[W]})`
> ` >= min(d,w-1)(2w+d-n)_+`.                            `(FTF)`

For a zero-hole direct fan around `x`, all leaves are exact false twins with

`N(y)=W_x=(V(G)\{v})\N(x)`

and

`w=|W_x|=b-lambda-1+epsilon_x`.

Hence

> `e(overline{G[W_x]})`
> ` >= (1/2)min(d,w-1)`
> `      (d+2epsilon_x-lambda-2)_+`.                     `(DFQ)`

Since a leaf has local triangle count `e(G[W_x])`,

> `e(G[N(y)])`
> ` <= binom(w,2)`
> `    -(1/2)min(d,w-1)`
> `      (d+2epsilon_x-lambda-2)_+`.                     `(DTS)`

Thus a linear exact false-twin fan either forces a quadratically sparse common side (bipartite-like behaviour) or is absorbed by large root imbalance relative to centre slack.

Core equality/stability package:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/`.

## 11. Verification at this checkpoint

The package contains the hand theorem files plus `check_fan_equality_stability.py` and a frozen JSON summary.

Independent graph-atlas audit over all 21 D2C isomorphism classes through order seven:

- 31 admissible unique-common-neighbour fans;
- 63 exact witness-neighbourhood checks;
- 31 witness missing-edge checks;
- 140 threshold-stability checks;
- 4 zero-hole fan checks;
- 20 false-twin classes;
- 53 false-twin vertex-level dichotomy checks;
- 20 global false-twin floor checks;
- failures: 0.

The audit is support only. Boolean/Hamming conclusions and eventual/asymptotic claims rest on the hand arguments.

## 12. Live next move

Do not return to the closed mixed `{4,5}` selected-excess ladder, and do not optimize for first-proof priority on Erdős #742.

The highest-value next step is now the **bounded-hole fan classification**, especially the one-hole model forced by `(BFH)/(ZHC2)` in sparse-U beta-saturated slices.

1. **A/U one-hole branch.** Distinguish A-witnesses, whose canonical hole is the root `v`, from U-witnesses, whose hole must lie elsewhere. Classify the resulting witness graph (clique minus a low-degree defect) and matching-head geometry. Combine with `(HLOC)` and same-code edge payment.
2. **Rooted feedback.** Use `(AFG)` together with the global beta lower bounds and `(RTF)` to test whether a parameter region closes without a variational optimization.
3. **Direct branch.** Combine `(DFQ)/(DTS)` with the location of `W_x intersect B` and `Q=e(G[B])` to convert sparse common-side geometry into residual defect.
4. Keep the mandatory `X_3` control explicit at every step.

The separate `Q=0` false-twin-core branch remains distinct.

<!-- CURRENT-STATUS:END -->
