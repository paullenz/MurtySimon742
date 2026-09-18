# Ratio-two polarization and beta-source-pair Hamming stability

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural theorems; external review open. This note starts from the directional ratio-two theorem in `DIRECTIONAL_BETA_FIBRE_MOMENT_AND_RATIO_TWO.md` and studies the only asymptotic configuration that can approach its new endpoint.

The principal outputs are:

1. an exact Hamming-capacity inequality for pairs of designated beta sources;
2. a two-population polarization of the A-layer whenever `u/p -> 2` at fixed `lambda`;
3. near saturation of the source-pair inequality at that endpoint;
4. a resulting two-cluster description of the unmatched Boolean codes.

No global eventual second-extremal theorem is claimed.

---

## 1. Exact beta-source-pair Hamming capacity

For `x in A`, recall the designated beta-source set

`Y_x={y_i:i in I_x}`,

with `|Y_x|=ell_x`. The source-distinctness theorem says that the `y_i` are pairwise distinct.

For distinct unmatched vertices `y,z`, let

`M(y,z)=|{x in A:{y,z} subseteq Y_x}|`.

Fix one such common witness `x`. Suppose `y` is assigned to coordinate `i` in `I_x`. Since `z` is another designated source of `x`, beta-reuse geometry says

- `y` differs from `x` in coordinate `i`;
- `z` agrees with `x` in coordinate `i`.

Hence

`c(y)_i != c(z)_i`.                                      (1.1)

Moreover, for fixed `(y,i)`, the selected beta witness is unique: it is the chosen representative of the single physical P--U obligation at source `y` and fibre `i`. Therefore distinct common witnesses `x` give distinct disagreement coordinates `i` for `y`.

Consequently

> `M(y,z)<=dist_H(c(y),c(z))`.                            (1.2)

Summing over unordered pairs gives

`sum_x binom(ell_x,2)`

` <= sum_{y<z} dist_H(c(y),c(z))`

` =sum_i u_i^0 u_i^1`

` =(p u^2-H)/4`.                                         (1.3)

Thus:

> **BETA-SOURCE-PAIR HAMMING CAPACITY**
>
> `sum_x binom(ell_x,2) <= (p u^2-H)/4`.                 (BSP)

Equivalently,

> `sum_x ell_x(ell_x-1) <= (p u^2-H)/2`.                (1.4)

This is a hand injection and uses the selected system only through source-coordinate uniqueness.

---

## 2. Exact opposite-side capture gap

For an unmatched source `y` and coordinate `i`, let

`O_i(y)={z in U:c(z)_i != c(y)_i}`.

If the obligation `(y,i)` is beta-selected with witness `x=x(y,i)`, then

`Y_x\{y} subseteq O_i(y)`.                               (2.1)

Indeed every other designated source agrees with `x` at coordinate `i`, while `y` differs from `x` there.

The total ordered Hamming capacity is

`sum_{y in U} sum_i |O_i(y)|=(p u^2-H)/2`.              (2.2)

On the other hand, summing the covered opposite-side vertices over beta obligations gives

`sum_{beta (y,i)} (ell_{x(y,i)}-1)`

`=sum_x ell_x(ell_x-1)`.                                 (2.3)

Therefore the exact nonnegative gap

> `G_cap=(p u^2-H)/2-sum_x ell_x(ell_x-1)`               (2.4)

has the concrete decomposition

`G_cap`

`=sum_{alpha (y,i)} |O_i(y)|`

` +sum_{beta (y,i)} [|O_i(y)|-(ell_{x(y,i)}-1)]`.        (2.5)

So `G_cap` measures, literally, the source-coordinate Hamming capacity not captured by the designated source sets.

---

## 3. Polarization when u/p tends to 2

Assume now an above-`M(n)` sequence with

- fixed `lambda`;
- `p -> infinity`;
- `u/p -> 2`.

The directional deficiency--Hamming budget gives

`H=o(p^3)`,                                               (3.1)

`J=sum_x(p-ell_x)(u-d_x)=o(p^3)`.                        (3.2)

The preserved high-complexity estimates also give

`h_alpha=o(p^2)`, `q=o(p^2)`, `E_U=o(p^2)`.              (3.3)

Hence

`B=sum_x ell_x=pu-h_alpha=(2+o(1))p^2`,                 (3.4)

`a=(4+o(1))p`,                                           (3.5)

and

`s=u(p+u-1)-2q-E_U=(6+o(1))p^2`.                        (3.6)

Choose any sequence `eta_p -> 0` slowly enough that

`H/(eta_p^2 p^3) -> 0`

and

`J/(eta_p p^3) -> 0`.                                    (3.7)

Let

`K={i:|d_i|>=2 eta_p p}`.

Then `|K|=o(p)` by (3.1).

If

`d_U(x)>u/2+eta_p p+1`,                                  (3.8)

then every target coordinate `i in I_x` satisfies

`|d_i|>2 eta_p p`

by the loaded-witness side-occupancy lemma. Hence

`ell_x<=|K|=o(p)`.                                       (3.9)

Since `a=O(p)`, all vertices satisfying (3.8) contribute only `o(p^2)` beta load in total.

Define

`X={x in A:d_U(x)<=u/2+eta_p p+1}`,                      (3.10)

and `Z=A\X`.

Then

`sum_{x in X} ell_x=(2+o(1))p^2`.                       (3.11)

For `x in X`,

`u-d_U(x)>=(1-o(1))p`.

Using (3.2),

`sum_{x in X}(p-ell_x)=o(p^2)`.                         (3.12)

Equations (3.11)--(3.12) imply

> `|X|=(2+o(1))p`,                                      (3.13)
>
> `sum_{x in X} ell_x=(2+o(1))p^2`,                    (3.14)
>
> `sum_{x in X}(p-ell_x)=o(p^2)`.                      (3.15)

Since `a=(4+o(1))p`,

> `|Z|=(2+o(1))p`,                                      (3.16)
>
> `sum_{z in Z} ell_z=o(p^2)`.                         (3.17)

Finally use (3.6). Vertices in `X` have U-degree at most `(1+o(1))p`, while vertices in `Z` have U-degree at most `u=(2+o(1))p`. The capacities of the two classes sum to exactly the required leading term `6p^2`. Therefore both saturate asymptotically:

> `sum_{x in X} d_U(x)=(2+o(1))p^2`,                   (3.18)
>
> `sum_{z in Z} d_U(z)=(4+o(1))p^2`.                   (3.19)

Thus the endpoint has a rigid two-population shape:

- `X`: about `2p` vertices, beta load `p-o(p)` on average and U-degree `p+o(p)` on average;
- `Z`: about `2p` vertices, beta load `o(p)` on average and U-degree `2p-o(p)` on average.

This is the **RATIO-TWO POLARIZATION THEOREM**.

---

## 4. The beta-source pair inequality also saturates

From (3.13)--(3.15),

`sum_{x in X} ell_x(ell_x-1)=(2+o(1))p^3`.              (4.1)

The `Z` contribution is nonnegative, while by `u/p -> 2` and `H=o(p^3)`, the right side of (1.4) is

`(p u^2-H)/2=(2+o(1))p^3`.                              (4.2)

Therefore

> `G_cap=o(p^3)`.                                        (4.3)

So the source-pair Hamming injection is asymptotically saturated, not merely feasible.

Equivalently, among the `Theta(p^3)` ordered source-coordinate Hamming disagreements, only `o(p^3)` fail to be captured by the designated source set of the selected beta witness.

This is a stronger equality description than the earlier Jensen stability statement.

---

## 5. A two-cluster theorem for U

The saturation has a direct geometric consequence.

For a beta witness `x`, define its capture deficit

`g_cap(x)=sum_{i in I_x} [|O_i(y_i)|-(ell_x-1)]`.        (5.1)

By (2.5),

`sum_x g_cap(x)<=G_cap=o(p^3)`.                          (5.2)

Together with (3.13)--(3.15), there exist beta-heavy vertices `x in X` satisfying simultaneously

`ell_x=p-o(p)`,                                          (5.3)

`g_cap(x)=o(p^2)`.                                       (5.4)

Fix such an `x`, and write `c=c(x)`, `I=I_x`, `Y=Y_x`.

For every designated source `y_j in Y`, beta-reuse geometry gives

`c(y_j)_i=c_i` for all `i in I\{j}`,

and

`c(y_j)_j!=c_j`.                                         (5.5)

Since `|[p]\I|=o(p)`, every vertex of `Y` is at Hamming distance `o(p)` from `c`; on the target coordinates the distance is exactly one.

Now fix `i in I`. The opposite side `O_i(y_i)` is precisely the set of U-vertices whose coordinate-`i` bit equals `c_i`. The set `Y\{y_i}` lies inside that side. Therefore

`|O_i(y_i)|-(ell_x-1)`

is exactly the number of vertices in `U\Y` which agree with `c` at coordinate `i`. Summing over `i` and using (5.4),

`sum_{z in U\Y} |{i in I:c(z)_i=c_i}|=o(p^2)`.          (5.6)

But agreement with `c` is disagreement with `bar c`. Since

`|U\Y|=p+o(p)` and `|I|=p-o(p)`,                        (5.7)

(5.6) says that the vertices outside `Y` have average Hamming distance `o(p)` from `bar c`.

Consequently:

> **UNMATCHED TWO-CLUSTER STABILITY — internal candidate.**
>
> Along any fixed-`lambda`, above-threshold sequence with `u/p -> 2`, there exists a Boolean code `c` and a partition
>
> `U=U_+ dotcup U_-`,
>
> `|U_+|=p+o(p)`, `|U_-|=p+o(p)`,
>
> such that every vertex of `U_+` is `o(p)`-close to `c`, while all but `o(p)` vertices of `U_-` are `o(p)`-close to `bar c`.
>
> Moreover `U_+` may be chosen as the designated beta-source set of one beta-heavy A-vertex.

This is the first theorem in the unmatched branch that converts the analytic ratio endpoint into a concrete global Boolean geometry.

---

## 6. Strategic consequence

The ratio-two frontier is no longer an arbitrary high-complexity unmatched configuration. To approach it, the graph must simultaneously exhibit

1. an A-layer polarized into roughly `2p` beta-heavy/half-U-degree vertices and `2p` beta-light/almost-U-universal vertices;
2. almost balanced U-code columns (`H=o(p^3)`);
3. asymptotic saturation of the beta-source pair Hamming injection;
4. a two-cluster U-code distribution around a complementary pair `c,bar c`.

The next structural target should use D2C criticality on this bipolar configuration, rather than optimize the ratio constant further. In particular, beta-heavy A-vertices have large A-degree and, by the beta-reuse exclusion theorem, all their A-neighbours lie in the same near-`c` cylinder. The companion beta-side hole identity makes that local bipolarity exact up to degree slack.

The published 12/32 `X_3` control has `u=0` and is outside every assertion here.

---

## 7. Trust boundary

- `(BSP)` and the capture-gap decomposition are hand injections.
- The polarization and two-cluster conclusions are asymptotic internal candidates, conditional on fixed `lambda` and `u/p -> 2` along an above-threshold sequence.
- The proof uses the already-preserved selected-system uniqueness, high-complexity alpha/q bounds, and the new directional deficiency--Hamming budget.
- No claim is made for arbitrary growing `lambda` or for the separate `Q=0` branch.
