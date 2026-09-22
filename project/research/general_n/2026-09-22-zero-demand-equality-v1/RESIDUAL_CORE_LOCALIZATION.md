# Residual core localization: three columns and the r=5 strict-surplus obstruction

22 September 2026. Internal candidate mathematics. Maximum-degree root and legal selected assignment are mandatory. Dependencies: INDEPENDENT_RESIDUAL_SUPPORT.md, UNIT_RESIDUAL_COLUMNS.md, ZERO_DEMAND_EQUALITY.md and the raw bridge. No external theorem or full-strip proof is claimed.

## Exact positive-core ledger

Let C={i:R_i>0}, T=A minus C, P={c in C:d_c>R_c}, N=C minus P, and h_c=R_c-d_c for c in N. Let e(P), e(N), e(P,N) count edges of the actual F-core. The boundary lemma gives no F-edge from P to T. Consequently
t=f-r=e(P)-e(N)-sum_{c in P}R_c-sum_{c in N}h_c.
Indeed sum_P d_c=2e(P)+e(P,N), while the previous ledger subtracts all e(F[C]). This identity uses physical graph neighborhoods, not an abstract feasibility assertion.

If P is empty, t<=0; equality would force an independent F[C] and zero slack, excluded by the independent-support theorem when r>0. If 1<=|P|<=2, t<=choose(|P|,2)-|P|<0.

## At most three residual labels

If 1<=|C|<=3 then f<r. The only case not already strict above has |P|=3. Then C=P, and t<=3-3=0. Equality requires F[C]=K3 and all R_c=1, which the unit-column theorem excludes. Thus any nonbipartite graph at or above the target density must have at least four residual-support labels.

## Residual mass five: no strict product surplus

The partitions of five with <=3 parts are closed strictly by the preceding theorem. The all-unit partition is closed strictly by the unit-column theorem. Only (2,1,1,1) remains.

Suppose this partition has t>0. The ledger forces |P|=4: with |P|<=3 it gives t<=0. Thus C=P, no vertex of C has a T-neighbor, T is independent, and every F-edge lies in C. Since f>r=5 on four vertices, F[C]=K4 and f=6.

For a unit-residual label i, d_i=3 and x_i>=d_i-R_i=2. Thus the three unit labels have at least six selected incidences in total.

Let u be any B-source selected at a unit label i. Since F[C]=K4, the bridge makes u miss all four C-labels. Also u can be selected at at most one other C-label: selected F-neighbors at a selected label i inject into its residual column of size R_i=1. Therefore this source supplies at most two selected incidences among the unit labels, and has at least two residual crosspairs among C. Six unit-label selected incidences require at least three distinct sources, hence at least six residual crosspairs. This contradicts r=5.

Therefore r=5 implies f<=r. Unlike r<=4, equality f=r is NOT excluded by this argument.

## Consequences, with equality scope kept separate

Together with the earlier results:
- 1<=r<=4 implies f<r.
- r=5 implies f<=r.
- Every strict Murty-Simon counterexample requires r>=6.
- Writing D=floor(n^2/4)-b(n-b) and epsilon=m-floor(n^2/4), a strict counterexample has S>=r+2(D+epsilon)>=8+2D.
- Therefore S<=7 implies the edge bound. The balanced complete-bipartite equality characterization is proved here only for S<=4 (and the other separately proved support classes), not for all S<=7.

This is a bounded-demand improvement, not a proof throughout the live maximum-degree strip.

## Explicit unfinished equality configurations

For the remaining r=5 vector (2,1,1,1), t=0 can survive the core ledger. If |P|=3, P consists of the unit labels and induces a triangle; the heavy residual label has d=R=2, with zero, one or two neighbors in that triangle and its other neighbors in T. If |P|=4, the core is K4 minus a unit-unit edge with the heavy label of degree three. These are necessary actual-core shapes, not constructed D2C graphs. Their cross-source and deletion-witness compatibility remains to be tested.

Next: attack these equality core shapes using actual criticality and residual-source identities, preserving the balanced bipartite controls.
