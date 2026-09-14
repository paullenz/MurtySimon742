# Staircase-band Hall relaxation

14 September 2026. **Candidate necessary-condition theorem inside the directed target-capacity Hall relaxation. External mathematical review and novelty assessment remain OPEN.**

This note uses the exact staircase representation from [`STAIRCASE_THRESHOLD_HALL.md`](STAIRCASE_THRESHOLD_HALL.md) to compress a sharp-hardness up-set into ordered source bands. The result is a capacitated bipartite flow in which every target type sees a consecutive interval of bands.

## 1. Generator staircase and bands

Let `S` be a sharp-hardness up-set with minimal generators

```text
g_i=(q_i,c_i,P_i),
```

ordered so that

```text
c_1<c_2<...<c_h,
q_1<=q_2<=...<=q_h.                                    (1)
```

For each selected source type `tau=(q_tau,c_tau,P_tau)`, let

```text
i(tau)=min{i:c_tau<=c_i}.                              (2)
```

The staircase-threshold theorem says that `tau` is selected because it dominates `g_{i(tau)}`. Define band

```text
B_i={selected source copies with i(tau)=i}.             (3)
```

Let

```text
M_i = number of source copies in B_i,
D_i = sum of q_tau over source copies in B_i.           (4)
```

Every source type in `B_i` satisfies

```text
q_tau>=q_i,
c_tau<=c_i.                                             (5)
```

Hence its source interval obeys

```text
[q_tau,c_tau] subseteq [q_i,c_i].                       (6)
```

In particular,

```text
D_i>=q_i M_i.                                           (7)
```

## 2. Generator-compatible target interval

For target type

```text
sigma=(q_sigma,c_sigma,P_sigma),
```

the generator `g_i` is numerically compatible with `sigma` exactly when

```text
q_i<=c_sigma+1,
q_sigma<=c_i.                                           (8)
```

Define

```text
I_sigma={i: q_i<=c_sigma+1 and q_sigma<=c_i}.           (9)
```

Because `q_i` is nondecreasing and `c_i` is strictly increasing, the first inequality in (9) defines a prefix of the band order and the second a suffix. Therefore:

> **Consecutive-band lemma.** `I_sigma` is empty or a contiguous interval of band indices.

This is the first genuine one-dimensional consecutive-ones structure recovered after the earlier individual-source Ferrers shortcut failed. It appears only **after** passing to the verified generator staircase.

## 3. Neighborhood containment

Suppose a selected source type `tau in B_i` is numerically compatible with target type `sigma`. Then

```text
q_i<=q_tau<=c_sigma+1,
q_sigma<=c_tau<=c_i,
```

so `i in I_sigma`.

Thus:

> **Band-neighborhood containment.** Every actual target available to a selected source in band `B_i` is also generator-compatible with band `i`.

The generator neighborhood is generally larger; this step is a relaxation, not an equivalence.

## 4. Band upper capacity for a Hall cut

Take any set `J` of source bands. Let `S_J` be all selected source copies in those bands. Its exact demand is

```text
D(J)=sum_{i in J} D_i.                                  (10)
```

For target type `sigma`, define

```text
U_sigma(J)=sum_{i in J cap I_sigma} M_i - delta_sigma(J),   (11)
```

where

```text
delta_sigma(J)=1
```

exactly when `sigma` itself is a selected source type lying in a band of `J`, and is zero otherwise. The subtraction is the deleted self-arc for each target copy of type `sigma`.

By band-neighborhood containment, the actual number of sources in `S_J` available to each target copy of type `sigma` is at most `U_sigma(J)`. Therefore its total usable capacity is at most

```text
n_sigma min(P_sigma,U_sigma(J)).                        (12)
```

Hence every target-flow-feasible profile satisfies, for every band set `J`,

```text
sum_{i in J} D_i
 <= sum_sigma n_sigma min(P_sigma,U_sigma(J)).          (13)
```

Using (7) gives the weaker but simpler necessary inequality

```text
sum_{i in J} q_i M_i
 <= sum_sigma n_sigma min(P_sigma,U_sigma(J)).          (14)
```

## 5. Equivalent band-flow relaxation

Equation (13) is the Hall system of a smaller flow network.

Create source-band nodes `B_i` and target-type nodes `sigma`. Use capacities

```text
source -> B_i: D_i,                                     (15)

B_i -> sigma:
  n_sigma M_i                  if i in I_sigma
                                and sigma is not in B_i,
  n_sigma (M_i-1)              if sigma is a selected
                                source type in B_i,
  0                            if i notin I_sigma,       (16)

sigma -> sink: n_sigma P_sigma.                         (17)
```

Aggregating any legal exact target flow by source band and target type gives a legal flow in (15)-(17). Thus:

> **Staircase-band flow theorem.** Exact target-flow feasibility implies feasibility of the band network for total demand `sum_i D_i`.

Failure of the band network therefore excludes the profile. Passing it is only a relaxation and does not imply exact target-flow feasibility.

## 6. Why this compression matters

The exact type-level quotient can have one source node per distinct `(q,c,P)` type. The band relaxation has only

```text
h = number of canonical staircase generators            (18)
```

source-side nodes, and each target-type neighborhood among those nodes is a consecutive interval `I_sigma`.

In the current Murty-Simon source universe, `c<=a`, so

```text
h<=a+1.                                                 (19)
```

The resulting problem is therefore a capacitated interval-neighborhood flow over at most one source band per cross-degree level.

This is weaker than exact target Hall, but it is much closer to a symbolic all-order object. The natural next questions are whether Murty-specific demand/excess constraints make only a small collection of band intervals `J` extremal, or allow (13) to be bounded directly by aggregate staircase data.

## 7. Relation to the failed Ferrers shortcut

No contradiction is present. The earlier false simplification tried to linearly order **individual source vertices** so that every exact Hall cut was a prefix. Here:

- the exact target-Hall cut is first replaced by its proven sharp-hardness staircase;
- individual sources are then relaxed to generator bands;
- target neighborhoods become intervals of band indices, not necessarily prefixes;
- the band flow is necessary but not exact.

The loss of information is explicit and one-way.

## 8. Verification

[`verify_staircase_band_hall.py`](verify_staircase_band_hall.py) checks exhaustive small profiles and a deterministic broad challenge. For every sharp up-set it verifies:

1. every selected source interval is contained in its band-generator interval;
2. every target's generator-compatible bands form a contiguous interval;
3. actual compatible source counts are bounded by `U_sigma(J)` for every tested band set `J`;
4. exact band demand satisfies (7);
5. whenever exact target Hall is feasible for `S_J`, inequality (13) holds, and the direct exact Hall capacity never exceeds the band upper capacity.

## 9. Trust boundary

This theorem is a relaxation of the already-audited target-Hall system. It inherits all assumptions of that system and deliberately throws away within-band compatibility information. It is useful only as a necessary condition.

The unrestricted Murty-Simon conjecture is not proved by this result.
