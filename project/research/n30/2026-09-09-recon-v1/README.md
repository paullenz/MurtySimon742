# n=30 reconnaissance from the stripped n=29 machinery

9 September 2026. Research directed by Paul Lenz; derivation and internal checking by ChatGPT/Geeps.

**Status: reconnaissance only. No n=30 theorem or candidate theorem is claimed here.** The purpose is to determine whether the n=29 bridge/trusted-kernel framework parameterises cleanly, and to identify the smallest genuinely unresolved n=30 scopes before any bespoke computation is written.

## 1. Dense edge counts

The Fan strict upper expression used in the n=29 candidate is

```text
n^2/4 + [n^2-(81/5)n+56]/320.
```

At `n=30` this is exactly

```text
7247/32 = 226.46875.
```

Therefore an upper-bound counterexample to `e(G)<=225` can only have

```text
m=226.
```

Equality at `m=225` must be treated separately.

## 2. Degree-sum entry points

At `m=226`,

```text
2m=452,
```

so `Delta>=16`.

At `m=225`,

```text
2m=450,
```

so `Delta>=15`.

A universal vertex (`Delta=29`) forces a star and is sparse.

## 3. Scalar h-index elimination

Use the same general necessary inequality

```text
b+2t <= floor((n-b)^2/4),
```

where

```text
b=Delta,
a=n-1-b,
t=m-b(n-b).
```

For `m=226`:

| Delta | a | t | left `b+2t` | right | excluded? |
|---:|---:|---:|---:|---:|---|
| 16 | 13 | 2 | 20 | 49 | no |
| 17 | 12 | 5 | 27 | 42 | no |
| 18 | 11 | 10 | 38 | 36 | yes |

All larger `Delta` are still more strongly excluded. Thus the only h-index survivors at 226 edges are

```text
Delta=16,17.
```

For `m=225`:

| Delta | a | t | left `b+2t` | right | excluded? |
|---:|---:|---:|---:|---|
| 16 | 13 | 1 | 18 | 49 | no |
| 17 | 12 | 4 | 25 | 42 | no |
| 18 | 11 | 9 | 36 | 36 | not by h-index alone |
| 19 | 10 | 16 | 51 | 30 | yes |

Thus h-index leaves `Delta=15,16,17,18` at equality before the next hand reductions.

## 4. Delta=18 at m=225 is eliminated by charging

For `Delta=18`, `a=11`, `b=18`, `t=9`. The charging inequality requires

```text
sum_i s_i(12-2s_i)/(11-s_i) >= 18+18 = 36.
```

For integer `0<=s<=10`, the pointwise maximum is

```text
16/7,
```

attained at `s=4`. Hence eleven labels contribute at most

```text
176/7 < 36.
```

So `Delta=18` is impossible at `m=225`.

## 5. Delta=15 at m=225 gives the equality graph

If `Delta=15` and `m=225`, degree sum forces every vertex to have degree exactly 15.

At the dense non-bipartite scopes the published dominating-edge reduction excludes a dominating edge.

Every critical edge nevertheless has a direct or two-step witness.

For a two-step witness `uv` on 30 vertices, the two neighbourhoods have exactly one common vertex and their union lies among the other 28 vertices, so

```text
d(u)+d(v)<=29.
```

For a direct witness, the neighbourhoods are disjoint; if their total size were 30 their union would be all vertices and the witness edge would be dominating. Hence again

```text
d(u)+d(v)<=29.
```

But in a 15-regular graph every pair has degree sum 30. Thus no witness can exist, contradicting edge-criticality.

Therefore a 225-edge graph with `Delta=15` cannot be non-bipartite. A bipartite diameter-two graph is complete bipartite, and equality on 30 vertices forces

```text
K(15,15).
```

So the equality `Delta=15` scope is hand-resolved.

## 6. Remaining n=30 scopes after hand reductions

The first reconnaissance therefore reduces n=30 to exactly four dense non-bipartite scopes:

```text
m=226: Delta=16,17
m=225: Delta=16,17
```

Equivalently:

| m | Delta | a | b | t |
|---:|---:|---:|---:|---:|
| 226 | 16 | 13 | 16 | 2 |
| 226 | 17 | 12 | 17 | 5 |
| 225 | 16 | 13 | 16 | 1 |
| 225 | 17 | 12 | 17 | 4 |

This is a much narrower target than a fresh all-degree search.

## 7. Parameterisation significance

Two features are especially useful.

First, the `Delta=17` cases have

```text
a=12,
```

exactly the same label-side size as the difficult n=29 `Delta=16` case. The source side changes from `b=16` to `b=17`, and the surplus values increase to `t=5,4`. This is therefore the cleanest first test of whether the n=29 minimal trusted kernel is genuinely parameterised rather than order-specific.

Second, the `Delta=16` cases have `a=13,b=16,t=2,1`; these require a one-step increase in the label-side dimension but keep the old source-side size.

A sensible attack order is therefore:

```text
1. n30, Delta=17, m=226 (a=12,b=17,t=5)
2. n30, Delta=17, m=225 (a=12,b=17,t=4)
3. n30, Delta=16, m=226 (a=13,b=16,t=2)
4. n30, Delta=16, m=225 (a=13,b=16,t=1)
```

The first two maximise reuse of the audited n=29 bridge while testing whether the source-side formulas were genuinely general.

## 8. Standing rule for the n=30 attack

Do not copy the old n=29 pipeline and patch constants until it runs.

Instead:

1. derive every bridge inequality symbolically in `(a,b,t)`;
2. identify which steps require `t>0`, `delta(C)>=1`, or parity/order-specific facts;
3. regenerate the demand domain from the symbolic inequalities;
4. only then instantiate the four scopes above;
5. treat any scope that needs a new special-case lemma as a signal to reassess the general structure before adding machinery.

The accompanying `check_scope.py` reproduces the exact arithmetic reductions in this note using rational/integer arithmetic.
