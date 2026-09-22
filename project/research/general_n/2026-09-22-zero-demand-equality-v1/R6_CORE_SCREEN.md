# Residual-mass-six optimistic core screen

22 September 2026. Exact finite enumeration of an explicitly stated necessary relaxation. This is not a graph search and its survivors are not D2C realizations.

For each integer partition of r=6, screen_r6_core.py enumerates every simple graph on the positive-residual support C. It imposes:
- the proved edge charge R_i+R_j>=2;
- P={i:d_i>R_i} has no zero-residual neighbour;
- the exact core ledger t=e(P)-e(N)-sum_{P}R_i-sum_{N}(R_i-d_i);
- the selected-source capacity (d_i-R_i)^2<=sum_{j in N_F(i)}R_j at every i in P.

For N-labels with R_i>=2, the screen optimistically permits zero-residual leaves to fill d_i up to R_i and hence sets their slack to zero. For an isolated unit column it keeps slack one, since a (0,1) F-edge is forbidden. This deliberately enlarges the physical feasible set. A screen survivor is only a necessary residual-core shape.

## Exact result

Every partition except (2,1,1,1,1) has zero strict-surplus survivors. This includes the all-unit partition independently covered by the unit-column theorem.

For (2,1,1,1,1), 656 core graphs pass the preliminary local filters. Exactly 31 labelled graphs can have optimistic t>0. Permuting the four unit columns reduces these to four orbits, of labelled sizes 4,12,12,3. Three orbit representatives have seven edges and t_upper=1; the densest has eight edges and t_upper=2. The exact edge lists, degrees, P/N split and selected lower bounds are in R6_CORE_SCREEN.json.

Thus a strict residual-mass-six counterexample is forced into one residual partition and four optimistic core orbits. No theorem excludes those orbits yet. Zero-residual attachments, selected/residual source identities, legal supplements, deletion criticality, the maximum-root condition and full graph realizability remain to be imposed.

The useful negative conclusion is exact at the relaxation's declared level: no other r=6 residual partition or support core can carry strict surplus under the inherited necessary lemmas.

Next: enumerate physical source-state multisets for the four orbits, retaining exact column residual sums and selected lower bounds; then impose supplement uniqueness before any graph-realizability claim.
