# Exact second-strict two-X-hole branch: physical two-foot routing and cut-core saturation

Date: 2026-09-20

Status: internal conditional structural theorem inside the audited rigid one-code complete-cut branch. This note is structural and does not use a finite parameter scan. The zero-positive-rigid-cut caveat remains binding.

## 1. Setup

Assume the exact second-strict unloaded buffer layer

`epsilon_b=p-g+2`

with defect split

`(h_X,h_o)=(2,0)`.

Let the two buffer--X holes be `a_0,a_1`. Put

`R=X\{a_0,a_1}`, `|R|=x-2`.

Then b is complete to `R` and to all of `U_o`. The preserved reverse-witness exclusions imply every edge `bx`, `x in R`, uses an outside-U Orientation-A certificate

`bz in E`, `xz notin E`, `N(x) cap N(z)={b}`, `c(z)=bar c(x)`.

## 2. The whole outside layer misses Y and has no bar-d code

Fix `w in U_o`. Since `bw in E`, raw criticality of the rooted U-edge bw applies.

If `wy in E` for some `y in Y`, the orientation `w -> b` cannot use an A-witness in R because y becomes an extra common neighbour. The opposite orientation `b -> w` cannot use Y: besides the U-head w, every Y-source shares all `x-2>=1` buffer-head vertices of R with b. Nor can it use either hole `a_j`, since b and `a_j` share a tight matched endpoint on the nonempty difference set of `a_j`. Hence

> `E(U_o,Y)=emptyset`.                                    `(2X-UY)`

If `c(w)=bar d`, the same-code theorem for the edge bw requires a complementary d-coded A-witness. Such a witness lies in Y. With source b it has at least one R-vertex as an extra common neighbour; with source w it would need to be adjacent to b, contrary to `d_Y(b)=0`. Thus

> `U_o cap V_{bar d}=emptyset`.                           `(2X-NOBARD)`

Finally the orientation `b -> w` is impossible even without assuming a Y-neighbour: the only A-vertices nonadjacent to b are `Y union {a_0,a_1}`, Y misses w by `(2X-UY)`, and each hole shares a tight matched neighbour with b. Therefore every w must orient

> `w -> b`

through some q in R, giving

> `wq notin E`, `N(w) cap N(q)={b}`.                     `(2X-EVERY-UO-CERT)`

So every physical outside vertex is itself an outside certificate for at least one actual buffer head.

## 3. Exact two-foot coordinate routing

Fix a buffer head `x in R` and one outside witness z for bx. For each tight agreement coordinate

`i in I_x={i:c(x)_i=d_i}`,

the matched edge `zq_i` has the same self-pricing property as in the one-hole funnel: every singleton A-witness must be an X-vertex nonadjacent to b. There are exactly two such vertices, `a_0,a_1`.

For a foot `a_j` there are two possibilities.

### Reverse use of a foot

If `za_j in E`, then the original singleton `N(x) cap N(z)={b}` forces

`xa_j notin E`.

The foot can witness `q_i -> z` only when `a_jq_i notin E`, equivalently

> `i in I_{a_j}`.

Thus reverse-routed coordinates through `a_j` lie in the foot agreement set `I_{a_j}`.

### Forward use of a foot

If `za_j notin E`, then the foot can witness `z -> q_i` through

`N(z) cap N(a_j)={q_i}`.

A fixed physical pair `(z,a_j)` has one graph-fixed common-neighbour set, so this can happen for at most one coordinate i.

Moreover the tight matched singleton condition is exact. Since `c(z)=bar c(x)`, z and `a_j` must share exactly the one matched endpoint q_i and no other tight endpoint. In support notation this is equivalent to

> `S_{a_j} triangle S_x={i}`.                             `(2X-FWD-HAM1)`

Hence a forward coordinate through a foot forces the head code and foot code to be at Hamming distance exactly one.

### Two-foot cover

Every i in I_x must therefore be covered by one of the two feet, with the following normal form:

- an adjacent foot may reverse-cover coordinates only from its `I_{a_j}`;
- a nonadjacent foot may forward-cover at most one coordinate, and if it does then `d_H(c(a_j),c(x))=1`.

Consequences by the adjacency pattern of z to the two feet:

1. if z sees both feet, then `I_x subseteq I_{a_0} union I_{a_1}` and x misses both feet;
2. if z sees exactly one foot, all but at most one coordinate of I_x lie in that foot's agreement set, while any exceptional coordinate is a Hamming-one forward move through the other foot;
3. if z sees neither foot, then `|I_x|<=2`; when `|I_x|=2`, one coordinate must route through each foot and x is Hamming distance one from each foot code.

This is the exact two-foot support normal form promised by the previous handoff.

## 4. For y>=2, every X-vertex must be a common-core head when x>=4

Assume `y>=2` and `x>=4`. Fix any `a in X` and `y_0 in Y`.

The edge `ay_0` lies in a tight matched triangle because every X-code is neither d nor bar d.

Orientation `a -> y_0` has no witness:

- any X-witness shares a second Y-neighbour with a;
- a matched endpoint that distinguishes the codes also shares a second Y-neighbour with a;
- Y is independent;
- b, W_0 and U_o are Y-anticomplete by the unloaded/common-core setup and `(2X-UY)`.

Thus the edge must orient `y_0 -> a`. Avoiding a tight matched common neighbour with the d-coded source forces a witness of code `bar d`. No outside vertex has that code by `(2X-NOBARD)`.

For a hole `a_j`, b is not adjacent to the head, so the only possible witness is a common-core vertex whose unique X-neighbour is exactly `a_j`.

For a buffer head `x in R`, b is adjacent to x but cannot witness when `x>=4`: `N(y_0) cap N(b)` contains all `x-2>=2` vertices of R. Hence a common-core singleton-head witness is again required.

Therefore every vertex of X lies in the graph-fixed injective common-core head image. Since the common-core theorem has `|W_0|=k=x-g<=x`, this gives

> `k=x`, `g=0`, and the core head map is a bijection `W_0 <-> X`. `(2X-CORE-SAT)`

The `x=3` case is exceptional because b sees only one buffer head and may itself certify that one complete-cut edge; it remains a small-head tail.

## 5. Immediate physical bills in the saturated regime

Under `(2X-CORE-SAT)`, every outside vertex w certifies at least one buffer head q by `(2X-EVERY-UO-CERT)`. Let `c_q in W_0` be the unique core vertex whose X-head is q.

Since `c_qq in E`, the singleton `N(w) cap N(q)={b}` forces

> `wc_q notin E`.

Different outside vertices give distinct physical core--outside pairs, so

> `H_core=e_bar(W_0,U_o)>=|U_o|`.                         `(2X-HCORE)`

The exact common-core identity therefore strengthens to

> `E_core>=x(p+x-1)+|U_o|`.                              `(2X-ECORE)`

At the same time the second-strict buffer itself pays

> `epsilon_b=p+2`.

These are located physical costs before pair-local capacity or residual optimization.

## 6. Remaining task

The large mixed-hole arm is now closed for `y>=2` in the companion note. The remaining large second-strict branch is therefore this two-X-hole core-saturated geometry:

- `g=0`, `k=x`;
- all X-vertices are distinct graph-fixed common-core heads;
- every outside vertex certifies at least one buffer head and forces a distinct core--outside hole;
- each buffer head's tight agreement coordinates obey the exact two-foot routing normal form above.

The next structural target is to combine the two-foot support normal form with the core bijection: classify whether many heads can share the same outside witness/foot pattern without forcing additional core--outside holes or same-code criticality collisions. Only after extracting that geometry should the exact pair-local `Ccap_P/(ONE-P)/(CROWD)` and rooted residual ledger be applied.
