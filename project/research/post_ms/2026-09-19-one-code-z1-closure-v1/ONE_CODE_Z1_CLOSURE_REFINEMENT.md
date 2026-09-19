# One-code `z=1` closure refinement: finite edge cap, exact residual elimination, and loaded-buffer surcharge

Date: 2026-09-19

Status: **internal structural theorem package**. This note continues the corrected load-bearing statement in `ONE_CODE_Z1_NEAR_SATURATION_V2.md`; it does not use the invalidated v1 assertion that all internal `Y`-edges consume crossing holes.

The active objective is the eventual / sufficiently-large second-extremal D2C problem around

`M(n)=floor((n-1)^2/4)+1`.

The order-12, size-32 graph `X_3` remains a mandatory hostile control. The present branch has `u_-=k+1>0`, so it is inactive on the canonical `X_3` root (`u=0`).

## 1. Audit reconciliation and why this is the next move

The 19 September daily red-team audit required, in order:

1. independent repair of the two source-tuple premises;
2. actual-graph regression from D2C graphs through the rooted/Hall/pair-capacity interface, with `X_3` as a hostile control;
3. only then, exact pair-local work in the rigid one-code branch, followed by residual feedback.

Those upstream obligations are already recorded as satisfied at the current internal trust level. The immediately preceding hostile reread then corrected the full-support traffic bookkeeping by replacing the false `H<=rho` statement with

`A=c_Y+e(Y,U_d)+e_-<=rho`,

`m_Y=e(Y)-c_Y<=y-rho`.

The remaining explicit `z=1` tasks were the common-buffer loaded/equality cases and the full-support truncation strip

`B=(k+1)(p+k-1)<2y`.

This note stays exactly on that audit-authorized line. It does not reopen the mixed `{4,5}` ladder or the four-exception gate.

---

## 2. Setup

Use the notation of `ONE_CODE_Z1_NEAR_SATURATION_V2.md`:

- `u_-=k+1`, `k=x-g>0`;
- `Y` has size `y`, `X` has size `x`, and `a=x+y`;
- `U_-=U_{bar d}`;
- `e_-=e(G[U_-])`;
- `E_-=sum_{w in U_-} epsilon_w`;
- `Z=u(p-lambda)+2q+E_U`;
- `L=lambda+1`.

In the **full-support** branch, with

`A=c_Y+e(Y,U_d)+e_-`,

`j=rho-A`,

`B=(k+1)(p+k-1)`,

`Z0=(k+1)(a-1)`,

`D0=Z0-u(p-lambda)`,

the corrected exact normal form is

> `E_- >= B-j-2e_-`,                                      `(F1)`
>
> `Z >= Z0-j`,                                            `(F2)`
>
> `j+e_-<=y`.                                             `(F3)`

The new ingredient below is elementary but was not yet fed into `(F1)`:

> `e_-<=binom(k+1,2)`.                                    `(F4)`

Because `U_-` has exactly `k+1` vertices, `(F4)` is an actual graph-capacity bound, not an abstract score relaxation.

---

## 3. Structural unit I: the finite `U_-` edge cap sharpens the full-support slack floor

Put

`K=binom(k+1,2)`,

`c=min(K,y)`.

### Theorem 3.1 — finite-edge-cap U-slack floor

Every full-support `z=1` survivor satisfies

> `E_- >= [B-y-c]_+`.                                     `(CAP-E)`

This dominates the previous safe floor

`E_->=[B-2y]_+`

because `c<=y`.

### Proof

From `(F3)` and `(F4)`,

`j+2e_-=(j+e_-)+e_-<=y+min(K,y)=y+c`.

Substitute in `(F1)`:

`E_->=B-(j+2e_-)>=B-y-c`.

Non-negativity gives `(CAP-E)`. `square`

The point is structural: the old elimination allowed the internal `U_-` edge term to absorb up to `y` units of hole pressure, but a graph on `k+1` vertices has only `K` such edges.

---

## 4. Structural unit II: exact elimination of the full-support truncation strip

The old exact residual theorem covered `B>=2y`. The finite edge cap allows the same elimination **for every value of `B`**, including the unresolved strip `B<2y`.

For fixed `j`, the best possible choice of `e_-` in the relaxation `(F1)--(F4)` is

`e_- = min(K,y-j)`.

Let

`E0(j)=[B-j-2min(K,y-j)]_+`.

Then every survivor has

`E_U>=E0(j)`

and, by `(F2)` and the exact identity for `Z`,

`2q+E_U>=D0-j`.

For fixed `j`, the exact integer minimum of `q+E_U` is therefore

`E0(j)+ceil([D0-j-E0(j)]_+/2)`.

The one-dimensional minimization has a closed form.

### Theorem 4.1 — exact cap-aware residual elimination

Let `c=min(K,y)`. Every full-support `z=1` survivor satisfies the following piecewise bound.

#### Case I: `B<=y`

> `q+E_U >= ceil([D0-y]_+/2)`.                            `(R1)`

#### Case II: `y<B<=y+c`

> `q+E_U >= ceil([D0+B-2y]_+/2)`.                         `(R2)`

#### Case III: `B>y+c`

Put

`E*=B-y-c`.

Then

> `q+E_U >= E*+ceil([D0-B+2c]_+/2)`.                     `(R3)`

Consequently, in all three cases,

> `f >= (p-lambda)(p+u) + (right-hand side) - delta`.     `(RF)`

For an above-`M(n)` candidate one may replace `delta` by `D_M-1` exactly as in the preceding residual packages.

### Proof

The cap `e_-<=K` and room `e_-<=y-j` give

`E0(j)=[B-j-2min(K,y-j)]_+`.

There are two linear pieces, meeting at `j=y-c`:

- for `j<=y-c`, `E0(j)=[B-j-2c]_+`;
- for `j>=y-c`, `E0(j)=[B-2y+j]_+`.

Now minimize

`F(j)=E0(j)+ceil([D0-j-E0(j)]_+/2)`

over integers `0<=j<=y`.

If `B<=y`, the rightmost zero of `E0` is `j=y`, giving `(R1)`.

If `y<B<=y+c`, the rightmost zero is `j=2y-B`, giving `(R2)`.

If `B>y+c`, `E0` is strictly positive and V-shaped with its unique minimum at `j=y-c`, where `E0=B-y-c`. On the left, increasing `j` lowers `E0` by one while leaving `D0-j-E0` unchanged; on the right, increasing `j` raises `E0` by one while lowering the residual gap by two, so `F` cannot decrease. Evaluating at `j=y-c` gives `(R3)`. `square`

### Relation to the old `B>=2y` theorem

If `K>=y`, then `c=y`. For `B>2y`, `(R3)` becomes

`E*=B-2y`,

`q+E_U>=E*+ceil([D0-E*]_+/2)`,

exactly the old formula. If `K<y`, `(R3)` is strictly stronger because the finite `U_-` graph cannot realize the edge mass that the old relaxation implicitly allowed.

Thus the previous `B<2y` stop line is removed at the level of the corrected normal form.

---

## 5. Structural unit III: cap-binding stability and equality geometry

The strongest new geometry appears in Case III inside the formerly unresolved strip.

Assume

`B<2y`

and

`B>y+K`.

Then necessarily `K<y`, so `c=K`. Put

`h=y-K`,

`E*=B-y-K>0`.

### Theorem 5.1 — cap-binding stability

For every full-support survivor in this regime:

- if `j<=h`,

  > `E_- >= E*+(h-j)+2(K-e_-)`;                          `(S-left)`

- if `j>=h`,

  > `E_- >= E*+(j-h)+2((y-j)-e_-)`.                      `(S-right)`

Hence excess U-slack above `E*` directly controls distance from the single cap-binding corner `(j,e_-)=(y-K,K)`.

### Proof

When `j<=h`, the graph edge cap is the active edge bound, so

`B-j-2e_-=E*+(h-j)+2(K-e_-)`.

When `j>=h`, the room bound `e_-<=y-j` is active, and

`B-j-2e_-=E*+(j-h)+2((y-j)-e_-)`.

All displayed right sides are positive in Case III, so `(F1)` gives the result without truncation. `square`

### Corollary 5.2 — exact cap-binding equality model

If `E_-=E*`, then necessarily

> `j=y-K`,
>
> `e_-=K`.                                                `(EQ1)`

Therefore `G[U_-]=K_{k+1}`.

Moreover `j+e_-=y`. Since

`j=rho-A`,

`A>=e_-`,

`rho<=y`,

we obtain the chain

`y=j+e_-=rho-A+e_-<=rho<=y`.

Thus every inequality is equality:

> `rho=y`,
>
> `A=e_-=K`.                                              `(EQ2)`

Because

`A=c_Y+e(Y,U_d)+e_-`,

this forces

> `c_Y=0`,
>
> `e(Y,U_d)=0`.                                           `(EQ3)`

Finally `(MROOM)` gives

`m_Y<=y-rho=0`,

so

> `e(Y)=0`.                                               `(EQ4)`

The crossing matched count is then

`yg-y+rho=yg`,

so the global matched channel is saturated by the crossing layer.

Hence the cap-binding equality geometry is explicit:

1. `Y` is independent;
2. there are no `Y--U_d` same-code edges;
3. all `k+1` vertices of `U_-` are crossing witnesses;
4. `U_-` is a clique;
5. every source has exactly one crossing hole (`rho=y`);
6. the `K` auxiliary physical-hole uses are exactly the `K` edges of that clique;
7. matched crossing traffic saturates `P_P=yg`.

This is a much narrower object than the old scalar floor.

### Corollary 5.3 — equality-channel weighted gate

In the equality model, the weighted reservoir specializes to

> `L(yk+K) <= (k+1)L_Y+yE_-`.                             `(EQ-W)`

Also the same-code clique payment gives

> `S>=ceil((k+1)L/2)`.                                    `(EQ-CLQ)`

These should be used before any further global relaxation if the Case-III equality geometry survives the residual ledger.

---

## 6. Structural unit IV: the common-buffer loaded branch has an omitted `x`-defect surcharge

Return to the common-buffer support type. Let `W_0` be the `k` crossing-witness core and `b` the unique buffer. Put

`H=e(Y)+e(Y,U_d)+e_-`,

`e_+=e(Y)+e(Y,U_d)`.

The corrected v2 theorem already gives:

- `H<=y`;
- `W_0` is independent;
- the core pays `E_core>=k(p+k-2)`;
- every auxiliary use consumes a distinct `Y x {b}` physical pair;
- if `H>0`, then `d_X(b)=0` and

  `epsilon_b>=[p-y+k+e_+]_+`.

The previous defect statement recorded only

`Z>=k(a-1)+H`.

But once `H>0`, the conclusion `d_X(b)=0` supplies `x` additional `X--b` nonedges which are disjoint from the core and from the `H` auxiliary `Y--b` holes.

### Theorem 6.1 — loaded-buffer defect surcharge

If `H>0`, then

> `Z>=k(a-1)+x+H`.                                        `(CB-Z+)`

### Proof

Each of the `k` core witnesses is used by all `y` outside sources and has exactly one X-neighbour. Hence each core vertex contributes

`(x-1)+y=a-1`

A--U nonedges, for a total `k(a-1)`.

If `H>0`, the buffer has no X-neighbour, giving `x` further X--U nonedges. The `H` auxiliary certificates use `H` distinct `Y x {b}` physical pairs, all nonedges, giving another `H`. These sets of nonedges are disjoint. `square`

This is a strict strengthening of the previous loaded-buffer residual input.

---

## 7. Structural unit V: common-buffer unloaded versus loaded residual dichotomy

Assume the principal `g0=p-y>=1` regime used by the gamma/U score floor. Then the buffer-slack bracket is positive whenever `H>0`.

Put

`Ecore=k(p+k-2)`,

`Dcore=k(a-1)-u(p-lambda)`.

### Unloaded buffer: `H=0`

Then

`e(Y)=e(Y,U_d)=e_-=0`.

So `Y` and `U_-` are independent, there are no `Y--U_d` same-code edges, the crossing layer saturates the matched channel, and the extra buffer is inert with respect to the auxiliary reservoir.

The exact residual relaxation gives

> `q+E_U >= Ecore+ceil([Dcore-Ecore]_+/2)`.               `(CB0)`

### Loaded buffer: `H>0`

The core and buffer are distinct U-vertices, so their slack contributions add. Using the existing buffer floor and dropping only the nonnegative `e_+` term gives

> `E_U>=Ecore+(p-y)+k`.                                   `(CB-E+)`

By `(CB-Z+)`, `H>=1` gives

> `2q+E_U>=Dcore+x+1`.                                    `(CB-D+)`

Therefore every loaded common-buffer survivor satisfies

> `q+E_U`
> ` >= Eload+ceil([Dcore+x+1-Eload]_+/2)`,                `(CB+)`

where

`Eload=Ecore+(p-y)+k`.

Thus the `z=1` common-buffer branch splits into two sharply different geometries: an inert-buffer extension of the saturated rectangular model, or a loaded buffer that pays both an `x`-sized defect surcharge and a positive buffer-slack surcharge.

This finishes the previously requested loaded/equality bookkeeping at the level of the exact rooted residual ledger.

---

## 8. Structural unit VI: a direct `(CHAN-P)` score gate for either `z=1` support type

At `z=1`, `u_-=k+1`. The preserved channel-separated inequality is

`L_Y+2((k+1)L_Y+yE_-)/L >= y(p+2x-3g)`.

Multiplying by `L` gives

`alpha L_Y+beta E_- >= N`,

where

`alpha=L+2(k+1)`,

`beta=2y`,

`N=Ly(p+2x-3g)`.

Let

`A0=phi(g)`

be the gamma-collision floor on `L_A`, and let `E0` be any valid branch-specific floor on `E_-`:

- common buffer: `E0=Ecore` (or `Eload` in the loaded branch);
- full support: `E0=[B-y-min(K,y)]_+`.

Since `L_Y<=L_A`, `E_-<=E_U`, `L_A>=A0`, and `E_U>=E0`, every survivor must satisfy

### Theorem 8.1 — `CHAN-z1` global score floor

> `S=L_A+E_U`
> ` >= A0+E0`
> `  +ceil([N-alpha A0-beta E0]_+/max(alpha,beta))`.       `(CHAN-Z1)`

This is deliberately downstream of the pair-local structural work. It is not a substitute for `(CHAN-P)`; it is a compact contradiction gate once a support type and its exact `E_-` floor have already been identified.

---

## 9. Independent arithmetic audit

The companion script `check_one_code_z1_closure_refinement.py` performs two separate checks.

### 9.1 Exact-elimination replay

For

- `1<=y<=12`,
- `1<=k<=8`,
- `0<=B<70`,
- `-8<=D0<70`,

it brute-forces all integer triples `(j,e_-,E_U)` obeying the relaxed full-support constraints and compares the exact minimum of `q+E_U` with Theorem 4.1.

Recorded checks:

> **524,160** parameter instances, **zero mismatches**.

The script also brute-forces the two-variable integer minimization used in `(CHAN-Z1)` on **71,424** small coefficient/base/demand instances, again with **zero mismatches**.

This is an arithmetic audit of the eliminations only, not graph-realizability evidence.

### 9.2 Bounded score diagnostic

On the same coarse box used by the preceding `z=1` diagnostic (`3<=p<=18`, `1<=u<=18`):

- older shared-floor `z=1` possibilities: `86,820`;
- previous corrected support union: `78,167`;
- full-support states passing the old `[B-2y]_+` floor: `77,310`;
- full-support states passing the finite-edge-cap floor: `76,449`;
- old full-support choices removed by the cap floor: `861`;
- either support type after the cap floor: `77,339`;
- either support type after also applying `(CHAN-Z1)`: `77,338`.

Thus, relative to the previously frozen `78,167` support-union count, the new safe gates remove **829 additional abstract states**, and the total rejection relative to the old shared-floor `86,820` count rises from `8,653` to `9,482`.

These are abstract arithmetic states, **not counts of realizable D2C graphs**.

---

## 10. Consequence for the live frontier

The two explicit `z=1` tasks from the preceding handoff are now materially reduced.

1. **Full support:** the `B<2y` truncation strip no longer needs a separate scalar treatment. The finite graph edge cap `e_-<=binom(k+1,2)` gives an exact piecewise residual elimination for all `B`, and the cap-binding portion of the strip has a rigid equality model (`Y` independent, `U_-` complete, matched crossing channel saturated).
2. **Common buffer:** the branch is now a clean unloaded/loaded dichotomy. Any genuine buffer use forces the previously omitted `x` A--U defect surcharge plus buffer slack; the unloaded branch is an inert-buffer extension of the saturated rectangular crossing model.
3. `(CHAN-P)` now has a branch-specific compact score gate after these exact local floors are inserted.

The next highest-value move is therefore **not** a blind jump to `z=2`. First feed the surviving `z=1` equality/near-equality geometry back into the exact pair bill `(ONE-P)`, especially the Case-III full-support clique model and the unloaded common-buffer model. If those two equality models survive, classify their pair traffic directly; if they fail, `z=1` is essentially closed at the structural level and only then should the near-saturation analysis move to `z=2`.

## 11. Trust boundary

- This note depends on the corrected v2 full-support variables `A,j`, not the invalidated v1 `H<=rho` statement.
- The finite-edge cap is the literal graph bound on `e(G[U_-])`.
- The exact residual elimination is a hand integer optimization independently brute-force checked.
- The common-buffer `+x` defect term uses the already-proved v2 fact `H>0 => d_X(b)=0` and simply records the X--buffer nonedges that were previously left unused in the residual bound.
- `(CHAN-Z1)` is a necessary scalar consequence of the pair-local channel inequality and the branch-specific slack floors; pair-local variables remain preferred for equality analysis.
- No actual-graph mismatch has been observed. No eventual theorem is claimed.
