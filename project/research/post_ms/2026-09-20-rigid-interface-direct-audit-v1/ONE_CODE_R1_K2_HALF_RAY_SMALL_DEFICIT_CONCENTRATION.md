# Residual-one k=2 half-ray: small-deficit concentration normal form

Date: 2026-09-20

Status: **same-session conditional structural refinement / hostile model**, downstream of the corrected H--U B-layer capacity theorem and `ONE_CODE_R1_K2_HALF_RAY_HU_DEFICIT_TWO_BARRIER.md`. No graph-realizability claim is made.

## 1. Local deficit accounting

On the corrected half-ray put, for each `h_i in H`,

- `m_i` = missing H-degree;
- `r_i^q` = number of chosen reverse private-`q_l` certificates sourced at `h_i`;
- `r_i^j in {0,1}` = whether the chosen certificate partition uses the residual `q_j` slot at `h_i`;
- `s_i` = number of H--U edges sourced/assigned to the shared U-resource block.

Define local capacity deficits

`a_i=m_i-r_i^q`, `b_i=1-r_i^j`.

The H--U edge partition gives

`d_U(h_i)=r_i^q+r_i^j+s_i`,

while exact half-ray degree bookkeeping gives

`d_U(h_i)=m_i+3-epsilon_i`.

Therefore

> **`epsilon_i=2+a_i+b_i-s_i`.**                         `(SD-1)`

In particular

> **`s_i<=2+a_i+b_i`.**                                  `(SD-2)`

Let `B={i:b_i=1}` and `b=|B|`; let `a=sum a_i`. Then

> **`sum_{i in B}s_i <= 3b+a`.**                         `(SD-3)`

## 2. Most shared load lies on residual-saturated rows

Globally

`S=u-2-c0=t-1-c0`,

and `Delta=a+b+c0`. Hence the number `T` of shared-block edges on residual-saturated rows satisfies

> **`T >= S-(3b+a)`**
>
> **`=t-1-Delta-2b`**
>
> **`>=t-1-3Delta`.**                                    `(SD-4)`

Thus whenever `Delta=o(t)`, all but `o(t)` of the linear shared H--U load lies on rows whose `q_j` slot is saturated.

## 3. Those edges must be reverse-U through few residual-plus heads

Let

`P=U_j^-`, `g=|U\P|`.

The residual-column theorem gives `g<=c0<=Delta`. On a residual-saturated row the unique edge with head in `P` is already assigned to `R_j`; every other chosen shared edge on that row therefore has its U-head outside `P`.

Among the shared mechanisms, triangle-free endpoints and U-sourced A_X/Y arms use residual-bar U resources as their H--U endpoint/source. Hence a shared edge on a residual-saturated row with head outside `P` must be a **reverse-U-certified H--U edge**.

Consequently at least `T` reverse-U edges are concentrated through at most `g<=Delta` residual-plus U-heads.

For each such reverse-U edge from source `h_i`, the witness lies in the distinct endpoint-indexed class

`U_{bar d xor e_i}`.

The shared-resource injection makes these witnesses physically distinct over the `T` assigned edges. A fixed source row can contribute at most `g` such edges, one for each outside head. Therefore the source multiplicity is at most `g`.

## 4. Collective H-sparsity of the reverse witnesses

For a reverse-U certificate

`N(h_i) cap N(w)={r}`,

where `r` is the U-head, the witness `w` is nonadjacent to `h_i`. Moreover every H-neighbour of `h_i` must also be nonadjacent to `w`, or it would be an additional common neighbour. Hence

> **`d_H(w)<=m_i`.**                                     `(SD-5)`

Summing over the `T` distinct reverse witnesses and using source multiplicity at most `g`,

> **`sum_w d_H(w) <= g sum_i m_i = 2g M_H <= 2 Delta M_H`.** `(SD-6)`

Thus a small H--U capacity deficit forces a very explicit geometry:

- only `O(Delta)` U-vertices lie outside the residual-bar column;
- all but `O(Delta)` H rows have exactly one residual-bar U-neighbour;
- `t-O(Delta)` shared edges are reverse-U edges through those few outside heads;
- their witnesses are distinct endpoint-indexed vertices;
- collectively those witnesses have H-degree at most `2 Delta M_H`.

This is the correct concentration normal form to combine with U-sparsity and H--H criticality.

## 5. The Delta=2 boundary is not killed by H--U capacity alone

The `Delta>=2` theorem is locally sharp at the level of the corrected H--U capacity equations. The following hostile abstract normal form is consistent with all equations in this note and with the corrected H--U capacity decomposition; it is **not** asserted to be a D2C graph.

Take

`a=b=0`, `c0=2`, `g=1`, `M_H=0`.

Then H is complete, all H rows are residual-saturated, and

`S=t-3`.

Let

- `t_*` be the unique residual-plus U-vertex;
- `z in P` be the unique residual-bar neighbour of every H-row;
- `w_i` for `t-3` distinct source indices be endpoint-indexed reverse-U witnesses, each H-anticomplete;
- the two selected witnesses `W_s`, also H-anticomplete.

The U-count is exact:

`1 + 1 + (t-3) + 2 = t+1=u`.

Each chosen shared edge is `h_i t_*`, reverse-U-certified by its distinct `w_i`; every H-row uses `h_i z` as its residual-`q_j` edge. This realizes the H--U capacity counts with `Delta=2` and

`L_H=3t+1`.

## 6. Hostile replay against the preserved H--H split

The preserved H--H theorem says a dense H edge is certified either by a private foot or by an endpoint-indexed U witness, with only O(p) total U-certified H--H capacity. The hostile `Delta=2` normal form is not immediately contradicted by that theorem.

Indeed one may choose the universal residual-bar H-neighbour `z` to have code `d xor e_j`. Then z selects the d-endpoint in every private coordinate and therefore does not see any private foot `q_i`. All endpoint-indexed witnesses `w_i` and both selected witnesses are H-anticomplete. Hence the private-foot singleton equations for the complete H layer are not automatically spoiled by the U population described above.

So merely combining `H` complete with the existing H--H private-foot/U split does **not** yet improve the deficit-two barrier. This is an important negative result: the next proof must use an additional raw-criticality or diameter constraint involving the universal residual-bar H-neighbour z, the residual-plus head `t_*`, or the matched/private coordinates; another capacity-only relaxation is unlikely to suffice.

## 7. Next target

The sharp local hostile form suggests the following order.

1. Audit the literal `Delta=2` geometry under raw criticality of the edges `h_i z`, `h_i t_*`, and any forced edges incident with `z` or `t_*`.
2. Retain the exact codes: `z` can evade all private feet only by being private-d across almost every private coordinate, naturally pushing it toward code `d xor e_j`; test what residual-hub/private-spoke criticality then forces on its U/Y/K neighbourhood.
3. If `Delta=2` survives, generalize to fixed `Delta=d`: the concentration theorem `(SD-4)--(SD-6)` gives a finite-number-of-heads / many-distinct-witnesses template that should be amenable to a direct collision argument.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.