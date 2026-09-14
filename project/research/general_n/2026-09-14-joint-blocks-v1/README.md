# Shared block slack: pressure competes for the same selected places

14 September 2026. **Hand derivation under explicit selected-incidence/endpoint hypotheses; internally checked, external mathematical review OPEN. No whole-state promotion, realized graph or unrestricted Murty–Simon proof.** The [starting plan](PLAN.md) was committed before these experiments. This extends [conditioned excess](../2026-09-14-conditioned-excess-v1/README.md), not a replacement of its evidence.

## 1. The missing shared resource

A low-demand block can have J selections beyond those already forced into it. The preceding conditioned cap could allow each source to use those J spare places independently. Each individual cap was safe, but actual sources share ONE total of J. The following inequality retains that competition.

There is one actual binary selected-incidence matrix, with row sums q_u and column sums x_i=s_i+e_i. Let E=Esel=sum e_i and assume e_i>=0. Source u may select only eligible labels A_u; in the canonical projection A_u={i:s_i<=rho_u}. Define pressure d_u=(p_u-rho_u+1)_+, with a legitimate cap d_u<=D_u=(P_u-rho_u+1)_+. Every selected POSITIVE-demand label i satisfies d_u<=e_i. The use of these hypotheses for a graph inherits the canonical bridge's external-review boundary.

Choose ANY label block L containing all zero-demand labels. Set

    S_L=sum_{i in L}s_i,
    f_u=(q_u-|A_u outside L|)_+,
    m_u=|A_u intersect L|,
    M=sum_u f_u.

Fix its ACTUAL excess e_L and write

    H=E-e_L,
    J=S_L+e_L-M.

Negative J or an impossible block total rejects that branch; neither is clipped. Empty/full blocks have e_L=0/E respectively.

If k_u is the number of u's actual selections into L, then

    k_u>=f_u, k_u<=min(q_u,m_u), sum_u(k_u-f_u)=J.

For d>0, the q_u-k_u selected labels outside L are distinct positive-demand labels, each needing at least d excess. Consequently

    k_u >= q_u-floor(H/d).

Define the integer slack cost

    gamma_u(0;H)=0,
    gamma_u(d;H)=(q_u-f_u-floor(H/d))_+  for d>=1.

Only pressures satisfying max(f_u,q_u-floor(H/d))<=m_u are admissible; at d=0 require f_u<=m_u.

> **Shared-slack theorem**
>
>     sum_u gamma_u(d_u;H) <= J.                         (1)

Proof: gamma_u(d_u;H)<=k_u-f_u for every source. Sum over the SINGLE actual incidence matrix. No label excess is summed once per source as if those label sets were disjoint.

An equivalent particularly compact budget is

    H+sum_u gamma_u(d_u;H) <= E+S_L-M.                  (2)

The right side equals Q-r-2t-D0+S_L-M by the exact two-defect bridge. Structural surplus is t, q-thresholds are tau, and demand-block thresholds are eta. Esel and D0 remain separate.

## 2. Quantitative extension of the tight-block argument

If J=0, every source has k_u=f_u. Whenever q_u>f_u,

    d_u <= floor(H/(q_u-f_u)).

This is the saturation mechanism used in the row-295 equality proof. Positive slack can relax it, but not independently at every source. For integers h>=1 and v>=1 with v-floor(H/h)>0,

    #{u:d_u>=h and q_u-f_u>=v}
      <= floor(J/(v-floor(H/h))).                     (3)

Thus only a bounded number of sources can acquire high pressure by using the spare low-block places. This is a group-count consequence, not an empirical classifier.

For any nonnegative rational price lambda, (1) also implies

    sum_u d_u <= lambda*J
      +sum_u max_admissible_d [d-lambda*gamma_u(d;H)].  (4)

All scalar prices can be verified with exact rational arithmetic. The integer dynamic programme below can be strictly stronger than this separable rational bound; integrality is retained, not replaced by a numerical tolerance.

## 3. Exact finite pressure envelope and receiver cuts

For a receiver box A_u>=0, define free_u=min(A_u,rho_u-1) and G_u=A_u-free_u. Let Psi_L(e_L;G) be the maximum of sum_u d_u over admissible integers 0<=d_u<=min(D_u,G_u), subject to (1). The dynamic programme stores maximum accumulated pressure for each used slack 0,...,J. It is exact for this independent-pressure/one-budget projection ONLY, not for selected-matrix or graph realizability.

Any incoming vector y_u<=A_u has tail pressure d'_u=(y_u-rho_u+1)_+<=d_u. Slack cost is nondecreasing, so d' satisfies (1). Therefore

>     sum_u y_u <= sum_u free_u + Psi_L(e_L;G).       (5)

For T_tau={u:q_u>=tau}, take the interval upper box

    A_w=min(P_w, #{u!=w:tau<=q_u<=q_w+rho_w+1}).

A graph-derived orientation sends Q_tau=sum_{u in T_tau}q_u incoming units. Hence Q_tau exceeding the right side of (5) rejects the branch. The interval box drops reverse compatibility in the SAFE upper direction. No universal high-q-tail sufficiency, equality of Hall minima or fixed-q monotonicity is assumed.

The coarser full-orientation balance is sum d_u>=Q-r+b=b+2t+D0+Esel. It can also be compared directly to Psi. The implementation retains exact free-cap losses through (5).

## 4. Three additional original-sample exclusions

The new verifier directly examines the NINE preceding non-rejections. Its parent conditioned full output is pinned by canonical JSON SHA256 `7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e`. Every previously rejected branch remains covered by that earlier proof; every other branch is explicitly tested here. No branch is silently omitted.

The new complete exclusions are:

| Original sampled row | Low-demand threshold eta | New shared-slack branches completing prior coverage |
|---|---:|---|
| 240 | 2 | e_L=41,...,45; earlier e_L=39,40 already excluded |
| 258 | 2 | e_L=42,...,48; earlier e_L=38,...,41 already excluded |
| 342 | 3 | e_L=35,...,41; earlier e_L=33,34 already excluded |

The full range and inherited/new coverage are emitted explicitly. The cumulative SAME 713-row sample becomes **707 rejected / six not rejected**. Remaining rows are **108,160,338,347,471,586**. These are sampled relaxed profiles, NOT six remaining cases of the conjecture, and NOT a three-state reduction of the canonical 3607-state frontier.

### Hand-readable row-240 branch

At eta=2,e_L=41, the outside excess is H=4 and total spare low-block selections are J=2. At tau=1 the tail needs104 units and the free receiver capacity is28. Seventeen receivers can each contribute four pressure units for zero slack; one contributes two; four contribute one each for zero slack. That gives74 pressure units before spending slack. Every possible further pressure unit costs at least two slack, and the two available slack can buy at most one additional pressure unit. Thus

    incoming <=28+74+1=103 <104.

The entire remaining shared-slack branch table is:

    e_L:          41  42  43  44  45
    incoming cap:103 101 102 103 102
    demand:      104 104 104 104 104.

Earlier price certificates cover e_L39 and40 by224>209 and224>212. This gives complete coverage without treating one representative branch as the whole profile.

## 5. Soundness checks and hostile boundaries

Completed standard-library checks:

    9293 exhaustive actual selected-incidence configurations;
    25391 arbitrary label-block checks, including12305 with positive slack;
    10000 fresh random-incidence trials,7839 satisfying the stated source/label constraints;
    3000 independent brute-force comparisons covering237067 pressure vectors;
    all three standing hostile q-tail examples retained.

The incidence tests include empty/full blocks, arbitrary blocks rather than only prefixes, zero demands, zero pressure, individual ceilings and pressure monotonicity. Random incidence systems need not satisfy the positive-surplus scalar ledger; the separate fresh synthetic experiment below does. These evidence domains must not be conflated.

A tempting stronger claim, sum_u(q_u-k_u)d_u<=H, is FALSE: two sources can share one positive label. The actual matrix X=[[1,0],[1,0]], demands s=[1,0], residuals rho=[1,1], low block={the zero label}, and pressures[1,1] has H=1 but total high-incidence charge2. The valid theorem charges selected PLACES in the low block, not distinct excess falsely counted once across all sources. This hostile fixture is retained; it is not a positive-surplus graph.

The full new result canonical JSON hash is `35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6`. It includes the non-excluding branches and every final slack-DP table used in the new checks.

## 6. Simultaneous block experiment: useful tightening, no further profile closure

For a partition into equal-demand blocks of sizes n_j and exact shared excess totals E_j, any source with pressure d>0 can select at most min(n_j,floor(E_j/d)) labels from positive block j that it is eligible for. Zero-demand blocks instead contribute their eligible label count without that pressure restriction. Thus

    q_u <= sum_j allowed_labels(u,j,d).

All blocks must use ONE vector (E_j); optimizing each independently loses this constraint. We enumerated the surviving consistent block-total tuples and coupled these source caps with exact block-total restrictions in the previous upper envelope.

On the six remaining profiles this tested597 tuples:25 failed total capacity and118 failed a priced bound, leaving454 tuples across all six profiles. **No additional profile was fully excluded.** The full deterministic exploratory output, code, input dependence and digest are preserved. It is not a proof that joint incidence is feasible, nor evidence that every possible multiblock inequality has been exhausted. A full multiresource version of (1) remains available; this experiment did not solve that general optimization.

## 7. Fresh seeded scalar-bridge reconnaissance

Before inspecting its results, a fresh seed74220260919 was fixed for the preserved generator, keeping its domain and stopping rules unchanged. It ran100000 trials and produced715 profiles passing the stated scalar-ledger, source-cap, selected-incidence and potential-pair-flow conditions. Counts:44451 scalar-domain trials,5539 cap passes,1496 incidence passes,715 pair-flow passes,53 with zero-demand labels. This is the SAME generator with a new seed, not independently designed generation and not realized canonical graphs.

The resulting corpus SHA256 is `f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e`. Replaying the earlier and new necessary conditions yields:

    capped-spill rejections:              701
    additional block-pressure rejections:  3
    additional conditioned rejections:     1
    additional shared-slack rejections:   3
    not rejected:                         7
    total:                              715.

The new shared-slack rows in this FRESH corpus are163,362,687; they are not the same row namespace as the original713 sample. The seven fresh non-rejections are20,91,391,490,528,562,677. Their complete arrays and all three complete new branch certificates are retained. Fresh full-output canonical SHA256 is `754774a0d4fdb23c8403efe4c5e41f2df950ebf933f903ca7e3d335d6ce370f9`.

## 8. Scope and next question

No proof, verifier or historical counterexample was removed. The canonical promoted frontier stays1971 exclusions /3607 survivors /977 whole-state closures; the2655 relational candidates remain behind their independent complete-coverage, dual-agreement, zero-unresolved, aggregate and separate reviewed-ledger gate.

The next structural question is common selected-source usage across several label blocks. Current per-label upper envelopes can still choose incompatible best sources. The explicit remaining profiles constrain that search. Retain the exact q-layer/mincut, crossing-wall and independent maximum-cut/stability routes. Internal arithmetic, remote CI and evidence publication remain different from external mathematical acceptance.
