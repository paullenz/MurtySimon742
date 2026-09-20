# Residual-one orientation covering and escape-slack theorem

Date: 2026-09-20

Status: **same-session candidate theorem**, conditional on the rigid one-code residual-one interface and the hostile-replayed hub/orientation package. No finite scan is used as proof. The 20 September audit gate remains binding, including `X_3` and the zero-positive actual-D2C rigid-fixture caveat.

## 1. Setup

Retain the notation of `ONE_CODE_R1_PHYSICAL_REPRICE_AND_PRIVATE_ORIENTATION.md`.

- `K` is the set of `k` U-certified heads;
- `W_s={z_h:h in K}` are the selected witnesses;
- `H={h_i:i in I}` are the `m=p-1` matched-covered heads;
- `I=J1 disjoint_union J2`, where
  - `i in J1` means `c(h_i)=d xor e_i`,
  - `i in J2` means `c(h_i)=d xor e_i xor e_j`;
- `E=U\W_s`, with `|E|=c-1`;
- for every `(h,i)` the private spoke `z_h q_i` has orientation F or R:
  - F: `N(z_h) cap N(h_i)={q_i}`;
  - R: `N(q_i) cap N(h)={z_h}`.

The predecessor theorem already proves that every `i in J2` is forced R for every `h in K`, and if an escape vertex touches some `q_i`, `i in J2`, then it is anticomplete to K.

## 2. Radius-one rectangle forcing

Fix an escape vertex `w in E`. Define four index sets on the radius-one part:

- `A_w={h in K: wh in E(G)}`;
- `B_w={h in K: wz_h in E(G)}`;
- `S_w={i in J1: wq_i in E(G)}`;
- `T_w={i in J1: wh_i in E(G)}`.

For every `h in A_w` and `i in S_w`, orientation R is impossible: `w` would be a second common neighbour of `q_i` and `h` besides `z_h`. Hence the cell `(h,i)` is forced F.

For every `h in B_w` and `i in T_w`, orientation F is impossible: `w` would be a second common neighbour of `z_h` and `h_i` besides `q_i`. Hence the cell `(h,i)` is forced R.

Therefore the two forced rectangles cannot intersect:

> **`(A_w cap B_w) x (S_w cap T_w)=empty`.**             `(OC-RECT)`

Equivalently, for every escape vertex,

> **either `A_w cap B_w=empty` or `S_w cap T_w=empty`.** `(OC-DICH)`

This is a physical covering theorem for the radius-one orientation matrix, not a scalar relaxation.

## 3. Per-escape slack floor from J1

Write `a=|A_w|`, `b=|B_w|`, `sigma=|S_w|`, `tau=|T_w|`, and `j1=|J1|`.

If `A_w cap B_w=empty`, then `a+b<=k`. Among the `2k` possible pairs from `w` to `K union W_s`, at least `k` are missing.

If `S_w cap T_w=empty`, then `sigma+tau<=j1`. The escape vertex misses `j1-sigma` private endpoints `q_i` and `j1-tau` matched heads `h_i`, for at least

`2j1-(sigma+tau)>=j1`

missing pairs.

All these missing pairs lie inside the degree universe counted by the exact U-slack identity. Hence

> **`epsilon_w >= min(k,j1)` for every `w in E`.**       `(OC-J1)`

No summation or injectivity assumption is needed: this is vertexwise.

## 4. Combining J1 with the radius-two theorem

Let `j2=|J2|`, so `j1+j2=p-1`.

If `w` is `J2`-bad, meaning `wq_i` is an edge for some `i in J2`, predecessor `(OM-BAD0)` gives `E(w,K)=empty`, hence immediately

`epsilon_w>=k`.

If `w` is not `J2`-bad, then it misses every `q_i`, `i in J2`. These `j2` missing U-pairs are disjoint from the J1 pairs used in `(OC-J1)`, so

`epsilon_w>=min(k,j1)+j2 >= min(k,j1+j2)`.

Thus both cases give the composition-free bound

> **`epsilon_w >= min(k,p-1)` for every escape `w in E`.** `(OC-ESC)`

Since `|E|=c-1`, the whole escape reservoir pays

> **`E_E >= (c-1) min(k,p-1)`.**                         `(OC-RES)`

This is the main theorem of the note. It removes the need to decide whether the matched layer is radius-one-dominant or radius-two-dominant before pricing the physical escape reservoir.

## 5. Strengthened residual-one score gate

The hostile-replayed predecessor gives

`E_Ws >= k(p+k-2)+P`

and

`L_X+P >= T(s_f)`

with the independent exact Hamming floor `L_X>=L0(s_f)`.

Because `U=W_s disjoint_union E`, `(OC-RES)` is disjoint physical slack. Therefore every residual-one survivor must satisfy

> **`C0 >= k(p+k-2) + (c-1)min(k,p-1) + max{L0(s_f),T(s_f)}`** `(OC-SCORE)`

for its actual image size `2<=s_f<=k`.

This is strictly stronger than `(PR-SCORE)` whenever `c>=2` and `min(k,p-1)>0`.

## 6. Exact stress ray is no longer unbounded

On the preserved exact family

`c=p=2t`, `y=1`, `lambda=4t-2`, `u=x=3t`, `k=t+1`,

all matched heads may be chosen radius one, so this is precisely the previously dangerous endpoint. Here

`(c-1)min(k,p-1)=(2t-1)(t+1)=2t^2+t-1`,

`k(p+k-2)=3t^2+2t-1`,

and the best score choice is `s_f=k=t+1`, since the predecessor has `L0(s_f)>T(s_f)` and `L0` decreases with `s_f`. Also

`C0=12t^2+6t-4`,

`L0(t+1)=8t^2-t+2-2 floor((t+1)/2)`.

The remaining score margin is exactly

`M(t)=-t^2+4t-4+2 floor((t+1)/2)`.

Thus `M(4)=0`, `M(5)=-3`, and for `t>=5`,

`M(t+1)-M(t)<=-2t+5<0`.

Therefore:

> **the exact residual-one stress ray is rejected by `(OC-SCORE)` for every `t>=5`.**

Only the finite tail `t=2,3,4` survives this family calculation, corresponding to `n=10t+2<=42`.

This is not a closure of the full residual-one branch; it is a structural removal of the known unbounded scalar escape family.

## 7. Evidence status and next move

The new load-bearing point is `(OC-RECT)`: one escape vertex cannot simultaneously create an F-forcing K/W diagonal overlap and an R-forcing matched-fibre diagonal overlap. The resulting universal reservoir floor `(OC-RES)` is purely physical and does not depend on a finite scan.

Next work should hostile-replay `(OC-RECT)--(OC-RES)` directly from the two singleton equations, then optimize `(OC-SCORE)` over the full residual-one parameter set. If another unbounded family survives, preserve its exact geometry and attack it structurally rather than weakening the theorem into another broad-box diagnostic. Exact `Ccap_P/(ONE-P)/(CROWD)` remain pair-local whenever invoked, and rigid-interface reachability remains the principal global caveat.