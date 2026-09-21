# Repeated-S7 five-centre family

21 September 2026.  Uniform graph-level theorem.

For every `k>=1`, take the six coordinate vertices, a P1 hub, S0,S1,S2,S4,
and `k` vertices of code S7.  Distinguish one S7 vertex `z0`.  Join the P1 hub
to all coordinates; add S1--S2, S1--S4 and S0--z0; and join every remaining
S7 vertex to both S1 and z0.  There are no other A-edges.

The resulting graph is D2C and has

    n=20+k,
    m=6n-49.

For `k=1` this is the order-21 minimum graph.  Every one of its 77 deletion
witnesses avoids the neighbourhood `N_Q3[7] union {S1,z0}` of a prospective
new S7 vertex.  The five new edges of the first added S7 vertex likewise have
witnesses avoiding that same set.  Further added S7 vertices are false twins,
so induction preserves diameter two and every old and new deletion witness.
The checker records both certificate sets and directly replays `1<=k<=50`.

This family explains the second 83-edge order-22 mechanism and the exact
fixed-population MaxSAT pattern `max e(A)=2k+7` seen through `k=8`.  It gives
`m=89,95,101` at orders 23,24,25, one edge above the improved star-hub family;
the families tie at orders 22 and 26, after which the quadratic parity family
is denser.  The repeated-S7 family is therefore a useful small-order extremal
control, but its edge count is only linear.

No claim is made that `6n-49` is optimal over all five-centre graphs at these
orders.
