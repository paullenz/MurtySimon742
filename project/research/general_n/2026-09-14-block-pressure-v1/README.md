# Demand-block and source-specific priced pressure

14 September 2026. **Candidate universal consequences of the stated canonical bridge. Completed local integer verification; external mathematical review OPEN. No whole-state promotion, graph realization or all-order contradiction is claimed.**

This continues [capped spill](../2026-09-14-capped-spill-v1/README.md), [priced tails](../2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md) and [localized excess](../2026-09-14-localized-excess-v1/README.md). The previous 713-profile synthetic corpus had 694 rejections and 19 non-rejections. The new block/source-cap inequalities give exact certificates for SEVEN more profiles, leaving TWELVE. All old hypotheses and counterexamples remain in force.

## 1. Canonical domain and notation

Let X_ui be the actual binary selected incidence matrix. Its row degrees are q_u and column degrees x_i=s_i+e_i, with e_i>=0 and Esel=sum e_i. Positive-surplus residual activity gives rho_u>=1. Selected ui implies s_i<=rho_u. For every selected POSITIVE-demand label, canonical endpoint forcing gives

    d_u := (p_u-rho_u+1)_+ <= e_i.

The incoming bound gives d_u<=delta=b-a. The exact global identity remains

    Q=r+2t+D0+Esel.

Here t is structural surplus, tau a q threshold, and eta a label-demand threshold. Neither D0 nor the number of zero-demand labels z is Esel. Never assume z<=Esel.

Retain a legitimate target cap P_u>=0 from the minimum of all prior caps, including all-source spill and exact potential-pair degrees. Put

    D_u=(P_u-rho_u+1)_+.

Then actual pressure satisfies d_u<=D_u. A negative cap rejects the branch; it is not clipped silently. The positive-part definition of D is NOT a clipping of the target cap itself.

## 2. Charge only labels above a demand threshold

Fix eta>=0 and let

    L_eta={i:s_i<=eta}, m_eta=|L_eta|,
    v_u(eta)=(q_u-m_eta)_+.

A source choosing q_u DISTINCT labels must choose at least v_u(eta) labels outside L_eta. These labels have positive demand. For arbitrary nonnegative source weights alpha_u,

> **Demand-block pressure inequality**
>
> sum_u alpha_u v_u(eta) d_u
> <= sum_{i:s_i>eta} sum_{u:X_ui=1} alpha_u min(e_i,D_u).       (1)

Proof: multiply each actual high-label selected incidence at u by alpha_u d_u. Counting at u gives at least the left side. Counting at i and using d_u<=e_i,D_u gives the right side. No Hall-tail sufficiency, graph realization of a relaxed profile, or equality of independently optimized systems is asserted.

Eta=0, alpha=1 and replacing every D_u by delta recovers the previous capped positive-label charge. Positive eta excludes excess already tied to low-POSITIVE-demand labels, not only zero-demand labels. Keeping D_u distinguishes sources that cannot reach the global maximum pressure.

## 3. A closed-form hand bound

Let

    M_eta=sum_u (q_u-#{i:eta<s_i<=rho_u})_+,
    S_eta=sum_{i:s_i<=eta}s_i,
    B_eta=min(Esel,Esel+S_eta-M_eta).

Every source has at least the displayed unavoidable spill into L_eta, so

    e(L_eta)>=M_eta-S_eta,
    sum_{i:s_i>eta}e_i <= B_eta.

The minimum with Esel retains the trivial nonnegativity of low-block excess. If B_eta<0 the selected-incidence system is infeasible; do not replace it by zero. Write smax_eta=max({s_i:s_i>eta} union {0}). Equation (1), with alpha=1, therefore implies

> sum_u(q_u-m_eta)_+(p_u-rho_u+1)_+
> <= B_eta [smax_eta+min(B_eta,delta)].                       (2)

Indeed sum_high(s_i+e_i)min(e_i,delta) is at most smax_eta E_high + E_high min(E_high,delta), and this expression is nondecreasing in E_high>=0. This is a hand inequality under explicit bridge hypotheses, not merely an empirical classifier.

## 4. Retain source-specific pressure ceilings

For label i define eligible sources

    A_i={u:q_u>0, rho_u>=s_i}.

For a candidate integer e_i=e, x_i=s_i+e distinct members of A_i must be selected. Thus the i-term in (1) is bounded by

    T_i(e)=TopSum_{s_i+e}{alpha_u min(e,D_u):u in A_i}

when s_i>eta, and by zero otherwise. The candidate e must satisfy s_i+e<=|A_i|; it is not legitimate to truncate an impossible selection count and call it feasible.

The actual excess vector belongs to the following finite necessary projection:

    sum_i e_i=Esel,
    0<=e_i<=|A_i|-s_i,
    sum_{i:s_i<=h}e_i >= max(0,M_h-S_h)
      for each complete equal-demand prefix.

Let U(eta,alpha;P) be the maximum of sum_i T_i(e_i) over this projection. A standard integer prefix recurrence computes it: after i labels, record the largest score for each total excess; apply a prefix floor only AFTER the complete equal-demand block. Empty projection means infeasibility, not a zero upper bound. Then

> sum_u alpha_u v_u(eta)d_u <= U(eta,alpha;P).                 (3)

The recurrence is exact for the stated projection, not for selectable incidence matrices, orientations or graphs. The top-source choices for different labels may conflict; treating them independently only increases the upper bound. Actual selected incidences prove soundness. For alpha=1 and D<=delta, this is no larger than the hand bound (2).

## 5. Priced receiver inequality

For T_tau={u:q_u>=tau}, use the interval upper bound

    J_w(tau)=#{u!=w:tau<=q_u<=c_w+1}, c=q+rho,
    A_w=min(P_w,J_w(tau)),
    f_w=min(A_w,rho_w-1), g_w=A_w-f_w,
    w_w=alpha_w(q_w-m_eta)_+.

Every actual orientation must obey, for every theta>=0,

> theta(Q_tau-sum_w f_w)-sum_w(theta-w_w)_+ g_w
> <= U(eta,alpha;P).                                         (4)

The unweighted closed-form right side from (2) is also valid. The proof is the existing pointwise free/paid receiver inequality: tail incoming h_w is at most A_w and p_w; hence its pressure cost is bounded above by actual source pressure, while the left side lower-bounds that cost. Summing uses the SAME alpha-weighted block charge as in (1).

All new reported certificates use J, not an assumption of exact reverse compatibility. Exact compatible incoming can strengthen A if desired. A strict priced violation does not require a deficient interval tail. Finite searches over eta, tau, alpha or theta are certificate discovery, not universal existence proofs.

## 6. A short new hand certificate: 209 > 190

Zero-based row 664 of the frozen synthetic corpus has

    a=24, b=30, delta=6, t=1, D0=0, Esel=33,
    eta=1, M_eta=15, S_eta=1, B_eta=19, smax_eta=4.

The closed-form charge budget is

    19(4+6)=190.

At tau=3, with the already-derived all-source-spill caps and alpha=1,

    Q_tau=100, sum A=101, sum f=51.

For theta=8 the penalty sum is 183, giving required charge

    8(100-51)-183=209 > 190.

Thus the tail has nominal spare interval capacity but is too expensive. This needs neither a min-cost solver nor the integer upper-envelope recurrence. The separately checked source-specific integer upper bound for this unweighted block is 130, but that further improvement is not needed for the hand certificate.

## 7. Completed finite result: 19 -> 12, not a state-frontier reduction

The verifier reads the SAME 713-row corpus, SHA256

    157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572.

It first reproduces the prior 694 rejections and the exact 19 remaining row IDs. It then tests all demand-block breakpoints, q thresholds and price breakpoints with two fixed source-weight rules: alpha=1, and alpha=1 for q<=2 / alpha=3 for q>2. The latter is a choice of a valid universal inequality's coefficients, not an added graph hypothesis.

Seven additional integer certificates are frozen:

| Row | eta | tau | theta | Required charge | Upper envelope |
|---|---:|---:|---:|---:|---:|
| 39 | 1 | 4 | 21 | 576 | 471 |
| 76 | 1 | 4 | 18 | 209 | 147 |
| 119 | 0 | 4 | 18 | 456 | 444 |
| 406 | 1 | 3 | 5 | 200 | 193 |
| 664 | 1 | 3 | 24 | 617 | 387 |
| 682 | 1 | 4 | 18 | 621 | 609 |
| 688 | 1 | 5 | 9 | 114 | 111 |

Row 406 uses uniform weights; the other displayed strongest certificates use the q<=2 weight rule. The simpler unweighted 209>190 row-664 certificate is frozen separately.

Together with the retained prior screens, this is 701 rejected / 12 not rejected. Remaining rows:

    108,160,240,258,295,338,342,347,365,471,570,586.

These are sampled scalar/incidence/pair-flow relaxations, NOT realized graphs or complete state searches. The canonical promoted frontier remains 1,971 exclusions / 3,607 survivors and 977 whole-state closures. The independent 2,655-state audit has its own unchanged promotion gate.

## 8. Verification and hostile boundaries

`verify_block_pressure.py` completed:

- 9,293 exhaustive actual selected-incidence configurations, 33,356 new inequality checks, including variable source caps and source weights;
- 2,000 independent brute-force comparisons, including 579 nonempty and 1,421 empty projections: the second method enumerates labelled source subsets and excess vectors rather than using the top-sum/prefix recurrence;
- 1,000 receiver boxes with 14,806 incoming vectors, checking the price bound directly;
- all three standing hostile q-tail examples, preserving negative Hall minima and nondeficient high-q tails;
- all 713 frozen synthetic rows and the exact seven new certificates.

These are independently structured internal arithmetic tests, not external mathematical review or third-party reproduction. The old cap module supplies only previously frozen caps/baseline checks; the new charge, source-top bound, recurrence and receiver checks are implemented separately. No production C++ scanner is imported by the verifier.

The arbitrary-monotone-cap hostile example fails the canonical residual/edge ledger; Esel=5,z=2 fails selected-demand feasibility; Esel=19,z=4,s=0 fails S>=r+2t. Their old tail counterexamples remain reproduced. No restriction z<=Esel was added.

## 9. Failed extensions retained and next obligation

Merely replacing delta by source-specific pressure ceilings, without demand blocks or source weights, newly rejects only row 664. Positive-demand blocks give six new rejections; the tested source weighting adds row 688. A bounded multiblock-weight search found no additional rejection beyond those six. A further row-incidence Lagrangian search tightened some numerical upper bounds but produced no additional certified rejection on the tested twelve. Its floating optimization was discovery only; it supplies NO infeasibility certificate or proof of optimality. Exploratory code/results are retained in the portable bundle; these failures are not erased.

The residual row 295 reaches equality 126=126 in an unweighted source-cap charge bound. Equality-case incidence constraints are a sensible next hand target. More generally the twelve remaining relaxed profiles require stronger joint incidence/residual geometry or a genuinely different consequence, not an assertion that every useful weighting has been exhausted.

The exact q-layer, crossing-wall and independent maximum-cut routes remain preserved. Novelty assessment and external bridge review remain OPEN. No timeout, queue label, failed search or numerical optimizer status is promoted to mathematical proof.
