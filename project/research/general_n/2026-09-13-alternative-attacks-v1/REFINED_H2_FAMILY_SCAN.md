# Refined h2 adjacent-family scan

13 September 2026. **Exact integer triage of a necessary-condition relaxation. External mathematical review and independent computational reproduction remain OPEN. The scan itself is not a frontier theorem; its first-ranked active target, state 519, was subsequently closed by the separate whole-state package described below.**

## Purpose

This scan applies the refined baseline-3/order-statistic relaxation from `REFINED_BASELINE3_LEMMA.md` to the narrow N34 family structurally adjacent to the first five quantified whole-state closures.

The hash-verified input was reconstructed from the frozen compatible-routing `survivors.json` evidence. Before the later whole-state closures there were exactly 4,584 combined survivors. At scan time, removing states 227, 279, 382, 526 and 588 left 4,579 active states.

The family filter is

```text
layer = n34-m289,
a=15, b=18, t=1,
s_i in {2,3},
#{s_i=2} <= 4,
rho_u in {1,2,3},
#{rho_u=2} <= 3.
```

Exactly nine records satisfy this filter: the five then-closed regression states and four then-active companions.

## Exact family map at scan time

| state | status at scan time | demand profile | residual profile | later status |
|---:|:---:|---|---|---|
| 227 | closed | `2^4,3^11` | `1^7,2,3^10` | closed |
| 230 | active | `2^4,3^11` | `1^6,2^3,3^9` | active |
| 279 | closed | `2^3,3^12` | `1^7,3^11` | closed |
| 282 | active | `2^3,3^12` | `1^6,2^2,3^10` | active |
| 382 | closed | `2^2,3^13` | `1^6,2,3^11` | closed |
| 385 | active | `2^2,3^13` | `1^5,2^3,3^10` | active |
| 519 | active | `2,3^14` | `1^6,3^12` | **closed by follow-through** |
| 526 | closed | `2,3^14` | `1^5,2^2,3^11` | closed |
| 588 | closed | `3^15` | `1^5,2,3^12` | closed |

Preparation replay:

```text
source SHA256 = 2c6bb11ec3c6dfb45a07b511c1e85c8c44898201c0f045630e0f622ee93647eb
input  SHA256 = efa9c130563b80675b9adf4ea4dc156ba4be7b38f915a72fdca925538876bfb9
family records = 9
active family records at scan time = 4
```

## Regression result

The generic scanner reproduced a strictly positive refined-tail gap throughout every previously published strict tail range for states 227, 279, 382, 526 and 588. This is a regression check of the generic implementation, not an independent proof of those states.

## Active-state ranking produced by the scan

The scanner calls an excess layer non-strict when the relaxed minimum gap is at most zero. A non-strict layer is only a survivor of the relaxation; it is not a graph and not evidence of feasibility.

### 1. State 519

```text
s=2,3^14,
rho=1^6,3^12,
S=44, r=42,
Emax=34.
```

Nonstrict refined-tail layers were

```text
E=0:-3,
4:-8, 5:-5, 6:-6, 7:-12, 8:-18, 9:-27,
10:-24, 11:-7, 12:-10, 13:-9, 14:-10, 15:-15,
16:-10, 17:-5, 18:0,
22:-2, 23:-4, 24:-8.
```

Thus the cheap refined tail was already strict at `E=1,2,3`, `E=19,20,21`, and every `E=25,...,34`. The scan gave 19 non-strict layers and ranked state 519 first among the four active companions.

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

## Follow-through: state 519 closed

The ranking was acted on immediately. The stronger state-519 package retained the full excess histogram, the no-isolated-C bound `d_i<=13`, the residual-budget cap

```text
r >= q_u max(0,q_u-x_max),
```

the source lower-excess restriction

```text
L_u=max(0,p_u-rho_u+1,q_u+p_u-13),
```

and both the coarse residual support function and refined top-k endpoint envelope.

The exact sweep through `E=24` left only one coarse nonpositive profile at each of `E=6,8,9`. A new exact-demand source-availability refinement then closed all three layers. The tail verifier is strict for every `E=25,...,34`, and incoming capacity excludes `E>=35`.

Canonical files:

- `STATE_519_WHOLE_STATE.md`
- `STATE_519_REPLAY.md`
- `STATE_519_WHOLE_STATE_VERIFICATION.json`
- `ZERO_EXCESS_ENDPOINT_ORDER.md`

GitHub Actions run `34773463128` completed green on all proof-critical stages. State 519 therefore becomes the sixth internally verified whole-state exclusion, moving the frozen frontier to

```text
1,000 exclusions / 4,578 survivors
= 4,500 N34 + 78 N35.
```

The remaining active companions in this narrow family are now states **230, 282 and 385**.

## New general lesson from the follow-through

The state-519 exception work yields a reusable exact-demand endpoint-order lemma. For a zero-excess demand-`d` label, every selected source has

```text
rho_u>=d,
p_u<=rho_u-1,
q_u>0.
```

If the eligible source endpoint loads `q_u+p_u` are ordered increasingly, then the label's `C_i` is at least the `d`-th order statistic. For a zero-excess demand-two label this strengthens the universal baseline-three correction `-2` to a state-dependent `-lambda_2`. See `ZERO_EXCESS_ENDPOINT_ORDER.md`.

This suggests the next adjacent-family scan should optimize that endpoint order statistic jointly with the incoming ledger rather than use only `2z_0`.

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
- `.github/workflows/verify-state519-whole-state.yml`

The first generic scanner workflow attempt failed at compilation because `std::tie` was applied to temporary `size()` values; that tooling failure is preserved. The corrected family scan and the later state-519 whole-state replay both completed successfully.
