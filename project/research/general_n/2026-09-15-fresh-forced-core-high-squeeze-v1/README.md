# Fresh forced-core capacity and high-demand squeeze

15 September 2026. Successor to [`forced-core-capacity-v1`](../2026-09-15-forced-core-capacity-v1/README.md). It applies the same exact fixed-neighbourhood routing theorem to the seven survivors of the deliberately separate fresh seed `74220260919`, then adds one higher-demand consequence for the sole capacity-partition survivor. **Necessary-condition proof; external mathematical review OPEN.**

Result:

```text
fresh rows excluded by total forced-core receiver capacity:
  20, 91, 391, 528, 562, 677
fresh row490:
  forced-core partition itself survives
  all six candidate receivers are nevertheless forced used
  s>=3 selected demand = 45
  compatible selected-slot upper = 43
  => EXCLUDED

fresh synthetic sample:    715 / 715 rejected
original synthetic sample: 713 / 713 rejected
canonical finite frontier: unchanged at 4,626 exclusions / 952 survivors / 3,632 whole-state closures
```

These are synthetic necessary-condition profiles, not realized graphs and not canonical whole-state promotions. No unrestricted Murty–Simon proof is claimed.

## 1. General forced eligibility-core lemma

The argument is naturally stated for arbitrary residual level `r`, although the fresh exclusions below use `r=1`.

Put

```text
A_r = { i : s_i <= r },
h   = |A_r|,
U_r = { u : rho_u=r and q_u=h }.
```

Selected-incidence eligibility says every selected label at source `u` has `s_i<=rho_u`. Hence every `u in U_r` has the **same forced selected set**

```text
S_u=A_r.
```

For a selected obligation `(u,i)` from `u in U_r`, exact fixed-neighbourhood routing requires

```text
S_u minus N_v = {i},
S_v subset N_u.
```

Therefore any receiver `v` must satisfy the deliberately relaxed necessary conditions

```text
v not in U_r,
q_v <= h+r-1,
q_v+rho_v >= h-1.
```

It also has incoming capacity

```text
c_v = rho_v+b-a-1.
```

A fixed receiver can serve at most one core label because `A_r minus N_v` has one fixed singleton value. Thus the receiver capacities are indivisible across the `h` label classes, each of which has `|U_r|` obligations. In particular

```text
h |U_r| <= sum_{v in D_r} c_v
```

is necessary, and the stronger exact capacity-partition condition is necessary as well.

## 2. Six fresh survivors fail even the total-capacity inequality

For `r=1`, the fresh remainder gives:

```text
row   h   |U|   receiver capacities   total / required
 20   3    10   7,6,6,5               24 / 30  EXCLUDED
 91   2    12   4                       4 / 24  EXCLUDED
391   2    10   8,4                    12 / 20  EXCLUDED
528   1    11   7                       7 / 11  EXCLUDED
562   1     9   none                    0 /  9  EXCLUDED
677   1    10   none                    0 / 10  EXCLUDED
```

The candidate sets are deliberately relaxed supersets, so each shortage is a valid necessary-condition contradiction.

## 3. Row490: capacity survives, but every receiver is forced used

Row490 has

```text
A={0,1,2}, h=3,
U={1,4,5,11,12,13,19,21,22,26,28}, |U|=11.
```

The relaxed candidate receivers are exactly

```text
D={3,7,10,17,23,27}
```

with capacities

```text
8,6,6,9,8,7.
```

The raw capacity partition is feasible; its exact best minimum label-bin capacity is14 against required11. So this row is **not** excluded by the predecessor theorem alone.

However, every receiver has capacity at most9<11. Since each receiver is dedicated to at most one core label, each of the three core labels needs at least two receivers. That requires at least six distinct receivers, and `D` has exactly six. Hence **every member of D receives at least one forced-core obligation**.

## 4. High-demand squeeze: 43 < 45

If `v in D` is used by an obligation from forced source `u`, exact routing gives

```text
S_v subset N_u=A union R_u.
```

Here `rho_u=1`, so `R_u` contains exactly one label outside `A`. Consequently every used receiver has at most **one selected label outside A**.

Now look at the threshold `tau=3`. Every label with `s_i>=3` lies outside A, and selected-incidence eligibility requires its source to have `rho>=3`.

Row490 needs

```text
W_3 = sum_{s_i>=3} s_i = 45
```

selected high-label incidences. Before using the forced-receiver information, all sources with `rho>=3` have

```text
sum q_u = 46
```

selected slots in total.

Among the six forced-used receivers, the high-eligible ones are

```text
v=3:  rho=3, q=2  -> at most1 high selected label, loss1
v=17: rho=4, q=3  -> at most1 high selected label, loss2
v=23: rho=3, q=1  -> at most1 high selected label, loss0
```

Thus the global high-label selected-incidence upper is

```text
46-(1+2+0)=43 < 45.
```

Contradiction. This excludes row490.

The same observation generalizes: at residual level `r`, every used forced-core receiver has at most `r` selected labels outside `A_r`; therefore for every higher threshold `tau>r`, its `tau`-heavy selected count is at most `r`. This couples receiver usage directly to the threshold-demand machinery.

## 5. Exact replay

[`verify_fresh_forced_core.py`](verify_fresh_forced_core.py) reads the preserved fresh remainder, checks the seed and embedded source digest, reconstructs the seven forced cores and relaxed receiver sets, enumerates every receiver-to-core-label partition, and derives the row490 `tau=3` squeeze using integer arithmetic only.

Frozen parsed result: [`RESULT.json`](RESULT.json). Canonical JSON SHA-256:

```text
7357a5139417a1b48f94d8ddbb6122c57363ce70ab0c4586673a290a25c51464
```

Run [`run_replay.py`](run_replay.py) from repository root. A dedicated remote workflow is installed by this checkpoint and is not called successful until inspected.

## 6. Discovery/audit note

During exploration, an uncommitted SciPy/HiGHS label-compatible MILP also returned infeasible for row490. Project policy treats that status as **non-proof evidence only**. The exclusion committed here does not depend on that solver result: it is the explicit integer inequality `43<45` above, replayed directly from the preserved profile.

## 7. Next use

Both synthetic laboratories are now closed under accumulated necessary conditions. The structural next steps are therefore:

1. package the arbitrary-`r` forced eligibility-core lemma as a reviewer-facing theorem statement;
2. scan the **952 canonical survivors** for exact instances of the forced-core capacity and high-demand squeeze, without promoting a state unless the theorem hypotheses are fully met;
3. seek an aggregate inequality that removes the need for profile-by-profile receiver enumeration;
4. continue external review of the canonical graph-to-selected/residual bridge and fixed-neighbourhood routing theorem.
