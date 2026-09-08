# Independent audit of the graph-to-quasi-edge construction

8 September 2026. Internal assurance work by ChatGPT/Geeps. **Candidate proof status remains unchanged; independent specialist review remains OPEN.**

## Result

No defect was found in the complement edge-insertion construction used by the layer-sum proof. The argument was reconstructed from first principles, compared with the standard quasi-edge observation in the total-domination literature, checked by a second exhaustive implementation on a clean GitHub runner, and its local edge-insertion bridge was checked in Lean 4.19.0.

## 1. First-principles reconstruction

Let G be diameter-two edge-critical and H its complement. An adjacent pair xy totally dominates H exactly when xy is a nonedge of G and x,y have no common G-neighbour; equivalently their G-distance is greater than two. Since diam(G)=2, H contains no adjacent total-dominating pair.

Take a missing edge uw of H, i.e. an edge of G. Criticality says G-uw has diameter greater than two, so H+uw contains an adjacent total-dominating pair xy. Since H had none, adding uw must be essential to this pair. Therefore either xy={u,w}, or xy uses exactly one endpoint of the new edge and its other edge was already present in H. A pair avoiding both u and w would have unchanged adjacency and unchanged open-neighbourhood union and so would already totally dominate H, impossible.

Now choose v of minimum H-degree and put A=N_H(v), B=V(H)\N_H[v]. For a missing pair uw inside B, both u and w miss v. Thus {u,w} cannot totally dominate H+uw. Hence every newly created adjacent total-dominating pair has the form ui (or wi), where i is an old H-neighbour of the source. It must dominate v, so i belongs to A.

Suppose the pair is ui in H+uw. The only neighbourhood incidence added to ui's open-neighbourhood union is u-w. Therefore before insertion

    N_H(u) union N_H(i) = V(H) \ {w}.

In particular ui is an existing cross-edge, u and i both miss w, and ui has exactly one common miss, namely the supplement w. This is precisely the quasi-edge object used by the layer-sum proof.

The same reasoning also proves uniqueness of the exception for a fixed selected edge. Therefore one selected cross-edge cannot represent two different missing B-pairs. Once one quasi-edge is selected for each missing B-pair, the global selection is injective. At a fixed source, its labels are distinct because the selected cross-edges are distinct, and its supplements are distinct because the underlying missing B-pairs are distinct.

This establishes the particular properties subsequently used in the edge ledger, residual injection and unordered-pair capacity. No assumption of unique quasi-edge *choice* is made: a missing B-pair may have several possible quasi-edges; the construction chooses one.

## 2. Literature cross-check

The standard total-domination formulation describes the same mechanism: adding a missing edge to the relevant complement creates an adjacent dominating pair called a quasi-edge; it uses an endpoint of the added edge, need not be unique, and has a unique undominated vertex before insertion. The usual observation says that for a missing edge uv either {u,v} dominates, or there is z with uz having unique exception v (or zv having unique exception u).

Our root v and B-pair setup explicitly rules out the first alternative because both B endpoints miss v. Thus the project's construction is a specialization of the standard quasi-edge observation. This comparison supports the logic but is not a substitute for checking the later new inequalities.

References consulted in this audit include the Haynes-Henning-van der Merwe-Yeo maximum-degree paper and the Murty-Simon total-domination papers indexed in the project literature notes. No claim of exhaustive literature priority follows.

## 3. Independent exhaustive implementation

`src/check_construction_independent.py` was written separately from `check_layers.py`. It does not import or call the selected-system constructor. It directly:

1. rebuilds all labelled simple graphs for 3<=n<=6;
2. tests diameter-two edge-criticality by deleting every edge;
3. constructs H and every minimum-degree root;
4. for every missing H[B] pair uw, constructs H+uw;
5. enumerates *every* adjacent total-dominating pair in H+uw;
6. verifies that {u,w} is excluded by the root, that every new pair is incident with exactly one of u,w, that the other endpoint lies in A, that the cross-edge existed before insertion, and that its old open-neighbourhood union is exactly V\{supplement}.

Recorded result:

    labelled simple graphs:              33,864
    diameter-two edge-critical graphs:      608
    minimum-degree roots:                    920
    missing B-pairs checked:                 720
    new adjacent total-dominating pairs:     720
    valid quasi-edge characterisations:      720
    ordered-case SHA-256:
      1f2b1bb5bd91d54937f166abd0c26badd8ddd105441cd37a6d0150c557d46c5e

All assertions passed locally and again in GitHub Actions run `34194951298` on Ubuntu 24.04, commit `604ce7b16d559d35386960b2d6d9d50be5aee319`. In this small exhaustive domain each insertion happened to have one adjacent total-dominating pair, but the proof and checker do not assume uniqueness generally.

This is a second implementation by the same assistant, not external reproduction and not a universal proof by enumeration.

## 4. Lean extension

The existing `formal/QuasiCore.lean` slice previously began *after* the quasi-edge premises. It now includes explicit local definitions of adding one edge and an adjacent total-dominating pair, plus four bridge lemmas formalising:

- an added edge cannot affect an ordered adjacency whose left endpoint avoids both inserted endpoints;
- a genuinely new adjacent total-dominating pair must be incident with the added edge;
- the newly added endpoint-pair cannot totally dominate when the two endpoints have a common missed vertex;
- an adjacent total-dominating pair `u,i` created by adding `u,w`, under the stated distinctness/missing-edge hypotheses and absence of an old pair, yields `Quasi adj u i w`.

The first GitHub Lean run, `34194781386` at commit `799410e5bebe290e73b72d306c260bd6812fe18b`, failed because the proof script for the common-miss endpoint lemma used the wrong equality component/direction in four cases. The other new bridge lemmas elaborated. The case handling was corrected without changing the mathematical statement.

The corrected source at commit `60f943d5aeed683cc520e043a1b6b26f581a750c` passed GitHub Actions run `34194930796` using Lean 4.19.0 on Ubuntu 24.04. The workflow explicitly rejects `sorryAx`, warnings and errors. The log reports no `sorryAx`; together with the six existing local lemmas, ten local quasi-edge/edge-insertion lemmas now check in this scoped file.

This does **not** formalise diameter-two edge-criticality, the finite selection/injection construction, the residual ledger, threshold pair counting, the layer-sum inequality, or the 13/22 consequence.

## 5. Remaining gap after this audit

The major unformalised pieces before the numerical layer theorem are primarily finite-cardinality selection/injection statements and the threshold/layer counting. The minimum-degree edge ledger is elementary and independently re-derived. The highest-value next formal target is the residual injection or an abstract finite version of the threshold pair-capacity lemma.

The absence of positive-surplus actual graph examples is not resolved by this audit. Any counterexample to the Murty-Simon density bound in the relevant maximum-degree range would necessarily have positive surplus, so existing actual-graph samples cannot exercise that hypothetical regime.

**Verdict:** the graph-to-selected-system bridge is materially better supported than at the start of this audit; no blocking logical defect has been found. The full 13/22 result remains a candidate until the remaining new counting argument receives independent mathematical review (and, ideally, broader formalisation).
