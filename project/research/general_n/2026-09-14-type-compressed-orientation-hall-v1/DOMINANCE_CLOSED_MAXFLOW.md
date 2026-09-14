# Dominance-closed quotient max-flow corollary

14 September 2026. **Candidate structural corollary. External mathematical review and novelty assessment remain OPEN.**

This note combines the exact type-level quotient network from [`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md) with the hardness-upset theorem in [`DOMINANCE_UPSET_HALL.md`](DOMINANCE_UPSET_HALL.md).

## 1. Original quotient network

For each `(q,c,P)` type `tau` of multiplicity `n_tau`, the exact quotient target-flow network has

```text
s -> tau_L                   capacity n_tau q_tau,
tau_L -> sigma_R             capacity n_tau n_sigma
                                 when tau!=sigma and compatible,
tau_L -> tau_R               capacity n_tau(n_tau-1),
sigma_R -> t                 capacity n_sigma P_sigma.
```

Let

```text
Q=sum_tau n_tau q_tau.
```

Its minimum cut has value `Q + min_S F(S)`, where `F` is the complete-type Hall margin.

## 2. Hardness order

Recall

```text
tau >=_H beta
iff q_tau>=q_beta,
    c_tau<=c_beta,
    P_tau>=P_beta.
```

The dominance-upset theorem proves that among all minimum Hall-margin type sets there is one which is an up-set under `>=_H`.

## 3. Closure arcs

Augment the quotient network by adding, for every strict hardness relation

```text
tau >=_H beta,
```

a directed closure arc

```text
beta_L -> tau_L               capacity Q+1.             (1)
```

It is enough in practice to add only cover relations of the transitive reduction of the hardness poset.

Because every ordinary `s-t` cut has the all-source-arcs cut of capacity `Q` available, no minimum cut of the augmented network can cross an arc of capacity `Q+1`.

Thus every minimum cut source side satisfies

```text
beta_L on source side and tau>=_H beta
=> tau_L on source side.                                (2)
```

In other words, its selected source types form a hardness up-set.

## 4. Exactness theorem

> **Dominance-closed max-flow theorem.** Adding the closure arcs (1) does not change the minimum-cut value or the maximum-flow value of the exact type-level target network.

### Proof

Adding arcs cannot decrease a minimum cut, so

```text
mincut_augmented >= mincut_original.                    (3)
```

By the dominance-upset Hall theorem, the original network has a minimum Hall-margin source-type set `S*` which is a hardness up-set. Use the corresponding optimized target side to form an original minimum cut.

Because `S*` is an up-set, that cut crosses no closure arc (1). Therefore it has exactly the same capacity in the augmented network, giving

```text
mincut_augmented <= mincut_original.                    (4)
```

Together (3) and (4) give equality. Max-flow equality follows from max-flow/min-cut. QED.

## 5. Antichain certificate

Every finite-poset up-set is uniquely determined by its minimal elements. Those minimal elements form an antichain.

Therefore a minimum target-Hall witness can be encoded as

```text
(type table,
antichain A of hardness types,
S=up(A),
F(S)).
```

The antichain may contain more than one or two generators. [`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](PRINCIPAL_UPSET_COUNTEREXAMPLE.md) preserves explicit three- and four-type warnings against stronger generator-count shortcuts.

## 6. Why this form is useful

The original exact target network is already polynomial, so the point is not merely computational speed. The closure network exposes a clean order-theoretic boundary:

```text
interval compatibility
+ target capacities
+ source demand
=> 3D hardness poset
=> optimal Hall witness = an up-set
=> witness boundary = an antichain.
```

This reframes the general-theory problem. Rather than classify arbitrary source subsets, one may seek bounds on the antichain boundary of a deficient hardness up-set under the canonical Murty-Simon constraints.

## 7. Trust boundary

This is an exact corollary of the type-level target-flow theorem and the dominance-upset theorem. It does not make the target-flow relaxation sufficient for graph realizability, does not externally verify the canonical bridge, and does not prove the unrestricted Murty-Simon conjecture.
