# Residual-one k=2 cross-code complement-witness capacity

Date: 2026-09-20

Status: **same-session structural strengthening**, conditional on the raw cross-code complement localization theorem and `J2=empty`. No finite scan is used.

The preceding theorem says a U--U edge must orient from an endpoint whose complementary A-code is represented. Keeping the physical witness identity yields a sharp degree-capacity statement.

## 1. General capacity into complement-empty targets

Let V be a set of U-vertices such that

`A_{bar(c(t))}=empty` for every `t in V`.

Fix `w in U\V`. For an edge wt, `t in V`, the orientation sourced at t is impossible: it would require an A-witness of code `bar(c(t))`. Hence the edge must orient from w.

The witness then lies in the single A-code class `A_{bar(c(w))}`. For fixed w and fixed physical witness a, the graph-fixed singleton set

`N(w) cap N(a)`

can have only one singleton head t. Therefore distinct neighbours of w in V require distinct witnesses in `A_{bar(c(w))}`.

> **`d_V(w) <= |A_{bar(c(w))}|`.**                       `(CC-CAP)`

This is an ordered physical source/witness capacity, not merely a code-counting statement.

## 2. Specialization to q_j-nonneighbours at `J2=empty`

For a q_j-nonneighbour w write `c(w)=d xor S`, `S subseteq I`.

The previous complement-repertoire theorem gives

- if `S proper subset I`, then `A_{bar(c(w))}=empty`;
- if `S=I`, then `bar(c(w))=C=d xor e_j` and `A_C=K`, so `|A_C|=2`.

Let P be the proper-support q_j-nonneighbour set. Then

> **every proper-support q_j-nonneighbour has zero neighbours in P;**
>
> **every full-support q_j-nonneighbour has at most two neighbours in P.** `(CC-NONHUB)`

The first line recovers the global independence of P; the second is new cross-code capacity.

## 3. Consequence for a sparse D1 population versus K-heavy vertices

Suppose D is a D1 population that has been compressed by the hub/private-spoke theorems so that all but o(p) vertices are q_j-nonneighbours with proper support. Write this dominant subset as `P_D`, with

`|P_D|=(beta+o(1))p`.

Let R be a K-heavy population. The K-heavy hub rectangle implies that any lower-envelope sequence has only o(p) K-heavy q_j-neighbours. For every remaining q_j-nonneighbour `w in R`, `(CC-NONHUB)` gives

`d_{P_D}(w)<=2`.

The o(p) hub-neighbour exceptions contribute at most o(p^2) possible edges. Hence, if `|R|=(alpha+o(1))p`,

> **`M_U(R,P_D) >= (alpha beta-o(1))p^2`.**               `(CC-RD)`

Together with P_D independence,

> **`M_U(P_D) >= (beta^2/2-o(1))p^2`.**                  `(CC-DD)`

Thus the missing-U-edge currency between/inside the cheap D1 side is already

> **`M_U >= [alpha beta+beta^2/2-o(1)]p^2`**             `(CC-M)`

before any F0, F1, W-heavy or mixed sectors are counted.

## 4. R+D1 endpoint has a half-quadratic physical floor

Consider the asymptotic endpoint in which, up to o(p), the escape reservoir consists only of K-heavy R and compressed proper-support D1 vertices D. Then `alpha+beta=1`.

There are no K-free exceptional repair vertices. The preserved exception-budget theorem therefore gives for every K-heavy source `d_Y<=1`, hence

> `Z_Y(R)>=(alpha-o(1))p^2`.                              `(CC-RY)`

The same theorem gives the disjoint R-side bill

> `E_R+A_R >= (alpha^2/3-o(1))p^2`,                      `(CC-RCONS)`

where `A_R=Z_{H,R}`.

The three blocks `(CC-M)`, `(CC-RY)`, `(CC-RCONS)` are physically disjoint:

- `(CC-M)` is missing U--U pairs with a D1 endpoint;
- `(CC-RY)` is Y--R nonedges;
- `(CC-RCONS)` uses R-slack and H--R holes.

Therefore

`D_phys/p^2`
` >= alpha beta+beta^2/2 + alpha + alpha^2/3-o(1)`
` = 1/2 + alpha-alpha^2/6-o(1)`.

Since the last expression is at least 1/2 on `0<=alpha<=1`,

> **every compressed R+D1 endpoint satisfies**
> **`liminf D_phys/p^2 >= 1/2`.**                        `(CC-HALF)`

The minimum is approached only at the pure-D1 end alpha=0; any positive K-heavy density raises this particular lower bound.

This is a major increase over the predecessor coarse R+D1 envelope `(7-sqrt(33))/8≈0.15693`.

## 5. Scope and next move

`(CC-HALF)` is not yet a global low-k theorem: a configuration may retain linear F0 or other escape classes, and a D1 population may choose to pay the already-proved q_j-neighbour or dense/full-support penalties instead of entering the compressed proper-support normal form.

But it removes the specific cheap geometry isolated by the predecessor additive optimizer. The global minimizer must now migrate toward a reservoir with genuine K-free repair capacity (F0) and/or one of the other expensive classes, or deliberately pay the hub/support penalties.

The next global coefficient optimization should therefore combine:

- the R/F0 exception-conservation functional;
- the K-heavy Y-degree cap as a located `Z_Y(R)` bill;
- the compressed R+D1 half-quadratic theorem;
- F1/S/mixed class costs.

Global caveat unchanged: zero positive actual-D2C rigid complete Hall-cut fixtures with `x>=3` remain in bounded regression.