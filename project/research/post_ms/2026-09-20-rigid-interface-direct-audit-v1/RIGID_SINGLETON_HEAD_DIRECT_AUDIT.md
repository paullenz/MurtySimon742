# Independent direct audit of the rigid Hall singleton-head implication

Date: 2026-09-20

Status: **independent hand audit / scope hardening**, not forward closure. This addresses the daily red-team requirement created by the absence of any positive actual-D2C rigid complete Hall-cut fixture with `x>=3` in the bounded graph regression.

The purpose is deliberately narrow: rederive, from the exact Hall-cut semantics plus raw diameter-2-critical edge criticality, the implication

`M_X=E_X=0, x>=3`

`=>`

complete A-cut + outside-source singleton-head witnesses + the `x<=p+u` / U-code concentration consequences,

without importing `RIGID_HALL_WITNESS_GEOMETRY.md` or the downstream one-code language.

The result does **not** solve the separate realizability question. It reduces the trust risk in the hand implication conditional on the exact Hall event.

## 1. Exact meaning of the rigid event

Let the rooted partition be `V={v} dotcup B dotcup A`, and let the tight antipode pairs in B induce Boolean codes on A and the unmatched B-set U. Let `X` be a nonempty proper family of whole unordered complementary A-code pairs. Write

`A_X` for its A-vertices, `x=|A_X|`, and `Y=A\A_X`.

From the exact Hall-cut decomposition,

`M_X=x(a-x)-e(A_X,Y)`

is an integer number of missing A-cut edges, while

`E_X`

is the integer number of crossing non-direct A-edges whose fixed selected criticality source lies in `A_X`.

Therefore `M_X=E_X=0` has the literal graph meaning:

1. **the A-cut is complete:** every `x0 in A_X` is adjacent to every `y in Y`;
2. **every crossing edge is selected with source in Y.**

No capacity inequality is used in this translation.

For completeness, the near-equality Hall theorem obtains this event safely: in

`2E_X+M_X+J_X+kappa_X < 1`,

`E_X,M_X` are nonnegative integers, so `2E_X+M_X<1` implies exactly `E_X=M_X=0`. No integrality is required of `J_X` or `kappa_X`.

## 2. Every crossing edge is non-direct

Take `y in Y`, `x0 in A_X`. The two endpoint codes lie in different unordered complementary-pair classes, because X is a union of whole complementary pairs and y lies outside it.

If their codes were complementary, they would belong to the same unordered pair, contradiction. Hence the two p-bit codes are **not** complementary. Therefore at some tight coordinate the two vertices choose the same matched endpoint, giving a common B-neighbour. Thus the crossing A-edge is non-direct.

So raw criticality of the selected source orientation has a genuine witness `w` with

`yw notin E`, `x0w in E`, and

> `N(y) cap N(w)={x0}`.                                  `(RI-1)`

This is just the diameter-2-critical singleton certificate for a triangular/non-direct edge.

## 3. Singleton head is forced physically

Because the cut is complete, the source y is adjacent to every vertex of `A_X`. From `(RI-1)`, if w were adjacent to any `x1 in A_X\{x0}`, then x1 would be a second common neighbour of y and w. Hence

> `N(w) cap A_X={x0}`.                                   `(RI-2)`

This is a physical neighbourhood statement, not a selected-incidence count.

For fixed source y, the witnesses for different heads are distinct. Indeed, if the same physical w certified both heads x0 and x1, then the graph-fixed set `N(y) cap N(w)` would have to equal both `{x0}` and `{x1}`.

Thus every `y in Y` requires **x distinct physical witnesses**, each having exactly one A_X-neighbour.

## 4. A cannot supply such a witness when x>=3

This point is worth spelling out because it removes a hidden witness-location concern.

Suppose a witness w lay in A.

- If `w in A_X`, completeness of the cut gives `yw in E`, contradicting the required source-witness nonedge.
- If `w in Y`, completeness of the cut gives `A_X subseteq N(w)`. Since `x>=3` (indeed x>=2 suffices), y and w have every A_X vertex as a common neighbour, contradicting singleton `(RI-1)`.

The root v cannot witness an A-edge because it is nonadjacent to A, hence in particular to the head x0.

Therefore every selected crossing witness lies in B. Splitting B into tight matched endpoints and unmatched vertices U, every witness is either

- a tight matched endpoint, or
- an unmatched vertex of U.

This recovers the witness-location statement directly, with no coded-layer theorem imported.

## 5. At most one singleton matched endpoint per tight fibre

Fix a tight fibre `{q_i,r_i}`. Every A-vertex chooses exactly one of its two endpoints, so on A_X

`d_{A_X}(q_i)+d_{A_X}(r_i)=x`.

When `x>=3`, the two degrees cannot both equal one. Therefore each tight fibre contributes at most one matched endpoint whose A_X-neighbourhood has size exactly one.

If `mu_X` denotes the total number of such endpoints, then

> `mu_X<=p`.                                              `(RI-3)`

For a fixed source y, Section 3 requires x distinct singleton-head witnesses, and at most `mu_X` of them can be matched endpoints. Hence at least

> `k_y:=(x-mu_X)_+`

are distinct U-witnesses. In particular

> `x<=mu_X+u<=p+u`.                                      `(RI-4)`

This is the rigid size obstruction, now rederived without the earlier theorem package.

## 6. Complementary U-code is forced directly

Let w in U be one of the witnesses for source y. For each tight fibre i, y and w cannot choose the same matched endpoint: such an endpoint would be a common neighbour of y and w distinct from the A-head x0 in `(RI-1)`.

Because each has a well-defined tight-fibre code, they must choose opposite endpoints in **every** tight fibre. Therefore

> `c(w)=bar(c(y))`.                                       `(RI-5)`

So the `k_y` U-witnesses required by one source y all lie in the single physical U-code class `U_bar(c(y))`, giving

> `|U_bar(c(y))| >= (x-mu_X)_+ >= (x-p)_+`.              `(RI-6)`

If `h_Y` distinct A-codes occur in Y, their complementary U-code classes are disjoint. Summing gives

> `h_Y (x-mu_X)_+ <= u`,                                 `(RI-7)`

and hence the weaker but code-free matched-count form

> `h_Y (x-p)_+ <= u`.                                    `(RI-8)`

## 7. Independent conclusion and remaining gap

The complete logical chain

`M_X=E_X=0`

`=> complete A-cut + all selected crossing sources in Y`

`=> x distinct physical singleton-head witnesses per outside source`

`=> witnesses lie in matched B or U`

`=> at most p matched singleton witnesses`

`=> x<=p+u and complementary U-code concentration`

is therefore independently valid under the rooted tight-code definitions.

No downstream pair-capacity formula, same-code theorem, finite source-tuple theorem, or graph-regression observation is needed for this implication.

### Confidence effect

This materially reduces one part of the daily audit's rigid-interface risk: the **conditional singleton-head implication itself** now has an independent raw derivation.

What remains unresolved is different and must stay explicit:

> bounded actual-D2C regression still has **zero positive realized fixtures** with `x>=3`, `M_X=E_X=0`.

So reachability/nonrealizability of the rigid event remains open. The correct next interface attack is now sharper: investigate whether the conjunction itself can occur in an actual D2C graph, rather than re-auditing the elementary consequences once it occurs.