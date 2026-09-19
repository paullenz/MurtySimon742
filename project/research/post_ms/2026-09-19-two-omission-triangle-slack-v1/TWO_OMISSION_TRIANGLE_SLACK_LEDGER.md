# Two-omission full-support ledger: exact omitted-pair, outside-U and rooted-triangle corrections

Date: 2026-09-19

Status: **internal structural theorem package** for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

No all-order statement is asserted. The published 2024 order-12, size-32 D2C graph `X_3` remains a mandatory hostile control and is not touched by the present mechanism on its canonical root (`u=0`).

---

## 1. Audit reconciliation and scope

Before this line was advanced, the current `README.md`, `CURRENT_STATE.md`, recent commits and the 19 September daily adversarial audit/handoff were reread. The two upstream source-tuple premises singled out by that audit remain independently re-derived from raw rooted criticality at the exact raw/selected interface actually used downstream:

1. distinct physical-source identity for distinct target fibres at the relevant beta orientation; and
2. global selected `(source,coordinate)` uniqueness for one physical rooted B-edge/source-coordinate obligation.

The finite source-tuple capacity theorem therefore remains **conditional on those two named premises** in theorem wording; this note does not silently upgrade it to unconditional graph-level closure.

The independent actual-graph regression also remains in place through rooted partition, criticality slots, A-codes, Hall objects and pair-capacity quantities, with `X_3` as a hostile negative control and zero recorded graph/formula mismatches in the preserved corpus.

Accordingly this session follows, rather than departs from, the audit priority order: it stays in the authorized rigid one-code branch, starts from the graph-level source-visibility purification, uses the exact pair-local capacity together with `(ONE)` / `(CROWD)` only where justified, and feeds the surviving two-omission geometry directly into the rooted residual/triangle ledger. The closed mixed `{4,5}` ladder and the subordinate four-exception gate are not used.

---

## 2. Setup: the minimal full-support two-omission model

Use the notation of

`2026-09-19-one-code-source-visibility-v1/FULL_SUPPORT_SOURCE_VISIBILITY_PURIFICATION.md`.

Thus:

- `X,Y` partition the rooted A-layer across a rigid Hall cut;
- `X--Y` is complete;
- all vertices of `Y` have the same tight Boolean code `d`;
- `A_{bar d}=emptyset`;
- `U_-=U_{bar d}`;
- `g=g_P` is the relevant matched gamma-fibre count;
- `k=x-g>0`;
- the present branch is `z=1` full support with `u_-=|U_-|=k+1`;
- every vertex of `U_-` is used by the crossing support;
- source-visibility sterility has already proved

  `e(Y)=e(Y,U_d)=e(G[U_-])=0`.

We now specialize to the minimal-slack full-support case `h=0` from the preceding package. Every source `s in Y` uses exactly `k` of the `k+1` vertices of `U_-` and omits one vertex `o(s)`. The omission classification already proves there are exactly two omission vertices `o_1,o_2 in U_-`, that they share the same X-head `x_*`, and that all other `k-1` vertices of `U_-` have pairwise distinct X-heads different from `x_*`.

Write

`Y=Y_1 disjoint_union Y_2`,

where sources in `Y_i` omit `o_i`, and put

`alpha=|Y_1|`, `beta=|Y_2|`, `alpha,beta>=1`, `alpha+beta=y`.

For `w in U_-`, let `t_w` denote the number of Y-sources which use `w` as a crossing U-witness. Then

- every regular `w in U_-\{o_1,o_2}` has `t_w=y`;
- `t_{o_1}=beta`;
- `t_{o_2}=alpha`.

Hence

> `sum_{w in U_-} t_w = yk`.                              `(2.1)`

This exact multiplicity vector is the first useful replacement for the earlier scalar incidence count.

For the omitted pairs, define

`nu_i = |{s in Y_i : s o_i notin E(G)}|`,

`nu=nu_1+nu_2`.

Thus `nu` counts omitted source--witness pairs which are also graph nonedges. Used source--witness pairs are already nonedges by the singleton-common-neighbour crossing certificate.

Finally put

`U_o = U\U_-`, `u_o=|U_o|=u-k-1`.

This notation deliberately does **not** assume that all unmatched vertices outside `U_-` have code `d`: other unmatched code classes may exist.

Define the following exact correction terms:

- `H_Y =` number of nonedges in `Y x U_o`;
- `H_X =` number of nonedges in `X x U_o`;
- `H=H_X+H_Y`;
- `M =` number of nonedges in `U_- x U_o`, so

  `M=(k+1)u_o-e(U_-,U_o)`;

- `Q_rest = Q-e(U_-,U_o)`, where `Q=e(G[N(v)])` is the rooted triangle count.

All five quantities `nu,H_X,H_Y,M,Q_rest` are nonnegative integers.

Also retain

`B=(k+1)(p+k-1)`,

`Z0=(k+1)(a-1)`,

`Dbase=Z0-y-u(p-lambda)`.

---

## 3. Structural unit I: the exact two-omission A--U nonedge ledger

### Lemma 3.1

The contribution of `A x U_-` to the A--U nonedge count is exactly

> `Z(A,U_-)=Z0-y+nu`.                                    `(3.1)`

Consequently the full A--U nonedge count is

> `Z=Z0-y+nu+H`.                                         `(3.2)`

### Proof

Every `w in U_-` is used on the full crossing support and therefore has exactly one X-neighbour. Hence `X x U_-` contains

`(k+1)(x-1)`

nonedges.

Every source uses `k` U-witnesses, so the used Y--U_- pairs contribute exactly `yk` nonedges. The only remaining Y--U_- pairs are the y omitted pairs `(s,o(s))`; exactly `nu` of these are nonedges. Thus

`Z(Y,U_-)=yk+nu`.

Adding and using `a=x+y` gives

`(k+1)(x-1)+yk+nu=(k+1)(a-1)-y+nu=Z0-y+nu`.

The only A--U pairs not yet counted are `A x U_o`, whose nonedge count is `H`. `square`

### Corollary 3.2 — exact residual demand

Using the preserved rooted identity

`Z=u(p-lambda)+2q+E_U`,

we obtain the exact equation

> `2q+E_U = Dbase+nu+H`.                                  `(3.3)`

Thus the old lower bound `2q+E_U>=Dbase` has an explicit graph-level correction: omitted-pair nonedges and every A--outside-U nonedge enter one-for-one.

---

## 4. Structural unit II: exact Y-slack, including the omitted-pair surcharge

The exact one-code degree identity on the purified branch is

`L_Y=y(y-T0)+Z_Y`

because `e(Y)=0`.

The Y--U_- nonedge count is exactly `yk+nu`, while the Y--`U_o` nonedge count is exactly `H_Y`. Therefore

> `L_Y = y(y-T0+k)+nu+H_Y`.                               `(4.1)`

Using the preserved relation `y-T0+k=p-g`, this becomes

> `L_Y = y(p-g)+nu+H_Y`.                                  `(4.2)`

The preceding source-visibility package had the safe floor

`L_Y>=y(p-g+u_+)`

because `Y--U_d` is anticomplete. Equation `(4.2)` is the exact refinement: it retains all omitted-pair and all outside-U nonedges rather than only the forced `U_d` part.

In particular, every omitted pair which is a nonedge costs one unit in `L_Y` in addition to its unit in `Z`.

---

## 5. Structural unit III: exact individual and total U_- slack

For `w in U_-`, let `nu_w` be the number of omitted-source nonedges incident with w. Thus `nu_w=0` for regular w, `nu_{o_i}=nu_i`, and

`sum_w nu_w=nu`.

By source-visibility purification:

- `d_X(w)=1` for every `w in U_-`;
- `G[U_-]` is edgeless;
- exactly `t_w` Y-sources use w and are therefore nonadjacent to w;
- among the `y-t_w` omitted-source pairs at w, exactly `nu_w` are also nonedges.

Hence

`d_Y(w)=y-t_w-nu_w`.

Let

`m_w = u_o-d_{U_o}(w)`

be the number of missing edges from w into the rest of U. From the defining U-slack degree identity

`epsilon_w=p+u-1-d_{A union U}(w)`

we obtain, exactly,

> `epsilon_w = p-y+k-1+t_w+nu_w+m_w`.                    `(5.1)`

Summing `(5.1)` over the `k+1` vertices of `U_-`, using `(2.1)` and `sum m_w=M`, gives

### Theorem 5.1 — exact U_- slack ledger

> `E_- = B-y+nu+M`.                                       `(5.2)`

This is stronger than the earlier floor `E_->=B-y`: the entire gap is now identified by two physical graph defects, `nu` and `M`.

### Corollary 5.2 — the previous individual floor is recovered and sharpened

Put `s=p+k-1` and `c=s-y`. Since `m_w,nu_w>=0`, `(5.1)` gives

`epsilon_w>=c+t_w`.

Therefore

> `E_- >= (k-1)s+[2s-y]_+`.                               `(5.3)`

Indeed the regular vertices contribute `(k-1)s`, while the two omission vertices contribute at least

`[c+alpha]_+ + [c+beta]_+ >= [2c+y]_+=[2s-y]_+`.

When `y<=2s`, `(5.3)` equals `B-y`; when `y>2s`, it gives `(k-1)s`, which can be strictly stronger than the coarse truncation `[B-y]_+`.

Also

> `max(epsilon_{o_1},epsilon_{o_2}) >= [c+ceil(y/2)]_+`.   `(5.4)`

So an extreme imbalance of the two omission classes cannot hide all local slack.

---

## 6. Structural unit IV: rooted triangle--slack cancellation

The cross edges between `U_-` and `U_o` lie wholly inside the root neighbourhood `N(v)`, so they contribute to the rooted triangle count `Q=e(G[N(v)])`.

By definition

`Q = e(U_-,U_o)+Q_rest`,

and

`M=(k+1)u_o-e(U_-,U_o)`.

Adding `(5.2)` gives the exact cancellation

### Theorem 6.1 — triangle--slack bridge

> `Q+E_-`
> ` = B-y+nu+(k+1)u_o+Q_rest`.                            `(6.1)`

Hence

> `Q+E_U >= B-y+nu+(k+1)u_o`.                            `(6.2)`

Every edge moved into `U_- x U_o` raises `Q` by one and lowers `E_-` by one; the sum is invariant. Thus this whole degree of freedom disappears when the one-code geometry is fed into the rooted triangle ledger.

### Equality geometry

If `nu=0`, `M=0` and `Q_rest=0`, then simultaneously:

- each source is adjacent to its omitted U_- vertex and nonadjacent to all k used U_- witnesses;
- `G[U_-]` is edgeless;
- `U_-` is complete to `U_o`;
- no other root-neighbourhood edge contributes to Q beyond the complete `U_- x U_o` layer.

The first bullet makes ordinary triangles `s-x_*-o(s)` for the omitted **edges**. These are **not rooted-neighbourhood triangles** because `s,x_* in A` are root nonneighbours. This distinction is load-bearing: no such triangle is credited to `Q`.

This sentence records an adversarial self-correction made during the derivation. Treating the omitted-edge triangle as a contribution to Q would be false.

---

## 7. Structural unit V: exact cancellation of the omitted-pair variable outside E_-

Let

`E_o=E_U-E_-`.

Subtracting `(5.2)` from the exact residual equation `(3.3)` yields

> `2q+E_o`
> ` = Z0-B-u(p-lambda)+H-M`.                              `(7.1)`

The omitted-pair variable `nu` cancels **exactly**.

This does not make `nu` free: it still raises both `E_-` and `L_Y`, and therefore raises the global scorecard. What `(7.1)` says is more precise: once the forced U_- slack is peeled off, the residual competition between q and the outside-U slack depends on the outside A--U holes `H` versus the missing `U_- -- U_o` edges `M`, not on whether omitted source--U_- pairs themselves are edges.

The refined integer residual floor can be written compactly as follows. Put

`E0=B-y+nu+M`,

`D=Dbase+nu+H`.

Then every survivor satisfies

> `q+E_U >= E0+ceil([D-E0]_+/2)`.                         `(7.2)`

Equivalently,

> `q+E_U >= B-y+nu+M`
> ` +ceil([Dbase-B+y+H-M]_+/2)`,                          `(7.3)`

whenever the displayed exact `E_-` term is used. The threshold inside the positive part is independent of `nu`: each additional omitted-pair nonedge raises the lower bound linearly through `E_-` itself.

---

## 8. Structural unit VI: a corrected exact scorecard penalty

Because `L_A>=L_Y` and `E_U>=E_-`, equations `(4.2)` and `(5.2)` give

> `S=L_A+E_U`
> ` >= B-y+y(p-g)+2nu+H_Y+M`.                            `(8.1)`

Retaining the independent gamma-collision floor `L_A>=phi(g)` gives the sharper safe form

> `S >= B-y+nu+M`
> `     +max{phi(g), y(p-g)+nu+H_Y}`.                    `(8.2)`

Thus the minimal two-omission model has an explicit nonnegative correction vector:

`(nu,H_Y,M)`.

Every omitted-pair nonedge is especially expensive: it appears once in `E_-` and once in `L_Y`, before any outside-U or gamma cost is counted.

For an above-`M(n)` candidate, the preserved global upper scorecard `S<=C0` therefore gives a genuine stability gate. In particular, whenever the base term

`B-y+max{phi(g),y(p-g)}`

already uses all but `c` units of `C0`, one has immediately

`2nu+M <= c`

(and the exact max term can only strengthen this). Near scorecard equality the branch is therefore forced toward `nu=0` and `M=0`, i.e. omitted pairs are edges and `U_-` is complete to the rest of U.

---

## 9. Structural unit VII: reconcile exact pair capacity, `(ONE)` and `(CROWD)`

The audit specifically required the one-code branch to retain the exact pair-local capacity. In the purified one-code pair, the preserved result is

> `Ccap_P=R_code(S_P)[g+2S_P/L]`,                         `(9.1)`

because the two-sided matched-foot term `h_P` is exactly zero.

The exact crossing counts in the present `h=0` full-support model are

`C_P=yk`, `P_P=yg`, `t_P=xy`,

so the cleanest pair-capacity condition is already

> `2xy <= Ccap_P`
> `      =R_code(S_P)[g+2S_P/L]`.                        `(9.2)`

This is the purified full-support form of the pair bill; it is stronger and more transparent here than reintroducing a looser traffic decomposition.

For comparison, the preserved `(ONE-P)` inequality is

> `Ccap_P+L_Y >= y(p+2x-g)`.                              `(ONE)`

Substituting the exact Y-slack equation `(4.2)` gives

> `Ccap_P >= 2xy-yH_Y-nu-yu_o^*`,                        `(9.3)`

only if one chooses to split `H_Y` further into the code-d forced part and the remaining outside-U holes; without such a split, `(9.2)` should simply be kept as the stronger exact crossing statement. No artificial improvement is claimed from `(ONE)`.

The aligned crowding condition remains

> `S_P>=y(3y-D0)` whenever `3y>=D0`.                      `(CROWD)`

The correct synthesis is therefore structural rather than a new scalar relaxation:

1. `(9.2)` constrains the matched/code-radius pair capacity needed by the full `2xy` crossing demand;
2. `(CROWD)` constrains the pair-local score from below in the crowding regime;
3. `(8.2)` and `(7.2)` constrain the same graph through exact physical corrections `nu,H_Y,H_X,M` and the rooted residual ledger.

The next attack should keep these local quantities visible and solve the equality/near-equality intersection. Collapsing them prematurely to total `C0` is exactly the loss of geometry flagged by the previous audit.

**Caution on notation.** In the preserved pair-purification package `Ccap_P` denotes the exact pair capacity `(9.1)`. It is not the earlier weighted A/U-channel bound; the latter remains a separate channel inequality. This note follows the preserved definition and does not conflate the two.

---

## 10. Common-buffer comparison

The full-support two-omission model is now naturally paired with the unloaded common-buffer model.

- **one omission type / common buffer:** one vertex of `U_-` is unused by all crossing sources; source visibility localizes all auxiliary traffic to that buffer;
- **two omission types / full support:** every vertex of `U_-` is used by at least one source; source visibility kills all auxiliary same-code traffic, and the surviving geometry is governed by the correction vector above.

Thus the z=1 branch has been reduced to two genuinely explicit minimal geometries rather than an arbitrary witness family. The next useful theorem should compare their exact score/residual costs and then attack the equality cases by raw edge-criticality, rather than moving to z=2 yet.

---

## 11. Negative control and trust boundary

- `X_3` remains mandatory. Its canonical root has `u=0`, so the present unmatched-U mechanism is inactive. Nothing here excludes, explains away or contradicts the published 12/32 exception.
- The source-tuple capacity theorem remains conditional on the two named source/selection premises even though those premises have been independently re-derived at their intended interface.
- The graph-level actual-D2C regression remains an independent upstream control; no regression count is being treated as a proof of this rigid hand branch.
- Equations `(3.1)`, `(4.2)`, `(5.2)`, `(6.1)` and `(7.1)` are graph-count identities inside the already-purified minimal full-support model, not finite-scan observations.
- The individual floor `(5.3)` is a consequence of the exact local identity, not a replacement for it.
- No all-order second-extremal theorem is claimed.
- No finite parameter count is a graph count.

---

## 12. Precise next work

The highest-value continuation is now narrow.

1. **Raw-criticality attack on the equality vector.** Start with `nu=M=0` (and then the smallest positive corrections), where every omitted source--U_- pair is an edge and `U_-` is complete to `U_o`. Test whether edge-criticality of the omitted edge `s o(s)` can coexist with the duplicated X-head `x_*` without forcing an extra A--U hole, extra root-neighbourhood edge, or forbidden second common neighbour.
2. **Pair/residual equality intersection.** Keep `(9.2)`, `(CROWD)`, `(8.2)` and `(7.2)` simultaneously, retaining `S_P,H_X,H_Y,M,nu` rather than replacing them by one total score variable. Classify equality and first-near-equality parameter patterns.
3. **Compare with unloaded common buffer.** Put the two minimal z=1 normal forms into one score/residual table and determine which can survive as n grows.
4. **Only then move to z=2.** If z=1 is closed or reduced to a genuinely exceptional finite/equality family, generalize source-visibility buffer localization. Do not use the closed mixed `{4,5}` ladder or promote the subordinate four-exception gate unless it becomes genuinely load-bearing.

This is a direct continuation of the daily audit's priority proposal; no departure from that proposal is being recorded.
