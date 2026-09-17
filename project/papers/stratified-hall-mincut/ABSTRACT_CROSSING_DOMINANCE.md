# Stratified minimum-cut exactness under two-sided crossing dominance

17 September 2026. **Internal candidate theorem. External mathematical review and novelty assessment remain open.**

This note strips the q/c numerical compatibility relation out of the 14 September q-stratified minimum-cut proof. The proof uses only a two-sided neighbourhood-dominance property attached to capacity crossings inside equal-demand layers.

## 1. Model

Let `V` be a finite set. Each element is simultaneously a possible source and receiver. Partition `V` into layers `L_1,...,L_s`. Every source in layer `L_i` has the same nonnegative integer demand `d_i`. Each receiver `w` has a nonnegative integer capacity `P_w`.

Let `R` be a loopless directed compatibility relation on `V`.

For `S subseteq V`, define

`y_w(S)=#{u in S : u R w}`,

`H(S)=sum_w min(P_w,y_w(S))`,

`D(S)=sum_{u in S} d_{layer(u)}`,

`F(S)=H(S)-D(S)`.

For each layer and integer `k>=1`, put

`alpha_{i,k}=#{w in L_i : P_w>=k}`,

`beta_{i,k}(S)=#{w in L_i : y_w(S)>=k}`,

and define the layerwise rearranged capacity

`U(S)=sum_i sum_{k>=1} min(alpha_{i,k},beta_{i,k}(S))`.

The sums are finite.

## 2. Crossing-dominance axiom

Assume that whenever `x,y` lie in the same layer and

`P_x<P_y`,

the following hold:

1. **mutual layer compatibility:** `x R y` and `y R x`;
2. **incoming nesting away from the diagonal:** for every `z notin {x,y}`, `z R x => z R y`;
3. **outgoing nesting away from the diagonal:** for every `z notin {x,y}`, `x R z => y R z`.

Call this **two-sided crossing dominance** (`TCD`). It is deliberately stated only for strict capacity crossings; equal-capacity pairs need no ordering.

The condition resembles a two-sided Ferrers/threshold nesting with the diagonal removed, but no equivalence with a named graph class is claimed here.

## 3. Rearrangement gap and the membership orientation of a crossing

Layer-cake expansion gives

`H(S)=sum_i sum_k #{w in L_i : P_w>=k and y_w(S)>=k}`.

Therefore, for every `S`,

`H(S)<=U(S)`.

If strict inequality occurs in a layer, then for some level `m` there are `x,y` in that layer with

`P_x<m<=P_y`,

`y_x(S)>=m>y_y(S)`.

In particular `P_x<P_y`, so TCD applies.

Write the incoming counts from sources other than `x,y` as `a_x,a_y`. Incoming nesting gives `a_x<=a_y`. Mutual compatibility and looplessness give

`y_x(S)=a_x+1_{y in S}`,

`y_y(S)=a_y+1_{x in S}`.

Hence

`y_x(S)-y_y(S) <= 1_{y in S}-1_{x in S} <=1`.

Since the crossing has `y_x(S)>y_y(S)`, equality is forced throughout. Thus every positive rearrangement crossing has the orientation

`x notin S`, `y in S`,

and

`y_x(S)=y_y(S)+1`.

At the crossing level we may therefore take

`m=y_x(S)`, `y_y(S)=m-1<P_y`.

So the selected high-capacity endpoint `y` has positive receiver slack.

## 4. Submodularity and the maximal minimiser

For fixed `w`, the function `S -> y_w(S)` is modular and `t -> min(P_w,t)` is nondecreasing and concave on the nonnegative integers. Hence `S -> min(P_w,y_w(S))` is submodular. Therefore `H` and `F=H-D` are submodular, since `D` is modular.

Let

`gamma=min_S F(S)`.

The minimisers of a submodular set function form a lattice under union and intersection. Let `M+` be their union, the unique maximal minimiser.

If `S` is a minimiser and `x notin M+`, then `x` belongs to no minimiser. Integrality therefore gives

`F(S union {x})>=gamma+1`.                                      (4.1)

## 5. Neutral deletion lemma

Let `S` be a minimum witness contained in `M+`. Suppose a crossing pair `x,y` satisfies

`x notin M+`, `y in S`,

and lies in a common layer of demand `d`.

Define

`Z(S)={w:y_w(S)<P_w}`,

`T(S)={w:y_w(S)<=P_w}`.

Adding `x` increases capped receiver capacity by exactly one on each target in

`N^+(x) intersect Z(S)`.

By (4.1),

`|N^+(x) intersect Z(S)|-d >=1`,

so

`|N^+(x) intersect Z(S)|>=d+1`.                       (5.1)

Deleting `y` decreases capped receiver capacity by exactly one on each target in

`N^+(y) intersect T(S)`.

Since `S` is minimum,

`F(S\{y})-F(S)=d-|N^+(y) intersect T(S)|>=0`,

so

`|N^+(y) intersect T(S)|<=d`.                          (5.2)

The crossing orientation from Section 3 gives `x R y` and `y_y(S)<P_y`, hence

`y in N^+(x) intersect Z(S)`.

For every other `w` in that set, outgoing nesting gives `y R w`, while `y_w(S)<P_w` implies `w in T(S)`. Therefore

`(N^+(x) intersect Z(S))\{y} subseteq N^+(y) intersect T(S)`.

Combining with (5.1)-(5.2) gives equality throughout and

`F(S\{y})=F(S)=gamma`.

> **Neutral deletion lemma.** A crossing whose low endpoint lies outside `M+` can be removed by deleting its selected high endpoint without changing the minimum Hall margin.

## 6. Crossing removal

Start with `S_0=M+`. If `U(S_j)=H(S_j)`, stop. Otherwise choose a positive crossing and delete its selected high endpoint `y`.

At the moment `y` is deleted, Section 3 gives

`y_y(S_j)<P_y`.

Subsequent source deletions can only decrease `y_y`. Thus a previously deleted vertex can never later be the low-capacity/high-multiplicity endpoint of a positive crossing, because such an endpoint would require `y_y>=m>P_y`.

Every low endpoint seen later is therefore not a previously deleted member of `M+`. Since the current set is obtained from `M+` only by deletions, that low endpoint lies outside `M+`. The neutral deletion lemma applies at every step.

The process terminates after finitely many deletions at a minimum witness `S*` with

`U(S*)=H(S*)`.

## 7. Main theorem

> **Theorem (stratified rearrangement minimum-cut exactness under TCD).**
> For every finite layered directed Hall system satisfying TCD,
>
> `min_S [U(S)-D(S)] = min_S [H(S)-D(S)]`.
>
> In particular, a negative exact Hall margin exists if and only if a negative stratified-rearrangement margin exists.

Proof. Pointwise `U(S)>=H(S)` gives

`min(U-D)>=min(H-D)=gamma`.

Section 6 supplies a minimum exact witness `S*` with `U(S*)=H(S*)`, so

`U(S*)-D(S*)=H(S*)-D(S*)=gamma`.

QED.

## 8. Original q/c model as a corollary

The target-Hall system from which this theorem arose has, for each copy `w`, integers

`q_w`, `c_w>=q_w`, `P_w`,

compatibility

`u R w iff u!=w, q_u<=c_w+1, q_w<=c_u`,

and fixed-q cap monotonicity

`q_x=q_y, c_x<=c_y => P_x<=P_y`.

Take the layers to be equal-q classes and layer demand `d=q`.

If `P_x<P_y` in one q-layer, monotonicity forces `c_x<c_y`. Since `c_x,c_y>=q`, the pair is mutually compatible. For every third vertex `z`, the defining inequalities immediately give both

`z R x => z R y`,

and

`x R z => y R z`.

Thus TCD holds, and the 14 September q-stratified minimum-cut theorem is a corollary of the abstract theorem above.

This reduction removes the numerical q/c relation from the load-bearing proof. It is still useful in the D2C application because it supplies TCD automatically.

## 9. Regression evidence

`verify_crossing_dominance.py` tests the abstract theorem directly, without q/c variables.

Frozen exhaustive results:

- one layer, `n=4`, capacities `{0,1,2}`, layer demands `{0,1,2}`: 13,212 TCD capacity/digraph profiles and 39,636 demand instances; 2,760 instances have at least one pointwise rearrangement gap, comprising 7,080 pointwise-gap source sets; minimum-margin mismatches: **0**;
- two layers `{0,1}` and `{2,3}`, capacities `{0,1}`, layer demands independently in `{0,1,2}`: 19,120 TCD capacity/digraph profiles and 172,080 demand instances; 24,624 instances have a pointwise gap, comprising 46,188 pointwise-gap source sets; minimum-margin mismatches: **0**.

This is regression evidence only. The hand proof above is the theorem basis.

## 10. Trust and novelty boundary

The abstraction was derived and audited within the same research programme and has not received independent expert review. A preliminary literature search points to Ferrers/threshold digraph neighbourhood-inclusion theory as the closest structural language, but has not located the minimum-margin rearrangement theorem itself. No novelty claim is authorised until that comparison is completed.
