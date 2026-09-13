# Refined h2 adjacent-family scan

13 September 2026. **Exact integer triage of a necessary-condition relaxation. External mathematical review and independent computational reproduction remain OPEN. No frontier change is claimed by this scan alone.**

## Purpose

This scan applies the refined baseline-3/order-statistic relaxation from `REFINED_BASELINE3_LEMMA.md` to the narrow N34 family structurally adjacent to the five quantified whole-state closures already obtained.

The hash-verified input is reconstructed from the frozen compatible-routing `survivors.json` evidence. Before later whole-state closures there are exactly 4,584 combined survivors. Removing the five closed states 227, 279, 382, 526 and 588 leaves the current 4,579-state frontier.

The family filter is

```text
layer = n34-m289,
a=15, b=18, t=1,
s_i in {2,3},
#{s_i=2} <= 4,
rho_u in {1,2,3},
#{rho_u=2} <= 3.
```

Exactly nine records satisfy this filter: the five closed regression states and four active companions.

## Exact family map

| state | closed? | demand profile | residual profile |
|---:|:---:|---|---|
| 227 | yes | `2^4,3^11` | `1^7,2,3^10` |
| 230 | no | `2^4,3^11` | `1^6,2^3,3^9` |
| 279 | yes | `2^3,3^12` | `1^7,3^11` |
| 282 | no | `2^3,3^12` | `1^6,2^2,3^10` |
| 382 | yes | `2^2,3^13` | `1^6,2,3^11` |
| 385 | no | `2^2,3^13` | `1^5,2^3,3^10` |
| 519 | no | `2,3^14` | `1^6,3^12` |
| 526 | yes | `2,3^14` | `1^5,2^2,3^11` |
| 588 | yes | `3^15` | `1^5,2,3^12` |

Preparation replay:

```text
source SHA256 = 2c6bb11ec3c6dfb45a07b511c1e85c8c44898201c0f045630e0f622ee93647eb
input  SHA256 = efa9c130563b80675b9adf4ea4dc156ba4be7b38f915a72fdca925538876bfb9
family records = 9
active family records = 4
```

## Regression result

The generic scanner reproduces a strictly positive refined-tail gap throughout every previously published strict tail range for states 227, 279, 382, 526 and 588. This is a regression check of the generic implementation, not an independent proof of those states.

## Active-state ranking

The scanner ranks an excess layer as non-strict when the relaxed minimum gap is at most zero. A non-strict layer is only a survivor of the relaxation; it is not a graph and not evidence of feasibility.

### 1. State 519

```text
s=2,3^14,
rho=1^6,3^12,
S=44, r=42,
Emax=34.
```

Nonstrict refined-tail layers:

```text
E=0:-3,
4:-8, 5:-5, 6:-6, 7:-12, 8:-18, 9:-27,
10:-24, 11:-7, 12:-10, 13:-9, 14:-10, 15:-15,
16:-10, 17:-5, 18:0,
22:-2, 23:-4, 24:-8.
```

Thus the cheap refined tail is already strict at `E=1,2,3`, `E=19,20,21`, and every `E=25,...,34`. The scan gives 19 non-strict layers and ranks state 519 first among the four active companions.

### 2. State 282

```text
s=2^3,3^12,
rho=1^6,2^2,3^10,
S=42, r=40.
```

The refined tail is non-strict exactly for `E=0,...,20` and strict for `E=21,...,34`.

### 3. State 385

```text
s=2^2,3^13,
rho=1^5,2^3,3^10,
S=43, r=41.
```

The refined tail is non-strict exactly for `E=0,...,20` and strict for `E=21,...,34`.

### 4. State 230

```text
s=2^4,3^11,
rho=1^6,2^3,3^9,
S=41, r=39.
```

The refined tail is non-strict exactly for `E=0,...,22` and strict for `E=23,...,34`.

## Research consequence

State 519 is the natural next target. Its tail already leaves only a small number of separated low/mid excess layers. A stronger profile-by-profile calculation can retain the full excess histogram, the no-isolated-C bound `d_i<=13`, the residual-budget cap

```text
r >= q_u max(0,q_u-x_max),
```

the source lower-excess restriction

```text
L_u=max(0,p_u-rho_u+1,q_u+p_u-13),
```

and both the coarse residual support function and the refined top-k endpoint envelope. This is substantially stronger than the family tail while remaining selection-free.

A further state-519-specific issue is especially promising: its unique demand-two label has zero excess in each of the few coarse exceptional profiles found so far. Then selected-excess forces `p_u<=2` at both of its selected sources. Any exact low-excess verifier should couple that two-source availability condition directly to the incoming ledger rather than replacing the label's endpoint load by the trivial lower bound `C_i>=2`.

## Replay

Input reconstruction:

```bash
python3 prepare_refined_h2_family_scan.py
```

Generic family scan:

```bash
g++ -O2 -std=c++17 -Wall -Wextra -pedantic scan_refined_h2_family.cpp -o scan_refined_h2_family
./scan_refined_h2_family refined_h2_family_input.txt REFINED_H2_FAMILY_SCAN.tsv
```

GitHub Actions:

- `.github/workflows/replay-refined-h2-adjacent-input.yml`
- `.github/workflows/scan-refined-h2-adjacent-family.yml`

The first scanner workflow attempt failed at compilation because `std::tie` was applied to temporary `size()` values; that tooling failure is preserved. The corrected run completed successfully and produced the figures above.
