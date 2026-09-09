# n=29 common-potential compression checkpoint

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact finite potential verification plus computational support-minimality evidence. This note is not an unrestricted theorem and does not replace independent review of the graph-to-model bridge.

## 1. Exact order-wide potential

The current 9 BC + 7 SH support admits one common staircase-weight vector across all 996 regenerated n=29 RX-Hall hard profiles (902 with t=2 and 94 with t=3). The resulting candidate was rebuilt and checked with integer arithmetic after deterministic scaling/repair:

- 996 profiles;
- 364,805 envelope/model inequalities;
- 22,586 variables;
- zero row violations;
- zero bound violations.

Canonical checkpoint: `checkpoints/N29_ALL_T23_EXACT_RUN_34375129207.json` (manual publication commit `704eeb0fb05ae31bc5e1d04607f826eb07d38631` after the workflow's final push raced).

Thus the 16-shape object is an exact finite n=29 order-wide potential, conditional on the upstream RX-Hall bridge/frontier preparation.

## 2. The 38 exceptional t=2 profiles compress to an exact 14-shape potential

Boundary specialization from dmax=11 to dmax=10 separates 26 of the 64 profiles left by the original n=30 nine-shape transfer, leaving 38 difficult n=29 t=2 profiles.

A common 8 BC + 6 SH potential for all 38 has been exactified with integer-only acceptance. The exactifier records zero row and bound violations at scale 1,000,000.

Canonical checkpoint: `checkpoints/N29_COMMON_14_EXACT_RUN_34369583832.json`.

This is an exact finite **upper/existence** result for the common-support size. It does not by itself prove that 13 shapes are impossible.

## 3. Demand 45 is the single-profile bottleneck

Demand 45 has

```text
s   = (1,1,3,3,3,3,4,4,4,4,4,4)
rho = (1,1,1,1,1,1,1,1,1,3,3,3,4,4,4,4).
```

Across the canonical generated dictionary of 75 BC + 12 SH shapes, the zero-gap minimum-support MILP gives 13 = 7 BC + 6 SH shapes. The selected weights are close to quarter-integers.

Canonical checkpoint: `checkpoints/N29_DEMAND45_FULL_MIN_RUN_34374650328.json`.

This is computational support-minimality evidence under the stated MILP coefficient cap, not an exact mathematical impossibility certificate.

## 4. Demand 45's 13-shape optimum does not extend to all 38

Fixing those 13 shapes and allowing new common weights over all 38 profiles gives a clean LP infeasibility (HiGHS status 8; 17,621 rows, 899 variables).

Canonical checkpoint: `checkpoints/N29_DEMAND45_SUPPORT_COMMON38_RUN_34378926127.json`.

Moreover, all 74 possible one-shape additions from the rest of the canonical 87-shape dictionary were tested. None repairs the demand-45 support into a common 14-shape support for all 38.

Canonical checkpoint: `checkpoints/N29_DEMAND45_ONE_ADDITION_RUN_34379705773.json`.

So the exact common 14-shape object is not simply "demand45 plus one cut"; its BC basis must genuinely change.

## 5. A two-profile 14-support witness: demand 45 + demand 68

Demand 68 is a very small perturbation of demand 45:

```text
Demand 45:
  s counts   : 1^2, 3^4, 4^6
  rho counts : 1^9, 3^3, 4^4

Demand 68:
  s counts   : 1^1, 2^2, 3^4, 4^5
  rho counts : 1^9, 2^1, 3^2, 4^4
```

Equivalently, on the label side one 1 and one 4 are replaced by two 2s, while on the source side one residual degree 3 drops to 2. Both remain in the same t=2 surplus sector.

In the full canonical 75 BC + 12 SH dictionary, the minimum common-support MILP for just these two profiles is 14 = 8 BC + 6 SH with zero MIP gap at both coefficient caps M=200 and M=1000. The first corrected full-dictionary pair run therefore supplies a compact computational lower-bound witness against support 13 under both caps.

Canonical checkpoint: `checkpoints/N29_DEMAND45_PAIR_MIN_RUN_34379676403.json` (manual publication commit `ac7d8d515cd908c75a71ca6d96c1507501f16bea`).

This lower-bound statement remains MILP/computational rather than exact-Farkas. The support cardinality should therefore be described as **computationally pinned to 14 in the canonical generated dictionary**, while the existence/upper side is exact.

## 6. Stable SH family; moving BC family

The structural signal is much cleaner than the raw support count suggests.

The demand-45 optimum, the demand45+68 pair solutions, and the exact 38-profile common solution all use the same six SH staircase shapes. The complexity change lies in BC.

Across the corrected demand45+68 pair solutions and the exact common solution there is a stable six-BC core containing the first three low-threshold BC shapes together with the BC shapes represented by

```text
((1,-1),(2,-3),(4,-4),(5,-9),(10,-10)),
((2,-5),(3,-14)),
((4,-4),(5,-5),(6,-6),(7,-7),(8,-10),(9,-13)).
```

Two additional BC positions move on a small face of alternatives. This suggests that the 14-shape potential should not be interpreted as fourteen unrelated inequalities. A more promising symbolic model is

```text
six fixed SH staircases
+ six fixed/core BC staircases
+ two adaptive BC staircases determined by the demand/source profile.
```

## 7. Interpretation of the 45 -> 68 perturbation

The tiny 45-to-68 move smooths the demand profile (1+4 -> 2+2) while simultaneously lowering one source residual degree (3 -> 2). That move is enough to force a BC basis change while leaving the SH family unchanged.

This points toward a majorization/transport boundary in the BC correction rather than an increase in genuine Hall/supplement complexity. A symbolic generalization should therefore prioritize a parameterized BC envelope responsive to the demand and source degree distributions, with the SH correction family held fixed where possible.

## 8. Cross-order falsification already obtained

The exact n=29 16-shape support was also tested with one single shared staircase-weight vector across all 996 n=29 profiles plus all seven n=30 t=1 hard profiles (1003 profiles total). That LP is infeasible.

Canonical checkpoint: `checkpoints/CROSS_ORDER_ALL1003_FIXED16_RUN_34375647941.json` (commit `ef1c132f47cca792a165cb697834c270a8e3e60e`).

Therefore a general theorem should **not** assume order-independent fixed weights for the n=29 16 shapes. Shape-family universality with weights depending on (a,b,dmax,t) remains plausible and is the next more reasonable target.

## 9. Current next steps

1. isolate which individual n=30 hard profile(s), if any, are incompatible with all 996 n=29 profiles under the fixed 16-shape family;
2. materialize the canonical 75+12 dictionary with stable indices and compare the moving BC shapes geometrically;
3. seek a parameterized BC family explaining the demand45/demand68 basis switch;
4. if useful for publication, strengthen the 14-support lower-bound side beyond big-M MILP evidence (for example by an exact combinatorial/support-exclusion certificate);
5. test parameter-dependent reweighting across n=29 and n=30 before moving to n=31.

No unrestricted Murty-Simon theorem, external validation, or novelty determination is claimed here.
