# Residual-union forcing and mixed internal receiver costs

16 September 2026. Research directed by Paul Lenz; internal mathematical development and checks by ChatGPT/Geeps.

**Status: INTERNAL_CONDITIONAL_HAND_PROOFS_NOT_PROMOTED.** This bounded residual-return unit follows the recovered defect-to-leakage argument. It is not an original-graph realization, an unrestricted Murty–Simon proof, a catalogue replay or a promotion. External expert review and novelty assessment remain OPEN. The set-union statement below is a stronger use of the existing canonical endpoint injection, not a claim that the injection or standard counting principles are new.

## 1. Canonical facts and a stronger endpoint statement

Use the full selected representative system. Let J be the complement of a diameter-two edge-critical graph G, choose a minimum-degree pivot, and use its A/B partition. Put F=complement(J[A]). At B-vertex u write N_u=S_u disjoint-union R_u, with rho_u=|R_u|. For an A-label i, let delta_i=deg_F(i), R_i its total residual degree, x_i its selected degree and s_i=max(0,delta_i-R_i). The scalar R_i and set R_u are different objects.

A selected obligation (u,i)->v has i absent at v, every other selected label of u present at v, and S_v subset N_u. The last condition follows because a selected representative from v cannot have exception u (that would select both orientations of the same missing pair); it must dominate u. Every F-neighbour of i is present at u. Distinct selected labels at u have distinct destinations.

For j in N_F(i) intersect S_u, the distinct-destination property forces j present at v. The cross-edge jv is residual: its endpoints both miss A-label i, so it cannot be a selected quasi-edge whose only exception lies in B. Thus

    N_F(i) intersect S_u subset R_v.

Combining this with N_F(i) subset S_u union R_u proves the SET statement

    N_F(i) subset R_u union R_v,                         (U1)
    delta_i <= |R_u union R_v|
            = rho_u+rho_v-|R_u intersect R_v|.           (U2)

This counts distinct labels, rather than merely summing residual degrees. For example residual sets {0,1,2,3} and {0,1,2,4} have degree sum eight but union size five: they cannot support a selected label of F-degree seven. The older degree-sum inequality remains true but weaker.

If label i has positive demand and is residual at h0 specified support vertices, then

    delta_i=R_i+s_i >= h0+s_i.                           (U3)

Consequently every actual destination must satisfy |R_u union R_v|>=h0+s_i. This condition is necessary, not sufficient for any routing.

## 2. Leakage must pay for residual-profile deviations

Fix any core label set C. By (U2)-(U3),

    |R_v minus C| >= (h0+s_i-|C|-|R_u minus C|)_+.       (U4)

Indeed the union has at most |C| core labels and at most |R_u minus C|+|R_v minus C| other labels. When R_u subset C, the stronger exact form is

    |R_v minus C| >= h0+s_i-|(R_u union R_v) intersect C|.

In particular if h0=|C| and the monitored source residual set stays in C, every receiving vertex needs at least s_i residual labels OUTSIDE C. A receiver whose residual set also stays in C is impossible, regardless of its selected-label presence pattern.

This gives a direct profile-defect restriction on the previous leakage network. An actual monitored obligation node (u,i) may connect to an internal receiver v only if it passes destination absence, companion presence, reverse containment AND the union test (U2). These are necessary filters; imposing them cannot remove an actual canonical assignment. A flow in the resulting internal projection still is not a full original graph.

For a scalar shared certificate, suppose h0+s_i-|C|-|R_u minus C|>=q>=1 for every monitored obligation in question. Let B_C=sum_(v in V)|R_v minus C| and let gamma_max bound the shared incoming capacity of an internal vertex. Every active internal receiver consumes at least q of these residual incidences. Therefore

    internal escapes <= gamma_max * min(|V|,floor(B_C/q)). (U5)

The more informative filtered flow and individual capacities should be retained when available. A receiver serving several obligations pays its outside-C incidences ONCE, not once per arrival. The threshold is a MAXIMUM over its incoming requirements, not their sum. B_C is not automatically the earlier selected omission score, eta, beta, or presence-edit count P. An application must establish the appropriate relation.

## 3. Exact tight blocks: no full-profile destinations for positive labels

Now specialize only this section to T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d. The inherited tight-block argument gives K=N_F(T) minus T residual at all d high sources. Tight labels are selected only at H. All other B-vertices have residual degree at most d-1.

Let V be the FULL collection of low sources with residual set T minus {t} for some t, not merely the used tight receivers. Put O=B minus (H union V).

**No-profile-destination lemma.** If i in K has positive demand and is selected at a source u with R_u subset T, its destination lies in O.

A high destination contains i and is impossible. A destination v in V would have R_u union R_v subset T, hence delta_i<=d by (U2). But R_i>=d and s_i>0 give delta_i>=d+1. This contradiction does not require beta=0, equal pool sizes, all-or-none internal bundle presence or an equality value of Omega.

A one-hole label is a k in K with N_F(k) intersect T=T minus {t}. Any low source selecting k must carry all d-1 of those tight labels residually, so its residual set is exactly T minus {t}. High sources do not select K. Hence every selected one-hole label starts in V, and if its demand is positive its destination lies in O. No O-vertex can select ANY one-hole label, because that would put it in V by the same argument.

Thus in this structural regime partial SELECTED presence in V cannot create leakage: the residual-union condition forbids it before any defect allowance is spent. The earlier amplification countermodel is not contradicted: its common support has size one while its source-residual core has size three, and it is outside this no-profile-destination regime.

## 4. A source-level bundle-size/demand trade-off

Suppose a low source selects g>=1 positive-demand one-hole labels together. They must all omit the same tight label, because its residual set is a single full profile. For any one of them, i, the g-1 companion obligations have distinct destinations in O, by Section 3. Each such destination contains i, and i is residual there because O cannot select one-hole labels. These occurrences are outside the d high support vertices. Therefore

    R_i>=d+g-1.

Both endpoints of i's selected obligation are low. Using the older (or stronger union) endpoint bound delta_i<=2d-2 and positive demand yields

    s_i+g <= d-1.                                      (U6)

This holds for every member of the co-selected positive family. No maximum-size bundle is assumed; selecting additional positive one-hole labels only strengthens the restriction. For d=5, two co-selected labels of demand at least two must both have demand exactly two; three such labels cannot be co-selected. Four positive-demand one-hole labels cannot be co-selected at one source even with demand one.

This is a conditional local inequality. No theorem here forces every counterexample to have this tight block or these one-hole labels.

## 5. The 30-unit control now applies beyond exact equality

Assume the d=5 tight-block setting and five disjoint pairs of one-hole labels, each of demand at least two, with the two members of each pair co-selected at some low source. One intact source per pair suffices for this argument; no assertion that every other source has intact pair selections is needed. Additional monitored copies may reuse a receiver for the same label.

By (U6), such a source cannot select a third member of this positive one-hole family. Its residual labels are tight labels, so its family neighbourhood is exactly its own pair. By Section 3 every representative destination for the ten chosen label types lies in O, where none of those ten labels can be selected. A receiving vertex contains the companion residually. Each label has R_i>=5+1=6, demand at least two, and hence delta_i>=8.

At the chosen source at most four F-neighbours are residual. At most one selected F-neighbour belongs to the ten-label family (the source contains only its own pair). The endpoint injection therefore forces at least 8-4-1=3 residual labels OUTSIDE that family at the destination. Along with its companion, this forces rho_v>=4; as the destination is low, rho_v=4.

One receiver cannot serve both types of one pair, by absence versus companion presence. Nor can it serve different pairs: two distinct family companions plus at least three outside-family residual labels exceed its four slots. The outside-family reserve may be shared, which is why it is counted as three, not six. Thus the ten chosen types require ten distinct degree-four receivers. In positive surplus, other O-vertices have rho>=1, so

    sigma_O=sum_(v in O)(rho_v-1)>=30.                  (U7)

The number is not new; the APPLICABILITY is stronger than the old Omega=34 control. Pool size two, beta=0 and all-or-none presence at unmonitored internal vertices are no longer premises. Intact co-selections, the common tight structure and the positive demand thresholds remain premises. This is not robustness under arbitrary perturbations of residual supports or demands.

For the original motivating family with one such pair for each of the five omitted tight labels, demand two also forces every full pool to have at least two members. In the usual positive-surplus extra-selection setting the inherited Omega>=34 and exact budget remain applicable. Together with (U7) they give

    4a+5>=b+2tau+134

for THIS wider five-pair family, not for every d=5 configuration. With b>=a+2 and tau>=1 this family requires a>=45. The universal d=5 inequality remains 4a+5>=b+2tau+105; no new universal a-threshold or catalogue exclusion is claimed.

## 6. General mixed-return accounting when a common core is unavailable

The following auxiliary theorem was derived before the stronger core restriction was applied. It remains useful outside Section 3's regime and preserves the intermediate attempt rather than disguising it as a graph construction.

Let disjoint bundles L_t have g_t>=2 labels, positive demand at least s_t, common residual support H of size h0, and one intact monitored source u_t with N_(u_t) intersect L=L_t, all these incidences selected, rho_(u_t)<=C_t. Choose the actual destinations v_(t,i) of its g_t selected labels. They are distinct within t. Each lies outside H and outside ALL intact monitored sources: a same-bundle source contains i; a different-bundle source misses its companions.

Write b_(t,i) for the number of companions selected at v_(t,i), and d_(t,i) for the number of OTHER chosen destinations of this bundle at which i is selected. These are row and column sums of a zero-diagonal companion-selection matrix, so sum_i b_(t,i)=sum_i d_(t,i). The destinations of the remaining companions provide residual occurrences, giving

    R_i>=h0+g_t-1-d_(t,i).

If a receiver v serves chosen obligations from bundle-index set Z, reverse containment gives

    S_v intersect L subset intersection_(t in Z)L_t.

Thus a receiver serving two disjoint bundles selects NO monitored-family label. A receiver with selected companions is dedicated to just one bundle. This restriction cannot be omitted.

Let i_t be the type arriving from t at v. Selected companion F-neighbours would be forced residual by the endpoint injection, so at most g_t-1-b_(t,i_t) family companions can be F-neighbours. Positive demand and the source ceiling then force at least

    theta_(t,i_t)=(h0+s_t-C_t-d_(t,i_t)+b_(t,i_t))_+

residual labels outside L at v. Distinct residual companions from disjoint bundles are counted by a sum; outside-family requirements can overlap and are counted by a maximum. Consequently

    rho_v >= sum_(t in Z)(g_t-1-b_(t,i_t))
             +max_(t in Z)theta_(t,i_t).                (M1)

This is a joint receiver inequality coupled through the companion-selection matrices; row and column losses are not chosen independently. No no-selection-on-O assumption is required. Incoming capacities and unused canonical constraints may strengthen it.

### A closed paired-bundle resource bound

For p pairs, take a common A0=h0+s-C>=2 and a receiver ceiling A0+1 outside H. Let lambda in [1,A0+1] be any PROVED lower residual degree at a vertex selecting a family label (demand eligibility supplies lambda=s when applicable). For each chosen type i let b_i in {0,1} record whether its companion is selected at its destination. Its column count is b_(mate(i)).

Let n00,n11,n01 count pairs with respective flags (0,0), (1,1), or one of each. Every type in an 00 pair has a dedicated degree-A0+1 receiver. Each type in an 11 pair has a dedicated receiver of degree at least max(A0,lambda). In a mixed pair, the selected-companion type has a dedicated degree-A0+1 receiver. The other type can share with at most one other mixed residual type; one such receiver costs at least A0-1 excess units, two together at least A0. Merging such receivers saves A0-2>=0. Therefore, for W the DISTINCT chosen destinations,

    sum_(v in W)(rho_v-1)
      >= 2*A0*n00+2*(max(A0,lambda)-1)*n11
         +A0*n01+A0*floor(n01/2)+(A0-1)*(n01 mod 2).    (M2)

These destination classes cannot share a vertex across the counted cases. This is an exact minimum for the displayed RECEIVER-RESOURCE relaxation, not a sufficiency theorem for canonical graphs. The main general claim is the lower bound, whose proof does not rely on the test table.

For A0=3 and ceiling four, (M2) is at least 4p; with the extra independently established floor lambda=4 it is at least ceil(9p/2). For five pairs these give 20 and 23. They charge W, which can include INTERNAL receivers: neither is automatically a sigma_O bound. If all flags vanish, (M2) gives 6p=30. The resource-only 20/23 patterns do not invalidate Section 5: that structural theorem retains residual core identities absent from this weaker model and rules out selected companions altogether.

When residual activity holds globally, H, all intact monitored sources U, and W are disjoint. Hence a safe global conversion is

    r-b >= sum_(v in H)(rho_v-1)+sum_(u in U)(rho_u-1)
           +the right side of (M2).

Remaining nonnegative vertex contributions are discarded once. One must not add the W-bound to an old budget that already included those same internal vertices without subtracting their previous charge.

## 7. Executed tests and negative controls

`python3 check_return.py` compiles the accompanying C++17 checker. Python enumerates actual admissible receiver partitions; C++ uses subset dynamic programming. They agree on all 5,100 ordered parameter/flag rows, representing 12,360 compatible receiver partitions, including each cost, total partition count and optimal partition count. The domain is p=1..4, A0=2..6, lambda in {1,A0,A0+1}, and every binary companion flag pattern. Every computed cost equals (M2). The full compact-JSON table SHA256 is 188005655b37679651e93b3d8d72790ab15a901c84ca654c81bcb42906b01613.

The 510 symmetry-reduced records retain every observed cost/count triple and permit expansion to the full ordered table without solving any new optimization. They are preserved compressed, with a decoder checking the full digest. The local bundle additionally contains the full ordered table.

Other executed Python checks: 4,086 ternary family-neighbourhoods (865 admitting an arrival and 107 multiple bundles), 4,164 companion-selection matrices, and 6,912 positive-demand endpoint arrays. Controls preserve reverse-containment necessity, overlapping bundles, external-reserve reuse, positive-demand necessity, unsupported degree floors, monitored-copy reuse, and the distinction between W and O.

`python3 check_union.py` directly checks 66,429 finite set instances satisfying A-side containment and destination residual forcing. Unlike the earlier vacuous small-graph test, 28,981 have NONEMPTY forced destination residuals; 46,822 have source/destination residual overlap. It also checks 130,944 core-profile threshold arrays, including 24,637 passing the union threshold and 1,920 one-hole selection incompatibility cases. These are finite set/array checks ASSUMING the local premises, not original-graph enumeration or validation of the canonical bridge.

All new tests actually ran locally. Both language implementations were written by the same assistant; no independent expert acceptance or remote CI success is implied. No conjectural graph, full graph realization, catalogue replay, or literature novelty is asserted. Hand arguments establish the general statements; finite tests support the local reductions and bookkeeping.

## 8. Preservation, unchanged status and next mathematical question

The previous published shared-bundle theorem was read at 425830b5fc7a4e595235de8fae2b4481de4d6993. The pending defect-leakage mathematics was then recorded in the recovery checkpoint 456ea04f48411d834cb5a713f84e5db31f7fd4d4, with the complete original ZIP separately identified. Its original programs and exact cut data remain in that attachment, not falsely described as uploaded by the recovery transcription. The present unit publishes its OWN proof, programs and recorded results.

Dependencies are the canonical A-side domination, unique selected representatives, endpoint residual inclusion, reverse containment, and exact-tight-block K-residual/eligibility facts where explicitly specialized. Positive-surplus residual activity is used only in the conversions to full excess budgets. No dependency is promoted here.

Canonical ledger remains 4,626 exclusions / 952 survivors / 3,632 whole-state closures. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. External expert review OPEN. State 3349 and original equality replay remain unresolved/not rerun. No new universal d=5 threshold is claimed.

Next bounded task: incorporate the UNION-filtered, source-specific endpoint restriction into the shared defect/capacity formulation, allowing measured deviations of source residual sets from the common core. Relate the required outside-core receiver incidences to an explicitly shared profile budget; do not assume they equal a selection-omission count. Test a nonzero-profile-defect configuration, not another isolated Omega equality. The mixed-return matrices are a fallback for families without a common-core obstruction. A catalogue hypothesis-coverage census remains a distinct unperformed task.
