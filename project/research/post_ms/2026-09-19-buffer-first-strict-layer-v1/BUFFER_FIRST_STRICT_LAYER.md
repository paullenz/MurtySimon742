# First strict unloaded-buffer layer: unique-hole funnel

Date: 2026-09-19

Status: internal conditional structural theorem inside the audited rigid one-code `z=1` common-buffer branch. It follows the rooted matched-edge collapse of the former equality layer. No global eventual theorem or graph-realizability claim is made; `X_3` remains the mandatory negative control and lies outside this positive-buffer setup.

## 1. Why this is now the live layer

`BUFFER_ROOTED_MATCHED_EDGE_COLLAPSE.md` proves that an unloaded buffer cannot attain its old floor `epsilon_b=p-g`. Thus the closest surviving unloaded geometry is

> `d_Y(b)=0`, `epsilon_b=p-g+1`.                          `(S1)`

This note classifies that first strict layer before opening the loaded-buffer, `z=2`, or four-exception branches. The move is forced by the new upstream theorem and remains inside the 19 September audit boundary. The source-tuple theorem is not used here.

Retain

- `A=X dotcup Y`, `X--Y` complete, `x>=3`, `y>0`;
- every Y-code is `d`, while every X-code is neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`;
- `U_o=U\U_-`, `u_o=|U_o|`;
- the unloaded assumptions `e(Y)=e(Y,U_d)=e(G[U_-])=0` and `d_Y(b)=0`.

Put

`h_X=e_bar({b},X)`,

`h_o=e_bar({b},U_o)`.

---

## 2. Unit I — exact buffer-defect identity

The buffer has exactly

- the root neighbour;
- one matched neighbour in each of the `p` tight fibres;
- `x-h_X` neighbours in X;
- no Y-neighbour;
- no neighbour in `U_-\{b}`;
- `u_o-h_o` neighbours in `U_o`.

Since the root degree is `2p+u` and `u=k+1+u_o`, direct degree subtraction gives

> **`epsilon_b=t+h_X+h_o`.**                              `(DEF)`

Hence the first strict layer `(S1)` has exactly two physical subtypes:

1. **X-hole subtype:** `h_X=1`, `h_o=0`;
2. **outside-hole subtype:** `h_X=0`, `h_o=1`.

There is no hidden third way to spend the extra unit.

---

## 3. Unit II — the outside-hole subtype is impossible

Assume `h_X=0`, `h_o=1`. Let `z_0` be the unique non-neighbour of `b` in `U_o`.

Then `b--X` is complete.

For any buffer edge `bx`:

- a matched Orientation-A certificate is impossible by the preserved matched-channel collapse;
- an outside-U Orientation-A certificate is impossible by the new outside-certificate self-pricing theorem, because such a certificate would force `h_X>=1`;
- a reverse Orientation-B certificate cannot use the root, a matched endpoint, Y, `U_-`, or X for the same raw common-neighbour reasons as in the repaired buffer analysis;
- among `U_o`, only `z_0` is nonadjacent to `b`, so every reverse certificate would have to use this same physical witness `z_0`.

But the fixed pair `(b,z_0)` has one graph-fixed common neighbourhood. If it is a singleton, it determines at most one X-head. Thus `z_0` can reverse-certify at most one edge `bx`, whereas `b` is adjacent to all `x>=3` X-vertices.

Contradiction.

Therefore:

> **FIRST-STRICT SUBTYPE COLLAPSE.** The first strict unloaded layer has
>
> `h_X=1`, `h_o=0`.                                       `(S2)`

In particular `b` is complete to `U_o` and has a unique non-neighbour in X.

---

## 4. Unit III — reverse buffer criticality is impossible in the unique-X-hole subtype

Let `a_0` be the unique X-vertex with `ba_0 notin E`.

Consider any actual buffer edge `bx`, so `x in X\{a_0}`. A reverse certificate would require a witness `z` with

`xz in E`, `bz notin E`, `N(b) cap N(z)={x}`.             `(REV)`

No location survives.

- `z=v` is adjacent to b.
- `z` matched: b and z both lie in `B=N(v)` and share the root.
- `z in U_o`: impossible because `b--U_o` is complete by `(S2)`.
- `z in U_-`: b and z have the same code `bar d`, so they share their tight matched neighbours.
- `z in Y`: every vertex of Y sees all of X, while b sees `X\{a_0}`. Thus `N(b) cap N(z)` contains at least `x-1>=2` X-vertices.
- `z in X`: because `c(z)` is neither `d` nor `bar d`, it agrees with `c(b)=bar d` in at least one tight coordinate. Hence b and z have a common matched neighbour, so their common neighbourhood cannot be the singleton X-head in `(REV)`.

Thus no reverse orientation is available for any of the `x-1` buffer--X edges.

The preserved matched-channel collapse also excludes matched Orientation A. Therefore:

> **every edge `bx`, `x in X\{a_0}`, has an outside-U Orientation-A certificate.** `(S3)`

So the first strict layer does not merely contain one outside certificate: it contains one for every buffer neighbour in X.

---

## 5. Unit IV — unique-hole rooted funnel

Fix `x in X\{a_0}` and choose an outside certificate `z_x in U_o`:

`bz_x in E`, `xz_x notin E`, `N(x) cap N(z_x)={b}`,

`c(z_x)=bar c(x)`, and `z_x` is anticomplete to Y.        `(OUT)`

Because `c(x) != bar d`, choose any tight coordinate `i` with `c(x)_i=d_i`. As in the rooted matched-edge collapse, b and `z_x` share the matched endpoint `q_i` selected by `bar d` in this fibre, and `z_x q_i` is a rooted B-edge.

The outside-certificate self-pricing proof says that **every** rooted certificate of this edge must use an X-vertex nonadjacent to b. There is exactly one such vertex, `a_0`.

Hence:

> for every `x in X\{a_0}` and every coordinate `i` on which `c(x)_i=d_i`, the rooted B-edge `z_x q_i` is certified through the same physical vertex `a_0`. `(FUNNEL)`

This is a literal unique-hole funnel, not a score relaxation.

---

## 6. Unit V — exact orientation/code dichotomy at the funnel

Write supports relative to d:

`S_0={i:c(a_0)_i != d_i}`,

`S_x={i:c(x)_i != d_i}`,

and `I_x=[p]\S_x={i:c(x)_i=d_i}`.

Both `S_0` and `I_x` are nonempty because X contains neither `d` nor `bar d`.

For each `i in I_x`, `(FUNNEL)` leaves exactly two possible rooted orientations for `z_x q_i`.

### Forward

The source is `z_x`, the witness is `a_0`, and the singleton head is `q_i`:

`N(z_x) cap N(a_0)={q_i}`.

A rooted slot has source and A-witness nonadjacent, so `z_x a_0` is a nonedge. Also `a_0 q_i` is an edge. Since `q_i` is the `bar d` endpoint in fibre i,

> `i in S_0`.                                             `(F-CODE)`

For fixed physical pair `(z_x,a_0)`, its singleton common neighbourhood is graph-fixed. Therefore at most one coordinate in `I_x` can use the forward orientation.

### Reverse

The source is `q_i`, the witness is `a_0`, and the singleton head is `z_x`:

`N(q_i) cap N(a_0)={z_x}`.

Now `z_x a_0` is an edge while `q_i a_0` is a nonedge. Hence

> `i notin S_0`.                                          `(R-CODE)`

Because adjacency `z_x a_0` is a single graph fact, forward and reverse orientations cannot be mixed for different coordinates of the same outside witness.

It follows that every buffer neighbour x satisfies the sharp dichotomy:

> **Type F:** `z_x a_0` is a nonedge, `|I_x|=1`, and the unique coordinate in `I_x` lies in `S_0`; or
>
> **Type R:** `z_x a_0` is an edge and `I_x cap S_0=emptyset`, equivalently `S_0 subseteq S_x`. `(DICH)`

Thus the first strict layer has converted a degree defect into a Boolean support-nesting condition.

---

## 7. Unit VI — ordinary funnel heads are separated from the unique hole

In Type R we have `z_x a_0 in E`. The original outside certificate `(OUT)` has

`N(x) cap N(z_x)={b}`.

Therefore `xa_0` must be a nonedge; otherwise `a_0` would be a second common neighbour of x and `z_x`.

Consequently:

> if `|I_x|>=2`, then x is necessarily Type R, so
>
> `S_0 subseteq S_x` and `x a_0 notin E`.                `(SEP)`

Equivalently, every X-neighbour of `a_0` among the buffer neighbours must be Type F and hence has

> `|S_x|=p-1`.                                            `(EXTREME)`

So **all internal X-edges incident with the unique buffer hole are forced onto almost-complementary A-codes**. Any buffer neighbour whose code is not at Hamming radius `p-1` from d is physically separated from `a_0`.

This is the first structural bridge from the strict buffer defect to X-density/Hall geometry.

---

## 8. Consequence and next move

The former equality layer is closed, and the first strict unloaded layer is now reduced to one sharply located geometry:

- exactly one buffer--X hole `ba_0`;
- no buffer--`U_o` holes;
- every remaining buffer--X edge is outside-U certified;
- all rooted matched-edge certificates generated by those outside witnesses funnel through `a_0`;
- every buffer-neighbour code is either almost complementary to d (`|S_x|=p-1`) or contains the full support `S_0` and is nonadjacent to `a_0`.

The next attack should intersect `(DICH)/(SEP)` with the existing exact Hall X-density identity and pair-local `Ccap_P`. The key question is now finite and structural: either many Type-F heads force an extreme-radius code population, or Type-R dominance makes `a_0` nearly isolated in `G[X]` and forces nested code support. Either outcome should be priced before moving to the loaded buffer.

If the first strict layer survives that density/support intersection, feed its unique physical hole into the rooted slot/residual ledger. Only after this layer is closed or sharply classified should the loaded-buffer alternative be promoted. `m=g+2`, `z=2`, and the four-exception gate remain deferred.

`X_3` remains unaffected because its canonical root has `u=0` and it never enters this common-buffer positive-U branch.
