# Minimal outside reservoir: core-code collapse and star separation

Date: 2026-09-19

Status: hand structural mathematics inside the rigid one-code `z=1`, unloaded positive-buffer common-buffer branch. This is conditional on the rigid complete-Hall hypotheses and is not an eventual D2C theorem.

## Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, root `README.md`, the latest commits, the 19 September daily red-team audit, `SOURCE_PREMISE_REPAIR.md`, and the independent actual-D2C graph regression through rooted slots, codes, Hall objects and exact pair capacity. The audit boundary is unchanged: P1/P2 are used only in their repaired raw/selected meanings; the finite source-tuple theorem is not treated as unconditional graph-level closure; `X_3` remains a mandatory hostile control; no actual bounded-corpus fixture realizes the full rigid complete-Hall cut; exact `Ccap_P`, `(ONE-P)` and `(CROWD)` remain mandatory; the four-exception gate is subordinate.

The previous handoff asked first for the minimal outside-reservoir layer `m=g+1`. This note follows that priority exactly. It does not move to `z=2`, loaded buffer, or extra buffer slack.

## Setup retained

Use the notation of `POSITIVE_BUFFER_REVERSE_COLLAPSE_AND_HEAD_DICHOTOMY.md`:

- `X--Y` complete, `x>=3`, `y>0`;
- every `Y`-vertex has code `d`; `X` contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, `e(G[U_-])=0`;
- `r_b=0`, `epsilon_b=t`, so `b--X` and `b--U_o` are complete;
- `X=H_M dotcup H_0`, where `|H_M|=g`, `|H_0|=k`;
- each `H_M` head has a singleton A-code class;
- every buffer--X edge is outside-U certified;
- every outside buffer witness is anticomplete to `Y`;
- `m>=g+1` distinct physical outside witnesses.

Now impose the first equality reservoir

> `m=g+1`.                                                `(MR)`

Let the `g` witnesses serving `H_M` be `z_1,...,z_g`. Since they are pairwise distinct and cannot serve a core head, there is exactly one further selected outside witness; call it `z_*`. Every core head must use `z_*`.

---

## Unit I — common core witness forces one core code

For an outside certificate of `bx`, A/U localization gives

`c(z)=bar c(x)`.

Since `z_*` serves every `x in H_0`, all core heads have one common tight code; write it `c_*`. Thus

> `c(x)=c_*` for every `x in H_0`,
>
> `c(z_*)=bar c_*`.                                      `(C1)`

No `H_M` head can have code `c_*`: every `H_M` code is a singleton A-code class, whereas `H_0` already contains the `k>=1` core occurrence(s), and the head sets are disjoint. Since `Y` has code `d` and `c_*` lies in `X`, `c_* notin {d,bar d}`.

Therefore the A-multiplicities in the complementary pair `P_*={c_*,bar c_*}` satisfy

> `n_{c_*}=k`,
>
> `n_{bar c_*}<=1`.                                      `(C2)`

The second inequality holds because any A-vertex of code `bar c_*` lies in `X`, hence in `H_M`, and the `H_M` codes are pairwise distinct.

This is a new pair-local concentration statement generated purely by minimal physical witness population.

---

## Unit II — the core code class is independent

Assume `k>=2` and suppose two core heads `x_i,x_j in H_0` are adjacent. Because `X--Y` is complete and `b--X` is complete, this edge lies in triangles. A criticality certificate for `x_i x_j` must distinguish its two endpoints.

No possible location works:

- a matched endpoint cannot distinguish them because `c(x_i)=c(x_j)=c_*`;
- a `Y`-vertex or `b` is adjacent to both;
- an `X`-witness has every nonempty `Y` as an additional common neighbour with the opposite endpoint;
- an outside unmatched witness shares `b` with the opposite endpoint;
- a core vertex `w in W_0` can distinguish only its own graph-fixed head, but `w` has code `bar d`; since `c_*` is neither `d` nor `bar d`, `c_*` and `bar d` are neither equal nor complementary, so they agree in at least one tight coordinate and hence share a matched neighbour. The required common neighbourhood cannot be a singleton.

Thus

> `G[H_0]` is independent.                               `(C3)`

Together with `(C2)`, the existing exact code-crowding identity immediately gives the safe local floor

> `L_{c_*} >= [k(k-T_0)]_+`,                             `(C4)`

where `T_0=a-p`, because `e_A(c_*)=0` in `2e_A(c)>=n_c(n_c-T_0)-L_c`.

This floor is often zero, but when active it is genuinely pair-local and should be retained rather than replaced by total score slack.

---

## Unit III — the common witness is anticomplete to the whole core U-block

For each `w in W_0`, let `h(w) in H_0` be its graph-fixed core head. Since `z_*` certifies the buffer edge `b h(w)`,

`N(h(w)) cap N(z_*)={b}`.

But `w~h(w)`. Hence necessarily

> `w z_* notin E` for every `w in W_0`.                  `(C5)`

So `z_*` is anticomplete to all of `W_0`, not merely missing one unspecified core pair. These are exactly `k` physical U--U nonedges.

This strengthens the generic outside-witness slack bound, because those same holes also cost degree at the `z_*` endpoint.

---

## Unit IV — exact common-witness slack identity

Put

`u_o=|U_o|=u-k-1`,

`A_* = g-d_{H_M}(z_*)`,

`M_* = (u_o-1)-d_{U_o\{z_*}}(z_*)`.

Thus `A_*` counts missing `z_*--H_M` pairs and `M_*` counts missing pairs from `z_*` to the rest of `U_o`.

The common witness has:

- no neighbours in `Y`;
- no neighbours in `H_0`;
- no neighbours in `W_0` by `(C5)`;
- the neighbour `b`;
- exactly `g-A_*` neighbours in `H_M`;
- exactly `u_o-1-M_*` neighbours in `U_o\{z_*}`.

Therefore, using `d_{A union U}(z_*)=p+u-1-epsilon_{z_*}`,

> **`epsilon_{z_*}=t+k+A_*+M_*`.**                      `(C6)`

This is exact. In particular

> `epsilon_{z_*}>=t+k`,                                  `(C7)`

whereas the generic multiplicity floor for one witness carrying `k` heads only gave `t`.

Let `s_1=[t-k+1]_+`. The `g` singleton `H_M` witnesses are distinct from `z_*` and each has slack at least `s_1`. Combining `(C6)` with the exact core floor and `epsilon_b=t` gives

> `E_U >= k(p+k)+2t+k+g s_1+A_*+M_*`.                   `(EU*)`

Hence, already at `A_*=M_*=0`, the minimal-reservoir layer gains `k` units over the predecessor outside-slack treatment when `k<=t`, and gains the entire positive common-witness payment when `k>t`.

---

## Unit V — star separation around `z_*`

The singleton condition has a second consequence. If `w in U_o\{z_*}` is adjacent to `z_*`, then for every `x in H_0` one must have `xw notin E`; otherwise `w` is a second common neighbour of `x,z_*` besides `b`.

Thus, with

`d_*:=d_{U_o\{z_*}}(z_*)=u_o-1-M_*`,

> `e_bar(H_0,N_{U_o}(z_*))=k d_*`.                       `(SEP-U)`

Likewise, if `h in H_M` is adjacent to `z_*`, then `h` cannot be adjacent to any core head. Hence

> `e(H_0,N_{H_M}(z_*))=0`.                               `(SEP-X)`

Equivalently, at most the `A_*` matched-crossing heads missed by `z_*` can carry any `H_0--H_M` edge. Since `H_0` is independent,

> `e(X) <= binom(g,2)+k A_*`.                            `(EX)`

This is a useful equality/stability dichotomy: making `z_*` highly adjacent saves its own degree slack, but it physically separates the entire core head block from those neighbours.

---

## Unit VI — Hall identity feeds the separation back into `L_X`

In the rigid Hall cut, `M_X=E_X=0`, so the exact cut identity is

> `2e(X)=x(x-T_0)-L_X+Z_X`.                              `(HALL)`

The following A--U holes are physically distinct:

1. `k(x-1)` from the `k` core witnesses in `W_0` to the wrong X-heads;
2. `x` selected buffer-head/outside-witness nonedges;
3. `A_*` missing `z_*--H_M` pairs;
4. `k d_*` star-separation holes from `(SEP-U)`.

Therefore

> `Z_X>=k(x-1)+x+A_*+k d_*`.                             `(ZX*)`

Using `(EX)` in `(HALL)` gives the new local Hall-slack floor

> `L_X >= [`
> ` x(x-T_0)+k(x-1)+x+A_*+k d_*`
> ` -g(g-1)-2kA_* ]_+`.                                  `(LX*)`

Equivalently, since `d_*=u_o-1-M_*`,

> `L_X >= [B_X+k(u_o-1-M_*)+(1-2k)A_*]_+`,              `(LX2)`

where

`B_X=x(x-T_0)+k(x-1)+x-g(g-1)`.

This is the first place in the minimal-reservoir classification where the common-code geometry, physical outside star, and exact Hall decomposition meet in one formula.

---

## Unit VII — strengthened scorecard and residual bridge

The previous positive-buffer theorem gives

`L_Y>=y(p+2)`

and the gamma-collision floor `L_A>=phi(g)`, with `phi(g)=g(g-1)` for `g>=3` and `0` otherwise. Together with `(C4)` and `(LX*)`, the minimal-reservoir score satisfies

> `S=E_U+L_A`
>
> `>= k(p+k)+2t+k+g s_1+A_*+M_*`
> ` +max{ y(p+2), phi(g), [k(k-T_0)]_+, LX_*(A_*,M_*) }`. `(S-MR)`

For the rooted residual side, the predecessor physical-hole floor was

`Z_+=ka+y(g+2)+g`.

Units IV--V add `A_*+k d_*`, so

> `Z>=Z_+ + A_*+k(u_o-1-M_*)`.                           `(Z-MR)`

Put

`E_*=k(p+k)+2t+k+g s_1`,

`R_0=Z_+ + k(u_o-1)-u(p-lambda)-E_*`.

If one temporarily drops only the extra `L_A` terms in `(S-MR)` and minimizes the exact rooted identity

`Z=u(p-lambda)+2q+E_U`,

the `A_*` term cancels from `Z-E_U`. Consequently

> `q+E_U >=`
> ` min_{0<=M<=u_o-1}`
> ` { E_*+M+ceil([R_0-(k+1)M]_+/2) }`.                  `(QE-MR)`

The minimizer has a clean interpretation. An edge from `z_*` to another outside vertex costs `k` A--U holes through star separation; deleting that U--U edge instead raises unmatched slack. The rooted ledger prices exactly that physical edge/nonedge choice rather than hiding it in total score slack.

For `k=1`, the active part cancels exactly and `(QE-MR)` reduces to the same value throughout the transition interval. For `k>=2`, increasing `M` is beneficial only until the residual term is extinguished; hence only the integer(s) around `R_0/(k+1)` and the endpoints need be checked.

---

## Diagnostic support

A bounded arithmetic diagnostic on the same box as the predecessor positive-buffer checker (`3<=p<=18`, `u<=18`) was run only on states surviving the already-promoted population and score floors. There were `133,835` such abstract states (`5,815` with `t=1`).

For the **minimal-reservoir comparator `m=g+1` only**, exact minimization of `(S-MR)` over the physically allowed integers

`0<=A_*<=g`, `0<=M_*<=u_o-1`

rejects `10,250` of those states, leaving `123,585`. In the `t=1` slice it rejects `295`, leaving `5,520`.

These are abstract parameter-state diagnostics, not graph counts and not realizability evidence. No claim is made that states with `m>g+1` are excluded by this comparator.

---

## Mandatory negative control and trust boundary

`X_3` has `u=0` and never enters this branch, which requires `k>0`, a common buffer, positive buffer slack and at least `g+1` outside unmatched witnesses. Nothing here excludes the order-12 hostile control.

Promoted level: hand-proved conditional structural theorem inside the rigid one-code branch. The new deductions use raw D2C criticality, tight-code adjacency, the already-audited rigid Hall identities and literal physical edge/nonedge counts. They do not use the finite source-tuple theorem. The exact `Ccap_P`, `(ONE-P)` and `(CROWD)` constraints remain mandatory on every survivor; the present gain comes from physical geometry before another scalar pair relaxation.

## Next move

Stay on `m=g+1` long enough to intersect `(S-MR)` and `(QE-MR)` with the exact pair-local `Ccap_P/(ONE-P)/(CROWD)` system **without replacing `S_P` by total `C0`**. The first equality geometry to test is `A_*=0`, where `z_*` is complete to `H_M` and `(SEP-X)` makes the whole core block `H_0` isolated inside `G[X]`. Feed that exact `e(X)` collapse into the pair-local slack allocation and rooted unused-slot ledger. Only if this survives should `m=g+2` be opened.