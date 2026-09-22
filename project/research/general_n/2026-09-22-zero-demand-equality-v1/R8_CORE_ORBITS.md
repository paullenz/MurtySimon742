# Exact colour-preserving quotient of the strict `r=8` core census

Trust level: internal exact computation of the existing optimistic necessary relaxation. This is not graph realizability and is not a proof of the global conjecture.

The 11,350 labelled strict-surplus survivors from the previous census collapse to **68 exact orbits** under permutations preserving each residual-mass class:

| Residual partition | labelled survivors | exact orbits |
|---|---:|---:|
| `(3,2,1,1,1)` | 2 | 2 |
| `(3,1,1,1,1,1)` | 157 | 5 |
| `(2,2,2,1,1)` | 1 | 1 |
| `(2,2,1,1,1,1)` | 685 | 29 |
| `(2,1,1,1,1,1,1)` | 10,505 | 31 |

The previously closed `(2,2,2,1,1)` orbit is retained as a regression control, leaving 67 exact core orbits in four partitions for physical-source screening. Canonical masks and full representatives are saved in `R8_CORE_ORBITS.json`.

Method: enumerate the identical local/core relaxation used by `screen_r8_core_counts.py`; for each survivor take the minimum edge mask over the direct product of symmetric groups on equal-`R` labels. The sum of labelled survivors reproduces 11,350 exactly.
