# Beta-side hole identity and bipolar Boolean geometry

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate exact structural theorem, with an asymptotic ratio-two corollary. External review open.

This note sharpens the beta-reuse side-occupancy lemma. For a selected beta witness, the entire chosen tight-fibre side in `A union U` can be counted exactly from degrees. The result is an exact hole identity controlled by maximum-degree slack. At the ratio-two frontier it forces almost the whole `A union U` layer into two complementary Hamming clusters.

---

## 1. Exact side size of a tight-fibre endpoint

Fix a tight fibre

`P_i={q_i,q_i'}`.

Every vertex of `A union U` chooses exactly one endpoint of `P_i`. The matched endpoint `q_i'` has

- the root `v` as a neighbour;
- exactly one neighbour in each of the other `p-1` tight fibres;
- no neighbour at its tight mate `q_i`.

Hence, if `epsilon_{q_i'}=b-d(q_i')`, the number of `A union U` vertices choosing `q_i'` is exactly

> `p+u-epsilon_{q_i'}`.                                  (1.1)

The two side sizes sum correctly because the two endpoint slacks add to `lambda+1`.

---

## 2. A beta witness almost exhausts its chosen side

Suppose `x in A` beta-certifies the P--U obligation with unmatched source `y_i` and matched target `q_i`. Thus

`x~y_i`, `x not~q_i`, and `N(x) cap N(q_i)={y_i}`.       (2.1)

Since `x` is a tight-fibre transversal, it chooses `q_i'`.

Every other neighbour of `x` in `A union U` is nonadjacent to `q_i` by (2.1), and therefore also chooses `q_i'`. Thus the set

`{x} union (N_{A union U}(x)\{y_i})`                    (2.2)

lies entirely on the `q_i'` side.

Now

`d_{A union U}(x)=d(x)-p=p+u-epsilon_x`,                (2.3)

because `x` has exactly one matched neighbour in each of the `p` tight fibres. The set in (2.2) therefore has size

`p+u-epsilon_x`.                                         (2.4)

Comparing (2.4) with the exact side size (1.1) gives:

> **BETA-SIDE HOLE IDENTITY.**
>
> For every beta target `i in I_x`, the number of vertices in `A union U` which
>
> - choose the same endpoint of fibre `i` as `x`, but
> - are neither `x` nor adjacent to `x`,
>
> is exactly
>
> `epsilon_x-epsilon_{q_i'}`.                            (BH)

In particular,

> `epsilon_x>=epsilon_{q_i'}`                            (2.5)

for every beta target of `x`.

So the old side-occupancy inequality is the U-only shadow of an exact full-side exhaustion theorem.

---

## 3. Exact local bipolar code identities

Let

`S=A union U`,

and fix a beta-loaded `x`. Write `I=I_x`, `ell=|I|`, and let `c=c(x)` be its partial Boolean code.

### Neighbours

For every target coordinate `i in I`, exactly one S-neighbour of `x`, namely the designated source `y_i`, differs from `x` in coordinate `i`; every other S-neighbour agrees there.

Therefore

> `sum_{z in N_S(x)} dist_I(c(z),c)=ell`.                (3.1)

Indeed the designated sources form the one-coordinate-deviation pattern on `I`, while A-neighbours and central U-neighbours agree with `x` throughout `I`.

### Non-neighbours

Let

`R_x=S\({x} union N_S(x))`.

For a target `i`, the holes counted by `(BH)` are exactly the vertices of `R_x` which agree with `x` in coordinate `i`. Therefore

> `sum_{z in R_x} |{i in I:c(z)_i=c_i}|`
>
> `=ell epsilon_x-sum_{i in I} epsilon_{q_i'}`
>
> `<=ell epsilon_x`.                                     (3.2)

Agreement with `c` is disagreement with `bar c`. Hence (3.2) is equivalently

> `sum_{z in R_x} dist_I(c(z),bar c)`
>
> `=ell epsilon_x-sum_{i in I} epsilon_{q_i'}`.          (3.3)

Equations (3.1) and (3.3) are an exact **LOCAL BIPOLAR CODE IDENTITY**: neighbours of a beta-heavy witness lie close to its code, while non-neighbours lie close to the complementary code, with the error paid directly by maximum-degree slack.

---

## 4. Aggregate A-slack charge from matched endpoint slack

Summing the pointwise domination (2.5) over the beta targets of `x` gives

`ell_x epsilon_x >= sum_{i in I_x} epsilon_{q_i'}`.      (4.1)

Summing over all A-witnesses and using `ell_x<=p`,

> `pL_A`
>
> `>=sum_{beta (y,i)} epsilon_{mate(target(y,i))}`.       (4.2)

Thus beta obligations directed against fibres whose witness-side matched endpoint has positive slack consume A-side slack globally.

For fixed `lambda=-1` all tight endpoints have zero slack and (4.2) is vacuous, as it should be. For nonnegative or growing `lambda`, this provides a new exact payment term which may help remove the current fixed-`lambda` restriction.

---

## 5. Ratio-two corollary: all of A union U becomes bipolar

Assume an above-`M(n)` sequence with fixed `lambda` and `u/p -> 2`.

By `RATIO_TWO_POLARIZATION_AND_SOURCE_PAIR_STABILITY.md`, the beta-heavy population contains vertices with

`ell_x=p-o(p)`.                                          (5.1)

Also `(GS-A)` gives `L_A=O(p)`, while there are `(2+o(1))p` beta-heavy vertices. Since their total beta deficit is `o(p^2)`, one may choose a beta-heavy `x` satisfying simultaneously

`ell_x=p-o(p)`,                                          (5.2)

`epsilon_x=O(1)`.                                        (5.3)

For this `x`, put `I=I_x`, `c=c(x)`.

The S-neighbourhood size is exact:

`|N_S(x)|=p+u-epsilon_x=(3+o(1))p`.                     (5.4)

The non-neighbour set has

`|R_x|=p+u-lambda-2+epsilon_x=(3+o(1))p`.               (5.5)

By (3.1), the total target-coordinate distance of `N_S(x)` from `c` is only `ell_x=O(p)`. By (3.3), the total target-coordinate distance of `R_x` from `bar c` is at most

`ell_x epsilon_x=O(p)`.                                  (5.6)

Since only `o(p)` coordinates lie outside `I`, this yields:

> **FULL S-LAYER BIPOLAR STABILITY — internal candidate.**
>
> Along any fixed-`lambda`, above-threshold sequence with `u/p -> 2`, there exists a Boolean code `c` and a partition
>
> `A union U = S_+ dotcup S_-`
>
> with
>
> `|S_+|=(3+o(1))p`, `|S_-|=(3+o(1))p`,
>
> such that every vertex of `S_+` is `o(p)`-close to `c`, while all but `o(p)` vertices of `S_-` are `o(p)`-close to `bar c`.
>
> One may take `S_+={x} union N_S(x)` and `S_-=R_x`.

In fact the restricted Hamming energy is much stronger than merely `o(p)`: neighbours contribute only one target-coordinate error per designated source in total, while the entire non-neighbour cluster contributes only `O(p)` target-coordinate errors when `epsilon_x=O(1)`.

This upgrades the U-only two-cluster theorem to an almost complete bipolar description of the entire partial-Boolean layer.

---

## 6. Why this is a better next frontier

At the new ratio-two endpoint, a hypothetical counterexample is no longer just a dense A--U graph with balanced code columns. It must look, on `A union U`, like two nearly complementary Boolean clouds of size about `3p` each, cut almost exactly by the adjacency of one low-slack beta-heavy A-vertex.

The next attack should exploit D2C criticality across this bipolar cut. Natural targets are:

1. price A-edges inside the near-`c` neighbour cloud, where many endpoints share almost all matched neighbours;
2. price distance-two requirements between the two almost-complementary clouds, which share few matched neighbours;
3. combine (4.2) with the tight-pair slack distribution to extend the ratio-two analysis beyond fixed `lambda`.

This is more structured than another row-cover or ratio-constant optimization.

---

## 7. Trust boundary

- `(BH)`, (3.1), (3.3), and (4.2) are exact hand identities/inequalities in the partial-Boolean near-full branch.
- The ratio-two bipolar corollary additionally uses the fixed-`lambda` polarization theorem and the above-threshold bound `L_A=O(p)`.
- No statement here applies to the full-tight `u=0` hostile control; the published 12/32 `X_3` remains untouched.
- No global eventual second-extremal theorem is claimed.
