# n=29 Delta=16 — fully fresh finite verifier v1

8 September 2026. Prepared during the restarted red-team audit requested by Paul Lenz.

**Status: PASS in the development run; clean-runner replay supplied. Same-assistant independent implementation, not independent researcher reproduction, peer review, or formal verification. The n=29 theorem remains a CANDIDATE.**

## Purpose

The original n=29 Delta=16 exclusion reused the hash-pinned n=28 direct197 implementation. Its production replay is exact and heavily checked, but common implementation ancestry remained a material trust boundary.

This directory now supplies a second, end-to-end finite implementation for the two N=29 Delta=16 scopes. **The clean runtime uses no inherited Murty-Simon verifier/model module and no inherited prepared input.** It starts from the audited mathematical inequalities and independently generates the finite domains, propagates the joint states, builds the strongest endpoint relaxation, and verifies exact integer Farkas contradictions.

The point is not to claim a new theorem. It is to test whether the same candidate contradiction survives a materially separate implementation.

## Source

- `fresh_prepare.py` — exact charging-domain enumeration, residual-total bounds, source-count/support cuts, and exact-checked dual pruning.
- `fresh_rows.cpp` — third independently written residual-row enumerator and source-capacity scanner.
- `fresh_joint.py` — pure-Python joint-state engine: column DP, matching, Hall flow, pair Hall, and row-feasibility recurrence.
- `fresh_endpoint.py` — independently coded strongest endpoint LP and exact integer Farkas checker.
- `run_independent.py` — end-to-end orchestration, redundant boundary recounts, certificate generation and evidence packaging.

Generated evidence:

- `N29_INDEPENDENT_D16_STATES.json.gz` — all fresh joint survivors;
- `N29_INDEPENDENT_D16_CERTIFICATES.json.gz` — all accepted exact endpoint certificates;
- `MANIFEST.json` — source/evidence hashes and exact result summary.

The binary evidence is generated and committed by the clean workflow rather than being routed through the text connector, preventing payload truncation.

## Fresh early finite domain

For `a=12`, `b=16`, the fresh demand generator enumerates every nondecreasing demand tuple satisfying

`sum s_i(13-2s_i)/(12-s_i) >= 16+2t`

using exact rational arithmetic.

It independently reproduces the full charging domains and early dispositions:

| scope | charging domain | source-count | support | dual | retained |
|---|---:|---:|---:|---:|---:|
| `m=211`, `t=3` | 4,867 | 3,488 | 261 | 779 | 339 |
| `m=210`, `t=2` | 9,251 | 6,990 | 116 | 1,244 | 901 |

The support cut is implemented directly from the high-demand source/supplement pair budget. The dual LP is used only to propose weights; every accepted dual rejection is converted to rational/integer data and checked exactly against all residual-degree types.

In development, the fresh retained demand files were **byte-for-byte identical** to the production retained demand files.

## Fresh residual-row scan

`fresh_rows.cpp` independently enumerates sorted length-16 residual profiles with entries in `1,...,12`. It applies the source-capacity Hall condition and iterated supplement-cap refinement from scratch.

The complete raw domains and survivor counts are:

| scope | raw residual profiles | row survivors |
|---|---:|---:|
| `m=211`, `t=3` | 1,848,957 | 206 |
| `m=210`, `t=2` | 5,765,218 | 2,087 |

In development, both the survivor files and per-demand band files were **byte-for-byte identical** to the two previously preserved production scanners. The hard `r<=60-t` guard rejected zero rows in these retained bands; its mathematical justification remains documented separately as red-team finding `RT-N29-001`.

`run_independent.py` independently recounts the raw residual-profile totals again using an integer-partition dynamic program, so the C++ enumerator is not the sole count authority.

## Fresh projected filter

The projected zero-slack and pair-threshold cuts are independently recomputed by `run_independent.py`, yielding:

- `m=211`: 206 -> **118** projected rows;
- `m=210`: 2,087 -> **1,225** projected rows.

The development implementation previously matched the production projected survivor sets exactly row-for-row. The clean fully fresh workflow no longer needs the production projected files.

## Fresh joint-state engine

`fresh_joint.py` uses only Python's standard library. It independently implements:

- exact column-total dynamic programming;
- source-to-supplement distinct matching;
- Dinic max-flow for source Hall;
- pair Hall over label subsets;
- selected/residual/missing three-state row feasibility using exact bitset DP;
- iterative source-cap, forced-incidence and column-domain propagation.

The resulting partitions are:

### `m=211`, 118 projected rows

| disposition | count |
|---|---:|
| survivor | 36 |
| source matching | 38 |
| source Hall | 2 |
| joint total source | 42 |

### `m=210`, 1,225 projected rows

| disposition | count |
|---|---:|
| survivor | 593 |
| source matching | 311 |
| source Hall | 29 |
| label domain | 6 |
| total source | 58 |
| joint total source | 222 |
| pair Hall | 6 |

These exactly reproduce the production joint disposition counts; the development comparison also matched the states row-by-row.

## Fresh endpoint model

`fresh_endpoint.py` independently encodes one strongest continuous endpoint relaxation for every fresh joint survivor. It does not reproduce the production 213/378/2 staging; all survivors are sent through the same strongest model.

The model contains, among other things:

- selected/residual/missing source-label incidences;
- residual column totals and F-edge incidences;
- selected source-to-supplement arcs and pair injection;
- supplement forcing;
- exact source selected-degree types and source/supplement pair-degree flow;
- source-conditioned residual/F-degree ledgers and source-local criticality bound;
- actual column selected degrees `x_i`;
- source supplement indegrees `p_u`;
- selected-incidence coupling `R_i+x_i >= q_u+p_u`.

The source imports no production LP builder or checker.

During development, the two deepest old endpoint cases reproduced the same variable and equality dimensions as the production endpoint model and independently gave exact RHS contradictions `-830` and `-355`.

## Exact certificate rule

SciPy/HiGHS may propose a dual ray. Numerical infeasibility alone is never an exclusion.

For each row, the fresh checker constructs integer multipliers and verifies exactly that:

- every inequality multiplier is a nonnegative integer;
- equality multipliers are signed integers;
- every combined primal-variable coefficient is nonnegative;
- the combined right-hand side is strictly negative.

The development run produced exact certificates for **all 629 fresh joint survivors**:

- 36/36 at `m=211`;
- 593/593 at `m=210`;
- unresolved: **0**.

The least-negative exact RHS in development was `-10`, so even the tightest accepted contradiction was strictly exact.

## Clean replay

The workflow is `.github/workflows/n29-independent-d16.yml`.

It starts from a clean Ubuntu 24.04 checkout and:

1. pins SciPy 1.17.0;
2. compiles only this directory's `fresh_rows.cpp`;
3. generates both demand domains with `fresh_prepare.py`;
4. enumerates and screens all residual profiles with `fresh_rows.cpp`;
5. independently rechecks the charging counts, preparation classifications and raw-profile counts;
6. recomputes the projected filter;
7. runs the pure-Python joint engine;
8. builds the fresh strongest endpoint model for every joint survivor;
9. requires an exact integer Farkas certificate for every endpoint exclusion;
10. uploads and commits the complete states/certificate bundles and hash manifest.

No n=28 archive, production N=29 wrapper, production row scanner, production joint checker or production LP builder is used by this clean finite replay.

## What this improves

This removes the largest same-implementation computational trust boundary in the N=29 Delta=16 candidate. The finite contradiction is now supported by a separate source tree from demand generation through the final exact certificates.

It also materially mitigates `RT-N29-002`: the new run preserves **all 629** accepted endpoint Farkas certificates, rather than only aggregate phase counts. The historical preservation limitation of the original production artifacts remains recorded and is not retroactively rewritten.

## What remains open

This is still work written and checked by the same assistant, so it is **not independent researcher reproduction**. It also does not formally prove the graph-theoretic lifting from a hypothetical D2C graph into the finite constraints; that remains a mathematical review obligation.

Highest-value remaining assurance:

- specialist reconstruction of the graph-to-model necessity;
- a separately authored program/researcher replay;
- formalisation of the structural lemmas and/or finite certificate checker.

The n=29 statement should remain labelled **CANDIDATE** until that external assurance exists.
