# N34 state 231 — whole-state exclusion

13 September 2026. **Candidate whole-state exclusion inside the frozen N34 generalisation experiment. External mathematical review remains OPEN.**

## Frozen scalar state

The class-packing scanner uses

```text
state = 231
n2 = 4
n3 = 11
rho multiplicities = 1^5, 2^5, 3^8
S = 41
r = 39
a = 15
b = 18
```

Equivalently the demand side has four demand-two labels and eleven demand-three labels in the canonical low-demand encoding.

## Previous residual obstruction

The earlier endpoint class-packing pass had reduced the state to five nonpositive excess layers. The preserved diagnostic is [`STATE_231_CLASS_PACKING_RESIDUALS.tsv`](STATE_231_CLASS_PACKING_RESIDUALS.tsv):

| E | gap before class packing | separate-class packing gap |
|---:|---:|---:|
| 6 | -5 | +1 |
| 7 | -2 | -1 |
| 8 | -3 | +1 |
| 9 | -7 | +1 |
| 10 | -3 | -3 |

Thus the only remaining failures of the quantified relaxation were `E=7` and `E=10`.

## New ingredient: mixed demand-class Hall projection

[`ENDPOINT_CLASS_PACKING.md`](ENDPOINT_CLASS_PACKING.md), Section 10, records the new joint threshold obstruction. For any proposed set of `i` low-endpoint demand-two labels and `j` low-endpoint demand-three labels, the same low-load source incidences must satisfy

```text
2i+3j
 <= sum_{rho=2 low sources} min(q_u,i)
  + sum_{rho>=3 low sources} min(q_u,i+j).
```

This is only used as a necessary Hall condition. At each endpoint threshold the scanner maximises the number of labels that can remain below the threshold subject to all such inequalities. Threshold summation gives a lower bound on the **combined** endpoint mass of the two zero-excess classes.

Crucially, the mixed bound is used only to reject an incoming-`p` allocation when the resulting endpoint lower bound exceeds the exact budget

```text
sum_i C_i = r+Q.
```

The score objective itself continues to use the previously proved separate demand-two contribution. Hence the refinement does not obtain its gain by adding the same endpoint mass twice.

## Replay result

The strengthened generator [`make_class_packing_scanner.py`](make_class_packing_scanner.py) was replayed on all five previously nonpositive layers. The preserved output is [`STATE_231_JOINT_HALL_RESULTS.tsv`](STATE_231_JOINT_HALL_RESULTS.tsv):

| E | strengthened minimum gap |
|---:|---:|
| 6 | +1 |
| 7 | +1 |
| 8 | +1 |
| 9 | +1 |
| 10 | +1 |

So both former residual failures become strict, and every previously nonpositive excess layer is now excluded.

The GitHub Actions replay `test class-packing state231 residuals`, run `34783958120`, completed successfully and preserved its raw five-layer output as artifact `state231-class-packing-results` (artifact id `10325662932`, SHA-256 digest `b7edf9ccf54323aa4a58825e1b827eb71c57c0dd3aa434679d51e5b9786d9dda`).

## Whole-state conclusion

The preceding quantified family scan was already strict outside `E=6,7,8,9,10`. Since the joint-Hall replay is now strict on all five of those residual layers, **state 231 is excluded as a whole scalar state in the frozen N34 experiment**.

This is a scalar-state exclusion, not a claim that a graph with these aggregate parameters was constructed or independently ruled out directly. It inherits the trust boundary of the canonical selected/residual bridge and of the frozen N34 catalogue.

## Audit strengthening

A separate independent small-system verifier, [`verify_joint_endpoint_hall_small.py`](verify_joint_endpoint_hall_small.py), exhaustively compares the mixed threshold lower bound with the exact minimum endpoint mass for small simple incidence systems. It is wired into CI so later edits to either the lemma or scanner cannot silently change this ingredient without a replay.
