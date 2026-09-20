# Residual-one k=2 compressed global one-half barrier

Date: 2026-09-20

Status: **same-session conditional strengthening** of `ONE_CODE_R1_K2_COMPRESSED_GLOBAL_7_16.md`, downstream of the same audited residual-one `k=2`, `J2=empty` interface. No finite scan is used. The earlier `7/16` bound remains correct but is superseded by the stronger calculation below on the same compressed normal form.

## 1. One more consequence of W_s--U_bar(d) anticompleteness

The residual-one hub package already gives

`E(W_s,U_{bar d})=empty`.

This can also be replayed directly: if `z_h in W_s` and `w in U_{bar d}` were adjacent, same-code U--U criticality would require a complementary A-witness in the `d`-class, namely Y. In the orientation sourced at `w`, the singleton head `z_h` is unavailable because `z_h` is Y-anticomplete. In the orientation sourced at `z_h`, the K-head h is an additional common neighbour because `h in N_A(z_h)` and K is complete to Y. Hence no such edge exists.

Therefore every escape vertex that touches `W_s` has code different from `bar d`.

At `J2=empty`, the A-code repertoire has sizes

- `|A_d|=|Y|=p-1`;
- `|A_C|=|K|=2`;
- every radius-one head code has size one;
- all other A-code classes are empty.

So for any source `w` with `c(w)!=bar d`, the complement-witness capacity theorem gives

> `d_P(w)<=2`                                             `(HG-CAP)`

whenever P is a set of complement-empty proper-support q_j-nonneighbours.

This applies automatically to every F1, W-heavy and mixed escape because each touches W_s.

## 2. In the compressed normal form, P is almost anticomplete to the whole escape reservoir

Keep the compressed hypotheses from the predecessor note:

1. all but `o(p)` vertices of the W_s-free non-K-heavy class D are proper-support q_j-nonneighbours; call this dominant set P, with `|P|=(delta+o(1))p`;
2. all but `o(p)` K-heavy vertices R miss q_j.

P is independent by the cross-code localization theorem.

Every nonhub R-vertex also has code different from `bar d`: the code `bar d` differs from d at the residual coordinate j and therefore sees q_j. Hence `(HG-CAP)` applies to all but `o(p)` vertices of R as well.

For T=F1 union W-heavy and for M=mixed, `(HG-CAP)` applies without any hub assumption because these vertices touch W_s.

Thus every vertex of `E\P`, except for `o(p)` compressed exceptions, has at most two neighbours in P. Consequently

> `M_U(P,E\P) >= (delta(1-delta)-o(1))p^2`,              `(HG-CROSS)`
>
> `M_U(P) >= (delta^2/2-o(1))p^2`.                       `(HG-IN)`

Adding,

> **`M_U(P,E) >= (delta-delta^2/2-o(1))p^2`.**           `(HG-M)`

This strengthens the predecessor R--P-only missing-edge bill and, crucially, is independent of how the non-D mass is split among R, T and M.

## 3. Add the K-heavy Y-capacity block

Let alpha be the K-heavy density and phi the F0 density. Only F0 can supply the exceptional U-witness capacity for K-heavy--Y certificates, so the preserved Y-capacity theorem gives

`Z_Y(R)/p^2 >= alpha(1-phi)-o(1)`.

Since `phi<=delta`,

> `Z_Y(R)/p^2 >= alpha(1-delta)-o(1)`.                  `(HG-Y)`

The Y--R block is disjoint from the missing-U block `(HG-M)`. Therefore the compressed geometry satisfies

> **`liminf D_phys/p^2 >=`**
> **`L2 := delta-delta^2/2 + alpha(1-delta)`.**          `(HG-L2)`

## 4. Combine with the additive class floor

The predecessor additive partition theorem gives

`liminf D_phys/p^2 >= delta/2 + vartheta(1+alpha)+mu`,

where

`alpha+delta+vartheta+mu=1`.

Because `1+alpha>=1`,

> **`liminf D_phys/p^2 >=`**
> **`L1 := 1-alpha-delta/2`.**                           `(HG-L1)`

The two bounds are simultaneous.

If `L1<1/2`, then

`alpha>(1-delta)/2`.

Since `(HG-L2)` is increasing in alpha for `delta<1`,

`L2 > delta-delta^2/2 + (1-delta)^2/2 = 1/2`.

At `delta=1`, `L2=1/2` directly. Hence for every admissible alpha,delta,

> **Compressed global half barrier**
>
> **`liminf D_phys/p^2 >= 1/2`.**                        `(HG-HALF)`

This strictly supersedes the predecessor `7/16` bound on the same compressed normal form.

## 5. Equality structure before mixed-slack feedback

Equality in both `(HG-L1)` and `(HG-L2)` requires

`alpha=(1-delta)/2`,

`vartheta=0`,

`mu=(1-delta)/2`.

Equality in the Y-cap step additionally requires `phi=delta`, so asymptotically all of D is F0. Thus the relaxed equality continuum is

> **`R : F0 : M = (1-delta)/2 : delta : (1-delta)/2`,**  `(HG-EQ0)`

with no linear F1/W-heavy sector.

## 6. Mixed vertices receive an extra F0/P slack bill

A mixed vertex already has the mandatory mixing slack floor `epsilon_w>=p+1`. That proof accounts for

- two missing pairs inside `K union W_s`, and
- `p-1` missing matched-fibre pairs.

These sets do not contain escape vertices from P.

But every mixed vertex touches W_s, hence has code different from `bar d`, so `(HG-CAP)` gives at most two neighbours in P. Therefore each mixed vertex has at least `|P|-2` **additional** missing U-neighbours, disjoint from the pairs used in the `p+1` mixing proof. Thus

> **`epsilon_w >= p+|P|-1` for every mixed w.**          `(HG-MIXSLACK)`

Asymptotically the mixed-slack coefficient is `1+delta`, not merely one.

Likewise T-to-P missing U-pairs are disjoint from the predecessor T bill, so the T coefficient can only increase. Hence, for fixed alpha,delta, the cheapest destination for the residual mass remains M and the additive bound sharpens to

> `L1' = delta/2 + (1-alpha-delta)(1+delta)`.             `(HG-L1P)`

The half barrier remains the global minimum, but the interior equality continuum `(HG-EQ0)` is destroyed: substituting `alpha=mu=(1-delta)/2` gives

`L1'=(1+delta-delta^2)/2 > 1/2`

for every `0<delta<1`.

Therefore equality at coefficient `1/2` can occur only at the two extreme relaxed endpoints:

1. `delta=1`: asymptotically pure compressed F0;
2. `delta=0`: asymptotically `R:M=1:1` with no D/T mass.

## 7. Strategic consequence

The low-k compressed problem has now split into two literal hostile endpoints rather than a broad class mixture.

### Endpoint A: pure F0

Almost every escape is

- K-free and W_s-free;
- a q_j-nonneighbour;
- proper-support (indeed cheap support is sparse);
- contained in the global independent proper-support set P.

The exact F0 sector identity shows that equality in its `1/2` physical floor forces almost all remaining H/Y deficit and slack to vanish. This is a rigid graph-level object and should be attacked directly by A--U edge criticality and maximum-degree saturation.

### Endpoint B: half K-heavy / half mixed

There is asymptotically no F0 repair capacity. Hence K-heavy vertices have `d_Y<=1` literally, while every mixed vertex has exactly one K-neighbour and one selected-witness neighbour with the same head index by the beta cross exclusions. This endpoint should be attacked by R--M U--U criticality and the two aligned mixed types.

No claim is made that either endpoint is realizable. The point is that the compressed asymptotic optimization is now exact enough that further scalar refinement should be subordinate to these two raw-criticality classifications.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; all statements remain conditional downstream mathematics pending independent hostile replay.