# Rigid one-code source visibility: sterile crossing witnesses and full-support purification

Date: 2026-09-19

Status: **internal structural theorem package** for the eventual / sufficiently-large D2C second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

This note continues the corrected `z=1` work after `ONE_CODE_Z1_CLOSURE_REFINEMENT.md`. It does not use the invalidated full-support traffic argument from the first `z=1` draft. Instead it returns to the graph-level same-code criticality lemma and exploits a simple visibility fact that was not previously fed back into the one-code branch.

The published order-12, size-32 graph `X_3` remains a mandatory hostile control. The present mechanism requires unmatched crossing witnesses and is inactive on its canonical root (`u=0`).

## 1. Audit reconciliation

The 19 September adversarial audit elevated the graph-to-selected premises and actual-graph regression before downstream one-code theory. Those obligations were independently repaired and regression-tested before this line was resumed. The previous session then removed the scalar `B<2y` stop line by adding the finite edge cap on `U_{bar d}`.

A hostile reread of the equality geometry exposed a stronger graph-level fact: a U-witness already used on the complete rigid cut sees one vertex of `X`, while every source in `Y` sees all of `X`. Such a used witness therefore cannot participate in any same-code unique-common-neighbour certificate whose head is outside `X`. This makes the used crossing-witness layer **sterile** for the auxiliary same-code channels.

This is upstream of the finite edge cap and supersedes it whenever the crossing support is full.

---

## 2. Setup and preserved graph-level inputs

Use the rigid one-code notation:

- `X` and `Y` partition the A-layer across a rigid Hall cut;
- `X--Y` is complete;
- every vertex of `Y` has Boolean code `d`;
- `A_{bar d}=emptyset`;
- `U_-=U_{bar d}`, `U_+=U_d`;
- `g=g_P`, `k=x-g>0`.

Let `W subseteq U_-` be the union of U-witnesses actually used by crossing certificates from `Y` to `X`.

Two previously verified facts are load-bearing.

1. **Rigid crossing witness.** If `w in W`, then

   > `d_X(w)=1`.                                          `(V1)`

   Indeed, the source `s in Y` is adjacent to every vertex of `X`, while `N(s) cap N(w)` is the singleton crossing head.

2. **Same-code localization.** For every same-code edge in the coded layer `A union U`, there is an endpoint-source / complementary-witness certificate. In the present pure pair:

   - an edge inside `Y` has a source in `Y` and witness in `U_-`;
   - an edge `Y--U_+` has source in `Y` and witness in `U_-`;
   - an edge inside `U_-` has source in `U_-` and witness in `Y`.

These are graph-level existence statements; they do not depend on which certificate was selected for a downstream traffic count.

---

## 3. Structural unit I: used crossing witnesses are sterile for the auxiliary same-code channels

### Theorem 3.1 — source-visibility sterility

Let `w in W`. Then:

1. `w` cannot witness a same-code edge whose source lies in `Y` and whose head lies in `Y union U_+`;
2. `w` cannot be the source of a same-code edge inside `U_-` witnessed by a vertex of `Y`.

### Proof

By `(V1)`, let `x_w` be the unique neighbour of `w` in `X`.

Every `s in Y` is adjacent to every vertex of `X`, hence in particular to `x_w`.

For item 1, a putative same-code certificate with source `s in Y`, witness `w`, and head `h in Y union U_+` would have

`N(s) cap N(w)={h}`.

But `x_w` is also a common neighbour of `s,w`, and `x_w` lies in `X`, disjoint from `Y union U_+`. Contradiction.

For item 2, a putative certificate with source `w`, witness `s in Y`, and head `h in U_-` again has `x_w in N(w) cap N(s)`, with `x_w != h`. Contradiction. `square`

The argument is deliberately elementary: complete visibility of `X` by `Y` makes any already-used U-witness incompatible with a second singleton-common-neighbour role whose head is not its X-neighbour.

---

## 4. Structural unit II: general buffer localization

Put

`B_U=U_-\W`, `r=|B_U|`.

Call these vertices **buffers** relative to the crossing support.

### Corollary 4.1 — auxiliary traffic lives on buffers

Every same-code certificate of the following types uses a buffer vertex:

- an edge inside `Y`;
- an edge `Y--U_+`;
- an edge inside `U_-`.

More precisely:

1. every witness for an edge inside `Y` or `Y--U_+` lies in `B_U`;
2. every edge of `G[U_-]` is oriented, for its same-code certificate, from a source in `B_U`;
3. therefore `W` is independent and `B_U` is a vertex cover of `G[U_-]`;
4. any buffer which is actually used in one of these auxiliary certificates has `d_X=0`.

### Proof

Items 1--3 are immediate from Theorem 3.1 and same-code localization.

For item 4, let an active buffer `b` appear either as witness to a Y-source or as source witnessed by `Y`. If `b` had an X-neighbour `x_b`, then the same visibility argument as in Theorem 3.1 would place `x_b` in the relevant source/witness common neighbourhood in addition to the prescribed head. `square`

### Corollary 4.2 — general buffer edge and physical-pair capacities

With `s=|W|` and `r=|B_U|`,

> `e(G[U_-]) <= rs+binom(r,2)`.                           `(BUF-E)`

Moreover, choose the graph-level complementary-witness certificate supplied by same-code localization for **every** edge inside `Y`, every edge `Y--U_+`, and every edge inside `U_-`. These certificates inject across all three families into physical pairs in

`Y x B_U`.

Therefore the full graph edge counts, not merely a selected A/U subchannel, satisfy

> `e(Y)+e(Y,U_+)+e(G[U_-]) <= yr`.                         `(BUF-P)`

This is a structural refinement of the coarse reservoir `e_++e_-<=y(u_--k)`: the true auxiliary reservoir is controlled by the number of **unused crossing vertices**, not merely by excess U-population. It also bypasses the selected-channel ambiguity for internal `Y` edges, because `(BUF-P)` chooses an independently guaranteed same-code certificate for every such graph edge.

For `z=1`, `r` is either one (common-buffer support) or zero (full support), exactly recovering the support dichotomy from a single graph-level principle.

---

## 5. Structural unit III: full support is completely auxiliary-free

Now specialize to the corrected `z=1` full-support branch:

`u_-=k+1`

and every vertex of `U_-` lies in `W`. Hence `B_U=emptyset`.

### Theorem 5.1 — full-support purification

Every full-support `z=1` survivor satisfies

> `e(Y)=0`,                                                `(FS-Y)`
>
> `e(Y,U_+)=0`,                                           `(FS-YU)`
>
> `e(G[U_-])=0`.                                          `(FS-U)`

In particular the full-support auxiliary-hole variable of the corrected v2 bookkeeping vanishes:

> `A=0`,                                                  `(FS-A)`
>
> `j=rho`.                                                `(FS-J)`

### Proof

With no buffers, Corollary 4.1 leaves no possible complementary witness for an internal `Y` edge or `Y--U_+` edge and no possible source for an internal `U_-` edge. Same-code localization is an existence theorem, so the edges themselves cannot exist. The displayed bookkeeping consequences follow. `square`

This is stronger than the finite edge cap from the immediately preceding package. That cap remains true but is no longer load-bearing in full support.

It also clarifies the earlier v1/v2 issue. The first v1 proof incorrectly argued that all internal `Y` traffic *selected* the A/U channel. That selection statement remains invalid. Nevertheless, full support actually has **no internal `Y` edge at all**, by the independent same-code source-visibility argument above.

---

## 6. Structural unit IV: exact one-parameter full-support normal form

Let

`rho`

be the number of crossing holes, as in the corrected v2 theorem, and put

> `h:=y-rho`.                                             `(H)`

Thus `h` is the number of outside sources using all `k+1` U-witnesses rather than only `k`.

Recall

`B=(k+1)(p+k-1)`,

`Z0=(k+1)(a-1)`,

`D0=Z0-u(p-lambda)`.

Since `A=e_-=0` and `j=rho`, the corrected full-support equations collapse to

> `E_- >= B-y+h`,                                         `(H-E)`
>
> `Z >= Z0-y+h`.                                          `(H-Z)`

Because `Y` and `U_+` are anticomplete, and each source has `k+h_s` crossing U-nonneighbours with total crossing incidence `yk+h`, the exact degree identity on `Y` also gives

> `L_Y >= y(p-g+u_+)+h`.                                  `(H-L)`

### Proof of `(H-L)`

Since `e(Y)=0`, the exact one-code degree identity is

`L_Y=y(y-T0)+Z_Y`.

Every `Y--U_+` pair is a nonedge, contributing `yu_+`. Crossing U-witness incidences contribute `yk+h` further Y--U nonedges. Therefore

`L_Y>=y(y-T0)+yu_++yk+h`.

Using `y-T0+k=p-g` gives `(H-L)`. `square`

Thus one scalar `h` simultaneously costs U-slack, A--U defect, and Y-slack.

### Corollary 6.1 — full-support score floor

Every full-support `z=1` survivor satisfies

> `S=L_A+E_U`
> ` >= max(phi(g), y(p-g+u_+)+h)`
> `    +[B-y+h]_+`.                                       `(FS-SCORE)`

The safe parameter-only version is obtained at `h=0`, `u_+=0`:

> `S >= max(phi(g),y(p-g))+[B-y]_+`.                      `(FS-SCORE0)`

---

## 7. Structural unit V: exact residual elimination is now one line

From `(H-Z)` and

`Z=u(p-lambda)+2q+E_U`,

put

`Dbase=D0-y`,

`Ebase=[B-y]_+`.

For fixed `h>=0`,

`E_U>=[B-y+h]_+`,

`2q+E_U>=Dbase+h`.

Both requirements are monotone in `h`, so the minimum occurs at `h=0`.

### Theorem 7.1 — purified full-support residual floor

> `q+E_U`
> ` >= Ebase+ceil([Dbase-Ebase]_+/2)`.                    `(FS-QE)`

Equivalently:

- if `B<=y`,

  > `q+E_U>=ceil([D0-y]_+/2)`;

- if `B>y`,

  > `q+E_U>=B-y+ceil([D0-B]_+/2)`.                        `(FS-QE+)`

Hence

> `f >= (p-lambda)(p+u)`
> `     +Ebase+ceil([Dbase-Ebase]_+/2)-delta`.            `(FS-F)`

This supersedes the cap-aware three-case scalar formula in full support. The preceding formula remains valid but weaker.

---

## 8. Structural unit VI: exact crossing-channel counts

The purified graph has no same-code auxiliary edge traffic. Consequently, with `h=y-rho`, the crossing layer itself has exact channel counts:

> `C_P=yk+h`,                                             `(FS-C)`
>
> `P_P=yg-h`,                                             `(FS-P)`
>
> `t_P=xy`.                                               `(FS-T)`

Indeed, `h` sources use `k+1` U-witnesses and the other `y-h` use `k`; the remaining crossing certificates are matched, and there are no internal Y-edges.

The exact pair capacity therefore becomes the clean necessary condition

> `2xy <= R_code(S_P)[g+2S_P/L]`.                         `(FS-PAIR)`

Moreover `(H-L)` shows that the degree bill already supplies

`L_Y>=y(p-g+u_+)+h`.

Adding `2xy` to this lower bound recovers `(ONE-P)` with an additional margin `yu_++h`. Thus, on the purified full-support branch, the most transparent pair-local statement is the exact crossing demand `(FS-PAIR)` plus `(H-L)`; the older `(ONE-P)` is no longer the sharpest description of the geometry.

---

## 9. Structural unit VII: minimal-slack full support has exactly two omission types

The equality geometry `h=0` deserves direct classification.

Then every source in `Y` uses exactly `k` of the `k+1` vertices of `U_-`, together with all `g` relevant matched gamma feet. For `s in Y`, let

`o(s) in U_-`

be the unique U-vertex omitted by that source.

Every used crossing witness has a fixed unique X-neighbour. Let

`Gamma_d`

be the `g` matched gamma-`d` feet. Since every source uses all of them, their X-heads are fixed and pairwise distinct. Let `X_U` be the remaining `k` heads in `X`.

Each `w in U_-` has a fixed head

`eta(w) in X_U`.

For every source `s`, the restriction

> `eta : U_-\{o(s)} -> X_U`                               `(OM1)`

is a bijection, because those `k` U-witnesses, together with the `g` matched feet, must certify the `x=g+k` distinct crossing heads.

### Theorem 9.1 — omission-pair classification

Let

`O={o(s):s in Y}`.

Then either:

1. `|O|=1`: all sources omit the same U-vertex, so the crossing support has size `k` and this is precisely the common-buffer model; or
2. `|O|=2`: the support is full, the two vertices in `O` have the same X-head under `eta`, and every other vertex of `U_-` has a distinct X-head different from that shared head.

In particular, a minimal-slack full-support `z=1` model has **exactly two omission types**.

### Proof

For any `o in O`, `(OM1)` says that deleting `o` makes `eta` a bijection from a `(k)`-set to the `k` heads.

If `o_1 != o_2` both lie in `O`, any collision of `eta` must involve `o_1` (otherwise it survives after deleting `o_1`) and must also involve `o_2`. Since `k+1` vertices map to only `k` heads, there is a collision; therefore it is exactly the pair `{o_1,o_2}`, with

`eta(o_1)=eta(o_2)`.

A third possible omission `o_3` would leave the collision `{o_1,o_2}` present after deleting `o_3`, contradicting `(OM1)`. Hence `|O|<=2`.

If `|O|=1`, that single omitted vertex is never used, giving the common-buffer support. If the support is full, `|O|` cannot be one, so it is exactly two. The injectivity statements for all other vertices follow from either bijective restriction. `square`

This is the first genuinely explicit combinatorial classification of the minimal full-support witness pattern: it is not an arbitrary family of `k`-subsets of a `(k+1)`-set, but a two-omission design tied to a unique duplicated X-head.

---

## 10. Independent audit and bounded diagnostic

The companion checker performs two independent finite audits.

1. It brute-forces the purified residual relaxation for
   `0<=B<70`, `1<=y<=14`, `-10<=D0<80` and compares with `(FS-QE)`.

   Recorded: **88,200** instances, **zero mismatches**.

2. It enumerates all maps from a `(k+1)`-set to a `k`-set for `1<=k<=5` and checks the omission-map theorem whenever at least two deletions yield bijections.

   Recorded: **2,083** qualifying maps, **zero counterexamples**.

A coarse parameter diagnostic on the same `3<=p<=18`, `1<=u<=18` box gives:

- older shared-floor z=1 possibilities: `86,820`;
- union after the preceding finite-edge-cap refinement: `77,339`;
- full-support possibilities under the new source-visibility score floor: `64,275`;
- union with the unchanged coarse common-buffer gate: `76,584`.

Thus source visibility removes a further **755** abstract support-union states relative to the preceding `77,339` cap-only union, and the total safe rejection relative to `86,820` rises to **10,236** at this stage. These are abstract parameter states, not D2C graph counts.

(The earlier downstream `CHAN-Z1` gate can be applied on top; the structural result here is the graph-level purification, not the scan count.)

---

## 11. Consequence for the frontier

The `z=1` geometry is now substantially more compact.

- **Common-buffer support:** auxiliary same-code traffic can only use the unique unused buffer; active use forces that buffer to have no X-neighbour and pays the loaded-buffer residual surcharge already preserved.
- **Full support:** there is no auxiliary same-code traffic at all. A single scalar `h=y-rho` prices U-slack, defect and Y-slack simultaneously; the exact residual minimum occurs at `h=0`.
- **Minimal full support (`h=0`):** every source omits one U-witness, but full support forces exactly two omission types and a unique duplicated U-witness head in `X`.

The next highest-value attack is therefore the two-omission head-collision model itself, together with the unloaded common-buffer model. In both cases use exact pair capacity and the rooted residual/triangle ledger before proceeding to `z=2`.

For later `z>=2` work, Corollary 4.1 should be treated as the organizing principle: **used crossing witnesses are sterile; all auxiliary same-code traffic is forced onto unused buffers.** This is a structural theorem, not a finite-scan heuristic.

## 12. Trust boundary

- The new sterility theorem uses only the graph-level same-code localization, complete rigid cut, and the already-verified singleton X-head property of used U-witnesses.
- It is independent of the selected-channel bookkeeping error that motivated the v2 repair.
- The full-support conclusions are graph-level nonexistence statements for the relevant same-code edges.
- The residual and omission-map consequences are exact deductions and have independent finite arithmetic/combinatorial replay.
- No actual-graph mismatch has been observed. No eventual theorem is claimed.
