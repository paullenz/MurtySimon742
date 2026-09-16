# Defect-to-leakage result recovered from the pending evidence package

16 September 2026. Research directed by Paul Lenz; mathematical development by ChatGPT/Geeps.

**Status: RECOVERED_INTERNAL_CONDITIONAL_PROOF_NOT_PROMOTED.** This self-contained preservation transcription records the mathematical content of the completed but unpublished defect-leakage unit. It is not a new theorem or a claim to have freshly executed its tests. The original literal proof, original code, exact costs and cut certificates, proposed handoff and patch remain preserved in `MurtySimon742_Defect_Leakage_2026-09-16.zip`, SHA256 `7efea9bfe160b8a6d560900ec998e6fad46b43beb09da27a00b4c112a3ae1da3`. This file is a recovery transcription, not claimed byte-identical to the original proof. The original attachment is not uploaded by this commit; the companion provenance record says precisely which evidence remains attachment-only. This prevents the research result from remaining absent from the canonical handoff while preserving its original evidence without alteration.

## 1. Setup and scope

Use the full canonical selected/residual construction, or a reduced system satisfying the explicitly used properties. For a B-vertex u, write N_u=S_u disjoint-union R_u, rho_u=|R_u|. For an A-label i, R_i is its residual degree, x_i its selected degree, delta_i=deg_F(i), and s_i=max(0,delta_i-R_i). These scalar and set uses of R are different. A selected obligation (u,i)->v satisfies

    i not in N_v;
    S_u minus {i} subset N_v;
    N_F(i) subset N_u;
    N_F(i) intersect S_u subset R_v;
    x_i>=s_i;
    incoming_degree(v)<=rho_v+k, k=b-a-1.

Different selected labels at a source have distinct destinations. The full fixed-neighbourhood B-routing theorem also requires reverse containment S_v subset N_u. Dropping it in the projection below enlarges the possible internal leakage; the projection is not an exact graph-realization criterion.

Partition B into H,V,O, and a chosen label family L into disjoint bundles L_t, g_t=|L_t|>=2. For each t choose m_t>=1 intact monitored sources U_t subset V such that

    S_u intersect L=L_t, R_u intersect L=empty, rho_u<=C_t.

Every L-label is residual at all h0=|H| support vertices. No O-vertex selects an L-label. Each label in L_t has positive demand at least s_t>=1. Outside residual degrees have a ceiling c; for excess-cost conclusions assume rho_w>=1 on O. These properties are assumptions inherited from the published shared-bundle theorem, not consequences of an arbitrary numerical tightness score.

## 2. Label-specific internal leakage network

For v in V and bundle t put

    e_(v,t)=min(|N_v intersect L_t|,|L_t minus N_v|),
    P=sum_(v,t)e_(v,t).

Disjointness makes P the minimum number of label-presence edits to make each internal bundle all-or-none. It is NOT automatically a selected-incidence or demand deficit.

An intact monitored obligation with i in L_t can terminate at an internal v only if

    N_v intersect L_t=L_t minus {i}.

Indeed destination absence excludes i while the source's remaining selected bundle labels must be present. Each eligible vertex/bundle cell therefore has defect one and identifies one missing label type.

Construct a type node (t,i) of supply m_t and receiver nodes v of capacity c_v=rho_v+k>=0. Join (t,i) to v exactly when the displayed singleton omission holds. Type-to-receiver edge capacity may be Q+1, Q=sum_t m_t*g_t. Each actual escaping assignment gives an integral feasible flow. Identifying different sources of the same label is a relaxation, not permission to assign an individual original source twice.

For a type subset X and its full receiver-neighbour union Gamma(X), the cut bound is

    actual total escapes <= Lambda
       = min_X [sum_(j not in X)m_j + sum_(v in Gamma(X))c_v].

The equality with maximum flow is the usual integer augmenting-path/min-cut fact: after exhaustion, all neighbours of reachable type nodes are reachable, since those edges have capacity greater than total possible flow; the reachable cut attains the displayed form. No novelty is claimed for flow theory.

The same network on every type subfamily gives necessary bounds on simultaneous escapes. In particular a set X of types whose m_j copies ALL escape must obey

    sum_(j in X)m_j <= sum_(v in Gamma(X))c_v

for every subset of X. Different bundles may share internal receivers, and their capacities are never re-spent separately.

A weaker scalar bound is

    Lambda <= sum_v min(c_v,sum_(eligible t at v)m_t)
           <= min(m_max,c_max)*P.

The first inequality uses at most one eligible type per bundle at each vertex. For the second, min(c_v,sum m_t)<=sum min(c_v,m_t); each eligible cell contributes one unit of P and each summand is at most min(m_max,c_max). If V is empty take c_max=0. Partial cells with more than one missing label can increase P without permitting an escape.

This projection is at least as strong as summing the older independent allowances

    sum_t min(g_t*m_t,sum_(v partially present for t)min(m_t,c_v)).

It retains both shared receiver capacity and the single supply m_t for each type, which those separate allowances can spend more than once.

## 3. Specified template defects

Let (S_v^0,R_v^0) be an explicitly specified internal template whose L-neighbourhoods are unions of complete bundles. Then

    P <= sum_v |(N_v intersect L) symmetric-difference (N_v^0 intersect L)|
      <= D_S+D_R,

where D_S,D_R are the selected and residual symmetric-difference incidence counts in L. The first inequality holds because P uses the nearest all-or-none template; the second holds pointwise since changing a union requires changing at least one component.

In the deletion-only case with unchanged residual incidences, this gives P<=deleted selections. Without controlling D_R the same conclusion is invalid: residual additions can create partial presence without selected deletions.

If nominal monitored sources U_t^0 number M_t, discard every source failing the intact full-bundle condition. Each discarded source requires at least one incidence edit, so retained m_t>=max(0,M_t-D_source,t). The theorem uses the actual positive retained count; if none remains the bundle cannot be monitored this way. This discards obligations only from the monitored subproblem, not from the original full representative system. Source ceilings, demand lower bounds and residual support must still hold. The strategy's abstract high-demand omission count does not itself furnish the required template for every internal receiver.

## 4. Feed the actual shared leakage back into outside cost

For the actual internal flow, let x_(t,i) be the number of escaping copies. Define E_t={i:x_(t,i)=m_t}, e_t=|E_t|. They are fully escaped TYPES, not individual arcs, and their simultaneous feasibility is constrained by the shared type cuts above.

If a monitored i in L_t has an O-destination, then i is not fully escaped. Each other type not fully escaped has an O-destination carrying i residually. Different such types within a bundle require distinct receivers: a receiver for type j omits j, whereas one for another type must contain j. These receivers are outside H. Hence

    R_i>=h0+g_t-1-e_t

for an arriving label. For an arbitrary label the precise bound is h0+g_t-1-|E_t minus {i}|, avoiding a negative count when all types escape.

At an O-receiver serving bundle-index set Z the predecessor's endpoint injection yields

    rho_w >= sum_(t in Z)(g_t-1)+max_(t in Z)theta_t,
    theta_t=(h0+s_t-C_t-e_t)_+.

The mate labels of disjoint bundles are distinct. Residual labels outside L forced by different arrivals may coincide, so their count is a MAXIMUM, not a sum. Each receiver takes at most min(rho_w+k,sum_(t in Z)m_t) monitored arrivals. Applying this to the same feasible internal flow gives a joint outside-cost lower bound. Choosing independent worst-case erased sets that violate the shared cuts would lose essential information.

For the five paired bundles, h0=5, m_t=2, s_t=2, C_t=4, outside 1<=rho<=4 and k>=1, with all other hypotheses retained:

* If no type fully escapes, theta_t=3 for every bundle. Each active receiver contains one mate and three non-L residual labels, so has rho=4 and serves one bundle and one type. Ten types require ten such receivers: sigma_O>=30.
* If Lambda<=1, no type can fully escape because it has two copies. The same bound 30 holds.
* If Lambda<=2, at most one type fully escapes. If exactly one does, the other four bundles require eight separate degree-four receivers, cost 24. The remaining type in the damaged bundle has theta=2 and needs a degree-at-least-three receiver, cost at least two. It cannot share with an intact bundle because two distinct mates plus three non-L labels exceed the ceiling four. Thus sigma_O>=26.

One capacity-two internal receiver defective for multiple bundles still absorbs only two arcs TOTAL; it must not be given two independent capacities per bundle. For contrast two separate capacity-two receivers can erase types in different bundles in a resource relaxation. The three unaffected bundles cost 18; the two weakened remaining types can share two mates plus a common two-label non-L reserve, cost three, giving relaxed total 21. This is a resource-only witness, not a canonical routing or graph. No new universal d=5 threshold follows from these parameter-specific comparisons.

## 5. Explicit one-defect/many-escapes control

For m>=2 take A-labels i,j,z1,z2,z3 and B consisting of intact sources u_1,...,u_m, an internal damaged source v, outside o, support h and three auxiliary vertices. Put

    S_(u_l)={i,j}, R_(u_l)={z1,z2,z3};
    S_v={j}, R_v={z1,z2,z3};
    S_o=empty, R_o={i};
    S_h=empty, R_h={i,j};
    S_aux=empty, R_aux={z1} for three auxiliaries.

Let N_F(i)={z1,z2,z3}, N_F(j)={z1,z2}, and no other F-edges. Then a=5,b=m+6,k=m, the demands of i,j are one and other demands zero. Assign u_l->v labelled i; assign all j-incidences from the intact sources and v to o. These assign all selected incidences once and use distinct missing unordered pairs. The original recorded checker verifies destination absence, forward/reverse containment, domination across other missing neighbours, A-side domination, eligibility, endpoint inclusion and inequality, label demands, and source/incoming capacities. The v capacity is m+3; the o capacity is m+1.

The all-or-none internal template adds only the selected i-incidence at v. Removing it gives P=1 and one selected deletion, but m monitored escapes to v. This demonstrates amplification under the reduced assumptions. It does NOT construct an original positive-surplus counterexample: e(F)=5,r=3m+9,tau=-3m-4<0; full original edge-criticality and a routed ideal template are not asserted. Additional positive-surplus constraints could strengthen the conclusion.

## 6. Previously executed evidence and its preservation location

The pending attachment reports Python all-type-cut enumeration and C++ integral augmenting paths agreeing on 159,612 network costs, with both cut certificates checked in each case. Domains are (types,receivers)=(1,1),(2,1),(2,2),(2,3),(3,2),(3,3),(4,2), all binary adjacency patterns, supplies 1 or 2 and capacities 0,1,2. The stored three-byte-per-row table has decompressed SHA256 e39f308864bf7bea5c2fa291a265307fc2820e019d4b28592f57f58904e017a6.

Additional reported checks: 37,440 presence/capacity configurations, of which 12,420 have a strictly stronger joint than separate allowance; 324 template-edit patterns; six exact resource controls with costs 30,30,26,26,26,21; nineteen complete reduced-routing amplification examples m=2..20; five negative controls. Source and exact outputs remain unchanged in the attached original bundle. This recovery commit is not a fresh execution of those checks. Both original implementations are by the same assistant, not independent expert verification. These are not original-graph enumeration, inherited-bridge validation, catalogue replay, or a novelty audit.

The original files and hashes are identified in RECOVERY_RECEIPT.json. Absence of a code or binary file from this recovery directory must not be mistaken for an upload of that file; only this proof transcription, the receipt, handoff, and exact predecessor archive are added remotely. The complete original evidence has a separate durable chat attachment, with its ZIP hash above. Any later full transfer should retain those bytes and not reinterpret historical local checks as fresh CI.

## 7. Dependencies, unchanged status, next task

Dependency: project/research/general_n/2026-09-16-shared-bundle-budget-v1/PROOF.md at 425830b5fc7a4e595235de8fae2b4481de4d6993, plus its explicit endpoint and fixed-neighbourhood dependencies. No inherited proof is promoted by this recovery.

Canonical ledger unchanged: 4,626 exclusions / 952 survivors / 3,632 whole-state closures. The 41 strict/equality certificates remain NOT_PROMOTED, the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED, external expert review OPEN. State 3349 and original equality replay remain unresolved/not rerun respectively. The universal d=5 joint inequality remains 4a+5>=b+2tau+105.

Next bounded unit: internal destinations of escaped obligations must contain their mates. Split those mate incidences into selected and residual ones, charge the residual part in the SAME shared budget, and constrain the selected part by eligibility and endpoint restrictions. Prove incidence-reuse accounting before summing. Determine whether substantial permitted leakage repays its apparent outside saving, or preserve a precise countermodel. Do not assume arbitrary omissions control P or restart isolated Omega case chasing.
