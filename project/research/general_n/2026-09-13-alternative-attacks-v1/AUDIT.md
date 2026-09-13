# Audit and failure record — alternative attacks v1

13 September 2026. This file records both positive findings and invalidated/limited routes. **External mathematical review remains OPEN.**

## 1. Corrected switching interpretation

The earlier pair-overlap replay repaired 23 selected-incidence matrices by degree-preserving two-source/two-label switches. Those switches preserve the abstract row and column margins and the tested eligibility condition.

They are **not automatically legal switches between quasi-edge representatives in an actual graph**. A switched cross-edge may fail the exact total-domination condition needed to represent the corresponding missing B-pair. Therefore the initial idea of treating the entire transportation fibre as freely switchable in a real graph was too strong.

Current correction:

- use the transportation fibre only inside explicitly relaxed/all-geometry models;
- when making graph-level statements, either retain actual candidate availability or use selection-free consequences such as the raw candidate-capacity lemmas in `SELECTION_FREE.md`.

No theorem relies on the invalid stronger switching interpretation.

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

A reduced fixed-margin integer formulation later returned an infeasible status. That status motivated the case split but is not itself the accepted certificate. The accepted result is the hand argument in `MARGIN_CLASS_EXAMPLE.md`; `verify_margin_example.py` checks its arithmetic.

No whole scalar state is excluded by this checkpoint.

## 5. Direct small-graph challenge boundary

`verify_selection_free_small.py` reconstructs the definitions directly on 728 D2C graphs (21 atlas graphs through order 7 and 707 deterministic generated graphs at orders 8-12), across 1,169 minimum-degree complement roots. It checks 3,856 candidate quasi-edges, 77,696 universal `|K_u|` subset inequalities and 2,338 deterministic legal representative systems for the selected-excess inequality, with zero violations.

Crucially, all 1,169 tested roots have `t<=0`. Therefore this experiment does **not** challenge the positive-surplus sharpening `q_u<=c_u-1` or the `kappa_u=min(c_u-1,|K_u|)` subset bound. The hand proof, not finite testing, is the basis for that sharpening.

## 6. New hand lemmas and dependency boundary

The following candidate hand statements are new in this checkpoint:

1. raw candidate quasi-edge restrictions `d_i<=c_u-1` and `C_i>=mu_u`;
2. candidate-capacity subset inequality `e(overline{H[B]}[U])<=sum_(u in U) kappa_u`;
3. selected-excess inequality `p_u-rho_u+1<=x_i-s_i` on a selected positive-demand incidence;
4. its summed version and exact-demand corollary `p_u<=rho_u-1` for active sources;
5. exact-demand interval realization `q_u+p_u<=C_i<=rho_u+q_u-1`;
6. the all-selected-geometries exclusion of N34 state 227's saved `(q,x=s)` margin class.

Items 3-5 are short consequences of the existing canonical bridge and inherit every correctness dependency of that bridge. Items 1-2 are rederived directly from the raw candidate quasi-edge definition but still depend on the complement/quasi-edge implication from diameter-two edge-criticality.

External review and novelty assessment are open.

## 7. Repository/tooling note

During tool-interface probing an unreferenced Git tree/commit object was created without moving any branch ref. `main` remained unchanged. It is not part of the research history and no tracked repository file was modified by that probe.

## 8. Claims deliberately not made

This checkpoint does **not** claim:

- a proof of the unrestricted Murty-Simon conjecture;
- an improvement to the 994/4,584 whole-state generalisation frontier;
- that arbitrary degree-preserving switches correspond to legal quasi-edge switches in a graph;
- that the maximum-cut inequality `I<=M` is proved;
- that solver timeout or infeasibility is proof;
- that N34/N35 fixed-order candidate ledgers require modification.
