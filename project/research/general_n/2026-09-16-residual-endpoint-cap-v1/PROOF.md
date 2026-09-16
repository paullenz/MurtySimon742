# A residual-endpoint cap strengthens the tight-block budget

16 September 2026. Research directed by Paul Lenz; internal mathematical development and checks by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded mathematical continuation from `9e0c4559d45df0bd033a422bdf18fe0b81078e0b` in `paullenz/MurtySimon742`. The preceding administrative checkpoint had already confirmed publication of the two-hole proof. This unit resumes its two near-equality branches. All graph conclusions are conditional on the full canonical selected/residual construction. Independent expert review remains OPEN. No catalogue replay, new catalogue exclusion, promotion, graph realization, sharpness or literature-novelty claim is made.

## 1. Results and scope

In the exact tight-block setting with `|T|=|H|=d>=2`, let `K=N_F(T) minus T`. The new consequence of the inherited supplement-residual inequality is

    s_k <= d-2 for EVERY k in K.                            (E1)

Here s_k is label demand. A more detailed statement is

    x_k>0 ==> delta_k<=2d-2, while R_k>=d for all k in K.     (E2)

The degree bound is NOT asserted when x_k=0. Zero-demand labels may still be selected; no inference in the opposite direction is made. The local implication (E1) does not require positive surplus or extra selections, once the full tight-block hypotheses are available.

For the previously studied `d=5`, positive-surplus extra-selection branch, this gives the stronger HAND bound

    Omega := 5h+3L+eta >= 34,                              (E3)

rather than the preceding 31. In particular it closes both recorded Omega=31 branches without assuming their beta values vanish or that their tight interface is complete.

The global consequence is

    4a+5 >= b+2*tau+104.                                  (E4)

With the original maximum-degree restriction b>=a+2 when tau>0,

    a >= ceil((101+2*tau)/3).                             (E5)

For positive integer tau, extra selections now require **a>=35**. Thus E=0 through **a=34**, compared with a=33 previously. This is high-source rigidity, NOT automatic whole-state exclusion. The bound is not a realizability assertion at a=35 and does not remove the exact five-by-five tight-block hypotheses. The all-d statement (E1) and the d=5 budget application (E3)-(E5) have different scopes.

This unit identifies a stronger use of an existing bridge lemma. It does not claim the supplement-residual inequality itself as new, or invalidate the earlier, weaker conclusions. The previous interface and row models remain valid as relaxations; they deliberately omitted the constraint now being imposed.

## 2. Canonical notation and inherited graph properties

Let G be a finite simple diameter-two edge-critical graph, J its complement, and v a minimum-degree vertex of J. Set

    A=N_J(v), B=V(J) minus N_J[v],
    a=|A|, b=|B|=Delta(G), F=complement(J[A]).

For each A-label i, delta_i=deg_F(i), R_i is its residual degree into B, x_i its selected degree, and s_i=max(0,delta_i-R_i). At a B-source u, its A-neighbourhood is N_u=S_u disjoint-union R_u, with rho_u=|R_u|. R_i is a number; R_u is a set. Put r=sum_i R_i=sum_u rho_u and tau=e(F)-r=e(G)-b(a+1).

Use the FULL selected representative system: one representative for every missing unordered pair of J[B], distinct destinations for selected labels at a source, and no double orientation. Every selected incidence (u,i)->w is an actual quasi-edge: u and i together dominate all vertices of J except w. In particular it dominates every A-label. The canonical bridge yields

    x_i>=s_i; i in S_u implies s_i<=rho_u;
    N_F(i) subset N_u;
    i not in N_w; S_u minus {i} subset N_w.                (E6)

Define T={i:s_i=d}, H={u:rho_u>=d}, and assume |T|=|H|=d. T is the whole demand-d level. Every tight label must be selected at all d high sources and nowhere else. No label can have demand exceeding d, since it would require more than d distinct eligible sources. Labels outside T have demand at most d-1.

For clarity, K is residual at every high source as follows. A label k in K has a tight F-neighbour; A-side domination for that tight label puts k in N_u at every high u. If high u selected k, its destination w would have to contain all T by forward containment. A low w cannot do this: none of T is selected there and d residual slots would be necessary. A high w already contains k, violating destination absence. Hence k is never selected at H, proving

    K subset R_u for every u in H; R_k>=d.                (E7)

No demand-thinned routing can be substituted for this representative system.

## 3. The endpoint inequality, rederived at the point of use

The canonical bridge Section 6.2 proves, for any selected (u,k)->w,

    delta_k <= rho_u+rho_w.                              (E8)

Here is its residual-incidence injection. Take an F-neighbour j of k. A-side domination puts j in N_u. If j is residual at u, charge it there. Otherwise j is selected at u, say with destination z. This z differs from w, so the quasi-edge for j must dominate w. Since uw is a missing J[B] pair, jw is a J-edge.

The edge jw is residual: its two endpoints both miss the A-label k (jk is absent from J[A], and kw is absent by destination absence). It therefore cannot be a selected quasi-edge whose only exception lies in B. Distinct such j yield distinct residual incidences at w. The source-residual and destination-residual charges are disjoint incidences. This proves (E8), including cases where other residual incidences are unused or the two residual label sets overlap.

Now fix k in K. If x_k=0, x_k>=s_k gives s_k=0. Otherwise choose a selected incidence (u,k)->w. By (E7), u is low. Every high source contains k, so destination absence also forces w to be low. Thus rho_u,rho_w<=d-1, and (E8) gives delta_k<=2d-2. As R_k>=d,

    s_k=max(0,delta_k-R_k)<=d-2  (d>=2),

proving (E1)-(E2).

**Parameterized form.** In any full canonical representative system, suppose a label is residual at r0 specified sources and every other B-vertex has residual degree at most c. If it is selected, both its source and destination lie outside the specified sources, so delta<=2c. Consequently its demand is at most max(0,2c-r0), whether it is selected or not. The tight-block application takes r0=d and c=d-1. This is a conditional corollary of (E8), not a new graph-to-representative theorem.

## 4. Immediate closure of the requested near-equality branches

For d=5, (E1) gives 4-s_k>=1 for every k in K. Therefore

    eta=sum_{i outside T}(4-s_i) >= |K|=9+h.              (E9)

The published handoff restricted Omega=31 to (h,L,eta)=(5,0,6) or (6,0,1). The first would require eta>=14; the second eta>=15. Both contradict (E9).

This argument does not transplant beta=0, complete F[T], or saturated four-source selection from the old equality case. It proves a constraint valid before any of those specializations. The previously excluded Omega=30 pattern also violates (E9); its twin-label routing proof remains preserved as an alternative, more specialized obstruction.

## 5. A stronger hand minimum for all h and L in the d=5 branch

Assume now d=5, tau>0 and E>0. The inherited disjoint-tight-destination argument gives at least two used receivers for each tight label. Use the FULL profile pools

    V_t={low u:R_u=T minus {t}}, p_t=|V_t|=2+u_t,
    V=union_t V_t, m=sum_t p_t=10+L, L=sum_t u_t,
    h=kappa-9, beta_t=R_t-(m-p_t)>=0.

Used receivers may be a strict subset of the full pools. Let q_t count missing T-K incidences at t, nu_t its missing internal tight degree, mu the number of missing edges in F[T], Q=sum_t q_t, and beta=sum_t beta_t. Exact tight-degree accounting gives

    q_t+nu_t+beta_t=h-L+u_t;
    Q+2mu+beta=5h-4L.                                  (E10)

All these variables are nonnegative integers. Write n0 for the number of common K-labels, n_t for labels whose only missing tight neighbour is t, N=sum_t n_t, and n2 for labels missing at least two tight neighbours. Every K-label meets T, so the last class has two to four holes. Then

    kappa=9+h=n0+N+n2;
    N+2n2<=Q<=5h-4L; n_t<=q_t<=h.                       (E11)

Common labels cannot be selected anywhere, and have deficit four. One-hole labels missing t can be selected only at V_t: their other four tight neighbours must all be residual at a low selecting source. Their demands are thus at most min(3,p_t), combining this profile cap with (E1). Two-or-more-hole labels have deficit at least one by (E1). Hence

    eta >=4n0+sum_t max(1,2-u_t)*n_t+n2
         =kappa+3n0+N-W,
    W=sum_{t:u_t>=1} n_t.                               (E12)

This retains the individual pool penalties. Since 2n0+N>=2kappa-Q, and W<=h*#{t:u_t>=1}<=hL,

    eta >=3kappa-Q+n0-W
         >=27-2h+(4-h)L.

Thus

    Omega>=27+3h+(7-h)L.                               (E13)

Two other bounds will be used. First (E9) gives

    Omega>=9+6h+3L.                                    (E14)

Second, the predecessor's hand inequality, derived from the weaker common/one-hole penalties, is

    Omega>=36-h+(11-h)L.                               (E15)

For completeness: eta>=4n0+sum_t(2-u_t)_+ n_t. Replace this by 4kappa-2Q-sum_t min(2,u_t)n_t, using N+2n2<=Q. The final sum is at most hL by n_t<=h and sum u_t=L. Substituting Q<=5h-4L yields eta>=36-6h+(8-h)L, and then (E15).

The new minimum follows with no bounded enumeration or optimization premise:

- For h=0,1,2, (E15) gives Omega>=36-h>=34.
- For 3<=h<=6, (E13) gives Omega>=27+3h>=36, since 7-h is positive.
- For h>=7, (E14) gives Omega>=9+6h>=51.

These cover every nonnegative integer h, proving (E3). In particular Omega=32 and 33 are excluded as well as both Omega=31 branches.

### Equality in the new relaxation is not a graph construction

An actual configuration attaining Omega=34 would have to satisfy h=2,L=0,eta=24. Then kappa=11, p_t=2. From (E11)-(E12), n0>=kappa-Q>=1 and eta>=3kappa-Q+n0>=23+n0. Equality therefore forces

    n0=1, N=10, n2=0, Q=10, mu=beta=0,
    q_t=n_t=2 for each t, and eta=24.                   (E16)

The common label has zero demand; each of the ten one-hole labels has demand two and is selected at both vertices in its single eligible pool. All outside-K contributions to eta vanish. The row relaxation attains 34 at this parameter pattern, but the full destinations and the other nonnegative global slack terms have not been determined here. No attainability or sharpness assertion is made. This is the next structural pattern, not the old fifteen-two-hole pattern.

## 6. Insert the cap into the exact global identity

Let O=B minus (H union V), and define

    alpha=sum_i max(0,R_i-delta_i),
    sigma_H=sum_{u in H}(rho_u-kappa),
    sigma_O=sum_{u in O}(rho_u-1).

These are nonnegative under the stated hypotheses. The sigma_O assertion uses canonical residual activity for tau>0; that is why the b-dependent budget is not automatically extended to tau=0.

The source partition and positive-part demand identity give exactly

    r=5kappa+4m+(b-5-m)+sigma_H+sigma_O,
    sum_i s_i=r+2tau+alpha=4a+5-eta.

Therefore

    4a+5-b-2tau=70+Omega+alpha+sigma_H+sigma_O.           (E17)

Insert Omega>=34 to prove (E4). The original maximum-degree sum gives 2tau<=b(b-a-1), hence b>=a+2 when tau>0. Substitution yields 3a>=101+2tau, proving (E5). For tau>=1, a>=35 is necessary if extras exist.

Only the d=5 numerical budget is updated in this unit. The all-d cap (E1) has not yet been applied to the other d tables or the frozen catalogue. Rigidity E=0 is not automatically exclusion of the whole state, and nothing here proves the unrestricted conjecture.

## 7. Executed checks and their limitations

Run `python3 check_cap.py` beside `verify_cap.cpp` (Python standard library and a C++17 compiler). No downloaded inputs are required.

The Python row checker uses nondecreasing pool vectors, expanded price slots and greedy allocation. C++ enumerates all ordered pool vectors and computes allocations by dynamic programming. They agree on the COMPLETE symmetry-reduced outer cost table: **2,940 rows representing 29,424 ordered pool/type tuples**, including multiplicities. This does not count every internal allocation of one-hole labels. The minima for h=0..6 are **36,35,34,36,39,42,45**; the sole minimizing outer key is (h,L,u0..u4,n0,N,n2)=(2,0,0,0,0,0,0,1,10,0). The search is sufficient for this row minimum because its exhibited cost 34 is less than 5h for all h>=7. The all-h graph bound is the hand proof above, not extrapolation from this finite table.

Further executed Python checks cover **299,332** selected-label scalar arrays (d=2..16), **137,256** local source/destination residual-incidence masks, **1,626** hand-envelope parameter pairs, and **5,832** scalar arrays for the parameterized cap. Six controls preserve the need for residual presence at all high sources, two low endpoints, the conditional degree bound, the unchanged old relaxation, the two rejected near-equality triples, and the lack of an original-graph realization at the new relaxed minimum.

Exact row costs are preserved in domain-indexed form: `EXACT_ROWS.indexed.json` stores the actually compared cost sequence, and `unpack_rows.py` reconstructs the input keys and permutation multiplicities without recomputing costs. It verifies the SHA256 of the complete table. `check_cap.py` independently regenerates `EXACT_ROW_COSTS.json.gz` and the exact results.

Both algorithms are by the same assistant. The scalar and mask tests assume the tested necessary conditions; they do not validate the inherited graph-to-representative bridge or establish graph realizability. No original-graph enumeration, catalogue replay, independent expert acceptance, remote CI result or literature novelty is claimed.

## 8. Dependencies, preservation and next bounded task

Inspected main: `9e0c4559d45df0bd033a422bdf18fe0b81078e0b`. CURRENT_STATE was read first, then AGENTS and the precise sources needed:

- `project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`, Section 6.2 (blob `4b6aa9e69166393d9a75c514f6f384a85c12363f`). The endpoint inequality is rederived in Section 3 above, not merely quoted.
- `project/research/general_n/2026-09-16-two-hole-routing-obstruction-v1/PROOF.md`, especially its full-profile notation, exact row equations, hand bound and global identity (blob `9174b011b7e984db4df79fd52a6462ed907f56ef`).
- Predecessor CURRENT_STATE blob `8a0ea5ff7220253f27a88d3b7d61a3cb05eab0ca`, archived unchanged in this checkpoint. Publication protocol and earlier administrative evidence are untouched.

Canonical totals remain **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration remains unresolved. Original equality replay was not rerun. All previous proofs, weaker models, failed routes and reviewer materials remain preserved.

**Next mathematical task:** quantify the destination/residual cost of the new Omega=34 pattern (E16), retaining alpha, sigma_H and especially sigma_O in (E17). There are two saturated one-hole labels in each full pool and one globally unselected common label. Determine what destinations their selected incidences can use, and prove any unavoidable extra global cost. Do not infer that equality in the row relaxation is realizable, or that excluding only Omega=34 settles all larger-Omega branches. Preserve the first result or counterexample before another unit. Applying (E1) to other d is a separate subsequent task, not an already-completed table update.
