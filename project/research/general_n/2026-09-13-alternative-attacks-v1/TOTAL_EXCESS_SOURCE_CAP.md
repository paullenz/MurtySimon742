# Total-excess source cap

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note extracts a simple but strong selection-free consequence of the selected-excess incidence bound. It interpolates the exact-demand cap `p_u<=rho_u-1` to every excess layer and is designed to feed directly into the orientation target-flow system.

## 1. Setup

For a scalar state write

```text
x_i=s_i+e_i,
e_i>=0,
E=sum_i e_i.
```

For a source `u in B`, retain

```text
q_u = number of selected labels at u,
p_u = incoming selected missing-edge load,
rho_u = residual A-cross degree.
```

The established selected-excess incidence bound says that on every selected incidence `u-i` whose label has positive demand `s_i>0`,

```text
p_u-rho_u+1 <= e_i.                                  (1)
```

Equivalently, with

```text
L_u=max(0,p_u-rho_u+1),                              (2)
```

every selected positive-demand label at `u` has excess at least `L_u`.

Selected incidences at a fixed source use distinct labels.

## 2. All-positive-demand form

First suppose every label has `s_i>0`. A source with `q_u>0` has `q_u` distinct selected positive-demand labels. Summing (1) over those labels gives

```text
E >= q_u L_u.                                        (3)
```

Hence

```text
L_u <= floor(E/q_u),                                 (4)
```

and therefore

```text
p_u <= rho_u + floor(E/q_u) - 1.                    (5)
```

> **Total-excess source cap, positive-demand form.** If `q_u>0` and all labels have positive demand, every legal branch satisfies (5).

At `E=0`, (5) is exactly

```text
p_u<=rho_u-1,                                        (6)
```

recovering the exact-demand corollary. For large `q_u`, (5) stays strong even when total excess is nonzero.

## 3. Zero-demand correction

Now allow zero-demand labels. Put

```text
z=#{i:s_i=0}.                                        (7)
```

A zero-demand label used by source `u` must have `x_i>0`, hence

```text
e_i=x_i>=1.                                          (8)
```

Let `k` be the number of zero-demand labels selected at `u`. Then

```text
0<=k<=min(z,q_u,E).                                  (9)
```

The `k` zero-demand labels consume at least `k` units of total excess. The other `q_u-k` selected labels have positive demand and, by (1), each consumes at least `L_u`. Thus, whenever `L_u>=1`,

```text
E >= k + (q_u-k)L_u.                                (10)
```

For fixed `L_u>=1`, the right side is minimized by making `k` as large as possible. Define

```text
k_* = min(z,q_u,E).                                  (11)
```

If `q_u>k_*`, then (10) gives the universal bound

```text
L_u <= floor((E-k_*)/(q_u-k_*)).                    (12)
```

Therefore

```text
p_u <= rho_u
       + floor((E-k_*)/(q_u-k_*))
       - 1.                                          (13)
```

If `q_u<=k_*`, the source could in principle place all of its selected incidences on activated zero-demand labels, so (1) alone gives no incoming cap beyond the other canonical inequalities.

> **Total-excess source cap, zero-demand form.** For `q_u>k_*`, every legal branch satisfies (13), with `k_*` from (11).

### Exact-demand endpoint

When `E=0`, `k_*=0`, so every active source has

```text
p_u<=rho_u-1                                         (14)
```

regardless of how many zero-demand labels exist: none can be activated without positive excess.

## 4. Relation to the threshold-excess family

The existing threshold family says, with

```text
h_l=#{i:e_i>=l},
```

that

```text
q_u>h_l => p_u<=rho_u+l-2.                           (15)
```

Since `E>=l h_l`, one has `h_l<=floor(E/l)`. Choosing the first threshold for which a source necessarily exceeds `h_l` already yields a coarse version of (5).

The direct summation argument is sharper because it uses the fact that **all `q_u` distinct selected positive-demand incidences at that source** must simultaneously carry the same lower excess `L_u`.

Thus (5)/(13) should be applied before the more detailed `h_l` profile machinery; the latter remains useful when the actual excess distribution is retained.

## 5. Orientation-flow coupling

For a fixed total excess `E` and source margin `q`, the target-capacity flow may safely use

```text
P_u = min(
  b-1-q_u,
  rho_u+b-a-1,
  d_KD(u)-q_u,
  total-excess source cap when applicable
).                                                    (16)
```

Every actual incoming degree `p_u` is at most `P_u`. Therefore failure of the orientation target-flow Hall system with these strengthened capacities is a valid exclusion certificate for that `(E,q)` branch.

This is selection-free at the excess-profile level: it requires only total `E`, not the individual `e_i`.

## 6. Proof-certificate form

For a rejected source profile it is enough to record

```text
E,
q,
rho,
z,
k_*(u),
P_u,
```

plus the target-flow cut or aggregate capacity deficit that fails. No floating-point solver is required.

## 7. Trust boundary

The summation in (3)/(10) is elementary once the selected-excess incidence inequality (1) and source-label simplicity are accepted. Its Murty-Simon application therefore inherits the trust boundary of those canonical-bridge statements. It is a necessary condition only; satisfying the cap does not imply graph feasibility.
