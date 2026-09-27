# Fixed-support Hall closure: reductions, a saddle theorem, and a sharp boundary

27 September 2026. User-requested mathematical continuation in `paullenz/MurtySimon742`.
Inspected predecessor: `e00989f1b47c78bfb8a133ef89ffc06cc73ba9fb`.

**Status: internally proved deductions and reproducible finite checks. Not external verification, formal proof-assistant certification, a novelty claim, or a general Murty-Simon proof.** The preceding closure proof was read, not independently blinded. Its full statement and proof are preserved byte-for-byte as `THEOREM_A.md`; that archived text's relative test-file references belong to the preceding closure bundle and its next-step paragraph is superseded by Section 12 here. The earlier downloadable closure bundle was checked against all 15 entries of its manifest; its millions of earlier test instances were not rerun or re-credited here.

## 1. What this session resolves

The original capped Hall problem has a complete, explicit reduction to a prescribed-zero binary matrix with exact margins. The genuinely substantive comparison concerns the **sorting/rearrangement step**, not whether the exact matching problem is a network-flow problem. More importantly, a dummy-receiver construction proves that feasibility equivalence for the right closed class already implies the full minimum-deficit identity. Therefore, “our conclusion gives the entire deficit, rather than only feasibility” is **not by itself a valid distinction from prior work**.

The closure theorem also yields a pure saddle point: the original placement of receiver capacities maximises achievable flow among all within-layer permutations, with one common source cut bounding every competing placement. A seven-vertex example shows why this cannot follow from unrestricted Hall/min-cut duality: all capacity placements can be equally flow-optimal while the sorted relaxation still misses one unit of deficit. Disjoint copies give arbitrarily large additive gaps.

The general fixed-support matrix formulation is settled below. A reduction of the structural sorting theorem to the specialised Anstee/Chen conditions is **not settled**: the needed full theorem texts were not obtained. This is a bounded literature-access limitation, not evidence of novelty.

## 2. Definitions and inherited closure theorem

Let V be a finite vertex set partitioned into layers. R is a fixed loopless directed relation. All allowed source-to-receiver arcs have capacity one. Receiver capacities P and source demands d are nonnegative integers. Source and receiver copies remain distinct, despite sharing labels.

For S contained in V, define

\[
y_w(S)=|\{u\in S:uRw\}|,\quad D(S)=\sum_{u\in S}d_u,
\]
\[
H_P(S)=\sum_w\min(P_w,y_w(S)),\quad F_P(S)=H_P(S)-D(S).
\]

For a layer L and positive integer k let a(L,k) count its capacities at least k and b(L,k,S) count its incoming multiplicities at least k. Put

\[
U(S)=\sum_L\sum_{k\ge1}\min(a(L,k),b(L,k,S)).
\]

Equivalently, within each layer sort the capacity list and incoming-count list separately in the same order, and sum their paired minima. Always H_P(S) <= U(S).

**Theorem A (preceding checkpoint).** For each same-layer pair x,y with P_x<P_y, assume: (i) zRx implies zRy for z outside {x,y}; (ii) xRz implies yRz for z outside {x,y}; (iii) yRx implies xRy; and (iv) d_x>=d_y. Equal-capacity pairs and pairs in different layers have no such constraints. Then

\[
\min_S F_P(S)=\min_S(U(S)-D(S))=:\gamma.
\]

There is an exact minimizer S* with H_P(S*)=U(S*). It is constructible from the maximal exact minimizer by at most |V| neutral source deletions. `THEOREM_A.md` contains the full proof, including the maximal-minimizer and permanent-slack arguments. Original TCD, which requires mutual arcs for strict-capacity pairs and constant demand within each layer, is a subclass.

**Trust boundary.** Theorem A is an internal hand proof. The deductions below are proved from its stated conclusion where explicitly indicated. Several other results below hold for arbitrary supports without Theorem A.

## 3. Rearrangement as an exact capacity-permutation envelope

Let Pi be the finite set of all distinct capacity placements obtained by permuting P separately inside each layer, holding R, d and the layers fixed. Write P^pi for such a placement and e for the original placement. Define F_pi(S)=H_(P^pi)(S)-D(S).

**Proposition 1 (no structural hypotheses).** For every S,

\[
U(S)=\max_{\pi\in\Pi}H_{P^\pi}(S).
\]

**Proof.** At threshold k in a layer, the contribution to H is the intersection size of the capacity and multiplicity superlevel sets. It is at most the smaller of their sizes. Assign the sorted capacity list to the receiver labels in sorted incoming-count order. Every pair of superlevel sets is then nested, simultaneously for all k. This one placement attains every threshold upper bound in that layer, and the choices for different layers are independent. Summing proves the identity. Ties may be broken arbitrarily. QED.

The placement attaining this maximum can depend on S. Treating it as one globally chosen placement without proof would be a quantifier error.

## 4. Pure saddle point and optimal capacity placement

**Theorem B (consequence of Theorem A).** There is a source set S* such that, for every capacity placement pi and every source set S,

\[
F_\pi(S^*)\le\gamma\le F_e(S).
\]

Consequently

\[
\boxed{\max_\pi\min_S F_\pi(S)
=\gamma
=\min_S\max_\pi F_\pi(S).}
\]

The original placement e attains the left maximum. Thus it maximises supported unit-edge flow among all allowed within-layer capacity rearrangements.

**Proof.** Choose the exact minimum witness S* with H_P(S*)=U(S*) given by Theorem A. Proposition 1 gives

\[
F_\pi(S^*)\le U(S^*)-D(S^*)=\gamma=F_e(S^*).
\]

Minimality gives gamma<=F_e(S) for every S. Therefore min_S F_pi(S)<=gamma for every pi, with equality for e. Taking the pointwise maximum first gives U-D, whose minimum is gamma. Finally, for a fixed placement, the flow value is D(V)+min_S F_pi(S): minimise each receiver's side of a cut in the network s->u (d_u), u->w (one if uRw), w->t (P^pi_w). This proves the flow assertion. QED.

S* need not be a minimum cut for every competing placement. It is a common upper-bounding cut. Nor is e necessarily the unique best placement.

## 5. Universal-dummy reduction: feasibility implies the entire deficit

Write gamma_H=min(H-D) and gamma_U=min(U-D) for an arbitrary integer instance. Both are nonpositive because the empty set has margin zero, and gamma_H<=gamma_U.

For an integer q>=0, add q new vertices. Each new vertex has receiver capacity one, source demand zero, and no outgoing arcs. Every original source reaches every new receiver. Put the new vertices into one new layer; do not merge this layer with any original layer.

**Lemma 2.** In the augmented instance,

\[
\gamma_H(q)=\min(0,\gamma_H+q),\qquad
\gamma_U(q)=\min(0,\gamma_U+q).
\]

**Proof.** For an augmented source set S', let S=S' intersect V. Dummy sources add no demand or receiver incidence. If S is nonempty, all q dummy receivers contribute one to both H and U. If S is empty, all terms are zero. Thus each nonempty original source set has its two margins shifted by q, while the empty set remains zero. Minimising gives the displayed identities. This also covers gamma_H=0 or gamma_U=0, whether or not a nonempty minimizer exists. QED.

The transformation preserves all four hypotheses of Theorem A. For a strict-capacity pair of original vertices, dummy sources reach neither member and both original vertices reach every dummy receiver. Within the dummy layer all capacities are equal. It also preserves the stronger original TCD assumptions.

**Theorem C.** On any class of integer instances closed under this dummy construction, the following two universal claims are equivalent:

1. The inequalities U(S)>=D(S) for all S are sufficient for feasible routing of every source demand.
2. min(H-D)=min(U-D) for every instance in the class.

Necessity of the U inequalities is automatic from H<=U; feasible routing is equivalent to gamma_H=0.

**Proof of the nontrivial implication.** For an arbitrary original instance choose q=-gamma_U, an integer. Lemma 2 gives gamma_U(q)=0. Assumed feasibility sufficiency in the augmented instance yields gamma_H(q)=0, hence gamma_H+q>=0. Therefore gamma_H>=gamma_U; the opposite inequality always holds. The reverse implication follows immediately at gamma_U=0. QED.

This is a mathematical correction to an overly broad possible novelty argument. A literature theorem need only establish the right feasibility implication on the dummy-closed class; it need not state the full deficit formula separately. Ordinary exact Hall criteria do not, on their own, establish that implication for U.

## 6. Exact reduction to a prescribed-zero binary matrix

Let D=D(V), C=sum_w P_w, and choose an integer target t with 0<=t<=min(D,C). Put a=D-t and b=C-t. Let A be the n-by-n zero-one support matrix of R.

Construct a binary matrix with n+b rows and n+a columns, allowed support

\[
\begin{pmatrix}
A&J_{n\times a}\\
J_{b\times n}&0_{b\times a}
\end{pmatrix},
\]

row sums (d_1,...,d_n,1,...,1), with b trailing ones, and column sums (P_1,...,P_n,1,...,1), with a trailing ones. Each original forbidden entry, including the original zero diagonal, remains forbidden. J denotes an all-allowed block; the bottom-right block is forbidden, not optional.

**Proposition 3.** This exact-margin binary matrix exists if and only if the original supported flow has value at least t.

**Proof.** An integral original flow of value at least t can have unit arcs removed until its value is t. Regard its original n-by-n block as X. Its total row shortfall is a. Assign each unit of row shortfall to a different dummy column; this makes every dummy column sum one and every original row sum d_u. Its total column shortfall is b. Assign each unit to a different dummy row, making every dummy row sum one and every original column sum P_w. Since the dummy columns and rows are distinct unit objects and all cross-block entries are allowed, each constructed entry is zero or one. The bottom-right block stays zero.

Conversely, every dummy column gets its single unit from the original rows. Thus a units of the original row total D lie outside the original block, leaving exactly t inside. That block obeys R and the original row/column upper bounds. It is an original flow of value t. QED.

This is an explicit existence reduction, not a claim of a new matrix-realisation theorem. With binary-encoded huge capacities the unit-expanded matrix can be large. A compact (n+1)-by-(n+1) bounded-integer version uses one slack column of sum a and one slack row of sum b, bounds d_u on the top-right entries and P_w on the bottom-left entries, and fixes the corner to zero. The same conservation proof applies.

**Crucial limitation.** Padding places the exact H problem inside the general prescribed-zero matrix problem. It does not convert arbitrary fixed support into the complete off-diagonal support of ordinary digraph degree-realisation criteria. Nor does it yet derive the U inequalities from a specialised covering-matrix theorem. Those are separate obligations.

## 7. A seven-vertex minimax gap, with an unbounded additive extension

Let V={0,...,6}, one layer, and define seven triples, with arithmetic modulo seven,

\[
L_j=\{j,j+1,j+3\}.
\]

Allow uRw exactly when u is not in L_w. Give every source demand one. The capacity multiset is (4,4,0,0,0,0,0).

Every vertex belongs to three triples and every pair of distinct triples intersects in one vertex. One direct verification is that the six ordered nonzero differences of {0,1,3} give every nonzero residue modulo seven exactly once. Also w belongs to L_w, so the relation is loopless. Each receiver sees four sources and each source reaches four receivers.

There are 21 different capacity placements. If receivers j,k are active, their visible-source union is V minus (L_j intersect L_k), of size six. Hence their flow value is at most six. Each receiver has two visible sources not visible to the other, and they have two common visible sources. Send each exclusive pair to its receiver and split the two common sources; both loads are three, below capacity four. Thus **every placement has flow six**, and every exact minimum margin is -1.

For any source set S, let y_(1)>=...>=y_(7) be its sorted receiver counts. Each count is at most four, so Proposition 1 gives U(S)=y_(1)+y_(2). Since each selected source contributes to four receiver counts,

\[
U(S)\ge\frac{2}{7}\sum_w y_w(S)
=\frac{8}{7}|S|\ge D(S).
\]

The empty set attains zero, and consequently

\[
\boxed{\max_\pi\min_S F_\pi(S)=-1<0=\min_S\max_\pi F_\pi(S).}
\]

This disproves the inference that an optimal original capacity placement alone implies closure. All 21 placements are optimal here, yet every one has a closure gap. It also disproves an unrestricted exchange of min and max. It is **not** a counterexample to Theorem A: the required nesting conditions fail, verified for every placement.

For any positive integer r, take r disjoint copies, each in its own layer, with no cross-copy arcs. H, U and D add over the copies; all choices of source sets and within-layer placements factor independently. Every placement has flow 6r, the exact minimum margin is -r, and the sorted minimum margin is zero. Thus the unrestricted additive closure gap is unbounded. This extension is a direct-sum hand proof, not an exhaustively enumerated large-instance claim.

## 8. Capacity ties do not legitimise fixed-support prefix tests

Use four vertices, all P=d=1 in one layer. Put both directed arcs between hub 0 and each of leaves 1,2,3, and no other arcs. Theorem A holds because all capacities tie; H=U pointwise.

In order 0,1,2,3, the four initial-prefix H-D margins are 2,2,1,0. Yet the leaf set {1,2,3} has H=1 and D=3, margin -2, and maximum flow is two. On the complete off-diagonal support, the same degree vectors permit flow four (a directed four-cycle).

Thus retaining degree order while forgetting fixed support is not a valid reduction. Even replacing the usual complete-support formula by exact fixed-support H only on those prefixes is insufficient. This rules out those direct substitutions, not every possible gadget reduction.

## 9. A solver-independent certificate, and an equivalence

A certificate consists of the complete labelled instance, a set E_f of distinct allowed unit arcs respecting the source and receiver bounds, and a source set S satisfying

\[
|E_f|=D(V\setminus S)+H_P(S),\qquad H_P(S)=U(S).
\]

**Proposition 4.** Such a certificate proves, for this instance, that the original flow is optimal, min(H-D)=min(U-D), and the original capacity placement maximises flow among all within-layer permutations. No structural hypothesis of Theorem A is required by the verifier.

**Proof.** The feasible flow is a lower bound and the displayed cut is an equal upper bound. It is therefore optimal and S is an exact minimizer. Equality H=U there, together with H<=U everywhere, proves the minimum-margin identity. For every placement pi, Proposition 1 gives H_pi(S)<=U(S)=H_P(S). The same source cut bounds that placement's flow by |E_f|. QED.

Conversely, whenever an integer instance satisfies the minimum-margin identity, take a minimizer of U-D. Its exact margin lies between the same minimum value and itself, so it is also an exact minimizer with H=U. An integral maximum flow supplies the other half of the certificate. Hence this certificate exists **if and only if** that instance has closure. This does not provide an algorithm for discovering closure in arbitrary instances; it gives a compact way to verify a claimed instance witness.

`verify_certificate.py` implements only these local checks, with no search, solver, residual graph, imports from the producer, or reliance on Theorem A. It independently calculates U by threshold counts while the producer uses sorting. Validation uses explicit exceptions, not Python assertions, and remains active with `python -O`.

The saved nontrivial proper-cut example has P=(0,1,3), d=(1,1,2), layers {0,1};{2}, and arcs 0->1,1->0,0->2,1->2,2->1. Original flow is three, while swapping the capacities inside {0,1} reduces flow to two. The common source witness S={2} has original H=U=1 and demand two. The certificate proves the result directly.

## 10. Primary-source comparison and its exact limits

**Fulkerson-Chen-type digraph criterion.** Berger's full arXiv text [B], Theorems 1 and 3, was read; the displayed Theorem 1 was also checked in a rendered PDF page. In the complete off-diagonal support case, with equal total exact margins and after transposing the degree interpretation as necessary, the criterion compares the first k demands with

\[
\sum_{i\le k}\min(P_i,k-1)+\sum_{i>k}\min(P_i,k).
\]

This is precisely H for that prefix because every receiver sees k selected sources, except selected labels see k-1. Theorem 3 allows demands sorted nonincreasingly and restricts tests to drop indices and the final index. Nothing in that theorem supplies arbitrary additional prescribed zeros. Section 8 is a direct fixed-support obstruction. This is a comparison of stated mathematics, not an assertion about historical priority among Fulkerson, Chen, Anstee and Berger.

**General entry-bounded matrices.** Anstee's 1983 publisher abstract [A83] explicitly studies integral matrices with fixed row/column sums and entry bounds via integral network flows. Section 6 gives a fully explicit reduction into that general setup. Only the abstract, not all theorem statements in that paper, was obtained here. No specialised theorem number or uninspected hypothesis is claimed to have been checked.

**Specialised covering/bounded-matrix criteria.** Anstee 1982 [A82] was accessible as its publisher's opening extract, not its full 16 pages. William Y. C. Chen 1992 [C92] was accessible at abstract level: it advertises necessary-and-sufficient criteria under a main condition, unifying earlier results. That main condition has **not** been extracted or checked. Failure to obtain it is not a separation theorem. An indirect reduction to those criteria remains possible.

**Exact unmatched step.** Determine whether their structural conditions, applied directly or through a support-preserving transformation, imply

\[
\forall S\quad U(S)\ge D(S)
\quad\Longrightarrow\quad
\text{a supported flow meeting all demands exists}
\]

for the integer, loopless, pair-excluding nested class of Section 2. By Section 5, once that implication holds on the dummy-closed class, the full deficit identity follows. Repeating generic Hall/max-flow duality or the exact-margin padding construction alone does not answer this question.

### Sources and access status

[B] Annabell Berger, *A Note on the Characterization of Digraph Sequences*, arXiv:1112.1215v2 (17 September 2013), full text, particularly Theorems 1 and 3. Journal version: *A note on the characterization of digraphic sequences*, Discrete Mathematics 314 (2014), 38-41, DOI 10.1016/j.disc.2013.09.010. https://arxiv.org/pdf/1112.1215

[A83] R. P. Anstee, *The network flows approach for matrices with given row and column sums*, Discrete Mathematics 44(2) (1983), 125-138, DOI 10.1016/0012-365X(83)90053-5. Publisher abstract only. https://www.sciencedirect.com/science/article/pii/0012365X83900535

[A82] R. P. Anstee, *Properties of a Class of (0,1)-Matrices Covering a given Matrix*, Canadian Journal of Mathematics 34(2) (1982), 438-453, DOI 10.4153/CJM-1982-029-3. Publisher extract only. https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/properties-of-a-class-of-01matrices-covering-a-given-matrix/9A3857D219511017536142BD7F132C91

[C92] William Y. C. Chen, *Integral matrices with given row and column sums*, Journal of Combinatorial Theory, Series A 61(2) (1992), 153-172, DOI 10.1016/0097-3165(92)90015-M. Publisher abstract only. https://www.sciencedirect.com/science/article/pii/009731659290015M

These are citations and access records, not redistributed copies of copyrighted papers. No novelty conclusion is drawn from the search.

## 11. Fresh computational evidence and reproduction

`check_reductions.py` uses only the Python standard library. Its flow producer is separate from the small certificate verifier. It also enumerates all source sets to test the flow oracle and maximal-minimum-cut projection. Fresh results:

| Check | Exact scope/result |
|---|---|
| Eligible instances | 33,552 labelled n=3 instances, P,d in {0,1,2}, all 64 loopless supports, layers (0,0,0) or (0,0,1), filtered by Theorem A |
| Capacity comparisons | 52,056 instance-placement pairs and 416,448 source-set payoff entries; zero saddle or envelope mismatches |
| Deletion traces | 324 neutral deletions in deterministic traces, exact margins preserved |
| Flow deficiencies | 18,925 instances with flow strictly below both total demand and total receiver capacity |
| Dummy construction | 2,592 augmented instances, 38,880 source-set entries, 2,160 hypothesis-preserving cases; exact margin-shift identities pass |
| Binary padding | 764 target-threshold instances, 468 feasible; 711,632 candidate padded matrices examined; existence agrees with independently enumerated original flows |
| Minimax obstruction | All 21 capacity placements and all 128 source sets per placement saved; actual flow six versus sorted feasible demand seven |
| Certificate rejection | 19 named corruptions rejected, including a valid optimal flow/cut pair with H<U; that case is rejected specifically for its rearrangement gap |

The padding search stops on the first witness, or exhausts all candidate matrices when none exists; 711,632 is the actual number examined, not a claim that all possible matrices in feasible cases were inspected. Domain details and source hashes are recorded in the two result files. No random sampling is used. The checker refuses Python -O because its regression assertions must be active; the independent verifier does not rely on assertions.

Run from this directory:

```sh
python3 check_reductions.py --output replay --part core
python3 check_reductions.py --output replay --part padding
python3 verify_certificate.py replay/PROPER_CUT_CERTIFICATE.json
python3 -O verify_certificate.py replay/PROPER_CUT_CERTIFICATE.json
```

The ordered small-instance record digest is
`1fd72577bf8356f7a4ae9b6c0875be10250a9fb8436c1178a3062db1838c382b`.
It is not a cryptographic proof of the universal theorem; it identifies a reproducible ordered enumeration. These targeted checks overlap previous small-instance domains and are not added to the previous millions as new distinct coverage.

## 12. Next task and unchanged project controls

**Next mathematical action:** obtain the full stated structural condition and sufficiency theorem from [C92], or the corresponding covering-matrix criterion in [A82], and test it against Section 2 after the explicit transformations of Sections 5-6. Record the variable map, each hypothesis, and the resulting inequality. A positive reduction must derive U-feasibility sufficiency; a negative result must exhibit a specific failed hypothesis and remain limited to that proposed reduction. Do not substitute another enumeration, a generic max-flow citation, or a novelty claim.

External specialist review of Theorem A remains separate and open. No general Murty-Simon conclusion, n=25 status, inherited threshold, equality classification, X3, audit34854911792, or suspended n18 row is promoted. This is one user-triggered continuation, not a restarted cadence. No research schedules, services, deployments, paid compute, or unrelated financial/health alerts were changed.
