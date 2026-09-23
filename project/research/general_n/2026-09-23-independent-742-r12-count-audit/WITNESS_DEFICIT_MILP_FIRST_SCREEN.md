# Exact witness-deficit MILP: first screen

The model minimizes total degree deficit over an abstract assigned-witness graph for fixed demand vector d, witness counts x, rho and Delta.

It retains:
- binary incidences i--t with left degrees x_i;
- integer centre and endpoint deficits;
- pair constraints delta_i+delta_t>=rho+1 on every incidence;
- collision constraints deg(t)<=h_i=2x_i-d_i on every incidence;
- the full quadratic star inequality for every label;
- exact endpoint-deficit reuse through the same right vertex.

This is stronger than the multiplicity-compressed scalar inequality but remains an abstract assigned-witness feasibility test, not an actual graph-realizability proof.

The scalar screen first permits n=14, Delta=8, rho=2, Dmax=12. Its largest-margin pattern is d=(6,3,2,2,2), x=(7,3,2,2,2), h=(8,3,2,2,2). The exact MILP optimum is D=21. Therefore this apparent survivor cannot occur within a strict counterexample's deficit budget.

This does not close the n=14 row: other demand and witness-count patterns remain to be enumerated. The exact next action is exhaustive row screening, preserving any abstract survivor for actual-graph realizability analysis.
