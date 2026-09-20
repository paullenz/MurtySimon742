# Maximal outside-certificate selection as a matching problem; direct closure of the one-witness branch

Date: 2026-09-20

Status: internal structural theorem package. The matching normalization below is derived before F/R classification from the raw first-strict eligibility relation. The final `m=1` closure is conditional on the already-audited first-strict unique-hole setup, the raw outside reverse-fan theorem, the same-code/internal-X theorem used by the current handoff, and the previously preserved all-R closure.

## 1. Audit reconciliation

This session began by rereading `CURRENT_STATE.md`, root `README.md`, the latest commits, the 20 September daily red-team audit, the current maximal-selection scope audit, the first-strict theorem, and the raw outside reverse-fan theorem. The audit trust boundary is unchanged: selected `(source,coordinate)` uniqueness is not raw-witness uniqueness; `X_3` remains the mandatory negative control; no bounded positive actual-D2C fixture realizes the full rigid complete-cut hypotheses; pair-local `Ccap_P/(ONE-P)/(CROWD)` remains mandatory downstream.

The present normalization is deliberately upstream of selected F/R labels. It replaces the informal “maximize the number of physical witnesses” language by an exact bipartite matching invariant.

## 2. Raw eligibility graph

Let

- `L = X' = X\{a_0}`;
- `R = U_o`;
- `xz in E(H)` iff the physical outside vertex `z` is a valid outside-U certificate for the buffer edge `bx`, i.e. the raw singleton relation required by the first-strict theorem holds.

This graph `H` is defined before choosing representatives, before F/R classification, and before building Hall objects.

Two previously proved raw facts say that `H` has no isolated vertices on either side:

1. every `x in X'` has an outside-U certificate, because every surviving buffer edge `bx` is outside-U certified;
2. every `z in U_o` can certify at least one buffer edge, by `BUFFER_UO_REVERSE_FAN.md`.

A representative selection is precisely a map `f:L -> R` with `xf(x) in E(H)`.

## 3. Maximal image size equals the matching number

### Theorem 3.1

If `m` is the maximum possible number of distinct physical witnesses used by a valid representative selection, then

> `m = nu(H)`.

### Proof

Given any selection whose image contains `m0` distinct witnesses, choose for each image witness one head mapped to it. Different image witnesses have disjoint nonempty preimage sets, so the chosen head-witness edges form a matching of size `m0`. Hence every selection image has size at most `nu(H)`.

Conversely, let `M` be a matching of size `t`. Fix the matched witness on each matched head. Every unmatched head has positive degree in `H`, so choose any eligible witness for it. This extends `M` to a full representative selection whose image contains all `t` matched witnesses. Hence the maximal image size is at least `nu(H)`.

Therefore `m=nu(H)`. `square`

This removes the scope ambiguity in the earlier maximal-selection argument: the quantity being maximized is a graph invariant of the raw eligibility relation, not a property of a pre-existing F/R labeling.

## 4. The one-witness consequence is exact

### Corollary 4.1

Under maximal selection,

> `m=1  =>  |U_o|=1`.

### Proof

Here `nu(H)=1`. Since `|X'|=x-1>=2` and `H` has no isolated vertices on either side, the right side cannot contain two vertices. Indeed a bipartite graph of matching number one has all edges incident with one common vertex; if both bipartition classes had at least two nonisolated vertices, two disjoint edges could be chosen. Thus `|U_o|=1`. `square`

This is the clean independent repair of the maximal-selection normalization used by the current one-witness handoff.

## 5. Direct matched-edge obstruction in maximal `m=1` all-F

The preserved all-R `m=1` arm is already empty. Thus the surviving maximal `m=1` arm is all-F. Let its sole outside witness be `z`, and let all vertices of `X'` have the common all-F code `C`. Its agreement set with `d` is the singleton `{i_0}`. Hence `C` differs from `d` in `p-1` coordinates.

The independently preserved same-code/internal-X argument gives

- `G[X']` edgeless;
- `d_{X'}(a_0)<=1`.

Since `|X'|>=2`, choose `x in X'` with `xa_0 notin E`.

Assume `p>=3`. Choose a coordinate `j` on which `C` differs from `d`. Let `q_j` be the `bar d` endpoint of the corresponding tight matched fibre. Then

- `xq_j in E`, because `C_j != d_j`;
- `bq_j in E`, because `c(b)=bar d`;
- `bx in E`.

Thus the edge `xq_j` lies in the triangle `x-b-q_j` and must possess a raw singleton criticality witness.

We show that neither orientation is possible.

### Orientation A: source `q_j`, head `x`

Any witness in the rooted B-side has the root as an extra common neighbour with `q_j`, so cannot give the singleton `{x}`.

On the A-side:

- every `y in Y` is adjacent to `x`, but `q_j` is adjacent to every vertex of `X'`; because `|X'|>=2`, any such Y-witness has another X' vertex as an extra common neighbour with `q_j`;
- another X' vertex is not adjacent to `x` because `G[X']` is empty;
- `a_0` is not adjacent to the chosen `x`.

Hence this orientation has no witness.

### Orientation B: source `x`, head `q_j`

A-side witnesses fail:

- vertices of `Y` miss `q_j` because they have code `d`;
- any other X' vertex shares all of `Y` (and also the buffer) with `x`, so cannot form a singleton common neighbourhood;
- if `a_0q_j in E`, then `x` and `a_0` still share the nonempty set `Y`, so `a_0` cannot isolate `q_j`.

For rooted-B witnesses:

- `b` and every common-core `bar d` vertex share with `x` every `bar d` fibre endpoint selected by `C`; since `p-1>=2`, there is another such endpoint besides `q_j`;
- the sole outside witness `z` has code `bar C`, so it misses `q_j` at every coordinate where `C` differs from `d`;
- the root sees all of the several B-neighbours of `x`, not only `q_j`;
- a `d`-endpoint of any tight fibre shares every vertex of the nonempty set `Y` with `x` whenever it is adjacent to `q_j`;
- a `bar d` endpoint different from `q_j` shares the buffer `b` with `x` whenever it is adjacent to `q_j`.

Additional cross-edges inside the rooted B-side can only add common neighbours; they do not remove the fixed extra common neighbours just listed. Therefore no B-side witness gives singleton `{q_j}`.

Both orientations fail, contradicting raw D2C edge-criticality. Hence

> maximal `m=1` all-F is impossible for `p>=3`.          `(M1-PGE3-CLOSE)`

The argument is graph-level and does not use the finite parameter scans or the exact-score pinch.

## 6. Complete maximal `m=1` closure

The existing preserved work already closes:

- the all-R `m=1` polarization;
- all maximal `m=1`, `y>=2` rows analytically;
- the `y=1` arithmetic except for the literal point `(p,k,g,x,y,u,lambda)=(3,1,2,3,1,3,4)`.

The new theorem kills that literal point, and in fact every all-F maximal `m=1` configuration with `p>=3`. The prior `y>=2` and `y=1` analyses cover the small `p<=2` remainder.

Therefore, conditional on the audited rigid first-strict setup and the raw reverse-fan theorem,

> **the maximal-selection one-witness branch is empty.**  `(MAX-M1-CLOSED)`

This eliminates the last one-witness equality pinch without needing to instantiate an order-14 graph.

## 7. General certificate-core decomposition for `m>=2`

By Theorem 3.1 and König's theorem, the raw eligibility graph has a vertex cover `K=S dotcup T` of size exactly `m`, where `S subseteq X'`, `T subseteq U_o`.

Write `s=|S|`, so `|T|=m-s`. Then

- every uncovered head `x in X'\S` has all eligible witnesses in `T`;
- every uncovered outside vertex `z in U_o\T` has all eligible heads in `S`;
- all those neighbourhoods are nonempty by the two-sided reverse-fan/nonisolation theorem.

Thus the full physical certificate incidence relation is controlled by at most `m` head/witness centres. In particular:

- if `s=0`, then `U_o=T` and `|U_o|=m`;
- if `s=m`, then `X'=S` and `x-1=m`.

For `m=2` there are exactly three cover geometries:

1. **two-witness cover:** `|U_o|=2`;
2. **two-head cover:** `|X'|=2`, hence `x=3`;
3. **mixed cover:** one distinguished head `x_*` and one distinguished witness `z_*`; every other head has eligible neighbourhood exactly `{z_*}`, and every other outside witness has eligible neighbourhood exactly `{x_*}` (the centre edge `x_*z_*` is optional).

This is a statement about raw physical eligibility, not selected witness incidences.

## 8. Reverse-fan upgrade: the whole outside reservoir is visible to the Y-ledger

Put

`omega=|U_o|=u-k-1`.

The raw reverse-fan theorem says every physical `z in U_o` certifies at least one buffer edge. The standard outside-certificate localization then makes every such `z` anticomplete to `Y`. The unloaded common core and buffer are also anticomplete to `Y`. Hence

> `Y--U` is empty throughout the first-strict unloaded branch.       `(YU0)`

Since every `y0 in Y` has `d_A(y0)=x`, its slack is not merely bounded by the number of selected witnesses; it is exact:

> `epsilon_{y0}=p+u-x=p-g+1+omega`.                   `(Y-EXACT)`

Therefore

> `L_Y=y(p-g+1+omega)`.                                `(LY-PHYSICAL)`

This strictly strengthens the earlier selected-witness floor `y(p-g+1+m)` whenever the physical reservoir has unused leaves (`omega>m`). It is important for the `m=2` mixed/two-head cover geometries, where `omega` can exceed two.

## 9. Eligibility components are code components

For every raw eligibility edge `xz`, outside localization gives

> `c(z)=bar c(x)`.

Therefore one physical outside vertex can certify heads from only one tight X-code class. Conversely every head and every outside vertex is nonisolated in `H`. Thus `H` is the disjoint union of nonempty bipartite code components

`H_C = H[X'_C,U_{bar C}]`,

one for each X-code `C` represented in `X'`.

If `h` is the number of distinct X-codes in `X'`, then

> `m=nu(H)=sum_C nu(H_C) >= h`.                         `(CODE-MATCH)`

For `m=2`, necessarily `h in {1,2}`.

If `h=2`, each code component has matching number one. Since it has no isolated vertices internally, each component is a star. Consequently for each of the two code classes:

- if it contains at least two heads, it has exactly one physical complementary-code outside witness;
- if it contains at least two physical outside witnesses, it contains exactly one head.

This physical statement is stronger than selected representative uniqueness.

## 10. Single-code obstruction for maximal `m>=2`

Assume `h=1`; write the common X'-code as `C`. Then every physical outside vertex has code `bar C` by Section 9. Suppose

`d_H(C,d)>=2`.

Choose a coordinate `j` where `C` differs from `d`. Because `|X'|>=2`, choose a head `x in X'` for which `a_0` cannot be the unique A-witness for the edge `xq_j`: if `a_0` has zero or at least two neighbours in `X'`, any suitable/nonadjacent head works; if it has exactly one, choose another head.

The same raw criticality exhaustion as in Section 5 applies with one change: there may now be several outside witnesses, but every one has code `bar C`, and therefore every one misses `q_j`. All other fixed extra-common-neighbour obstructions remain. Hence the edge `xq_j` has no singleton criticality certificate.

Therefore every single-code survivor must satisfy

> `d_H(C,d)=1`.                                         `(ONECODE-R1)`

For `p>=3`, this has agreement block size `p-1>=2`, so it cannot be Type F (a Type-F block is a singleton). Thus every representative in a maximal selection is Type R. A maximum matching of size `m>=2` supplies two distinct selected outside witnesses on two heads of the same code, but the Type-R fixed-foot overlap theorem forces those witnesses to be identical. Contradiction.

Hence

> `p>=3 and m>=2  =>  h>=2`.                            `(NO-ONECODE)`

In particular for maximal `m=2`, `p>=3` forces exactly two X-code classes.

## 11. Bulk-block covering lemma

Now take `m=2`, `p>=3`, so there are exactly two code classes `C,D` with disjoint nonempty agreement blocks `I_C,I_D` from the preserved funnel theorem.

Suppose class `C` contains at least two heads. Choose a head `x` in that class so that `a_0` cannot uniquely witness the matched edge considered below (the same zero/one/many-neighbour choice as in Section 10).

For every coordinate `j notin I_C`, the edge `xq_j` has the fixed triangle through `b`. Exhaust raw criticality exactly as above. The only new possible witness not already eliminated is an outside vertex from the *other* code class `D`. Such a vertex has code `bar D` and is adjacent to `q_j` exactly when `D_j=d_j`, i.e. exactly when `j in I_D`.

Therefore criticality of every such edge forces

> `[p]\I_C subseteq I_D`.

The agreement blocks are disjoint, so the reverse inclusion is automatic. Hence

> `I_D=[p]\I_C`, and `I_C dotcup I_D=[p]`.              `(BLOCK-PARTITION)`

Thus as soon as either of the two classes is a bulk class (multiplicity at least two), the two agreement blocks partition all tight coordinates.

## 12. Consequence: the large-X two-witness branch is forced F/R complementary

If `x>=4`, then `|X'|=x-1>=3`; with only two code classes, at least one class is bulk. Hence `(BLOCK-PARTITION)` applies.

Class types are determined by their blocks:

- F-blocks are singletons contained in `S_0`;
- R-blocks are nonempty subsets of `I_0=[p]\S_0`.

For `p>=3`, the partition has the following consequences:

- **FF** is impossible: two singleton blocks can partition `[p]` only when `p=2`;
- **RR** is impossible: both blocks lie in `I_0` and cannot cover the nonempty set `S_0`;
- therefore the classes are exactly **one F and one R**.

Moreover partitioning forces

> `|S_0|=1`, `I_F=S_0`, `I_R=I_0`.                     `(FR-NORMAL)`

Equivalently the two X'-codes are complementary: the R-code differs from `d` on the unique coordinate `S_0`, while the F-code agrees with `d` there and differs on all remaining coordinates.

So the entire maximal `m=2`, `p>=3`, `x>=4` branch has the rigid normal form

> **one F code, one R code, complementary to each other, with `S_0` a singleton.**

The R-code has exactly one physical outside witness: any eligible witness for an R-block must be adjacent to `a_0`, and the reverse fixed-foot singleton at any coordinate of `I_R` determines that physical witness uniquely. Hence:

- if the F class is also bulk, it too has one physical witness (its matching-one component is a star with at least two heads), so `omega=2`;
- if `omega>2`, the F class must consist of exactly one head, all extra physical outside witnesses belong to its complementary-code star, and the R class contains the remaining `x-2` heads served by its unique physical witness.

This is the live two-witness structural pinch.

## 13. Next attack

The `m=1` branch is now closed. For `m=2`, the remaining work splits cleanly:

1. `p>=3,x>=4`: attack the F/R complementary normal form of Section 12 with the exact physical Y-price `(LY-PHYSICAL)`, pair-local `Ccap_P/(ONE-P)/(CROWD)`, and the rooted residual ledger. Separate `omega=2` from the `omega>2` case, where the F side is one head with a physical witness star and the R side is a bulk class with one graph-fixed witness.
2. `x=3`: both code classes may be singleton and the bulk-block lemma need not fire; retain as a small-head exceptional slice and price it through the pair/residual ledger.
3. `p<=2`: retain as a small-fibre exceptional slice; do not let it obstruct the sufficiently-large structural theorem.

The next hand target should be to close or finitely pinch `omega>2` in the complementary F/R normal form. Every extra F-star witness is anticomplete to Y by `(YU0)`, increases the exact pair-local source bill by `y`, and is physically tied to the unique F head. That is the most direct place to combine the new raw certificate geometry with the audited pair-local capacity machinery.
