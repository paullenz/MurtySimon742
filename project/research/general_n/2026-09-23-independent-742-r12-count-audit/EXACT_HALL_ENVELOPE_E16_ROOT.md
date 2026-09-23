# Exact Hall envelope of the unique fourth-batch E=16 root

Scope: internal, computer-assisted actual-graph evidence. This is not an external proof and does not promote an abstract profile.

## Graph and independent criticality check

The unique fourth-batch scalar-envelope root with E>=15 is the graph at n=28, seed 370, maximum-degree root 0, with Delta=15. The replay checked diameter two and, independently for every edge, that deleting that edge raises the diameter above two. Thus this unit concerns an actual diameter-two-critical graph.

The maximum-root partition is

- A = {3, 5, 6, 8, 9, 13, 20, 21, 24, 25, 26, 27};
- B = {1, 2, 4, 7, 10, 11, 12, 14, 15, 16, 17, 18, 19, 22, 23}.

The scalar positive-demand-eligible labels are 21, 25 and 26:
- i=21: h=11, |C_i|=6, scalar margin 2|C_i|-h=1;
- i=25: h=11, |C_i|=8, scalar margin 5;
- i=26: h=10, |C_i|=10, scalar margin 10.

Their separate margins sum to E=16, but their certificate-edge sets overlap.

## Exact assignment calculation

Each edge of G[B] can be assigned to at most one eligible label, exactly as required by a legal graph-level certificate choice. Dynamic programming over the eligible-edge choices produced 555 reachable count vectors (x_21,x_25,x_26). For each vector the demand is

S = sum_i max(0, 2x_i-h_i).

The exact maximum is S=10, attained by assigning all ten edges of C_26 to label 26 and assigning no eligible certificate to labels 21 or 25. The scalar E=16 therefore overestimates the exact graph-level envelope by six. This root cannot meet the strict-counterexample requirement S>=15.

Demand-state multiplicities:
- S=0: 216
- S=1: 72
- S=2: 36
- S=3: 42
- S=4: 36
- S=5: 39
- S=6: 35
- S=7: 16
- S=8: 33
- S=9: 3
- S=10: 27

## Collision geometry

The only crossed-supplement collision label pairs are (5,9), (8,9), and (9,21), all on supplement pair {2,10}. Every pair fails PAIR-ELIG. In particular, the root's decisive obstruction is not categorical collision injectivity; it is competition for physical certificate edges among the genuinely eligible labels.

## Trust limit and next reduction

This exact result applies to one actual graph. It suggests replacing the loose scalar sum E with a graph-level subset-union Hall envelope. The next unit must prove that envelope from legal certificate selection and then test it on fresh actual-D2C live-strip roots. No universal theorem is claimed here.
