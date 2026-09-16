# Tight-interface holes force a demand deficit

16 September 2026. Research directed by Paul Lenz; internal mathematical development and checks by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded continuation from `c9cc277e10ec854a7fa7f00766393e5ba68e7597` in `paullenz/MurtySimon742`. This is a conditional derivation under the FULL canonical graph-to-selected/residual bridge and the exact tight-block hypotheses. Independent expert review of that bridge, the inherited routing statements and this argument remains OPEN. No catalogue replay, original-graph enumeration, new catalogue exclusion, promotion, realizability or literature-novelty claim is made.

## 1. New conclusions

In the setup below, assume `tau>0`, `d>=3`, and `|T|=|H|=d`. Put `z=chi(Gamma)`. The strengthened budget is

    (d-1)(a-2*z*d) >= b+2*tau-1.                         (S1)

The exact new ingredient, in the predecessor's notation, is

    eta+d*(kappa-1-z*(d-1)) >= d*(z+1)-1.                (S2)

Thus the minimum possible neighbourhood and maximum possible outside demand cannot occur together. A neighbourhood near its lower bound forces common tight neighbours, each having zero selected degree and zero demand. Enlarging the neighbourhood avoids some of that deficit but costs residual incidences at every high source. Integer minimization quantifies the trade-off.

If the number E of extra high-source selections is positive, then `z>=2`, so

    (d-1)(a-4d) >= b+2*tau-1.                            (S3)

The earlier right side was `b-3d+2*tau`: the new necessary condition improves it by exactly `3d-1`.

For an actual canonical graph, `b=Delta(G)` and positive surplus imply `b>=a+2`. Consequently

    a >= 2*z*(d+1)+ceil((4*z+1+2*tau)/(d-2)).             (S4)

In the E>0 branch this gives

    a >= 4d+4+ceil((9+2*tau)/(d-2)).                      (S5)

For d=5 and integer tau>=1, extras require a>=28; hence E=0 through a=27. The previous necessary threshold was a>=23. No assertion is made that extras exist at either threshold.

Since z>=1 even without extras, every such tight block also requires

    a >= 2d+2+ceil((5+2*tau)/(d-2)).                      (S6)

Failure of (S6), when the full hypotheses have been established, excludes that configuration. Failure of the stronger extra-branch condition (S5) only forces E=0; it does NOT automatically exclude the whole state. Applying either conclusion to a catalogue ID still requires a whole-state justification and the normal promotion gate.

## 2. Setup and inherited facts

Let G be a finite simple diameter-two edge-critical graph, J its complement, v a minimum-degree vertex of J, A=N_J(v), and B=V(J) minus N_J[v]. Write

    a=|A|, b=|B|=Delta(G), n=a+b+1,
    F=complement(J[A]), tau=e(G)-b(a+1)=e(F)-r.

For an A-label i, let delta_i=deg_F(i), R_i be its total residual degree into B, x_i its selected degree, and s_i=max(0,delta_i-R_i). At a B-vertex u, N_u is partitioned into the selected-label set S_u and residual-label set R_u, and rho_u=|R_u|. Distinguish the number R_i at a label from the set R_u at a source.

Use the FULL selected representative system: exactly one representative for every missing unordered pair of J[B], distinct destinations for selected labels at a source, and no double orientation. The canonical bridge supplies

    x_i>=s_i; i in S_u implies s_i<=rho_u;
    r=sum_i R_i=sum_u rho_u; e(F)=r+tau.

A selected incidence of label i at u must dominate every A-vertex, so N_F(i) is contained in N_u. For tau>0, every B-vertex has rho_u>=1. These are inherited hypotheses/results, not claims proved by the finite interface checks below.

Define

    T={i:s_i=d}, H={u:rho_u>=d}, and assume |T|=|H|=d.
    K=(union over t in T of N_F(t)) minus T; kappa=|K|.

T is the ENTIRE demand-d level, not a chosen subset. Each t in T is selected at all d high sources and at no source outside H. No label has demand larger than d, since it would need more than d distinct eligible sources. Hence s_i<=d-1 outside T.

The predecessor establishes that K is residual at every high source. Every tight destination receiving t has residual set exactly T minus {t} and omits t from its whole A-neighbourhood. Let U_t be the pool of tight destinations for t, c_t=|U_t|, and ell=sum_t c_t. The U_t are pairwise disjoint and their union U is disjoint from H.

For high source u, let D_u be its d tight destinations. Gamma is the graph on H in which uw is an edge exactly when D_u and D_w are disjoint. Put z=chi(Gamma). Colouring high sources by their t-destination gives c_t>=z for each t. Every extra high selection uses an edge of Gamma, so E>0 implies z>=2. Always z>=1.

In particular, for every t in T,

    ell-c_t <= R_t = delta_t-d <= kappa-1.               (I1)

Thus kappa>=kappa_0:=1+z(d-1). Set

    h=kappa-kappa_0 >=0; L=ell-z*d >=0.

Both h and L are integers.

## 3. Common tight neighbours are globally unselected

Let W={k in K:T is contained in N_F(k)}, and w=|W|. Every k in W is already residual at all high sources. If k were selected at a non-high source u, A-side domination would force all T into N_u. No tight label is selected at a non-high source, so all d tight labels would have to be residual there, contradicting rho_u<d.

Therefore, for each k in W,

    x_k=0, s_k=0, R_k>=delta_k.                          (I2)

This is the common-neighbour observation from the earlier first-boundary proof, applied only to actual common neighbours. It does NOT say that all K-labels are unselected when the T-K interface is not complete. Nor does it infer unselection from zero demand: the implication is proved in the opposite direction.

With eta=sum_{i outside T}(d-1-s_i), every summand is nonnegative and each k in W contributes d-1. Hence

    eta >= (d-1)*w.                                     (I3)

## 4. Count holes in the tight interface

Let mu be the number of missing F-edges inside T, relative to a complete graph, and Q the number of missing F-edges between T and K, relative to the complete bipartite interface. All F-neighbours of a tight label lie in T union K.

The total deficit of the tight degrees from their maximum d-1+kappa is EXACTLY

    sum_{t in T}(d-1+kappa-delta_t) = 2*mu+Q.            (I4)

A missing edge inside T contributes twice; a missing T-K edge contributes once. Using delta_t=d+R_t and (I1),

    2*mu+Q = d*(kappa-1)-sum_{t in T}R_t
           <= d*(kappa-1)-(d-1)*ell
            = d*h-(d-1)*L.                              (I5)

Every non-common K-label accounts for at least one of the Q missing interface edges. Thus kappa-w<=Q, and

    w >= max(0, kappa-d*h+(d-1)*L+2*mu)
      = max(0, kappa_0-(d-1)*h+(d-1)*L+2*mu).           (I6)

Combining (I3) and (I6) is a more informative, parameter-sensitive bound than (S2). It retains losses caused by extra receivers and missing edges inside T. In particular, after discarding only nonnegative terms,

    eta >= (d-1)*max(0, 1+z*(d-1)-(d-1)*h).             (I7)

This proves the demand deficit without assuming an unjustified extension of all-K unselection beyond saturation.

## 5. Exact integer minimization

It remains to lower-bound d*h plus the right side of (I7).

If 0<=h<=z, the expression inside the maximum is 1+(d-1)(z-h), so

    d*h+(d-1)[1+(d-1)(z-h)]
      = d*z+d-1 + [(d-1)^2-d]*(z-h)
      >= d*z+d-1.                                      (I8)

The coefficient (d-1)^2-d is positive for every d>=3.

If h>=z+1, just its first term gives

    d*h >= d*z+d > d*z+d-1.                             (I9)

These exhaust the nonnegative INTEGER values of h, proving (S2). The relaxed expression is minimized at h=z. This locates the weakest point of this counting argument; it does NOT establish that a canonical graph realizes equality there. In particular, the argument has not yet used how many sources can select a weak K-label missing only one tight neighbour.

The d>=3 restriction here is essential: for d=2, z=1, h=0 the relaxed expression is 2 rather than the claimed 3. The predecessor separately rules out the full positive-surplus tight-block hypotheses for d=1 and d=2; those exclusions are not re-proved or extended by this integer argument.

## 6. Insert the deficit into the exact global identity

For completeness, let O=B minus (H union U), and define

    alpha=sum_i max(0,R_i-delta_i),
    sigma_H=sum_{u in H}(rho_u-kappa),
    sigma_O=sum_{u in O}(rho_u-1).

These are nonnegative in the stated regime. The positive-part identity and disjoint B-source count give the predecessor's exact identity

    a(d-1)+d-b-2*tau
      = z*d*(2d-3)+d*h+(d-2)*L
        +eta+alpha+sigma_H+sigma_O.                     (I10)

Indeed S=sum_i s_i=r+2*tau+alpha, while
r=d*kappa+ell*(d-1)+sigma_H+(b-d-ell)+sigma_O.
Combining these with S=a(d-1)+d-eta verifies (I10) directly. No positive-part term is silently dropped from an equality.

Insert (S2) and discard the remaining nonnegative terms. Since

    z*d*(2d-3)+d*(z+1)-1 = 2*z*d*(d-1)+d-1,

we get

    a(d-1)+d-b-2*tau >= 2*z*d*(d-1)+d-1,

which is precisely (S1). The refined version retains (I6), (d-2)L, alpha, sigma_H, and sigma_O. No claim is made that these remaining losses can vanish simultaneously in a graph.

The b-dependent statement uses rho_u>=1 at O and therefore is asserted here only for tau>0. No automatic extension to tau=0 is made.

## 7. Maximum-degree corollaries

The maximum-degree sum in the original graph yields

    2*tau <= b*(b-a-1).

Thus tau>0 gives b>=a+2. Substituting this into (S1) gives

    (d-2)*a >= 2*z*d*(d-1)+1+2*tau.

Since d(d-1)=(d-2)(d+1)+2, integer rounding gives (S4). Apply z>=2 for extras, or z>=1 for existence of any tight block, to obtain (S5) and (S6).

For integer tau>=1:

| d | Previous minimum a for extras | New minimum a for extras | New minimum a for any such tight block |
|---|---:|---:|---:|
| 3 | 19 | 27 | 15 |
| 4 | 20 | 26 | 14 |
| 5 | 23 | 28 | 15 |
| 6 | 27 | 31 | 16 |
| 7 | 31 | 35 | 18 |
| 8 | 34 | 38 | 20 |

Every entry is a necessary lower bound under the full hypotheses, not a graph realization, new catalogue result, or unrestricted theorem. Using actual b, tau and z in (S1) can be stronger than these simplified bounds.

## 8. Executed checks and their precise limits

Run `python3 check_slack.py` beside `verify_slack.cpp`; it requires Python 3 and a C++17-capable g++. No downloaded inputs or third-party Python packages are required.

The Python checker generates interfaces within individual tight-degree budgets. The C++ checker instead exhaustively scans binary interfaces and computes tight degrees directly. On the specified small domains they produce matching counts and three aggregate fingerprints (sum, sum of squares modulo 2^64, and XOR of injectively encoded configuration IDs) for **243,149 accepted interface/count configurations**. Aggregate fingerprint agreement is not a proof that independently stored full decision lists were compared; no such claim is made.

The exact test domain is d=3, z=1, kappa=3..6; d=3, z=2, kappa=5..7; and d=4, z=1, kappa=4. Receiver counts range independently over z and z+1. These are intentionally relaxed A-side interfaces satisfying the tested tight-degree bounds; they are NOT full canonical selected/residual systems or original diameter-two critical graphs.

Additional executed checks cover **88,384 scalar minimization cases**, **429,210 refined receiver-slack cases**, and **7,632 integer-threshold cases**. Four negative controls preserve the d=2 failure, a formal predecessor-budget equality that violates the omitted common-label penalty, the distinction between continuous and integer h, and an interface with both common and weak K-labels.

The two implementations were written by the same assistant using different enumeration structures. They are internal cross-checks, not independent expert acceptance. They do not validate the inherited canonical bridge, prove graph realizability, replay the catalogue, or settle external novelty. See `CHECK_RESULTS.json` for the exact outputs.

## 9. Dependencies, preservation and next bounded task

All mathematical dependencies were inspected at immutable commit `c9cc277e10ec854a7fa7f00766393e5ba68e7597`:

- `project/research/general_n/2026-09-16-global-tight-block-budget-v1/PROOF.md`, especially its setup, receiver bounds and exact slack identity.
- `project/research/general_n/2026-09-16-first-extra-boundary-v1/PROOF.md`, especially common-neighbour zero selection and the warning against all-K unselection outside saturation (blob `b724f1d57300b8dce0e788cc145826fc3cd1da15`).
- `project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`, especially Sections 2-6 and 9.
- Live predecessor `CURRENT_STATE.md`, blob `751040ed8c445c65b322275e9059392f9668ba95`, archived unchanged with this checkpoint.

Canonical totals remain **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. State 3349 enumeration and original equality replay remain unresolved/not rerun respectively. Earlier proofs, controls, reviewer material, README history and audit gates are unchanged.

**Next bounded mathematical task:** examine the weakest h=z branch by bounding selected degree of weak K-labels that miss exactly one member of T. Relate their eligible source count to their omitted-label receiver pool and to any additional residual occurrences of tight labels outside U. Quantify the additional cost before claiming a stronger bound. Do not treat equality in (I7)-(I9) as a canonical realization and do not assume every residual-profile source is already a used tight receiver without proving the residual accounting needed for that step.
