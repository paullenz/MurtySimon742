# Exact bounded search for the opposite-edge core

21 September 2026. Exact finite result for listed physical code multisets; not an arbitrary-multiplicity theorem.

Normalize the support to {0,1,6,7}, retain C00 and omit C01, and collapse the parity populations to one P0 and one P1. The mandatory minimum physical multiset is

    C00,C10,C11,C20,C21,P0,P1,S0,S1,S6,S7.

An exact SAT encoding leaves every one of the 55 possible A-edges free. It requires diameter at most two in the full graph and, for every present fixed or variable edge, selects a pair that has no path of length at most two after deletion. Hence its models are exactly the D2C graphs on the fixed root/Q3/A-B skeleton and chosen code multiset.

The 20-vertex minimum multiset is UNSAT. Adding one extra S0, S6, C10 or C21 remains UNSAT, as does adding one each of S0 and S6. These are six exact finite exclusions, not evidence that every larger multiplicity is impossible.

The encoder independently returns SAT and an actual graph-level D2C check passes for X3, the 19-vertex five-coordinate parity-plane construction and the 20-vertex six-coordinate construction. No type-pruning relation is used to restrict A-edges.

Reproduce with `PYTHONPATH=/workspace/scratch/a4369cb67676/deps python sat_opposite_edge_core.py`; dependency: python-sat. Full clause/variable counts and exact multisets are recorded in `OPPOSITE_EDGE_CORE_SAT_RESULTS.json`.

The next mathematical task is to extract the physical obstruction and identify which multiplicity must grow in any surviving core.
