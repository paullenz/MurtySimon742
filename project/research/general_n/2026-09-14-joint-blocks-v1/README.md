# Shared block slack: pressure competes for the same selected places

14 September 2026. **Hand derivation under explicit selected-incidence/endpoint hypotheses; internally checked, external mathematical review OPEN. No whole-state promotion, realized graph or unrestricted Murty–Simon proof.** The [starting plan](PLAN.md) was committed before these experiments. This extends [conditioned excess](../2026-09-14-conditioned-excess-v1/README.md), not a replacement of its evidence. The complete end-to-end replay has now PASSED; see [CI_AUDIT.md](CI_AUDIT.md).

## 1. The missing shared resource

A low-demand block can have J selections beyond those already forced into it. The preceding conditioned cap could allow each source to use those J spare places independently. Each individual cap was safe, but actual sources share ONE total of J. The following inequality retains that competition.

There is one actual binary selected-incidence matrix, with row sums q_u and column sums x_i=s_i+e_i. Let E=Esel=sum e_i and assume e_i>=0. Source u may select only eligible labels A_u; in the canonical projection A_u={i:s_i<=rho_u}. Define pressure d_u=(p_u-rho_u+1)_+, with a legitimate cap d_u<=D_u=(P_u-rho_u+1)_+. Every selected POSITIVE-demand label i satisfies d_u<=e_i. Applying these hypotheses to a graph inherits the canonical bridge's external-review boundary.

Choose ANY label block L containing all zero-demand labels. Set

```text
S_L=sum_{i in L}s_i,
f_u=(q_u-|A_u outside L|)_+,
m_u=|A_u intersect L|,
M=sum_u f_u.
```

Fix its ACTUAL excess e_L and write H=E-e_L and J=S_L+e_L-M. Negative J or an impossible block total rejects that branch; neither is clipped. Empty/full blocks have e_L=0/E respectively.

If k_u is the number of u's actual selections into L, then

```text
k_u>=f_u, k_u<=min(q_u,m_u), sum_u(k_u-f_u)=J.
```

For d>0, the q_u-k_u selected labels outside L are distinct positive-demand labels, each needing at least d excess. Consequently k_u>=q_u-floor(H/d). Define

```text
gamma_u(0;H)=0,
gamma_u(d;H)=(q_u-f_u-floor(H/d))_+ for d>=1.
```

Only pressures satisfying max(f_u,q_u-floor(H/d))<=m_u are admissible; at d=0 require f_u<=m_u.

> **Shared-slack theorem**
>
>     sum_u gamma_u(d_u;H) <= J.                         (1)

Proof: gamma_u(d_u;H)<=k_u-f_u for every source. Sum over the SINGLE actual incidence matrix. No label excess is summed once per source as if those label sets were disjoint.

Equivalently,

```text
H+sum_u gamma_u(d_u;H) <= E+S_L-M.                       (2)
```

The right side equals Q-r-2t-D0+S_L-M by the exact two-defect bridge. Structural surplus is t, q-thresholds are tau, and demand-block thresholds are eta. Esel and D0 remain separate.

## 2. Quantitative extension of the tight-block argument

If J=0, every source has k_u=f_u. Whenever q_u>f_u,

```text
d_u <= floor(H/(q_u-f_u)).
```

This is the saturation mechanism used in the row-295 equality proof. Positive slack can relax it, but not independently at every source. For integers h>=1 and v>=1 with v-floor(H/h)>0,

```text
#{u:d_u>=h and q_u-f_u>=v}
 <= floor(J/(v-floor(H/h))).                            (3)
```

Only a bounded number of sources can acquire high pressure by using the spare low-block places. This is a group-count consequence, not an empirical classifier.

For every nonnegative rational price lambda, (1) also implies

```text
sum_u d_u <= lambda*J
 +sum_u max_admissible_d [d-lambda*gamma_u(d;H)].          (4)
```

The integer dynamic programme can be strictly stronger than this separable rational bound. Its integral restriction is not replaced by a numerical tolerance.

## 3. Exact finite pressure envelope and receiver cuts

For a receiver box A_u>=0, define free_u=min(A_u,rho_u-1) and G_u=A_u-free_u. Let Psi_L(e_L;G) be the maximum of sum d_u over admissible integers 0<=d_u<=min(D_u,G_u), subject to (1). The dynamic programme stores maximum accumulated pressure for each used slack 0,...,J. It is exact for this independent-pressure/one-budget projection ONLY, not selected-matrix or graph realizability.

Let y be the incoming vector from a subset of sources in the SAME actual orientation whose full incoming vector is p. Then 0<=y_u<=p_u. Suppose also y_u<=A_u. Its pressure d'_u=(y_u-rho_u+1)_+ is at most d_u, at most G_u, and at most D_u. The admissible pressure sets are downward closed and gamma is nondecreasing, so d' satisfies (1). Since y_u<=free_u+d'_u, we obtain

>     sum_u y_u <= sum_u free_u + Psi_L(e_L;G).        (5)

The condition y_u<=p_u is essential. An arbitrary vector satisfying only the nominal box y_u<=A_u need not inherit the selected-incidence pressure constraints. The prior draft's phrase 'any incoming vector y<=A' omitted this domination condition in its prose; it is made explicit here rather than asserted for an unrestricted receiver box. Actual tail incoming vectors always satisfy it, so the intended graph-derived-tail implication, executable verifier, frozen arithmetic and exclusions are unchanged.

For T_tau={u:q_u>=tau}, take the interval upper box

```text
A_w=min(P_w, #{u!=w:tau<=q_u<=q_w+rho_w+1}).
```

A graph-derived orientation sends Q_tau=sum_{u in T_tau}q_u incoming units from those sources. Its actual incoming vector has y<=p and y<=A as required. If Q_tau exceeds (5), the branch is impossible. The interval box drops reverse compatibility in the SAFE upper direction. No universal high-q-tail sufficiency, equality of Hall minima or fixed-q monotonicity is assumed.

The coarser full-orientation balance is sum d_u>=Q-r+b=b+2t+D0+Esel. It can also be compared directly to Psi. The implementation retains exact free-cap losses through (5).

## 4. Three additional original-sample exclusions

The new verifier directly examines the NINE preceding non-rejections. Its parent full output is pinned by canonical JSON SHA256 `7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e`. Previously rejected branches remain covered by that earlier proof; every other branch is tested here. No branch is silently omitted.

| Original sampled row | Low-demand threshold eta | New branches completing prior coverage |
|---|---:|---|
| 240 | 2 | e_L=41,...,45; earlier e_L=39,40 already excluded |
| 258 | 2 | e_L=42,...,48; earlier e_L=38,...,41 already excluded |
| 342 | 3 | e_L=35,...,41; earlier e_L=33,34 already excluded |

The cumulative SAME 713-row sample becomes **707 rejected / six not rejected**. Remaining rows are **108,160,338,347,471,586**. They are sampled relaxed profiles, NOT six remaining cases of the conjecture or a three-state reduction of the canonical 3,607-state frontier.

### Hand-readable row-240 branch

At eta=2,e_L=41, outside excess is H=4 and spare low-block selections are J=2. At tau=1 the tail needs 104 units and free receiver capacity is 28. Seventeen receivers can each contribute four pressure units for zero slack; one contributes two; four contribute one each. This gives 74 pressure units without spending slack.

With only TWO slack available, every affordable move above that zero-slack baseline adds at most one pressure unit and costs two slack. Moves that would gain more require at least three slack and are unavailable in this branch. Thus

```text
incoming <= 28+74+1 = 103 < 104.
```

The complete exact new branch table is

```text
e_L:           41  42  43  44  45
incoming cap: 103 101 102 102 102
demand:       104 104 104 104 104.
```

Earlier price certificates cover e_L=39 and 40 by 224>209 and 224>212. This gives complete coverage, not one representative branch treated as the whole profile.

**Documentation correction:** the initial draft said every further pressure unit costs two slack without restricting to affordable moves. That statement is too broad: a move costing three slack can buy several units, but is unavailable when J=2. The corrected argument above states the actual budget restriction. The draft's row-44 bound 103 was a valid conservative upper bound; the exact computed maximum is 102. The theorem, executable verifier, frozen hash and exclusions were unchanged. The initial wording remains in Git history.

## 5. Soundness checks and hostile boundaries

Completed standard-library checks comprise 9,293 exhaustive actual selected-incidence configurations; 25,391 arbitrary label-block checks, including 12,305 with positive slack; 10,000 fresh random-incidence trials, of which 7,839 satisfy the stated source/label constraints; 3,000 independent brute-force comparisons covering 237,067 pressure vectors; and all three standing hostile q-tail examples.

The incidence tests include empty/full blocks, arbitrary blocks rather than only prefixes, zero demands and pressure, individual ceilings and simultaneous partition-cap checks. These incidence systems need not satisfy the positive-surplus scalar ledger; the separate fresh synthetic experiment below does. The domains must not be conflated.

The tempting stronger claim sum_u(q_u-k_u)d_u<=H is FALSE: two sources can share one positive label. X=[[1,0],[1,0]], s=[1,0], rho=[1,1], low block={the zero label}, pressures[1,1] has H=1 but total high-incidence charge 2. The valid theorem charges selected PLACES in the low block, not distinct excess falsely counted once across all sources. This actual-incidence hostile fixture is retained; it is not a positive-surplus graph.

The full new result canonical JSON SHA256 is `35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6`. The complete committed output includes non-excluding ranges and every final slack-DP table used in new certificates.

## 6. Simultaneous block experiment: no further profile closure

For a partition into equal-demand blocks of sizes n_j and exact shared excess totals E_j, a source with pressure d>0 can select at most min(n_j,floor(E_j/d)) labels from eligible positive block j. Zero-demand blocks contribute their eligible label count without that restriction. Thus q_u cannot exceed the sum of these per-block allowed counts. All blocks must use ONE vector (E_j).

Enumerating the surviving consistent block-total tuples and coupling these source caps with exact block-total charge-envelope constraints tested 597 tuples on the six remaining profiles. Of these, 25 failed total capacity and 118 failed a priced bound; 454 tuples remain across all six profiles. **No additional profile was fully excluded.** The deterministic exploration is reproducible from the committed inputs and source, with its complete-output digest recorded separately.

This is not a proof of joint incidence feasibility, nor exhaustion of all multiblock inequalities. The full multiresource version of (1) remains a further route; this experiment did not solve that general optimization.

## 7. Fresh seeded scalar-bridge reconnaissance

Before inspecting results, fresh seed 74220260919 was fixed for the preserved generator, keeping its domain and stopping rules unchanged. It ran 100,000 trials: 44,451 scalar-domain trials, 5,539 cap passes, 1,496 incidence passes and 715 pair-flow passes, 53 with zero-demand labels. This is the SAME generator with a new seed, not independently designed generation or realized canonical graphs.

Corpus SHA256: `f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e`.

```text
capped-spill rejections:                701
additional block-pressure rejections:    3
additional conditioned rejections:       1
additional shared-slack rejections:      3
not rejected:                            7
total:                                 715.
```

The new shared-slack rows in this FRESH corpus are 163,362,687, not the same row namespace as the original 713 sample. Its seven non-rejections are 20,91,391,490,528,562,677. Their full arrays and the three complete new branch certificates are retained. Fresh full-output canonical SHA256: `754774a0d4fdb23c8403efe4c5e41f2df950ebf933f903ca7e3d335d6ce370f9`.

## 8. Scope and next question

No previous proof, verifier or counterexample was removed. The canonical promoted frontier stays 1,971 exclusions / 3,607 survivors / 977 whole-state closures. The 2,655 relational candidates remain behind complete coverage, dual agreement, zero unresolved states, a successful aggregate and a separate reviewed ledger step.

The next structural question is common selected-source usage across several blocks. Current per-label envelopes can still choose incompatible best sources. The explicit remaining profiles constrain that search. Retain the exact q-layer/mincut, crossing-wall and independent maximum-cut/stability routes. Internal arithmetic, remote CI and evidence publication remain distinct from external mathematical acceptance.
