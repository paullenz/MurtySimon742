# Conditioned source pricing: exact row budgets on the surviving branches

14 September 2026. **Continuation of the source-price and shared-slack routes. Exact algebraic bound plus deterministic standard-library reconnaissance; external mathematical review OPEN. No new profile, canonical-state or unrestricted Murty–Simon exclusion.** This package is separate from both the original [source-price package](../2026-09-14-source-sharing-v1/README.md) and the [stronger search / joint-witness package](../2026-09-14-source-pricing-witnesses-v1/README.md) so their complete negative results remain intact.

## Why this continuation is different

The original source-price experiment used an unconditioned excess domain. The next planned step was to combine the same exact row-budget dualization with the **same fixed block-excess total** and branch-specific legitimate caps already used in the conditioned/shared-slack pipeline. That is done here.

For one actual binary selected-incidence matrix `X_ui`, exact row sums are `sum_i X_ui=q_u` and exact column sums are `sum_u X_ui=s_i+e_i`. With source weight `alpha_u`, pressure ceiling `D_u=(P_u-rho_u+1)_+`, charge threshold `xi`, and arbitrary integer source prices `lambda_u`, define

```text
w_ui(e_i)=alpha_u*min(e_i,D_u) if s_i>xi, else 0.
```

Then

```text
C = sum_i sum_u X_ui w_ui(e_i)
  = sum_u lambda_u q_u
    + sum_i sum_u X_ui (w_ui(e_i)-lambda_u).
```

For fixed `e_i`, column `i` uses exactly `s_i+e_i` eligible sources, so its adjusted contribution is at most the sum of the largest `s_i+e_i` eligible adjusted scores. The dynamic programme maximizes these exact integer column scores over the existing total excess, prefix floors and **fixed low-block excess `e_L`**. Zero prices reproduce the corresponding conditioned top-source envelope exactly.

This is a safe Lagrangian upper bound. The finite price search is only a certificate finder; failure to find a contradiction is retained as a non-rejection. Rational prices are equivalent after clearing denominators, and a common additive source-price constant is a gauge because total selected incidence is fixed.

## Internal soundness audit

`verify_conditioned_source_pricing.py` reuses the previously committed cap, receiver and shared-slack modules and implements the priced conditioned envelope independently. The local deterministic audit completed:

```text
actual selected-incidence configurations:  9,293
priced charge inequalities:               24,063
strict improvements over zero price:         150
```

Every tested actual incidence charge is at most the priced envelope. Zero price agrees exactly with the preceding conditioned upper envelope. A retained strict fixture has two demand-one labels and four unit-row sources: the zero-price labelwise relaxation gives upper 2 by reusing the attractive source twice, whereas source price `[0,0,0,1]` gives upper 1 because that source's exact row sum is one.

## Complete targeted boundary scan

For each profile the verifier first applies all inherited conditioned and shared-slack branch tests. It chooses the demand threshold `eta` with the fewest surviving branches and applies source pricing to **every remaining `e_L` branch** at that threshold. The two most promising standing charge systems are tested with deterministic integer price search and local coordinate refinement near a possible contradiction.

This search is finite and is not claimed exhaustive over all price vectors or all `eta`; any strict contradiction it finds is valid, while a failure is merely a non-rejection.

### Original namespace

| Row | target `eta` | source-price branches tested | remaining `e_L` after pricing |
|---:|---:|---:|---|
| 108 | 2 | 5 | 33,34,35,36,37 |
| 160 | 1 | 2 | 33,34 |
| 338 | 1 | 5 | 28,29,30,31,32 |
| 347 | 3 | 5 | 52,53,54,55,56 |
| 471 | 2 | 6 | 39,40,41,42,43,47 |
| 586 | 2 | 4 | 45,46,47,52 |

**No original profile is newly excluded.** The most informative tightening is row 471:

```text
e_L=39: zero-price upper 232 -> priced upper 225; receiver lower 224; gap -1.
e_L=40: zero-price upper 230 -> priced upper 225; receiver lower 223; gap -2.
```

For both branches the retained best price vector puts price 1 on source indices 9 and 23 and zero on all other sources. This is a near miss, not a certificate. It says the exact row budgets account for almost all of the remaining relaxation gap on these two branches.

### Fresh-seed namespace

The seven fresh shared-slack non-rejections are tested **separately**, preserving their distinct row namespace.

| Fresh row | target `eta` | source-price branches tested | remaining `e_L` |
|---:|---:|---:|---|
| 20 | 2 | 3 | 37,38,39 |
| 91 | 1 | 2 | 26,27 |
| 391 | 1 | 4 | 21,22,23,24 |
| 490 | 2 | 2 | 54,55 |
| 528 | 2 | 6 | 26,27,28,29,30,31 |
| 562 | 0 | 7 | 15,16,17,18,19,20,21 |
| 677 | 1 | 7 | 14,15,16,17,18,19,20 |

Again **no profile is newly excluded**. Fresh row 391 improves its four tested branch upper bounds by 4,3,2,1 units respectively but remains far from contradiction; fresh row 528 gains one unit on one branch. Other tested fresh branches are zero-price optimal in this finite search.

## Exact output and scope

The complete deterministic local output is reproducible from committed inputs and code. Its canonical file SHA-256 is

```text
1aec5dc47102ec24f64cc9776c624b32d025112b06fb643f306a0768e091639a
```

`RESULT_SUMMARY.json` records every target threshold and surviving branch, the row-471 near-tight data and the audit totals. The workflow generates the complete full JSON, checks this exact hash and uploads it as an artifact. Until that remote run is inspected, the result is local/internal rather than remotely replayed.

These are synthetic necessary-condition profiles, not actual graphs or canonical scalar states. Original sample stays 707/713 rejected, fresh stays 708/715 rejected, and the canonical promoted frontier stays **1,971 exclusions / 3,607 survivors / 977 whole-state closures**. The **2,655 recovered relational candidates remain UNPROMOTED** behind their separate audit gate.

## What this negative result teaches

Source pricing is a genuine exact strengthening, but most boundary branches are already zero-price optimal. Row 471 is different: exact row budgets remove seven and five units and leave margins only one and two. That makes it a high-value target for the next structural step.

The next attack should therefore retain **one actual selected-incidence matrix** and its row/column sums while imposing the stronger selected-label/destination constraints identified by the sibling joint-witness work. In particular, inspect row-471 `eta=2`, `e_L=39,40` for source saturation / Hall-type obstructions and for the shared residual-neighbourhood condition. Do not simply broaden a blind price search. Equality branches such as original row338 should likewise be treated as rigidity targets, not as evidence of realizability.
