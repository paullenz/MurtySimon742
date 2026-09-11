# n=30 threshold-tail endpoint attack

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate analytic hardening; the `n=30, Delta=16, m=226` endpoint now has a hand route after the universal bridge. Independent mathematical review remains open.**

## Target

For `n=30, Delta=16`, put

```text
a=13,
b=16,
t=m-224.
```

The threshold-tail construction gives the necessary inequality

```text
Q_{13,16}(s) >= 16+2t.
```

Historically, an exact full-domain check over all

```text
C(25,13)=5,200,300
```

nondecreasing demand multisets `0<=s_i<=12` found

```text
max Q_{13,16}=21,
```

uniquely at `(3^13)`, and exactly seven profiles with `Q>=20`.

That exhaustive classification is no longer a logical dependency at the upper endpoint. [`N30_M226_HAND_PROFILE_REDUCTION.md`](N30_M226_HAND_PROFILE_REDUCTION.md) proves by hand that

```text
Q<=21,
Q=21 only at (3^13),
```

and that `Q>=20` holds exactly for

```text
(2^2,3^11),
(2,3^12),
(3^13),
(3^4,4^9),
(3^2,4^11),
(3,4^12),
(4^13).
```

The proof uses a monotone clipping chain and a two-variable tail calculation. It also derives by hand the exact nine residual rows below. The small standard-library audit [`verify_hand_profile_reduction.py`](verify_hand_profile_reduction.py) checks only the local clipping obligations, 105 cap-four tail pairs, cap-five preimages and the nine-row reconstruction; it does **not** perform the historical 5,200,300-profile sweep.

Hence `t<=2`, so every `Delta=16` scope with `m>=227` is excluded by the hand threshold-tail bound.

The sole upper-bound endpoint is

```text
m=226,
t=2,
Q>=20.
```

## Exact nine rows

```text
s=(2,2,3^11), rho=(1^7,2,3^8), r=33
s=(2,3^12),   rho=(1^7,3^9),   r=34
s=(3^13),     rho=(1^7,3^9),   r=34
s=(3^13),     rho=(1^7,3^8,4), r=35
s=(3^13),     rho=(1^6,2,3^9), r=35
s=(3^4,4^9),  rho=(1^6,3^2,4^8), r=44
s=(3^2,4^11), rho=(1^5,2,3,4^9), r=46
s=(3,4^12),   rho=(1^5,2,4^10), r=47
s=(4^13),     rho=(1^5,3,4^10), r=48
```

[`N30_M226_HAND_ENDPOINT_REDUCTION.md`](N30_M226_HAND_ENDPOINT_REDUCTION.md) then excludes these rows by hand: one dies immediately from demand-ledger equality and the remaining eight by a label-excess versus supplement-Hall contradiction. [`verify_hand_endpoint_table.py`](verify_hand_endpoint_table.py) checks the tiny integer endpoint table without a solver.

Thus, conditional on the universal graph-to-model / threshold-tail lemmas already used by the project, the complete `n=30, Delta=16, m=226` endpoint no longer logically depends on:

- the 5,200,300-demand maximisation;
- the residual-row enumeration;
- the final grouped LP / exact Farkas certificates.

All historical exact evidence remains preserved as independent corroboration and regression material.

This analytic hardening does **not** remove the exact finite work currently used at `m=225, Delta=16` for the equality classification of the full `n=30` candidate theorem, and it does not promote the project beyond candidate status. Independent specialist review remains open.
