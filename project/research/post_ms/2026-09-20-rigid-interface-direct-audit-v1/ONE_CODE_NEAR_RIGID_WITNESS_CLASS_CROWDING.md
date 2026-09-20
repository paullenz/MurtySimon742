# One-code near-rigid cut — complementary U-witness class crowding

Date: 2026-09-20

Status: **same-session structural strengthening**, conditional on the exact rigid Hall event `M_X=E_X=0`, the one-code outside layer, and the same near-rigid Hall provenance used in `ONE_CODE_NEAR_RIGID_SLOT_PRICE.md`. The bounded actual-D2C regression still has no positive rigid complete Hall-cut fixture with `x>=3`; this note does not remove that interface caveat.

The point is to exploit a resource not charged in the predecessor slot-price theorem: for one minimum-U source, its selected U-witnesses form a very large **single Boolean code class**. Same-code criticality then limits how dense that witness class can be, while maximum-degree bookkeeping forces density unless the class pays U-slack.

## 1. Setup

Use the one-code rigid notation. The outside source layer is

`Y=A_d`, `|Y|=y>=1`,

for one tight code `d`; the complementary A-class `A_bar(d)` is empty in this one-code endpoint. Put

`x=|A_X|>=3`,

`g0=p-y`,

`c=lambda+1-g0>=0`.

The rooted size identity is

> `u=x-p+c`.                                              `(WC-0)`

Fix a source `s in Y` with minimum selected U-witness count

`k=k_*`.

Let `W subseteq U_bar(d)` be its selected U-witness set, so `|W|=k`, and put

`d_U^*=u-k`.

Every `w in W` has exactly one A_X-neighbour, the heads are distinct across W, and `s` is nonadjacent to every vertex of W. The predecessor distinct-head theorem gives

> `k >= x-rho >= x-p = u-c`,                              `(WC-1)`

so

> `0<=d_U^*<=c`.                                          `(WC-2)`

The selected matched-covered head set has size

> `m=x-k=p-c+d_U^*`.                                      `(WC-3)`

In particular the matched/U split of a minimum source is controlled by the same rooted gap `c` that bounds the number of U vertices escaping W.

## 2. Same-code edges inside W have only Y witnesses

All vertices of W have the same Boolean code `bar(d)`. Consider an edge `ww'` of `G[W]`.

The independently repaired full coded-layer same-code criticality theorem applies. Since both possible sources `w,w'` lie in U, its witness must lie in A and have complementary code d. In the one-code endpoint this means the witness lies in Y.

Choose one criticality orientation and witness for every edge of `G[W]`. For `t in Y` put

`r_t=d_W(t)`.

If `r_t=0`, t cannot witness a W-edge because the certificate head must be a W-neighbour of t. If `r_t>0`, every edge witnessed by t uses a source in `W\N(t)`. The ordered `(source,t)` injection from the repaired same-code theorem implies that t witnesses at most

`k-r_t <= k-1`

edges.

The fixed minimum source s has `r_s=0`, because every w in W is a selected witness for s and hence is nonadjacent to s. Therefore at most `y-1` Y-vertices can be active W-edge witnesses, and

> **`e(W) <= (y-1)(k-1)`.**                              `(WC-4)`

A slightly more local form is

> `e(W) <= sum_{t:r_t>0}(k-r_t)`,                         `(WC-4a)`

which should be retained in any equality analysis.

This is a physical edge-capacity theorem, not a code-distribution relaxation: the large complementary U-witness class cannot be arbitrarily dense because every one of its same-code edges must consume an ordered U-source/Y-witness certificate.

## 3. Maximum degree forces W-slack

For `w in W`, the only possible neighbours outside W are:

- the root v;
- its p selected matched neighbours;
- its unique A_X head;
- at most `y-1` vertices of Y, because `ws` is a nonedge;
- the `d_U^*=u-k` vertices of `U\W`.

Thus at most

`p+y+d_U^*+1`

neighbours lie outside W. Since `d(w)=2p+u-epsilon_w`,

> `d_W(w) >= g0+k-1-epsilon_w`.

Summing over W gives

> **`2e(W) >= k(g0+k-1)-E_W`,**                          `(WC-5)`

where `E_W=sum_{w in W}epsilon_w`.

Combining `(WC-4)` and `(WC-5)` yields the new witness-class slack bill

> **`E_W >= k(g0+k-1)-2(y-1)(k-1)`.**                   `(WC-6)`

Every w in W is used by s, so the raw singleton-witness degree count also gives `epsilon_w>=g0`. Hence the safe sharpened form is

> **`E_U >= E_W >=`
> ` max{ k g0, k(g0+k-1)-2(y-1)(k-1) }`.**              `(WC-7)`

Compared with the preserved all-source incidence floor

`E_U>=k(p-1)=k(g0+y-1)`,

the best unconditional U-slack input is therefore

> **`E_U >=`
> ` E_class(k):=max{`
> `   k(p-1),`
> `   k(g0+k-1)-2(y-1)(k-1)`
> ` }`.                                                   `(WC-8)`

The second term becomes quadratically stronger when the minimum source needs many U-witnesses relative to the outside layer y.

## 4. Collapse rho and g_P only after retaining their physical meaning

Let H be the heads matched-covered for the same minimum source s. Then

`|H|=m=x-k`.

The chosen matched witnesses have distinct singleton heads, so

`m<=rho<=g_P`.

The preserved gamma-collision floor is

`phi(g)=g(g-1)` for `g>=3`, and zero for `g<=2`.

Since phi is nondecreasing,

> `phi(g_P)>=phi(m)=phi(x-k)`.                             `(WC-9)`

When `m>=3`, the private-coordinate/Hamming near-rigid theorem also gives

> `L_X > xg0-k(x-k)-p/2`.

Define its exact integral floor

`ell(k)=max(0,floor(xg0-k(x-k)-p/2)+1)`

for `k<=x-3`, and `ell(k)=0` for `k>=x-2`.

The pair-collision and Hamming-slot prices are both A-slack bills and must be combined by maximum, not by addition. Since `(WC-8)` is an E_U bill, it can be added. Thus every one-code near-rigid survivor satisfies the one-dimensional physical score floor

> **`E_U+L_A >=`
> ` E_class(k)+max{phi(x-k),ell(k)}`**                    `(WC-10)`

for its actual minimum-source count k, where

> `max(0,x-p)<=k<=min(u,x)`.                              `(WC-11)`

Consequently the parameter-only version is

> **`E_U+L_A >= Omega_class:=`
> ` min_{k in [max(0,x-p),min(u,x)]}`
> ` [E_class(k)+max{phi(x-k),ell(k)}]`.**                 `(WC-12)`

This does not replace the exact tuple `(c,rho,k_*,g_P,...)` for pair-local work. It is a safe scalar corollary useful for identifying regimes where the witness class itself already self-prices.

## 5. The zero-gap c=0 geometry is exact

The rooted gap `c=0` is much more rigid than the preceding inequalities suggest.

From `(WC-0)` and `(WC-1)`,

`u=x-p`, `k>=u`.

But k cannot exceed the U population, so

> `k=u`, `m=p`, `rho=p`, and `g_P=p`.                     `(WC-Z0-1)`

Thus the fixed source s uses **every U vertex** as a complementary singleton X-witness.

For any t in Y, exact degree bookkeeping after the p matched neighbours and complete X-cut gives

> `epsilon_t+d_Y(t)+d_U(t)=c=0`.

Therefore

> `epsilon_t=0`, `d_Y(t)=0`, `d_U(t)=0` for all t in Y.  `(WC-Z0-2)`

So Y is independent and anticomplete to U.

Now every U vertex has code `bar(d)`. If two U vertices were adjacent, the repaired same-code U-edge theorem would require an A_d=Y witness adjacent to the certificate head. This is impossible because Y is anticomplete to U. Hence

> **`G[U]` is independent.**                              `(WC-Z0-3)`

Each U vertex therefore has exactly the root, p matched neighbours and one X-neighbour, so

> **`epsilon_w=p+u-2` for every w in U`,**
> **`E_U=u(p+u-2)`.**                                     `(WC-Z0-4)`

The p matched-covered heads use all p singleton matched resources, so `g_P=p`; for p>=3 the preserved collision floor gives

> **`L_A>=p(p-1)`.**                                      `(WC-Z0-5)`

Therefore

> **`E_U+L_A >= u(p+u-2)+p(p-1)`.**                      `(WC-Z0-6)`

This is an exact physical zero-gap bill, not a finite-scan observation.

## 6. Above-M consequence: c=0 is bounded to six tiny parameter tuples

Assume p>=3 and an above-M(n) candidate, so the standard score ceiling is

`E_U+L_A<=C0`,

with

`C0=2(D_M-1)+lambda(p+u)-p`,

`D_M=b(n-b)-M(n)`, `b=2p+u`, `n=2b-lambda`.

In the c=0 branch,

`g0=lambda+1`, `y=p-lambda-1>=1`, hence `0<=lambda<=p-2`.

Put

`S0=u(p+u-2)+p(p-1)`.

A direct parity evaluation of `S0-C0` gives, for `lambda=2r`,

`S0-C0=p^2+pu+u^2-(2r+4)(p+u)+2r^2+2r+4`,

and for `lambda=2r+1`,

`S0-C0=p^2+pu+u^2-(2r+5)(p+u)+2r^2+4r+6`.

As lambda increases by one while `lambda<=p-2`, this difference is nonincreasing; the two alternating step sizes are

`lambda+2-p-u` and `lambda+1-p-u`,

so the minimum occurs at `lambda=p-2`.

At that endpoint:

- if p is even,

  `S0-C0=[p^2-6p+2u^2-4u+8]/2`;

- if p is odd,

  `S0-C0=[p^2-6p+2u^2-4u+9]/2`.

For every p>=5 this is strictly positive for all u>=0. For p=3 or p=4 it is nonpositive only for `u in {0,1,2}`; moving lambda below p-2 makes the difference positive in those remaining cases.

Hence:

> **Zero-gap finite-order theorem.** For p>=3, any above-M(n) graph reaching this one-code rigid near-rigid interface with c=0 must have
>
> `lambda=p-2`,
>
> `(p,u) in {(3,0),(3,1),(3,2),(4,0),(4,1),(4,2)}`.       `(WC-Z0-7)`

Equivalently `y=1`, and its order is at most

> **`n<=18`.**                                            `(WC-Z0-8)`

This does **not** prove that any of the six tiny parameter tuples is realizable. The graph-level rigid-fixture regression currently realizes none with `x>=3`.

## 7. Trust boundary and next move

The new structural input is only the same-code crowding argument `(WC-4)--(WC-8)` and its c=0 specialization. It uses:

1. the independently repaired full coded-layer same-code criticality theorem;
2. the independently repaired ordered `(source,witness)` injection;
3. the already audited rigid singleton-head localization;
4. elementary maximum-degree counts.

`(WC-10)--(WC-12)` additionally use the preserved private-coordinate Hamming-slot theorem and gamma-collision floor. The zero-gap finite-order theorem uses only the standard above-M score ceiling after the exact physical geometry has been established.

`X_3` is untouched: it has lambda=4,p=4,u=0 and does not satisfy c=0 in this rigid one-code setup.

The next attack should keep the actual escape count `d_U^*=u-k<=c`. For c>0, W still contains all but at most c U vertices. The useful refinement of `(WC-4a)` is to retain the active Y--W witness set together with the c-unit Y adjacency budget, rather than immediately replacing it by y-1. In parallel, exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` should be intersected with `(WC-10)` before any total-score collapse.