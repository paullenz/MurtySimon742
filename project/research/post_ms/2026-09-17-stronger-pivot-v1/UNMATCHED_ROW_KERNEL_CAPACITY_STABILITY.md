# Unmatched-row kernel, antipode eligibility, and capacity stability

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorems; not externally reviewed.** This note continues the near-full tight-antipode programme from `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md` and `UNMATCHED_ROW_SINGLETON_COVER.md`. It does not assume the false all-order 2019 Dailly–Foucaud–Hansberg strengthening. The published order-12/32 `X_3` graph remains a mandatory negative control in the already-understood full-tight `u=0` branch.

Let the tight antipodes at a maximum-degree root `v` be the `p` pairs

`P_i={u_i,w_i}`,

let `U` be the unmatched part of `B=N(v)`, and assume `p>=3`. Every `y in U` chooses exactly one endpoint `q_i` from each `P_i`. Write `c(y) in {0,1}^p` for that partial Boolean code.

For fixed `y`, let `K_y` be the graph on `[p]` in which `ij` is an edge exactly when the two selected endpoints `q_i,q_j` are adjacent. Put

`L_y=bar K_y`.

The row-singleton reduction gives the `p` constraints

`{A_i,{i}}`,  where  `A_i=N_{L_y}(i)`.

The resulting graph is denoted `Psi(K_y)`.

---

## 1. A finite-kernel theorem for every cheap unmatched row

The row system has a stronger structural consequence than the already-preserved `tau=1` classification.

Let `K` be any graph on `[p]`, put `L=bar K`, and let `C` be a vertex cover of `Psi(K)` of size `t`. Define

`X={i : {i} in C}`.

Then `|X|<=t`. For every `i notin X`, the singleton endpoint `{i}` is absent from the cover, so the row edge

`{N_L(i),{i}}`

forces

`N_L(i) in C`.

Hence the vertices outside `X` realise at most `t` distinct open neighbourhoods in `L`.

If

`N_L(i)=N_L(j)`

for distinct `i,j`, then neither `i` nor `j` belongs to this common open neighbourhood. Thus `ij` is a nonedge of `L`, and the two vertices have the same neighbours outside `{i,j}`. Equivalently, `i,j` are **true twins in `K`**:

`N_K[i]=N_K[j]`.

Therefore:

> **ROW-KERNEL THEOREM.** If `tau(Psi(K))<=t`, then there is a set `X` of at most `t` exceptional coordinates such that `K-X` is partitioned into at most `t` true-twin cliques.
>
> Equivalently, every row of cover at most `t` is obtained from a graph on at most `2t` kernel vertices by cloning at most `t` designated vertices into true-twin cliques.

This is a finite-template reduction for every fixed row-cover budget. It is independent of `p`.

### Quantitative one-code capacity

For a subset/code `C subseteq [p]`, put

`m(C)=|{i:N_L(i)=C}|`.

In `Psi(K)`,

- if `|C|!=1`, then `deg(C)=m(C)`;
- if `C={j}`, then `deg(C)=m(C)+1`, the extra incidence being the singleton endpoint of row `j`.

Thus, with

`D(K)=max( max_{|C|!=1} m(C), max_j (m({j})+1) )`,

we have the elementary but useful lower bound

> `tau(Psi(K)) >= ceil(p/D(K))`.                         (1.1)

Consequently a row cover of size `t` forces a neighbourhood/twin class of size at least `ceil(p/t)-1`, and usually `ceil(p/t)` unless the heavily used cover code is itself a singleton.

---

## 2. Exact structure of all two-code rows

The cases `tau(Psi(K))<=2` admit a complete hand classification. Again put `L=bar K`.

Take a cover of at most two row-code vertices and classify it by the number of singleton coordinate codes among the chosen cover vertices.

### No singleton cover code

Every open neighbourhood `N_L(i)` is one of at most two fixed sets. Equal open-neighbourhood classes are independent in `L`, and symmetry forces adjacency between the two classes to be all-or-nothing. Hence `L` is complete bipartite, allowing the empty graph as the degenerate one-class case.

### Exactly one singleton cover code

Let the singleton be `{x}`. Every row other than `x` must have neighbourhood either `{x}` or the second cover code. If that second code is actually used, symmetry forces it to be the empty set. Thus `L` is a star centred at `x` together with isolated vertices. The spanning-star endpoint includes the already-known one-code case.

### Two singleton cover codes

Let them be `{x}` and `{y}`. Every other vertex has open neighbourhood exactly `{x}` or exactly `{y}`. Thus every vertex outside `{x,y}` is a leaf attached to exactly one of the two centres; the edge `xy` may be present or absent and there are no other edges.

Conversely each of these three forms has the displayed two-code cover. Therefore:

> **TWO-CODE ROW CLASSIFICATION.** `tau(Psi(K))<=2` if and only if `L=bar K` has one of the following forms:
>
> 1. a complete bipartite graph (including the empty degeneration);
> 2. a star plus isolated vertices;
> 3. a two-centre graph in which every other vertex is a leaf of exactly one centre, with the centre edge optional.

The old one-code theorem is recovered as the strict subcase

`tau(Psi(K))=1 iff L is empty or a spanning star`,

i.e. `K=K_p` or `K=K_{p-1} dotcup K_1`.

This exact `tau<=2` result replaces an unstructured list of the eleven order-seven two-code examples by three uniform normal forms.

---

## 3. Exact bridge from a row to matched-antipode eligibility

The row graph is not merely a support gadget: its complement degrees record exactly which matched antipodes are possible.

Let `q_i` be the endpoint of `P_i` adjacent to `y`, and let `q_i'` be its tight mate. The two forced witness codes for the physical edge `y q_i` satisfy

> `alpha(q_i) Delta bar(c(y)) = N_{L_y}(i)`,             (3.1)
>
> `beta_i(y) Delta bar(c(y)) = {i}`.                    (3.2)

These are exactly the two translated row endpoints from the row-singleton reduction.

Now compare `c(y)` with the antipode code of the **non-neighbour** `q_i'`. The definition of `alpha` gives

> `c(y)=alpha(q_i')`
>
> `iff i is universal in K_y`
>
> `iff i is isolated in L_y`.                           (3.3)

Hence:

> **MATCHED-ANTIPODE ELIGIBILITY THEOREM.** The number of matched endpoints that are even code-eligible to be antipodes of `y` is exactly the number of isolated vertices of `L_y`.

If `L_y` has no isolated vertex, then `y` has no possible antipode in the matched part `P`. The preserved no-private-foot theorem says that every unmatched vertex nevertheless has an antipode. Therefore:

> **NO-ISOLATE COROLLARY.** If `L_y` has no isolated vertex, then `y` has a complementary unmatched antipode `z in U`, and
>
> `c(z)=bar(c(y))`.

Combining this with the exact two-code classification yields a particularly small cheap-row dichotomy:

> **TWO-CODE ANTIPODE DICHOTOMY.** If `tau(Psi(K_y))<=2`, then either
>
> 1. `y` is forced into a complementary `U--U` antipode, or
> 2. every nonedge of `K_y` is incident with one common coordinate (with the complete graph allowed as the zero-nonedge case).

Indeed, among the three `tau<=2` complement forms, the only ones with an isolated vertex are the empty graph or a star together with isolates (the isolated-centre degeneration of the two-centre form is the same star-plus-isolate case).

This is the first compact classification of all unmatched rows that can be covered with only two codes **and** avoid an immediate complementary antipode.

---

## 4. Selected/Hall alpha-spill inequality

Retain the A-code multiplicities

`n_c=|{x in A : c(x)=c}|`,  so  `sum_c n_c=a`.

For a matched endpoint `q in P`, let

`d_U(q)=|N(q) cap U|`

and let `h_q` be the number of its `P--U` obligations that the selected system orients to the alpha endpoint `alpha(q)`.

The preserved per-source capacity rule gives

> `h_q <= n_{alpha(q)}`.                                (4.1)

Let `B_beta` be the total number of `P--U` obligations oriented from their unmatched source, hence to beta codes. Since there are exactly `pu` physical `P--U` edges,

`B_beta=pu-sum_q h_q`.

Define the alpha weight

`W_alpha=sum_{q in P} n_{alpha(q)}`.

Then

> `B_beta >= pu-W_alpha`.                               (4.2)

Every beta-oriented obligation from a fixed unmatched source `y` uses a distinct selected cross edge `yx`. Distinct sources give distinct physical cross edges. Therefore all beta-oriented obligations inject into `E(A,U)`, and

> `B_beta <= s=e_G(A,U)`.                               (4.3)

Combining (4.2)--(4.3):

> **ALPHA-SPILL THEOREM.**
>
> `s >= pu-W_alpha`.                                    (4.4)

A fibrewise refinement is

> `B_beta >= sum_{q in P}(d_U(q)-n_{alpha(q)})_+`
>
> `       >= sum_{i=1}^p (u-n_{alpha(u_i)}-n_{alpha(w_i)})_+`.   (4.5)

Let `bar q=binom(u,2)-q` be the number of nonedges inside `U`. The exact unmatched-slack ledger becomes

`E_U=u(p+u-1)-2q-s = pu+2 bar q-s`.

Hence (4.4) is equivalently the upper bound

> `E_U <= 2 bar q + W_alpha`.                           (4.6)

This directly converts unmatched slack into either nonedges of `U` or A-mass on alpha codes.

---

## 5. Alpha multiplicity is a switching true-twin invariant

The weight `W_alpha` has a structural interpretation rather than being an opaque Boolean multiplicity.

Label the two endpoints of fibre `i` by `(i,0),(i,1)`, and write the 2-lift signing as `sigma_ij in {0,1}`, with

`(i,s)~(j,s xor sigma_ij)`.

Let the signed row `rho_i in {0,1}^p` have

`rho_i(i)=0`,  `rho_i(j)=sigma_ij` for `j!=i`.

Then the antipode transversal of endpoint `(i,s)` is

> `alpha(i,s)=(1-s) 1 xor rho_i`.                       (5.1)

Consequently, for any Boolean code `c`,

> `|alpha^{-1}(c)| = |{i : rho_i in {c,bar c}}|`.       (5.2)

Call the right side a **projective signed-row class**. Put

`mu_alpha=max_c |alpha^{-1}(c)|`.

A projective signed-row class can be switched into a true-twin clique: if `rho_i=c xor theta_i 1` on a class `I`, choose the switching vector with those `theta_i`; the diagonal condition forces `theta_i=c_i`, all vertices of `I` become pairwise adjacent, and their adjacency to every outside coordinate is identical. Conversely, a true-twin clique in any switched state normalises its signed rows into one projective class.

Therefore:

> **PROJECTIVE-TWIN THEOREM.**
>
> `mu_alpha` is exactly the largest size of a true-twin clique occurring in any switching state of the matched 2-lift.       (5.3)

Since `W_alpha<=mu_alpha a`, the alpha-spill theorem has the coarser purely structural form

> `s >= pu-mu_alpha a`,                                 (5.4)
>
> `E_U <= 2 bar q + mu_alpha a`.                        (5.5)

The advantage of (5.3) is that a Hall-capacity obstruction can now be phrased in the same switching language as the already-developed full-tight machinery.

---

## 6. Beta pools are radius-one Hamming spheres

There is also an exact overlap theorem on the beta side. For an unmatched code `c`, its complete beta pool is

`B(c)={bar c Delta {i}: i in [p]}`.

Thus `B(c)` is the radius-one Hamming sphere around `bar c` with the centre omitted.

For codes `c,d`, direct hypercube algebra gives

> `|B(c) cap B(d)| = p` if `c=d`,
>
> `|B(c) cap B(d)| = 2` if `dist(c,d)=2`,
>
> `|B(c) cap B(d)| = 0` otherwise.                     (6.1)

In particular, for `p>=3`, complementary U--U antipode classes have **disjoint beta pools**.

Group unmatched vertices by their partial code. Let

`t_c=|{y in U:c(y)=c}|`

and let `B_c` be the number of beta-oriented obligations sourced by that code class. A fixed beta code can occur at most once in each row of the class, hence at most `t_c` times across that class. Therefore the selected beta support contributed by class `c` has size at least

> `ceil(B_c/t_c)`.                                      (6.2)

If `C_U` is the set of occupied unmatched codes and `e_2(C_U)` is the number of unordered pairs at Hamming distance two, first-order inclusion-exclusion with (6.1) gives

> `|selected beta-code support|`
>
> ` >= sum_{c in C_U} ceil(B_c/t_c) - 2 e_2(C_U)`.      (6.3)

For a complementary pair `c,bar c` and `p>=3`, there is no overlap term at all:

> support from the two classes
>
> ` >= ceil(B_c/t_c)+ceil(B_bar c/t_bar c)`.            (6.4)

This is the natural support counterpart to the alpha-spill inequality and is especially relevant to the complementary U--U antipodes forced by Section 3.

---

## 7. Strategic consequence

The unmatched-row frontier is now considerably smaller.

- Fixed row-cover budget `t` implies a finite `2t`-vertex kernel plus true-twin blow-ups.
- `tau<=2` has only three explicit complement normal forms.
- A `tau<=2` row that can avoid a complementary U--U antipode has all of its nonedges concentrated at one coordinate.
- Selected/Hall capacities force unmatched slack to be paid by U-nonedges or weighted alpha-code mass.
- Alpha multiplicity is exactly a switching true-twin invariant.
- Complementary antipode code classes have disjoint beta pools.

The next high-value step is therefore **not** to enumerate arbitrary unmatched rows. It is to combine the two-code antipode dichotomy with the alpha/beta capacity inequalities: generic rows have cover at least three; cheap rows either collapse to a one-centre nonedge normal form or force complementary U-code classes whose beta supports cannot overlap.
