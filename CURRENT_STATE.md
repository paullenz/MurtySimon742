# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_SOURCE_SUPPORT_COMBINED_CHANNEL_FOUR_EXCEPTION_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed and is not a live branch. The active branch is the triangle-containing unmatched/errorful antipode regime.

The current structural spine is

`residual defect -> rooted-triangle transfer -> forced A-edge mass -> complete witness channels -> complementary-pair slack pricing + matched-B self-pricing -> direct bounded-surplus bipartite stability`.

This checkpoint adds two material results:

1. **complete A-edge channel capacity:** direct and A/U traffic can be combined on each complementary Boolean-code pair before taking maxima, so all three A-edge witness channels are now paid from actual slack with no free direct/AU channel split;
2. **four-exception direct stability:** a bounded-surplus direct fan in a live triangle-containing above-`M(n)` graph of order at least 23 needs at least **five** vertices outside its near-bipartite core.

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

## 2. Rooted residual / triangle spine

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

There are `p` tight antipode pairs in `B` and an unmatched set `U`, `u=|U|`, so

> `b=2p+u`,
>
> `a=2p+u-lambda-1`.

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

The live objective is to prove `delta>=D_M` for all sufficiently large triangle-containing candidates.

Core residual package:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/`.

## 3. Preserved switching / Hall / source-tuple stack

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x`. The exact source-tuple hierarchy remains

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`     `(FDPr)`

for every `r>=3`, with integrated deficit profile

> `sum_{x in L}(p-ell_x)>=Phi_r(|L|)`.                    `(IST)`

Put

> `B_beta=sum_x ell_x`.

The main beta lower bounds are

> `B_beta >= [pu-R_hat a]_+`,                             `(STL)`
>
> `B_beta >= p(lambda+1-2p)_+`,                           `(RBF)`

where `R_hat=min(p,R_*)` and `R_*` is the preserved switching/Hall class cap.

Applying `(IST)` to all of `A` gives the integrated total beta envelope

> `B_beta<=ap-Phi_r(a)`.                                  `(ITB)`

For positive beta support `A_+={x:ell_x>0}`, define

> `N_sup(B)=max(ceil(B/min(p,u)), max_{r>=3} N_r(B))`,

where

> `N_r(B)=min{N:Np-Phi_r(N)>=B}`.

Then

> `|A_+|>=N_sup(B_beta)`.                                 `(NSUP)`

Consequently the zero-beta cross-edge reservoir is bounded by

> `s_0<=u[a-N_sup(B_beta)]`.                              `(S0ST)`

and the preserved unmatched-slack floor is

> `E_U`
> ` >=u(p+u-1)-3au+B_beta`
> `   +uN_sup(B_beta)-2a`.                                `(ST-E)`

For a parameter-only use above `M(n)`, put

> `B_*=max(0,p(lambda+1-2p),pu-R_hat a)`.                 `(B*)`

Then `(ST-E)` may use `B_*` on the right.

The independent beta-sensitive U-edge cap remains

> `q<=au-B_beta+N_1`,                                    `(BQ)`

where `N_1=|{x:ell_x=1}|`.

For `u=O(p)` and `lambda=o(p)`, every finite limiting unmatched ratio still satisfies `u/p<27/14` asymptotically.

The repaired cylinder theorem is retained as a finite/equality diagnostic rather than the generic quadratic closure mechanism.

## 4. Complete A-edge witness channels

Every internal A-edge belongs to exactly one of three chosen criticality channels:

1. direct;
2. matched-B witness;
3. A/U unique-common-neighbour witness.

Write their total traffics as `D`, `P_B`, `C`; then

> `f=D+P_B+C`.                                             `(CH)`

Matched-B traffic satisfies

> `P_B<=sigma_0 a`,                                       `(MB1)`

and a switchable zero-signed matched subcore gives

> `L_A>=sigma_0(sigma_0-1)` for `sigma_0>=3`.             `(MB2)`

Thus with

> `R_A(L)=max(2,floor((1+sqrt(1+4L))/2))`,                `(RA)`

one has

> `sigma_0<=R_A(L_A)`.                                    `(MB3)`

The A/U fan geometry remains preserved: one source with distinct A/U witnesses creates an induced matching cut between heads and witnesses, and all witnesses have the complementary Boolean code. The self-priced complementary-pair fan cost `C_pair(d)` remains useful for equality/stability work.

Core A/U packages:

`project/research/post_ms/2026-09-18-a-edge-fan-rigidity-v1/`,

`project/research/post_ms/2026-09-18-fan-self-pricing-v1/`.

## 5. New combined complementary-pair channel capacity

For code `c`, write

`n_c=|A_c|`, `N_c=|(A union U)_c|`,

`w_c=N_c+n_c=2n_c+t_c`,

`L_c=sum_{x in A_c}epsilon_x`,

`S_c=sum_{z in (A union U)_c}epsilon_z`.

Let

> `D_0=5p+5u-3lambda-2`.

The preserved aligned-code self-pricing theorem is

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`.                      `(AC1)`

For a complementary pair `Pi={c,bar c}` with pair slack `s`, define

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`.      `(RC)`

Then

> `w_c,w_bar c<=R_code(s)` and
> `n_c,n_bar c<=R_code(s)/2`.                             `(RCH)`

Let `D_Pi` be direct A-edges crossing the pair and `C_Pi` the chosen A/U traffic sourced from its two codes. Combining the weighted direct-edge inequality with the preserved weighted A/U capacity gives the new exact theorem

> `2(lambda+1)(D_Pi+C_Pi)`
> ` <=R_code(S_Pi)(2L_Pi+S_Pi)`.                         `(CCP)`

Summing complementary pairs yields

> `2(lambda+1)(D+C)`
> ` <=R_code(S)(2L_A+S)`.                                `(GCC)`

Adding the matched-B channel gives the complete A-edge capacity

> `f`
> ` <=aR_A(L_A)`
> `   +[R_code(S)/(2(lambda+1))](2L_A+S)`.                `(ACE)`

Thus all three A-edge witness channels are now paid from the **actual** slack variables, without a free direct/AU channel split.

Using `(RQ2)`, this is equivalently a rooted-triangle capacity:

> `delta+Q`
> ` <=L_A+aR_A(L_A)`
> `   +[R_code(S)/(2(lambda+1))](2L_A+S)`.                `(RTC)`

Since `Q=p(p+u-1)+q`, it gives the direct U-edge ceiling

> `q`
> ` <=L_A+aR_A(L_A)`
> `   +[R_code(S)/(2(lambda+1))](2L_A+S)`
> `   -delta-p(p+u-1)`.                                  `(QCC)`

This should be intersected with the independent beta/source cap `(BQ)`.

### Source-conditioned finite version

Above `M(n)`, define

> `E_*=max(0,u(p+u-1)-3au+B_*+uN_sup(B_*)-2a)`.           `(E*)`

If `E_*>C_0`, the tuple is impossible. Otherwise put

> `L_*=C_0-E_*`.                                          `(L*)`

Then every candidate satisfies

> `f`
> ` <=aR_A(L_*)`
> `   +[R_code(C_0)/(2(lambda+1))](2L_*+C_0),             `(PACE)`

and therefore

> `q`
> ` <=aR_A(L_*)`
> `   +[R_code(C_0)/(2(lambda+1))](2L_*+C_0)`
> `   -(p-lambda)(p+u)+D_M-1`.                            `(PQCC)`

A finite diagnostic confirms that this fully collapsed parameter-only form is still too lossy to close the generic region by itself. The value of `(ACE)/(QCC)` is the **actual-slack coupling**; do not discard the split prematurely.

Core theorem:

`project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/COMBINED_COMPLEMENT_PAIR_CHANNEL_CAPACITY.md`.

## 6. Preserved direct-fan hole geometry

Fix an A-source `x` and its direct fan

`D_x={y in A:xy is direct}`, `d=|D_x|>=2`.

Put

`W=(V(G)\{v})\N(x)`,

`H_y=W\N(y)`,

`h_y=|H_y|=epsilon_x+epsilon_y-(lambda+1)`,

and

> `eta=sum_{y in D_x}h_y`.                                `(FH0)`

Write

> `w=|W|=a+epsilon_x`,
>
> `z=|V\(D_x union W)|=b+1-d-epsilon_x`.                 `(FH1)`

Also `w>=d+1`, `D_x` is independent, there are no D-Z edges, and

> `e(D_x,W)=dw-eta`.

If

> `eta<=d-2`,                                              `(FH2)`

there is a universal zero-hole leaf and the private-support injection holds from every internally active vertex of `W` into `Z`. With `t=|W^+|`,

> `t<=z`,
>
> `e(W,Z)<=zw-t(w-1)`,
>
> `e(G[W])<=binom(t,2)`,                                  `(FH3)`

and

> `m<=w(n-w)+binom(z,2)-t(w-1)+binom(t,2)-eta`.          `(FH4)`

The previous checkpoint closed `z<=3` for `n>=11`.

## 7. New bounded-surplus four-exception theorem

The `z=4` case is now also closed for sufficiently large graphs.

If `G[W]` is nonempty, `(FH4)` directly gives

> `m<=M(n)` for `n>=17`.                                  `(FHA)`

If `W` is independent, put `J=G[Z]`. Every W-vertex has a Z-neighbourhood dominating `J`, and every Z-vertex has a W-neighbour.

The four-vertex kernel is treated completely:

- `e(J)=0`: triangle-free;
- one edge: triangle criticality gives `m<=dw+2w+d+1`;
- `P3+K1`: the path-incidence bound gives `m<=dw+2w+4`;
- `2K2`: at most two Z escapes per doubled edge-family, giving `m<=dw+2w+6`;
- `K3+K1`: singleton triangle types give `m<=dw+2w+4`;
- `K1,3`: leaf-incidence hole charging gives `m<=dw+w+d+4`;
- `P4` and all four-vertex kernels with at least four edges admit a safe-incidence assignment. For every W-vertex with `r>=3` Z-neighbours, at least `r-2` triangular incidences must use forward D-witnesses. If `A_z` assignments land at coordinate `z`, then

  > `eta>=A_z(A_z-1)`.                                   `(SAFE1)`

  With

  > `R_eta=floor((1+sqrt(1+4eta))/2)`,

  this gives

  > `sum_z A_z<=4R_eta`,
  > `4R_eta-eta<=6`.                                     `(SAFE2)`

  Hence `P4` satisfies `m<=dw+2w+9`, and every `e(J)>=4` kernel satisfies

  > `m<=dw+2w+12`.                                       `(SAFE3)`

  The last bound is at most `M(n)` for `n>=23` under `w>=d+1` and `n=d+w+4`.

Therefore:

### Four-exception gate

For `n>=23`, if a direct fan has

> `eta<=d-2` and `z<=4`,                                  `(FHG)`

then the graph is triangle-free or `m<=M(n)`.

Equivalently, every live triangle-containing above-`M(n)` candidate of order at least 23 satisfies, for every direct fan,

> `eta>=d-1`,
>
> **or**
>
> `z>=5`.                                                  `(FH5)`

Using `z=b+1-d-epsilon_x`,

> `eta>=d-1`,
>
> **or**
>
> `d+epsilon_x<=b-4`.                                     `(FH6)`

For exact zero surplus,

> `d+epsilon_x<=b-4`.                                     `(FH7)`

If instead

> `d+epsilon_x>=b-3`,                                     `(FH8)`

then the surplus side must hold and

> `sum_{y in D_x}epsilon_y`
> ` >=d(lambda+2-epsilon_x)-1`.                           `(FH9)`

Thus the direct local slack bill now triggers one external exception earlier than at the previous checkpoint.

Core theorem:

`project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/DIRECT_FAN_BOUNDED_SURPLUS_FOUR_EXCEPTION_GATE.md`.

## 8. Audit / trust boundary

The new package contains an independent checker and frozen summary:

`project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/check_combined_channel_four_exception.py`,

`project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/COMBINED_CHANNEL_FOUR_EXCEPTION_AUDIT_SUMMARY.json`.

New audit support totals **1,173,503 checks with zero failures**, including:

- 500,000 random exact-integer combined complementary-pair capacity trials;
- all 110 dense four-vertex dominating-set safe-incidence cases (`e(J)>=4`), plus all five P4 high-degree cases;
- 100,001 integer hole-compression checks;
- 55,408 internally-active `z=4` second-extremal envelope checks;
- 517,979 independent-W kernel envelope checks in the claimed `n>=23` range.

These computations are audit support only. The promoted claims are the hand inequalities in the theorem notes.

Earlier audits and theorem packages remain preserved.

## 9. Live research frontier

The highest-value next move is now **not** another standalone fan lemma.

The compact live system is:

1. exact residual target `delta>=D_M`;
2. rooted transfer `delta+Q=L_A+f` and `f>=F_min`;
3. source/Hall beta support -> `E_U` floor;
4. independent beta-sensitive `q` ceiling `(BQ)`;
5. complete actual-slack A-edge channel capacity `(ACE)/(QCC)`;
6. direct bounded-surplus stability `(FH5)/(FH6)`.

The next structural synthesis should keep the actual split

> `S=E_U+L_A`

rather than substituting `S=C_0` everywhere, and eliminate `q,f` between `(FMIN)`, `(BQ)`, `(QCC)` and the residual identities. The point is now to determine whether any actual slack split can simultaneously support the forced rooted-triangle mass and all three A-edge witness channels.

If a surviving equality regime remains, the direct theorem says it must either accumulate at least one unit of hole surplus per fan leaf or maintain at least five external exceptions; the A/U side remains pair-self-priced. That is the current compact, externally reviewable stability frontier.

The order-12 `X_3` exception remains explicitly allowed throughout.
<!-- CURRENT-STATUS:END -->
