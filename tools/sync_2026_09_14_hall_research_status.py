#!/usr/bin/env python3
"""Idempotently expose the 14 Sep Hall advance on canonical navigation surfaces.

This script changes documentation only. It must not alter any canonical closure
ledger or headline frontier count.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "CURRENT_STATE.md"
README = ROOT / "README.md"
ALT = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1/README.md"
FULL = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_FULL_FRONTIER.md"
THEOREM = ROOT / "project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/TYPE_COMPRESSED_ORIENTATION_HALL.md"

THEOREM_LINK = "project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md"


def replace_once_or_present(text, old, new, label):
    if new in text:
        return text
    if old not in text:
        raise SystemExit(f"documentation anchor missing for {label}")
    return text.replace(old, new, 1)


def append_once(path, marker, block):
    text = path.read_text()
    if marker in text:
        return False
    if not text.endswith("\n"):
        text += "\n"
    text += "\n" + block.strip() + "\n"
    path.write_text(text)
    return True


def update_current():
    text = CURRENT.read_text()
    anchor = "- exact directed compatibility and Hall-flow projection: an orientation `u->w` requires `q_u<=q_w+rho_w+1` and `q_w<=q_u+rho_u`; the resulting source-target relation is genuinely two-dimensional rather than Ferrers in general."
    addition = anchor + "\n- whole-type orientation Hall theorem: for a fixed target-flow profile, group sources/targets by identical `(q,c,P)` type. The exact Hall margin is separately discretely concave in every type-count coordinate, so if any labelled Hall cut fails then a union of complete `(q,c,P)` type classes also fails with at least as large a deficiency. The target-flow test therefore reduces exactly to at most `2^k` complete-type cuts for `k` distinct types; [the theorem package](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md) has a green exact finite audit but external mathematical review and novelty assessment remain open."
    text = replace_once_or_present(text, anchor, addition, "CURRENT_STATE Hall theorem bullet")
    CURRENT.write_text(text)

    append_once(
        CURRENT,
        "## 14 September 2026 — active post-pair relational programme",
        """
## 14 September 2026 — active post-pair relational programme

The **canonical promoted frontier remains `1,971 exclusions / 3,607 survivors`**. A stronger post-pair relational discovery programme is running over those 3,607 ledger-current scalar survivors, but its discoveries are deliberately **not canonical closures** until they pass fresh cross-implementation audit and frozen-certificate promotion.

The execution chain is documented in [`POST_PAIR_RELATIONAL_FULL_FRONTIER.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_FULL_FRONTIER.md): checkpointed per-state discovery, explicit timeout/error recording, a long-budget recovery pass for every unresolved or unattempted layer-state, then fresh primary and independent type-count replay of every discovery exclusion. N34 and N35 whole-state promotions use separate ledgers so layer provenance cannot be silently conflated.

The intended canonical discovery experiment is GitHub Actions run `34818390230` at head `94f89d5d0147842f9d0c2e10606d2117e62400f5`. A later duplicate full scan was accidentally queued before the expensive workflow was made manual-only; it has no canonical status and cannot promote anything. All future full-frontier discovery launches are explicit `workflow_dispatch` operations.

The dominant structural lesson from early reconnaissance is that the exact **directed target-Hall** layer is much stronger than the older one-dimensional threshold projection. This motivated the [whole-type orientation Hall theorem](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md): arbitrary labelled target-Hall cuts reduce exactly to unions of complete `(q,c,P)` types. Its frozen internal verifier checked `14,330` profiles, `593,984` labelled/compressed cut equalities and `391,896` coordinate-concavity lines with zero discrepancies. These are internal checks, not external acceptance.
""",
    )


def update_root_readme():
    text = README.read_text()
    old = "Important candidate all-order or parameterized results include balanced-degree reduction; the `7/12` maximum-degree theorem candidate; heavy-load/routing families; joint routing and demand/tail projection; compatible-destination routing and Hall/flow criteria; containment spill and pair-overlap inequalities; shared residual budgets; selection-free candidate capacity; the selected-excess / threshold family; the refined baseline-3/order-statistic lemma; the zero-excess endpoint-order lemma; exact low-demand incidence-capacity; mixed-class joint Hall; and the orientation target-capacity lemma for missing-edge orientations."
    new = "Important candidate all-order or parameterized results include balanced-degree reduction; the `7/12` maximum-degree theorem candidate; heavy-load/routing families; joint routing and demand/tail projection; compatible-destination routing and Hall/flow criteria; containment spill and pair-overlap inequalities; shared residual budgets; selection-free candidate capacity; the selected-excess / threshold family; the refined baseline-3/order-statistic lemma; the zero-excess endpoint-order lemma; exact low-demand incidence-capacity; mixed-class joint Hall; the orientation target-capacity lemma for missing-edge orientations; and the exact whole-type reduction for the two-dimensional target-Hall system."
    text = replace_once_or_present(text, old, new, "root general-results sentence")

    anchor = "- [Fixed-neighbourhood / arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md)."
    addition = anchor + "\n- [Whole-type orientation Hall research package](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md) — exact reduction of labelled target-Hall cuts to unions of complete `(q,c,P)` types; green internal exact audit, external review/novelty open."
    text = replace_once_or_present(text, anchor, addition, "root reviewer package link")
    README.write_text(text)


def update_alt_readme():
    text = ALT.read_text()
    anchor = "10. **Potential-pair capacity** — [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md) forgets the orientation but retains which unordered pairs could possibly be missing, giving `p_u+q_u<=d_KD(u)`; this is the mechanism behind the audited 943-state frontier family."
    addition = anchor + "\n11. **Whole-type target-Hall reduction** — the [14 September theorem package](../2026-09-14-type-compressed-orientation-hall-v1/README.md) proves that the exact target-Hall margin is coordinatewise concave in identical `(q,c,P)` type counts, so any failing labelled cut has an equally strong or stronger witness that is a union of complete types."
    text = replace_once_or_present(text, anchor, addition, "alternative-attacks hierarchy")
    # Avoid duplicate ordinal 11 on the pre-existing low-c item.
    text = text.replace("11. **Low-`c`/high-`q` threshold obstruction**", "12. **Low-`c`/high-`q` threshold obstruction**", 1)
    ALT.write_text(text)


def update_full_frontier_record():
    append_once(
        FULL,
        "## Canonical discovery-run provenance",
        """
## Canonical discovery-run provenance

The intended first full-frontier discovery experiment is GitHub Actions run `34818390230`, head `94f89d5d0147842f9d0c2e10606d2117e62400f5`. It was launched before the later layer-state checkpoint hardening; the downstream summarizer therefore reconstructs layer identity from each frozen shard input and rejects any unresolved ambiguity rather than guessing.

A later code update queued a redundant second full-frontier run before the expensive scan workflow was changed to manual-only. That duplicate run is noncanonical reconnaissance: it has no authority to change a ledger or headline count. The promotion path is gated entirely on the layer-safe aggregate/recovery/audit chain documented above.
""",
    )


def update_theorem_assumption():
    text = THEOREM.read_text()
    old = "where\n\n```text\nc_u=q_u+rho_u,"
    new = "where every `P_w` is a valid **nonnegative integer** upper bound on the target indegree `p_w` (a negative candidate cap already excludes the profile before this flow is formed), and\n\n```text\nc_u=q_u+rho_u,"
    text = replace_once_or_present(text, old, new, "theorem P nonnegativity")
    THEOREM.write_text(text)


def main():
    update_current()
    update_root_readme()
    update_alt_readme()
    update_full_frontier_record()
    update_theorem_assumption()
    print("HALL_RESEARCH_STATUS_SYNC_OK")
    print("canonical_frontier_unchanged=1971/3607")
    print("whole_type_hall_package=" + THEOREM_LINK)


if __name__ == "__main__":
    main()
