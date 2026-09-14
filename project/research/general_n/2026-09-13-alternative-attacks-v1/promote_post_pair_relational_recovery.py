#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = Path(__file__).resolve().parent
CERT = BASE / "POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv"
AUDIT = BASE / "POST_PAIR_RELATIONAL_RECOVERY_AUDIT.json"
LEDGER = BASE / "WHOLE_STATE_LEDGER.tsv"
RECOVERY = BASE / "POST_PAIR_RELATIONAL_RECOVERY.md"
PACKAGE_README = BASE / "README.md"
ROOT_README = ROOT / "README.md"
CURRENT_STATE = ROOT / "CURRENT_STATE.md"

EXPECTED_IDS = [
    961, 1025, 2620, 2706, 2897, 3007, 3139, 3202,
    3302, 3359, 3480, 3599, 4145, 4559, 4654, 4994,
]
EXPECTED_TRIGGER_RUN = 34817529642
EXPECTED_TRIGGER_HEAD = "c2b426da46284617681081797d1c571d23cd531d"
METHOD = "post-pair relational cross-implementation closure"
RECORD = "POST_PAIR_RELATIONAL_RECOVERY.md"


def replace_once_or_done(text, old, new, label):
    if old in text:
        return text.replace(old, new)
    if new in text:
        return text
    raise SystemExit(f"expected documentation text not found for {label}: {old!r}")


def validate_certificate():
    if not CERT.is_file() or not AUDIT.is_file():
        raise SystemExit("missing aggregate relational certificate/audit")
    with CERT.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = [int(r["state_id"]) for r in rows]
    if ids != EXPECTED_IDS:
        raise SystemExit(f"certificate ids mismatch: {ids}")
    for row in rows:
        if row["layer"] != "0" or row["status"] != "RELATIONAL_EXCLUDED" or row["witness_E"] != "-1":
            raise SystemExit(f"invalid excluded row: {row}")
    cert_sha = hashlib.sha256(CERT.read_bytes()).hexdigest()
    audit = json.loads(AUDIT.read_text())
    if audit.get("trigger_run_id") != EXPECTED_TRIGGER_RUN:
        raise SystemExit("unexpected aggregate trigger run")
    if audit.get("trigger_head_sha") != EXPECTED_TRIGGER_HEAD:
        raise SystemExit("unexpected aggregate trigger head")
    if audit.get("state_ids") != EXPECTED_IDS or audit.get("state_count") != len(EXPECTED_IDS):
        raise SystemExit("aggregate state list/count mismatch")
    if audit.get("all_comparisons") != "PASS":
        raise SystemExit("aggregate comparison status is not PASS")
    if audit.get("combined_tsv_sha256") != cert_sha:
        raise SystemExit("aggregate audit does not hash-bind certificate")
    return rows, audit, cert_sha


def update_ledger():
    with LEDGER.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    by_state = {int(r["state"]): r for r in rows}
    already = [state for state in EXPECTED_IDS if state in by_state]
    if already and len(already) != len(EXPECTED_IDS):
        raise SystemExit(f"partial relational promotion already present: {already}")
    if len(already) == len(EXPECTED_IDS):
        for state in EXPECTED_IDS:
            row = by_state[state]
            if row["method"] != METHOD or row["record"] != RECORD:
                raise SystemExit(f"wrong existing relational provenance for {state}: {row}")
        return False
    rows.extend({"state": str(state), "method": METHOD, "record": RECORD} for state in EXPECTED_IDS)
    with LEDGER.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["state", "method", "record"], delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)
    return True


def patch_common_counts(path):
    text = path.read_text()
    pairs = [
        ("961 quantified whole-state closures", "977 quantified whole-state closures", "whole-state count"),
        ("**961 quantified whole-state closures**", "**977 quantified whole-state closures**", "bold whole-state count"),
        ("**961 quantified N34-derived whole-state exclusions**", "**977 quantified N34-derived whole-state exclusions**", "package whole-state count"),
        ("1,955 exclusions / 3,623 survivors", "1,971 exclusions / 3,607 survivors", "frontier count"),
        ("**1,955/3,623**", "**1,971/3,607**", "compact frontier count"),
        ("3,545 N34 equality-derived survivors", "3,529 N34 equality-derived survivors", "N34 survivor count"),
        ("`3,545` are N34 equality-derived", "`3,529` are N34 equality-derived", "inline N34 survivor count"),
    ]
    for old, new, label in pairs:
        if old in text or new in text:
            text = replace_once_or_done(text, old, new, f"{path.name}: {label}")
    path.write_text(text)


def update_recovery_record(audit, cert_sha):
    text = RECOVERY.read_text()
    old = "**At creation of this checkpoint:** 16 recovery candidates identified; **0 newly promoted from this interrupted pilot**. Canonical frontier remains `1,955 exclusions / 3,623 survivors` until the audit gates above are completed and recorded."
    new = (
        "**Promotion complete after cross-implementation audit.** GitHub Actions run "
        f"`{audit['trigger_run_id']}` at head `{audit['trigger_head_sha']}` completed all 16 isolated state jobs. "
        "For every state, the primary vector-enumeration scanner and independent type-count scanner agreed exactly on the full proof-relevant stage counts and final `RELATIONAL_EXCLUDED` status. "
        f"The frozen aggregate certificate has SHA-256 `{cert_sha}`. The 16 states are now promoted to `WHOLE_STATE_LEDGER.tsv`; canonical frontier is `1,971 exclusions / 3,607 survivors` with `977` quantified whole-state closures. External mathematical review and genuinely independent third-party reproduction remain open."
    )
    text = replace_once_or_done(text, old, new, "recovery status")
    RECOVERY.write_text(text)


def append_checkpoint(path, heading, body):
    text = path.read_text()
    if heading in text:
        return
    if not text.endswith("\n"):
        text += "\n"
    text += "\n" + heading + "\n\n" + body.strip() + "\n"
    path.write_text(text)


def update_docs(audit, cert_sha):
    for path in (ROOT_README, CURRENT_STATE, PACKAGE_README):
        patch_common_counts(path)

    root = ROOT_README.read_text()
    root = root.replace(
        "**Updated 13 September 2026 through the audited potential-pair frontier promotion:",
        "**Updated 14 September 2026 through the audited post-pair relational recovery promotion:",
    )
    ROOT_README.write_text(root)

    current = CURRENT_STATE.read_text()
    current = current.replace(
        "**Research state reconciled:** 13 September 2026 through the audited potential-pair frontier promotion:",
        "**Research state reconciled:** 14 September 2026 through the audited post-pair relational recovery promotion:",
    )
    current = current.replace("currently verifies `961` ledger states", "currently verifies `977` ledger states")
    CURRENT_STATE.write_text(current)

    package = PACKAGE_README.read_text()
    package = package.replace("remaining **4,568** frozen scalar survivors", "remaining **3,607** frozen scalar survivors")
    PACKAGE_README.write_text(package)

    update_recovery_record(audit, cert_sha)

    block = f"""
The interrupted 1/32 relational pilot has now been recovered state-by-state. Sixteen N34-derived states passed fresh isolated replay in both the original vector-enumeration implementation and an independent type-count implementation; every proof-relevant stage count agreed exactly. The aggregate certificate is [`POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv), hash `{cert_sha}`, with provenance in [`POST_PAIR_RELATIONAL_RECOVERY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_RECOVERY.md).

Canonical generalisation frontier after promotion:

```text
1,971 exclusions / 3,607 survivors,
3,529 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

The coarse low-residual-reservoir theorem was also scanned over the pre-promotion 3,623-state frontier: it applied to 3,421 states but closed none. That negative result is preserved in `LOW_RESIDUAL_RESERVOIR_RESULT.md` and is evidence that the exact two-dimensional relational structure carries information not captured by the coarse symbolic reservoir count.

**Next priority:** run the checkpointable relational machinery over the remaining ledger-current survivor frontier, preserving per-state artifacts and promoting only cross-checked closures; in parallel, extract symbolic two-dimensional Hall/dominance consequences that could replace finite scanning by a general theorem.
"""
    append_checkpoint(CURRENT_STATE, "## 14 September 2026 — relational recovery promotion", block)

    package_block = f"""
The cancelled pilot has been recovered under the audit protocol in [`POST_PAIR_RELATIONAL_RECOVERY.md`](POST_PAIR_RELATIONAL_RECOVERY.md). Sixteen states are now promoted after exact agreement between the primary scanner and an independent type-count implementation. The frozen aggregate certificate is [`POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv`](POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv), SHA-256 `{cert_sha}`. Canonical frontier is **1,971 exclusions / 3,607 survivors**.

The earlier low-residual-reservoir scan remains a preserved negative result: 3,421 of the then-current 3,623 states were in scope, but it excluded zero whole states. The active route is therefore the stronger relational Hall/min-cost layer, not further tuning of that coarse reservoir bound.
"""
    append_checkpoint(PACKAGE_README, "## Post-pair relational recovery promotion — 14 September 2026", package_block)

    root_block = f"""
Sixteen further N34-derived scalar states have been promoted after a fresh state-by-state post-pair relational replay and exact agreement between two implementations with different q-profile representations and potential-pair calculations. See [`POST_PAIR_RELATIONAL_RECOVERY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_RECOVERY.md). Aggregate certificate SHA-256: `{cert_sha}`. The canonical frozen frontier is now **1,971 exclusions / 3,607 survivors**. These are quantified scalar exclusions inside the generalisation experiment, not an unrestricted proof of Murty-Simon.
"""
    append_checkpoint(ROOT_README, "## 14 September 2026 relational recovery checkpoint", root_block)


def main():
    _, audit, cert_sha = validate_certificate()
    changed = update_ledger()
    update_docs(audit, cert_sha)
    print("POST_PAIR_RELATIONAL_PROMOTION_READY")
    print("ledger_changed", int(changed))
    print("states", len(EXPECTED_IDS))
    print("certificate_sha256", cert_sha)
    print("new_frontier", "1971/3607")


if __name__ == "__main__":
    main()
