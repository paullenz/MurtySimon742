# Maximum-cut reformulation and reconnaissance

13 September 2026. **Alternative research route. No theorem beyond the stated hand lemmas is claimed.**

## 1. Exact reformulation around a cut

Let `G` be any graph and let `X union Y=V(G)` be a vertex bipartition. Put

```text
I = e(G[X])+e(G[Y])
M = |X||Y|-e_G(X,Y).
```

Thus `I` is the number of internal edges and `M` the number of missing cross-pairs. Since

```text
e(G)=e_G(X,Y)+I,
|X||Y|=e_G(X,Y)+M,
```

we have the exact identity

```text
e(G)=|X||Y|+I-M,                           (1.1)
```

or equivalently

```text
M-I=|X||Y|-e(G).                            (1.2)
```

Therefore Murty-Simon follows immediately if one can prove that a diameter-two edge-critical graph has **some** cut with

```text
I<=M.                                       (1.3)
```

In particular it would suffice to prove (1.3) for a maximum cut. This is equivalent to showing that at least one maximum cut has side product `|X||Y|>=e(G)`.

For a maximum cut, single-vertex flips give the familiar local optimality condition

```text
d_cross(v)>=d_inside(v)                    (1.4)
```

for every vertex `v`. That condition alone is not enough for (1.3) in arbitrary graphs; diameter-two edge-criticality must supply the additional structure.

## 2. A tempting direct injection is false

A natural first attempt is to assign every internal edge of a maximum cut to a distinct missing cross-pair using the unique two-path witness that makes the internal edge critical. This is **not valid in general**.

Our own deterministic reconnaissance encountered an order-eight D2C example whose maximum-cut internal edge has no such direct cross witness. Independently, the public Erdős-Lean #742 research log records a definition-checked order-ten obstruction in which the maximum cut is unique up to complementation and contains an internal edge with no eligible cross-nonedge witness:

https://github.com/edisonymy/erdos-lean-research/blob/main/experiments/erdos742/RESULTS.md

That external result falsifies the naïve matching/injection proof architecture. It does **not** falsify the broader numerical target `I<=M`; a successful maximum-cut proof would need a more global charging, alternating-path, or aggregate argument.

## 3. Exact small-order and deterministic reconnaissance

`maxcut_recon.py` performs evidence-only checks:

1. every unlabeled D2C graph in NetworkX's graph atlas (orders at most seven);
2. a deterministic family of edge-minimal diameter-two graphs generated at orders 8 through 12;
3. sampled positive blow-ups of `C5` through order 30.

The frozen output `MAXCUT_RECON.json` records:

```text
atlas D2C graphs checked                  21
deterministically generated D2C graphs  707
total D2C instances                     728
maximum-cut I<=M violations               0
minimum observed margin M-I               0
sampled positive C5 blow-ups           2226
C5 blow-up violations                     0
minimum C5 blow-up margin                 1
```

Every maximum cut up to complementation is enumerated for the order-at-most-12 graphs. These finite checks are reconnaissance, not proof.

The script also records the Caccetta-Haggkvist degree-square expression only as a **negative control**. That inequality is known false for D2C graphs in general, so its survival in this sample is deliberately not treated as evidence for a universal theorem.

## 4. Hand lemma: positive C5 blow-ups satisfy the cut target

Consider a positive blow-up of the five-cycle: replace its vertices cyclically by nonempty independent sets `A1,...,A5` of sizes `a1,...,a5`, and put all edges between consecutive classes.

A maximum cut can be chosen without splitting any class. Indeed, with the split counts of four classes fixed, the cut size is linear in the split count of the fifth, so an optimum occurs at an endpoint; iterate over the classes.

For an unsplit cut of the weighted five-cycle, exactly one cycle edge can be left internal at optimum, and it can be chosen to have minimum weight `a_i a_(i+1)`. Relabel so the minimum edge is `A5 A1`. Use the alternating maximum cut

```text
X=A1 union A3 union A5,
Y=A2 union A4.
```

Then

```text
I=a1*a5,
M=a1*a4+a5*a2.                            (4.1)
```

Minimality of `a1*a5` among consecutive products gives

```text
a1<=a4,
a5<=a2.
```

Hence

```text
M >= a1^2+a5^2 >= 2 a1 a5 >= I.          (4.2)
```

So every positive independent-set blow-up of `C5` satisfies the maximum-cut target, in fact with the stronger estimate `M>=2I` for this chosen maximum cut.

This is a small infinite-family check of the route, not progress on the general conjecture by itself.

## 5. What a viable maximum-cut proof now needs

The direct one-internal-edge/one-cross-nonedge matching route is dead. The remaining plausible mechanisms are more global:

- charge several internal critical edges against a pool of cross nonedges with bounded multiplicity;
- use alternating exchanges between maximum cuts to expose a deficient set, then invoke criticality to force additional missing cross-pairs;
- combine the local critical-edge witness characterization with (1.4) and a Hall-type inequality on **sets** of internal edges rather than individual edges;
- derive a stability statement: if `M<I`, then the cut is so dense and nearly balanced that criticality forces a forbidden local configuration.

This route is deliberately independent of the current canonical A/B selected-residual framework and is retained as a parallel insurance line.
