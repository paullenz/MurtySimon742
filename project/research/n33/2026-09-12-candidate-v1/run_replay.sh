#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP="${TMPDIR:-/tmp}/n33_t2_frontier_check.$$"
trap 'rm -f "$TMP"' EXIT

g++ -O3 -std=c++17 "$HERE/check_n33_t2_frontier.cpp" -o "$TMP"
"$TMP"
python3 "$HERE/n33_t2_shifted_potential_exact.py"
