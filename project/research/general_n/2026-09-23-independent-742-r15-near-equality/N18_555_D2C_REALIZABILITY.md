# n=18 d=x=h=(5,5,5): exact D2C realizability check

Status: internal exact computation, pending independent encoding and reduction audit.

The strengthened abstract survivor uses total deficit 16 exactly:

- three label vertices have deficit 5 and degree 5;
- four common witnesses have deficit 0 and degree 10;
- one common witness has deficit 1 and degree 9;
- all ten remaining vertices have deficit 0 and degree 10.

Because `x=h=5`, all three labels have the same complete missed-witness set T and hence the same five-vertex neighbourhood C. For a fixed witness, any source for one label lies in the common C and is therefore already a common neighbour for each other label-witness pair. Exact uniqueness forces one common source. Source-demand injection within a label makes the five witness sources distinct, hence T-C is a perfect matching.

The script `check_n18_555_d2c_z3.py` fixes these degrees and incidences, leaves every other permitted edge Boolean, and imposes:

1. every nonedge has a common neighbour (diameter at most two);
2. every present edge has an exact deletion certificate: either its endpoints have no common neighbour, or one endpoint has a non-neighbour whose unique common neighbour with it is the other endpoint.

The second condition is an exact local characterization of diameter-two edge-criticality.

Z3 result: **UNSAT**.

Therefore no D2C graph realizes this rigid survivor, conditional on the stated source-interface deduction and correct encoding. Before promotion, independently stage-check satisfiability without criticality and replay any SAT model through a direct graph checker, while retaining UNSAT as internal rather than external verification.
