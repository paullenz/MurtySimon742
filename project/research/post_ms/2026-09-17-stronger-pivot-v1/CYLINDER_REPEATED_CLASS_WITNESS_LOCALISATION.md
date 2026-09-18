# Cylinder repeated-class witness localisation

**Status:** corrective structural theorem / internal checkpoint, 18 September 2026.

This note repairs an important scope issue in the preceding cylinder-criticality discussion. The beta-cylinder pigeonhole theorem guarantees a **repeated code class inside the central cylinder**, but it does not guarantee that this class has exactly the centre's Boolean code. The same-code criticality lemma therefore cannot simply be applied to the whole pigeonholed class.

The correct statement is stronger in a different direction: a repeated cylinder class differs from the centre only on beta-deficit coordinates, and D2C criticality localises every possible matched-B exceptional witness to those differing coordinates. Thus the gap is repairable, but the matched-B exception must be kept explicitly.

The published order-12 `X_3` hostile control has `u=0` and is unaffected.

## 1. Setup

Let the tight fibres be

`P_i={q_i^0,q_i^1}`, `i=1,...,p`.

Every vertex of `A union U` has a Boolean code `c` recording its chosen/adjacent endpoint in every tight fibre.

Fix `x in A` with beta target set `I_x`, beta load

`ell_x=|I_x|`,

and deficit

`k_x=p-ell_x`.

The preserved beta-cylinder theorem says that all A-neighbours of `x` lie in the central cylinder determined by `c(x)` on the targeted coordinates `I_x`. Consequently some full code class `R subseteq N_A(x)` has

`|R|>=ceil((p-epsilon_x)_+/2^{k_x})`,

and every `z in R` has one common code `c_R` satisfying

`c_R|_{I_x}=c(x)|_{I_x}`.

Put

`D={i:c_R(i)!=c(x)(i)}`.

Then

> `D subseteq [p]\I_x`, and therefore `|D|<=k_x`.         `(CR1)`

The earlier note implicitly specialised to `D=emptyset`. The statements below treat arbitrary `D`.

---

## 2. Critical edge witness trichotomy for near-code A-edges

Assume `ell_x>=1`, so every `z in R` shares at least one matched-B neighbour with `x`. Hence deleting `xz` does not separate `x` and `z` beyond distance two. D2C criticality therefore supplies one of the standard two orientations:

- **outgoing:** a vertex `w` with `N(x) cap N(w)={z}`;
- **incoming:** a vertex `w` with `N(z) cap N(w)={x}`.

The location of `w` is almost completely determined.

### Lemma 2.1 (unmatched/A witnesses are complementary to the source)

If the critical witness `w` lies in `A union U`, then its Boolean code is the complement of the source code:

- in the outgoing orientation, `c(w)=bar c(x)`;
- in the incoming orientation, `c(w)=bar c_R`.

### Proof

If `w` shared any matched-B neighbour with the source, that matched endpoint would be a second common neighbour in the relevant unique-common-neighbour pair. Since both vertices choose exactly one endpoint in every tight fibre, `w` must choose the opposite endpoint in every coordinate.

### Lemma 2.2 (matched-B exceptional witnesses live only in differing fibres)

Suppose the witness is a matched endpoint `w=q_i^s`.

For an outgoing orientation `N(x) cap N(w)={z}`:

1. `i in D`;
2. `w` is the endpoint chosen by `c_R` and not by `c(x)` in fibre `i`;
3. for every `j!=i`, the physical B-edge from `w` into fibre `P_j` goes to the endpoint opposite `c(x)(j)`.

For an incoming orientation `N(z) cap N(w)={x}`:

1. `i in D`;
2. `w` is the endpoint chosen by `c(x)` and not by `c_R` in fibre `i`;
3. for every `j!=i`, the physical B-edge from `w` into `P_j` goes to the endpoint opposite `c_R(j)`.

### Proof

In the outgoing case, `z` is adjacent to `w` while `x` is not, so the two codes differ in coordinate `i`, proving `i in D` and item 2. If the B-edge from `w` to some other fibre `P_j` landed at the endpoint chosen by `x`, that endpoint would be adjacent to both `x` and `w`, contradicting `N(x) cap N(w)={z}`. The incoming case is symmetric with source `z` and head `x`.

Thus a matched-B critical witness is not arbitrary: it is a row-complement endpoint attached to one of the at most `k_x` deficit coordinates.

---

## 3. Repetition kills matched-B witnesses on the outgoing side

The repeated-class pigeonhole now becomes useful.

### Theorem 3.1 (no matched outgoing witness for a repeated class)

If `|R|>=2`, then **no** edge `xz`, `z in R`, can use a matched-B witness in the outgoing orientation.

### Proof

Let `w=q_i^s` be an outgoing matched witness. Since all vertices of `R` have the same code `c_R` and `w` is the endpoint selected by that code in fibre `i`, `w` is adjacent to every vertex of `R`. The centre `x` is also adjacent to every vertex of `R` by definition. Hence

`R subseteq N(x) cap N(w)`.

If `|R|>=2`, this contradicts the required equality `N(x) cap N(w)={z}`.

Therefore every outgoing critical witness for the repeated class lies in `A union U`, has code `bar c(x)`, and is charged by the preserved unique-common-neighbour slack identity.

Moreover the outgoing witnesses are pairwise distinct, exactly as in the same-code case.

---

## 4. The only uncharged escape is a bounded set of incoming matched feet

For incoming orientations, a matched-B witness can be reused, but Lemma 2.2 shows that there are at most `|D|<=k_x` possible matched endpoints.

Thus every repeated cylinder class `R` admits the exact decomposition

> `R = O dotcup I_AU dotcup I_P`,                         `(CR2)`

where

- every `z in O` has a distinct outgoing witness in `A union U` of code `bar c(x)`;
- every `z in I_AU` has an incoming witness in `A union U` of code `bar c_R`;
- every `z in I_P` has an incoming witness among at most `|D|<=k_x` matched endpoints, one in each eligible differing fibre and satisfying the row-complement condition of Lemma 2.2.

The first two pieces are exactly in the scorecard-priced world of `UNIQUE_COMMON_NEIGHBOR_SLACK_AND_CYLINDER_CRITICALITY.md`. The third is the only additional escape created by `c_R!=c(x)`.

### Corollary 4.1 (bounded matched-foot support)

If the repeated class uses `g_P` distinct matched-B incoming feet, then

> `g_P<=|D|<=k_x`.                                        `(CR3)`

Hence a bounded-deficit cylinder has only a bounded number of matched-B foot types available, regardless of the size of the repeated class.

---

## 5. Reused matched feet still force density, but their slack is not yet in the scorecard

Let one eligible matched endpoint `w` certify an incoming source set

`S_w subseteq I_P`,

so

`N(z) cap N(w)={x}` for every `z in S_w`.

The unique-common-neighbour hole identity itself does **not** require `w in A union U`. Put

`epsilon_w=b-d(w)`.

Then for every `z in S_w`,

`|H(z,w)|=epsilon_z+epsilon_w-(lambda+1)`.

Because `w` is nonadjacent to every vertex of the code class `R`, every non-neighbour of `z` inside `S_w` is a hole. Therefore the common-foot density estimate extends verbatim:

> `d_overline{G[S_w]}(z)`
> `<=epsilon_z+epsilon_w-(lambda+1)`.                     `(CR4)`

and

> `omega(G[S_w])`
> `>=ceil(|S_w|^2/(|S_w|+sum_{z in S_w}[epsilon_z+epsilon_w-(lambda+1)]))`. `(CR5)`

The important trust-boundary point is that `epsilon_w` is a matched-endpoint slack and is **not itself part of `E_U+L_A`**. Any aggregate cylinder theorem must therefore either

1. convert these at-most-`k_x` matched-foot slacks into the existing beta endpoint-slack payments `T_i`, or
2. show that heavy reuse of the few matched feet creates a forbidden/expensive row-complement configuration.

It is not legitimate simply to count `epsilon_w` in the A/U scorecard.

---

## 6. Corrected relationship with the same-code clique theorem

If `D=emptyset`, then `c_R=c(x)`, the matched-foot escape disappears completely, and the full same-code criticality theory applies. In particular the new global same-code clique payment

`E_U+L_A>=ceil(r(lambda+1)/2)`

holds for every clique of order `r` inside `R`.

If `D!=emptyset`, that theorem still applies to cliques **within one code class whose edges are being priced relative to sources of the same code**, but it must not be inferred solely from the cylinder pigeonhole centre `x`.

This distinction corrects the overly broad wording in the previous live-state description that D2C criticality had already priced an arbitrary pigeonholed cylinder class exactly as a same-code class of the centre.

---

## 7. Strategic consequence

The local cylinder route is now cleaner rather than weaker.

For a low-deficit centre `x`, the pigeonholed repeated class differs from `c(x)` in at most `k_x` coordinates. If it is genuinely repeated (`|R|>=2`):

- all outgoing criticality is forced into A/U complementary witnesses and therefore pays the existing scorecard slack machinery;
- all A/U incoming criticality is likewise complementary-code controlled;
- the only non-scorecard escape consists of at most `k_x` matched endpoints, each with a rigid row-complement signature;
- reuse of any such endpoint forces the incoming source block dense by `(CR4)--(CR5)`.

The next cylinder theorem should therefore target **matched-foot reuse across many low-deficit centres**. Since each centre has only `k_x` such exceptional feet, an overlap/capacity argument can plausibly convert repeated use into endpoint-slack payment or a rigid signed-row obstruction.

This is a more precise target than the previous informal request to bound arbitrary complementary near-clique reuse.

## 8. Trust boundary

- This note is partly corrective: it narrows an implicit scope leap in the previous cylinder discussion.
- The beta-cylinder pigeonhole itself remains valid.
- Lemmas 2.1--2.2 and Theorem 3.1 are hand consequences of the tight-fibre transversal structure and D2C critical witnesses.
- `(CR4)--(CR5)` use the exact unique-common-neighbour hole identity, now with a matched-B foot.
- No aggregate closure is claimed.
- `X_3` has `u=0` and is unaffected.
