# Type-compressed orientation Hall theorem

14 September 2026. **Candidate structural theorem inside the canonical selected/residual bridge. External mathematical review and novelty assessment remain OPEN.**

## 1. Purpose

The post-pair relational scan shows that the directed target-capacity Hall condition is frequently stronger than the preceding scalar and unordered-pair conditions. The exact target network from [`../2026-09-13-alternative-attacks-v1/ORIENTATION_FLOW_HALL.md`](../2026-09-13-alternative-attacks-v1/ORIENTATION_FLOW_HALL.md) has one source copy and one target copy of every `u in B`:

```text
source -> u_L     capacity q_u,
u_L -> w_R      capacity 1 if D(u,w),
w_R -> sink       capacity P_w,
```

where

```text
c_u=q_u+rho_u,
D(u,w) iff u!=w,
            q_u<=c_w+1,
            q_w<=c_u.
```

The ordinary capacitated Hall criterion quantifies over every vertex subset `W subseteq B`. The theorem below shows that, once a `q,c,P` profile is fixed, all subsets with the same counts of identical source types are exactly equivalent. This is an exact compression, not a relaxation.

## 2. Types

Group vertices by the triple

```text
tau=(q_tau,c_tau,P_tau).
```

Let `T_tau` be the corresponding type class and

```text
n_tau=|T_tau|.
```

For two types define the identity-free compatibility indicator

```text
A_{tau,sigma}=1
```

exactly when the numerical directed compatibility inequalities hold:

```text
q_tau<=c_sigma+1,
q_sigma<=c_tau.
```

The actual vertex relation still deletes the diagonal `u=w`. In the canonical setting `c_tau=q_tau+rho_tau>=q_tau`, so `A_{tau,tau}=1`; it is retained symbolically below to make the diagonal correction explicit.

For a source subset `W`, write

```text
x_tau=|W cap T_tau|,
0<=x_tau<=n_tau.
```

Define the type-level incoming multiplicity at a target of type `sigma` before deleting its own source copy by

```text
m_sigma(x)=sum_tau A_{tau,sigma} x_tau.                (1)
```

## 3. Exact compressed cut formula

A target `w` of type `sigma` sees

```text
m_sigma(x)
```

sources from `W` if `w notin W`, and

```text
m_sigma(x)-A_{sigma,sigma}
```

if `w in W`, because only then must the forbidden self-arc be removed.

There are `n_sigma-x_sigma` targets of the first kind and `x_sigma` of the second kind. Hence the complete target capacity available to `W` is exactly

```text
R(x)=sum_sigma [
       (n_sigma-x_sigma) min(P_sigma,m_sigma(x))
       + x_sigma min(P_sigma,m_sigma(x)-A_{sigma,sigma})
     ].                                                (2)
```

The source demand of `W` is

```text
L(x)=sum_tau q_tau x_tau.                              (3)
```

Therefore:

> **Type-compressed orientation Hall theorem.** The directed target-flow relaxation has a value-`Q` flow if and only if, for every integer type-count vector `x` satisfying `0<=x_tau<=n_tau`,
>
> ```text
> L(x)<=R(x).                                          (4)
> ```
>
> Equivalently, target-flow infeasibility has a certificate consisting only of the finite type table and one violating integer count vector `x`.

### Proof

The vertex-level capacitated Hall theorem says that a value-`Q` flow exists if and only if every source subset `W` satisfies

```text
sum_{u in W} q_u
 <= sum_{w in B} min(P_w, |N_D^-(w) cap W|).           (5)
```

Fix the type-count vector `x` of `W`. The left side of (5) is exactly (3). For any target `w` of type `sigma`, all numerical compatibility tests against a source depend only on the source type. Thus the number of compatible sources in `W` is `m_sigma(x)`, except that the source copy of `w` itself must be deleted when `w in W`, giving `m_sigma(x)-A_{sigma,sigma}`. Summing the target contribution over the `n_sigma-x_sigma` targets outside `W` and the `x_sigma` targets inside `W` gives (2).

Hence every two source subsets with the same type-count vector have identical Hall demand and identical Hall capacity. Quantifying over all subsets `W` is therefore exactly equivalent to quantifying over all feasible integer vectors `x`. QED.

## 4. Canonical simplification

Because the canonical bridge has

```text
c_tau=q_tau+rho_tau>=q_tau,
```

we always have `A_{tau,tau}=1`. Thus (2) becomes

```text
R(x)=sum_sigma [
       (n_sigma-x_sigma) min(P_sigma,m_sigma(x))
       + x_sigma min(P_sigma,m_sigma(x)-1)
     ].                                                (6)
```

The only non-type-symmetric feature of the original vertex network is therefore a one-unit diagonal correction on targets whose own source lies in the cut.

## 5. Two-dimensional dominance form

The compatibility test

```text
q_tau<=c_sigma+1,
c_tau>=q_sigma
```

is a two-dimensional dominance rectangle. Consequently

```text
m_sigma(x)
```

is a weighted two-dimensional orthant count of the chosen source types.

This makes precise the earlier diagnosis that there is no general one-dimensional Ferrers ordering. The exact target Hall obstruction is nevertheless much smaller than an arbitrary `2^b` subset system whenever the profile has repeated `(q,c,P)` types.

The theorem therefore offers two possible routes:

1. **finite acceleration:** enumerate bounded type counts rather than labelled source subsets when extracting Hall cut certificates;
2. **general theory:** seek inequalities controlling the minimum of `R(x)-L(x)` over two-dimensional dominance count vectors.

## 6. Single-type and few-type corollaries

If `W` uses `x` sources from one type `tau` and no other source type, then (6) gives the explicit necessary inequality

```text
x q_tau
 <= sum_{sigma!=tau:A_{tau,sigma}=1}
       n_sigma min(P_sigma,x)
    +(n_tau-x) min(P_tau,x)
    +x min(P_tau,x-1).                                (7)
```

This family detects congestion caused by repeated high-demand sources even when every one of them individually has enough targets.

More generally, a cut supported on `k` source types is governed by a `k`-variable integer inequality obtained directly from (1)-(4). Thus a useful empirical question is how many source types are needed by the minimum deficient cuts on the current frontier.

## 7. Important non-claim: whole type classes only

The theorem does **not** assert that it is enough to choose

```text
x_tau in {0,n_tau}.
```

The `min(P_sigma,m_sigma)` saturation and the diagonal correction can make a proper fraction of a repeated type the strongest cut. The committed verifier searches explicitly for such counterexamples. If found, they are preserved as a warning against replacing (4) by a whole-type-only test.

## 8. Certificates and audit

A compressed target-Hall failure can be recorded as:

```text
(type q,c,P,n table),
violating x vector,
all m_sigma(x),
L(x),
R(x),
deficiency L-R.
```

Every quantity is integer. Expanding any count vector `x` to an arbitrary labelled subset with those type counts reproduces the same vertex-level Hall cut exactly.

[`verify_type_compressed_orientation_hall.py`](verify_type_compressed_orientation_hall.py) independently checks the formula against direct labelled-subset enumeration on a deterministic small-profile suite and searches for a failure of the stronger whole-type-only shortcut.

## 9. Trust boundary

This theorem is an exact compression of the target-flow relaxation once the data `(q,c,P)` and the directed compatibility relation are accepted. Its Murty-Simon application still depends on the canonical graph-to-constraint bridge and on the validity of the target capacity bounds used to define `P`. Passing all compressed cuts is only target-flow feasibility, not graph feasibility.

The unrestricted Murty-Simon conjecture is not proved by this result.
