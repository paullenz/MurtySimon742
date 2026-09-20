# One-witness all-R polarization is empty

Date: 2026-09-20

Status: **internal conditional structural closure** inside the independently audited first-strict unloaded branch. This note closes the entire `m=1` all-R polarization, not merely the later Hamming-equality subarm. The rigid complete-cut realizability caveat remains unchanged.

## 1. Setup

Use the audited one-witness polarization theorem. In the all-R case:

- every buffer neighbour in `X'=X\{a_0}` has one common tight code `C`;
- the unique selected outside witness `z in U_o` has code `bar C`;
- `z a_0 in E`, `N_A(z)={a_0}`;
- for every `x in X'`, `N(x) cap N(z)={b}`;
- writing supports relative to d, `S_0={i:c(a_0)_i!=d_i}` and `S_C={i:C_i!=d_i}`, Type R gives `empty != S_0 subseteq S_C`;
- `I_C=[p]\S_C` is nonempty because `C!=bar d`;
- for every `i in I_C`, if `q_i` is the matched endpoint selected by `bar d`, the reverse funnel gives
  `N(q_i) cap N(a_0)={z}`.

The unloaded assumptions also include `e(Y)=0`, `d_Y(b)=0`, and `X--Y` complete.

## 2. Core exclusion is valid on the whole all-R arm

### Lemma 2.1

`a_0` is anticomplete to `W_0`.

### Proof

Choose any `i in I_C`. Every core vertex `w in W_0` has code `bar d`, hence `wq_i in E`. If `wa_0` were also an edge, w would belong to `N(q_i) cap N(a_0)`, contradicting the graph-fixed singleton `{z}`. `square`

Thus the k injective core heads all lie in `X'`, so `k<=x-1` and `g=x-k>=1` throughout the all-R polarization. This generalizes the later equality-arm core exclusion.

## 3. The edge `a_0y` has no raw criticality certificate

Fix arbitrary `y in Y`. The edge `a_0y` exists because `X--Y` is complete. It lies in a triangle because `a_0` and y agree in every coordinate outside the nonempty proper support `S_0`.

Apply raw triangle-edge criticality. We exhaust both orientations.

### 3.1 Source `a_0`, head y

A witness must be nonadjacent to `a_0`, adjacent to y, and have singleton common neighbourhood with `a_0` equal to `{y}`.

**Matched witness.** Such a witness must be the d-selected endpoint in some coordinate `i in S_0`. Since `S_0 subseteq S_C`, C differs from d there, so `z=bar C` agrees with d at i. Hence z is adjacent both to that matched endpoint and to `a_0`; z is an extra common neighbour distinct from y. Impossible.

**A-witness.** A Y-vertex other than y is not adjacent to y because `e(Y)=0`. A vertex `x in X'` is adjacent to y and is nonadjacent to `a_0` in the all-R case, but `a_0` and x choose the same non-d matched endpoint in every coordinate of `S_0` (binary codes and `S_0 subseteq S_C`). Thus they have a tight matched common neighbour distinct from y. Impossible.

**U-witness.** The buffer is not adjacent to y. Every core vertex has code `bar d`; if it were adjacent to y, it would still share with `a_0` every matched endpoint indexed by `S_0`, so it cannot be a singleton witness. By `BUFFER_UO_Y_ANTICOMPLETENESS.md`, no vertex of `U_o` is adjacent to y. Impossible.

The root is not adjacent to the A-head y. Thus the orientation `a_0 -> y` is impossible.

### 3.2 Source y, head `a_0`

A witness must be nonadjacent to y, adjacent to `a_0`, and have singleton common neighbourhood with y equal to `{a_0}`.

**Matched witness.** It must be the `a_0`-selected endpoint in some `i in S_0`. Since `S_0 subseteq S_C`, every vertex of `X'` selects the same endpoint. Every vertex of `X'` is also adjacent to y. Hence the common neighbourhood contains all `x-1>=2` vertices of `X'`, not just `a_0`. Impossible.

**A-witness.** Every X-vertex is adjacent to y, so it cannot be a nonadjacent witness. Any other Y-vertex is nonadjacent to y and adjacent to `a_0`, but two Y-vertices have the same code d and therefore share all p tight matched neighbours (and in fact all X). Impossible.

**U-witness.** The buffer and every core vertex are nonadjacent to `a_0` by the unique hole and Lemma 2.1. The distinguished z is adjacent to `a_0` and nonadjacent to Y, but y and z share a matched endpoint in every coordinate of the nonempty set `S_C` because `z=bar C` agrees with d there. So z cannot witness.

Now take any `w in U_o\{z}` adjacent to `a_0`. Choose `i in I_C`, which is nonempty. The fixed reverse-funnel identity `N(q_i) cap N(a_0)={z}` forces `wq_i` to be a nonedge. Since `q_i` is the `bar d` endpoint in fibre i, w must select the d endpoint in that tight fibre. The Y-source y selects the same d endpoint. Thus y and w have a matched common neighbour distinct from `a_0`. Impossible.

The root is not adjacent to the A-head. Hence the reverse orientation is impossible.

Both orientations fail, contradicting raw D2C criticality of the triangle edge `a_0y`.

## 4. Closure theorem

> **THEOREM — the `m=1` all-R polarization is empty.**
>
> No graph satisfying the audited first-strict unloaded hypotheses can realize the one-witness all-R case.

This is strictly upstream of the later all-R equality-pinch/grid/resource programme. Therefore the all-R equality pinch, the exact d/J optimization, the residual certificate grid and its diagnostics remain valid conditional mathematics on a parent geometry now proved empty; they are no longer a live realizability branch.

## 5. Immediate one-witness consequence

The independently audited polarization theorem says `m=1` is either all-F or all-R. The all-R arm is now empty. Hence:

> **every surviving one-witness first-strict geometry is all-F.**

In particular the existing exact all-F Hamming-slot bill applies unconditionally within `m=1`:

`r >= x + y[p-1-floor((p-2)/x)]`,

and for `p>=3`,

> `r>=a+y`.

The old statement “all one-witness geometries except one literal all-R equality arm pay `+y`” therefore strengthens to “all surviving one-witness geometries pay `+y`.”