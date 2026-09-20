# Residual-one k=2: universal residual-bar H-hub obstruction

Date: 2026-09-20

Status: **same-session conditional structural theorem**, under the corrected residual-one `k=2`, `J2=empty` interface. It uses the rooted B-layer separation guard and the preserved H--H certificate split; it does not use the superseded H--U private-foot chain.

## 1. Statement

Let `P=U_j^-` be the residual-bar U column. Suppose `z in P` is adjacent to every private matched head `h_i in H`.

Write `p_i` for the matched endpoint selected by `d` in private coordinate `i`, and `q_i` for the opposite endpoint selected by `bar d`.

> **THEOREM (PRIVATE-SPOKE OBSTRUCTION).** If `z` is H-universal, then `z` cannot be adjacent to `p_i` for any private coordinate `i`.

Equivalently, every private coordinate of `c(z)` is `bar d`; because `z in P` already has residual bit `bar d_j`,

> **`c(z)=bar d`.**                                      `(PS-1)`

If in addition H is complete, then for `t>=3` such a vertex cannot exist.

## 2. Raw criticality of `z p_i`

Assume for contradiction that `z p_i` is an edge for some private coordinate i. This edge lies wholly in the rooted B-layer. By the rooted layer-separation guard, a valid certificate witness cannot also lie in B: source and a B-witness would share the root. Thus the witness lies in A.

There are two possible singleton orientations.

### 2.1 Forward orientation from z

Suppose

`N(z) cap N(a)={p_i}`

with `a in A`.

The A-vertices adjacent to `p_i` are precisely of the following types in the residual-one repertoire.

- `Y=A_d`;
- `K=A_{d xor e_j}`;
- private heads `h_l` with `l!=i`.

A private head `h_l` cannot be the witness because z is H-universal, so `z h_l` is an edge while a certificate witness must be nonadjacent to its source.

If `a in Y`, then every H-vertex is adjacent to both z and a, because z is H-universal and the X--Y cut is complete. Since H is nonempty, the singleton equation fails.

If `a in K`, then both z and a are adjacent to the residual opposite endpoint `q_j`: z because `z in P`, and a because every K-code is `d xor e_j`. Thus `q_j` is a common neighbour distinct from the prescribed head `p_i`. Again the singleton equation fails.

So the forward orientation is impossible.

### 2.2 Reverse orientation from `p_i`

Now suppose

`N(p_i) cap N(a)={z}`.

The witness a must be adjacent to z and nonadjacent to `p_i`. Among A, the unique private-code type missing `p_i` is `h_i`; Y, K and every `h_l` with `l!=i` all select `p_i`.

Hence necessarily `a=h_i`. H-universality gives `z h_i in E`, as required for the singleton head. But every Y-vertex is adjacent both to `p_i` (its code is d) and to `h_i` (complete X--Y cut). Since `y>0` on the half-ray, there is an additional common neighbour besides z. Contradiction.

Both orientations fail. Therefore `z p_i` cannot be an edge for any private i, proving `(PS-1)`.

## 3. Complete-H corollary

Assume now H is complete. By `(PS-1)`, z has code `bar d`, so z is adjacent to every private opposite endpoint `q_i`.

The preserved H--H certificate split says an H--H edge `h_i h_l` is certified either

- by one of the private feet `q_i,q_l`, or
- by an endpoint-indexed U-witness;

and the total number of U-certified H--H edges is at most `u`.

But H-universality means z is adjacent to both endpoints `h_i,h_l`, while `z q_i` and `z q_l` are also edges. Hence z is an illicit second common neighbour for either private-foot orientation. No H--H edge can therefore use a private foot. Every H--H edge must be U-certified, giving

> **`binom(h,2)<=u`.**                                   `(PS-2)`

On the corrected half-ray `h=2t-1`, `u=t+1`; `(PS-2)` fails for every `t>=3`.

Thus:

> **COROLLARY.** On the corrected half-ray with `t>=3`, H complete forbids an H-universal residual-bar U-vertex. `(PS-3)`

## 4. Consequence for the Delta=2 hostile normal form

The abstract `Delta=2` saturation pattern in `ONE_CODE_R1_K2_HALF_RAY_SMALL_DEFICIT_CONCENTRATION.md` had

- `a=b=0`, `c0=2`, `g=1`, `M_H=0`;
- H complete;
- one residual-bar U-vertex z serving as the unique P-neighbour of **every** H-row.

That z is H-universal, so `(PS-3)` kills this candidate immediately for every `t>=3`.

Therefore the specific capacity-saturating `Delta=2` normal form is not compatible with raw private-spoke criticality. This does **not yet prove global `Delta>=3`**, because the other allocations of two deficit units `(a,b,c0)` remain to be classified.

## 5. Next exact task

Classify the remaining `Delta=2` allocations:

`(2,0,0)`, `(1,1,0)`, `(0,2,0)`, `(1,0,1)`, `(0,1,1)`.

The first is already impossible by shared-edge placement; the two `c0=0` cases are bounded by the local row inequality `s_i<=2+a_i+b_i`; the genuinely interesting cases are `(1,0,1)` and `(0,1,1)`, where one residual-plus head survives. Apply the same private-spoke obstruction to whichever residual-bar vertices must carry the saturated-row P-neighbour load, and combine with the collective reverse-witness H-degree bound.

Upstream caveat unchanged: bounded actual-D2C regression has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.