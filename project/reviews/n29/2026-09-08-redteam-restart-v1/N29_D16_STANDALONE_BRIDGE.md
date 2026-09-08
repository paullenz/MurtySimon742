# n=29, Delta=16: standalone graph-to-model bridge

8 September 2026. Research direction: Paul Lenz. Mathematical development and internal audit: ChatGPT/Geeps.

**Status: candidate mathematics; same-assistant derivation, not independent peer review.** This note does not alter the frozen n=29 candidate proof. Its purpose is to isolate, in one place, the complete hand bridge from an actual 29-vertex diameter-two edge-critical graph with `Delta=16` to the reduced finite model used by the minimal trusted-kernel replay.

The intended review question is deliberately narrow:

> If such a graph existed at 210 or 211 edges, would it necessarily produce a state admitted by the minimal finite pipeline and a feasible point of the corrected v2 relaxation?

The answer proved below is **yes, conditional on the displayed graph lemmas**. The clean replay then supplies exact integer Farkas contradictions for every remaining finite state. External review of the graph lemmas remains open.

---

## 1. Scope and notation

Let `G` be a finite simple diameter-two edge-critical graph on

`n=29`

vertices. In this note assume

`Delta(G)=16`

and let

`m=e(G) in {210,211}`.

Put `H=\bar G`. Choose a vertex `v` of minimum degree in `H`. Since

`deg_H(v)=29-1-16=12`,

set

`A=N_H(v)`, `B=V(H)\N_H[v]`,

so

`a=|A|=12`, `b=|B|=16`.

Let

`C=H[A]`, `F=\bar C`

where the complement defining `F` is taken on `A` only. For `i in A` write

`d_i=deg_F(i)`.

Finally define the surplus parameter

`t=m-b(n-b)=m-16*13`,

so

`(m,t)=(211,3)` or `(210,2)`.

Throughout, all neighbourhoods in the bridge are open neighbourhoods in `H` unless explicitly stated otherwise.

---

## 2. Complement form of edge-criticality

### Lemma 2.1 — adjacent total-dominating pairs

For an edge `xy` of `H`, the pair `{x,y}` is an adjacent total-dominating pair in `H` if and only if `xy` is a nonedge of `G` whose endpoints have no common neighbour in `G`.

### Proof

Because `xy in E(H)`, each endpoint belongs to the other's open `H`-neighbourhood. A third vertex `z` fails to lie in `N_H(x) union N_H(y)` exactly when `z` is adjacent in `G` to both `x` and `y`. Thus

`N_H(x) union N_H(y)=V(H)`

is equivalent to saying that `x,y` have no common `G`-neighbour. Since they are nonadjacent in `G`, this is exactly the failure of a path of length at most two between them. QED.

Since `G` has diameter two, `H` has no adjacent total-dominating pair. Deleting a critical edge of `G` is the same as adding the corresponding missing edge to `H`; by edge-criticality, the enlarged complement contains a new adjacent total-dominating pair.

---

## 3. Missing B-pairs and selected cross-edges

Take a missing unordered pair `uw` of `H[B]`. Equivalently, `uw` is an edge of `G`.

### Lemma 3.1 — quasi-edge construction

After inserting `uw` into `H`, a new adjacent total-dominating pair has the form `{u,i}` or `{w,i}` for some `i in A`. If it is `{u,i}`, then the cross-edge `ui` already existed in `H` and, before insertion,

`N_H(u) union N_H(i)=V(H)\{w}`.

Write this as

`ui -> w`.

### Proof

Only the neighbourhoods of `u` and `w` change when `uw` is inserted, so a newly total-dominating old edge must use `u` or `w`, unless the new pair is `{u,w}` itself. The latter is impossible because both `u` and `w` miss `v`, so even after insertion their open neighbourhoods do not cover `v`.

Suppose the new pair is `{u,i}`. Its adjacency cannot be the newly inserted edge unless `i=w`, already excluded, so `ui` existed before insertion. To dominate `v`, since `u` misses `v`, the other endpoint must satisfy `iv in E(H)`, hence `i in A`.

Before insertion `{u,i}` was not total-dominating, and the only new neighbour acquired by either endpoint is `w` at `u`. Therefore the unique previously uncovered vertex is exactly `w`, proving the displayed identity. QED.

Choose **one** such cross-edge for every missing unordered pair of `H[B]`. Call the chosen cross-edges **selected**. Every other existing edge of `H[A,B]` is **residual**.

### Lemma 3.2 — injection and uniqueness

A selected cross-edge determines the missing unordered B-pair that selected it. Hence distinct missing B-pairs select distinct cross-edges. At a fixed B-source, selected labels are distinct and their supplements are distinct. Every unordered B-pair carries at most one chosen orientation.

### Proof

For a selected cross-edge `ui`, its B-endpoint `u` is the source and the identity

`N_H(u) union N_H(i)=V\{w}`

recovers the unique exception `w`. Thus the missing pair is `{u,w}`. A simple graph gives distinct labels for distinct incident cross-edges; distinct selected edges at source `u` cannot have the same supplement because that would recover the same missing pair. QED.

---

## 4. Residual/selected degrees and the exact ledger

For `u in B` let

- `rho_u` = residual degree from `u` into `A`;
- `q_u` = selected degree from `u` into `A`.

For `i in A` let

- `R_i` = residual degree from `i` into `B`;
- `x_i` = selected degree from `i` into `B`.

For `u in B` also let `p_u` be the number of missing B-pairs incident with `u` whose chosen orientation points **into** `u`; equivalently, `p_u` is supplement indegree.

Put

`r=sum_{u in B} rho_u = sum_{i in A} R_i`,

and define the label demand

`s_i=max(0,d_i-R_i)`, `S=sum_i s_i`.

### Lemma 4.1 — exact edge ledger

`e(F)=r+t`, and therefore

`sum_i d_i=2(r+t)`, `sum_i R_i=r`.

### Proof

Selected cross-edges are in bijection with missing unordered pairs of `H[B]`. Hence

`(# selected cross-edges)+e(H[B])=C(b,2)`.

Now count `E(H)` by the partition `{v},A,B`:

`e(H)=a+e(C)+r+C(b,2)`.

On the other hand `e(H)=C(n,2)-m` and `e(C)=C(a,2)-e(F)`. Using `n=a+b+1` and simplifying gives

`e(F)=r+m-b(a+1)=r+t`.

The remaining identities are degree sums. QED.

### Lemma 4.2 — label minimum-degree demand

For every `i in A`,

`x_i >= d_i-R_i`,

hence

`x_i>=s_i`, `0<=s_i<=a-1`, and

`S>=r+2t`.

### Proof

Because `v` has minimum `H`-degree `a`, every `i in A` has degree at least `a`. Its degree is

`1 + deg_C(i) + R_i+x_i`

`=1+(a-1-d_i)+R_i+x_i`

`=a-d_i+R_i+x_i`.

Thus `x_i>=d_i-R_i`, hence `x_i>=s_i`. Also

`S=sum max(0,d_i-R_i) >= sum(d_i-R_i)`

`=2(r+t)-r=r+2t`.

Since a selected source for a positive demand has residual degree at most `a-1` by Lemma 5.2 below, positive demands are at most `a-1`; the zero case is trivial. QED.

---

## 5. Pointwise source/supplement forcing

Fix a selected edge

`ui -> w`.

Thus `u,w in B`, `i in A`, `uw` is missing in `H`, `ui in E(H)`, and

`N_H(u) union N_H(i)=V\{w}`.

### Lemma 5.1 — F-neighbours force cross-neighbours

If `j` is an `F`-neighbour of `i`, then `uj in E(H)`.

### Proof

`ij in E(F)` means `ij notin E(H)`. Since `j != w` and `{u,i}` covers every vertex except `w`, `j` must be covered by `u`. QED.

### Lemma 5.2 — source-demand inequality

For every selected `ui->w`,

`d_i <= rho_u+R_i`.

Consequently, if `s_i>0`, then

`s_i<=rho_u`.

### Proof

Apply Lemma 5.1 to all `d_i` F-neighbours `j` of `i`. At most `rho_u` of the forced edges `uj` are residual.

If a remaining `uj` is selected, write `uj->w_j`. Its supplement `w_j` is distinct from `w` and from the supplements of the other selected edges at `u`. Because `ui->w` must dominate `w_j` and `u` misses `w_j`, the edge `iw_j` lies in `H`.

Moreover `iw_j` is residual. Indeed `ij` is missing in `H`, and because `w_j` is the unique exception of `uj->w_j`, `jw_j` is also missing. Thus the cross-edge `iw_j` has the A-vertex `j` missed by both endpoints. A selected cross-edge in our construction has its unique exception in `B`, so `iw_j` cannot be selected.

Distinct supplements give distinct residual edges at column `i`. Hence the nonresidual forced `uj` edges inject into the `R_i` residual edges at `i`, proving

`d_i<=rho_u+R_i`.

If `s_i>0`, then `s_i=d_i-R_i<=rho_u`. QED.

### Corollary 5.3 — source demand

A label of demand `s_i>0` has at least `s_i` distinct selected sources, and every one of those sources has residual degree at least `s_i`.

### Proof

By Lemma 4.2, `x_i>=s_i`; simple-graph incidence makes the selected sources distinct. Lemma 5.2 applies to every selected incidence at the label. QED.

### Lemma 5.4 — supplement residual-degree forcing

For every selected `ui->w`,

`d_i<=rho_u+rho_w`

and

`rho_w+q_w>=q_u-1`.

### Proof

Again inspect the F-neighbours `j` of `i`. Residual edges `uj` account for at most `rho_u` of them. If `uj` is selected with supplement `w_j`, then `w != w_j`; the quasi-edge `uj->w_j` must dominate `w`, and `u` misses `w`, so `wj in E(H)`.

This edge `wj` is residual: `wi` is missing because `w` is the exception of `ui->w`, and `ij` is missing because `ij in F`; hence the A-vertex `i` is missed by both endpoints of `wj`, impossible for a selected cross-edge whose unique exception is in `B`. Distinct labels `j` give distinct residual edges at `w`. Therefore `d_i<=rho_u+rho_w`.

For the second inequality, `w` is adjacent in `H` to every other selected label at `u`, by the same domination argument. These `q_u-1` cross-edges at `w` are distinct and are either residual or selected, giving `rho_w+q_w>=q_u-1`. QED.

### Lemma 5.5 — source-local selected-slot bounds

For every `u in B`,

`q_u+rho_u<=a`.

Also

`q_u+p_u`

is exactly the number of missing `H[B]` pairs incident with `u`. Hence

`q_u+p_u<=b-1`

and

`p_u<=rho_u+b-a-1`.

At `a=12,b=16`, this is

`p_u<=rho_u+3`.

### Proof

The first inequality is just the number `a` of possible cross-neighbours.

Every missing B-pair incident with `u` receives exactly one chosen orientation. It contributes once to `q_u` if oriented out of `u` and once to `p_u` if oriented into `u`. Thus `q_u+p_u` is the missing degree of `u` inside `H[B]`.

Therefore

`deg_H(u)=(q_u+rho_u)+[b-1-(q_u+p_u)]`

`=rho_u+b-1-p_u`.

Minimum degree gives `deg_H(u)>=a`, so `p_u<=rho_u+b-a-1`. QED.

### Lemma 5.6 — source-local degree bound

For selected `ui->w`,

`d_i<=rho_u+q_u-1`.

### Proof

Every F-neighbour of `i` is an H-neighbour of `u` by Lemma 5.1. Source `u` has `rho_u+q_u` cross-neighbours in total, but `i` itself is a selected cross-neighbour and is not an F-neighbour of itself. QED.

### Lemma 5.7 — endpoint load

For selected `ui->w`,

`R_i+x_i >= q_u+p_u`.

### Proof

The B-neighbours of `i` include the following distinct vertices:

1. source `u` itself;
2. the `q_u-1` supplements of the other selected labels at source `u`;
3. the `p_u` sources of selected missing B-pairs oriented into `u`.

The first two families are adjacent to `i` by the domination property of `ui->w`. For an incoming source `z`, the pair `zu` is missing in `H`. It cannot be the pair `{u,w}`, because that pair is already oriented out of `u`; hence `z!=w`. Since `ui->w` must dominate `z` and `u` misses `z`, we have `iz in E(H)`.

An incoming source cannot equal an outgoing supplement: that would orient the same missing unordered pair both ways, contradicting Lemma 3.2. Thus all `q_u+p_u` vertices are distinct B-neighbours of `i`, whose total cross-degree is `R_i+x_i`. QED.

---

## 6. Residual activity when t>0

Both n=29 dense scopes have `t>0`.

### Lemma 6.1 — every B-row is residual-active

For every `u in B`,

`rho_u>=1`.

### Proof

Assume `rho_u=0`. Let

`U=N_H(u) cap A`, `T=A\U`.

All cross-edges from `u` to `U` are selected.

There is no F-edge between `U` and `T`. Indeed, for `i in U` the selected edge `ui->w_i` must dominate every `j in T`; since `u` misses `j`, `ij in E(H)`.

Now count two disjoint families of residual cross-edges.

**F-edges inside U.** If `ij in E(F[U])`, write the selected edges at `u` as `ui->w_i` and `uj->w_j`. The two cross-edges `iw_j` and `jw_i` exist by the quasi-edge domination property and are residual by the same A-exception argument used in Lemma 5.2. They are distinct. Across different F-edges, the construction is injective because supplements at source `u` are distinct. Thus `F[U]` supplies `2e(F[U])` distinct residual edges, all with A-endpoint in `U`.

**F-edges inside T.** Let `ij in E(F[T])`. Insert the missing H-edge `ij`. A newly adjacent total-dominating pair cannot be `{i,j}`, because both `i` and `j` miss `u`. It must use `i` or `j`, say an old edge `iz` whose unique old exception is `j`. To dominate `u`, `z` must neighbour `u`. It cannot be `v`. It also cannot lie in `A`: then `z in U`, but there are no F-edges between `U` and `T`, so `zj in E(H)`, contradicting that `j` is the exception. Hence `z in B`.

The resulting cross-edge `iz` has unique exception `j in A`, so it is not one of our selected B-pair cross-edges and is residual. Different missing A-pairs give different such cross-edges because the old edge plus its unique exception recovers the pair. These residual edges have A-endpoint in `T`, so they are disjoint from the first family.

Therefore

`r >= 2e(F[U])+e(F[T])`.

Since there are no F-edges between `U` and `T`,

`e(F)=e(F[U])+e(F[T])`,

and hence

`r>=e(F)=r+t`,

contradicting `t>0`. QED.

Thus

`r>=b=16`.

---

## 7. Charging inequality

### Lemma 7.1 — exact charging bound

For every graph in scope,

`r-b >= sum_i s_i(s_i-1)/(a-s_i)`.

Consequently

`sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t`.        (7.1)

At `a=12,b=16`,

`sum_i s_i(13-2s_i)/(12-s_i) >= 16+2t`.       (7.2)

### Proof

For each label `i`, choose exactly `s_i` of its actual selected incidences; this is possible because `x_i>=s_i`. For a chosen incidence with source `u`, Corollary 5.3 gives `rho_u>=s_i`. Also the incidence is selected, so `q_u>=1`; with `q_u+rho_u<=a`, this implies `rho_u<=a-1`.

Charge the chosen incidence by

`(rho_u-1)/(a-rho_u)`.

At source `u`, there are at most `q_u<=a-rho_u` chosen incidences, so total charge at `u` is at most `rho_u-1`. Summing sources and using residual activity gives total charge at most

`sum_u(rho_u-1)=r-b`.

For fixed label `i`, the function `(x-1)/(a-x)` is increasing for integer `1<=x<=a-1`. Each of its `s_i` chosen sources has `rho_u>=s_i`, so the label receives at least

`s_i(s_i-1)/(a-s_i)`

charge. This proves the first inequality.

Since `S>=r+2t`, we have `r<=S-2t`. Therefore

`S-2t-b >= sum_i s_i(s_i-1)/(a-s_i)`.

Move the sum to the left and simplify each term to obtain (7.1). QED.

This is the complete charging-domain condition used by `minimal_prepare.py`.

---

## 8. Excluding an isolated vertex of C

The corrected v2 model uses the bound `d_i<=10`. Here is the complete bridge.

### Lemma 8.1 — delta(C)>=1

In either n=29 dense Delta=16 scope, `C=H[A]` has no isolated vertex. Therefore

`d_i<=a-2=10`

for every `i in A`.

### Proof

Suppose `x in A` is isolated in `C`, and put `X=A\{x}`.

For each missing H-pair `ij` inside `X` (equivalently each F-edge in `F[X]`), insert `ij`. The new total-dominating pair cannot be `{i,j}`, because both miss `x`. If it uses `i`, say as an old edge `iz` with exception `j`, then to dominate `x`, `z` must neighbour `x`. It cannot be `v`, because `v` is already adjacent to `j` and so cannot leave `j` as the exception. Since `x` has no C-neighbours, `z` cannot lie in `A`. Hence `z in B`.

Thus every F-edge in `F[X]` injects into a residual cross-edge with A-endpoint in `X`; it is residual because its unique exception is in `A`. The number of such edges is

`C(a-1,2)-e(C)`.

Now obtain one additional residual edge for every B-vertex `z`.

- If `z` is used as the B-endpoint of one of the preceding residual quasi-edges `iz` with exception `j`, then `xz in E(H)` because that quasi-edge must dominate `x`. The edge `xz` is residual: both `x` and `z` miss `j` (`xj` is absent because `x` is isolated in `C`, and `zj` is absent because `j` is the exception), so `xz` cannot be a selected cross-edge with unique exception in `B`.
- If `z` is not used in the first family, residual activity supplies some residual edge incident with source `z`.

These `b` extra residual edges are source-distinct. They are disjoint from the first family: at a used source their A-endpoint is `x` rather than a vertex of `X`, and at an unused source the first family has no edge.

Hence

`r >= C(a-1,2)-e(C)+b`.

But from `e(F)=r+t` and `e(F)=C(a,2)-e(C)`,

`e(C)+r=C(a,2)-t`.

Therefore

`b <= C(a,2)-t-C(a-1,2)=a-1-t`.

For `a=12,b=16`, the right side is `8` when `t=3` and `9` when `t=2`, contradiction. Thus `delta(C)>=1`, and

`d_i=(a-1)-deg_C(i)<=a-2=10`. QED.

A further consequence is `e(C)>=ceil(a/2)=6`, hence `r<=60-t`; the minimal scanner deliberately does **not** use this stronger row-total cut, so its omission only enlarges the finite relaxation.

---

## 9. Exact threshold capacity

For integer `h>=1`, define

`I_h={i in A:s_i>=h}`, `W_h=sum_{i in I_h}s_i`,

`Z_h={u in B:rho_u>=h}`, `z_h=|Z_h|`.

### Lemma 9.1 — threshold source-supplement capacity

If `W_h>0`, then `z_h>=h` and

`W_h <= h z_h + C(z_h-h,2)`,

or equivalently

`2W_h <= z_h^2-z_h+h(h+1)`.                 (9.1)

### Proof

Let `ell_u` be the number of **actual** selected incidences at source `u` whose label lies in `I_h`. By source demand, a source outside `Z_h` selects no heavy label. Also

`W_h=sum_{i in I_h}s_i <= sum_{i in I_h}x_i = sum_{u in Z_h}ell_u`.

If `W_h>0`, at least one heavy label has demand at least `h`, and therefore has at least `h` distinct selected sources, all in `Z_h`; so `z_h>=h`.

Call a source in `Z_h` high-load if `ell_u>h`, and let `J` be the set of such sources, `j=|J|`.

Take a heavy selection `ui->w` from a high-load source. Its supplement `w` neighbours every other selected heavy label at `u`, giving at least `ell_u-1>=h` distinct heavy-label H-neighbours. If `w` lay outside `Z_h`, then `rho_w<h`. Source demand prevents `w` from selecting any heavy label, so all those heavy-label neighbours would be residual, forcing `rho_w>=h`, contradiction. Hence every supplement of a high-load heavy selection lies in `Z_h`.

By Lemma 3.2, high-load heavy arcs use distinct unordered B-pairs wholly inside `Z_h` and incident with `J`. There are exactly

`j(z_h-j)+C(j,2)=j z_h-j(j+1)/2`

such pairs. The other `z_h-j` sources have at most `h` heavy selections each. Therefore

`W_h <= (z_h-j)h + j z_h-j(j+1)/2`.          (9.2)

Set `q=z_h-h`. Subtract the right side of (9.2) from the claimed bound `h z_h+C(q,2)`. The exact gap is

`(q-j)(q-j-1)/2`,

which is nonnegative for every integer `q-j`. This proves (9.1). QED.

This proof depends on two structural premises only: one selected orientation per unordered B-pair, and confinement of supplements of high-load heavy selections to `Z_h`.

---

## 10. Demand-stage finite cuts are necessary

The minimal preparation stage first enumerates every nondecreasing length-12 integer demand tuple `s` with `0<=s_i<=10` satisfying (7.2). Sorting loses no graph: it only chooses a canonical representative of the multiset of A-label demands.

For a fixed demand tuple define

`charge(s)=sum_i s_i(s_i-1)/(a-s_i)`.

From Lemma 7.1 and residual activity,

`r >= b+ceil(charge(s))`.

From `S>=r+2t`,

`r<=S-2t`.

Also `e(F)<=C(a,2)` and `e(F)=r+t`, so

`r<=C(a,2)-t`.

Thus every graph row total lies in the exact safe interval used by `minimal_prepare.py`:

`r_min=b+ceil(charge(s))`,

`r_max=min(S-2t,C(a,2)-t)`.                 (10.1)

### Threshold/source-count pruning

For `h>=2`, residual activity gives

`r=sum_u rho_u >= b+z_h(h-1)`,

so any graph with `r<=r_max` satisfies

`z_h<=floor((r_max-b)/(h-1))`, also `z_h<=b`.              (10.2)

A maximum demand `H` among the labels with demand at least `h` requires at least `H` sources in `Z_h`. If this exceeds the upper bound (10.2), the demand profile is impossible.

Otherwise substitute the same upper bound for `z_h` into the increasing right side of (9.1). If `2W_h` exceeds it, the profile is impossible. These are exactly the `source_count` and `threshold` certificates in `minimal_prepare.py`.

### Exact source-capacity dual

Let the demands be sorted decreasingly for this paragraph and let `D_k` be the sum of the largest `k` demands. If `n_j` is the number of B-sources of residual degree `j`, `1<=j<=a`, then

`sum_j n_j=b`,

`sum_j (j-1)n_j=r-b<=r_max-b`.               (10.3)

A source of residual degree `j` has at most `a-j` selected slots and can select only labels of demand at most `j`. Therefore its contribution to the largest-demand `k`-prefix is at most

`A_{k,j}=min(a-j, # {labels in top k with s_i<=j})`.

Every actual graph must satisfy

`D_k <= sum_j n_j A_{k,j}`                  (10.4)

for every `k`.

The saved dual certificate consists of nonnegative rational/integer prefix weights `y_k`, a free multiplier `mu`, and a positive scale `lambda` such that, for every residual degree `j`,

`mu + sum_k y_k A_{k,j} <= lambda(j-1)`,     (10.5)

while

`sum_k y_k D_k + b mu > lambda(r_max-b)`.   (10.6)

Multiplying (10.4) by `y_k`, summing, then using (10.3) and (10.5) contradicts (10.6). Floating-point optimisation is used only to propose these weights; the inequalities (10.5)-(10.6) are checked exactly before rejection.

Thus every demand profile removed by the minimal preparation stage is genuinely incompatible with an actual graph.

---

## 11. Residual-row scanner preserves every graph

For every retained demand tuple, the scanner enumerates every nondecreasing length-16 row multiset

`rho=(rho_1,...,rho_16)`

with `1<=rho_u<=a` and total in (10.1). Sorting is only a canonical representative of the B-source residual-degree multiset; no correlation with the separately sorted A-demand multiset is assumed.

For a concrete row define the initial cap

`c_u=min(a-rho_u, # {i:s_i<=rho_u})`.

Actual `q_u` satisfies `q_u<=c_u`: the first term is Lemma 5.5; the second follows from source demand.

For the largest-demand `k` labels, let `e_{u,k}` be the number among them eligible at source `u`. Then every graph must satisfy

`D_k <= sum_u min(c_u,e_{u,k})`              (11.1)

because a source contributes at most its selected-degree cap and at most one incidence to each eligible label. A failed inequality therefore safely rejects the row.

Now suppose the current caps `c_w` are valid upper bounds on the actual `q_w`. If source `u` has actual selected degree `q`, its `q` supplements are distinct and Lemma 5.4 gives

`rho_w+q_w>=q-1`

for each supplement. Hence at least `q` distinct vertices `w!=u` satisfy

`rho_w+c_w>=q-1`.

It follows that `q_u` is at most the largest `q<=c_u` having at least `q` such supporters. Replacing every cap by this value therefore preserves a valid upper bound. Simultaneous monotone iteration to a fixed point cannot remove an actual graph. Rechecking (11.1) at the refined caps is again necessary.

These are the only rejection rules in `minimal_rows.cpp`.

---

## 12. Every surviving graph maps to the corrected v2 LP

The last finite model is `independent_threshold_model_v2.py`. It is a **relaxation**: the claim needed here is only that every actual graph induces a feasible point. We now give that embedding explicitly.

Group A-labels by equal demand. For demand group `g`, let its demand be `s_g` and size `n_g`. Group B-sources by equal residual degree. For source group `k`, let its residual degree be `rho_k` and size `n_k`.

### 12.1 Label variables

For each demand group define

`Y_{g,d,R}` = fraction of labels in group `g` having actual pair `(d_i,R_i)=(d,R)`.

For `h>=1`, define

`T_{g,d,R,h}` = fraction **of the whole demand group g** consisting of labels with `(d_i,R_i)=(d,R)` and `x_i>=h`.

Thus `T` is not renormalised within an option. This is the normalization point corrected after the v1 bug.

Every actual label obeys

- if `s_g>0`, `d-R=s_g`; if `s_g=0`, `d<=R`;
- `d<=10` by Lemma 8.1;
- `x_i<=b-R_i`, so with `U=b-R`, `U>=s_g`;
- the `T` tails are nested and equal `Y` for `h<=s_g` because `x_i>=s_g`.

The global empirical averages give exactly

`sum n_g d Y = 2(r+t)`,

`sum n_g R Y = r`.

### 12.2 Source-type variables

For source group `k`, define

`W_{k,q,p}` = fraction of sources in group `k` with actual `(q_u,p_u)=(q,p)`.

Lemma 5.5 gives exactly the option bounds used by v2:

`q<=a-rho_k`,

`p<=rho_k+b-a-1`,

`q+p<=b-1`.

### 12.3 Oriented missing-pair flow

For residual groups `k,l` and selected-degree values `q,q'`, let

`P_{k,l,q,q'}`

be the density, among ordered distinct source/target vertex pairs of those residual groups, of chosen missing-pair orientations `u -> w` whose source has selected degree `q` and whose target has selected degree `q'`.

Averaging actual outgoing and incoming missing-pair orientations gives the v2 source-flow equalities. Lemma 5.4 supplies the compatibility condition

`rho_l+q' >= q-1`.

For two different residual groups, one-orientation-per-unordered-pair gives total orientation density at most one. For a single group the exact density bound is at most `1/2`; v2 uses the weaker bound `<=1`, so every graph still satisfies it.

### 12.4 Selected source-label incidence variables

For source residual group `k`, demand group `g`, source type `(q,p)` and label option `(d,R)`, define

`Z_{k,g,q,p,d,R}`

as the number of actual selected cross-edges of that combined type divided by `n_k n_g`.

Every such actual selected incidence satisfies

`s_g<=rho_k`                         by Lemma 5.2,

`d<=rho_k+R`                         by Lemma 5.2,

`d<=rho_k+q-1`                       by Lemma 5.6,

`R+x>=q+p`                           by Lemma 5.7.

Thus it requires

`x>=req=max(1,q+p-R)`.

The per-source identities are dimensionally

`sum_{g,d,R} n_g Z = q W`.

For any fixed demand group, a source can select each label at most once, giving the v2 per-group incidence cap.

For a fixed label option `(g,d,R)`, the per-label selected-degree identity is

`sum_k n_k Z = E[x] = sum_{h=1}^U T_h`.       (12.1)

**There is no extra factor `n_g` on the right of (12.1).** The historical v1 threshold model inserted that factor and was therefore overconstrained. The corrected v2 code implements (12.1).

Finally, for any threshold `h`, selected incidences whose source type requires `x>=h` can only land on labels with `x>=h`. Their available selected-slot capacity per label is exactly

`E[x 1{x>=h}] = (h-1)T_h + sum_{j=h}^U T_j`.   (12.2)

Indeed, for an individual integer `x`, the right side contributes zero when `x<h` and contributes `(h-1)+(x-h+1)=x` when `x>=h`. Averaging gives (12.2). Hence every nested Hall inequality in corrected v2 is satisfied by the empirical graph point.

All empirical variables lie in `[0,1]`, so the model's explicit upper bounds are also satisfied.

Therefore **every actual graph surviving the earlier necessary cuts induces a feasible point of the corrected v2 LP**.

---

## 13. Exact-certificate handoff

The minimal pipeline now has a completely explicit soundness chain:

`actual graph`

`-> selected/residual system (Sections 2-6)`

`-> charging-admissible demand profile (Section 7)`

`-> threshold/dual-admissible demand profile (Sections 9-10)`

`-> Hall/refinement-admissible residual row (Section 11)`

`-> feasible corrected-v2 LP point (Section 12)`.

The clean minimal replay reports:

| m | t | retained demands | residual rows | exact late rejections | final survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

For every final row, floating-point HiGHS is used only to propose a Farkas ray. The aggregate checker reconstructs the corrected v2 model and verifies an integer certificate exactly. In the model's sign convention, nonnegative multipliers are applied to inequalities and signed multipliers to equalities; after combination every coefficient of a nonnegative primal variable is checked nonnegative while the combined right-hand side is strictly negative. A feasible primal point would therefore imply a nonnegative quantity is at most a negative number, impossible.

Thus, **if every hand lemma above is correct and the exact certificate checker has the stated semantics, the clean zero-survivor replay excludes Delta=16 at both 210 and 211 edges.**

This remains candidate mathematics until independently reviewed.

---

## 14. Reviewer checklist

The highest-value hostile checks are:

1. Lemma 3.1: does insertion of a missing B-pair always force the claimed cross quasi-edge?
2. Lemma 3.2: can two chosen missing pairs ever collide on a selected edge or unordered B-pair?
3. Lemmas 5.2 and 5.4: are the forced cross-edges genuinely residual, especially the A-exception argument?
4. Lemma 5.7: are the incoming-source and outgoing-supplement families always disjoint?
5. Lemma 6.1: in the `rho_u=0` contradiction, are both residual-edge families injective and disjoint?
6. Lemma 7.1: does the source charge budget remain valid at every boundary value?
7. Lemma 9.1: does high-load supplement confinement use exactly the hypotheses proved earlier?
8. Sections 10-11: does every finite pruning step only discard systems already impossible for an actual graph?
9. Section 12: are all empirical variable normalizations dimensionally correct, especially (12.1)-(12.2)?
10. Exact Farkas checker: is its sign convention exactly the one asserted in Section 13?

A failure at any one of these universal steps is blocking regardless of how many workflows are green.
