# Witness geometry of a rigid Hall cut

Date: 2026-09-18

Status: hand structural consequence of the near-equality Hall theorem and the preserved non-direct A-edge certificate decomposition. No eventual second-extremal theorem is claimed.

## 1. Rigid Hall cut

Let `X` be a nonempty proper family of complementary tight-code pairs and put

> `x=a_X`, `Y=A\A_X`.

Assume the rigid conclusion from `HALL_DENSITY_STABILITY.md`:

> `M_X=0`,
>
> `E_X=0`.                                                `(R0)`

Thus:

1. the A-cut is complete: every vertex of `A_X` is adjacent to every vertex of `Y`;
2. every crossing A-edge chooses its criticality source endpoint in `Y`.

The second point refers to the fixed one-certificate-per-non-direct-edge choice used throughout the Hall system.

Because direct A-edges stay inside one complementary pair, every crossing edge is non-direct. Its chosen witness therefore belongs to one of the preserved non-direct channels: a matched-B witness or a U witness.

## 2. Singleton-head witness property

Fix `y in Y`. For every `x0 in A_X`, the crossing edge `yx0` is sourced at `y`. Let `w_{x0}` be its chosen criticality witness. Then

> `N(y) cap N(w_{x0})={x0}`.                              `(W1)`

Since `y` is adjacent to **every** vertex of `A_X`, `(W1)` forces

> `N(w_{x0}) cap A_X={x0}`.                               `(W2)`

Moreover, the witnesses `w_{x0}` are pairwise distinct as `x0` varies: a single fixed source--witness pair has a unique singleton common neighbour.

Hence every outside source `y` needs `x` distinct B-side witnesses whose neighbourhood in `A_X` is a singleton.

## 3. Matched witnesses are scarce

Let `mu_X` be the number of matched B-endpoints whose neighbourhood in `A_X` has size exactly one.

For each tight fibre `i`, its two matched endpoints partition `A_X` according to the i-th Boolean coordinate, so their A_X-degrees sum to `x`. If `x>=3`, at most one endpoint of a fibre can have A_X-degree one. Therefore

> `mu_X<=p` for `x>=3`.                                   `(MW)`

It follows from the singleton-head witness property that at least

> `(x-mu_X)_+`                                            `(UW0)`

of the witnesses for a fixed outside source `y` must lie in `U`.

In particular,

> `x<=mu_X+u<=p+u`.                                       `(SIZE)`

Thus a proper rigid Hall family of order at least three can never contain more than `p+u` A-vertices.

## 4. U-witness code concentration

The preserved A/U unique-common-neighbour theorem says that a U-witness used by an A-source `y` has tight Boolean code complementary to `c(y)`. Consequently all the U-witnesses counted in `(UW0)` lie in the **same** U-code class `U_bar(c(y))`.

Therefore, for every `y in Y`,

> `|U_bar(c(y))| >= (x-mu_X)_+`.                          `(UC)`

Let `h_Y` be the number of distinct tight Boolean codes represented in `Y`. Distinct source codes require distinct complementary U-code classes, so summing `(UC)` gives

> `h_Y (x-mu_X)_+ <= u`.                                 `(CODE)`

Using `mu_X<=p`,

> `h_Y (x-p)_+ <= u`.                                    `(CODE0)`

This is a strong collapse statement for a large rigid Hall family.

### Corollary 4.1 — outside-code collapse

For `x>p`:

> `h_Y <= floor(u/(x-p))`.                               `(COLL)`

In particular:

- if `x>p+u/2`, then `h_Y<=1`;
- if `x>p+u/3`, then `h_Y<=2`;
- more generally, if `x>p+u/k`, then `h_Y<=k-1`.

Thus a near-maximal low-density Hall family, once the `<1` stability threshold makes it rigid, forces the entire complementary A-layer into very few Boolean code classes.

## 5. Coupling back to Hall stability

If a capacity-low-density family `X` has

> `x(T0+tau-x)<1`,                                       `(S1)`

then the Hall stability theorem gives `(R0)`. Provided `x>=3`, the present theorem therefore adds

> `x<=p+u`,                                               `(S2)`
>
> `h_Y(x-p)_+<=u`.                                       `(S3)`

This is genuinely stronger than the numerical Hall mass bound `x<T0+tau`: it turns near equality into a concrete Boolean-code stability model.

The remaining one-code/two-code outside cases are attractive classification targets because the preserved aligned-code crowding theorem already self-prices a large same-code A-class, while the source-tuple machinery controls the corresponding U-code populations forced by `(UC)`.

## 6. Negative control

The published order-12 graph `X_3` is not excluded. Its canonical root has independent A and zero non-direct A-edge demand, so the rigid crossing-source configuration considered here is not forced.