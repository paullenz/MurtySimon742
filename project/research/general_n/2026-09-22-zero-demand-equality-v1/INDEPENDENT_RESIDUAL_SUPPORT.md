# Independent residual support and two-column obstruction

22 September 2026. Internal candidate proof, independently derived from raw criticality and the selected-crosspair bridge. No external review or full-strip theorem is claimed. Every statement uses a maximum-degree root and every legal selected-triple assignment. Notation and dependencies: RAW_PROFILE_BRIDGE.md in the sibling raw-profile-bridge package, LOW_RESIDUAL_OBSTRUCTION.md, UNIT_RESIDUAL_COLUMNS.md, and ZERO_DEMAND_EQUALITY.md.

Write C={i in A:R_i>0}, T=A minus C. Let Z_i be the residual B-source set and X_i the selected B-source set; M_i=X_i disjoint-union Z_i is the B-nonneighbor set. Put d_i=deg_F(i), r=sum R_i, f=e(F), t=f-r. The prior edge-charge lemma excludes an F-edge with both ends in T.

## Boundary lemma

If ci is an F-edge with i in T, then X_i=M_i is a subset of Z_c: a selected source at i cannot also be selected at c when R_i=0. The bridge also gives X_c subset M_i. Consequently X_c subset Z_c, so X_c is empty and d_c<=R_c. This is a physical selected/residual exclusion, not a scalar relaxation.

## Theorem: an independent residual support has f<r

Assume r>0 and F[C] has no edges. Then F is bipartite with parts C,T. The boundary lemma gives d_c<=R_c for nonisolated c; the same inequality is trivial for isolated c. Thus f=sum_C d_c<=r.

Suppose equality. Every c has d_c=R_c>0, X_c empty, and M_c=Z_c. The maximum-root degree sum with m=b(n-b) implies b>=a+1. For every F-neighbor i of c, M_i=X_i subset Z_c.

Consider deleting ci. Its endpoints retain a common B-neighbor since b>R_c=d_c<=|T|. Any pair i,j of T-neighbors of c likewise retains a common B-neighbor outside Z_c. For a pair c,d of C-neighbors of i, either another common T-neighbor remains, or i was their only common T-neighbor. In the latter case
R_c+R_d=d_c+d_d=|N_F(c) union N_F(d)|+1<=|T|+1<=a-1<b,
so a common B-neighbor remains outside Z_c union Z_d. These exhaust the A-pairs whose two-path can use ci; root pairs are unaffected. Criticality must therefore be witnessed by a missing crosspair.

A selected missing crosspair has its unique common neighbor in B and cannot be witnessed by ci. Since R_i=0, the witness must be (c,u), u in Z_c, with unique common neighbor i. Distinct edges ci require distinct witnesses at c. Because d_c=R_c, they use all of Z_c bijectively; write u_{c,i} for the witness assigned to ci.

The witness u_{c,i} is adjacent to i and to no other F-neighbor of c. It has no B-neighbor outside Z_c, since all those B-vertices are adjacent to c. Hence, for every neighbor i,
M_i=Z_c minus {u_{c,i}}.
If R_c=1, this makes X_i empty, contradicting x_i>=d_i>=1. If R_c>=2, choose distinct neighbors i,j. The missing crosspair u_{c,j}-i is selected, and its B-supplement must be u_{c,i}: the source has B-neighbors only in Z_c, and i has just this one neighbor there. Conversely u_{c,i}-j must select supplement u_{c,j}. This selects the same unordered B-edge twice, impossible. Equality is excluded and f<=r-1.

The argument permits multiple C-neighbors at a T-label and repeated residual sources across different columns. It does not assume disjoint Z_c.

## Corollary: at most two residual labels

For 1<=|C|<=2, f<=r-1. The independent-core case is above. Otherwise C={p,q} and pq is an F-edge. A center with a T-neighbor obeys d_c<=R_c by the boundary lemma; one without a T-neighbor has d_c=1<=R_c. Therefore f=d_p+d_q-1<=r-1.

## Corollary: residual mass and demand through four

The prior unit-column proof closes all-unit residual vectors. Prior small-partition arguments close r<=3 and, at r=4, all partitions except (2,2). The two-column corollary closes (2,2). Thus 1<=r<=4 implies f<=r-1.

Let D=floor(n^2/4)-b(n-b)>=0 and epsilon=m-floor(n^2/4). Since S>=r+2t and t=D+epsilon, any non-bipartite equality case or strict counterexample must have r>=5 and S>=5+2D+2epsilon. In particular S<=4 implies the Murty-Simon bound, with equality only for balanced complete bipartite graphs (the r=0 case uses zero-demand rigidity). A strict counterexample needs S>=7+2D.

These are bounded-demand and support-structure results only; the remaining positive-demand strip is open.

## Exact core ledger for the next attack

Let h_c=(R_c-d_c)_+ and P={c in C:d_c>R_c}. The boundary lemma implies N_F(P) subset C. Since T is independent,
t = sum_{c in P}(d_c-R_c) - sum_{c in C}h_c - e(F[C]).
This identity localizes possible surplus to residual-support vertices with positive demand and no zero-residual neighbors. It is an exact graph identity, not a realizability sufficiency claim.
