#!/usr/bin/env python3
"""Synchronise reviewer/restart surfaces after the audited pair-capacity promotion.

This script is intentionally assertive: it patches only known pre-promotion
text/marker blocks and aborts if those anchors are absent. It does not alter
proof artifacts or the canonical ledger.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "README.md"
STATE = ROOT / "CURRENT_STATE.md"
ALT = ROOT / "project/research/general_n/2026-09-13-alternative-attacks-v1/README.md"


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{label}: expected one exact anchor, found {n}")
    return text.replace(old, new, 1)


def replace_marker(text, start, end, body, label):
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    new = start + "\n" + body.rstrip() + "\n" + end
    text2, n = pat.subn(new, text, count=1)
    if n != 1:
        raise SystemExit(f"{label}: marker block not found uniquely")
    return text2


def patch_main(text):
    text = replace_once(
        text,
        "**Updated 13 September 2026 through the canonical N34 whole-state ledger: 16 quantified whole-state closures, frontier 1,010/4,568. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.**",
        "**Updated 13 September 2026 through the audited potential-pair frontier promotion: 961 quantified whole-state closures, frontier 1,955/3,623. Independent mathematical review, novelty assessment and genuinely independent third-party computational reproduction remain OPEN.**",
        "main headline",
    )
    text = replace_once(
        text,
        "| Generalisation frontier | **1,010 exclusions / 4,568 survivors** from the canonical N34 whole-state ledger; these are scalar states in a frozen experiment, not surviving graphs |",
        "| Generalisation frontier | **1,955 exclusions / 3,623 survivors** from the canonical quantified whole-state ledger; `3,545` are N34 equality-derived and `78` are N35 `m=306`-derived; these are scalar states in a frozen experiment, not surviving graphs |",
        "main headline table",
    )

    ledger_body = r"""### Canonical N34 whole-state ledger

The canonical [`WHOLE_STATE_LEDGER.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/WHOLE_STATE_LEDGER.tsv) now records **961 distinct quantified whole-state exclusions**. Eighteen were established on the earlier individual/family lines; a further **943 N34-derived scalar states** are excluded by the audited potential-pair capacity family.

The large promotion is documented in [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md), with the exact promoted state certificate in [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv). Two structurally different full-frontier implementations agree exactly on the 943-state excluded set and, for every excluded state, on exhaustive profile counts and best capacity deficits.

The durability checker [`tools/check_n34_whole_state_ledger.py`](tools/check_n34_whole_state_ledger.py) protects the 18 earlier closures plus the hash-pinned 943-state family and verifies their ledger provenance.

The current frozen frontier is therefore

```text
1,955 exclusions / 3,623 survivors,
3,545 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

Survival in this catalogue is not graph feasibility. The unrestricted Murty–Simon conjecture remains unproved by this project."""
    text = replace_marker(
        text,
        "<!-- N34-WHOLE-STATE-LEDGER:START -->",
        "<!-- N34-WHOLE-STATE-LEDGER:END -->",
        ledger_body,
        "main ledger marker",
    )

    text = text.replace("## What the 16 closures suggest", "## What the quantified closures suggest")
    text = text.replace(
        "| [Alternative attacks](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) | Selection-free/excess/Hall/orientation lemmas and 16 quantified whole-state closures | Current primary programme; next task is generalising orientation/flow capacity and rescanning the remaining frontier |",
        "| [Alternative attacks](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) | Selection-free/excess/Hall/orientation/potential-pair lemmas and 961 quantified whole-state closures | Current primary programme; potential-pair capacity removed 943 further N34-derived scalar states; symbolic generalisation and the 3,623-state residual frontier are now primary |",
    )
    text = text.replace(
        "The next target set should be chosen by applying the new orientation-capacity and joint-Hall machinery to the **remaining 4,568 frozen scalar survivors**, rather than by continuing an obsolete local ranking.",
        "The older local target lists are obsolete. The current residual experiment contains **3,623 frozen scalar survivors**; the next targets should be chosen by combining potential-pair capacity, orientation Hall/flow, selected-incidence Hall and excess-budget machinery on that reduced frontier.",
    )

    priorities = r"""## Current research priorities

1. **Generalise the potential-pair obstruction symbolically.** The strongest compact new consequence is the low-`c`/high-`q` product bound `Q + ell_r u_r <= binom(b,2)` for every threshold `r`. Optimise the `(q,c)` distributions under this family, `q+rho<=a`, demand forcing and incoming caps, seeking an all-order theorem rather than further finite accumulation.
2. **Rescan the remaining 3,623 scalar survivors with the stronger relational systems.** Apply exact pair-choice Hall, target-capacity Hall, selected-incidence Hall and the excess-budget min-cost coupling only after the cheap potential-pair screen; use the new survivor structure to rank genuinely hard branches.
3. **Understand the 78 N35-derived survivors separately.** The potential-pair family closes 943 N34-derived states but none of the 78 N35-derived states, so this residual class is a valuable diagnostic of what the current theorem still misses.
4. **Strengthen independent audit/reproduction.** Prioritise external checking of the canonical bridge, directed compatibility, total-excess source cap and potential-pair theorem. The two internal implementations and green CI are strong replay evidence, not external acceptance.
5. **Continue genuinely independent routes.** Preserve and develop maximum-cut/stability, selection-free and other structurally different approaches; use failures to test whether the orientation/pair picture is genuinely central rather than merely effective on the frozen catalogue.
6. **Return to exact shared-residual/destination geometry only after quantified pruning.** The cheaper reusable theory should first identify where pair capacity and Hall/flow stop; bespoke geometry belongs on that residual set, not on already excluded states.
"""
    pat = re.compile(r"## Current research priorities\n.*?(?=\n## Trust boundary)", re.S)
    text, n = pat.subn(priorities.rstrip(), text, count=1)
    if n != 1:
        raise SystemExit("main priorities block not found")

    old_latest = "For restart-level detail, read [`CURRENT_STATE.md`](CURRENT_STATE.md). For the latest quantified advance, read [`ORIENTATION_TARGET_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_TARGET_CAPACITY.md), [`STATE_77_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_77_WHOLE_STATE.md), [`STATE_60_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_60_WHOLE_STATE.md), and [`verify_e0_orientation_capacity.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/verify_e0_orientation_capacity.py)."
    new_latest = "For restart-level detail, read [`CURRENT_STATE.md`](CURRENT_STATE.md). For the latest quantified advance, read [`POTENTIAL_PAIR_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POTENTIAL_PAIR_CAPACITY.md), [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md), [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md), and [`ORIENTATION_FLOW_HALL.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_FLOW_HALL.md)."
    text = replace_once(text, old_latest, new_latest, "main latest links")
    return text


def patch_state(text):
    text = replace_once(
        text,
        "**Research state reconciled:** 13 September 2026 through the canonical N34 whole-state ledger: **16 quantified closures** (`227, 279, 588, 526, 382, 519, 230, 282, 385, 153, 122, 283, 154, 231, 77, 60`), frontier **1,010/4,568**. External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.",
        "**Research state reconciled:** 13 September 2026 through the audited potential-pair frontier promotion: **961 quantified whole-state closures**, frontier **1,955/3,623** (`3,545` N34-derived survivors plus `78` N35-derived survivors). Eighteen closures predate the large family; **943 further N34-derived scalar states** are protected by the cross-implementation potential-pair audit. External mathematical review, novelty assessment and genuinely independent third-party computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.",
        "state headline",
    )
    text = replace_once(
        text,
        "**Durability guard:** [`tools/check_n34_whole_state_ledger.py`](tools/check_n34_whole_state_ledger.py) pins all 16 current closures in `KNOWN_MINIMUM`, including states `77` and `60`. New closures may be added, but a later ledger/README rewrite must not silently remove any preserved closure.",
        "**Durability guard:** [`tools/check_n34_whole_state_ledger.py`](tools/check_n34_whole_state_ledger.py) protects the 18 earlier closures plus the hash-pinned **943-state** [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv) family, checks ledger provenance, and currently verifies `961` ledger states. New closures may be added, but a later ledger/README rewrite must not silently remove any preserved closure.",
        "state durability",
    )

    orientation_bullet = "- orientation target-capacity lemma for selected missing-B-edge orientations: if an edge is oriented `u->w`, then `q_u-1<=q_w+rho_w`; consequently, for every integer `k`, `sum_{w:q_w+rho_w<=k} p_w <= sum_{u:q_u<=k+1} q_u`. The exact E=0 replay closes states 77 and 60 with a minimum six-incidence deficit."
    expanded = orientation_bullet + "\n- exact directed compatibility and Hall-flow projection: an orientation `u->w` requires `q_u<=q_w+rho_w+1` and `q_w<=q_u+rho_u`; the resulting source-target relation is genuinely two-dimensional rather than Ferrers in general.\n- total-excess source cap: in all-positive-demand branches, `p_u<=rho_u+floor(E/q_u)-1` for every active source, with an explicit zero-demand correction in the general statement.\n- potential-pair capacity theorem: the actual missing graph `J` is a subgraph of a scalar potential graph `K_D`, giving `p_u+q_u<=d_KD(u)`; two structurally different full-frontier implementations use this to close 943 further N34-derived scalar states.\n- low-`c`/high-`q` cross obstruction: for every integer `r`, with `ell_r=#{w:q_w+rho_w<=r}` and `u_r=#{u:q_u>=r+2}`, every legal branch satisfies `Q+ell_r*u_r<=binom(b,2)`."
    text = replace_once(text, orientation_bullet, expanded, "state general-theory bullets")

    latest = r"""## Latest large frontier advance: potential-pair capacity

The orientation work sharpened from a one-sided target cut to the exact directed compatibility condition

```text
D(u,w) iff u!=w,
              q_u<=q_w+rho_w+1,
              q_w<=q_u+rho_u.
```

An unordered pair can be missing only if one of its two directions is compatible. This defines the potential-pair graph `K_D`; the actual missing graph satisfies

```text
J subseteq K_D,
q_u+p_u=d_J(u)<=d_KD(u).
```

The resulting pointwise cap, combined with canonical incoming/simple bounds and the total-excess source cap, was scanned over a deliberately **enlarged** q-universe: only `q_u<=min(a-rho_u,#{i:s_i<=rho_u})` and `sum q=S+E` were assumed, so no selected-incidence Hall feasibility was needed for the exclusions.

Two structurally different full-frontier implementations agree exactly on **943 further N34-derived whole-state exclusions**. The first constructs directed pairs from expanded source vectors; the second enumerates `(rho,q)` type multiplicities and computes `d_KD` from the closed-form counting theorem. On every excluded state they agree exactly on exhaustive profile count, pre-pair pass count and best final deficit. See [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md).

The promoted frozen frontier is

```text
1,955 exclusions / 3,623 survivors,
3,545 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

The theorem itself is separately replayed in [`verify_potential_pair_capacity.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/verify_potential_pair_capacity.py), which checked 122,608 small `(q,rho)` profiles, 2,259,488 ordered pairs and 588,416 degree identities. These are internal replay checks, not external acceptance.

A compact symbolic consequence is the threshold product obstruction

```text
Q + ell_r*u_r <= binom(b,2)
```

for every integer `r`, where `ell_r` counts low-`c` vertices and `u_r` counts high-`q` sources. This is now the highest-leverage all-order route.
"""
    anchor = "## Current whole-state generalisation record"
    if "## Latest large frontier advance: potential-pair capacity" not in text:
        if anchor not in text:
            raise SystemExit("state current-record anchor absent")
        text = text.replace(anchor, latest.rstrip() + "\n\n" + anchor, 1)

    text = replace_once(
        text,
        "```text\n1,010 exclusions / 4,568 survivors.\n```\n\nBreakdown:\n\n```text\n4,490 N34 equality-derived survivors,\n78 N35 m=306-derived survivors.\n```",
        "```text\n1,955 exclusions / 3,623 survivors.\n```\n\nBreakdown:\n\n```text\n3,545 N34 equality-derived survivors,\n78 N35 m=306-derived survivors.\n```",
        "state current frontier",
    )
    text = text.replace("## General-theory lesson from the 16 closures", "## General-theory lesson from the quantified closures")
    text = text.replace(
        "New targets should be chosen only after rescanning the remaining 4,568-state frontier with the orientation-capacity and joint-Hall machinery.",
        "The old target ranking is superseded. The remaining **3,623-state** frontier should now be attacked with pair-choice/target Hall, selected-incidence Hall and excess-budget coupling after the cheap potential-pair screen.",
    )

    obligations_old = "2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selection-free candidate capacity, selected excess, threshold family, refined baseline/order-statistic lemma, zero-excess endpoint-order lemma and orientation target-capacity lemma."
    obligations_new = "2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selected excess, total-excess source capacity, exact directed compatibility, potential-pair capacity, the low-c/high-q threshold product obstruction and the orientation Hall/flow projections."
    text = replace_once(text, obligations_old, obligations_new, "state obligations")

    priorities = r"""## Current research priorities

### P1. Convert potential-pair capacity into an all-order scalar theorem

Start from [`POTENTIAL_PAIR_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POTENTIAL_PAIR_CAPACITY.md) and the threshold consequence [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md):

```text
Q + ell_r*u_r <= binom(b,2)
```

for every integer `r`. Optimise this together with `q+rho<=a`, demand forcing and incoming/total-excess caps. The goal is a parameterised theorem, not further finite accumulation.

### P2. Rescan the residual 3,623-state frontier with stronger relational machinery

Potential-pair capacity has already removed 943 current states. On the survivors, escalate in cost order: pair-choice Hall, target-capacity Hall, selected-incidence Hall, then the weighted excess-budget min-cost coupling. Preserve exact residual structure and use it to select the next theorem target.

### P3. Diagnose the 78 N35-derived survivors

The 943-state family contains no N35-derived closure. Compare their `(q,c,rho,s)` structure with the eliminated N34 population to identify the structural feature missing from the present potential-pair theorem.

### P4. Strengthen independent audit and reproduction

Prioritise external checking of the canonical bridge, directed compatibility, total-excess source cap and potential-pair theorem. The two internal frontier implementations agree exactly on all 943 exclusions, but same-assistant independent code remains internal replay evidence.

### P5. Continue independent routes and preservation

Continue maximum-cut/stability, selection-free and other genuinely different approaches. Preserve failures, counterexamples, solver timeouts and corrected interpretations; never infer proof from timeout or numerical infeasibility alone.
"""
    pat = re.compile(r"## Current research priorities\n.*?(?=\n## Research/preservation rules)", re.S)
    text, n = pat.subn(priorities.rstrip(), text, count=1)
    if n != 1:
        raise SystemExit("state priorities block absent")

    text = text.replace(
        "- the canonical whole-state ledger guard must retain every independently committed closure in its `KNOWN_MINIMUM` set; states `77` and `60` are explicitly protected alongside the earlier 14 closures;",
        "- the canonical whole-state ledger guard must retain every independently committed closure; it explicitly protects the 18 earlier closures and the hash-pinned 943-state potential-pair family with provenance checks;",
    )
    text = text.replace(
        "4. inspect `REFINED_BASELINE3_LEMMA.md`, `ZERO_EXCESS_ENDPOINT_ORDER.md`, `ENDPOINT_CLASS_PACKING.md`, [`ORIENTATION_TARGET_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_TARGET_CAPACITY.md), `make_class_packing_scanner.py`, [`verify_e0_orientation_capacity.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/verify_e0_orientation_capacity.py) and the current residual result tables;\n5. continue from P1/P2 unless later preserved work changes priority;",
        "4. inspect [`POTENTIAL_PAIR_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POTENTIAL_PAIR_CAPACITY.md), [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md), [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md), [`ORIENTATION_FLOW_HALL.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_FLOW_HALL.md), and the current residual result tables;\n5. continue from P1/P2 unless later preserved work changes priority;",
    )
    return text


def patch_alt(text):
    text = replace_once(
        text,
        "The quantified line now has **16 whole-state N34 exclusions**:\n\n```text\n227, 279, 588, 526, 382, 519, 230, 282, 385, 153, 122, 283, 154, 231, 77, 60.\n```",
        "The canonical ledger now has **961 quantified N34-derived whole-state exclusions**: 18 earlier individually/family audited closures plus a cross-implementation-audited **943-state potential-pair capacity family**. The exact 943 IDs are preserved in [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv), with audit provenance in [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](PAIR_CAPACITY_FRONTIER_AUDIT.md).",
        "alt opening closures",
    )
    text = replace_once(
        text,
        "```text\n1,010 exclusions / 4,568 survivors,\n```\n\nsplit as\n\n```text\n4,490 N34 equality-derived survivors,\n78 N35 m=306-derived survivors.\n```",
        "```text\n1,955 exclusions / 3,623 survivors,\n```\n\nsplit as\n\n```text\n3,545 N34 equality-derived survivors,\n78 N35 m=306-derived survivors.\n```",
        "alt frontier",
    )
    text = replace_once(
        text,
        "The durability checker [`../../../../tools/check_n34_whole_state_ledger.py`](../../../../tools/check_n34_whole_state_ledger.py) pins all 16 current closures in `KNOWN_MINIMUM`, explicitly including states `77` and `60`. New closures may be added, but an accidental later ledger/README rewrite must not silently remove a preserved closure.",
        "The durability checker [`../../../../tools/check_n34_whole_state_ledger.py`](../../../../tools/check_n34_whole_state_ledger.py) protects the 18 earlier closures plus the hash-pinned 943-state potential-pair family and verifies the ledger provenance of every promoted family member. New closures may be added, but an accidental later ledger/README rewrite must not silently remove a preserved closure.",
        "alt durability",
    )
    block = r"""### Canonical closure ledger

The canonical [`WHOLE_STATE_LEDGER.tsv`](WHOLE_STATE_LEDGER.tsv) contains **961 quantified whole-state exclusions**. The large current family is documented in [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](PAIR_CAPACITY_FRONTIER_AUDIT.md), with exact IDs in [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv).

Two full-frontier implementations—expanded source vectors with pairwise directed compatibility, and independent `(rho,q)` type-count enumeration using the closed-form potential degree—agree exactly on the 943 promoted exclusions and their exhaustive certificate statistics.

Canonical frontier: **1,955 exclusions / 3,623 survivors** (`3,545` N34-derived plus `78` N35-derived).

The durability checker [`../../../../tools/check_n34_whole_state_ledger.py`](../../../../tools/check_n34_whole_state_ledger.py) hash-pins the 943-state certificate and checks ledger provenance."""
    text = replace_marker(
        text,
        "<!-- CANONICAL-WHOLE-STATE-LEDGER:START -->",
        "<!-- CANONICAL-WHOLE-STATE-LEDGER:END -->",
        block,
        "alt ledger marker",
    )

    old7 = "7. **Orientation target capacity** — [`ORIENTATION_TARGET_CAPACITY.md`](ORIENTATION_TARGET_CAPACITY.md) links the selected-label constraints back to the actual missing-edge orientation. For every oriented missing pair `u->w`, `q_u-1<=q_w+rho_w`; hence low-cross-degree targets have a Hall-type incoming-capacity restriction."
    new7 = old7 + "\n8. **Exact orientation Hall flow** — [`ORIENTATION_FLOW_HALL.md`](ORIENTATION_FLOW_HALL.md) keeps the companion endpoint inequality, proves the exact directed compatibility relation and records why the full relation is two-dimensional rather than Ferrers in general.\n9. **Total-excess source capacity** — [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md) interpolates the exact-demand incoming cap across every total-excess layer.\n10. **Potential-pair capacity** — [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md) forgets the orientation but retains which unordered pairs could possibly be missing, giving `p_u+q_u<=d_KD(u)`; this is the mechanism behind the audited 943-state frontier family.\n11. **Low-c/high-q threshold obstruction** — [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md) extracts the compact all-order candidate inequality `Q+ell_r*u_r<=binom(b,2)` for every threshold `r`."
    text = replace_once(text, old7, new7, "alt hierarchy")

    text = text.replace(
        " -> missing-edge orientation / flow capacity.\n```",
        " -> missing-edge orientation / flow capacity\n -> potential-pair capacity\n -> low-c/high-q threshold obstruction.\n```",
    )
    return text


def main():
    files = [(MAIN, patch_main), (STATE, patch_state), (ALT, patch_alt)]
    for path, fn in files:
        before = path.read_text()
        after = fn(before)
        if after == before:
            raise SystemExit(f"{path}: patch made no change")
        path.write_text(after)
        print("UPDATED", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
