# Live-strip collision recovery check

23 September 2026. Status: **FRESH INTERNAL COMPUTATIONAL EVIDENCE; NO THEOREM PROMOTION**.

This recovery session independently regenerated a deterministic greedy edge-deletion batch from complete graphs on n=17..28, 40 seeds per order (480 graphs total). Each resulting graph was independently certified to have diameter two and to fail diameter two after deletion of every remaining edge.

For every maximum-degree root satisfying the unresolved strip

\[
1/2 < \Delta/n < 250/429,
\]

we reconstructed every endpoint-label certificate on G[B]-edges directly from unique-common-neighbour data. Across 62 live-strip maximum-degree root states there were 404 co-selected F-edge candidate occurrences and zero G[B]-edges lacking an endpoint-label certificate.

The unrestricted crossed-supplement map is **not** injective even inside the live strip: 13 collision images occur. All 13 have source multiplicity exactly two. Thus a strip-restricted categorical injectivity claim is also false.

However, for each of the 13 collision images, an exact dynamic program over the independent certificate choices on every G[B]-edge was run with the collision certificates forced. It tested whether the two collided labels could simultaneously satisfy positive demand, equivalently x_i>R_i and x_k>R_k (or x_i>H_i/2 and x_k>H_k/2). Result: **0/13 collision images admit both labels demand-positive**.

This is fresh finite evidence only. It does not prove demand-restricted injectivity in the live strip, and it does not replace graph-realizability arguments. It does sharpen the next target: unrestricted live-strip injectivity is now refuted, while the live-strip **positive-demand** version survives this independent batch.

A first live-strip collision occurs at n=21, Delta=12, root 2, with labels {4,7}, supplements {3,8}, and sources {13,14}; both-positive demand is infeasible under exhaustive certificate-choice DP. Other collisions occur down to Delta/n=11/21 and remain multiplicity two in this batch.

Exact batch totals: 480 certified D2C graphs; 62 live-strip maximum-degree root states; 404 co-selected F-edge candidate occurrences; 13 collision images; maximum collision multiplicity 2; 0 both-positive-demand feasible collision images.

Next action: derive a theorem-level obstruction from the positive-demand inequalities plus the exact collision motif, rather than pursuing any form of unrestricted injectivity. In particular, for a collision on labels i,k and supplements p,q, retain the forced G K_{2,m} source-supplement motif, the crossed residual incidences q-i and p-k, and the inequalities x_i>R_i, x_k>R_k; seek a charge showing these cannot coexist in the live strip or quantify the residual/degree cost when they do.
