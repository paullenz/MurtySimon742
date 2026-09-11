# 11 September analytic hardening of the n=30 upper range

This note reduces the current n=30 Fan-free candidate proof's computational dependency surface. It does not change the candidate statement or historical evidence.

## Delta=17

Here `a=12,b=17` and

```text
t=m-221.
```

The charging inequality gives

```text
sum_i s_i(13-2s_i)/(12-s_i) >= 17+2t.
```

For every integer `0<=s<=11`,

```text
s(13-2s)/(12-s)<=5/2.
```

With twelve labels the total is at most 30, hence

```text
17+2t<=30,
t<=6,
m<=227.
```

Therefore every `Delta=17` scope with `m>=228` is excluded analytically. The historical explicit scan showing zero charging-feasible profiles at `m=228..255` is no longer a logical dependency. The boundary `m=227` remains the existing 15-profile exact threshold calculation.

## Delta=16

Here `a=13,b=16` and

```text
t=m-224.
```

For every integer `0<=s<=12`,

```text
s(14-2s)/(13-s)<=8/3,
```

because

```text
8/3-s(14-2s)/(13-s)
=2(s-4)(3s-13)/(3(13-s))>=0.
```

With thirteen labels the charging sum is at most `104/3`. Therefore

```text
16+2t<=104/3,
t<=9,
m<=233.
```

Hence every `Delta=16` scope with `m>=234` is excluded analytically. The historical zero-domain statement for `m=234..240` remains corroborating evidence only. The boundary `m=233` remains the existing nine-profile exact threshold calculation.

Full cross-order derivation: `project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md`.
