# Shared-core endpoint: selected-witness separation

Date: 2026-09-19

Status: physical refinement of `SHARED_CORE_R22_PAIR_PINCH.md`, under the same rigid one-code / minimal-reservoir / `R2+R2`, `h=1,c=2,d0=2`, `k>=3` hypotheses. Conditional structural mathematics only; not graph-realizability evidence.

## 1. Exact/near pair regime

Stay on the deep pair arm `D<=-6`. Let

`s_P=(C0-sigma_P)-(p^2+M-k-8)`

be the slack above the exact shared-core pair minimum. The preceding theorem proved that if `s_P<=1`, then

`[D+2Delta]_+ + (Jmax-J) <= s_P`,

where

`Jmax=2k+8`.

Therefore

> `Jmax-J<=1`.                                           `(1)`

The two active repeated-core channels and the three bidirected singleton-type channels can now be read as literal physical adjacencies rather than only an incidence count.

## 2. Unit I — both defect witnesses miss the common core witness

Let the two radius-two defect heads be `h_1,h_2`, with their selected outside witnesses `z_1,z_2`. Let `z_*` be the common selected outside witness serving every core head in `H_0`.

Because `d0=2`, `z_*` is adjacent to both defect heads. Each active core channel has at most `k+1` incidences:

- the already-present adjacency `z_*--h_i`;
- at most `k` reverse adjacencies from `z_i` to the `k` core heads.

If one of `z_1,z_2` had no core-head neighbour, at least `k>=3` incidences would be missing from `Jmax`, contradicting `(1)`. Thus each `z_i` is adjacent to at least one core head `x_i in H_0`.

The defining selected-witness certificate for the core head is

`N(x_i) cap N(z_*)={b}`.

Since `z_i~x_i`, adjacency `z_i~z_*` would make `z_i` a second common neighbour besides `b`. Hence

> **`z_1 z_* notin E` and `z_2 z_* notin E`.**           `(2)`

The `g+1` selected outside witnesses are physically distinct in the minimal reservoir, so these are two distinct `z_*--(U_o\{z_*})` nonedges. Therefore

> **`M>=2`.**                                             `(M2)`

At exact pair equality (`s_P=0`), in fact each defect witness is adjacent to all `k` core heads. At one unit of pair slack, at least `2k-1` of the `2k` reverse core incidences are present.

## 3. Unit II — every active singleton channel separates its two witnesses

Consider any bidirected support channel between two singleton head classes `h_s,h_t`, with selected outside witnesses `z_s,z_t`. One direction active means, say, `z_s~h_t`.

The selected certificate for `h_t` gives

`N(h_t) cap N(z_t)={b}`.

If `z_s~z_t`, then `z_s` would be another common neighbour of `h_t,z_t`, contradiction. Thus one active direction already forces

> **`z_s z_t notin E`.**                                  `(3)`

Under `(1)`, none of the three bidirected channels can be completely inactive: losing both directions on one channel would cost two incidences. Hence all three associated selected-witness pairs are nonedges.

In the shared-core topology these are:

1. the two defect witnesses `z_1,z_2`;
2. `z_1` and the witness serving the private radius-one class on the first defect's private coordinate;
3. `z_2` and the witness serving the private radius-one class on the second defect's private coordinate.

The minimal-reservoir witness distinctness makes these three physical U-o nonedges distinct.

## 4. Unit III — sharpened physical q ceiling

The preserved generic minimal-reservoir ceiling is

`q <= binom(u,2)-binom(k+1,2)-k-M`.

The three witness-witness nonedges from Section 3 are not among:

- the `binom(k+1,2)` missing pairs internal to the independent `U_-` block;
- the `k` forced `z_*--W_0` nonedges;
- the `M` missing `z_*--(U_o\{z_*})` pairs.

They therefore sharpen the exact/near endpoint ceiling to

> **`q <= binom(u,2)-binom(k+1,2)-k-M-3`.**              `(Q-3)`

Together with `(M2)`, the pair endpoint now carries at least five specifically located U-pair nonedges beyond the independent `U_-` block / `z_*--W_0` baseline: two incident with `z_*` and three among the selected singleton witnesses.

## 5. Unit IV — bounded replay

Replaying the same bounded `t=1` no-E1 diagnostic from the preceding note:

- exact-or-one-unit shared-core endpoint states before `(M2)`: `49`;
- after the necessary `M>=2` condition: **`39`**;
- exact pair-equality states before `(M2)`: `48`;
- after `M>=2`: **`38`**.

The exact-or-one-unit by-k distribution becomes

- `k=3:15`;
- `k=4:9`;
- `k=5:11`;
- `k=6:4`.

The exact-equality distribution is

- `k=3:15`;
- `k=4:9`;
- `k=5:11`;
- `k=6:3`.

Applying the additional `-3` in `(Q-3)` to the existing physical rooted upper bound causes no further state closure on this bounded box. That negative result is informative: after the newly forced witness separation is installed, the remaining rooted `q/E_U` ceiling is still too loose for another scalar q correction alone to finish the endpoint family.

These are abstract parameter states, not graph counts or realizability evidence.

## 6. Consequence

The exact/near shared-core endpoint is now a more literal graph geometry:

- both defect witnesses meet core heads and therefore miss `z_*`;
- all three support channels force pairwise nonadjacency of their selected outside witnesses;
- `M>=2`;
- q loses three additional physical U-o edges;
- every surviving X-edge remains positive-Hamming by the preceding endpoint theorem.

The next useful move is not another scalar q subtraction. It is to use the *locations* of these five forced U-pair nonedges in the criticality/Hall ledger, especially the three nonedges among selected H_M witnesses, to seek additional A/U holes or unmatched slack. The bounded replay shows that merely subtracting their count from q does not yet pinch the residual budget tightly enough.
