# Same-type cross witnesses are independent

Date: 2026-09-20

Status: **internal conditional sharpening** of the all-R residual-grid cover. All daily-audit caveats remain binding.

## 1. D-type outside witnesses

A D-type outside cross witness has code `bar d` and one graph-fixed X-head:

`N_X(w)={x_w}`.

Take two such witnesses `w_1,w_2`. Suppose `w_1w_2` were an edge. It is a same-code U--U edge, so the raw same-code theorem requires an A-witness of complementary code d, hence a vertex `y in Y`, in one of the two orientations.

If the source is `w_1`, then y is adjacent to the unique X-head `x_{w_1}` because X--Y is complete, while `w_1x_{w_1}` is an edge. Thus `x_{w_1}` is a common neighbour of source `w_1` and witness y, distinct from the required singleton head `w_2`. Contradiction. The other orientation is identical.

Therefore

> every family of D-type outside cross witnesses is independent. `(D-INDEP)`

## 2. C-type outside witnesses

A C-type outside cross witness has code `bar C` and one graph-fixed Y-head:

`N_Y(w)={y_w}`.

Suppose two C-type witnesses `w_1,w_2` were adjacent. Same-code U--U criticality requires an A-witness of complementary code C, hence a vertex `x in X`.

If the source is `w_1`, then x is adjacent to the fixed Y-head `y_{w_1}` because X--Y is complete, and `w_1y_{w_1}` is an edge. Hence `y_{w_1}` is a common neighbour of source and witness, distinct from the required singleton head `w_2`. Contradiction. Again the opposite orientation is symmetric.

Therefore

> every family of C-type outside cross witnesses is independent. `(C-INDEP)`

The argument does not require distinct fixed heads; having a fixed opposite-side head at all is enough.

## 3. Physical q surcharge

The C- and D-type witness populations lie among the d z-nonneighbours, hence outside `U_-`, z, and the purified J-set. Their within-type nonedges are therefore new physical U--U holes, disjoint from:

- the `binom(k+1,2)` nonedges inside `U_-`;
- the k+d nonedges incident with z already charged in the all-R pinch;
- the `binom(J,2)` holes inside the purified J-set.

Thus the rooted triangle ceiling sharpens to

> `q <= binom(u,2)-binom(k+1,2)-k-d-binom(J,2)`
> `     -binom(s_C,2)-binom(s_D,2)`.                   `(Q-CROSS-INDEP)`

Cross-type C--D adjacencies are not constrained by this argument and are not charged.

## 4. Focused diagnostic effect

Adding `(Q-CROSS-INDEP)` to the residual-grid typed `e(X)=0` replay leaves

> **58,999** abstract rows admitting an `e(X)=0` tuple,

split as:

- **54,392** with `y>=2`;
- **4,607** with `y=1`.

The grid-cover checkpoint had 60,552 such slice rows, so same-type independence removes a further **1,553** from the focused slice.

This remains a slice diagnostic, not a total survivor count and not graph evidence.

## 5. Structural significance

The row-saturated and column-saturated cover regimes now self-price quadratically in the corresponding physical witness population. In particular:

- row-saturated cover forces `s_D>=g` and therefore at least `binom(g,2)` additional U--U holes;
- column-saturated cover forces `s_C>=y` and therefore at least `binom(y,2)` additional U--U holes.

The next clean synthesis is to combine this quadratic q loss with the exact pair/local score and residual identity, rather than inventing a new global inequality.
