# Strict exterior slack expansion of the canonical Hall witness

14 September 2026. **Candidate exact structural corollary inside the directed target-capacity Hall relaxation. External mathematical review and novelty assessment remain OPEN.**

The one-type marginal inequalities for the canonical maximal Hall minimizer extend to every collection of exterior type classes. The result gives a second capacitated Hall system living in the **unsaturated receiver slots left by the canonical witness**.

## 1. Canonical witness and receiver slack

Let `M+` be the unique maximal minimum complete-type Hall witness and write

```text
m=F(M+).                                                (1)
```

For every target type `sigma`, let

```text
y_sigma=y_sigma(M+),
s_sigma=(P_sigma-y_sigma)_+.                            (2)
```

Thus `s_sigma` is the target capacity still unused at the level of the Hall capacity function after all sources in `M+` are selected.

Let

```text
O={tau:tau notin M+}                                   (3)
```

be the exterior type set.

## 2. Addition multiplicity of an exterior set

For a nonempty complete-type set `T subseteq O`, define

```text
K_T(sigma)
 = sum_{tau in T} n_tau A_{tau,sigma}
   - 1_{sigma in T},                                   (4)
```

where `A_{tau,sigma}` is the numerical directed-compatibility indicator.

Equation (4) is exactly the additional number of selected sources visible to each fixed target copy of type `sigma` when all classes in `T` are added to `M+`. The subtraction is the forbidden self-source when the target's own type is newly selected.

Therefore the exact target-capacity gain is

```text
G(T)
 = H(M+ union T)-H(M+)
 = sum_sigma n_sigma min(s_sigma,K_T(sigma)).           (5)
```

Let the added source demand be

```text
D(T)=sum_{tau in T} n_tau q_tau.                        (6)
```

## 3. Strict exterior expansion theorem

Since `M+` is the union of **all** minimizers, no strict superset of `M+` is a minimizer. Thus for every nonempty `T subseteq O`, integrality gives

```text
F(M+ union T)>=m+1.                                    (7)
```

Subtracting `F(M+)=m` and using (5)-(6) yields:

> **Strict exterior slack-expansion theorem.** For every nonempty complete-type set `T` outside the canonical witness,
>
> ```text
> sum_sigma n_sigma min(s_sigma,K_T(sigma))
> >= D(T)+1.                                            (8)
> ```

The `+1` is sharp in general.

For singleton `T={tau}`, (8) is exactly the strict exterior marginal inequality from `CANONICAL_HALL_MARGINALS.md`.

## 4. Residual-slot network interpretation

Construct a capacitated bipartite network with:

- one source node for each exterior type `tau in O`, carrying demand `n_tau q_tau`;
- target type `sigma` carrying residual capacity `n_sigma s_sigma`;
- source-target incidence according to the same numerical directed compatibility, with the usual diagonal deletion for a target whose type is itself in the chosen exterior source set.

For any exterior source set `T`, the available residual receiver capacity is exactly the left side of (8). Hence every nonempty source set has residual Hall surplus at least one.

So the canonical maximum minimizer leaves behind a **strictly expanding residual receiver system** outside its staircase boundary.

This is a stronger conceptual statement than saying merely that individual exterior types have positive marginal cost.

## 5. Whole-exterior consequence

Taking `T=O` gives

```text
sum_sigma n_sigma min(s_sigma,K_O(sigma))
 >= D(O)+1.                                             (9)
```

Thus the total demand outside `M+` must fit into the unsaturated compatibility slots left by `M+`, with at least one unit of Hall slack.

Since

```text
min(s_sigma,K_O(sigma))<=s_sigma,                      (10)
```

we obtain the simple necessary condition

```text
sum_sigma n_sigma s_sigma >= D(O)+1                    (11)
```

whenever `O` is nonempty.

The left side is the total unused target-capacity mass at the canonical cut; the right side is the entire source demand outside the cut plus one.

This is potentially useful because

```text
sum_sigma n_sigma s_sigma
 = sum_sigma n_sigma(P_sigma-y_sigma)_+                (12)
```

can be bounded from the Murty-specific target caps and receiver-layer inequalities.

## 6. Interior dual statement

Let `M-` be the intersection of all minimum Hall witnesses. For every nonempty complete-type set

```text
R subseteq M-,                                         (13)
```

`M+\R` cannot be a minimizer. If

```text
L(R)=H(M+)-H(M+\R)                                    (14)
```

is the receiver-capacity loss on removal, then

```text
L(R)<=D(R)-1.                                          (15)
```

For arbitrary `R subseteq M+`, without the `M-` hypothesis, minimality gives only

```text
L(R)<=D(R).                                            (16)
```

## 7. Why this may help general theory

A hypothetical Hall-deficient Murty-Simon profile now has to support two simultaneous structures:

1. an exact deficient canonical staircase `M+`; and
2. a strict residual Hall-expansion system on every collection of types outside that staircase.

The exterior cannot simply be discarded after locating a bad cut: its demand must be routed through the leftover receiver slack of the same profile.

The immediate attack is to combine (11), or the sharper family (8), with:

```text
P_sigma<=b-1-q_sigma,
P_sigma<=rho_sigma+b-a-1,
sum rho=r,
q+rho<=a,
```

and the receiver-layer bounds. A contradiction would show that a canonical deficient staircase cannot coexist with the required exterior expansion.

## 8. Trust boundary

This theorem is an exact consequence of the finite Hall margin and maximal/minimal minimizer definitions. Its Murty-Simon use inherits the canonical bridge and target-capacity model. It does not assert graph realizability from Hall feasibility and does not prove the unrestricted conjecture.
