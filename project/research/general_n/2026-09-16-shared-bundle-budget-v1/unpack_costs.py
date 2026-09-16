#!/usr/bin/env python3
"""Decode saved costs without solving the capacity problem again."""
import base64
import gzip
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
expected = json.loads((root/'CHECK_RESULTS.json').read_text())['exact_capacity_table']
compressed = base64.b64decode((root/'EXACT_COSTS.bin.gz.b64').read_text().strip(), validate=True)
data = gzip.decompress(compressed)
if len(data) != expected['rows'] or hashlib.sha256(data).hexdigest() != expected['sha256']:
    raise ValueError('Decoded capacity evidence does not match its length and SHA256')
(root/'EXACT_COSTS.bin').write_bytes(data)
print(f"Verified {len(data)} archived costs; no capacities recomputed.")
