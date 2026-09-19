# Minimal anticomplete-buffer X-edge criticality

Date: 2026-09-19

Status: internal structural theorem for the unloaded common-buffer comparator in the rigid one-code `z=1` branch. This note continues `UNLOADED_COMMON_BUFFER_SOURCE_EDGE_DICHOTOMY.md` and treats the cheapest `r=0` buffer geometry. It does not use the finite source-tuple theorem and makes no eventual second-extremal claim.

## 1. Setup and scope

Retain the unloaded common-buffer notation:

- `X--Y` is a complete rigid A-cut, `x=|X|>=3`, `y=|Y|`;
- every source in Y has code d and `A_{bar d}=emptyset`;
- `g=g_P`, `k=x-g>0`;
- `U_-=W_0 disjoint_union {b}`, where `|W_0|=k`;
- every source uses all `k` members of `W_0` and all `g` gamma-d matched feet as crossing witnesses;
- the buffer b is unused by every crossing certificate;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`.

Now assume the anticomplete-buffer branch

> `d_Y(b)=0`.                                              `(1.1)`

The preceding score theorem gives

> `epsilon_b>=p-g`.                                        `(1.2)`

We specialize first to equality in this **buffer slack floor**:

> `epsilon_b=p-g`.                                         `(1.3)`

The degree proof of `(1.2)` shows that equality forces

> `b--X` complete,                                         `(1.4)`
>
> `b--U_o` complete,                                      `(1.5)`

where `U_o=U\U_-`.

If additionally `epsilon_b=0`, then `(1.2)` forces `g=p`; however the criticality classification below needs only `(1.3)--(1.5)`, not zero slack.

The objective is to understand the x critical edges `b x`, `x in X`, using raw D2C criticality before another scalar score collapse.

## 2. A generalized gamma localization lemma

The matched-foot localization argument does not require its source to lie in A.

### Lemma 2.1 — gamma localization for an A/U source

Let `s in A union U`, let `w` be a matched B endpoint, and suppose

- `s w` is a nonedge;
- `N(s) intersect N(w)={h}`;
- the singleton head h is not in the matched layer.

Then

> `c(s)=gamma(w)`.                                         `(2.1)`

### Proof

In the fibre containing w, the source s must choose the mate of w. In every other tight fibre, if s chose the matched endpoint adjacent to w, that endpoint would be a second common neighbour of s and w, distinct from the nonmatched singleton head h. Hence s chooses the opposite endpoint in every tight fibre, exactly the row-complement code `gamma(w)`. `square`

This is the same fibrewise proof used earlier for A-sources; the tight-code definition applies equally to unmatched U-vertices.

## 3. Structural unit I — every minimal buffer--X edge lies in a triangle

Fix `x0 in X`. By `(1.4)`, `b x0` is an edge.

The code of b is `bar d`. Since X is a union of whole complementary pairs and the outside pair `{d,bar d}` lies in Y/U rather than X, the code `c(x0)` is neither d nor `bar d`.

Therefore `c(x0)` is neither equal to nor complementary to `c(b)=bar d`. In particular the two codes agree in at least one tight coordinate. At that coordinate b and x0 choose the same matched endpoint, which is a common neighbour.

### Lemma 3.1

Every edge `b x0`, `x0 in X`, lies in at least one triangle.       `(3.1)`

Consequently deleting `b x0` does not separate b and x0 beyond distance two; D2C criticality must be witnessed by an external damaged vertex in one of the two singleton-common-neighbour orientations.

## 4. Orientation I: source x0, foot z, singleton head b

The first orientation has a vertex z satisfying

- `x0 z in E`,
- `b z notin E`,
- `N(x0) intersect N(z)={b}`.                              `(4.1)`

We classify every possible location of z.

### 4.1 The root is impossible

If `z=v`, then `b z` is an edge because b lies in B, contradicting `(4.1)`.

### 4.2 z cannot lie in X

If `z in X`, then every vertex of Y is adjacent to both x0 and z because the rigid cut is complete. Since `y>0`, the common neighbourhood cannot be the singleton `{b}`.

### 4.3 z cannot lie in Y or in U_-

If `z in Y`, then `b z` is a nonedge as required, but `x0 z` is an edge. However every core witness in `W_0` used by z has x0 as a possible common X head only when its fixed head is x0; more directly, all of X is not common to x0 and z because x0 is itself, so use the tight-code argument: `N(x0) cap N(z)={b}` contains no matched-B vertex, hence `c(z)=bar c(x0)`. Since z has code d, this would force `c(x0)=bar d`, impossible for X.

If `z in U_-`, then `(1.5)` is irrelevant but `b z` is a nonedge because `G[U_-]` is edgeless. Again the singleton head b is unmatched, so x0 and z have no common matched-B neighbour. Thus

`c(z)=bar c(x0)`.

But every z in U_- has code `bar d`, forcing `c(x0)=d`, again impossible for X.

### 4.4 z in U_o is exactly a complementary-code outside witness

If `z in U_o`, condition `(1.5)` would make `b z` an edge, contradicting `(4.1)`.

Thus **under exact buffer-slack equality `(1.3)` there is in fact no U_o Orientation-I witness.**

This is stronger than the looser pre-equality classification, where an outside witness would necessarily have code `bar c(x0)` and be anticomplete to Y. Equality removes that channel completely by making b complete to U_o.

### 4.5 The only surviving Orientation-I location is matched B

Let z be a matched endpoint. The singleton head b is unmatched, so Lemma 2.1 gives

> `gamma(z)=c(x0)`.                                        `(4.2)`

### Theorem 4.1 — Orientation-I localization at buffer-slack equality

Under `(1.3)`, every Orientation-I certificate for the edge `b x0` uses a matched endpoint z satisfying

> `gamma(z)=c(x0)`.                                        `(4.3)`

No root, A-vertex, or unmatched B-vertex can serve.

## 5. Orientation II: source b, matched foot z, singleton head x0

The reverse orientation has z satisfying

- `b z` is a nonedge,
- `x0 z` is an edge,
- `N(b) intersect N(z)={x0}`.                              `(5.1)`

Again classify all locations.

### 5.1 z cannot be the root, X or U_o

The root and every vertex of X and U_o are adjacent to b by definition or `(1.4)--(1.5)`, contradicting the required nonedge `b z`.

### 5.2 z cannot lie in Y

If `z in Y`, then z is adjacent to every X-vertex, while b is also adjacent to every X-vertex by `(1.4)`. Hence

`X subseteq N(b) intersect N(z)`,

and `x>=3`, contradicting singleton common neighbourhood.

### 5.3 z cannot lie in U_-

If `z in U_-`, then `b z` is indeed a nonedge, but b and z have the same tight code `bar d`. They therefore share the selected endpoint in every tight fibre, giving at least p common matched neighbours. Since the one-code tight branch has `p>=1`, `(5.1)` cannot hold.

### 5.4 matched endpoints have one gamma code

The only possible z is matched B. Applying Lemma 2.1 with source b gives

> `gamma(z)=c(b)=bar d`.                                   `(5.2)`

There are exactly g such matched endpoints: one in each tight fibre whose gamma complementary pair is `{d,bar d}`. Conversely any fibre with a gamma-`bar d` endpoint has gamma-d at its mate, so it is counted by `g=g_P`.

For a fixed matched endpoint z, the graph set `N(b) intersect N(z)` is fixed. If it is a singleton, it determines at most one head x0.

### Theorem 5.1 — reverse matched capacity

At most g vertices `x0 in X` can have their edge `b x0` certified in Orientation II.                                      `(5.3)`

This is an actual physical-foot capacity, not selected traffic bookkeeping.

## 6. Structural unit II — at least k buffer--X edges require code-aligned matched feet

There are x buffer--X edges and at most g can use Orientation II. Since `k=x-g`, at least k of them must use Orientation I.

By Theorem 4.1 each such edge `b x0` has a matched foot z with

> `gamma(z)=c(x0)`.                                        `(6.1)`

### Theorem 6.1 — minimal-buffer matched-foot demand

Under the unloaded anticomplete-buffer equality geometry `(1.3)`, at least

> `k=x-g`                                                  `(6.2)`

vertices of X require a matched criticality foot whose gamma code equals that vertex's own tight code.

No injectivity between Orientation-I feet for different X-vertices is asserted. A single matched endpoint has one fixed common-neighbour set with a given source, but different sources can in principle use the same foot. The theorem is therefore deliberately phrased as a **source/code demand**, not as k distinct matched endpoints.

## 7. Structural unit III — code support consequence

Let

> `X_match={x0 in X : the edge b x0 uses Orientation I}`.

Then `|X_match|>=k` and every code represented in `X_match` must occur among the p matched gamma endpoint codes.

Put

> `Gamma={gamma(w): w is a matched B endpoint}`.

Then

> `c(X_match) subseteq Gamma`,                             `(7.1)`

where the left side denotes the set of codes represented by X_match.

Since opposite matched endpoints have complementary gamma codes, Gamma is a union of at most p complementary code pairs. This is a genuine additional compatibility constraint between the rigid Hall family X and the signed tight-fibre core.

It does not yet yield a useful numerical lower bound without controlling multiplicities of X-code classes, so no such bound is promoted here.

## 8. Zero-buffer-slack specialization

If in addition

> `epsilon_b=0`,                                           `(8.1)`

then `(1.2)` and `(1.3)` imply

> `g=p`.                                                   `(8.2)`

The reverse Orientation-II capacity is then at most p, while

`k=x-p`.

Thus whenever `x>p`, at least `x-p` buffer--X edges still require Orientation-I gamma alignment.

At zero buffer slack, b is simultaneously:

- complete to X;
- complete to U_o;
- anticomplete to Y and `W_0`;
- incident to exactly one matched endpoint in every tight fibre.

This is a very rigid physical neighbourhood and is the next natural object to compare with the exact pair-local capacity and switching-sign structure.

## 9. What this adds to the common-buffer frontier

The previous score profile showed that the `r=0` branch is the cheapest common-buffer model in a large fraction of surviving abstract parameter states. The present theorem shows that attaining the minimum buffer slack there is not merely a scalar event: it forces the entire `b--X` complete layer to be certified through two matched-B channels only.

One channel, Orientation II, has total physical capacity at most g. Every remaining edge forces its X-source code to occur as a matched gamma code.

This is exactly the kind of local compatibility that was lost in earlier global score relaxations.

## 10. Trust boundary and next step

This note uses only:

- raw D2C edge criticality;
- rigid cut completeness;
- pair purity;
- tight-code complementarity;
- exact buffer-degree equality;
- generalized matched-foot gamma localization.

It does not use the finite source-tuple capacity theorem, the four-exception gate, or any graph count diagnostic. `X_3` remains untouched because `u=0` on its canonical root.

The next step should **not** assume the Orientation-I matched feet are distinct. Instead, group the forced `X_match` sources by tight code and combine their multiplicities with:

1. the existing gamma-collision / zero-signed-subcore penalty;
2. the exact pair-local `Ccap_P` and `(CROWD)` bills already active on the outside pair;
3. the fact that the buffer itself has code `bar d` and zero or minimal slack.

A useful target is a compact dichotomy: either many X-sources share a gamma-supported code and create quadratic A-slack, or many gamma code classes are needed and the signed tight-fibre core acquires a correspondingly constrained row structure. No multiplicity claim beyond `(6.2)` is currently promoted.
