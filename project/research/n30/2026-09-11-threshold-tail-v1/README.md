# n=30 threshold-tail endpoint attack

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: active research; no change yet to the current n=30 candidate proof.**

## Target

For `n=30, Delta=16`, put

```text
a=13,
b=16,
t=m-224.
```

The threshold-tail construction gives a necessary inequality

```text
Q_{13,16}(s) >= 16+2t.
```

An exact full-domain check over all

```text
C(25,13)=5,200,300
```

nondecreasing demand multisets `0<=s_i<=12` gives

```text
max Q_{13,16}=21,
```

uniquely at `(3^13)`. Hence `t<=2`, so every `Delta=16` scope with `m>=227` is already excluded by threshold tails.

The sole upper-bound endpoint is therefore

```text
m=226,
t=2,
Q>=20.
```

Exactly seven demand multisets have `Q>=20`:

```text
(2^2,3^11),
(2,3^12),
(3^13),
(3^4,4^9),
(3^2,4^11),
(3,4^12),
(4^13).
```

Tail-slack accounting forces exactly nine residual rows. These agree one-for-one with the nine historical row-threshold survivors from workflow `34287440190` and the nine exact Farkas rejections from workflow `34287739057`.

The research goal is to replace those nine historical Farkas exclusions by a short hand argument, ideally one or two structural inequalities.

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

The historical exact endpoint route remains valid corroboration. No theorem status is promoted by this note.
