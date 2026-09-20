# Residual-one k=2 compressed W_s-free global 7/16 barrier

Date: 2026-09-20

Status: **same-session conditional structural synthesis**, downstream of the residual-one `k=2`, `J2=empty` package, the hostile-repaired cross-code complement localization/capacity theorem, the K-heavy Y-capacity theorem, and the preserved escape-class partition. No finite scan is used.

This note reconciles the newest complement-capacity work with the older D1/F0 split. It also extends the private-spoke/hub dichotomy to the fully-free `F0` class and identifies the next asymptotic normal form.

## 1. Audit replay of the cross-code capacity input

For an edge `wt` with `w,t in U`, both endpoints share the root. Hence the criticality witness for either singleton orientation must lie in `A`, not in the rooted `B` layer. If the singleton head is the opposite U-endpoint, the source and A-witness may share no matched endpoint, so their tight-fibre codes are coordinatewise complementary.

Thus every U--U edge must orient from an endpoint whose complementary A-code is represented. For a fixed source `w` and fixed physical A-witness `a`, the graph-fixed set `N(w) cap N(a)` has only one singleton head. Therefore, for any target set `V` whose vertices have complement-empty A-codes,

`d_V(w) <= |A_{bar(c(w))}|`.

At `J2=empty`, every proper-support `q_j`-nonneighbour has complement-empty A-code; a full-support `q_j`-nonneighbour has complementary class `K`, of size two. Hence the proper-support nonhub set is independent, and every nonhub source has at most two neighbours in it. This hostile replay found no additional witness location or orientation omitted by the predecessor theorem.

## 2. The private-spoke theorem extends to F0

Let `t in F0`, so `t` is anticomplete to both `K={a,b}` and the selected-witness pair `W_s={z_a,z_b}`. Suppose `tq_i` is an edge for a private coordinate `i in I=[p]\{j}`.

Raw rooted B-edge criticality again has exactly the two familiar outcomes.

Forward: the A-witness containing `q_i` is forced to be `h_i`, so

`N(t) cap N(h_i)={q_i}`,

and since every Y-vertex is adjacent to `h_i`, one gets `N_Y(t)=empty`.

Reverse: a K-witness is unavailable because `t` has no K-neighbour; a Y-witness fails because `h_i` would be an additional common neighbour; and `h_i` itself contains `q_i`. Hence the witness is some `h_l in H\{h_i}` with

`N(q_i) cap N(h_l)={t}`.

Therefore the W_s-free private-spoke forward/Y-killing versus reverse/H-consuming dichotomy does not require `d_K(t)>=1`; it also holds for fully-free F0 vertices.

## 3. F0 residual-hub neighbours have the same expensive split

Now suppose `t in F0` and `tq_j` is an edge. At the all-radius-one endpoint `N_A(q_j)=K`.

In the forward orientation, the A-witness containing `q_j` is therefore one of the two K-heads. The singleton equation forces `t` to be Y-anticomplete, because K is complete to Y, and also anticomplete to every K-heavy escape, because every K-heavy escape is adjacent to both K-heads.

In the reverse orientation, K is unavailable (F0 is K-free), Y is impossible because the two K-heads would be extra common neighbours of `q_j` and a Y-witness, and the witness is forced into H. Distinct reverse F0 hub-neighbours require distinct matched heads, and those heads miss every other F0 hub-neighbour. Thus a reverse population of size `v` inside a hub-neighbour set of size `tau` creates at least

`v(tau-1)`

located H--U holes.

So a positive-density F0 hub-neighbour population pays either a linear-times-p Y/R block on its forward part or a quadratic H--U rectangle on its reverse part. The cheap F0 endpoint is therefore driven toward `q_j`-nonneighbours for the same structural reason as D1.

## 4. Cheap F0 private support is sparse

Apply the extended private-spoke dichotomy to a set N of nonhub F0 vertices. Let

`L=sum_{t in N}|S(t)|`

be total private-support incidence and let `f0` count vertices with at least one forward private spoke. The same argument as for D1 gives

`Z_{Y,N} >= f0(p-1)`

and, after retaining only reverse incidences and using fixed-coordinate witness injectivity,

`Z_{H,N} >= max{0,[L_R^2/(p-1)-L_R]/(p-1)}`,

where `L_R >= [L-f0(p-1)]_+`.

Hence a positive normalized support density has a positive located-hole price. In particular, any asymptotically cheap F0 population must have average private support `o(p)`. Since a full support has size `p-1`, only `o(p)` cheap F0 vertices can use the exceptional full-support code.

Thus the same compression that was previously proved for D1 extends to F0: up to lower-order mass, cheap W_s-free non-K-heavy escapes are proper-support `q_j`-nonneighbours.

## 5. Compressed W_s-free sector: global missing-U bill

Use the preserved escape partition

- `R`: K-heavy, density `alpha`;
- `D`: W_s-free non-K-heavy (F0 or D1), density `delta`;
- `T`: F1 plus W-heavy, density `vartheta`;
- `M`: mixed, density `mu`;

with `alpha+delta+vartheta+mu=1` asymptotically.

Assume the compressed normal form:

1. all but `o(p)` vertices of D are proper-support `q_j`-nonneighbours;
2. all but `o(p)` vertices of R miss `q_j`.

Let P be the dominant proper-support part of D. Then the cross-code theorem gives

`M_U(P) >= (delta^2/2-o(1))p^2`.

Every nonhub R-vertex has at most two neighbours in P, regardless of whether its own support is proper or full. Therefore

`M_U(R,P) >= (alpha delta-o(1))p^2`.

These missing-U blocks are disjoint.

Let `phi` be the F0 density. Only F0 can provide the exceptional repair capacity for K-heavy--Y certificates, and `phi<=delta`. The preserved Y-capacity theorem therefore gives

`Z_Y(R)/p^2 >= alpha(1-phi)-o(1) >= alpha(1-delta)-o(1)`.

This Y--R block is disjoint from the two missing-U blocks. Consequently every compressed configuration satisfies

> `liminf D_phys/p^2 >= alpha + delta^2/2`.              `(CG-L2)`

where `D_phys=E_U+Z_X+Z_Y+M_U`.

## 6. Combine with the additive class floor

The predecessor class-additive theorem gives

`D_phys >= d(p-2)/2 + theta(p-1+r)+m(p+1)`.

After normalization,

`liminf D_phys/p^2 >= delta/2+vartheta(1+alpha)+mu`.

Since `vartheta+mu=1-alpha-delta` and `1+alpha>=1`,

> `liminf D_phys/p^2 >= 1-alpha-delta/2`.                `(CG-L1)`

The two bounds `(CG-L1)` and `(CG-L2)` are simultaneous, so

`liminf D_phys/p^2 >= max{1-alpha-delta/2, alpha+delta^2/2}`.

Minimize over `alpha,delta>=0`, `alpha+delta<=1`. For fixed delta the first term decreases and the second increases with alpha, so the minimum occurs at equality,

`alpha=(2-delta-delta^2)/4`.

The common value is

`(2-delta+delta^2)/4`,

whose minimum on `[0,1]` occurs at `delta=1/2`. Therefore

> **Compressed global barrier**
>
> `liminf D_phys/p^2 >= 7/16 = 0.4375`.                 `(CG-7/16)`

The relaxed equality proportions are

`alpha=5/16`, `delta=1/2`, `vartheta=0`, `mu=3/16`.

Moreover equality in the Y-cap step requires `phi=delta`, so the entire D-sector must asymptotically be F0 rather than D1. Thus the new putative cheap endpoint is no longer the 31:69 K-heavy/D1 geometry from the predecessor unweighted synthesis. Under compression it migrates to the approximate ratio

> `R : F0 : M = 5 : 8 : 3`,

with no linear F1/W-heavy sector.

## 7. Strategic consequence

This does not close the low-k ray: the theorem is conditional on the compressed nonhub/proper-support normal form, and positive-density departures from that normal form have their own hub/support penalties that have not yet been jointly optimized with `(CG-7/16)`.

But the live asymptotic target has changed materially. Any configuration trying to stay below the compressed `7/16` barrier must keep a positive-density population outside the compressed W_s-free normal form, or exploit the mixed sector strongly enough to change the simultaneous optimization. The next raw-criticality attack should therefore be on the new `R:F0:M = 5:8:3` endpoint, especially F0--mixed and mixed--private-coordinate certificates, while retaining the explicit hub/support departure penalties rather than replacing them by an unweighted scalar.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; all statements remain conditional downstream mathematics pending the next independent hostile audit.