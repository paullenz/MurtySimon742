# Canonical antichain certificate for orientation Hall

14 September 2026. **Candidate exact structural corollary for the directed target-capacity Hall relaxation. External mathematical review and novelty assessment remain OPEN.**

This note combines the exact type-level Hall margin, its submodularity, and the sharpened dominance exchange theorem into a canonical certificate format.

## 1. Setup

Use the complete-type Hall margin

```text
F(S)=
 sum_sigma n_sigma
   min(P_sigma, sum_{tau in S} w_{tau,sigma})
 -sum_{tau in S} n_tau q_tau,
```

from [`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md). Here `S` is a set of distinct `(q,c,P)` types and the diagonal deletion is already absorbed into `w`.

The target flow is feasible exactly when

```text
min_S F(S) >= 0.                                      (1)
```

The function `F` is submodular.

Use the sharp hardness order from [`SHARP_DOMINANCE_UPSET_HALL.md`](SHARP_DOMINANCE_UPSET_HALL.md):

```text
x >=_* y
iff c_x <= c_y
    and [q_x > q_y or (q_x=q_y and P_x>=P_y)].         (2)
```

## 2. The minimizers form a lattice

Let

```text
m=min_S F(S).
```

If `S` and `T` are both minimizers, submodularity gives

```text
F(S cap T)+F(S union T) <= F(S)+F(T)=2m.
```

But both terms on the left are at least `m`, so equality is forced:

```text
F(S cap T)=F(S union T)=m.                             (3)
```

Hence the family of minimizers is closed under intersection and union.

Because the type set is finite, there are therefore unique extremal minimizers

```text
M^- = intersection of all minimizers,
M^+ = union of all minimizers.                         (4)
```

`M^-` is the unique inclusion-minimal minimizer and `M^+` the unique inclusion-maximal minimizer. In particular, `M^+` is the unique maximum-cardinality minimizer.

## 3. Canonical sharp up-set

The sharp dominance theorem proves that every maximum-cardinality minimizer is an up-set under `>=_*`. Since `M^+` is the unique maximum-cardinality minimizer,

> **Canonical maximal-witness theorem.** `M^+` is a sharp-hardness up-set.

Thus there is no need to choose an arbitrary deficient Hall cut. The data `(q,c,P,n)` determine a unique preferred minimum-margin witness `M^+`.

If `m<0`, this is a canonical Hall-failure certificate. If `m>=0`, no target-Hall failure exists.

## 4. Unique antichain boundary

Let `A` be the set of minimal elements of `M^+` under `>=_*`. Then:

1. `A` is an antichain;
2. `A` is unique;
3. `M^+` is exactly the up-closure of `A`:

```text
M^+ = up_*(A)
    = {x : x>=_*a for some a in A}.                    (5)
```

Therefore every target-Hall failure has a canonical compact representation

```text
(type table, antichain A, M^+=up_*(A), F(M^+)=m<0).    (6)
```

The generator set can genuinely contain more than one incomparable type. The preserved examples in [`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](PRINCIPAL_UPSET_COUNTEREXAMPLE.md) show that one generator is insufficient in general and that even two generators are not enough in every small profile.

## 5. Staircase shape of the boundary

The sharp order imposes a useful geometry on `A`.

Take distinct generators `g,h in A`.

### Different demands

If

```text
q_g < q_h,
```

then necessarily

```text
c_g < c_h.                                             (7)
```

Otherwise `c_h<=c_g`, and the strict demand inequality would give `h>=_*g`, contradicting that `A` is an antichain.

Thus generators with distinct demand values form a strictly increasing staircase in the `(q,c)` plane.

### Equal demand

If

```text
q_g=q_h,
c_g<c_h,
```

then necessarily

```text
P_g<P_h.                                               (8)
```

Otherwise `P_g>=P_h` and `g>=_*h`.

So within one demand level, increasing `c` along the boundary forces strictly increasing target cap `P`.

These conditions do not bound the generator count by a universal constant; they identify the exact staircase geometry that any stronger theorem must control.

## 6. Extraction from one maximum flow

[`DOMINANCE_CLOSED_MAXFLOW.md`](DOMINANCE_CLOSED_MAXFLOW.md) adds closure arcs of capacity `Q+1` from an easier source type to every harder type that dominates it. Since every ordinary cut has capacity at most `Q`, no minimum cut crosses such an arc, and the minimum-cut value is unchanged.

After any maximum flow in this closure-augmented quotient network, let `R_t` be the vertices that can reach the sink through residual-capacity arcs. Then

```text
V \ R_t                                                (9)
```

is the unique **maximal source-side minimum cut**. Every source-side minimum cut is contained in it: if a source-side cut contained a vertex with a residual path to the sink, some residual arc on that path would leave the cut, contradicting equality of the cut capacity with the maximum-flow value.

Projecting the source-type nodes of `V\R_t` gives exactly `M^+`. Its minimal sharp-hardness elements give `A`.

Consequently the canonical antichain certificate can be extracted in polynomial time from one exact integer max-flow computation; exponential type-set enumeration is not required.

## 7. Certificate audit

A verifier needs only:

```text
1. the type table (q,c,P,n),
2. the claimed generator antichain A,
3. the reconstructed up-closure M^+,
4. the integer Hall margin F(M^+).
```

For stronger provenance it may also replay the closure-augmented quotient max flow and verify that the maximal residual min-cut projects to the same `M^+`.

[`verify_canonical_antichain_certificate.py`](verify_canonical_antichain_certificate.py) performs this comparison on exhaustive small profiles and a deterministic broad challenge.

## 8. Trust boundary

This is exact for the directed target-capacity Hall relaxation once the `(q,c,P)` profile and target caps are accepted. Its Murty-Simon application inherits the canonical graph-to-constraint bridge. A target-flow obstruction is a necessary-condition failure; target-flow feasibility is not graph realizability.

The unrestricted Murty-Simon conjecture is not proved by this result.
