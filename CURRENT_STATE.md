# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live graph-theory problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The 2019 Dailly–Foucaud–Hansberg all-order strengthening is false: the published 2024 order-12, size-32 D2C graph remains a mandatory hostile control. Existing Murty–Simon / Erdős #742 work and the standalone-paper programme remain preserved, but they are not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `DENSE_ALL_PRIVATE_BRANCH_EXCLUDED_VIA_EDGE_WITNESS_PRICING_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit stepped back from paper extraction and from further refinement of the old all-private gap inequality. The higher-value move was to price the criticality witness of **every** `B`-edge in the near-rigid private-foot model.

**INSPECTED PREDECESSOR:** latest `main` through the README-sync commits, with the substantive predecessor `1ce9501fab51f4e249c2bc04b67b4ce78cb4c48e` (`Generalize Hall mincut theorem and close exact all-private branch`).

## New result — all-private edge-witness pricing

Use a maximum-degree root `v` with

`B=N(v)`, `A=V(G)\N[v]`, `b=|B|`, `F=G[A]`, `Q=e(G[B])`, `delta=b(n-b)-m=r-e(F)`.

Let `T` be the triangle-active vertices of `B`, `t=|T|`, and assume the **all-private** branch: every `u in T` has a private foot `x_u in A` with `N(x_u) intersect B={u}`. Put

`X={x_u:u in T}`, `C=binom(t,2)`, `s=C-Q`,

and let

`d=C-e(F[X])`

be the number of missing private-foot edges. Let `E` be the number of missing `A-B` incidences whose `A`-endpoint lies outside `X`.

Maximum degree alone gives

`delta-s >= t(b-t)+d`.                                (P1)

The new criticality input is an injective charge for every edge `uw` of `G[B]`. Deleting `uw`, the endpoints remain at distance two through `v`, so criticality supplies (after orientation) an `A`-vertex `z` with

`z~u`, `z not~w`, `N(z) intersect N(w)={u}`.

- if `z=x_u`, charge `uw` to the forced missing foot edge `x_u x_w`;
- otherwise `z` lies outside the private-foot set and charge `uw` to the missing cross incidence `(z,w)`.

Both charge types are injective, hence

`Q <= d+E`.                                            (P2)

Combining (P1), (P2), the exact cross-deficit ledger, and nonnegative maximum-degree slack yields the compact theorem

> **ALL-PRIVATE EDGE-WITNESS PRICING (APW)**
>
> `3 delta >= binom(t,2) + 2s + 2t(b-t)`.

For `b>=7`, the right side (ignoring `2s`) is minimized over `2<=t<=b` at `t=2`, giving

`3 delta >= 4b-7`.                                     (P3)

The complete derivation is preserved in

`project/research/post_ms/2026-09-17-stronger-pivot-v1/ALL_PRIVATE_EDGE_WITNESS_PRICING.md`.

## Dense second-extremal consequence

Assume `n>=14` and

`m>=M(n)+1`.

If a maximum-degree root lies in a triangle (`Q>0`), then average degree forces `b>=floor(n/2)`. The parity forms for

`delta=b(n-b)-m`

give an upper bound strictly below `(4b-7)/3`, contradicting (P3). Therefore the all-private branch is impossible.

> **DENSE ROOT ANTIPODE THEOREM — internal candidate.**
>
> For a D2C graph of order `n>=14` with `m>=M(n)+1`, if a maximum-degree vertex `v` lies in a triangle, then there exist `u,w in N(v)` with
>
> `uw notin E(G)` and `N(u) intersect N(w)={v}`.

Thus every sufficiently-large above-threshold counterexample with a maximum-degree triangle root is forced directly into the **disjoint-support antipode branch**.

## Negative control

The published 2024 order-12, size-32 counterexample remains untouched. The independent `X_3` reconstruction has root parameters

`n=12`, `b=8`, `F=empty`, `delta=0`, `Q=12`.

It is not all-private and already exhibits cube antipodes. The new theorem therefore classifies it on the antipode side rather than falsely excluding it. The theorem is deliberately stated from `n>=14`.

## Verification

`check_all_private_edge_witness_pricing.py` preserves two regressions:

1. graph-atlas D2C classes through order 7: three all-private maximum-degree triangle roots, zero failures of (P1), APW, witness existence, charge injectivity, or `Q<=d+E`;
2. exact integer arithmetic for the dense consequence through `n=5000`, with no failure.

The checks are evidence only; the hand proof is the mathematical basis.

## Preserved earlier core

The 12-vertex literature correction and hypercube-face hostile control remain mandatory. The root-edge antipode/private-foot theorem, earlier APG stability theorem, residual-defect identities, zero-residual Boolean-flow theorem, internal `n<=294` cutoff, selected/Hall machinery, and fixed-order ledgers remain preserved. The closed mixed `{4,5}` selected-excess ladder is not a live target.

The standalone Hall/min-cut and Boolean-flow paper candidates remain preserved under `project/papers/`, but the active optimization target is now the eventual second-extremal D2C problem.

## Trust boundary

APW and the dense-root antipode theorem are internal hand results with finite regression. External mathematical review and novelty assessment remain open. No eventual second-extremal theorem is claimed.

The two genuine live gaps are now clearer:

1. **maximum-triangle-root scope:** a triangle-containing D2C graph might conceivably have every maximum-degree vertex outside all triangles;
2. **antipode branch:** once a disjoint-support antipode exists, the residual/selected structure still has to be converted into a second-extremal defect contradiction while preserving the order-12 hostile control.

**UNPRESERVED WORK:** None after this checkpoint once the current-state commit is published.

**NEXT ACTION:** Critically prioritize the **maximum-triangle-root scope gate** before further antipode optimization. Try to prove that an above-threshold sufficiently-large triangle-containing D2C graph has a maximum-degree vertex in a triangle. Use the existing small-order diagnostic and triangle-edge critical feet, but do not assume the statement if the degree comparison fails. If a counter-configuration emerges, preserve it and immediately switch to the explicit fallback: reroot at a highest-degree triangle vertex and re-derive the root inequalities with slack `epsilon=Delta(G)-d(v)`. Only after that scope issue is controlled should the project spend another full unit sharpening the antipode branch.
<!-- CURRENT-STATUS:END -->
