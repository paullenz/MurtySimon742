#!/usr/bin/env python3
"""Idempotently advance CURRENT_STATE.md from antichain to staircase-band status.

This script assumes the general/ledger and Hall-structure synchronizers have
already run. It changes research-status prose only, never canonical ledger
counts.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "CURRENT_STATE.md"
HSTART = "<!-- HALL-STRUCTURE-2026-09-14:START -->"
HEND = "<!-- HALL-STRUCTURE-2026-09-14:END -->"
PSTART = "<!-- CURRENT-PRIORITIES-2026-09-14:START -->"
PEND = "<!-- CURRENT-PRIORITIES-2026-09-14:END -->"
ASTART = "<!-- ACTIVE-RELATIONAL-2026-09-14:START -->"
AEND = "<!-- ACTIVE-RELATIONAL-2026-09-14:END -->"

HALL = r'''<!-- HALL-STRUCTURE-2026-09-14:START -->
## 14 September Hall-structure checkpoint

**Status boundary.** The canonical promoted whole-state position remains **977 quantified closures, 1,971 exclusions / 3,607 survivors**. Nothing in this section changes that ledger count. The full post-pair relational scan remains discovery/reconnaissance until its recovery pass and fresh cross-implementation audit complete; only a later separately gated promotion may change the headline frontier.

The current Hall package is [`project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md), with detailed provenance in [`AUDIT.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/AUDIT.md) and [`STAIRCASE_AUDIT.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STAIRCASE_AUDIT.md).

### Internally audited exact target-Hall structure

- **Whole-type Hall theorem:** complete `(q,c,P)` type classes suffice for a minimum target-Hall cut; run `34820069162` is green.
- **Exact type-level max-flow and submodularity:** labelled target flow is min-cut equivalent to the quotient type network; run `34821405958` is green.
- **Sharp dominance:**

  ```text
  x >=_* y iff c_x<=c_y
                 and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
  ```

  If `q_x>=q_y+2` and `c_x<=c_y`, every minimum Hall witness containing `y` contains `x`, independent of `P`. Run `34830228571` is green; artifact digest `sha256:b686e3f9663a082aa9b0ff9fa89d1c0a29904ca3622f205421a895e3babbf37c`.
- **Canonical antichain certificate:** minimum-margin type sets form a lattice; their union `M+` is the unique maximal minimizer, a sharp-hardness up-set, and is uniquely represented by its minimal generator antichain. A closure-augmented quotient max-flow extracts the same `M+`. Run `34830787798` is green; artifact digest `sha256:2ed919e019c7f65a21fbbe92d81e5db84db14e39889bd259d559e2feded08433`.
- **Exact moving staircase:** ordering the generators by cross degree gives

  ```text
  c_1<...<c_h,
  q_1<=...<=q_h,
  ```

  with `P` strictly increasing on every equal-`q` plateau. Membership in the sharp up-set is exactly a moving `(q,P)` threshold at the first generator cross-degree above the type. Run `34831605792` is green; artifact digest `sha256:96ca7d14e9b823ae428f677f21cf60cfa519e7f6326799fcf9b331e433d38ace`.

This moving staircase is not the disproved one-dimensional Ferrers shortcut: the threshold changes with `c`, and genuinely multi-generator boundaries occur.

### Verified staircase-band relaxation

[`STAIRCASE_BAND_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STAIRCASE_BAND_HALL.md) groups selected sources by staircase band. Every source interval in a band is contained in its generator interval. For each target type the generator-compatible source bands form an empty set or a **contiguous interval of band indices**.

Exact target-flow feasibility therefore implies feasibility of a smaller capacitated interval-neighborhood band flow. This step is deliberately a **necessary relaxation**, not an exact equivalence. Run `34832155910` is green; frozen audit totals include `2,786` profiles, `39,991` sharp up-sets, `1,334,288` incoming upper-bound checks and `210,356` band-set capacity checks, with zero discrepancies. Artifact digest: `sha256:ced7c25892c42a0a13a61c404642da6f27af21607655be255b20efd498a03a24`.

In the current Murty-Simon source universe, `c=q+rho` and the q-profile cap includes `q<=a-rho`, so `c<=a`. Since canonical staircase generators have distinct integer `c`, there is at most one generator breakpoint per cross-degree level and hence `h<=a+1`.

### Preserved negative results on generator count

[`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/PRINCIPAL_UPSET_COUNTEREXAMPLE.md) already rules out one principal up-set and a universal two-generator shortcut.

The Murty-specific pilot [`MURTY_ANTICHAIN_PROFILE_STATS_PILOT.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/MURTY_ANTICHAIN_PROFILE_STATS_PILOT.md), run `34831697002`, strengthens that warning. It tested `201,493,148` profiles in the same deterministic 15-state frontier sample and cross-checked **every** labelled target-Hall failure against the dominance-closed quotient max-flow. Among `205,919` target-Hall failures the canonical generator histogram was:

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

The modal obstruction uses four generators and actual Murty-Simon profiles reach eight. This is reconnaissance, not an all-order theorem or a promotion result. It decisively lowers the priority of any small-constant generator approach and points instead to aggregate staircase-band inequalities.

### Full frontier relational scan

The layer/state-safe full scan of the canonical `3,607` survivors is GitHub Actions run `34820187136`, head `3255c0641b00ae97c426d1e089a6b6c92c8300fc`. It uses per-state checkpointing and treats timeouts/errors as unresolved, never as exclusions. The downstream chain remains:

```text
checkpointed discovery
 -> layer-safe aggregate
 -> long-budget recovery of every unresolved/unattempted state
 -> fresh two-implementation state-by-state audit
 -> separate gated promotion only after agreement.
```

A scan shard or preliminary relational exclusion is **not canonical evidence by itself**. N34 and N35 provenance remain in separate ledgers.
<!-- HALL-STRUCTURE-2026-09-14:END -->'''

PRIORITIES = r'''<!-- CURRENT-PRIORITIES-2026-09-14:START -->
## Current research priorities

### P1. Attack the aggregate consecutive-band Hall inequalities

The exact canonical target-Hall obstruction is now a verified moving staircase; actual Murty-Simon profiles often need 4–6 generators and can need 8, so a bounded-generator theorem is not the preferred route. Use [`STAIRCASE_BAND_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STAIRCASE_BAND_HALL.md) as the next symbolic interface: combine the contiguous band neighborhoods with `c=q+rho`, `q<=a-rho`, target caps `P`, demand forcing, selected incidence, pair capacity, unordered-pair Hall and excess-budget constraints. Seek aggregate interval/band inequalities or a restricted parametric family of violating band intervals.

### P2. Complete, recover and independently audit the 3,607-state relational scan

Run `34820187136` is the layer/state-safe checkpointed discovery pass over the canonical survivor frontier. Record every timeout/error as unresolved; recover all unresolved/unattempted layer-states with the long-budget pass; then freshly replay every discovery exclusion through both the vector and independent type-count implementations. Only a later separately gated certificate promotion may change the canonical `1,971/3,607` headline.

### P3. Explain the N35-derived layer

Keep N34 and N35 closure ledgers separate. Compare the 78 N35-derived survivors against eliminated N34 profiles using the exact staircase and band descriptions. The single N35 pilot state showed only 1–4 generator target-Hall failures while the sampled N34 states reached eight, but that sample is far too small for a claim; use it only to choose structural statistics worth testing.

### P4. Strengthen independent review and reproduction

Prioritise external checking of the canonical bridge, exact directed compatibility, whole-type Hall theorem, quotient max-flow equivalence, sharp dominance, canonical antichain/staircase, total-excess source cap and potential-pair theorem. Repository CI and separately written same-assistant code are internal evidence, not third-party acceptance.

### P5. Preserve genuinely different routes

Continue maximum-cut/stability, selection-free and other independent approaches when they have leverage. Preserve negative results, invalidated shortcuts and solver/time-out evidence. Never infer proof from timeout, numerical infeasibility or a solver status alone.
<!-- CURRENT-PRIORITIES-2026-09-14:END -->'''

ACTIVE = r'''<!-- ACTIVE-RELATIONAL-2026-09-14:START -->
## 14 September 2026 — active post-pair relational programme

The **canonical promoted frontier remains `1,971 exclusions / 3,607 survivors`**. The stronger post-pair relational programme is discovery only until full coverage/recovery, fresh cross-implementation audit and a separately gated promotion.

The authoritative layer/state-safe discovery run is GitHub Actions run `34820187136` at head `3255c0641b00ae97c426d1e089a6b6c92c8300fc`. Every record is keyed by `(layer,state)` and each state is checkpointed separately. The earlier run `34818390230` is preserved as historical reconnaissance rather than the authoritative full-frontier pass.

The execution chain is documented in [`POST_PAIR_RELATIONAL_FULL_FRONTIER.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_FULL_FRONTIER.md): checkpointed discovery, layer-safe aggregation, explicit unresolved accounting, long-budget recovery, then fresh primary and independent type-count replay of every candidate exclusion. N34 and N35 promotions use separate ledgers.

The structural track has progressed from labelled target flow to complete types, exact quotient max-flow, submodularity, sharp hardness up-sets, a canonical antichain, an exact moving staircase, and now a verified consecutive-band necessary relaxation. The Murty-specific antichain pilot shows that high generator counts are real inside the scanned relaxation, so the active theory target is **aggregate staircase-band demand/capacity**, not a small-generator shortcut.
<!-- ACTIVE-RELATIONAL-2026-09-14:END -->'''


def replace(text, start, end, block):
    if text.count(start) != 1 or text.count(end) != 1:
        raise SystemExit(f"markers missing or duplicated: {start}")
    return re.sub(re.escape(start) + r".*?" + re.escape(end), block, text, count=1, flags=re.S)


def rewrite(text):
    text = replace(text, HSTART, HEND, HALL)
    text = replace(text, PSTART, PEND, PRIORITIES)
    text = replace(text, ASTART, AEND, ACTIVE)
    return text


def main():
    old = PATH.read_text()
    new = rewrite(old)
    PATH.write_text(new)
    if rewrite(new) != new:
        raise SystemExit("staircase current-state synchronizer is not idempotent")
    required = [
        "977 quantified closures, 1,971 exclusions / 3,607 survivors",
        "run `34831605792` is green",
        "run `34832155910` is green",
        "run `34831697002`",
        "205,919",
        "8:        9",
        "### P1. Attack the aggregate consecutive-band Hall inequalities",
        "run `34820187136`",
        "separate gated promotion only after agreement",
    ]
    missing = [x for x in required if x not in new]
    if missing:
        raise SystemExit(f"staircase handoff missing: {missing}")
    print("CURRENT_STATE_STAIRCASE_20260914_OK")


if __name__ == "__main__":
    main()
