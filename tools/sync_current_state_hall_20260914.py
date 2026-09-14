#!/usr/bin/env python3
"""Idempotently keep CURRENT_STATE.md aligned with the 14 Sep Hall checkpoint.

This synchronizes *research status only*. Canonical frontier counts remain
ledger-derived elsewhere and are intentionally not changed by this script.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "CURRENT_STATE.md"
START = "<!-- HALL-STRUCTURE-2026-09-14:START -->"
END = "<!-- HALL-STRUCTURE-2026-09-14:END -->"
PSTART = "<!-- CURRENT-PRIORITIES-2026-09-14:START -->"
PEND = "<!-- CURRENT-PRIORITIES-2026-09-14:END -->"
ASTART = "<!-- ACTIVE-RELATIONAL-2026-09-14:START -->"
AEND = "<!-- ACTIVE-RELATIONAL-2026-09-14:END -->"

BLOCK = r'''<!-- HALL-STRUCTURE-2026-09-14:START -->
## 14 September Hall-structure checkpoint

**Status boundary.** The canonical promoted whole-state position remains **977 quantified closures, 1,971 exclusions / 3,607 survivors**. Nothing in this section changes that ledger count. The full post-pair relational scan is discovery/reconnaissance until its recovery pass and fresh cross-implementation audit complete; only a later separately gated promotion may change the headline frontier.

### Exact target-Hall compression

The current orientation/Hall package is [`project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md).

- **Whole-type Hall theorem.** For fixed `(q,c,P)` data, every labelled Hall cut is represented exactly by type counts, and coordinatewise discrete concavity implies a minimum Hall margin is attained by a union of complete `(q,c,P)` type classes. GitHub Actions run `34820069162` is green; its frozen audit checked `14,330` profiles, `593,984` labelled/compressed cut equalities and `391,896` coordinate-concavity lines with zero discrepancies.
- **Exact type-level max-flow theorem.** The full labelled target network is equivalent, by min-cut equality, to a quotient network on the distinct `(q,c,P)` types. The Hall-margin set function is submodular. GitHub Actions run `34821405958` is green. This gives exact small type-level certificates rather than labelled max-flow witnesses.
- **Interval form.** Numerical directed compatibility is exactly intersection of source interval `[q,c]` with target interval `[q,c+1]`, before deletion of the self-arc. This is the correct replacement for the disproved one-dimensional Ferrers-prefix simplification.

### Dominance and antichain structure

- [`DOMINANCE_UPSET_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/DOMINANCE_UPSET_HALL.md) proves an exchange/up-set theorem for the initial hardness order `q` up, `c` down, `P` up. Its independent CI replay, run `34827519117`, is green; the preserved artifact digest is `sha256:5e0977bedbd2615df54f4f31f95ec4847635355f10fad835257d92a65697bd21`.
- [`SHARP_DOMINANCE_UPSET_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SHARP_DOMINANCE_UPSET_HALL.md) strengthens the exchange order to

  ```text
  x >=_* y  iff  c_x<=c_y
                 and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
  ```

  In particular, if `q_x>=q_y+2` and `c_x<=c_y`, **every** minimum Hall witness containing `y` also contains `x`, irrespective of `P`. The frozen same-assistant local audit is green on `4,286` profiles, with `1,123,108` submodularity checks, `372,455` sharp exchange checks and `126,654` strict-gap checks. A dedicated GitHub CI replay is present; until its result is separately frozen, this sharper statement must not be described as independently reproduced or externally reviewed.
- The exact quotient network can be augmented with capacity-`Q+1` dominance-closure arcs without changing its min-cut value; see [`DOMINANCE_CLOSED_MAXFLOW.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/DOMINANCE_CLOSED_MAXFLOW.md).
- [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_ANTICHAIN_CERTIFICATE.md) records the next exact consequence: submodularity makes the minimum-margin cuts a lattice, so there is a unique maximal minimizer `M+`; it is a sharp-hardness up-set and is uniquely represented by its minimal antichain generators. This gives a canonical Hall-failure certificate and an exact staircase geometry for the boundary. Its dedicated independent arithmetic verifier is the current next audit target.

### Preserved failed simplifications

[`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/PRINCIPAL_UPSET_COUNTEREXAMPLE.md) prevents a false next step. A three-type `V` profile has every principal up-set nondeficient but a two-generator up-set of margin `-1`; a four-type example needs three incomparable generators. Therefore neither single-type cuts nor one principal up-set is exact in general.

The 15-state principal-upset reconnaissance pilot completed green as a computation but **is not a promotion certificate**: the full relational stack excluded `13/15` states, while principal up-sets completely explained only `2/13`. Principal up-sets killed `17,284` individual profiles versus `14,768` for single-type cuts, so they help pruning but do not capture the genuine multi-generator obstruction.

### Full frontier relational scan

The layer/state-safe full scan of the canonical `3,607` survivors is GitHub Actions run `34820187136`, head `3255c0641b00ae97c426d1e089a6b6c92c8300fc`. It uses per-state checkpointing and treats timeouts/errors as unresolved, never as exclusions. The downstream chain is:

```text
checkpointed discovery
 -> layer-safe aggregate
 -> long-budget recovery of every unresolved/unattempted state
 -> fresh two-implementation state-by-state audit
 -> separate gated promotion only after agreement.
```

A scan shard or preliminary relational exclusion is **not canonical evidence by itself**. N34 and N35 provenance are kept in separate ledgers to prevent layer-count drift. The correct structural priority while this scan proceeds is to analyse the sharp dominance **antichain boundary** of deficient type-level min-cuts, not to force the already-refuted principal-upset shortcut.
<!-- HALL-STRUCTURE-2026-09-14:END -->'''

PRIORITIES = r'''<!-- CURRENT-PRIORITIES-2026-09-14:START -->
## Current research priorities

### P1. Characterise the canonical Hall antichain boundary

Start from [`SHARP_DOMINANCE_UPSET_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SHARP_DOMINANCE_UPSET_HALL.md), [`DOMINANCE_CLOSED_MAXFLOW.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/DOMINANCE_CLOSED_MAXFLOW.md), and [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_ANTICHAIN_CERTIFICATE.md). Verify the canonical maximal-mincut/antichain certificate independently, then seek further exact restrictions on the staircase generators. Do **not** assume a universal one- or two-generator bound: the preserved counterexamples rule those out in general.

### P2. Complete, recover and independently audit the 3,607-state relational scan

Run `34820187136` is the layer/state-safe checkpointed discovery pass over the canonical survivor frontier. Let every shard complete; record every timeout/error as unresolved; recover all unresolved/unattempted layer-states with the long-budget pass; then freshly replay every discovery exclusion through both the vector and independent type-count implementations. Only a later separately gated certificate promotion may change the canonical `1,971/3,607` headline.

### P3. Explain the N35-derived layer

Keep N34 and N35 closure ledgers separate. Compare the 78 N35-derived survivors against eliminated N34 profiles under the exact type-Hall, sharp-dominance and antichain descriptions. The goal is to identify a structural parameter that explains the layer difference, not merely to accumulate N35 exclusions.

### P4. Strengthen independent review and reproduction

Prioritise external checking of the canonical bridge, exact directed compatibility, whole-type Hall theorem, type-level max-flow equivalence, total-excess source cap, potential-pair theorem and the new dominance/antichain arguments. Repository CI and separately written same-assistant code are internal evidence, not third-party acceptance.

### P5. Preserve genuinely different routes

Continue maximum-cut/stability, selection-free and other independent approaches when they have leverage. Preserve negative results such as the coarse low-residual-reservoir scan and every counterexample to an over-strong simplification. Never infer proof from timeout, numerical infeasibility or a solver status alone.
<!-- CURRENT-PRIORITIES-2026-09-14:END -->'''

ACTIVE = r'''<!-- ACTIVE-RELATIONAL-2026-09-14:START -->
## 14 September 2026 — active post-pair relational programme

The **canonical promoted frontier remains `1,971 exclusions / 3,607 survivors`**. A stronger post-pair relational programme is running over those 3,607 ledger-current scalar survivors, but its discoveries are deliberately **not canonical closures** until they pass full coverage/recovery, fresh cross-implementation audit and a separately gated promotion.

The current layer/state-safe discovery run is GitHub Actions run `34820187136` at head `3255c0641b00ae97c426d1e089a6b6c92c8300fc`. It checkpointed every state separately and identifies every record by `(layer,state)`, so later timeout/cancellation cannot erase earlier completed evidence or conflate N34 and N35 IDs. The earlier run `34818390230` is preserved as historical reconnaissance but is not the authoritative full-frontier discovery pass.

The execution chain is documented in [`POST_PAIR_RELATIONAL_FULL_FRONTIER.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_FULL_FRONTIER.md): checkpointed discovery, layer-safe aggregation, explicit unresolved accounting, long-budget recovery of every unresolved/unattempted layer-state, then fresh primary and independent type-count replay of every candidate exclusion. N34 and N35 promotions use separate ledgers.

In parallel, the target-Hall layer has been converted from an opaque labelled max-flow obstruction into exact type-level structure: complete types, quotient max-flow, submodular Hall margin, sharp hardness up-sets, dominance-closed min-cut, and now a canonical antichain boundary. The preserved principal-upset counterexample shows that genuine multi-generator antichains are necessary. The next structural task is therefore to verify and characterise that canonical antichain certificate while the finite scan completes.
<!-- ACTIVE-RELATIONAL-2026-09-14:END -->'''


def replace_marked_or_section(text, start, end, heading, replacement, following_heading=None):
    if start in text or end in text:
        if text.count(start) != 1 or text.count(end) != 1:
            raise SystemExit(f"malformed markers: {start}")
        return re.sub(re.escape(start) + r".*?" + re.escape(end), replacement, text, count=1, flags=re.S)
    if following_heading is None:
        pattern = r"\n" + re.escape(heading) + r"\n.*\Z"
        new, n = re.subn(pattern, "\n" + replacement + "\n", text, count=1, flags=re.S)
    else:
        pattern = r"\n" + re.escape(heading) + r"\n.*?(?=\n" + re.escape(following_heading) + r"\n)"
        new, n = re.subn(pattern, "\n" + replacement + "\n", text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f"section not found exactly once: {heading}")
    return new


def rewrite(text: str) -> str:
    # Update reconciliation phrase without touching ledger-derived numbers.
    text = text.replace(
        "**Research state reconciled:** 14 September 2026 through the audited post-pair relational recovery promotion:",
        "**Research state reconciled:** 14 September 2026 through the audited post-pair relational recovery promotion and Hall-structure checkpoint:",
        1,
    )

    # The adjacent-family paragraph was a live instruction when the frontier was
    # 3,623. Preserve the history but point current work to the canonical 3,607.
    text = text.replace(
        "The remaining **3,623-state** frontier should now be attacked with pair-choice/target Hall, selected-incidence Hall and excess-budget coupling after the cheap potential-pair screen.",
        "The historical 3,623-state frontier has since fallen to the canonical **3,607-state** frontier after the audited 16-state relational recovery. Current work uses the checkpointed relational discovery/recovery/audit pipeline described below.",
    )

    # Hall checkpoint near the top.
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise SystemExit("malformed Hall checkpoint markers")
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), BLOCK, text, count=1, flags=re.S)
    else:
        anchor = "\n## Headline fixed-order candidate status\n"
        if text.count(anchor) != 1:
            raise SystemExit("CURRENT_STATE Hall insertion anchor not found exactly once")
        text = text.replace(anchor, "\n" + BLOCK + "\n" + anchor, 1)

    text = replace_marked_or_section(
        text, PSTART, PEND,
        "## Current research priorities", PRIORITIES,
        "## Research/preservation rules",
    )
    text = replace_marked_or_section(
        text, ASTART, AEND,
        "## 14 September 2026 — active post-pair relational programme", ACTIVE,
        None,
    )
    return text


def main():
    old = PATH.read_text()
    new = rewrite(old)
    PATH.write_text(new)
    # Idempotency / required-status guards.
    again = rewrite(new)
    if again != new:
        raise SystemExit("Hall current-state synchronizer is not idempotent")
    required = [
        "977 quantified closures, 1,971 exclusions / 3,607 survivors",
        "Exact type-level max-flow theorem",
        "SHARP_DOMINANCE_UPSET_HALL.md",
        "CANONICAL_ANTICHAIN_CERTIFICATE.md",
        "PRINCIPAL_UPSET_COUNTEREXAMPLE.md",
        "34820187136",
        "separate gated promotion only after agreement",
        "### P1. Characterise the canonical Hall antichain boundary",
        "### P2. Complete, recover and independently audit the 3,607-state relational scan",
        "The earlier run `34818390230` is preserved as historical reconnaissance",
    ]
    missing = [x for x in required if x not in new]
    if missing:
        raise SystemExit(f"CURRENT_STATE Hall checkpoint missing: {missing}")
    print("CURRENT_STATE_HALL_20260914_OK")


if __name__ == "__main__":
    main()
