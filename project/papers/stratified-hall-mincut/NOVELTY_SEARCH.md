# Novelty search — stratified Hall/min-cut paper

**Status:** active preliminary comparison; no novelty claim authorised.

## Current structural reduction

The theorem no longer depends on the specific q/c numerical compatibility relation. Its abstract hypothesis is two-sided crossing dominance inside equal-demand layers: strict receiver-capacity order forces mutual compatibility and nested incoming/outgoing neighbourhoods away from the deleted diagonal.

This makes Ferrers/threshold digraph literature more directly relevant than the first search pass suggested.

## Closest literature lead identified so far

Gordana Marmulla and Ulrik Brandes, **On Relations between Neighborhoods of Threshold and Ferrers Digraphs**, *Journal of Graph Algorithms and Applications* 30(1), 207–235 (2026), DOI: https://doi.org/10.7155/jgaa.v30i1.3099.

Their paper studies linearly nested in/out-neighbourhoods in Ferrers digraphs and what remains of those orders after loops are removed to obtain threshold digraphs. This is structurally close to our 'nested away from the diagonal' condition. It does **not**, from the material inspected so far, establish our minimum Hall-margin rearrangement theorem; a full theorem-by-theorem comparison remains required.

Classical Ferrers/chain graph literature is also relevant because nested neighbourhoods are its defining feature. Standard Hall-deficiency and max-flow/min-cut results supply the surrounding min-max framework, while submodular minimisation supplies the lattice of minimum witnesses. None of those components should be presented as new.

## Required comparison questions

For each candidate antecedent ask:

- Is its digraph/bipartite representation equivalent to TCD after deleting the diagonal or adding loops?
- Does it prove equality of a layerwise rearranged *minimum deficiency*, or merely a feasibility/matching criterion?
- Does it guarantee a crossing-free minimum witness?
- Is the neutral-deletion operation already standard in this exact form?
- Can SH1 be reduced to a known Ferrers completion, threshold-digraph, Monge, or polymatroidal min-cut theorem?

## Search themes still open

1. Ferrers and threshold digraph neighbourhood-inclusion preorders;
2. chain/Ferrers bipartite b-matching and capacitated Hall deficiency;
3. submodular minimiser uncrossing and canonical minimum cuts;
4. Monge/comonotone transportation and rearrangement inequalities;
5. polymatroidal and transversal-matroid deficiency formulas.

## Search vocabulary

`minimum Hall deficiency`, `maximum deficiency set`, `lattice Hall witnesses`, `Ferrers capacitated matching`, `threshold digraph matching`, `nested neighbourhood Hall theorem`, `Monge bipartite b-matching`, `comonotone rearrangement min cut`, `submodular minimum witness deletion`, `uncrossing Hall deficiency`, `polymatroidal Hall theorem`.

A preliminary web pass on 17 September 2026 has not exposed an obviously identical minimum-margin theorem. That is not sufficient evidence for novelty.
