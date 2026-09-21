# Near-equality boundary population forces a complementary-U repair reservoir

Date: 2026-09-21

Status: raw structural theorem inside the rigid complete one-code interface. Conditional on a repeated one-code outside block and the corrected full-boundary theorem; no graph-level reachability claim.

## 1. Setup

Let `Y=A_d` with `y>=2`, selected matched-head set `S`, `m=|S|>=2`, and suppose the generic matched-forward-free face `L=empty` (in particular `C=empty` or `|C|>=3`). For a minimum outside source let

- `k` be its selected complementary U-witness count;
- `e=u-k`;
- the full-boundary theorem gives `p<=e`.

This note studies the first surviving population face after the strict equality obstruction:

> **`e=p`.**                                             `(1.1)`

Equivalently, every U-vertex outside the k selected complementary witnesses is needed to fill one of the p distinct boundary one-match code classes.

## 2. Exact U-spectrum on `e=p`

For every coordinate i, repeated-code reverse exclusion and `L=empty` force U-forward support. A U-forward witness at i has code

`bar d xor e_i`,

and distinct coordinates require distinct code classes.

Since there are p coordinates and exactly e=p vertices outside the selected complementary witness set, equality forces:

1. exactly one vertex `w_i` of code `bar d xor e_i` for each i;
2. these p vertices exhaust `U\K`, where K is the k selected complementary-witness set;
3. every vertex of K has code `bar d`;
4. there are no other U-code classes.

Thus

> **`U = K disjoint_union {w_1,...,w_p}`**,              `(2.1)`
>
> **`c(z)=bar d` for `z in K`,**                         `(2.2)`
>
> **`c(w_i)=bar d xor e_i`.**                            `(2.3)`

## 3. Each boundary vertex is A-anticomplete

Fix i. Because `w_i` is the unique U-forward candidate at coordinate i, it must serve the boundary edge `y q_i^{d_i}` for every `y in Y`. Therefore it is nonadjacent to every y.

The raw boundary theorem already gives `N_X(w_i)=empty`. Hence

> **`N_A(w_i)=empty` for every i.**                      `(3.1)`

In particular every `w_i` is unusable as an A--U neighbour of any selected head.

## 4. Diameter two forces repair through K

For `i in S`, let `h_i in X` be the selected matched head with

`c(h_i)=d xor e_i`.

Then

`c(w_i)=overline{c(h_i)}`,

so h_i and w_i have no common tight matched endpoint. They are not adjacent because w_i is X-anticomplete. They have no common neighbour in A by `(3.1)`, no common neighbour at the root, and no common neighbour among the p vertices `w_j`, because every w_j is X-anticomplete.

Since the graph has diameter two, every selected coordinate therefore requires at least one common neighbour in K:

> for every `i in S` there exists `z in K` with
>
> **`z~h_i` and `z~w_i`.**                               `(4.1)`

Equivalently the k complementary U-vertices must cover all m aligned selected head/boundary-witness pairs.

This produces a physically localized repair map

> **`rho:S -> K`**                                       `(4.2)`

with `rho(i)` adjacent to both h_i and w_i.

## 5. The one-repair-vertex face

If `k=1`, write `K={z}`. Then `(4.1)` becomes

> **`z` is adjacent to every selected head `h_i` and every aligned boundary vertex `w_i`, `i in S`.** `(5.1)`

Since `c(z)=bar d`, this is a very rigid hub geometry: one unmatched root-neighbour of complementary code must simultaneously repair all diameter-two failures created by the exact boundary spectrum.

The natural next audit is raw criticality of the U--U edges `z w_i` and the A--U edges `z h_i`. Any bounded reuse capacity for one physical z would turn `(4.2)` into a lower bound on k and therefore a stronger population/gap theorem.

## 6. Scope

No global selected `(source,coordinate)` uniqueness, source-tuple capacity theorem, rooted-Q inequality, score ceiling, or H--U private-foot argument is used. The theorem is a direct consequence of the corrected boundary trichotomy, exact population equality `e=p`, tight-code transversality, and diameter two.
