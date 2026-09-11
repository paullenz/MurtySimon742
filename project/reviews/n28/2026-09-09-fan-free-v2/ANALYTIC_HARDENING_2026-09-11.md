# 11 September analytic hardening of the n=28 upper range

This note reduces the current n=28 Fan-free candidate proof's computational dependency surface. It does not change the candidate statement or any historical checkpoint.

At `Delta=15`, the complement/residual parameters have `a=12,b=15` and

```text
t=m-195.
```

The charging inequality gives

```text
sum_i s_i(13-2s_i)/(12-s_i) >= 15+2t.
```

For every integer `0<=s<=11`,

```text
s(13-2s)/(12-s)<=5/2,
```

with equality only at `s=4`. Therefore the twelve summands total at most 30, so

```text
15+2t<=30,
t<=7,
m<=202.
```

Hence every n=28, Delta=15 scope with `m>=203` is excluded analytically. The historical statement that the charging domain is empty at `m=203..210` remains a useful replay check but is no longer a logical computational dependency.

The finite proof obligations at Delta=15 above the direct 197 case are therefore only `m=198,199,200,201,202`, all already covered by the preserved exact workflows.

Full derivation and cross-order context: `project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md`.
