# Exceptional-gamma-foot collapse in the `t=1` E2 frontier

Date: 2026-09-19

Status: conditional hand mathematics inside the audited rigid one-code / positive-buffer / minimal-reservoir branch. This is not graph-realizability evidence and does not assert the false all-order 2019 conjecture. The published order-12 graph `X_3` remains a mandatory negative control.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, the root `README.md`, the latest commits through `924f98f78cee240df3b5b87ab9a07eaa9f53f07c`, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, and the independent actual-D2C regression.

The audit boundary is unchanged:

- distinct physical beta-source identity is accepted only at the raw singleton-criticality level actually proved;
- global `(source,coordinate)` uniqueness is selected-representative uniqueness, not raw-witness uniqueness;
- the finite source-tuple theorem is not used as unconditional graph-level closure;
- the actual-D2C regression retains `X_3`, has zero recorded graph/formula mismatches, and still has no positive fixture realizing the full rigid complete-cut hypotheses;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- the four-exception gate remains subordinate.

The predecessor asked to trace the physical selected-witness geometry by raw criticality rather than add another scalar residual inequality. This note follows that instruction. The result invalidates the previously identified `d0=2` shared-core endpoint and replaces it by a stronger matched-foot localization.

## 2. Setup

Retain the first positive-buffer equality geometry:

- `X--Y` complete, `x>=3`, `y>0`;
- every `Y`-code is `d`, while `X` contains neither `d` nor `bar d`;
- `P={d,bar d}` and `g=g_P` is the number of tight fibres whose two gamma codes form `P`;
- `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k=x-g>0`;
- `b--X` and `b--U_o` complete, `b--Y` empty;
- in the minimal reservoir `m=g+1`, every X-code class has one selected outside witness in `U_o`; the repeated core class `H_0` of size `k` has common witness `z_*`, and the singleton `H_M` classes have distinct selected witnesses;
- a selected outside witness `z_s` serving head/code class `h_s` satisfies
  `c(z_s)=bar c(h_s)`, is anticomplete to `Y`, and its own certificate has
  `N(h_s) cap N(z_s)={b}`.

For a head `h`, write `S(h)` for the support of `c(h)` relative to `d`.

## 3. Unit I — secondary criticality of a wrong-head witness edge

Let `z_s` be the selected outside witness serving `h_s`, and suppose it is adjacent to a wrong head `h_t!=h_s`.

Because `b` is adjacent to both `z_s` and `h_t`, the edge `z_s h_t` lies in a triangle. Apply triangle-edge criticality.

### Orientation II is impossible

Suppose a witness `w` satisfies

`w~h_t`, `w!~z_s`, `N(z_s) cap N(w)={h_t}`.

- `w in B=N(v)` is impossible because `w` and `z_s` share the root `v`.
- `w in X` is impossible because `b` is a second common neighbour of `w,z_s`.
- `w in Y` is impossible because `S(h_s)` is nonempty (`X` contains no code `d`). At every coordinate `j in S(h_s)`, `c(z_s)=bar c(h_s)` agrees with `d`, so `z_s` and the Y-vertex share the selected matched endpoint in fibre `j`. Hence their common neighbourhood cannot be the singleton `{h_t}`.

No location survives.

### Orientation I forces a matched foot

Thus there is a witness `w` with

`w~z_s`, `w!~h_t`, `N(h_t) cap N(w)={z_s}`.

- `w in A` is impossible: a Y-vertex is nonadjacent to `z_s`; an X-vertex shares every nonempty Y-vertex with `h_t`.
- `w in U_o` is impossible because `b` is adjacent to both `w` and `h_t`.
- `w=b` is impossible because `b~h_t`.
- `w in U_-\{b}` has code `bar d`. Since `c(h_t)!=d`, the two codes are not complementary, so `w` and `h_t` share a selected matched endpoint, contradicting singletonness.

Therefore `w` is a matched endpoint; call it `q`.

The generalized matched-foot localization already used in the audited zero-buffer closure applies to

`q!~h_t`, `N(h_t) cap N(q)={z_s}`,

because the singleton member `z_s` is unmatched. Hence

> **`gamma(q)=c(h_t)`.**                                  `(SG1)`

Also `q!~b`, otherwise `b` would be another common neighbour of `h_t,q`. Since `b` has code `bar d`, `q` is the endpoint selected by `d` in its tight fibre, say fibre `j`. The adjacency `q~z_s`, together with `c(z_s)=bar c(h_s)`, then implies

> **`j in S(h_s)`.**                                      `(SG2)`

Combining:

> **SECONDARY MATCHED-FOOT THEOREM.** Every active wrong-head adjacency `z_s~h_t` chooses a support coordinate `j in S(h_s)` such that the `d`-selected matched endpoint `q_j^d` satisfies
>
> `gamma(q_j^d)=c(h_t)`.                                  `(SG)`

This is a raw triangle-criticality statement plus the previously audited matched-foot localization. It uses no cross-source witness injectivity.

## 4. Unit II — only exceptional gamma fibres can carry wrong-head traffic

If fibre `j` belongs to the complementary gamma pair `P={d,bar d}`, then both of its matched endpoints have gamma code in `{d,bar d}`. But `(SG1)` says the relevant endpoint has gamma code `c(h_t)`, and `X` contains neither `d` nor `bar d`.

Therefore:

> **EXCEPTIONAL-FIBRE LOCALIZATION.** Every wrong-head selected-witness edge uses one of the `t=p-g_P` tight fibres whose gamma pair is not `P`. `(EF)`

Consequences for arbitrary `t`:

- `S(h_s)` must meet the exceptional coordinate set;
- the target code is one of at most `t` graph-fixed gamma codes, one from each exceptional fibre.

For `t=1`, let `e` be the unique exceptional coordinate and put

`c_e:=gamma(q_e^d)`.

Then every wrong-head edge satisfies simultaneously

> `e in S(h_s)`,                                          `(T1-S)`
>
> `c(h_t)=c_e`.                                           `(T1-T)`

Thus **all wrong-head traffic in the entire minimal reservoir targets one fixed X-code class**. This supersedes the earlier treatment in which each support coordinate was allowed an independent target gamma code.

## 5. Unit III — the previous `d0=2` shared-core topology is impossible

In the shared-core `R2+R2` topology, write

- core support `{r}`;
- defect supports `{r,i}` and `{r,j}`.

The predecessor's deepest endpoint had `d0=2`, meaning the common core witness `z_*` was adjacent to both defect heads of two distinct codes.

But `z_*` has source support `{r}`. By `(SG)`, every wrong head adjacent to `z_*` must have the single graph-fixed code `gamma(q_r^d)`. Two distinct defect codes cannot both equal it.

Hence

> **`d0<=1`.**                                            `(D0)`

In particular the entire previously promoted `h=1,c=2,d0=2` endpoint — including all 39 bounded exact/one-unit rows retained after the `M>=2` filter — is graph-theoretically impossible. The 39-row ledger remains useful as a historical diagnostic but is no longer a live frontier.

## 6. Unit IV — exact `t=1` E2 traffic hierarchy

The one-exception theorem makes the finite E2 support geometry much smaller. For a fixed exceptional coordinate `e` and target code `c_e`, a source class can contribute wrong-head traffic only if

1. its support contains `e`;
2. its support intersects the target support (the previously proved support-intersection condition);
3. it is not the target's own selected class.

If the target is the repeated core class, one eligible source witness can contribute at most `k` incidences; otherwise the target class is singleton and contributes at most one.

A direct case split over the canonical E2 supports gives the following sharp envelopes when all support-eligible singleton classes are present (missing classes only lower them).

### `R2+R2`

| overlap `h` | core incidences `c` | maximum `J` |
|---|---:|---:|
| 1 | 2 | `2k` |
| 1 | 1 | `k` |
| 0 | 1 | `k` |
| 1 | 0 | `2` |
| 0 | 0 | `1` |

For every `k>=3`, the unique maximum `2k` occurs in the shared-core topology `h=1,c=2`, with

> `e=r`, `c_e=c(H_0)`, and `d0=0`.                       `(CHEAP-R22)`

Both defect witnesses may then point into the core class; the common core witness has no wrong-head edge at all.

### `R3`

- if the radius-three defect contains the core coordinate (`c=1`), `J<=k`;
- if it does not (`c=0`), `J<=1`.

Thus the shared-core `R2+R2` topology remains the correct pair-cheapest E2 family, but **with the opposite core orientation from the previous handoff**: `d0=0`, not `d0=2`.

The companion checker independently exhausts the canonical support/exceptional-coordinate choices and verifies this table for a broad range of `k`.

## 7. Unit V — every X-edge also localizes to the exceptional gamma pair

There is a second use of the same criticality mechanism which is independent of selected outside witnesses.

Let `xy` be any edge of `G[X]`. It lies in triangles through `b` and every Y-vertex. Take one triangle-edge criticality orientation

`w~x`, `w!~y`, `N(y) cap N(w)={x}`.

Exactly as in the zero-buffer X-edge proof:

- the root, Y, `b`, X, and `U_o` locations are impossible;
- a vertex of `W_0` has code `bar d` and shares a matched neighbour with `y` because `c(y)!=d`;
- the only surviving location is a matched endpoint `q`.

Matched-foot localization gives

> `gamma(q)=c(y)`.                                        `(XE1)`

Since `c(y)` is not `d` or `bar d`, the fibre of `q` cannot be one of the `g_P` P-fibres. Therefore, at `t=1`, `q` lies in the unique exceptional fibre. Let its gamma pair be

`P_e={c_e^0,c_e^1}`.

Then

> **EXCEPTIONAL-PAIR VERTEX-COVER THEOREM.** Every edge of `G[X]` has at least one endpoint whose X-code lies in `P_e`. `(XE2)`

There is a useful injective strengthening. Suppose a code `c in P_e` is represented in X. There is exactly one matched endpoint `q_c` in the exceptional fibre with `gamma(q_c)=c`. For every X-edge whose only P_e-coded endpoint is a vertex `y` of code `c`, its criticality certificate must use this same `q_c` and has

`N(y) cap N(q_c)={the other endpoint}`.

A fixed pair `(y,q_c)` has only one singleton head. Hence

> every P_e-coded X-vertex has X-degree at most one whenever the complementary gamma code is absent from X. `(XE3)`

## 8. Unit VI — shared-core R2+R2 forces `e(X)<=k`

In the shared-core R2+R2 code support, the represented X-codes are:

- one repeated radius-one core code;
- two radius-two defect codes with supports `{r,i}` and `{r,j}`;
- the remaining singleton radius-one codes.

No two represented X-codes are complementary.

For `p>=4`, this is immediate from support size: complements of radius-one codes have radius at least three, and the only possible radius-two/radius-two complement coincidence at `p=4` would require disjoint supports, whereas the two defects share `r`.

For `p=3`, the H_M population consists exactly of the two defects, and a direct check of `{r}`, `{r,i}`, `{r,j}` again shows no complementary pair.

Therefore `P_e` meets X in at most one code class. That class has multiplicity at most `k`, with equality only if it is the repeated core class. By `(XE2)--(XE3)`,

> **`e(X)<=k`.**                                          `(EX-K)`

This is much stronger than the old support-channel density envelopes. It is a raw criticality consequence of `t=1` plus the E2 code geometry.

For a row with common-witness parameter `A`, the preserved maximum is

`Emax(A)=binom(g,2)+kA`,

so

> `Delta=Emax(A)-e(X)`
> ` >= binom(g,2)+kA-k`.                                  `(DELTA-K)`

Also `(T1-T)` lets `z_*` see at most one H_M code class, hence

> `A>=g-1`.                                               `(A1)`

## 9. Unit VII — corrected pair-local gate

The preserved selected-witness slack/Hall decomposition is

`sum epsilon_selected >= p(g+1)+k+M-J`,

`L_X >= [D+2Delta]_+`.

At `t=1`, `g=p-1`, so `p(g+1)=p^2`. Units IV and VI give `J<=2k` and `(DELTA-K)`. Therefore every shared-core R2+R2 survivor satisfies the new pair-local necessary condition

> **`p^2+M-k`
> ` +[D+2(binom(g,2)+kA-k)]_+`
> ` <= C0-sigma_P`,**                                    `(NEW-PAIR)`
>
> with `A in {g-1,g}`.

This keeps the audit-mandated exact `sigma_P/Ccap_P` budget. It does not replace pair slack by total score slack.

The former deep endpoint

`p^2+M-k-8<=C0-sigma_P`

came from a topology (`d0=2`) now ruled out by `(D0)`. It must not be used as a live equality model.

In the uniquely traffic-maximal corrected geometry `(CHEAP-R22)`, `A=g`, the exceptional coordinate is the repeated-core coordinate, the exceptional d-endpoint has gamma equal to the core code, `H_M` is independent, and all wrong-head traffic is defect-witness-to-core traffic. If equality is approached in `(NEW-PAIR)`, the surviving X-graph is therefore forced toward a matching-like graph with at most one X-neighbour per core vertex, rather than the dense H_M geometry assumed by the old endpoint.

## 10. Consequence and next move

This run changes the frontier materially:

1. the 39 preserved exact/near `d0=2` states are not survivors — their topology is impossible;
2. the correct `t=1,E=2,k>=3` pair-cheapest family is still shared-core R2+R2, but it has `d0=0`, unique exceptional coordinate `r`, a single target code equal to the repeated core code, and `J<=2k`;
3. independently, all X-edges are controlled by the unique exceptional gamma pair, giving `e(X)<=k` and the corrected pair gate `(NEW-PAIR)`.

The next coherent attack is therefore not the old five-U-nonedge endpoint. It is the corrected shared-core `d0=0` exceptional-fibre geometry: intersect `(NEW-PAIR)` with the exact rooted residual/slot ledger and classify equality in `e(X)<=k`. Only if that survives should the `J<=k` R2+R2/R3 alternatives be opened.

`X_3` is unaffected: it has `u=0` and does not enter the rigid positive-buffer/minimal-reservoir hypotheses.
