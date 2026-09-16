# Individual pool prices: an improved small-block bound and a surviving two-hole obstruction

16 September 2026. Research directed by Paul Lenz; internal mathematical development and checks by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded continuation from `afeb6ac3f573f8525bde05083689c4efabf1a4f5` in `paullenz/MurtySimon742`. The results below are conditional on the full canonical selected/residual bridge and its exact tight-block hypotheses. No catalogue replay, new state exclusion, promotion, original-graph realization, sharpness or literature-novelty claim is made. Independent expert review remains OPEN.

## 1. Outcome and limits

Retaining individual pool prices eliminates the targeted d=5,z=2 scalar minimizer `(h,L,n0,n1,n2)=(4,2,1,12,0)` at cost 30: it actually incurs at least 16 further demand-deficit units, so its row-priced cost is at least 46.

However, the other old minimizer `(6,0,0,0,15)` survives. An explicit binary T-K interface attains the strengthened row relaxation at cost 30. Thus the d=5 global necessary threshold for extras remains a>=33, NOT a larger value. Eliminating one optimizer is not a proof that the optimal value increases.

There is a smaller genuine improvement: for d=4,z=2 the row-relaxation minimum is 19 rather than 17, improving the necessary threshold for extras from a>=29 to a>=30 when tau>=1. These bounds use all inherited hypotheses; E=0 is rigidity, not automatic whole-state exclusion.

The refinement keeps individual one-hole prices and necessary consequences of the exact row equations. It still relaxes the distribution and selection of labels with at least two holes. It is not a complete realization model for those rows or for original graphs.

## 2. Setup and inherited facts

Let G be a finite simple diameter-two edge-critical graph, J its complement, v a minimum-degree pivot in J, A=N_J(v), B=V(J) minus N_J[v], a=|A|, b=|B|=Delta(G), and F=complement(J[A]). At an A-label i write delta_i=deg_F(i), residual B-degree R_i, selected degree x_i, and demand s_i=max(0,delta_i-R_i). At a B-source u write N_u=S_u disjoint-union R_u, with rho_u=|R_u|. The scalar R_i and set R_u are distinct objects. The full representative system supplies x_i>=s_i, selected incidence implies s_i<=rho_u, and A-side domination N_F(i) subset N_u. Let r=sum_i R_i=sum_u rho_u and tau=e(F)-r=e(G)-b(a+1).

Assume tau>0, d>=3, T={i:s_i=d}, H={u:rho_u>=d}, and |T|=|H|=d. T is the entire demand-d level. The inherited bridge and tight-destination facts imply: all tight labels are selected at every high source and nowhere else; no demand exceeds d; K=N_F(T) minus T is residual at each high source. Write kappa=|K|.

Use full profile pools V_t={u outside H:R_u=T minus {t}}, p_t=|V_t|, m=sum p_t. These include, but need not equal, the used tight receiver pools. Choose a common integer lower bound z>=1 with p_t>=z. The inherited disjoint-destination argument permits z=2 when extras E>0, and z=1 is always available.

Put kappa_0=1+z(d-1), h=kappa-kappa_0, p_t=z+u_t, L=sum u_t=m-zd. All are nonnegative integers. With beta_t=R_t-(m-p_t)>=0, missing internal tight degree nu_t, and number q_t of missing T-K edges at t, the predecessor proves the exact row equations

    q_t+nu_t+beta_t = h-L+u_t.                       (R1)

For common K-labels the demand is zero. A one-hole K-label missing t can be selected only at V_t, so its demand is at most min(d-1,p_t). Let n0 be the number of common labels, n_t the number of one-hole labels missing t, and n2 the number with at least two holes. Then, with N=sum n_t,

    n0+N+n2=kappa,
    eta:=sum_{i outside T}(d-1-s_i)
       >= (d-1)n0+sum_t n_t*(d-1-z-u_t)_+.           (R2)

One-hole confinement is not extended without proof to multi-hole labels.

## 3. A finite row-priced relaxation

For fixed d,z, define C(d,z) as the minimum of

    d*h+(d-2)*L+(d-1)*n0+sum_t n_t*g_t,
    g_t=max(0,d-1-z-u_t),                            (R3)

over nonnegative integer h,L,u_t,n0,n_t,n2 satisfying

    sum u_t=L, kappa=kappa_0+h,
    c_t:=h-L+u_t>=0,
    0<=n_t<=c_t,
    n0+sum n_t+n2=kappa,
    sum n_t+2*n2<=d*h-(d-1)*L.                      (R4)

Every actual configuration yields a feasible tuple: n_t<=q_t<=c_t follows from (R1); each multi-hole label consumes at least two missing T-K incidences; sum q_t cannot exceed the sum of the row capacities. The converse is NOT asserted. In particular, (R4) does not require the multi-hole incidences to be assigned consistently across individual rows.

By (R2), every actual configuration satisfies

    d*h+(d-2)*L+eta >= C(d,z).                       (R5)

The search is finite with a proved cutoff, not a heuristic truncation. Set

    h0=ceil(2*kappa_0/(d-2)).

At h=h0,L=0, choose n0=0, every n_t=0, and n2=kappa. This is feasible in (R4), because 2*kappa<=d*h0. Therefore C(d,z)<=d*h0, while h>h0 costs more than d*h0 before any other term. It suffices to search

    0<=h<=h0, 0<=L<=floor(d*h/(d-1)).                (R6)

For fixed h,L,u,n0,N, the best one-hole allocation is especially simple. Make c_t copies of price g_t for each row, sort all copies, and sum the cheapest N. This is the exact minimum under the bounds 0<=n_t<=c_t: replacing a chosen more expensive slot by an unchosen cheaper slot never increases cost. Each c_t may be truncated at kappa, because N<=kappa. A separate bounded-allocation dynamic program checks the same optimum without sorting prices.

Because g_t>=max(0,d-1-z-L), every row tuple maps to a predecessor scalar tuple with no greater coarse cost. Thus C(d,z)>=B(d,z). This is a symbolic comparison of nested necessary-condition relaxations, not a sufficiency claim.

## 4. The targeted d=5 minimizer pays sixteen extra units

Fix d=5,z=2,h=4,L=2,n0=1,N=12,n2=0. Then kappa=13 and the total row capacity is

    sum c_t=5*4-4*2=12.

All twelve one-hole labels must fill those capacities, so n_t=c_t=2+u_t. There are only two pool-distribution types up to permutation:

- u=(2,0,0,0,0): pool sizes and one-hole counts are (4,2,2,2,2), with prices (0,2,2,2,2), giving extra deficit 16.
- u=(1,1,0,0,0): sizes and counts are (3,3,2,2,2), with prices (1,1,2,2,2), giving extra deficit 18.

The common label already costs four deficit units. Hence the total row-priced expression is at least

    5*4+3*2+4+16 = 46,

not 30. All 15 ordered distributions are checked: five have deficit 16 and ten have deficit 18. This is a statement about this fixed type tuple, not a universal replacement of B(5,2) by 46.

## 5. The second minimizer survives the row and interface tests

The freshly replayed predecessor scalar case B(5,2)=30 has exactly two minimizing type tuples:

    (h,L,n0,N,n2)=(4,2,1,12,0), (6,0,0,0,15).

The first is eliminated at cost 30 by Section 4. For the second, take p_t=2 for all five t, kappa=15, h=6, L=0, no common or one-hole labels, and fifteen two-hole labels. Its cost in (R3) is 30, so C(5,2)=30 by the nested lower bound.

This alternative even has an explicit binary interface satisfying the exact tight row equations, not just the aggregate relaxation. Label T by 0,1,2,3,4. Make ten K-labels whose hole pairs are the ten distinct unordered pairs of T. Add five more distinct K-labels with hole pairs

    {0,1}, {1,2}, {2,3}, {3,4}, {0,4}.

Different K-labels may have the same hole pair: the underlying T-K graph is still simple, since they are distinct vertices. Make F[T] complete, and join each K-label to exactly the three tight labels outside its hole pair. Every tight label has six missing K-neighbours. Thus

    q_t=6, nu_t=0, delta_t=4+15-6=13,
    R_t=delta_t-d=8=m-p_t,
    beta_t=0,

for every t. All row capacities are six and all equations (R1) hold. The relaxed penalty is zero because all K-labels are in the multi-hole class.

**This is not an original diameter-two critical graph, or even a complete canonical selected/residual system.** It specifies the interface and formal tight residual totals only. It does not construct the selected destinations, remaining A-side edges, full residual incidences, or positive surplus. Its legitimate role is to prove that individual one-hole row prices and these interface equations alone cannot raise the global d=5 relaxed minimum beyond 30.

## 6. Bounds and checked values

The inherited exact global budget, now using the full profile pools, gives

    a(d-1)+d-b-2*tau
      = z*d*(2d-3)+d*h+(d-2)*L+eta
        +alpha+sigma_H+sigma_O,

where the last three terms are nonnegative under the stated hypotheses. Insert (R5):

    a(d-1)+d >= b+2*tau+z*d*(2d-3)+C(d,z).          (R7)

The b-dependent term uses positive-surplus residual activity; tau=0 is not included automatically. With the canonical maximum-degree bound b>=a+2,

    a>=ceil((z*d*(2d-3)+C(d,z)-d+2+2*tau)/(d-2)).  (R8)

Exact finite minimization for z=2 gives:

| d | Previous B(d,2) | Row-priced C(d,2) | Necessary minimum a for extras, tau>=1 |
|---|---:|---:|---:|
| 3 | 8 | 8 | 27 |
| 4 | 17 | 19 | 30 |
| 5 | 30 | 30 | 33 |
| 6 | 35 | 35 | 36 |
| 7 | 39 | 39 | 38 |
| 8 | 40 | 40 | 41 |
| 9 | 45 | 45 | 45 |
| 10 | 50 | 50 | 48 |

Only the d=4 threshold changes within this tested z=2 range. For d=4 the minima within each h=0..7 slice are 21,20,19,20,22,24,26,28. The unique symmetry-reduced minimizing key is h=2,L=0,u=(0,0,0,0),n0=1,N=8,n2=0, at cost 19. In particular its inequality is 3a+4>=b+2*tau+59, requiring a>=30 when tau>=1. These are conditional necessary thresholds, not existence or sharpness assertions.

For d=5 the h=0..6 slice minima are 36,35,34,33,32,31,30; the only remaining minimizing type is the two-hole case in Section 5. No new catalogue ID is excluded or promoted.

## 7. Executed verification and limitations

Run `python3 check_rows.py` beside `verify_rows.cpp`. Only Python standard-library modules and a C++17 compiler are needed. No external data download is required.

Python enumerates sorted extra-pool vectors, weights each by its exact permutation count, and uses greedy unit-price allocation. C++ independently enumerates ordered pool compositions and solves each allocation by bounded dynamic programming. They agree exactly on all minima, every h-slice minimum, feasible tuple counts and complete symmetry-reduced minimizing keys for 16 parameter pairs (d=3..10,z=1,2), covering 638,396 feasible ordered pool/type tuples.

The counted tuple is (h,L,ordered u,n0,total one-hole count,n2); its allocations n_t are optimized, not individually counted. The stored minimizing keys give these outer variables, not every tied n_t allocation. `ROW_MINIMIZERS.json` preserves the complete comparison output with this meaning.

Additional executed checks cover all 15 targeted distributions, the explicit surviving two-hole interface, a fresh full-composition replay of all 1,457 predecessor d=5,z=2 scalar tuples, and 533 accepted small binary interface/profile cases. `CHECK_RESULTS.json` and the source specify their scope.

Negative controls retain the cheapest-pool underpricing, the surviving second minimizer, the distinction between an interface and an original graph, and the prohibition on applying one-hole prices to multi-hole labels without a new lemma. Both implementations are by the same assistant. This is internal verification of a necessary-condition model, not independent expert review, inherited-bridge validation, catalogue replay or original-graph enumeration.

## 8. Preservation and next bounded question

Sources were read at immutable predecessor `afeb6ac3f573f8525bde05083689c4efabf1a4f5`:

- `project/research/general_n/2026-09-16-weak-label-profile-budget-v1/PROOF.md`, blob `8fcd37e5aac6e9958a8688f1f4ad5037449cbb3c`, especially (P1)-(P13).
- Its locally supplied evidence ZIP, including the predecessor scalar minimizers and source; the d=5 scalar case was freshly checked rather than just copied.
- Live `CURRENT_STATE.md`, blob `01e649ea1bb4a7c659a8090b995dfce510735033`, archived unchanged in this checkpoint; AGENTS.md was read after the live handoff.

Canonical totals stay **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates and 170-candidate audit retain their separate unpromoted statuses. State 3349 enumeration, catalogue application, independent review and earlier unresolved work remain open. Earlier evidence is not rewritten.

**Next bounded mathematical task:** test the full selected-destination obligations of the surviving d=5 two-hole equality pattern. Its tight row equations force p_t=2, q_t=6 and beta_t=0. Determine what equality of the demand-deficit bound forces about selecting sources for each two-hole label, then use destination absence, forward containment and distinct destinations. The displayed interface is only a necessary-condition witness; do not assume it extends to the canonical graph. Preserve the first valid contradiction or surviving full-routing control before broadening the model.
