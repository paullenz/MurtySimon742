# Fixed-foot target injectivity and corrected shared-core `t=1,E=2` pinch

Date: 2026-09-19

Status: internal conditional mathematics inside the audited rigid one-code / positive-buffer / minimal-reservoir branch. This note does **not** assert graph realizability, the false all-order 2019 Dailly–Foucaud–Hansberg conjecture, or a global eventual theorem. The order-12 graph `X_3` remains a mandatory negative control.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, the root `README.md`, the latest commits through `14948a7cb4944ba8aea58cde306e2dee2abd0f78`, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, the actual-D2C graph-level regression status, and the new exceptional-gamma-foot theorem.

The binding trust boundary is unchanged:

- distinct physical beta-source identity is accepted only at the raw singleton-criticality level actually proved;
- `(source,coordinate)` uniqueness means selected-representative uniqueness, not raw-witness uniqueness;
- the finite source-tuple theorem is not unconditional graph-level closure;
- the actual-D2C regression retains `X_3`, reports zero recorded graph/formula mismatches, and still has no positive fixture realizing all rigid complete-cut hypotheses;
- exact pair-local `S_P/Ccap_P` is retained; `(ONE-P)` and `(CROWD)` are used only where already proved dominated by stronger physical bills;
- the four-exception gate remains subordinate.

There is no departure from the audit priority order. The immediate handoff asked for equality/stability in `e(X)<=k` in the corrected `t=1` exceptional-fibre geometry. The first step below is a raw-criticality strengthening of the very matched-foot statement that created that geometry.

## 2. Setup retained

Stay in

- `m=g+1`, `t=p-g=1`, `k=x-g>=3`;
- the exact `E=2` shared-core `R2+R2` support type;
- core support `{r}` and two defect supports `{r,i}`, `{r,j}`;
- unique exceptional gamma coordinate `e=r`;
- exceptional `d`-selected matched endpoint `q_e` with `gamma(q_e)=c_*`, the repeated core code;
- `H_0` is the core code class, `|H_0|=k`;
- `H_M` contains the two radius-two defects and the remaining singleton radius-one classes.

Write `J` for selected outside-witness wrong-head incidences and `e_X=e(G[X])`.

The predecessor proved that every wrong-head edge `z_s h` in the `t=1` layer has the *same graph-fixed matched foot* `q_e` and satisfies

`N(h) cap N(q_e)={z_s}`.                                    `(2.1)`

It also proved that every X-edge has a critical matched foot in the exceptional fibre.

## 3. Unit I — fixed-foot target injectivity

### Theorem 3.1

At `t=1`, a fixed target head `h` can receive at most one selected outside-witness wrong-head edge.

### Proof

If distinct selected witnesses `z_s` and `z_t` both hit `h`, the exceptional-fibre localization gives the same foot `q_e` in both cases. Equation `(2.1)` would then give simultaneously

`N(h) cap N(q_e)={z_s}`

and

`N(h) cap N(q_e)={z_t}`.

The left side is one fixed set, so `z_s=z_t`, contradiction. `square`

Thus if all wrong-head traffic targets one code class `C`,

> **`J <= |C|`.**                                           `(TI)`

This is target injectivity. It is independent of the source-tuple injectivity premises and uses no assumption that raw witnesses are globally unique.

### Corrected E2 traffic hierarchy

The preceding exceptional-gamma note correctly localized every `t=1` wrong-head edge to one target code, but its support-only traffic count still allowed two different sources to hit the same target head. `(TI)` removes that overcount.

For `k>=3`:

- shared-core `R2+R2`, core target: `J<=k` (not `2k`);
- one-core `R2+R2`, core target: `J<=k`;
- core-containing `R3`, core target: `J<=k`;
- any singleton target: `J<=1`.

So the latest support hierarchy is superseded at exactly this point: the unique `2k` traffic escape does not exist.

## 4. Unit II — exact shared-core orientation and star-forest structure

In the traffic-maximal shared-core orientation the exceptional target code is the repeated core code `c_*`.

### Lemma 4.1 — `A=g` exactly

The common core witness `z_*` serves `H_0`. Any adjacency from `z_*` to an `H_M` head would be a wrong-head adjacency whose target code is that `H_M` code. But at `t=1` every wrong-head target code is the fixed code `c_*`. Hence no such adjacency exists:

> **`z_*` is anticomplete to `H_M`, so `A=g`.**            `(A=G)`

This sharpens the predecessor's `A in {g-1,g}`.

### Lemma 4.2 — every X-edge uses a core endpoint

The exceptional gamma pair is a vertex cover of `G[X]`. In the shared-core represented-code set no complementary pair occurs, and the only represented exceptional gamma code in the core-target orientation is `c_*`. Therefore every X-edge has one endpoint in `H_0`.

The fixed-foot singleton argument from the predecessor also gives every core vertex X-degree at most one.

### Lemma 4.3 — both radius-two defect heads are isolated in `G[X]`

A defect support contains `r`, whereas `q_e` is the `d`-selected matched endpoint in fibre `r`. Hence each defect head is nonadjacent to `q_e`.

If a core--defect edge existed, the X-edge criticality localization would require the non-core endpoint to be the singleton common neighbour of the core head and `q_e`; in particular that non-core endpoint would have to be adjacent to `q_e`. Contradiction.

Thus both defects are isolated.

### Corollary 4.4 — matching-star geometry

Every possible X-edge joins a core vertex of support `{r}` to a radius-one singleton head of support `{s}` with `s!=r`. Such an edge has Hamming distance exactly two. Consequently:

- `H_M` is independent;
- both defects are isolated;
- every core vertex has X-degree at most one;
- every actual X-edge has positive Hamming excess `rho=1`;
- `G[X]` is a star forest whose leaves lie in `H_0` and whose centers lie among the nondefect radius-one singleton classes.

This is the equality/stability classification requested by the handoff, up to the degrees of the star centers.

## 5. Unit III — wrong-head/X-edge conservation

Let a core head `x in H_0` receive a wrong-head selected witness `z_s`. By `(2.1)`,

`N(x) cap N(q_e)={z_s}`.                                    `(5.1)`

If `x` also had an X-neighbour `h`, Lemma 4.2 and the X-edge matched-foot localization would give `h in N(x) cap N(q_e)`, contradicting `(5.1)`.

Target injectivity says each wrong-head incidence uses a distinct core target. Lemma 4.2 says each X-edge uses a distinct core leaf because core X-degree is at most one. The two sets of core heads are disjoint. Therefore

> **`J + e_X <= k`.**                                      `(CONS)`

This is the key conservation law: wrong-head traffic and internal X-density spend the same `k` physical core heads.

There is also a small physical coupling to the unmatched defect variable `M`. If `J>0`, some defect witness `z_i` hits a core head `x`. The core witness certificate is `N(x) cap N(z_*)={b}`. Thus `z_i` cannot also be adjacent to `z_*`, and so

> **`J>0 => M>=1`.**                                      `(M-ACT)`

No multiplication by `J` is claimed; one active defect witness may hit several core heads.

## 6. Unit IV — exact pair-local density/traffic tradeoff

At `t=1`, the preserved selected-witness slack bound is

`sum epsilon_selected >= p^2+k+M-J`.

With `(CONS)`,

> `sum epsilon_selected >= p^2+M+e_X`.                   `(6.1)`

Since `A=g`, put

`Emax=binom(g,2)+kg`,

and

`R:=D+2Emax`.

The exact Hall bill is

`L_X >= [D+2(Emax-e_X)]_+=[R-2e_X]_+`.

Let `T=C0-sigma_P`, retaining the exact pair-local capacity threshold. Every corrected shared-core survivor therefore satisfies

> **`p^2+M+e_X+[R-2e_X]_+ <= T`, `0<=e_X<=k`.**           `(PAIR-E)`

This is stronger than inserting `J<=k` and `e_X<=k` separately: the same core heads cannot finance both savings.

### Closed elimination of `e_X`

Define

`F_k(R)=min_{0<=e<=k}{e+[R-2e]_+}`.

Then exactly

> `F_k(R)=0`, if `R<=0`;
>
> `F_k(R)=ceil(R/2)`, if `0<R<=2k`;
>
> `F_k(R)=R-k`, if `R>=2k`.                               `(FK)`

Hence the parameter-only necessary pair gate is

> **`p^2+M+F_k(R) <= T`.**                                `(PAIR-CLOSED)`

If `M=0`, `(M-ACT)` gives `J=0`, so the stronger special gate is

> **`p^2+k+[D+2(Emax-k)]_+ <= T`.**                       `(M0-PAIR)`

### Stability around pair equality

If the left side of `(PAIR-CLOSED)` has slack at most `s`, then the allowed internal edge count is pinned:

- if `R<=0`, `e_X<=s`;
- if `0<R<2k`,
  `[floor(R/2)-s]_+ <= e_X <= min(k,ceil(R/2)+s)`;
- if `R>=2k`, `e_X>=k-s`.

Thus the corrected equality family has three literal geometries: wrong-head-heavy, mixed, and X-edge-heavy. Pair slack can no longer move freely between witness traffic and Hall density.

## 7. Unit V — linear rooted-slot surcharge for the star forest

Use the audited local theorem

`sum_{w in N_A(z)} d_H(c(w),c(z)) <= r_z d_A(z)`.        `(LH)`

In this exact `E=2` support geometry the total X-to-`d` Hamming length is `x+2`.

### Y vertices

Every `y0 in Y` has `d_A(y0)=x` and incident Hamming sum `x+2`, so

> `r_y>=2` for every `y in Y`.                            `(RY2)`

### Core vertices

An isolated core head has crossing numerator/degree `y/y`, so costs at least one slot. A core leaf of the X-star forest has one Hamming-two X-edge, so its ratio is

`(y+2)/(y+1)>1`,

and it costs at least two slots. Since distinct X-edges use distinct core leaves, the core contribution is at least

> `k+e_X`.                                                `(RC)`

### `H_M` vertices

Each radius-two defect is isolated but has crossing Hamming ratio `2y/y=2`, so the two defects cost two slots each. Every nondefect radius-one center incident with at least one core leaf has ratio

`(y+2d)/(y+d)>1`

and therefore also costs at least two slots; an isolated radius-one singleton costs at least one.

Let `c_X` be the number of nonisolated `H_M` star centers. The `H_M` contribution is at least

> `g+2+c_X`.                                              `(RHM)`

Summing the three disjoint A-parts gives

> **`r >= a+y+2+e_X+c_X`.**                              `(R-STAR)`

In particular,

> **`r >= a+y+2+e_X+1_{e_X>0}`.**                        `(R-STAR-SAFE)`

This is substantially stronger in this geometry than the generic `eta_2(e_X)` surcharge: every internal X-edge creates its own extra local slot at its distinct core leaf.

## 8. Unit VI — independent bounded diagnostic

A companion checker independently replays the same abstract parameter box used by the E1/E2 diagnostics (`3<=p<=18`, `1<=u<=18`) without changing any predecessor filters. It first reproduces exactly:

- `933` `t=1` states with no support-capped E1 route;
- their distribution `k=1:223, 2:201, 3:146, 4:104, 5:82, 6:60, 7:53, 8:47, 9:17`;
- hence `509` states in the current `k>=3` E2 frontier.

It then applies only the corrected shared-core necessary conditions above.

- `477/509` have at least one predecessor row with `A=g`;
- only `147/509` even retain a row whose predecessor lower bound on `e_X` is compatible with the star-forest range;
- **zero** of those rows satisfy `(PAIR-E)` with the exact `sigma_P` budget;
- therefore zero of the `509` states retain the corrected shared-core core-target route on this diagnostic box;
- the smallest pair-budget failure margin among the `147` nonempty edge-range states is `9` score units.

The rooted slot gate `(R-STAR-SAFE)` is implemented as a second check, but is never reached by a pair-feasible row on this box.

These are abstract parameter states, not D2C graphs. The zero count is diagnostic evidence for seeking an analytic shared-core closure; it is **not** a finite proof of the eventual theorem and is not graph-realizability evidence.

## 9. Consequence and next move

The corrected `t=1,E=2,k>=3` shared-core family is much more rigid than the predecessor state suggested:

1. fixed-foot target injectivity halves its maximal wrong-head traffic (`2k -> k`);
2. the common core witness is forced anticomplete to all `H_M`, so `A=g`;
3. `G[X]` is a star forest with isolated defects and core leaves of degree at most one;
4. wrong-head targets and X-edge leaves obey `J+e_X<=k`;
5. exact pair capacity collapses to the V-shaped gate `(PAIR-CLOSED)`;
6. the rooted local-slot ledger becomes linear in `e_X`, `(R-STAR)`;
7. the entire corrected shared-core route disappears on the existing bounded diagnostic box before the rooted-slot gate is even needed.

The highest-value next task is to turn `(PAIR-CLOSED)` plus the explicit formulas for `D,Emax,C0,sigma_P` into a compact analytic exclusion over the full shared-core parameter range. If that does not close it, use `(R-STAR)` and the exact rooted residual ceiling. Only after that should the tied `J<=k` one-core `R2+R2` and core-containing `R3` topologies be opened. `k=2,k=1,m=g+2`, loaded buffer, `z=2`, and the four-exception gate remain deferred.

`X_3` is unaffected: it has `u=0` and never enters the present rigid positive-buffer/minimal-reservoir hypotheses.
