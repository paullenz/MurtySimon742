#!/usr/bin/env python3
"""Decode stored diagnostic results without recomputing any decisions."""
import base64, gzip, hashlib
from pathlib import Path
p = Path(__file__).resolve().parent
raw = gzip.decompress(base64.b64decode((p/'CHECK_RESULTS.json.gz.b64').read_bytes(), validate=False))
expected = '02d8af63c61dc78c337d564254e998d5572dafb9ba4746080abc5d4f5e2f419e'
if hashlib.sha256(raw).hexdigest() != expected:
    raise SystemExit('Stored result digest mismatch')
(p/'CHECK_RESULTS.json').write_bytes(raw)
print('Exact stored results decoded and digest checked:', expected)
