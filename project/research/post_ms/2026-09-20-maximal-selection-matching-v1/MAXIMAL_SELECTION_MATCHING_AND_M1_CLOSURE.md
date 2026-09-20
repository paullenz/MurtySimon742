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

This is the next compact structural frontier after `(MAX-M1-CLOSED)`. It is a statement about raw physical eligibility, not selected witness incidences.

## 8. Next attack

Start with `m=2` under the three König-cover geometries. Choose representatives only after fixing the raw cover. Then classify the selected pairs into F/R and intersect the cover with the already-proved disjoint agreement-block theorem and exact pair-local `Ccap_P/(ONE-P)/(CROWD)`. The mixed double-star geometry is especially rigid: a maximum matching forces one noncentral head to use the central witness and the central head to use a noncentral witness, while all remaining leaves are forced to the corresponding centre. This creates a highly polarized physical load profile suitable for the source-slack and rooted residual ledger.
