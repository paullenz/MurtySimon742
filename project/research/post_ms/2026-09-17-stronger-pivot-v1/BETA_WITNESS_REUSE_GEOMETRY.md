# Beta-witness reuse geometry in the dense A--U layer

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural lemma; external review open. This note follows `UNMATCHED_INTERNAL_EDGE_CAPACITY.md`. It addresses the dense A--U layer forced there when `u=Theta(p)`.

Retain the near-full partial-Boolean setup with `p` tight fibres, unmatched set `U`, A-layer `A`, `|A|=a`, and beta-oriented P--U selected obligations.

For `x in A`, let

`ell_x`

be the number of P--U obligations whose canonical selected representative is beta-oriented from the unmatched source and uses the physical A--U edge incident with `x`.

The preserved alpha-spill theorem gives

`B_beta=sum_{x in A} ell_x >= pu-W_alpha >= pu-mu_alpha a`.       (1.1)

The point of this note is that a large `ell_x` is not merely a degree count: D2C criticality forces a strong coordinatewise exclusion pattern on every other neighbour of `x`.

---

## 1. One A-vertex cannot beta-certify two targets in the same tight fibre

Suppose `x` beta-certifies the P--U edge `yq`, where `q` is a matched endpoint and `y in U` is adjacent to `q`. The standard B-edge criticality orientation gives

`x~y`,

`x not~q`,

`N(x) cap N(q)={y}`.                                      (1.2)

This is the same witness condition used in the all-private B-edge pricing theorem.

If `x` beta-certified a second edge `zq` at the same matched target, then both `y,z` would lie in `N(x) cap N(q)`, contradicting (1.2). This is the beta-target injectivity from the companion note.

Nor can `x` beta-certify an edge to the tight mate `q'` in the same fibre: tightness makes every A-vertex adjacent to exactly one endpoint of that fibre, while beta certification requires nonadjacency to the target. Since `x not~q`, one has `x~q'`.

Therefore:

> **FIBREWISE BETA-LOAD BOUND**
>
> `ell_x<=p` for every `x in A`.                         (1.3)

Moreover the `ell_x` beta obligations used by `x` have targets in `ell_x` distinct tight fibres.

---

## 2. Reuse creates a codimension-ell exclusion pattern

Let `I_x` be the set of tight fibres in which `x` is used as a beta witness. For each `i in I_x`, let

- `q_i` be the matched target in fibre `i`;
- `y_i in U` be the unmatched source whose edge `y_i q_i` is beta-certified by `x`;
- `q_i'` be the tight mate of `q_i`.

Condition (1.2) says that **every neighbour of `x` other than `y_i` is nonadjacent to `q_i`**. Every vertex of `A union U` is a tight-fibre transversal, so nonadjacency to `q_i` forces adjacency to `q_i'`.

Hence, simultaneously for every `i in I_x`:

1. `x` is adjacent to `q_i'` and nonadjacent to `q_i`;
2. the exceptional source `y_i` is adjacent to `q_i`;
3. every other vertex of `(N_A(x) union N_U(x))\{y_i}` is adjacent to `q_i'`.

In particular, if `i,j in I_x` are distinct, then `y_j`, being another neighbour of `x`, is adjacent to `q_i'`. Thus on the coordinates in `I_x`, the beta sources form exactly a one-coordinate-deviation pattern around the transversal chosen by `x`:

- `y_i` differs from `x` in fibre `i`;
- `y_i` agrees with `x` in every fibre `j in I_x\{i}`;
- every other A- or U-neighbour of `x` agrees with `x` on all fibres in `I_x`.

Therefore:

> **BETA-REUSE EXCLUSION THEOREM.** If `ell_x=l`, then outside its `l` designated beta sources, every neighbour of `x` in `A union U` lies in the codimension-`l` transversal class obtained by fixing the `l` target fibres to the mates `q_i'`. The `l` beta sources occupy the `l` one-coordinate deviations from that class.       (2.1)

This is a physical adjacency statement; it does not depend on a choice of Boolean 0/1 labels.

It is much stronger than saying that beta codes lie in a Hamming sphere. It controls **all other neighbours of the reused witness**.

---

## 3. A linear unmatched layer forces linear beta load

Sum (1.3) over A and combine with (1.1). Let

`X_beta={x in A:ell_x>0}`.

Since each loaded A-vertex carries at most `p` obligations,

> `|X_beta| >= ceil(B_beta/p)`
>
> `          >= ceil(u-mu_alpha a/p)`.                  (3.1)

Also the mean beta load over all A-vertices is at least

> `(1/a) sum_x ell_x >= pu/a-mu_alpha`.                 (3.2)

Hence some A-vertex satisfies

> `ell_x >= ceil(pu/a-mu_alpha)`.                       (3.3)

In an above-threshold candidate `mu_alpha<=R_*`. Thus

> `|X_beta| >= ceil(u-R_* a/p)`,                         (3.4)
>
> `max_x ell_x >= ceil(pu/a-R_*)`.                      (3.5)

If `u=cp+O(1)` with fixed `c>0` and fixed `lambda`, then

`a=(2+c)p+O(1)`, `R_*=O(sqrt(p))`,

so

> `|X_beta| >= cp-O(sqrt(p))`,                           (3.6)

and

> `max_x ell_x >= [c/(2+c)]p-O(sqrt(p))`.               (3.7)

More strongly, the average load itself is

> `B_beta/a >= [c/(2+c)]p-O(sqrt(p))`.                  (3.8)

Thus a linear unmatched layer forces not just many beta edges but a large population of A-vertices whose criticality witnesses are reused across linearly many distinct tight fibres.

---

## 4. Interface with the sparse-U / dense-cross shape

The predecessor note shows, in the same regime,

- `q=e(U)=O(p^(3/2))`;
- `s=e(A,U)=Theta(p^2)`.

The present theorem shows how such a dense A--U graph must be organised if the selected beta system is to fit inside it: many A-vertices have a linear set `I_x` of tight targets, and all but one exceptional U-neighbour per target coordinate must avoid the corresponding matched endpoint.

So the remaining obstruction can be phrased as a concrete incidence problem:

> Can a D2C graph support a quadratically dense A--U bipartite layer in which linearly many A-vertices each impose a codimension-Theta(p) matched-fibre exclusion pattern on almost all of their U-neighbours, while the unmatched code support simultaneously proliferates over linearly many complementary code-pair types?

That is substantially more rigid than the original capacitated row problem.

The next useful theorem should aggregate these exclusion patterns over `x in X_beta`. A double count of `(x,z,i)` with `xz in E(A,U)` and `i in I_x` should compare the forced matched-fibre choices of U-vertices against the linear complementary-code-pair proliferation already proved. Such a count has a realistic chance of producing the missing linear slack term in `(GS-A)`.

No eventual second-extremal theorem is claimed. The order-12/32 `X_3` graph has `u=0` and is outside this argument.