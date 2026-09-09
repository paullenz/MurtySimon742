# Analytic min-hinge reduction and parameter template

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite identities and exact t=3 finite potential; the first naive cross-surplus parameter template has been falsified at t=2. Not an unrestricted theorem.**

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

## 2. Incidence-sum lemma

For every actual selected source-label incidence `u -> i`, RX2 and RX3 give the
BC coordinate domination

```text
d_i = R_i+s_i <= rho_u+q_u-1 = alpha_u,
v_i = b-(R_i+x_i) <= b-(q_u+p_u) = w_u.
```

Every `H_{D,V}` is coordinatewise nondecreasing, hence

```text
H_{D,V}(d_i,v_i) <= H_{D,V}(alpha_u,w_u)
```

on every selected incidence. Summing over the selected incidence graph counts
each label `i` exactly `x_i` times and each source `u` exactly `q_u` times, giving
the direct graph-level inequality

```text
sum_i x_i H_{D,V}(d_i,v_i)
    <=
sum_u q_u H_{D,V}(alpha_u,w_u).                 (MH1)
```

Therefore the characteristic `x*F` and `q*F` terms in the finite duals are not
LP artefacts: for any nonnegative min-hinge potential `F`, their global transport
inequality follows by pointwise monotonicity and double counting. This is the
main bridge from the finite analytic potential toward a hand argument.

## 3. Exact n=29, t=3 finite prototype

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

## 4. First parameter pattern and its falsification

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

For `a=12,t=3` this reproduces all nine exact features and re-solves all 94
`t=3` profiles with the same floating objective as the original nine-feature
proposal.

However this literal extrapolation is **false at t=2**. Its specialization

```text
T(12,2) =
(0,0),(0,1),(0,8),(0,9),(0,10),(0,11),(1,0),(3,0)
```

is LP-infeasible on the 38 difficult t=2 profiles even when all 12 canonical SH
staircase corrections are made available. More strongly, it is infeasible on
*demand 45 alone* with all 12 SH shapes. The preserved batch is

`checkpoints/PARAMETRIC_MIN_HINGE_TEMPLATE_RUN_34388537787.json`.

This is a useful hostile falsification: the exact t=3 pattern is real, but the
breakpoint rule does not transport unchanged to t=2. The correct next question is
therefore which min-hinges the t=2 geometry actually selects from the full
analytic dictionary, not how to patch the failed rule ad hoc.

## 5. Current falsification programme

1. give demand 45 every min-hinge `H_{D,V}` on the complete `(d,v)` grid, with and
   without the full canonical SH correction dictionary;
2. repeat on the 38-profile t=2 core with common hinge/SH weights;
3. if the complete min-hinge family survives hard38, test all 902 t=2 profiles;
4. mine the sparse active hinge locations and compare them to the exact t=3 nine
   features before proposing a second parameter rule;
5. exactify any positive compact result before theorem use;
6. use n=30,t=1 only after the t=2 breakpoint mechanism is understood.

Failure of the complete nonnegative min-hinge family on demand 45 would be a
major negative result for this analytic architecture and would trigger a return
to richer BC staircase functions rather than feature proliferation.

## 6. Useful midpoint observation

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
variable (`R` or `q`) cancels from the sum. For integer variables the right side
can be replaced by the appropriate floor.

In fact, ignoring endpoint clipping of `R` or `q`, the corresponding maximum of
the hinge over the transport variable is attained by balancing the two affine
arguments. This makes the sum `D+V` a natural scalar parameter of each hinge and
suggests a route to closed envelope formulae. The remaining difficulty is that
MH1 is weighted by the actual incidence degrees `x_i` and `q_u`; a useful general
proof must combine these hinge envelopes with the source/supplement threshold
transport and demand identities without discarding too much profile information.
