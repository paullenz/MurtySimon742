# Residual-budget projection to label degree mass

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact algebraic projection inside the positive-demand zero-slack RX-Hall framework. This is not an unrestricted Murty-Simon theorem.**

## 1. Setup

Use the generic RX-Hall notation from this directory. For every positive-demand A-label `i`,

```text
s_i = d_i - R_i > 0,
```

so exactly

```text
d_i = R_i + s_i.
```

In the zero-slack sector,

```text
sum_i s_i = r + 2t,
sum_i R_i = r.
```

Therefore

```text
sum_i d_i = 2r + 2t = 2(r+t).                    (DM1)
```

Since the residual ledger gives `e(F)=r+t`, this is also

```text
sum_i d_i = 2e(F).                                (DM1')
```

Thus the exact residual-column budget can be projected to an exact total label-degree mass without retaining `R_i` as an independent global variable.

## 2. Local RX constraints in `(s,d,y)` coordinates

Write

```text
y_i = x_i - s_i >= 0.
```

The local label box

```text
0 <= R_i <= dmax-s_i,
s_i <= x_i <= b-R_i
```

becomes

```text
s_i <= d_i <= dmax,                               (DM2)
0 <= y_i <= b-d_i.                                (DM3)
```

For a selected incidence from source `u` of type `(rho_u,q_u,p_u)` to label `i`, RX1-RX3 become

```text
s_i <= rho_u,                                     (DM4)
d_i <= rho_u + q_u - 1,                          (DM5)
d_i + y_i >= q_u + p_u.                          (DM6)
```

Indeed RX2 is `R_i+s_i<=rho_u+q_u-1`, hence DM5, while RX3 is

```text
R_i+x_i = (d_i-s_i)+(s_i+y_i) = d_i+y_i >= q_u+p_u.
```

The previous RX4 lower bound follows immediately by combining DM5-DM6:

```text
y_i >= p_u-rho_u+1,
```

when the right side is positive.

## 3. Why this projection matters

The stripped positive-demand incidence problem can therefore be expressed with label types

```text
(s_i,d_i,y_i)
```

rather than `(s_i,R_i,x_i)`, with the exact global identity DM1 and the local compatibility box DM2-DM6.

Conceptually, the exact residual budget is not merely an implementation constraint. It says that the label-degree profile has a fixed total mass `2(r+t)`. RX2 then constrains which portion of that mass can be used by a source according to the threshold

```text
rho_u+q_u-1.
```

This suggests a projected Hall/majorization route: eliminate the individual `d_i` by combining the fixed mass DM1 with threshold capacities induced by DM5 and the lower-load requirement DM6.

## 4. Candidate threshold form

For any integer threshold `h`, DM1-DM2 imply the elementary mass bounds

```text
sum_{i:d_i<=h} d_i <= h * #{i:d_i<=h},
```

and

```text
sum_{i:d_i>h} d_i >= (h+1) * #{i:d_i>h}.
```

Since a source `(rho,q,p)` can select only labels with

```text
d_i <= rho+q-1,
```

Hall demand from low `(rho+q)` source classes must be absorbed by a low-degree prefix of the label profile. At the same time DM6 requires enough `d_i+y_i` mass for large `q+p` classes.

The research target is therefore to derive one or a small family of inequalities coupling

```text
source thresholds rho+q-1,
source loads q and p,
label degree mass sum d_i=2(r+t),
label slack y_i<=b-d_i.
```

If successful, this would replace the residual-variable LP by a threshold/majorization theorem and may be substantially more amenable to all-n analysis.

## 5. Trust boundary

This note is only an exact change of variables plus elementary consequences of the already stated RX framework. It does not claim that the resulting projected inequalities are sufficient, nor that the current n=30 equality frontier is closed by them. The concurrent residual-budget ablations are intended to test exactly that question before any general theorem is claimed.
