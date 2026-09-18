# Unique-common-neighbour slack and beta-cylinder edge criticality

**Status:** internal structural lemmas / candidate research checkpoint, 18 September 2026. These statements belong to the near-full partial-Boolean branch. They do **not** assert an eventual second-extremal theorem. The published order-12, size-32 `X_3` graph has `u=0` and is untouched.

## 1. Setup

Use the current near-full notation. A maximum-degree root has neighbourhood size

`b=2p+u`,

and

`lambda=2b-n`,

so

`n=2b-lambda`.

For every `z in A union U`, put

`epsilon_z=b-d(z)`.

Every vertex of `A union U` chooses exactly one endpoint from each of the `p` tight antipode fibres and therefore has a Boolean code `c(z) in {0,1}^p`.

The beta-cylinder theorem already gives the following. If `x in A` has beta target set `I_x`, beta deficit `k_x=p-|I_x|`, and slack `epsilon_x`, then every A-neighbour of `x` lies in the central cylinder `C_x`, and

`d_A(x)>=(p-epsilon_x)_+`.

Since only `2^{k_x}` full Boolean codes extend the cylinder restriction, one of those code classes contributes at least

`ceil((p-epsilon_x)_+/2^{k_x})`

A-neighbours of `x`.

The point of this note is to price the edges from `x` into such a repeated code class by D2C edge criticality.

---

## 2. Exact unique-common-neighbour slack identity

### Lemma 2.1 (slack = baseline + holes)

Let `z,w in A union U` be nonadjacent and suppose

`N(z) cap N(w)={t}`.

Define the hole set

`H(z,w)=V(G) \ ({z,w} union N(z) union N(w))`.

Then

> `|H(z,w)|=epsilon_z+epsilon_w-(lambda+1)`.              `(UCH)`

In particular

> `epsilon_z+epsilon_w>=lambda+1`.                        `(UCS)`

Equality holds if and only if every vertex other than `z,w` is adjacent to at least one of them.

### Proof

Because `z,w` are nonadjacent and have exactly one common neighbour,

`|N(z) union N(w)|=d(z)+d(w)-1`.

There are `n-2` vertices different from `z,w`, hence

`|H(z,w)|`

`=n-2-[d(z)+d(w)-1]`

`=n-1-d(z)-d(w)`.

Now `n=2b-lambda` and `d(z)=b-epsilon_z`, `d(w)=b-epsilon_w`. Therefore

`|H(z,w)|`

`=2b-lambda-1-2b+epsilon_z+epsilon_w`

`=epsilon_z+epsilon_w-(lambda+1)`.

This proves `(UCH)` and `(UCS)`.

This identity is useful because every critical triangle-edge in a diameter-2-critical graph produces exactly such a unique-common-neighbour pair.

---

## 3. Same-code A-edges force complementary-code witnesses

### Lemma 3.1 (critical same-code edge localisation)

Assume `p>=2`. Let `x,z in A` satisfy

`c(x)=c(z)`

and

`xz in E(G)`.

Then there is a vertex `w in A union U` with

> `c(w)=bar c(x)=bar c(z)`

such that one of the following holds:

1. `xw` is a nonedge and `N(x) cap N(w)={z}`; or
2. `zw` is a nonedge and `N(z) cap N(w)={x}`.

Thus every same-code A-edge is certified across the complementary Boolean code class.

### Proof

The vertices `x,z` have the same matched-B neighbourhood, containing one endpoint from each tight fibre. Since `p>=2`, the edge `xz` lies in a triangle and deleting `xz` does not make `x,z` themselves distance greater than two.

Because the graph is diameter-2-critical, deletion of `xz` must destroy all length-at-most-two paths for some pair. Any such path in the original graph that uses the edge `xz` has length two, so one endpoint of the destroyed pair is `x` or `z`. Consequently there is a vertex `w` satisfying one of the two unique-common-neighbour alternatives above.

The witness `w` cannot be the root: `x` and `z` each have at least two matched-B neighbours of the root. It cannot be a matched-B endpoint either: if a matched endpoint is adjacent to one of `x,z`, it is adjacent to the other because their Boolean codes agree, contradicting the required nonedge in the unique-common-neighbour pair. Hence `w in A union U`.

Finally the unique-common-neighbour condition forbids `w` from sharing any matched-B neighbour with the source (`x` in case 1, `z` in case 2). Both vertices choose exactly one endpoint of each tight pair, so `w` must choose the opposite endpoint in every coordinate. Hence `c(w)=bar c(x)`.

---

## 4. Exact star decomposition inside a cylinder code class

Fix `x in A`, and let `R subseteq N_A(x)` be a set of A-neighbours with

`c(z)=c(x)` for every `z in R`.

Choose one critical witness for every edge `xz`, `z in R`, using Lemma 3.1.

Partition the edges into two types.

- **outgoing from `x`:** `N(x) cap N(w_z)={z}`;
- **incoming to `x`:** `N(z) cap N(w_z)={x}`.

Write `O subseteq R` for the outgoing heads. For incoming edges group their sources by common witness: for a complementary-code vertex `w`, let

`S_w={z in R : N(z) cap N(w)={x}}`.

### Lemma 4.1 (outgoing witnesses are injective)

The witnesses `{w_z:z in O}` are pairwise distinct. Moreover

> `sum_{z in O} epsilon_{w_z}`
> `>= |O|(lambda+1-epsilon_x)`.                           `(OUT)`

The right side may of course be replaced by its positive part.

### Proof

A single vertex cannot satisfy `N(x) cap N(w)={z}` for two different values of `z`. Thus the witnesses are distinct. Applying `(UCS)` to each pair `(x,w_z)` gives

`epsilon_{w_z}>=lambda+1-epsilon_x`,

and summing proves `(OUT)`.

Since all these witnesses lie in `A union U`, their slacks are charged directly to `L_A+E_U`.

### Lemma 4.2 (common-foot hole control)

Fix an incoming witness `w` and put `t=|S_w|`. For every `z in S_w`,

> `d_{overline{G[S_w]}}(z)`
> `<=epsilon_z+epsilon_w-(lambda+1)`.                     `(CFH)`

Consequently

> `2 e(overline{G[S_w]})`
> `<=sum_{z in S_w}epsilon_z+t(epsilon_w-lambda-1)`.      `(CFE)`

and the clique number satisfies

> `omega(G[S_w])`
> `>= ceil( t^2 / ( t + sum_{z in S_w}[epsilon_z+epsilon_w-(lambda+1)] ) )`. `(CFC)`

### Proof

For every `z in S_w`, the pair `z,w` is nonadjacent and has unique common neighbour `x`. Every other `z' in S_w` is also nonadjacent to `w`. If `zz'` is a nonedge, then `z'` is adjacent to neither member of the pair `(z,w)`, so it is a hole of that pair. Lemma 2.1 therefore bounds the number of such `z'` by the right side of `(CFH)`.

Summing degrees in the complement gives `(CFE)`. Applying the Caro--Wei bound to `overline{G[S_w]}` and then Cauchy/Jensen gives

`alpha(overline{G[S_w]}) >= t^2/(t+2e(overline{G[S_w]}))`,

which together with `(CFE)` proves `(CFC)`.

### Structural consequence

The beta-cylinder multiplicity from the previous checkpoint now has an exact D2C refinement. If

`t_x=ceil((p-epsilon_x)_+/2^{k_x})`,

then some repeated A-code neighbourhood of `x` of size at least `t_x` admits a decomposition

> `R=O dotcup (dotcup_w S_w)`

such that

- the outgoing part uses distinct complementary-code witnesses and pays `(OUT)` directly into `E_U+L_A`;
- every concentrated incoming part is forced to be dense by `(CFH)--(CFC)` unless its source/foot slacks already pay for the missing edges.

This is the first exact conversion of the beta-cylinder multiplicity statement into D2C edge-critical structure.

---

## 5. Zero-hole rigidity and the dual-clique normal form

The equality case of Lemma 2.1 is much more rigid than the inequality alone suggests.

### Lemma 5.1 (zero-hole dual clique)

Fix a vertex `x in A union U`. Suppose there are distinct vertices

`v_1,...,v_t`

and distinct vertices

`w_1,...,w_t`

such that for every `i`

`N(x) cap N(w_i)={v_i}`

and

`epsilon_x+epsilon_{w_i}=lambda+1`.

Then:

1. the vertices `w_1,...,w_t` form a clique;
2. `w_i v_i` is an edge;
3. `w_i v_j` is a nonedge whenever `i!=j`;
4. `x` is adjacent to every `v_i` and to no `w_i`.

Thus the bipartite graph between `{v_i}` and `{w_i}` is exactly a perfect matching, while the `w_i` form a clique.

If in addition the `v_i` form a clique, the induced structure is two cliques joined by a perfect matching, with `x` complete to the `v`-clique and anticomplete to the `w`-clique.

### Proof

Items 2 and 4 are contained in `N(x) cap N(w_i)={v_i}`. For `i!=j`, the vertex `v_j` is adjacent to `x`; if it were adjacent to `w_i`, it would be a second common neighbour of `x,w_i`, proving item 3.

By `(UCH)`, the slack equality says the pair `(x,w_i)` has no holes. The vertex `w_j` is not adjacent to `x`; therefore it must be adjacent to `w_i`. This proves item 1.

### Lemma 5.2 (approximate dual clique)

Under the same unique-common-neighbour hypotheses but without slack equality, put

`h_i=epsilon_x+epsilon_{w_i}-(lambda+1)`.

Then

> `2e(overline{G[W]}) <= sum_i h_i`,                      `(ADC)`

where `W={w_1,...,w_t}`.

The off-diagonal cross edges `w_i v_j` (`i!=j`) are still all absent.

### Proof

For fixed `i`, any `w_j` nonadjacent to `w_i` is also nonadjacent to `x`, hence is a hole of `(x,w_i)`. Thus the complement degree of `w_i` in `W` is at most `h_i`. Sum over `i`.

---

## 6. Same-code clique transfers to a complementary near-clique

### Theorem 6.1 (dual-clique transfer)

Let `K subseteq A` be a clique of size `r>=2` whose vertices all have one Boolean code `c`. Choose, for every edge of `G[K]`, one of the two critical orientations supplied by Lemma 3.1. This gives a tournament orientation of the complete graph on `K`.

There is a vertex `x in K` with at least

`t>=floor(r/2)`

out-neighbours. For those `t` heads choose their witnesses `w_1,...,w_t`. Then:

- the witnesses are distinct and all have code `bar c`;
- the cross graph from the `t` heads to the witnesses is exactly the matching `v_i w_i`;
- the complementary-code witness set `W` obeys

> `2e(overline{G[W]})`
> `<= t epsilon_x + sum_{w in W}epsilon_w-t(lambda+1)`.  `(DCT)`

Hence a large same-code A-clique cannot simply disappear under criticality: it transfers at least half its order into a complementary-code set which is itself a near-clique unless the source and witness slacks pay for the missing edges.

### Proof

A tournament has a vertex of outdegree at least `floor(r/2)`. Apply Lemma 4.1 to its outgoing edges and Lemma 5.2 to their distinct witnesses. The exact matching statement follows from the unique-common-neighbour condition, as in Lemma 5.1.

---

## 7. Strategic consequence

The previous beta-cylinder theorem said that bounded beta deficit and low A-slack force a large repeated A-code class among the neighbours of a witness. The new lemmas show that this repeated class is not a passive multiplicity:

1. every edge from the cylinder centre to that class is certified by a complementary-code unique-common-neighbour pair;
2. dispersed certification uses distinct complementary witnesses and pays slack directly;
3. concentrated certification forces a dense same-code block;
4. dense same-code cliques transfer to complementary near-cliques with exact matching geometry;
5. the zero-hole equality case is a rigid dual-clique/matching normal form.

The next useful step is to combine this edge-critical decomposition with the integrated source-tuple profile. In particular, one should count how many low-deficit/low-slack cylinder centres can be supported by the same complementary near-clique before the private-foot / unique-common-neighbour geometry forces either additional `L_A+E_U` or an impossible overlap pattern.

No such aggregate closure is claimed here.

## 8. Trust boundary

- `(UCH)` is an exact degree-count identity.
- Lemma 3.1 is the standard edge-criticality witness argument plus the partial-Boolean transversal property.
- `(CFH)--(DCT)` are hand injections/counts from the unique-common-neighbour hole sets.
- The statements are local structural lemmas; they do not claim the near-full branch is closed.
- The `X_3` negative control has `u=0` and is unaffected.
