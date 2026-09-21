# Raw boundary-code-edge trichotomy for a rigid complete Hall cut

Date: 2026-09-21

Status: raw graph-theoretic necessary condition for **realizability** of the rigid complete-Hall-cut interface. It is upstream of the later one-code half-ray algebra and does not use the superseded H--U private-foot coordinate-slice argument.

## 1. Setup

Let `G` be diameter-2-critical, root at a maximum-degree vertex `v`, and use the usual rooted partition

- `B=N(v)`, `A=V\N[v]`;
- tight antipode fibres `{q_i^0,q_i^1}`, `i=1,...,p`;
- unmatched rooted neighbours `U`;
- tight Boolean code `c(z)` for every `z in A union U`.

Let `X` be a nonempty proper union of complementary A-code pair classes and put `Y=A\X`. Assume the **rigid complete-cut hypotheses**

- `x=|X|>=3`;
- every `X--Y` pair is an edge;
- every crossing A-edge is sourced from `Y` in the rigid Hall certificate system.

The theorem below in fact uses only completeness of the A-cut and raw triangle-edge criticality; it does not assume that a particular preselected crossing certificate is the one under discussion.

Fix `y in Y` with tight code `d=c(y)`. Write `q_i^{d_i}` for the matched endpoint selected by `y` in fibre `i`.

Define

`I(d,X)={i : some x in X has c(x)_i=d_i}`.

Thus for `i in I(d,X)` the boundary B--A edge

`y q_i^{d_i}`

lies in a triangle through `X`.

Also define the universal-agreement coordinates

`C(d,X)={j : every x in X has c(x)_j=d_j}`.

Finally, define the relative matched-row graph `R_d` on the tight coordinates by

`j~_d l`

iff the opposite endpoint `q_j^{1-d_j}` is adjacent to the selected endpoint `q_l^{d_l}`. Tight-fibre transversality makes this relation symmetric.

## 2. Trichotomy

### Theorem 2.1 — boundary-code-edge certificate trichotomy

For every `i in I(d,X)`, raw criticality of the triangular edge `y q_i^{d_i}` forces at least one of the following three mechanisms.

#### (U-forward)

`y` is the criticality source and the witness is an unmatched rooted neighbour `w in U` satisfying

- `N(w) cap X = empty`;
- `c(w)=bar d xor e_i`;
- and the exact certificate condition
  `N(y) cap N(w)={q_i^{d_i}}`.

In particular, the witness code agrees with `d` **only** in coordinate `i`.

#### (matched-forward)

`y` is the source and the witness is an opposite matched endpoint

`q_j^{1-d_j}`

for some `j in C(d,X)`, with

- `N_{R_d}(j)={i}`;
- and therefore `j` is a global degree-one vertex of `R_d` whose sole neighbour is `i`.

Equivalently, the witness is X-anticomplete and among the matched endpoints selected by `y` it sees exactly `q_i^{d_i}`.

#### (X-reverse)

`q_i^{d_i}` is the source and the witness lies in `X`. Its tight code is forced to be

`gamma(q_i^{d_i})`,

where `gamma` is the usual row-complement matched-foot code. The witness must in addition satisfy the exact singleton condition

`N(q_i^{d_i}) cap N(w)={y}`.

No other physical witness location is possible.

### Proof

Because `i in I(d,X)`, choose `x in X` adjacent to `q_i^{d_i}`. Since the cut is complete, `xy` is also an edge. Thus `y q_i^{d_i}` is triangular, so the standard triangle-edge criticality dichotomy gives either

`N(y) cap N(w)={q_i^{d_i}}`

or

`N(q_i^{d_i}) cap N(w)={y}`.

#### Forward orientation

The witness cannot lie in `X`, because `X--Y` is complete and a witness must be nonadjacent to source `y`. It cannot lie in `Y`: every `Y` vertex is adjacent to every vertex of `X`, so any such witness together with `y` would have all of `X` as extra common neighbours. It cannot be the root.

Hence a forward witness lies in `B`. If it lies in `U`, tight transversality says it selects exactly one endpoint in every fibre. The singleton common-neighbour equation with `y` means that the selected endpoint agrees with `y` exactly in fibre `i` and disagrees in every other tight fibre. Therefore

`c(w)=bar d xor e_i`.

Moreover every `x in X` is adjacent to `y`, so exact singletonhood forces `w` to miss every `x in X`. This is (U-forward).

If the forward witness is matched, it must be an endpoint that `y` does not see, hence has the form `q_j^{1-d_j}`. X-anticompleteness then forces every X-code to choose the opposite endpoint `q_j^{d_j}`, so `j in C(d,X)`. The common matched endpoints of `y` and this witness are exactly the selected endpoints `q_l^{d_l}` for which `j~_d l`. Singletonhood at head `q_i^{d_i}` therefore gives

`N_{R_d}(j)={i}`.

This is (matched-forward).

#### Reverse orientation

A reverse witness cannot lie in `B`: source `q_i^{d_i}` and any B-vertex share the root `v`, an unwanted extra common neighbour. The root itself is not adjacent to head `y`. A reverse witness cannot lie in `Y`: by the definition of `I(d,X)` there is an `x in X` adjacent to `q_i^{d_i}`, and cut completeness makes the same `x` adjacent to every Y-vertex, producing an extra common neighbour. Hence the witness lies in `X`.

To avoid the source `q_i^{d_i}`, its code has the opposite bit at coordinate `i`. In every other fibre it must choose the endpoint opposite the unique matched endpoint adjacent to `q_i^{d_i}`; otherwise that matched endpoint would be a second common neighbour. These bits are exactly the row-complement code `gamma(q_i^{d_i})`. This is (X-reverse). `square`

## 3. Immediate certificate-cover consequences

For fixed outside code `d`, define the coarse U-support

`U_0(d,X)={i in I(d,X): there exists w in U with c(w)=bar d xor e_i and N_X(w)=empty}`.

This is deliberately a **superset** of the coordinates having a genuine exact U-forward certificate. Since the codes `bar d xor e_i` are distinct,

`|U_0(d,X)|<=u`.

Define the matched-leaf head support

`L(d,X)={i in I(d,X): there exists j in C(d,X) with N_{R_d}(j)={i}}`.

For the reverse channel put

`X_e={x in X:c(x)=e}`.

### Corollary 3.1 — realizability cover

For every `i in I(d,X)`,

`i in U_0(d,X) union L(d,X)`

or else

`|X_{gamma(q_i^{d_i})}| >= |Y_d|`,

where `Y_d={y in Y:c(y)=d}`.

### Proof

If `i` has neither possible forward support, Theorem 2.1 forces the reverse orientation for the edge `y q_i^{d_i}` for every `y in Y_d`. For fixed source `q_i^{d_i}`, one physical witness `w` cannot have

`N(q_i^{d_i}) cap N(w)={y_1}`

and also equal `{y_2}` for distinct heads. Thus the `|Y_d|` reverse edges require `|Y_d|` distinct witnesses, all in the forced code class `X_{gamma(q_i^{d_i})}`. `square`

This is a raw **reachability filter** for the rigid Hall interface. It is independent of which A-edge certificate policy was used to discover the rigid cut.

## 4. Universal-coordinate pressure

If `i in C(d,X)`, then every X-code has bit `d_i` at coordinate `i`, whereas

`gamma(q_i^{d_i})_i=1-d_i`.

Therefore the reverse mechanism is impossible on a universal coordinate.

### Corollary 4.1

For every `i in C(d,X)`, every outside source of code `d` must use a forward U or matched-leaf witness. In particular, for one fixed `y in Y_d`, the witnesses for distinct `i in C(d,X)` are physically distinct, and

`|C(d,X)| <= u + ell_C`,

where

`ell_C=|{j in C(d,X): deg_{R_d}(j)=1 and N_{R_d}(j) subseteq C(d,X)}|`.

If `u=0`, then necessarily every coordinate in `C(d,X)` is a degree-one vertex of `R_d`, its unique neighbour also lies in `C(d,X)`, and

`R_d[C(d,X)]`

is a perfect matching with no `R_d` edge from `C(d,X)` to its complement. In particular

`|C(d,X)|`

must be even.

### Proof

Reverse is unavailable as observed. A fixed U witness has one fixed one-match code `bar d xor e_i`, so it can serve at most one coordinate. A fixed matched witness `q_j^{1-d_j}` has one singleton matched head because `N_{R_d}(j)` is a singleton. Hence the certificate assignment for one fixed `y` is injective into the union of U witnesses and eligible matched leaves, giving the inequality.

If `u=0`, an injective assignment from the finite set `C` into eligible matched leaves contained in `C` is a bijection. Hence every coordinate in `C` is a global leaf and its unique neighbour lies in `C`; the induced graph is 1-regular, hence a perfect matching. `square`

## 5. Why this matters for the zero-positive-fixture gap

The bounded actual-D2C regression had previously established that no tested graph realizes a rigid complete Hall cut with `x>=3`, but that was only a coverage statement. The present theorem identifies a **new raw necessary mechanism** that any such realization must satisfy before the one-code pair-capacity inequalities are even consulted.

The next useful compression is to combine Corollary 3.1 with multiplicities of the forced `gamma(q_i^{d_i})` classes: reverse-only boundary coordinates either consume many distinct large X-code classes or create a large repeated-gamma family, which can then be charged by the independently preserved gamma-collision theorem. That synthesis is kept separate so the raw trichotomy itself remains easy to audit.
