#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
MODE="${1:---fast}"
echo "Erdos #742 n=25 reproducibility release v1"
python3 scripts/verify_artifacts.py
python3 scripts/verify_zip_integrity.py
python3 scripts/verify_ledger.py
python3 scripts/run_k2_fast.py
python3 scripts/run_k4_fast.py
python3 scripts/verify_k2_job_manifest.py
if [[ "$MODE" == "--full" ]]; then
  python3 scripts/verify_external.py
  python3 scripts/check_full_dependencies.py
  TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
  unzip -q external/delta14_full_checkpoint_2026-09-06.zip -d "$TMP/full"
  TOP="$(find "$TMP/full" -mindepth 1 -maxdepth 1 -type d | head -1)"
  if [[ -z "$TOP" ]]; then TOP="$TMP/full"; fi
  echo "Running checkpoint ledger/catalogue audits from: $TOP"
  (cd "$TOP" && python3 audit_delta14_ledgers.py)
  (cd "$TOP" && python3 audit_delta14_k5_catalogues.py)
  echo "Full proof replay is intentionally a separate explicit command because it can be long. See THIRD_PARTY_AUDIT.md."
fi
echo "REPRODUCIBILITY CHECKS PASS ($MODE)"
