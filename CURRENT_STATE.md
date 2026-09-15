# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**15 September 2026 — checkpoint `forced-core-capacity-v1`.** Inspected predecessor: `66a49c5a3d61937e7d8a9e92ca7d7ee0937f5a7e`. The fixed-neighbourhood labelled-routing criterion now gives a short receiver-capacity obstruction for the last two original synthetic non-rejections. In row160, ten `rho=1,q=3` sources are forced onto the same three selected labels; their three label classes require capacity10 each, while the only relaxed candidate receiver capacities are `5,5,5,4,4,4,4`, whose best possible minimum bin is9. In row338, ten `rho=1,q=2` sources are forced onto the same two labels, creating20 obligations against only `6+6+5=17` candidate receiver capacity. **Rows160 and338 are excluded, so the ORIGINAL synthetic sample is now 713/713 rejected. Canonical finite frontier remains4,626 exclusions / 952 survivors /3,632 whole-state closures. Fresh sample remains708/715 in its separate namespace.** External review remains OPEN.
<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged by the synthetic-sample closure

```text
whole-state closures:             3,632
canonical exclusions:             4,626
canonical survivors:                952
  N34-derived survivors:             949
  N35-derived survivors:               3
recovered relational candidates:  2,655 — AUDITED AND PROMOTED
```

The reviewed relational promotion remains the current canonical finite frontier. Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

## Original synthetic boundary sample — now 713/713

The predecessor singleton-destination theorem excluded rows347,471,586 and left rows160 and338. The new [`forced-core-capacity-v1`](project/research/general_n/2026-09-15-forced-core-capacity-v1/README.md) excludes both remaining profiles using selected-incidence eligibility plus the exact fixed-neighbourhood routing criterion.

Let

```text
A={i:s_i<=1}, h=|A|, U={u:rho_u=1 and q_u=h}.
```

Every `u in U` is forced to have `S_u=A`. For an obligation `(u,i)` to destination `v`, the retained routing theorem requires

```text
S_u minus N_v = {i},
S_v subset N_u,
```

with incoming capacity `c_v=rho_v+b-a-1`. Hence any receiver of a forced-core obligation must satisfy

```text
v not in U,
q_v<=h,
q_v+rho_v>=h-1.
```

Moreover each fixed receiver can serve at most one core label because `A minus N_v` has a unique singleton value. Thus its whole incoming capacity is indivisible across the core-label classes.

Exact profile certificates:

```text
row160:
  core labels             0,1,2
  forced sources          0,1,2,3,13,16,17,19,25,26
  relaxed receivers       4,9,10,14,15,18,22
  capacities              5,5,5,4,4,4,4
  required per label      10
  best possible min bin    9   => EXCLUDED

row338:
  core labels             0,1
  forced sources          6,7,9,10,11,14,15,22,26,27
  relaxed receivers       0,1,3
  capacities              6,6,5
  required obligations    20
  total receiver capacity 17   => EXCLUDED
```

The row160 contradiction also has a one-line pigeonhole proof: seven receivers split over three labels force at least two labels to use at most two receivers; a two-receiver bin reaches10 only as `5+5`, which would require four capacity-5 receivers, but only three exist.

The standard-library verifier enumerates every receiver-label assignment and a 290-pattern tiny structural challenge. Frozen canonical parsed-result SHA256:

```text
8784209ee05bb1ec6cd6da559e8845dbfeee3e041a96dcce9f41360c6d12920e
```

Local exact replay passed. Dedicated remote CI is installed by this checkpoint and **must not be called successful until inspected**.

## Singleton and row471 history — preserved

The preceding [`singleton-destination-trap-v1`](project/research/general_n/2026-09-15-singleton-destination-trap-v1/README.md) remains an independent structural result. It excluded original rows347,471,586 by forcing `(q,rho)=(1,1)` sources onto `q<=1` destinations and then exposing unordered-pair Hall deficiencies. Its dedicated workflow34910561258 completed SUCCESS.

Earlier row471 exact work remains useful independent evidence:

- `e_L=39,40`: conditioned rigidity closure, remote run34906169745 SUCCESS.
- `e_L=41`: independent high-block/common-pressure contradiction.
- `e_L=42,43`: exact source-group split with `214<222` and `215<222`; remote run34909572352 SUCCESS.

The singleton theorem superseded the need to attack `e_L=47`, but none of those predecessor packages is deleted.

## Exact row108 finish — remotely reproduced

Row108 remains excluded by its separate selected-incidence/source-sharing route. Its standard-library verifier enumerates46,662 excess histograms, leaves1,201 row/type-incidence-feasible histograms, disposes of1,124 by exact incidence-charge flow below211, and sends77 to exact common-pressure branch-and-bound.57,867 branch nodes are visited; none attains211. Remote workflow34906766833/job104185160249 completed SUCCESS.

## Fresh namespace — deliberately separate

The fresh seed sample remains **708/715 rejected** with seven retained profiles in its own namespace. Neither the singleton nor forced-core checkpoint changes that count until those seven profiles are explicitly scanned. Do not mix row namespaces.

## Immediate next target

The original 713-profile laboratory is now closed under the accumulated necessary conditions. The next useful work is therefore structural rather than more original-sample grinding:

1. scan the seven retained fresh-seed profiles with the singleton and forced-core receiver-capacity lemmas, preserving all non-rejections;
2. generalize the forced-core argument from `rho=1` to low-eligibility cores at arbitrary residual level `r`;
3. test the resulting theorem against the 952 canonical survivors, without promoting anything beyond its proved scope;
4. continue external review of the canonical graph-to-selected/residual bridge and the fixed-neighbourhood routing theorem on which this synthetic closure depends.
<!-- CURRENT-STATUS:END -->

## Preservation, failures and audit gates

The complete pre-row108 handoff remains preserved byte-for-byte in [`CURRENT_STATE_PRE_ROW108_2026-09-14.md`](CURRENT_STATE_PRE_ROW108_2026-09-14.md); earlier archives, reviewer packages, counterexamples and negative experiments remain intact.

Historical failures remain failures: source-price transfer run34904353492, N30 navigation run34906766832, the red-team-history guard failure34908428824, and standalone row471 process commit `2667a909...` are not repainted by later repairs. The branch-specific charge route did not itself finish row471; the singleton-destination theorem is a distinct stronger structural argument. The forced-core theorem is another distinct successor and does not retrospectively turn earlier uncoupled witnesses into graph realizations.

The 2,655 relational candidates have cleared complete coverage, dual agreement, zero unresolved cases, successful aggregate and the separate reviewed-ledger step. Their promotion changes the canonical finite frontier. Synthetic sample exclusions, including the new 713/713 closure, **do not** change it.

Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge, selected-incidence eligibility, destination capacities and the fixed-neighbourhood labelled-routing criterion.
