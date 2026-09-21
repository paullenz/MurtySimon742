# Equality-spectrum diameter obstruction for repeated one-code blocks

Date: 2026-09-21

Status: raw structural theorem inside the rigid complete one-code interface. This note strengthens `ONE_CODE_BOUNDARY_WITNESS_SPECTRUM.md` by using only diameter two, the repeated-code boundary trichotomy, and the exact equality spectrum. It does not address reachability of the rigid interface from arbitrary D2C graphs.

## 1. Setup

Let `Y=A_d` be a repeated outside block, `y>=2`, with selected matched-head count `m>=2`. Assume the generic universal-coordinate face `|C|=0` or `|C|>=3`, so the matched-forward head set is empty, `L=empty`.

The full-boundary theorem gives `p<=u-k`. The equality-spectrum note showed that equality in the population lower bound `u>=p`, namely `u=p`, forces

- `k=0`;
- exactly one U-vertex `w_i` of code `bar d xor e_i` for every coordinate `i`;
- every `w_i` is X-anticomplete;
- there are no other U-vertices.

For every selected matched-head coordinate `i in S`, the corresponding head `h_i in X` has code `d xor e_i`.

## 2. The unique boundary witness is Y-anticomplete

Fix a coordinate `i` and a source `y0 in Y`.

Because `y>=2`, the X-reverse arm of the boundary trichotomy is impossible. Because `L=empty`, matched-forward support is impossible. Therefore the boundary edge

`y0 q_i^{d_i}`

must use a U-forward witness of code `bar d xor e_i`.

Under `u=p`, there is exactly one such vertex, namely `w_i`. Hence `w_i` is the U-forward witness for coordinate `i` for **every** source `y0 in Y`.

The forward singleton condition is

`N(y0) cap N(w_i)={q_i^{d_i}}`.

In particular `y0 w_i` is not an edge. Since `y0` was arbitrary,

> **`N_Y(w_i)=empty` for every i.**                    `(2.1)`

The boundary theorem already gives `N_X(w_i)=empty`, so equality forces

> **`N_A(w_i)=empty` for every i.**                    `(2.2)`

Thus the whole U-layer is A-anticomplete on the equality face.

## 3. Complementary selected head and witness have no common neighbour

Fix any selected coordinate `i in S` (such an i exists because `m>=2`).

The selected head and its aligned U-forward witness have complementary tight codes:

`c(h_i)=d xor e_i`,

`c(w_i)=bar d xor e_i = overline{c(h_i)}`.

Hence tight-fibre transversality gives **no common matched endpoint** in B.

They also have no common neighbour elsewhere:

- the root `v` is not adjacent to `h_i in A`;
- every unmatched vertex lies in U, and equality makes every U-vertex X-anticomplete, so no U-vertex is adjacent to `h_i`;
- by `(2.2)`, `w_i` has no neighbour in A at all.

Therefore

> **`N(h_i) cap N(w_i)=empty`.**                        `(3.1)`

Also `h_i w_i` is not an edge because every U-forward witness is X-anticomplete.

Thus `dist(h_i,w_i)>2`, contradicting the assumption that G has diameter two.

## 4. Theorem

> **Equality-spectrum diameter obstruction.**  
> In a repeated one-code rigid cut with `y>=2`, `m>=2`, and generic universal-coordinate face `|C|=0` or `|C|>=3`, the equality case `u=p` is impossible. Hence
>
> **`u>=p+1`.**                                        `(4.1)`

This is stronger than the previous population lower bound `u>=p` and uses neither rooted-Q nor score accounting.

## 5. Immediate hostile-family consequence

The exact scalar family

`g0=1, y=p-1, c=u=p, lambda=p, x=p, k=0, m=p, r=0`

from `ONE_CODE_ROOTED_Q_HOSTILE_SCALAR_FAMILY.md` lies in the generic `C=empty` face and has `u=p`. Therefore it is **not physically realizable**, even before invoking rooted-Q or any score inequality.

Its failure mechanism is literal diameter-two failure: full boundary equality forces U to be A-anticomplete, while each selected head `h_i` is paired with an aligned complementary-code `w_i` having no possible common neighbour.

## 6. Exceptional faces

The same argument immediately excludes population equality whenever at least one selected matched-head coordinate is U-forward and the equality population exhausts U by boundary witnesses. Thus:

- on `|C|=1`, equality `u=p-1` is impossible because `m>=2` and at most one coordinate can be matched-forward, leaving at least one selected coordinate U-forward;
- on `|C|=2`, equality `u=p-2` is impossible whenever `m>=3`, because at most two coordinates are matched-forward;
- the only population-equality geometry not eliminated by this argument is the sharp exceptional possibility `|C|=2`, `m=2`, `L=S`, where both selected coordinates are matched-forward and no aligned selected coordinate is forced to have a U-forward witness.

These are direct consequences of the same diameter-two argument and should be treated as the corrected population frontier.

## 7. Scope

No source-tuple capacity theorem, global selected `(source,coordinate)` uniqueness, H--U private-foot argument, finite scan, or score inequality is used. The only inputs are the corrected repeated-code boundary trichotomy, full exposure/equality spectrum, and diameter two.
