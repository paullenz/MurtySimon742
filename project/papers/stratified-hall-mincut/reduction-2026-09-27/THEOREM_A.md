# Hall/min-cut closure: a weaker adjacency hypothesis and antitone demands

**27 September 2026. Internal hand proof and finite computational audit; not external review, formal certification, or a novelty claim.**

Inspected repository: `paullenz/MurtySimon742`, base commit `e00989f1b47c78bfb8a133ef89ffc06cc73ba9fb`.
Original argument: `../ABSTRACT_CROSSING_DOMINANCE.md` (blob `03c3fd9fda0d507440b1fcfa8510a322291a201d`).
Working manuscript: `../MANUSCRIPT.md` (blob `d745e07ee8ee47b66d16d6aa538673b11ed1f1a4`).
The original proof was read before this derivation; this is **not a blinded independent proof**. The finite checker was newly written rather than copied from the repository checker.

## 1. Verdict on the inherited proof

No defect was found in the original TCD theorem at its stated hypotheses. In particular, the maximal-minimizer argument is essential as used, the strict/non-strict saturation inequalities in the addition/deletion formulas are correct, and the permanent-slack invariant justifies every subsequent deletion. The statement concerns equality of **minimum margins**, not equality of capacities for every source set or equality at every minimizer.

The proof also supports the following strictly broader statement. This is an internal strengthening of the repository theorem, not an assertion of literature novelty.

## 2. Model and strengthened statement

Let V be a finite set partitioned into layers L_i. Let R be a loopless directed relation, with each admissible source-to-receiver arc having unit capacity. Each vertex u has an integer demand d_u >= 0 and integer receiver capacity P_u >= 0. Source and receiver copies are distinguished when forming the flow network even though their labels both belong to V.

For S subseteq V define

\[
y_w(S)=|\{u\in S:uRw\}|,\qquad D(S)=\sum_{u\in S}d_u,
\]
\[
H(S)=\sum_{w\in V}\min(P_w,y_w(S)),\qquad F(S)=H(S)-D(S).
\]

For each layer and positive integer k put

\[
\alpha_{i,k}=|\{w\in L_i:P_w\geq k\}|,\qquad
\beta_{i,k}(S)=|\{w\in L_i:y_w(S)\geq k\}|,
\]
\[
U(S)=\sum_i\sum_{k\geq1}\min(\alpha_{i,k},\beta_{i,k}(S)).
\]

All sums are finite. Equivalently, sort the capacities and multiplicities separately in each layer in the same order and sum their pairwise minima. At each threshold, the two sorted superlevel sets are nested, so their intersection has the smaller cardinality. This proves the equivalence with the displayed formula without assuming a matching theorem.

For every same-layer pair x,y with P_x < P_y assume:

1. **Pair-excluding incoming nesting:** zRx implies zRy for every z outside {x,y}.
2. **Pair-excluding outgoing nesting:** xRz implies yRz for every z outside {x,y}.
3. **No downward-only arc:** yRx implies xRy. Both arcs may be absent; the upward arc alone is allowed.
4. **Antitone demand:** d_x >= d_y.

There is no pairwise requirement at equal capacities, and no capacity-order requirement between different layers. In particular, demands at equal capacities need not be equal. Antitone here means nonincreasing demand when capacity strictly increases within a layer.

> **Theorem A.** Under these hypotheses,
> \[
> \min_{S\subseteq V}(U(S)-D(S))=\min_{S\subseteq V}(H(S)-D(S)).
> \]
> Moreover, the maximal minimizer of F can be reduced to a minimizer S* with U(S*)=H(S*) by at most |V| deletions. Any choice of a currently positive crossing is permitted.

Original TCD assumes both arcs between every strict-capacity pair and equal demand throughout each layer. It implies all four hypotheses. Thus Theorem A includes the original result.

## 3. Rearrangement gaps produce oriented crossings

For a layer i and threshold k, write A={w in L_i:P_w>=k} and B={w in L_i:y_w(S)>=k}. The contribution to H is |A intersect B|, whereas that to U is min(|A|,|B|). Thus H(S)<=U(S).

If the inequality is strict, some threshold has both B minus A and A minus B nonempty. Choose x in B minus A and y in A minus B. Then

\[
P_x<k\leq P_y,\qquad y_x(S)\geq k>y_y(S). \tag{3.1}
\]

Let a_x,a_y count incoming arcs from selected vertices other than x,y. Incoming nesting gives a_x<=a_y. Set b=1_{yRx} and c=1_{xRy}. Looplessness gives exactly

\[
y_x(S)-y_y(S)=a_x-a_y+1_{y\in S}b-1_{x\in S}c.
\]

The left side is a positive integer. Therefore b=1, y belongs to S, and a_x=a_y. Hypothesis 3 gives c=1. Positivity then forces x notin S and

\[
y_x(S)=y_y(S)+1. \tag{3.2}
\]

Since k is integral, (3.1)-(3.2) give k=y_x(S) and y_y(S)=k-1<P_y. Thus a positive crossing automatically supplies both arcs and positive receiver slack at its selected high-capacity endpoint. This is why assuming both arcs in advance was stronger than necessary.

Conversely, the existence of a pair satisfying (3.1) makes both threshold differences nonempty, so it really certifies a positive gap. A checker can locate a crossing without scanning thresholds by testing

\[
\max(P_x,y_y(S))<\min(P_y,y_x(S)).
\]

## 4. The maximal minimum witness

For S subseteq T and u notin T, the marginal contribution of adding u to a fixed receiver is zero if u does not reach it; otherwise it is one precisely while that receiver is below its integer capacity. This contribution cannot increase as S grows to T. Consequently H is submodular. Subtracting modular D preserves submodularity.

Put gamma=min F. If A,B are minimizers, submodularity yields

\[
2\gamma=F(A)+F(B)\geq F(A\cup B)+F(A\cap B)\geq2\gamma.
\]

Both union and intersection are minimizers. Finiteness implies that the union M+ of all minimizers is itself a minimizer, and is the unique inclusion-wise maximal one.

If x notin M+ and S is a minimizer, S union {x} cannot be a minimizer. Because F is integer valued,

\[
F(S\cup\{x\})-F(S)\geq1. \tag{4.1}
\]

This is the step where integrality of both demands and capped-capacity increments matters. Mere strict positivity is insufficient for this proof; a fractional-demand counterexample is given below.

## 5. Generalized neutral deletion

Suppose S is a minimizer and (x,y) is a positive crossing with x notin M+. Define

\[
Z(S)=\{w:y_w(S)<P_w\},\qquad T(S)=\{w:y_w(S)\leq P_w\},
\]
\[
a=|N^+(x)\cap Z(S)|,\qquad b=|N^+(y)\cap T(S)|.
\]

Adding x has margin change a-d_x. By (4.1), a>=d_x+1. Deleting y has margin change d_y-b; minimality of S implies b<=d_y.

Section 3 shows that y is in N+(x) intersect Z(S). Every other w in this set is distinct from x,y (x is excluded by looplessness), so outgoing nesting gives yRw. Also w in Z(S) implies w in T(S). Hence

\[
(N^+(x)\cap Z(S))\setminus\{y\}\subseteq N^+(y)\cap T(S).
\]

Therefore

\[
d_y\ \geq\ b\ \geq\ a-1\ \geq\ d_x\ \geq\ d_y. \tag{5.1}
\]

Every inequality is equality. In particular d_x=d_y, b=d_y, and

\[
F(S\setminus\{y\})=F(S)=\gamma.
\]

Thus the deletion is neutral. A further useful conclusion is that a removable crossing at these witnesses can occur only between equal-demand vertices, even though demands elsewhere in its layer may differ.

The deletion loss uses <= P_w, not < P_w: a receiver exactly at capacity loses one unit when a selected incident source is removed. At P_w=0, no incident selected source can have y_w(S)<=0, so zero capacities are handled correctly.

## 6. Why iteration is valid

Start with S_0=M+. At any step with a positive gap, Section 3 gives a crossing whose low endpoint x is outside the current S_j and whose high endpoint y belongs to it.

Any vertex previously deleted had its receiver count strictly below its capacity at deletion. Subsequent source deletions can only decrease that count. It can never become a low endpoint of a positive crossing, since that would require y_x(S_j)>=k>P_x.

The only vertices outside S_j that were originally in M+ are previously deleted ones. Therefore the current low endpoint is outside M+. Section 5 applies, so deletion preserves gamma. This maintains the induction hypothesis at every step, for every crossing choice.

At most |M+| deletions are possible. If all sources are deleted, H=U=0 automatically, so the process must stop at a minimizer S* with H(S*)=U(S*). Since U>=H pointwise,

\[
\min(U-D)\geq\gamma=H(S^*)-D(S^*)=U(S^*)-D(S^*)\geq\min(U-D).
\]

This proves Theorem A. Empty V, empty S, zero demands, zero capacities, and capacity ties introduce no exception. QED.

## 7. A constructive max-flow implementation

Create source s, sink t, source copies u_L and receiver copies w_R. Add arcs s->u_L with capacity d_u, u_L->w_R with capacity 1 exactly when uRw, and w_R->t with capacity P_w.

If a cut has source-label set S on the s side, an individual receiver w may be put on either side. Its cheapest contribution is min(P_w,y_w(S)). The remaining cut contribution is D(V minus S). Minimizing over receiver placements therefore gives

\[
\text{minimum cut}=D(V)+\min_S F(S).
\]

An integral maximum flow gives the corresponding capacitated matching; all demand is routable exactly when the minimum margin is zero. The empty source set ensures the minimum margin is never positive.

There is a small but important algorithmic distinction. Ordinary residual reachability **from s** gives the smallest minimum-cut source side. To obtain M+, after a maximum flow instead take all network vertices that **cannot reach t** in the residual network. This is the largest minimum-cut source side: it has no positive residual arc leaving it, and every minimum-cut source side is contained in it. Projecting its source copies gives exactly M+, because every minimizing S extends to a minimum cut.

Then apply the proved deletions. With an adjacency matrix, finding a crossing by testing all pairs costs O(n^2) per deletion; updating counts costs O(n). At most n deletions gives O(n^3) work after the max-flow computation. This is a constructive consequence, not a new fast max-flow algorithm. It avoids trying to minimize U directly or assuming U is submodular.

`check_closure.py` implements a separate Edmonds-Karp flow oracle and checks its M+ against the union of **all** minimizers obtained by exhaustive enumeration. The finite oracle is not a production large-instance solver.

## 8. Exact failure cases outside the hypotheses

All listed minima are verified by full source-subset tables in `BOUNDARIES.json`. Vertex order is the array order; an unlisted arc is absent. Each example is a failure of the weakened claim, not a counterexample to Theorem A.

| Dropped restriction | P | d | Layers | Arcs | min(H-D) | min(U-D) |
|---|---|---|---|---|---:|---:|
| No downward-only arc | (0,1) | (1,1) | {0,1} | 1->0 | -2 | -1 |
| Incoming nesting | (0,1,0) | (0,0,1) | {0,1};{2} | 0->1,1->0,2->0 | -1 | 0 |
| Outgoing nesting | (0,1,1) | (1,1,0) | {0,1};{2} | 0->1,1->0,0->2 | -1 | 0 |
| Antitone demand | (0,1) | (0,1) | {0,1} | 0->1,1->0 | -1 | 0 |
| Integer demand | (0,1) | (1/2,1/2) | {0,1} | 0->1,1->0 | -1/2 | 0 |
| Looplessness | (1,2) | (2,2) | {0,1} | 0->0,0->1,1->0 | -2 | -1 |

Smallest pointwise failure: two mutually compatible vertices with P=(0,1), d=(1,1). For S={1}, H=0, U=1 and F=-1; nevertheless both global minimum margins are -1, attained jointly at S={0,1}. Thus a minimum exact witness need not itself be crossing-free.

The omission search found no one-layer counterexample through n=4 with P in 0..n-1 and common d in 0..n when dropping incoming or outgoing nesting separately. That bounded negative search does not establish either condition is redundant. The three-vertex **two-layer** examples above disprove both blanket weakenings.

## 9. A non-vacuous separation from threshold/Ferrers digraphs

Take one layer with five vertices 0,1,2,3,4, capacities P=(1,1,1,1,2), and all demands one. Add arcs 0->1 and 2->3, and both arcs between 4 and every other vertex. Add no other arcs.

For each strict capacity pair (x,4), mutual compatibility and both nesting conditions hold because 4 reaches, and is reached by, all other vertices. Thus even original TCD holds. For S={0,4}, incoming counts are (1,2,1,1,1), giving H=5 and U=6: the rearrangement question is non-vacuous.

However the off-diagonal submatrix with source rows 0,2 and receiver columns 1,3 is the identity 2-by-2 matrix. Its two present diagonal entries are graph arcs, not self-loops; its two cross entries are absent. No change to vertex self-loops can remove this obstruction. There is therefore **no Ferrers diagonal completion**. The checker explicitly confirms this for all 32 loop assignments.

This refutes an identification of the theorem's entire hypothesis class with threshold digraphs obtained by removing loops from Ferrers digraphs. It does not prove the minimum-margin theorem is new, nor rule out an indirect reduction to a different known theorem.

## 10. Exact next mathematical step

Close the remaining **novelty/reduction** obligation, rather than running more tiny-graph tests or resuming Murty-Simon branches: compare Theorem A, including its fixed compatibility support, arbitrary capacity ties, and full minimum-margin identity, with the classical capacitated Hall / prescribed-zero 0-1 matrix literature. Start with the Fulkerson-Chen comparison documented in `LITERATURE.md` and the five-vertex separating example above. The required output is an explicit hypothesis-and-conclusion-preserving reduction to a cited theorem, or a precisely bounded statement of the unmatched part. Do not infer novelty from failed keyword searches.

External mathematical review of this hand proof remains a separate obligation. No general Murty-Simon theorem, equality classification, or previously suspended row has been promoted by this checkpoint.
