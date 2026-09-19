# Minimal-reservoir noncheap replay and one-defect witness-intersection theorem

Date: 2026-09-19

Status: internal structural theorem/checker package for the eventual / sufficiently-large dense diameter-2-critical programme around `M(n)=floor((n-1)^2/4)+1`. Everything below remains conditional on the rigid one-code complete-cut hypotheses. It is not graph-realizability evidence and does not assert the false all-order 2019 Dailly–Foucaud–Hansberg conjecture.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, root `README.md`, the newest commits, the 19 September daily red-team audit, `SOURCE_PREMISE_REPAIR.md`, and `RIGID_GRAPH_LEVEL_REGRESSION.md`.

The audit boundary remains binding:

- distinct physical beta-source identity is proved directly from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a selected-representative statement, not raw-witness uniqueness;
- the finite source-tuple theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression still has zero recorded graph/formula mismatches and retains `X_3` as the mandatory hostile control;
- no bounded-corpus D2C graph realizes the full rigid complete-cut hypotheses, so the mathematics here remains a conditional hand implication;
- exact pair-local `S_P/Ccap_P` stays live; `(ONE-P)` and `(CROWD)` are treated as consequences only where already proved from stronger physical bills;
- the four-exception gate remains subordinate.

There is no departure from the audit's requested priority order. The predecessor explicitly asked first for an independent replay of the distribution-sensitive noncheap floor `R_N(A,M)`, and then for direct classification of the geometry selected by the optimizer.

## 2. Retained setup

Stay in the positive-buffer unloaded common-buffer rigid one-code branch at minimal outside reservoir `m=g+1`:

- `X--Y` is complete, `x>=3`, `y>0`, `a=x+y`;
- every Y-vertex has code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `X=H_M dotcup H_0`, with `|H_M|=g`, `|H_0|=k`;
- `H_0` is one independent code class with common code `c_*` and common selected outside witness `z_*`;
- the H_M codes are pairwise distinct singleton A-code classes, each with its own selected outside witness;
- `A:=g-d_{H_M}(z_*)`, `M:=(u_o-1)-d_{U_o\{z_*}}(z_*)`, `N=u-k-2`;
- `D(A,M)=Q_H-(2k-1)A-kM` and `E_max(A)=binom(g,2)+kA`;
- the predecessor exact pair-local gate, density lower bound `e_min(A,M)`, and rooted residual upper budget remain in force.

For `v in X`, write

`e_v=d_H(c(v),d)-1`, `E=sum_X e_v`.

The present note treats the noncheap branch `E>=1` and then its first optimizer layer `E=1`.

## 3. Unit I — independent replay of the distribution-sensitive noncheap floor

The predecessor theorem defined

`R_N(A,M)=min_E { a+y ceil(E/x)+max(Gamma(E,e_min), parity(E,e_min)) }`,

with the exact feasible support set respecting the k-fold core code, the radius-one remainder surcharge, and the parity-density surcharge.

The companion checker in this package reimplements those support and parity minimizations independently of the theorem text and replays them on exactly the bounded abstract box used by the predecessor diagnostics.

Starting from the 64,557 states that survived the earlier coarse noncheap/sphere dichotomy, the distribution-sensitive noncheap gate leaves

> **64,461 abstract parameter states**,

so it excludes a further

> **96 states**.

The rejection count by `t=p-g` is

`{1:0, 2:1, 3:4, 4:5, 5:7, 6:9, 7:12, 8:7, 9:14, 10:11, 11:10, 12:10, 13:3, 14:2, 15:0, 16:1, 17:0, 18:0}`.

In particular, all 5,404 previous `t=1` states remain. The optimizer nevertheless has a clear signal: on the noncheap-surviving states, `E=1` is the minimum row floor far more often than larger Hamming excess. That makes the one-defect geometry the correct next structural target rather than opening `m=g+2`.

These are arithmetic states, not D2C graphs.

## 4. Unit II — support-intersection localization for selected outside witnesses

For a head-code class with code `c_s`, let `z_s` be its selected outside buffer witness. The A/U localization already gives

`c(z_s)=bar c_s`,

and the buffer-edge certificate gives the singleton relation

`N(h_s) cap N(z_s)={b}`

for every head `h_s` served by `z_s`.

Define the support of an X-code relative to d by

`S(c)={i:c_i!=d_i}`.

### Theorem 4.1 — wrong-head adjacency implies support intersection

If `h` is an X-head not served by `z_s` and `z_s h` is an edge, then

> **`S(c_s) cap S(c(h)) != emptyset`.**                   `(INT)`

### Proof

The edge `z_s h` lies in the triangle through b, so criticality requires one of the two singleton orientations.

In the orientation whose auxiliary witness is paired with `z_s`, no B-vertex can work because every two B-vertices share the root. An A-witness has an additional common A-neighbour forced by the complete X--Y cut or by the head-code multiplicities, and an unmatched U-witness has an additional common neighbour forced by the buffer/core geometry. Thus the only possible surviving location in the reverse orientation is a matched endpoint `q_i` adjacent to `z_s` and nonadjacent to h.

For b not to be a second common neighbour of h and `q_i`, the endpoint selected by `z_s` at coordinate i must be the d-endpoint, not the `bar d` endpoint selected by b. Since `c(z_s)=bar c_s`, this means `c_s` differs from d at i. Since h is nonadjacent to the same matched endpoint, h selects the opposite endpoint and also differs from d at i. Hence `i in S(c_s) cap S(c(h))`. `square`

This recovers the old cheap-sphere anticompleteness when all X supports are distinct singletons, but it remains useful when a small number of Hamming defects are present.

## 5. Unit III — exact one-defect classification

Assume now

> `E=1`.

There is exactly one defect head `h_D` with Hamming radius two from d; every other X-vertex has radius one. If `k>1`, the defect must lie in `H_M`, because a core defect would be repeated k times and contribute at least k units to E. If `k=1`, the defect may lie either in `H_M` or in the one-vertex core.

Let `S_D` be the two-coordinate support of the defect code. All remaining radius-one code classes have distinct singleton supports.

By `(INT)`, every selected outside witness is anticomplete to every wrong head except possibly across a defect/radius-one pair whose singleton coordinate belongs to `S_D`.

In particular, for the common witness `z_*`:

- if `k>1`, the defect lies in `H_M`, and `z_*` can have at most that one H_M neighbour, so

  > **`A in {g-1,g}`;**

- if `k=1`, a core defect is possible and `z_*` can meet at most the two H_M classes whose singleton coordinates lie in `S_D`, so

  > **`g-A<=2`.**

Thus the one-defect branch is forced to the endpoint of the old A-interval: the common witness is missing essentially the whole H_M layer.

## 6. Unit IV — one-defect internal Hamming surcharge

An internal edge has Hamming excess

`rho_vw=d_H(c(v),c(w))-1`.

For two radius-one vertices, `rho=1`. A defect/radius-one edge has `rho=0` only when the radius-one singleton coordinate belongs to `S_D`; otherwise its Hamming distance is three and `rho=2`.

Star separation further limits how many zero-rho defect edges can occur. Define

`c_1(A)=min(2,g-1)` if `A=0`,

and

`c_1(A)=min(x-1,k+1)` if `A>0`.

Then at most `c_1(A)` internal X-edges can have `rho=0` in the one-defect geometry.

Consequently at least

`J_+=[e(X)-c_1(A)]_+`

internal edges have positive Hamming excess. If q radius-one vertices have positive `tau_v`, every positive-rho edge lies inside the vertex set consisting of the defect plus those q vertices, so

`J_+<=binom(q+1,2)`.

Let `eta(j)` be the least q with `binom(q+1,2)>=j`. The local slot theorem therefore sharpens the E=1 row to

> **`r>=a+y+1+eta([e(X)-c_1(A)]_+)`.**                   `(E1-SLOT)`

The `+y` is paid by every Y-vertex, the first `+1` is paid by the defect vertex itself, and the eta-term is paid by radius-one vertices physically incident with positive-Hamming-excess internal edges.

## 7. Unit V — witness-incidence / X-density cancellation

Let

`d:=g-A=d_{H_M}(z_*)`

and

`Delta:=E_max(A)-e(X)>=0`.

Let J be the total number of A-neighbours across the `g+1` selected outside witnesses.

The singleton relation for each selected buffer certificate gives a useful tradeoff: if a selected witness for head h_s is adjacent to a wrong head h, then `h_s h` must be a nonedge, otherwise h is a second common neighbour of `h_s` and the witness.

In the one-defect geometry, the only wrong-head adjacencies are incident with the defect. The `d` adjacencies already encoded by `z_*` can make at most `(k+1)d` selected witness incidences free relative to the star-separation maximum `E_max(A)`. Every further missing permitted X-edge supports at most two directed selected-witness incidences. Therefore

> **`J<=(k+1)d+2Delta`.**                                `(J-DELTA)`

Every selected outside witness w satisfies

`epsilon_w>=p-d_A(w)`.

For the distinguished common witness the exact identity gives an extra `k+M` beyond this generic floor. Hence the selected witnesses contribute

> `sum epsilon_w >= p(g+1)+k+M-J`.                        `(WIT)`

On the Hall side, the exact cut identity and the physical `Z_X` floor give the stronger deficiency form

> **`L_X>=D(A,M)+2Delta`.**                               `(H-DELTA)`

(use `L_X>=0` if the displayed right side is negative).

Combining `(J-DELTA)`, `(WIT)`, and `(H-DELTA)` yields a cancellation: for every `Delta>=0`,

`[D+2Delta]_+-2Delta >= D`.

Therefore the score outside the distinguished pair P obeys the density-free linear lower bound

> **`S-S_P >= p(g+1)+k+M-(k+1)(g-A)+D(A,M)`.**           `(E1-LIN)`

Since exact crossing capacity requires `S_P>=sigma_P`, every one-defect survivor must satisfy

> **`p(g+1)+k+M-(k+1)(g-A)+D(A,M) <= C0-sigma_P`.**      `(E1-PAIR)`

This is the main structural gain of the session. Sacrificing X-density to create more selected-witness A-adjacencies cannot evade the pair bill: the Hall slack generated by the same missing edges cancels the apparent saving two-for-two.

For `t=1`, `g=p-1`, so `(E1-PAIR)` becomes

> `p^2+k+M-(k+1)(g-A)+D(A,M) <= C0-sigma_P`,

with `g-A<=1` for `k>1` and `g-A<=2` for `k=1`.

A weaker but intuitive corollary is that the p selected outside witnesses in the `t=1` one-defect layer contribute at least `p^2+M-3` unmatched slack before Hall slack is added. Thus a single Hamming defect buys only a bounded O(1) escape from the `p^2` cheap-sphere witness bill.

## 8. Unit VI — combined diagnostic after the one-defect theorem

The companion checker keeps all E>=2 rows under the independently replayed `R_N` floor and replaces only the E=1 rows by the new endpoint restriction, `(E1-SLOT)`, and `(E1-PAIR)`.

On the same bounded abstract box:

- earlier coarse noncheap/sphere survivors: `64,557`;
- after exact distribution-sensitive `R_N`: `64,461`;
- after the one-defect structural theorem: **`64,457`**.

Thus the new one-defect theorem closes four more union states beyond `R_N`; it closes six noncheap branches, with two of those states still surviving through the independently retained cheap-sphere branch.

The four new union exclusions occur at `t=2,10,12,13`.

The difficult `t=1` slice is not yet closed: all 5,404 states still have a noncheap route. However the optimizer is now highly structured:

- `4,762` of those states still minimize at `E=1`;
- `642` minimize at `E>=2` after the new E=1 price is imposed.

So `E=1` remains the dominant `t=1` bottleneck, but the next layer is now visible rather than hidden inside a coarse noncheap relaxation.

Again, these are abstract parameter-state diagnostics, not graph counts or realizability evidence.

## 9. Next structural move

Stay on `m=g+1`; do not open `m=g+2` yet.

The next move should use the one-defect localization before adding any new scalar relaxation. In the `t=1` layer there are p head-code classes: p-1 radius-one classes and one radius-two defect class. The selected witness layer therefore differs from the fully cheap Boolean sphere in exactly one class. The highest-value questions are:

1. intersect `(E1-PAIR)` with the exact rooted q/E_U residual allocation rather than only the row upper budget;
2. classify whether both directed witness adjacencies across a defect/radius-one support pair can coexist without violating the two original singleton certificates;
3. exploit the fact that if one selected witness adjacency is used to save unmatched slack, the corresponding defect--radius-one head edge is forced absent;
4. only after exhausting E=1 should the 642 `t=1` rows whose optimizer moved to `E>=2` be split into the exact E=2 support patterns.

`X_3` remains outside the hypotheses (`u=0`, no active rigid complete A-cut) and is untouched.