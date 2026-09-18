# Near-full tight-antipode normal form and augmented orientation constraints

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted.** This note begins at the live post-full-tight frontier. It does not assume the false all-order 2019 second-extremal conjecture. The published 2024 order-12/32 `X_3` graph remains the mandatory hostile control and sits in the already-understood full-tight `u=0` branch.

Let `G` be D2C, let `v` be a maximum-degree root, and put

`B=N(v)`, `A=V(G)\N[v]`, `b=|B|`, `a=|A|`, `lambda=2b-n=b-a-1`.

Let the complete set of tight antipodes at `v` consist of

`P_i={u_i,w_i}`, `1<=i<=p`.

Tight antipodes form a matching by `ANTIPODE_TIGHT_MATCHING_STABILITY.md`. Put

`P=union_i P_i`, `U=B\P`, `u=|U|`, so `b=2p+u`.

Write

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`,

and retain the canonical residual variables

`Q=e(G[B])`, `Q+r=# nonedges between A and B`, `delta=r-f`.

---

## 1. Partial Boolean-pair normal form

Tightness of `P_i` means every vertex outside `{v,u_i,w_i}` is adjacent to exactly one endpoint of `P_i`.

Therefore:

1. between any two tight pairs `P_i,P_j`, the induced `2 x 2` bipartite graph is a perfect matching;
2. every unmatched `y in U` has exactly one neighbour in every `P_i`;
3. every `x in A` has exactly one neighbour in every `P_i`.

Thus every vertex of `A union U` carries a canonical partial Boolean code

`c(z) in {0,1}^p`,

recording its chosen endpoint in each tight pair.

The matched part `G[P]` is a 2-lift of `K_p`, exactly as in the full-tight branch, but now the unmatched B-vertices themselves are additional transversals of the same fibres.

### Exact rooted-triangle count

There are

- `2 binom(p,2)=p(p-1)` edges between tight pairs;
- exactly `pu` edges between `P` and `U`;
- `q` edges inside `U`.

Hence

> `Q = p(p-1)+pu+q = p(p+u-1)+q`.          (1.1)

### Exact cross and residual counts

The A--B edge count is

`e_G(A,B)=ap+s`.

Since `b=2p+u`, the number of missing A--B incidences is

`ab-(ap+s)=a(p+u)-s`.

Using `Q+r` for the same quantity gives

> `r = a(p+u)-s-Q`
>
> `  = (p+u)(a-p)+p-s-q`.                 (1.2)

Therefore

> `delta=(p+u)(a-p)+p-s-q-f`.             (1.3)

These identities are exact; no density assumption is used.

### Slack on unmatched B and on A

For `y in U`, write `d_U(y)` and `d_A(y)` for its degrees into `U` and `A`. Then

`d_G(y)=1+p+d_U(y)+d_A(y)`,

so its maximum-degree slack is

`epsilon_y=p+u-1-d_U(y)-d_A(y)`.

Hence

> `E_U:=sum_{y in U} epsilon_y = u(p+u-1)-2q-s`.       (1.4)

Similarly, for `x in A`,

`epsilon_x=p+u-d_U(x)-d_F(x)`,

and therefore

> `L_A:=sum_{x in A} epsilon_x = a(p+u)-s-2f`.         (1.5)

Every tight pair satisfies

`epsilon_{u_i}+epsilon_{w_i}=lambda+1`.

Thus

> `sum_{z in B} epsilon_z = p(lambda+1)+E_U`.          (1.6)

This agrees with the canonical B-slack ledger.

---

## 2. Two or more tight pairs eliminate private feet

Assume `p>=2`.

Every vertex of `B` is triangle-active at the root:

- an endpoint of a tight pair has a B-neighbour in every other tight pair;
- an unmatched vertex has one B-neighbour in every tight pair.

Now let `x in A`. The partial Boolean normal form gives

`|N_B(x) cap P|=p>=2`.

So no A-vertex can satisfy `N_B(x)={y}` for any `y in B`. In other words:

> **NO-PRIVATE-FOOT LEMMA.** If `p>=2`, no triangle-active root neighbour has a private A-foot.

The preserved root-edge dichotomy therefore has only the antipode alternative available. Consequently:

> **ANTIPODE-COVER COROLLARY.** If `p>=2`, every vertex of `B` has at least one antipode partner at `v`.

The matched vertices already possess their tight partners. Every `y in U` has no tight partner by definition of `U`, so every antipode incident with `y` is errorful:

`eta>=1`.

This is the first exact bridge from a near-full tight matching to the errorful-antipode stability problem: **unmatched vertices cannot hide in the private-foot branch.**

---

## 3. Partial-code restrictions on errorful antipodes

Fix the partial Boolean coordinates supplied by the tight pairs.

### 3.1 Antipodes inside U

If `y,z in U` are antipodes, then they have no common neighbour in any tight pair. Since each chooses exactly one endpoint of each `P_i`, their choices must be opposite in every coordinate:

> `c(z)=bar(c(y))`.                                    (3.1)

Thus the U--U antipode graph runs only between complementary partial-code classes.

### 3.2 An unmatched vertex antipodal to a matched endpoint

Let `q in P_i` and let `q'` be its tight mate. Define the transversal `alpha(q)` intrinsically by:

- in `P_i`, choose `q'`;
- in every `P_j`, `j!=i`, choose the endpoint **not** adjacent to `q`.

If `y in U` is antipodal to `q`, then the no-common-neighbour condition forces

> `c(y)=alpha(q)`.                                     (3.2)

Moreover the two slack identities give an exact error formula. Since

`epsilon_q+epsilon_q'=lambda+1`

and

`epsilon_y+epsilon_q=lambda+1+eta(yq)`,

we get

> `eta(yq)=epsilon_y-epsilon_q'`.                      (3.3)

Because `y` is unmatched, this antipode is errorful, so

> `epsilon_y >= epsilon_q'+1`.                         (3.4)

Thus a matched-endpoint antipode forces both a special partial Boolean code and a strict slack comparison with the endpoint's tight mate.

---

## 4. The full-tight orientation graph survives as a necessary subproblem

Restrict attention to B-edges whose two endpoints lie in distinct tight pairs. Their induced graph is the same 2-lift of `K_p` as in the full-tight branch.

For such a physical B-edge, the preserved selected-witness argument uses an A-vertex and, on the `p` tight coordinates, forces exactly the same two orientation codes as in the full-tight construction. Therefore, if `C_A` is the set of distinct partial codes actually realised by A-vertices, then

> `C_A` is a vertex cover of the ordinary full-tight orientation-code graph `Omega_P`.      (4.1)

Hence

> `tau(Omega_P) <= |C_A| <= a`.                        (4.2)

This imports every **support-only** full-tight exclusion into the near-full branch without importing any full-tight residual identity.

Since

`a=b-lambda-1=2p+u-lambda-1`,

we have

> `a<=2p  iff  u<=lambda+1`.                           (4.3)

The preserved full-tight hierarchy proves that, for `p>=19`, every minimum switching defect `d_*>=5` has strict support excess `tau(Omega_P)>2p` (the `d_*=0,...,4` cases required additional full-tight arguments and are not imported here).

Therefore:

> **LOW-DEFECT REDUCTION.** If `p>=19` and `u<=lambda+1`, then the inherited matched-pair switching problem must satisfy
>
> `d_*<=4`.                                             (4.4)

Equivalently, if `p>=19` and `d_*>=5`, then any above-threshold near-full candidate must have

> `u>=lambda+2`.                                       (4.5)

This is only a reduction, not a closure: low switching defect `0,...,4` must still be combined with the unmatched/errorful structure.

---

## 5. Augmented orientation-code constraints from unmatched vertices

The ordinary `Omega_P` uses only the `P--P` rooted triangle edges. The unmatched vertices generate additional exact selected-witness constraints.

Let `y in U`, and for each `i` let `q_i in P_i` be the unique endpoint adjacent to `y`.

For each physical edge `y q_i`, the canonical selected representative can be oriented in one of two ways.

### Orientation from the matched endpoint

If

`q_i x -> y`,

then on the tight coordinates the witness `x in A` must choose the transversal `alpha(q_i)` defined in Section 3.2.

### Orientation from the unmatched endpoint

If

`y x -> q_i`,

then the code of `x` is the unique transversal `beta_i(y)` which

- chooses `q_i` in coordinate `i`;
- in every `j!=i`, chooses the endpoint of `P_j` not adjacent to `y`.

Thus every `P--U` edge produces the two-code constraint

> `{ alpha(q_i), beta_i(y) }`.                         (5.1)

Likewise, if `yz in E(G[U])`, orienting the selected representative from `y` forces the transversal complementary to `c(y)` in every tight coordinate, while orienting from `z` forces the complement of `c(z)`. Hence every U--U edge gives

> `{ bar(c(y)), bar(c(z)) }`.                          (5.2)

Together with the ordinary P--P orientation edges, these define an **augmented orientation multigraph** `Omega^+` on `{0,1}^p` (loops are allowed when the two forced codes coincide).

> **AUGMENTED COVER NECESSITY.** The realised A-code set `C_A` is a vertex cover of `Omega^+`.      (5.3)

This is exact and uses every rooted triangle edge in `G[B]`, not only the matched-pair subgraph.

### Capacity refinement

Support alone discards multiplicity. The canonical selected system gives a stronger per-source capacity rule:

- for a fixed B-source `z`, distinct selected obligations use distinct cross edges `zx`;
- therefore, if `n_c` A-vertices realise code `c`, at most `n_c` obligations from that fixed source can be assigned to the orientation endpoint `c`.

So the near-full problem is naturally a **capacitated orientation-cover problem** on `Omega^+`, with capacities given by A-code multiplicities. This is the correct place to reuse the selected/Hall machinery; it is strictly richer than the old support cover and does not require pretending the unmatched vertices are full tight fibres.

---

## 6. Strategic consequence

The full-tight branch should not be reopened. The near-full branch now has an exact zero-error core plus explicit error coordinates:

- `p` tight pairs form a genuine 2-lift/Boolean subsystem;
- every A-vertex and every unmatched B-vertex is a transversal of that subsystem;
- `p>=2` makes private feet impossible and forces every unmatched B-vertex into an **errorful antipode**;
- those antipodes obey complementary/special-code restrictions;
- all rooted B-edges are encoded by the augmented orientation graph `Omega^+` with per-source Hall capacities.

The next highest-value target is therefore not another switching-defect scan. It is a stability theorem for `Omega^+` showing that either

1. the unmatched set forces strict support/capacity excess, or
2. the unmatched partial codes collapse to a small number of low-defect exceptional patterns, which can then be priced using `delta=r-e(F)` and the antipode error identities.

The companion note `ANTIPODE_BRANCHING_ERROR_PAYMENT.md` supplies a second ingredient: branching in the antipode graph itself has a quadratic error cost.
