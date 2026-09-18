# Complete unmatched rows force A-side clique-private feet

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal hand theorem; not externally reviewed. This attacks one of the two one-code row normal forms from `UNMATCHED_ROW_SINGLETON_COVER.md` by using D2C criticality rather than support counting alone.

## 1. General clique private-foot lemma

Let `C` be a clique of size `s>=3` in a diameter-2-critical graph `G`.

Take an edge `xy` of `G[C]`. After deleting `xy`, the endpoints remain at distance two through any third vertex of `C`. Hence `(x,y)` itself cannot witness criticality of the deleted edge.

Therefore, after orienting `xy` if necessary, there is a vertex `h` adjacent to the source `x` such that

`h not~y`

and

`N(h) intersect N(y)={x}`.                                      (1.1)

Because `y` is adjacent to every vertex of `C\{y}`, equation (1.1) forces

> `N(h) intersect C={x}`.                                        (1.2)

Orient the clique edge as `x -> y`. Doing this for every edge gives a tournament orientation of `K_s`.

Any source vertex with positive outdegree has a private foot satisfying (1.2). One foot cannot serve two different sources, because its neighbourhood in `C` would then have to be two different singletons. A tournament has at most one sink, so at least `s-1` vertices have positive outdegree.

Hence:

> **CLIQUE PRIVATE-FOOT THEOREM.** Every clique `C` of order `s>=3` in a D2C graph has at least `s-1` distinct external vertices `h` with
>
> `|N(h) intersect C|=1`.
>
> More precisely, all but at most one vertex of `C` can be assigned a distinct private foot adjacent to it and to no other vertex of `C`.   `(CPF)`

This is a direct edge-criticality statement; no selected/Hall machinery is used.

## 2. Rooted B-cliques force the feet into A

Now let `v` be the maximum-degree root and suppose

`C subseteq B=N(v)`.

A private foot `h` for a source `x in C` cannot lie in `B`: every B-vertex is adjacent to `v`, and every target `y in C\{x}` is also adjacent to `v`, so `v` would be a second common neighbour of `h` and `y`, contradicting (1.1).

The foot is not the root itself either. Therefore every clique-private foot lies in

`A=V\N[v]`.

Thus:

> **ROOTED CLIQUE COROLLARY.** If `C subseteq B` is a clique of size `s>=3`, then at least `s-1` distinct vertices of A are private to distinct sources of C.   `(RCPF)`

This is an A-side payment for large cliques inside the root neighbourhood.

## 3. Apply to the cheap complete unmatched row

Return to the near-full tight-pair setup. Let `y in U` have the one-code complete row

`K_y=K_p`.

Let `q_i in P_i` be the endpoint selected by `y`. By definition of `K_y`, the selected endpoints `q_1,...,q_p` form a clique. Since `y` is adjacent to every `q_i`,

> `C_y={y,q_1,...,q_p}`

is a clique in `B` of size `p+1`.

For `p>=2`, (RCPF) forces at least `p` distinct A-vertices private to distinct sources of `C_y`. At most one source of `C_y` lacks such a foot.

The partial Boolean code of each possible foot is forced.

### Foot private to q_i

A foot `h_i` private to `q_i` is adjacent to `q_i` and to none of the other selected endpoints `q_j`; it is also nonadjacent to `y` because `y in C_y\{q_i}`. Since every A-vertex chooses one endpoint from every tight pair, its code is exactly

> `c(h_i)=beta_i(y)`.                                           (3.1)

### Foot private to y

A foot `h_y` private to `y` is nonadjacent to every selected endpoint `q_i`, so

> `c(h_y)=bar c(y)`.                                             (3.2)

It is adjacent to `y` by definition of a private foot.

Therefore:

> **COMPLETE-ROW PRIVATE-FOOT THEOREM.** If `K_y=K_p`, then A contains at least `p` distinct clique-private feet. Moreover A realises at least `p-1` of the `p` distinct beta codes
>
> `beta_i(y)=bar c(y) Delta {i}`,
>
> and if the omitted source is one of the matched `q_i`, A also contains a private foot of code `bar c(y)` adjacent only to `y` inside `C_y`.   `(CRPF)`

So the apparently cheapest row-cover case `tau(Psi(K_y))=1` is not cheap once criticality of the entire B-clique is priced: it creates an almost-complete radius-one beta sphere in A.

## 4. Private beta feet cannot serve as beta witnesses for the same row

For the physical P--U edge `yq_i`, a beta-oriented selected witness has code `beta_i(y)` **and is adjacent to y**; beta obligations inject into A--U edges.

By contrast, a clique-private foot for source `q_i` also has code `beta_i(y)` but is **nonadjacent to y** by (3.1).

Hence the private foot cannot itself discharge a beta-oriented obligation for `yq_i`.

Consequently, whenever coordinate `i` simultaneously

1. has a clique-private foot for `q_i`, and
2. is beta-oriented in the selected witness system for `yq_i`,

one needs at least two A-vertices of code `beta_i(y)`: one nonadjacent private foot and one adjacent beta witness. Thus

> `n_{beta_i(y)}>=2`                                             `(4.1)`

on every such coordinate.

Since at least `p-1` coordinates have clique-private feet, any beta spill from a complete row is multiplicity-expensive on all but at most one coordinate.

## 5. Several complete rows of the same code

If several unmatched vertices have the same partial code `c` and complete row `K_p`, they use the same B-clique of selected matched endpoints but different unmatched vertices. A single A-vertex of beta code `bar c Delta {i}` may be private to `q_i` for several such cliques only if it is nonadjacent to every corresponding unmatched row vertex.

Therefore the complete-row class has a clean dichotomy:

- beta-code vertices used as clique-private feet sit on the **nonadjacent** side of those row vertices;
- beta-code vertices used as selected beta witnesses sit on the **adjacent** side.

The two roles are disjoint at the vertex level. This gives a natural multiplicity refinement of the preserved per-source alpha-spill inequality for repeated complete rows.

No global numerical closure is claimed here; the next step is to combine this disjoint-role fact with A-code multiplicities and total A-side slack.

## 6. Strategic significance

The previous one-code row theorem left two cheap cases:

1. `K_y=K_p`;
2. `K_y=K_{p-1} dotcup K_1`.

The second already forces a complementary U--U antipode and therefore enters the strengthened Boolean fan/error machinery.

The first is now also structurally priced: it forces a B-clique of order `p+1`, at least `p` distinct A-side private feet, and at least `p-1` distinct beta-sphere codes in A. Any selected beta spill then requires additional multiplicity in those same codes.

Thus neither one-code row remains an unstructured escape. The remaining task is quantitative: convert the resulting A-code/private-foot populations into `L_A` or residual defect through maximum-degree slack and criticality of their A-side edges.

The published 12-vertex/32-edge control remains unaffected; this note concerns the unmatched `u>0` branch.