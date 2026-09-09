# n=29 t=3 Hall-core certificate mining

9 September 2026. Derived from the exact artifact of clean workflow run `34329608225` (`rx-hall-t3-hall-core`, artifact id `10095198703`, artifact SHA-256 `ad76420ef1035889cb5b8b5584b515f05d6ec253ecf685c060024f62af133d7c`).

**Status: descriptive mining of already exact certificates. Not a new theorem.**

## Exact source

The artifact contains 94 exact integer Farkas certificates for the hard n=29, Delta=16, m=211, t=3 Hall-core rows. The accompanying independent standard-library checker passes all 94 records.

For each certificate, the inequality rows can be classified without interpreting floating-point output:

1. the first 12 inequality slots are the nested source/supplement transport thresholds `k=1,...,12`;
2. the subsequent pre-bound rows are one/two-rectangle Hall cuts;
3. the final `variables` rows are elementary unit-density bounds `x<=1`.

The boundary is exact because the generator appends one unit bound for every model variable after all structural inequalities.

## Pattern counts

Across all 94 exact contradictions:

```text
category                         certificates using it
transport thresholds                         94/94
one/two-rectangle Hall cuts                   94/94
unit-density bounds                           94/94
```

Nonzero structural rows per certificate:

```text
                         min    median    max
transport thresholds       1       2       5
Hall domains                2       4       8
unit-density rows           1       6      14
```

The Hall-domain count distribution is:

```text
2 domains:  6 certificates
3 domains: 37
4 domains: 29
5 domains: 17
6 domains:  2
7 domains:  2
8 domains:  1
```

Thus 72/94 certificates use at most four Hall domains, and 89/94 use at most five.

## Transport-threshold usage

The number of certificates with a nonzero multiplier on each nested transport threshold is:

```text
k=1:  0
k=2: 87
k=3: 52
k=4: 44
k=5: 24
k=6: 13
k=7:  8
k>=8: 0
```

The absence of `k=1` is unsurprising because global source/supplement balance already captures the lowest layer. The dominant repeated signal is the `k=2` transport cut, with a short decreasing tail through `k=7`.

## Equality usage

The exact certificates use between 4 and 7 equality rows:

```text
4 equalities:  3 certificates
5 equalities: 24
6 equalities: 40
7 equalities: 27
```

These come from source-type normalization, global q/p balance, label-load normalization and total selected-incidence balance.

## Interpretation

The exact contradictions do **not** look as though they require a large arbitrary Hall staircase. Most use only a handful of Hall domains together with two or three low transport thresholds. This strengthens the research case for trying to derive a small weighted threshold inequality rather than reproducing the full LP symbolically.

A particularly natural first target is a weighted combination of

```text
HC4_2, HC4_3, ...
```

with a small chain of rectangle Hall inequalities `HC6/HC7`, followed by layer-cake elimination of the label extra-load variables `y_i`.

The unit-density rows occur in every current certificate, so they should not simply be discarded. At graph level they correspond to elementary finite-capacity/simplicity constraints rather than a deep structural ingredient; a symbolic proof should account for their contribution explicitly.

## Next falsification / mining step

Run the same two-rectangle Hall core on the regenerated n=30 t=2 and t=1 frontiers. If it survives, compare the exact threshold/Hall support patterns across n=29 and n=30 and retain only support families which recur across orders. If it fails, inspect the preserved survivor profiles before strengthening the model.
