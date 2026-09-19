# Unloaded common-buffer source-edge dichotomy

Date: 2026-09-19

Status: internal hand theorem for the minimal common-buffer comparator in the rigid one-code `z=1` branch. It is conditional on the same rigid-cut hypotheses as the preceding one-code work. It does not use the finite source-tuple theorem and does not claim an eventual bound.

## 1. Why this branch is now load-bearing

The full-support `z=1`, `h=0` branch has just been sharpened substantially: raw criticality forces every source to be nonadjacent to its unique omitted `U_-` vertex, so the previous apparent `-y` savings disappear. The other minimal `z=1` support type is the common-buffer branch. It therefore becomes necessary to subject its cheapest unloaded geometry to the same raw-criticality test before moving to `z=2`.

This is not a departure from the 19 September audit. It remains inside the audit-authorized one-code rigid branch, and `X_3` is unaffected because its canonical root has `u=0`.

## 2. Setup

Use the purified one-code notation:

- the rigid A-cut is `X--Y`, complete, with `x=|X|>=3`, `y=|Y|`;
- every source in Y has code d and `A_{bar d}=emptyset`;
- `g=g_P`, `k=x-g>0`;
- `U_-=U_{bar d}` has size `k+1`;
- every source uses exactly k unmatched crossing witnesses and exactly g matched gamma-d feet.

In the **common-buffer** support type there is a k-set

`W_0 subset U_-`

used by every source, and one buffer

`b in U_-\W_0`

which is unused by every crossing certificate.

Restrict in this note to the **unloaded** common-buffer comparator

> `e(Y)=e(Y,U_d)=e(G[U_-])=0`.                             `(2.1)`

This is exactly the `H=0` branch singled out by the previous handoff as the cheapest common-buffer geometry. In particular Y is independent, the core and buffer are mutually nonadjacent, and every source is nonadjacent to every core witness because each core member is used by every source.

Put

- `U_o=U\U_-`, `u_o=|U_o|=u-k-1`;
- `r=d_Y(b)`, the number of sources adjacent to the buffer;
- `nu_b=y-r`, the number of source--buffer nonedges;
- `d_o=d_{U_o}(b)`;
- `H_Y` = the total number of Y--`U_o` nonedges.

The common-core slack floor already proved is

> `E_core>=k(p+k-2)`.                                      `(2.2)`

## 3. Structural unit I — any source--buffer edge is triangle-free

Fix `s in Y` with

> `s b in E(G)`.                                           `(3.1)`

### Theorem 3.1

The edge `s b` has no common neighbour at all:

> `N(s) intersect N(b)=emptyset`.                         `(3.2)`

Equivalently every source--buffer edge in the unloaded common-buffer branch is a direct, triangle-free critical edge.

### Proof

Suppose `s b` lay in a triangle. Since deleting a triangle edge leaves its endpoints at distance two, D2C criticality supplies an external damaged vertex in one of the two singleton-common-neighbour orientations.

**Orientation A.** There is z with `s z` an edge, `b z` a nonedge and

`N(b) intersect N(z)={s}`.

The witness z cannot be in B, since b and every B-vertex share the root; and it cannot be the root. Thus `z in A`. Since Y is independent while `s z` is an edge, `z in X`. The displayed singleton contains no matched-B vertex, so b and z have no common matched neighbour. Tight-code complementarity therefore gives

`c(z)=bar c(b)=d`.

Pair purity says every A-vertex of code d lies in Y, contradicting `z in X`.

**Orientation B.** There is z with `b z` an edge, `s z` a nonedge and

`N(s) intersect N(z)={b}`.                                `(3.3)`

All possible locations are impossible:

- `z=v`: s has one matched B-neighbour in every tight fibre, so its common B-neighbourhood with the root cannot be the singleton `{b}`;
- `z in X`: impossible because `X--Y` is complete, contrary to `s z` being a nonedge;
- `z in Y`: every X-vertex is a common neighbour of s and z, and `x>=3`;
- `z in U_-`: impossible because `(2.1)` makes `U_-` independent;
- `z in U_o`: the singleton `(3.3)` has no matched-B vertex, so `c(z)=bar c(s)=bar d`, forcing `z in U_-=U_{bar d}`, contradiction;
- z matched: the same generalized matched-foot localization used in the full-support note gives `gamma(z)=c(s)=d`. Every source already uses all g gamma-d matched endpoints as crossing witnesses, so the graph-fixed common neighbourhood of `(s,z)` is already a singleton X-head, not the unmatched vertex b.

Both orientations are impossible. Therefore the temporary assumption that `s b` lies in a triangle is false. `square`

This theorem is per edge and uses no witness injectivity across sources.

## 4. Structural unit II — a loaded source edge expels the buffer from X

If `r>0`, choose a source `s` adjacent to b. Every `x0 in X` is adjacent to s because the rigid cut is complete. If b were adjacent to any such `x0`, then `x0` would be a common neighbour of s and b, contradicting Theorem 3.1.

### Corollary 4.1

If the buffer has even one Y-neighbour, then

> `d_X(b)=0`.                                              `(4.1)`

Thus the buffer has a sharp all-or-nothing source-visibility dichotomy:

- if `d_X(b)>0`, it is anticomplete to Y;
- if `d_Y(b)>0`, it is anticomplete to X.

This is stronger than the preceding loaded-buffer statement, which obtained `d_X(b)=0` only when the buffer was used by an auxiliary selected certificate.

## 5. Structural unit III — buffer--U_o edges force rectangular Y-holes

Assume `r>0` and let

`R=N_Y(b)`, `|R|=r`.

If `z in N_{U_o}(b)`, then Theorem 3.1 applied to every edge `s b`, `s in R`, says z cannot also be adjacent to s. Hence

> `R x N_{U_o}(b)`

is an anticomplete rectangle.

### Corollary 5.1 — rectangular hole product

> `H_Y>=r d_o`.                                           `(5.1)`

This is physical graph incidence, not certificate counting. Sharing the same buffer--`U_o` neighbour across many sources multiplies the Y-hole bill rather than saving it.

## 6. Structural unit IV — exact buffer slack when `r>0`

Under `(2.1)` and Corollary 4.1, the buffer has exactly

- one root neighbour;
- p matched-fibre neighbours;
- r Y-neighbours;
- no X-neighbours;
- no neighbours in `U_-\{b}`;
- `d_o` neighbours in `U_o`.

Since the root has maximum degree `b_total=2p+u`, the buffer slack is exactly

> `epsilon_b=p+k+u_o-r-d_o`.                              `(6.1)`

In particular

> `epsilon_b>=p+k-r`.                                      `(6.2)`

Combining `(5.1)` and `(6.1)` gives a useful traffic/slack trade: increasing `d_o` lowers buffer slack by one but creates at least r new Y-holes.

## 7. Structural unit V — exact Y-slack with source--buffer adjacency

Every source has

- k forced nonedges to the common core `W_0`;
- a buffer nonedge exactly when it is outside `R`, contributing `nu_b=y-r`;
- the Y--`U_o` holes counted by `H_Y`;
- no internal Y-edge by `(2.1)`.

The A-degree identity therefore gives

### Lemma 7.1

> `L_Y=y(p-g+1)-r+H_Y`.                                  `(7.1)`

Using `(5.1)`,

> `L_Y>=y(p-g+1)-r+r d_o`.                               `(7.2)`

Thus a source--buffer edge saves one omitted-pair nonedge, but any buffer--`U_o` edge used to recover buffer degree creates r Y-holes at once.

## 8. Structural unit VI — exact one-dimensional direct-buffer score profile

Let

`A0=phi(g)`,

`P0=p+k+u_o`,

`L_r=y(p-g+1)-r`.

For fixed `r>=1`, equations `(5.1)`, `(6.1)`, `(7.1)` and the independent gamma floor give

> `S`
> ` >= E_core + P0-r-d_o`
> `    +max{A0, L_r+r d_o}`.                              `(8.1)`

The feasible range is

> `0<=d_o<=min(u_o,P0-r)`.                                `(8.2)`

Define the exact integer profile

> `Theta_r`
> ` :=min_{0<=d<=min(u_o,P0-r)}`
> `     {P0-r-d+max[A0,L_r+r d]}`.                        `(8.3)`

Then every unloaded common-buffer geometry with exactly r source neighbours satisfies

> `S>=E_core+Theta_r`.                                    `(8.4)`

For `r>1`, the objective decreases with d while the gamma term dominates and increases with d once the Y-slack term dominates, so the minimizer is one of the two integers nearest the crossing

> `d=(A0-L_r)/r`,                                         `(8.5)`

clamped to the feasible interval. For `r=1` the post-crossing objective is flat. Hence `(8.3)` is an explicit O(1) candidate calculation, not a new high-dimensional optimization.

## 9. Structural unit VII — the anticomplete-buffer branch `r=0`

If `r=0`, Theorem 3.1 is vacuous because there is no source--buffer edge, and the buffer may use X-neighbours. However, its physical degree still gives a clean floor.

The buffer has no Y-neighbour and no other `U_-` neighbour. It can have at most x X-neighbours and at most `u_o` outside-U neighbours. Therefore

`epsilon_b`
` >= p+k+u_o-x-u_o`
` =p-g`,                                                   `(9.1)`

because `x=g+k`.

All y source--buffer pairs are nonedges, so

> `L_Y>=y(p-g+1)`.                                        `(9.2)`

Thus:

### Theorem 9.1 — anticomplete-buffer score floor

> `S`
> ` >=E_core+(p-g)`
> `   +max{phi(g),y(p-g+1)}`.                             `(9.3)`

The zero-slack buffer case is extremely rigid: equality in `(9.1)` requires `g=p`, b complete to X, and b complete to `U_o`.

## 10. Unified unloaded common-buffer floor

Define

`Theta_0=(p-g)+max{phi(g),y(p-g+1)}`

and `Theta_r` by `(8.3)` for `1<=r<=y` whenever its feasible interval is nonempty. Then

### Theorem 10.1

> `S>=E_core+min_{0<=r<=y} Theta_r`.                      `(10.1)`

This is a structural strengthening of the predecessor common-buffer gate

`S>=phi(g)+E_core`,

because it prices the buffer itself and the Y-slack forced by whether that buffer is adjacent or nonadjacent to the outside sources.

## 11. Diagnostic impact

On the same abstract parameter grid used by `check_one_code_z1_near_saturation.py` (`3<=p<=18`, `1<=u<=18`, all admissible lambda and `3<=x<a`):

- predecessor common-buffer score gate survivors: 76,463;
- survivors after Theorem 10.1: 64,892;
- additional abstract states rejected within the common-buffer model: 11,571.

Among the surviving parameter states, the cheapest branch is `r=0` in 40,589 cases and `r>0` in 24,303 cases. These are **not graph counts** and do not establish realizability.

The full-support forced-nonedge/outside-spill gate has 59,028 survivors on the same grid; at the coarse existential parameter level those are contained in the new common-buffer survivor set. Thus the common-buffer branch, not full support, is now the limiting minimal `z=1` comparator on this diagnostic grid.

## 12. Negative control and next move

`X_3` has `u=0`, so the common-buffer branch is inactive and the mandatory hostile graph remains allowed.

The next coherent attack should stay on the common-buffer branch rather than move to `z=2`. In particular:

1. inspect the exact `r=0` equality geometry, especially the forced `g=p`, complete-X/complete-`U_o` structure when buffer slack is zero;
2. for `r>0`, combine the triangle-free source--buffer edges with raw criticality of the adjacent edges incident to the buffer and with the exact pair-local `Ccap_P` before replacing local slack by total `C0`;
3. preserve the full-support theorem as the more expensive comparator unless a new constraint reverses that ordering.
