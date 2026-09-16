# A shared residual budget for selected-label bundles

16 September 2026. Research directed by Paul Lenz; internal mathematical development by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded mathematical unit following the strategic checkpoint `888e24fe285db0363a2670370e933963f937a02b` in `paullenz/MurtySimon742`. The main result is a parameterized, conditional shared-receiver inequality, with explicit accounting for reuse of residual incidences. It does not assume a five-by-five tight block or an equality value of Omega. A bounded-leakage version is proved, but a theorem deriving the needed bundle structure or leakage bound from arbitrary near-tightness is NOT claimed. All original-graph applications remain conditional on the canonical selected/residual bridge. External review and literature-novelty assessment remain OPEN. No catalogue replay or promotion.

## 1. Canonical facts used, and notation

Use the full canonical representative system of a diameter-two edge-critical graph G. Let J be its complement, A the neighbourhood of a minimum-degree pivot in J, B the remaining vertices, a=|A|, b=|B|, F=complement(J[A]), and Delta_F(i)=deg_F(i). Write

    N_u = S_u disjoint-union R_u,   rho_u=|R_u|,
    R_i = number of B-vertices carrying label i residually,
    x_i = number selecting i,       s_i=max(0,Delta_F(i)-R_i).

R_i is a number at a label; R_u is a set at a source. Different selected labels at a source have distinct destinations. For an actual selected obligation e=(u,i)->v, the canonical construction supplies

    i not in N_v,   S_u minus {i} subset N_v,
    N_F(i) subset N_u,   x_i>=s_i,
    incoming_degree(v) <= rho_v + k,  k=b-a-1.             (1)

A more informative form of the existing endpoint injection is

    N_F(i) intersect S_u subset R_v.                       (2)

Indeed, a selected j at u with ij in F has a different destination from v, so j is present at v by domination. Both j and v miss A-label i; hence jv cannot itself be a selected cross quasi-edge, and is residual. This is the same injection underlying Delta_F(i)<=rho_u+rho_v, not a newly claimed graph-to-model theorem.

The proof below uses only (1)-(2), residual/selected disjointness, and its explicitly listed bundle hypotheses. The reverse-containment condition of the existing fixed-neighbourhood flow theorem may further restrict destinations; it is not needed for this necessary inequality. The flow theorem itself is not being rediscovered or replaced.

## 2. Bundle hypotheses and explicit leakage allowances

Partition B as H disjoint-union V disjoint-union O, and put h0=|H|. Partition a chosen family of labels L into disjoint bundles L_t, indexed by t in I, with g_t=|L_t|>=2. Assume:

(A) Every label of L is residual at every vertex of H.

(B) For each t there is a set U_t subset V of m_t>=1 distinct monitored sources such that, for every u in U_t,

    S_u intersect L = L_t,    R_u intersect L = empty,
    rho_u <= C_t.                                          (3)

These source sets are automatically disjoint. Every member of L_t is selected at every source of U_t. Other selected labels outside L, other sources, and other obligations are allowed.

(C) No vertex of O selects a label of L. All such labels present at O are therefore residual. There is a common upper bound rho_v<=c for v in O.

(D) Every label in L_t has positive demand at least s_t>=1.

(E) Of the m_t*g_t monitored obligations from U_t labelled by L_t, at most D_t have destinations outside O, where 0<=D_t<=m_t*g_t is a proved integer allowance. D_t is NOT presumed small merely because an unrelated scalar deficit is small.

The closed-bundle case D_t=0 follows without assuming any destinations in advance if, at every v in V, each bundle is either entirely present or entirely absent:

    N_v intersect L_t belongs to {empty,L_t}.              (4)

A destination for label i in L_t cannot be H by (A). It cannot be V: if the whole bundle is present it contains i, and if absent it misses a different selected member of L_t. This proves the zero-leakage assertion using (1) and g_t>=2.

One usable way to certify nonzero D_t is to count partially present internal destinations. Let B_t={v in V:0<|N_v intersect L_t|<g_t}. A monitored obligation escaping O must use B_t. Each such receiver can receive at most one label type from that bundle and at most m_t monitored arcs. Thus

    actual_escapes_t <= min(m_t*g_t,
                           sum_(v in B_t) min(m_t,rho_v+k)). (5)

This is valid whenever the canonical capacities are nonnegative. One may set D_t equal to this right side or use any independently proved smaller upper bound on actual_escapes_t. It need not equal the actual escaped count. Simultaneous allowances may overestimate the capacity of shared bad receivers, which weakens rather than strengthens the result. A joint bound on escapes can retain that shared capacity separately.

Define

    eps_t = min(g_t-1, floor(D_t/m_t)),
    theta_t = max(0, h0+s_t-C_t-eps_t).                    (6)

These are parameters, not an assumption of tight demand or equal pool sizes.

## 3. Compulsory residual occurrences: the first cost

**Lemma 1.** Every i in L_t has

    R_i >= h0 + g_t-1-eps_t.                              (7)

**Proof.** A receiver in O cannot receive two different label types i,j of L_t: the arc labelled i requires j present, whereas the arc labelled j requires j absent. It may receive several monitored arcs with the SAME label, from at most m_t different sources.

At most floor(D_t/m_t) label types can have ALL their m_t monitored obligations escape O. For any fixed i, at least g_t-1-eps_t other label types have an O-destination. Choose one such destination per type. They are distinct by the preceding observation; each contains i by forward containment, residually by (C). They are outside H, whose h0 occurrences are already residual by (A). This proves (7).

This does not multiply the residual cost by m_t: several sources can reuse one receiver for the same label. Nor are destinations of different bundles assumed distinct.

## 4. Residual cost at a shared receiver: the second cost

For v in O let I_v be the set of bundle indices having a monitored obligation assigned to v. Then

    rho_v >= sum_(t in I_v)(g_t-1) + max_(t in I_v)theta_t, (8)

with the maximum and sum zero for an unused receiver. Also, its number l_v of monitored incoming arcs satisfies

    l_v <= min(rho_v+k, sum_(t in I_v)m_t).                (9)

**Proof of (8).** For each t in I_v, at most one label type i_t can arrive from L_t. Every other label in that bundle is present residually at v by (1) and (C). The bundles are disjoint, so these force sum(g_t-1) distinct L-residual incidences.

Consider one arriving (u,i) from bundle t. By (3) and A-side domination, i has no F-neighbour in any other bundle. Among N_F(i) intersect S_u, at most g_t-1 labels are in L. As at most rho_u<=C_t neighbours of i are residual at u, (2) forces at least

    max(0, Delta_F(i)-C_t-(g_t-1))

residual labels OUTSIDE L at v. Positive demand is important: by (D), Delta_F(i)=R_i+s_i, so (7) makes this lower bound at least theta_t. Residual labels outside L might be the SAME for obligations from different bundles. We therefore take their MAXIMUM, not their sum. They are disjoint from the already counted L-incidences. This proves (8).

For (9), only one label type per bundle may arrive, with at most m_t monitored occurrences of it. The canonical incoming capacity is shared by all obligations, and hence bounds the monitored subset as well.

These two lemmas provide the incidence-reuse accounting. Forced mates from different bundles have distinct labels; repeated obligations with the same label may share them; external residual labels may be shared and are counted only by a maximum; each receiver's total capacity is used once.

## 5. A shared-budget inequality and checkable scalar certificates

For integer r>=0 define F_D(r) by

    F_D(r) = max min(max(0,r+k), sum_(t in Z)m_t),          (10)

where the maximum ranges over subsets Z of I satisfying

    sum_(t in Z)(g_t-1) + max_(t in Z)theta_t <= r.        (11)

The empty subset has value zero. Clipping r+k at zero just permits a harmless relaxed definition on impossible negative-capacity parameters. In a canonical configuration actual incoming capacities are nonnegative.

Set Q=sum_t m_t*g_t and D=sum_t D_t. Every actual routing satisfies

    Q-D <= sum_(v in O) F_D(rho_v).                       (12)

Indeed at least Q-D monitored obligations end in O. At each v, its actual set I_v satisfies (11) by (8), and (9) gives l_v<=F_D(rho_v). Sum over distinct receivers ONCE. Formula (12) is necessary, not a characterization of original graph realization or even of all compatible arc assignments.

The same assertion can be applied to any chosen subfamily of bundles. Do not add different subfamily inequalities as though their receiver costs were disjoint.

Assume now 1<=rho_v<=c for v in O, as supplied by positive-surplus canonical residual activity. If rational A0>0 and B0>=0 satisfy

    F_D(r) <= A0*(r-1)+B0 for r=1,...,c,

then a finite, checkable joint certificate is

    sum_(v in O)(rho_v-1) >= (Q-D-B0*|O|)/A0.             (13)

Integer rounding may strengthen this. If F_D(1)=0, one valid choice is B0=0 and A0=max_(2<=r<=c)F_D(r)/(r-1), when this maximum is positive. If F_D is identically zero, (12) directly excludes Q>D. If F_D(1)>0, a zero-intercept excess certificate cannot be asserted: cost-free residual-degree-one receivers must remain in the bound. One can instead retain B0, use total residual cost, or an integer resource-cover calculation.

The linear-price step in (13) is elementary summation/weak duality, not a novelty claim for flow duality. The new content of this unit is the graph-specific cost envelope (7)-(11) and its controlled-leakage derivation. This theorem is not simply the existing fixed-cross-set Hall test: it gives a necessary cost inequality before specifying full cross-neighbourhoods of the receivers.

## 6. Test on the Omega=34 pattern, without claiming global applicability

Only in this section specialize to the endpoint-cap proof's d=5 equality pattern. That proof establishes

    h=2, L_profile=0, eta=24, kappa=11,
    one common K-label and ten one-hole K-labels,
    two one-hole labels per full pool V_t, |V_t|=2,
    complete F[T], beta_t=0, demand two on each one-hole label.

L in the general theorem now denotes the TEN one-hole labels, not the common K-label; it is not the scalar L_profile. There are five bundles, each a pair. Take H to be the five high sources, V the ten full-profile sources, and O the remaining low sources.

Verify the bundle hypotheses rather than assume them. L is residual at H. A one-hole label missing t can be selected only in V_t, and demand two forces both its members to select it. The residual sets in V are entirely tight labels, so each bundle has all-or-none presence there and each source selects exactly its own pair from L. beta=0 means O contains no tight labels. Every one-hole label has four tight F-neighbours, so no O-vertex can select one. Thus

    h0=5, g_t=2, m_t=2, s_t=2, C_t=4, c=4, D_t=0,
    theta_t=3, Q=20.                                    (14)

Positive surplus gives k=b-a-1>=1 and rho_v>=1. Equations (10)-(11) yield

    F_D(1)=F_D(2)=F_D(3)=0, F_D(4)=2.                    (15)

A receiver needs one mate label plus at least three residual labels outside L. It therefore has degree four and can serve only ONE bundle. The two monitored sources of that bundle may share it for the same outgoing label, but its two different labels require distinct destinations.

From (12), at least ten different O-vertices have residual degree four, giving

    sigma_O=sum_(v in O)(rho_v-1) >= 30.                 (16)

This is a JOINT residual cost, not twenty separate costs of three. The latter incorrect sum would give sixty by charging the same receiver twice.

Retain the exact identity from the predecessor:

    4a+5-b-2tau = 70+Omega+alpha+sigma_H+sigma_O.

At Omega=34, (16) gives a branch-specific right side at least 134:

    Omega=34 ==> 4a+5>=b+2tau+134.                       (17)

For tau>=1 and b>=a+2 this branch requires a>=45. That is ONLY the Omega=34 branch; it is NOT a new universal a>=45 condition for extras.

Because Omega>=34 was already proved, integrality and nonnegative slack also give the modest global corollary

    Omega+alpha+sigma_H+sigma_O >=35,
    4a+5>=b+2tau+105,
    a>=ceil((102+2tau)/3) for extras.                    (18)

At tau=1 this still rounds to a>=35, so the simplified previous threshold DOES NOT change. The substantive advance is the shared-budget theorem and the quantified penalty hidden in the former minimizing branch, not another claimed one-unit improvement in that threshold. Equation (17) does not by itself prove that the equality pattern is impossible for every a.

## 7. What the leakage version really supplies

The theorem permits varying group sizes, pool sizes, positive demands, source ceilings and nonzero certified D_t. It does not require exact tightness, beta=0, or zero demand deficit as global hypotheses. Those facts were used only to verify its hypotheses for the chosen control pattern.

For a concrete arithmetic stability test, keep the parameters in (14), but suppose all bundle hypotheses other than internal all-or-none presence hold and at most ONE of the twenty monitored arcs can escape O. Some single bundle then has allowance one and the others zero. As m_t=2, every eps_t is still zero, so (15) remains unchanged. At least nineteen arcs end in O. At most two can use one receiver, so at least ten degree-four receivers are still necessary, and sigma_O>=30 still follows. Formula (13) alone would give the weaker rounded bound 29; the stronger value 30 uses the discrete receiver count in (15).

This is a conditional robustness statement, not proof that one missing selected incidence in an arbitrary graph causes at most one escaping arc. Such a conversion still needs a theorem. Formula (5) is one explicitly justified way to turn measured partial internal presence into leakage allowances. Missing selections at monitored sources themselves require choosing intact source subsets or a separate extension; they are not silently covered.

## 8. Checks, controls and preserved boundaries

Run `python3 check_budget.py` beside `verify_budget.cpp`. Python uses bundle-subset maximization for (10); C++ independently enumerates integer incoming allocations per group. Exact full cost lists are compared, not only sample minima or aggregate fingerprints. Domain: one to three bundles, each (g,m,theta) in {2,3} x {1,2} x {0,1,2,3}; k in {-1,0,2}; r=1,...,6. There are 78,624 cost entries. The source order completely specifies the domain; exact output is stored in compressed form with its decompressed SHA256.

Further checks enumerate 78,076 small monitored-arc assignments including explicit escape symbols; 2,306 pass the necessary within-bundle label-type compatibility filter and all satisfy the compulsory-mate bound. There are 75,894 local finite set tests of the disjoint-mate plus maximum-external-union calculation, and 14,256 scalar checks of the positive-demand endpoint estimate. The Omega control and one-leakage variant are checked by exact integer resource-cover dynamic programming. Negative controls preserve source-sharing, overlap of external labels, positive-demand necessity, the no-selected-L-at-O assumption, free degree-one receivers, and the limits of the leakage claim.

These are tests of auxiliary incidence/receiver models and arithmetic. They do NOT enumerate original diameter-two edge-critical graphs, validate the inherited canonical bridge, perform catalogue replay, establish sharpness, or constitute independent expert acceptance. Both implementations are by the same assistant. A resource-only witness at cost thirty is a witness for the relaxed accounting model, NOT a full graph or full canonical routing.

## 9. Dependencies, preservation and next question

All repository dependencies were read at predecessor `888e24fe285db0363a2670370e933963f937a02b`:

- CURRENT_STATE.md, blob b97a218245fe77e6dcc6461fda394cebd0c2d7a8, read first and archived unchanged.
- AGENTS.md, blob 9c5a6f2ac1e36ddc7416a57b6fcc2287600af2c8.
- `2026-09-16-residual-endpoint-cap-v1/PROOF.md`, blob 9ca15674830462a1ae28fd3acf55dd824a41900f, Sections 2-6: endpoint injection, equality structure and exact budget.
- `2026-09-12-arc-realisation-pilot-v1/FIXED_NEIGHBOURHOOD_FLOW.md`, blob 8c0cb53a435227153198b73b313b2332d9403d1e: labelled compatibility, receiver capacities and scope limits.

External primary-source orientation for standard capacity pricing: MIT 6.854, Lecture Notes on duality, https://courses.csail.mit.edu/6.854/16/Notes/n12-duality.html. No external theorem is needed for the elementary proof here, and no novelty comparison beyond this limited orientation is asserted.

Canonical ledger unchanged: 4,626 exclusions / 952 survivors / 3,632 whole-state closures. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration remains unresolved. No original equality replay or remote CI result is claimed.

**Next bounded task:** turn a measured incidence/profile defect into a bound on the escaping monitored arcs while retaining the *shared* capacities of bad internal destinations. Start with intact source subsets and partial bundle presence as in (5); either prove a bound depending on an explicit defect measure or give a small necessary-condition countermodel demonstrating amplification. Do not equate an arbitrary omission count with D_t. Keep the joint Omega-plus-slack objective and true counterexample surplus margin visible; do not revert automatically to the next isolated equality integer. A catalogue coverage census is still a separate unperformed task.
