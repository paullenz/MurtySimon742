# A destination obstruction closes the saturated two-hole minimum

16 September 2026. Research directed by Paul Lenz; internal mathematical development and checks by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded continuation from `002713dc090035ec4f01d8eaaf9d27023082bc4d` in `paullenz/MurtySimon742`. This is a conditional hand proof under the full canonical selected/residual bridge and its exact tight-block hypotheses. The finite checks below support the new argument; they are not needed to prove the minimum or to exclude its equality pattern. Independent expert review remains OPEN. No catalogue replay, new catalogue exclusion, promotion, original-graph realization, sharpness, or literature-novelty claim is made.

## 1. Result

For a positive-surplus canonical configuration with exactly five demand-five labels and exactly five high sources, choose z=2 when extra high-source selections E are present. With h, L and eta as defined below, the new conclusion is

    Omega := 5h+3L+eta >= 31.                              (D1)

The preceding row relaxation had minimum 30 and retained a fifteen-label two-hole pattern. This note proves that no pattern attaining that minimum can satisfy the actual selected-destination rules, not merely that the particular displayed interface fails.

The inherited exact budget therefore strengthens to

    4a+5 >= b+2*tau+101.                                  (D2)

Since b is the original graph's maximum degree, tau>0 implies b>=a+2. Thus extras under these hypotheses require

    a >= ceil((98+2*tau)/3).                              (D3)

In particular integer tau>=1 forces **a>=34**: extras are impossible through **a=33**, compared with a=32 previously. This is rigidity, NOT automatic whole-state exclusion. It does not assert realizability at a=34 or remove the exact five-by-five tight-block hypotheses.

The unchanged row relaxation still has C(5,2)=30. We have not changed that numerical claim: (D1) is stronger because it imposes a routing condition absent from that relaxation.

## 2. Setup and exact assumptions

Let G be a finite simple diameter-two edge-critical graph, J its complement, and v a minimum-degree pivot in J. Set A=N_J(v), B=V(J) minus N_J[v], a=|A|, b=|B|=Delta(G), and F=complement(J[A]). At an A-label i write delta_i=deg_F(i), residual B-degree R_i, selected degree x_i, and demand s_i=max(0,delta_i-R_i). At a B-source u, N_u=S_u disjoint-union R_u and rho_u=|R_u|. The scalar R_i at a label and the set R_u at a source are different objects. Put r=sum_i R_i=sum_u rho_u and tau=e(F)-r=e(G)-b(a+1)>0.

Use the FULL selected representative system, with one chosen representative for every missing unordered J[B]-pair. Different selected labels at a source have different destinations and the two orientations of one missing pair cannot both be chosen. The canonical bridge supplies

    x_i>=s_i;  i in S_u implies s_i<=rho_u;
    i in S_u implies N_F(i) subset N_u.

For an actual selected obligation (u,k)->w it supplies

    k not in N_w; S_u minus {k} subset N_w.               (D4)

The first is destination absence. For the second, another selected label j at u has a different destination from w; its quasi-edge must dominate w, and u misses w. Hence j is present at w. No reverse-containment assumption is needed for the NEW contradiction below.

Assume

    T={i:s_i=5}, H={u:rho_u>=5}, |T|=|H|=5.

T is the ENTIRE demand-five level. Every t in T is selected at every high source and nowhere else. No label can have demand exceeding five, because it would need more than five distinct eligible sources, all in H. Thus 0<=s_i<=4 outside T.

Set K=N_F(T) minus T, kappa=|K|. The inherited tight-destination argument gives K subset R_u at every high source. A used receiver of a tight label t has residual set exactly T minus {t}. Define the FULL pools

    V_t={u in B minus H:R_u=T minus {t}},
    p_t=|V_t|, V=union_t V_t, m=sum_t p_t.

They need not be identical to the used receiver pools. In the extra-selection branch E>0 the inherited disjoint-destination lemma gives p_t>=2 for each t. This permits the choice z=2, independent of whether larger common lower bounds are possible.

Put

    p_t=2+u_t, L=sum_t u_t=m-10,
    h=kappa-9,
    beta_t=R_t-(m-p_t)>=0, beta=sum_t beta_t.

All h,L,u_t are nonnegative integers. The beta_t count residual occurrences of tight t OUTSIDE V; high sources select T and therefore carry no tight labels residually.

Let q_t count missing T-K incidences at t, nu_t its missing degree inside F[T], mu the number of missing internal tight edges, and Q=sum_t q_t. Exact degree accounting gives

    q_t+nu_t+beta_t=h-L+u_t,
    2mu+Q+beta=5h-4L.                                   (D5)

## 3. A hand bound replacing the numerical minimum table

Let n0 be the number of K-labels with no missing tight neighbour, n_t the number missing exactly t, N=sum_t n_t, and n2 the number missing at least two tight neighbours. Every K-label meets some tight label; its number of holes is at most four. Then

    n0+N+n2=kappa=9+h,
    N+2n2 <= Q <= 5h-4L.                                (D6)

Common K-labels cannot be selected: at high sources K is residual, and selection at a low source would force five residual tight labels there. Their demand is zero. A one-hole label missing t can be selected only at V_t, so its demand is at most min(4,p_t). Consequently

    eta:=sum_{i outside T}(4-s_i)
       >=4n0+sum_t g_t*n_t, g_t=(2-u_t)_+.              (D7)

Also n_t<=q_t<=h-L+u_t<=h by (D5). Since u_t are integers and nonnegative,

    2-g_t=min(2,u_t),
    sum_t n_t*(2-g_t)<=h*sum_t min(2,u_t)<=hL.           (D8)

Use (D6) to expand the right side of (D7):

    eta >=4kappa-2Q-sum_t(2-g_t)*n_t
        >=4(9+h)-2(5h-4L)-hL
         =36-6h+(8-h)L.

Therefore

    Omega=5h+3L+eta >=36-h+(11-h)L.                     (D9)

This algebraic inequality is valid for every actual configuration with the stated parameters. Its right side becomes less useful for large h; we do not use it there.

If 0<=h<=5, (D9) gives Omega>=36-h>=31. If h>=7, the elementary bound Omega>=5h gives Omega>=35. If h=6, (D9) gives Omega>=30+5L. Thus the ONLY possible way to violate (D1) is

    h=6, L=0, eta=0, Omega=30.                          (D10)

There is no need to assume an independently enumerated minimizer list for this reduction. The numerical row table is freshly checked below as supporting evidence, not as a mathematical premise.

## 4. What equality forces, beyond the displayed interface

Suppose (D10) holds. Then kappa=15 and every full pool has p_t=2. Since eta=0 is a sum of nonnegative terms, every label outside T, in particular every K-label, has demand four.

At L=0 all u_t=0 and g_t=2. Equation (D7) then forces n0=N=0, so all fifteen K-labels have at least two holes. By (D5)-(D6),

    30<=Q<=30.

It follows that every K-label has EXACTLY two holes and mu=beta=0. Thus F[T] is complete, each beta_t=0, and the individual row equations give

    q_t=6, R_t=8, p_t=2 for every t in T.               (D11)

These conclusions hold for every hypothetical equality configuration, not just the earlier ten-pairs-plus-five-cycle example.

**No low source outside V contains any tight label.** Indeed beta_t=0 means all residual occurrences of t are in V. No low source selects t. Hence t is absent from the whole A-neighbourhood of every source in B minus (H union V).

## 5. Two-hole labels are selected at every eligible pool source

Write P_k={s,t} for the two tight labels missed by k in K. Its F-neighbours in T are exactly T minus P_k, a set of three labels. Any source selecting k must have residual degree at least s_k=4. It is not high, because K is residual at H. It is therefore low with rho=4, and A-side domination forces those three tight labels into its residual set.

By beta=0, that selecting source cannot lie outside V. At a source in V_r the tight A-neighbourhood is exactly T minus {r}, so selection of k is possible only for r in P_k. Thus the eligible selecting sources are contained in

    V_s union V_t,

which has exactly four vertices. As x_k>=s_k=4, all four MUST select k. At any other V_r, k is neither selectable by A-side domination nor residual, because the residual set is entirely in T. Therefore

    k in N_w, for w in V_r, iff r in P_k,
    and every such occurrence is selected.              (D12)

Every source in V_t consequently selects exactly q_t=6 K-labels, namely those whose hole pair contains t. Labels outside T union K may also be selected; ignoring them only weakens forward containment.

Let O=B minus (H union V). No source in O can select ANY K-label: every such label has three tight F-neighbours, while an O-source contains no tight label. Hence all K-labels present at O are residual, and

    |N_w intersect K|<=rho_w<=4 for w in O.              (D13)

We did not assume sigma_O=0, alpha=0 or sigma_H=0. In particular (D13) uses only the definition of low sources and the forced beta=0, not equality in the global residual budget.

## 6. Twin-label destination obstruction

The following elementary local statement isolates the routing mechanism.

**Lemma.** Partition possible destinations into H,V,O. Suppose label k is present at every H-vertex; labels k and j have identical presence at every V-vertex; and each O-vertex contains at most c labels of a set K. If a source selects both k,j in K and at least c+2 K-labels in total, its selected obligation for k has no destination satisfying (D4).

**Proof.** H is excluded because it contains k. V is excluded because forward containment requires j present whereas destination absence requires k absent. At O, forward containment requires at least c+1 other selected K-labels, exceeding its capacity c. These three cases exhaust destinations. This lemma is a necessary-condition obstruction, not a characterization of allowable routings.

Apply the lemma with c=4. Choose any t and any source u in V_t. Its six selected K-labels have hole pairs {t,s}, with only four possible other endpoints s. By the pigeonhole principle two distinct labels k,j have the same hole pair. By (D12), their presence is identical at EVERY profile destination. By K subset R_w for high w, k is present at every high destination. Equation (D13) supplies c=4 outside H union V. The lemma therefore rules out a destination for k, contradicting the full selected representative system.

Thus (D10) is impossible. Together with Section 3 and integrality, this proves **Omega>=31**, namely (D1). The argument covers every saturated fifteen-two-hole-label interface, without a case enumeration of multigraphs.

## 7. Global budget and actual consequence

Retain the predecessor's definitions

    alpha=sum_i max(0,R_i-delta_i),
    sigma_H=sum_{u in H}(rho_u-kappa),
    sigma_O=sum_{u in O}(rho_u-1).

These are nonnegative under the stated hypotheses; sigma_O uses positive-surplus residual activity. The exact selected/residual budget at d=5,z=2 is

    4a+5-b-2*tau=70+Omega+alpha+sigma_H+sigma_O.           (D14)

Insert (D1) to obtain (D2). The original maximum-degree sum gives 2*tau<=b*(b-a-1), hence b>=a+2 for positive integer tau. Therefore

    3a>=98+2*tau,

which proves (D3). For tau>=1, a>=34 is necessary if extras exist. For example at a=33, (D2) would require 137>=b+2*tau+101>=138, a contradiction.

This does not exclude every d=5 tight block: configurations with E=0 do not automatically have the p_t>=2 premise used here. Nor does it address all graph orders or prove the unrestricted conjecture. No bounds for d other than five or for tau=0 are changed by this note.

## 8. Executed checks, preserved failures and scope

Run `python3 check_routing.py` beside `verify_routing.cpp`. Only Python standard-library modules and a C++17 compiler are required. It writes `CHECK_RESULTS.json` and `EXACT_DECISIONS.json.gz`.

Python enumerates the degree-six hole multigraph by assigning multiplicities subject to remaining degrees. C++ instead chooses the six multiplicities within four tight vertices and solves the four incident to the fifth by the degree equations. They agree on the complete reduced destination-decision lists for **654** interfaces. Tight vertices are distinguished; K-label permutations within a hole-pair type are removed, and repeated hole pairs are allowed. This covers all multisets of fifteen two-hole labels with q_t=6.

Each interface forces sixty selected source/label incidences (ten pool sources, six K-labels each). The tests use only destination absence and forward containment among K-labels, after the symbolic high/off-profile exclusions. In ninety interfaces, fifty-six of the sixty incidences already have no destination; in the other 564, all sixty fail. In total, **38,880 of 39,240** mandatory incidences fail this relaxed destination test, and no interface permits all its mandatory selections to be routed. The predecessor's displayed interface fails for all sixty. No success on an individual incidence is interpreted as a complete routing.

A second comparison freshly checks the d=5,z=2 row relaxation. Python uses sorted pools and greedy price allocation; C++ uses ordered pools and dynamic programming. They agree on **29,424 ordered pool/type tuples**, all h-slice minima [36,35,34,33,32,31,30], and the unique minimizing outer key. Every tuple tested satisfies the new hand inequality (D9). As in the predecessor, this counts outer tuples, not every individual allocation of one-hole labels.

Additional tests cover 990 local residual masks and 83,740 instances of the twin predicate. Four controls record why beta=0, zero demand deficit and the six-selected-label capacity threshold matter. Dropping beta=0 allows local eligible sources outside V; lowering the demand permits otherwise identical hole types to have different selected-source sets; selecting only five K-labels removes the four-slot capacity contradiction. These controls are local necessary-condition examples, not full canonical graphs.

Both implementations are by the same assistant. These are internal finite checks, not independent expert acceptance, original critical-graph enumeration, validation of the inherited bridge, or catalogue replay. The hand proof in Sections 3-7 does not depend on these finite counts. The prior interface remains a valid interface-only control and is not deleted or mislabeled as an original-graph counterexample.

## 9. Dependencies, preservation and next task

Inspected predecessor: `002713dc090035ec4f01d8eaaf9d27023082bc4d`; CURRENT_STATE was read first, then AGENTS and the exact mathematical inputs. Sources:

- `project/research/general_n/2026-09-16-individual-pool-rows-v1/PROOF.md`, blob `97e0ff433ef7e34f5fd7932e5f8361de906de709`; full proof and supplied evidence ZIP read locally. Its exact row model is rechecked, not merely assumed from a summary.
- `project/research/general_n/2026-09-16-weak-label-profile-budget-v1/PROOF.md`, especially the full-profile definitions, beta accounting and budget, as preserved in the supplied proof and preceding immutable repository evidence.
- The inherited canonical bridge and disjoint-tight-destination dependencies remain explicit. This continuation does not claim a fresh external audit of them. The new forward-containment use is rederived in Section 2.
- Predecessor `CURRENT_STATE.md`, blob `c26d7d19b07da0493f48ca72e697eeabba27f48d`, archived unchanged with this checkpoint.

For external terminology only, the quasi-edge/supplement formulation in Lemma 3.1 of arXiv:1610.00360v2 was consulted (https://arxiv.org/html/1610.00360v2). No result from that paper is used to justify the new counting/routing lemma, and this limited check is not a novelty assessment.

Canonical totals remain **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. Catalogue application, state 3349 enumeration and independent review remain open. Original equality replay was not rerun. Earlier proofs, failures, controls, reviewer materials and promotion gates are preserved unchanged.

**Next bounded mathematical task:** analyze the next possible slack Omega=31 without exporting saturation assumptions. The hand inequality restricts it to (h,L,eta)=(5,0,6) or (6,0,1). Determine which demand-deficit or tight-residual deviations in each branch can break the twin-label obstruction, and what they cost. Do not assume beta=0, complete F[T], or full four-source selection in a branch unless its exact accounting proves them. Preserve the first valid contradiction or surviving routing control before starting another unit.
