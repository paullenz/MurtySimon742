# Zero-buffer code simplex and small-lambda closure

Date: 2026-09-19

Status: internal hand-theorem package in the rigid one-code `z=1` unloaded common-buffer branch. It is conditional on the same rigid-cut hypotheses as the preceding one-code work. It does **not** claim the eventual second-extremal theorem.

## 1. Audit reconciliation

Before forward mathematics this run, `CURRENT_STATE.md`, the root `README.md`, the latest commits, the 19 September daily adversarial audit/handoff, the source-premise repair, and the independent actual-D2C Hall/pair-capacity regression were reread.

There is no departure from the audit priority order. The two source-tuple premises remain repaired at the raw/selected level; the finite source-tuple theorem is not treated as unconditional graph-level closure; the graph-level regression still records zero graph/formula mismatches and retains `X_3`; no actual rigid complete Hall cut with `x>=3` has yet been found, so the present branch remains a conditional hand implication; exact `Ccap_P`, `(ONE-P)` and `(CROWD)` remain available and are not replaced by a scan. The four-exception gate remains subordinate.

The current handoff had already proved, in the zero-buffer common-buffer subbranch, that the reverse matched channel is empty and every buffer--X edge is certified by an outside unmatched witness. The highest-value next move was therefore to apply raw criticality to the *other* zero-buffer edge family, namely `b--U_o`, before doing more scalar optimization.

## 2. Setup

Retain the zero-buffer common-buffer hypotheses:

- `X--Y` is a complete rigid A-cut, with `x=|X|>=3`, `y=|Y|>0`;
- every vertex of `Y` has code `d`, and `A_{\bar d}=emptyset`;
- `g=p`, `k=x-p>0`, so `x=p+k`;
- `U_-=U_{\bar d}=W_0 dotcup {b}`, with `|W_0|=k`;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- `epsilon_b=0`, hence `b` is complete to `X` and to `U_o:=U\U_-`, and anticomplete to `Y`;
- every `w in W_0` has exactly one X-neighbour, its graph-fixed core head;
- for each tight fibre `i`, the gamma-`d` matched endpoint `q_i` has exactly one X-neighbour `h_i`, and the `p` matched heads `h_i` are distinct;
- every buffer--X edge `bx` has an outside witness `z_x in U_o` with
  `xz_x notin E`, `bz_x in E`, `N(x) cap N(z_x)={b}`, and
  `c(z_x)=bar(c(x))`.

Put

> `u_o=|U_o|=u-k-1`,
>
> `rho:=u-k=u_o+1`.

Then

> `u=k+rho`,
>
> `y=p+rho-lambda-1`.

The preceding exact common-core identity and reverse collapse give

> `E_core=k(p+k-1)+H_core`,
>
> `H_core>=k`,
>
> hence `E_core>=k(p+k)`.

The published `X_3` control has `u=0` and never enters these hypotheses.

## 3. Unit I — raw criticality of every buffer--outside edge

Fix `z in U_o`. Zero buffer slack gives `bz in E`.

Because both `b,z` lie in `U subset B`, they share the root. Thus the edge `bz` lies in a triangle, so D2C criticality supplies one of the two singleton-common-neighbour orientations.

### Theorem 3.1 — outside-edge orientation

Exactly the following orientation can survive:

> there is `a_z in X` such that
>
> `ba_z in E`, `za_z notin E`,
>
> `N(z) cap N(a_z)={b}`.                                  `(BUO)`

The opposite orientation is impossible.

### Proof

Any singleton witness for the triangle edge `bz` lies in `A`: a B-witness shares the root with the U-source, producing an extra common neighbour, and the root itself has the matched neighbours of the U-source in its common neighbourhood.

Suppose first that the witness `a` is adjacent to `z` and nonadjacent to `b`, with

`N(b) cap N(a)={z}`.

Since `b` is complete to X and anticomplete to Y, `a in Y`. But `X--Y` is complete and `b` is complete to X, so every vertex of X is a common neighbour of `a` and `b`. Since `x>=3`, the common neighbourhood cannot be the singleton `{z}`. Contradiction.

Therefore the surviving orientation has `a_z` adjacent to b and nonadjacent to z, hence `a_z in X`, and its singleton is `(BUO)`. square

This is a raw graph-criticality statement and uses no witness-incidence injectivity.

## 4. Unit II — the whole outside layer is anticomplete to Y

### Corollary 4.1

For every `z in U_o`,

> `N_Y(z)=emptyset`,                                      `(YUO0)`
>
> and `c(a_z)=bar(c(z))`.                                 `(COMP-UO)`

### Proof

Every `y in Y` is adjacent to `a_z` because the cut is complete. If `yz` were also an edge, y would be a second common neighbour of `z` and `a_z` in `(BUO)`. Hence `z` is anticomplete to Y.

Also `(BUO)` has no matched B-vertex in its singleton common neighbourhood. Therefore `z` and `a_z` cannot agree in any tight coordinate, so their Boolean codes are complementary. square

The core `W_0` is already anticomplete to Y because every core vertex is used as a crossing witness, and b is anticomplete to Y by the zero-buffer branch. Hence:

### Corollary 4.2 — total Y--U anticompleteness

> `e(Y,U)=0`.                                             `(YU0)`

In particular `U_d=emptyset`: an outside vertex of code d would require an X-witness of code `bar d`, but `A_bar d=emptyset`, while `U_-=U_bar d`.

Every `y in Y` therefore has exactly x neighbours in `A union U`, namely X. The A-degree identity gives the exact slack

> `epsilon_y=p+u-x=rho`,
>
> `L_Y=y rho=rho(p+rho-lambda-1)`.                        `(LY-rho)`

Also every selected beta source must be a U-neighbour, so

> `ell_y=0` for every `y in Y`.                            `(Y-beta0)`

Thus all beta load, if any, is expelled into X.

## 5. Unit III — the X-code simplex is exact

Orient each tight coordinate i so that bit 1 means adjacency to the gamma-d endpoint `q_i`.

Since

> `N_X(q_i)={h_i}`

and the matched heads `h_1,...,h_p` are distinct, one has

> `c(h_i)=e_i`                                             `(SIMP-1)`

for the ith unit vector.

Every core head belongs to `H_0=X\H_M`; it is not any `h_i`, hence is nonadjacent to every `q_i`. Therefore every core head has code

> `0^p`.                                                   `(SIMP-0)`

Consequently:

### Theorem 5.1 — code-simplex form

> `supp_A(X)={0^p,e_1,...,e_p}`,                           `(SIMP)`
>
> with multiplicities
>
> `n_{0^p}=k`, `n_{e_i}=1`.

This is a physical-code classification, not a population inequality.

## 6. Unit IV — exact support duality with U_o

The reverse-collapse certificate for every `x in X` supplies `z_x in U_o` with

`c(z_x)=bar(c(x))`.

Conversely Unit I supplies, for every `z in U_o`, an `a_z in X` with

`c(a_z)=bar(c(z))`.

Therefore:

### Theorem 6.1 — support duality

> `supp_U(U_o)=bar(supp_A(X))`
>
> `={1^p,1^p-e_1,...,1^p-e_p}`.                            `(DUAL)`

In particular

> `u_o>=p+1`,
>
> `rho>=p+2`.                                              `(POP+)`

This strengthens the preceding mere requirement `u_o>=1` by a whole matched-core order.

## 7. Unit V — small Boolean dimensions are impossible

The outside code pair `P={d,bar d}` is disjoint from X because X is a union of whole complementary-pair families and Y occupies d outside X.

For `p=1`, the Boolean cube has only P, so X cannot be nonempty.

For `p=2`, the simplex support `{00,10,01}` touches both complementary pairs of the 2-cube: `{00,11}` and `{10,01}`. No pair remains for P.

For `p=3`, the four simplex codes `000,e_1,e_2,e_3` lie in four distinct complementary pairs, which exhaust all `2^(3-1)=4` complementary pairs. Again no pair remains for P.

Hence:

> `p>=4`.                                                  `(P4)`

This is independent of the scorecard.

## 8. Unit VI — a stronger physical A--U hole ledger

The total A--U nonedge count `Z` has three disjoint contributions.

1. By `(YU0)`, all `yu` pairs in `Y x U` are nonedges.
2. Each of the k core vertices has exactly one X-neighbour, so `X x W_0` contributes exactly `k(x-1)` nonedges.
3. In `X x U_o`, the selected buffer-X certificates cover every X-row by a nonedge, while `(BUO)` covers every U_o-column by a nonedge. Therefore this bipartite nonedge set has size at least `max(x,u_o)`.

Thus

> `Z>=yu+k(x-1)+max(x,u_o)`.                              `(Z-PHYS)`

Using the exact rooted identity

> `Z=u(p-lambda)+2q+E_U`

and `y-(p-lambda)=rho-1=u_o`, this becomes the lambda-free physical residual floor

> `2q+E_U`
>
> `>=u u_o+k(x-1)+max(x,u_o)`.                            `(QE-PHYS)`

Together with `E_U>=k(p+k)`, exact integer minimization gives

> `q+E_U`
>
> `>=E_0+ceil([D_phys-E_0]_+/2)`,                         `(QE-MIN)`
>
> where `E_0=k(p+k)` and
>
> `D_phys=u u_o+k(x-1)+max(x,u_o)`.

This is a stronger rooted-residual feed than the previous selected-witness-only hole count.

## 9. Unit VII — quadratic zero-buffer score gate

The exact disjoint contributions `E_core` and `L_Y` give

> `S=E_U+L_A`
>
> `>=k(p+k)+rho(p+rho-lambda-1)`.                         `(S-QUAD)`

The gamma collision floor remains simultaneous:

> `S>=k(p+k)+max{p(p-1),rho(p+rho-lambda-1)}`             `(S-QUAD+)`

for `p>=4`.

For an above-`M(n)` candidate,

> `S<=C0=(lambda+3)p+(lambda+2)u-2H_lambda-4`,
>
> `H_lambda=floor((lambda+1)^2/4)`.

Substituting `u=k+rho` into `(S-QUAD)` gives the necessary quadratic gate

> `(k+rho-lambda-3)p`
>
> ` +k(k-lambda-2)`
>
> ` +rho(rho-2lambda-3)`
>
> ` +2H_lambda+4 <=0`.                                    `(QG)`

This is a hand consequence of physical incidence. No finite scan is used in the proof.

## 10. Unit VIII — lambda=1 and lambda=2 are closed

The preceding run already closed `lambda=0`.

Write `rho=p+s`; `(POP+)` gives `s>=2`, and `(P4)` gives `p>=4`.

For `lambda=1`, `(QG)` becomes

`k^2+(p-3)k +2p^2+3ps-9p+s^2-5s+6 <=0`.

Over `p>=4,s>=2,k>=1`, every term combination is minimized at the boundary `p=4,s=2,k=1`, where the left side is already positive. Hence no `lambda=1` candidate exists.

For `lambda=2`, `(QG)` becomes

`k^2+(p-4)k +2p^2+3ps-12p+s^2-7s+8 <=0`.

Again the expression is increasing away from `p=4,s=2,k=1` on the allowed integer region; at that boundary it equals 7. Hence no `lambda=2` candidate exists.

Therefore:

> **SMALL-IMBALANCE ZERO-BUFFER CLOSURE.**
>
> The zero-buffer rigid one-code common-buffer branch has no above-`M(n)` candidate with
>
> `lambda in {0,1,2}`.                                    `(L012)`

The `lambda=0` case is the preceding scorecard theorem; `lambda=1,2` are closed here by the new code-support geometry plus `(QG)`.

## 11. Unit IX — lambda=3 collapses to three scalar cases

Set `lambda=3`; then `H_lambda=4`.

With `rho=p+s`, `(QG)` is

> `k^2+(p-5)k`
>
> ` +2p^2+3ps-15p+s^2-9s+12 <=0`.                        `(L3G)`

For `p>=5`, this is minimized at `k=1,s=2`, where it is already positive. Hence `p=4`.

At `p=4`, `(L3G)` reduces to

> `k^2-k+s^2+3s-16<=0`.

Since `s>=2`, one must have `s=2`, hence

> `rho=6`.

Then the inequality is `k^2-k-6<=0`, so

> `k in {1,2,3}`.

Thus the entire lambda=3 zero-buffer branch is reduced structurally to

> `(p,rho,k)=(4,6,1),(4,6,2),(4,6,3)`.                   `(L3-3)`

A bounded checker reproduces this reduction, but the reduction above is the proof.

## 12. Unit X — minimal-support extra slack

The lambda=3 residue has `rho=p+2`, hence

> `u_o=p+1`.

By `(DUAL)`, U_o has exactly p+1 represented codes, so there is exactly one U_o vertex in each complementary simplex code. Let `z_0` be the unique vertex of code `1^p`, complementary to the core-head code `0^p`.

Every one of the k core heads must use `z_0` as its buffer-X witness. Therefore `z_0` is nonadjacent to every core head. Unit IV of the reverse-collapse proof also forces the corresponding k core witnesses in W_0 to be nonadjacent to `z_0`.

Unit II gives `z_0` no Y-neighbours. Hence its possible neighbours in `A union U` are contained in

- the p matched heads;
- b;
- the other p vertices of U_o.

So

> `d_{A union U}(z_0)<=2p+1`.

But

> `d_{A union U}(z_0)=p+u-1-epsilon_{z_0}`
>
> `=2p+k+1-epsilon_{z_0}`

when `u=k+p+2`. Thus

> `epsilon_{z_0}>=k`.                                     `(Z0-SLACK)`

This slack lies outside both `E_core` and `L_Y`. Therefore in the minimal-support layer

> `S>=k(p+k)+L_Y+k`.                                      `(MS-SCORE)`

For `(p,rho,k)=(4,6,3)`, the right side is

`21+36+3=60`,

while `C0=57`. Hence the k=3 lambda=3 case is impossible.

## 13. Unit XI — the minimal-support X-layer is independent

Assume `p>=4` and `rho=p+2`.

The simplex codes `0^p,e_1,...,e_p` contain no complementary pair, so an internal X-edge cannot be direct.

A matched-B certificate sourced in X would require a matched endpoint whose gamma code equals the source code. But at `g=p` every matched gamma code is `d` or `bar d`, while X avoids both. Thus the matched channel is unavailable.

For an A/U certificate sourced at `x in X`, the witness must have code `bar(c(x))`. In the minimal-support layer `(DUAL)` gives exactly one such physical vertex `z_x in U_o`, and there is no A-vertex or U_- vertex of that code. But the buffer-X certificate has already fixed

> `N(x) cap N(z_x)={b}`.

The same ordered physical pair cannot certify an internal X-edge with a different singleton head.

Whichever endpoint of a putative X-edge is chosen as source, the same obstruction applies. Therefore

> `e(X)=0`.                                                `(X0)`

Since the unloaded branch also has `e(Y)=0` and `X--Y` is complete,

> `f=e(A)=xy`.                                             `(F=XY)`

## 14. Unit XII — lambda=3, k=2 is impossible

For `(p,rho,k)=(4,6,2)`,

- `u=8`, `u_o=5`;
- `x=y=6`;
- `(X0)` gives `f=36`;
- `D_M=2p+u-H_lambda-1=11`, so an above-threshold candidate has `delta<=10`;
- `(Z0-SLACK)` and the core floor give
  `E_U>=k(p+k)+k=12+2=14`;
- `(QE-PHYS)` gives
  `2q+E_U>=8*5+2*5+6=56`.

But the exact residual identity gives

`f=(p-lambda)(p+u)+q+E_U-delta`

and hence

> `q+E_U=24+delta`.

Therefore

`2q+E_U=2(24+delta)-E_U`
`<=48+20-14=54`,

contradicting the required 56.

So k=2 is impossible. Together with Unit X, only

> `(lambda,p,rho,k)=(3,4,6,1)`                            `(L3-LAST)`

survives this run.

## 15. Exact ledger for the sole lambda=3 survivor

For `(lambda,p,rho,k)=(3,4,6,1)`,

- `u=7`, `u_o=5`;
- `x=5`, `y=6`;
- `a=11`, `n=27`;
- `f=xy=30`;
- `D_M=10`, so `delta<=9`;
- `L_Y=36`;
- `E_core>=5`, `epsilon_{z_0}>=1`, so `E_U>=6`;
- `(QE-PHYS)` gives `2q+E_U>=44`.

The exact score identity is

> `S=2delta+lambda(p+u)-p=2delta+29`.

Since `S>=42`, integrality gives `delta>=7`. Thus

> `delta in {7,8,9}`.

Also `q=e(G[U])`. Here U has seven vertices and at least the two forced U-nonedges `wb` and `wz_0`, so

> `q<=19`.

The residual identity gives

> `q+E_U=19+delta`.

Combining `q<=19`, `L_A>=L_Y=36`, and `S=2delta+29` leaves exactly the following six score tuples:

> `(delta,E_U,q,L_X)`
>
> `(7,7,19,0)`,
>
> `(8,8,19,1)`, `(8,9,18,0)`,
>
> `(9,9,19,2)`, `(9,10,18,1)`, `(9,11,17,0)`.

These are algebraic/physical necessity states, not realizability claims.

The first state is particularly rigid: all allowable U-edges except the two forced holes are present, `L_X=0`, and the complete simplex-support pattern is exact. This is now a small structural object for direct edge-criticality attack, not a broad parameter strip.

## 16. Trust boundary, negative control, and next move

No source-tuple theorem was needed for the new closures. The new ingredients are raw edge criticality of `b--U_o`, exact Boolean code adjacency to the matched gamma-d endpoints, already-established reverse-collapse certificates, and exact rooted identities.

No raw-witness injectivity is assumed. The row/column cover in `(Z-PHYS)` counts physical A--U nonedges. Support duality asserts only existence of code classes, except in the explicitly stated minimal-support layer where population equality forces one vertex per code.

`X_3` remains untouched: its canonical root has `u=0`, whereas this branch requires `u_o>=p+1`.

The next attack should **not** move to `z=2`. First exhaust `(L3-LAST)`, beginning with the delta=7 equality state where `q=19`, `E_U=7`, `L_X=0`, U is missing only the two already-forced edges at the coarse ledger level, and the five U_o code classes are fixed. Raw criticality of the resulting dense U_o edge set is the highest-value target. If that closes, test the five remaining delta=8/9 slack states before advancing to `lambda=4`.

The exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain available as secondary checks, but the present gain came from retaining physical incidence rather than relaxing back to total pair capacity.
