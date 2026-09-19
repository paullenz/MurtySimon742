# One-code bidirectional certificate reservoir

Date: 2026-09-19

Status: internal hand-theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

The published order-12, size-32 graph `X_3` remains a mandatory hostile control. Nothing here asserts an all-order second-extremal theorem.

## 1. Audit reconciliation and reason for this move

The 19 September daily red-team audit required the graph-to-source/Hall interface to be independently repaired before further downstream theory. That obligation has now been met at the selected source-tuple level and extended by the independent actual-graph Hall/pair-capacity regression in `2026-09-19-rigid-graph-regression-v1`.

The same audit then prioritized the exact one-code rigid branch, retaining pair-local geometry rather than collapsing immediately to a global scalar. `ONE_CODE_PAIR_PURIFICATION.md` established pair purity, `h_P=0`, the sharper gamma-versus-U witness count `k=(x-g_P)_+`, `(ONE-P)`, `(CHAN-P)`, and residual feedback.

This note follows that priority. The new observation is that the same physical `Y x U_{\bar d}` nonedges which carry the A/U certificate channel are also the only possible certificate reservoir for two families of same-code edges. Those uses are mutually exclusive because a fixed physical source/witness pair has a fixed singleton common-neighbour set. This turns a capacity estimate into a structural conservation law.

No mixed `{4,5}` ladder is reopened. The four-exception gate remains subordinate.

---

## 2. Setup

Use the rigid one-code notation from `ONE_CODE_PAIR_PURIFICATION.md`.

Let `X` be a rigid Hall family with

`x=|A_X|>=3`,

`Y=A\A_X`, `y=|Y|>=1`,

and complete cut `X--Y`, with every crossing edge choosing its criticality source in `Y`.

Assume all vertices of `Y` have one tight Boolean code `d`, and put

`P={d,\bar d}`.

Pair purity gives

`A_d=Y`, `A_{\bar d}=emptyset`.

Write

- `g=g_P` for the number of tight fibres whose gamma pair is `P`;
- `k=(x-g)_+`;
- `U_+=U_d`, `u_+=|U_+|`, `E_+=sum_{w in U_+} epsilon_w`;
- `U_-=U_{\bar d}`, `u_-=|U_-|`, `E_-=sum_{w in U_-} epsilon_w`;
- `L_Y=sum_{z in Y} epsilon_z`;
- `L=lambda+1`;
- `T0=a-p=p+u-lambda-1`.

Let

`e_+=e(G[Y union U_+])`,

`e_-=e(G[U_-])`.

Finally let `C_P` be the A/U unique-common-neighbour traffic sourced in the outside pair `P`, exactly as in the purified one-code theorem. For `g<=x`, that theorem gives

`C_P >= yk+e(Y)`.

The interesting case below is `k>0`; all inequalities remain formally true when `k=0`.

---

## 3. First structural unit: the same-code `U_+` layer is independent

### Lemma 3.1 — `U_d` independence

> `e(G[U_+])=0`.                                          `(U+IND)`

### Proof

The full coded-layer same-code localization theorem says that a same-code edge with source in `U_d` requires its unique-common-neighbour witness in `A_{\bar d}`. Pair purity gives `A_{\bar d}=emptyset`. Equivalently, the preserved same-code U-edge capacity

`e_U(d)<=|U_d||A_{\bar d}|`

has zero right side. Hence `U_+` is independent. `square`

Consequently

> `e_+=e(Y)+e(Y,U_+)`.                                    `(3.1)`

This matters because every extra same-code edge in the `d` cylinder beyond the already-counted internal `Y` edges is a `Y--U_+` edge and has only one possible source orientation.

---

## 4. Second structural unit: three channels share one physical reservoir

### Lemma 4.1 — orientation of the two auxiliary same-code channels

Every edge of `G[Y,U_+]` admits a same-code criticality certificate whose source lies in `Y` and whose witness lies in `U_-`.

Every edge of `G[U_-]` admits a same-code criticality certificate whose source lies in `U_-` and whose witness lies in `Y`.

### Proof

For a `Y--U_+` edge both endpoints have code `d`. A certificate sourced at the `U_+` endpoint would require its witness in `A_{\bar d}`, which is empty. Thus the source must be the `Y` endpoint; same-code localization then puts the witness in `V_{\bar d}=U_-`.

For a `U_---U_-` edge, the source is an unmatched vertex of code `\bar d`. The same-code U-source clause forces the witness into `A_d=Y`. `square`

### Lemma 4.2 — physical-pair exclusivity

Choose one certificate for each object in the following three disjoint edge/traffic families:

1. each A/U traffic unit counted by `C_P`;
2. each edge of `G[Y,U_+]`;
3. each edge of `G[U_-]`.

Map the chosen certificate to its underlying **unordered physical pair** `{s,w}` with `s in Y`, `w in U_-`.

> This map is injective across the union of all three families.          `(PAIR-INJ)`

### Proof

Within each family, the usual unique-common-neighbour injection applies: a fixed source/witness pair has a fixed singleton common-neighbour set and therefore determines the head.

It remains to rule out collisions between families. For a fixed physical pair `{s,w}` with `s in Y`, `w in U_-`, the set

`N(s) cap N(w)`

is independent of which orientation is being discussed.

- A certificate counted by `C_P` has its head in `A` (it certifies an A-edge).
- A certificate of a `Y--U_+` edge has its head in `U_+`.
- A certificate of a `U_---U_-` edge has its head in `U_-`.

These three head sets are pairwise disjoint. The same physical pair therefore cannot certify objects from two different families. `square`

This is the key new conservation law: the two orientations of a physical `Y--U_-` nonedge do not create two independent capacities, because the common-neighbour singleton is a property of the unordered pair.

---

## 5. Third structural unit: exact bidirectional reservoir inequalities

There are exactly `y u_-` physical pairs in `Y x U_-`.

### Theorem 5.1 — unweighted reservoir

> `C_P+e(Y,U_+)+e_- <= y u_-`.                            `(RES)`

Using `C_P>=yk+e(Y)` and `(3.1)`,

> `yk+e_++e_- <= y u_-`.                                 `(RES0)`

Equivalently,

> `e_++e_- <= y(u_--k)`.                                 `(RES-EXCESS)`

In particular,

> `u_- >= k`.                                             `(5.1)`

The previously known witness-population lower bound is thus the zero-edge special case of a stronger statement: every unit of same-code edge mass in the two aligned cylinders consumes physical complement capacity that would otherwise be available to the mandatory crossing witnesses.

### Theorem 5.2 — weighted reservoir

Every used physical pair satisfies the unique-common-neighbour slack inequality

`epsilon_s+epsilon_w>=L`.

Since each `s in Y` occurs in at most `u_-` physical pairs and each `w in U_-` in at most `y`, injectivity gives

> `L[C_P+e(Y,U_+)+e_-]`
> ` <= u_- L_Y+yE_-`.                                     `(WRES)`

Hence

> `L[yk+e_++e_-] <= u_- L_Y+yE_-`.                       `(WRES0)`

This is stronger than treating the A/U channel and same-code crowding as separate scorecard consumers.

---

## 6. Fourth structural unit: crowding closes against reservoir excess

The exact coded-layer crowding inequalities apply on both sides of the pair.

For code `d`, use `N_d=y+u_+`, `t_d=u_+`, `S_d=L_Y+E_+`. Since `U_+` is independent,

> `2e_+ >= [(y+u_+)(y+u_+-T0)-u_+-(L_Y+E_+)]_+`.        `(CROWD+)`

For code `\bar d`, there is no A-mass, so

> `2e_- >= [u_-(u_--T0-1)-E_-]_+`.                       `(CROWD-)`

Combining with `(RES-EXCESS)` gives the local cylinder inequality

> `[(y+u_+)(y+u_+-T0)-u_+-(L_Y+E_+)]_+`
> ` +[u_-(u_--T0-1)-E_-]_+`
> ` <= 2y(u_--k)`.                                        `(CYL)`

This is an exact structural necessary condition, not a finite-scan rule.

### Corollary 6.1 — scorecard-relaxed cylinder gate

For an above-`M(n)` candidate, `S=L_A+E_U<=C0`. In particular

`(L_Y+E_+)+E_-<=C0`.

Put

`D_+(t)=(y+t)(y+t-T0)-t`,

`D_-(s)=s(s-T0-1)`.

Then every survivor must admit integers

`k<=s<=u`, `0<=t<=u-s`

such that

> `[D_+(t)]_+ + [D_-(s)]_+ -2y(s-k) <= C0`.              `(CYL0)`

Define the explicit finite local functional

> `Theta(y,k;T0,u)`
> ` := min_{k<=s<=u, 0<=t<=u-s}`
> `    {[D_+(t)]_+ + [D_-(s)]_+ -2y(s-k)}`.              `(THETA)`

Then

> `Theta(y,k;T0,u)<=C0`                                   `(THETA-GATE)`

is necessary for every rigid one-code above-threshold survivor.

This minimization is small and structural. For fixed `s`, `D_+(t)` is a convex quadratic, so its minimizing integer `t` is one of the two integers nearest

`(T0+1-2y)/2`,

clamped to `[0,u-s]`. Thus `(THETA)` reduces exactly to a one-dimensional scan over `s`, and if `2y>=T0+1` the minimizing choice is simply `t=0`.

The point is not the scan itself: `(CYL)` says why a large complementary unmatched class cannot be used freely to supply witnesses. Once `u_-` exceeds the mandatory `k`, its own same-code crowding, together with crowding on the `d` side, starts consuming the very `Y x U_-` certificate reservoir that the extra population was meant to provide.

---

## 7. Fifth structural unit: equality / near-saturation geometry

Write

`z=u_--k>=0`.

Then `(RES-EXCESS)` says

> `e_++e_-<=yz`.                                          `(7.1)`

So `z` has a direct interpretation: it is the **entire edge-room budget**, measured in blocks of `y`, for both aligned same-code cylinders.

### Theorem 7.1 — saturated reservoir classification

Assume `k>0` and

> `u_-=k`.                                                `(SAT)`

Then all of the following hold:

1. `e_+=e_-=0`;
2. `Y` is independent;
3. there are no `Y--U_+` edges;
4. `U_-` is independent;
5. `C_P=yk`;
6. every physical pair in `Y x U_-` is used by exactly one A/U certificate;
7. if `g<=x` (so `g+k=x`), then the matched traffic also saturates:
   `P_P=yg`;
8. every outside source uses all `g` gamma-`d` matched feet and all `k` vertices of `U_-` as its `x` crossing witnesses;
9. the `g+k=x` witness objects have pairwise distinct singleton neighbours in `X`, and those neighbours exhaust `X`.

Thus the crossing certificate system is a complete rectangular product

> `Y x (Gamma_d union U_-)`,

with `|Gamma_d|=g`, `|U_-|=k`, and the witness side in bijection with the `x` heads of `X`.

### Proof

With `u_-=k`, `(RES-EXCESS)` forces `e_+=e_-=0`, giving items 1--4. The lower bound `C_P>=yk+e(Y)` and the upper bound `(RES)` now give `C_P=yk`, proving item 5; injectivity and equality with all `yk` physical pairs gives item 6.

The total pair traffic satisfies `t_P>=xy+e(Y)=xy` and `t_P=P_P+C_P`. Since `C_P=yk`,

`P_P>=y(x-k)=yg`.

The purified matched bound gives `P_P<=yg`, hence equality. Therefore every one of the `yg` possible source/gamma-foot incidences is used, while item 6 says every source/unmatched-witness incidence is used. This proves item 8.

Every crossing witness has exactly one neighbour in `X`, because the source is adjacent to the entire complete cut and the source/witness common neighbourhood is a singleton. For a fixed source the `x` crossing edges have distinct heads, so the `g+k=x` witness objects have distinct `X` neighbours and cover `X`. `square`

This equality model is much sharper than the old population statement `u_->=k`. If later inequalities drive `u_--k` to zero or one, the graph geometry becomes nearly explicit rather than merely numerically constrained.

---

## 8. Sixth structural unit: a capacity surcharge in the global scorecard

The weighted reservoir can be converted into a compact scorecard floor while retaining the gamma and U-witness payments.

Assume the `g0=p-y>=1` branch, so the purified theorem gives

`E_- >= E0:=k(p-1)`.

Let

`A0:=phi(g)`, where `phi(g)=g(g-1)` for `g>=3` and `phi(g)=0` for `g<=2`.

The gamma-collision theorem gives `L_A>=A0`. Put

`R:=yk+e_++e_-`.

### Theorem 8.1 — reservoir score surcharge

Every such one-code survivor satisfies

> `S=L_A+E_U`
> ` >= A0+E0`
> `    +ceil( [L R-u A0-y E0]_+ / max(u,y) )`.            `(SUR)`

In particular, using only `R>=yk`,

> `S >= A0+E0`
> `    +ceil( [Lyk-u A0-y E0]_+ / max(u,y) )`.            `(SUR0)`

### Proof

Write

`L_A=A0+A1`, `E_U=E0+E1`, with `A1,E1>=0`.

Since `u_-<=u`, `L_Y<=L_A`, and `E_-<=E_U`, `(WRES0)` implies

`LR <= uA0+yE0+uA1+yE1`
`   <= uA0+yE0+max(u,y)(A1+E1)`.

Rearrange and use integrality. `square`

For an above-threshold graph, `S<=C0`, so `(SUR)` is an immediate contradiction whenever its right side exceeds `C0`.

### Directional residual feedback

The same weighted inequality and `S<=C0` can force *which side* of the scorecard must carry the payment.

If `y>u`, then

`LR <= uL_A+yE_U <= uC0+(y-u)E_U`,

so

> `E_U >= ceil([LR-uC0]_+/(y-u))`.                        `(EU-CAP)`

Let

`Enew=max(E0, ceil([LR-uC0]_+/(y-u)))`.

Using the already established one-code deficit

`Z>=k(a-1)=u(p-lambda)+2q+E_U`

in inequality form gives

`2q+E_U >= k(a-1)-u(p-lambda)`.

Hence the exact integer minimization yields

> `q+E_U >= Enew`
> ` +ceil([k(a-1)-u(p-lambda)-Enew]_+/2)`.                `(QE-RES)`

Substitution into

`f=(p-lambda)(p+u)+q+E_U-delta`

feeds the reservoir payment directly into the rooted residual defect ledger.

If `u>y`, the symmetric argument forces A-slack instead:

> `L_A >= ceil([LR-yC0]_+/(u-y))`.                        `(LA-CAP)`

If `u=y`, the necessary condition is simply

> `LR<=uC0`.                                              `(BAL-CAP)`

This directional split is useful because only the `y>u` side automatically strengthens the residual/A-edge lower bound; the `u>y` side instead strengthens the Hamming/collision side of the argument.

No new lower bound for the rooted triangle count `Q` is claimed here: extra payment can move between `q` and `E_U`, so the exact residual ledger must be respected rather than double-counted.

---

## 9. Diagnostic consequence

A deliberately generous finite diagnostic accompanies this note. It does **not** enumerate D2C graphs. It asks only whether the scorecard-relaxed cylinder gate `(THETA-GATE)` can hold after the previously established gamma/U score floors.

Over the same coarse box used by the purified one-code audit (`3<=p<=18`, `1<=u<=18`):

- old one-code population-feasible states: `106,368`;
- states rejected already by the shared gamma plus U-witness score floor: `16,967`;
- states rejected after adding the new, deliberately relaxed bidirectional-reservoir/crowding gate: `17,877`;
- additional rejections from the reservoir gate: `910`.

The gate used for this count is intentionally weaker than `(CYL)`: it gives the entire global scorecard `C0` to the two crowding deficits and ignores the gamma/U placement constraints while minimizing over every possible `u_-,u_+`. Therefore a rejection is robust as an arithmetic consequence of the hand inequalities; survival is not graph evidence.

The numerical gain is secondary to the structural point: the extra complementary unmatched population that was previously treated only as witness capacity has now acquired an exact competing cost through same-code edge criticality.

---

## 10. Mandatory negative control

`X_3` remains untouched. At its canonical cube root,

`u=0`, `A` is independent, and there is no nontrivial rigid complete A-cut in the present branch. Thus `k>0` and the `Y x U_-` reservoir never arise.

The larger cube-face controls `X_4,X_5` likewise lie outside the tight-fibre one-code branch (`p=0` at the canonical root used by the regression). The new conservation law therefore does not accidentally exclude the known order-12 counterexample or reinterpret exact residual saturation as sufficient for extremality.

---

## 11. Trust boundary and next move

What is hand-derived here:

- `U_d` independence from pair purity and same-code U-source localization;
- physical-pair exclusivity across the A/U, `Y--U_d`, and `U_{\bar d}--U_{\bar d}` channels;
- exact unweighted and weighted reservoir inequalities;
- the crowding/reservoir cylinder gate;
- the saturated-reservoir equality geometry;
- the scorecard surcharge and directional residual feedback.

What remains conditional:

- existence of a realizable rigid cut with `x>=3` is still not witnessed in the bounded actual-graph corpus;
- the entire note therefore remains a conditional structural theorem inside that branch, not empirical evidence that the branch occurs;
- no eventual second-extremal theorem is claimed.

The highest-value next move is now to use `(CYL)` and the saturated/near-saturated classification against the remaining one-code geometry **before** introducing another global relaxation. In particular:

1. classify `u_--k=0,1,2` exactly;
2. in the `2y>=T0+1` regime, eliminate `u_+` from `(THETA)` and solve the one-variable `u_-` quadratic exactly;
3. feed any surviving near-saturated geometry through `(QE-RES)` and the rooted `delta=r-f` ledger;
4. only if a genuine asymptotic family survives should attention return to the non-rigid Hall branch.
