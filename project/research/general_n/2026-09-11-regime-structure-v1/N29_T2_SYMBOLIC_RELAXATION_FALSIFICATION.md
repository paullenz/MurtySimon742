# n=29, t=2: falsifying over-coarse symbolic relaxations

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact counterexample inside a deliberately weakened profile relaxation. This does not contradict the preserved exact RX-Hall certificate. It identifies which source-geometry hypothesis is genuinely needed by any symbolic compression.**

## Question

Can the `nu1=0 -> T2` finite regime be proved from only the coarse demand/profile identities, without using the supplement-cap source geometry?

For `n=29, Delta=16, t=2`, the positive-demand sector has

```text
sum_i s_i = sum_u rho_u + 4,
nu1 = #{i:s_i=1}.
```

The exact scalar template `T2` is the one preserved in

```text
project/research/general_n/2026-09-09-rx-hall-v1/
  n29_t2_sh3_c11_three_scalar_exact.py
```

A first attempted symbolic relaxation kept the demand threshold/bounds and the degree-sum identity, but weakened the source side. That relaxation admits negative `T2` certificate gap, so those coarse identities are insufficient.

More importantly, the following **integer** demand/source pair survives the demand preparation and the initial source-capacity Hall inequalities but is killed by the monotone supplement-cap refinement.

## Exact separating counterexample

Take

```text
s   = (2,2,2,2,2,2,2,2,3,3,3,3)
rho = (1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3).
```

Then

```text
sum(s)   = 28,
sum(rho) = 24,
sum(s)-sum(rho) = 4.
```

The audited demand score is

```text
8*(2*(13-4)/(12-2)) + 4*(3*(13-6)/(12-3))
 = 8*(9/5) + 4*(7/3)
 = 356/15
 > 20 = b+2t.
```

The charging quantity is

```text
8*(2*1/(12-2)) + 4*(3*2/(12-3))
 = 8/5 + 8/3
 = 64/15.
```

Hence the residual lower bound is

```text
16 + ceil(64/15) = 21,
```

while the upper bound is

```text
min(sum(s)-4, C(12,2)-2) = min(24,64)=24.
```

Thus `sum(rho)=24` lies inside the coarse audited residual band. Direct replay of the threshold and source-capacity dual preparation tests gives no demand-side rejection for this `s`.

### Initial Hall stage

For every `rho=1` source, no demand has `s_i<=1`, so its selected-degree cap is zero.

For every `rho=3` source,

```text
qcap = min(12-3, #{i:s_i<=3}) = min(9,12)=9.
```

Therefore the initial caps are

```text
(0 x 12, 9 x 4).
```

The largest-demand-prefix Hall checks pass at this stage.

### Supplement-cap refinement

For a `rho=3` source to have selected degree `q`, it needs `q` other sources `w` satisfying

```text
rho_w + qcap_w >= q-1.
```

With the above caps, the fixed-point refinement reduces the four active caps from `9` to `3`, giving

```text
(0 x 12, 3 x 4).
```

Now the top-five demand prefix has demand

```text
3+3+3+3+2 = 14,
```

but total available supply is only

```text
4*3 = 12.
```

So the refined Hall condition fails exactly as intended by `minimal_rows.cpp`.

## Why this matters for the symbolic attack

Evaluated with the preserved exact rational `T2` scalar template, this weakened profile has certificate gap

```text
-604/5 < 0.
```

Therefore any attempted hand proof of the `nu1=0 -> T2` regime that uses only

- the demand threshold,
- the residual degree-sum identity,
- the coarse residual band,
- and the first-stage source-capacity Hall constraints

cannot be sufficient: the monotone supplement-cap geometry (or a valid symbolic consequence of it) is essential.

This is useful falsification. It narrows the next proof target from “derive T2 from generic histogram identities” to:

> extract a small analytic inequality from the supplement-cap fixed-point condition that excludes this and all analogous negative-gap histograms.

A promising language is to track threshold counts of sources satisfying `rho_u + q_u >= j`, because the refinement condition directly constrains how many sources can sustain selected degree at each level.
