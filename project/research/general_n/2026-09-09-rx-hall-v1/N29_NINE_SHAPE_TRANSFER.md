# Cross-order transfer of the n=30 nine-shape staircase dictionary to n=29

9 September 2026. Finite falsification / transfer checkpoint inside the pairwise staircase programme. **This is not a universal theorem and is not needed for the completed n=29 candidate proof.**

## Question

The n=30 hard frontier admits an exact common pairwise staircase potential with globally minimal generated support

\[
9=6\text{ BC}+3\text{ SH}.
\]

To test whether those staircase shapes are merely an n=30 fit, keep exactly the same nine generator shapes and move to the independently regenerated n=29 `Delta=16` RX-Hall hard frontiers at

```text
(a,b,dmax)=(12,16,10).
```

For each n=29 profile separately, allow the continuous staircase/global coefficients and profile envelope variables to refit. No new staircase shape is allowed.

This is deliberately a shape-transfer test, not a shared-coefficient theorem and not proof evidence: numerical LP feasibility is reconnaissance only.

## Regenerated n=29 domains

The existing exact RX-Hall workflow regenerates from committed source:

```text
t=3: 94 hard positive zero-slack profiles;
t=2: 902 hard positive zero-slack profiles.
```

These 996 profiles are the same semantic `(s,rho)` state space used by the pairwise staircase envelope model.

## Result

Workflow run: `34363239363`.

Aggregate artifact:

```text
artifact id: 10108747833
sha256: d2b744df79798bc81e0d2f67b901318aa757f54145fa110f52874d860bfbd7e4
```

Coverage by the **unchanged n=30 nine-shape dictionary**:

| n=29 scope | hard profiles | separated by same 9 shapes | not separated | coverage |
|---|---:|---:|---:|---:|
| `t=3` | 94 | 94 | 0 | 100% |
| `t=2` | 902 | 838 | 64 | 92.9047% |
| total | 996 | 932 | 64 | 93.5743% |

Thus the same finite staircase dictionary transfers to every `t=3` profile and more than 92% of the substantially larger `t=2` frontier, despite changing from `(a,t)=(13,1)` at n=30 to `(12,2)` or `(12,3)` at n=29.

## Interpretation

This is strong anti-overfitting evidence for the **shape family**, not a theorem:

- the coefficients are allowed to refit profile by profile;
- feasibility is floating-point reconnaissance in this transfer test;
- the n=29 fixed-order proof does not depend on it;
- the 64 `t=2` profiles are genuine survivors of this restricted nine-shape envelope dictionary, not graph survivors.

The immediate research target is therefore narrow: explain or eliminate the 64 `t=2` transfer survivors using the smallest order/surplus correction possible before enlarging the staircase dictionary.

Two of the globally optimal n=30 BC shapes contain a terminal generator `(11,-11)`, while the n=29 label support has `dmax=10`. The first correction test should therefore specialise/remove these unreachable n=30 boundary generators and re-run the 64 survivors before introducing any genuinely new shape.
