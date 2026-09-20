# Two-X-hole branch — same-code head independence and class self-pricing

Date: 2026-09-20

Status: **same-session internal structural strengthening** of the core-saturated two-X-hole branch. This uses the independently re-derived raw same-code theorem from `SAME_CODE_RAW_CRITICALITY_AUDIT.md` and the certificate-incidence ledger from `TWO_X_HOLE_CERTIFICATE_INCIDENCE.md`.

## 1. Setup

Assume the exact second-strict two-X-hole geometry with `y>=2`, `x>=4`.

From the preserved normal form and incidence strengthening:

- `g=0`, `k=x`;
- `W_0 <-> X` is a graph-fixed core-head bijection;
- `R=X\{a_0,a_1}` consists of the `x-2` actual buffer heads;
- every `x in R` has at least one outside certificate `z in U_o` with
  `xz notin E`, `N(x) cap N(z)={b}`, `c(z)=bar c(x)`;
- every physical outside vertex is incident with at least one such head;
- `b--U_o` is complete and `b--R` is complete;
- `U_o` is Y-anticomplete;
- every X-code is different from both d and bar d.

## 2. Same-code buffer heads are independent

### Theorem 2.1

If `x,x' in R` have the same tight code C, then

> `xx' notin E(G)`.                                      `(2X-CLASS-INDEP)`

### Proof

Suppose `xx'` is an edge. The independently re-derived same-code theorem applies because the two endpoints lie in the coded layer and have equal code. It supplies an orientation with source `s in {x,x'}` and a witness `w in A union U` satisfying

`sw notin E`, `N(s) cap N(w)={head}`, `c(w)=bar C`.

We exhaust the two possible witness regions.

**A-witness.** If `w in X`, then both s and w are adjacent to every vertex of Y. Since the head lies in X, any Y-vertex is an additional common neighbour distinct from the head. Hence no X-witness works. If `w in Y`, then `c(w)=d=bar C`, forcing `C=bar d`, excluded by the rigid one-code setup.

**U-witness.** If `w in U_o`, then `bw in E` because `h_o=0`, while `bs in E` because `s in R`. Thus b is an extra common neighbour. If `w in U_-=W_0 dotcup {b}`, then `c(w)=bar d`; the complementary-code requirement `bar C=bar d` would force `C=d`, also excluded.

No witness location remains. Contradiction. `square`

The argument actually needs only `y>=1` at the A-witness step, but we record it inside the currently core-saturated `y>=2` branch.

## 3. Quadratic head-class slack

Let C be a represented R-code and put

> `n_C=|R cap A_C|`.

By `(2X-CLASS-INDEP)`, a head `x in R cap A_C` misses the other `n_C-1` members of its own code class.

It also has the following forced degree restrictions:

- exactly p tight matched neighbours;
- all y vertices of Y may be neighbours;
- among X it has at most `x-n_C` neighbours, because the other `n_C-1` same-code R-heads are absent;
- among the common core it sees only its unique graph-fixed head vertex `c_x`;
- it sees the buffer b;
- it misses at least one outside certificate in U_o, so it has at most `omega-1` U_o-neighbours.

Thus

`d(x)<=p+y+(x-n_C)+1+1+(omega-1)`

`    =p+x+y+omega+1-n_C`.

The maximum-degree root has degree

`2p+u=2p+x+1+omega`.

Therefore

> **`epsilon_x>=p-y+n_C`.**                             `(2X-XPAY0)`

Using nonnegative slack,

> **`epsilon_x>=[p-y+n_C]_+`.**                         `(2X-XPAY)`

Summing over the class gives

> `L_C^X>=n_C[p-y+n_C]_+`.                              `(2X-CLASS-PAY)`

Hence the whole buffer-head population satisfies

> **`L_R>=sum_C n_C[p-y+n_C]_+`.**                      `(2X-R-PAY)`

This is a genuine quadratic multiplicity price when a head code class grows. It is not visible in the previous total `x[p+1-y]_+` floor.

## 4. Interaction with the certificate-incidence classes

The incidence decomposition from `TWO_X_HOLE_CERTIFICATE_INCIDENCE.md` pairs the same head classes with their complementary outside classes:

- head multiplicity `n_C>=1`;
- physical outside multiplicity `m_C>=1` in code `bar C`;
- certificate traffic `L_C>=max(n_C,m_C)`.

Thus each represented code class pays simultaneously through

1. head slack `n_C[p-y+n_C]_+`;
2. located core--outside holes `L_C`;
3. outside-witness slack through the selected loads `r_z`;
4. the exact two-foot support restrictions inherited from the normal form.

The important point is that these prices are **class-local and correlated**. A class cannot make `n_C` large to save on the number of distinct codes without paying quadratically in X-slack; nor can it make `m_C` large without increasing the physical incidence/core-hole ledger.

## 5. Same-code outside edges have only the two hole witnesses available

There is a second useful restriction. Let `z,z' in U_o` have the same code `bar C` and suppose `zz' in E`.

The same-code theorem says that a U-source must use an A-witness of complementary code C.

- Any C-coded buffer head in R is adjacent to b, as is the U-source, so b is an extra common neighbour and such a head cannot witness the U-U edge.
- Any other X-vertex used as witness is still adjacent to all Y, but the sharper buffer obstruction above already removes the R-heads.
- A Y-witness would force C=d, excluded.

Therefore any viable witness must be one of the two buffer holes `a_0,a_1`, and it must itself have code C.

Consequently, for each represented outside code class, same-code U_o edges can consume only ordered `(source,a_j)` pairs with a complementary-coded hole. Ordered-pair injectivity then gives the safe bound

> `e(G[U_o cap V_{bar C}]) <= h_C m_C`,                 `(2X-UCLASS)`

where

> `h_C=#{j in {0,1}:c(a_j)=C} <=2`.

In particular if neither hole has code C, the entire complementary outside class is independent.

This does not yet control cross-code U_o edges, but it removes unrestricted internal density from every class not represented by a hole code.

## 6. Next structural target

The live two-X-hole problem is now a finite **foot-pattern / code-class allocation** problem rather than an anonymous outside reservoir:

- each represented head code C must satisfy one of the two-foot routing patterns;
- its head class is independent and pays `(2X-CLASS-PAY)`;
- its complementary witness class pays the incidence/core-hole ledger;
- same-code edges inside that witness class are impossible unless one of only two hole codes equals C.

The next theorem should classify which head codes can occur in the four witness-foot adjacency patterns and bound the number of large `n_C` classes. Only after that classification should the local pair-capacity budget be optimized.