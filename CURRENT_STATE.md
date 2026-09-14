# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**15 September 2026 — checkpoint `row471-e42-e43-common-pressure-v1`.** Inspected predecessor: `2c640dcb2226bd4a6d056dc9da46cc4be9a53bc1`. The independently verified row471 `e_L=41` closure is preserved. A separate exact source-group common-pressure split now closes conditioned branches `e_L=42,43`, with total charge uppers `214,215` against the inherited exact receiver lower `222`; the same verifier independently rechecks `e_L=41` at `213<222`. **Row471 itself remains open only on `e_L=47`; original synthetic sample remains 708/713. Canonical finite frontier remains 4,626 exclusions / 952 survivors / 3,632 whole-state closures.** External review remains OPEN.
<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — promoted current frontier

```text
whole-state closures:             3,632
canonical exclusions:             4,626
canonical survivors:                952
  N34-derived survivors:             949
  N35-derived survivors:               3
recovered relational candidates:  2,655 — AUDITED AND PROMOTED
```

Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

## Relational validation lane — promoted

Discovery/recovery run `34844403328` and independent audit run `34854911792` cover the exact same 2,655-key set (SHA256 `67593252e0bc27766c24c8bf38060c8b0f98384a6f61fc02ac1e25fafb0ecfa2`), with zero unresolved states and successful two-implementation aggregate agreement. The separate reviewed ledger step confirmed zero overlap with the pre-existing ledgers and promoted 2,580 N34 plus 75 N35 closures. The remaining relational frontier is 952 states: 949 N34 and 3 N35. See the promotion audit in the alternative-attacks package. This remains finite evidence conditional on the canonical bridge, not an unrestricted proof.

## Boundary-profile status

The shared block-slack package had rejected707/713 original synthetic profiles and708/715 fresh profiles. The row108 [`conditioned-source-sharing-v1`](project/research/general_n/2026-09-14-conditioned-source-sharing-v1/README.md) exclusion raises the ORIGINAL sample to **708/713 rejected**, with exactly **160,338,347,471,586** not rejected. This is sample-level evidence only. The fresh sample remains **708/715 rejected** in its separate namespace. No canonical whole-state closure follows from that sample result.

For row471, the earlier rigidity step closed conditioned branches `e_L=39,40`; run34906169745 completed SUCCESS and passed the exact conditioned scan, frozen-output digest check and rigidity verifier. The independently developed [`row471-e41-v1`](project/research/general_n/2026-09-15-row471-e41-v1/README.md) closes `e_L=41` by a shared high-excess/common-pressure incidence contradiction `28>24`. The new [`row471-e42-e43-common-pressure-v1`](project/research/general_n/2026-09-15-row471-e42-e43-common-pressure-v1/README.md) closes `e_L=42,43` by an exact source-group split: the `rho=2` symmetry DP has charge maxima `44,54`, the high-source nested-excess DP has maxima `38,29`, and the `rho=1` contribution is at most132, giving `214<222` and `215<222`. Its `e_L=41` calculation `213<222` is only an independent regression. **Only `e_L=47` remains for row471.**

## Row471 `e_L=42,43` exact common-pressure split

At `eta=2`, the low block has base demand13. Sources divide into 12 sources with `rho=1` and total row sum33, four sources with `rho=2` and row sums `7,4,4,3`, and nine sources with `rho=3` and total row sum45. Every `rho<=2` selection is low-block, so for branch excess `e_L`, the high sources use exactly

```text
L=e_L-38
```

low selections, while the twelve demand-three labels have total excess

```text
H=47-e_L.
```

For `e_L=41,42,43`, `(L,H)=(3,6),(4,5),(5,4)`. The inherited exact receiver certificate with `charge_eta=0`, uniform source weight, `tau=1`, `theta=5` gives `free=22`, `penalty=148`, and hence the same lower bound

```text
C=sum q_u d_u >= 5*(96-22)-148 = 222.
```

The twelve `rho=1` sources have pressure ceiling4, so contribute at most132. For the four `rho=2` sources, an exact symmetry DP tracks selected degree and maximum selected-source pressure on the four demand-two labels; the shared high-source low-slot budget gives exact safe maxima `36,44,54`. For the nine `rho=3` sources, sorting high-label excesses and maximally nesting pressure requirements gives exact safe maxima `45,38,29`. Thus the combined safe upper bounds are

```text
e_L=41: 132+36+45=213 < 222  (independent regression)
e_L=42: 132+44+38=214 < 222  (new closure)
e_L=43: 132+54+29=215 < 222  (new closure)
```

The exact standard-library replay passed locally. Frozen canonical parsed-result SHA256 is `b2f2b8f1f714eb11225c07d9a9595154a7c53523b5d8da74be8a2028c170cc15`. A dedicated remote workflow is installed by this checkpoint and is **not called successful until inspected**.

## Exact row108 finish — remotely reproduced

For row108, shared-slack gives cumulative ranges `e_{s<=1}=26..33` and `e_{s<=2}=33..37`, hence40 monotone exact block-total tuples. Replaying the preserved simultaneous-multiblock screen rejects8 and leaves32. One fixed signed source-price vector closes24; the final eight require unit charge at least211 under one common source pressure.

The standard-library verifier enumerates **46,662** excess histograms, leaves **1,201** exact row/type-incidence-feasible histograms, disposes of **1,124** by exact incidence-charge flow below211, and sends the remaining **77** to exact common-pressure branch-and-bound. **57,867** branch nodes are visited; none attains211. Complete verifier output canonical SHA256: `5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629`.

Local replay passed before publication. Remote workflow **34906766833**, job **104185160249**, completed **SUCCESS**; its `Exact conditioned row-108 replay` step also completed SUCCESS. Status-sync run34906766824 and reviewer-navigation run34906766838 likewise completed SUCCESS on the predecessor row108 commit.

## Failure preservation and documentation repair

N30 reviewer-v3 package run **34906766832** on predecessor `010ea199...` FAILED at `Check complete proof tables, current links and release hashes`. Its log shows the specific assertion `releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf`: the predecessor's condensed protected reviewer section had retained package README links but removed the explicit frozen PDF paths required by the N30 integrity checker. No N30 proof or release bytes were changed. The row108 receipt commit restored the full n25–n30 manuscript/verification PDF navigation. The failed run remains failed and is not repainted green.

The root README has regained the earlier hostile/red-team history that had been lost during later condensation: the real n29 grouped-model normalization defect and correction, blind external-AI n29 challenge and resulting analytic hardening, Fan-dependency challenge and Fan-free replacement, fixed-order adversarial replays, and general7/12 hostile audit. The restored block is guarded by `tools/check_readme_review_materials.py`. Standing orders now require README updates to be additive/reconciliatory; substantive historical content must not be silently deleted or compressed.

Strengthened guard run **34908428824** remains FAILED. Its failure was navigational, not mathematical: `START_HERE_FOR_REVIEWERS.md` existed at the README top but not inside the protected `REVIEW-MATERIALS` block. The subsequent repair adds that link inside the protected block and does not weaken the red-team-history checks.

The standalone research-note commit `2667a909...` is also retained as a process failure against the every-commit paired-status rule. Later checkpoints correct the live surfaces and add exact verification rather than rewriting that predecessor as compliant.

## Immediate next target

Attack the final row471 branch `e_L=47`. It is structurally different from `41–43`: all selected excess is in the low block and the inherited best charge system uses `charge_eta=2`, so the exact `C>=222` lower bound above is unavailable. The next attack should impose selected-label/destination compatibility and the bridge's **ONE shared residual neighbourhood per source**, rather than extrapolating the charge split outside its valid domain. In parallel, carry exact common-pressure/source-incidence across the other retained original profiles. Preserve every non-rejection and keep the fresh namespace separate.

For a canonical arc `u->w` and selected-label sets `S_u,S_w`, retain

```text
1 <= |S_u minus S_w| <= rho_w+1,
|S_w minus S_u| <= rho_u,
| (union_{w:u->w} S_w) minus S_u | <= rho_u.
```

The last line enforces one shared residual neighbourhood at each source. Full multiresource shared slack, exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability remain preserved alternatives.
<!-- CURRENT-STATUS:END -->

## Preservation and audit gates

The complete pre-row108 handoff is preserved byte-for-byte in [`CURRENT_STATE_PRE_ROW108_2026-09-14.md`](CURRENT_STATE_PRE_ROW108_2026-09-14.md); earlier archives, reviewer packages, counterexamples and negative experiments remain intact.

The 2,655 recovered relational candidates have cleared complete coverage, dual agreement, zero unresolved cases, successful aggregate and the separate reviewed-ledger step. Their ledger promotion changes only the canonical finite frontier. Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge.

The root README is also part of the preservation surface. Its hostile/red-team audit history and reviewer-navigation blocks are protected content. Future status work must add/reconcile rather than erase; moving details to an archive is allowed only while retaining a substantive root summary and direct links, unless the user explicitly requests removal or compression.
