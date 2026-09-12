# Hostile internal audit — N33 candidate-v1

12 September 2026. Same-assistant hostile audit. **This is not independent external mathematical review.**

## Verdict

**NO BLOCKING FLAW FOUND in the assembled N33 candidate route.**

The proof remains conditional on the universal selected/residual bridge, the twelve-/thirteen-/fourteen-label tail theorems and the correctness of the exact 25-state finite envelope replay.

## 1. Coverage audit

At `m>=272`, average degree is at least `544/33>16`, so `Delta>=17`.

Every possible maximum degree is covered:

- `Delta=17`: hand witness-deficit argument covers `m>=273` and equality `m=272`.
- `Delta=18`: `m>=273` is scalar-impossible; `m=272` is the 29-state exact/hand frontier.
- `Delta=19`: thirteen-label theorem excludes the target range.
- `20<=Delta<=31`: twelve-label source-independent theorem puts the graph below 272.
- `Delta=32`: universal-vertex D2C graph is a star.

No maximum-degree branch is missing.

## 2. Delta=17 witness arithmetic

For `Delta=17`, define deficits `epsilon_x=17-d(x)` and `T=561-2m`. With no dominating edge, every witness pair has total deficit at least two. The inherited witness count gives

```text
m <= C(h,2)+h(33-h)+o(o-1),
2h+o <= T.
```

At `m>=273`, `T<=15`. Independent recomputation of the maxima for `h=0,...,7` gives

```text
210, 188, 173, 165, 164, 170, 183, 203,
```

all below 273.

At `m=272`, `T=17`. The independent table for `h=0,...,8` is

```text
272, 242, 219, 203, 194, 192, 197, 209, 228.
```

Thus equality uniquely forces `h=0,o=17`. The standard direct/two-step witness capacity inside `O` gives

```text
272 <= e(O)+2(C(17,2)-e(O)) = 272-e(O),
```

so `O` is independent. Its 17 vertices all have degree 16 and there are 16 outside vertices, forcing `K(17,16)`. No finite computation is used here.

## 3. Higher-degree arithmetic

For `Delta=18`, `(a,b)=(14,18)` and the benchmark is 270. At `m>=273`, `t>=3`, so the bridge gives `Q>=24`, contradicting the fourteen-label bound `Q<=23`.

For `Delta=19`, `(a,b)=(13,19)`, benchmark 266 and `m>=272` gives `t>=6`, hence `Q>=31>21`, contradicting the thirteen-label theorem.

For `Delta>=20`, `a<=12`. Positive surplus above `b(33-b)` is excluded by the twelve-label theorem, while `b(33-b)<=260<272` in this range.

These reductions are consistent and leave only `Delta=18,m=272` as the new frontier.

## 4. Uniform dmax=12 dependency

The finite model uses `d_i<=12`. For `(a,b,t)=(14,18,2)`, the isolated-`C` lemma would force

```text
18 <= 14-1-2 = 11
```

if `C` had an isolated vertex. Hence `delta(C)>=1`. Since `F` is the complement of `C` on 14 vertices, `d_F(i)<=12` for every label. The cap is therefore valid uniformly across the equality frontier.

## 5. Frontier completeness

The independent C++ recursion enumerates exactly

```text
C(27,14)=20,058,300
```

nondecreasing fourteen-demand multisets and reproduces

```text
Q22=18,
Q23=3,
Q>23=0.
```

Thus exactly 21 demand profiles survive `Q>=22`. Every one is positive and every demand is at most five.

For a demand profile, residual tails satisfy both

```text
z_h >= gamma_h(W_h)
```

and monotonicity `z_h>=z_{h+1}`. The verifier takes the monotone closure of the lower bounds. If the closure adds `c` tail units, the remaining total slack is

```text
Q-(b+2t)-c = Q-22-c.
```

Every dominating residual-degree multiset can be obtained from the monotone-minimal multiset by raising residual degrees one unit at a time; each such increment raises exactly one tail count. Sorting only removes duplicate representations. Therefore distributing `0,...,available` increments is a conservative complete enumeration of residual-degree multisets satisfying the retained tail/ledger inequalities.

The result is exactly 29 states:

```text
Q=22 : 18 states
Q=23 : 11 states.
```

The domain deliberately allows weaker-than-exact positive-demand ledger states when the inequality permits them; this is safe over-enumeration for an exclusion proof.

## 6. Shifted nine-rectangle potential

The global potential is

```text
4 B(2,0)+2 B(2,7)+B(2,9)+B(2,11)+B(2,14)+B(2,15)
          +B(3,10)+B(3,12)+B(3,13).
```

Because `v=b-h`, this preserves exactly the N32 graph-level `h` cutoffs; only the `v` thresholds move by one when `b` changes 17->18. Every generator is coordinatewise nondecreasing, so the potential-certificate lemma applies.

The finite envelope model keeps the potential weights fixed. It uses only graph-necessary label/source ranges, `s<=rho`, the source degree and supplement caps, threshold transport and the exact residual resource in the scalar gap. Omitting stronger graph constraints can create false survivors, not false exclusions.

A fresh local replay found 25 feasible scalar certificate proposals and four infeasible potential rows. Every one of the 25 proposals exactified at denominator 10,000 after the established one-sided `ell/sigma` repair. Integer rechecking found zero local-row or bound violations; the strict gap numerators range from `-9990` to `-9937`. The four non-covered rows are exactly the four hand profiles listed in the proof.

Floating feasibility is therefore discovery only; accepted exclusions use integer arithmetic.

## 7. Hand-profile A audit

```text
s=(3,4,5^12), rho=(1^6,3,4,5^10).
```

At `h=4`, `W=64` and `Z` has ten `rho=5` sources plus one `rho=4` source. The latter can carry at most the sole demand-four heavy label, hence contributes at most one heavy incidence and is never in `J={ell>4}`.

For `j=|J|`, the refined capacity is

```text
1 + 4(10-j) + 11j - j(j+1)/2.
```

Independent evaluation for `j=0,...,10` is

```text
41,47,52,56,59,61,62,62,61,59,56.
```

The maximum 62 is below `W=64`. Contradiction.

## 8. Hand-profile B audit

```text
s=(3,5^13), rho=(1^6,3,5^11).
```

At `h=4`, `W=65=C_4(11)`. Equality in threshold capacity forces `j=6` or `7`, every high source heavy-active, and every demand-five label to have `x=5`. Therefore at least

```text
65-(11-j)*4 >= 45
```

heavy arcs from `J` have supplements in `Z`, so `sum_Z p>=45`.

For an active `rho=5` source on a demand-five label,

```text
q+p <= R+x = d <= rho+q-1 = q+4,
```

hence `p<=4`. Eleven sources give `sum_Z p<=44`. Contradiction.

## 9. Hand-profile C audit

```text
s=(4^2,5^12), rho=(1^6,4^2,5^10).
```

At `h=5`, `W=60=C_5(10)`. Equality forces all ten `rho=5` sources to carry at least five demand-five incidences and every demand-five label to have `x=5`.

At `h=4`, the two `rho=4` sources can carry only the two demand-four labels, so together contribute at most four heavy incidences. Since `W_4=68`, at least 64 heavy arcs originate in the ten `rho=5` sources. All ten lie in the `h=4` set `J`, hence these arcs have supplements in `Z_4` and `sum_Z p>=64`.

The ten `rho=5` sources have `p<=4` by the exact demand-five incidence argument, contributing at most 40. Each `rho=4` source has the universal bound

```text
p<=rho+b-a-1=7,
```

so the two contribute at most 14. Thus `sum_Z p<=54`, contradiction.

## 10. Hand-profile D audit

```text
s=(4,5^13), rho=(1^6,4,5^11).
```

At `h=2`, `W=69=C_2(12)`. Equality gives `j=9` or `10`, all labels satisfy `x=s`, and at least

```text
69-(12-j)*2 >= 63
```

heavy arcs from `J` have supplements in `Z`, so `sum_Z p>=63`.

For any active high source, `x=s` yields

```text
q+p <= R+x = d <= rho+q-1,
```

hence `p<=rho-1`. The one `rho=4` and eleven `rho=5` sources give

```text
sum_Z p <= 3+11*4 = 47,
```

contradiction.

## 11. Main remaining risks / external priorities

1. Recheck the universal selected/residual bridge from graph definitions.
2. Recheck threshold capacity and, especially, every inference from equality in that proof.
3. Recheck endpoint load/source forcing and the source supplement bound.
4. Independently reproduce the 21-profile / 29-state frontier.
5. Independently replay the 25 exact finite envelope certificates.
6. Review the inherited twelve-, thirteen- and fourteen-label hand theorems.
7. Perform an independent literature/novelty assessment before any publication-priority claim.

## 12. Bottom line

The audit found no missing maximum-degree branch, no accepted floating infeasibility, no arithmetic mismatch in the witness tables, no missed residual-tail state under the retained inequalities, and no failure in the four displayed hand contradictions.

**Candidate status is justified internally; external mathematical validation remains open.**
