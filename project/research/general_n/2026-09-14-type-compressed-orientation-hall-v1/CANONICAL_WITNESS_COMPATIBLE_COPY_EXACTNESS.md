# Canonical-witness exactness of compatible-copy staircase bands

14 September 2026. **Candidate exact structural corollary inside the directed target-capacity Hall relaxation. External mathematical review and novelty assessment remain OPEN.**

This note records a strengthening discovered after the compatible-copy band refinement was formalized and independently finite-verified.

The compatible-copy band network is a relaxation for an arbitrary selected source set. However, when the selected source set is the canonical maximal minimum Hall witness `M+`, its **all-bands cut is exactly the original Hall cut `M+`**. Consequently the refined band system detects every exact target-Hall failure once it is built from the canonical witness.

## 1. Exact Hall margin

Let the complete `(q,c,P)` type table have multiplicities `n_sigma`. For a complete-type source set `S`, let

```text
m_sigma(S)
 = number of source copies in S numerically compatible
   with a fixed target copy of type sigma,
   before deleting the target's own source copy.
```

Then the exact Hall margin is

```text
F(S)
 = sum_sigma n_sigma min(
       P_sigma,
       m_sigma(S)-1_{sigma in S}
     )
   - sum_{tau in S} n_tau q_tau.                       (1)
```

The target-flow network is feasible exactly when

```text
min_S F(S) >= 0.                                       (2)
```

Let `M+` be the unique maximal minimum-margin witness from `CANONICAL_ANTICHAIN_CERTIFICATE.md`. It is a sharp-hardness up-set and therefore has canonical staircase bands

```text
B_1,...,B_h.                                           (3)
```

## 2. Compatible-copy band data

For each band `i` and target type `sigma`, the compatible-copy refinement defines

```text
C_{i,sigma}
 = number of source copies in B_i numerically compatible
   with a fixed target copy of type sigma,              (4)
```

and

```text
delta_{i,sigma}=1                                      (5)
```

exactly when type `sigma` itself is selected and lies in band `i`, and zero otherwise.

Let

```text
D_i = total q-demand of source copies in B_i.           (6)
```

The compatible-copy band Hall inequality for a set `J` of bands is

```text
sum_{i in J} D_i
 <= sum_sigma n_sigma min(
      P_sigma,
      sum_{i in J}(C_{i,sigma}-delta_{i,sigma})
    ).                                                  (7)
```

## 3. Whole-staircase identity

Take

```text
J={1,...,h},                                            (8)
```

the set of **all** bands of `S`.

Because the bands partition the selected source copies,

```text
sum_i C_{i,sigma} = m_sigma(S).                         (9)
```

Also a selected type belongs to exactly one band, so

```text
sum_i delta_{i,sigma} = 1_{sigma in S}.                (10)
```

Finally,

```text
sum_i D_i = sum_{tau in S} n_tau q_tau.                (11)
```

Substituting (9)-(11) into (7) shows that the all-band margin is exactly

```text
sum_sigma n_sigma min(
       P_sigma,
       m_sigma(S)-1_{sigma in S}
     )
 - sum_{tau in S} n_tau q_tau
 = F(S).                                                (12)
```

Therefore:

> **Whole-staircase identity.** For every complete-type sharp up-set `S`, the Hall margin of the all-bands cut in its compatible-copy band network is exactly the original target-Hall margin `F(S)`.

No approximation remains in this particular cut.

## 4. Canonical-witness exactness theorem

Let

```text
m=min_S F(S),                                           (13)
```

and let `M+` be the canonical maximal minimizer.

> **Canonical-witness compatible-copy exactness.** The original target-flow network is feasible if and only if the compatible-copy band network constructed from `M+` is feasible.

### Proof: infeasible direction

If the original target flow is infeasible, then by Hall

```text
m=F(M+)<0.                                              (14)
```

By the whole-staircase identity, the all-bands cut of the compatible-copy network built from `M+` has the same negative margin. Hence that band network is infeasible.

### Proof: feasible direction

If the original target flow is feasible, take a value-`Q` exact flow. Restrict it to the source copies belonging to `M+`; this gives a legal exact selected-source flow of value

```text
D(M+)=sum_{tau in M+} n_tau q_tau.                     (15)
```

The compatible-copy aggregation theorem then maps that restricted flow to a legal flow of the same value in the compatible-copy band network. Hence the band network is feasible.

This proves the equivalence. QED.

## 5. Consequence for the frozen 15-state pilot

The earlier pilot contained

```text
205,919 exact target-Hall failures.                     (16)
```

For every such failure the pilot scanner extracts the canonical maximal minimum witness and its staircase bands. The theorem above therefore implies, profile by profile, that the compatible-copy band network must reject **all 205,919 failures**.

Thus the statement

```text
205,919 / 205,919
```

is not merely an empirical extrapolation from the coarse-band result plus state 226. It is a consequence of the exact canonical-witness identity, conditional only on the already audited target-Hall/canonical-witness/compatible-copy chain.

A fresh single-pass pilot replay is still valuable as a software integration audit, but it is no longer mathematically needed to justify the count.

## 6. What this does and does not simplify

This result is stronger than the previous interpretation of the compatible-copy network.

For an arbitrary selected set `S`, compatible-copy aggregation can still lose source-level transport correlations on proper sub-band cuts. But for a **deficient complete-type cut `S` itself**, the all-bands cut retains its Hall margin exactly. In particular the canonical deficient witness `M+` can never be lost by compatible-copy aggregation.

The theorem does **not** give a stand-alone faster algorithm for finding `M+`: the canonical witness is currently extracted from the exact quotient max-flow/min-cut. Its value is structural and certifying:

```text
exact target-Hall failure
 -> canonical sharp up-set M+
 -> monotone generator staircase
 -> compatible-copy bands
 -> one all-bands inequality with exactly the same deficiency.       (17)
```

The remaining general-theory problem is therefore to bound the two sides of this single canonical staircase inequality directly from Murty-Simon data, without first solving the finite max-flow instance.

## 7. Research consequence

The natural symbolic target is now the whole-staircase inequality

```text
sum_{tau in M+} n_tau q_tau
 <= sum_sigma n_sigma min(
      P_sigma,
      sum_i(C_{i,sigma}-delta_{i,sigma})
    ).                                                  (18)
```

with `M+` reconstructed from its monotone generator staircase.

A general proof route would show that the Murty-Simon bridge constraints force (18) for every admissible canonical staircase. Since an exact target-Hall counterexample would require the reverse strict inequality, such a theorem would eliminate the entire orientation-Hall obstruction at once.

## 8. Trust boundary

The statement is exact inside the target-capacity Hall model. Its Murty-Simon use inherits the canonical graph-to-constraint bridge, target-capacity bounds `P`, sharp-hardness theorem, canonical maximal-witness theorem and staircase representation.

It does not by itself prove that target-flow feasibility is graph feasibility and does not prove the unrestricted Murty-Simon conjecture.
