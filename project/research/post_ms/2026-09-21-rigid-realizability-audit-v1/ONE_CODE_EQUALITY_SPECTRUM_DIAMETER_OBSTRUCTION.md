# Equality-spectrum diameter obstruction for repeated one-code blocks

Date: 2026-09-21

Status: raw structural theorem inside the rigid complete one-code interface. This note strengthens `ONE_CODE_BOUNDARY_WITNESS_SPECTRUM.md` by using only diameter two, the repeated-code boundary trichotomy, and the exact equality spectrum. It does not address reachability of the rigid interface from arbitrary D2C graphs.

## 1. Setup

Let `Y=A_d` be a repeated outside block, `y>=2`, with selected matched-head count `m>=2`. The full-boundary theorem gives

`p <= u-k+|L|`,

where `L=L(d,X)` is the matched-forward support set and `k>=0` is the selected complementary-U count of a minimum outside source. Therefore

`u >= p-|L|`.

Suppose equality holds:

> `u=p-|L|`.                                           `(1.1)`

Then equality in the cover forces `k=0`, every coordinate outside L to be U-forward, and U to be exhausted by exactly one vertex

`w_i in U_{bar d xor e_i}`

for each `i notin L`. There are no other U-vertices. Every such `w_i` is X-anticomplete.

For every selected matched-head coordinate `i in S`, the corresponding head `h_i in X` has code

`c(h_i)=d xor e_i`.

Full exposure also gives `C subseteq [p]\S`.

## 2. Equality always leaves a selected coordinate U-forward

We first check the only possible obstruction to the argument: could all selected coordinates lie in L?

- If `C=empty` or `|C|>=3`, then `L=empty`.
- If `|C|=1`, then `|L|<=1`, while `m=|S|>=2`, so `S\L` is nonempty.
- If `|C|=2`, any universal coordinate that is a global leaf already sees the other universal coordinate. Hence its sole possible neighbour, and therefore the head it supports, is the **other coordinate in C**. Thus `L subseteq C`. Since `C cap S=empty`, again `S cap L=empty`.

Therefore in every universal-coordinate face there exists

> **`i in S\L`.**                                      `(2.1)`

That coordinate is necessarily U-forward under equality `(1.1)`.

## 3. The unique aligned boundary witness is Y-anticomplete

Fix `i in S\L` and a source `y0 in Y`.

Because `y>=2`, the X-reverse arm of the boundary trichotomy is impossible. Because `i notin L`, matched-forward support is impossible. Therefore the boundary edge

`y0 q_i^{d_i}`

must use a U-forward witness of code `bar d xor e_i`.

Under population equality there is exactly one such vertex, namely `w_i`. Hence `w_i` is the U-forward witness at coordinate i for **every** source `y0 in Y`.

The forward singleton condition is

`N(y0) cap N(w_i)={q_i^{d_i}}`.

In particular `y0 w_i` is not an edge. Since `y0` was arbitrary,

> **`N_Y(w_i)=empty`.**                                `(3.1)`

The boundary theorem already gives `N_X(w_i)=empty`, so

> **`N_A(w_i)=empty`.**                                `(3.2)`

## 4. Complementary selected head and witness have no common neighbour

The selected head and its aligned U-forward witness have complementary tight codes:

`c(h_i)=d xor e_i`,

`c(w_i)=bar d xor e_i = overline{c(h_i)}`.

Hence tight-fibre transversality gives no common matched endpoint in B.

They also have no common neighbour elsewhere:

- the root v is not adjacent to `h_i in A`;
- equality exhausts U by U-forward witnesses, every one of which is X-anticomplete, so no unmatched vertex is adjacent to `h_i`;
- by `(3.2)`, `w_i` has no neighbour in A.

Therefore

> **`N(h_i) cap N(w_i)=empty`.**                        `(4.1)`

Also `h_iw_i` is not an edge because every U-forward witness is X-anticomplete. Thus `dist(h_i,w_i)>2`, contradicting diameter two.

## 5. Theorem — strict boundary-population inequality

> **Equality-spectrum diameter obstruction.**  
> In every repeated one-code rigid cut with `y>=2` and `m>=2`, population equality `u=p-|L|` is impossible. Therefore
>
> **`u >= p-|L|+1`.**                                  `(5.1)`

Combining with the global leaf theorem gives the exact facewise consequences

- `C=empty` or `|C|>=3`: **`u>=p+1`**;
- `|C|=1`: **`u>=p`**;
- `|C|=2`: **`u>=p-|L|+1>=p-1`**.

There is no surviving `m=2,L=S` exception: in the two-universal-coordinate face simultaneous matched-forward support is internal to C, so `L subseteq C` while `S cap C=empty`.

## 6. Immediate hostile-family consequence

The exact scalar family

`g0=1, y=p-1, c=u=p, lambda=p, x=p, k=0, m=p, r=0`

from `ONE_CODE_ROOTED_Q_HOSTILE_SCALAR_FAMILY.md` lies in the generic `C=empty` face and has `u=p`. It violates `(5.1)` and is therefore **not physically realizable**, even before invoking rooted-Q or any score inequality.

Its failure mechanism is literal diameter-two failure: full boundary equality forces the aligned U-witness to be A-anticomplete, while its selected head has complementary tight code, leaving the pair with no common neighbour.

## 7. Scope

No source-tuple capacity theorem, global selected `(source,coordinate)` uniqueness, H--U private-foot argument, finite scan, or score inequality is used. The only inputs are the corrected repeated-code boundary trichotomy, full exposure/equality spectrum, the global matched-leaf theorem, tight-code transversality, and diameter two.
