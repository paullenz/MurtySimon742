# Analytic min-hinge reduction and parameter template

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite identity plus a parameter-template conjecture. Not an unrestricted theorem.**

## 1. Exact hinge identity

Use the BC coordinates

```text
d = R+s,                 v = b-(R+x)          (label side),
alpha = rho+q-1,         w = b-(q+p)          (source side).
```

For nonnegative integers `D,V`, define

```text
H_{D,V}(d,v) = min((d-D)_+, (v-V)_+).
```

For integer `d,v` there is the exact finite identity

```text
H_{D,V}(d,v)
  = sum_{k>=1} 1[d >= D+k and v >= V+k].
```

Proof: both sides count the positive integers `k` with
`k <= d-D` and `k <= v-V`. Hence each min-hinge is exactly a chain of nested
BC Hall rectangles along a slope-one diagonal. It is therefore a canonical
monotone Hall test, not merely a fitted nonlinear feature.

Consequently every nonnegative combination

```text
F(d,v) = sum_{D,V} c_{D,V} H_{D,V}(d,v),   c_{D,V} >= 0,
```

is a nonnegative weighted sum of valid nested Hall upper-set inequalities.

## 2. Exact n=29, t=3 finite prototype

For `(a,b,t,dmax)=(12,16,3,10)`, all 94 regenerated hard RX-Hall profiles admit
one exact rational BC-only potential using exactly the following nine min-hinges:

```text
(0,0), (0,2),
(1,7), (1,8), (1,9), (1,10), (1,11),
(2,0), (4,0).
```

The exact checkpoint is
`checkpoints/N29_T3_MIN_HINGE_EXACT_RUN_34384549422.json`.
It checks 30,646 inequalities in integer arithmetic, with zero row/bound
violations and worst exact profile margin nearly twice the required margin.

## 3. Parameter pattern

The nine observed breakpoints have a parameter-only description with no fitted
constants. For `(a,t)=(12,3)` they are exactly the specialization of

```text
T(a,t) = {
  (0,0),
  (0,t-1),
  (t-2,V) for V=a-t-2,...,a-1,
  (t-1,0),
  (t+1,0)
},
```

with duplicate points removed and nonnegative coordinates understood in the
small-`t` boundary cases.

For `a=12,t=3` this gives

```text
(0,0), (0,2),
(1,7),(1,8),(1,9),(1,10),(1,11),
(2,0),(4,0),
```

exactly.

This motivates the **parameterized min-hinge template conjecture**: the useful
BC potential at general `(a,b,t)` may be chosen from the small family `T(a,t)`,
with coefficients depending on the global parameters rather than on individual
residual profiles. The conjecture is deliberately stronger than the evidence
and must be attacked by cross-surplus/cross-order falsification.

## 4. Immediate falsification programme

The first tests are intentionally hostile:

1. reproduce the exact-known `n=29,t=3` geometry from `T(12,3)`;
2. test `T(12,2)` on the 38 difficult `n=29,t=2` profiles, first without SH and
   then with the complete canonical 12-shape SH dictionary;
3. if the hard38 test survives, test the same template across all 902 `t=2`
   hard profiles;
4. treat demand 45 separately, because it is the unique hard38 profile known to
   be individually infeasible with the complete 75-shape BC staircase dictionary
   and no SH correction;
5. only after surviving `t=2`, specialize the same rule to the `n=30,t=1`
   laboratory.

A finite success remains proposal evidence until exactified. A failure is to be
preserved and used to refine or abandon the template rather than patched ad hoc.

## 5. Useful midpoint observation

For every hinge,

```text
H_{D,V}(R+s, b-R-x)
 <= 1/2 * (s+b-x-D-V)_+,
```

and

```text
H_{D,V}(rho+q-1, b-q-p)
 <= 1/2 * (rho+b-p-1-D-V)_+.
```

This follows from `min(u,v) <= (u+v)/2`; in both cases the internal transport
variable (`R` or `q`) cancels from the sum. The integer version can be sharpened
with a floor. This cancellation is a candidate route for replacing finite LP
envelopes by symbolic source/label bounds, but no theorem-level global estimate
is claimed here yet.
