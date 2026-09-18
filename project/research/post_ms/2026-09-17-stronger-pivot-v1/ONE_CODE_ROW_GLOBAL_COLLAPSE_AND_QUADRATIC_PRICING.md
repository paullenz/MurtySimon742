# One-code unmatched rows force global core collapse and quadratic A-slack

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not externally reviewed.** This note combines the exact one-code row classification in `UNMATCHED_ROW_KERNEL_CAPACITY_STABILITY.md` with the new A-side pricing theorem in `MATCHED_PRIVATE_FOOT_SLACK_AND_COMPLETE_ROW_QUADRATIC_EXCLUSION.md`.

The important correction is that the quadratic A-slack theorem is **not confined to complete unmatched rows**. The other one-code row, `K_{p-1} dotcup K_1`, also collapses the entire matched 2-lift to the zero-signing class after one fibre switch.

---

## 1. Setup

Fix a maximum-degree root `v`, tight fibres

`P_i={q_i,q_i'}`, `i=1,...,p`, `p>=3`,

and unmatched set `U` of size `u`.

For `y in U`, let `q_i` denote the endpoint of `P_i` adjacent to `y`, and let `K_y` be the graph on `[p]` in which

`ij in E(K_y) iff q_i q_j in E(G)`.

The exact row theorem says

> `tau(Psi(K_y))=1`
>
> iff
>
> `K_y=K_p` or `K_y=K_{p-1} dotcup K_1`.                       `(OC1)`

---

## 2. Complete row

If `K_y=K_p`, every selected-selected pair `q_iq_j` is an edge. Between every pair of tight fibres the matched-core edges form a perfect matching, so the mate-mate edge `q_i'q_j'` is also present and the two cross edges are absent.

Thus directly

`G[P]=K_p dotcup K_p`.

This is the already-preserved complete-row global core lemma.

---

## 3. Clique-plus-isolate row

Now suppose

`K_y=K_{p-1} dotcup K_1`.

Let `r` be the isolated coordinate.

For every pair `i,j != r`, the selected endpoints are adjacent:

`q_i q_j in E(G)`.

Hence the fibre matching between `P_i,P_j` is parallel with respect to the selected labels.

For every `j != r`, however,

`q_r q_j notin E(G)`.

Since the two edges between `P_r` and `P_j` form a perfect matching, they must be the cross pair

`q_r q_j'`, `q_r' q_j`.

Now switch the labels in the single fibre `P_r`:

`q_r <-> q_r'`.

After this one switch, every fibre pair is parallel. Therefore

> **ONE-ISOLATE GLOBAL CORE LEMMA.** If one unmatched row has
>
> `K_y=K_{p-1} dotcup K_1`,
>
> then the complete matched 2-lift is switching-equivalent to
>
> `K_p dotcup K_p`.                                             `(OC2)`

Under the switched zero-signing labels, the same physical unmatched vertex `y` simply has Hamming-weight-one code (or, after global complement, weight `p-1`).

Thus the distinction between the two one-code row types is a distinction of the unmatched **Hamming layer**, not of the global matched signing.

---

## 4. Unified one-code global normal form

Combining `(OC1)` and `(OC2)`:

> **ONE-CODE GLOBAL COLLAPSE THEOREM.** If any unmatched row satisfies
>
> `tau(Psi(K_y))=1`,
>
> then after switching tight fibres
>
> `G[P]=K_p dotcup K_p`.                                       `(OC3)`

In that normalization every A/U row satisfies

`K_z=K_{rho(z)} dotcup K_{p-rho(z)}`,

where `rho(z)` is its Hamming distance from one zero-signing centre.

The original one-code row lies in one of the four boundary layers

`rho in {0,1,p-1,p}`.

The centre layers `0,p` are complete rows. The layers `1,p-1` are clique-plus-isolate rows and, by the preserved matched-antipode eligibility theorem, have no matched antipode; every unmatched vertex in those layers must therefore enter a complementary U--U antipode.

---

## 5. Quadratic A-side pricing applies to every one-code row

Once `(OC3)` holds, the matched orientation graph is exactly

`Omega_P=K_p dotcup K_p`,

on the singleton and co-singleton code spheres. A real A-code support contains at least `p-1` classes from each sphere.

The edge-by-edge private-foot slack theorem from `MATCHED_PRIVATE_FOOT_SLACK_AND_COMPLETE_ROW_QUADRATIC_EXCLUSION.md` depends only on this zero-signing matched core and the mandatory sphere support. It does **not** use that the triggering unmatched row itself is complete.

Therefore the same conclusion holds:

> **ONE-CODE QUADRATIC A-SLACK THEOREM.** If some unmatched row has
>
> `tau(Psi(K_y))=1`,
>
> then
>
> `L_A>=p(p-1)`.                                                `(OC4)`

Consequently the exact second-extremal exclusion region also transfers unchanged. Put

`c_lambda=ceil(lambda(lambda+2)/2)`.

If

> `(lambda+2)u <= p^2-(lambda+4)p+c_lambda+3`,                  `(OC5)`

then a near-full D2C graph containing **either** one-code row type satisfies

`m<=M(n)`.

Important special cases:

- `lambda=-1`: one-code rows are excluded above `M(n)` when
  `u<=p^2-3p+3`;
- `lambda=0`: excluded when
  `2u<=p^2-4p+3`;
- `lambda=1`: excluded when
  `3u<=p^2-5p+5`.

Thus the entire `tau=1` unmatched-row escape is pushed out of the genuinely near-full regime.

---

## 6. Strategic consequence

Previously the two one-code rows were handled by different mechanisms:

- complete row -> clique/private feet;
- clique-plus-isolate -> complementary U--U antipode/fan.

The fan statement remains true for the clique-plus-isolate row, but it is no longer the only pricing available. Both one-code cases now first trigger the same global matched-core collapse and the same quadratic lower bound

`L_A>=p(p-1)`.

This materially narrows the active row problem. Inside the quadratic region `(OC5)`, any hypothetical above-`M(n)` near-full configuration must have

> `tau(Psi(K_y))>=2` for every unmatched row `y`.                `(OC6)`

The next compact target is therefore the already-classified `tau<=2` family: complete-bipartite complements, star-plus-isolates, and two-centre complements. The best route is to determine which of these `tau=2` kernels force a bounded-switching-defect matched core and whether the new private-foot slack transfer can price their matched cliques edge-by-edge.

The published 2024 order-12/size-32 graph remains untouched: it is full-tight (`u=0`) and has no unmatched rows.

No all-order second-extremal theorem is claimed.
