# Minimal-reservoir noncheap Hamming concentration/density theorem

Date: 2026-09-19

Status: internal structural theorem package for the eventual / sufficiently-large dense diameter-2-critical programme around `M(n)=floor((n-1)^2/4)+1`. This remains conditional on the rigid one-code complete-cut hypotheses. It is not a graph-realizability theorem and does not assert the false all-order 2019 Dailly–Foucaud–Hansberg conjecture.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, `README.md`, the latest commits, the 19 September daily red-team audit, `SOURCE_PREMISE_REPAIR.md`, and `RIGID_GRAPH_LEVEL_REGRESSION.md`.

The audit boundary is unchanged and binding:

- distinct physical beta-source identity is proved from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a selected-representative statement, not raw witness uniqueness;
- the finite source-tuple theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression still has zero recorded graph/formula mismatches and retains `X_3` as the mandatory hostile control;
- no bounded-corpus D2C graph realizes the full rigid complete-cut hypotheses, so the mathematics below is a conditional hand implication;
- exact pair-local `S_P/Ccap_P` remains mandatory; `(ONE-P)` and `(CROWD)` remain consequences of stronger physical bills only in the already-identified equality geometry;
- the four-exception gate remains subordinate.

The predecessor explicitly identified the non-Hamming-cheapest `m=g+1` branch as the bottleneck and asked for the exact distribution of extra Hamming units to be intersected with pair-forced density. This note follows that priority and does not open `m=g+2`, `z=2`, loaded buffer, extra buffer slack, or the closed mixed `{4,5}` ladder.

## 2. Retained setup

Stay in the positive-buffer unloaded common-buffer rigid one-code branch with minimal outside reservoir `m=g+1`:

- `X--Y` is complete, `x>=3`, `y>0`, `a=x+y`;
- every Y-vertex has code `d`;
- `X=H_M dotcup H_0`, with `|H_M|=g`, `|H_0|=k=x-g>0`;
- `H_0` has one common code `c_*`, is independent, and the `H_M` codes are pairwise distinct singleton A-code classes;
- no X-code equals `d` or `bar d`;
- exact pair/Hall variables `A,M,D(A,M),H(A,M),B_P,sigma_P` and the pair-forced X-density theorem from the predecessor remain in force;
- for every A-vertex z, the preserved local theorem is

  `sum_{w in N_A(z)} d_H(c(w),c(z)) <= r_z d_A(z)`,

  with `sum_{z in A} r_z=r`.

For `v in X` define

`h_v:=d_H(c(v),d)`,

`e_v:=h_v-1>=0`,

and put

`E:=sum_{v in X} e_v = H_X-x`.

The present note treats the non-cheapest branch `E>=1`.

Because every H_M code is a singleton A-code class, H_0 is independent, and the H_0 code cannot equal an H_M singleton code, every internal X-edge joins distinct codes.

For `vw in E(G[X])` define the internal Hamming excess

`rho_vw:=d_H(c(v),c(w))-1>=0`,

and for `v in X`

`tau_v:=sum_{w in N_X(v)} rho_vw`.

## 3. Unit I — exact vertexwise noncheap slot decomposition

### Theorem 3.1

Every `y0 in Y` satisfies

`r_{y0} >= 1 + ceil(E/x)`.

Every `v in X` satisfies

`r_v >= 1 + ceil((y e_v + tau_v)/(y+d_X(v)))`.

Consequently

> **`r >= a + y ceil(E/x)`**
> **`    + sum_{v in X} ceil((y e_v+tau_v)/(y+d_X(v))).`**   `(DIST-SLOT)`

### Proof

For `y0 in Y`, `d_A(y0)=x` and the Hamming length of its x crossing edges is

`sum_{v in X} h_v=x+E`.

Apply the local slot theorem.

For `v in X`, the y crossing edges contribute `y(1+e_v)`. Every internal edge `vw` contributes `1+rho_vw`. Hence the local Hamming numerator is

`y+d_X(v)+y e_v+tau_v=d_A(v)+y e_v+tau_v`.

Apply the local slot theorem and integrality. Summing the disjoint X and Y contributions proves `(DIST-SLOT)`. `square`

This is the exact distributional strengthening requested by the previous handoff; it retains where the extra Hamming units live instead of replacing them immediately by `H_X>=x+1`.

## 4. Unit II — the old noncheap floor was always missing at least one X-slot

If `E>=1`, some X-vertex has `e_v>0`. For that vertex the second term in Theorem 3.1 is positive, so it pays at least one extra slot beyond its universal baseline one. Every Y-vertex also pays at least one extra slot because `ceil(E/x)>=1`.

Therefore every non-cheapest survivor satisfies

> **`r>=a+y+1`.**                                           `(NONCHEAP+1)`

The predecessor bound `r>=a+y` was safe but not sharp: a nonzero Hamming defect cannot be paid entirely on the Y side because the X-vertex carrying the defect itself sees all y crossing edges.

More generally, if

`P={v in X:e_v>0}` and `s=|P|`,

then every vertex of P pays an extra X-slot, so

> `r>=a+y ceil(E/x)+s`.                                     `(SUPPORT0)`

## 5. Unit III — concentration/dispersion via the radius-one remainder

Let `Z=X\P`, so every vertex in Z has Hamming radius exactly one from d. Any edge inside `G[Z]` joins two distinct one-flip codes and therefore has Hamming distance exactly two. Thus every endpoint of an edge in `G[Z]` has `tau_v>0` and pays an additional X-slot.

Let

`j_0:=e(G[Z])`.

If `mu(j)` denotes the least q with `binom(q,2)>=j` (and `mu(0)=0`), then at least `mu(j_0)` vertices of Z are incident to these edges. Hence

> **`r>=a+y ceil(E/x)+s+mu(j_0)`.**                         `(CD1)`

Only

`binom(x,2)-binom(x-s,2)`

edges of G[X] can have at least one endpoint in P. Therefore

> `j_0 >= [ e(X)-binom(x,2)+binom(x-s,2) ]_+`.             `(CD2)`

Combining,

> **`r>=a+y ceil(E/x)+s`**
> **`    +mu([e(X)-binom(x,2)+binom(x-s,2)]_+).`**          `(CD3)`

This is the desired concentration/dispersion mechanism. Spreading the extra Hamming units raises s directly. Concentrating them leaves many radius-one vertices; pair-forced density then creates radius-one/radius-one edges, and those edges force further local slot surcharge.

## 6. Unit IV — exact feasible support sizes respect the H_0 block

The k vertices of H_0 share one code, so their Hamming excess is a common integer `e_*`. The g vertices of H_M have individual excesses `e_1,...,e_g`. Since X contains neither d nor `bar d`, every excess lies in `[0,p-2]` and

`E=k e_*+sum_i e_i`.

Thus the support size s is not an arbitrary integer. Let `q=p-2` and define `S(E)` as follows.

Core-cheap (`e_*=0`): if `E<=gq`, any feasible number l of positive H_M excesses satisfies

`ceil(E/q)<=l<=min(E,g)`,

and contributes support `s=l`.

Core-noncheap (`e_*>=1`): for some `e_* in {1,...,q}`, put `R=E-k e_*`. Necessarily `0<=R<=gq`; if `R=0`, `s=k`; if `R>0`,

`ceil(R/q)<=l<=min(R,g)`

and `s=k+l`.

These are exactly the support sizes permitted by the block multiplicity, ignoring only the finer question of which concrete Boolean supports realize the radii.

Define the block concentration/dispersion floor

`Gamma(E,e):=`

` min_{s in S(E)} { s + mu([e-binom(x,2)+binom(x-s,2)]_+) }`.

Then every actual noncheap geometry satisfies

> **`r>=a+y ceil(E/x)+Gamma(E,e(X)).`**                     `(BLOCK-CD)`

A useful immediate subcase is: if `e_*>0`, all k core vertices themselves carry Hamming defect, hence

> **`r>=a+y ceil(E/x)+k >= a+y+k`.**                       `(CORE-NONCHEAP)`

So the cheapest possible noncheap geometry is pushed toward `e_*=0`, with defect concentrated among matched heads.

## 7. Unit V — parity turns pair-forced density into Hamming excess on edges

For binary codes,

`d_H(c(v),c(w)) = |S_v triangle S_w|`,

where `|S_v|=h_v=1+e_v`. Hence the parity of the internal Hamming distance equals the parity of `h_v+h_w`, equivalently the parity of `e_v+e_w`.

If `e_v` and `e_w` have the same parity, an internal edge has positive even Hamming distance, hence at least two. Therefore `rho_vw>=1` on every same-parity internal edge.

Let m be the number of X-vertices with odd e_v. At most `m(x-m)` internal edges are opposite-parity, so

`sum_{vw in E(X)} rho_vw >= [e(X)-m(x-m)]_+`.

Because every odd positive excess uses at least one unit of E, `m<=min(E,x)`. Define

`C_x(E):=max_{0<=m<=min(E,x)} m(x-m)`.

Equivalently,

- `C_x(E)=E(x-E)` while `E<x/2`;
- `C_x(E)=floor(x^2/4)` once `E>=x/2`.

Then

> `sum rho_vw >= [e(X)-C_x(E)]_+`.                         `(PAR1)`

Also

`sum_{v in X}(y e_v+tau_v)=yE+2 sum rho_vw`.

Since every denominator `y+d_X(v)<=a-1`, the total integer X-surcharge in `(DIST-SLOT)` is at least

> **`ceil((yE+2[e(X)-C_x(E)]_+)/(a-1)).`**                 `(PAR2)`

Thus the block-support and parity-density mechanisms may be combined safely:

> **`r>=a+y ceil(E/x)`**
> **` + max{ Gamma(E,e(X)),`**
> **`          ceil((yE+2[e(X)-C_x(E)]_+)/(a-1)) }.`**     `(N-FLOOR)`

This is a compact structural statement: density cannot be hidden merely by choosing where to place the noncheap code radii.

## 8. Unit VI — feed the theorem back into the exact pair/Hall row

For an admissible allocation `(A,M)`, retain the predecessor exact pair-local gate

`H(A,M)<=B_P=C0-O_0-sigma_P`

and the pair-budget X-density lower bound

`2e(X)>=Q_H+g(g-1)-B_P+2A-(k-1)M`.

Define

`e_min(A,M):=`

` max(0, ceil((Q_H+g(g-1)-B_P+2A-(k-1)M)/2)).`

Both terms in `(N-FLOOR)` are monotone in `e(X)`, so it is safe to replace `e(X)` by `e_min(A,M)`.

Define the row-wise noncheap slot floor

`R_N(A,M):=`

` min_{1<=E<=x(p-2), S(E) nonempty}`

` { a+y ceil(E/x)`

`   +max( Gamma(E,e_min(A,M)),`

`          ceil((yE+2[e_min(A,M)-C_x(E)]_+)/(a-1)) ) }`.

The exact rooted residual upper budget from the predecessor remains

`r <= (p-lambda)(p+u)`

`     +binom(u,2)-binom(k+1,2)-k-M`

`     +C0-Y_0-[D(A,M)]_+`.

Therefore an actual noncheap `m=g+1` survivor must have at least one pair/Hall-admissible `(A,M)` for which that upper budget is at least `R_N(A,M)`.

This is the first direct intersection of the exact pair-local density theorem with a distribution-sensitive Hamming slot floor. It preserves `S_P/Ccap_P`; no pair-local score is donated back to the global total.

## 9. Interpretation and next work

The noncheap branch has become a finite structural optimizer with a clear geometric meaning rather than the coarse scalar `r>=a+y`.

The immediate strongest consequences are:

1. every noncheap state costs at least `a+y+1` rooted slots;
2. a core-code defect costs all k core heads at once;
3. concentrating defect on a few matched heads leaves a large one-flip remainder, on which pair-forced X-density creates extra length-two edges;
4. dispersing defect raises the number of defect-bearing X-vertices directly;
5. parity gives an independent density-to-Hamming-excess conversion even when the one-flip remainder estimate is weak;
6. all of these can be tested row-by-row against the already-audited exact pair-local and residual budgets.

No full bounded-box replay is promoted in this checkpoint. The theorem is preserved first; the next run should implement `R_N(A,M)` independently, replay it against the previous 64,557 abstract survivors, inspect the `t=1` slice first, and then attack any equality geometry selected by the optimizer. If the optimizer consistently chooses `E=1`, classify the unique one-defect matched-head geometry directly. If it chooses core defect or larger E, use `(CORE-NONCHEAP)` and the parity term before opening any larger reservoir.

`X_3` remains outside the hypotheses (`u=0`, no active rigid complete A-cut) and is untouched.