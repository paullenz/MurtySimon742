# Code orientation forced by a large rigid Hall family

Date: 2026-09-18

Status: structural corollary of `RIGID_HALL_WITNESS_GEOMETRY.md`.

Let `X` be a nonempty proper rigid Hall family with `x=a_X>=3`, so its A-cut is complete and every crossing edge is sourced from the complementary A-family. Retain

> `mu_X = # {matched B-endpoints having exactly one neighbour in A_X}`.

The witness theorem gives

> `x<=mu_X+u`,                                            `(1)`

while each tight fibre contributes at most one singleton endpoint, so `mu_X<=p`.

## 1. Many singleton coordinates when `x>u`

For tight coordinate `i`, let

> `n_i^0=|{z in A_X:c_i(z)=0}|`,
>
> `n_i^1=|{z in A_X:c_i(z)=1}|`.

Since `x>=3`, a matched endpoint has singleton A_X-neighbourhood exactly when

> `min(n_i^0,n_i^1)=1`.

Thus `mu_X` is exactly the number of singleton coordinates. From `(1)`:

### Theorem 1.1

If `x>u`, then

> `#{i:min(n_i^0,n_i^1)=1} = mu_X >= x-u`.               `(SC)`

So a rigid Hall family larger than the unmatched layer must have at least `x-u` tight coordinates in which all but one A_X vertex choose the same matched endpoint.

Equivalently, if `z_i` is the unique minority vertex at singleton coordinate `i`, then the singleton-coordinate Hamming contribution satisfies

> `sum_{unordered {z,z'} subset A_X} d_H(c(z),c(z'))`
> ` >= (x-u)(x-1)`.                                      `(HE)`

No adjacency assumption inside `A_X` is used in `(HE)`; it is a pure Boolean-code stability statement.

## 2. Bi-sided complementary pairs collapse

Call a complementary code pair `P={c,bar c}` **bi-sided in X** if both `A_c` and `A_bar c` are nonempty.

At every coordinate, a bi-sided pair contributes at least one A_X vertex of each bit, because `c` and `bar c` differ in every tight coordinate. Therefore:

- if two distinct complementary pairs are bi-sided, then every coordinate has at least two vertices of each bit and `mu_X=0`;
- if one bi-sided pair has at least two vertices on each side, the same conclusion holds.

Combining with Theorem 1.1 gives:

### Theorem 2.1 — one-sided orientation theorem

If a rigid Hall family satisfies `x>u`, then:

1. at most **one** complementary code pair represented in `X` can be bi-sided;
2. if such an exceptional bi-sided pair exists, one of its two code classes has size exactly one;
3. every other occupied complementary pair in `X` is one-sided: exactly one of its two complementary A-code classes is populated.

Thus the large rigid family is not merely concentrated in Hall density; it admits an almost global **orientation of complementary code pairs**.

## 3. Interaction with the outside-code collapse

The companion witness theorem also gives, if `h_Y` is the number of distinct A-codes outside `X`,

> `h_Y(x-p)_+<=u`.                                       `(OUT)`

Hence a rigid family in the regime

> `x>max(u,p+u/2)`                                       `(BIG)`

simultaneously has:

- at least `x-u` singleton tight coordinates;
- an almost entirely one-sided orientation of its internal complementary pairs;
- **one single tight code** on the outside A-layer.

This is now a quite specific Boolean stability model. It is a more promising classification target than another scalar Hall estimate: the remaining geometry consists of a one-code outside class joined completely to an almost one-sided family of complementary code classes, with at least `x-u` singleton coordinates and with the U-class complementary to the outside code containing at least `x-mu_X` singleton-head witnesses.

## 4. Strategic note

The next attack on this rigid branch should exploit the preserved source/cylinder machinery on the one-sided code orientation. In particular, singleton coordinates identify explicit minority vertices; if many singleton coordinates are carried by few A_X vertices, they create high Hamming concentration, while if they are spread among many vertices, the code family has a large set of distinct one-coordinate deviations. Either outcome is substantially more structured than the unrestricted pair-allocation problem.

The order-12 `X_3` negative control is unaffected: the rigid crossing-cut configuration is not forced at its canonical root.