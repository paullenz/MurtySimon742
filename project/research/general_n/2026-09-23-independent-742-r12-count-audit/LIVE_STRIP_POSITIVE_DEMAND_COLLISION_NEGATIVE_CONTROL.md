# Live-strip positive-demand collision negative control

23 September 2026. Status: **categorical live-strip positive-demand injectivity is false**.

A fresh independent greedy-deletion expansion over n=17..36 with 80 seeds per order produced 1,600 independently edge-deletion-certified diameter-two-critical graphs. There were 123 maximum-degree root states with 1/2 < Delta/n < 250/429, containing 997 co-selected F-edge candidate occurrences and 34 crossed-supplement collision images.

At n=23, seed 47, maximum-degree root 7 has Delta=13, so Delta/n=13/23 lies inside the unresolved strip. The labels {1,4} collide at supplements {0,20} for distinct sources 11 and 17. The forced certificates are (11,1,0), (11,4,20), (17,1,0), (17,4,20).

A complete legal certificate selection exists with collided-label rows

- label 1: H-degree 10, selected x=6, residual R=4, demand d=2;
- label 4: H-degree 9, selected x=5, residual R=4, demand d=1.

Thus both collided labels are demand-positive. Both are also graph-eligible under the selection-independent filter: their selectable counts are s_1=s_4=6, giving 2s_1-h_1=2 and 2s_4-h_4=3.

The full legal selection is:

(11,1,0), (17,1,0), (15,1,5), (16,1,5), (22,1,5), (14,3,8), (16,4,8), (8,19,18), (11,12,17), (11,4,20), (13,4,14), (13,1,18), (15,4,14), (17,4,20), (18,9,20), (22,2,21).

The total demand of this selection is S=3, so this is a negative control for the collision route only. It is not a Murty--Simon counterexample and does not challenge the internal S<=14 closure. It refutes only the proposed universal statement that live-strip crossed-supplement collisions cannot join two positive-demand labels.

An exact MILP over all legal certificate choices, with the four collision certificates forced and both collided labels constrained positive, shows that the maximum possible total demand for this graph/root/collision is **S=3**. Thus this negative control cannot be lifted into the S>=15 regime by a different legal completion.

A second ELIG--ELIG collision in the same graph, on labels {3,6} with supplements {0,20}, is infeasible when both collided labels are constrained positive demand.

Route consequence: retire categorical live-strip demand-positive injectivity. Keep the proved supplement-pair congestion bound M_pq <= codeg_{G[B]}(p,q) and move to a quantitative charge using demand magnitude, collision multiplicity, B-two-path congestion and especially the large-surplus regime. The present negative control has d_1+d_4=3 and globally maximal forced-collision S=3, so the S>=15 regime forced by any strict residual counterexample remains the relevant place for a sharpened theorem.
