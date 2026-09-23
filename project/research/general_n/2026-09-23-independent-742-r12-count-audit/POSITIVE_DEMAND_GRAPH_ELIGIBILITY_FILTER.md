# Graph-level eligibility filter for positive demand

23 September 2026. Status: **PROVED INTERNAL NECESSARY CONDITION; FRESH LIVE-STRIP REGRESSION**.

Fix a maximum-degree root v, put B=N(v), A=V(G)\(B union {v}), and fix a label i in A. Let

- h_i = |{u in B : ui notin E(G)}|, the H-degree of i into B;
- s_i = the number of such B-sources u for which u and i have exactly one common G-neighbour, and that unique common neighbour lies in B.

Every selected incidence ui in the endpoint-label framework must be one of these s_i graph-realizable unique-common-neighbour incidences. Hence, for every legal selection,

x_i <= s_i.

Since the residual count is R_i=h_i-x_i, positive demand means

d_i=x_i-R_i=2x_i-h_i>0.

Therefore a necessary graph-level condition for i ever to be demand-positive is

2 s_i > h_i.                                      (ELIG)

This condition is selection-independent and uses the actual graph, not abstract profile feasibility. It provides a cheap pre-selection filter: labels with 2s_i<=h_i can be deleted from every demand-positive collision search before any certificate-choice optimization.

## Live-strip collision consequence

The fresh independent batch used in `LIVE_STRIP_COLLISION_RECOVERY_CHECK.md` contains 13 crossed-supplement collision images in the unresolved degree strip. For every one of the 13, at least one collided label violates (ELIG). Thus **none of the 13 collisions can possibly have both labels demand-positive under any legal selection**, without needing the later dynamic program.

The eligibility margin is 2s_i-h_i. Across the 13 collision images, the better of the two worst-endpoint margins is still -2: each collision has at least one endpoint satisfying 2s_i-h_i<=-2. So the finite sample is not merely failing on parity equality at margin zero.

Examples:

- n=21, Delta=12, root 2, labels {4,7}: (h_4,h_7)=(9,9), (s_4,s_7)=(4,2), margins (-1,-5).
- n=24, Delta=13, root 9, labels {0,1}: (h_0,h_1)=(11,8), (s_0,s_1)=(5,3), margins (-1,-2).
- n=26, Delta=14, root 2, labels {3,18}: (h_3,h_18)=(11,12), (s_3,s_18)=(5,5), margins (-1,-2).

The unrestricted live-strip collision statement remains false; this filter does not prove that two ELIG labels cannot collide. It narrows the exact theorem-level target to:

> show that a crossed-supplement collision in n/2<Delta<250n/429 cannot join two labels satisfying 2s_i>h_i and 2s_k>h_k, or derive enough additional residual/degree charge from such an ELIG--ELIG collision to close the robust plateau.

This is preferable to optimizing over selections first because (ELIG) is an actual-graph invariant and directly addresses the graph-to-profile trust boundary.
