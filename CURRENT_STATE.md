# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_RESIDUAL_SPLIT_LOCAL_COUPLING_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed and is not a live branch. The active branch is the triangle-containing unmatched/errorful antipode regime.

The current structural spine is

`residual defect -> rooted-triangle transfer -> exact unmatched-slack A-edge demand -> source/Hall beta support -> complete witness channels -> pair/local stability`.

This checkpoint adds four connected results:

1. the exact residual identity is rewritten as `f=(p-lambda)(p+u)+q+E_U-delta`, so every unit of unmatched slack is also one unit of forced A-edge demand;
2. `s<=au` gives a lower bound on `q`, while the beta-sensitive q theorem plus a new load-one compression gives a parameter-only q ceiling and hence an additional `E_U` floor;
3. the matched-B channel gets a second aligned-code capacity using the fact that the gamma complementary pairs partition the `p` tight fibres;
4. the complete scalar synthesis is monotone and one-dimensional, but a finite diagnostic shows that this global collapse is still too weak: the next gain must remain complementary-pair/local rather than replacing pair slack by total `S`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is only the eventual comparison threshold.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 D2C graph has been reconstructed exactly and is isomorphic to the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`.

Its rooted-triangle transfer is endpoint-saturated: `Q-f=12`. At the canonical root `u=0`, `F_min=0=f`, and `A` is independent. The new residual split below is exactly `0=0` on this graph.

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

### New exact residual split

Rearranging `(RQ3)` gives

> `f=(p-lambda)(p+u)+q+E_U-delta`.                        `(RSF)`

Thus every above-`M(n)` candidate (`delta<=D_M-1`) satisfies

> `f>=F_0+q+E_U`,                                         `(RSF+)`

where

> `F_0=(p-lambda)(p+u)-D_M+1`.

The previous bound `F_min=F_0+q` remains valid but is weaker by exactly `E_U`.

Above threshold,

> `S<=C_0:=2(D_M-1)+lambda(p+u)-p`.                       `(C0)`

Core residual packages:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/`,

`project/research/post_ms/2026-09-18-residual-split-aligned-matched-v1/`.

## 3. Preserved source/Hall stack and new q/E coupling

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x`. The exact source-tuple hierarchy remains

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`     `(FDPr)`

for every `r>=3`, with integrated deficit profile

> `sum_{x in L}(p-ell_x)>=Phi_r(|L|)`.                    `(IST)`

Put `B_beta=sum_x ell_x`. The main beta floors are

> `B_beta >= [pu-R_hat a]_+`,                             `(STL)`
>
> `B_beta >= p(lambda+1-2p)_+`.                           `(RBF)`

Applying `(IST)` to all of `A` gives

> `B_beta<=ap-Phi_r(a)`.                                  `(ITB)`

For positive beta support `A_+={x:ell_x>0}`, define the preserved support floor `N_sup(B)`. Then

> `|A_+|>=N_sup(B_beta)`,                                 `(NSUP)`

and

> `E_U`
> ` >=u(p+u-1)-3au+B_beta`
> `   +uN_sup(B_beta)-2a`.                                `(ST-E)`

For parameter-only use put

> `B_*=max(0,p(lambda+1-2p),pu-R_hat a)`,                 `(B*)`

and

> `E_*=max(0,u(p+u-1)-3au+B_*+uN_sup(B_*)-2a)`.          `(E*)`

The independent beta-sensitive U-edge cap remains

> `q<=au-B_beta+N_1`,                                     `(BQ)`

where `N_1=|{x:ell_x=1}|`.

### New cross-edge q floor

Since `s<=au`, the identity for `E_U` gives

> `q>=ceil([u(lambda-p)-E_U]_+/2)`.                       `(QL)`

### New load-one compression

Put `m_0=min(p,u)`. If `m_0>=2`, then

> `N_1<=floor((m_0a-B_beta)/(m_0-1))`.                    `(N1)`

Hence, using `B_beta>=B_*`,

> `q<=Q_beta^*`
>
> `:=min(binomial(u,2),`
> `       au-B_*+floor((m_0a-B_*)/(m_0-1)))`.             `(QB*)`

Therefore

> `E_U>=[u(lambda-p)-2Q_beta^*]_+`.                       `(ECROSS)`

The combined parameter-only unmatched-slack floor is

> `E_hat=max(E_*,[u(lambda-p)-2Q_beta^*]_+)`.             `(EHAT)`

For `m_0=1`, use only the trivial `q<=binomial(u,2)` in this step.

## 4. Complete A-edge witness channels

Every internal A-edge belongs to exactly one chosen channel:

1. direct;
2. matched-B witness;
3. A/U unique-common-neighbour witness.

Write their total traffics as `D`, `P_B`, `C`; then

> `f=D+P_B+C`.                                             `(CH)`

The preserved matched-B self-pricing theorem gives

> `P_B<=aR_A(L_A)`,                                       `(MB)`

where

> `R_A(L)=max(2,floor((1+sqrt(1+4L))/2))`.                `(RA)`

For Boolean code `c`, write

`n_c=|A_c|`, `N_c=|(A union U)_c|`,

`w_c=N_c+n_c=2n_c+t_c`,

and let `S_c,L_c` be the corresponding total/A-slack.

With

> `D_0=5p+5u-3lambda-2`,

aligned-code self-pricing gives

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`.                      `(AC1)`

Define

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`.      `(RC)`

Then for every complementary pair with slack at most `S`,

> `n_c,n_bar c<=R_code(S)/2`.                             `(RCH)`

The preserved combined direct+A/U theorem is

> `D+C`
> ` <=[R_code(S)/(2(lambda+1))](2L_A+S)`.                `(GCC)`

## 5. New aligned-code matched-B capacity

The preserved matched-foot complementary-pair inequality is

> `P_Pi`
> ` <=g_Pi max(n_c,n_bar c)`
> `   +sum_{i in I_Pi}min(t_i^0,t_i^1)`.                 `(CP4)`

The gamma complementary pairs partition the `p` tight fibres, so

> `sum_Pi g_Pi=p`.                                        `(GP)`

Fibre polarization gives

> `(lambda+1)sum_i min(t_i^0,t_i^1)`
> ` <=R_A(L_A)L_A`.                                       `(POL)`

Combining `(GP)`, `(POL)` and `(RCH)` gives the new second matched-B cap

> `P_B`
> ` <= pR_code(S)/2`
> `    +R_A(L_A)L_A/(lambda+1)`.                          `(AMB)`

Therefore

> `P_B`
> ` <=min(aR_A(L_A),`
> `       pR_code(S)/2+R_A(L_A)L_A/(lambda+1))`.          `(AMB+)`

Adding `(GCC)` gives the refined complete channel envelope

> `f`
> ` <=min(aR_A(L_A),`
> `       pR_code(S)/2+R_A(L_A)L_A/(lambda+1))`
> `   +[R_code(S)/(2(lambda+1))](2L_A+S).                 `(ACE+)`

## 6. One-dimensional split feasibility

For fixed `S`, substitute `L_A=S-E` into `(ACE+)` and call the right side `Cap(S,E)`.

Then:

- `Cap(S,E)` is nondecreasing in `S`;
- `Cap(S,E)` is nonincreasing in `E`;
- `chi(E):=E+ceil([u(lambda-p)-E]_+/2)` is nondecreasing in `E`.

Using `(RSF+)`, `(QL)`, `S<=C_0`, and `E_U>=E_hat`, every above-threshold candidate satisfies

> `F_0+chi(E_hat)<=Cap(C_0,E_hat)`.                        `(SCF)`

Failure of `(SCF)` is a finite parameter-only exclusion.

This is the strongest current global scalar synthesis of the source/Hall and complete-channel stacks.

Core theorem:

`project/research/post_ms/2026-09-18-residual-split-aligned-matched-v1/RESIDUAL_SPLIT_ALIGNED_MATCHED_CAPACITY.md`.

## 7. Preserved direct bounded-surplus stability

For a direct fan `D_x` of order `d`, put

`W=(V\{v})\N(x)`,

`h_y=epsilon_x+epsilon_y-(lambda+1)`,

`eta=sum_{y in D_x}h_y`,

`z=|V\(D_x union W)|=b+1-d-epsilon_x`.

The four-exception theorem remains:

> for `n>=23`, if `eta<=d-2` and `z<=4`, then the graph is triangle-free or `m<=M(n)`.

Thus every live triangle-containing above-`M(n)` candidate of order at least 23 satisfies, for every direct fan,

> `eta>=d-1`,
>
> or
>
> `z>=5`.                                                  `(FH5)`

Equivalently,

> `eta>=d-1`,
>
> or
>
> `d+epsilon_x<=b-4`.                                     `(FH6)`

Core theorem:

`project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/DIRECT_FAN_BOUNDED_SURPLUS_FOUR_EXCEPTION_GATE.md`.

## 8. Audit and diagnostic outcome

New package:

`project/research/post_ms/2026-09-18-residual-split-aligned-matched-v1/`.

Its checker records **850,000 algebra checks with zero failures**:

- 200,000 exact residual-split checks;
- 200,000 cross-edge q-floor checks;
- 150,000 load-one compression checks;
- 200,000 aligned matched-cap algebra checks;
- 100,000 split-cap monotonicity checks.

A conservative finite scalar diagnostic (`3<=p<=30`, `1<=u<=2p`, root-imbalance beta floor plus `r=3` source support) finds:

- 56,238 parameter tuples;
- 10,298 already beta-impossible;
- 45,940 remaining scalar tuples;
- zero additional generic closures from either the old collapsed channel criterion or `(SCF)`.

The aligned matched-B cap can reduce the old scalar channel allowance (minimum observed ratio `9/11`), but on all 21,739 scanned tuples with `F_0>0`, the old branch `aR_A(L_A)` is already the smaller matched cap. Thus the improvement does not attack the forced-A-edge region in the conservative scan.

This is the key strategic obstruction from the session: **another global replacement of pair slack by total `S` is unlikely to close the live branch.**

The computations are audit/diagnostic support only; the promoted claims are the hand inequalities above.

## 9. Live research frontier

The next move should keep complementary-pair allocation or direct-fan locality intact.

The compact live system is now:

1. exact target `delta>=D_M`;
2. exact split `(RSF)`, so unmatched slack itself raises forced A-edge demand;
3. source/Hall beta support plus `(QL)/(QB*)` gives `E_U` floors;
4. complete actual-slack channel capacity `(ACE+)`;
5. direct bounded-surplus stability `(FH5)/(FH6)`;
6. A/U complementary-pair self-pricing from the preserved fan packages.

The finite diagnostic says the scalar envelope has too much room. The highest-value next theorem should therefore be **local**: either a complementary-pair version of the residual demand that prevents all forced `f` from moving to unrelated slack-rich pairs, or an aggregate use of `(FH5)` showing that a large direct share of the forced A-edge traffic necessarily pays hole surplus before the channel sum is globalized.

Do not return to the closed mixed `{4,5}` ladder, and do not optimize for first-proof priority on Erdős #742.

The order-12 `X_3` exception remains explicitly allowed throughout.
<!-- CURRENT-STATUS:END -->
