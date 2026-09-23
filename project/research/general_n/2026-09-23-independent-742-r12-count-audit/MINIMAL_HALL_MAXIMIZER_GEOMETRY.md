# Geometry of an inclusion-minimal exact-H maximizer

Let L be inclusion-minimal among subsets attaining the exact Hall envelope
H=2|union_{i in L}C_i|-sum_{i in L}h_i.

For each i in L define its private set
P_i=C_i minus union_{j in L minus {i}}C_j,
and let Q be the union edges belonging to at least two C_i.

Minimality gives
2|P_i|-h_i >= 1
for every i. The private sets are pairwise disjoint, and the union is their disjoint union together with Q. Therefore

H = sum_{i in L}(2|P_i|-h_i) + 2|Q|.

This decomposes any hypothetical H>=15 obstruction into integer private surpluses (at least one per active label) plus twice a shared-edge overlap count. In particular:
- |P_i|>=floor(h_i/2)+1 for every active label;
- sum_i |P_i|<=e(G[B]);
- 2e(G[B])>=sum_i h_i+H, hence an H>=15 obstruction needs 2e(G[B])>=sum_i h_i+15.

For fixed i, each certificate edge in P_i is associated with a distinct missed endpoint t in B and certifies that i and t have a unique common neighbor. Thus every active label needs unique-common-neighbor witnesses on strictly more than half of its missed B-vertices.

## Hostile-root inspection

The twelve highest-H roots from the second fresh batch were reconstructed. Maximum H=10 occurs at n=40, seed 611, root 15. Its minimal maximizing set has two labels with h=14 each, private counts 10 and 8, private surpluses 6 and 2, and one shared union edge; hence H=6+2+2=10.

The decomposition is exact bookkeeping, but the inequalities above do not yet rule out H>=15. The next step is a degree/collision charge on the many distinct unique-common-neighbor witnesses, not another categorical injectivity claim.
