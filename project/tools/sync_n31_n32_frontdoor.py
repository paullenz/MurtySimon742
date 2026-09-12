#!/usr/bin/env python3
"""Idempotently sync N31/N32 status into the repository front-door files.

This script is intentionally narrow: it patches README.md,
START_HERE_FOR_REVIEWERS.md and releases/REVIEW_READY_INDEX.md only. It asserts
stable markers before insertion and refuses to guess if those markers disappear.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected marker exactly once, found {n}: {old!r}')
    return text.replace(old, new, 1)


def sync_root():
    p = ROOT / 'README.md'
    t = p.read_text()
    t = t.replace('**Updated 11 September 2026.', '**Updated 12 September 2026.', 1)

    n30 = "| `n=30` | Complete candidate: `e(G) <= 225`, equality exactly `K(15,15)`; **reviewer-v3 package** with self-contained hand lemmas and every proof-critical integer table; Delta>=17 closed by a hand bound, Delta=15 equality proved directly; internal arithmetic REPRODUCED; independent specialist review OPEN |"
    add = n30 + "\n| `n=31` | Complete candidate: `e(G) <= 240`, equality exactly `K(15,16)`; source-first reviewer-v1 package; hand route with thirteen-label equality closure and witness-deficit balanced branch; hostile internal audit found no blocking flaw; external review OPEN |\n| `n=32` | Complete candidate: `e(G) <= 256`, equality exactly `K(16,16)`; **reviewer-v1 source package**; `m>=258` hand-closed, 257-edge branch exact nine-rectangle closure, equality branch has exact finite replay plus one hand tight-threshold contradiction; hostile internal audit found no blocking flaw; external review OPEN |"
    if '| `n=32` |' not in t:
        t = replace_once(t, n30, add, 'README headline table')

    block = """## 12 September fixed-order extension: n=31 and n=32

The fixed-order candidate frontier has been extended beyond n=30.

- **n=31:** candidate `e(G)<=240`, equality exactly `K(15,16)`. Start with [`releases/n31-reviewer-v1/README.md`](releases/n31-reviewer-v1/README.md). The route is predominantly hand/structural and its hostile internal audit found no blocking flaw.
- **n=32:** candidate `e(G)<=256`, equality exactly `K(16,16)`. Start with [`releases/n32-reviewer-v1/README.md`](releases/n32-reviewer-v1/README.md). The difficult `Delta=17` branch combines hand tail lemmas with exact finite replay. At equality, the exact ledger is 1,369 lifted-potential exclusions, 614 full RX/Hall exact Farkas exclusions, 61 strengthened zero-demand exact exclusions, one pre-model arithmetic impossibility and one hand tight-threshold contradiction. No floating-point infeasibility is a proof event.

Both claims remain **candidate mathematics** pending genuinely independent specialist review. The unrestricted Murty-Simon conjecture remains unsolved.

"""
    if '## 12 September fixed-order extension: n=31 and n=32' not in t:
        t = replace_once(t, '## Public-review note\n', block + '## Public-review note\n', 'README public-review marker')
    p.write_text(t)


def sync_start():
    p = ROOT / 'START_HERE_FOR_REVIEWERS.md'
    t = p.read_text()
    t = t.replace('**Updated 11 September 2026.**', '**Updated 12 September 2026.**', 1)

    n30 = '- `n=30`: `e(G) <= 225`, equality only `K(15,15)`.'
    if '- `n=32`:' not in t:
        t = replace_once(
            t, n30,
            n30 + '\n- `n=31`: `e(G) <= 240`, equality only `K(15,16)`;\n- `n=32`: `e(G) <= 256`, equality only `K(16,16)`.',
            'START headline list')

    old = 'The canonical PDF reviewer packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, and **reviewer-v3 at `n=30`**. N29 has no proof-critical computation; N30 combines hand lemmas with explicit finite integer tables.'
    new = 'The canonical reviewer packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, **reviewer-v3 at `n=30`**, and source-first **reviewer-v1 packages at `n=31,32`**. N29 has no proof-critical computation; N30 combines hand lemmas with explicit finite integer tables; N31 is predominantly hand/structural; N32 uses hand reductions plus exact finite replay in the difficult `Delta=17` branch.'
    if old in t:
        t = replace_once(t, old, new, 'START package sentence')

    block = """## n=31 and n=32 fixed-order extensions

### n=31

Candidate `e(G)<=240`, equality exactly `K(15,16)`.

- [`releases/n31-reviewer-v1/README.md`](releases/n31-reviewer-v1/README.md)
- [`project/research/n31/2026-09-11-hand-route-v1/PROOF.md`](project/research/n31/2026-09-11-hand-route-v1/PROOF.md)
- [`project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md`](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md)

### n=32

Candidate `e(G)<=256`, equality exactly `K(16,16)`.

- [`releases/n32-reviewer-v1/README.md`](releases/n32-reviewer-v1/README.md)
- [`project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md`](project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md)
- [`project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md`](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md)
- [`project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md`](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md)

For N32 the highest-value external targets are the shared selected/residual bridge, threshold-capacity equality, endpoint load, the t=1 residual-tail expansion and the strengthened zero-demand model. Exact replay is important implementation evidence but is not a substitute for reviewing those implications.

"""
    if '## n=31 and n=32 fixed-order extensions' not in t:
        t = replace_once(t, '## n=25: the natural fixed-order paper to inspect\n', block + '## n=25: the natural fixed-order paper to inspect\n', 'START n25 marker')

    t = t.replace('n=25,27,28,29,30`', 'n=25,27,28,29,30,31,32`')
    p.write_text(t)


def sync_index():
    p = ROOT / 'releases' / 'REVIEW_READY_INDEX.md'
    t = p.read_text()
    t = t.replace('Updated 11 September 2026.', 'Updated 12 September 2026.', 1)
    t = t.replace(
        'The current fixed-order PDF packages are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, and **reviewer-v3 at `n=30`**. N28 retains its 11 September analytic-hardening annotation. N30 reviewer-v3 contains the complete hand-lemma and finite-table proof, companion and portable ZIP.',
        'The current fixed-order PDF packages are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, and **reviewer-v3 at `n=30`**. Source-first reviewer-v1 packages now cover `n=31,32`. N28 retains its 11 September analytic-hardening annotation. N30 reviewer-v3 contains the complete hand-lemma and finite-table proof, companion and portable ZIP; N31/N32 are currently Markdown/replay packages rather than PDF releases.'
    )
    n30row = '| n30 | `e(G) <= 225, with equality exactly K(15,15)` | [PDF v3](n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) | [PDF v3](n30-reviewer-v3/N30_Verification_Companion_v3.pdf) | **Reviewer-v3 hand lemmas + explicit integer tables**; [package](n30-reviewer-v3/README.md), [ZIP](n30-reviewer-v3/N30_Reviewer_Package_v3.zip), [proof](../project/reviews/n30/2026-09-11-reviewer-v3/PROOF.md); internal arithmetic REPRODUCED; independent review OPEN; [v2 history](n30-reviewer-v2/README.md) |'
    rows = n30row + '\n| n31 | `e(G) <= 240, with equality exactly K(15,16)` | [source package](n31-reviewer-v1/README.md) | [hostile audit](../project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md) | **Reviewer-v1 source-first hand route**; no blocking flaw found internally; independent review OPEN |\n| n32 | `e(G) <= 256, with equality exactly K(16,16)` | [source package](n32-reviewer-v1/README.md) | [exact equality ledger](../project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) | **Reviewer-v1 hand + exact finite replay**; hostile internal audit found no blocking flaw; independent review OPEN |'
    if '| n32 |' not in t:
        t = replace_once(t, n30row, rows, 'review index n30 row')
    t = t.replace('n=25,27,28,29,30 and the retained', 'n=25,27,28,29,30,31,32 and the retained')
    t = t.replace('at n=25,27,28,29,30.', 'at n=25,27,28,29,30,31,32.')
    p.write_text(t)


def main():
    sync_root()
    sync_start()
    sync_index()
    print('PASS: synchronized README.md, START_HERE_FOR_REVIEWERS.md, releases/REVIEW_READY_INDEX.md')


if __name__ == '__main__':
    main()
