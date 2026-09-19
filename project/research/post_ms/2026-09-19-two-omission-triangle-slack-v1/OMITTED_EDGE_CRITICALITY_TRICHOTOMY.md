# Omitted-edge criticality trichotomy in the minimal full-support two-omission model

Date: 2026-09-19

Status: **proved local structural lemma** inside the already-purified rigid one-code `z=1`, `h=0`, full-support branch. This note deliberately does not assume any unverified lower bound on the B-degree of a tight-code source.

The notation and trust boundary are those of `TWO_OMISSION_TRIANGLE_SLACK_LEDGER.md`. In particular `nu=0` means every source `s in Y_i` is adjacent to its omitted vertex `o_i`; `o_1,o_2` share the duplicated X-head `x_*`; `X--Y` is complete; `Y` and `U_-` are independent; and every `o_i` has unique X-neighbour `x_*`.

---

## 1. Generic critical-edge orientation lemma

Let `uv` be an edge of a diameter-two-critical graph G. If `uv` lies in a triangle, then there is a vertex `z notin {u,v}` such that one of the following holds:

1. `uz notin E`, `vz in E`, and

   `N(u) intersect N(z) = {v}`;

2. `vz notin E`, `uz in E`, and

   `N(v) intersect N(z) = {u}`.

### Proof

Deleting `uv` raises the diameter above two, so some pair has distance greater than two in `G-uv`. Any length-at-most-two path in G which disappears on deleting `uv` must use `uv`. A two-edge path containing `uv` has u or v as an endpoint, so a damaged pair can be chosen with one endpoint in `{u,v}`. Because `uv` lies in a triangle, u and v themselves remain at distance two after deletion. Thus the other endpoint is an external vertex z. For the corresponding two-edge path through the deleted edge to be the only path of length at most two, the stated adjacency and singleton-common-neighbour condition are necessary and sufficient. `square`

This lemma is elementary, but it is useful here because the omitted edge sits in a very constrained triangle.

---

## 2. Apply the lemma to an omitted edge

Assume `nu=0` and fix `s in Y_i`. Then `s o_i` is an edge. Moreover

`s - x_* - o_i - s`

is a triangle, because `X--Y` is complete and `x_*` is the X-head of `o_i`.

Apply the generic lemma to `s o_i`.

### Orientation A: the damaged pair is based at `o_i`

There is z with

- `s z in E`,
- `o_i z notin E`,
- `N(o_i) intersect N(z)={s}`.

Then z cannot lie in B: both `o_i` and every B-vertex are adjacent to the root v, which would be a second common neighbour. It also cannot be v because `o_i v` is an edge, whereas this orientation requires `o_i z` to be a nonedge. Thus z lies in A.

Since z is adjacent to s and Y is independent, z lies in X. But every z in X is adjacent to every source in Y, while `o_i` is adjacent to every source in `Y_i` when `nu=0`. Hence

`Y_i subseteq N(o_i) intersect N(z)`.

Therefore:

> **Lemma 2.1.** If `|Y_i|>=2`, Orientation A is impossible.       `(A-exclusion)`

So every omitted edge from a non-singleton omission class must be certified in the opposite orientation.

---

## 3. Orientation B gives a three-way physical witness classification

For `s in Y_i` with `|Y_i|>=2`, there is therefore z with

- `o_i z in E`,
- `s z notin E`,
- `N(s) intersect N(z)={o_i}`.                              `(3.1)`

We now locate z.

### z is not in X

This is immediate from `X--Y`: s is adjacent to every X-vertex, contradicting `s z notin E`.

### z is not in Y

If z lies in Y, then both s and z are adjacent to every vertex of X. Since `k=x-g>0`, we have `x>0`, so `N(s) intersect N(z)` contains an X-vertex. But `(3.1)` says the common neighbourhood is the singleton `{o_i}`, and `o_i notin X`. Contradiction.

### z is not in `U_-`

The purified full-support branch has `e(G[U_-])=0`, whereas `(3.1)` requires the edge `o_i z`.

Thus the witness z lies in exactly one of the following locations:

1. **the root:** `z=v`;
2. **outside unmatched set:** `z in U_o=U\U_-`;
3. **the matched B-layer:** z is one of the 2p matched B-vertices.

The singleton condition immediately adds more information.

- If `z=v`, then

  `N(s) intersect N(v)=N_B(s)={o_i}`.                      `(ROOT)`

  Thus the source has B-degree exactly one.

- If `z in U_o`, then `s z` is a Y--U_o nonedge and hence contributes one unit to `H_Y`. Moreover z has no X-neighbour: otherwise any X-neighbour of z would also be adjacent to s and would be a second common neighbour in `(3.1)`. Thus

  `d_X(z)=0`.                                              `(OUT)`

- If z lies in the matched B-layer, again `d_X(z)=0`. The required edge `o_i z` is an edge wholly inside `N(v)` and is not in the `U_- -- U_o` layer, so it contributes to `Q_rest`. Thus

  `Q_rest>=1`.                                             `(MATCHED)`

We have proved:

### Theorem 3.1 — omitted-edge criticality trichotomy

Assume `nu=0`. For every source `s in Y_i` belonging to a non-singleton omission class `|Y_i|>=2`, at least one of the following holds:

> **(ROOT)** `N_B(s)={o_i}`;
>
> **(OUT)** there is `z in U_o` with `s z` a nonedge, `o_i z` an edge, `d_X(z)=0`, and `N(s) intersect N(z)={o_i}`;
>
> **(MATCHED)** there is a matched B-vertex z with `o_i z` an edge, `s z` a nonedge, `d_X(z)=0`, and `N(s) intersect N(z)={o_i}`.

The witnesses need not be distinct for different sources, so no per-source additive count is claimed.

---

## 4. Equality-vector consequence

The exact two-omission score/triangle ledger shows that the cheapest full-support geometry drives toward

`nu=M=H_Y=Q_rest=0`.

Under the last two zero conditions, alternatives `(OUT)` and `(MATCHED)` above are impossible. Therefore:

### Corollary 4.1

If

`nu=H_Y=Q_rest=0`,

then every source in every non-singleton omission class satisfies

> `N_B(s)={o_i}`.                                         `(4.1)`

In particular, since `alpha+beta=y` and both classes are nonempty, if `y>=3` then at least one omission class has size at least two. Hence the exact equality vector forces at least one entire non-singleton omission class to consist of B-degree-one sources.

This is the correct next bottleneck. A verified structural lower bound excluding B-degree one for a tight-code source in this rigid branch would immediately show that the strict zero-correction equality vector is impossible for `y>=3`. **No such lower bound is assumed here until its definition-level proof has been reread or independently reconstructed.**

---

## 5. Interaction with the exact correction ledger

The trichotomy is useful even before the root alternative is excluded.

- Every `(OUT)` witness makes `H_Y>0`, and therefore raises both the exact Y-slack

  `L_Y=y(p-g)+nu+H_Y`

  and the full residual demand

  `2q+E_U=Dbase+nu+H_X+H_Y`.

- Every `(MATCHED)` witness makes `Q_rest>0`, and therefore raises the exact triangle/slack invariant

  `Q+E_-=B-y+nu+(k+1)u_o+Q_rest`.

- The only way to avoid both correction channels for a source in a non-singleton omission class is the very sparse root certificate `(ROOT)`, namely `d_B(s)=1` with unique B-neighbour `o_i`.

Thus raw edge-criticality has converted the cheapest algebraic equality vector into a concrete local source-degree question. This is a materially smaller and more externally reviewable target than the previous undifferentiated residual inequality.

---

## 6. Audit cautions

1. This note does **not** count one correction per source. Witness sharing is allowed.
2. It does **not** assert that `(ROOT)` is impossible. That is the next definition-level lemma to verify.
3. The ordinary triangle `s-x_*-o_i` is used only to ensure that deletion of `s o_i` does not separate the endpoints themselves. It is not counted in rooted `Q=e(G[N(v)])`.
4. `X_3` remains untouched: on its canonical root `u=0`, this unmatched-U full-support branch is inactive.
5. The source-tuple capacity theorem remains conditional on the two upstream premises named in the daily audit; this local critical-edge lemma does not alter that trust boundary.

---

## 7. Next move

Before claiming strict equality closure, recover from the foundational rooted/A-code definitions (or independently rederive from raw criticality) the exact lower bound on `d_B(s)` for a tight-code source `s in Y` in this branch. If `d_B(s)>=2` is genuinely theorem-level here, then `(ROOT)` disappears and the zero-correction equality vector is impossible for every `y>=3`. If B-degree one is allowed, classify that sparse source directly rather than hiding it behind a scalar inequality.
