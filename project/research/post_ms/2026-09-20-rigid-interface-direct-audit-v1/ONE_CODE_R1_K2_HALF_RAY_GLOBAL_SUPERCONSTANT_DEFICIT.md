# Residual-one k=2 half-ray: global superconstant residual-slot deficit

Date: 2026-09-20

Status: **same-session conditional structural theorem, pending the midnight red-team audit.** It is downstream of the corrected rigid one-code residual-one interface, the repaired H--U B-layer classification, the independently replayed residual-slot collapse theorem, and the H--H private-foot certificate split. It does **not** use the superseded H--U private-foot coordinate-slice chain. Bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.

## 1. Setup

On the corrected intermediate half-ray

- `p=2t`, `c=y=t`, `u=t+1`, `h=|H|=2t-1`,
- `k=2`, `J2=empty`,
- `Delta=a+b+c0`, where `a=2M_H-R_q`, `b=h-R_j`, `c0=(u-2)-S`,
- `N=R_j=h-b` is the number of residual-`q_j`-saturated H-sources,
- `P=U_j^-` is the residual-bar U column and `g=|U\P|`.

The predecessor residual-slot theorem, independently replayed this session, gives

`a+c0 >= binom(N,2)`

and therefore

`Delta >= h-N+binom(N,2)`.

Write

`s=Delta-h >= 0`.

Then

`a+c0=s+N`                                                `(SC-1)`

and the stability inequality gives

`N <= R(s):=(3+sqrt(9+8s))/2`.                            `(SC-2)`

For convenience put

`D=s+R(s)`.

Thus `a<=D` and `c0<=D`.

## 2. Equality at the predecessor barrier is impossible for t>=5

The predecessor theorem gave `Delta>=h`. This session classified all equality faces `Delta=h`. By `(SC-2)`, `N<=3`.

### N=3

Here `a+c0=3`. The three saturated rows are independent. A D=0 carrier loses both internal reverse-private slots; recovering both requires a D=2 carrier whose D-set is exactly the other two saturated indices. The carriers must be physically distinct. Hence equality forces

`a=0`, `c0=3`,

with three distinct D=2 carriers and the saturated triple complete to every unsaturated H-row.

Each such carrier is then forced H-degree one: for an edge from its saturated row to an unsaturated row, the carrier sees the opposite private foot, so the only valid H--H private-foot orientation is sourced at the unsaturated row; its singleton equation forbids the carrier from seeing that row. The physical-slot equality forces `g=0`. B1 cannot touch any H-row, endpoint-indexed vertices are H-free, and the carriers' only H--U edges are already assigned to `R_j`. Therefore `S=0`, contradicting `S=t-4` for `t>=5`.

### N=2

The internal mutual holes and physical D=2 carrier count reduce the equality allocations to the same small list analyzed in the session ledger. In the potentially cheapest allocation `a=0,c0=2`, two distinct D=2 carriers are required and both are forced H-degree one. The physical-slot count forces `g=0`. A B1 shared resource can touch only an unsaturated row missed by both saturated rows; there is at most one such row. Two B1 vertices on it would block every reverse-private certificate sourced there, contradicting `a=0`. Hence at most one B1 shared edge exists, while endpoint-indexed resources are H-free and the two carrier edges are already `R_j`. Thus `S<=1`, contradicting `S=t-3` for `t>=5`. The allocations `(a,c0)=(2,0),(1,1)` have still less usable shared capacity once their residual carriers are accounted for.

### N=1

Here `a+c0=1`. If `c0=0`, the residual carrier consumes a physical shared slot but its sole H--U edge is already `R_j`, contradicting full shared saturation. If `a=0,c0=1`, a D=0 carrier makes the saturated H-row universal and again leaves no usable linear shared supply. A D=2 carrier consumes the unique non-shared slot and has H-degree one. B1 vertices can occur only on at most two exceptional H-rows indexed by the carrier D-set; because `a=0`, each such row supports at most one B1 neighbour. Hence `S<=2`, contradicting `S=t-2` for `t>=5`.

### N=0

Now `a=c0=0`, so `R_j=0`, `R_q=2M_H`, and `S=u-2`. Equality in shared-resource capacity forces every vertex of `U\W_s` to be B1 or endpoint-indexed and used by the shared block. Endpoint-indexed vertices are H-anticomplete, so every H--U edge is incident with B1 and

`e(H,U)<=|B1|<=u-2`.

But the mechanism partition gives

`e(H,U)=2M_H+(u-2)`.

Thus `M_H=0`, H is complete, and all `u-2=t-1` nonselected U-vertices are B1. B1 vertices attached to two distinct H-rows would block both private-foot orientations of the H-edge joining those rows, so all B1 vertices attach to one row `h_*`. The exact local identity gives

`d_U(h_*)=3-epsilon_*<=3`,

but the B1 attachment gives `d_U(h_*)=t-1`. Hence `t<=4`.

Therefore:

> **STRICT BARRIER. For every `t>=5`, `Delta>=h+1=2t`, hence `L_H>=5t-1`.** `(SC-3)`

## 3. B1 rows consume the reverse-private deficit

Let `B1` denote the H-positive `bar d` vertices of H-degree exactly one, and let `T` be the set of H-rows touched by B1.

If two rows in T were adjacent, a B1 neighbour at each endpoint would see the opposite private foot and block both H--H private-foot orientations. Endpoint-indexed U-certificates are unavailable by the replayed EC-1/EC-2 theorem. Hence `T` is independent.

Moreover, if `h_i in T` and `h_i h_l` is a missing H-edge, a B1 neighbour of `h_i` sees `q_l`, so the reverse-private H--U mechanism from source `h_i` through `q_l` is impossible. Thus every missing H-edge sourced at a B1-touched row contributes to `a`:

`a >= sum_{i in T} m_i >= |T|(|T|-1)`.                  `(SC-4)`

The exact local H-degree identity gives

`d_U(h_i)<=m_i+3`.

If `B_i` B1 vertices attach to `h_i`, then `B_i<=m_i+3`. Summing over T,

`|B1| <= a+3|T|`.                                         `(SC-5)`

Define

`rho(a)=(1+sqrt(1+4a))/2`.

From `(SC-4)`, `|T|<=rho(a)`, so

> `|B1| <= a+3rho(a)`.                                    `(SC-B1)`

## 4. H-degree bound for exceptional residual-bar vertices

Take an H-positive `w in P` which is not B1. The raw private-spoke theorem gives a private D-set of size 0 or 2. Every H-neighbour index lies outside D, hence w sees the corresponding private foot `q_i`.

If two H-neighbours were adjacent, w would block both H--H private-foot orientations. Thus `N_H(w)` is independent. Every ordered hole within this H-neighbourhood is also unavailable to `R_q`, because w is adjacent to the source and sees the witness private foot. Therefore

`d_H(w)(d_H(w)-1)<=a`.                                    `(SC-P)`

So `d_H(w)<=rho(a)`.

## 5. New outside-P matched-spoke lemma

Now take an H-positive `w in U\P`. Since w is residual-plus, the residual coordinate j belongs to

`D(w)={r : w selects the d-endpoint p_r}`.

Suppose `h_i in N_H(w)` and `i in D(w)`. Then `w p_i` is a rooted B-edge.

### Reverse orientation is impossible

A witness in A which misses `p_i` must be `h_i` in the `J2=empty` repertoire. But every Y-vertex is adjacent to both `p_i` and `h_i`, so `N(p_i) cap N(h_i)` contains all of Y in addition to the proposed singleton U-head. Since `y=t>0`, reverse orientation cannot certify `w p_i`.

### Forward orientation forces a tiny D-set

For a forward singleton with head `p_i`, the A-witness must agree with w at coordinate i and be fibre-complementary at every other coordinate. Relative to d, its support is exactly

`D(w)\{i}`.

The available A-code supports are only `empty`, `{j}`, and `{l}` for private l. Therefore `D(w)\{i}` has size at most one.

Because `j in D(w)`, two distinct H-neighbour indices i,l cannot both lie in D(w): applying the preceding statement to i would leave both j and l in `D(w)\{i}`.

Hence:

> **at most one H-neighbour of an outside-P U-vertex lies on a d-bit private coordinate.** `(SC-Q1)`

All remaining H-neighbours correspond to bar-bit coordinates, so w sees their private feet. As above, they form an independent H-set and all ordered holes within that set are unavailable to `R_q`. Consequently

> **`(d_H(w)-1)(d_H(w)-2)<=a`.**                          `(SC-Q2)`

Define

`kappa(a)=(3+sqrt(1+4a))/2`.

Then every H-positive outside-P exceptional vertex has `d_H(w)<=kappa(a)`.

## 6. Global shared-resource count

The shared block has size

`S=u-2-c0=t-1-c0`.                                       `(SC-S1)`

Every physical shared resource is either

- a B1 vertex, or
- an endpoint-indexed vertex.

Endpoint-indexed vertices are H-anticomplete. Since the shared-resource universe has size `u-2`, exactly `c0` physical U slots lie outside the used shared-resource set. Thus every H-positive U-vertex is either a B1 vertex or belongs to a set of at most `c0` exceptional physical vertices.

By `(SC-B1)`, `(SC-P)`, and `(SC-Q2)`,

`e(H,U) <= a+3rho(a)+c0 kappa(a)`.                        `(SC-S2)`

Since every shared mechanism is assigned to an H--U edge,

`S<=e(H,U)`.

Using `a,c0<=D`, monotonicity gives the explicit necessary condition

> **`t <= 1+2D+3rho(D)+D kappa(D)`,**                     `(SC-FIN)`
>
> where `D=s+(3+sqrt(9+8s))/2`.

## 7. Superconstant consequence

As `s->infinity`,

`D=s+O(sqrt(s))`,

`rho(D)=sqrt(D)+O(1)`,

`kappa(D)=sqrt(D)+O(1)`.

Therefore `(SC-FIN)` gives

`t <= (1+o(1)) s^(3/2)`.

Equivalently:

> **`s >= (1-o(1)) t^(2/3)`.**                            `(SC-ASYM)`

Since `s=Delta-h` and `L_H=3t-1+Delta`,

> **`Delta >= h+(1-o(1))t^(2/3)`,**
>
> **`L_H >= 5t-2+(1-o(1))t^(2/3)`.**                     `(SC-H)`

This is a superconstant strengthening of the corrected half-ray H-slack barrier. It does not close the full branch against the quadratic score ceiling, but it rules out every fixed-excess saturation pattern and shows that the H--U capacity deficit must diverge polynomially.

## 8. Hostile model and why the matched-spoke lemma matters

Before `(SC-Q1)` was identified, the current equations admitted an abstract `g=1,s=1` star normal form: one outside-P U-head of code d could apparently support `t-2` reverse-U H--U certificates through `t-2` endpoint-indexed witnesses while H stayed complete. This is not an actual graph construction, but it showed that the residual-bar proof did not automatically globalize.

The matched-spoke lemma kills exactly that escape: an outside-P H-head with many H-neighbours cannot have d-bits on more than one of those coordinates; the remaining bar-bit H-neighbourhood creates a quadratic directed-hole bill in a. Thus the same physical deficit controls both P and outside-P exceptional heads.

## 9. Audit status and next task

The predecessor EC-1 through EC-12 chain was independently replayed before this extension. The new equality exclusions and `(SC-Q1)--(SC-ASYM)` are same-session results and should be the first target of the midnight adversarial audit.

Highest-value next task after audit: stress-test `(SC-S2)` for resource-role overlap and then feed the superconstant `L_H` excess into the exact score/rooted ledger. If it survives, the next structural target is to improve the exceptional-head degree bound or couple it to U-slack strongly enough to obtain a linear or quadratic excess. The upstream rigid-interface reachability risk remains unchanged.