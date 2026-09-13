# Audit and failure record — alternative attacks v1

13 September 2026. This file records positive findings, invalidated routes, scope boundaries and the later state-227 whole-state closure. **External mathematical review and independent reproduction remain OPEN.**

## 1. Corrected switching interpretation

The earlier pair-overlap replay repaired 23 selected-incidence matrices by degree-preserving two-source/two-label switches. Those switches preserve the abstract row and column margins and the tested eligibility condition.

They are **not automatically legal switches between quasi-edge representatives in an actual graph**. A switched cross-edge may fail the exact total-domination condition needed to represent the corresponding missing B-pair. Therefore the initial idea of treating the entire transportation fibre as freely switchable in a real graph was too strong.

Current correction:

- use the transportation fibre only inside explicitly relaxed/all-geometry models;
- when making graph-level statements, either retain actual candidate availability or use selection-free consequences such as the raw candidate-capacity lemmas in `SELECTION_FREE.md`.

No active theorem relies on the invalid stronger switching interpretation.

## 2. Maximum-cut direct-injection failure

The exact identity `e(G)=|X||Y|+I-M` makes `I<=M` an attractive target. A direct matching proof assigning each internal edge to a uniquely witnessed missing cross-pair is false.

- Deterministic local reconnaissance found an order-eight D2C example with a maximum-cut internal edge lacking the required direct cross witness.
- Independently, the public Erdős-Lean #742 project records a definition-checked order-ten obstruction and a verifier for the same proposed matching architecture:
  https://github.com/edisonymy/erdos-lean-research/blob/main/experiments/erdos742/RESULTS.md

This kills the naïve injection, not the aggregate `I<=M` inequality. The maximum-cut route remains exploratory at the global charging/stability level.

## 3. Maximum-cut finite evidence boundary

`MAXCUT_RECON.json` records zero violations among 728 D2C instances through order 12 (21 exhaustive atlas instances through order 7 and 707 deterministic generated instances at orders 8-12), plus 2,226 sampled positive C5 blow-ups through order 30.

These checks do not establish completeness at orders 8-12 and do not prove any all-order theorem. The generated graphs are deterministic under the recorded seed but are only a sample.

The degree-square diagnostic is retained only as a negative control because that inequality is already known false in general.

## 4. Geometry-model solver boundary

An exploratory broad state-227 integer formulation timed out without an incumbent. This is **not** evidence of infeasibility and is not used as a proof event.

A reduced fixed-margin integer formulation later returned an infeasible status. That status motivated the case split but is not itself an accepted certificate. The accepted margin-class result is the hand argument in `MARGIN_CLASS_EXAMPLE.md`.

The later whole-state closure in `STATE_227_WHOLE_STATE.md` also does **not** use any solver infeasibility status. It consists of exact finite enumeration plus hand inequalities.

## 5. Direct small-graph challenge boundary

`verify_selection_free_small.py` reconstructs the definitions directly on 728 D2C graphs (21 atlas graphs through order 7 and 707 deterministic generated graphs at orders 8-12), across 1,169 minimum-degree complement roots. It checks 3,856 candidate quasi-edges, 77,696 universal `|K_u|` subset inequalities and 2,338 deterministic legal representative systems for the selected-excess inequality, with zero violations.

Crucially, all 1,169 tested roots have `t<=0`. Therefore this experiment does **not** challenge the positive-surplus sharpening `q_u<=c_u-1` or the `kappa_u=min(c_u-1,|K_u|)` subset bound. The hand proof, not finite testing, is the basis for that sharpening.

## 6. Hand lemmas and dependency boundary

The following candidate hand statements are active in this checkpoint:

1. raw candidate quasi-edge restrictions `d_i<=c_u-1` and `C_i>=mu_u`;
2. candidate-capacity subset inequality `e(overline{H[B]}[U])<=sum_(u in U) kappa_u`;
3. selected-excess inequality `p_u-rho_u+1<=x_i-s_i` on a selected positive-demand incidence;
4. its summed version and exact-demand corollary `p_u<=rho_u-1` for active sources;
5. exact-demand interval realization `q_u+p_u<=C_i<=rho_u+q_u-1`;
6. threshold consequence: if `h_l=#{i:x_i-s_i>=l}`, then `q_u>h_l => p_u<=rho_u+l-2`;
7. all-selected-geometries exclusion of the saved state-227 exact-demand margin class;
8. all-q exact-demand exclusion for state 227;
9. whole-state exclusion of state 227 after the complete excess analysis.

Items 3-6 are short consequences of the canonical bridge and inherit every correctness dependency of that bridge. Items 1-2 are rederived directly from the raw candidate quasi-edge definition but still depend on the complement/quasi-edge implication from diameter-two edge-criticality.

External review and novelty assessment remain open.

## 7. State-227 whole-state arithmetic boundary

`STATE_227_WHOLE_STATE.md` divides the proof into three disjoint excess regimes.

### E=0,...,20

`verify_state227_exact_to20.cpp` enumerates every excess profile up to permutation within the demand-two and demand-three classes, every allowed source selected-degree vector and the exact minimum incoming assignment under the stated excess restrictions.

Recorded totals:

```text
49,847 profiles,
40,548 strict exclusions,
9,297 source-infeasible profiles,
2 equality profiles.
```

The two equality profiles are exactly the previously preserved E=6 and E=7 cases. The finite envelope alone does not exclude them; the endpoint-rigidity hand arguments in `EXCESS_SWEEP_TO_8.md` are proof-critical.

### E=21,...,34

The tail proof deliberately uses a weaker source cap than is actually available. If `h=#{i:e_i>=2}`, a `rho=3` source with `q>h` has `p<=3`; when `q<=h` the verifier retains only the basic `p<=5` cap. It ignores the stronger `p=5` excess-three requirement and other profile restrictions.

For each E, q-vector and h, `verify_state227_tail.cpp` exactly minimizes source load and exactly maximizes the permitted top-k endpoint correction over all label excess allocations. All fourteen E-layers have strictly positive global gaps; the minimum is 8 at E=21.

### E>=35

The basic incoming caps alone give

```text
sum p <= 7*3+1*4+10*5=75,
```

whereas `sum p=41+E>=76`. No enumeration is used here.

The three regimes cover every `E>=0`; hence the state-227 exclusion is a genuine whole-state claim, conditional on the canonical bridge.

## 8. Frontier interpretation

Before the state-227 closure, the frozen generalisation record was

```text
994 exclusions / 4,584 survivors.
```

State 227 was one of those survivors. The new record is therefore

```text
995 exclusions / 4,583 survivors,
```

with 4,505 N34 equality-derived survivors and 78 N35 survivors.

This must not be confused with the fixed-order N34 theorem candidate, which was already closed independently. The new result is evidence about the reach of the general quantified machinery.

## 9. Repository/tooling note

During earlier tool-interface probing an unreferenced Git tree/commit object was created without moving any branch ref. `main` remained unchanged. It is not part of the research history and no tracked repository file was modified by that probe.

During the present closure work temporary research branches were also created before publication. Only commits ultimately fast-forwarded to `main` are part of the canonical history; unused branch refs carry no mathematical status.

## 10. Claims deliberately not made

This checkpoint does **not** claim:

- a proof of the unrestricted Murty–Simon conjecture;
- that the remaining 4,583 scalar states are realizable graphs;
- that arbitrary degree-preserving switches correspond to legal quasi-edge switches in a graph;
- that the maximum-cut inequality `I<=M` is proved;
- that solver timeout or infeasibility is proof;
- that N34/N35 fixed-order candidate ledgers require modification;
- that the state-227 finite arithmetic has received independent computational reproduction or specialist mathematical acceptance.
