# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_SELF_PRICED_FAN_TWO_EXCEPTION_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The live branch is the triangle-containing unmatched/errorful antipode regime.

The current spine is

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete witness channels -> direct fan OR A/U fan -> false-twin blow-up stability OR self-priced complementary-pair fan cost`.

Two former structural escapes are now substantially narrowed:

- the A/U fan alternative “perhaps its complementary code class is huge” is no longer free, because same-code crowding prices that population into the **same pair slack**;
- the exact direct-fan equality model cannot remain an above-`M(n)` triangle-containing graph with at most two vertices outside its false-twin bipartite core.

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

## 2. Residual defect / rooted-triangle spine

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

## 5. Preserved A/U fan normal form

For one A/U fan let `d=|W_x|`, and define

`g_i=epsilon_x+epsilon_{w_i}-(lambda+1)`,

`G_x=sum_i g_i`.

Then

> `2e(overline{G[W_x]})<=G_x`.                            `(EWM)`

Every A-witness has the root as one of its holes. Zero-hole witnesses therefore lie in `U`; the exact zero-hole witness side is a U-clique. The one-hole model is a clique minus a matching, with the A-witness root holes classified.

Put

`P=p+u`, `T=P-lambda-1=a-p`, `L=lambda+1`.

The coarse fan slack threshold remains

> `S>=2d(d-T)_+`.                                         `(AUFS)`

The whole-code / bounded-hole package yields the pair-local fan inequality

> `d(2d-T-1)<=(1+2M_P/L)S_P`,                            `(PFC3)`

for the supporting complementary code pair, where

`M_P=max(N_c,N_bar c)`, `S_P=S_c+S_bar c`.

Preserved package:

`project/research/post_ms/2026-09-18-fan-equality-stability-v1/`.

## 6. Self-priced complementary-pair fan theorem

The earlier same-code crowding theorem closes the apparent large-code escape in `(PFC3)`.

For code `c`, put

`N_c=|(A union U)_c|`, `n_c=|A_c|`,

`w_c=N_c+n_c`, `S_c=sum_{z:c(z)=c}epsilon_z`.

Define

> `D_0=T+2(a+u)+1=5p+5u-3lambda-2`.                      `(AC0)`

The preserved aligned-code self-pricing inequality is

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`.                      `(AC1)`

For `s>=0`, define

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`.      `(RC)`

If `Pi={c,bar c}` has pair slack `S_Pi=s`, then `(AC1)` on both sides gives

> `M_Pi<=R_code(s)`.                                      `(PLC)`

Therefore every A/U fan supported on `Pi` obeys

> `d(2d-T-1)<=Psi(S_Pi)`,                                 `(SPF)`

where

> `Psi(s)=s(1+2R_code(s)/L)`.                             `(PSI)`

Define the exact integer fan cost

> `C_pair(d)=min{s>=0:d(2d-T-1)<=Psi(s)}`,                `(SPC)`

with `C_pair(d)=0` if the left side is nonpositive. Then

> `S_Pi>=C_pair(d)`.                                      `(SPC2)`

Thus “large complementary code class” is no longer a separate free branch: if it makes the fan cheap, its own pair slack has already paid for it.

For distinct complementary pairs carrying fans `d_j`, disjointness of pair slacks gives

> `sum_j C_pair(d_j)<=S`.                                 `(SPP)`

Core theorem:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/SELF_PRICED_COMPLEMENT_PAIR_FANS_AND_ROOTED_GATE.md`.

## 7. A/U rooted q gate

Define

> `R_D(T,L_A)=floor((T+sqrt(T^2+4L_A))/2)`,              `(RD)`
>
> `R_AU^*(S)=max{d>=0:max(2d(d-T)_+,C_pair(d))<=S}`.     `(RAU*)`

The rooted fan gate implies

> `H<=max(aR_D(T,L_A),2aR_AU^*(S))`.                     `(QG1)`

Substituting `(H)` and `(FMIN)` gives the fan-derived U-edge ceiling

> `q<=sigma_0a`
> `   +max(aR_D(T,L_A),2aR_AU^*(S))`
> `   -(p-lambda)(p+u)+D_M-1`.                           `(QG2)`

Intersect `(QG2)` with the independent beta-sensitive cap `(BQ)`. Both now constrain the same `q` in

> `Q=p(p+u-1)+q`

and the residual identity `(RQ3)`.

With

`d_D=ceil(H/a)`, `d_C=ceil(H/(2a))`,

a convenient exact two-fan contradiction is

> `d_D(d_D-T)_+>L_A`                                     `(RG-D)`

and simultaneously

> `max(2d_C(d_C-T)_+,C_pair(d_C))>S`.                    `(RG-C)`

A diagnostic replacing all actual slacks by `C_0` is still too coarse to close the generic branch; the local/actual slack information is essential.

## 8. Direct branch: false-twin private support

The exact zero-surplus direct fan has false-twin leaves. Let `D` be any false-twin class in a D2C graph, `d=|D|>=2`, with common open neighbourhood `W`, `w=|W|`. Put

`Z=V(G)\(D union W)`, `z=|Z|=n-d-w`,

`W^+={x in W:d_{G[W]}(x)>0}`, `t=|W^+|`.

For every `x in W^+`, triangle-edge criticality forces a distinct private witness `y in Z` satisfying

> `N(y) intersect W={x}`.                                 `(FT-private)`

Hence

> `t<=z`,                                                  `(FT1)`
>
> `e(G[W])<=binom(min(w,z),2)`,                           `(FT4)`
>
> `2e(overline{G[W]}) >= (d+2w-n)_+(n-d-1)`.             `(FT5)`

The private witnesses also give

> `e(W,Z)<=zw-t(w-1)`,                                   `(FT8)`

so

> `m<=w(n-w)+binom(z,2)-t(w-1)+binom(t,2)`.              `(FT10)`

At `z=0`, this forces

> `G=K_{d,w}`.                                            `(FT7)`

Core theorem:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/FALSE_TWIN_PRIVATE_SUPPORT_AND_BIPARTITE_STABILITY.md`.

## 9. New two-exception false-twin second-extremal gate

Let

> `B_w=floor(n^2/4)-w(n-w)>=0`.                           `(TE4)`

Since

> `floor(n^2/4)-M(n)=floor(n/2)-1`,                      `(TE5)`

`(FT10)` gives the exact sufficient second-extremal criterion

> `B_w+t(w-1)-binom(t,2)-binom(z,2)`
> ` >= floor(n/2)-1`
>
> ` ==> m<=M(n)`.                                         `(TE6)`

This already closes the internally active `z=2` case for `n>=7`. More precisely:

- `z=0`: `G` is complete bipartite;
- `z=1`: `t<=1`, but any edge of `G[W]` would require two active endpoints, so `W` is independent and `G` is triangle-free;
- `z=2` and `G[W]` nonempty: `t=2`, and `(TE6)` holds for every `n>=7`, hence `m<=M(n)`;
- `z=2` and `W` independent: a direct triangle-edge criticality argument shows `G` is triangle-free. If `Z={r,s}` formed a triangle `r-s-x-r`, criticality of `rx` and `sx` forces `N_W(r)=N_W(s)={x}`, after which the triangle edge `rs` has no possible criticality witness.

Therefore:

> **If `n>=7`, a D2C graph with a false-twin class and `z<=2` is either complete bipartite, triangle-free, or has `m<=M(n)`.** `(TE-main)`

Consequently, in the live triangle-containing above-`M(n)` branch,

> `z>=3`                                                   `(TE13)`

for every false-twin class.

For an exact zero-surplus rooted direct fan of order `d`,

> `z=b+1-d-epsilon_x`,

so any live survivor must satisfy

> `d+epsilon_x<=b-2`.                                     `(ZF-gate)`

Core theorem:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/FALSE_TWIN_TWO_EXCEPTION_SECOND_EXTREMAL_GATE.md`.

This is the first direct-branch result in the current fan programme that reaches the actual `M(n)` threshold rather than only producing a sparsity estimate.

## 10. Verification

Earlier graph-atlas and arithmetic checks remain preserved, including:

- all 21 D2C graph-atlas classes through order seven for the fan normal form / equality kernels;
- whole-code/hybrid fan profile: **12,445,875** exact checks, failures `0`;
- earlier complementary-pair fan packing: **38,342,788** primitive feasible cases, failures `0`.

New independent audits at this checkpoint:

- aligned-code local inversion `(AC1)->(PLC)`: **915,945** exact feasible triples, failures `0`;
- self-priced substitution `(PFC3)+(PLC)->(SPF)`: **24,942,685** primitive feasible cases, failures `0`;
- false-twin support on all 21 D2C graph-atlas classes through order seven: **25** false-twin classes, **2** internally active `W` vertices/private-witness tests, **25** support-cap tests and **25** strengthened missing-floor tests, failures `0`;
- two-exception atlas regression: **21** false-twin classes with `z<=2` (`17` with `z=0`, `0` with `z=1`, `4` with `z=2`), with no triangle-containing `z=2` class and no failures.

These are audit support only. The promoted statements rest on the hand proofs.

Checker and frozen summary:

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/check_fan_self_pricing_and_false_twins.py`

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/FAN_SELF_PRICING_AUDIT_SUMMARY.json`.

## 11. Live next move

Do not return to the closed mixed `{4,5}` selected-excess ladder and do not optimize for first-proof priority on Erdős #742.

The previous generic “large complementary-code-class/Hall alternative” has been absorbed by `(PLC)/(SPF)`. The exact direct false-twin branch is also closed through two external exceptions in the live triangle-containing above-threshold regime.

The highest-value next moves are now:

1. **A/U branch:** combine the self-priced fan cost `(SPC)/(SPP)` and fan-derived `q` ceiling `(QG2)` with the beta/source-tuple cap `(BQ)/(IST)`, aiming for a compact residual contradiction rather than another free-variable optimization.
2. **Direct branch:** extend the private-support theorem from exact false twins to bounded-hole direct fans. The exact equality model now has a concrete target: any above-threshold triangle-containing survivor needs at least three external exceptions.
3. **Rooted synthesis:** feed the improved direct and A/U branch bounds into `F_min`; the eventual theorem should come from showing that neither stability model can absorb the rooted A-edge demand below `D_M` once the core is sufficiently large.
4. Keep `X_3` explicit throughout. It has `u=0`, `F_min=0` and remains a required finite exception.

The separate triangle-free / false-twin-core branch remains distinct and should use the known triangle-free second-extremal results rather than be reproved here.

<!-- CURRENT-STATUS:END -->