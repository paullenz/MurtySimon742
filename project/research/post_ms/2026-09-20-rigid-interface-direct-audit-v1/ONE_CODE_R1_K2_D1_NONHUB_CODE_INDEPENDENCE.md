# Residual-one k=2 nonhub D1 code-class independence

Date: 2026-09-20

Status: **same-session structural lemma**, conditional on `r=1`, `J2=empty`, and the independently repaired same-code U--U criticality theorem. No finite scan is used.

The nonhub private-spoke theorem pushes any cheap linear D1 population toward sparse private support. At `J2=empty` the available A-codes are so restricted that almost every corresponding U-code class is forced independent.

## 1. A-code repertoire at the all-radius-one endpoint

Relative to the source code d, the X/Y layer contains only

- Y: code d;
- K: code `C=d xor e_j`;
- matched heads `h_i`: code `d xor e_i`, for `i in I=[p]\{j}`.

There are no radius-two matched heads `d xor e_i xor e_j` because `J2=empty`.

Thus the complete A-code repertoire is

> `d`, `d xor e_j`, and `d xor e_i` (`i in I`).          `(CI-A)`

## 2. Codes of q_j-nonneighbour U-vertices

If a U-vertex t misses q_j, its code agrees with d at j. Write

> `c(t)=d xor S`, with `S subseteq I`.                    `(CI-U)`

Its complementary code relative to the p coordinates is

`bar(c(t)) = d xor ({j} union (I\S))`.                   `(CI-COMP)`

Compare `(CI-COMP)` with the A-code list `(CI-A)`.

- It cannot equal d because it differs at j.
- It cannot equal `d xor e_i` because it differs at j.
- It equals `C=d xor e_j` **if and only if** `I\S=empty`, i.e. `S=I`.

Therefore

> **if `S` is a proper subset of I, then `A_{bar(c(t))}=empty`.** `(CI-ABS)`

The unique exceptional support is the full support `S=I`, whose complementary A-code is C and is represented by K.

## 3. Same-code U--U criticality forces independence

The hostile-repaired same-code U--U theorem says that an edge joining two U-vertices of the same code gamma requires a complementary A-code witness `bar gamma` in the appropriate singleton orientation.

For every proper support `S proper subset I`, `(CI-ABS)` says that no such A-vertex exists. Hence

> **`G[U_{d xor S}]` is independent for every proper `S subset I`.** `(CI-IND)`

This includes in particular

- the zero-support class `U_d`;
- every singleton-support class `U_{d xor e_i}`;
- every bounded-support class as long as it is not the full private set I.

No claim is made for the exceptional full-support class `U_{d xor I}=U_{bar C}`: its complementary A-code C is represented by K, so same-code edges there are not excluded by this argument.

## 4. Physical missing-edge bill from code multiplicities

For any q_j-nonneighbour set N, let `n_S` be the number of its vertices with support S. Then `(CI-IND)` gives the literal missing-U-edge block

> **`M_U(N) >= sum_{S proper I} binom(n_S,2)`,**           `(CI-BILL)`

where only pairs internal to N are counted.

This is a graph-theoretic bill, not an entropy estimate. It becomes quadratic whenever a positive fraction of N lies in o(p)-many proper support classes.

The sparse-support theorem says that a cheap D1 population has average support `o(p)`. `(CI-BILL)` therefore exposes the remaining escape mechanism precisely: to avoid a new quadratic U-edge deficit, that population must spread itself across many distinct small support sets rather than concentrate in a few code classes.

## 5. The sharp hostile endpoint: singleton-support spreading

For `|N|` of order p there are already `p-1` singleton supports `{i}`. Hence `(CI-BILL)` alone does **not** close the branch: N can in principle assign essentially one vertex to each singleton support and incur no internal same-code collision.

That observation is important. The current local theorems do not justify replacing sparse support by code concentration. The true permissive endpoint is instead a near-injective assignment

`t -> i(t)`

with `S(t)={i(t)}` for almost all D1 vertices.

This is the next literal geometry to attack. It must be coupled to

- the row constraint `S(t) subseteq F_a` or `F_b` according to the unique K-neighbour;
- the raw private-spoke F/R certificate at coordinate `i(t)`;
- the K-heavy reservoir's own q_i incidence/certificate requirements;
- the weighted rooted residual ledger.

## 6. Strategic conclusion

The cheap endpoint is no longer an amorphous D1 reservoir. Up to lower-order mass it is forced toward:

1. q_j-nonneighbours;
2. sparse private support;
3. many distinct proper U-code classes, plausibly singleton supports;
4. row-compatible private coordinates.

The next attack should test whether a near-matching between D1 vertices and private coordinates can coexist with a linear K-heavy reservoir. If it can at the abstract certificate level, preserve that as a hostile normal form rather than pretending the present machinery closes it.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics pending hostile replay.