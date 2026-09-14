# Source pricing and the boundary of uncoupled incidence/orientation

14 September 2026. Continuation of the precommitted [plan](PLAN.md). **New exact conditional bound and integer-checked relaxation witnesses; external mathematical review and novelty assessment OPEN. No whole-state promotion or graph realization.**

The root README's fixed-order/general candidate table was moved immediately below its introduction in `be8c3a82d6304986f4fab09cdcd07b2b737f4835`; its reviewer navigation was unchanged. The shared-slack CI receipt was updated from historical queued status to its recorded successful replay.

## 1. Source-priced selected-incidence upper bound

Assume one binary selected-incidence matrix X, with row sums q_u and column sums x_i=s_i+e_i, e_i>=0, total excess E=sum e_i. Source u can use only eligible labels; the present projection uses s_i<=rho_u, rho_u>=1. Let p be actual full incoming degree, d_u=(p_u-rho_u+1)_+, p_u<=P_u, and D_u=(P_u-rho_u+1)_+. At every selected POSITIVE-demand label, assume d_u<=e_i. These are conditional hypotheses inherited from the canonical bridge, not a new proof of that bridge.

Fix xi>=0, coefficients alpha_u>=0 and ARBITRARY SIGNED source prices pi_u. The actual charge is

```text
C = sum_{i:s_i>xi} sum_u X_ui alpha_u d_u.
```

For label i, let I_i={u:q_u>0,rho_u>=s_i}. Define Top_k as the sum of exactly k largest entries, including negative entries when required, and

```text
Phi_i(e;pi) = Top_{s_i+e} {
  1_{s_i>xi} alpha_u min(e,D_u) - pi_u : u in I_i
}.
```

Let A be any explicitly specified allocation domain containing every actual excess vector. Our verifier retains nonnegative integer e, sum e=E, s_i+e_i<=|I_i|, and EVERY prefix forced-selection inequality in sorted label order:

```text
sum_{i in L}(s_i+e_i)
 >= sum_u (q_u - #{eligible labels outside L})_+.
```

Then

> **Source-priced envelope**
>
>     C <= U(pi) := sum_u q_u pi_u + max_{e in A} sum_i Phi_i(e_i;pi).

Proof: at the actual incidence ui on a charged label, alpha_u d_u<=alpha_u min(e_i,D_u). Subtract pi_u at EVERY selected incidence and restore sum q_u pi_u using the exact row sums. At each actual column, its s_i+e_i selected sources form an admissible subset of I_i, so their reduced score is at most Phi_i. Finally maximize over an allocation domain containing the actual e. This uses only an upper bound, not equality with a joint incidence optimum.

Zero prices recover THIS envelope's unpriced version with the SAME allocation domain. They do not assert equality with every earlier conditioned or block-based calculation. A dynamic programme over total excess computes the stated bound exactly. Rational coefficients are scaled to integers before replay. Numerical optimization is used only to suggest prices; no numerical optimum, infeasibility status or tolerance is accepted as a certificate.

**Two important safeguards.** Uncharged and zero-demand columns still contribute their -pi_u terms. Omitting them makes signed pricing invalid: one source, one zero-demand selected label and price -1 would falsely give upper bound -1 for zero charge. Also, adding one constant to every source price must leave U unchanged because sum q=sum(s+e). The verifier tests this gauge identity.

A strict tiny example is q=[1,1,2], s=[1,1], rho=[1,1,1], P=[1,0,0], E=2, alpha=[1,1,1]. Zero prices give U=2; pi=[1,0,0] gives U=1. X=[[1,0],[0,1],[1,1]] attains charge 1. This is an abstract incidence example, not a positive-surplus canonical graph.

## 2. Matching receiver lower bound

For a q-tail T_tau, keep its ACTUAL incoming contribution y<=p. The safe interval box is

```text
A_u=min(P_u, #{v!=u:tau<=q_v<=q_u+rho_u+1}).
F_u=min(A_u,rho_u-1), G_u=A_u-F_u,
h_u=(q_u-#{eligible labels with s_i<=xi})_+,
w_u=alpha_u h_u, Q_tau=sum_{v in T_tau}q_v.
```

For every theta>=0,

```text
C >= theta*(Q_tau-sum F_u) - sum_u (theta-w_u)_+ G_u.
```

Indeed C>=sum w_u d_u, while z_u=(y_u-rho_u+1)_+<=d_u, 0<=z_u<=G_u and sum z_u>=Q_tau-sum F_u. Apply w_u z_u>=theta z_u-(theta-w_u)_+G_u and sum. Domination y<=p is essential. A bare receiver box does not inherit selected-incidence pressure conditions.

The executable checks all its finite q-thresholds and theta in {0} union {w_u}; when Q_tau<=sum A_u these breakpoints suffice for the maximum of this piecewise-linear bound. If Q_tau>sum A_u, the simpler capacity contradiction applies. No universal q-tail sufficiency or Hall-minimum identity is assumed.

## 3. Exact six-profile results: stronger bounds, no new exclusion

Only the SIX ORIGINAL shared-slack non-rejections were tested here: 108,160,338,347,471,586. The seven fresh-seed rows have NOT been tested by this checkpoint and remain a separate namespace. Two alpha families and two xi values produce 24 finite price searches; 21 improve their own zero-price bound. Every best price and all 24 lower/upper comparisons are retained in [BEST_PRICES.json](BEST_PRICES.json) and replayed without an optimizer.

For xi=0 and alpha=1 when q<=2, alpha=3 otherwise:

| Original row | Receiver lower bound | Zero-price upper bound | Achieved source-priced upper bound |
|---|---:|---:|---:|
| 108 | 457 | 705 | 517 |
| 160 | 360 | 516 | 468 |
| 338 | 159 | 445 | 320 |
| 347 | 809 | 1,143 | 1,067 |
| 471 | 570 | 738 | 640.75 |
| 586 | 447 | 990 | 906 |

These are achieved valid upper bounds, not claims of globally optimal prices. NONE is a strict contradiction. No earlier screen is removed: the original sample remains 707/713 rejected, with six non-rejections.

The numerical exploration began with 45 iterations of unrestricted per-source prices and a large search box on row108. Its weaker best upper bound was 532.64 for the displayed charge. The revised discovery uses type-constant prices, a bounded box and at most 120 iterations. Best prices, settings, original script and raw-trace digests are preserved in this package and [DISCOVERY_INDEX.json](DISCOVERY_INDEX.json). All attained objective sequences and full raw iteration traces are retained in the portable bundle; exact proof replay does not depend on reproducing numerical optimization.

## 4. A useful obstruction to the route itself

An enlarged necessary model simultaneously imposes an actual selected-incidence matrix, the scalar ledgers, source eligibility, exact row/column sums, positive-label endpoint pressure, supplied target caps, and an actual simple directed orientation. The orientation has outgoing degrees q, incoming degrees p, no loops or opposite arcs, and both numerical compatibility inequalities. It does NOT identify a selected label with each outgoing arc or build residual cross-neighbourhoods.

The numerical search produced three explicit candidates, now checked by a separately written integer-only verifier:

| Original row | Selected incidences | Directed arcs | Positive-label endpoint checks |
|---|---:|---:|---:|
| 160 | 81 | 81 | 81 |
| 338 | 101 | 101 | 86 |
| 347 | 129 | 129 | 129 |

[JOINT_WITNESSES.json](JOINT_WITNESSES.json) contains all selected label sets, arcs, excesses, incoming degrees and pressures. Their exact existence proves that the LISTED relaxation alone cannot exclude these three profiles. It does not establish graph realizability or compliance with every stronger condition elsewhere in the repository. Eighteen deliberate witness corruptions were rejected.

The 8-second discovery attempts on rows108 and471 ended without incumbents. The solver reported row586 infeasible, but supplied no accepted exact infeasibility certificate. ALL THREE remain unresolved here. A numerical infeasibility status is not a new profile exclusion.

## 5. Where the witnesses fail: labels must travel with destinations

This reconnects to the retained [fixed-neighbourhood flow route](../2026-09-12-arc-realisation-pilot-v1/FIXED_NEIGHBOURHOOD_FLOW.md); it is not a claim that the old route or its unsuccessful experiments were absent.

Let S_u be u's selected-label set and N_u its full cross-neighbourhood. For a canonical arc u->w, opposite selection w->u is forbidden. Every selected edge at w must therefore dominate u, giving S_w subset N_u. The label assigned to u->w is absent from N_w, while every OTHER selected label at u belongs to N_w. Consequently

```text
1 <= |S_u minus S_w| <= rho_w+1,
|S_w minus S_u| <= rho_u,
| (union_{w:u->w} S_w) minus S_u | <= rho_u.
```

The last condition counts a SHARED residual neighbourhood at u. It is not the sum of independently reusable residual budgets. The implications follow from the canonical unique-exception property; their graph application retains its external-review dependency.

All three PARTICULAR witnesses fail these necessary coupling tests. Their pair-violation counts are58,71,95, and their residual-union violation counts are8,8,15, respectively. For row338, zero-based source4 would require15 distinct residual labels but has rho=3. Full diagnostics are regenerable from the witnesses, with per-object digests and representative failures in [JOINT_VERIFIED.json](JOINT_VERIFIED.json).

**This invalidates these witnesses as graph-derived configurations, NOT every incidence/orientation realization of their profiles.** To exclude a profile, one must exclude every allowed realization, not only the returned witness. The next targeted attack should enforce selected-label/destination and common residual-neighbourhood coupling, rather than indefinitely optimizing only the now-demonstrably-insufficient uncoupled projection.

## 6. Verification and trust boundary

[VERIFIED_RESULT.json](VERIFIED_RESULT.json) records 9,043 exhaustive tiny selected-incidence configurations, 9,043 gauge checks, 626 independent column-subset enumeration comparisons from 1,000 attempted random profiles with negative-excess cases omitted, and 1,000 valid oriented-incidence lower-bound checks from 1,078 trials. These tiny domains are not the positive-surplus scalar corpus. The six input records separately satisfy their stated scalar identities.

The source-priced DP was compared with independently structured column-subset enumeration, and all 24 frozen price evaluations were replayed exactly. This is same-assistant internal verification, not independent third-party review. New remote CI is NOT claimed by this checkpoint; the earlier shared-slack run's success covers its own earlier scope only.

Canonical totals remain **1,971 exclusions / 3,607 survivors / 977 whole-state closures**. All **2,655 relational candidates remain UNPROMOTED** behind the existing complete-coverage, dual-agreement, zero-unresolved, successful-aggregate and separate-reviewed-ledger gates. No existing audit workflow, budget or concurrency was changed. Fixed-order candidates and the general7/12 candidate are unchanged. All prior proof packages, corrections and reviewer navigation remain retained.
