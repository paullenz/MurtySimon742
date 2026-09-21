# Raw boundary-code-edge trichotomy for a rigid complete Hall cut

Date: 2026-09-21

Status: raw graph-theoretic necessary condition for **realizability** of the rigid complete-Hall-cut interface. It is upstream of the later one-code algebra and does not use the superseded H--U private-foot coordinate-slice argument. **21 September correction:** the reverse arm is impossible whenever the relevant outside code class has multiplicity at least two; an earlier corollary retained only a weaker witness-count condition and subsequent reverse-gamma work must be read with this strengthening.

## 1. Setup

Let `G` be diameter-2-critical, root at a maximum-degree vertex `v`, and use the usual rooted partition

- `B=N(v)`, `A=V\N[v]`;
- tight antipode fibres `{q_i^0,q_i^1}`, `i=1,...,p`;
- unmatched rooted neighbours `U`;
- tight Boolean code `c(z)` for every `z in A union U`.

Let `X` be a nonempty proper union of complementary A-code pair classes and put `Y=A\X`. Assume the rigid complete-cut hypotheses

- `x=|X|>=3`;
- every `X--Y` pair is an edge;
- every crossing A-edge is sourced from `Y` in the rigid Hall certificate system.

The theorem below uses only completeness of the A-cut and raw triangle-edge criticality; it does not assume that a particular preselected crossing certificate is the one under discussion.

Fix `y in Y` with tight code `d=c(y)`. Write `q_i^{d_i}` for the matched endpoint selected by y in fibre i.

Define

`I(d,X)={i : some x in X has c(x)_i=d_i}`.

Thus for `i in I(d,X)` the boundary B--A edge

`y q_i^{d_i}`

lies in a triangle through X.

Also define

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
- `N(y) cap N(w)={q_i^{d_i}}`.

#### (matched-forward)

`y` is the source and the witness is an opposite matched endpoint `q_j^{1-d_j}` for some `j in C(d,X)`, with

- `N_{R_d}(j)={i}`;
- hence j is a global degree-one vertex of R_d whose sole neighbour is i.

#### (X-reverse)

`q_i^{d_i}` is the source and the witness lies in X. Its tight code is forced to be

`gamma(q_i^{d_i})`,

and it must satisfy

`N(q_i^{d_i}) cap N(w)={y}`.

No other physical witness location is possible.

### Proof

Because `i in I(d,X)`, choose `x in X` adjacent to `q_i^{d_i}`. Since the cut is complete, xy is also an edge. Thus `y q_i^{d_i}` is triangular and triangle-edge criticality gives either

`N(y) cap N(w)={q_i^{d_i}}`

or

`N(q_i^{d_i}) cap N(w)={y}`.

For the forward orientation, the witness cannot lie in X (it must miss source y), cannot lie in Y (X gives extra common neighbours), and cannot be the root. Hence it lies in B. If unmatched, tight transversality forces code `bar d xor e_i`, and exact singletonhood forces X-anticompleteness. If matched, it is an opposite endpoint `q_j^{1-d_j}`; X-anticompleteness forces `j in C(d,X)`, and exact singletonhood gives `N_{R_d}(j)={i}`.

For the reverse orientation, a B-witness shares root v with source `q_i^{d_i}`, the root itself misses y, and a Y-witness has an X-generated extra common neighbour, so the witness lies in X. Avoiding the source and every unwanted matched common neighbour forces code `gamma(q_i^{d_i})`. `square`

## 3. Same-code multiplicity kills the reverse arm

Let

`Y_d={z in Y:c(z)=d}`, `y_d=|Y_d|`.

### Theorem 3.1 — repeated-code reverse exclusion

If

> **`y_d>=2`,**

then the X-reverse mechanism is impossible for every boundary edge `y q_i^{d_i}` with `y in Y_d`.

### Proof

Suppose a reverse witness `w in X` existed for one such edge. The rigid cut is complete, so w is adjacent to **every** vertex of `Y_d`. The matched source `q_i^{d_i}` is also adjacent to every vertex of `Y_d`, because all those vertices have bit `d_i` in coordinate i. Therefore

`Y_d subseteq N(q_i^{d_i}) cap N(w)`.

If `y_d>=2`, this common-neighbour set cannot equal the required singleton `{y}`. Contradiction. `square`

This observation is stronger than the earlier fixed-source witness-count corollary: repeated same-code outside heads do not require *many* reverse witnesses; they forbid the reverse orientation altogether.

### Corollary 3.2 — repeated-code realizability cover

If `y_d>=2`, then for every exposed coordinate

> **`i in U_0(d,X) union L(d,X)`.**                      `(3.1)`

There is no reverse-only coordinate for that outside code class.

If `y_d=1`, the reverse arm may remain possible and its witness is still forced into `X_{gamma(q_i^{d_i})}`.

## 4. Coarse support sets

Define

`U_0(d,X)={i in I(d,X): there exists w in U with c(w)=bar d xor e_i and N_X(w)=empty}`.

Since the one-match codes are distinct,

`|U_0(d,X)|<=u`.

Define

`L(d,X)={i in I(d,X): there exists j in C(d,X) with N_{R_d}(j)={i}}`.

For `y_d=1`, if a coordinate has neither possible forward support, Theorem 2.1 forces an X-reverse witness of code `gamma(q_i^{d_i})`.

For `y_d>=2`, Corollary 3.2 is the exact stronger statement and should be used instead of any reverse-gamma capacity relaxation.

## 5. Universal-coordinate pressure

If `i in C(d,X)`, then every X-code has bit `d_i` at coordinate i, whereas `gamma(q_i^{d_i})_i=1-d_i`. Therefore reverse is impossible on a universal coordinate even when `y_d=1`.

For every `i in C(d,X)`, every outside source of code d must therefore use a forward U or matched-leaf witness. For one fixed y the witnesses for distinct universal coordinates are physically distinct, giving

`|C(d,X)| <= u + ell_C`,

where `ell_C` counts eligible matched leaves. If `u=0`, `R_d[C]` is a perfect matching with no edge from C to its complement.

## 6. Why this matters

The bounded actual-D2C regression had established no tested positive rigid complete Hall cut with `x>=3`. The boundary theorem now gives a sharper literal obstruction:

- for any outside code class occurring at least twice, every exposed boundary coordinate must route **forward**;
- U-forward coordinates consume distinct one-match U-code classes;
- matched-forward support is controlled by global leaves of R_d and is later shown to have size at most two.

Thus repeated outside codes remove the entire reverse-gamma escape channel. Any downstream note that treated reverse-only coordinates with `y_d>=2` as potentially realizable is superseded by Theorem 3.1 and must be repaired before use.
