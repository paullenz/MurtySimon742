# Equal-q / equal-preincoming selection inversions on the frozen pilot

14 September 2026. **Reconnaissance only. This is stronger experimental evidence than the q-crossing result, not a promoted theorem and not needed by the q-stratified minimum-cut exactness theorem.**

## Statistic

For the canonical maximal Hall minimizer `M+`, call an equal-`(q,m)` block **selection-inverted** if it contains

```text
x notin M+,
y in M+,
q_x=q_y=q,
m_x=m_y=m,
c_x<c_y.                                               (1)
```

No capacity condition is imposed. Thus every positive q-crossing is a selection inversion, but an inversion can exist without contributing to `C_q`.

The scanner records one bit per exact target-Hall failure: whether any such inversion exists.

## Frozen-pilot result

The diagnostic was replayed over the same deterministic 15-state input used by the q-crossing pilot. Aggregating all state outputs gives

```text
states:                              15
profiles tested:             201,493,148
exact target-Hall failures:      205,919
q-crossing-positive profiles:           0
selection-inverted profiles:            0
```

So every one of the 205,919 canonical maximal Hall failures in this pilot satisfies the stronger empirical property

```text
for every equal-(q,m) block,
all selected copies lie at or below every exterior copy in c.       (2)
```

The state-level target-Hall failure counts were

```text
state 226      64,232
state 1626     63,818
state 2439     48,448
state 2984      1,681
state 4073     13,871
state 5519        477
state 6085     12,260
state 6998        562
state 7610          7
state 8179        253
state 8727         10
state 9440          0
state 10098         0
state 11007       204
state 429          96
----------------------
total          205,919
```

Every state had zero selection-inverted failure profiles.

## Interpretation

This observation explains why the frozen pilot has `C_q=0` in an especially strong way: the selected/exterior order does not even create a geometric crossing at equal `q` and equal preincoming count, before target caps are compared.

However, this stronger maximal-witness phenomenon is **not required** for exact q-stratified failure detection. [`Q_STRATIFIED_MINCUT_EXACTNESS.md`](Q_STRATIFIED_MINCUT_EXACTNESS.md) shows that if a minimum witness ever does have a positive crossing, a neutral deletion process reaches another minimum witness with `C_q=0`.

Therefore the inversion statistic should remain diagnostic evidence for additional Murty structure, not become an assumption in the main theorem chain.

## Reproduction

[`make_q_selection_inversion_scanner.py`](make_q_selection_inversion_scanner.py) instruments the generated q-crossing scanner without changing any canonical decision. It keeps, for each equal `(q,m)` block,

```text
minimum c among exterior targets,
maximum c among selected targets,
```

and flags the profile exactly when

```text
min_exterior_c < max_selected_c.                       (3)
```

The committed workflow [`scan-q-selection-inversion-pilot.yml`](../../../../.github/workflows/scan-q-selection-inversion-pilot.yml) regenerates the full scanner chain, replays the deterministic pilot and asserts the aggregate baseline and zero-inversion result.

## Trust boundary

This is finite reconnaissance on a fixed 15-state sample. It does not prove that canonical maximal minimizers are universally inversion-free, does not promote a new whole-state exclusion, and is not needed for the exact minimum-cut theorem. External review remains open.
