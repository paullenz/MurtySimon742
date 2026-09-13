# Independent CI replay of the adjacent-family closure

13 September 2026.

The committed workflow

```text
.github/workflows/scan-incidence-capacity-family.yml
```

independently checked the final exact integer verifier

```text
project/research/general_n/2026-09-13-alternative-attacks-v1/scan_incidence_capacity_family.cpp
```

in GitHub Actions run

```text
34779806843
```

at commit

```text
b9157c5cf9f90c50ed144809be720f529664c85d
```

The run completed successfully. It checked all

```text
3 states * 35 excess layers = 105 state/layer pairs
```

for states

```text
230, 282, 385
```

and required the final exact-relaxation gap to be strictly positive in every case.

The run therefore independently reproduces the committed verifier's whole-layer arithmetic and compilation in a clean GitHub-hosted environment. It is stronger than a local-only replay, but it is **not** an independent implementation of the mathematics: the CI job recompiles and executes the same committed source code.

Accordingly the present trust boundary is:

- independent clean-environment replay of the committed verifier: **COMPLETE / GREEN**;
- independent reimplementation of the verifier: **OPEN**;
- external mathematical review of the canonical bridge and new lemmas: **OPEN**;
- unrestricted Murty–Simon conjecture: **NOT PROVED**.

The proof/status note is `INCIDENCE_CAPACITY_FAMILY_CLOSURE.md`.
