# Residual-one k=2 half-ray: Delta-three barrier

Date: 2026-09-20

Status: **same-session conditional theorem**, downstream of the corrected H--U B-layer capacity decomposition, the small-deficit concentration theorem, the preserved H--H certificate split, and the raw private-spoke obstruction. It does not use the superseded H--U private-foot chain and does not assert graph-level realizability of the rigid interface.

## 1. Setup

On the corrected half-ray

`p=2t, c=y=t, u=t+1, h=2t-1`,

write

`a=2M_H-R_q`, `b=h-R_j`, `c0=(u-2)-S`,

and

`Delta=a+b+c0`.

The predecessor notes give

- `g=|U\P|<=c0`, where `P=U_j^-`;
- `L_H=3t-1+Delta`;
- on a residual-saturated H-row, the unique P-neighbour is the edge assigned to the residual `q_j` certificate;
- local row accounting `epsilon_i=2+a_i+b_i-s_i`, hence `s_i<=2+a_i+b_i`;
- shared edges on saturated rows must be reverse-U edges with their U-head outside P;
- every such reverse-U witness from source `h_i` satisfies `d_H(w)<=m_i`;
- the total U-certified H--H edge capacity is at most `u`.

The earlier theorem already proves `Delta>=2` for `t>=5`. We now classify every allocation with `Delta=2`.

## 2. The three cases with c0=0

### `(a,b,c0)=(2,0,0)`

Here `g=0` and every H-row is residual-saturated. The shared load is `S=t-1>0`, but a saturated row has no U-head outside P. Equivalently the exact placement inequality has zero right-hand side. Impossible for every `t>=2`.

### `(1,1,0)`

Again `g=0`. All shared edges must lie on the unique residual-unsaturated row. The local row bound there is

`s_i<=2+a_i+b_i<=4`.

Since `S=t-1`, this case is impossible for `t>=6`.

### `(0,2,0)`

There are two residual-unsaturated rows, each with `s_i<=3`. Hence `S=t-1<=6`; this case is impossible for `t>=8`.

Thus no `c0=0` allocation survives for `t>=8`.

## 3. The case `(1,0,1)`

All H-rows are residual-saturated and `S=t-2`. For `t>=3`, `g` cannot be zero, so `g=1`; write `U\P={t_*}`. Every shared edge is therefore a reverse-U edge to `t_*`.

Because `|P|=t` and `S=t-2=|P|-2`, the shared-resource injection exhausts

`P = W_s disjoint_union {the t-2 reverse-U witnesses}`.

The selected witnesses `W_s` are H-anticomplete. Every H-row has exactly one P-neighbour, so the reverse-U witnesses must supply at least h H--P incidences. If witness w is sourced from `h_i`, singleton criticality gives `d_H(w)<=m_i`; with one outside head each source occurs at most once. Therefore

`h <= sum_w d_H(w) <= sum_i m_i = 2M_H`.                `(DT-1)`

On the other hand every saturated row has at most `g+1=2` U-neighbours, so the global residual-slot degree bound gives

`e(H,U)<=2h`.

The exact capacity decomposition at `Delta=2` gives

`e(H,U)=2M_H+h+u-4=2M_H+3t-4`.

Hence

`2M_H<=t+2`.                                             `(DT-2)`

Combining `(DT-1)` and `(DT-2)` gives

`2t-1<=2M_H<=t+2`,

which is impossible for `t>=4`; at `t=3` it would force the even integer `2M_H` to equal 5, also impossible. Thus `(1,0,1)` is impossible for every `t>=3`.

## 4. Private-spoke code classification for an H-positive P-carrier

The remaining case needs a refinement of the universal-hub obstruction.

For `z in P`, let

`D(z)={i private : z p_i in E}`,

where `p_i` is the matched endpoint selected by d in private coordinate i. Suppose `d_H(z)>0`.

For every `i in D(z)`, raw B-edge criticality of `z p_i` has no reverse orientation: the only A-vertex missing `p_i` is `h_i`; if `z h_i` is absent it cannot be the singleton-head witness, while if `z h_i` is present then every Y-vertex is an additional common neighbour of `p_i,h_i`.

In the forward orientation:

- a Y-witness is impossible because any H-neighbour of z is also adjacent to Y;
- a K-witness is impossible because z and every K-vertex both see the residual endpoint `q_j`, giving an extra common neighbour;
- hence the witness must be some `h_l`, `l!=i`, nonadjacent to z.

Comparing matched fibres in the singleton equation shows that the only common matched endpoint may be `p_i`. Since `h_l` uses `bar d` at l and d at every other private coordinate, this forces

> **`D(z)={i,l}`.**                                      `(DT-3)`

Moreover the symmetric edge `z p_l` forces z to miss `h_i` as well. Thus an H-positive P-vertex has either

- `D(z)=empty`, or
- `D(z)={i,l}` and it is nonadjacent to both `h_i,h_l`.

Now let `C` be any set of H-vertices of missing H-degree zero which are adjacent to z. For every `h_r in C`, its index r is outside `D(z)`, so z sees the private foot `q_r`. For any two vertices `h_r,h_s in C`, the H-edge `h_rh_s` is therefore spoiled in **both** private-foot orientations by the common neighbour z. The preserved H--H split forces this edge to be U-certified.

Since at most u H--H edges are U-certified globally,

> **`binom(|C|,2)<=u`.**                                 `(DT-4)`

Put

`R(t)=floor((1+sqrt(1+8u))/2)=floor((1+sqrt(8t+9))/2)`.

Then every H-positive P-carrier is adjacent to at most `R(t)` H-vertices of missing degree zero.

## 5. The case `(0,1,1)`

There is one residual-unsaturated H-row. For `t>=6`, `g=0` would force all `S=t-2>3` shared edges onto that row, contradicting its local bound `s_i<=3`. Hence `g=1`.

Let `s0` be the number of shared edges on the unique unsaturated row. Then `0<=s0<=3`. The remaining

`T=S-s0=t-2-s0`

shared edges lie on residual-saturated rows. Each is reverse-U to the unique outside head and has a distinct endpoint-indexed witness.

On a saturated source row, `a_i=b_i=0`; since it already has its residual P-edge and its one outside shared edge, its private-certificate count is zero. Equivalently `m_i=0`. Thus the T source rows form a clique of H-vertices of missing degree zero.

Their T reverse-U witnesses are H-anticomplete by `d_H(w)<=m_i=0`; the two selected witnesses are also H-anticomplete.

Because `c0=1` and `g=1`, the shared-resource injection is exact:

`|P\W_s|=t-2=S`.

After removing the T H-anticomplete reverse witnesses, only `s0` vertices of P remain capable of supplying the unique P-neighbour required by the T saturated source rows. Thus those T rows are covered by at most `s0<=3` H-positive P-carriers.

By `(DT-4)`, each carrier covers at most `R(t)` of these clique rows. Therefore

> **`t-2-s0 <= s0 R(t)`.**                               `(DT-5)`

The most permissive choice is `s0=3`, so a necessary condition is

`t-5 <= 3 floor((1+sqrt(8t+9))/2)`.

This fails already at `t=30` (`25>24`), and for every `t>=31` follows from the corresponding strict continuous inequality

`t-5 > (3/2)(1+sqrt(8t+9))`.

Hence `(0,1,1)` is impossible for every `t>=30`.

## 6. Delta-three barrier

All six nonnegative allocations of `a+b+c0=2` are now excluded for sufficiently large t. Therefore:

> **THEOREM. On the corrected half-ray, for every `t>=30`,**
>
> **`Delta>=3`, and hence `L_H>=3t+2`.**                 `(DT-6)`

The numerical gain over the previous floor is only one unit. The structural gain is larger: every configuration within two units of simultaneous H--U capacity saturation is now impossible, and the proof combines three genuinely different currencies:

1. residual-column location of shared resources;
2. exact row capacity / reverse-witness concentration;
3. raw private-spoke criticality plus global H--H U-certificate capacity.

## 7. Next target

Do not merely iterate the integer case split mechanically. Use the proof of `(DT-4)` as the scalable ingredient. For fixed or `o(t)` Delta, almost all shared load lies on missing-degree-small saturated H rows and is concentrated through `O(Delta)` outside heads. The remaining P-carriers must cover many such nearly-complete H rows. Private-spoke criticality restricts each carrier's private d-support, while the H--H split limits how many mutually adjacent rows one carrier can touch.

The next goal is an inequality of the form

`T <= O((Delta+1)*sqrt(u + error(M_H,Delta)))`

or stronger. Combined with `T>=t-O(Delta)`, this would force `Delta=Omega(sqrt(t))` immediately and perhaps, after iteration with the H-hole term, `Delta=Omega(t)`.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.