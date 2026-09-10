# Exact bounded claim — Erdős Problem 742

## Definitions

Let `G` be a finite simple graph. Write `n=|V(G)|` and `e(G)=|E(G)|`.

`G` is **diameter-2-critical** if `diam(G)=2` and deletion of any edge destroys that property, i.e. for every edge `e`, the graph `G-e` has diameter greater than 2 (including the disconnected case under the usual convention).

## Claim

For each

```text
n in S := {25, 27, 28, 29, 30},
```

if `G` is a diameter-2-critical graph on `n` vertices, then

```text
e(G) <= floor(n^2/4).
```

Moreover, equality holds if and only if

```text
G ≅ K(floor(n/2), ceil(n/2)).
```

Thus explicitly:

```text
n=25: e(G) <= 156, equality iff G ≅ K(12,13)
n=27: e(G) <= 182, equality iff G ≅ K(13,14)
n=28: e(G) <= 196, equality iff G ≅ K(14,14)
n=29: e(G) <= 210, equality iff G ≅ K(14,15)
n=30: e(G) <= 225, equality iff G ≅ K(15,15)
```

## Scope exclusions

This submission does **not** assert:

- the unrestricted Murty–Simon conjecture for all `n`;
- the conjunction of the conjecture for every `n<=30`;
- any new result at `n=26`;
- external validation, peer review, journal acceptance or Lean formal verification;
- that any exploratory RX-Hall / staircase calculation is required by these five fixed-order claims.

## Status

This is a **candidate bounded theorem package** supported by hand reductions, exact finite certificates, replay code and internal hostile audits in the linked repository. Independent specialist review remains open.

## Preferred logical dependency surface

The current fixed-order editions are the Fan-free reviewer-v2 packages. G. Fan's 1987 upper-density theorem is historical context, not a logical dependency of the submitted fixed-order proofs.

The most important common mathematical trust boundary is the graph-to-residual / graph-to-demand construction. Machine replays can verify the finite arithmetic conditional on that bridge; they do not substitute for an external proof audit of the bridge itself.
