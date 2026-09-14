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

The ordinary capacitated Hall criterion quantifies over every vertex subset `W subseteq B`. The first compression below replaces labelled subsets by counts of identical `(q,c,P)` types. A second, stronger observation then uses discrete concavity to show that a minimum Hall margin is always attained by a **union of complete type classes**.

Thus the full target-flow Hall test is equivalent to at most `2^k` cuts when the profile has `k` distinct `(q,c,P)` types.

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

The actual vertex relation still deletes the diagonal `u=w`. In the canonical setting `c_tau=q_tau+rho_tau>=q_tau`, so

```text
A_{tau,tau}=1.                                        (1)
```

For a source subset `W`, write

```text
x_tau=|W cap T_tau|,
0<=x_tau<=n_tau.
```

Define the type-level incoming multiplicity at a target of type `sigma` before deleting its own source copy by

```text
m_sigma(x)=sum_tau A_{tau,sigma} x_tau.                (2)
```

## 3. Exact type-count cut formula

A target `w` of type `sigma` sees `m_sigma(x)` sources from `W` if `w notin W`, and `m_sigma(x)-1` if `w in W`, by (1) and the forbidden self-arc.

There are `n_sigma-x_sigma` targets of the first kind and `x_sigma` of the second kind. Hence the complete target capacity available to `W` is exactly

```text
R(x)=sum_sigma [
       (n_sigma-x_sigma) min(P_sigma,m_sigma(x))
       + x_sigma min(P_sigma,m_sigma(x)-1)
     ].                                                (3)
```

The source demand of `W` is

```text
L(x)=sum_tau q_tau x_tau.                              (4)
```

Therefore the ordinary vertex Hall system is exactly equivalent to

```text
L(x)<=R(x)                                             (5)
```

for every integer vector `0<=x_tau<=n_tau`.

### Proof of the type-count formula

The vertex-level capacitated Hall theorem says that a value-`Q` flow exists if and only if every source subset `W` satisfies

```text
sum_{u in W} q_u
 <= sum_{w in B} min(P_w, |N_D^-(w) cap W|).           (6)
```

Fix the type-count vector `x` of `W`. The left side is (4). All numerical compatibility tests against a target depend only on source and target types. The only labelled exception is the deleted self-arc, which subtracts one exactly when the target's own source belongs to `W`. Summing over targets of each type gives (3). Thus every two labelled subsets with the same type counts have the same Hall margin. QED.

## 4. Coordinatewise concavity

Define the Hall margin

```text
F(x)=R(x)-L(x).                                        (7)
```

Fix all coordinates except `x_tau` and vary

```text
x=x_tau in {0,1,...,n_tau}.
```

We show that `F` is a discrete concave function of this one coordinate.

For a target type `sigma!=tau`, its contribution to `R` is either constant in `x` or has the form

```text
(n_sigma-x_sigma) h(a+x)
 + x_sigma h(a+x-1),                                  (8)
```

where

```text
h(y)=min(P_sigma,y).
```

The integer function `h` is concave: its successive increments are `1` until saturation and `0` afterwards. Hence (8), a nonnegative linear combination of shifted copies of `h`, is concave in `x`.

For `sigma=tau`, write

```text
m_tau(x)=a+x,
```

where `a` is independent of `x`. Its own target contribution is

```text
g(x)=(n_tau-x) h(a+x)+x h(a+x-1),                    (9)
```

with `h(y)=min(P_tau,y)`.

When `a+x<=P_tau`,

```text
g(x)=n_tau a+(n_tau-1)x.                              (10)
```

When `a+x>=P_tau+1`,

```text
g(x)=n_tau P_tau.                                     (11)
```

If the transition occurs inside the interval, put `x_0=P_tau-a`. The successive increments of `g` are

```text
n_tau-1, ..., n_tau-1, x_0, 0, ..., 0.                (12)
```

A genuine transition to `x_0+1` inside the domain implies `x_0<=n_tau-1`, so these increments are nonincreasing. Thus `g` is discretely concave.

Every target-type contribution is therefore concave in `x_tau`; subtracting the linear term `q_tau x_tau` preserves concavity. Hence:

> **Coordinatewise concavity lemma.** Holding all other type counts fixed, `F(x)` is discretely concave in each coordinate `x_tau` separately.

## 5. Whole-type reduction

A concave function on a finite integer interval attains a minimum at an endpoint. Starting from any type-count vector `x`, apply the coordinatewise concavity lemma to the first coordinate and replace it by either `0` or `n_tau` without increasing `F`. Repeat for every coordinate. After finitely many steps one obtains a box vertex `x*` with

```text
x*_tau in {0,n_tau}
```

for every type and

```text
F(x*)<=F(x).                                           (13)
```

Consequently:

> **Whole-type orientation Hall theorem.** The target-flow relaxation has a value-`Q` flow if and only if Hall inequality (5) holds for the type-count vectors satisfying
>
> ```text
> x_tau in {0,n_tau}                                  (14)
> ```
>
> for every `(q,c,P)` type `tau`.
>
> Equivalently, if any labelled Hall cut fails, then a union of complete `(q,c,P)` type classes also fails, with at least as large a deficiency.

This is stronger than the initial type-count compression: `prod_tau(n_tau+1)` possible count vectors collapse to at most `2^k` complete-type unions, where `k` is the number of distinct types.

## 6. Closed formula for a union of types

Let `S` be a set of source types and take

```text
x_tau=n_tau  if tau in S,
x_tau=0      otherwise.
```

Then

```text
m_sigma(S)=sum_{tau in S} A_{tau,sigma} n_tau.         (15)
```

The Hall demand is

```text
L(S)=sum_{tau in S} q_tau n_tau,                       (16)
```

and the target capacity is

```text
R(S)=sum_{sigma notin S}
       n_sigma min(P_sigma,m_sigma(S))
     +sum_{sigma in S}
       n_sigma min(P_sigma,m_sigma(S)-1).              (17)
```

Thus every target-flow exclusion has a compact certificate

```text
(type table, selected type set S, L(S), R(S), deficiency).
```

No labelled subset or generic max-flow certificate is needed to verify the cut once the type data are fixed.

## 7. Two-dimensional dominance form

The compatibility test

```text
q_tau<=c_sigma+1,
c_tau>=q_sigma
```

is a two-dimensional dominance rectangle. Therefore `m_sigma(S)` is a weighted two-dimensional orthant count of complete source types.

The earlier red-team result still stands: there is no general single Ferrers ordering of individual sources. The new theorem identifies the correct replacement: **unions of complete two-dimensional types** suffice for the full target Hall relaxation.

This suggests a sharper symbolic programme. Instead of arbitrary source subsets, analyze type sets `S` under the partial order on `(q,c)` and seek further closure properties of a minimum deficient type set—for example, whether one may restrict to particular antichains, ideals, or staircase boundaries. Such reductions require separate proof and are not assumed here.

## 8. Repeated-type special case

For one type `tau` alone, taking the complete class gives the necessary inequality

```text
n_tau q_tau
 <= sum_{sigma!=tau:A_{tau,sigma}=1}
       n_sigma min(P_sigma,n_tau)
    +n_tau min(P_tau,n_tau-1).                        (18)
```

The whole-type theorem shows that partial selection of that class never yields a strictly stronger global minimum than some complete-type union, although the witnessing union may contain additional types.

## 9. Verification and red-team boundary

[`verify_type_compressed_orientation_hall.py`](verify_type_compressed_orientation_hall.py) is intended to check three independent arithmetic facts on deterministic small profiles:

1. the direct labelled-subset Hall margin equals formula (3) for every labelled subset;
2. the minimum over all integer type-count vectors equals the minimum over whole-type box vertices;
3. the discrete first differences in every coordinate are nonincreasing.

The verifier is an audit of the finite identities, not the basis of the hand proof above. Any counterexample blocks use of the whole-type reduction.

## 10. Trust boundary

The concavity and type-compression arguments are elementary finite combinatorics once the target-flow network is accepted. Their Murty-Simon application still depends on the canonical graph-to-constraint bridge and on the validity of the target capacities `P`. Passing every whole-type cut proves only feasibility of this target-flow relaxation, not graph feasibility.

The unrestricted Murty-Simon conjecture is not proved by this result.
