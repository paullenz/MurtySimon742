# Audit record — Hall staircase and band layers

14 September 2026. **Internal exact audits green. External mathematical review, novelty assessment and genuinely independent third-party reproduction remain OPEN.**

This note continues [`AUDIT.md`](AUDIT.md) from the canonical-antichain layer into the moving-threshold staircase, the consecutive-band relaxation, and the Murty-specific generator-complexity pilot.

## 1. Exact staircase-threshold theorem

[`STAIRCASE_THRESHOLD_HALL.md`](STAIRCASE_THRESHOLD_HALL.md) proves that every sharp-hardness up-set has a unique moving threshold representation. If its minimal generators are ordered by

```text
c_1<c_2<...<c_h,
```

then

```text
q_1<=q_2<=...<=q_h,
```

and `P` strictly increases on every equal-`q` plateau. For a type `x=(q,c,P)`, if `i(c)=min{i:c<=c_i}`, then

```text
x is selected
iff q>q_i(c)
    or [q=q_i(c) and P>=P_i(c)].
```

This is an exact representation of the already-proved sharp up-set. It does **not** revive the false one-dimensional Ferrers-prefix claim: the threshold changes with cross degree `c`, and multiple incomparable generators can be essential.

### CI replay

GitHub Actions run:

```text
run id:    34831605792
head:      93fcbd1baa56633ad1aa8686ec1e3b296ee0f782
conclusion: success
artifact:  10342113783
artifact digest:
sha256:96ca7d14e9b823ae428f677f21cf60cfa519e7f6326799fcf9b331e433d38ace
```

Frozen record: [`STAIRCASE_THRESHOLD_HALL_VERIFICATION.json`](STAIRCASE_THRESHOLD_HALL_VERIFICATION.json).

Exact audit totals:

```text
profiles:                  4,286
sharp up-sets checked:    69,136
distinct-c checks:        69,136
generator-step checks:    77,285
membership checks:       411,436
reconstruction checks:    69,136
rectangle-margin checks:  69,136
maximum generators:            6
zero discrepancies.
```

The verifier independently reconstructs every sharp up-set from the moving `(q,P)` threshold and checks the staircase rectangle-count formula against the direct complete-type Hall margin.

## 2. Murty-specific staircase-height bound

In the current canonical frontier universe,

```text
c=q+rho
```

and the q-profile generation cap includes

```text
q<=a-rho.
```

Hence

```text
c<=a.
```

Since distinct generators have distinct integer cross degree, the canonical staircase has at most one breakpoint per `c` level, giving the immediate problem-specific bound

```text
h<=a+1.
```

This is a safe linear bound, not a claim that `h` is small or constant.

## 3. Staircase-band Hall relaxation

[`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md) groups selected sources according to the first generator cross-degree above their own `c`. If `B_i` is a band with source-copy count `M_i` and exact total demand `D_i`, every source interval in that band is contained in the generator interval `[q_i,c_i]`.

For target type `sigma`, the generator-compatible band set is

```text
I_sigma={i:q_i<=c_sigma+1 and q_sigma<=c_i}.
```

Because generator `q_i` is nondecreasing and `c_i` strictly increases, `I_sigma` is empty or a **contiguous interval of band indices**. This is the first legitimate consecutive-ones structure recovered after the false individual-source Ferrers shortcut: it appears only after exact staircase reduction and is used as an explicit relaxation.

For any band set `J`, exact target Hall is bounded above by the band capacity

```text
sum_sigma n_sigma min(P_sigma,U_sigma(J)),
```

where `U_sigma(J)` counts generator-compatible source copies from chosen bands with the target's own source copy deleted when appropriate. Therefore exact target-flow feasibility implies feasibility of the smaller band flow. Failure is a valid obstruction; passing the band flow is only a relaxation.

### CI replay

GitHub Actions run:

```text
run id:    34832155910
head:      1369bee8e44596a4ea5eac0f7af9fe6d76206164
conclusion: success
artifact:  10342159518
artifact digest:
sha256:ced7c25892c42a0a13a61c404642da6f27af21607655be255b20efd498a03a24
```

Frozen record: [`STAIRCASE_BAND_HALL_VERIFICATION.json`](STAIRCASE_BAND_HALL_VERIFICATION.json).

Audit totals:

```text
profiles:                            2,786
sharp up-sets checked:              39,991
band-demand checks:                 79,626
source-interval containment:       112,807
target interval-neighborhood:      214,908
incoming upper-bound checks:     1,334,288
band-set capacity checks:          210,356
maximum bands:                           6
zero discrepancies.
```

## 4. Murty-specific canonical-antichain pilot

[`MURTY_ANTICHAIN_PROFILE_STATS_PILOT.md`](MURTY_ANTICHAIN_PROFILE_STATS_PILOT.md) measures the exact canonical generator count on the same deterministic 15-state Murty-Simon pilot used for the earlier single-type and principal-upset reach scans.

GitHub Actions run:

```text
run id:    34831697002
head:      d976a4fccb0fb0201ce75498b40909765af6d480
conclusion: success
artifact:  10342124522
artifact digest:
sha256:b0f5596399faf3e273a981a0e8c2929b3c1c2c34bf50047e2be085bf4bb65222
```

The scanner aborts unless every labelled target-flow failure has exactly the same maximum-flow value in the independently constructed sharp-dominance-closed quotient network. Thus generator statistics are counted only after exact flow equality.

Aggregate:

```text
states:                              15
N34-derived:                         14
N35-derived:                          1
profiles tested:            201,493,148
target-Hall failures:           205,919
relationally excluded states:        13
relational survivors:                 2
maximum canonical generators:         8
```

Generator distribution among the 205,919 actual target-Hall failures:

```text
1:      214
2:    6,722
3:   41,452
4:   80,972
5:   58,775
6:   16,349
7:    1,426
8:        9
9+:       0
```

The modal obstruction uses **four** generators. Five-generator obstructions are also extremely common, and one N34 pilot state reaches eight.

This is decisive evidence against spending effort on a universal one-, two-, or other small-constant generator theorem inside the current relaxation. It does not prove anything about asymptotic generator counts.

Frozen records:

- [`MURTY_ANTICHAIN_PROFILE_STATS_PILOT_SUMMARY.json`](MURTY_ANTICHAIN_PROFILE_STATS_PILOT_SUMMARY.json)
- [`MURTY_ANTICHAIN_PROFILE_STATS_PILOT.tsv`](MURTY_ANTICHAIN_PROFILE_STATS_PILOT.tsv)
- [`make_antichain_stats_scanner.py`](make_antichain_stats_scanner.py)

## 5. Current safe structural chain

The internally audited target-Hall chain is now

```text
labelled target flow
 -> complete (q,c,P) type cuts
 -> exact quotient max-flow
 -> submodular Hall margin
 -> sharp dominance up-set
 -> canonical maximal-mincut antichain
 -> exact moving-threshold staircase
 -> consecutive-band flow relaxation.
```

The first six arrows through the staircase representation are exact within the target-Hall relaxation. The final band step is deliberately one-way: exact flow implies band-flow feasibility, not conversely.

## 6. Research consequence

The next all-order target is no longer a bounded number of generators. It is an aggregate theorem for a monotone staircase whose target neighborhoods are intervals of staircase bands.

The most promising route is to combine the band demands/capacities with Murty-Simon-specific information absent from arbitrary Hall profiles:

- `c=q+rho`;
- the canonical cap `q<=a-rho`;
- exact target-capacity formula `P`;
- demand forcing and selected-incidence constraints;
- total excess and excess-budget bounds;
- the pair-capacity and unordered-pair Hall layers that every target-Hall profile has already survived.

A useful general theorem would show that these earlier constraints force every legal staircase-band flow to have nonnegative Hall margin, or reduce the possible violating band intervals to a tractable parametric family.

## 7. Trust boundary

All CI records above are internal exact/reproducible evidence, not external mathematical acceptance. The entire package inherits the canonical graph-to-constraint bridge and target-capacity assumptions. The Murty-specific pilot is reconnaissance only and promotes no state.

The unrestricted Murty-Simon conjecture remains unproved by this project.
