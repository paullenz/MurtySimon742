# Complete-row global normal form and mirror-capacity rigidity

18 September 2026. Research directed by Paul Lenz; derivation and finite regression by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted.** This note continues `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`, `UNMATCHED_ROW_SINGLETON_COVER.md`, `UNMATCHED_ROW_KERNEL_CAPACITY_STABILITY.md`, and `COMPLETE_ROW_CLIQUE_PRIVATE_FEET.md`. Its purpose is to exploit the apparently local cheap row `K_y=K_p` globally, rather than treating it as one more row-cover exception.

Throughout, fix a maximum-degree root `v`, a complete tight matching

`P_1,...,P_p`, `P_i={q_i,q_i'}`, `p>=3`,

and unmatched set `U=B\P`. Put `u=|U|`, `b=2p+u`, and

`lambda=2b-n=b-a-1`, so `a=2p+u-lambda-1`.

Assume that some unmatched vertex `y in U` has complete selected-endpoint row

`K_y=K_p`.

Switch coordinates so that

`c(y)=0^p`,

and write

`Q={q_1,...,q_p}`

for the matched endpoints selected by `y`, with `Q'={q_1',...,q_p'}` their tight mates.

---

## 1. One complete row determines the entire matched 2-lift

Because `K_y=K_p`, every edge `q_iq_j` is present.

Between any two tight fibres `P_i,P_j`, the matched-core edges form a perfect matching. Hence, once `q_iq_j` is present, the second edge is necessarily `q_i'q_j'`, while the two cross edges are absent.

Therefore a single complete unmatched row forces

> **COMPLETE-ROW GLOBAL CORE LEMMA.**
>
> `G[P]=K_p dotcup K_p`,
>
> with components `Q` and `Q'`.

So the matched signing is switching-equivalent to the zero signing. This is a global collapse of the whole matched 2-lift, not merely a local property of `y`.

---

## 2. Every other row is now a Hamming-layer object

For any `z in A union U`, let

`S(z)={i:c_i(z)=1}`

relative to the normalization above, and write

`rho(z)=|S(z)|=d_H(c(z),c(y))`.

The selected matched endpoints of `z` are

- `q_i` for `i notin S(z)`;
- `q_i'` for `i in S(z)`.

Since `Q` and `Q'` are the two clique components of `G[P]`, two selected endpoints are adjacent exactly when they lie on the same side. Hence

> `K_z = K_{rho(z)} dotcup K_{p-rho(z)}`.                 (CR1)

Equivalently,

> `bar K_z = K_{rho(z),p-rho(z)}`.                       (CR2)

This makes the exact row-singleton cover immediate from the preserved `tau<=2` classification:

> `tau(Psi(K_z))=1` for `rho(z) in {0,1,p-1,p}`;
>
> `tau(Psi(K_z))=2` for `2<=rho(z)<=p-2`.                (CR3)

The four cover-one Hamming layers split into two structurally different types:

- `rho=0,p`: complete rows;
- `rho=1,p-1`: clique-plus-one-isolate rows.

The matched-antipode eligibility theorem says that eligible matched endpoints correspond to isolated vertices of `bar K_z`. But `K_{rho,p-rho}` has isolated vertices only when `rho=0` or `p`.

Therefore:

> **NON-CENTRE ANTIPODE COROLLARY.** Every unmatched `z` whose code is not one of the two centres `0^p,1^p` has no eligible matched antipode. Since `p>=2` rules out private A-feet for root edges, such a `z` must have an antipode in `U`, and that partner has complementary code `bar c(z)`.

Thus one complete row Hamming-stratifies the entire unmatched population and sends every non-centre row into the U--U antipode/error system.

---

## 3. The matched orientation-code graph is exactly two cliques

For the zero signing, direct evaluation of the preserved forced-code formula gives the P--P orientation graph

> `Omega_P = K_p dotcup K_p`.                              (CR4)

One component is the radius-one sphere around `0^p`, namely the singleton codes

`{i}`, `i=1,...,p`,

and the other is the radius-one sphere around `1^p`, namely the co-singletons

`[p]\{i}`, `i=1,...,p`.

Consequently

> `tau(Omega_P)=2p-2`.                                     (CR5)

Any realised A-code support therefore contains at least `p-1` distinct classes in each of these two disjoint spheres.

Since

`a=2p+u-lambda-1`,

the number of A vertices beyond the bare P--P support lower bound is exactly

> `R_A := a-(2p-2)=u-lambda+1`.                            (CR6)

This quantity is a useful support-stability budget for the complete-row branch.

---

## 4. Two-centre Hall spill inequality

Under the zero signing all alpha codes collapse to the two centre codes.

For each coordinate `i`, define

`t_i^0 = |{z in U:c_i(z)=0}|`,

`t_i^1 = |{z in U:c_i(z)=1}| = u-t_i^0`.

Let

`n_0=|{x in A:c(x)=0^p}|`,

`n_1=|{x in A:c(x)=1^p}|`.

For source `q_i` on the `Q` side, every unmatched row selecting `q_i` has the same alpha code `1^p`. Per-source Hall capacity therefore allows at most `n_1` of the `t_i^0` obligations to be discharged alpha-side. The rest must beta-spill. The complementary statement holds for `q_i'`.

Hence, if `B_beta` is the total number of beta-oriented P--U obligations,

> `B_beta >= sum_i (t_i^0-n_1)_+ + sum_i (t_i^1-n_0)_+`.  (CR7)

This is the general alpha-spill theorem specialized to the globally collapsed core, where the alpha kernel has only two codes.

---

## 5. Mirror-centre multiplicity theorem

Let

`Y_0={y in U:c(y)=0^p}`

and put `t_0=|Y_0|`. Every vertex of `Y_0` is a complete row. Let `n_1` be the A-multiplicity of the opposite centre code `1^p`.

Suppose first that

`n_1<t_0`.                                                     (5.1)

Fix a source `q_i in Q`. The `t_0` row obligations `yq_i`, `y in Y_0`, all have alpha code `1^p`. Per-source Hall capacity can discharge at most `n_1` of them through that alpha class. Therefore at least one obligation at **every** coordinate `i` beta-spills.

Thus A contains a beta-selected witness of every co-singleton code

`beta_i = 1^p Delta {i}`,

and each such witness is adjacent to some row in `Y_0`.

Now use the clique `Q` itself. The preserved D2C clique-criticality lemma gives private A-feet for all but at most one source of the clique. Hence for at least `p-1` indices `i`, there is an A-vertex `h_i` adjacent to `q_i` and to no other vertex of `Q`.

Its Boolean code is exactly `beta_i`.

Crucially, `h_i` is nonadjacent to **every** complete row in `Y_0`. Indeed, choose an internal critical edge of `Q` for which `h_i` is the source foot, say with target `q_j`. Every row in `Y_0` is adjacent to `q_j`; if it were also adjacent to `h_i`, it would be a second common neighbour of `h_i` and the target, contradicting the private-foot witness condition.

Therefore the private foot `h_i` cannot coincide with the beta-selected witness in code class `beta_i`, because the selected witness is adjacent to a row of `Y_0`.

So under (5.1):

- all `p` co-singleton classes contain a beta-selected A-vertex;
- at least `p-1` of those classes contain an additional, distinct private-foot A-vertex.

The co-singleton sphere therefore contains at least

`2p-1`

A vertices.

The opposite singleton component of `Omega_P` independently requires at least `p-1` A vertices, and the centre code `1^p` contributes `n_1` further vertices. These code classes are pairwise disjoint for `p>=3`. Hence

> `n_1<t_0  ==>  a>=3p-2+n_1`.                           (CR8)

In particular, if

`a<=3p-3`,                                                     (5.2)

then (CR8) is impossible, so

> `n_1>=t_0`.                                                  (CR9)

By complement symmetry, if `Y_1={y in U:c(y)=1^p}`, `t_1=|Y_1|`, then under the same support-budget condition

> `n_0>=t_1`.                                                  (CR10)

Using (CR6), condition (5.2) has the equivalent forms

> `a<=3p-3`
>
> `iff u<=p+lambda-2`
>
> `iff R_A<=p-1`.                                              (CR11)

We therefore record:

> **MIRROR-CENTRE MULTIPLICITY THEOREM.** In the complete-row global normal form, if `p>=3` and `R_A<=p-1`, then every complete-row centre population in U is mirrored by at least as many A-vertices in the opposite centre code:
>
> `n_1>=t_0`, `n_0>=t_1`.

This is a combined Hall-capacity + clique-criticality statement. It is stronger than merely saying that complete rows occupy cheap one-code covers.

---

## 6. All-complete unmatched populations are rigid

Suppose every unmatched row is complete. By (CR1), this means every U-code is one of the two centres, so

`t_0+t_1=u`.

Under `R_A<=p-1`, the mirror theorem gives

`n_0+n_1>=u`.

Together with the mandatory `2p-2` P--P sphere support,

> `a>=2p-2+u`.                                                (CR12)

But

`a=2p+u-lambda-1`.

Thus any all-complete configuration in the small-surplus regime satisfies

> `lambda<=1`.                                                 (CR13)

More precisely, the number of A vertices left after paying for the two mandatory sphere supports and the mirrored centre population is at most

> `a-(2p-2+u)=1-lambda`.                                      (CR14)

Therefore:

- `lambda>=2`: impossible in this regime;
- `lambda=1`: exact support saturation;
- `lambda=0`: at most one additional A vertex;
- `lambda=-1`: at most two additional A vertices.

The hard near-balanced cases have therefore become finite-surplus support configurations once all unmatched rows are complete.

This is not yet a second-extremal closure: the remaining one/two extra vertices can still carry many F-edges, and the centre multiplicities themselves require defect pricing.

---

## 7. A useful failed route: raw private-foot nonneighbour counting is too weak

It is tempting to convert the complete-row private feet directly into `L_A` by counting their forced nonneighbours in U.

For a co-singleton private foot `h_i`, chosen from a critical edge `q_i -> q_j` inside `Q`, every complete row of centre `0^p` is nonadjacent to `h_i`. Combining only this fact with the degree definition gives at best a bound of the schematic form

`epsilon_{h_i} >= (t_0+lambda-u)_+`,

and hence a sidewise estimate like

`L_A >= (p-1)(t_0+lambda-u)_+`.

For the hard cases `lambda=-1,0`, one always has `t_0<=u`, so this payment is usually zero. The same problem occurs on the complementary side.

Therefore **raw nonneighbour counting is not the right bridge to `L_A`**. The next argument must exploit role multiplicity and/or F-separation among the mandatory sphere/private-foot populations, rather than merely the fact that private feet miss complete rows.

This negative result is preserved to prevent repeated return to a weak route.

---

## 8. Next structural target: private-foot F-separation

The complete-row normal form provides two natural private-foot layers.

For every non-sink source `q_i` of the clique `Q`, choose an internal critical target `q_{tau(i)}` and a private foot `h_i` of co-singleton code `1^p Delta {i}`. Similarly, on `Q'`, choose `q'_{sigma(j)}` and a private foot `g_j` of singleton code `{j}`.

If `h_i g_j` is an F-edge, the private-foot condition for `h_i` forces `g_j` to be nonadjacent to `q_{tau(i)}`. A singleton-code vertex is nonadjacent to exactly one Q-endpoint, namely `q_j`. Hence

`tau(i)=j`.

Symmetrically, the private-foot condition for `g_j` forces

`sigma(j)=i`.

Thus cross-layer F-edges between the chosen private feet can occur only at mutual target pairs. In particular they form a matching.

This local rule is promising, but no global `L_A` or `e(F)` bound is promoted here: same-layer private-foot edges and edges to the small support surplus still need to be priced correctly.

---

## 9. Finite regression and trust boundary

The companion checker `check_complete_row_global_normal_form.py` performs only regression/audit support. It verifies for `p=3,...,10`:

- the zero-signing matched core is `K_p dotcup K_p`;
- for every Boolean code, `K_z=K_r dotcup K_{p-r}`;
- the exact row-singleton cover is 1 precisely on Hamming layers `0,1,p-1,p`, and 2 on every interior layer;
- `Omega_P` has exactly two `K_p` components and `tau(Omega_P)=2p-2`.

It also sweeps the arithmetic equivalence (CR11) for a wider parameter box.

The checker does **not** prove the D2C clique-private-foot lemma, Hall-capacity theorem, or mirror-centre theorem; those are hand arguments inherited/derived above.

The published `12/32` graph remains untouched. It is a full-tight `u=0`, `p=4`, residual-zero hostile control, whereas every theorem in this note assumes the near-full complete-row setup with an unmatched complete row.

No all-order second-extremal theorem is claimed.
