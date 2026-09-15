# Selected-incidence Ferrers theorem v1

15 September 2026. General structural lemma; external review open.

This checkpoint removes one generic max-flow stage from the selected/residual relaxation. The selected-incidence network is a Ferrers bipartite graph because source `u` is eligible for label `i` exactly when

```text
s_i <= rho_u.
```

The exact circulation used in the canonical scanners can therefore be characterized by a finite family of demand-threshold inequalities.

## Theorem

Let `I` be the label set and `U` the source set. Label `i` has required selected-incidence degree `s_i`. Source `u` has exact selected-incidence degree `q_u` and threshold `rho_u`. An edge `u-i` is available iff `s_i<=rho_u`. Assume the row-eligibility bounds already present in the canonical enumeration:

```text
0 <= q_u <= |{ i : s_i <= rho_u }|.
```

Then there exists a `0/1` incidence matrix `x_{ui}` satisfying

```text
x_{ui}=0                    if s_i > rho_u,
sum_i x_{ui}=q_u           for every source u,
sum_u x_{ui}>=s_i          for every label i
```

if and only if, for every distinct demand value `d` occurring among the `s_i`,

```text
sum_{i:s_i>=d} s_i
  <=
  sum_u min(
      q_u,
      |{ i : d <= s_i <= rho_u }|
  ).                                           (F_d)
```

Thus the generic selected-incidence max-flow/circulation test is equivalent to checking the explicit suffix inequalities `(F_d)`.

## Proof

### 1. Reduce exact row sums to a capacitated demand cover

First ask only for a `0/1` eligible incidence matrix with

```text
sum_i x_{ui} <= q_u,
sum_u x_{ui} >= s_i.
```

If such a cover exists, every source row can be extended independently to exact size `q_u`: while row `u` has fewer than `q_u` ones, the bound `q_u<=|N(u)|` guarantees an unused eligible edge in that row. Adding such an edge cannot violate the label upper bound used in the circulation model, because that upper bound is exactly the number of eligible sources for the label and each source-label edge is used at most once.

So exact-row feasibility is equivalent to feasibility of this capacitated lower-demand cover.

### 2. Standard capacitated Hall condition

For any label set `Y subset I`, the sources can contribute at most

```text
sum_u min(q_u, |N(u) intersect Y|)
```

units into `Y`. By max-flow/min-cut (equivalently the capacitated Hall theorem), the cover exists iff every `Y` satisfies

```text
sum_{i in Y} s_i
  <=
  sum_u min(q_u, |N(u) intersect Y|).           (H_Y)
```

### 3. For each cardinality, the worst label set is the largest-demand prefix

Sort the label demands nonincreasingly. Fix `|Y|=k`. If `Y` contains a label `j` while a label `i` outside `Y` has `s_i>=s_j`, replace `j` by `i`.

The left side of `(H_Y)` weakly increases. For every source, eligibility is monotone in the opposite direction: replacing a lower-demand label by a higher-demand label cannot increase `|N(u) intersect Y|`. Hence the right side weakly decreases. Repeating the exchange shows that the hardest set of size `k` is the `k` largest-demand labels.

Therefore it suffices to check all nonincreasing demand prefixes.

### 4. Equal-demand blocks need only their endpoints

It remains to reduce all prefix lengths to the endpoints of equal-demand blocks. Suppose a block has common demand `d`, with `l` of its labels added after the previous prefix. For source `u`, the number of eligible labels in that growing prefix is either constant (`rho_u<d`) or increases as `a_u+l` (`rho_u>=d`). Hence its contribution

```text
min(q_u, a_u+l)
```

is a concave function of `l`. Summing over sources preserves concavity. The demand side increases affinely by `d*l`, so Hall slack (capacity minus demand) is concave through the block.

A concave function that is nonnegative at both block endpoints is nonnegative at every intermediate integer point. Thus only the complete suffixes

```text
{ i : s_i >= d }
```

need be checked. These are exactly `(F_d)`.

Necessity of `(F_d)` is immediate because each is a special case of `(H_Y)`. This proves equivalence.

## Consequences for the project

1. `variable_incidence(...)` is no longer mathematically necessary as a generic max-flow computation. It can be replaced by the explicit Ferrers suffix test.
2. Every failure of the selected-incidence stage has a short integer certificate: a demand threshold `d` with left side strictly larger than right side.
3. The theorem is all-order within the canonical selected/residual relaxation; it is not limited to N34/N35 or to the forced-core family.
4. This does **not** by itself strengthen the canonical frontier. It is a structural normalization of an already-used necessary condition.

The preceding [`threshold-hall-normal-form-v1`](../2026-09-15-threshold-hall-normal-form-v1/README.md) replay already gave exact stage-by-stage agreement between this suffix test and the old incidence max-flow on 23 audited N34 closure states. The theorem explains that agreement rather than merely observing it.

## Red-team regression

`audit_incidence_ferrers.cpp` independently compares three decisions:

- the lower-demand cover max-flow;
- the original exact-row lower-bound circulation semantics;
- the explicit threshold inequalities above.

It exhaustively enumerates sorted small instances with `1<=|I|,|U|<=4`, demand/threshold values from `0` through `|U|`, and every row degree `0<=q_u<=|N(u)|`.

Recorded result:

```text
cases=1206288 mismatches=0 max_a=4 max_b=4
```

This regression is corroboration, not the proof; the proof is the exchange/concavity argument above.

## Next structural target

The pair-slot and target-capacity networks are not plain Ferrers graphs because pair identities and the forbidden self-arc perturb nesting. The 23-state threshold replay nevertheless shows that monotone source sets

```text
X(R,k)={i:rho_i>=R,q_i>=k}
```

capture every generic pair/target Hall failure encountered there. The next target is to identify sufficient conditions under which arbitrary deficient source sets in those networks can be compressed to such threshold sets.

## Status discipline

This lemma changes the representation of one necessary condition, not the canonical ledger. **Canonical status remains 4,626 exclusions / 952 survivors / 3,632 whole-state closures.** External mathematical review of the bridge and of this Ferrers reduction remains open.
