# Residual-one k=2 F0--Y certificate correction: forward branch is impossible

Date: 2026-09-20

Status: **same-session hostile correction and strengthening**, conditional on the audited rigid one-code residual-one interface, `k=2`, `J2=empty`, and the compressed typical-F0 setup. No finite scan is used. This note explicitly supersedes the forward-witness part of `ONE_CODE_R1_K2_PURE_F0_Y_EDGE_CERTIFICATE_OBSTRUCTION.md` and the downstream golden forward/reverse/dual witness split in `ONE_CODE_R1_K2_Q1_CERTIFICATE_WITNESS_SPLIT.md`.

The global caveat is unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`.

## 1. Audit reconciliation

The 20 September daily red-team gate remains binding: `X_3` is the mandatory hostile control; repaired P1/P2 semantics and the later raw same-code / ordered `(source,witness)` audit remain the valid upstream interface; exact pair-local quantities must stay pair-local; finite parameter scans are not graph evidence.

This hostile replay found a concrete mistake in the immediately preceding same-session F0--Y analysis. The old forward branch allowed the witness to be an atypical U-vertex. That is impossible because the source is itself in U, so the rooted vertex is an unavoidable second common neighbour.

There is also a scope correction to the raw two-orientation lemma used in the predecessor note: the convenient singleton orientation follows automatically for an edge lying in a triangle. It is not a theorem for an arbitrary edge without checking that deleting the edge does not separate its own endpoints beyond distance two. The present F0--Y application is safe because a typical F0 vertex has H-neighbours and Y is complete to H, so every typical F0--Y edge lies in a triangle.

## 2. Setup

Use the exact residual-one low-k notation

- `K={a,b}`;
- `W_s={z_a,z_b}`;
- `I=[p]\{j}`;
- `J2=empty`, so the A-code repertoire is
  - `d` on Y,
  - `C=d xor e_j` on K,
  - `d xor e_i` on `h_i in H`, `i in I`;
- on the exact stress ray, `y=p-1`, `u=x=p+1`, and the escape reservoir `E=U\W_s` has size `p-1`.

Let T be the predecessor typical F0 set. Thus, after the compressed equality reductions, a typical `t in T` is K-free and W_s-free, misses `q_j`, has sparse private support, is Y-near-complete and H-near-complete, and `G[T]` is independent.

Fix an edge `ty`, with `t in T` and `y in Y`.

## 3. The old forward U-witness branch is impossible

Suppose the edge `ty` uses the orientation sourced at `t`:

`r in N(y)\N[t]`,

`N(t) cap N(r)={y}`.                                      `(FC-FWD)`

Because `t in U`, it is adjacent to the rooted vertex v.

Any candidate `r in U` is also adjacent to v, so v is a common neighbour of t and r distinct from y. Hence no U-vertex can satisfy `(FC-FWD)`.

The same root obstruction excludes the tight matched/root-neighbour layer. Therefore a forward witness would have to lie in A.

But `A=X union Y` here:

- if `r in X`, then r is adjacent to every Y-vertex, while t has `y-o(p)` Y-neighbours, so `N(t) cap N(r)` contains many Y-vertices;
- if `r in Y`, then r is adjacent to every H-vertex, while t has `p-o(p)` H-neighbours, so `N(t) cap N(r)` contains many H-vertices.

Thus a typical F0--Y edge has **no valid forward orientation**.

> **Every typical F0--Y edge is forced into the reverse orientation.** `(FC-REVONLY)`

This invalidates the predecessor claim that forward witnesses may lie in the atypical escape reservoir.

## 4. Reverse witnesses have code `bar d` and lie in U

The reverse orientation has

`w in N(t)\N[y]`,

`N(y) cap N(w)={t}`.                                      `(FC-REV)`

Because y has code d, any matched endpoint seen by both y and w would be a common neighbour distinct from t. Therefore w must disagree with d in every tight coordinate:

> `c(w)=bar d`.                                           `(FC-CODE)`

At `J2=empty` and `p>=3`, the complete A-code repertoire is `d`, `d xor e_j`, and the `d xor e_i`. None equals `bar d`. Hence

> `A_{bar d}=empty`, so every reverse witness lies in `U_{bar d}`. `(FC-LOC)`

The two selected witnesses `z_a,z_b` also have code `bar d`, but neither can serve as w. If `z_h` were a witness, its selected K-head h is adjacent to z_h and every y in Y, producing a common neighbour h distinct from t. Thus

> **`w in U_{bar d}\W_s`.**                               `(FC-LOC+)`

Moreover, because Y is complete to X, the singleton equation `(FC-REV)` forces

> **`N_X(w)=empty`.**                                     `(FC-X0)`

## 5. Every reverse witness is a residual-hub neighbour

At `J2=empty`, a q_j-nonneighbour has code `d xor S` with `S subseteq I`; in particular it agrees with d at coordinate j.

A vertex of code `bar d` disagrees with d at j. Therefore a reverse witness cannot be a q_j-nonneighbour:

> **every reverse F0--Y witness is adjacent to `q_j`.**   `(FC-HUB)`

Combined with `(FC-X0)` and the selected-witness exclusions, the reverse witness class is forced into the K-free / W_s-free residual-hub side. Thus the predecessor F0 hub-spoke theorem applies directly to every such physical witness.

This is an important redirection: the witness reservoir is not an arbitrary atypical escape population. It is a very specific `U_{bar d}` hub-neighbour population.

## 6. Certificate capacity sharpens the density threshold from the golden ratio to one half

Let

`|T|=(tau+o(1))p`,

`|Y|=(q+o(1))p`, with `q>0`,

and let B be the set of distinct reverse witnesses used by the T--Y edge certificates.

A fixed ordered pair `(y,w)` has one graph-fixed common-neighbour set, so it can certify at most one head t. Therefore one physical reverse witness can certify at most `|Y|` T--Y edges.

The typical T--Y demand is

`|T||Y|-o(p^2)`.

Hence

> **`|B| >= |T|-o(p)`.**                                 `(FC-BSIZE)`

Since `G[T]` is independent, a reverse witness cannot itself lie in T: it must be adjacent to its certified head t. Thus B and T are disjoint.

On the exact q=1 ray, `|E|=p-1`, so

`|T|+|B| <= p-1`.

Together with `(FC-BSIZE)`, this gives

> **`tau <= 1/2+o(1)`.**                                 `(FC-HALFPOP)`

This supersedes the predecessor golden threshold

`tau <= (sqrt(5)-1)/2 = 0.618...`.

The golden ratio appeared only because the invalid forward-U-witness branch was allowed to contribute certificate capacity.

## 7. Reverse witnesses carry an exact load-sensitive physical price

For `w in B`, let `R_w` be the number of T--Y edges reverse-certified by w. Distinct certified edges using w have distinct Y-sources by ordered-pair injection, so w is nonadjacent to at least `R_w` distinct vertices of Y.

On the exact q=1 ray,

`p+u-1=2p`,

and the exact U-side identity is

`2p-epsilon_w=d_{A union U}(w)`.

Using `N_X(w)=empty`, `d_Y(w)<=y-R_w=p-1-R_w`, and `d_U(w)<=u-1=p`,

`2p-epsilon_w <= (p-1-R_w)+p`.

Therefore

> **`epsilon_w >= 1+R_w`.**                              `(FC-SLACK)`

Summing over B, if D is the number of reverse-certified T--Y edges,

> **`E_B >= |B|+D`.**                                    `(FC-E)`

The same certificates also consume distinct physical Y--B nonedges:

> **`Z_Y(B) >= D`.**                                     `(FC-ZY)`

And `(FC-X0)` gives

> **`Z_X(B)=x|B|`.**                                     `(FC-ZX)`

So the corrected certificate subsystem has a purely reverse, load-sensitive price. It does not need the predecessor forward/reverse/dual LP.

## 8. The half-density endpoint has a paired-star normal form

Suppose the exact q=1 ray approaches the population boundary `tau=1/2` and the reverse capacity bound is asymptotically sharp. Then

- `|B|=|T|+o(p)`;
- virtually every available ordered pair `(y,w) in Y x B` must be used as a reverse certificate;
- hence B is Y-anticomplete up to `o(p^2)` exceptional pairs;
- every used `(y,w)` has a unique head `t in T` with `N(y) cap N(w)={t}`.

Now count triples `(w,t,y)` with `wt,ty in E`. Since every `t in T` is Y-near-complete,

`sum_{wt in E(B,T)} d_Y(t) = (y-o(p)) e(B,T)`.

At capacity equality, the certificate pairs contribute `|B|y-o(p^2)` singleton triples. Consequently

> **`e(B,T)=|B|+o(p)`.**                                 `(FC-ANCHOR)`

Thus the half-density extremal geometry is not a dense exceptional reservoir. It is an asymptotic **anchor matching**: B and T have equal linear size, but only about one B--T edge per B vertex, while each matched pair can support almost the whole Y-certificate fan.

Equivalently, for almost every fixed y, the certificate assignment is asymptotically a bijection between B and T; the sparse B--T graph must support essentially the same perfect-matching-scale anchor structure.

This creates the additional located missing-U block

> **`M_U(B,T) >= |B||T|-|B|-o(p^2)`.**                  `(FC-BT)`

Together with T-independence, this materially raises the corrected weighted price at the boundary.

In the exact idealization where B is completely Y-anticomplete, same-code criticality also forbids B--B edges: a same-code U--U edge in `U_{bar d}` would require an A_d=Y witness, but no Y-vertex is adjacent to either endpoint. This exact equality observation is useful as a hostile model, but no asymptotic `e(B)=o(p^2)` theorem is claimed here without an additional stability argument.

## 9. What is superseded and what survives

The following parts of the predecessor same-session chain are withdrawn:

1. the assertion that a forward typical F0--Y certificate can use an atypical escape U-witness;
2. the unrestricted edge version of the raw two-orientation lemma (triangle-edge scope is sufficient here);
3. the F/R/B witness-population LP on q=1;
4. the golden threshold `tau<=rho=(sqrt(5)-1)/2`;
5. the derived golden dual-role equality geometry;
6. the piecewise `W_min(tau)` formula and `W_min(rho)=2`, because they price a branch that does not exist.

The following predecessor conclusions survive and are strengthened:

- reverse witnesses are X-anticomplete;
- ordered `(source,witness)` injection remains valid;
- T--Y criticality requires a positive-density exceptional witness reservoir;
- the correct reservoir is now localized to `U_{bar d}\W_s`, adjacent to q_j;
- the population threshold strengthens to `tau<=1/2+o(1)`;
- the half-density endpoint has a sparse anchor-matching rather than golden dual-role structure.

## 10. Next attack

The highest-value next step is the residual-hub edge of every `w in B`. The preserved F0 hub theorem gives only two outcomes for `wq_j`:

- a forward hub certificate, consistent with the already-forced Y-antichain but also forcing anticompleteness to the K-heavy reservoir;
- a reverse hub certificate through H, producing an injective H--B rectangle.

Thus a linear B population either creates additional H--U holes or is pushed entirely into the forward hub arm. The forward-only endpoint should then be combined with `(FC-BT)`, T-independence, the exact `E_B/Z_X/Z_Y` price, and the rooted residual/Q ledger. The redirected `y=o(p)` regime remains a separate large-gap target.

No eventual theorem or finite threshold is claimed by this correction.