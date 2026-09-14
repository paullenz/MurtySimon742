# Exact type-level max-flow corollary

14 September 2026. **Candidate structural corollary of the whole-type orientation Hall theorem. External mathematical review and novelty assessment remain OPEN.**

## 1. Setup

Use the target-flow relaxation and type notation of [`TYPE_COMPRESSED_ORIENTATION_HALL.md`](TYPE_COMPRESSED_ORIENTATION_HALL.md). A type

```text
tau=(q_tau,c_tau,P_tau)
```

has multiplicity `n_tau`, with every `P_tau` a nonnegative integer target-capacity upper bound. Numerical directed compatibility is

```text
A_{tau,sigma}=1
 iff q_tau<=c_sigma+1 and q_sigma<=c_tau.
```

In the canonical application `c_tau>=q_tau`, so `A_{tau,tau}=1`.

The full labelled target network has `n_tau` source vertices of type `tau`, each demanding `q_tau`, and `n_sigma` target vertices of type `sigma`, each with capacity `P_sigma`. Every compatible ordered pair gives a unit source-target edge, except that the diagonal `u=w` is deleted.

## 2. Quotient network

Construct a type-level network with nodes

```text
s,
{tau_L},
{sigma_R},
t.
```

Give it capacities

```text
s -> tau_L:
    n_tau q_tau,                                       (1)

tau_L -> sigma_R:
    0                              if A_{tau,sigma}=0,
    n_tau n_sigma                  if A_{tau,sigma}=1 and tau!=sigma,
    n_tau(n_tau-1)                 if tau=sigma,        (2)

sigma_R -> t:
    n_sigma P_sigma.                                   (3)
```

Let

```text
Q=sum_tau n_tau q_tau.
```

Then:

> **Exact type-level max-flow theorem.** The full labelled target-flow network has a value-`Q` flow if and only if the quotient type network (1)-(3) has a value-`Q` flow.

### Necessity

Aggregate any labelled value-`Q` flow by source and target types. A distinct-type block contains at most `n_tau n_sigma` unit ordered pairs; a same-type block contains at most `n_tau(n_tau-1)` because the diagonal is absent. The aggregated flow therefore respects (1)-(3).

### Sufficiency via min cuts

Consider a type-set `S` placed on the source side of a quotient-network cut. For a target type `sigma`, the total compatible capacity arriving from `S` is

```text
n_sigma m_sigma(S)          if sigma notin S,
n_sigma(m_sigma(S)-1)       if sigma in S,              (4)
```

where

```text
m_sigma(S)=sum_{tau in S} A_{tau,sigma} n_tau.
```

Optimizing the side of `sigma_R` contributes exactly

```text
n_sigma min(P_sigma,m_sigma(S))
```

when `sigma notin S`, and

```text
n_sigma min(P_sigma,m_sigma(S)-1)
```

when `sigma in S`. Thus the quotient min-cut condition for every source-type set `S` is precisely the complete-type Hall inequality

```text
L(S)<=R(S)                                             (5)
```

from the whole-type orientation Hall theorem.

That theorem proves that these complete-type cuts are equivalent to **all** labelled source-subset Hall cuts. By max-flow/min-cut in the labelled network, (5) for every `S` is equivalent to a labelled value-`Q` flow. Hence quotient value `Q` is sufficient. QED.

## 3. Compact cut function

The diagonal correction can be absorbed into a type-to-target weight

```text
w_{tau,sigma}=
    A_{tau,sigma} n_tau     if tau!=sigma,
    n_sigma-1               if tau=sigma.              (6)
```

Because `A_{sigma,sigma}=1`, for every type set `S`,

```text
m_sigma(S)-1_{sigma in S}
 =sum_{tau in S} w_{tau,sigma}.                        (7)
```

Therefore the Hall margin has the closed set-function form

```text
F(S)=
 sum_sigma n_sigma
   min(P_sigma, sum_{tau in S} w_{tau,sigma})
 -sum_{tau in S} n_tau q_tau.                          (8)
```

The target flow is feasible exactly when

```text
min_S F(S)>=0.                                         (9)
```

A negative minimizer is a complete-type Hall certificate.

## 4. Submodularity

For fixed `sigma`,

```text
S -> sum_{tau in S} w_{tau,sigma}
```

is a nonnegative modular set function. The truncation

```text
x -> min(P_sigma,x)
```

is nondecreasing and concave. A concave nondecreasing function of a nonnegative modular set function is submodular. Therefore every target term in (8) is submodular.

The source-demand term

```text
sum_{tau in S} n_tau q_tau
```

is modular, so subtracting it preserves submodularity. Hence:

> **Submodular Hall-margin corollary.** `F(S)` in (8) is a submodular set function on the type set.

This gives the uncrossing inequality

```text
F(S cap T)+F(S union T)<=F(S)+F(T).                    (10)
```

Consequently, if two type sets both attain the global minimum Hall margin, their intersection and union also attain the same minimum. More generally, if `F(S)<0` and `F(T)<0`, then (10) guarantees that at least one of `S cap T` and `S union T` is also deficient.

## 5. Why this is useful

The result has three distinct uses.

### Exact computational compression

A labelled target network with `b` source vertices, `b` target vertices and up to `b(b-1)` unit compatibility arcs is replaced by a network with `k` source types, `k` target types and at most `k^2` aggregate arcs, where `k` is the number of distinct `(q,c,P)` types.

The quotient network is **exact**, not a relaxation.

### Small integer certificates

A failure certificate can be recorded entirely by

```text
(type table, deficient type set S, F(S)).
```

No labelled cut is needed.

### General-theory route

The compatibility relation is a two-dimensional dominance condition in `(q,c)`, while the exact obstruction is now the minimum of the submodular function (8). This suggests a concrete next problem: characterize a minimum deficient type set using the dominance order. Standard submodularity alone does **not** prove that a minimizer is a down-set, up-set, antichain, or one-dimensional prefix; any such further compression requires its own proof or counterexample search.

## 6. Red-team boundary

This corollary does **not** claim that an arbitrary feasible flow in the quotient network can be naively expanded edge-by-edge into a labelled flow. Sufficiency is established through equality of the complete-type min-cut conditions plus the whole-type Hall theorem, not by assuming a block-flow decomposition.

Likewise, submodularity does not make every deficient-set family closed under union and intersection. Equation (10) only gives the stated uncrossing consequences.

## 7. Verification

[`verify_type_level_maxflow.py`](verify_type_level_maxflow.py) independently constructs both networks on deterministic small profiles, computes exact integer max flows, evaluates every type-set margin (8), and checks:

1. labelled max flow equals quotient max flow;
2. both equal `Q` exactly when `min_S F(S)>=0`;
3. the direct complete-type Hall formula equals (8);
4. the submodular inequality (10) holds for every pair of type sets in the exhaustive test suite.

The finite verifier supports but does not replace the hand proof.

## 8. Trust boundary

The quotient theorem is exact for the directed target-flow relaxation. Its Murty-Simon application inherits the canonical bridge and the target-capacity assumptions. Feasibility of this target flow is still only a necessary condition for a diameter-two edge-critical graph.

The unrestricted Murty-Simon conjecture is not proved by this result.
