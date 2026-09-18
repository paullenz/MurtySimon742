# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_SELF_PRICED_FAN_FALSE_TWIN_SUPPORT_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime.

The current spine is

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete witness channels -> direct fan OR A/U fan -> false-twin private-support stability OR self-priced complementary-pair fan cost`.

The previous generic “large complementary code class” escape in the A/U fan branch is no longer a free alternative: aligned-code crowding prices it into the same pair slack. No global eventual second-extremal theorem is claimed.

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

> `f>=F_min`,                                             `(FTR)`

where

> `F_min=(p-lambda)(p+u)+q-D_M+1`.                        `(FMIN)`

Above `M(n)`, integrality also gives the parameter-only scorecard ceiling

> `S<=C_0:=2(D_M-1)+lambda(p+u)-p`.                       `(C0)`

The live target is to prove `delta>=D_M` for all sufficiently large graphs in the triangle-containing branch.

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

The repaired cylinder theorem remains useful for finite/equality diagnostics but is not the generic quadratic closure mechanism.

## 4. Complete A-edge witness channels and rooted fan gate

Every internal A-edge belongs to one of three critical-witness channels:

1. direct;
2. matched-B witness;
3. A/U unique-common-neighbour witness.

Matched-B traffic satisfies the preserved `P_B<=sigma_0a` capacity, with stronger self-pricing when reuse is heavy.

For an A/U source `x`, distinct heads `h_i` and witnesses `w_i` satisfy

> `N(x) intersect N(w_i)={h_i}`,                          `(UCN)`
>
> `G[H_x,W_x]` is exactly the matching `h_iw_i`,          `(IMC)`
>
> all witnesses have the one Boolean code `bar(c(x))`.   `(WCODE)`

Put

> `H=(F_min-sigma_0a)_+`.                                 `(H)`

The rooted transfer dichotomy says:

> either some source has a direct fan of order at least `ceil(H/a)`,
>
> or some source has an A/U fan of order at least `ceil(H/(2a))`. `(FG)`

Core package:

`project/research/post_ms/2026-09-18-a-edge-fan-rigidity-v1/`.

## 5. Preserved A/U fan geometry

For one A/U fan let `d=|W_x|`, and define

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|=epsilon_x+epsilon_{w_i}-(lambda+1)`,

`G_x=sum_i g_i`.

The fan normal form gives

> `2e(overline{G[W_x]})<=G_x`.                            `(EWM)`

Every A-witness has the root as one of its holes. Zero-hole witnesses therefore lie in `U`; the exact zero-hole witness side is a U-clique. The one-hole model is a clique minus a matching, with the A-witness root holes explicitly classified.

Put

`P=p+u`, `T=P-lambda-1=a-p`.

The coarse fan slack threshold remains

> `S>=2d(d-T)_+`.                                         `(AUFS)`

The whole-code capacity and bounded-hole staircase remain available, including the source-local complementary-pair inequality

> `2d^2-(T+1)d<=S_bar(c(x))+2E_x`,                        `(PFC2)`

where

> `E_x<=M_P S_P/(lambda+1)`                               `(PE)`

for the supporting complementary pair `P={c,bar c}`.

Thus

> `d(2d-T-1)<=(1+2M_P/(lambda+1))S_P`.                   `(PFC3)`

Preserved files:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/`.

## 6. Aligned-code self-pricing eliminates the large-code fan escape

The earlier same-code crowding package supplies the missing composition with `(PFC3)`.

For a code `c`, put

`N_c=|(A union U)_c|`, `n_c=|A_c|`,

`w_c=N_c+n_c`, `S_c=sum_{z:c(z)=c}epsilon_z`.

Define

> `D_0=T+2(a+u)+1=5p+5u-3lambda-2`.                      `(AC0)`

The preserved aligned-code crowding theorem is

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`.                      `(AC1)`

For any integer slack budget `s>=0`, define

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`.      `(RC)`

If an unordered complementary pair `Pi={c,bar c}` has pair slack `S_Pi=s`, then `(AC1)` applies separately to both sides, so

> `M_Pi=max(N_c,N_bar c)<=R_code(s)`.                     `(PLC)`

Hence the supporting code population is paid from the **same pair slack**. Substituting into `(PFC3)` gives the self-priced fan theorem

> `d(2d-T-1)<=Psi(S_Pi)`,                                 `(SPF)`

where

> `Psi(s)=s(1+2R_code(s)/(lambda+1))`.                    `(PSI)`

Define the exact integer fan cost

> `C_pair(d)=min{s>=0:d(2d-T-1)<=Psi(s)}`,                `(SPC)`

with `C_pair(d)=0` when the left side is nonpositive. Then

> `S_Pi>=C_pair(d)`.                                      `(SPC2)`

This removes the previous generic structural alternative “or `M_Pi` is large”. A large supporting code class is no longer free.

For a floor-free reviewer form, put

`R_bar(s)=(D_0+sqrt(D_0^2+12s))/3`.

If `y=R_bar(s)`, then `s=y(3y-2D_0)/4`, and every fan satisfies the cubic normal form

> `4(lambda+1)d(2d-T-1)`
> ` <= y(3y-2D_0)(lambda+1+2y)`.                         `(SPF-cubic)`

Core theorem:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/SELF_PRICED_COMPLEMENT_PAIR_FANS_AND_ROOTED_GATE.md`.

## 7. Self-priced fan packing and rooted q gate

Distinct unordered complementary pairs have disjoint slack budgets. Therefore, choosing at most one fan of order `d_j` from each distinct pair gives

> `sum_j C_pair(d_j)<=S`.                                 `(SPP)`

This is the correct distribution-free form of complementary-pair fan packing: local code concentration has already been absorbed into the local cost.

Above `M(n)`, let

> `R_0=R_code(C_0)`.                                      `(R0)`

Every A/U fan obeys

> `d(2d-T-1)<=C_0(1+2R_0/(lambda+1))`,                   `(GF1)`

and hence

> `d<=floor((T+1+sqrt((T+1)^2+8C_0(1+2R_0/(lambda+1))))/4)`. `(GF2)`

The actual-slack version is preferred to this global ceiling.

Define

> `R_D(T,L_A)=floor((T+sqrt(T^2+4L_A))/2)`,              `(RD)`
>
> `R_AU^*(S)=max{d>=0:max(2d(d-T)_+,C_pair(d))<=S}`.     `(RAU*)`

The rooted fan gate implies

> `H<=max(aR_D(T,L_A),2aR_AU^*(S))`.                     `(QG1)`

Substituting `(H)` and `(FMIN)` gives the fan-derived rooted U-edge ceiling

> `q<=sigma_0a`
> `   +max(aR_D(T,L_A),2aR_AU^*(S))`
> `   -(p-lambda)(p+u)+D_M-1`.                           `(QG2)`

Intersect `(QG2)` with the independent beta-sensitive cap `(BQ)`. Both now constrain the same `q` occurring in

> `Q=p(p+u-1)+q`

and the residual identity `(RQ3)`.

A convenient exact two-fan closure criterion is: with

`d_D=ceil(H/a)`, `d_C=ceil(H/(2a))`,

if

> `d_D(d_D-T)_+>L_A`                                     `(RG-D)`

and

> `max(2d_C(d_C-T)_+,C_pair(d_C))>S`,                    `(RG-C)`

then the assumed above-`M(n)` candidate is impossible.

A coarse diagnostic replacing all actual slacks by `C_0` does **not** generically close the branch; retaining the local/actual slack information is essential.

## 8. Direct branch: false-twin private-support theorem

The exact zero-surplus direct fan has false-twin leaves. The old generic false-twin missing-edge floor has now been strengthened using edge criticality itself.

Let `D` be any false-twin class in a D2C graph, `d=|D|>=2`, with common open neighbourhood `W`, `w=|W|`. Put

`Z=V(G)\(D union W)`, `z=|Z|=n-d-w`,

and

`W^+={x in W:d_{G[W]}(x)>0}`.

For every `x in W^+`, choose `x' in W` with `xx'` an edge and `u in D`. The triangle edge `ux` must have a criticality certificate. The orientation through `N(x) intersect N(y)={u}` is impossible when `d>=2`; a second false twin would be another common neighbour. Therefore the certificate has

> `N(u) intersect N(y)={x}`.

Since `N(u)=W`, this gives a distinct external private witness `y in Z` with

> `N(y) intersect W={x}`.                                 `(FT-private)`

Hence there is an injection

> `W^+ -> Z`,                                             `(FT1)`

so

> `|W^+|<=z`.                                             `(FT3)`

All internal edges of `W` lie on `W^+`, therefore

> `e(G[W])<=binom(min(w,z),2)`.                           `(FT4)`

Equivalently, the strengthened false-twin floor is

> `2e(overline{G[W]})`
> ` >= (d+2w-n)_+(n-d-1)`.                               `(FT5)`

This dominates the previous

`min(d,w-1)(d+2w-n)_+`

floor whenever the positive part is nonzero.

At least `(d+2w-n)_+=w-z` vertices of `W` are isolated in `G[W]`. In particular, if `z=0`, then `W` is independent and

> `G=K_{d,w}`.                                            `(FT7)`

Thus the exact direct equality model is a complete-bipartite blow-up, and departures from it require distinct private external support vertices.

If `t=|W^+|`, the private witnesses also give

> `e(W,Z)<=zw-t(w-1)`,                                   `(FT8)`
>
> `e(W)<=binom(t,2)`,                                    `(FT9)`

and therefore

> `m<=dw+binom(t,2)+zw-t(w-1)+binom(z,2)`.               `(FT10)`

For a zero-surplus rooted direct fan of order `d`, with source slack `epsilon_x`,

> `2e(overline{G[W]})`
> ` >= (d-lambda-2+2epsilon_x)_+(n-d-1)`.                `(ZF4)`

Core theorem:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/FALSE_TWIN_PRIVATE_SUPPORT_AND_BIPARTITE_STABILITY.md`.

The next direct-branch target is the bounded-hole stability extension, not another Boolean-code optimization.

## 9. Verification

Earlier graph-atlas and arithmetic checks remain preserved, including:

- all 21 D2C graph-atlas classes through order seven for the fan normal form / equality kernels;
- whole-code/hybrid fan profile: **12,445,875** exact checks, failures `0`;
- earlier complementary-pair fan packing: **38,342,788** primitive feasible cases, failures `0`.

New independent audits at this checkpoint:

- aligned-code local inversion `(AC1)->(PLC)`: **915,945** exact feasible triples, failures `0`;
- self-priced substitution `(PFC3)+(PLC)->(SPF)`: **24,942,685** primitive feasible cases, failures `0`;
- false-twin support on all 21 D2C graph-atlas classes through order seven: **25** false-twin classes, **2** internally active `W` vertices/private-witness tests, **25** support-cap tests and **25** strengthened missing-floor tests, failures `0`.

These are audit support only. The promoted statements rest on the hand proofs.

Checker and frozen summary:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/check_fan_self_pricing_and_false_twins.py`

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/FAN_SELF_PRICING_AUDIT_SUMMARY.json`.

## 10. Live next move

Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

The previous generic “large complementary-code-class/Hall alternative” has been algebraically absorbed by `(PLC)/(SPF)`. Do not reopen it as a separate branch unless a source-tuple argument needs code-local information.

The highest-value next moves are now tightly focused:

1. **A/U branch:** combine the self-priced fan cost `(SPC)/(SPP)` and fan-derived `q` ceiling `(QG2)` with the beta/source-tuple cap `(BQ)/(IST)`. The objective is a compact residual contradiction in the triangle-containing branch, not another free-variable optimization.
2. **Direct branch:** extend the private-support injection from exact false twins to bounded-hole direct fans, then feed the resulting common-side sparsity directly into `Q=p(p+u-1)+q`, `delta+Q=L_A+f`, and `delta=r-f`.
3. **Rooted synthesis:** use both branches to bound the rooted-transfer demand `F_min`; an eventual theorem should arise by showing that for sufficiently large parameters neither stability model can absorb the required A-edge mass below `D_M`.
4. Keep `X_3` explicit throughout. It has `u=0`, `F_min=0` and remains a required finite exception.

The separate `Q=0` / triangle-free / false-twin-core branch remains distinct.

<!-- CURRENT-STATUS:END -->