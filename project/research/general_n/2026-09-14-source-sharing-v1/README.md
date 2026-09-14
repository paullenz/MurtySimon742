# Source-priced selected-incidence charge

14 September 2026. Continuation of the [committed source-sharing plan](PLAN.md). **An exact necessary bound under explicit selected-incidence hypotheses, with finite internal checks. External mathematical review and novelty assessment OPEN. No new profile or whole-state exclusion.** The pricing argument is elementary row-budget dualization; no claim of novelty is made for that device.

## 1. Retain one source budget while optimizing columns

Let X_ui be one binary selected-incidence matrix. Its source row sums are q_u and label column sums are x_i=s_i+e_i, with s_i,e_i>=0 and E=sum e_i. Sources satisfy rho_u>=1 and may select label i only if rho_u>=s_i. Let nonnegative pressures d_u and ceilings D_u satisfy d_u<=D_u and, at every selected positive-demand label, d_u<=e_i. Applying these hypotheses to a graph inherits the canonical selected/residual bridge and its external-review boundary. They do not, by themselves, characterize a graph.

Fix nonnegative source weights alpha_u and a charge threshold xi>=0. Define

```text
C_xi = sum_{u,i:s_i>xi} alpha_u*d_u*X_ui,
g_ui(e) = alpha_u*min(e,D_u) if s_i>xi, and 0 otherwise,
B_i = {u:q_u>0 and rho_u>=s_i}.
```

For any SIGNED rational source prices lambda_u, and any excess domain E_domain containing all actual admissible excess allocations,

> **Source-priced upper bound**
>
> ```text
> C_xi <= U(lambda)
> := sum_u lambda_u*q_u
>    + max_{e in E_domain}
>        sum_i Top_{s_i+e_i}{g_ui(e_i)-lambda_u : u in B_i}.       (1)
> ```

Top_k means the sum of EXACTLY k largest entries. Top_0=0; k>|B_i| is impossible. Negative shifted entries must not be discarded. The sum runs over ALL labels, including zero-demand and uncharged labels: their charge is zero but their source-price contribution need not be.

**Proof.** Endpoint forcing and the ceilings give C_xi<=sum_ui X_ui*g_ui(e_i). Subtract lambda_u at every selected incidence and restore it using the exact row equality sum_i X_ui=q_u:

```text
sum_ui X_ui*g_ui(e_i)
 = sum_u lambda_u*q_u + sum_i sum_u X_ui*(g_ui(e_i)-lambda_u).
```

Each column contains exactly s_i+e_i distinct eligible sources. Its shifted sum is bounded above by the corresponding Top term. Finally maximize over a domain containing the actual excess allocation. This proves (1). Signed prices are legitimate because restoration uses equality, not an inequality on source usage.

Zero prices recover the corresponding independent top-source envelope on the SAME excess domain. Taking the minimum over any finite family that includes zero cannot weaken that particular envelope. It need not dominate every earlier conditioned or shared-slack test, and finite price search need not find the best bound.

## 2. Exact excess dynamic programme

The implemented domain retains integer e_i>=0, sum e_i=E, selected-column ceilings s_i+e_i<=|B_i|, and all forced label-prefix floors. Sort labels by s. For a prefix L_j, every source must place at least

```text
f_uj = (q_u - #{eligible labels outside L_j})_+
```

selections in that prefix. Therefore sum_{i in L_j}(s_i+e_i)>=sum_u f_uj. This is safe for every labelled prefix, including prefixes splitting an equal-demand block. The programme stores the maximum shifted score at each processed prefix and exact used excess. Impossible states are absent, not rounded to zero; negative finite scores remain finite. A fixed-prefix exact-excess branch is supported, but the recorded six-profile experiment does not use conditioning.

All executable arithmetic is integer: rational prices use signed numerators and one positive denominator, and upper_scaled/scale is the exact upper bound. The implementation uses integer nonnegative weights; rational nonnegative weights can be handled by clearing denominators first.

The DP is exact for this column/excess projection, NOT for a common incidence matrix, common pressure realization, or graph. Its reconstructed relaxed source counts can differ greatly from q. Those discrepancies propose later prices; they are not incidence witnesses.

## 3. A strict hand example, and why restoration matters

Use q=[1,1,2], rho=[1,1,1], s=[1,1], D=[1,1,1], E=2 and alpha=[10,1,1]. The actual selected matrix

```text
X = [[1,0], [0,1], [1,1]], e=[1,1], d=[1,1,1]
```

has charge 13. The zero-price column envelope is 22, because each column independently reuses the high-weight first source. Prices lambda=[9,0,0] give shifted score 2 per column and row restoration 9, so U=2+2+9=13. The price bound is strictly tighter and attains this actual incidence charge.

Omitting row restoration would falsely give 4<13. This counterexample is explicitly tested. A zero-demand signed-price fixture and an impossible empty-prefix branch are also retained. These are selected-incidence illustrations, not positive-surplus canonical profiles or Murty–Simon graphs.

## 4. Receiver lower bound used in this first experiment

For full incoming p with sum p=Q=sum q, 0<=p_u<=P_u and d_u=(p_u-rho_u+1)_+, put

```text
free_u=min(P_u,rho_u-1),
D_u=(P_u-rho_u+1)_+,
R=(Q-sum free_u)_+.
```

Since p_u<=free_u+d_u, sum d_u>=R. With z zero-demand labels, each source has at least (q_u-z)_+ selected positive-demand labels. Consequently, for xi=0,

```text
C_0 >= min sum_u alpha_u*(q_u-z)_+*d_u,
         over integer 0<=d_u<=D_u and sum d_u>=R.              (2)
```

The coefficients are nonnegative, so the minimum is obtained by buying R cheapest pressure units, respecting the D_u unit capacities. If fewer than R units exist, the receiver projection is impossible and requires separate reporting. This is a coarse full-incoming lower bound, not a high-q-tail sufficiency theorem. It explicitly covers row338's zero-demand label.

An exclusion requires the exact strict comparison lower>U. Equality or non-contradiction is a non-rejection, never a graph construction.

## 5. Original-six experiment: four upper-bound improvements, zero closures

The input is the already committed [original twelve-row remainder](../2026-09-14-block-pressure-v1/REMAINDER_12.json), Git blob `70b6fb160c82179c52ef8d88be673a4a729016a4`. Only original rows108,160,338,347,471,586 are selected. A local minimal transcription of the six used arrays is also preserved in ORIGINAL_SIX_INPUT.json; the remote replay uses the canonical twelve-row input and compares every result value.

For each row, 48 price vectors are tested for each of two weight vectors: alpha=1, and alpha=1 for q<=2 / 3 for q>2. Prices have denominator2, start at zero, and update by a deterministic source-count discrepancy step. Numerator steps are4 for iterations0–11,2 for12–23,1 thereafter. Source-index tie-breaking is fixed. The 576 evaluated price vectors are a finite heuristic, not optimization completeness. Every score and retained bound is exact, and the best price is replayed separately.

| Original row | Unit lower | Unit upper, zero/best | Weighted lower | Weighted zero-price upper | Best tested weighted upper |
|---|---:|---:|---:|---:|---:|
| 108 | 211 | 235 / 235 | 457 | 705 | 677 |
| 160 | 144 | 172 / 172 | 360 | 516 | 516 |
| 338 | 63 | 155 / 155 | 89 | 445 | 445 |
| 347 | 289 | 381 / 381 | 809 | 1,143 | 1,127 |
| 471 | 222 | 248 / 248 | 570 | 738 | 1,441/2 |
| 586 | 201 | 350 / 350 | 447 | 990 | 982 |

**All six remain unexcluded.** Four weighted upper bounds improve against their own zero-price baseline, but this first projection is not claimed stronger than the full earlier conditioned/shared-slack pipeline. All unit-weight searches retain zero as best. Large non-improving exploratory steps and every complete score trace remain in [ORIGINAL_SIX_RESULTS.json](ORIGINAL_SIX_RESULTS.json), together with best signed price vectors, maximizing excess allocations and relaxed source counts. A failed price search is not evidence that a graph exists or that no stronger prices can work.

The fresh seven profiles were NOT retested here. Original sample707/713, fresh sample708/715, canonical1,971 exclusions /3,607 survivors /977 whole-state closures, fixed-order candidates and the2,655 unpromoted candidates are unchanged.

## 6. Internal verification and reproducibility

[verify_source_prices.py](verify_source_prices.py) completed9,043 incidence/demand configurations: all binary matrices with1<=sources,labels<=3 and every compatible demand vector. For each configuration rho/caps/weights/signed prices are assigned deterministically; this does NOT exhaust all parameter assignments. The test checks that the actual matrix charge is bounded by (1), including zero-demand and uncharged labels.

A separately structured Cartesian excess enumerator matches the DP exactly in371 valid random small cases (282 nonempty projections) from600 attempts with seed74220260914 and E<=6. Three explicit hostile/boundary checks include the missing-restoration counterexample, zero-demand signed pricing and impossible fixed-prefix branch. [VERIFICATION.json](VERIFICATION.json) records these domains and counts. These are same-assistant internal checks, not external review or actual-graph enumeration.

From repository root:

```sh
python3 project/research/general_n/2026-09-14-source-sharing-v1/run_replay.py
```

This uses only the Python standard library, verifies input provenance and frozen result hashes, reruns every new test and all576 price evaluations, and compares both complete parsed JSON objects. No live artifact, numerical optimizer or network is required. At initial publication the new remote replay is not yet claimed passed; a later dated receipt must distinguish its result from the local checks and prior shared-slack CI.

## 7. Next structural test and preserved limitations

Combine source pricing with the SAME conditioned block-excess totals and branch-specific legitimate caps, retaining every possible branch. Then compare source-price bounds with sharper receiver lower bounds or common-pressure row-pattern constraints. Test the seven fresh profiles separately once the mechanism is fixed. The gap remaining in the six-profile table shows this first unconditioned/coarse pairing is not enough; it does not justify abandoning or promoting the larger approach.

The source budget is now priced globally, but independent per-column excess maxima and inconsistent pressures remain relaxations. Full multiresource shared slack and explicit common selected-incidence feasibility remain distinct successors. Preserve all previous failures, exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability routes, and all external-review and audit gates.
