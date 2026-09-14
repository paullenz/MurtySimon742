# Exterior-slack sharp-upset reduction

14 September 2026. **Candidate exact structural corollary inside the canonical target-Hall framework. External mathematical review and novelty assessment remain OPEN.**

The strict exterior slack-expansion theorem quantifies over every nonempty exterior source set. This note shows that a failure of that strict expansion would always have a sharp-upset certificate in a second Hall system whose target capacities are the residual slacks left by the primary canonical witness.

The consequence is a two-staircase formulation of the canonical obstruction.

## 1. Labelled canonical maximal witness

Work first on the labelled target-Hall margin

```text
F(W)=sum_w min(P_w,d_W(w))-sum_{u in W}q_u.            (1)
```

The function is submodular, so its minimizers form a lattice. Let

```text
M+ = union of all labelled minimizers.                  (2)
```

Then `M+` is the unique inclusion-maximal minimizer. The sharp dominance theorem makes every maximum-cardinality minimizer a sharp-hardness up-set; identical `(q,c,P)` vertices dominate one another both ways, so `M+` is a union of complete types and coincides with the canonical complete-type maximal witness used elsewhere in the package.

Consequently, for **every nonempty labelled set**

```text
T subseteq B\M+,                                       (3)
```

integrality and maximality give

```text
F(M+ union T)>=F(M+)+1.                                (4)
```

Thus the strict exterior expansion may be read at labelled level, not only after complete-type aggregation.

## 2. Residual-slack Hall system

For each target vertex `w`, define

```text
s_w=(P_w-d_M+(w))_+,                                   (5)
```

where `d_M+(w)` is the number of directed-compatible sources from `M+`, with the usual diagonal deletion.

Let

```text
O=B\M+.                                                 (6)
```

For `T subseteq O`, define

```text
F_s(T)
 =sum_w min(s_w,k_T(w))-sum_{u in T}q_u,               (7)
```

where `k_T(w)` is the exact compatible-source count contributed by `T`.

Subtracting `F(M+)` from `F(M+ union T)` gives exactly

```text
F_s(T)=F(M+ union T)-F(M+).                            (8)
```

Hence (4) is equivalent to

```text
F_s(T)>=1 for every nonempty T subseteq O.              (9)
```

The exterior of a canonical maximal witness is therefore a **strictly expanding Hall system** with the same directed compatibility geometry and residual target caps `s_w`.

## 3. Residual sharp-hardness order

Apply the sharp exchange lemma to the residual system (7). Its source intervals remain `[q_u,c_u]`; only target capacities change from `P_w` to `s_w`.

Define on exterior labelled vertices

```text
x >=_s y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and s_x>=s_y)].            (10)
```

The proof of the one-unit diagonal-loss and equal-demand exchange lemmas is unchanged with `s` in place of `P`. Therefore a maximum-cardinality global minimizer of `F_s` is an up-set under `>=_s`.

## 4. Exact reduction of strict expansion to nonempty up-sets

> **Exterior-slack up-set theorem.** The following are equivalent:
>
> 1. `F_s(T)>=1` for every nonempty `T subseteq O`;
> 2. `F_s(U)>=1` for every nonempty `>=_s` up-set `U subseteq O`.

### Proof

`1 => 2` is immediate.

For the converse, suppose 1 fails. Because all values are integers, there is a nonempty `T` with

```text
F_s(T)<=0.                                              (11)
```

The empty set has `F_s(empty)=0`, so the global minimum `m_s` of `F_s` satisfies `m_s<=0`.

- If `m_s<0`, every global minimizer is nonempty. Choose one of maximum cardinality. The sharp dominance-upset theorem applied to target caps `s` makes it a nonempty `>=_s` up-set with margin `<0`.
- If `m_s=0`, both the empty set and at least one nonempty set satisfying (11) are minimizers. By submodularity, the union of all minimizers is again a minimizer. It is nonempty, has maximum cardinality among minimizers, and hence is a `>=_s` up-set with margin `0`.

In either case a nonempty residual sharp up-set violates condition 2. Contradiction. QED.

Thus no arbitrary exterior subset family is required to state the strict expansion system exactly.

## 5. Residual staircase form

Let a nonempty residual sharp up-set have minimal generators under `>=_s`. The same antichain argument as for the primary Hall witness gives, after ordering generators by cross degree,

```text
c_1<...<c_h,
q_1<=...<=q_h,                                         (12)
```

with residual slack cap

```text
s_1<...<s_j
```

strictly increasing along every equal-`q` plateau.

Membership is therefore again a moving threshold:

```text
q>q_i,
or q=q_i and s>=s_i                                   (13)
```

at the first generator cross-degree above the exterior type.

So the full strict exterior expansion theorem is equivalent to requiring positive margin on a family of **residual-slack staircases**.

## 6. Two coupled staircases

Any hypothetical canonical target-Hall failure in the Murty-Simon relaxation now has two coupled structures:

```text
primary system:
  target caps P
  -> deficient canonical maximal staircase M+

exterior residual system:
  target caps s=(P-y(M+))_+
  -> every nonempty residual-slack staircase has margin >=1.
```

The primary staircase creates the residual slack distribution; the exterior sources must then strictly expand into that same distribution.

A general contradiction can therefore seek to prove that Murty residual/source-cap constraints force some residual-slack staircase outside a deficient primary staircase to have margin <=0.

This is substantially narrower than an arbitrary-subset formulation on either side.

## 7. Relation to the layer projection

For each residual-slack staircase `U`, [`EXTERIOR_SLACK_LAYER_PROJECTION.md`](EXTERIOR_SLACK_LAYER_PROJECTION.md) gives the necessary layered inequality

```text
D(U)+1 <= sum_j min(sigma_j,kappa_j(U)).                (14)
```

with Murty bounds on the slack layers and compatibility layers.

Thus the preferred analytic route is now

```text
primary deficient staircase
 -> residual slack layers
 -> residual sharp staircase U
 -> exterior layered upper bound
 -> contradiction with strict +1 expansion.            (15)
```

## 8. Trust boundary

This theorem is an exact finite consequence of labelled Hall submodularity, the canonical maximal-minimizer definition, integrality and the already proved sharp exchange lemma applied with residual caps `s`. Its Murty-Simon interpretation remains conditional on the canonical graph-to-constraint bridge and target-capacity model. It does not assert graph realizability and does not prove the unrestricted conjecture.
