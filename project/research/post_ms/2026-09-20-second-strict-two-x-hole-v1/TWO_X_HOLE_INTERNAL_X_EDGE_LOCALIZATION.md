# Two-X-hole branch — complete localization of internal X-edges

Date: 2026-09-20

Status: **same-session internal structural theorem** inside the core-saturated exact second-strict two-X-hole branch (`y>=2`, `x>=4`). This note strengthens the class-local independence result: the entire buffer-head set `R` is independent regardless of code, and every remaining X-edge must be sourced from one of the two physical holes through a complementary-code outside witness.

## 1. Setup

Retain the exact two-X-hole normal form:

- buffer holes `a_0,a_1`;
- `R=X\{a_0,a_1}`, with b complete to R and U_o;
- U_o is Y-anticomplete;
- `g=0`, `k=x`, and `W_0<->X` is a graph-fixed core-head bijection; write `c_x` for the unique core vertex adjacent to `x in X`;
- every X-code is neither d nor bar d;
- every `z in U_o` is an outside certificate for at least one R-head q, with `c(z)=bar c(q)`.

## 2. The whole buffer-head set R is independent

### Theorem 2.1

> **`G[R]` is edgeless.**                                 `(2X-R0)`

### Proof

Assume `xx' in E` with distinct `x,x' in R`. The edge lies in a triangle (indeed through b and through every Y-vertex), so raw triangle-edge criticality gives an orientation with source s in `{x,x'}`, head h the other endpoint, and witness w satisfying

`sw notin E`, `N(s) cap N(w)={h}`.

We exhaust witness locations without using any equality of the endpoint codes.

**A-layer.** A witness in X shares every Y-vertex with the X-source s, giving an extra common neighbour distinct from h. A Y-vertex is adjacent to s and so cannot be the required non-neighbour witness.

**Root.** The root is not adjacent to the A-head h.

**Tight matched layer.** A d-side matched witness is adjacent to every Y-vertex, again giving a common Y-neighbour with s. A bar-d-side matched witness `q_i` can distinguish the endpoint codes only when s is nonadjacent to `q_i`; but the graph-fixed core head `c_s` has code bar d, is adjacent to `q_i`, and is adjacent to s. Thus `c_s` is an extra common neighbour.

**Common core.** The only core vertex adjacent to h is `c_h`. Since `s` has code different from d, it selects a bar-d endpoint `q_j` in at least one tight fibre. The core vertex `c_h` also selects `q_j`, so s and `c_h` have an extra matched common neighbour.

**Buffer.** b is adjacent to the source s, so it cannot be a witness.

**Outside layer.** Every outside vertex w is adjacent to b, and so is the source s. Hence b is an extra common neighbour of s and w.

No location survives. Contradiction. `square`

This strictly strengthens the previous same-code class independence: the code relation between two R-heads is irrelevant.

## 3. Any hole--R edge must be certified from the hole through U_o

Fix `j in {0,1}` and `x in R`. Suppose `a_jx in E`.

### Theorem 3.1 — hole-edge localization

The only possible raw criticality orientation is

> `a_j -> x`

with a witness `z in U_o` such that

> `a_jz notin E`, `xz in E`, `N(a_j) cap N(z)={x}`,       `(HX-SING)`
>
> **`c(z)=bar c(a_j)`.**                                  `(HX-CODE)`

### Proof

The reverse orientation `x -> a_j` is impossible:

- X-witnesses share Y with x; Y-witnesses are adjacent to x;
- the root misses the A-head;
- a d-side matched witness shares Y with x;
- a bar-d-side matched witness shares the graph-fixed core head `c_x` with x;
- the only core vertex adjacent to `a_j` is `c_{a_j}`, and it shares a bar-d matched endpoint with x because `c(x)!=d`;
- b is not adjacent to the head `a_j`;
- every outside witness shares b with the source x.

For the orientation `a_j -> x`, the same A/root/matched/core exclusions apply with `a_j` as source: a d-side matched witness has a common Y-neighbour, a bar-d-side matched witness has the extra common core vertex `c_{a_j}`, and the candidate buffer b shares at least one tight bar-d endpoint with `a_j` because `c(a_j)!=d`. Hence only `U_o` remains.

Finally, if `c(z)` agreed with `c(a_j)` in any tight coordinate, their shared matched endpoint would be a common neighbour distinct from x. Therefore their codes are complementary. `square`

A fixed physical ordered pair `(a_j,z)` has a graph-fixed singleton common-neighbour set, so it can certify at most one hole--R edge.

## 4. A hole--hole edge has the same outside-witness localization

If `a_0a_1 in E`, both orientations have the same witness-location exhaustion: A/root/matched/core/buffer candidates all carry a fixed extra common neighbour, so any certificate must lie in U_o and its code must complement the chosen source-hole code.

Thus a hole--hole edge, if present, consumes one ordered pair `(a_j,z)` with

`c(z)=bar c(a_j)`

for one of the two physical holes.

## 5. Internal X-edge capacity is paid only by witness classes complementary to hole codes

For a head code C represented in R, retain

`m_C=|U_o cap V_{bar C}|`.

Every physical outside vertex belongs to such a represented complementary class because every outside vertex certifies at least one R-head.

By Theorems 3.1 and 4, an internal X-edge can be certified only from a hole `a_j` and only by an outside vertex of code `bar c(a_j)`. Ordered-pair injectivity gives

> **`e(G[X])<=m_{c(a_0)}+m_{c(a_1)}`**,                 `(2X-XEDGE-CAP)`

where `m_H=0` when the hole code H is not represented in R. If the two holes have the same code, the same outside vertex may contribute once for each physical source hole, which is why the multiplicity appears twice in the displayed sum.

Immediate consequence:

> if neither hole code is represented among R, then **`G[X]=emptyset`**. `(2X-X0-IF-NO-HOLE-CODE)`

Thus all possible internal X-density is concentrated in at most two distinguished head-code classes: the classes equal to the physical hole codes.

## 6. Strong uniform slack floor for every R-head

By `(2X-R0)`, a vertex `x in R` has at most the two holes as X-neighbours. It has

- p tight matched neighbours;
- at most y Y-neighbours (in fact all y);
- at most two X-neighbours;
- exactly one common-core neighbour `c_x`;
- the buffer neighbour b;
- at most `omega-1` outside neighbours because at least one outside certificate for `bx` is a non-neighbour.

Therefore

`d(x)<=p+y+2+1+1+(omega-1)=p+y+omega+3`.

The root degree is `2p+x+1+omega`, hence

> **`epsilon_x>=p+x-y-2`**,                              `(2X-RPAY)`

or safely

> `epsilon_x>=[p+x-y-2]_+`.

Summing over the `x-2` buffer heads gives

> **`L_R>=(x-2)[p+x-y-2]_+`.**                          `(2X-RPAY-SUM)`

This dominates the earlier class-quadratic bound in regimes where y is not too large; the class bound remains useful when a single code class is large.

## 7. Strategic consequence

The two-X-hole branch has now lost essentially all anonymous X-density:

- R is independent;
- every residual X-edge touches a physical hole;
- every such edge consumes a complementary witness from one of at most two distinguished code classes;
- every R-head pays the uniform slack floor `(2X-RPAY)`.

The next structural target is to combine the two-foot coordinate routing with those two distinguished hole-code classes. If neither hole code can be represented by a buffer head under the routing normal form, the entire X-layer becomes independent immediately. If one can be represented, its complementary witness class is simultaneously responsible for both buffer certificates and all possible internal X-edge certificates, creating a sharply localized load/self-pricing problem.