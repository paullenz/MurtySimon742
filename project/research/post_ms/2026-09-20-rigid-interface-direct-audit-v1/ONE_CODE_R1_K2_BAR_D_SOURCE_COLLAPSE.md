# Residual-one k=2 `bar d` source collapse and quarter missing-U floor

Date: 2026-09-20

Status: **same-session conditional structural theorem**, under residual dimension one, `k=2`, `J2=empty`, `p>=3`. No finite scan is used.

This continues `ONE_CODE_R1_K2_U_DENSITY_SOURCE_CAPACITY.md`. The class previously identified as the only possible source of quadratic U-density collapses further: an H-anticomplete `bar d` source is automatically Y-anticomplete, and two such vertices cannot be adjacent. Consequently the U-layer itself has an asymptotic quarter-quadratic missing-edge floor.

## 1. The only linear-capacity source class

Recall

`B_0={w in U_{bar d}:d_H(w)=0}`.

The preceding source-capacity theorem showed:

- `bar d` vertices with an H-neighbour cannot source U--U edges;
- every non-`bar d` U-code has complementary A-class of size at most two;
- hence only B_0 can supply linear oriented U--U degree.

We now classify B_0 more sharply.

## 2. Every B_0 vertex is Y-anticomplete

Take `w in B_0`. Since `c(w)=bar d`, w sees every private endpoint `q_i`, `i in I`.

Fix i and apply raw criticality to the triangle edge `wq_i`.

### Orientation sourced at w

The witness must lie in A and be adjacent to q_i. At `J2=empty`, the unique A-head at q_i is h_i. Thus the forward orientation is

`N(w) cap N(h_i)={q_i}`.                                  `(BD-F)`

Since h_i is adjacent to every Y-vertex, `(BD-F)` implies

> `N_Y(w)=empty`.                                         `(BD-Y0)`

### Opposite orientation is impossible

A witness inside the rooted B-layer shares the root with q_i and cannot give a singleton U-head.

A Y-witness has h_i as an extra common neighbour with q_i.

An H-witness would have to be adjacent to w, impossible because `d_H(w)=0`.

A K-witness k is also impossible. Although k is nonadjacent to q_i for `i in I`, its selected witness `z_k in W_s` has code `bar d`, so `z_k q_i` is an edge; and `z_k k` is the selected head-witness edge. Hence `z_k` is an extra common neighbour of q_i and k, distinct from w.

Thus no reverse private-spoke orientation exists. The forward orientation `(BD-F)` is forced for every private coordinate, proving `(BD-Y0)`.

Therefore

> **every vertex of B_0 is simultaneously H-anticomplete and Y-anticomplete.** `(BD-A0)`

It may still have K-neighbours, but it misses the two large A-blocks H and Y.

## 3. B_0 is independent

Suppose `w,t in B_0` are adjacent.

They have the same code `bar d`. The raw same-code U--U theorem says either orientation must use a witness in the complementary A-code class `A_d=Y`.

But `(BD-Y0)` says no Y-vertex is adjacent to either endpoint. A Y-witness cannot be adjacent to the head of the certificate.

Hence no orientation exists, contradicting criticality.

> **`G[B_0]` is independent.**                            `(BD-IND)`

## 4. Exact asymptotic upper bound on U-edges

Let `b=|B_0|`.

Orient every U--U edge by one valid certificate.

- a source in B_0 can only head toward `U\B_0`, because B_0 is independent, so all edges sourced in B_0 lie among at most `b(u-b)` physical cross pairs;
- `U_{bar d}\B_0` has H-neighbours and therefore has zero source capacity by the predecessor theorem;
- every remaining U-vertex has complementary A-class of size at most two, so all edges sourced outside B_0 contribute at most `2(u-b)` oriented edges.

Consequently

> **`e(U) <= b(u-b)+2(u-b)`.**                           `(BD-EU)`

On the exact low-k ray `u=p+1`, write `b=(eta+o(1))p`. Then

`e(U)/p^2 <= eta(1-eta)+o(1) <= 1/4+o(1)`.

Therefore

> **`M_U >= (1/4-o(1))p^2`.**                            `(BD-QUARTER)`

This is independent of the old escape-class optimizer. It follows directly from the tiny A-code repertoire, raw source/witness injection, the global H/Y polarization, and the private-spoke fan.

Because the rooted ledger weights `M_U` by two, `(BD-QUARTER)` contributes at least coefficient `1/2` to `2M_U`.

## 5. B_0 also carries linear U-slack per vertex

For `w in B_0`, `(BD-A0)` gives at least

`|H|+y=2p-2`

A-nonneighbours on the exact ray. The exact per-U identity is

`z_A(w)+m_U(w)=p+epsilon_w`.

Hence

> **`epsilon_w >= p-2+m_U(w)`.**                         `(BD-SLACK)`

In particular, if `|B_0|=(eta+o(1))p`, then

> `E_U(B_0) >= (eta-o(1))p^2`,                           `(BD-ES)`

before the additional missing-U incidence term is counted.

Thus the U-density mechanism is expensive twice: the only linearly capable sources form an independent A-sparse class and themselves carry linear degree slack.

## 6. Current weighted gap

Combine only universally disjoint/safe terms on the exact ray:

- global H/Y polarization: `Z_X+Z_Y >= (1-o(1))p^2`;
- `(BD-QUARTER)`: `2M_U >= (1/2-o(1))p^2`;
- `(BD-ES)`: `E_U >= (eta-o(1))p^2`.

This is not yet a closure against the legitimate coefficient-four combined ceiling; eta is not bounded below by the quarter theorem alone. The importance of `(BD-QUARTER)` is structural: **the U-layer can no longer be asymptotically complete in this branch.**

The next optimization should retain eta explicitly and add the class-specific cost of `U\B_0`. In particular, when eta is small, `(BD-EU)` itself is much stronger than the universal quarter bound; when eta is large, `(BD-SLACK)` is stronger. Their tradeoff should be combined exactly with the A-side slack `L_A` and the rooted residual identity.

## 7. Trust boundary

The theorem remains conditional on reaching the rigid one-code residual-one `J2=empty` branch. It does not solve the upstream zero-positive-fixture gap, and it does not assert an eventual threshold.