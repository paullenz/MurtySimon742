# Assigned-witness source-union endpoint charge

24 September 2026. Status: proved internal graph-level lemma at the assigned-certificate interface. It is a necessary condition, not a complete graph-realizability characterization.

Let v be a maximum-degree root, B=N(v), A=V(G)\(B union {v}), Delta=|B|, a=|A|=n-1-Delta, and rho=2Delta-n. For a label i in A put C_i=N(i) intersect B, so |C_i|=Delta-h_i.

In an assigned-witness graph W*, an incidence i--t comes from a physical B-edge u_i t assigned to i, with i nonadjacent to t and N(i) intersect N(t)={u_i}. For a fixed right endpoint t, let I_t=N_W*(t), r_t=|I_t|, and U_t={u_i:i in I_t}.

## Lemma

The sources in U_t are distinct, each u_i is a private point of C_i within the family {C_j:j in I_t}, and

    delta_t >= |union_{i in I_t} C_i| - a
             >= rho + r_t - min_{i in I_t} h_i.

### Proof

A physical edge is assigned to only one label. At fixed t, the physical edges u_i t belonging to distinct W* incidences are therefore distinct, so their sources u_i are distinct.

For j different from i, t is adjacent to u_i. If u_i also belonged to C_j=N(j) intersect B, then u_i would be a common neighbour of j and t. But their assigned incidence has unique common neighbour u_j, distinct from u_i. Hence u_i is not in C_j.

Moreover, N(t) intersects C_i in exactly {u_i}. Thus within the B-set union C_i, t is adjacent exactly to the r_t private sources and misses every other vertex. It also misses all r_t labels in I_t. These two non-neighbour sets are disjoint, so

    d(t) <= n-1-r_t-(|union C_i|-r_t)
         = n-1-|union C_i|.

Since delta_t=Delta-d(t) and a=n-1-Delta, the first inequality follows. Private sources give

    |union C_i| >= max_i |C_i| + r_t - 1.

Substitute |C_i|=Delta-h_i and Delta-a=rho+1 to obtain the second inequality. QED.

## Additive consequence

Because distinct right endpoints are distinct graph vertices,

    D >= sum_{i in L} delta_i
         + sum_{t:r_t>0} max(0, |union_{i in I_t} C_i|-a).

The profile-only relaxation is obtained by replacing each union term by

    g(I_t)=max(0, rho+r_t-min_{i in I_t} h_i).

Unlike the existing pair inequality delta_i+delta_t>=rho+1, this charge is purely on the endpoint and can be added once per right vertex. It is directly linearizable in the existing right-type witness MILP.

## Regression

The preserved checker exhausted every locally assignable (distinct-source) subset of at most eight labels at every B-endpoint of every maximum-degree root in:

- 570 complete-graph greedy-deletion D2C graphs, orders 8 through 26;
- balanced K_5,5, K_5,6, K_6,6 and K_6,7 controls;
- the published 12-vertex X3 control reconstructed as the Q3-root graph.

All 575 graphs were independently checked edge-by-edge for diameter-two-criticality. Across 921 maximum-degree roots and 15,957 compatible subsets there were zero source-privacy failures and zero charge violations. The source-union floor was strictly stronger than the best pairwise endpoint lower bound in 779 subsets, with maximum gain five. Equality occurred, so no unproved +1 strengthening is available.

The regression supports the proof implementation but is not its basis. The next exact step is to add g(J) to each right-type J in the demand-15/16 necessary-condition MILP.
