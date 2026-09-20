# All-R equality pinch: exact used-witness pricing and cross-edge reservoir

Date: 2026-09-20

Status: **internal conditional structural theorem package** inside the audited one-code / first-strict / one-witness / all-R equality pinch. This note starts only after the 20 September daily red-team audit and the raw-criticality re-derivation in `2026-09-20-same-code-raw-criticality-audit-v1/SAME_CODE_RAW_CRITICALITY_AUDIT.md`. It does not assert realizability of the rigid complete-cut hypotheses and does not infer an eventual threshold from the finite diagnostic.

## 1. Audit reconciliation

The binding audit is `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Before this work, `CURRENT_STATE.md`, root `README.md`, the latest commits, the daily audit, and the new raw same-code audit were read. The daily audit required raw re-derivation of same-code criticality / ordered `(source,witness)` injectivity before further all-R deductions. Commit `c3a82e10a89406770d71ed613671296ee7f0f302` supplies that re-derivation and also proves the stronger head-reserve and witness-slack statements used below.

The following remain binding:

- `X_3` is the mandatory order-12 / 32-edge hostile control;
- the rigid complete-cut branch still has zero positive actual-D2C fixture in the bounded graph regression;
- exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain local;
- finite parameter scans are diagnostics, never graph counts or realizability evidence.

## 2. Setup

Use the literal all-R equality pinch notation from `ALL_R_PINCH_LOCAL_FEEDBACK.md`.

- `A=X dotcup Y`, `|X|=x>=3`, `|Y|=y>0`, `X--Y` complete;
- every X-vertex has code `C`, every Y-vertex code `d`, and `d_H(C,d)=1`;
- `a_0` is isolated in `G[X]`, `X'=X\{a_0}`, `N=x-1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, with injective core-head map into `X'`;
- `g=x-k`, `u_o=u-k-1`;
- `z in U_o` is the distinguished `bar C` witness with `N_A(z)={a_0}`;
- `d_z` (written simply `d` below) is the number of nonneighbours of z in `U_o\{z}`;
- `J=u_o-1-d` is the number of z-neighbours there;
- the J-set is `bar C`, A-anticomplete and independent;
- internal X-edges can use only complementary witnesses among the d z-nonneighbours.

For a family of selected internal-X certificates, let `m` be the number of **actually used physical** complementary witnesses and `r_i` their selected loads. Put `e=e(X)` and `h=x-2=N-1`.

The raw audit proves

`1<=r_i<=h`, `sum r_i=e`, `m<=d`,

and for each used witness

`epsilon_i >= [p-x+r_i+2]_+`.

## 3. Unit I — core-head injection forces `g>=1`

The common-core head map `W_0 -> X` is injective. The already-proved exclusion `a_0--W_0=empty` means no core head is `a_0`; hence all k distinct core heads lie in `X'`, which has N=x-1 vertices.

Therefore

> `k<=x-1`, equivalently `g=x-k>=1`.                    `(G-POS)`

This is a genuine structural gate. Any abstract row with `g=0` in the literal all-R equality pinch is spurious.

## 4. Unit II — used witnesses cannot buy `a_0` degree

Every U-neighbour of `a_0` other than z must lie among the d outside vertices nonadjacent to z. A used internal-X witness has code `bar C`, and the raw audit proves it is nonadjacent to `a_0`. Hence the m used witnesses are unavailable as possible extra U-neighbours of `a_0`.

Thus

> `d_U(a_0)<=1+(d-m)`,                                  `(A0-DM-DEG)`

and direct degree counting gives

> `epsilon_{a_0}>=p+u-y-d+m-1`.                         `(A0-DM)`

Together with `epsilon_z=p+k-1+d`,

> `epsilon_z+epsilon_{a_0}>=2p+k+u-y+m-2`.              `(ZA0-M-CONS)`

Each physical internal-X witness therefore raises the old d-independent z/a0 conservation floor by one.

## 5. Unit III — used witnesses create a located A--U hole ledger

Fix a used witness w with selected source set of size `r_w`.

The raw same-code audit gives four disjoint located A-nonneighbour groups for w:

1. all y vertices of Y;
2. the `r_w` selected X-sources;
3. `a_0`;
4. z is a U-nonneighbour, already included in d but not in the A-hole ledger.

The first three groups produce `y+1+r_w` A--U holes in the column of w. Distinct used witnesses give disjoint U-columns. Summing over the m used witnesses gives the additional physical bounds

> `Z_X >= Z_X^0+NJ+e+m`,                                `(ZX-M)`
>
> `Z >= Z_0+NJ+e+m(y+1)`.                               `(Z-M)`

The `+e` terms are the selected X-source holes; the `+m` in `(ZX-M)` is the `a_0` hole for every used witness.

## 6. Unit IV — exact fixed-m load price

Write

`c=x-p-2`.

For fixed `(e,m)`, minimizing

`sum_i [p-x+r_i+2]_+ = sum_i [r_i-c]_+`

over `1<=r_i<=h`, `sum r_i=e`, is exact:

> `P(e,m)=[e-mc]_+`.                                    `(LOAD-PRICE)`

The admissible range is

> `m<=e<=mh`, with `m<=d`,                              `(LOAD-RANGE)`

plus `e<=binom(N,2)`. For `e=0`, necessarily `m=0`.

This keeps the actual number of physical witnesses rather than replacing it by d.

## 7. Unit V — exact local Hall inequality with physical holes

Retain the notation of `ALL_R_PINCH_LOCAL_FEEDBACK.md`:

`E_0(d)=k(p+k)+(p-g+1)+(p+k-1+d)+Jp`,

`B_d=x(p-y)+Z_X^0+NJ-C_0+E_0(d)`.

The exact Hall identity is

`2e=x(p-y)-L_X+Z_X`.

Since `L_X<=C_0-E_U`, `(ZX-M)`, `E_U>=E_0(d)+P(e,m)` imply

`2e >= B_d+e+m+P(e,m)`.

Hence every survivor must satisfy the stronger exact local condition

> `e >= B_d+m+P(e,m)`.                                  `(H-M-EXACT)`

simultaneously with `(LOAD-RANGE)`, the exact pair gate

> `Sigma_P^+(1)+epsilon_z+epsilon_{a_0}<=C_0`,          `(PAIR-M)`

the total U-score ceiling using `(A0-DM)`, the physical q ceiling from the J independent set, `(Z-M)`, and the rooted residual requirement.

This strictly strengthens the predecessor relaxation `2e>=B_d+[e-d(x-p)_+]_+` whenever internal X-edge witnesses are used.

## 8. Unit VI — raw criticality of the complete X--Y cut

The preceding optimization leaves many rows with `e(X)=0`, so the complete `X--Y` cut itself becomes the next load-bearing structure.

Fix an edge `xy` with `x in X`, `y in Y`. It lies in a triangle because the two codes agree in `p-1>=2` tight fibres. Apply raw triangle-edge criticality.

### 8.1 Witness locations when `y>=2`

No A-witness works: a same-side A-witness has the same code as the source and therefore shares tight matched neighbours with it, while an opposite-side A-vertex is adjacent to the source.

The root cannot witness an A--A edge. A matched witness can only be the endpoint in the unique special fibre where C and d differ. In orientation `Y -> X`, that matched endpoint has every X-vertex as a common neighbour with the Y-source, so `x>=3` forbids a singleton head. In orientation `X -> Y`, the opposite matched endpoint has every Y-vertex as a common neighbour with the X-source, so `y>=2` forbids a singleton head.

Therefore, for `y>=2`, every X--Y edge is U-certified in one of exactly two ways:

- source in X: witness code `bar C`;
- source in Y: witness code `bar d`.

### 8.2 Fixed-head localization

If `w in U_{bar C}` certifies `x -> y`, then x is adjacent to every Y-vertex, so the singleton condition forces

> `N_Y(w)={y}`.                                         `(XY-C-HEAD)`

If `w in U_{bar d}` certifies `y -> x`, then y is adjacent to every X-vertex, so

> `N_X(w)={x}`.                                         `(XY-D-HEAD)`

Thus one outside witness can certify at most x edges in the first orientation or at most y edges in the second.

### 8.3 Only d outside vertices are available beyond the core

The k common-core vertices are `bar d`-coded and have k distinct X-heads, so together they can certify at most `ky` cross edges. The buffer b cannot certify a Y-source edge because it has at least two X common neighbours, and z cannot certify an X-source edge because `N_Y(z)=empty`.

Every z-neighbour in `U_o\{z}` is `bar C` and A-anticomplete, so it certifies no X--Y edge. Any usable outside `bar C` or `bar d` witness is therefore among the d z-nonneighbours.

The complete cut has xy edges. After allowing the core its maximal `ky` contribution, at least

`xy-ky=(x-k)y=gy`

edges must be certified by those d outside vertices. Each such vertex certifies at most `max{x,y}` cross edges. Hence for `y>=2`:

> `d max{x,y} >= gy`.                                   `(XY-d-CAP)`

Equivalently

> `d >= ceil(gy/max{x,y})`.                             `(XY-d-LOW)`

For `y=1` the special matched endpoint may in principle certify X-source edges, so this lower bound is not asserted.

## 9. Diagnostic consequence

A direct diagnostic implementation on the same abstract box as the audited all-R checker (`3<=p<=18`, `1<=u<=18`, `lambda>=0`) was run with:

- the audited predecessor one-witness gate retained;
- exact pair-local `Sigma_P^+(1)` retained;
- `(G-POS)`;
- the exact `(e,m)` load range and `(LOAD-PRICE)`;
- `(A0-DM)`, `(ZX-M)`, `(Z-M)`, `(H-M-EXACT)`;
- the J independent-set q ceiling;
- `(XY-d-CAP)` when `y>=2`.

The audited predecessor equality-pinch baseline remains **173,347** abstract rows. The strengthened necessary system leaves provisionally

> **78,582** abstract rows.

Within a first-feasible-witness diagnostic, most remaining rows still choose `e=0`; this makes the complete-cut criticality route, rather than further internal-X witness pricing, the next structural target.

These are parameter rows only. The 78,582 figure is a diagnostic checkpoint and should remain provisional until the companion checker is committed and independently replayed.

## 10. Next move

1. Preserve and independently replay the exact `(d,m,e)` checker; any mismatch blocks use of the 78,582 count.
2. Attack the dominant `e(X)=0` survivors via the localized X--Y certificate stars `(XY-C-HEAD)/(XY-D-HEAD)`, replacing the crude `max{x,y}` capacity by a slack-weighted two-reservoir inequality.
3. Feed any forced outside witness population into `Q`, `E_U`, `Z`, and `delta=r-e(F)` using physical holes, not survivor counts.
4. Keep the zero-positive-fixture rigid-cut gap explicit. Do not open `m>=2`, loaded-buffer, `z=2`, or the four-exception route merely because this local diagnostic shrinks.
