# Summed high-q-tail pressure

14 September 2026. **Exact hand consequence of the high-q-tail Hall family inside the directed target-capacity model. External review remains OPEN.**

This note does **not** assume that high-q tails are sufficient for all Hall failures. Instead, it asks what follows if every high-q tail is nondeficient. The result converts the whole tail family into weighted source-load inequalities.

## 1. High-q tails

For integer `t>=1`, let

```text
S_t={u:q_u>=t}.
```

For target `w`, define

```text
N_t(w)=#{u in S_t:D(u,w)}.
```

The exact receiver capacity of the tail is

```text
H_t=sum_w min(P_w,N_t(w)),                             (1)
```

while its source demand is

```text
D_t=sum_{u:q_u>=t}q_u.                                 (2)
```

If every high-q tail is nondeficient, then

```text
D_t<=H_t                                                (3)
```

for every `t`.

## 2. Weighted layer-cake form

Choose arbitrary weights

```text
lambda_t>=0
```

and define the nondecreasing transform

```text
Phi(j)=sum_{1<=t<=j}lambda_t,
Phi(0)=0.                                               (4)
```

Summing (2) against the weights gives

```text
sum_t lambda_t D_t
 = sum_u q_u Phi(q_u).                                 (5)
```

For a fixed target `w`, list the demands of all directed-compatible sources in nonincreasing order:

```text
r_{w,1}>=r_{w,2}>=...>=r_{w,m_w}.                      (6)
```

The layer-cake identity gives

```text
sum_t lambda_t min(P_w,N_t(w))
 = sum_{j=1}^{min(P_w,m_w)} Phi(r_{w,j}).               (7)
```

Indeed `min(P_w,N_t(w))` counts how many of the top `P_w` compatible-source demands reach level `t`; summing their threshold weights reconstructs `Phi`.

Therefore:

> **Weighted q-tail pressure theorem.** If every high-q tail is nondeficient, then for every nonnegative weight sequence `lambda`,
>
> ```text
> sum_u q_u Phi(q_u)
> <=
> sum_w sum_{j=1}^{min(P_w,m_w)} Phi(r_{w,j}).          (8)
> ```

No approximation is used in (8).

Conversely, taking `lambda` supported on one threshold recovers the corresponding tail inequality (3). Thus the full weighted family is simply a dual/layer-cake encoding of all high-q-tail Hall cuts.

## 3. Uniform-weight quadratic consequence

Take

```text
lambda_t=1,
Phi(j)=j.
```

Equation (8) becomes

> ```text
> sum_u q_u^2
> <=
> sum_w TopSum_{P_w}{q_u:D(u,w)}.                      (9)
> ```

Here `TopSum_P` means the sum of the `P` largest values, using all compatible values if fewer than `P` exist.

This is the exact summed-tail pressure inequality.

Because directed compatibility implies

```text
q_u<=c_w+1
```

for every source counted at target `w`, a weaker scalar corollary is

```text
sum_u q_u^2
 <= sum_w P_w(c_w+1).                                  (10)
```

The exact top-compatible form (9) is usually much stronger than (10).

## 4. Combination with the canonical target caps

The current post-pair caps give, among other terms,

```text
P_w<=rho_w+b-a-1,
P_w<=b-1-q_w,
P_w<=d_K(w)-q_w,                                       (11)
```

plus the selected-excess cap where applicable.

Substituting any valid upper cap into (10) gives theorem-safe scalar necessary conditions. For example,

```text
sum q_u^2
 <= sum_w (rho_w+b-a-1)(c_w+1)                         (12)
```

whenever the residual cap is nonnegative on a legal branch.

These scalar projections are not claimed to be sharp enough for the all-order proof; their role is to expose which moments of the q-distribution a tail argument controls.

## 5. Frozen 812-profile diagnosis

The 812 difficult frozen profiles from GitHub Actions run `34850187436` were evaluated against (9).

```text
profiles:                         812
violating exact top-compatible (9): 476
not violating (9):                336
```

The much weaker scalar projection (10) detects only one of the 812 profiles.

Thus the exact compatible-source ranking matters substantially. At the same time, a single unweighted quadratic moment cannot explain the complete tail phenomenon.

A finite minimax test over common nonnegative weights also found no one fixed strict weighted combination covering all 812 profiles. This is reconnaissance only, but it shows why the next proof should permit an **adaptive threshold or structural case split**, rather than searching for one universal quadratic potential.

## 6. Relation to the bridge defect decomposition

[`BRIDGE_TWO_DEFECT_DECOMPOSITION.md`](BRIDGE_TWO_DEFECT_DECOMPOSITION.md) gives

```text
Q=r+2t+D0+Esel.                                        (13)
```

The left side of (9) is bounded below by concentration inequalities in terms of `Q`, while the right side is controlled by target caps and compatibility. Therefore (9) is a natural place to combine:

```text
net selected-load surplus Q-r,
q-distribution concentration,
receiver-cap scarcity,
directed compatibility.                                (14)
```

The frozen diagnosis shows that this route can explain a large part, but not all, of the difficult residue without retaining the individual threshold cuts.

## 7. Trust boundary

Equations (5)-(10) are elementary layer-cake identities inside the directed target-capacity Hall model. They make no q-tail sufficiency claim. The 812-profile reach numbers are reconnaissance and not a theorem. Murty-Simon use of the cap substitutions inherits the canonical bridge trust boundary.
