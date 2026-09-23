# Subset-union Hall envelope

Status: proved internally from the graph-level certificate-selection interface and tested only on actual, independently certified diameter-two-critical graphs.

## Lemma

Fix a maximum-degree root v, its neighbor side B, and labels i in A. Let h_i be the number of B-vertices missed by i. Let C_i be the set of physical edges of G[B] which can carry a legal unique-common-neighbor certificate for label i.

For any legal certificate assignment, write x_i for the number of assigned physical B-edges carrying label i, and let P={i:2x_i>h_i}. Then

S = sum_{i in P}(2x_i-h_i)
  <= 2 |union_{i in P} C_i| - sum_{i in P}h_i.

Consequently
H(G,v):=max_{L subseteq A} (2|union_{i in L}C_i|-sum_{i in L}h_i)
satisfies S<=H(G,v). Labels with 2|C_i|<=h_i can be omitted from the maximum.

## Proof

A legal selection assigns each physical edge of G[B] at most once. Every edge counted by x_i lies in C_i. Therefore sum_{i in P}x_i is at most the size of union_{i in P}C_i. Substitute this bound into the displayed expression for S. Taking the maximum over all label subsets gives S<=H. If 2|C_i|<=h_i, adjoining i cannot increase the displayed subset value, so only scalar-eligible labels need be enumerated.

This proof uses physical graph edges and legal certificate choices. It does not assert that an abstract source/profile solution is graph-realizable.

## Fresh disjoint screen

A new generator used Python's Mersenne Twister, seeds 450--549 and n=17--42. Each of the 2,600 outputs was obtained by greedy edge deletion from K_n and then independently checked to have diameter two and to lose the diameter-two property after deletion of every edge.

- certified graphs: 2,600 / 2,600;
- live-strip maximum-root states: 169;
- scalar E>=15 roots: 2;
- maximum scalar E: 19;
- H>=15 roots: 0;
- maximum H: 7.

The two scalar false positives collapsed from (E,H)=(15,5) and (19,7). This is finite internal evidence, not a universal H<15 theorem.

## Exact next check

Screen a larger disjoint batch and compare H with exact legal assignment DP on every scalar E>=15 root. Any H>=15 root must be preserved as a hostile actual-graph witness; absence in a finite batch authorizes no general claim.
