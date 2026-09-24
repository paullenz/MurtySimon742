# n=19, Delta=11: v4 abstract-survivor explosion

24 September 2026, 08:00 scheduled session. Status: failed scalar-extension
route preserved; graph realizability is not established.

The first 200 stable indices were run through the exact-small-star v4 model
with `rho=3` and strict-counterexample allowance `Dmax=27`. Unlike the
adjacent `n=19, Delta=10` row, this prefix produced many abstract survivors.
The first three are:

| index | demand `d` | selected `x` | height `h` | exact deficit | gap |
|---:|---|---|---|---:|---:|
| 1 | `(9,6)` | `(9,6)` | `(9,6)` | 23 | -4 |
| 2 | `(9,6)` | `(9,7)` | `(9,8)` | 18 | -9 |
| 3 | `(9,6)` | `(9,8)` | `(9,10)` | 17 | -10 |

The output volume itself is the useful negative result: simply extending
scalar shards at this row cannot supply a graph theorem. The bounded pivot is
to retain actual source sets `C_i`, private-source incomparability, and edge
criticality, beginning with the extremal two-label profile at index 3. No
prefix-closure claim is made.
