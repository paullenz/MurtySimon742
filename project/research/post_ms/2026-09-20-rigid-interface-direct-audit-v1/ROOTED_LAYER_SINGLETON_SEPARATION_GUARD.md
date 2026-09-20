# Rooted singleton layer-separation guard

Date: 2026-09-20

Status: **raw graph-level audit invariant**, independent of the rigid-cut interface.

## Lemma

Fix a root v and put `B=N(v)`, `A=V\N[v]`.

If `s,w in B`, then

`v in N(s) cap N(w)`.

Consequently no singleton equation of the form

`N(s) cap N(w)={a}`

with `a!=v` can hold when both source and witness lie in B.

Equivalently:

> **any external singleton witness paired with a B-source and having a non-root singleton head must lie outside B.** `(LAYER-SEP)`

This is elementary, but it is load-bearing in the rooted D2C certificate calculus.

## Immediate audit rules

1. For an A--B edge `ab`, a certificate orientation sourced at the B endpoint cannot use a matched endpoint or U-vertex as external witness, because both lie in B.
2. For a B--B edge, the standard rooted criticality orientations must use an A-witness; this is exactly the form used in the residual-hub and private-spoke theorems.
3. An A-source may legitimately use a B-witness. Thus H--H private-foot equations such as `N(h_l) cap N(q_i)={h_i}` are not affected.
4. Any future proposed singleton equation should be checked first against the rooted layer of its source and witness before code or degree arithmetic is applied.

## Reason for preservation

The immediately preceding H--U frontier violated `(LAYER-SEP)` by treating `q_i` as a possible witness against a U-source. That false branch has now been superseded. Keeping this trivial-looking lemma explicit provides a cheap adversarial lint rule against recurrence and cleanly distinguishes the valid B-edge private-spoke machinery from the invalid U-source/private-foot claim.

`X_3` and the unresolved rigid-interface reachability gate remain untouched by this graph-level invariant.