#!/usr/bin/env python3
from pathlib import Path
import re


def replace_section(text: str, start: str, end: str, new: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + new.rstrip() + "\n\n" + text[j:]


# Top-level README.
p = Path("README.md")
s = p.read_text()
s = re.sub(
    r"^\| `n=29` \|.*$",
    "| `n=29` | Complete candidate: `e(G) <= 210`, equality exactly `K(14,15)`; **reviewer-v4 package**; Delta=16 now closed by a hand threshold-tail proof with no proof-critical computation; historical minimal-kernel/Farkas replay retained as corroboration; external review open |",
    s,
    flags=re.M,
)
s = s.replace(
    "The current reviewer-facing PDF packages are Fan-free v2 at `n=25,27,28,30` and reviewer-v3 at `n=29`.",
    "The current reviewer-facing PDF packages are Fan-free v2 at `n=25,27,28,30` and reviewer-v4 at `n=29`.",
)
s = s.replace(
    "[reviewer-v3 proof](project/reviews/n29/2026-09-11-reviewer-v3/PROOF.md)",
    "[reviewer-v4 proof](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md)",
)
s = s.replace(
    "[reviewer-v3 release package](releases/n29-reviewer-v3/README.md)",
    "[reviewer-v4 release package](releases/n29-reviewer-v4/README.md)",
)
marker = "A separate proof-text audit also found a **non-blocking sign/order typo** in an intermediate explanatory sentence of the expanded threshold-capacity lemma. The corrected sign is exactly the direction needed to prove the already-used final inequality, so no numerical result or candidate status changed. The historical lemma records the correction explicitly; reviewer-v3 rewrites the proof self-contained.\n"
note = "\nLater on 11 September, the threshold-capacity family was summed over residual-degree tails to obtain a stronger demand-only inequality. A new hand clipping argument proves `Q(s)<=18`, while the bridge gives `Q(s)>=16+2t` for `Delta=16`, hence `t<=1`. Therefore the entire `n=29, Delta=16, m>=210` branch is now excluded without proof-critical computation. Reviewer-v4 is the current review surface; reviewer-v3 and its corrected minimal-kernel/Farkas route remain frozen as independent corroboration and audit history.\n"
if note.strip() not in s and marker in s:
    s = s.replace(marker, marker + note)

n29 = r'''### n=29 — complete candidate

**Candidate:**

```text
e(G) <= 210 = floor(29^2/4),
with equality exactly K(14,15).
```

[**Current reviewer-v4 package**](releases/n29-reviewer-v4/README.md) · [reviewer-v4 manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) · [reviewer-v4 verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf) · [canonical reviewer-v4 proof](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md) · [threshold-tail hand proof](project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md) · [frozen self-contained bridge](project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md) · [historical reviewer-v3 package](releases/n29-reviewer-v3/README.md).

The proof does **not** depend on Fan's density theorem or on the active general-N/RX-Hall research. `Delta=15` is handled by a witness-deficit count, which also forces `K(14,15)` at 210. `Delta=17` is excluded by a short pointwise charging bound, `Delta=18..27` by the residual h-index inequality, and a universal vertex gives a star.

The former difficult `Delta=16` branch is now hand-reduced completely. With `t=m-208`, the bridge gives residual activity, `S>=r+2t`, selected-incidence forcing and threshold capacity. Summing residual-degree tails gives a demand-only lower bound `Q(s)>=16+2t`. A hand monotone-clipping argument proves `Q(s)<=18`, so `t<=1`. Therefore **every `Delta=16` graph with `m>=210` is impossible**.

Accordingly, the historical demand enumeration, residual-row scan, Hall pruning, corrected cumulative-threshold/source-q-flow LP and exact Farkas certificates are no longer logical dependencies of the N29 theorem proof. The corrected minimal kernel remains preserved as independent corroboration: at 211 edges it rejected all 126 residual rows, and at 210 edges all 1,467 rows, by exact integer Farkas verification. The earlier v1 grouped-model normalization bug and its correction remain public audit history.

The hand tail lemma has two independent exact regressions: a small local-obligation checker and a full 1,352,078-demand-multiset audit; both pass, but neither is a proof premise. The proof is therefore logically computation-free at N29 while retaining substantial computational cross-checks.

**Status: complete candidate; independent mathematical review OPEN.**'''
s = replace_section(s, "### n=29 — complete candidate", "### n=30 — complete candidate", n29)
p.write_text(s)


# Reviewer entry point.
p = Path("START_HERE_FOR_REVIEWERS.md")
s = p.read_text()
s = s.replace(
    "The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28,30` and **reviewer-v3 at `n=29`**, hardened after the blind external-assistant red-team.",
    "The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28,30` and **reviewer-v4 at `n=29`**, with the entire dense `Delta=16` branch now excluded by a hand threshold-tail argument.",
)
s = s.replace(
    "- `n=29, Delta=16`: `m=215` is a hand threshold contradiction and every `m>=216` is a one-line hand exclusion;",
    "- `n=29, Delta=16`: the later reviewer-v4 threshold-tail proof is stronger and excludes **every `m>=210` by hand**; the earlier pointwise caps remain historical corroboration;",
)
sec = r'''## Recommended bridge audit: n=29

The n=29 candidate is now an especially clean place to audit the universal graph-to-demand machinery because **no finite computation is logically required by reviewer-v4**.

**Current reviewer-v4 package:**

- [`releases/n29-reviewer-v4/README.md`](releases/n29-reviewer-v4/README.md)
- [`releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf`](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf)
- [`releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf`](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf)

**Canonical sources:**

- [`project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md`](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md)
- [`project/reviews/n29/2026-09-11-reviewer-v4/VERIFICATION_COMPANION.md`](project/reviews/n29/2026-09-11-reviewer-v4/VERIFICATION_COMPANION.md)
- [`project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md`](project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md)
- [`project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`](project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md) — frozen self-contained bridge, appended to the v4 PDF.

For `Delta=16`, reviewer-v4 uses only the exact ledger/demand inequality, residual activity, selected-incidence forcing, selected-source capacity and threshold capacity. These give `Q(s)>=16+2t`; the hand tail-deficit argument gives `Q(s)<=18`, hence `t<=1` and excludes every `m>=210` in this degree branch.

The corrected reviewer-v3 minimal kernel remains valuable independent evidence, but is no longer proof-critical. Its exact replays reject 126/126 rows at `m=211` and 1,467/1,467 rows at `m=210`. The old v1 grouped-model normalization bug remains quarantined and documented.

The highest-value review is now the **universal bridge + threshold-capacity lemma + hand clipping argument**, followed by the short `Delta=15`, `Delta=17` and residual h-index branches. A rerun of the late LP/Farkas stack is optional corroboration, not a prerequisite to assess v4.
'''
s = replace_section(s, "## Recommended bridge audit: n=29", "## n=30 complete candidate", sec)
p.write_text(s)


# Review-ready index.
p = Path("releases/REVIEW_READY_INDEX.md")
s = p.read_text()
s = s.replace(
    "The current fixed-order PDF packages are Fan-free reviewer-v2 at `n=25,27,28,30` and **reviewer-v3 at `n=29`**.",
    "The current fixed-order PDF packages are Fan-free reviewer-v2 at `n=25,27,28,30` and **reviewer-v4 at `n=29`**.",
)
s = re.sub(
    r"^\| n29 \|.*$",
    "| n29 | `e(G) <= 210, with equality exactly K(14,15)` | [PDF v4](n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) | [PDF v4](n29-reviewer-v4/N29_Verification_Companion_v4.pdf) | **Reviewer-v4 hand-reduced** — [package](n29-reviewer-v4/README.md), [proof source](../project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md), [threshold-tail lemma](../project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md), [frozen bridge](../project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md); no proof-critical N29 computation; independent review OPEN; [v3 history](n29-reviewer-v3/README.md) |",
    s,
    flags=re.M,
)
s = s.replace(
    "The current PDF packages are reviewer-v2 at n=25,27,28,30 and reviewer-v3 at n=29.",
    "The current PDF packages are reviewer-v2 at n=25,27,28,30 and reviewer-v4 at n=29.",
)
p.write_text(s)
