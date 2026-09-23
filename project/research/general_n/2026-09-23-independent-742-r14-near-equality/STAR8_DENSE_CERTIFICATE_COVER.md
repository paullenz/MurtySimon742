# Eight-witness dense certificate cover closes the first n=18 tuple

Status: internally verified finite graph-criticality calculation.

The exact seven-witness screen forces any D<=16 realization of d=(8,7), x=h=(8,7) into:

    delta_i=delta_j=7,
    exactly two endpoint-deficit units,
    D=16,
    all other deficits zero.

For the eight-witness label i, |R_i|=h_i-delta_i=1 and therefore |Z_i|=5. Its available star slack is

    sum epsilon_t = 8*7 + sum_{t in T_i} delta_t - 8*3 <= 34.

The general bound sum epsilon_t >= C(8,2)+m, where m is the number of missing T-edges, implies m<=6. Thus it is enough to screen all eight-vertex graphs with at most six missing edges.

Every such graph is obtained by taking one of the 1,044 unlabeled seven-vertex atlas representatives and adjoining an eighth vertex with one of its 2^7 possible neighbourhoods. After density filtering and exact-mask deduplication, 1,264 labeled extensions were tested. For each, an exact weighted set-cover MILP minimized the Z-certificate cost with at most five certificate vertices.

Result:

    minimum star slack = 40
    missing edges at minimum = 6
    certificate cost at minimum = 28

Allowing six certificate vertices gives the same minimum. Since 40>34, the forced D=16 equality case is impossible. Together with the seven-witness reduction, this excludes the full tuple d=(8,7), x=h=(8,7) under D<=16.

This is a tuple exclusion only. The n=18,Delta=10 row search had stopped at this first tuple and must now continue.
