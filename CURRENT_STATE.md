# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_SELF_PRICED_AU_BOUNDED_SURPLUS_DIRECT_THREE_EXCEPTION_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime.

The current spine is

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete witness channels -> direct fan OR A/U fan -> bounded-surplus bipartite stability OR self-priced complementary-pair fan cost`.

The direct branch has advanced materially at this checkpoint: the private-support theorem no longer requires exact false twins. A direct fan whose **total** hole surplus is at most `d-2` still has the same private-support injection, and in an above-`M(n)` triangle-containing graph of order at least 11 it requires at least **four** external exceptions. Equivalently, every live direct fan satisfies a compact `surplus OR four exceptions` dichotomy.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is only the eventual comparison threshold.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 D2C graph has been reconstructed exactly and is isomorphic to the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`.

Its rooted-triangle transfer is endpoint-saturated: `Q-f=12`. At the canonical root `u=0`, `F_min=0=f`, and `A` is independent, so there is no positive direct or A/U fan forced by the live machinery.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

## 2. Residual defect / rooted-triangle spine

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

There are `p` tight antipode pairs in `B` and an unmatched set `U`, `u=|U|`, so

`b=2p+u`,

`a=2p+u-lambda-1`.

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

Then

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

> `f>=F_min=(p-lambda)(p+u)+q-D_M+1`.                    `(FMIN)`

Above `M(n)`, integrality gives

> `S<=C_0:=2(D_M-1)+lambda(p+u)-p`.                       `(C0)`

The live objective is to prove `delta>=D_M` for all sufficiently large graphs in the triangle-containing branch.

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

Thus above `M(n)`

> `sigma_0<=R_A(C_0)`,                                    `(ZSC)`

where

> `R_A(L)=max(2,floor((1+sqrt(1+4L))/2))`.

For `u=O(p)` and `lambda=o(p)`, every finite limiting unmatched ratio still satisfies `u/p<27/14` asymptotically.

The repaired cylinder theorem is retained as a finite/equality diagnostic, not the generic quadratic closure mechanism.

## 4. Complete A-edge channels and rooted fan gate

Every internal A-edge belongs to one of three critical-witness channels:

1. direct;
2. matched-B witness;
3. A/U unique-common-neighbour witness.

Matched-B traffic satisfies `P_B<=sigma_0a` together with stronger self-pricing when reuse is heavy.

For an A/U source `x`, distinct heads `h_i` and witnesses `w_i` satisfy

> `N(x) intersect N(w_i)={h_i}`,                          `(UCN)`
>
> `G[H_x,W_x]` is exactly the matching `h_iw_i`,          `(IMC)`
>
> all witnesses have Boolean code `bar(c(x))`.           `(WCODE)`

Put

> `H=(F_min-sigma_0a)_+`.                                 `(H)`

The rooted transfer dichotomy says:

> either some source has a direct fan of order at least `ceil(H/a)`,
>
> or some source has an A/U fan of order at least `ceil(H/(2a))`. `(FG)`

Core package:

`project/research/post_ms/2026-09-18-a-edge-fan-rigidity-v1/`.

## 5. Self-priced A/U complementary-pair branch

For one A/U fan let `d` be its order. Put

`P=p+u`, `T=P-lambda-1=a-p`, `L=lambda+1`.

The coarse fan slack threshold remains

> `S>=2d(d-T)_+`.                                         `(AUFS)`

For code `c`, write

`N_c=|(A union U)_c|`, `n_c=|A_c|`,

`w_c=N_c+n_c`, `S_c=sum_{z:c(z)=c}epsilon_z`.

Define

> `D_0=T+2(a+u)+1=5p+5u-3lambda-2`,                      `(AC0)`
>
> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`.                      `(AC1)`

For a complementary pair `Pi={c,bar c}` with pair slack `s`, put

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`.      `(RC)`

The whole-code fan theorem plus `(AC1)` gives

> `d(2d-T-1)<=Psi(S_Pi)`,                                 `(SPF)`

where

> `Psi(s)=s(1+2R_code(s)/L)`.                             `(PSI)`

Define

> `C_pair(d)=min{s>=0:d(2d-T-1)<=Psi(s)}`.                `(SPC)`

Then every A/U fan supported on `Pi` obeys

> `S_Pi>=C_pair(d)`.                                      `(SPC2)`

For distinct complementary pairs carrying fans `d_j`,

> `sum_j C_pair(d_j)<=S`.                                 `(SPP)`

Thus a large complementary code class is no longer a free A/U escape: if it makes a fan feasible, its own pair slack has already paid for it.

The fan-derived U-edge ceiling remains

> `q<=sigma_0a`
> `   +max(aR_D(T,L_A),2aR_AU^*(S))`
> `   -(p-lambda)(p+u)+D_M-1`,                            `(QG2)`

and should be intersected with the independent beta/source cap `(BQ)`.

Core theorem:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/SELF_PRICED_COMPLEMENT_PAIR_FANS_AND_ROOTED_GATE.md`.

## 6. Direct-fan hole geometry

Fix an A-source `x` and its direct fan

`D_x={y in A:xy is direct}`, `d=|D_x|>=2`.

Put

`W=(V(G)\{v})\N(x)`,

`H_y=W\N(y)`,

`h_y=|H_y|=epsilon_x+epsilon_y-(lambda+1)`,

and define the **total direct-fan hole surplus**

> `eta=sum_{y in D_x}h_y`.                                `(BH0)`

Write

`w=|W|`, `Z=V(G)\(D_x union W)`, `z=|Z|`.

The rooted identities are

> `w=a+epsilon_x`,                                        `(BH1)`
>
> `z=b+1-d-epsilon_x`.                                    `(BH2)`

Since `d<=a-1`, one has `w>=d+1`.

The exact false-twin model is `eta=0`, but the new theorem does not require exact equality.

## 7. New bounded-surplus private-support theorem

If

> `eta<=d-2`,                                              `(BH5)`

then at least two leaves have zero holes. Choosing one such leaf `y_0` gives `N(y_0)=W`.

Triangle-edge criticality then yields an injection

> `phi:W^+ -> Z`,                                         `(BH7)`

where

`W^+={t in W:d_{G[W]}(t)>0}`,

such that

> `N(phi(t)) intersect W={t}`.                            `(BH8)`

The reverse triangle-edge orientation would require at least one hole incidence on `{t,q}` for every one of the other `d-1` leaves, contradicting `eta<=d-2`.

Thus

> `t:=|W^+|<=z`,                                          `(BH9)`
>
> `e(W,Z)<=zw-t(w-1)`,                                   `(BH11)`
>
> `e(G[W])<=binom(t,2)`.                                 `(BH12)`

Since `e(D_x,W)=dw-eta`,

> `m<=w(n-w)+binom(z,2)-t(w-1)+binom(t,2)-eta`.          `(BH13)`

Equivalently, every direct fan satisfies the structural dichotomy

> `eta>=d-1`,
>
> **or** the private-support injection `(BH7)-(BH8)` holds. `(BH10)`

Core theorem:

`project/research/post_ms/2026-09-18-direct-fan-three-exception-v1/DIRECT_FAN_BOUNDED_SURPLUS_THREE_EXCEPTION_GATE.md`.

## 8. New bounded-surplus three-exception second-extremal gate

Let

> `B_w=floor(n^2/4)-w(n-w)`.

From `(BH13)`,

> `B_w+eta+t(w-1)-binom(t,2)-binom(z,2)`
> ` >= floor(n/2)-1`
>
> ` ==> m<=M(n)`.                                         `(BH14)`

The low-exception cases now close throughout the whole total-hole range `eta<=d-2`:

- `z<=1`: `W` is independent and the graph is triangle-free;
- `z=2`, `G[W]` nonempty: `t=2` and `(BH14)` gives `m<=M(n)` for `n>=7`;
- `z=2`, `W` independent and triangle-containing: triangle-edge criticality gives `d_W(r),d_W(s)<=eta+1`, hence `m<=dw+eta+3<=M(n)`;
- `z=3`, `G[W]` nonempty: `(BH14)` gives `m<=M(n)` for `n>=11`;
- `z=3`, `W` independent: a complete four-case analysis of `J=G[Z]` (`0,1,2,3` Z-edges) gives `m<=M(n)` whenever the graph is triangle-containing.

The two nontrivial incidence bounds in the independent `z=3` analysis are:

- if `J=P_3`, and `E=e(W,Z)-w`, then

  > `E<=eta+2`;                                            `(BH29)`

- if `J=K_3`, then criticality of the Z-edges forces singleton W-types on a vertex cover of `K_3`, and

  > `E<=eta+1`.                                            `(BH33)`

Hence the main theorem is:

> **If `n>=11`, a direct fan of order `d>=2` with `eta<=d-2` and `z<=3` occurs in a D2C graph, then the graph is triangle-free or `m<=M(n)`.** `(BH-main)`

Therefore every live triangle-containing above-`M(n)` candidate of order at least 11 satisfies, for every direct fan,

> `eta>=d-1`,
>
> **or**
>
> `z>=4`.                                                   `(BH37)`

Using `z=b+1-d-epsilon_x`, equivalently

> `eta>=d-1`,
>
> **or**
>
> `d+epsilon_x<=b-3`.                                     `(BH38)`

This strictly improves the old exact-false-twin gate `z>=3` / `d+epsilon_x<=b-2` and extends it to nonzero bounded total hole mass.

For an exact zero-surplus direct fan (`eta=0`), every live survivor now satisfies

> `z>=4`, `d+epsilon_x<=b-3`.                             `(BH40)`

If instead `d+epsilon_x>=b-2`, then `(BH38)` forces `eta>=d-1`, so

> `sum_{y in D_x}epsilon_y`
> ` >= d(lambda+2-epsilon_x)-1`.                          `(BH41)`

Together with the preserved degree floor, this gives

> `L_A>=epsilon_x`
> `    +max{d(d-T)_+, d(lambda+2-epsilon_x)-1}`.          `(BH42)`

Thus the near-boundary direct branch now self-prices locally in the same qualitative sense as the complementary-pair A/U branch.

## 9. Verification

Earlier audits remain preserved, including the A/U whole-code/profile and complementary-pair self-pricing checks, the graph-atlas fan checks, and the exact two-exception false-twin audit.

New independent audit support for the bounded-surplus direct theorem:

- integer envelope checks (`z=2/3`, active and independent cases): **667,417**;
- `P_3` incidence inequalities: **29,700**;
- `K_3` incidence inequalities: **28,561**;
- exact `eta=0,z=3` quotient regression: **16,912** candidate type models, including **43** D2C models and **17** triangle-containing D2C models, all with `m<=M(n)`;
- total new checks: **742,590**, failures `0`.

These are audit support only; the promoted statements rest on the hand proofs.

Checker and frozen summary:

`project/research/post_ms/2026-09-18-direct-fan-three-exception-v1/check_direct_fan_three_exception.py`

`project/research/post_ms/2026-09-18-direct-fan-three-exception-v1/DIRECT_FAN_THREE_EXCEPTION_AUDIT_SUMMARY.json`.

## 10. Live next move

Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

The direct branch and A/U branch now both have genuine local self-pricing mechanisms:

- **direct:** `eta>=d-1` or at least four external exceptions, with `(BH42)` pricing the near-boundary alternative into local A-slack;
- **A/U:** `S_Pi>=C_pair(d)` on the actual supporting complementary code pair.

The highest-value next move is therefore **rooted synthesis**, not another standalone fan lemma:

1. replace the old global direct-fan radius `R_D(T,L_A)` inside the rooted fan gate by the source-resolved dichotomy `(BH38)/(BH42)`;
2. combine that direct local cost with the A/U pair cost `(SPC)/(SPP)` and the matched-B cap `sigma_0a` to upper-bound the A-edge mass `f` demanded by `(FMIN)`;
3. keep `q` live and intersect the resulting rooted gate with `(BQ)`, because `Q=p(p+u-1)+q` is the exact rooted-triangle transfer variable;
4. look for a compact contradiction in `delta=r-f<D_M`, rather than reverting to a many-variable continuum optimization.

A secondary direct-branch target, if the synthesis stalls, is the next stability layer `eta>=d-1`: determine whether that hole surplus can be charged globally without reusing the source slack `epsilon_x` too many times.

The separate triangle-free branch remains distinct and should use the known triangle-free second-extremal results rather than be reproved here.

Keep `X_3` explicit throughout. It has `u=0`, `f=0`, `F_min=0` and remains a required finite exception.

<!-- CURRENT-STATUS:END -->