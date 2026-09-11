# n=29, t=2: exact unit-demand regime structure

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural diagnostic inside the already-preserved RX-Hall 3-D model. Not a general-N theorem. Independent mathematical review remains open.**

## Result

Let

```text
nu1(s) = #{ i : s_i = 1 }.
```

For the complete regenerated `n=29, Delta=16, t=2` RX-Hall frontier of 902 profiles, the three exact rational scalar templates from [`N29_T2_3D_THREE_TEMPLATE_EXACT.md`](../2026-09-09-rx-hall-v1/N29_T2_3D_THREE_TEMPLATE_EXACT.md) admit the following exact deterministic assignment:

```text
nu1 = 0  -> T2   825 profiles
nu1 = 1  -> T1    76 profiles
nu1 = 2  -> T0     1 profile
```

No other value of `nu1` occurs on this frontier. Every assigned template has strictly positive exact `fractions.Fraction` certificate gap.

Thus the 902-profile three-template compression is not an arbitrary profile clustering: **one elementary integer statistic partitions the entire frontier into three exact template-valid regimes.**

In the positive-demand sector used here,

```text
nu1 = #{s_i <= 1} = qcap_1,
```

so the scan independently found equivalent exact one-feature partitions using `s_eq_1`, `s_le_1`, `s_ge_2`, and `qcap_1`.

## Alignment with the exact three-template lower bound

The exact incompatibility triangle proving that two scalar templates do not suffice consists of profiles `0`, `3`, and `77`. These lie in the three distinct `nu1` regimes:

| profile index | demand id | `nu1` | exact unique-template role |
|---:|---:|---:|---|
| 0 | 45 | 2 | T0-only witness |
| 3 | 70 | 1 | T1-only witness |
| 77 | 154 | 0 | T2-only witness |

Hence the same elementary statistic that gives the exact three-regime upper assignment also separates the three pairwise-incompatible lower-bound witnesses.

This does **not** by itself prove that `nu1` causes the incompatibility or that an analogous rule holds for general `(n,t)`. It is, however, materially stronger structural evidence than the raw fact that three templates happen to cover 902 finite profiles.

## Exact coverage-mask census

The three exact templates overlap substantially. Writing a mask in `(T0,T1,T2)` order, the exact frontier census is

```text
001   19
010   20
011  129
100    1
110   40
111  693
```

There are therefore 40 profiles covered by exactly one of the three templates, 169 by exactly two, and 693 by all three, matching the preserved exact three-template certificate. The deterministic `nu1` partition deliberately chooses one template for each profile even where other templates also work.

## Reproducibility

Diagnostic source:

```text
n29_t2_regime_structure_scan.py
```

Workflow:

```text
.github/workflows/general-rx-hall-n29-t2-regime-structure.yml
```

Successful GitHub Actions run:

```text
run id:      34580767040
artifact id: 10191502232
artifact:    n29-t2-regime-structure
zip SHA-256: 87352f45da8ae314c672b347d70bc701984de40eba770d94f11d871e6ac92c6d
```

The workflow regenerates the `t=2` frontier, recomputes all three exact rational template gaps, and searches elementary threshold statistics. The regime conclusion above is accepted only after direct exact-gap checking; no machine-learning model or numerical classifier participates.

## Cross-laboratory interpretation

The adjacent exact finite laboratories now look like this:

- `n=30,t=1`: two templates; the preserved exact assignment separates the seven hard profiles by the number of unit demands (`nu1=2` versus `nu1=1`).
- `n=29,t=2`: three templates; the complete 902-profile frontier is exactly partitioned by `nu1=0,1,2` as proved above.
- `n=29,t=3`: four templates; `nu1` alone is insufficient, but the preserved exact four-template replay uses a depth-2 count tree involving only `count(rho=1)`, presence of `s=5`, and presence of `s=1`.

Accordingly the safest current structural target is **not** the overly specific claim that `nu1` always indexes the regimes. A better falsifiable hypothesis is:

> for surplus `t`, the RX-Hall frontier admits a parameter-generated partition into at most `t+1` scalar regimes described by a small decision tree of elementary demand/source counts.

The exact finite minima `2,3,4` make `t+1` natural, but this remains a working hypothesis rather than a theorem.

## Next tests

1. verify that the exact lower-bound clique/witness set at `t=3` hits all four leaves of the preserved elementary count tree;
2. isolate which count transitions distinguish the four `t=3` leaves and compare them symbolically with the `t=1,2` unit-demand transitions;
3. seek a parameterized count-tree rule before generating additional feature families;
4. attack that rule on a fresh finite parameter domain before any general-N proof attempt;
5. keep the graph-to-profile/RX-Hall bridge and 3-D potential lemma as the principal independent-review trust boundary.
