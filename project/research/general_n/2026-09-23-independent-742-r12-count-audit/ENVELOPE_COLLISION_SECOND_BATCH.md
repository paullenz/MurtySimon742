# Large-envelope collision second-batch check

23 September 2026. Status: **FINITE NEGATIVE CONTROL AND TARGET REFINEMENT**.

A disjoint second batch (n=17..32, seeds 100..199) was independently generated and edge-deletion-certified. It produced 156 live-strip maximum-degree root states. One root has graph-level surplus envelope E(G,v)=15 **and** crossed-supplement collisions, so the provisional finite pattern "E>=15 implies no collision" is false even in this bounded search.

The negative control is n=20, seed 112, root 3, Delta=11 (Delta/n=0.55), with E=15 and four crossed-supplement collision images. However all four collisions have at least one graph-ineligible endpoint, so none can join two positive-demand labels under any legal selection. The four label pairs are {0,4}, {0,9}, {0,14}, and {14,19}, all at supplement pair {7,11}; label 0 has eligibility margin 2s-h=-4, label 14 has margin -4, label 4 has -3, and label 19 has margin 0.

The root's positive envelope comes instead from labels 2,9,13,18 with envelope contributions 5,4,1,5 respectively. Thus large total envelope can coexist with supplement-pair reuse, but in this example the reuse is confined to labels that cannot carry positive demand.

Combined with the first disjoint batch (seeds 0..99), 3,200 independently certified graphs produced 300 live-strip maximum-degree root states. Three roots had E>=15. None of those three contained an ELIG--ELIG crossed-supplement collision.

This is finite evidence only. The sharpened theorem target is therefore not "E>=15 forbids collisions". It is:

> if E(G,v)>=15 in the live strip, control or exclude crossed-supplement collisions whose **both endpoints are graph-eligible** (2s_i>h_i and 2s_k>h_k), since only such collisions can affect positive-demand capacity.

The n=23 positive-demand collision negative control remains outside this sharpened regime because its graph-level envelope is E=13 and its exact forced-collision maximum total demand is S=3.
