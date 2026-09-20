# First-strict outside-U reverse fan

Date: 2026-09-20

Status: internal conditional structural theorem in the audited first-strict unloaded unique-hole branch. This strengthens `BUFFER_UO_Y_ANTICOMPLETENESS.md` and is independent of the later all-R resource calculations.

## 1. Every `b--U_o` edge is reverse-certified through X'

Fix arbitrary `w in U_o`. The first-strict theorem gives `bw in E`. The edge lies in a triangle through the root.

As in the Y-anticompleteness proof, a raw criticality witness for a U-source edge cannot lie at the root or in the root neighbourhood: the root would be an extra common neighbour distinct from the U-head. Hence the witness lies in A.

### Source b, head w is impossible

A witness must be nonadjacent to b, so it lies in `Y union {a_0}`.

- A Y-vertex is not adjacent to w by `BUFFER_UO_Y_ANTICOMPLETENESS.md`, so it cannot be adjacent to the head.
- If `a_0w in E`, a0 is still impossible as a singleton witness because b and a0 share a tight matched endpoint in every coordinate of the nonempty support `S_0={i:c(a_0)_i!=d_i}`: b has code `bar d`, and in those coordinates a0 selects the same `bar d` endpoint.

Thus the orientation `b -> w` has no certificate.

### Therefore source w, head b

A witness x must be adjacent to b, hence

> `x in X'=X\{a_0}`.

Raw criticality gives

> `wx notin E`,
>
> `N(w) cap N(x)={b}`.                                  `(UO-REV)`

This holds for **every** physical vertex `w in U_o`.

Consequently every outside-U column contains at least one located X'--U hole:

> `e_bar(X',U_o)>=|U_o|=u-k-1`.                         `(UO-XHOLE)`

## 2. Code consequence

The singleton in `(UO-REV)` leaves no room for a shared tight matched neighbour between w and x. Hence their codes are complementary:

> for each `w in U_o`, at least one reverse witness `x_w in X'` satisfies
>
> `c(w)=bar c(x_w)`.                                    `(UO-COMP)`

This is a direct raw-criticality localization, not a selected source-tuple argument.

## 3. One-witness corollary

In either `m=1` polarization, all vertices of X' have one common code C. Therefore `(UO-COMP)` collapses the entire outside layer to one code:

> `U_o subseteq V_{bar C}`.                             `(M1-UO-CODE)`

Now suppose two vertices `w_1,w_2 in U_o` were adjacent. They have the same code `bar C`. The independently audited same-code theorem says either U-source orientation requires an A-witness of code C. In a one-witness polarization `A_C=X'` (a0 has a different code in all-F; in all-R equality/coincidence it may join C, but b is still adjacent to every X' and the argument below can use a buffer-neighbour C-vertex). Any such X' witness is adjacent to b, while each source `w_i` is also adjacent to b. Thus b is a common neighbour distinct from the U-head, contradicting singleton certification.

In the all-F case, where `A_C=X'` exactly, this gives the clean theorem

> `G[U_o]` is edgeless.                                 `(F-UO-INDEP)`

Combined with `z--W_0=empty`, the all-F triangle ceiling sharpens to

> `q<=binom(u,2)-binom(k+1,2)-binom(u_o,2)-k`.         `(F-Q-UO)`

The terms are disjoint physical missing pairs: the independent `U_-`, the independent `U_o`, and the k cross pairs from z to `W_0`.

## 4. Why this matters

The outside reservoir is not free even before Hall optimization. Every outside vertex is forced to purchase an X' hole, and in the surviving one-witness all-F geometry the entire outside layer is one complementary code class and is independent. This gives a quadratic `binom(u_o,2)` physical loss in Q when the outside reservoir grows.