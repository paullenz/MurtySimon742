# Residual-one k=2 pure-F0 Y-edge certificate obstruction

Date: 2026-09-20

Status: **same-session conditional structural theorem**, downstream of the audited rigid one-code residual-one interface, the hostile-replayed `k=2`, `J2=empty` package, and the compressed pure-F0 normal form. No finite scan is used. This note does **not** assert that the rigid complete Hall cut is graph-realizable; bounded actual-D2C regression still has zero positive rigid complete-cut fixtures with `x>=3`.

The immediate purpose is to attack the only coefficient-`1/2` endpoint left by `ONE_CODE_R1_K2_COMPRESSED_HALF_ADDITIVE_REFINEMENT.md`: an almost-independent F0 escape reservoir which is simultaneously almost complete to `H` and `Y`.

## 1. Independent stability replay of the half-barrier functional

Recall

`F = delta-delta^2/2 + alpha(1-delta) + vartheta(1+alpha) + mu(1+delta)`

with

`alpha+delta+vartheta+mu=1`.

Eliminating `alpha=1-delta-vartheta-mu` gives the exact identity

> `F - [1/2+(1-delta)^2/2]`
> `= mu(2delta-vartheta)+vartheta(1-vartheta)`.          `(FY-STAB0)`

The right side is nonnegative on the simplex. Indeed, if `vartheta<=2delta` this is immediate. If `vartheta>2delta`, its coefficient of `mu` is negative, so for fixed `delta,vartheta` it is minimized at `mu=1-delta-vartheta`; substitution gives

`delta(2-2delta-vartheta)>=0`.

Therefore the predecessor half barrier admits the stronger stability form

> **`F >= 1/2+(1-delta)^2/2`.**                         `(FY-STAB)`

In particular, `F<=1/2+eta` forces

> **`1-delta <= sqrt(2eta)`.**                           `(FY-STAB1)`

Moreover, once `delta>=1/2`, using `vartheta<=1-delta` in `(FY-STAB0)` gives

`2delta-vartheta>=3delta-1>=1/2`,

and `1-vartheta>=delta>=1/2`. Hence

> `F-1/2 >= (1-delta)^2/2 + (vartheta+mu)/2`.            `(FY-STAB2)`

Thus near equality quantitatively suppresses the T and mixed sectors linearly, while the total non-D mass is at most square-root scale.

This is an independent algebraic replay; it does not use the predecessor two-case minimization.

## 2. Raw edge-criticality lemma

For completeness, use only the definition of diameter-2-criticality.

Let `uv` be an edge of a diameter-2-critical graph. Deleting `uv` makes some pair have distance greater than two. Any path of length at most two destroyed by deleting `uv` must have `u` or `v` as an endpoint. Hence one of the following holds:

- there is `r in N(v)\N[u]` with `N(u) cap N(r)={v}`;
- there is `r in N(u)\N[v]` with `N(v) cap N(r)={u}`.

Call these the forward and reverse orientations of `uv`. A fixed ordered pair `(u,r)` determines its singleton common-neighbour set, so it can certify at most one forward endpoint `v`; similarly a fixed ordered pair `(v,r)` can certify at most one reverse endpoint `u`.

This is the only new general D2C fact used below.

## 3. The pure-F0 high-Y setup

Work in the `k=2`, `J2=empty` compressed endpoint. Write

`K={a,b}`, `W_s={z_a,z_b}`, `I=[p]\{j}`.

At coefficient `1/2`, the predecessor normal form has an escape set `E` with all but `o(p)` vertices in a typical F0 set `T` satisfying, uniformly after discarding another `o(p)` vertices if necessary,

- `N_K(t)=N_{W_s}(t)=empty`;
- `tq_j` is absent;
- private support `{i:tq_i in E(G)}` has size `o(p)`;
- `t` misses only `o(p)` vertices of `H`;
- `t` misses only `o(p)` vertices of `Y`;
- the typical F0 reservoir is independent.

The last three statements are exactly the sparse-support / half-barrier equality consequences: `M_U(E)` already supplies the full half-quadratic term, while `Z_X,Z_Y,E_U=o(p^2)` and the F0 sector identity force simultaneous H/Y near-completeness and average slack `2+o(p)`.

The argument below needs only the high-Y condition

> `y/p -> q>0`.                                          `(FY-HY)`

The exact low-k stress ray has `q=1`, since `y=p-1`.

## 4. Forward certificates for a typical F0--Y edge are exceptional

Fix `t in T` and `y0 in N_Y(t)`. Suppose the edge `ty0` takes the forward orientation, so

`r in N(y0)\N[t]`,

`N(t) cap N(r)={y0}`.                                   `(FY-F0)`

The witness `r` cannot lie in `X`: every X-vertex is adjacent to all of Y, while t has `q p-o(p)` Y-neighbours, so `(FY-F0)` would contain many Y common neighbours.

It cannot lie in Y: every Y-vertex is adjacent to all of H, while t has `p-o(p)` H-neighbours, so there would be many H common neighbours.

It cannot be a private matched endpoint `q_i`, `i in I`, because at `J2=empty` no Y-vertex is adjacent to `q_i`. It cannot be either selected witness `z_a,z_b`, because the residual-one hub theorem makes those witnesses Y-anticomplete. The root is also impossible: its common neighbours with t contain the large A-neighbourhood of t. The single residual hub `q_j` can contribute only `O(p)` certificates globally and is asymptotically negligible.

Finally, `r` cannot be another typical vertex of T. Two typical F0 vertices have

`|N_Y(t) cap N_Y(r)| = q p-o(p)>1`,

contradicting the singleton equation `(FY-F0)`.

Thus every forward certificate, apart from `o(p^2)` negligible special incidences, uses an **atypical escape vertex** `r in E\T`.

For fixed `(t,r)`, the graph-fixed set `N(t) cap N(r)` can equal `{y0}` for at most one `y0`. Hence, if

`|E\T|=(e+o(1))p`,

then the total number of forward-certified T--Y edges is at most

> **`(1-e)e p^2+o(p^2)`.**                              `(FY-FCAP)`

Here the normalization `|T|=(1-e+o(1))p` is the exact low-k-ray normalization `c=p`; the qualitative `e=o(1)` contradiction below needs only `|T|=Theta(p)` and `|E\T|=o(p)`.

## 5. Reverse certificates are also exceptional

Now suppose `ty0` takes the reverse orientation. Then

`r in N(t)\N[y0]`,

`N(y0) cap N(r)={t}`.                                   `(FY-R0)`

Because every Y-vertex is adjacent to every X-vertex, `(FY-R0)` forces

> **`N_X(r)=empty`.**                                    `(FY-X0)`

Otherwise any X-neighbour of r is a second common neighbour of `y0` and r.

This excludes every typical F0 vertex, since a typical F0 vertex has `p-o(p)` H-neighbours. It also excludes every private endpoint `q_i`, which has its matched X-neighbour `h_i`; each selected witness `z_h`, which has its K-head; and the residual hub `q_j`, which lies in the preserved beta fan and has K-neighbours. X- and Y-witnesses were already impossible, and the root is adjacent to y0.

Therefore reverse witnesses also lie in an atypical X-anticomplete part of the escape reservoir, of size at most `(e+o(1))p` in the exact-ray normalization.

For a fixed `(y0,r)`, the singleton set `N(y0) cap N(r)` can equal `{t}` for at most one t. Hence the total number of reverse-certified T--Y edges is at most

> **`q e p^2+o(p^2)`.**                                 `(FY-RCAP)`

## 6. Certificate-capacity obstruction

Typical F0 vertices are Y-complete up to `o(p)` holes, so the number of T--Y edges is

> `q(1-e)p^2+o(p^2)`.                                   `(FY-DEMAND)`

Every such edge must take one of the two raw criticality orientations. Combining `(FY-FCAP)`, `(FY-RCAP)` and `(FY-DEMAND)` gives the necessary asymptotic capacity inequality

> **`q(1-e) <= e(1-e+q)`.**                             `(FY-CAP)`

Equivalently,

`e^2-(1+2q)e+q <=0`.

Thus any high-Y realization must have

> **`e >= e_*(q):=[1+2q-sqrt(1+4q^2)]/2 >0`.**          `(FY-ESTAR)`

For the exact low-k ray, `q=1`, so

> **`e >= (3-sqrt(5))/2 = 0.381966...`.**               `(FY-GOLD)`

This is a physical certificate-capacity statement, not a score relaxation.

## 7. Certificate witnesses themselves carry a located quadratic hole price

The preceding capacity theorem can be strengthened without identifying the atypical witness class.

If `r` is a forward witness for `ty0`, then `(FY-F0)` implies

`N_Y(t) cap N_Y(r)={y0}`.

For a typical t, `|Y\N_Y(t)|=o(p)`. Hence

> `d_Y(r)<=1+|Y\N_Y(t)|=o(p)`,

so every distinct forward-witness vertex is **Y-sparse** and contributes

> `y-o(p)=q p-o(p)`                                      `(FY-FHOLE)`

located Y--B nonedges.

If `r` is a reverse witness, `(FY-X0)` says it is X-anticomplete. Since `x=p+1` in the residual-one `k=2` branch, every distinct reverse-witness vertex contributes

> `p+1`                                                  `(FY-RHOLE)`

located X--B nonedges.

Let `f p+o(p)` and `r p+o(p)` be the numbers of distinct forward- and reverse-witness vertices used by the typical T--Y edge set, and write `tau=|T|/p`. The same fixed-pair injection gives the certificate-capacity constraint

> `tau*f + q*r >= tau*q`.                                `(FY-FR-CAP)`

The located witness-hole bill is

> `(Z_Y+Z_X)/p^2 >= q*f+r-o(1)`.                         `(FY-FR-HOLE)`

Minimizing `q f+r` subject to `(FY-FR-CAP)` gives

> **`(Z_Y+Z_X)/p^2 >= min{q^2,tau}-o(1)`.**             `(FY-LOC)`

Indeed a forward witness buys `tau` units of certificate capacity at cost q, while a reverse witness buys q units at cost one.

At the pure-F0 endpoint `tau->1`; since `0<q<=1`, this becomes

> **`(Z_Y+Z_X)/p^2 >= q^2-o(1)`.**                      `(FY-LOC-PURE)`

This directly contradicts the half-barrier equality requirement `Z_X+Z_Y=o(p^2)` whenever q is bounded below. It is stronger than merely observing that the atypical witness density is positive.

On the exact low-k stress ray q tends to one, so F0--Y criticality alone forces an additional located-hole coefficient asymptotic to one on top of the independent-reservoir half coefficient. Thus the physical defect is driven to the leading-order ceiling scale `3/2 p^2`; the remaining question there is now lower-order rigidity, not another missing quadratic term.

## 8. Consequence for the coefficient-1/2 endpoint

The pure-F0 half-barrier endpoint has `e=o(1)` and `Z_X+Z_Y=o(p^2)`. Both `(FY-ESTAR)` and the stronger `(FY-LOC-PURE)` rule this out whenever `y/p` is bounded below by a positive constant.

Therefore:

> **There is no coefficient-`1/2` pure-F0 sequence with `liminf y/p>0`.** `(FY-NOHIGHY)`

In particular, the exact unbounded low-k stress ray

`c=p`, `y=p-1`, `lambda=p`, `u=x=p+1`, `k=2`

cannot approach the compressed half-barrier endpoint. Its only remaining coefficient-`1/2` geometry is eliminated by raw F0--Y edge criticality.

More generally, any hypothetical sequence that still approaches coefficient `1/2` after the compressed additive theorem must leave the high-Y regime:

> **near-half survival forces `y/p ->0` unless a positive-density, quadratically priced certificate reservoir is paid for.** `(FY-REDIR)`

## 9. Trust boundary and next attack

This note does **not** yet claim a finite-order closure. The new high-Y obstruction is asymptotic and conditional on the compressed pure-F0 normal form; the positive located witness-hole price must still be combined with the exact lower-order score/rooted ledger if one wants an explicit finite threshold.

The next highest-value work is therefore:

1. hostile-replay the forward/reverse witness exclusions in Sections 4--5 against the exact rooted vertex partition;
2. combine `(FY-LOC-PURE)` with the exact ray score ceiling `C0=floor((3p^2+10p-4)/2)` and retain lower-order terms rather than only leading coefficients;
3. if the exact ray survives at leading equality, classify the witness sets that make `(FY-FR-CAP)` and `(FY-FR-HOLE)` simultaneously sharp;
4. treat the redirected `y=o(p)` regime through `g0=p-y` and the existing large-gap / rooted residual ledger rather than by further high-Y F0 algebra.

Global audit caveat unchanged: the rigid complete Hall-cut reachability problem remains upstream and unresolved; `X_3` remains the mandatory negative control.