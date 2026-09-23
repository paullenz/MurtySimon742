# n=18, Delta=10: deficit-14 optimizer excluded by nested source geometry

Status: internal graph-level obstruction, conditional on the assigned-witness interface.

Let labels i,j have d=(8,7), x=h=(8,7). In the strict-star deficit-14 optimizer, the right endpoint types give T_j subset T_i, with a unique vertex p in T_i minus T_j. Since x=h, T_i and T_j are the complete missed-B sets, so their B-neighbour sets satisfy

    C_i subset C_j = C_i union {p}.

For any shared witness t in T_j, its assigned i-certificate has source u in C_i and N(i) intersect N(t)={u}. Thus t is adjacent to u. Since u also lies in C_j, the unique-common-neighbour condition for t's assigned j-certificate forces that certificate to use the same source u and forces t nonadjacent to every other vertex of C_j, in particular p.

Therefore p is nonadjacent to all seven vertices of T_j. Also p lies in T_i, so p is nonadjacent to i. Hence p has at least eight nonneighbors among the other 17 vertices, and

    degree(p) <= 17-8 = 9.

But the exact deficit-14 optimizer assigns delta_p=0, requiring degree(p)=Delta=10. Contradiction.

This excludes the deficit-14 optimizer, not every deficit-15/16 realization of the tuple.
