# Compatible-copy staircase-band Hall refinement

14 September 2026. **Candidate necessary-condition theorem inside the directed target-capacity Hall relaxation. External mathematical review and novelty assessment remain OPEN.**

This note strengthens [`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md) by restoring exactly one piece of information deliberately discarded by the coarse band relaxation: whether each selected source copy in a band is individually compatible with a target type.

The refinement was suggested by the unique false negative in the frozen 15-state band-reach pilot, state `226`. The theorem below is general and does not depend on that state.

## 1. Setup

Let `S` be a sharp-hardness up-set, written as a union of complete `(q,c,P)` type classes, with canonical staircase bands

```text
B_1,...,B_h.
```

For each source band `B_i`, let

```text
D_i = total selected source demand in B_i.
```

For every target type

```text
sigma=(q_sigma,c_sigma,P_sigma)
```

let `n_sigma` be its multiplicity in the full profile.

The directed numerical compatibility relation is

```text
A(tau,sigma)=1
```

exactly when

```text
q_tau <= c_sigma+1,
q_sigma <= c_tau.
```

As in the exact target network, the diagonal source-target pair is deleted when source and target are the same labelled vertex.

## 2. Compatible-copy counts

For each source band `i` and target type `sigma`, define

```text
C_{i,sigma}
  = sum over selected source types tau in B_i
      n_tau A(tau,sigma).                               (1)
```

Thus `C_{i,sigma}` is the actual number of selected source copies in band `i` whose numerical type is compatible with a fixed target copy of type `sigma`, before deleting the target's own source copy.

Define

```text
delta_{i,sigma}=1                                      (2)
```

exactly when type `sigma` itself is selected and belongs to band `i`, and `0` otherwise.

Because a sharp-hardness witness contains either all or none of a type class, every target copy of a selected type `sigma` has its own source copy present in the same band. Hence every fixed target copy of type `sigma` has exactly

```text
C_{i,sigma}-delta_{i,sigma}                             (3)
```

available labelled source copies from band `i`.

Consequently the total number of exact unit-capacity source-target arcs from band `i` to all targets of type `sigma` is exactly

```text
K_{i,sigma}
  = n_sigma (C_{i,sigma}-delta_{i,sigma}).              (4)
```

## 3. Refined band network

Construct a capacitated network with source-band nodes `B_i` and target-type nodes `sigma`:

```text
source -> B_i:          D_i,
B_i -> sigma:           K_{i,sigma},
sigma -> sink:          n_sigma P_sigma.                (5)
```

The total requested flow is

```text
D = sum_i D_i.                                          (6)
```

> **Compatible-copy band theorem.** If the exact selected-source target network admits a flow of value `D`, then the compatible-copy band network (5) also admits a flow of value `D`.
>
> Therefore infeasibility of the compatible-copy band network is a valid necessary-condition certificate against exact target-flow feasibility.

### Proof

Take any legal exact selected-source flow of value `D`.

Aggregate every selected source copy into its canonical band and aggregate all target copies with the same `(q,c,P)` type. For each ordered pair `(i,sigma)`, let `f_{i,sigma}` be the total exact flow carried by arcs from source copies in band `i` to target copies of type `sigma`.

There are exactly `K_{i,sigma}` such labelled unit-capacity arcs by (4), so

```text
f_{i,sigma} <= K_{i,sigma}.                             (7)
```

Flow conservation at the exact source copies gives total outgoing flow `D_i` from band `i`. Flow entering all targets of type `sigma` is at most their total target capacity `n_sigma P_sigma`.

Thus the aggregated values `f_{i,sigma}` form a legal flow of value `D` in (5). QED.

## 4. It is stronger than the coarse staircase-band relaxation

Let `M_i` be the number of selected source copies in band `i` and let the canonical band generator be `g_i`.

The neighborhood-containment lemma from [`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md) says that if any selected source copy in `B_i` is compatible with target type `sigma`, then `g_i` is compatible with `sigma`.

Therefore

```text
0 <= C_{i,sigma} <= M_i,                               (8)
```

and if the coarse generator-compatible edge does not exist then

```text
C_{i,sigma}=0.                                          (9)
```

After the same self-deletion correction, every compatible-copy edge capacity is at most its coarse-band counterpart. Hence:

> **Monotonicity corollary.** Every profile rejected by the verified coarse staircase-band network is also rejected by the compatible-copy refinement.

The refinement can reject additional profiles but cannot resurrect a coarse-band failure.

## 5. Hall form

For any set `J` of source bands, define

```text
D(J)=sum_{i in J} D_i.                                  (10)
```

A necessary Hall inequality for the refined network is

```text
D(J)
 <= sum_sigma n_sigma min(
        P_sigma,
        sum_{i in J}(C_{i,sigma}-delta_{i,sigma})
      ).                                                (11)
```

Equivalently, failure of any inequality (11) certifies failure of the refined band flow.

Unlike the coarse relaxation, the incoming term in (11) contains no invented within-band source-target incidences: every counted incidence corresponds to a genuine exact compatibility.

## 6. What information is still lost

The compatible-copy refinement is still a relaxation in general.

Equation (4) preserves the exact **number** of compatible source-target arcs between each band and target type, but the source band node pools all demand from different source types. It therefore forgets which source type inside the band owns which compatible arcs across different target types.

So the remaining possible gap from exact target Hall is a transport-correlation loss, not a compatibility-count loss.

This distinction is useful for general theory: after this refinement, any surviving discrepancy must arise from the inability to realize several band-to-target allocations simultaneously at the individual source level.

## 7. State 226 diagnostic

The frozen state-226 exception to the coarse relaxation has selected source bands

```text
band 0: type (q,c,rho,P,n)=(4,6,2,2,1),
band 1: types
        (5,9,4,4,1),
        (6,9,3,3,5).
```

For target type

```text
(q,c,P,n)=(2,4,4,1),
```

the coarse band-1 model counts all six source copies because the band generator `(5,9,4,4)` is compatible. In reality only the single generator copy is compatible; the five `(6,9,3,3)` copies fail `6<=4+1`.

The compatible-copy refinement therefore removes exactly five spurious incidences. The frozen diagnostic gives effective receiving capacities

```text
target 1:  2
target 2: 15
target 3:  2
target 4:  4
target 5: 15
             --
total       38
```

against selected band demand `39`, so the refined network rejects the unique coarse-band exception.

Combined with monotonicity, this yields the already recorded **derived frozen-pilot conclusion** that all `205,919/205,919` exact target-Hall failures in the deterministic 15-state pilot are detected by the refinement.

That empirical conclusion is not promoted here to an all-order equivalence theorem.

## 8. Independent verification boundary

[`verify_compatible_copy_band_hall.py`](verify_compatible_copy_band_hall.py) is intentionally separate from the earlier staircase-band verifier. It independently checks on exhaustive small profiles, deterministic random profiles and the frozen state-226 fixture that:

1. the capacity formula (4) equals the explicit number of compatible labelled source-target arcs;
2. every refined edge capacity is at most the corresponding coarse-band capacity;
3. maximum exact selected-source flow never exceeds maximum refined-band flow;
4. exact selected-source feasibility always implies refined-band feasibility;
5. the state-226 refined network has flow `38` against demand `39`.

Passing that verifier is an internal finite audit of this theorem, not external mathematical acceptance.

## 9. Trust boundary

This theorem is conditional on the already stated target-flow model, canonical sharp-hardness witness and staircase-band construction. It does not establish that the compatible-copy band network is equivalent to exact target Hall on all Murty-Simon profiles, and it does not prove the unrestricted Murty-Simon conjecture.
