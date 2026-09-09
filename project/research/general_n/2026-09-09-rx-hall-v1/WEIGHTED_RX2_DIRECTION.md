# Weighted RX2 / degree-mass direction

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact necessary inequalities and a proposed elimination direction; not yet a closing theorem.**

## 1. Degree-mass coordinates

In the positive-demand zero-slack sector use the projection

```text
d_i = R_i+s_i,
y_i = x_i-s_i,
sum_i d_i = 2(r+t).
```

For every selected source-label incidence `u->i`, RX2 gives

```text
d_i <= rho_u+q_u-1.                               (W1)
```

## 2. Weighted summation of RX2

Sum W1 over all selected incidences. Label `i` occurs exactly `x_i` times and source `u` sends exactly `q_u` incidences, hence

```text
sum_i x_i d_i
  <= sum_u q_u (rho_u+q_u-1).                     (W2)
```

Since `x_i>=s_i`,

```text
sum_i s_i d_i
  <= sum_u q_u (rho_u+q_u-1).                     (W3)
```

This removes the incidence graph completely. It retains more of RX2 than the earlier RX4 projection because the exact label-degree mass remains visible.

## 3. Exact lower envelope on the left

For a fixed sorted demand profile `s=(s_i)`, the degrees satisfy

```text
s_i <= d_i <= dmax,
sum_i d_i = 2(r+t).
```

Therefore the minimum possible value of

```text
sum_i s_i d_i
```

is obtained by placing the extra degree mass `d_i-s_i` greedily on the smallest demand weights `s_i`, subject to `d_i<=dmax`. Equivalently, if

```text
E = 2(r+t)-sum_i s_i = r,
```

then

```text
min sum_i s_i d_i
  = sum_i s_i^2
    + min { sum_i s_i R_i :
            0<=R_i<=dmax-s_i,
            sum_i R_i=r }.                         (W4)
```

The minimizer is the standard bounded fractional-knapsack allocation to increasing `s_i`; because all data and capacities are integral, an integral minimizer exists by filling the cheapest coordinates first.

Call this exact lower envelope `L(s,r,dmax)`.

Any actual graph in this sector must therefore satisfy

```text
L(s,r,dmax)
  <= sum_u q_u(rho_u+q_u-1).                       (W5)
```

## 4. Research target on the source side

The remaining task is to maximize the right side of W5 over the source-type constraints

```text
q_u+rho_u<=a,
p_u<=rho_u+(b-a-1),
q_u+p_u<=b-1,
sum q_u=sum p_u,
```

plus the nested supplement-transport inequalities and, if necessary, the exact grouped transport condition.

Crucially, W5 no longer contains labels, residual columns or source-label incidences. If a sharp symbolic upper envelope

```text
U(rho;a,b)
```

for the source side can be derived, then

```text
L(s,r,dmax) <= U(rho;a,b)                          (W6)
```

would be a purely profile-level necessary condition.

## 5. Why this is worth testing

The n=30 equality-frontier ablations show that strengthening Hall geometry alone and restoring exact source/supplement transport alone do not remove most surviving states. The exact residual budget is therefore the natural missing resource to expose. W2-W6 are the simplest direct way to expose it without restoring the old final LP.

The next computational falsification test should compare W5/W6 against the preserved n=30 `m=225` hard survivor profiles, and then against n=29/n=30 scopes already closed by exact RX-Hall certificates. A failure is useful: it identifies how much of RX3 or source-label coupling still needs to be retained.
