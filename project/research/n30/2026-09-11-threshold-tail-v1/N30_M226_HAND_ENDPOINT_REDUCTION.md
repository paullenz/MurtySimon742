# Hand Hall elimination of the n=30, Delta=16, m=226 endpoint

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate analytic hardening. Independent mathematical review remains open.**  
This note replaces the *last* historical grouped-LP/Farkas step at the `m=226, Delta=16` endpoint **conditional on the threshold-tail reduction to the nine residual rows recorded in this directory**. The old exact Farkas certificates remain preserved as independent corroboration.

## 1. Setup

For `n=30, Delta=16`, put

```text
a=13,
b=16,
t=m-224.
```

At `m=226`, `t=2`. The threshold-tail reduction leaves seven demand multisets and exactly nine residual rows. One of the nine is immediately impossible:

```text
s=(3^13),
rho=(1^7,3^9),
r=34.
```

All thirteen demands are positive, and here the demand lower bound is tight only if

```text
s_i=d_i-R_i
```

for every label. Hence

```text
S=sum_i(d_i-R_i)=2(r+t)-r=r+4=38,
```

but `S=39`, contradiction.

We therefore have eight nontrivial rows to exclude.

## 2. Tight demand and selected excess

Every one of the remaining eight rows has

```text
S=r+4.
```

Since always

```text
S=sum_i max(0,d_i-R_i) >= sum_i(d_i-R_i)=r+4,
```

and every displayed demand is positive, equality forces

```text
s_i=d_i-R_i                              (2.1)
```

for every label.

Let

```text
x_i = selected degree of label i,
e_i = x_i-s_i >=0,
M   = sum_i x_i = sum_u q_u,
E   = sum_i e_i = M-S.
```

Fix a selected incidence `ui->w`. The universal bridge gives

```text
d_i <= rho_u+q_u-1                       (2.2)
q_u+p_u <= R_i+x_i.                       (2.3)
```

Substitute `d_i=R_i+s_i` and `x_i=s_i+e_i`. Eliminating `R_i,q_u` gives

```text
e_i >= p_u-rho_u+1.                       (2.4)
```

Also

```text
p_u <= rho_u+2,
```

so with

```text
alpha_u=max(0,p_u-rho_u+1),
```

we have

```text
0<=alpha_u<=3.                             (2.5)
```

The selected-incidence forcing lemma also gives

```text
s_i<=rho_u                                 (2.6)
```

on every selected incidence. In particular, if `rho_u<min_i s_i`, then `q_u=0`.

## 3. Label-side upper bound

Define

```text
B0=sum_u q_u alpha_u.
```

Each of the `q_u` selected incidences from source `u` lands at a label with `e_i>=alpha_u`. Since `alpha_u<=3`, summing incidence by incidence gives

```text
B0 <= sum_i x_i min(e_i,3).                (3.1)
```

For every `s>=0,e>=0`,

```text
(s+e) min(e,3) <= (s+3)e.                 (3.2)
```

Indeed this is immediate for `e<=3`, while for `e>=3` it is equivalent to `3s+3e <= se+3e`, i.e. `s(e-3)>=0`.

Let

```text
c=max_i s_i + 3.
```

Then (3.1)--(3.2) give

```text
B0 <= c sum_i e_i = cE.                   (3.3)
```

Thus any actual graph must satisfy `B0<=cE`.

## 4. Supplement Hall tails

For `k>=1`, define

```text
H_k = sum_{u:q_u>=k+1} q_u
      - sum_{w:rho_w+q_w>=k} p_w.
```

The supplement-forcing lemma says that every selected arc from source `u` to supplement `w` satisfies

```text
rho_w+q_w >= q_u-1.
```

Hence every outgoing selected arc from a source with `q_u>=k+1` must land at a vertex counted in the second term. The selected orientations form genuine source-to-supplement arcs, so

```text
H_k<=0                                    (4.1)
```

for every `k`.

No pair-capacity inequality, cumulative-threshold LP, Farkas certificate, or selected-label-group source cap is used below.

## 5. Tiny source certificates

For a source of residual degree `rho`, define

```text
h_k(rho,q,p)=q*1[q>=k+1]-p*1[rho+q>=k].
```

For each residual row in the table below, choose denominator `D`, put `c=max s+3`, and use the listed nonzero integer weights `z_k`.

For every allowed source type

```text
0<=q<=13-rho,
0<=p<=rho+2,
q+p<=15,
```

with the additional necessary condition `q=0` whenever `rho<min s`, direct integer minimisation of the displayed piecewise-linear expression gives

```text
D*q*(alpha-c) + sum_k z_k h_k(rho,q,p) >= L_rho.   (5.1)
```

The table records the exact minima `L_rho`; `verify_hand_endpoint_table.py` independently checks every allowed integer `(rho,q,p)` pair.

| demand `s` | residual histogram `rho` | `D` | `c` | nonzero `z_k` | exact `L_rho` by residual degree | `delta` |
|---|---|---:|---:|---|---|---:|
| `(2^2,3^11)` | `(1^7,2,3^8)` | 2 | 6 | `z2=6,z5=z6=z8=1` | `L1=0,L2=-42,L3=-50` | 1 |
| `(2,3^12)` | `(1^7,3^9)` | 2 | 6 | `z2=3,z3=4,z6=z8=1` | `L1=0,L3=-50` | 3 |
| `(3^13)` | `(1^7,3^8,4)` | 2 | 6 | `z2=7,z6=z7=1` | `L1=0,L3=-48,L4=-60` | 12 |
| `(3^13)` | `(1^6,2,3^9)` | 2 | 6 | `z2=3,z3=4,z6=z8=1` | `L1=0,L2=-12,L3=-50` | 3 |
| `(3^4,4^9)` | `(1^6,3^2,4^8)` | 3 | 7 | `z2=11,z5=z6=1,z7=2` | `L1=0,L3=-90,L4=-102` | 4 |
| `(3^2,4^11)` | `(1^5,2,3,4^9)` | 3 | 7 | `z2=6,z3=z4=3,z6=z7=z8=1` | `L1=0,L2=-24,L3=-90,L4=-102` | 6 |
| `(3,4^12)` | `(1^5,2,4^10)` | 2 | 7 | `z2=z3=z5=3,z8=1` | `L1=0,L2=-12,L4=-70` | 1 |
| `(4^13)` | `(1^5,3,4^10)` | 2 | 7 | `z1=1,z2=5,z4=z5=z6=z7=1` | `L1=-3,L3=-30,L4=-68` | `3/2` |

Here

```text
delta = cS + (1/D) sum_rho n_rho L_rho,
```

where `n_rho` is the multiplicity of residual degree `rho` in the row. All eight values are strictly positive.

Now sum (5.1) over all sixteen sources. The `h_k` terms sum to `H_k`, so

```text
D(B0-cM) + sum_k z_k H_k >= sum_rho n_rho L_rho.
```

By (4.1), every `H_k<=0` and every `z_k>=0`. Therefore

```text
D(B0-cM) >= sum_rho n_rho L_rho.
```

Adding `DcS` and using `E=M-S` gives

```text
B0-cE >= delta >0.                        (5.2)
```

Thus

```text
B0 > cE,                                  (5.3)
```

contradicting the necessary label-side inequality (3.3).

All eight nontrivial rows are impossible.

## 6. Consequence

Conditional on the threshold-tail reduction to the seven `Q>=20` demand multisets and their nine residual rows, the complete `n=30, Delta=16, m=226` endpoint is now excluded by hand:

1. one row dies from `S=r+4` immediately;
2. the other eight die from the label-excess / supplement-Hall contradiction above.

The historical final grouped LP and exact Farkas certificates at `m=226` are therefore no longer logically necessary **once the threshold-tail profile/row reduction is accepted**.

This note does not yet alter the canonical n=30 reviewer package. The remaining high-value task is to replace or sharply compress the exact `Q>=20` profile classification itself, so that the entire `m=226, Delta=16` branch can become transparently hand-derived from the universal bridge.
