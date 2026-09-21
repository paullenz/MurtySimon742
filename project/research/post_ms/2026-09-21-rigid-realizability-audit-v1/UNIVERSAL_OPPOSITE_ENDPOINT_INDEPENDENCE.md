# Universal opposite endpoints are independent: collapse of the matched-leaf escape

Date: 2026-09-21

Status: raw D2C criticality theorem for realizability of a rigid complete one-code cut. This strengthens `UNIVERSAL_BOUNDARY_U_SLACK_BILL.md` by showing that the matched-leaf escape is available only in an isolated two-coordinate configuration.

## 1. Rooted B-edge lemma

### Lemma 1.1 — two A-anticomplete rooted neighbours cannot be adjacent

Let `v` be the root, `B=N(v)`, `A=V\N[v]`. If `r,s in B` satisfy

`N_A(r)=N_A(s)=empty`,

then

`rs notin E(G)`.

### Proof

Suppose `rs` is an edge. It lies in the triangle `r-v-s`. Raw triangle-edge criticality therefore requires one of

`N(r) cap N(w)={s}`

or

`N(s) cap N(w)={r}`

for some witness `w`.

A witness in B is impossible because it shares the root v with the B-source. The root itself is adjacent to the source. A witness in A is impossible because the head (`r` or `s`) is A-anticomplete. No location remains. Contradiction. `square`

This elementary lemma is independent of Hall selection, A-edge certificate policy and source-tuple capacity.

## 2. Universal coordinates form a clique in the relative row graph

In the rigid complete one-code cut `Y=A_d`, let

`C=C(d,X)={j: every x in X has c(x)_j=d_j}`.

For every `j in C`, the opposite matched endpoint

`r_j=q_j^{1-d_j}`

is A-anticomplete: Y selects `q_j^{d_j}` by definition, and universality says X does the same.

Take distinct `j,l in C`. Tight-pair transversality says `r_j` is adjacent to exactly one endpoint of fibre l. By Lemma 1.1 it cannot be adjacent to the A-anticomplete endpoint `r_l=q_l^{1-d_l}`. Hence it must be adjacent to `q_l^{d_l}`.

By definition of the relative row graph `R_d`,

`j~_d l`.

Therefore:

### Theorem 2.1 — universal-row clique

`R_d[C]` is complete.                                           `(2.1)`

This turns a purely A-code agreement condition into a rigid statement about the physical matched layer.

## 3. Collapse of matched-forward leaves

The boundary-code-edge trichotomy showed that a matched-forward witness for a universal head `i in C` must be an opposite endpoint `r_j` with

`j in C`, `N_{R_d}(j)={i}`.

But Theorem 2.1 gives

`deg_{R_d[C]}(j)=|C|-1`.

Hence:

### Corollary 3.1

If `|C|>=3`, **no universal coordinate has matched-forward support**.

If `|C|=1`, matched-forward support is also impossible because the witness coordinate must differ from the head coordinate and lie in C.

If `|C|=2`, say `C={i,j}`, matched-forward support is possible only if the relevant witness coordinate is a global leaf. Both universal coordinates can be covered by matched-forward witnesses only when `C` is an isolated `K_2` component of `R_d`.

Thus the only fully matched escape from universal-coordinate U-slack is an isolated two-coordinate block.

## 4. Strengthened universal U-slack bill

Combine Corollary 3.1 with the unmatched-witness slack theorem.

Assume `p>=y`.

- If `|C|=1` or `|C|>=3`, every universal coordinate must use U-forward witnesses for every outside source, so

  `E_U >= p|C|`.                                            `(4.1)`

- If `|C|=2`, either the two coordinates form the isolated matched `K_2` escape, or at least one coordinate pays the U-forward bill. More precisely, if `m_C` is the number of the two heads actually supplied by eligible global matched leaves, then

  `E_U >= p(2-m_C)`, `0<=m_C<=2`,                          `(4.2)`

  and `m_C=2` requires an isolated `K_2` in `R_d`.

Population also gives `|C|<=u` whenever `|C|!=2` and C is nonempty, because the required U-forward code classes are distinct.

### Corollary 4.1 — unmatched-free case

If `u=0`, a nonempty universal set is possible only in the exceptional form

`|C|=2`

with `R_d[C]` an isolated `K_2`.

This strictly strengthens the earlier parity-only observation.

## 5. Half-ray consequence

On the corrected half-ray `p=2t`, `y=t`, any universal set of size other than two costs

`E_U >= 2t|C|`.

Thus a linear universal block is automatically quadratically expensive. The only zero-U-slack matched escape is concentrated into at most two universal coordinates and has a completely explicit physical matched-row geometry.

## 6. Significance

The bounded graph regression had found no positive rigid complete pair-family cut. The present theorem explains another reason such cuts are difficult to realize: the apparent matched-forward escape from the boundary trichotomy is almost entirely illusory. Once the opposite endpoints are recognized as A-anticomplete, raw criticality forces them to be independent, which makes the relative row graph complete on the universal coordinates and destroys degree-one witness leaves except for an isolated two-coordinate block.

The next useful question is therefore concentrated on the non-universal coordinates: after at most the isolated `K_2` exception, they must be paid for by one-match U witnesses or large reverse gamma classes.
