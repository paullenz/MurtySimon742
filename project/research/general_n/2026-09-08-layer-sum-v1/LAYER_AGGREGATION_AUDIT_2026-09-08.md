# Adversarial audit of the layer aggregation

8 September 2026. Internal assurance by ChatGPT/Geeps. **The full 13/22 result remains CANDIDATE; independent mathematical review remains OPEN.**

## Verdict

No blocking defect has been found in the passage from the threshold family

    2 W_h <= z_h^2-z_h+h(h+1)

to the cubic residual inequality. The audit instead exposes a slightly stronger intermediate statement. If

    H=max_i s_i,
    r_H=sum_{h=1}^H z_h=sum_u min(rho_u,H),

then for S>0

    3 S^3 <= a^2 r_H(2r_H+1).                       (A)

Since r_H<=r, this immediately implies the published candidate inequality

    3 S^3 <= a^2 r(2r+1).

The stronger form isolates the only final relaxation: replacing the residual mass visible below the maximum demand by the full residual mass.

## 1. Maximum-demand confinement is stronger than previously stated

Choose a label i with s_i=H. Since x_i>=s_i, that label occurs on at least H distinct selected cross-edges. They have distinct sources because a simple cross-edge (u,i) can be selected at most once. Source demand gives rho_u>=H at each of those sources.

Consequently every one of the first H residual tail counts contains those H sources:

    z_h>=H  for 1<=h<=H.

Summing gives the stronger observation

    r_H=sum_{h=1}^H z_h >= H^2.                     (B)

The earlier proof only recorded H^2<=r. Statement (B) is what the aggregation actually supplies before the final relaxation r_H<=r.

## 2. First Cauchy-Schwarz step

Let

    W_h=sum_{i:s_i>=h} s_i,
    L=sum_{h=1}^H sqrt(W_h).

The layer-cake identity is exact:

    sum_h W_h=sum_i s_i^2.

Cauchy-Schwarz on the a demands gives

    S^2 <= a sum_i s_i^2 = a sum_h W_h.

Also W_h<=S, so W_h<=sqrt(S)sqrt(W_h). Hence

    sum_h W_h <= sqrt(S)L.

For S>0,

    S^3 <= a^2 L^2.                                 (C)

There is no reversal or strictness issue here. The only use of W_h<=S is termwise and all quantities are nonnegative.

## 3. Weighted Cauchy-Schwarz step

Because z_h>=H>=1, every denominator is positive. Write

    sqrt(W_h)=sqrt(z_h)*sqrt(W_h/z_h).

Cauchy-Schwarz gives

    L^2 <= (sum_h z_h)(sum_h W_h/z_h)
         = r_H sum_h W_h/z_h.                       (D)

Divide the threshold inequality by z_h and sum:

    2 sum_h W_h/z_h
      <= sum_h z_h - H + sum_h h(h+1)/z_h
      = r_H-H + sum_h h(h+1)/z_h.

Using z_h>=H,

    sum_h h(h+1)/z_h
      <= (1/H) sum_{h=1}^H h(h+1)
      = (H+1)(H+2)/3.

Therefore

    2 sum_h W_h/z_h
      <= r_H + (H^2+2)/3
      <= r_H + (r_H+2)/3
      = (4r_H+2)/3,                                 (E)

where the second inequality is exactly (B).

Combining (D) and (E) gives

    3 L^2 <= r_H(2r_H+1).                           (F)

Equations (C) and (F) prove (A). Since x -> x(2x+1) is increasing for x>=0 and r_H<=r, the original cubic bound follows.

This version is cleaner than the earlier presentation because no mixed replacement of r_H and H^2 by r is needed inside one product.

## 4. Independent abstract counterexample search

A new checker, `src/check_layer_aggregation_adversarial.py`, does not enumerate graphs. It enumerates every nondecreasing demand multiset of length a with entries in {0,...,a-1} for every 1<=a<=11. For each profile it constructs the componentwise-minimal nonincreasing integer tail z_h satisfying exactly the two structural consequences used here:

1. z_h>=H for 1<=h<=H;
2. 2W_h<=z_h^2-z_h+h(h+1).

The monotone closure is necessary because z_h is a degree-tail count. This is adversarial: any other feasible tail has at least as much truncated mass r_H, and the right side of (A) is increasing in r_H. Thus the minimal tail is the hardest abstract case for the cubic inequality for that demand profile.

The complete domain through a=11 contains:

    sorted demand profiles:       478,192
    nonzero profiles:             478,181
    threshold levels checked:   4,215,632

The checker also verifies the layer-cake identity, S^2<=a sum s_i^2, r_H>=H^2, the exact rational summed-threshold estimate, and (A) using integer arithmetic except for exact `Fraction` divisions.

The smallest observed integer slack in (A) is positive. The smallest observed ratio RHS/LHS is

    13301/11000 = 1.2091818...

at a=11 with all eleven demands equal to 10 and r_H=141. This numerical margin is not asserted to persist asymptotically and is not used in the proof.

## 5. Scope and remaining risk

This audit is deliberately abstract. It does not claim that every tested demand/tail profile is graph-realisable, nor does it use absence of a finite counterexample as the universal proof. The universal argument is the short chain (B)-(F), using standard Cauchy-Schwarz plus the already-audited threshold inequality.

The main remaining mathematical risks now lie upstream and downstream rather than inside the aggregation algebra:

* upstream: the graph-to-threshold structural premises, especially source demand and high-source supplement confinement;
* downstream: solving the cubic residual inequality into the surplus bound `t<4a^2/81+1/8` and assembling the exact 13/22 degree consequence.

The upstream pieces now have separate construction, residual-injection and threshold-capacity audits, plus a scoped local Lean slice for quasi-edge logic. The full finite-cardinality reduction and the layer aggregation are not formally verified in Lean.

**Research decision:** treat the layer aggregation as internally strengthened, with (A) as the preferred intermediate statement. Before trying to improve 13/22, attack the downstream cubic-to-surplus optimisation and small-order assembly independently.
