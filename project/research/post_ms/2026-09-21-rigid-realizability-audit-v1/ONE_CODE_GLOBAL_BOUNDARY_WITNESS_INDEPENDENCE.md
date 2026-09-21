# Global independence of used U-forward boundary witnesses

Date: 2026-09-21

Status: raw graph-theoretic theorem inside the repeated rigid one-code interface. This removes the exact-population hypothesis from the earlier boundary-W independence argument. Conditional only on reaching the rigid complete one-code cut with `y>=2,m>=2`.

## 1. Setup

Let `Y=A_d`, `y>=2`, and let the selected matched-head count satisfy `m>=2`. Full exposure gives `I(d,X)=[p]`. Repeated-code reverse exclusion says every exposed coordinate is U-forward or matched-forward.

Let `L=L(d,X)` be the matched-forward head set and write `ell=|L|`. For each coordinate `i notin L`, choose one actual U-forward witness for every boundary edge

`y q_i^{d_i}`, `y in Y`.

Let `W_i` be the set of unmatched vertices used by these chosen certificates and put

`W = union_{i notin L} W_i`, `W=|W|`.

Every `W_i` is nonempty, every vertex in `W_i` has code `bar d xor e_i`, and the raw boundary theorem gives

> **`N_X(w)=empty` for every `w in W`.**                 `(1.1)`

Because the one-match code classes are distinct,

> **`W>=p-ell`.**                                       `(1.2)`

For `w in W`, let `t_w` be the number of chosen boundary edges for which w is the U-forward witness. Since every pair `(y,i)` with `y in Y`, `i notin L`, contributes exactly one chosen witness,

> **`sum_{w in W} t_w = y(p-ell)`.**                    `(1.3)`

## 2. The used boundary-witness set W is independent

Take distinct `w in W_i` and `w' in W_j` and suppose `ww'` is an edge.

Both vertices lie in `B=N(v)`, so the edge is triangular through the root. Triangle-edge criticality must give one of the two orientations. Consider the orientation with source w and head w'. Any B-witness is impossible because it would share the root with the B-source. Thus the witness must lie in A.

It cannot lie in X, because the head w' is X-anticomplete by `(1.1)`. Hence it would have to be a vertex `y in Y`, of code d.

But w has code `bar d xor e_i`. Therefore y and w agree at tight coordinate i and share the matched endpoint `q_i^{d_i}`. Consequently their common-neighbour set already contains that matched endpoint, in addition to the required head w'. It cannot equal the singleton `{w'}`.

The reverse orientation is identical, using coordinate j for w'. Hence neither orientation is possible.

Therefore

> **`G[W]` is independent.**                             `(2.1)`

This holds even if i=j.

## 3. Service-counted U-slack floor

For any `w in W`:

- w misses every X-vertex by `(1.1)`;
- w is nonadjacent to every outside source for which it is the chosen U-forward witness, so it misses at least `t_w` Y-vertices;
- w misses the other `W-1` vertices of W by `(2.1)`.

For an unmatched rooted neighbour z, the exact degree-deficit identity is

`epsilon_z = z_A + m_U(z) - (a-p)`,

where `z_A` and `m_U(z)` count its missing A- and U-neighbours. Applying this to w gives

`epsilon_w >= x+t_w+(W-1)-(a-p)`.

Since `a=x+y` and `g0=p-y`,

> **`epsilon_w >= g0+t_w+W-1`.**                        `(3.1)`

Summing and using `(1.3)`,

`E_W >= W(g0+W-1)+y(p-ell)`.

The first term is increasing in W for `g0>=1`, and `W>=p-ell`. Therefore

`E_W >= (p-ell)(g0+p-ell-1)+y(p-ell)`.

Because `g0+y=p`, this collapses exactly to

> **`E_U >= E_W >= (p-ell)(2p-ell-1)`.**                `(3.2)`

This is independent of y, g0, e, u and the multiplicities inside the one-match code classes.

The facewise forms are

- `C=empty` or `|C|>=3`: `ell=0`, so **`E_U>=p(2p-1)`**;
- `|C|=1`: `ell<=1`, so **`E_U>=2(p-1)^2`**;
- `|C|=2`: use the exact ell, with the universal coarse floor **`E_U>=(p-2)(2p-3)`**.

## 4. Complementary selected U-witnesses add a disjoint bill

Let k be the minimum number of selected complementary U-witnesses used by an outside source. Across all outside sources, let K be the union of actual selected complementary-code witnesses. Every vertex of K has code `bar d`, so `K cap W=empty`.

If `z in K` is used by `t_z` outside sources, singleton-head criticality forces it to have exactly one X-neighbour and to miss all `t_z` source vertices. Hence

`epsilon_z >= g0+t_z-1`.

The total selected source-witness incidence is at least `yk`, and `|K|>=k`. Since `g0>=1`, summing gives

> **`E_K>=k(p-1)`.**                                    `(4.1)`

Combining the physically disjoint W and K layers gives the general repeated-code boundary bill

> **`E_U >= (p-ell)(2p-ell-1)+k(p-1)`.**               `(4.2)`

This extends the earlier exact `e=p` repair-reservoir formula to arbitrary boundary-forward multiplicity.

## 5. Strategic consequence

The old scalar rooted-Q hostile family was only the sharp equality example. The entire repeated-code `m>=2` branch now pays roughly `2p^2` U-slack before any H--U carrier analysis or source-tuple capacity is invoked, plus a further `k(p-1)` bill for complementary selected witnesses.

The next step is to combine `(4.2)` with the exact score ceiling, the occupancy identity `e=c-r`, the relation `u=e+k`, the full-boundary requirement `p<=e+ell`, and the independent U-bound. This converts the physical boundary witness set into a macroscopic parameter wedge for the whole repeated-code branch rather than merely the `e=p` face.

## 6. Scope

No source-tuple capacity theorem, global selected `(source,coordinate)` uniqueness, rooted-Q inequality, or superseded H--U private-foot argument is used. The independence proof is direct raw D2C criticality plus tight-code transversality; the service-counted slack uses only the rooted degree identity and one selected witness per physical boundary edge.
