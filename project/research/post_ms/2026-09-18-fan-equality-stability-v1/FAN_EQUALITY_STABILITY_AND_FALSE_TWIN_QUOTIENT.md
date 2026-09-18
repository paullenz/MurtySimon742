# Fan equality stability and false-twin quotient

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large second-extremal diameter-2-critical programme around

`M(n)=floor((n-1)^2/4)+1`.

The published 2024 order-12, size-32 D2C graph `X_3` remains a mandatory negative control. No all-order or eventual second-extremal theorem is claimed here.

## 1. Why this is the next move

The preceding checkpoint reduced any large rooted-transfer A-edge demand to two explicit fan geometries:

1. a direct A-edge fan whose leaves are near false twins;
2. an A/U unique-common-neighbour fan with an induced matching cut between heads and same-code witnesses.

The right next question is not another global traffic bound. It is what the equality and near-equality cases of those two fan geometries actually look like.

This note obtains three new pieces of structure.

- A/U fan holes admit an exact normal form. Zero hole forces every witness into `U`, makes the witness side a clique, and makes all but at most one matching head-witness edge direct.
- With total hole mass `G`, all but an explicit exceptional set of heads are simultaneously near-direct to their matched witness and Hamming-close to the source code.
- An exact false-twin class in any D2C graph forces a private-certifier / sparse-common-side dichotomy. Applied to a zero-hole direct fan, this gives a quadratic missing-edge floor inside the common neighbourhood and therefore a local triangle suppression theorem.

These are structural statements. The finite scans below are audit support only.

## 2. Setup for one A/U fan

Work in the live near-full partial-Boolean branch around the fixed maximum-degree root `v`.

Let `x in A` be an A-source with chosen A/U certificates

`N(x) intersect N(w_i) = {h_i}`

for `i=1,...,d`, where the heads `h_i in A` are distinct and the witnesses `w_i in A union U` are distinct. The preceding induced-matching theorem gives

`G[H_x,W_x]` equal to the matching `h_i w_i`,

and all witnesses have one common Boolean code

`c(w_i)=bar(c(x))`.

Put

`Y_x = V(G) \ ({x} union N(x))`.

Thus every witness `w_i` lies in `Y_x`.

For each certificate define the external-hole set

`Z_i = V(G) \ ({x,w_i} union N(x) union N(w_i))`.

Equivalently, `Z_i` is the set of vertices adjacent to neither `x` nor `w_i`. Put

`g_i = |Z_i| = epsilon_x + epsilon_{w_i} - (lambda+1)`

and

`G_x = sum_i g_i`.

The nonnegativity of every `g_i` is the preserved unique-common-neighbour slack inequality.

## 3. Exact fan-hole normal form

### Lemma 3.1 — exact witness neighbourhood

For every `i`,

`N(w_i) = {h_i} union (Y_x \ ({w_i} union Z_i)).`         `(EFN)`

Proof. Inside `N(x)`, the unique-common-neighbour condition says that `w_i` is adjacent only to `h_i`. Outside `N(x)`, every vertex other than `x,w_i` that is not adjacent to `w_i` is, by definition, in `Z_i`. This partitions the vertex set. square

### Corollary 3.2 — witness-side missing edges

For the witness set `W_x={w_1,...,w_d}`,

`d_{overline{G[W_x]}}(w_i) <= g_i`,

and therefore

`2 e(overline{G[W_x]}) <= G_x`.                          `(EWM)`

This recovers the earlier missing-edge estimate but now as part of a complete local normal form.

### Lemma 3.3 — A-witnesses consume a root hole

If `w_i in A`, then `v in Z_i`. Hence

`w_i in A  =>  g_i>=1`.

Consequently

`|W_x intersect A| <= G_x`,

and

`|W_x intersect U| >= (d-G_x)_+`.                        `(AWU)`

Proof. Both `x` and an A-witness are nonadjacent to the maximum-degree root `v`, so `v` is adjacent to neither member of the unique-common-neighbour pair. square

### Corollary 3.4 — low-hole fans force U-edges

Let

`r_x=(d-G_x)_+`.

Then

`q=e(G[U])`

satisfies

`q >= max{0, binom(r_x,2)-floor(G_x/2)}.`                 `(FQLB)`

Proof. At least `r_x` witnesses lie in `U`. Among all witnesses there are at most `floor(G_x/2)` missing pairs by `(EWM)`, hence the same is true on any U-subset of the witnesses. square

Thus a low-hole linear A/U fan cannot have an innocuous witness side: unless hole mass is large enough to move witnesses into `A` or delete many witness-witness edges, it creates a large clique-like subgraph inside `U`. Since

`Q=p(p+u-1)+q`,

this also feeds directly back into the rooted-triangle transfer variable.

## 4. Zero-hole A/U fans have an exact dual form

Assume now

`G_x=0`.

Then every `g_i=0`.

### Theorem 4.1 — zero-hole fan classification

If `p>=1`, then:

1. every witness lies in `U`;
2. `W_x` is a clique, hence `q>=binom(d,2)`;
3. for all but at most one index `i`,

   `N(h_i) intersect Y_x = {w_i}`;                       `(CLEAN)`

4. for every index satisfying `(CLEAN)`,

   `N(h_i) intersect N(w_i)=empty`;                       `(MDIR)`

   in particular the matching edge `h_i w_i` is direct;
5. for every such index,

   `c(h_i)=c(x)`.

Hence a zero-hole fan consists of a U-clique of complementary-code witnesses and, with at most one exception, a parallel family of source-code A-heads joined to those witnesses by direct matching edges.

Proof.

By Lemma 3.3, an A-witness would give `g_i>=1`, so every witness lies in `U`.

By `(EFN)`, when `g_i=0`,

`N(w_i) = {h_i} union (Y_x\{w_i}).`

Therefore every two distinct witnesses are adjacent and `W_x` is a clique.

Fix `i!=j`. Since `c(w_i)=c(w_j)`, the two witnesses share all `p` selected tight-core endpoints, so the edge `w_iw_j` is not direct. D2C criticality must therefore certify it in one of the two orientations.

Suppose it is certified from `w_i` through `w_j` by an external vertex `z`, so

`N(w_i) intersect N(z)={w_j}`.

The vertex `z` is adjacent to `w_j` and nonadjacent to `w_i`. If `z in N(x)`, then `(EFN)` for `w_j` forces `z=h_j`. If `z in Y_x`, then zero hole for `w_i` makes `z` adjacent to `w_i`, a contradiction. The vertex `x` is not adjacent to `w_j`. Hence `z=h_j`.

Now `(EFN)` for `w_i` shows that every vertex of `Y_x\{w_i}` is adjacent to `w_i`. Thus

`N(w_i) intersect N(h_j)={w_j}`

forces

`N(h_j) intersect Y_x={w_j}`.

So every pair `{i,j}` has at least one endpoint whose head satisfies `(CLEAN)`. The indices failing `(CLEAN)` therefore form an independent set in the complete graph on `[d]`, and there can be at most one of them.

For a clean index `i`, the witness `w_i` has no neighbour in `N(x)` other than `h_i`, while the head `h_i` has no neighbour in `Y_x` other than `w_i`. These two neighbourhoods therefore have empty intersection, proving `(MDIR)`.

Finally, `w_i` has code `bar(c(x))`. If `h_i` agreed with `w_i` in any tight coordinate, their common selected endpoint in `B` would be a common neighbour, contradicting `(MDIR)`. Hence `c(h_i)=bar(c(w_i))=c(x)`. square

### Corollary 4.2 — exact equality model is incompatible with sparse U

Any zero-hole A/U fan of order `d` satisfies

`binom(d,2) <= q`.                                       `(ZHQ)`

Thus any independent argument giving `q=o(p^2)` rules out a zero-hole A/U fan of linear order `d=Theta(p)`.

This applies in particular in every previously established slice where the beta-sensitive q-cap is subquadratic.

## 5. Quantitative stability of the A/U equality model

For each head put

`t_i = |N(h_i) intersect (Y_x\{w_i})|`.

Thus `t_i=0` is exactly the clean condition from the zero-hole theorem.

### Lemma 5.1 — head-or-hole certification of witness edges

Let `w_iw_j` be an edge of `G[W_x]`. Since the witnesses have one Boolean code and `p>=1`, this edge is not direct.

If a criticality certificate is oriented from `w_i` through `w_j`, then exactly one of the following occurs.

1. **matching-head certificate:** the external certifier is `h_j`, and then

   `t_j <= g_i`;                                         `(HHC)`

2. **hole certificate:** the external certifier lies in `Z_i`.

Moreover, for fixed `i`, distinct hole-certified target edges use distinct vertices of `Z_i`. Hence the total number of hole-certified witness edges, after choosing one orientation/certificate for each such edge, is at most

`G_x`.                                                    `(HCC)`

Proof. Let `z` certify the orientation, so `z` is adjacent to `w_j`, nonadjacent to `w_i`, and

`N(w_i) intersect N(z)={w_j}`.

If `z in N(x)`, `(EFN)` for `w_j` gives `z=h_j`. Every neighbour of `h_j` in `Y_x\{w_j}` must then be nonadjacent to `w_i`, hence belongs to `Z_i`; this proves `t_j<=g_i`.

If `z` is outside `N(x)` and is not `x`, then nonadjacency to `w_i` puts it in `Z_i`. A fixed ordered pair `(w_i,z)` has at most one singleton common neighbour, so it can certify at most one target edge. square

### Theorem 5.2 — threshold stability

Fix an integer `tau>=0` and define

`B_tau={i: g_i<=tau < t_i}`.

Then

`|B_tau|(|B_tau|-1) <= 3G_x`.                            `(BST)`

Consequently, if

`R(G)=floor((1+sqrt(1+12G))/2)`,

then all but at most

`floor(G_x/(tau+1)) + R(G_x)`                            `(EXC)`

indices satisfy simultaneously

`g_i<=tau`

and

`t_i<=tau`.                                               `(GOOD)`

Proof. Consider a pair `i,j in B_tau`.

If `w_iw_j` is absent, charge the pair to a missing witness edge. By `(EWM)` there are at most `G_x/2` such pairs in total.

If `w_iw_j` is present, a matching-head certificate is impossible in either orientation: `t_j>tau>=g_i` and `t_i>tau>=g_j`, contradicting `(HHC)`. Hence the edge must be hole-certified. By `(HCC)` there are at most `G_x` such edges in total.

Therefore

`binom(|B_tau|,2) <= 3G_x/2`,

which is `(BST)`. The number of indices with `g_i>tau` is at most `floor(G_x/(tau+1))`; adding the bound for `B_tau` gives `(EXC)`. square

### Corollary 5.3 — near-direct matching edges and Hamming localization

For every good index in `(GOOD)`,

`|N(h_i) intersect N(w_i)| <= t_i <= tau`.               `(NMD)`

Moreover

`dist_H(c(h_i),c(x)) <= tau`.                            `(HLOC)`

Proof. By `(EFN)`, the only possible common neighbours of `h_i` and `w_i` lie among the `t_i` vertices of `N(h_i) intersect (Y_x\{w_i})`; this gives `(NMD)`.

A tight-core endpoint is a common neighbour of `h_i` and `w_i` exactly on a coordinate where the two codes agree. Since `c(w_i)=bar(c(x))`, such an agreement is exactly a coordinate where `c(h_i)` differs from `c(x)`. Hence the Hamming distance is bounded by the total common-neighbour count. square

### Corollary 5.4 — asymptotic two-cluster normal form

Suppose `d=Theta(p)` and `G_x=o(p^2)`. Taking, for example, `tau=floor(sqrt(G_x))` when `G_x>0`, all but `o(p)` heads lie within Hamming distance `o(p)` of `c(x)`, while every witness has the exact antipodal code `bar(c(x))`.

Thus a low-hole linear A/U fan is not merely an induced matching with a near-clique witness side. It is asymptotically a two-cluster antipodal Hamming configuration joined by the induced matching.

When `G_x=0`, Theorem 4.1 recovers the exact version.

## 6. A generic false-twin theorem for D2C graphs

The direct-fan equality model can be treated without any Boolean machinery.

Let `D` be a false-twin class in an arbitrary diameter-2-critical graph `G`: every `y in D` has exactly the same open neighbourhood

`N(y)=W`.

Put

`d=|D|`, `w=|W|`,

and assume `d>=2`, `w>=2`.

The class `D` is independent and disjoint from `W`.

Call `z in W` **privately certified** if there exists a vertex `q notin W` with

`N(q) intersect W={z}`.

### Lemma 6.1 — private-certifier / sparse-side dichotomy

For every `z in W`, at least one of the following holds.

1. `d_{G[W]}(z)=0`;
2. `z` is privately certified;
3. `z` has at least `d` nonneighbours inside `W`.

Proof. Suppose `z` has a neighbour in `W`, so for every `y in D` the edge `yz` is not direct because

`N(y) intersect N(z)=W intersect N(z)`

is nonempty.

If `z` is not privately certified, a criticality certificate for `yz` cannot be oriented from `y` through `z`: such a certificate would be a vertex `q` with

`N(y) intersect N(q)=N(q) intersect W={z}`, 

which is precisely a private certificate.

Therefore every edge `yz`, `y in D`, must be certified in the opposite orientation. There is a vertex `q_y` such that

`N(z) intersect N(q_y)={y}`.

Because `q_y` is adjacent to `y` and `N(y)=W`, we have `q_y in W`; because the common neighbourhood is the singleton `{y}`, `q_y` is nonadjacent to `z`. Distinct leaves give distinct `q_y`, since a fixed pair `(z,q)` has only one singleton common neighbour. Thus `z` has at least `d` nonneighbours in `W`. square

### Theorem 6.2 — false-twin common-side missing-edge floor

Let `e_bar(W)=e(overline{G[W]})`. Then

`2 e_bar(W) >= min(d,w-1) (2w+d-n)_+`.                  `(FTF)`

Proof. A private-certifying vertex `q` determines at most one vertex of `W`. Since a false twin `y in D` has `N(y) intersect W=W` and `w>=2`, no member of `D` is such a private certifier. Hence the number of privately certified vertices of `W` is at most

`n-w-d`.

Every remaining vertex of `W` has at least `min(d,w-1)` nonneighbours in `W` by Lemma 6.1. Summing complement-degrees over `W` gives

`2e_bar(W)`
` >= [w-(n-w-d)]_+ min(d,w-1)`,

which is `(FTF)`. square

This is a useful equality-classification theorem in its own right: a large false-twin class can only coexist with a dense common side if the graph has enough outside vertices to provide distinct private certificates.

## 7. Consequence for a zero-hole direct fan

Return to the live rooted setup. Let `x in A` have a direct fan `D_x` of order `d`, and suppose every leaf has zero direct-hole surplus:

`epsilon_x+epsilon_y=lambda+1`

for every `y in D_x`.

The preceding direct-fan theorem gives the exact false-twin relation

`N(y)=W_x=(V(G)\{v})\N(x)`

for every leaf.

Put `w=|W_x|`. Since `d(x)=b-epsilon_x` and `n=2b-lambda`,

`w=n-1-d(x)=b-lambda-1+epsilon_x`.

Applying `(FTF)` gives the finite project-specific inequality

`e(overline{G[W_x]})`
` >= (1/2) min(d,w-1)`
`      (d+2epsilon_x-lambda-2)_+.`                       `(DFQ)`

### Corollary 7.1 — local triangle suppression

For every leaf `y in D_x`,

`N(y)=W_x`,

so the number of triangles containing `y` is exactly `e(G[W_x])`. Hence

`e(G[N(y)])`
` <= binom(w,2)`
`    -(1/2) min(d,w-1)`
`      (d+2epsilon_x-lambda-2)_+.`                       `(DTS)`

Thus a large exact false-twin fan forces a quadratic loss of triangles on its common side unless the fan size is absorbed by the root-imbalance/slack term `lambda+2-2epsilon_x`.

In particular, along a sequence with `d=Theta(p)`, if

`d+2epsilon_x-lambda = Omega(p)`,

then

`e(overline{G[W_x]})=Omega(p^2)`.

So the exact direct-fan equality model really does collapse toward a bipartite/sparse-common-side geometry unless the root imbalance is itself large enough to absorb the fan.

## 8. Interaction with rooted transfer

The new A/U inequality `(FQLB)` feeds directly into

`F_min=(p-lambda)(p+u)+q-D_M+1`.

Therefore a low-hole A/U fan raises the rooted-transfer A-edge demand by at least

`max{0, binom((d-G_x)_+,2)-floor(G_x/2)}`.

This is a feedback mechanism absent from the preceding fan-feasibility theorem: the equality geometry that tries to carry many A-edge certificates also creates internal `U` edges, and those same edges increase `Q` and therefore increase the A-edge mass required by rooted transfer.

On the direct side, `(DFQ)/(DTS)` replaces the vague phrase “false-twin/bipartite-like” by a finite theorem: a large exact false-twin block either has a quadratically sparse common side or is paid for by large `lambda` relative to its centre slack.

These two statements are the appropriate equality-model inputs for the next residual-defect step.

## 9. Scope and mandatory negative control

Nothing here proves the global eventual second-extremal theorem.

The 12-vertex, 32-edge graph `X_3` remains untouched. At the canonical root it has `u=0` and `F_min=0`, so the rooted-transfer argument does not force a positive A/U fan or direct-fan demand. The new fan theorems are universal conditional statements and do not suppress that graph.

The triangle-free second-extremal branch remains separately known; the live purpose of these lemmas is the triangle-containing near-full branch.

## 10. Next structural target

The next move should use the two new equality penalties rather than optimize another global constant.

1. Insert `(FQLB)` into the rooted-transfer fan branch and ask whether the resulting `q -> F_min -> fan size -> q` feedback closes a parameter region.
2. In the direct branch, combine `(DFQ)` with the location of `W_x intersect B` and the rooted triangle count `Q=e(G[B])` to convert common-side sparsity into residual defect.
3. In the A/U branch, combine `(HLOC)` with selected/Hall machinery: a linear fan with subquadratic hole mass forces almost all heads into an `o(p)` Hamming ball around the source code while the witnesses occupy the exact antipodal code. This is far more rigid than a generic macroscopic code class and should be the next code-capacity object.
