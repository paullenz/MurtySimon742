# First-strict buffer funnel: disjoint agreement blocks, outside-reservoir pricing, and rooted-slot feedback

Date: 2026-09-19

Status: **internal structural theorem package**, conditional on the audited rigid one-code complete-cut hypotheses. This note continues `BUFFER_FIRST_STRICT_LAYER.md` and `MATCHED_CHANNEL_SCOPE_AUDIT.md`; it does not reopen the closed buffer-equality descendants.

## 1. Audit reconciliation

Before this work the live `CURRENT_STATE.md`, root `README.md`, latest commits, the 19 September daily red-team audit, the repaired source-premise proof, and the independent actual-D2C Hall/pair-capacity regression were reread.

The trust boundary is unchanged:

- physical beta-source distinctness is proved from raw singleton criticality;
- global `(source,coordinate)` uniqueness is a selected-representative statement, not a raw-witness uniqueness statement;
- the graph-level regression still records no graph/formula mismatch and retains `X_3` as the mandatory hostile control;
- no bounded actual-D2C fixture realizes the full rigid complete-cut hypotheses, so everything below remains a conditional hand implication;
- exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain mandatory;
- the four-exception gate remains subordinate.

The preceding handoff explicitly asked for the density/support dichotomy inside the first strict unloaded-buffer layer. The present note stays on that line.

## 2. Setup inherited from the first-strict theorem

Keep the rigid one-code common-buffer notation:

- `A=X dotcup Y`, `|X|=x>=3`, `|Y|=y>0`, and `X--Y` is complete;
- every vertex of `Y` has tight code `d`, while every X-code is neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, and every vertex of `U_-` has code `bar d`;
- the unloaded hypotheses hold: `e(Y)=e(Y,U_d)=e(G[U_-])=0` and `d_Y(b)=0`;
- the first strict buffer layer has

  `epsilon_b=p-g+1`.

By `BUFFER_FIRST_STRICT_LAYER.md`, there is a unique `a_0 in X` with

`b a_0 notin E`,

while `b` is complete to `X\{a_0}` and to `U_o=U\U_-`.

For every `x in X\{a_0}`, choose one outside-U certificate `z_x in U_o` for the edge `bx`:

`b z_x in E`, `x z_x notin E`, `N(x) cap N(z_x)={b}`,

`c(z_x)=bar c(x)`, and `z_x` is anticomplete to `Y`.

Put

`S_0={i:c(a_0)_i != d_i}`,

`I_0=[p]\S_0`,

and for every `x != a_0`,

`S_x={i:c(x)_i != d_i}`, `I_x=[p]\S_x`.

Because neither `a_0` nor a buffer-neighbour has code `d` or `bar d`,

`1<=|S_0|<=p-1`, and every `I_x` is nonempty and proper.

The first-strict funnel theorem gives two types.

- **Type F:** `z_x a_0 notin E`; then `I_x={i}` for one `i in S_0`.
- **Type R:** `z_x a_0 in E`; then `S_0 subseteq S_x`, equivalently `I_x subseteq I_0`, and `x a_0 notin E`.

Let

`N=x-1`,

`F=# {Type-F vertices in X\{a_0}}`,

`R=N-F`,

and write `s=|S_0|`.

## 3. Structural unit I — fixed-foot overlap rigidity for Type R

### Theorem 3.1 — Type-R overlap collapse

Let `x,x'` be Type-R buffer neighbours. If

`I_x cap I_x' != empty`,

then

`z_x=z_x'`, `c(x)=c(x')`, and hence `I_x=I_x'`.

Therefore the agreement sets of **distinct Type-R code classes are pairwise disjoint**.

### Proof

Choose `i in I_x cap I_x'`. Since both vertices are Type R, the reverse funnel at coordinate `i` says

`N(q_i) cap N(a_0)={z_x}`

and also

`N(q_i) cap N(a_0)={z_x'}`,

where `q_i` is the graph-fixed `bar d` endpoint of tight fibre `i`. The left side is a fixed graph set, so `z_x=z_x'`.

Outside-U localization gives

`c(z_x)=bar c(x)`, `c(z_x')=bar c(x')`.

Thus the common physical witness forces `c(x)=c(x')`, and a binary code is determined by its agreement set with `d`, so `I_x=I_x'`. `square`

This uses only raw singleton common-neighbour identities. It does not use source-tuple injectivity.

## 4. Structural unit II — disjoint agreement-block normal form

Group `X\{a_0}` by tight code. For a code class `C`, let

`I_C={i:C_i=d_i}`

and let `m_C` be its multiplicity.

### Theorem 4.1 — disjoint agreement blocks

The distinct code classes represented in `X\{a_0}` have pairwise disjoint nonempty agreement blocks `I_C`.

More precisely:

1. a Type-F class has `I_C={i}` for one `i in S_0`;
2. distinct Type-F classes use distinct coordinates of `S_0`;
3. a Type-R class has `empty != I_C subseteq I_0`;
4. distinct Type-R classes have disjoint `I_C` by Theorem 3.1;
5. Type-F and Type-R blocks are automatically disjoint because they lie in `S_0` and `I_0`, respectively.

Hence, if `h` is the number of distinct buffer-neighbour code classes,

`sum_C |I_C| <= p`, and in particular `h<=p`.

For two distinct buffer-neighbour code classes `C,D`,

`d_H(C,D)=|I_C|+|I_D|`.

For a Type-F class `C`,

`d_H(c(a_0),C)=p-s+1`.

For a Type-R class `C`,

`d_H(c(a_0),C)=|I_0|-|I_C|`,

but `a_0` is nonadjacent to every vertex of that class.

### Proof

Only the distance identities require comment. Relative to `d`, a buffer-neighbour code agrees exactly on `I_C` and equals `bar d` elsewhere. Distinct blocks are disjoint, so two such codes differ exactly on `I_C union I_D`. The formulas involving `a_0` follow from its agreement set `I_0`. `square`

This is the promised density/support reduction: the live strict layer is no longer an arbitrary Boolean family. Its distinct buffer-neighbour codes form disjoint coordinate blocks.

## 5. Structural unit III — outside-witness support and reuse

Since `c(z_x)=bar c(x)`, the support of the selected outside witness relative to `d` is exactly `I_x`:

`{i:c(z_x)_i != d_i}=I_x`.

Thus witnesses belonging to distinct buffer-neighbour code classes lie in distinct U-code classes with pairwise disjoint nonempty supports.

There is an additional asymmetry between F and R.

### Lemma 5.1 — Type-R class has one graph-fixed selected witness

All vertices in a fixed Type-R code class use the same selected outside witness.

### Proof

Every vertex in the class has the same nonempty block `I_C`. Fix `i in I_C`. The reverse funnel for every class member identifies its selected witness with the unique graph set

`N(q_i) cap N(a_0)`.

Hence all chosen witnesses coincide. `square`

For Type F this conclusion need not hold: different physical witnesses with the same singleton support may share the same forward singleton foot. We do **not** impose raw-witness uniqueness there.

Let `m` be the number of distinct physical outside witnesses among the chosen certificates for the `N=x-1` buffer-neighbour edges, and let `t_w` be the number of heads served by witness `w`. Then

`sum_w t_w=N`, `t_w>=1`,

and every witness serves only one A-code class.

In the above-`M(n)`, `lambda>=0` regime, the preserved aligned-code self-pricing theorem gives

`n_c <= R_A`,

where

`R_A=floor(R_code(C0)/2)`

and

`R_code(S)=floor((D_code+sqrt(D_code^2+12S))/3)`,

`D_code=5p+5u-3lambda-2`.

Therefore

`h>=ceil(N/R_A)`,

`m>=h>=ceil(N/R_A)`,

and the disjoint-block theorem gives the new capacity gate

> `N <= p R_A`.                                          `(BLOCK-CAP)`

If `R_A=0`, the strict branch is impossible.

## 6. Structural unit IV — every distinct outside witness prices the Y-sources

### Theorem 6.1 — strict funnel source-slack floor

Every `y0 in Y` satisfies

`epsilon_{y0} >= p-g+1+m`.

Consequently

> `L_Y >= y(p-g+1+m)`.                                    `(LY-STRICT)`

### Proof

Because `e(Y)=0` and `X--Y` is complete,

`d_A(y0)=x`.

Every Y-source is nonadjacent to all `k` core vertices in `W_0`, to the buffer `b`, and to every one of the `m` distinct outside witnesses, since each outside witness is anticomplete to all of Y. Thus it has at least `k+1+m` U-nonneighbours.

Using

`epsilon_{y0}=p+u-x-d_U(y0)`

and `x=g+k`,

`epsilon_{y0}>=p-x+k+1+m=p-g+1+m`. `square`

This re-derives the source payment directly from degrees; no buffer-equality hypothesis is imported.

The common core and buffer lie in the outside pair

`P={d,bar d}`.

The preserved common-buffer core theorem gives

`E_core>=k(p+k-2)`,

and the present layer has `epsilon_b=p-g+1`. Hence the **pair-local physical floor** is

> `S_P >= P_0(m)`,                                        `(P0)`
>
> `P_0(m)=k(p+k-2)+(p-g+1)+y(p-g+1+m)`.

The exact crossing demand is still

`2xy<=Ccap_P(S_P)`,

with

`Ccap_P(S)=R_code(S)(g+2S/(lambda+1))`

because `h_P=0` in the one-sided pair.

Moreover `(ONE-P)` becomes automatic once `(P0)` and exact crossing capacity hold:

`Ccap_P+L_Y >= 2xy+y(p-g+1+m)`

`=y(p+2x-g)+y(1+m)`.

Thus `(ONE-P)` is satisfied with surplus `y(1+m)`. `(CROWD)` remains an independent lower bound and is retained.

Define the exact pair threshold

`Sigma_P(m)`

as the least integer `S` such that

1. `S>=P_0(m)`;
2. `S>=y(3y-D_code)` when the crowding right side is positive;
3. `Ccap_P(S)>=2xy`.

This definition deliberately keeps the pair variable local; no total-score substitution has occurred.

## 7. Structural unit V — outside-reservoir slack and the core-separation surcharge

For a selected outside witness `w`, let `t_w` be its served-head load.

Since `w` is anticomplete to Y and nonadjacent to every served head,

`epsilon_w >= [p-x+t_w]_+`.

The strict layer gives a further physical surcharge. Every core vertex `w_0 in W_0` has a graph-fixed head `h(w_0) in H_0` with `w_0 h(w_0) in E`. If that head is not `a_0`, its chosen outside witness `z` satisfies

`N(h(w_0)) cap N(z)={b}`.

Therefore `w_0 z` must be a nonedge. At most one core head can equal `a_0`. Put

`chi=1` if `a_0 in H_0`, and `chi=0` otherwise.

Then at least

`k-chi`

distinct `W_0--U_o` nonedges are forced.

If `m_F` denotes the number of distinct Type-F outside witnesses, each of those witnesses also misses `a_0`.

Summing the A- and U-nonneighbour contributions and using convex truncation gives

> `E_W >= [N+(k-chi)+m_F-m(x-p)]_+`.                     `(EW-STRICT)`

In particular the universally weakest choice `chi=1` gives

> `E_W >= [N+k-1+m_F-m(x-p)]_+`.                         `(EW-WEAK)`

The same `k-chi` physical U-nonedges sharpen the rooted triangle ceiling:

> `q <= binom(u,2)-binom(k+1,2)-(k-chi)`.                `(Q-STRICT)`

The first subtraction is the independent set `U_-=W_0 dotcup {b}`; the second counts distinct `W_0--U_o` holes.

These are graph-level incidences, not witness-incidence multiplicities.

## 8. Structural unit VI — Type-F versus `a_0` slack conservation

Every Type-R buffer neighbour is nonadjacent to `a_0`. Only Type-F heads can possibly be adjacent to it. Also `b a_0` is the unique buffer-X hole.

Hence

`d_A(a_0)<=y+F`,

`d_U(a_0)<=u-1`.

Since `a_0` has exactly `p` tight matched neighbours,

`d(a_0)<=p+y+F+u-1`.

With root degree `b=2p+u`,

> `epsilon_{a_0} >= p-y+1-F`.                             `(A0-SLACK)`

Equivalently, writing `g_0=p-y`,

> `F+epsilon_{a_0} >= g_0+1`.                            `(F-EPS)`

Because `c(a_0)` is neither `d` nor `bar d`, `epsilon_{a_0}` lies outside pair `P`.

Combining `(EW-STRICT)`, `(F-EPS)` and the exact pair threshold yields the genuinely pair-local resource gate

> `Sigma_P(m)+E_W+epsilon_{a_0} <= C0`.                  `(PAIR-OUT)`

Therefore, for fixed physical witness count `m`, every above-threshold survivor must have

> `F >= F_*(m):=[g_0+1+Sigma_P(m)+E_W-C0]_+`.            `(F-STAR)`

If `F_*(m)>N`, that witness-count row is impossible.

This is the clean strict-layer conservation law: buying a cheaper `a_0` forces Type-F heads; buying fewer Type-F heads spends score outside the audited pair.

## 9. Structural unit VII — local Hamming slots price Type F

For every `y0 in Y`, `d_A(y0)=x`. Its Hamming load across the complete cut is

`H_Y(y0)=s+sum_{x!=a_0}(p-|I_x|)`.

A Type-F head has `|I_x|=1`, hence radius `p-1` from `d`. A Type-R block lies in `I_0`, so

`p-|I_x| >= p-|I_0|=s`.

Therefore

> `H_Y(y0) >= x s+F(p-1-s)`.                             `(HY-F)`

The audited local witness-slot theorem gives

> `r_{y0} >= s+ceil(F(p-1-s)/x)`.                        `(RY-F)`

Every X-vertex has at least one Y-neighbour of a different tight code, so every X-vertex has `r_z>=1`. Summing gives

> `r >= x+y[s+ceil(F(p-1-s)/x)]`.                        `(R-F-S)`

For `0<=F<=x-1`, the bracket is nondecreasing in the integer `s`. Since `1<=s<=p-1`, the parameter-only form is

> `r >= a+y ceil(F(p-2)/x)`.                             `(R-F)`

Thus, for `p>=3`, even one forced Type-F head causes the discrete jump

> `F>0  ==>  r>=a+y`.

Together with `r=f+delta` this is already a defect statement. Using the exact rooted identity

`r=(p-lambda)(p+u)+q+E_U`,

it becomes

> `q+E_U >= a+y ceil(F(p-2)/x)-(p-lambda)(p+u)`.         `(QE-F)`

Combining with `(F-STAR)` gives a pair-to-residual feedback without replacing `S_P` by total slack before the geometry is extracted.

## 10. Structural unit VIII — class-count Hamming floor

The disjoint blocks give a second slot bound which does not mention F explicitly.

Let the distinct buffer-neighbour classes have multiplicities `m_j` and block sizes `q_j`. Then

`sum m_j=N`, `m_j<=R_A`, `q_j>=1`, `sum q_j<=p`.

Let

`h_0=ceil(N/R_A)`.

If `h_0>p`, `(BLOCK-CAP)` already closes the branch.

If `h_0=1`, the exclusion of code `d` gives the safe baseline Hamming load `H_Y(y0)>=x`.

If `h_0>=2`,

`sum m_j q_j`

`=N+sum m_j(q_j-1)`

`<=N+R_A(p-h)`

`<=N+R_A(p-h_0)`.

Since `s>=1`, every Y-source therefore has

> `H_Y(y0) >= H_*`,                                      `(H-STAR)`
>
> `H_*=1+N(p-1)-R_A(p-h_0)`.

Hence

> `r >= x+y ceil(H_*/x)`.                                `(R-CLASS)`

This is the exact relaxed optimum under only disjoint-block and class-cap information; it becomes active once at least two code classes are forced.

## 11. One-witness polarization

The structurally cheapest physical reservoir deserves to be isolated.

### Theorem 11.1 — `m=1` polarization

If all `N=x-1` buffer-neighbour edges use one physical outside witness, then all buffer neighbours have one code. Consequently exactly one of the following holds:

1. **all-F:** `F=N`, with a single agreement coordinate `I={i} subseteq S_0`;
2. **all-R:** `F=0`, with one nonempty block `I subseteq I_0`.

No mixed F/R one-witness geometry exists.

In the all-F case the unique outside witness is anticomplete to **all of A**, so

> `epsilon_z>=p`.                                        `(M1-F)`

Every Y-source has Hamming load at least

> `1+N(p-1)`,

so

> `r_y>=ceil((1+N(p-1))/x)`.

In the all-R case the unique witness has A-neighbourhood exactly `{a_0}`, so

> `epsilon_z>=p-1`,                                      `(M1-R1)`

`a_0` is isolated in `G[X]`, and

> `epsilon_{a_0}>=g_0+1`.                                `(M1-R2)`

The Hamming-cheapest all-R subcase is

`s=1`, `I=I_0`,

in which **all of X has one code at Hamming distance one from d**.

This is now the principal equality geometry to attack if the strict layer survives the resource gates.

## 12. Exact finite resource cone for diagnostics

For a finite abstract check, keep the structural variables rather than flattening them.

Let `h_F` and `h_R` be the numbers of Type-F and Type-R code classes. Above threshold,

`h_F>=ceil(F/R_A)` when `F>0`,

`h_R>=ceil((N-F)/R_A)` when `N-F>0`.

Support geometry requires

`h_F<=s`, `h_R<=p-s`, `1<=s<=p-1`.

A Type-R class contributes exactly one selected physical witness. If `m_F` is the number of physical Type-F witnesses, then

`h_F<=m_F<=F`,

`m=h_R+m_F`.

For fixed `(F,m)`, the smallest possible Hamming-slot value is obtained at the smallest feasible

`s=max(1,h_F)`.

The exact necessary diagnostic inequalities are then:

1. `Sigma_P(m)` is finite;
2. `(PAIR-OUT)` with `(EW-STRICT)`;
3. `(R-F-S)`;
4. `(Q-STRICT)`;
5. `E_U<=C0-max{phi(g), L_Y+epsilon_{a_0}}`, with `L_Y` from `(LY-STRICT)`.

No finite scan over these variables is a realizability proof. Its purpose is to identify the surviving equality geometry for the next hand proof.

## 13. Diagnostic replay

The companion checker scans the same broad abstract box used by recent one-code diagnostics:

`3<=p<=18`, `1<=u<=18`, `lambda>=0`,

restricted to the principal `g_0=p-y>=1` first-strict common-buffer rows satisfying the coarse predecessor score floor

`phi(g)+k(p+k-2)+(p-g+1)<=C0`.

This deliberately defines an abstract parameter baseline; it is **not** a count of D2C graphs.

Recorded counts after enforcing the structural consistency between F/R classes and physical witnesses are:

- coarse first-strict rows: **248,798**;
- rejected by the exact pair/outside-reservoir gate before residual capacity: **23,646**;
- pair/outside survivors: **225,152**;
- additional rows rejected by the rooted-slot plus physical-q residual gate: **36,240**;
- final abstract survivors: **188,912**.

Among the minimum-cost retained diagnostic routes, the one-witness polarized geometries dominate:

- **129,415** select the all-F `m=1` route;
- **31,856** select the all-R `m=1` route.

These route counts are optimizer diagnostics, not graph counts and not uniqueness claims. Their mathematical value is that the next hand attack should focus first on the two one-witness polarized geometries, especially the all-R cheapest subcase `s=1`, `I=I_0`.

The checker also verifies the support-block arithmetic, the exact pair-local `Ccap_P` threshold, `(CROWD)`, the core-separation surcharge, and the residual ceilings independently of the theorem prose.

## 14. Trust boundary and next move

What is now proved conditionally inside the rigid first-strict branch:

1. distinct buffer-neighbour codes have pairwise disjoint agreement blocks;
2. Type-R classes have graph-fixed outside witnesses;
3. all `x-1` buffer neighbours force a physical outside-reservoir population and the source floor `(LY-STRICT)`;
4. pair-local score has the explicit floor `(P0)` and `(ONE-P)` is dominated after exact crossing capacity;
5. core-head certificates force at least `k-1` additional physical U-U holes and the strengthened `(EW-WEAK)/(Q-STRICT)` bills;
6. Type-F multiplicity trades exactly against `a_0` slack via `(F-EPS)`;
7. Type-F multiplicity is converted into unused rooted slots by `(R-F)`;
8. the cheapest `m=1` reservoir polarizes completely into all-F or all-R.

The next hand target should **not** open `m=g+2`, `z=2`, or the four-exception gate. It should attack the polarized one-witness geometries:

- **all-R first:** use `N_A(z)={a_0}`, `a_0` isolated in `G[X]`, `epsilon_z>=p-1`, `epsilon_{a_0}>=p-y+1`, and the cheapest code geometry `d_H(c(X),d)=1`; trace raw criticality of the remaining X- and U-edges and feed any forced holes into `(Q-STRICT)`;
- **all-F second:** exploit `N_A(z)=emptyset`, `epsilon_z>=p`, and the large exact Y-side Hamming load `1+(x-1)(p-1)`.

If those two polarizations are closed, the surviving multi-witness rows already have disjoint support blocks and can be attacked by the same pair/slot resource cone rather than by reopening older equality descendants.
