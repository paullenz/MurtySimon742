# Weak-label profile caps and the cost of extra sources

16 September 2026. Research directed by Paul Lenz; internal mathematical development and checks by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded mathematical continuation from `31f6c8aca964de0bcaed0cdfe03f14d7abbd7e18` in `paullenz/MurtySimon742`. All conclusions are conditional on the full canonical selected/residual bridge and the exact tight-block assumptions. Independent expert review remains OPEN. No original-graph enumeration, catalogue replay, new catalogue exclusion, promotion, sharpness or literature-novelty claim is made.

## 1. The new source restriction

Keep the predecessor's canonical notation: G is a finite simple diameter-two edge-critical graph; its complement J has a minimum-degree pivot v; A=N_J(v), B=V(J) minus N_J[v], a=|A|, b=|B|=Delta(G), and F=complement(J[A]). For each A-label i, delta_i=deg_F(i), R_i is its total residual degree into B, x_i its selected degree, and s_i=max(0,delta_i-R_i). At a B-source u, N_u=S_u disjoint-union R_u and rho_u=|R_u|. The number R_i and set R_u are different objects. Write r=sum_i R_i=sum_u rho_u and tau=e(F)-r=e(G)-b(a+1).

Assume throughout

    tau>0, d>=3, T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d.

T is the ENTIRE demand-d level. The full canonical selected system, not a demand-thinned routing, gives x_i>=s_i and s_i<=rho_u at every selected incidence (u,i). Thus every t in T is selected at all high sources and nowhere else. No label has demand greater than d, so s_i<=d-1 outside T. A selected label i at u satisfies A-side domination N_F(i) subset N_u.

Put K=N_F(T) minus T, kappa=|K|. The inherited tight-destination argument proves K subset R_u at every high u, and that every receiver of tight label t has residual set exactly T minus {t}. Write U_t for the USED tight receivers for t.

The new step is to distinguish U_t from the FULL residual-profile pool

    V_t={u in B minus H : R_u=T minus {t}},
    p_t=|V_t|, V=union_t V_t, m=sum_t p_t.

The V_t are pairwise disjoint, U_t subset V_t, and V is disjoint from H. There may be sources in V_t not used by any tight obligation. Nothing below identifies these two sets.

Let K_t be the labels k in K with exactly one missing tight F-neighbour, namely

    N_F(k) intersect T = T minus {t}.

Then

    k in K_t ==> every selected source of k belongs to V_t,
    x_k<=p_t, and s_k<=min(d-1,p_t).                    (P1)

**Proof.** No high source selects k, since K is residual there. At a non-high source selecting k, A-side domination forces T minus {t} into its A-neighbourhood. Tight labels cannot be selected at a non-high source; all d-1 are therefore residual. As rho_u<d, its residual set is exactly T minus {t}. This proves (P1) using all eligible sources, not just used receivers.

A label in K adjacent in F to ALL of T cannot be selected anywhere: at a low source it would force d residual tight labels, while at high sources it is already residual. Hence x_k=s_k=0 for each such common label. This derives unselection before zero demand; zero demand alone does not imply unselection.

## 2. Extra profile sources have an exact residual cost

Choose a positive integer z such that p_t>=z for every t. **Unlike the predecessor, z here need not equal chi(Gamma): it is a chosen common lower bound on the full pool sizes.** The inherited routing implies z=1 is always valid. If E>0, the extra-selection disjoint-destination lemma supplies two distinct used receivers for every t, so z=2 is valid. All formulas below are proved for any such chosen lower bound; no monotonicity assumption about a computed minimum as z varies is needed.

Every source in V other than V_t carries t residually. Define

    beta_t=R_t-(m-p_t)>=0, beta=sum_t beta_t.

These beta_t count residual occurrences of tight labels OUTSIDE V. High sources select T, so none of these occurrences is at H. In particular adding a source to V_t consumes one residual occurrence of each of the other d-1 tight labels. Such additions are not free.

All F-neighbours of t lie in T union K, and R_t=delta_t-d. Consequently

    m-p_t <= R_t <= kappa-1.

Since p_s>=z for all s, kappa>=kappa_0:=1+z(d-1). Put

    h=kappa-kappa_0>=0,
    L=m-zd>=0, so p_t=z+u_t, u_t>=0, sum_t u_t=L.

These parameters are integers. Let mu count missing edges inside F[T], and Q missing T-K edges, relative to their complete interfaces. Exact tight-degree accounting gives

    2mu+Q+beta = d*h-(d-1)*L.                          (P2)

Indeed 2mu+Q=sum_t(d-1+kappa-delta_t)
=d(kappa-1)-sum_t R_t, and sum_t R_t=(d-1)m+beta.

A per-label version, retained for the next attack, is

    q_t+nu_t+beta_t = h-L+u_t,                         (P3)

where q_t is the number of missing T-K edges at t and nu_t its missing internal T-degree. Dropping (P3) in the scalar relaxation below makes that relaxation potentially weaker, not stronger.

## 3. A refined demand deficit

Partition K into common labels (n0 of them), one-hole labels (n1 of them), and labels with at least two missing tight neighbours (n2 of them). A label in K has at least one tight F-neighbour; the last class therefore has between two and d-1 holes. For d=3 its members have exactly two holes. Write n_t=|K_t|, so n1=sum_t n_t and n0+n1+n2=kappa.

Define eta=sum_{i outside T}(d-1-s_i). All summands are nonnegative. The common-label argument and (P1) prove

    eta >= (d-1)n0 + sum_t n_t*(d-1-p_t)_+.            (P4)

Also

    n1+2*n2 <= Q <= d*h-(d-1)*L.                       (P5)

Because p_t<=z+L, a weaker scalar form of (P4) is

    eta >= (d-1)n0 + f*n1,
    f=max(0,d-1-z-L).                                  (P6)

This deliberately gives EVERY one-hole label the largest pool size permitted by the total L. Different labels may actually be tied to smaller pools; their distribution is not enforced by (P6). Nor is a label missing two neighbours incorrectly restricted to a d-1-element residual profile: such labels may use smaller residual sets, and their penalty is relaxed to zero.

### Why the predecessor's weakest point was too optimistic

At equality in the predecessor's total slack bound, h=z and L=0, there is one common label and all remaining dz K-labels have exactly one hole. Equations (P2) and the common-label count force mu=beta=0 there. Now p_t=z, so (P4) adds dz*(d-1-z)_+ to the previously available eta=d-1.

For d=5,z=2 this former equality pattern has kappa=11, one common and ten one-hole labels. Its slack is at least 10+4+10*2=34, rather than 14. **This is a statement about that branch only.** The new global relaxed minimum is 30 at a different (h,L), not 34 everywhere. We do not transplant an equality-branch penalty to all configurations.

## 4. Exact finite scalar minimization

For d>=3,z>=1 define B(d,z) as the minimum of

    d*h+(d-2)*L+(d-1)*n0+max(0,d-1-z-L)*n1            (P7)

over nonnegative integers h,L,n0,n1,n2 subject to

    kappa=1+z(d-1)+h,
    n0+n1+n2=kappa,
    n1+2*n2 <= d*h-(d-1)*L.                            (P8)

This is a NECESSARY-CONDITION RELAXATION, not a characterization of graph realizability. Every actual configuration yields a feasible tuple and, by (P6),

    d*h+(d-2)*L+eta >= B(d,z).                         (P9)

The minimum can be computed with a provably finite search. Put

    h0=ceil(2*(1+z(d-1))/(d-2)).

At h=h0,L=0, the relaxed tuple n0=n1=0,n2=kappa is feasible because 2*kappa<=d*h0. Thus B(d,z)<=d*h0. Any h>h0 costs at least d*h>d*h0 and cannot improve the minimum. It is enough to search

    0<=h<=h0, 0<=L<=floor(d*h/(d-1)).                   (P10)

For fixed h,L,n0 the least feasible n1 is

    n1_min=max(0,2*(kappa-n0)-[d*h-(d-1)*L]).

It is allowed exactly when n1_min<=kappa-n0. Since its coefficient is nonnegative, this eliminates n1 from the Python minimization. The C++ checker independently enumerates EVERY n0,n1,n2 composition instead. When f=0 the Python code retains all minimizing n1, so full minimizer-list comparison is meaningful.

The new B is never weaker than the predecessor's d(z+1)-1. Indeed (P8) implies n0>=max(0,kappa-[d*h-(d-1)*L]), and (P7) is at least the common-label relaxation used in the predecessor. This observation is also tested numerically, but its justification is symbolic.

## 5. Insert the profile deficit in the exact global identity

Let O=B minus (H union V), and define

    alpha=sum_i max(0,R_i-delta_i),
    sigma_H=sum_{u in H}(rho_u-kappa),
    sigma_O=sum_{u in O}(rho_u-1).

All are nonnegative in the stated regime: K is residual at every high source, and positive-surplus canonical residual activity gives rho_u>=1 at all B-vertices. The exact source and label identities are

    r=d*kappa+m*(d-1)+(b-d-m)+sigma_H+sigma_O,
    sum_i s_i=r+2*tau+alpha=a(d-1)+d-eta.

Therefore, with the FULL pools V rather than just U,

    a(d-1)+d-b-2*tau
      = z*d*(2d-3)+d*h+(d-2)*L+eta
        +alpha+sigma_H+sigma_O.                        (P11)

Every source is counted exactly once. Inserting (P9) yields the new global necessary condition

    a(d-1)+d >= b+2*tau+z*d*(2d-3)+B(d,z).              (P12)

This b-dependent statement uses positive-surplus residual activity. It is not automatically extended to tau=0. No equality-attainment or graph-realization assertion follows from a minimizer of (P7).

Since b=Delta(G), degree summation gives 2*tau<=b*(b-a-1), hence b>=a+2 when tau>0. Thus

    a >= ceil([z*d*(2d-3)+B(d,z)-d+2+2*tau]/(d-2)).    (P13)

Use z=1 for a necessary condition on any such tight block. Use z=2 when E>0. Failure of the z=2 condition forces E=0, NOT automatic exclusion of the whole state. Failure of the z=1 condition excludes a configuration only after its full hypotheses are established. Applying either to a catalogue ID and promotion are separate tasks not performed here.

## 6. Checked numerical consequences

For integer tau>=1, exact minimization gives:

| d | B(d,2) | Previous minimum a for extras | New minimum a for extras | New minimum a for any such block (z=1) |
|---|---:|---:|---:|---:|
| 3 | 8 | 27 | 27 | 16 |
| 4 | 17 | 26 | 29 | 16 |
| 5 | 30 | 28 | 33 | 18 |
| 6 | 35 | 31 | 36 | 18 |
| 7 | 39 | 35 | 38 | 19 |
| 8 | 40 | 38 | 41 | 21 |
| 9 | 45 | 42 | 45 | 23 |
| 10 | 50 | 46 | 48 | 25 |

For d=5, extras are now impossible through a=32 under the full assumptions, compared with a=27 previously. At z=2 its budget reads

    4a+5 >= b+2*tau+100.

With b>=a+2 and tau>=1 this forces a>=33 if extras exist. This does not say extras exist at 33. More generally actual b and tau in (P12) can give stronger bounds than this table.

## 7. Executed checks and precise limits

Run `python3 check_profiles.py` beside `verify_minima.cpp`; only Python standard-library modules and a C++17 compiler are used. No downloaded inputs are needed.

The Python eliminated-variable minimizer and C++ full-composition enumerator agree EXACTLY on the minimum, feasible-tuple count and COMPLETE list of all minimizing tuples for 131 (d,z) pairs: d=3..20,z=1..min(d,4), and d=21..50,z=1,2. The C++ enumeration covers 1,774,146 feasible scalar tuples. Their matching lists are preserved losslessly in `MINIMIZERS.json.gz.b64`; the checker regenerates `MINIMIZERS.json`. Decode the archived copy with `python3 -c "import base64,gzip,pathlib; p=pathlib.Path('MINIMIZERS.json.gz.b64'); p.with_name('MINIMIZERS.json').write_bytes(gzip.decompress(base64.b64decode(p.read_bytes())))"`. The SHA256 of the decoded JSON is recorded in `CHECK_RESULTS.json`. This comparison is not merely aggregate fingerprint agreement.

Further executed Python checks cover 88,139 multisets of nonempty proper T-residual subsets (d=3..5, bounded source counts), verifying the exact one-hole eligibility and outside-profile residual accounting. They also cover 244,683 accepted relaxed binary tight interfaces and full-profile count configurations, checking (P2), (P4)-(P9). Exact domains and outputs are in the source and `CHECK_RESULTS.json`.

Four negative controls preserve: used pools need not be full pools; the one-hole profile rule does not extend to two-hole labels; zero demand need not mean zero selected degree; a scalar minimizer need not respect individual pool prices or be a canonical realization. `explore.py` preserves the initial coarse exploratory minimizer; its heuristic search cutoff is NOT the certification code. The certified driver uses (P10).

Both implementations were written by the same assistant. These are targeted necessary-condition checks, not independent expert review, original critical-graph enumeration, validation of the inherited canonical bridge, or catalogue exclusions. The symbolic proof of source confinement is separate from these finite checks. No unsupported comparison with the literature or novelty claim is made.

## 8. Dependencies, preservation and next step

The live handoff and AGENTS were read first on main; inspected head was `31f6c8aca964de0bcaed0cdfe03f14d7abbd7e18`. Mathematical dependencies:

- `project/research/general_n/2026-09-16-tight-interface-slack-v1/PROOF.md`, especially Sections 2-6; blob `d39f57eeaef72dc2b7358755af43b7ce89c80af2` (the user-provided full proof was also read locally).
- Its stated canonical bridge, global-budget and first-boundary dependencies, preserved at that head. This continuation rederives the needed profile and counting identities rather than claiming a new external audit of those inherited lemmas.
- Predecessor `CURRENT_STATE.md`, blob `b1cc7624fe4d1840bcb341beba815cac3315023b`, archived unchanged with this checkpoint.

Canonical totals remain **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration is unresolved; original equality replay is not rerun. Prior proofs, failed routes, review materials and audit gates are preserved.

**Next bounded mathematical task:** retain individual profile prices (d-1-p_t)_+ and the row identities (P3), rather than charging all weak labels at the cheapest possible price. Start with the d=5,z=2 relaxed minimizers (h=4,L=2,n0=1,n1=12,n2=0), and test whether distributing the two extra profile sources among five pools can actually support their twelve one-hole labels at zero deficit. Preserve any improved conditional inequality, infeasible relaxed minimum, or counterexample before a further unit. This concerns feasibility in a stronger necessary-condition model, not automatic original-graph realizability or catalogue promotion.
