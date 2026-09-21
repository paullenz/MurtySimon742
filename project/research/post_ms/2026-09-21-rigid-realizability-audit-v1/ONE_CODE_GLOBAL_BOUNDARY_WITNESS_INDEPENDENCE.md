# Global independence of used U-forward boundary witnesses

Date: 2026-09-21

Status: raw graph-theoretic theorem inside the repeated rigid one-code interface. This removes the exact-population hypothesis from the earlier boundary-W independence argument. Conditional only on reaching the rigid complete one-code cut with `y>=2,m>=2`.

## 1. Setup

Let `Y=A_d`, `y>=2`, and let the selected matched-head count satisfy `m>=2`. Full exposure gives `I(d,X)=[p]`. Repeated-code reverse exclusion says every exposed coordinate is U-forward or matched-forward.

Let `L=L(d,X)` be the matched-forward head set. For each coordinate `i notin L`, let `W_i` be the set of actual unmatched vertices that are used as U-forward witnesses for at least one boundary edge

`y q_i^{d_i}`, `y in Y`.

Put

`W = union_{i notin L} W_i`.

Every `W_i` is nonempty, every vertex in `W_i` has code `bar d xor e_i`, and the raw boundary theorem gives

> **`N_X(w)=empty` for every `w in W`.**                 `(1.1)`

Because the one-match code classes are distinct,

> **`|W|>=p-|L|`.**                                     `(1.2)`

## 2. The used boundary-witness set W is independent

Take distinct `w in W_i` and `w' in W_j` and suppose `ww'` is an edge.

Both vertices lie in `B=N(v)`, so the edge is triangular through the root. Triangle-edge criticality must give one of the two orientations. Consider the orientation with source w and head w'. Any B-witness is impossible because it would share the root with the B-source. Thus the witness must lie in A.

It cannot lie in X, because the head w' is X-anticomplete by `(1.1)`. Hence it would have to be a vertex `y in Y`, of code d.

But w has code `bar d xor e_i`. Therefore y and w agree at tight coordinate i and share the matched endpoint `q_i^{d_i}`. Consequently their common-neighbour set already contains that matched endpoint, in addition to the required head w'. It cannot equal the singleton `{w'}`.

The reverse orientation is identical, using coordinate j for w'. Hence neither orientation is possible.

Therefore

> **`G[W]` is independent.**                             `(2.1)`

This holds even if i=j: every used U-forward witness in the same one-match class still shares coordinate i with every Y-code-d candidate witness, so the same obstruction applies.

## 3. General quadratic U-slack floor

Write `W=|W|`. For any `w in W`:

- w sees the root;
- w sees exactly one endpoint of every tight pair, hence exactly p matched vertices;
- w sees no X-vertex;
- w sees no vertex of W by `(2.1)`;
- at most all y vertices of Y;
- at most the `u-W` unmatched vertices outside W.

Thus

`deg(w) <= 1+p+y+(u-W)`.

Since the root degree is `b=2p+u`,

> **`epsilon_w >= p+W-y-1 = g0+W-1`.**                 `(3.1)`

Summing over W gives

> **`E_U >= W(g0+W-1)`.**                               `(3.2)`

Using `(1.2)` and `g0>=1`, the right side is increasing in W, so

> **`E_U >= (p-|L|)(g0+p-|L|-1)`.**                    `(3.3)`

The global matched-leaf theorem has `|L|<=2`. Hence every repeated one-code rigid cut with `m>=2` carries a quadratic U-slack bill from the boundary witnesses alone:

> **`E_U >= (p-2)(g0+p-3)`**                            `(3.4)`

as a universal coarse form, with the stronger facewise bounds

- `C=empty` or `|C|>=3`: `L=empty`, so **`E_U>=p(g0+p-1)`**;
- `|C|=1`: **`E_U>=(p-1)(g0+p-2)`**;
- `|C|=2`: use the exact `|L|` in `(3.3)`.

## 4. Why this is stronger than the exact-equality argument

The earlier `e=p` theorem obtained A-anticompleteness of a unique witness in every coordinate class and then independence. The present argument needs neither uniqueness nor Y-anticompleteness. It uses only:

1. every *used* U-forward witness is X-anticomplete;
2. any rooted B-edge between two such witnesses would need an A-witness;
3. X cannot supply that witness;
4. every Y candidate shares a forced matched neighbour with the B-source.

Thus the quadratic boundary bill persists for arbitrary U-forward multiplicities and arbitrary `e>=p-|L|`.

## 5. Strategic consequence

The old scalar rooted-Q hostile family was only the sharp equality example. More generally, the entire repeated-code `m>=2` branch pays order `p^2` U-slack whenever p is large, before any H--U carrier analysis or source-tuple capacity is invoked.

The next step is to combine `(3.3)` with the exact score ceiling and the independent U-bound, while retaining the full-boundary gap `c>=p+r-|L|`. This should convert the physical boundary witness set into a macroscopic restriction on `g0,r,c` for the whole repeated-code branch rather than merely the `e=p` face.

## 6. Scope

No source-tuple capacity theorem, global selected `(source,coordinate)` uniqueness, rooted-Q inequality, or superseded H--U private-foot argument is used. The independence proof is direct raw D2C criticality plus tight-code transversality.
