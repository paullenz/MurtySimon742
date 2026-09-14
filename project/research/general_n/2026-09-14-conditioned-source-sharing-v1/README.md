# Conditioned source sharing: exact row-108 closure

14 September 2026. Successor to the [source-priced selected-incidence bound](../2026-09-14-source-sharing-v1/README.md), the [conditioned source-price scan](../2026-09-14-conditioned-source-pricing-v1/README.md), and the [shared block-slack package](../2026-09-14-joint-blocks-v1/README.md). **This package excludes original synthetic profile row 108 inside the stated selected-incidence relaxation. It does not close a canonical whole state, prove graph non-realizability beyond that bridge, or prove the unrestricted conjecture. External mathematical review remains OPEN.**

## 1. What changed

The first source-price experiment deliberately used one coarse unconditioned excess domain and found no profile closure. The later conditioned-source-price scan retained the SAME exact demand-block excess totals and branch-specific legitimate caps across all six original and seven fresh boundary profiles; it improved several bounds but still closed no profile. Here row108 is tightened one step further by restoring exact row/type incidence feasibility and, where needed, ONE common pressure per source.

For row 108 the selected demands have three blocks:

```text
s=1: 2 labels
s=2: 3 labels
s=3: 19 labels
Esel=45
```

The shared-slack replay leaves cumulative low-block excess ranges

```text
e_{s<=1} in {26,...,33}
e_{s<=2} in {33,...,37}.
```

Keeping only monotone cumulative totals gives 40 exact block-total tuples. Replaying the already preserved simultaneous-multiblock screen rejects 8 and leaves 32. The new argument resolves all 32.

## 2. One fixed source price closes 24 of the 32 tuples

For a fixed exact block-total vector, let `D_u` be the legitimate branch-specific pressure ceiling and use unit source weights with charge threshold zero. The source-price identity from the predecessor package is now maximized only over excess allocations having those exact block totals.

A single signed price vector is enough for 24 tuples:

```text
lambda = (0,-4,0,0,0,0,0,0,0,0,0,0,-4,0,0,0,0,0,0,0,0,-4,0,0,0,0,0,0).
```

Indices are zero-based in the executable vector; equivalently the second, thirteenth and twenty-second sources receive price `-4`. All three have `q_u=5` in row 108. For every selected incidence the verifier subtracts the source price inside the column score and restores exactly `sum lambda_u q_u`, so signed prices are sound because the source row sums are equalities.

For 24 exact block-total tuples the resulting conditioned source-price upper is strictly below the corresponding exact receiver lower. No price optimization claim is made: this one vector is simply a reusable certificate.

The eight tuples not closed by that vector are

```text
(26,33), (26,35), (26,36), (26,37),
(27,33), (27,36), (27,37), (28,37),
```

where each pair is `(e_{s<=1}, e_{s<=2})`.

## 3. Common pressure is the missing correlation for the final eight

For a fixed excess histogram, source `u` has one pressure

```text
d_u = (p_u-rho_u+1)_+,
```

not a different pressure at each selected label. Every selected positive-demand label with excess `e_i` therefore requires `d_u<=e_i`. Since row 108 has no zero-demand labels, its unit-weight charge is exactly

```text
C_0 = sum_u q_u d_u.
```

The receiver calculation for all eight tuples requires `C_0>=211`.

The verifier enumerates excess histograms only up to permutations of labels having the same demand. Across the eight tuples there are **46,662** such histograms. Exact bipartite row/type flow leaves only **1,201** histograms compatible with the required source row sums and label column totals.

For **1,124** of those, an exact min-cost/max-charge flow already gives a per-incidence charge upper below 211 even while allowing inconsistent source pressures from one label to another. The remaining **77** are checked with the common pressure restored. A finite branch-and-bound enumerates possible integer `d_u`; at each partial branch, an exact bipartite flow tests whether the row/type incidences can still be realized under the imposed pressure thresholds. Monotonic infeasibility and a source-local `q_u`-th-largest eligible-excess cap are the only branch prunes. The complete proof visits **57,867** branch nodes. None reaches charge 211.

Thus every one of the final eight block-total tuples is impossible in this selected-incidence relaxation, and row 108 is excluded.

## 4. Consequence and strict scope

The original fixed-seed synthetic sample therefore moves from

```text
707 / 713 rejected; 6 not rejected
```

to

```text
708 / 713 rejected; 5 not rejected:
160, 338, 347, 471, 586.
```

This is **one additional synthetic-profile exclusion only**. It is not a new canonical whole-state closure, does not change the promoted `1,971 / 3,607 / 977` frontier, does not promote any of the 2,655 recovered relational candidates, and says nothing new about the seven fresh-seed profiles. Surviving relaxed profiles are not graph constructions.

The older 454/597 simultaneous-multiblock non-rejection remains preserved as the predecessor negative experiment. This package does not rewrite it as a success+ rather, it adds the common-source correlation that experiment explicitly lacked.

## 5. Exact replay

[`verify_row108.py`](verify_row108.py) uses only the Python standard library. It verifies the canonical original input hash, the frozen shared-slack result hash, reconstructs the old row-108 multiblock screen, checks the 24 fixed-price certificates, enumerates all 46,662 excess histograms for the final eight tuples, performs exact flow calculations, and runs the common-pressure branch proofs.

The complete verifier output has canonical parsed-JSON SHA-256

```text
5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629
```

Run the complete frozen replay from repository root with

```sh
python3 project/research/general_n/2026-09-14-conditioned-source-sharing-v1/run_replay.py
```

The local complete replay passed before publication. Remote CI is a separate gate and is not called successful until its run is inspected.

## 6. Next target

Do not broaden blind price search. The conditioned-price predecessor leaves original row471 only one and two units short on its `eta=2`, `e_L=39,40` branches, while the stronger uncoupled-witness work shows that selected-incidence/orientation constraints alone are insufficient on rows160,338,347. Prioritize destination-label compatibility and the bridge's ONE shared residual neighbourhood, especially on row471, while carrying this exact common-pressure/source-incidence mechanism across the five remaining originals in parallel. Preserve every non-rejection and keep the fresh-seed namespace separate.
