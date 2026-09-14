# Synthesis with the concurrent selected-excess tail-loss checkpoint

The interval-budget note was committed on top of `94cbfd966f6fd913ad9f96bdc4b0ba835c530dbb`, which appeared during this session and was then explicitly reviewed. That checkpoint's [selected-excess tail-loss identity](../2026-09-14-type-compressed-orientation-hall-v1/SELECTED_EXCESS_TAIL_LOSS_BUDGET.md) and the interval bound are complementary, not rival claims.

Use delta=b-a and E=Esel. For j=1,...,delta define

```text
alpha_j=min(E,z)+floor(max(E-z,0)/j)+1,
ell_u=sum_j 1_{q_u>=alpha_j},
eta_u=(c_u+delta-1-dK_u-ell_u)_+,
L_K=sum_u eta_u.
```

The exact cap identity is P_u=rho_u+delta-1-ell_u-eta_u. Consequently the interval note's total cap loss is

```text
Lambda=sum_j N(alpha_j)+L_K.
```

Substitution into its one-sided theorem gives the entirely explicit sufficient criterion

> ```text
> 2t+D0+Esel + sum_{j=1}^{delta}N(alpha_j) + L_K
> + Omega_tau - Q_<tau > b(delta-1).
> ```

Whenever this inequality holds, the high-q tail at tau is deficient. Adding Xi_tau makes the left side minus b(delta-1) the EXACT tail deficiency. No universal existence of such a tau has been proved.

In the concurrent note's notation, the exact vacancy V(T_tau) is precisely Omega_tau+Xi_tau. Its aggregate sum-P screen is Lambda<=G; the interval contribution identifies when remaining capacity cannot be reached even after dropping reverse compatibility. Thus the new frozen detection figures must not be described as new exclusions from the already-used sum-P screen.

The independent interval verifier also checks the selected-loss identity on 179,375 scalar cases, including zero demands, z>E, q=0 and absent selected caps, and checks the combined cap decomposition whenever target_caps is evaluated. The ordinary graph bridge and external review remain separate assumptions.
