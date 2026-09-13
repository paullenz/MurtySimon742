# Shared residual-budget continuation

13 September 2026. **Candidate general hand arguments with exact fixed-pattern
evidence. External review, novelty and independent reproduction remain OPEN.**

The [hand argument](SHARED_BUDGET.md) couples endpoint loads through residual
degrees shared by every selected source using the same label. It also gives
a general weighted pair/endpoint inequality and a short **balance-or-
concentration alternative** for the selected incidence family.

For M active sources, c used labels, selected total Q, residual total r and
empty-source incoming capacity H0, a balanced selected-label cover implies

```text
(2c-M)Q <= c H0 + M r.
```

If this inequality fails, every viable selected arrangement must concentrate
more than (M/c)|I| active sources entirely inside some smaller label set I.
The hand proof establishes the alternative for arbitrary orders. It remains
a conditional structural result, not an unrestricted density theorem.

## Exact application and controls

The input is precisely the previous 4,584 saved selected patterns, after
their recorded pair repairs. Incoming degrees p are allowed to vary. Each
stage retains the same selected sets and all numerical rejections require
an exact certificate.

| Stage | Additional fixed-pattern exclusions | Patterns left |
|---|---:|---:|
| Shared-label endpoint budget | 4,449 | 135 |
| Exact residual-row configuration control, without pair constraints | 13 | 122 |
| Joint pair constraints and endpoint/residual budgets | 25 | 97 |
| Total | **4,487** | **97** |

All 26 earlier unweighted local residual-cover failures are already covered
by the first stage. A separate pair-only control resolves attribution for
the final 25: **3** fail weighted pair counting alone; **22** have exact
fractional witnesses for the pair-only and endpoint-placement controls
separately, but their conjunction has an exact obstruction. Thus those 22
show a real interaction between the two necessary-condition systems.

The balanced-cover corollary supplies short integer-flow certificates for
**1,871** of the 4,449 endpoint exclusions. In the complete 4,584-pattern
study, 1,883 admit a balanced cover and 2,701 have a directly checkable
concentration witness. Twelve balanced patterns satisfy the displayed
inequality and are not excluded by that corollary.

These are **fixed selected-pattern results only**. The generalisation
frontier remains **994 whole-state exclusions / 4,584 surviving scalar
states**. A scalar state may choose another selected geometry, another
source-degree vector or additional selected incidences x_i>s_i. None of
those alternatives is exhausted here. The 97 passing witnesses are rational
mixtures of residual rows, not simultaneous integer placements or graphs.
The N34/N35 fixed-order candidate proofs are already closed by their own
packages and are unchanged.

## A compact hand example

The saved N34 state-227 selected pattern has M=11, c=15, Q=41, r=39 and
H0=21. Its checked balanced cover would require

```text
19*41 <= 15*21 + 11*39,
779   <= 744,
```

a contradiction. [EXAMPLE.json](EXAMPLE.json) includes the selected sets and
the small integer flow witnessing balance. This excludes that arrangement;
an alternative arrangement would have to exhibit the concentration described
by the hand theorem.

## Verification and evidence

[verify.py](verify.py) uses only the Python standard library and imports none
of the discovery models. It reconstructs the frozen input, verifies all
4,449 endpoint certificates and 38 additional certificates, checks all
balanced/concentration witnesses, and directly checks 122 fractional control
witnesses, 97 joint witnesses and the pair-only attribution evidence.
[VERIFICATION.json](VERIFICATION.json) records the exact outcome.

The 38 additional certificates also have a checked integer-weight
compression in [COMPACT_CERTIFICATES.json](COMPACT_CERTIFICATES.json).
The original rational certificates remain preserved. The verifier challenges
the signed-price inequality on tiny abstract cross-data configurations,
including positive pair deficits. These are algebraic checks, not an
enumeration of actual D2C graphs.

The source files and evidence are:

- [endpoint_control.py](endpoint_control.py) and [ENDPOINT_CONTROL.json](ENDPOINT_CONTROL.json);
- [balanced_cover.py](balanced_cover.py) and [BALANCED_COVER.json](BALANCED_COVER.json);
- [shared_pair_cover.py](shared_pair_cover.py) and [SHARED_PAIR.json](SHARED_PAIR.json);
- [pair_only_control.py](pair_only_control.py) and [PAIR_ONLY_CONTROL.json](PAIR_ONLY_CONTROL.json);
- [compress_certificates.py](compress_certificates.py);
- [scope audit and failure record](AUDIT.md), [environment](ENVIRONMENT.json)
  and [file hashes](MANIFEST.json).

From the repository root:

```sh
python project/research/general_n/2026-09-13-shared-residual-budget-v1/verify.py
```

Discovery additionally requires NumPy and SciPy. Run, in order,
`endpoint_control.py`, `balanced_cover.py`, `shared_pair_cover.py`,
`pair_only_control.py`, `compress_certificates.py`, then `verify.py`.
Discovery scripts regenerate their output files; original timings are not
reproduced by a later run. The verifier is independent of solver choice.

## Next research question

Use the balance-or-concentration alternative to constrain **all admissible
selected geometries** of a state, including different q and x>=s. In the
concentrated case, combine the forced label subset with pair traces and exact
destination containment. On the 97 passing frozen patterns, test simultaneous
integer residual placement and exact Hall routing. No whole-state claim is
permitted without coverage of all branches.
