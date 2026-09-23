# Graph-level surplus envelope

23 September 2026. Status: **PROVED INTERNAL NECESSARY CONDITION; ACTUAL-GRAPH FILTER**.

Fix a maximum-degree root v, with B=N(v) and A=V(G)\(B union {v}). For each label i in A define

- h_i = |{u in B : ui notin E(G)}|;
- s_i = the number of those H-incidences ui having exactly one common G-neighbour, with that unique common neighbour in B.

Only these s_i incidences can ever be selected by the endpoint-label certificate construction. Hence every legal selection satisfies x_i<=s_i. Since R_i=h_i-x_i and d_i=max(0,x_i-R_i)=max(0,2x_i-h_i),

\[
d_i \le \max(0,2s_i-h_i).
\]

Summing gives the selection-independent graph-level envelope

\[
S=\sum_i d_i \le E(G,v):=\sum_{i\in A}\max(0,2s_i-h_i).
\]

This is stronger than the per-label eligibility test and lives entirely on the actual graph before any abstract profile optimization. In particular, any strict residual counterexample in the current programme, which internally already requires S>=15, must satisfy E(G,v)>=15 at the chosen maximum-degree root.

## Fresh live-strip screen

On a fresh independently generated and edge-deletion-certified batch covering n=17..32 and seeds 0..99, there were 144 maximum-degree root states in the unresolved strip. The envelope statistics were:

- maximum E(G,v): 21;
- roots with E>=15: 2;
- roots with crossed-supplement collisions: 25;
- roots having both E>=15 and any crossed-supplement collision: **0**.

Thus the present actual-graph sample cleanly separates the two phenomena that the proof needs to combine: large potential surplus and supplement-pair reuse did not occur together. This is finite evidence only; it is not a theorem that E>=15 forbids collisions.

The largest envelope root had n=20, seed 47, root 8, Delta=11 and E=21, with no crossed-supplement collision. The preserved n=23 positive-demand collision negative control has E=13, below the strict-counterexample threshold even before optimizing a legal selection; its exact forced-collision maximum is only S=3.

## Route consequence

The next structural target should be stated at graph level:

> in the live strip, show that E(G,v)>=15 severely limits crossed-supplement congestion, ideally enough to make the weighted pair-lift close; or find an actual D2C negative control with E>=15 and a collision.

This avoids asking for false categorical injectivity and respects the graph-to-profile trust boundary. It also gives a cheap exact prefilter for future actual-graph searches: roots with E<=14 cannot represent the strict residual obstruction at all.
