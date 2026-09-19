# The cube-face saturation family and why `X_3` is the unique dense tight-fibre member

Date: 2026-09-19

Status: exact graph construction and negative-control theorem for the eventual second-extremal programme. This does not prove the eventual classification.

## 1. Motivation

The mandatory published order-12, size-32 graph `X_3` is represented at its canonical root by a cube `Q_3`: the root is adjacent to all cube vertices and three additional vertices see the three coordinate-zero faces. At that root every B--A nonedge slot is consumed by a rooted cube-edge criticality certificate, so `r=f=delta=0`.

It is useful to know whether that mechanism is an isolated accident. It is not: the exact witness-slot saturation extends to every hypercube dimension. What *is* exceptional about dimension three is that it is simultaneously

1. diameter-2-critical;
2. exact-slot-saturated;
3. above the second-extremal target `M(n)`; and
4. inside the tight-antipode / partial-Boolean branch (`p>0`).

The higher-dimensional saturation controls are much sparser and have **no tight fibres at the cube root**. This cleanly separates the hostile `X_3` phenomenon from the eventual dense tight-fibre branch.

---

## 2. Construction

For `k>=1`, define `X_k` as follows.

- Cube vertices are the binary strings `x in {0,1}^k`, with the usual hypercube edges.
- Add a root `r` adjacent to every cube vertex.
- Add vertices `a_1,...,a_k`.
- Join `a_i` to exactly the cube vertices whose `i`-th bit is zero.
- There are no other edges.

Thus

> `n_k=2^k+k+1`,                                         `(2.1)`
>
> `m_k=k2^{k-1}+2^k+k2^{k-1}`
> `   =(k+1)2^k`.                                        `(2.2)`

At the root `r`,

> `B=Q_k`, `|B|=2^k`,                                    `(2.3)`
>
> `A={a_1,...,a_k}`, `|A|=k`.                            `(2.4)`

The rooted triangle count is

> `Q=e(G[B])=k2^{k-1}`.                                  `(2.5)`

---

## 3. Diameter two

### Lemma 3.1

`X_k` has diameter at most two for every `k>=1`.

### Proof

- Any two cube vertices have the common neighbour `r`.
- `r` and `a_i` have a common cube neighbour with bit `i=0`.
- `a_i` and `a_j` have a common cube neighbour with both coordinates zero.
- If a cube vertex `x` has `x_i=0`, it is adjacent to `a_i`; if `x_i=1`, flipping coordinate `i` produces a cube neighbour of `x` adjacent to `a_i`.

The graph is not complete, so its diameter is two. `square`

---

## 4. Every edge is critical for `k>=3`

There are three edge types.

### Lemma 4.1 — root--cube edges

Fix a cube vertex `x`. For `k>=3`, writing `bar x` for its bitwise complement,

> `N(x) cap N(bar x)={r}`.                               `(4.1)`

Hence the edge `rx` is critical.

### Proof

`x` and `bar x` are at cube Hamming distance `k>=3`, so they have no common cube neighbour. They have no common face vertex because in every coordinate exactly one of the two bits is zero. Both are adjacent to `r`. Thus `(4.1)` holds. Deleting `rx` destroys the unique two-step path from `x` to `bar x` through `r`. `square`

### Lemma 4.2 — cube edges

Let cube vertices `x,y` differ in coordinate `i`, with `x_i=1` and `y_i=0`. Then

> `N(x) cap N(a_i)={y}`.                                 `(4.2)`

Hence the cube edge `xy` is critical.

### Proof

The neighbours of `a_i` are exactly the cube vertices with `i`-th bit zero. Among the cube neighbours of `x`, exactly one has bit `i=0`: the vertex obtained by flipping coordinate `i`, namely `y`. `square`

### Lemma 4.3 — face--cube edges

Let `x_i=0` and let `x^i` be obtained from `x` by flipping coordinate `i` to one. Then

> `N(a_i) cap N(x^i)={x}`.                               `(4.3)`

Hence the edge `a_i x` is critical.

### Proof

Again a common neighbour of `a_i` and `x^i` must be a cube vertex with bit `i=0`. Among the cube neighbours of `x^i`, the unique such vertex is `x`. `square`

### Theorem 4.4 — infinite exact D2C saturation family

For every `k>=3`, `X_k` is diameter-2-critical.

This is a genuine infinite D2C family, not merely an abstract rooted incidence model.

---

## 5. Exact rooted witness-slot saturation

At the cube root, every face vertex `a_i` is nonadjacent to exactly the `2^{k-1}` cube vertices with bit `i=1`. Hence the number of B--A nonedge slots is

> `|Omega|=k2^{k-1}=Q`.                                  `(5.1)`

The certificate in Lemma 4.2 maps a cube edge in coordinate `i`, oriented from its bit-one endpoint, to exactly the missing slot `(x,a_i)`. This is a bijection

> `E(Q_k) <-> Omega`.                                    `(5.2)`

Therefore

> `r=0`.                                                  `(5.3)`

The A-layer is independent, so

> `f=0`.                                                  `(5.4)`

Moreover

> `b(n-b)=2^k(k+1)=m_k`,                                 `(5.5)`

hence the root residual defect is

> `delta=b(n-b)-m_k=0=r-f`.                              `(5.6)`

Thus exact witness-slot saturation is not peculiar to order 12. It persists in arbitrarily large D2C graphs.

The eventual programme therefore cannot use `r=0` or hypercube-like slot saturation *alone* as a small-order obstruction; density/balance is essential.

---

## 6. Only `X_3` is dense enough

For `k=3`,

> `n_3=12`, `m_3=32`, `M(12)=31`.                        `(6.1)`

So `X_3` exceeds the live second-extremal target by one edge.

For every `k>=4`,

`(n_k-1)^2/4-m_k`

`=[2^k(2^k-2k-4)+k^2]/4`.                                `(6.2)`

Since `2^k-2k-4>=4` at `k=4` and increases thereafter, the right side is at least `20`. Consequently

> `m_k < floor((n_k-1)^2/4) < M(n_k)` for every `k>=4`.  `(6.3)`

### Theorem 6.1 — unique above-target member

Among the D2C cube-face graphs `X_k`, `k>=3`, the only graph at or above `M(n)` is `X_3`.

Thus the infinite exact-saturation continuation immediately falls away from the dense second-extremal regime after dimension three.

---

## 7. Tight antipodes exist only in dimension three

The distinction is even sharper at the rooted tight-fibre level.

### Lemma 7.1 — `X_3` has four tight fibres

At the cube root of `X_3`, each antipodal cube pair `{x,bar x}` is a tight antipode pair. The four antipodal pairs partition `B`, so

> `p=4`, `u=0`.                                           `(7.1)`

### Proof

Antipodes in `Q_3` have no cube common neighbour, and no face vertex is adjacent to both; their only common neighbour is `r`. Every other cube vertex is a neighbour of exactly one endpoint of an antipodal pair, and every face vertex sees exactly one endpoint because the two bit strings are complementary. This is exactly the tight-pair transversal condition. `square`

### Lemma 7.2 — no tight fibre for `k>=4`

At the cube root of `X_k`, `k>=4`, there is no tight antipode pair. Hence

> `p=0`, `u=2^k`.                                        `(7.2)`

### Proof

Suppose cube vertices `x,y` formed a tight pair. Every other cube vertex would have to be adjacent to exactly one of `x,y`. Because the pair has no common neighbour in `B`, their cube neighbourhoods are disjoint, so together they contain at most `2k` cube vertices. Tight transversality would require them to cover all `2^k-2` other cube vertices. But

> `2^k-2>2k` for `k>=4`.

Contradiction. `square`

### Corollary 7.3 — `X_3` is the unique tight-fibre saturation member

Dimension three is the unique member of this exact-saturation D2C family in which the saturated cube root also supplies a nontrivial tight-fibre decomposition.

This is a useful explanation for why `X_3` is such a dangerous negative control for the present tight-code/Hall machinery: it sits exactly at the one hypercube dimension where slot saturation, high relative density and tight antipodal transversality coexist.

---

## 8. Regression values

The companion graph-level checker reconstructs:

| graph | `n` | `m` | `M(n)` | `p` | `u` | `Q` | `r` | `f` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `X_3` | 12 | 32 | 31 | 4 | 0 | 12 | 0 | 0 |
| `X_4` | 21 | 80 | 101 | 0 | 16 | 32 | 0 | 0 |
| `X_5` | 38 | 192 | 343 | 0 | 32 | 80 | 0 | 0 |

All three are independently checked to be D2C before any rooted calculation is accepted.

---

## 9. Strategic consequence

The higher-dimensional controls change the interpretation of the order-12 exception in a useful way.

- The **saturation mechanism is real and scalable**; it must not be dismissed as an order-12 coincidence.
- The **dangerous density is not scalable** inside this family; already `X_4` is 21 edges below `M(21)`.
- The **tight-fibre interface is dimension-three specific** in this family; the partial-Boolean/Hall branch is therefore not merely rediscovering generic hypercube saturation.

For the eventual dense theorem, the right target remains a balance/stability statement: if a large graph is close enough to the balanced second-extremal density while also carrying a substantial tight-fibre structure, then the exact-saturation geometry must either collapse into a forbidden small-dimensional configuration or incur enough residual/slack cost to fall below `M(n)`.

That is compatible with, and strengthens the motivation for, the pair-local rigid programme rather than replacing it.
