#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$HERE/replay-output}"
SHARDS="${N32_SHARDS:-32}"
WORKERS="${N32_WORKERS:-4}"
mkdir -p "$OUT/rx" "$OUT/zero"

CXX="${CXX:-g++}"
"$CXX" -O3 -std=c++17 "$HERE/check_n32_t1_frontier.cpp" -o "$OUT/check_n32_t1_frontier"
"$OUT/check_n32_t1_frontier" --csv "$OUT/N32_T1_FRONTIER.csv"

python3 -I -B "$HERE/n32_t1_lifted_potential_exact.py" \
  --frontier "$OUT/N32_T1_FRONTIER.csv" \
  --survivors "$OUT/N32_T1_SURVIVORS.jsonl" \
  --zero-states "$OUT/N32_T1_ZERO_STATES.jsonl" \
  --output "$OUT/N32_T1_LIFTED_EXACT.json"

# Shards are mathematically independent. Run a bounded number concurrently so
# CI remains practical without changing any model or acceptance criterion.
seq 0 $((SHARDS-1)) | xargs -P "$WORKERS" -I{} \
  python3 -I -B "$HERE/n32_t1_full_rx_exact.py" \
    --survivors "$OUT/N32_T1_SURVIVORS.jsonl" \
    --shard "{}" --shards "$SHARDS" \
    --output "$OUT/rx/shard_{}.json"

seq 0 $((SHARDS-1)) | xargs -P "$WORKERS" -I{} \
  python3 -I -B "$HERE/n32_t1_zero_exact.py" \
    --zero-states "$OUT/N32_T1_ZERO_STATES.jsonl" \
    --shard "{}" --shards "$SHARDS" \
    --output "$OUT/zero/shard_{}.json"

python3 -I -B "$HERE/aggregate_n32_t1_replay.py" \
  --lifted "$OUT/N32_T1_LIFTED_EXACT.json" \
  --rx-glob "$OUT/rx/shard_*.json" \
  --zero-glob "$OUT/zero/shard_*.json" \
  --output "$OUT/N32_T1_AGGREGATE.json"

echo "PASS: N32 t=1 exact replay. See $OUT/N32_T1_AGGREGATE.json"
