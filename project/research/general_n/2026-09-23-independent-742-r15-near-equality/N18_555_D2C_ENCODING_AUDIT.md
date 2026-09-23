# Audit of the d=x=h=(5,5,5) D2C UNSAT encoding

The model was staged:

- exact degrees and fixed source geometry: **SAT**;
- exact degrees, fixed geometry and diameter at most two: **SAT**;
- the same constraints plus edge-deletion criticality: **UNSAT**.

Thus UNSAT is not caused by an inconsistent degree sequence, the perfect-matching source reduction, or diameter alone.

A separately coded NetworkX replay of a diameter-stage SAT model confirmed:

- required degree vector: exact;
- label/C and T/C incidences: exact;
- edge count: 82;
- connected diameter: 2;
- D2C: false;
- noncritical edges: 61.

The local criticality predicate used by Z3 was then compared with literal edge deletion followed by connectivity/diameter calculation on every edge of every connected Graph Atlas graph with diameter at most two. Coverage: 457 graphs, 5,553 edges, **zero mismatches**.

This substantially hardens the internal exclusion. The remaining trust boundary is the mathematical deduction from the project’s assigned-witness/source interface to the fixed common-C/perfect-matching geometry; the code does not independently reconstruct that upstream interface from raw D2C selection.
