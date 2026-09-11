# Audit of the graph-to-certificate implications

**No blocking flaw identified in the reviewed implications. This is internal same-assistant mathematical review, not independent specialist acceptance.**

The proof surface used by this assembly is the [canonical parameterized bridge](../../general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md). The audit followed every implication needed by the N30 supplementary route: Sections 1–9 and 11 of that bridge, the two tail arguments, the profile/row classifications, and the two endpoint certificate arguments. Charging, isolated-C and the general h-index corollary are not required by the new assembly.

## 1. Criticality and selected representatives

For distinct vertices x,y, distance greater than two in G is equivalent to an adjacent total-dominating pair in its complement H: adjacency in H means xy is absent in G, and total domination means there is no vertex adjacent to both x and y in G. Open neighborhoods include both endpoints precisely when the pair is adjacent in H.

Adding a missing B-pair uw changes only the H-neighborhoods of u and w, so any newly total-dominating pair uses at least one endpoint. It cannot be uw itself because both endpoints still miss the root v. An existing pair ui must therefore become total dominating by covering its unique former exception w. Its auxiliary i lies in A to dominate v.

A selected cross-edge uniquely determines its source and its sole undominated B-vertex. It therefore identifies its indexing missing unordered B-pair. Selecting one representative per unordered pair gives an injection and prohibits opposite orientations. At a fixed source both labels and supplements are distinct. These facts are needed later; selecting one edge per orientation instead would invalidate the pair counts.

## 2. Ledger and demand

Selected edges plus H[B]-edges count each unordered B-pair once. Substitution into the complement edge count gives exactly `e(F)=r+t`. Minimum complement degree gives `x_i>=d_i-R_i`; hence `s_i=max(0,d_i-R_i)` satisfies `x_i>=s_i` and `S>=r+2t`.

This uses only the minimum-degree root and simple-graph counting. No stronger isolated-C conclusion is being inserted into the label degree cap: F has a vertices, so the direct bound is `d_i<=a-1`.

## 3. Forced residual edges and positive-surplus activity

For selected `ui->w`, each F-neighbor j of i forces an H-edge uj. If it is residual, it is counted at u. If selected `uj->z`, then z differs from w, `uz` is absent, and `iz` is forced. Both i and z miss the A-vertex j; therefore iz cannot be a selected edge, whose only exception lies in B. Distinct supplements make these forced residual incidences injective. This proves `d_i<=rho_u+R_i` and `s_i<=rho_u`.

The analogous count at supplement w gives `d_i<=rho_u+rho_w`; the assembly does not need that stronger second residual inequality, but its injection has the same valid disjointness mechanism.

For residual activity, suppose some rho_u=0 and partition A into its cross-neighbors U and nonneighbors T. Every u-to-U edge is selected, so an F-edge between U and T would leave an A-vertex undominated, impossible. Each F[U]-edge forces two distinct residual cross-edges with A-endpoints in U. Each F[T]-edge, when added in H, forces a cross quasi-edge with exception in A: the pair cannot use both T-endpoints because they miss u; an A-auxiliary would force a forbidden F-edge between U and T. Its unique exception identifies the original F[T]-edge, so this is injective into residual edges with A-endpoint in T. The two families are disjoint. Thus `r>=2e(F[U])+e(F[T])>=e(F)=r+t`, contradicting t>0.

The proof is universal in a,b and does not assume t is one or two. That is essential for the new Delta=17 transfer.

## 4. Source, supplement and endpoint capacities

Every F-neighbor of label i is an A-neighbor of its selected source u, different from i itself; hence `d_i<=rho_u+q_u-1`. Other selected labels at u force distinct cross-neighbors of the supplement w, giving `rho_w+q_w>=q_u-1`.

The exact degree calculation is

$$
d_H(u)=(\rho_u+q_u)+(b-1-q_u-p_u)=\rho_u+b-1-p_u\ge a.
$$

Thus `p_u<=rho_u+b-a-1`; at a=13,b=16 this is `p<=rho+2`. Together with `q<=a-rho`, it already implies `q+p<=15`. The endpoint box must include the boundary `p=rho+2`. No `rho+1` tightening is valid here.

For a selected ui, label i is adjacent to u, the other outward supplements of u, and all inward sources to u. The two latter families cannot collide because that would select opposite orientations of one unordered pair. Hence `R_i+x_i>=q_u+p_u`.

Individual label and source caps follow from distinct simple-graph incidences and `s_i<=rho_u`: `x_i<=#{rho>=s_i}` and `q_u<=#{s_i<=rho_u}`. These are upper bounds on actual degrees, not assumptions of independent realizability of relaxed vertex states.

## 5. Threshold capacity and the transfer

At threshold h, call selected labels heavy when their demand is at least h. A source with more than h heavy labels has every heavy supplement in Z_h: the other heavy labels force at least h cross-edges at that supplement; either all are residual, or a selected one already forces rho>=h.

For j such sources among z_h vertices, unordered-pair injection bounds their arcs by `j*z_h-j(j+1)/2`. Other sources contribute at most h each. The difference between `h*z_h+C(z_h-h,2)` and that combined bound is `(z_h-h-j)(z_h-h-j-1)/2`, nonnegative for every integer j. This yields the stated capacity without a source-count-specific constant.

Defining the inverse capacity without an upper cutoff therefore preserves the graph implication for any b. A profile whose inverse exceeded b would simply be impossible for an actual graph. Padding at most twelve labels with zeros leaves Q unchanged. The twelve-label hand proof has no step requiring b=16, so it legitimately gives the N30 Delta>=17 exclusion.

## 6. Ledger equality, potentials and signs

If every s_i is positive, its definition already forces `s_i=d_i-R_i`; summing gives `S=r+2t`. If the ledger is tight but a label has s_i=0, equality of `sum max(0,d_i-R_i)` and `sum(d_i-R_i)` forces `d_i=R_i` there too. Thus all tight rows satisfy `d_i=R_i+s_i`, including all four zero-demand m225 rows.

Combining source-degree forcing and endpoint load gives the three coordinate inequalities used by the monotone potentials. Their coordinates are nonnegative on the full local boxes. Every potential coefficient is nonnegative; `s*v`, threshold indicators and rectangles are coordinatewise nondecreasing. Summing incidence inequalities counts each label x_i times and each source q_u times, giving the correct sign.

The four-envelope sum cancels the c and mu terms using `sum x=sum q=sum p`. Nonnegative supplement-tail weights multiply nonpositive H_k. Therefore the summed lower envelopes cannot exceed lambda*r. Strictly positive reported gaps contradict the graph. The independent evaluator matches all 844 gaps, not only the first successful certificate per row.

At m226, the alpha bound is exactly three. The elementary inequality `(s+e)min(e,3)<=(s+3)e` is valid for all nonnegative integer s,e. The source inequalities, after subtracting nonpositive Hall-tail terms, give the required lower bound on `B0-cE`; no sign reversal was found.

## 7. Historical wording clarifications

Two errors in older copies do not change the mathematical implications used here:

1. Section 4.1 of the frozen N29 reviewer-v3 bridge says that j is the unique exception of `uj->z`. The exception is **z**. What is needed is that jz is absent, which follows because z is that exception. Canonical Section 6.1 states this correctly.
2. The frozen N29 bridge and the older `2026-09-11-universal-selected-residual-bridge-v1/UNIVERSAL_BRIDGE.md` omit q_u in an intermediate source-degree display. The correct formula is printed in Section 4 above and canonical Section 7. The already-stated supplement bound remains correct. The earlier [source-degree erratum](../../../reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md) remains applicable.

The m226 endpoint note also describes the positive-demand implication imprecisely using the word “tight”. Positivity alone gives `s_i=d_i-R_i`; no tightness assumption is required to exclude its one positive-slack row. The assembled proof uses the direct implication.

Historical proof sources are left unchanged and hash-accounted in the publication. These are wording/display clarifications, not new missing lemmas or repaired numerical exclusions.

## 8. Limits

No blocking flaw was found in the reviewed chain, but the main risk remains a universal graph argument, not a floating-point calculation. The exhaustive regressions test arithmetic demand vectors, not all thirty-vertex graphs, and do not prove the bridge. Independent specialist scrutiny remains essential. This audit does not certify unrelated earlier discovery models, and no governed theorem-ledger status is promoted.
