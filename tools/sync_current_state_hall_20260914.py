#!/usr/bin/env python3
"""Idempotently keep CURRENT_STATE.md aligned with the 14 Sep Hall checkpoint.

This synchronizes *research status only*.  Canonical frontier counts remain
ledger-derived elsewhere and are intentionally not changed by this script.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "CURRENT_STATE.md"
START = "<!-- HALL-STRUCTURE-2026-09-14:START -->"
END = "<!-- HALL-STRUCTURE-2026-09-14:END -->"

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
- The exact quotient network can be augmented with capacity-`Q+1` dominance-closure arcs without changing its min-cut value; see [`DOMINANCE_CLOSED_MAXFLOW.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/DOMINANCE_CLOSED_MAXFLOW.md). Thus an optimal Hall witness can be represented by an **up-set**, hence by its minimal antichain boundary.

### Preserved failed simplifications

[`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/PRINCIPAL_UPSET_COUNTEREXAMPLE.md) prevents a false next step. A three-type `V` profile has every principal up-set nondeficient but a two-generator up-set of margin `-1`; a four-type example needs three incomparable generators. Therefore neither single-type cuts nor one principal up-set is exact in general.

The 15-state principal-upset reconnaissance pilot completed green as a computation but **is not a promotion certificate**: the full relational stack excluded `13/15` states, while principal up-sets completely explained only `2/13`. Principal up-sets killed `17,284` individual profiles versus `14,768` for single-type cuts, so they help pruning but do not capture the genuine multi-generator obstruction.

### Full frontier relational scan

The layer/state-safe full scan of the canonical `3,607` survivors is GitHub Actions run `34820187136`. It uses per-state checkpointing and treats timeouts/errors as unresolved, never as exclusions. The downstream chain is:

```text
checkpointed discovery
 -> layer-safe aggregate
 -> long-budget recovery of every unresolved/unattempted state
 -> fresh two-implementation state-by-state audit
 -> separate gated promotion only after agreement.
```

A scan shard or preliminary relational exclusion is **not canonical evidence by itself**. N34 and N35 provenance are kept in separate ledgers to prevent layer-count drift. The correct structural priority while this scan proceeds is to analyse the sharp dominance **antichain boundary** of deficient type-level min-cuts, not to force the already-refuted principal-upset shortcut.
<!-- HALL-STRUCTURE-2026-09-14:END -->'''


def rewrite(text: str) -> str:
    # Update the reconciliation phrase without touching ledger-derived numbers.
    text = text.replace(
        "**Research state reconciled:** 14 September 2026 through the audited post-pair relational recovery promotion:",
        "**Research state reconciled:** 14 September 2026 through the audited post-pair relational recovery promotion and Hall-structure checkpoint:",
        1,
    )
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise SystemExit("malformed Hall checkpoint markers")
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), BLOCK, text, count=1, flags=re.S)
        return text
    anchor = "\n## Headline fixed-order candidate status\n"
    if text.count(anchor) != 1:
        raise SystemExit("CURRENT_STATE insertion anchor not found exactly once")
    return text.replace(anchor, "\n" + BLOCK + "\n" + anchor, 1)


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
        "PRINCIPAL_UPSET_COUNTEREXAMPLE.md",
        "34820187136",
        "separate gated promotion only after agreement",
    ]
    missing = [x for x in required if x not in new]
    if missing:
        raise SystemExit(f"CURRENT_STATE Hall checkpoint missing: {missing}")
    print("CURRENT_STATE_HALL_20260914_OK")


if __name__ == "__main__":
    main()
