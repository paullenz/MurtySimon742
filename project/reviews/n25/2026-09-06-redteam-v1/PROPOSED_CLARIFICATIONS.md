# Clarifications proposed after the red-team audit

These are proposed additions for a future reviewer edition. The frozen edition 1 has not been changed.

## State the hypotheses before the residual lemmas

Let H be a simple 3-total-domination-edge-critical graph. Choose a vertex v of minimum degree a, and put A=N_H(v), B=V(H) minus N_H[v]. For each unordered missing pair in B choose exactly one eligible cross quasi-edge; the other A–B edges are residual. Define C, F, r, rho, R, q, L and t as in Section 4.

The inequalities d_B(i)≥d_F(i) and Q≥r+2t use the minimum-degree choice of v. The source/column bounds use one chosen cross quasi-edge per unordered missing B-pair, giving distinct supplements at a fixed source. The implication that every B-vertex is residual-active requires **t>0**, strictly. The low-k extra-edge count requires that all B-vertices are residual-active.

The witness-count lemma in Section 3 assumes that G has no dominating edge. The complete bipartite case must therefore be settled before this lemma is applied.

## A direct alternative for maximum degree at least 17

This observation provides another derivation of the high-degree exclusion, conditional on the candidate's general residual ledger and all-active lemma. It is not required for the existing proof, which cites a published theorem.

Suppose G is a non-bipartite, non-star diameter-2-critical graph of order 25 with at least 156 edges. Let H be its complement, let a=delta(H), and put b=24-a. If Delta(G)≥17, then 1≤a≤7. We have e(H)≤144 and

\[
0\le e(C)+r=L\le144-a-\binom{24-a}{2}.
\]

For a=1,2,3,4,5,6 the right side is respectively -110,-89,-69,-50,-32,-15, a contradiction. For a=7 it is 1, so L≤1 and

\[
t=\binom72-L\ge20>0.
\]

The general all-active lemma then gives r≥b=17, while the ledger gives r≤L≤1, again a contradiction. Thus the dense non-bipartite cases with Delta(G)≥17 can also be excluded using these structural lemmas. The star case a=0 was already handled separately.

## Guard the primary matching helper before broader reuse

In `general_primary.py`, `matches()` uses `zip()`. If there are fewer suppliers than labels, it currently ignores the extra labels. Add a length check before the comparison:

```python
def matches(easiest_labels, strongest_suppliers):
    return (len(easiest_labels) <= len(strongest_suppliers)
            and all(d <= c for d, c in
                    zip(reversed(easiest_labels), strongest_suppliers)))
```

The frozen n=25 scans use a=9 or 10, b=15 or 14, and positive residual degrees; their q never exceeds 9 while at least 13 suppliers are available. The proposed guard therefore does not change any audited result. The a=8 case is settled structurally and is also safe with respect to this bound. No frozen source file has been patched.
