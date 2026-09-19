# Zero-buffer complete separation and unconditional branch closure

Date: 2026-09-19

Status: internal hand-theorem continuation inside the rigid one-code `z=1` unloaded common-buffer branch. This note strengthens `ZERO_BUFFER_CORE_OUTSIDE_SEPARATION_AND_LAMBDA7_FRONTIER.md` and closes the entire zero-buffer subbranch for every admissible `lambda>=0`. It does **not** claim the eventual second-extremal theorem; the rigid one-code hypotheses remain conditional hand implications because no actual D2C fixture with the full rigid complete Hall cut has yet been found.

## 1. Audit reconciliation and reason for departing from the lambda=7 handoff

Before forward mathematics, the current `CURRENT_STATE.md`, root `README.md`, latest commits, the 19 September daily red-team audit/handoff, `SOURCE_PREMISE_REPAIR.md`, and the independent actual-D2C Hall/pair-capacity regression were reread.

The audit order remains binding:

- distinct physical beta sources are proved from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a selected-representative convention, not raw-witness uniqueness;
- the finite source-tuple theorem is not used here as unconditional graph closure;
- the independent graph-level regression still contains hostile `X_3`, reaches the exact Hall/pair-capacity interface, and has no recorded graph/formula mismatch;
- no actual rigid complete Hall cut with `x>=3` has been found, so the one-code conclusions remain conditional on the rigid hypotheses;
- the four-exception gate stays subordinate.

The previous handoff proposed a local attack on the remaining lambda=7 `5 x 5` `X--U_o` matrix. The first raw-criticality classification of one such edge in fact does not depend on lambda=7. It proves `X--U_o` is empty throughout the zero-buffer branch. That stronger local theorem dominates the lambda-by-lambda programme, so this note follows it rather than continuing the superseded finite frontier. Exact `Ccap_P`, `(ONE-P)` and `(CROWD)` remain valid inherited constraints; they are simply not load-bearing once the physical edge set itself disappears.

The mandatory `X_3` control is untouched: its canonical root has `u=0`, whereas the branch below has `k>0` and `u_o>=p+1`.

## 2. Retained zero-buffer structure

Retain the established unloaded common-buffer zero-slack hypotheses:

- `X--Y` is complete, `x=|X|=p+k`, `k>0`, `y=|Y|>0`;
- all `Y` vertices have one code `d`, while `X` contains neither `d` nor `bar d`;
- `g=p`, so every matched endpoint has gamma code in `{d,bar d}`;
- `U_-=U_{bar d}=W_0 dotcup {b}`, `|W_0|=k`, and `U_-` is independent;
- `b` is complete to `X` and `U_o:=U\U_-`, and anticomplete to `Y`;
- `Y` is anticomplete to all of `U`;
- every `w in W_0` has exactly one X-neighbour, its core head;
- `U_o` is independent and `W_0--U_o` is anticomplete;
- with `rho:=u-k=u_o+1`, one has `rho>=p+2` and `p>=4`;
- the X-code simplex is `supp_A(X)={0^p,e_1,...,e_p}` with multiplicities `k,1,...,1`;
- `supp_U(U_o)` is its complementary support;
- the size relation is

  `y=p+rho-lambda-1>=1`.

We also retain the generalized matched-foot localization: if `q` is a matched endpoint, `a in A` is nonadjacent to `q`, and `N(a) cap N(q)` is a singleton whose member is not a matched endpoint, then

`c(a)=gamma(q)`.

This is the same coordinate-by-coordinate proof as the preserved matched-foot source-code lemma: the source chooses the mate of `q` in its own fibre and the endpoint opposite every matched neighbour of `q` in every other fibre.

## 3. Unit I — the entire X--U_o cut is empty

### Theorem 3.1

> `e(X,U_o)=0`.                                            `(XU0)`

### Proof

Fix `x in X`, `z in U_o`, and suppose `xz` is an edge. Since `b` is adjacent to both endpoints, the edge lies in a triangle. Diameter-2-criticality therefore gives one of the two singleton-common-neighbour orientations.

### Orientation A

There is a witness `t` with

`t~x`, `t!~z`, `N(z) cap N(t)={x}`.

The root cannot be `t`, because the root is not adjacent to `x`. A witness in `B=N(v)` is impossible because `z in B` and every B-vertex shares the root with z, giving an extra common neighbour distinct from x.

Thus `t in A=X dotcup Y`.

If `t in X`, then `b` is adjacent to both `z` and `t`, again giving an extra common neighbour.

If `t in Y`, then `c(t)=d`. The singleton `{x}` contains no matched endpoint. Hence `t` and `z` cannot agree in any tight coordinate; otherwise their common selected endpoint in that tight fibre would be a second common neighbour. Therefore

`c(z)=bar c(t)=bar d`.

But `U_{bar d}=U_-=W_0 dotcup {b}`, whereas `z in U_o`. Contradiction.

So Orientation A is impossible.

### Orientation B

There is a witness `t` with

`t~z`, `t!~x`, `N(x) cap N(t)={z}`.

The root cannot serve: `x` has one neighbour in each of the `p` tight fibres and is also adjacent to `b`, so `N(x) cap N(v)` contains many vertices besides z.

If `t in A`, then `t` cannot lie in Y because Y is anticomplete to U. If `t in X`, then x and t have every vertex of the nonempty set Y as a common neighbour, in addition to z. Hence no A-witness exists.

If `t in U`, then:

- `t=b` is impossible because `b~x`;
- `t in W_0` is impossible because `W_0--U_o` is anticomplete;
- `t in U_o` is impossible because `U_o` is independent.

The only remaining possibility is a matched endpoint `q`. Generalized matched-foot localization gives

`c(x)=gamma(q)`.

But `g=p` means every matched gamma code is `d` or `bar d`, while X contains neither code. Contradiction.

Both orientations fail, so `xz` cannot be an edge. This proves `(XU0)`. square

This theorem is raw physical criticality plus the already-retained code/gamma interface. No witness-incidence injectivity is used.

## 4. Unit II — X itself is independent

### Theorem 4.1

> `e(X)=0`.                                                `(X0)`

### Proof

Suppose `xx'` is an edge inside X. It lies in triangles through b and through every vertex of Y. Consider one singleton-criticality orientation with witness t adjacent to x, nonadjacent to x', and

`N(x') cap N(t)={x}`.

The reverse orientation is symmetric.

- The root is not adjacent to x, so it cannot be t.
- A Y-witness is adjacent to both x and x' because `X--Y` is complete, so it cannot be nonadjacent to x'.
- The buffer b is adjacent to both endpoints.
- If `t in X`, then b and every Y-vertex are common neighbours of x' and t, contradicting singletonness.
- If `t in U_o`, `(XU0)` prevents `t~x`.
- If `t in W_0`, then singletonness contains no matched endpoint, so `c(x')=bar c(t)=d`; but X has no code d.
- If t is a matched endpoint q, generalized matched-foot localization gives `c(x')=gamma(q) in {d,bar d}`, again impossible for X.

No witness type remains. Therefore no internal X-edge exists. square

The previous duplicate-complement upper bound `e(X)<=k(rho-p-2)` is thus superseded in the zero-buffer branch by exact independence.

## 5. Unit III — every unmatched vertex except b has degree one in A union U

The earlier `U_o` and `W_0--U_o` separation, together with `(XU0)` and `(X0)`, makes the local geometry exact.

For every `w in W_0`:

- its unique A-neighbour is its core head in X;
- it has no Y-neighbour;
- `U_-` is independent;
- it has no U_o-neighbour.

Thus `d_{A union U}(w)=1`.

For every `z in U_o`:

- `(XU0)` and Y--U anticompleteness give no A-neighbour;
- `U_o` is independent and `W_0--U_o` is empty;
- z is adjacent to b.

Thus `d_{A union U}(z)=1`.

The buffer b has zero slack. Since the unmatched-vertex slack identity is

`epsilon_u=p+u-1-d_{A union U}(u)`,

all `u-1` vertices in `U\{b}` have exact slack `p+u-2`. Therefore

> `E_U=(u-1)(p+u-2)`.                                     `(EU-EXACT)`

The unmatched graph itself is still exactly the `b--U_o` star, so

> `q=e(G[U])=u_o=rho-1`.                                  `(Q-EXACT)`

## 6. Unit IV — exact A-side slack

Every Y-vertex has precisely the x vertices of X as neighbours in `A union U`. Hence

> `epsilon_y=p+u-x=rho`,
>
> `L_Y=rho y`.                                             `(LY-EXACT)`

For X, the only edges from X into `A union U` are:

- all `xy` edges to Y;
- all x buffer edges to b;
- exactly k core-head edges to W_0;
- no X-edge by `(X0)`;
- no X--U_o edge by `(XU0)`.

Summing the A-vertex slack identity `epsilon_x=p+u-d_{A union U}(x)` over X gives

`L_X=x(p+u)-[xy+x+k]`.

Using `u=k+rho` and `y=p+rho-lambda-1`, this simplifies exactly to

> `L_X=x lambda+k(x-1)`.                                  `(LX-EXACT)`

Thus the full score is no longer a floor but an exact expression:

> `S=E_U+L_X+L_Y`
>
> ` =(u-1)(p+u-2)+rho y+x lambda+k(x-1)`.                 `(S-EXACT)`

## 7. Unit V — exact score gap factorization

For an above-`M(n)` candidate the preserved score ceiling is

> `S<=C0=(lambda+3)p+(lambda+2)u-2H_lambda-4`,             `(C0)`

where

> `H_lambda=floor((lambda+1)^2/4)`.

Substitute

`u=k+rho`, `x=p+k`, `y=p+rho-lambda-1`

into `(S-EXACT)-(C0)`. Direct expansion and collection gives

> `S-C0`
>
> `=2[ H_lambda`
> `    +(k-1)(k+p+rho-2)`
> `    +(rho-p-2)`
> `    +rho(y-2)`
> `    +3 ]`.                                              `(GAP)`

Every term is now structural. The first three terms are nonnegative under

`lambda>=0`, `k>=1`, `rho>=p+2`.

## 8. Unit VI — all y>=2 states are impossible

If `y>=2`, then the bracket in `(GAP)` is at least 3. Hence

> `S-C0>=6>0`.

This contradicts the necessary above-threshold ceiling `S<=C0`.

Therefore no zero-buffer above-M candidate can have `y>=2`.

This immediately subsumes the entire previous lambda=0,...,7 staircase and every larger-lambda state with at least two Y-sources.

## 9. Unit VII — the y=1 boundary is also impossible

It remains only to test `y=1`. The size relation gives

`lambda=p+rho-2`.

Since `rho>=p+2`,

> `lambda>=2p`.

Consequently

`H_lambda=floor((lambda+1)^2/4)`

is at least

`floor((2p+1)^2/4)=p^2+p`.

At `y=1`, `(GAP)` becomes

`(S-C0)/2`

`=H_lambda+(k-1)(k+p+rho-2)+(rho-p-2)-rho+3`

`=H_lambda+(k-1)(k+p+rho-2)-p+1`.

Therefore

> `(S-C0)/2 >= p^2+1>0`.

So the y=1 boundary is impossible as well.

Combining Units VI and VII gives the main conclusion.

### Theorem 9.1 — zero-buffer branch closure

> **No above-`M(n)` graph can realize the rigid one-code unloaded common-buffer branch with zero buffer slack (`g=p`).**

Equivalently, within the conditional rigid one-code setup, every live common-buffer candidate must have positive buffer slack

> `p-g>=1`.                                                `(POS-BUF)`

This is a structural closure for the whole subbranch, not a bounded-lambda computation.

## 10. Negative control and trust boundary

`X_3` remains a mandatory hostile control and is not touched: its canonical root has `u=0`, whereas this proof requires the nonempty one-code unmatched/common-buffer geometry, in particular `k>0` and `u_o>=p+1`.

The new load-bearing steps are:

1. raw triangle-edge criticality for X--U_o;
2. the already-preserved generalized matched-foot source-code rule;
3. raw triangle-edge criticality for X--X;
4. exact degree bookkeeping;
5. the preserved above-M score ceiling.

No finite source-tuple theorem, four-exception gate, or finite realizability scan is used. The companion checker only verifies the displayed algebra and a bounded diagnostic grid; it is not proof of realizability or of the structural criticality lemmas.

## 11. Forward implication

The zero-buffer line is finished. The next coherent target is the corrected common-buffer branch with

`p-g>0`.

Return to `COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md` and `COMMON_CORE_EXACT_SLACK_AND_REVERSE_DEFICIT.md`, retaining the corrected matched/outside witness dichotomy. Intersect the first positive-buffer geometry with exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` before any coarse total-score relaxation, then feed surviving physical holes/slack into the rooted residual ledger. Do not return to the closed zero-buffer or mixed `{4,5}` branches, and do not move to `z=2` while the positive-buffer common-buffer geometry remains live.
